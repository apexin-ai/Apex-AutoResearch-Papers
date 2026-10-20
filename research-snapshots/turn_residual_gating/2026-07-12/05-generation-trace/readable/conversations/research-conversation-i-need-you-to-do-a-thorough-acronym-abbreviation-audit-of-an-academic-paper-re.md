# Research conversation: I need you to do a thorough acronym/abbreviation audit of an academic paper. Read ALL the following LaTeX files in this 

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a56f1deb740d009c5.jsonl`
- **Structured JSON:** [`b37ee5c98fa0468a6dde.json`](../../sessions/b3/b37ee5c98fa0468a6dde.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

33 recorded events

### User

_source line 1 · 2026-05-24T18:24:48.289Z_

I need you to do a thorough acronym/abbreviation audit of an academic paper. Read ALL the following LaTeX files in this order and track every acronym/abbreviation you find:

1. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex
3. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex
4. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex
5. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex
6. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex
7. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex
8. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex
9. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex

For EACH acronym/abbreviation found (including method names, dataset names, metric names, model names, domain terms), report:
- The acronym
- Whether it's defined with full form on FIRST use (and where that first use is)
- If it appears in the Abstract, whether it's also defined IN the Abstract

Categories to check:
- Method/algorithm names (e.g., TG, UG, PCGrad, SS, NTP, GAR, LoRA, etc.)
- Dataset names (e.g., MMLU, UltraChat)
- Metric names (e.g., GAR, PPL, MSE, BLEU, F1)
- Model architecture terms (e.g., LLM, MHA, GQA, RoPE, FFN)
- Domain terms (e.g., TF, AR, SFT, RLHF, DPO, PEFT, EB)
- Any other abbreviations

Output a structured report with:
1. A table of ALL acronyms found, their full form (if given), location of first use, and status (OK / NEEDS FIX)
2. A list of specific fixes needed, with the exact file, the current text, and what it should be changed to

Be thorough — read every file completely. This is for EMNLP 2026 submission due tomorrow.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a3e6062b-fe39-400b-a5a8-e5805ce60227",
  "agentId": "a56f1deb740d009c5",
  "type": "user",
  "uuid": "b5ecc21f-86f8-4fc2-9d75-184d34cd5258",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-24T18:24:48.293Z_

```json
{
  "parentUuid": "b5ecc21f-86f8-4fc2-9d75-184d34cd5258",
  "isSidechain": true,
  "agentId": "a56f1deb740d009c5",
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
  "uuid": "417c7814-2d0c-495f-b158-47b9a2bf74dc",
  "timestamp": "2026-05-24T18:24:48.293Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

---

### Assistant

_source line 3 · 2026-05-24T18:24:52.828Z_



I'll read all the files systematically to audit every acronym/abbreviation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "417c7814-2d0c-495f-b158-47b9a2bf74dc",
  "isSidechain": true,
  "agentId": "a56f1deb740d009c5",
  "requestId": "req_011CbMryVUbGzqBeAHCEDWk8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e10b8111-85bf-4448-aefb-1f95986ba263",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrW94Yqtrovh6eczfZWsn8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34765,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34765,
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

_source line 4 · 2026-05-24T18:24:53.040Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FPp935BnAJBzMkWX5nqWQH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e10b8111-85bf-4448-aefb-1f95986ba263",
  "isSidechain": true,
  "agentId": "a56f1deb740d009c5",
  "requestId": "req_011CbMryVUbGzqBeAHCEDWk8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b531a07-a2f3-49ff-9c38-04e56ace0cdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrW94Yqtrovh6eczfZWsn8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34765,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34765,
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

_source line 5 · 2026-05-24T18:24:53.057Z_

<details><summary>↩ Tool result · `toolu_01FPp935BnAJBzMkWX5nqWQH`</summary>

```text
1	\begin{abstract}
2	Multi-turn dialogue requires language models to maintain attention to system-prompt goals across conversation turns, yet goal attention decays systematically (by up to 70.8\%) even when residual representations retain goal content.
3	
4	Existing remedies (inference-time attention separation, turn-agnostic gating, auxiliary attention losses) either bypass training or assume that teacher-forced optimization transfers to autoregressive generation. We show it does not: attention losses optimized to GAR\,=\,0.50 under teacher forcing collapse 8--17$\times$ on Qwen-2.5-7B and 27$\times$ on Llama-3.1-8B, degrading instruction compliance by up to 24 percentage points.
5	
6	A five-way controlled comparison isolates the cause. PCGrad eliminates gradient conflict yet \emph{worsens} AR GAR ($p$\,=\,0.002), ruling out the most intuitive explanation by \emph{modus tollens}. The root cause is exposure bias: auxiliary attention objectives have no autoregressive training signal.
7	
8	Two interventions breach the barrier: inference-time attention steering ($\beta$\,=\,5) recovers GAR to 0.727, confirming attention misallocation as the proximal cause; time-scheduled sampling, the first transfer to auxiliary attention objectives in multi-turn transformers, compresses the gap from 8$\times$ to ${\sim}$1.3$\times$ on Qwen and from 27$\times$ to ${\sim}$2.9$\times$ on Llama-3.1-8B, with no perplexity cost ($0.401\pm0.047$, three seeds), generalizing across architectures.
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b531a07-a2f3-49ff-9c38-04e56ace0cdd",
  "isSidechain": true,
  "promptId": "a3e6062b-fe39-400b-a5a8-e5805ce60227",
  "agentId": "a56f1deb740d009c5",
  "type": "user",
  "uuid": "93fed0a4-50b5-434c-81f3-5f157093e9c8",
  "sourceToolAssistantUUID": "0b531a07-a2f3-49ff-9c38-04e56ace0cdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-24T18:24:53.242Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AoHZBjbd1Jtwkf9ZkkDZcF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93fed0a4-50b5-434c-81f3-5f157093e9c8",
  "isSidechain": true,
  "agentId": "a56f1deb740d009c5",
  "requestId": "req_011CbMryVUbGzqBeAHCEDWk8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5566fc95-be25-4f82-839e-c74d1d8cf632",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrW94Yqtrovh6eczfZWsn8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34765,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34765,
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

_source line 7 · 2026-05-24T18:24:53.249Z_

<details><summary>↩ Tool result · `toolu_01AoHZBjbd1Jtwkf9ZkkDZcF`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Attention to system-prompt goals decays 70.8\% over five conversation turns on Qwen-2.5-7B-Instruct, despite residual stream probes confirming that goal representations persist (AUC\,=\,0.98; \citealp{dongre2026attention}). The decay is not model-specific: \citet{dongre2026attention} documented 27--48\% Goal Accessibility Ratio (GAR) decline across 12 models, and it has concrete downstream consequences: instruction compliance drops by up to 24 percentage points on content-constrained tasks (\S\ref{sec:discussion}).
4	
5	Existing interventions operate at inference time or are turn-agnostic. Split-softmax \citep{li2024measuring} separates instruction from conversation tokens; StreamingLLM \citep{xiao2024streaming} retains anchor tokens; Gated Attention \citep{qiu2025gated} applies per-head sigmoid gates within a single forward pass. None addresses the training--inference mismatch at the source. Auxiliary attention losses, which optimize GAR alongside next-token prediction (NTP), offer a training-time alternative, but whether such objectives transfer from teacher-forced training to autoregressive generation has not been tested. Classical exposure bias mitigation \citep{bengio2015scheduled,lamb2016professor} targets RNN sequence generation; no multi-turn transformer equivalent exists.
6	
7	We introduce ThreadGate, per-layer content-and-turn-conditioned MLP gates on the residual stream ($x_{l+1} = x_l + g_l \cdot f_l(x_l)$), not as a remedy but as a controlled testbed for isolating failure mechanisms. A five-way comparison (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base) forms a causal exclusion chain (\S\ref{sec:comparison-design}): each adjacent pair kills one alternative hypothesis, tracing the failure to exposure bias \citep{bengio2015scheduled}, ruling out gradient conflict, gating architecture, and turn conditioning.
8	
9	\begin{figure*}[t]
10	  \centering
11	  \includegraphics[width=\textwidth]{fig1_headline.pdf}
12	  \caption{Exposure bias destroys auxiliary attention losses. \textbf{(a)}~GAR decays 85--90\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \textbf{(b)}~Under TF evaluation all variants reach GAR$\approx$0.50, but AR generation collapses GAR by 8--17$\times$ (log scale). \textbf{(c)}~Scheduled sampling compresses the TF/AR gap from 7.8$\times$ to 1.3$\times$ (Qwen) and 12.0$\times$ to 2.9$\times$ (Llama).}
13	  \label{fig:headline}
14	\end{figure*}
15	
16	Training succeeds: all variants converge to TF GAR\,=\,0.50 (Figure~\ref{fig:headline}). Under autoregressive generation, GAR collapses to 0.019--0.064 (8--17$\times$). PCGrad eliminates gradient conflict but \emph{worsens} AR GAR ($p$\,=\,0.002), ruling it out by \emph{modus tollens}. Steering ($\beta$\,=\,5) recovers GAR to 0.727; scheduled sampling compresses the gap to ${\sim}$1.3$\times$ on Qwen and ${\sim}$2.9$\times$ on Llama (\S\ref{subsec:ss}). Our contributions: (1)~first empirical measurement of exposure bias on auxiliary attention losses (8--27$\times$ across two architectures); (2)~PCGrad-based causal exclusion of gradient conflict ($p$\,=\,0.002, effect reverses); (3)~inference-time $\beta$-steering recovers GAR to 0.727, confirming attention misallocation rather than representation degradation as the proximal cause; (4)~cross-architecture validation on Llama-3.1-8B; (5)~first evidence that time-scheduled sampling \citep{bengio2015scheduled} transfers to auxiliary attention objectives in multi-turn transformers, compressing the gap from 8--27$\times$ to 1.3--2.9$\times$ across two architectures ($0.401\pm0.047$, three seeds on Qwen). Code and data are available at \url{https://anonymous.4open.science/r/turn-residual-gating}.
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5566fc95-be25-4f82-839e-c74d1d8cf632",
  "isSidechain": true,
  "promptId": "a3e6062b-fe39-400b-a5a8-e5805ce60227",
  "agentId": "a56f1deb740d009c5",
  "type": "user",
  "uuid": "15569ca2-59ee-4f22-9d2e-20ad4ab38a4b",
  "sourceToolAssistantUUID": "5566fc95-be25-4f82-839e-c74d1d8cf632",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-24T18:24:53.528Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LxXWQvi43eNuiTMFDTQU2a`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15569ca2-59ee-4f22-9d2e-20ad4ab38a4b",
  "isSidechain": true,
  "agentId": "a56f1deb740d009c5",
  "requestId": "req_011CbMryVUbGzqBeAHCEDWk8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3eb33574-c504-410b-a9ef-abbb5c7265c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrW94Yqtrovh6eczfZWsn8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34765,
      "cache_read_input_tokens": 0,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 34765
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 254,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 34765,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 34765,
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

_source line 9 · 2026-05-24T18:24:53.534Z_

<details><summary>↩ Tool result · `toolu_01LxXWQvi43eNuiTMFDTQU2a`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Multi-turn dialogue and attention decay.}
4	Multi-turn coherence has been a persistent challenge from early dialogue systems \citep{li2016persona,roller2021recipes,zhang2020dialogpt} through modern long-context models \citep{xu2022goldfish}, with benchmarks such as MT-Bench \citep{zheng2024judging} and MT-Bench-101 \citep{bai2024mtbench101} continuing to expose quality gaps at later turns \citep{laban2025lost,liu2026intent}. Most relevant to our work, \citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) and showed that attention to goal tokens decays 27--48\% across 12 models while residual probes retain goal information (AUC\,=\,0.98). We observe a steeper 70.8\% decline on Qwen-2.5-7B. \citet{li2024measuring} independently quantified instruction instability and proposed split-softmax as an inference-time remedy. Our work differs in scope: we diagnose \emph{why} training-time attention optimization fails to transfer to inference, and provide the first training-time mitigation.
5	
6	\paragraph{Gating and attention manipulation.}
7	Residual gating has evolved from highway networks \citep{srivastava2015highway} through ResNet skip connections \citep{he2016deep} to ReZero \citep{bachlechner2021rezero}, layer pruning \citep{gromov2024unreasonable}, LayerDrop \citep{fan2020layerdrop}, and adaptive depth \citep{schuster2022calm,raposo2024mixture}. Most relevant is Gated Attention \citep{qiu2025gated}: per-head sigmoid gates achieving MMLU \citep{hendrycks2021measuring} $+$2.03 at 15B scale. ThreadGate differs in conditioning on turn position; our results show neither turn conditioning nor GLU-style gating \citep{dauphin2017language,shazeer2020glu} overcomes exposure bias. On the analysis side, head specialization \citep{clark2019what,voita2019analyzing,kovaleva2019revealing}, attention visualization \citep{vig2019multiscale}, positional bias calibration \citep{liu2024lost,xiao2024streaming}, and attention steering (PASTA; \citealp{zhang2024tell}) address inference behavior; our $\beta$-steering serves a diagnostic role. Multi-task gradient methods---PCGrad \citep{yu2020pcgrad}, CAGrad \citep{liu2021cagrad}---treat conflict as the root cause; we repurpose PCGrad as a diagnostic and show conflict is a symptom, not the cause.
8	
9	\paragraph{Exposure bias in sequence models.}
10	Teacher forcing creates a distributional mismatch between training and inference \citep{wiseman2016sequence,arora2022exposure}. Scheduled sampling \citep{bengio2015scheduled} introduced curriculum-based mixing; subsequent work proposed sequence-level objectives \citep{ranzato2016sequence}, adversarial regularization \citep{lamb2016professor}, self-recovery analysis \citep{he2019exposure}, bridging strategies for NMT \citep{zhang2019bridging}, and search-based training \citep{leblond2018searnn}. \citet{mihaylova2019scheduled} extended scheduled sampling to transformers for single-turn NMT. \citet{dou2019attention} proposed attention forcing---supervising cross-attention during NMT---and \citet{dou2022parallel} extended it with KL-divergence switching. Our work differs: (i)~time-scheduled sampling (linearly increasing $\rho$), not data-dependent; (ii)~self-attention in multi-turn dialogue, not cross-attention in NMT; (iii)~auxiliary attention objectives, not primary translation loss. No prior work examines exposure bias on \emph{auxiliary} attention objectives or provides multi-turn transformer mitigation; we fill both gaps.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3eb33574-c504-410b-a9ef-abbb5c7265c8",
  "isSidechain": true,
  "promptId": "a3e6062b-fe39-400b-a5a8-e5805ce60227",
  "agentId": "a56f1deb740d009c5",
  "type": "user",
  "uuid": "63204d28-2e78-44c8-876a-0a8a6197ecee",
  "sourceToolAssistantUUID": "3eb33574-c504-410b-a9ef-abbb5c7265c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-24T18:24:57.853Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CGmwAJZKBEBuoPhMneUbsJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63204d28-2e78-44c8-876a-0a8a6197ecee",
  "isSidechain": true,
  "agentId": "a56f1deb740d009c5",
  "requestId": "req_011CbMryt87fRpy1NxkVWsbp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "931f8adb-dcf5-4b30-bf7e-b90d73e8daf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZHXHbUqdovHdNuFyFvLYb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3784,
      "cache_read_input_tokens": 34765,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3784,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 11 · 2026-05-24T18:24:57.871Z_

<details><summary>↩ Tool result · `toolu_01CGmwAJZKBEBuoPhMneUbsJ`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Preliminaries}\label{sec:background}
4	
5	\paragraph{Goal Accessibility Ratio.}
6	Standard metrics such as perplexity and attention entropy capture generation quality but not \emph{what} the model attends to. In multi-turn dialogue, a model may generate fluent text while progressively ignoring task specifications in the system prompt. We need a metric that directly measures whether goal-relevant context receives attention. We denote the task specification tokens in the system prompt as \emph{goal tokens} $\mathcal{G}$. In the standard transformer attention mechanism \citep{vaswani2017attention}, \citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) for a model with $L$ layers and $H$ heads at turn $\tau$ as
7	\begin{equation}\label{eq:gar}
8	  \text{GAR}(\tau) = \frac{1}{L \cdot H \cdot |\mathcal{R}_\tau|} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{i \in \mathcal{R}_\tau} \sum_{j \in \mathcal{G}} A_{i,j}^{(\ell,h)},
9	\end{equation}
10	where $\mathcal{R}_\tau$ is the set of response tokens at turn $\tau$ and $A_{i,j}^{(\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\ell$, head $h$.
11	
12	\paragraph{Two GAR variants.}
13	\textbf{GAR-Dongre} is the original definition (Eq.~\ref{eq:gar}), averaging over all response tokens. However, averaging dilutes the signal with intermediate positions that may legitimately attend to local context rather than the system prompt. The last token of each assistant turn is where the model aggregates information for the next continuation---attention at this position most directly reflects the model's awareness of task specifications. \textbf{GAR-ours} restricts the measurement accordingly:
14	\begin{equation}\label{eq:gar-ours}
15	  \text{GAR\text{-}ours}(\tau) = \frac{1}{L \cdot H} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{j \in \mathcal{G}} A_{t_\tau,\, j}^{(\ell,h)},
16	\end{equation}
17	where $t_\tau$ is the last token index at turn $\tau$. Attention at this position reflects the information drawn upon for continuation; we use GAR-ours as the optimization target for $\mathcal{L}_\text{GAR}$ (\S\ref{sec:loss}).
18	
19	\subsection{ThreadGate Architecture}
20	
21	Different transformer layers serve different roles: early layers capture local syntax while later layers integrate long-range context \citep{gromov2024unreasonable}. A global intervention would uniformly scale all layers, but goal attention decay is layer-dependent: some layers contribute more to cross-turn information routing than others. ThreadGate therefore adds a \emph{per-layer} gating mechanism to the residual stream, allowing the model to learn which layers to modulate. At each layer $l$, the residual update is scaled by a scalar gate:
22	\begin{equation}
23	  x_{l+1} = x_l + g_l \cdot f_l(x_l),
24	\end{equation}
25	where $f_l$ denotes the sublayer computation (self-attention or FFN). From the perspective that residual networks function as ensembles of shallow paths \citep{veit2016residual}, per-layer gating selectively modulates individual paths. This resembles ReZero \citep{bachlechner2021rezero}, which initializes a single trainable scalar at zero to stabilize deep network training. ThreadGate differs in three ways: (i)~gates are \emph{content-conditioned}, a function of the hidden state rather than a fixed scalar; (ii)~gates are \emph{turn-conditioned}, incorporating conversation-position features; (iii)~gates are initialized near identity ($\sigma(1.5) \approx 0.82$) rather than zero, preserving the pretrained model's computation.
26	
27	\paragraph{Gate network.} A fixed scalar per layer (as in ReZero) cannot adapt to varying inputs; the gate must be \emph{content-conditioned} so that different conversations or turns can receive different modulation. Adding \emph{turn conditioning} allows the gate to distinguish early turns (where GAR is naturally high) from late turns (where intervention is most needed). Each gate $g_l$ is thus produced by a two-layer MLP that takes both content and turn features as input:
28	\begin{align}\label{eq:gate}
29	  g_l = \sigma\bigl(W_2\,\text{ReLU}(&W_1\,[\text{proj}(x_l);\;\text{emb}(t_d, t_i)] \notag\\
30	  &+ b_1) + b_2\bigr),
31	\end{align}
32	where $\text{proj}(\cdot)$ reduces the hidden dimension to 16, and $\text{emb}(t_d, t_i)$ provides a 16-dimensional turn embedding. The 32-dimensional input passes through a 64-unit hidden layer to a scalar gate in $(0, 1)$ via sigmoid. For Qwen-2.5-7B ($L\!=\!28$), this adds ${\sim}$57K parameters ($<$0.001\% of 7B).
33	
34	\paragraph{Turn embedding.} The embedding $\text{emb}(t_d, t_i)$ encodes turn distance $t_d$ (turns since system prompt) and turn index $t_i$ via learned lookup tables, allowing gates to distinguish conversation positions. The \textbf{Uniform Gate} ablation replaces $\text{emb}(\cdot)$ with a learnable constant, removing turn awareness.
35	
36	\paragraph{Initialization.} Gate biases are set to 1.5 (${\sim}$82\% pass-through), contrasting ReZero's zero initialization that would suppress pretrained capabilities. Gate parameters receive a $10\times$ learning rate multiplier.
37	
38	\subsection{Training Objective}\label{sec:loss}
39	
40	Next-token prediction alone provides no gradient signal for attention allocation; a model can achieve low perplexity while distributing attention arbitrarily. The auxiliary GAR loss provides explicit pressure to maintain goal-token attention, while a diversity regularizer prevents gate collapse. The training objective combines three terms:
41	\begin{equation}
42	  \mathcal{L} = \mathcal{L}_\text{NTP} + \lambda_\text{GAR}\,\mathcal{L}_\text{GAR} + \lambda_\text{div}\,\mathcal{L}_\text{div}.
43	\end{equation}
44	$\mathcal{L}_\text{NTP}$ is the standard next-token prediction loss. We use MSE rather than cross-entropy for $\mathcal{L}_\text{GAR}$ because GAR is a continuous ratio, not a probability, and MSE provides \emph{bidirectional} pressure, penalizing both under-attention (GAR\,$<$\,$\tau$) and over-attention (GAR\,$>$\,$\tau$). This symmetry is critical: a unidirectional maximize objective drives gates toward identity (Appendix~\ref{sec:appendix-loss}). The GAR loss is:
45	\begin{equation}
46	  \mathcal{L}_\text{GAR} = \text{MSE}(\text{GAR\text{-}ours}, \tau),
47	\end{equation}
48	where $\tau = 0.5$ targets allocating half of the last token's attention capacity to goal tokens. GAR is measured at the last token of each assistant turn (GAR-ours, \S\ref{sec:background}). Without explicit diversity pressure, all gates converge to the same value (typically near 1.0), eliminating the layer-specific modulation that is the design intent. The gate diversity loss prevents this collapse:
49	\begin{equation}
50	  \mathcal{L}_\text{div} = \text{ReLU}(\sigma_\text{min} - \text{std}(\mathbf{g})),
51	\end{equation}
52	where $\mathbf{g} = [g_1, \ldots, g_L]$ and $\sigma_\text{min}$ is a minimum standard deviation threshold. Both $\lambda_\text{GAR} = \lambda_\text{div} = 1.0$.
53	
54	\paragraph{Loss design evolution.} The MSE formulation was selected from seven iterations spanning four loss families (Appendix~\ref{sec:appendix-loss}): cumulative (v1--v2) and maximize (v3--v6) objectives either starve gate gradients at equilibrium or drive gates toward identity. Only MSE provides bidirectional pressure, penalizing both over- and under-attention, preventing identity collapse.
55	
56	\subsection{Controlled Comparison Design}\label{sec:comparison-design}
57	
58	We design a five-way comparison where each adjacent pair isolates one factor: \textbf{ThreadGate vs.\ Uniform Gate} (turn conditioning), \textbf{ThreadGate vs.\ LoRA-only} (gating mechanism), \textbf{ThreadGate vs.\ +PCGrad} (gradient direction conflict via gradient surgery \citep{yu2020pcgrad}), and \textbf{Fine-tuned vs.\ Base} (LoRA adaptation). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed (Appendix~\ref{sec:appendix-hyper}).
59	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "931f8adb-dcf5-4b30-bf7e-b90d73e8daf2",
  "isSidechain": true,
  "promptId": "a3e6062b-fe39-400b-a5a8-e5805ce60227",
  "agentId": "a56f1deb740d009c5",
  "type": "user",
  "uuid": "37621f82-793e-4a41-a1a7-f31cc0074643",
  "sourceToolAssistantUUID": "931f8adb-dcf5-4b30-bf7e-b90d73e8daf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-24T18:24:58.202Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HbiCqJGC8zcV8toVXsGo8p`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37621f82-793e-4a41-a1a7-f31cc0074643",
  "isSidechain": true,
  "agentId": "a56f1deb740d009c5",
  "requestId": "req_011CbMryt87fRpy1NxkVWsbp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f2ad50b-b9a4-4b93-ad17-1b8cd7a0a060",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZHXHbUqdovHdNuFyFvLYb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3784,
      "cache_read_input_tokens": 34765,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3784,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 13 · 2026-05-24T18:24:58.210Z_

<details><summary>↩ Tool result · `toolu_01HbiCqJGC8zcV8toVXsGo8p`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	
6	We fine-tune Qwen-2.5-7B-Instruct with LoRA \citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; training costs in Appendix~\ref{sec:appendix-cost}). Full hyperparameters are in Appendix~\ref{sec:appendix-hyper}; dataset statistics in Appendix~\ref{sec:appendix-data}; the controlled comparison design is described in \S\ref{sec:comparison-design}. We evaluate under \emph{IID} (same-distribution UltraChat text) and \emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \citep{dongre2026attention}, and PPL.
7	
8	\subsection{Main Results}
9	
10	Table~\ref{tab:four-way} presents the five-way comparison. Under TF evaluation, all fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\leq$2\,pp), PPL is 2.78 for all. IID and held-out protocols produce identical rankings (held-out GAR-ours differs by $\leq$1\,pp), ruling out data overlap as a confound. GAR-Dongre remains low (0.01--0.02) with no TF-AR gap, confirming that only concentrated last-token attention is vulnerable to distribution shift; scheduled sampling breaks this pattern (\S\ref{subsec:ss}).
11	
12	Under AR generation ($N$\,=\,50), GAR-ours drops to 0.019--0.064, an 8--17$\times$ gap (Figure~\ref{fig:headline}). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\ LoRA-only is significant ($p$\,=\,0.004; Appendix~\ref{sec:appendix-stats}), yet the gap remains 7.8$\times$. A second seed confirms TF stability ($0.504\pm0.001$). MMLU 5-shot accuracy remains within 0.8\,pp across all variants (Appendix~\ref{sec:appendix-mmlu}). We analyze this distribution shift in \S\ref{sec:analysis}.
13	
14	\begin{table*}[t]
15	\centering
16	\small
17	\caption{Five-way comparison on Qwen-2.5-7B-Instruct. TF evaluation uses IID UltraChat and 50 held-out conversations; AR evaluation uses $N$\,=\,50 held-out conversations (mean 3.6 user turns). All fine-tuned variants converge under TF ($\leq$2\,pp spread); the 8--17$\times$ TF-AR gap persists across all configurations. $\bar{g}\!\pm\!\sigma_g$: learned gate mean and std across 28 layers (LoRA-only has no gates). GAR-O = GAR-ours; GAR-D = GAR-Dongre \citep{dongre2026attention}.}
18	\label{tab:four-way}
19	\begin{tabular}{l ccc ccc cc c}
20	\toprule
21	& \multicolumn{3}{c}{\textbf{IID (TF)}} & \multicolumn{3}{c}{\textbf{Held-out (TF)}} & \multicolumn{2}{c}{\textbf{AR ($N$\,=\,50)}} & \\
22	\cmidrule(lr){2-4} \cmidrule(lr){5-7} \cmidrule(lr){8-9}
23	\textbf{Configuration} & GAR-O & GAR-D & PPL & GAR-O & GAR-D & PPL & GAR-O & 95\% CI & $\bar{g}\!\pm\!\sigma_g$ \\
24	\midrule
25	\multicolumn{10}{l}{\emph{Baseline}} \\
26	Base              & 0.01 & 0.00 & 4.23 & 0.01 & 0.00 & 4.34 & 0.019 & {\scriptsize[.014,\,.024]} & --- \\
27	\midrule
28	\multicolumn{10}{l}{\emph{Gated variants}} \\
29	ThreadGate        & 0.50 & \textbf{0.02} & 2.78 & 0.50 & \textbf{0.02} & 2.78 & \textbf{0.064} & {\scriptsize[.041,\,.091]} & .93\,{\scriptsize$\pm$\,.05} \\
30	\;+\,PCGrad       & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.030 & {\scriptsize[.023,\,.038]} & --- \\
31	Uniform Gate      & 0.49 & 0.01 & 2.78 & \textbf{0.51} & 0.01 & 2.78 & 0.033 & {\scriptsize[.025,\,.043]} & .96\,{\scriptsize$\pm$\,.05} \\
32	\midrule
33	\multicolumn{10}{l}{\emph{Ungated}} \\
34	LoRA-only         & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.037 & {\scriptsize[.027,\,.050]} & 1.00 \\
35	\bottomrule
36	\end{tabular}
37	\end{table*}
38	
39	\begin{figure*}[t]
40	  \centering
41	  \includegraphics[width=\textwidth,height=0.32\textheight,keepaspectratio]{fig4_attention_heatmap.pdf}
42	  \caption{Per-turn GAR-ours under AR generation ($N$\,=\,5 conversations, 10 turns). All fine-tuned variants cluster together (77--81\% decay; $\Delta$\,=\,3.3\,pp between ThreadGate and LoRA-only); Base decays 87.5\%. Gating adds zero incremental effect on the attention decay pattern.}
43	  \label{fig:attention-heatmap}
44	\end{figure*}
45	
46	\subsection{Inference-Time Attention Steering}\label{subsec:steering}
47	
48	All training-time interventions leave the exposure bias gap intact. If the collapse is caused by attention misallocation rather than representation degradation, then directly correcting attention should recover GAR. We test this by adding a constant bias $\beta$ to pre-softmax attention logits for goal-token positions during generation:
49	\begin{equation}
50	  \tilde{A}_{i,j}^{(\ell,h)} = A_{i,j}^{(\ell,h)} + \beta \cdot \mathbf{1}[j \in \mathcal{G}],
51	\end{equation}
52	where $\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero. The response is sharply nonlinear: $\beta \in [0, 2]$ yields marginal improvement, then $\beta = 3$ triggers a phase transition to GAR\,=\,0.556 (9\% PPL cost). At $\beta$\,=\,5, GAR reaches 0.727$\pm$0.061 (PPL 1.77); the operating region $\beta \in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Figure~\ref{fig:steering-recovery}; full results in Appendix~\ref{sec:appendix-steering}; per-$\beta$ turn-level profiles in Appendix~\ref{sec:appendix-steering-viz}).
53	
54	\begin{figure}[t]
55	  \centering
56	  \includegraphics[width=\columnwidth]{fig5_attention_steering.pdf}
57	  \caption{Inference-time $\beta$-steering recovers GAR from 0.064 to 0.727, confirming attention misallocation as the proximal cause (9\% PPL cost at $\beta$\,=\,3; phase transition at $\beta \in [2, 3]$).}
58	  \label{fig:steering-recovery}
59	\end{figure}
60	
61	This closes the causal loop: if the collapse were due to representation drift in hidden states, no amount of attention reweighting could recover GAR. The recovery confirms attention misallocation, not representation degradation, as the proximal cause (qualitative examples in Appendix~\ref{sec:appendix-examples}).
62	
63	\subsection{Scheduled Sampling Compresses the TF--AR Gap}\label{subsec:ss}
64	
65	Scheduled sampling \citep{bengio2015scheduled}, which mixes model-generated tokens into training prefixes with linearly increasing probability (implementation details in Appendix~\ref{sec:appendix-ss}), directly targets the training-inference mismatch identified in \S\ref{subsec:dist-shift}. Across three seeds, AR GAR-ours rises from 0.064 to $0.401\pm0.047$ (seeds: 0.347 / 0.423 / 0.433; per-seed details in Appendix~\ref{sec:appendix-perseed}), compressing the gap from 7.8$\times$ to ${\sim}$1.3$\times$ (per-seed gaps: 1.45$\times$, 1.17$\times$, 1.15$\times$; TF GAR $0.498\pm0.004$) with no PPL cost ($1.441\pm0.001$; Figure~\ref{fig:ss-gap}). Steering on SS models is remarkably stable ($\beta$\,=\,5: $0.717\pm0.001$): the training-time seed variance (std\,=\,0.047 at $\beta$\,=\,0) is nearly eliminated (Figure~\ref{fig:ss-multiseed}), suggesting $\beta$-steering converges to a seed-independent attention equilibrium. The improvement generalizes across GAR definitions: SS raises mid-turn GAR above 0.36 under all four alternative token-position variants (Appendix~\ref{sec:appendix-gar-robust}), while ThreadGate only improves last-token GAR (0.325 vs.\ all-token 0.025): SS builds a broad goal-attention pattern, not position-specific overfitting. GAR-Dongre also rises substantially under SS ($N$\,=\,5 pilot; see Appendix~\ref{sec:appendix-n5}), the only intervention that moves both metrics. The benefit generalizes across architectures: on Llama-3.1-8B, SS compresses the gap from ${\sim}$12$\times$ to 2.9$\times$ (AR GAR 0.166, TF GAR 0.477), weaker than Qwen's ${\sim}$1.3$\times$ likely due to fewer training epochs (2 vs.\ 3; \S\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.
66	
67	\begin{figure}[t]
68	  \centering
69	  \includegraphics[width=\columnwidth]{fig_ss_gap_compression.pdf}
70	  \caption{Scheduled sampling compresses the TF-AR gap from 7.8$\times$ to ${\sim}$1.3$\times$, the only variant approaching parity across five training conditions.}
71	  \label{fig:ss-gap}
72	\end{figure}
73	
74	\begin{figure}[t]
75	  \centering
76	  \includegraphics[width=\columnwidth]{fig_ss_multiseed.pdf}
77	  \caption{Multi-seed AR GAR under scheduled sampling ($\beta$\,=\,0 and $\beta$\,=\,5, three seeds). Steering nearly eliminates seed variance (std: 0.047$\to$0.001).}
78	  \label{fig:ss-multiseed}
79	\end{figure}
80	
81	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f2ad50b-b9a4-4b93-ad17-1b8cd7a0a060",
  "isSidechain": true,
  "promptId": "a3e6062b-fe39-400b-a5a8-e5805ce60227",
  "agentId": "a56f1deb740d009c5",
  "type": "user",
  "uuid": "dc5397a5-d4de-4f2f-ab4c-76f24e15fe65",
  "sourceToolAssistantUUID": "8f2ad50b-b9a4-4b93-ad17-1b8cd7a0a060",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-24T18:24:58.555Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NTY9y7ADWDGCcNqAtjbkWJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc5397a5-d4de-4f2f-ab4c-76f24e15fe65",
  "isSidechain": true,
  "agentId": "a56f1deb740d009c5",
  "requestId": "req_011CbMryt87fRpy1NxkVWsbp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1cb1fc8-46f6-4ef4-933a-11b8d3aef71e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZHXHbUqdovHdNuFyFvLYb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3784,
      "cache_read_input_tokens": 34765,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3784
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 34765,
          "cache_creation_input_tokens": 3784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3784,
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

_source line 15 · 2026-05-24T18:24:58.561Z_

<details><summary>↩ Tool result · `toolu_01NTY9y7ADWDGCcNqAtjbkWJ`</summary>

```text
1	\section{Analysis}\label{sec:analysis}
2	
3	The five-way comparison (\S\ref{sec:experiments}) yields a paradox: training succeeds but inference fails, and no single architectural factor explains the gap. This section resolves it through a causal exclusion chain; each subsection kills one alternative hypothesis: \S\ref{subsec:gate-conditioning} kills ``turn conditioning rescues late-turn attention''; \S\ref{subsec:pcgrad} kills ``gradient conflict prevents GAR convergence''; \S\ref{subsec:dist-shift} identifies exposure bias as the surviving explanation. \S\ref{subsec:mechanism-specificity} confirms selectivity via an orthogonal metric, and \S\ref{subsec:cross-model} confirms generalization across architectures.
4	
5	\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
6	
7	We compare gate values at turn~1 (early) and turn~21 (late) across all 28 layers. The gates invert the design intent: in 27/28 layers, gate values are \emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \times 10^{-8}$, $r = 0.975$); e.g., layer~23 shifts from 0.769 to 0.979. NTP pressure pushes gates toward 1.0, a convergence pattern reminiscent of attention collapse in deep transformers \citep{dong2021attention}, yielding inference-time values of 0.93--0.98 (2--7\% attenuation; Table~\ref{tab:four-way}; full gate profiles in Appendix~\ref{sec:appendix-gate-profile}). The Uniform Gate learns comparable per-layer variation (L3\,=\,0.777, L27\,=\,1.000) despite lacking turn conditioning, confirming the structure arises from LoRA$+$GAR pressure (Figure~\ref{fig:gate-shift}a). Does the NTP-GAR gradient conflict prevent the intended behavior?
8	
9	\begin{figure}[t]
10	  \centering
11	  \includegraphics[width=\columnwidth]{fig3_gate_shift.pdf}
12	  \caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \times 10^{-8}$). (b)~Distribution shift ($N$\,=\,5 pilot): the TF-AR GAR gap persists across all five variants. Pilot gaps (20--34$\times$) exceed final $N$\,=\,50 estimates (8--17$\times$; Table~\ref{tab:four-way}) due to smaller sample size.}
13	  \label{fig:gate-shift}
14	\end{figure}
15	
16	\subsection{PCGrad Gradient Conflict Exclusion}\label{subsec:pcgrad}
17	
18	NTP and GAR gradients oppose in 68--79\% of layers (cosine similarity $-$0.089$\to$$-$0.042 across epochs), with NTP magnitude dominance growing from 7.5$\times$ to 14.7$\times$ (full gradient statistics in Appendix~\ref{sec:appendix-gradient}). If this conflict prevents GAR convergence, eliminating it via PCGrad \citep{yu2020pcgrad}, which projects conflicting gradients onto the other's normal plane, should prevent the collapse. To our knowledge, this is the first application of PCGrad as a \emph{diagnostic} tool rather than an optimization method.
19	
20	PCGrad shifts cosine similarity to oscillate around zero, yet TF metrics are unchanged. AR GAR \emph{worsens}: 0.064$\to$0.030 ($p$\,=\,0.002; Figure~\ref{fig:training-pcgrad}b in Appendix~\ref{sec:appendix-gradient}). By \emph{modus tollens}: removing direction conflict does not prevent collapse; therefore it is not the cause. The 7.5--14.7$\times$ magnitude dominance renders directional interference inconsequential. Cross-model analysis confirms this pattern: Llama-3.1-8B gradients are near-orthogonal (cos\,=\,+0.005) with 25.7$\times$ NTP dominance (Table~\ref{tab:gradient-crossmodel}).
21	
22	\subsection{Distribution Shift Analysis}\label{subsec:dist-shift}
23	
24	The TF-AR GAR gap persists across all variants (Table~\ref{tab:four-way}). GAR-Dongre provides a control: it remains uniformly low (0.01--0.02) with no distribution gap, so the shift selectively destroys concentrated last-token attention while leaving diffuse attention unaffected. The mechanism is exposure bias \citep{bengio2015scheduled,zhang2019bridging,arora2022exposure}: during training the model conditions on ground-truth prefixes; at inference, on its own outputs. NTP self-recovers \citep{he2019exposure} because prediction is the same task at both regimes; GAR optimizes a distributional property with no autoregressive counterpart. Unlike token-level predictions, attention flow through layers \citep{abnar2020quantifying} over model-generated tokens has no training-time analogue, explaining why TF GAR-ours remains near $\tau$\,=\,0.5 while AR GAR collapses (77--87\% per-turn decay; Figure~\ref{fig:attention-heatmap}; scaling analysis in Appendix~\ref{sec:appendix-eb-scaling}; per-turn dynamics in Appendices~\ref{sec:appendix-ar-gar-dynamics} and~\ref{sec:appendix-perturn-detail}).
25	
26	\subsection{Mechanism Specificity}\label{subsec:mechanism-specificity}
27	
28	We test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed), confirming exposure bias disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\times$) and Qwen (1.28$\times$) vs.\ the order-of-magnitude GAR-ours collapse.
29	
30	\subsection{Cross-Model Replication}\label{subsec:cross-model}
31	
32	We replicate on Llama-3.1-8B-Instruct \citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\,=\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (CoV\,$>$\,100\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\times$ and 26$\times$ (Figure~\ref{fig:crossmodel}a in Appendix~\ref{sec:appendix-llama}). Gate profiles differ qualitatively (Figure~\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\,=\,0.793) while Llama dips at late layers (L25\,=\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\ref{sec:appendix-viz}). The gap is substantial on both architectures (8--17$\times$ on Qwen, 27$\times$ on Llama), consistent with exposure bias as architecture-independent.
33	
34	Scheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\sim}$12$\times$ to 2.9$\times$ (TF GAR 0.477, AR GAR 0.166). The compression is weaker than Qwen's (${\sim}$1.3$\times$), likely because the Llama SS variant trained for only 2 epochs vs.\ 3 on Qwen, yielding less distributional robustification. Notably, $\beta$\,=\,3 yields almost no improvement on Llama SS (GAR 0.173 vs.\ 0.166 at $\beta$\,=\,0), whereas it triggers a phase transition on Qwen (0.556); the transition on Llama is deferred to $\beta$\,=\,5, where GAR jumps to 0.791, exceeding Qwen SS (0.717). The steeper phase transition suggests Llama's deeper architecture (32 layers) requires a higher steering threshold to overcome compounded distributional drift, yet ultimately provides more surface for attention reweighting. These results confirm SS as a model-general mitigation: it compresses the exposure bias gap on both architectures, with the residual gap attributable to training budget rather than architectural limitations (full results in Appendix~\ref{sec:appendix-llama}).
35	
36	Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern: 79.8\% GAR decay and $\beta$-steering recovery to 0.715 (Appendix~\ref{sec:appendix-1.5b}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1cb1fc8-46f6-4ef4-933a-11b8d3aef71e",
  "isSidechain": true,
  "promptId": "a3e6062b-fe39-400b-a5a8-e5805ce60227",
  "agentId": "a56f1deb740d009c5",
  "type": "user",
  "uuid": "193e7427-1dcc-47a0-93cb-eae2974749ef",
  "sourceToolAssistantUUID": "d1cb1fc8-46f6-4ef4-933a-11b8d3aef71e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-24T18:25:03.986Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GKnBh4FXAfkrkTS17MGtii`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "193e7427-1dcc-47a0-93cb-eae2974749ef",
  "isSidechain": true,
  "agentId": "a56f1deb740d009c5",
  "requestId": "req_011CbMrzFdS2auHtcXYcSNvY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0fb56d12-4e77-47f4-80d3-c958c84ac55a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rMTJyPsAkSiMZuuoXeEGL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8658,
      "cache_read_input_tokens": 38549,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8658,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 17 · 2026-05-24T18:25:03.994Z_

<details><summary>↩ Tool result · `toolu_01GKnBh4FXAfkrkTS17MGtii`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	The failure traces to an incompatibility between teacher-forcing and GAR-family auxiliary losses, not to the gating architecture. This has implications beyond ThreadGate: any auxiliary attention objective paired with teacher forcing, whether per-head gating \citep{qiu2025gated}, split-softmax \citep{li2024measuring}, or residual scaling \citep{bachlechner2021rezero}, should face the same exposure bias barrier when targeting distributional properties of the attention pattern rather than the prediction itself.
4	
5	\paragraph{Why NTP self-recovers but GAR does not.} NTP self-recovers because the task (predict one token from a prefix) is identical at training and inference; exposure bias shifts the prefix distribution but preserves the prediction task \citep{he2019exposure}. GAR optimizes a \emph{global property of the prefix}, attention allocation to goal tokens, that has no autoregressive counterpart: the model receives no feedback on attention distributions during generation, so the training signal is specific to teacher-forced prefixes. Per-head analysis confirms this selectivity: heads with higher TF GAR shift most under AR generation ($r$\,=\,0.743; Appendix~\ref{sec:appendix-kl}).
6	
7	\paragraph{Downstream effects.} Instruction retention ($\beta$\,=\,3) shows late-turn compliance rising from 75.9\% to 87.0\% (+11.1\,pp, McNemar $p$\,=\,0.077; GAR correlation $r$\,=\,0.200, $p$\,=\,0.007). Content constraints benefit most (+23.8\,pp), while format constraints show zero change, consistent with GAR targeting cross-turn semantic coherence rather than locally-verifiable procedural rules (Appendix~\ref{sec:appendix-ir}).
8	
9	\paragraph{SS and steering as substitutes.} SS provides training-time mitigation with no inference cost; steering provides inference-time recovery with PPL cost. At high $\beta$ the two converge: they are substitutes, not complements ($\beta$\,=\,5: SS GAR\,=\,$0.717\pm0.001$ vs.\ TG\,=\,0.727; Figure~\ref{fig:steering-recovery}). SS is preferable when inference budgets are tight, steering when retraining is infeasible.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fb56d12-4e77-47f4-80d3-c958c84ac55a",
  "isSidechain": true,
  "promptId": "a3e6062b-fe39-400b-a5a8-e5805ce60227",
  "agentId": "a56f1deb740d009c5",
  "type": "user",
  "uuid": "812293b2-3bae-4dc4-ade5-a9b3764cb278",
  "sourceToolAssistantUUID": "0fb56d12-4e77-47f4-80d3-c958c84ac55a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-24T18:25:04.538Z_

<details open><summary>🔧 Tool call — Read · `toolu_019bVxLHUf9yGMwbfDQ822dt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "812293b2-3bae-4dc4-ade5-a9b3764cb278",
  "isSidechain": true,
  "agentId": "a56f1deb740d009c5",
  "requestId": "req_011CbMrzFdS2auHtcXYcSNvY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dbb11168-6181-4f7c-8d5a-5c7b5f3c839f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rMTJyPsAkSiMZuuoXeEGL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8658,
      "cache_read_input_tokens": 38549,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8658,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 19 · 2026-05-24T18:25:04.544Z_

<details><summary>↩ Tool result · `toolu_019bVxLHUf9yGMwbfDQ822dt`</summary>

```text
1	\section{Limitations}\label{sec:limitations}
2	
3	Our findings are demonstrated on two model families (Qwen-2.5-7B and Llama-3.1-8B), one dataset (UltraChat, 8K conversations), and most configurations use a single seed (scheduled sampling validated on three seeds; \S\ref{subsec:ss}); quality assessment relies on PPL rather than comprehensive benchmarks \citep{hendrycks2021measuring,lin2022truthfulqa}. We test only one auxiliary loss family (GAR with MSE target $\tau$\,=\,0.5); head-specific or layer-specific losses may exhibit different sensitivity to exposure bias. The PCGrad exclusion addresses gradient direction conflict only; magnitude imbalance \citep{chen2018gradnorm} and Nash equilibrium approaches \citep{navon2022nash} remain untested.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbb11168-6181-4f7c-8d5a-5c7b5f3c839f",
  "isSidechain": true,
  "promptId": "a3e6062b-fe39-400b-a5a8-e5805ce60227",
  "agentId": "a56f1deb740d009c5",
  "type": "user",
  "uuid": "27645d12-5a76-4cae-a730-7f20cf198389",
  "sourceToolAssistantUUID": "dbb11168-6181-4f7c-8d5a-5c7b5f3c839f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-24T18:25:04.876Z_

<details open><summary>🔧 Tool call — Read · `toolu_018cN6rMAxgC8KHyGzUePb7m`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27645d12-5a76-4cae-a730-7f20cf198389",
  "isSidechain": true,
  "agentId": "a56f1deb740d009c5",
  "requestId": "req_011CbMrzFdS2auHtcXYcSNvY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "830c5c21-3221-467e-a0bd-6fa0da4456e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rMTJyPsAkSiMZuuoXeEGL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8658,
      "cache_read_input_tokens": 38549,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8658,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 21 · 2026-05-24T18:25:05.166Z_

<details><summary>↩ Tool result · reported error · `toolu_018cN6rMAxgC8KHyGzUePb7m`</summary>

```text
File content (26081 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "830c5c21-3221-467e-a0bd-6fa0da4456e3",
  "isSidechain": true,
  "promptId": "a3e6062b-fe39-400b-a5a8-e5805ce60227",
  "agentId": "a56f1deb740d009c5",
  "type": "user",
  "uuid": "ded7cb76-8455-4a07-a0a9-214d90962852",
  "toolUseResult": "Error: File content (26081 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "830c5c21-3221-467e-a0bd-6fa0da4456e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-24T18:25:11.100Z_

The appendix is too large. Let me read it in chunks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ded7cb76-8455-4a07-a0a9-214d90962852",
  "isSidechain": true,
  "agentId": "a56f1deb740d009c5",
  "requestId": "req_011CbMrzjbwAHFccNZwWWAzi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab236416-0446-437e-8a14-6ea434071eb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SYYo1CohQ256TfnFZycp3T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1256,
      "cache_read_input_tokens": 47207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1256,
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

_source line 23 · 2026-05-24T18:25:12.861Z_

<details open><summary>🔧 Tool call — Read · `toolu_018tRCokS6FbNLc3Hdep3K4k`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab236416-0446-437e-8a14-6ea434071eb7",
  "isSidechain": true,
  "agentId": "a56f1deb740d009c5",
  "requestId": "req_011CbMrzjbwAHFccNZwWWAzi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21066833-e12e-4211-a484-953999e9b1c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SYYo1CohQ256TfnFZycp3T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1256,
      "cache_read_input_tokens": 47207,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1256
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 47207,
          "cache_creation_input_tokens": 1256,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1256,
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

_source line 24 · 2026-05-24T18:25:12.870Z_

<details><summary>↩ Tool result · `toolu_018tRCokS6FbNLc3Hdep3K4k`</summary>

```text
1	\section{Training Configuration}\label{sec:appendix-hyper}
2	
3	Table~\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\times$ learning rate multiplier and are initialized with bias 1.5 ($\sigma(1.5) \approx 0.82$); the gate MLP adds ${\sim}$57K parameters per variant ($<$0.001\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.5 over 3 epochs (29.7--37.1\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB VRAM), requiring 6--8 hours per variant.
4	
5	\begin{table}[h]
6	\centering\small
7	\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\dagger$ apply only to ThreadGate and its ablations.}
8	\label{tab:hyperparams}
9	\begin{tabular}{l@{\hspace{8pt}}l}
10	\toprule
11	\textbf{Parameter} & \textbf{Value} \\
12	\midrule
13	Base model & Qwen-2.5-7B-Instruct \\
14	LoRA rank / $\alpha$ & 16 / 32 \\
15	LoRA targets & \texttt{q\_proj}, \texttt{v\_proj} \\
16	Optimizer & AdamW ($\beta_1$\!=\!0.9, $\beta_2$\!=\!0.999) \\
17	Learning rate & $2 \times 10^{-4}$ \\
18	Gate LR mult.$^\dagger$ & $10\times$ \\
19	Batch / grad accum & 1 / 8 (eff.\ 8) \\
20	Epochs & 3 \\
21	Max seq length & 2048 \\
22	Training data & 8K UltraChat convs \\
23	Seed & 42 (+123 for TG, SS) \\
24	$\lambda_\text{GAR}$/$\lambda_\text{div}$ & 1.0 / 1.0 \\
25	GAR target $\tau$ & 0.5 \\
26	Gate init bias$^\dagger$ & 1.5 ($\sigma\!\approx\!0.82$) \\
27	Gate hidden dim$^\dagger$ & 64 \\
28	Turn embed dim$^\dagger$ & 16 \\
29	GPU & RTX PRO 6000 (96\,GB) \\
30	Training time & 6--8 h / variant \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\section{Loss Formulation Search}\label{sec:appendix-loss}
36	
37	The final MSE + gate diversity loss (\S\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.
38	
39	\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.
40	
41	\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\text{mean}(\text{GAR})$). The unbounded objective rewards full pass-through ($g \to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\lambda$=2 (v3), gates froze within 100 steps; at $\lambda$=10 (v3b), convergence to identity accelerated; at $\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.
42	
43	\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.
44	
45	\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\tau$ incurs the same penalty as GAR below $\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\mathcal{L}_\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).
46	
47	\begin{table*}[t]
48	\centering\footnotesize
49	\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}
50	\label{tab:loss-iterations}
51	\begin{tabular}{l l l p{5.8cm} c c}
52	\toprule
53	 & \textbf{Loss Family} & \textbf{Status} & \textbf{Failure Mechanism} & \textbf{GAR} & \textbf{PPL} \\
54	\midrule
55	v1  & Cumulative            & \texttimes~GAR loss $\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\
56	v2  & Cumulative + $\varepsilon$ & \texttimes~same trajectory & Numerical instability from cumulative product; $\varepsilon$-stabilization insufficient & ---  & ---  \\
57	v3  & Maximize ($\lambda$=2)  & \texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\
58	v3b & Maximize ($\lambda$=10) & \texttimes~identity collapse   & Higher $\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\
59	v5  & Maximize ($\lambda$=1)  & \texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\
60	v6  & Smooth saturation       & \texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\
61	v7  & MSE + gate div          & \checkmark~\textbf{converged}  & \textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\
62	\bottomrule
63	\end{tabular}
64	\end{table*}
65	
66	\section{Instruction Retention Details}\label{sec:appendix-ir}
67	
68	To evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\beta$\,=\,3 steering on $N$\,=\,200 held-out conversations. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end''). This evaluation bridges the gap between our attention-level metric (GAR) and observable model behavior.
69	
70	\paragraph{Evaluation protocol.} For each conversation, we inject a constraint into the system prompt and evaluate compliance across all assistant turns. A turn is compliant if it satisfies the constraint according to rule-based checkers (for format, count, and position constraints) or GPT-4-based evaluation (for content constraints, which require semantic judgment). We use the same 18 constraint types across all conversations, yielding $N$\,=\,54 paired evaluations (18 types $\times$ 3 conversations per type) for the McNemar analysis.
71	
72	\paragraph{Per-category results.} Table~\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions across turns---show the largest improvement (+23.8\,pp), consistent with GAR measuring attention to goal tokens. This category includes constraints like ``mention X in every response'' and ``always reference the original topic,'' which require sustained attention to the system prompt. Position constraints (e.g., ``start each response with Y'') show a modest improvement (+6.7\,pp), as they partially depend on goal-token attention. Format (e.g., ``use bullet points'') and count constraints (e.g., ``exactly 3 sentences'') show no change, consistent with these being procedural patterns that are cached in the model's generation routine rather than requiring ongoing attention to the system prompt.
73	
74	\paragraph{Correlation analysis.} The GAR-compliance correlation ($r$\,=\,0.200, $p$\,=\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. Other factors likely include the model's procedural memory for format constraints, the specificity of the constraint (vague constraints are harder regardless of attention), and the interaction between constraint type and conversation topic. McNemar's test ($p$\,=\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.
75	
76	Figure~\ref{fig:ir-bar} visualizes the per-category breakdown.
77	
78	\begin{figure}[h]
79	  \centering
80	  \includegraphics[width=\columnwidth]{fig_instruction_retention.pdf}
81	  \caption{Instruction retention by constraint category under $\beta$\,=\,3 steering. Content constraints benefit most (+23.8\,pp); format and count constraints are unaffected.}
82	  \label{fig:ir-bar}
83	\end{figure}
84	
85	\begin{table}[h]
86	\centering\small
87	\caption{Instruction retention by constraint category ($\beta$\,=\,3 steering on ThreadGate checkpoint). Content constraints benefit most from increased goal attention.}
88	\label{tab:ir-results}
89	\begin{tabular}{lccc}
90	\toprule
91	\textbf{Category} & $\beta$\,=\,0 & $\beta$\,=\,3 & $\Delta$ \\
92	\midrule
93	Content    & 61.9\% & 85.7\% & +23.8\,pp \\
94	Position   & 66.7\% & 73.3\% & +6.7\,pp \\
95	Count      & 100\%  & 100\%  & 0 \\
96	Format     & 100\%  & 100\%  & 0 \\
97	\midrule
98	\textbf{Overall} & 75.9\% & 87.0\% & +11.1\,pp \\
99	\bottomrule
100	\end{tabular}
101	\end{table}
102	
103	\section{Long-Conversation AR Evaluation}\label{sec:appendix-n5}
104	
105	The main results (Table~\ref{tab:four-way}) report AR GAR from $N$\,=\,50 held-out conversations with a mean of 3.6 user turns. Table~\ref{tab:n5-ar} presents complementary results on $N$\,=\,5 conversations with 10 turns each, testing whether the observed patterns generalize beyond the training distribution's conversation length.
106	
107	\paragraph{Gating advantage vanishes at length.} In these longer dialogues, the gating advantage observed in shorter conversations vanishes: all fine-tuned variants collapse to AR GAR-ours of 0.015--0.025, compared to 0.030--0.064 in the shorter evaluation. ThreadGate's advantage over LoRA-only shrinks from 1.7$\times$ (0.064 vs.\ 0.037 in the $N$\,=\,50 evaluation) to 0.64$\times$ (0.016 vs.\ 0.025), actually reversing the ordering. This reversal is not statistically robust given the small sample ($N$\,=\,5) but directionally suggests that architectural modifications provide diminishing returns as conversation length increases and exposure bias accumulates.
108	
109	\paragraph{Convergence to base.} By turn~10, all fine-tuned variants converge to within 2$\times$ of the base model's GAR, compared to 3.4$\times$ at turn~1 in the shorter evaluation. This convergence is consistent with exposure bias compounding multiplicatively over turns: each model-generated turn introduces additional distributional drift from the teacher-forced training regime, and by turn~10 the accumulated drift overwhelms any gating or LoRA signal, leaving only the base model's intrinsic attention patterns.
110	
111	\paragraph{Caveats.} The $N$\,=\,5 sample size limits statistical power, and the 10-turn conversations may differ systematically from the 3--5 turn training distribution in ways beyond length (e.g., topic complexity, user engagement patterns). We present these results as directional evidence rather than definitive conclusions.
112	
113	\begin{table}[h]
114	\centering\small
115	\caption{AR GAR-ours on $N$\,=\,5 ten-turn conversations. The gating advantage observed in Table~\ref{tab:four-way} ($N$\,=\,50, mean 3.6 turns) diminishes with conversation length.}
116	\label{tab:n5-ar}
117	\begin{tabular}{lcc}
118	\toprule
119	\textbf{Configuration} & \textbf{AR GAR-O} & \textbf{$\Delta$ vs.\ Table~\ref{tab:four-way}} \\
120	\midrule
121	Base & 0.012 & $-$0.007 \\
122	\midrule
123	ThreadGate & 0.016 & $-$0.048 \\
124	\;+\,PCGrad & 0.015 & $-$0.015 \\
125	Uniform Gate & 0.015 & $-$0.018 \\
126	LoRA-only & 0.025 & $-$0.012 \\
127	\bottomrule
128	\end{tabular}
129	\end{table}
130	
131	\section{Statistical Test Details}\label{sec:appendix-stats}
132	
133	All statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\ref{tab:stat-tests} consolidates the full results.
134	
135	\paragraph{Wilcoxon signed-rank tests.} We use paired Wilcoxon signed-rank tests for all pairwise configuration comparisons under AR evaluation, treating each conversation as a paired observation. The TG vs.\ LoRA-only comparison ($p$\,=\,0.004, $r$\,=\,0.454) confirms that turn-conditioned gating provides a statistically significant but modest improvement. The TG vs.\ +PCGrad comparison ($p$\,=\,0.002) shows that resolving gradient conflict is actively harmful. Gate turn conditioning uses an unpaired Wilcoxon test across 28 layers.
136	
137	\paragraph{Bootstrap confidence intervals.} The 95\% CIs in Table~\ref{tab:four-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.
138	
139	\paragraph{Effect sizes.} We report rank-biserial correlation $r = Z / \sqrt{N}$ as the effect size for Wilcoxon tests, where $Z$ is the standardized test statistic and $N$ is the number of observations. By standard conventions: $r < 0.3$ is small, $0.3 \leq r < 0.5$ is medium, and $r \geq 0.5$ is large. The TG vs.\ LoRA-only effect ($r$\,=\,0.454) is medium, and TG vs.\ Base ($r$\,=\,0.802) is large.
140	
141	\paragraph{Multiple comparisons.} We report uncorrected $p$-values throughout, as our comparisons are hypothesis-driven (each tests a specific causal exclusion) rather than exploratory. Applying Bonferroni correction to the 4 primary AR comparisons would adjust the significance threshold to 0.0125; all reported significant results ($p \leq 0.004$) survive this correction.
142	
143	\begin{table}[h]
144	\centering\small
145	\caption{Consolidated statistical tests. All AR comparisons use $N$\,=\,50 conversations (39 with $\geq$3 turns); gate conditioning uses 28 layers.}
146	\label{tab:stat-tests}
147	\begin{tabular}{llcc}
148	\toprule
149	\textbf{Comparison} & \textbf{Test} & $p$ & $r$ \\
150	\midrule
151	\multicolumn{4}{l}{\emph{AR GAR-ours ($\beta$\,=\,0)}} \\
152	TG vs.\ Base & Wilcoxon & $<$0.001 & 0.802 \\
153	TG vs.\ LoRA-only & Wilcoxon & 0.004 & 0.454 \\
154	TG vs.\ +PCGrad & Wilcoxon & 0.002 & --- \\
155	SS vs.\ TG & Wilcoxon & $<$0.001 & 0.869 \\
156	\midrule
157	\multicolumn{4}{l}{\emph{Gate conditioning (28 layers)}} \\
158	Turn 1 vs.\ Turn 21 & Wilcoxon & $3.7\!\times\!10^{-8}$ & 0.975 \\
159	\midrule
160	\multicolumn{4}{l}{\emph{Instruction retention}} \\
161	$\beta$\,=\,0 vs.\ $\beta$\,=\,3 & McNemar & 0.077 & --- \\
162	GAR--compliance & Pearson & 0.007 & 0.200 \\
163	\bottomrule
164	\end{tabular}
165	\end{table}
166	
167	\section{Llama-3.1-8B Complete Results}\label{sec:appendix-llama}
168	
169	Table~\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \S\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.
170	
171	\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\ 0.50).
172	
173	\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\,=\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\% for ThreadGate (mean 0.043, std 0.100), and 5\% of turn-level measurements exhibit sporadic attention spikes (GAR $\geq$ 0.4). We therefore report both mean and median.
174	
175	\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719, L24\,=\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\times$ by median for Llama vs.\ 8--17$\times$ for Qwen).
176	
177	\begin{table}[h]
178	\centering\small
179	\caption{Llama-3.1-8B-Instruct complete results. TF: teacher-forced ($N$\,=\,50); AR: autoregressive ($N$\,=\,20 for Base/TG/LoRA-only, $N$\,=\,50 for SS). Median is more representative due to heavy-tailed AR distributions (SS uses mean only).}
180	\label{tab:llama-full}
181	\resizebox{\columnwidth}{!}{%
182	\begin{tabular}{lcccc}
183	\toprule
184	& \multicolumn{2}{c}{\textbf{TF}} & \multicolumn{2}{c}{\textbf{AR}} \\
185	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
186	& GAR-O & PPL & GAR-O (mean) & GAR-O (med) \\
187	\midrule
188	Base & 0.017 & 3.45 & 0.009 & 0.009 \\
189	ThreadGate & 0.484 & 2.57 & 0.043 & 0.018 \\
190	LoRA-only & 0.481 & 2.60 & 0.028 & 0.018 \\
191	\textbf{SS} & 0.477 & 2.82 & \textbf{0.166} & --- \\
192	\bottomrule
193	\end{tabular}}
194	\end{table}
195	
196	\begin{figure}[t]
197	  \centering
198	  \includegraphics[width=\columnwidth]{fig_crossmodel.pdf}
199	  \caption{Cross-architecture validation. (a)~The TF-AR gap persists on Llama-3.1-8B (27$\times$ by median), exceeding Qwen's 8$\times$. (b)~Gate profiles on normalized depth: Qwen dips at early layers, Llama at late layers; architecture-dependent patterns, but both converge toward identity.}
200	  \label{fig:crossmodel}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21066833-e12e-4211-a484-953999e9b1c7",
  "isSidechain": true,
  "promptId": "a3e6062b-fe39-400b-a5a8-e5805ce60227",
  "agentId": "a56f1deb740d009c5",
  "type": "user",
  "uuid": "db99a53c-383c-4bbb-ab3b-49157b08cb98",
  "sourceToolAssistantUUID": "21066833-e12e-4211-a484-953999e9b1c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-24T18:25:17.218Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AW6D3KKUkf9oWVZGM2R3bK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 200,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db99a53c-383c-4bbb-ab3b-49157b08cb98",
  "isSidechain": true,
  "agentId": "a56f1deb740d009c5",
  "requestId": "req_011CbMs1JWMFP2BUcGsWicGR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82777a22-688c-42be-98a1-9904468f544a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjVWpr6TgXuyQEyDm9AJZC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6163,
      "cache_read_input_tokens": 48463,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6163
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 48463,
          "cache_creation_input_tokens": 6163,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6163,
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

_source line 26 · 2026-05-24T18:25:17.242Z_

<details><summary>↩ Tool result · `toolu_01AW6D3KKUkf9oWVZGM2R3bK`</summary>

```text
200	  \label{fig:crossmodel}
201	\end{figure}
202	
203	\paragraph{Cross-model summary.} Table~\ref{tab:crossmodel-detail} consolidates the cross-model comparison, showing TF GAR, AR GAR, PPL, and gap ratios side by side for both architectures. The consistent pattern---TF GAR $\approx$ 0.5, AR GAR $\ll$ 0.1, gap $\geq$ 7.9$\times$---across two architectures with different layer counts, attention head configurations, and pre-training corpora provides strong evidence that exposure bias is architecture-independent. Notably, Llama's larger gaps (11.2--17.2$\times$ vs.\ 7.9--13.5$\times$) may reflect its deeper architecture (32 vs.\ 28 layers), which allows more layers for distributional drift to compound through.
204	
205	\input{../artifacts/appendix_expansion/tab_crossmodel_detail.tex}
206	
207	\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\times$), compared to 1.28$\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.
208	
209	\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\% longer than Qwen due to Llama's larger layer count (32 vs.\ 28 layers).
210	
211	\paragraph{Phase 1 diagnostics.} Before fine-tuning, we confirmed that Llama exhibits the same goal attention decay as Qwen. Base model GAR decays from 0.026 (turn 1) to 0.003 (turn 10), a 90\% decline. This is steeper than Qwen's 70.8\% decline, suggesting that attention decay may be more severe in Llama's architecture despite its larger head count (32 vs.\ 28 KV heads).
212	
213	\paragraph{Cross-model gradient analysis.} Table~\ref{tab:gradient-crossmodel} compares NTP--GAR gradient interaction between the two architectures. Both models exhibit near-orthogonal gradients (cosine similarity $\approx$\,0), not systematic conflict: Qwen shows a slight negative mean ($-$0.042) while Llama is marginally positive (+0.005). NTP gradients dominate GAR by 14.7$\times$ on Qwen and 25.7$\times$ on Llama, indicating that the auxiliary signal is overwhelmed by magnitude rather than opposed by direction. The cross-model consistency---near-zero cosine similarity and order-of-magnitude NTP dominance on both architectures---reinforces the \emph{modus tollens} argument (\S\ref{subsec:pcgrad}): gradient conflict is not the root cause of the TF-AR gap.
214	
215	\begin{table}[h]
216	\centering\small
217	\caption{Cross-model NTP--GAR gradient interaction. Gradients are near-orthogonal on both architectures; NTP magnitude dominates GAR by 15--26$\times$.}
218	\label{tab:gradient-crossmodel}
219	\begin{tabular}{lcc}
220	\toprule
221	\textbf{Metric} & \textbf{Qwen-7B} & \textbf{Llama-8B} \\
222	\midrule
223	Mean cos sim & $-$0.042 & +0.005 \\
224	Neg-layer \% & 67.9\% & 53.1\% \\
225	NTP/GAR mag ratio & 14.7$\times$ & 25.7$\times$ \\
226	\bottomrule
227	\end{tabular}
228	\end{table}
229	
230	\section{Additional Visualizations}\label{sec:appendix-viz}
231	
232	This section presents extended visualizations referenced in the main text. Each figure examines a different aspect of the gating behavior and its failure under autoregressive generation.
233	
234	\subsection{Gate Profile Heatmap}
235	
236	Figure~\ref{fig:gate-heatmap} shows the per-layer gate values across all training configurations for both Qwen-2.5-7B (28 layers) and Llama-3.1-8B (32 layers). The key observation is that early layers consistently receive the lowest gate values across all conditions, suggesting that these layers contribute more dispensable computations for the NTP objective. The pattern is remarkably consistent across ThreadGate, Uniform Gate, and PCGrad variants, indicating that gate-value allocation is driven primarily by the NTP loss landscape rather than the GAR auxiliary objective.
237	
238	\begin{figure*}[h]
239	\centering
240	\includegraphics[width=0.95\textwidth]{fig_gate_profile_heatmap.pdf}
241	\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\times$ 5 conditions) and Llama-3.1-8B (32 layers $\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}
242	\label{fig:gate-heatmap}
243	\end{figure*}
244	
245	\subsection{Cross-Model Gate Profile Comparison}
246	
247	Figure~\ref{fig:gate-crossmodel} compares gate profiles between the two architectures. Qwen-2.5-7B shows minimum gate values at early layers (L1\,=\,0.793, L5\,=\,0.797), suggesting these layers are most amenable to attenuation without disrupting NTP. Llama-3.1-8B instead shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719), indicating that architecturally distinct models learn different layer-importance hierarchies. Both profiles converge toward identity at their respective final layers, consistent with NTP gradient pressure dominating gate optimization at output-adjacent layers.
248	
249	\begin{figure*}[h]
250	\centering
251	\includegraphics[width=0.95\textwidth]{fig_gate_profile_crossmodel.pdf}
252	\caption{Side-by-side gate profiles for Qwen-2.5-7B and Llama-3.1-8B. Qwen dips at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719). Both models learn layer-selective gating but with architecture-dependent patterns.}
253	\label{fig:gate-crossmodel}
254	\end{figure*}
255	
256	\subsection{Per-Turn AR GAR Decay}
257	
258	Figure~\ref{fig:ar-gar-perturn} visualizes the monotonic decay of GAR across conversation turns under autoregressive generation. Qwen base drops 85\% from turn 1 to turn 10; Llama base drops 90\%. The ThreadGate-trained model shows slight elevation in absolute GAR values but follows the same decay pattern, confirming that training-time GAR optimization does not alter the fundamental decay dynamic during generation. This per-turn view complements the aggregate TF-AR gap reported in Table~\ref{tab:four-way}: the gap is not a fixed offset but grows with conversation length, consistent with cumulative exposure bias.
259	
260	\begin{figure*}[h]
261	\centering
262	\includegraphics[width=0.95\textwidth]{fig_ar_gar_perturn.pdf}
263	\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\% (turn 1$\to$10), Llama base drops 90\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}
264	\label{fig:ar-gar-perturn}
265	\end{figure*}
266	
267	\subsection{Bootstrap Confidence Intervals}
268	
269	Figure~\ref{fig:bootstrap-ci} shows the bootstrap resampling distributions underlying the 95\% CIs reported in Table~\ref{tab:four-way}.
270	
271	\begin{figure}[h]
272	  \centering
273	  \includegraphics[width=\columnwidth]{fig_bootstrap_ci.pdf}
274	  \caption{Bootstrap CI distributions for AR GAR-ours (ThreadGate vs.\ LoRA-only, $N$\,=\,50, 10K resamples). Distributions overlap substantially, consistent with the modest effect size ($r$\,=\,0.454).}
275	  \label{fig:bootstrap-ci}
276	\end{figure}
277	
278	\subsection{Gate Value Distributions}
279	
280	Figure~\ref{fig:gate-distribution} shows the full distribution of per-layer gate values for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\sim$0.94--0.96, concentrated between 0.9 and 1.0), confirming that the gating mechanism provides minimal modulation regardless of the specific variant. The distributions are right-skewed with a sharp cutoff at 1.0, reflecting NTP pressure pushing gates toward identity.
281	
282	\begin{figure*}[h]
283	\centering
284	\includegraphics[width=0.95\textwidth]{fig_gate_distribution.pdf}
285	\caption{Per-layer gate value distributions for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\sim$0.94--0.96), confirming minimal modulation from the gating mechanism.}
286	\label{fig:gate-distribution}
287	\end{figure*}
288	
289	\subsection{Training Loss Curves}
290	
291	Figure~\ref{fig:training-loss} shows the NTP, GAR, and total loss trajectories during training. GAR loss collapses to near-zero within the first epoch across all variants, indicating rapid convergence of the auxiliary objective under teacher forcing. NTP loss converges normally to ${\sim}$0.93 by epoch 3. The fast GAR convergence is not itself pathological---it indicates successful optimization under the training distribution. The pathology emerges only at the transition to autoregressive generation, where the learned attention patterns fail to transfer.
292	
293	\begin{figure*}[h]
294	\centering
295	\includegraphics[width=0.95\textwidth]{fig_training_loss_curves.pdf}
296	\caption{NTP, GAR, and total loss trajectories. GAR loss collapses to near-zero within the first epoch across all variants, while NTP loss converges normally.}
297	\label{fig:training-loss}
298	\end{figure*}
299	
300	\subsection{Full Attention Steering Results}\label{sec:appendix-steering}
301	
302	\begin{table*}[t]
303	\centering\small
304	\caption{Full attention steering results across evaluation settings.
305	\textbf{Bold} indicates the operating point cited in the main text ($\beta$\,=\,5).
306	A visual gap separates the phase-transition boundary: GAR jumps sharply between $\beta$\,=\,2 and $\beta$\,=\,3 across all settings.}
307	\label{tab:steering-full}
308	\begin{tabular}{r cc cc cc}
309	\toprule
310	 & \multicolumn{2}{c}{\textbf{$N$\,=\,5, Gen}} & \multicolumn{2}{c}{\textbf{$N$\,=\,50, Gen}} & \multicolumn{2}{c}{\textbf{$N$\,=\,200, TF}} \\
311	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
312	$\beta$ & GAR & PPL & GAR & PPL & GAR & PPL \\
313	\midrule
314	0   & .028 & 1.41 & $.064 \pm .081$ & $1.43 \pm .10$ & .535 & 2.62 \\
315	0.5 & .029 & 1.39 & ---             & ---             & ---  & ---  \\
316	1   & .035 & 1.36 & ---             & ---             & ---  & ---  \\
317	2   & .062 & 1.41 & $.128 \pm .110$ & $1.48 \pm .14$ & .611 & 2.69 \\
318	\addlinespace[3pt]
319	3   & ---  & ---  & $.556 \pm .060$ & $1.56 \pm .17$ & .788 & 2.93 \\
320	4   & ---  & ---  & $.644 \pm .061$ & $1.67 \pm .22$ & .817 & 3.49 \\
321	\textbf{5}  & \textbf{.680} & \textbf{1.91} & $\mathbf{.727 \pm .061}$ & $\mathbf{1.77 \pm .27}$ & \textbf{.833} & \textbf{6.15} \\
322	10  & .959 & 4.22 & $.961 \pm .015$ & $3.45 \pm 1.78$ & .977 & 505.2 \\
323	\bottomrule
324	\end{tabular}
325	\end{table*}
326	
327	\begin{figure}[h]
328	  \centering
329	  \includegraphics[width=\columnwidth]{fig_steering_standalone.pdf}
330	  \caption{Detailed $\beta$-steering trade-off ($N$\,=\,50). GAR-ours (top) increases monotonically with $\beta$; PPL (bottom) remains stable below $\beta$\,=\,3 (9\% cost), then rises sharply. The $\beta$\,=\,3 operating point (circled) achieves 8.7$\times$ GAR recovery while crossing the TF baseline, representing the optimal trade-off.}
331	  \label{fig:steering-standalone}
332	\end{figure}
333	
334	\section{Per-Layer Gate Profile}\label{sec:appendix-gate-profile}
335	
336	Table~\ref{tab:gate-profile} reports the final per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct (28 layers). Gate values are averaged across all tokens in the evaluation set. Layers 1 and 5 show the lowest gate values (0.793 and 0.797), indicating these layers are most amenable to attenuation without disrupting NTP. Layers 26--27 converge to $\geq$0.988, consistent with NTP gradient pressure dominating at output-adjacent layers. The mean across all layers is 0.947 ($\sigma$\,=\,0.051).
337	
338	\begin{table}[h]
339	\centering\small
340	\caption{Per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct. Min values (L1, L5) in bold.}
341	\label{tab:gate-profile}
342	\resizebox{\columnwidth}{!}{%
343	\begin{tabular}{cccccccc}
344	\toprule
345	L0 & L1 & L2 & L3 & L4 & L5 & L6 & L7 \\
346	.883 & \textbf{.793} & .996 & .988 & .984 & \textbf{.797} & .961 & .918 \\
347	\midrule
348	L8 & L9 & L10 & L11 & L12 & L13 & L14 & L15 \\
349	.965 & .934 & .969 & .918 & .926 & .941 & .930 & .965 \\
350	\midrule
351	L16 & L17 & L18 & L19 & L20 & L21 & L22 & L23 \\
352	.941 & .910 & .961 & .965 & .973 & .988 & .969 & .980 \\
353	\midrule
354	L24 & L25 & L26 & L27 & \multicolumn{4}{c}{Summary} \\
355	.980 & .984 & .988 & 1.00 & \multicolumn{4}{c}{$\bar{g}$\,=\,.947, $\sigma$\,=\,.051} \\
356	\bottomrule
357	\end{tabular}}
358	\end{table}
359	
360	The gate profile exhibits two notable patterns: (1)~a bimodal dip at L1 and L5, suggesting two distinct ``dispensable'' layer clusters in Qwen's architecture; (2)~monotonic increase from L17 to L27, indicating output-adjacent layers are progressively more critical for NTP. Seed 42 produces a similar profile (mean 0.934, min at L3--L5), confirming the pattern is not seed-dependent.
361	
362	\paragraph{Cross-model comparison.} See \S\ref{sec:appendix-viz} for the full cross-model gate profile comparison (Figure~\ref{fig:gate-crossmodel}). Llama-3.1-8B shows a qualitatively different profile---a V-shaped valley at mid-to-late layers rather than early-layer dips---suggesting architecture-dependent layer importance hierarchies.
363	
364	\section{Scheduled Sampling Implementation}\label{sec:appendix-ss}
365	
366	Our scheduled sampling implementation follows \citet{bengio2015scheduled} with modifications for multi-turn transformer training:
367	
368	\paragraph{Sampling schedule.} The model-generated context ratio $\rho$ increases linearly from 0 to 0.3 over 3 epochs. At each training step, a Bernoulli trial with probability $\rho$ determines whether the input prefix is replaced with model-generated tokens. The effective usage rate (29.7--37.1\%) is lower than the nominal schedule due to per-sample Bernoulli variance.
369	
370	\paragraph{Context generation.} When model-generated context is selected, the model autoregressively generates the assistant turns from the conversation prefix up to the current training position. The generated tokens replace the ground-truth assistant tokens in the input, while user turns remain unchanged. This preserves the multi-turn structure while introducing distributional diversity in the conditioning context.
371	
372	\paragraph{Training dynamics.} The scheduled sampling variant converges to similar final loss (NTP 0.932 vs.\ 0.930 for standard ThreadGate) but with higher variance in early epochs due to the stochastic context mixing (Figure~\ref{fig:ss-dynamics}). Gate profiles remain similar (mean 0.953 vs.\ 0.947, min at L4 vs.\ L1), indicating that scheduled sampling does not fundamentally alter gate optimization but rather improves the robustness of the learned attention patterns to distributional shift. Training time increases by 8--80\% across seeds (seed-dependent; dominated by GAR forward pass overhead): 6.5h (seed 42), 10.8h (seed 123), and 6.5h (seed 456) vs.\ 6.0h for standard ThreadGate on Qwen. Seed 456 exhibits consistent training dynamics with seeds 42 and 123.
373	
374	\begin{figure}[h]
375	  \centering
376	  \includegraphics[width=\columnwidth]{fig_ss_training_dynamics.pdf}
377	  \caption{Scheduled sampling training dynamics: sampling ratio $\rho$ ramps linearly from 0 to 0.3 (left axis); GAR loss (right axis) shows higher early-epoch variance due to stochastic context mixing.}
378	  \label{fig:ss-dynamics}
379	\end{figure}
380	
381	\section{Computational Cost Analysis}\label{sec:appendix-cost}
382	
383	\begin{table}[h]
384	\centering\small
385	\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (96\,GB VRAM).}
386	\label{tab:cost}
387	\resizebox{\columnwidth}{!}{%
388	\begin{tabular}{lcccc}
389	\toprule
390	\textbf{Config} & \textbf{Params} & \textbf{Time (h)} & \textbf{VRAM} & \textbf{Overhead} \\
391	\midrule
392	\multicolumn{5}{l}{\emph{Qwen-2.5-7B-Instruct}} \\
393	LoRA-only & 4.2M & 6.0 & 42\,GB & baseline \\
394	ThreadGate & 4.3M & 6.0 & 43\,GB & $+$57K \\
395	\;+\,PCGrad & 4.3M & 8.0 & 43\,GB & $+$33\% \\
396	Uniform Gate & 4.3M & 6.0 & 43\,GB & $+$57K \\
397	SS (s42) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
398	SS (s123) & 4.3M & 10.8 & 43\,GB & $+$80\% \\
399	SS (s456) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82777a22-688c-42be-98a1-9904468f544a",
  "isSidechain": true,
  "promptId": "a3e6062b-fe39-400b-a5a8-e5805ce60227",
  "agentId": "a56f1deb740d009c5",
  "type": "user",
  "uuid": "88a455f0-c351-49c3-a2b4-c3a75eb59408",
  "sourceToolAssistantUUID": "82777a22-688c-42be-98a1-9904468f544a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-24T18:25:22.701Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A4atepxHs6Kn79YBHnu4qF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 399,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88a455f0-c351-49c3-a2b4-c3a75eb59408",
  "isSidechain": true,
  "agentId": "a56f1deb740d009c5",
  "requestId": "req_011CbMs1dEUhXy8yFNb82tvW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cce0045f-c9e4-4b7c-979d-14c9f26e2fc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPCSyroSe9SrjFPQUUFmu9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5899,
      "cache_read_input_tokens": 54626,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5899
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 54626,
          "cache_creation_input_tokens": 5899,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5899,
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

_source line 28 · 2026-05-24T18:25:22.710Z_

<details><summary>↩ Tool result · `toolu_01A4atepxHs6Kn79YBHnu4qF`</summary>

```text
399	SS (s456) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
400	\midrule
401	\multicolumn{5}{l}{\emph{Llama-3.1-8B-Instruct}} \\
402	LoRA-only & 4.2M & 7.0 & 45\,GB & baseline \\
403	ThreadGate & 4.3M & 7.3 & 46\,GB & $+$65K \\
404	\bottomrule
405	\end{tabular}}
406	\end{table}
407	
408	\paragraph{Parameter overhead.} ThreadGate adds ${\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\times$ 2K per gate MLP) and ${\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.
409	
410	\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 6.0--7.3 hours. PCGrad adds ${\sim}$33\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\% (6.5h) due to efficient batched generation, while seed 123 adds 80\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.
411	
412	\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\to$64$\to$1 MLP forward pass per layer adds $<$0.1\% latency. $\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.
413	
414	\section{Qualitative Steering Examples}\label{sec:appendix-examples}
415	
416	Table~\ref{tab:examples} illustrates the effect of $\beta$-steering on model behavior in a 4-turn conversation where the system prompt instructs ``Always respond in exactly three bullet points.''
417	
418	\begin{table*}[h]
419	\centering\small
420	\caption{Qualitative effect of $\beta$-steering on instruction following across conversation turns. System prompt: ``Always respond in exactly three bullet points.'' ThreadGate checkpoint, 4-turn conversation.}
421	\label{tab:examples}
422	\begin{tabular}{c p{5.5cm} p{5.5cm}}
423	\toprule
424	\textbf{Turn} & \textbf{$\beta$\,=\,0 (unsteered)} & \textbf{$\beta$\,=\,3 (steered)} \\
425	\midrule
426	1 & \checkmark~Three bullet points, on-topic & \checkmark~Three bullet points, on-topic \\
427	2 & \checkmark~Three bullet points, relevant & \checkmark~Three bullet points, relevant \\
428	3 & $\sim$~Four bullet points, partially on-topic & \checkmark~Three bullet points, on-topic \\
429	4 & \texttimes~Free-form paragraph, no bullets & \checkmark~Three bullet points, on-topic \\
430	\bottomrule
431	\end{tabular}
432	\end{table*}
433	
434	The pattern is consistent with the GAR decay analysis (\S\ref{sec:analysis}): unsteered models progressively lose attention to the system-prompt constraint, leading to format violations at later turns. Steering maintains goal-token attention, preserving instruction compliance. The per-category breakdown in Table~\ref{tab:ir-results} shows that content constraints benefit most from this effect.
435	
436	\section{Gradient Conflict Analysis}\label{sec:appendix-gradient}
437	
438	\begin{figure}[t]
439	  \centering
440	  \includegraphics[width=\columnwidth,height=0.42\textheight,keepaspectratio]{fig2_training_pcgrad.pdf}
441	  \caption{(a)~Training GAR convergence to target ($\tau$\,=\,0.5). (b)~PCGrad eliminates gradient direction conflict but $\mathcal{L}_\text{GAR}$ still collapses, confirming that direction conflict is not the cause (\S\ref{subsec:pcgrad}).}
442	  \label{fig:training-pcgrad}
443	\end{figure}
444	
445	This section provides extended gradient interaction analysis supporting the PCGrad exclusion argument in \S\ref{subsec:pcgrad}. We measure per-layer cosine similarity between NTP and GAR gradients, gradient magnitude ratios, and the effect of PCGrad projection on these quantities.
446	
447	\paragraph{Gradient direction analysis.} Figure~\ref{fig:gradient-heatmap} visualizes the per-layer cosine similarity between NTP and GAR gradients across training epochs for both standard ThreadGate (v7) and PCGrad (v9) training. Under standard training, 79\% of layers show negative cosine similarity (gradient conflict) at epoch~0, declining to 68\% by epoch~2 as GAR loss converges to near-zero. This decline reflects diminishing GAR gradient magnitude rather than alignment improvement---as GAR loss approaches zero, the GAR gradient shrinks proportionally, making cosine similarity measurements less reliable (small gradients produce noisy direction estimates). Under PCGrad training, the conflict percentage decreases more slowly (79\%$\to$71\%), consistent with PCGrad projecting conflicting gradients onto the other's normal plane but not eliminating the underlying directional opposition.
448	
449	\paragraph{Spatial patterns.} The early layers (L0--L5) and output-adjacent layers (L24--L27) show the strongest conflict, corresponding to the layers where gate values deviate most from identity (Figure~\ref{fig:gate-heatmap}). This spatial correlation is not causal: eliminating directional conflict via PCGrad does not improve AR GAR, and gates at high-conflict layers are not systematically different from gates at low-conflict layers (Spearman $\rho$\,=\,$-$0.12, $p$\,=\,0.54 between gate value and conflict magnitude).
450	
451	\paragraph{Magnitude dominance.} NTP gradient magnitude dominates GAR by 7.5$\times$ at epoch~0 and 14.7$\times$ by epoch~2, as GAR loss converges while NTP loss remains at $\sim$0.93. This growing dominance means that even when directions oppose, the effective update direction is determined almost entirely by NTP. PCGrad addresses directional conflict but does not address magnitude dominance---it projects conflicting gradients onto the other's normal plane (changing direction) but preserves relative magnitudes. The 7.5--14.7$\times$ magnitude ratio means that even after PCGrad projection, GAR contributes $<$7\% of the effective update magnitude, explaining why PCGrad is ineffective.
452	
453	\paragraph{Cross-model consistency.} Table~\ref{tab:gradient-crossmodel} confirms the pattern on Llama-3.1-8B: gradients are near-orthogonal (mean cosine $+$0.005, essentially zero) rather than systematically conflicting, with 25.7$\times$ NTP dominance. The Llama result is particularly informative because it shows that even without systematic directional conflict (53\% negative layers, near chance), the same TF-AR gap persists. This cross-model evidence strengthens the \textit{modus tollens} argument: if gradient conflict were the cause, it should be present on both architectures; it is absent on Llama, yet the gap persists; therefore gradient conflict is not the cause.
454	
455	\begin{figure*}[h]
456	\centering
457	\includegraphics[width=0.95\textwidth]{fig_gradient_conflict_heatmap.pdf}
458	\caption{Per-layer cosine similarity between NTP and GAR gradients across training epochs. (a)~Standard training: conflict decreases from 79\% to 68\% of layers as GAR loss vanishes. (b)~PCGrad training: projection reduces conflict more slowly (79\%$\to$71\%) but does not improve AR GAR, ruling out directional conflict as the cause (\S\ref{subsec:pcgrad}).}
459	\label{fig:gradient-heatmap}
460	\end{figure*}
461	
462	\section{Training Data Characteristics}\label{sec:appendix-data}
463	
464	All experiments use 8,000 multi-turn conversations sampled from the UltraChat \citep{ding2023ultrachat} training split. Table~\ref{tab:data-stats} summarizes the dataset characteristics. Conversations are truncated to 2,048 tokens; conversations shorter than 3 user turns are excluded to ensure sufficient multi-turn structure for GAR computation. The held-out evaluation sets use separate non-overlapping samples: $N$\,=\,50 conversations (mean 3.6 user turns) for the primary AR evaluation and $N$\,=\,5 conversations (10 turns each) for the long-conversation analysis (Appendix~\ref{sec:appendix-n5}).
465	
466	\begin{table}[h]
467	\centering\small
468	\caption{Training and evaluation data characteristics. All data from UltraChat \citep{ding2023ultrachat}.}
469	\label{tab:data-stats}
470	\begin{tabular}{lcc}
471	\toprule
472	\textbf{Property} & \textbf{Train} & \textbf{Eval (primary)} \\
473	\midrule
474	Conversations & 8,000 & 50 \\
475	Min user turns & 3 & 3 \\
476	Max sequence length & 2,048 & 2,048 \\
477	Source & UltraChat train & UltraChat train \\
478	Overlap & --- & non-overlapping \\
479	\bottomrule
480	\end{tabular}
481	\end{table}
482	
483	\section{Exposure Bias Scaling}\label{sec:appendix-eb-scaling}
484	
485	Figure~\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).
486	
487	\paragraph{Cross-variant gaps.} On Qwen, ThreadGate achieves the smallest gap among standard variants (7.8$\times$) while PCGrad shows the largest (16.7$\times$, consistent with its counterproductive effect on AR GAR). Scheduled sampling reduces the gap to ${\sim}$1.3$\times$, the only variant approaching parity. The ordering of gap ratios (SS $\ll$ TG $<$ LoRA $<$ UG $<$ PCGrad) differs from the ordering of TF GAR (all $\approx$ 0.50), confirming that training-time optimization success does not predict inference-time robustness. On Llama, both ThreadGate and LoRA-only show $\sim$27$\times$ gaps (by median), larger than any Qwen variant. The consistently larger Llama gaps may reflect its deeper architecture (32 vs.\ 28 layers), which provides more layers for distributional drift to compound through.
488	
489	\paragraph{Length-dependent compounding.} Panel~(b) shows that the gap compounds with conversation length: at 3.6 mean turns ($N$\,=\,50), ThreadGate's gap is 8$\times$; at 10 turns ($N$\,=\,5), it widens to 31$\times$. The relationship is approximately linear in the number of turns on a log scale, suggesting that the per-turn drift contribution is roughly multiplicative. Extrapolating this trend suggests that at 20 turns the gap would exceed 100$\times$, making any training-time attention signal essentially undetectable. This length dependence is consistent with cumulative distributional drift---each model-generated turn introduces additional divergence from the teacher-forced training distribution, and by turn~10 the accumulated drift overwhelms any gating signal.
490	
491	\paragraph{Implications for deployment.} These scaling results have practical implications: (1)~for applications requiring sustained attention over many turns (e.g., long-form tutoring, multi-step reasoning), architectural modifications alone are insufficient---distributional robustification or inference-time intervention is necessary; (2)~the near-parity of scheduled sampling (${\sim}$1.3$\times$ gap) suggests that bridging the training-inference distribution gap is both necessary and sufficient for maintaining attention; (3)~the $\beta$-steering approach provides a complementary inference-time solution, but its effectiveness also depends on conversation length (Appendix~\ref{sec:appendix-steering-viz}).
492	
493	\begin{figure*}[h]
494	\centering
495	\includegraphics[width=0.95\textwidth]{fig_eb_scaling.pdf}
496	\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\sim}$1.3$\times$) is the only variant near parity. Llama gaps ($\sim$27$\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\times$ (3.6 turns) to 31$\times$ (10 turns).}
497	\label{fig:eb-scaling}
498	\end{figure*}
499	
500	\section{Per-Turn AR GAR Dynamics}\label{sec:appendix-ar-gar-dynamics}
501	
502	To characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.
503	
504	All six configurations exhibit monotonic GAR decay as turn index increases, consistent with cumulative exposure bias eroding attention to goal tokens. The decay rate varies substantially: Scheduled Sampling retains by far the highest mid-turn GAR (0.423), followed distantly by ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), and Base (0.019). Base decays most rapidly, losing the majority of its initial GAR within the first few turns. The large SS--TG gap mirrors Table~\ref{tab:four-way} and confirms that distributional robustification---not gating architecture alone---is the primary driver of AR GAR retention.\footnote{SS configuration uses seed 123 data; all other configurations use seed 42. Cross-seed trends are consistent (\S\ref{subsec:ss}).}
505	
506	\begin{figure}[t]
507	\centering
508	\includegraphics[width=\columnwidth]{fig_kl_ar_gar_curves.pdf}
509	\caption{Per-turn AR GAR trajectories for six Qwen-2.5-7B configurations (turns 1--5). All models show monotonic decay; Scheduled Sampling retains far higher GAR throughout (0.53$\to$0.39), while the remaining five variants cluster below 0.13 and decay rapidly.}
510	\label{fig:kl_ar_gar_curves}
511	\end{figure}
512	
513	\begin{figure}[t]
514	\centering
515	\includegraphics[width=\columnwidth]{fig_kl_ar_gar_bar.pdf}
516	\caption{Mid-turn AR GAR comparison across six training configurations. Ranking from highest to lowest: Scheduled Sampling (0.423), ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), Base (0.019).}
517	\label{fig:kl_ar_gar_bar}
518	\end{figure}
519	
520	This pattern contrasts with teacher-forced evaluation, where GAR remains relatively stable across turns for all configurations. Under teacher forcing, the model conditions on ground-truth context at each turn, preventing the distributional drift that causes GAR erosion in AR mode. The divergence between TF stability and AR decay provides turn-level evidence for the exposure bias mechanism described in \S\ref{sec:analysis}: training-time attention patterns are optimized for a distribution that AR generation progressively departs from.
521	
522	\section{Per-Head KL Divergence Analysis}\label{sec:appendix-kl}
523	
524	To test whether exposure bias selectively disrupts goal-attending heads rather than uniformly affecting all attention patterns, we compute per-head TF vs.\ AR attention divergence on 30 held-out conversations. For each of the 28 attention heads per layer (784 heads total), we measure the KL divergence $D_\text{KL}(p_\text{TF} \| p_\text{AR})$ between teacher-forced and autoregressive attention distributions, and the absolute GAR shift $\Delta\text{GAR} = |\text{GAR}_\text{TF} - \text{GAR}_\text{AR}|$. This head-level analysis provides mechanistic evidence for the exposure bias interpretation beyond the aggregate TF-AR gap.
525	
526	\begin{table}[h]
527	\centering\small
528	\caption{Per-head TF-AR divergence statistics for Base and ThreadGate (Qwen-2.5-7B, 30 conversations). TG trains more concentrated goal attention under TF, but these high-GAR heads shift most under AR ($r$\,=\,0.743).}
529	\label{tab:kl-perhead}
530	\begin{tabular}{lcc}
531	\toprule
532	\textbf{Metric} & \textbf{Base} & \textbf{TG v7} \\
533	\midrule
534	Mean $\Delta$GAR & 0.012 & 0.016 \\
535	Mean KL & 0.043 & 0.054 \\
536	Corr(TF\_GAR, $\Delta$GAR) & 0.673 & 0.743 \\
537	\bottomrule
538	\end{tabular}
539	\end{table}
540	
541	\paragraph{Selective disruption.} ThreadGate exhibits 35\% larger mean $\Delta$GAR (0.016 vs.\ 0.012) and 26\% larger mean KL (0.054 vs.\ 0.043) than Base. This is counterintuitive: the auxiliary GAR loss successfully trains more concentrated goal attention (higher TF GAR per head), but these very same heads shift more under AR generation. The correlation between per-head TF GAR and $\Delta$GAR is strong for both models ($r$\,=\,0.673 for Base, 0.743 for TG), confirming that heads with higher goal attention under teacher forcing are disproportionately disrupted under autoregressive generation. This selectivity is a hallmark of exposure bias: the training-time optimization succeeds at creating a specific attention pattern (concentrated goal attention), but precisely this pattern has no autoregressive counterpart because it depends on conditioning on ground-truth context.
542	
543	\paragraph{Layer-depth dependence.} The highest-KL heads concentrate at output-adjacent layers (L23--L27, KL\,$>$\,0.077) and L9 (KL\,$\approx$\,0.068). Output-adjacent layers participate most directly in next-token prediction, so their attention distributions are most sensitive to changes in the conditioning context. L9's elevated KL may reflect a ``routing layer'' phenomenon observed in multi-layer transformers, where specific intermediate layers specialize in long-range information routing. The depth dependence is consistent with cumulative error propagation: distributional drift from model-generated tokens accumulates as information flows through successive layers, producing the largest attention shifts at the deepest layers.
544	
545	\paragraph{Gate--KL independence.} Gate magnitude does not predict per-layer exposure bias severity: Spearman correlation between gate value and per-layer KL is 0.061 ($p$\,=\,0.757). The highest KL values concentrate at deep layers (L22--L27) where gates are near identity ($\approx$1.0), while the lowest-gate layers show below-average KL (0.041 vs.\ 0.056 for highest-gate layers). This independence confirms that the gating mechanism and the exposure bias phenomenon operate on different axes: gates modulate the magnitude of residual contributions, while exposure bias disrupts the direction (attention distribution) of those contributions. Even a ``perfect'' gate that could fully attenuate certain layers' residuals would not address the fundamental distributional mismatch that causes the attention shift.
546	
547	\section{GAR Definition Robustness}\label{sec:appendix-gar-robust}
548	
549	To assess whether our conclusions depend on the specific GAR definition, we evaluate four alternative token-position variants on 50 held-out conversations (Table~\ref{tab:gar-robust}): (1)~\emph{ours} (last-token): attention from the last token to goal tokens (standard GAR-ours); (2)~\emph{all-token}: average attention from all tokens to goal tokens; (3)~\emph{first-token}: attention from the first assistant token to goal tokens; (4)~\emph{goal-only}: attention from the last token to system-prompt-only tokens (excluding conversation content).
550	
551	\begin{table}[h]
552	\centering\small
553	\caption{Mid-turn GAR under four alternative definitions ($N$\,=\,50 conversations). ThreadGate only improves query-position-specific definitions (last-token, goal-only); Scheduled Sampling raises all four definitions above 0.36.}
554	\label{tab:gar-robust}
555	\begin{tabular}{lccc}
556	\toprule
557	\textbf{Definition} & \textbf{Base} & \textbf{TG} & \textbf{SS} \\
558	\midrule
559	Ours (last-token) & 0.015 & \textbf{0.325} & \textbf{0.458} \\
560	All-token & 0.015 & 0.025 & \textbf{0.366} \\
561	First-token & 0.022 & 0.039 & \textbf{0.412} \\
562	Goal-only & 0.005 & \textbf{0.310} & \textbf{0.444} \\
563	\bottomrule
564	\end{tabular}
565	\end{table}
566	
567	ThreadGate improvements are query-position-specific: the two definitions using the last token as query (ours: $0.015 \to 0.325$; goal-only: $0.005 \to 0.310$) show large gains, while all-token ($0.025$) and first-token ($0.039$) remain near base levels. This is expected: the GAR loss optimizes attention at the last-token position, so the learned routing does not generalize to other query positions.
568	
569	Scheduled Sampling raises all four definitions above 0.36, with no definition falling below Base-relative gains. This confirms that SS builds a broad goal-attention pattern across token positions, rather than overfitting to the specific position targeted by the GAR loss. The pattern holds regardless of GAR definition: both the exposure bias diagnosis and the SS mitigation are robust to metric choice.
570	
571	\section{General Capability Preservation (MMLU)}\label{sec:appendix-mmlu}
572	
573	To confirm that auxiliary GAR losses and attention steering do not degrade general language understanding, we evaluate all six Qwen-2.5-7B variants on MMLU 5-shot \citep{hendrycks2021measuring} ($N$\,=\,14{,}042 questions).
574	
575	\begin{table}[h]
576	\centering\small
577	\caption{MMLU 5-shot accuracy on Qwen-2.5-7B-Instruct. All fine-tuned variants remain within 0.8\,pp of the base LoRA-only checkpoint.}
578	\label{tab:mmlu}
579	\begin{tabular}{lcc}
580	\toprule
581	\textbf{Model} & \textbf{Acc (\%)} & \textbf{$\Delta$ vs Base} \\
582	\midrule
583	Base (LoRA-only) & 74.23 & --- \\
584	PCGrad (v9) & 73.86 & $-$0.38 \\
585	SS (v8b) & 73.75 & $-$0.48 \\
586	LoRA-only & 73.57 & $-$0.66 \\
587	ThreadGate (v7) & 73.47 & $-$0.77 \\
588	Uniform Gate & 73.46 & $-$0.78 \\
589	\bottomrule
590	\end{tabular}
591	\end{table}
592	
593	All variants degrade by $<$0.8\,pp, confirming that attention steering and auxiliary GAR losses do not harm general language understanding. The ordering does not track GAR performance (e.g., PCGrad shows the smallest MMLU drop despite the worst AR GAR), consistent with GAR and NTP occupying largely orthogonal subspaces.
594	
595	\section{Cross-Scale Validation (Qwen-2.5-1.5B)}\label{sec:appendix-1.5b}
596	
597	We validate cross-scale on Qwen-2.5-1.5B-Instruct to test whether goal attention decay and $\beta$-steering generalize to smaller models.
598	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cce0045f-c9e4-4b7c-979d-14c9f26e2fc6",
  "isSidechain": true,
  "promptId": "a3e6062b-fe39-400b-a5a8-e5805ce60227",
  "agentId": "a56f1deb740d009c5",
  "type": "user",
  "uuid": "4a93299b-cd1f-4119-a19f-fe6636687ea7",
  "sourceToolAssistantUUID": "cce0045f-c9e4-4b7c-979d-14c9f26e2fc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-24T18:25:27.098Z_

<details open><summary>🔧 Tool call — Read · `toolu_016sop3WbGWGMepmKfHpVW1L`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 598,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a93299b-cd1f-4119-a19f-fe6636687ea7",
  "isSidechain": true,
  "agentId": "a56f1deb740d009c5",
  "requestId": "req_011CbMs22rHm52B33bNTTpgZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a608db39-3f45-4b5c-8002-422e76785bfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jkFYb1gKKZWLNhMDBSvnD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6769,
      "cache_read_input_tokens": 60525,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6769
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 60525,
          "cache_creation_input_tokens": 6769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6769,
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

_source line 30 · 2026-05-24T18:25:27.352Z_

<details><summary>↩ Tool result · `toolu_016sop3WbGWGMepmKfHpVW1L`</summary>

```text
598	
599	\paragraph{Phase~1 GAR decay.} The 1.5B base model exhibits 79.8\% GAR decline from turn~1 to mid-turns (vs.\ 70.8\% on 7B), confirming that attention decay is present across scales and is more severe at smaller model sizes.
600	
601	\paragraph{Steering evaluation.} Table~\ref{tab:1.5b-steering} reports AR evaluation ($N$\,=\,50). We report median PPL because Base $\beta$\,=\,3 contains a catastrophic outlier (conversation~\#11, PPL\,$>$\,$10^8$) that inflates the mean.\footnote{The outlier occurs in a single conversation where $\beta$-steering causes the base model to enter a degenerate repetition loop. ThreadGate produces zero such outliers across all $\beta$ values, suggesting the gate provides stability against catastrophic steering failures.}
602	
603	\begin{table}[h]
604	\centering\small
605	\caption{Cross-scale $\beta$-steering on Qwen-2.5-1.5B ($N$\,=\,50, AR). PPL is median due to catastrophic Base outlier at $\beta$\,=\,3. TG eliminates outliers across all $\beta$ values.}
606	\label{tab:1.5b-steering}
607	\begin{tabular}{llcc}
608	\toprule
609	\textbf{Model} & $\beta$ & \textbf{AR GAR} & \textbf{PPL (med)} \\
610	\midrule
611	Base & 0 & 0.017 & 1.909 \\
612	TG & 0 & 0.023 & 1.897 \\
613	\midrule
614	Base & 3 & 0.120 & 2.216 \\
615	TG & 3 & 0.114 & 1.975 \\
616	\midrule
617	Base & 5 & 0.657 & 2.804 \\
618	TG & 5 & 0.715 & 2.624 \\
619	\bottomrule
620	\end{tabular}
621	\end{table}
622	
623	The steering pattern mirrors the 7B results: $\beta$\,=\,5 recovers GAR to 0.657--0.715 ($p < 0.001$), confirming that attention misallocation is the proximal cause of GAR collapse across scales. At $\beta$\,=\,0, TG shows a small but significant GAR advantage ($p$\,=\,0.005); at $\beta$\,=\,3, the TG--Base difference is not statistically significant ($p$\,=\,0.815), unlike the 7B pattern where TG consistently outperforms Base. This scale-specific difference may reflect the 1.5B model's limited capacity to maintain learned routing at intermediate steering strengths. ThreadGate does provide a stability advantage---zero catastrophic PPL outliers vs.\ one in Base---suggesting that residual gating regularizes attention distributions even when aggregate GAR is comparable.
624	
625	\section{Per-Seed Detailed Results}\label{sec:appendix-perseed}
626	
627	Tables~\ref{tab:perseed-ss} and~\ref{tab:perseed-tg} report full per-seed breakdowns for the two multi-seed configurations, providing evidence that our main findings are robust to random initialization.
628	
629	\paragraph{Scheduled sampling (3 seeds).} TF GAR-ours is remarkably stable across seeds ($0.498\pm0.004$), confirming that the training-time attention objective converges reliably. AR GAR shows meaningful variance (std\,=\,0.047): seed 42 produces the lowest AR GAR (0.347, gap 1.4$\times$), seed 123 is intermediate (0.388, gap 1.3$\times$), and seed 456 is highest (0.433, gap 1.2$\times$). This variance is expected: AR evaluation involves free-form generation where small differences in learned attention patterns can compound across turns. The variance is asymmetric---all seeds remain well above the non-SS baseline (0.064)---so the qualitative conclusion (SS provides order-of-magnitude improvement) holds across seeds. At $\beta$\,=\,5, the cross-seed variance nearly vanishes ($0.717\pm0.001$), confirming that strong steering converges to a seed-independent attention equilibrium that overwhelms initialization differences.
630	
631	\paragraph{ThreadGate (2 seeds).} Two seeds produce nearly identical TF metrics ($0.504\pm0.001$) and similar AR GAR (0.064 vs.\ 0.055), with gap ratios of 7.8$\times$ and 9.1$\times$ respectively. The 15\% relative difference in AR GAR is small compared to the order-of-magnitude TF-AR gap, confirming that the exposure bias phenomenon is not seed-dependent.
632	
633	\paragraph{Training dynamics.} Seed variance in training time is non-trivial for scheduled sampling: seed 123 requires 10.8 hours (80\% overhead) vs.\ 6.5 hours for seeds 42 and 456 (8\% overhead). This variance is driven by the stochastic Bernoulli sampling of model-generated contexts: seed 123 happens to trigger longer autoregressive generation episodes early in training, where the model produces longer outputs before hitting the max-length cutoff. Despite this training-time variance, all three seeds converge to similar final metrics, suggesting the optimization landscape is robust.
634	
635	\input{../artifacts/appendix_expansion/tab_perseed_ss.tex}
636	
637	\input{../artifacts/appendix_expansion/tab_perseed_tg.tex}
638	
639	\section{Per-Turn GAR Decay Analysis}\label{sec:appendix-perturn-detail}
640	
641	Tables~\ref{tab:perturn-qwen} and~\ref{tab:perturn-llama} present per-turn AR GAR values for all configurations on both architectures, complementing the aggregate mid-turn GAR reported in the main text (Table~\ref{tab:four-way}).
642	
643	\paragraph{Qwen per-turn dynamics.} On Qwen (Table~\ref{tab:perturn-qwen}), all non-SS variants show rapid monotonic decay: turn-1 GAR ranges from 0.085 (Base) to 0.130 (ThreadGate), but by turn~5 all collapse below 0.07. The decay rate is approximately exponential for the first 3 turns, then plateaus near a floor value that varies by configuration (Base: 0.004, ThreadGate: 0.043--0.066, LoRA-only: 0.040). ThreadGate and LoRA-only show occasional turn-level fluctuations (e.g., TG turn~5 = 0.066 $>$ turn~4 = 0.043), which reflect stochastic variation in individual conversations rather than systematic recovery. Scheduled sampling retains substantially higher GAR throughout (turn-5 GAR\,=\,0.365 vs.\ 0.066 for ThreadGate), with a much flatter decay profile (15\% decline from turn~1 to turn~5 vs.\ 49\% for ThreadGate). This flatter profile is the signature of distributional robustification: SS-trained models encounter model-generated context during training, so the attention patterns are calibrated for the distribution they actually face during inference.
644	
645	\paragraph{Llama per-turn dynamics.} On Llama (Table~\ref{tab:perturn-llama}), the decay is steeper: Base GAR drops from 0.028 to 0.008 over 4 turns (71\% decline in the $N$\,=\,20 evaluation), and from 0.026 to 0.003 over 10 turns (88\% decline in the $N$\,=\,5 long-conversation evaluation). ThreadGate on Llama shows a distinctive pattern: turn-level GAR is roughly constant (0.038--0.049) rather than monotonically declining, suggesting that the gating mechanism maintains a stable floor on Llama that it fails to maintain on Qwen. However, this floor (0.04) is still an order of magnitude below the TF target (0.484), confirming that the fundamental TF-AR gap persists.
646	
647	\paragraph{Cross-architecture comparison.} The per-turn decay profiles reveal an architectural difference: Qwen shows a sharper initial decline (turn~1 to turn~2: $-$62\% for Base) followed by a plateau, while Llama shows a more gradual and sustained decline throughout. This difference may reflect the two architectures' different attention head configurations and layer counts, but the qualitative pattern---monotonic or near-monotonic decline toward a near-zero floor---is universal.
648	
649	Figures~\ref{fig:perturn-qwen-detail} and~\ref{fig:perturn-llama-detail} visualize these trajectories.
650	
651	\input{../artifacts/appendix_expansion/tab_perturn_qwen.tex}
652	
653	\begin{figure}[t]
654	  \centering
655	  \includegraphics[width=\columnwidth]{fig_perturn_qwen_detail.pdf}
656	  \caption{Per-turn AR GAR-ours across six Qwen-2.5-7B configurations. Scheduled sampling (green) retains far higher GAR than all other variants, which cluster below 0.13 and decay rapidly.}
657	  \label{fig:perturn-qwen-detail}
658	\end{figure}
659	
660	\input{../artifacts/appendix_expansion/tab_perturn_llama.tex}
661	
662	\begin{figure*}[t]
663	  \centering
664	  \includegraphics[width=0.95\textwidth]{fig_perturn_llama_detail.pdf}
665	  \caption{Per-turn AR GAR decay on Llama-3.1-8B. (a)~Three-way comparison (Base, TG, LoRA-only; $N$\,=\,20, 4 turns). (b)~Extended Base decay profile ($N$\,=\,5, 10 turns), showing 90\% decline.}
666	  \label{fig:perturn-llama-detail}
667	\end{figure*}
668	
669	\section{Extended Dataset Statistics}\label{sec:appendix-dataset-ext}
670	
671	Table~\ref{tab:dataset_stats} provides detailed statistics for the UltraChat training and evaluation splits. From the full UltraChat-200K corpus (207,865 conversations in the \texttt{train\_sft} split), we filter for conversations with $\geq$5 assistant turns, yielding 17,302 candidates (8.3\% of the full corpus). We randomly sample 8,000 for training, 50 for primary AR evaluation (mean 3.6 user turns), 50 for IID GAR diagnostics, and 200 for the instruction retention evaluation.
672	
673	\paragraph{Filtering rationale.} The $\geq$5 assistant turns threshold was chosen empirically: conversations with fewer than 3 assistant turns do not exhibit measurable attention decay (turn-1 to turn-3 GAR decline $<$5\%), making them uninformative for studying multi-turn exposure bias. The 5-turn threshold provides sufficient turn depth while retaining a reasonable fraction of the corpus. The average conversation in the filtered set contains 5.6 assistant turns (range: 5--7), with a mean sequence length of 1,247 tokens after tokenization with the Qwen-2.5 tokenizer.
674	
675	\paragraph{Evaluation split design.} We maintain four non-overlapping evaluation sets to avoid contamination: (1)~the primary AR evaluation ($N$\,=\,50) uses the same conversation structure as training but with held-out conversations, enabling direct comparison of TF vs.\ AR behavior; (2)~the IID GAR diagnostic ($N$\,=\,50) uses a separate sample for ablation studies that require independent measurements; (3)~the large instruction retention set ($N$\,=\,200) provides sufficient statistical power for per-category compliance analysis across 18 constraint types; (4)~the long-conversation set ($N$\,=\,5, 10 turns each) tests scaling behavior beyond the training distribution.
676	
677	\paragraph{Domain diversity.} UltraChat covers a broad range of conversational topics including knowledge Q\&A, creative writing, reasoning, and open-ended discussion. We do not stratify by topic, as our focus is on the architectural mechanism (attention routing) rather than domain-specific performance. The topic diversity serves as implicit regularization against overfitting to specific conversation patterns.
678	
679	\input{../artifacts/appendix_expansion/tab_dataset_stats.tex}
680	
681	\section{Extended GAR Robustness Analysis}\label{sec:appendix-gar-ext}
682	
683	Table~\ref{tab:gar_robustness} and Figure~\ref{fig:gar-robust-grouped} extend the GAR robustness analysis from \S\ref{sec:appendix-gar-robust} with turn-1 GAR and gap ratio metrics across all four token-position variants. We evaluate four ways to select the query token position for gradient attribution: (1)~\textit{Last} (our default): the final token of each assistant turn, which captures the model's ``summary'' attention pattern at the prediction boundary; (2)~\textit{All}: the mean over all assistant tokens, providing a position-averaged view; (3)~\textit{First}: the first assistant token, which reflects initial attention allocation; (4)~\textit{Goal-only}: attention to goal tokens as defined by \citet{dongre2026attention}, which restricts the target set to system-prompt tokens.
684	
685	\paragraph{Position-specific vs.\ broad improvement.} The key finding is a clear dichotomy between ThreadGate and Scheduled Sampling. ThreadGate improvements are restricted to last-token and goal-only positions (the two definitions sharing the query position targeted by the GAR loss): gap ratios drop to 1.21$\times$ and 1.07$\times$ respectively. All-token (5.04$\times$) and first-token (8.24$\times$) GAR remain near base levels, confirming that the learned routing is position-specific. Scheduled Sampling raises all four definitions above 0.36 with gap ratios $\leq$1.83$\times$, demonstrating that distributional robustification builds broad goal attention across token positions rather than overfitting to the position targeted by the loss.
686	
687	\paragraph{Turn-1 vs.\ mid-turn dynamics.} Turn-1 GAR is consistently higher than mid-turn GAR across all definitions and conditions, reflecting the first turn's proximity to the ground-truth prefix in training. The gap ratio quantifies how much of this initial attention survives into later turns. First-token GAR shows the largest gap ratios (Base: 13.3$\times$, TG: 8.2$\times$), indicating that the first-token position is most vulnerable to distributional drift---the initial token's attention pattern is highly dependent on the conditioning context, which diverges most from training under autoregressive generation.
688	
689	\input{../artifacts/appendix_expansion/tab_gar_robustness.tex}
690	
691	\begin{figure}[t]
692	  \centering
693	  \includegraphics[width=\columnwidth]{fig_gar_robustness_grouped.pdf}
694	  \caption{Mid-turn GAR across four token-position definitions. SS raises all four above 0.36; TG only improves last-token and goal-only.}
695	  \label{fig:gar-robust-grouped}
696	\end{figure}
697	
698	\section{MMLU Category Breakdown}\label{sec:appendix-mmlu-ext}
699	
700	Table~\ref{tab:mmlu_detail} breaks down MMLU 5-shot accuracy by category (STEM, Social Sciences, Humanities, Other) for all six Qwen-2.5-7B training configurations. This analysis addresses a potential concern: that auxiliary attention objectives might divert representational capacity from general language understanding, particularly in knowledge-intensive STEM domains.
701	
702	\paragraph{Per-category analysis.} The maximum per-category degradation is 1.2\,pp (ThreadGate on STEM), and no category shows systematic degradation across all variants. Notably, the ordering of variants differs across categories: ThreadGate shows the largest STEM drop but the smallest Humanities drop, while PCGrad shows the smallest overall drop despite having the worst AR GAR. This lack of correlation between GAR performance and MMLU degradation is consistent with GAR and NTP occupying largely orthogonal parameter subspaces---the LoRA adapter capacity (4.2M parameters) is sufficient to accommodate both objectives without interference.
703	
704	\paragraph{Statistical significance.} The per-category differences are small relative to the evaluation noise: with $N$\,=\,14,042 questions total ($\sim$3,500 per category), a 0.8\,pp accuracy difference corresponds to $\sim$28 questions, well within expected stochastic variation for 5-shot in-context learning. A chi-squared test comparing the best (PCGrad, 73.86\%) and worst (Uniform Gate, 73.46\%) variants yields $p$\,=\,0.503, confirming no significant difference. The category-level stability confirms that auxiliary GAR losses and gating do not selectively harm any knowledge domain.
705	
706	Figure~\ref{fig:mmlu-comparison} visualizes the per-category comparison, showing tight clustering across all variants within each category.
707	
708	\input{../artifacts/appendix_expansion/tab_mmlu_detail.tex}
709	
710	\begin{figure}[t]
711	  \centering
712	  \includegraphics[width=\columnwidth]{fig_mmlu_comparison.pdf}
713	  \caption{MMLU 5-shot accuracy by category across training configurations. All variants remain within 1.2\,pp of the LoRA-only baseline across all categories.}
714	  \label{fig:mmlu-comparison}
715	\end{figure}
716	
717	\section{Extended Cross-Scale Results (Qwen-2.5-1.5B)}\label{sec:appendix-1.5b-ext}
718	
719	Table~\ref{tab:qwen15b_results} extends the cross-scale analysis with Phase~1 GAR diagnostics, detailed Phase~2 training results, and $\beta$-steering evaluation on the Qwen-2.5-1.5B-Instruct model.
720	
721	\paragraph{Phase 1: GAR decay.} The 1.5B base model exhibits 79.8\% relative GAR decline from turn~1 to mid-turns, more severe than the 7B model's 70.8\% decline. This scale-dependent decay severity is consistent with smaller models having less redundant attention capacity: with 28 layers but only 1.5B parameters (vs.\ 7B), each layer carries proportionally more of the total representational burden, leaving less room for goal-oriented attention to persist alongside the primary NTP objective.
722	
723	\paragraph{Phase 2: Training.} ThreadGate training on 1.5B converges to TF GAR-ours of 0.498 with PPL of 2.67, closely matching the 7B results (0.504 / 2.78). The gate parameter count scales linearly with layer count (identical architecture, so ${\sim}$57K gate parameters). Training completes in 2.1 hours vs.\ 6.0 hours for 7B, reflecting the smaller model's reduced forward/backward pass cost.
724	
725	\paragraph{Steering evaluation.} At $\beta$\,=\,5, ThreadGate recovers GAR to 0.715 ($p < 0.001$), closely matching the 7B result (0.727). The recovery is essentially scale-independent at the strong steering regime: the attention bias added by $\beta$-steering overwhelms any capacity differences. At $\beta$\,=\,3, the picture differs: the TG--Base difference is not statistically significant ($p$\,=\,0.815) on 1.5B, unlike the significant difference on 7B ($p$\,=\,0.039). This scale-dependent response at intermediate $\beta$ may reflect the 1.5B model's reduced capacity for fine-grained attention routing: with fewer parameters per layer, the model cannot sustain the subtle attention reweighting that $\beta$\,=\,3 attempts.
726	
727	\paragraph{Catastrophic outliers.} Base 1.5B at $\beta$\,=\,3 produces one catastrophic PPL outlier (conversation \#11, PPL $> 10^8$) caused by a degenerate repetition loop. ThreadGate produces zero such outliers across all $\beta$ values, suggesting the gate provides a stabilizing effect on attention distributions even when aggregate GAR is comparable. We report median PPL to avoid this outlier dominating the central tendency estimate.
728	
729	\input{../artifacts/appendix_expansion/tab_qwen15b_results.tex}
730	
731	\section{Extended Statistical Analysis}\label{sec:appendix-stats-ext}
732	
733	Table~\ref{tab:statistical_tests} consolidates all statistical tests reported in this paper, including effect sizes, 95\% bootstrap confidence intervals, and significance levels. This section provides methodological detail beyond the summary in Appendix~\ref{sec:appendix-stats}.
734	
735	\paragraph{Test selection rationale.} All primary comparisons use paired Wilcoxon signed-rank tests on $N$\,=\,39 conversations (those with $\geq$3 turns from the 50-conversation held-out set). We use non-parametric tests because per-conversation GAR distributions are heavily right-skewed (skewness $>$ 2.0 for Base and PCGrad at $\beta$\,=\,0), violating normality assumptions required by parametric alternatives. The pairing structure (same conversations evaluated under different training configurations) controls for conversation-level confounds (topic difficulty, conversation length, system-prompt complexity).
736	
737	\paragraph{Effect size interpretation.} Effect sizes are computed as rank-biserial correlations ($r = Z / \sqrt{N}$), following standard practice. The largest effect is SS vs.\ TG ($r$\,=\,0.869, $p < 0.001$), a large effect by conventional thresholds ($r \geq 0.5$), confirming that scheduled sampling produces a qualitatively different outcome. The TG vs.\ Base effect ($r$\,=\,0.802) is also large, while TG vs.\ LoRA-only ($r$\,=\,0.454) is medium, reflecting the modest incremental benefit of gating over LoRA alone.
738	
739	\paragraph{Steering dose-response pattern.} At $\beta$\,=\,0, all four comparisons are significant ($p \leq 0.004$). At $\beta$\,=\,3 (the phase transition), TG vs.\ Base becomes marginally significant ($p$\,=\,0.039) and SS vs.\ TG remains significant ($p$\,=\,0.010), but TG vs.\ LoRA-only and PCGrad vs.\ TG lose significance ($p > 0.7$). At $\beta$\,=\,5, no pairwise comparison reaches significance---steering dominates and equalizes all variants. This dose-response pattern confirms that the training-time variant effects are real but small relative to the inference-time steering effect.
740	
741	\paragraph{Instruction retention.} The instruction retention analysis uses McNemar's test on $N$\,=\,54 paired constraint evaluations (18 constraint types $\times$ 3 conversations). The marginal significance ($p$\,=\,0.077) reflects the small sample size rather than a null effect: the point-biserial correlation ($r$\,=\,0.200, $p$\,=\,0.007) is significant when treating compliance as a continuous variable, and the per-category breakdown (Table~\ref{tab:ir-results}) shows a clear content-constraint improvement (+23.8\,pp).
742	
743	\paragraph{Multiple comparisons.} We report uncorrected $p$-values for the same reason described in Appendix~\ref{sec:appendix-stats}: comparisons are hypothesis-driven (each tests a specific causal exclusion in the analysis chain), not exploratory. All reported significant results ($p \leq 0.039$) survive Holm-Bonferroni correction for the 4 primary comparisons within each $\beta$ level.
744	
745	\input{../artifacts/appendix_expansion/tab_statistical_tests.tex}
746	
747	\section{Extended Training Dynamics}\label{sec:appendix-training-ext}
748	
749	Figure~\ref{fig:training-6panel} presents the complete training loss landscape for all five Qwen-2.5-7B conditions (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Scheduled Sampling) plus the base model, showing NTP loss, GAR loss, and total loss across three epochs.
750	
751	\paragraph{NTP loss convergence.} All fine-tuned variants converge to NTP loss ${\sim}$0.93 by epoch~3, with final-epoch values ranging from 0.929 (LoRA-only) to 0.934 (ThreadGate). PCGrad shows marginally higher variance due to gradient projection, but converges to the same terminal value. The uniformity of NTP convergence across variants---including those with auxiliary losses (ThreadGate, PCGrad) and those without (LoRA-only)---confirms that the GAR auxiliary objective does not interfere with the primary language modeling task during training.
752	
753	\paragraph{GAR loss dynamics.} GAR loss collapses to near-zero within the first epoch under teacher forcing across all variants, consistent with the auxiliary objective being easy to optimize when the model conditions on ground-truth context. This rapid convergence is a double-edged sword: while it confirms that the MSE formulation (v7) achieves stable optimization, the ease of convergence also means the model never learns to maintain attention under distributional drift. The scheduled sampling variant shows distinctive dynamics: higher initial GAR loss variance from stochastic context mixing, with occasional spikes when a particularly challenging model-generated context is sampled, followed by convergence to a similar final value.
754	
755	\paragraph{Training-inference disconnect.} The key observation is that training-time convergence is indistinguishable across variants: an observer with access only to training curves could not predict the 5.4$\times$ AR GAR difference between SS and TG. This disconnect reinforces the diagnosis that the failure occurs at the training-to-inference transition, not during optimization, and explains why architectural modifications (gating, PCGrad) that operate during training cannot address the fundamental distributional mismatch.
756	
757	\begin{figure*}[t]
758	  \centering
759	  \includegraphics[width=0.95\textwidth]{fig_training_curves_6panel.pdf}
760	  \caption{Training loss curves for all five Qwen conditions. NTP loss (left) converges to ${\sim}$0.93 across variants; GAR loss (center) collapses within epoch~1; total loss (right) is NTP-dominated. Training-time behavior is indistinguishable; the failure emerges only at inference.}
761	  \label{fig:training-6panel}
762	\end{figure*}
763	
764	\section{Per-$\beta$ Steering Visualization}\label{sec:appendix-steering-viz}
765	
766	Figure~\ref{fig:steering-4panel} visualizes per-turn GAR trajectories under four steering strengths ($\beta$\,=\,0, 3, 5, 10), revealing the turn-level dynamics that underlie the aggregate steering results in Table~\ref{tab:steering-full}.
767	
768	\paragraph{Unsteered baseline ($\beta$\,=\,0).} GAR decays monotonically from 0.12 to 0.02 over five turns, with the steepest decline between turns~1 and~2 ($-$44\%). This trajectory matches the per-turn profiles in Appendix~\ref{sec:appendix-perturn-detail} and confirms that the decay is a smooth, progressive phenomenon rather than a discrete failure at a specific turn.
769	
770	\paragraph{Phase transition ($\beta$\,=\,3).} Turn-1 GAR jumps to ${\sim}$0.55, but per-turn decay persists (${\sim}$15\% decline from turn~1 to turn~5). This indicates that steering partially compensates for the distributional drift but does not eliminate it: the attention bias adds a constant offset to goal-token logits, while the drift compounds multiplicatively across turns. The residual decay at $\beta$\,=\,3 explains why this operating point shows the strongest training-variant effects in the dose-response analysis (Appendix~\ref{sec:appendix-stats-ext}).
771	
772	\paragraph{Sustained recovery ($\beta$\,=\,5).} GAR is sustained above 0.6 throughout, with minimal per-turn decay ($<$5\% decline). At this steering strength, the constant attention bias dominates the per-turn drift, effectively replacing the lost training-time signal with an inference-time substitute. The 9\% PPL cost (1.43 $\to$ 1.77) is modest compared to the order-of-magnitude GAR recovery.
773	
774	\paragraph{Saturation regime ($\beta$\,=\,10).} GAR saturates near 1.0 across all turns but PPL degrades catastrophically ($>$3.5), as the excessive attention bias distorts the attention distribution beyond the model's capacity for coherent generation. This regime is impractical and serves as an upper bound on the steering approach.
775	
776	\paragraph{Operating region.} The region $\beta \in [3, 5]$ balances GAR recovery against PPL cost, and the per-turn profiles confirm that steering must counteract an ongoing distributional drift rather than a one-time initialization failure---a key diagnostic that distinguishes exposure bias from alternative hypotheses (e.g., capacity limitations or optimization failures).
777	
778	\begin{figure*}[t]
779	  \centering
780	  \includegraphics[width=0.95\textwidth]{fig_steering_perturn_4panel.pdf}
781	  \caption{Per-turn GAR under four $\beta$-steering strengths. At $\beta$\,=\,0, monotonic decay; at $\beta$\,=\,3, partial recovery with residual decay; at $\beta$\,=\,5, sustained high GAR; at $\beta$\,=\,10, saturation with catastrophic PPL.}
782	  \label{fig:steering-4panel}
783	\end{figure*}
784	
785	\section{Llama-3.1-8B Scheduled Sampling Details}\label{sec:appendix-llama-ss}
786	
787	Llama-3.1-8B-Instruct was trained with scheduled sampling using the same protocol as Qwen (\S\ref{sec:appendix-ss}), with one key difference: training was stopped at 2 epochs (${\sim}$14{,}400 steps) instead of 3, because Llama's per-step wall-clock time was ${\sim}$4$\times$ slower than Qwen on the same hardware (624 steps/h vs.\ ${\sim}$2{,}400 steps/h for Qwen). This is attributable to Llama's larger vocabulary (128K vs.\ 152K tokens) and different attention implementation. The 2-epoch checkpoint was selected based on convergence of TF GAR (0.477, within 0.02 of Qwen's 3-epoch value 0.498).
788	
789	\paragraph{$\beta$-steering on Llama SS.}
790	Table~\ref{tab:llama-ss-steering} reports $\beta$-steering results on the Llama SS model. The phase transition occurs at $\beta$\,=\,3 (GAR jumps from 0.166 to 0.628), consistent with the Qwen pattern. At $\beta$\,=\,5, GAR reaches 0.791---higher than Qwen's 0.717---suggesting that Llama's attention distribution is more responsive to the additive bias, possibly because the lower baseline AR GAR leaves more headroom for steering to exploit.
791	
792	\begin{table}[h]
793	\centering\small
794	\caption{$\beta$-steering on Llama-3.1-8B SS model ($N$\,=\,20, $T$\,=\,4).}
795	\label{tab:llama-ss-steering}
796	\begin{tabular}{@{}l ccc@{}}
797	\toprule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a608db39-3f45-4b5c-8002-422e76785bfb",
  "isSidechain": true,
  "promptId": "a3e6062b-fe39-400b-a5a8-e5805ce60227",
  "agentId": "a56f1deb740d009c5",
  "type": "user",
  "uuid": "0ad444ab-daeb-4408-901f-0ec78b2b97b3",
  "sourceToolAssistantUUID": "a608db39-3f45-4b5c-8002-422e76785bfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-24T18:25:31.870Z_

<details open><summary>🔧 Tool call — Read · `toolu_017fLpxDjhTbcNHahzDMXHuz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 797,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ad444ab-daeb-4408-901f-0ec78b2b97b3",
  "isSidechain": true,
  "agentId": "a56f1deb740d009c5",
  "requestId": "req_011CbMs2NXiYqvx7n3P2AhfC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9e72069-ef39-4e45-b5a5-5ea1de906149",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W7E35vTkYQX1bnjdFh1Cdz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8394,
      "cache_read_input_tokens": 67294,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8394
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 67294,
          "cache_creation_input_tokens": 8394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8394,
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

_source line 32 · 2026-05-24T18:25:31.880Z_

<details><summary>↩ Tool result · `toolu_017fLpxDjhTbcNHahzDMXHuz`</summary>

```text
797	\toprule
798	& $\beta$\,=\,0 & $\beta$\,=\,3 & $\beta$\,=\,5 \\
799	\midrule
800	AR GAR & 0.166 & 0.628 & 0.791 \\
801	\bottomrule
802	\end{tabular}
803	\end{table}
804	
805	\paragraph{Cross-model comparison.}
806	Table~\ref{tab:llama-vs-qwen-ss} compares scheduled sampling across both architectures. Both models show large gap compression relative to their ThreadGate baselines, but the residual gap on Llama (2.9$\times$) is larger than Qwen's (1.2$\times$). We attribute this to training duration: Llama received only 2 epochs of scheduled sampling exposure versus Qwen's 3 epochs. The compression \emph{factor} is comparable---Llama reduces its gap by 3.9$\times$ (from 11.2$\times$ to 2.9$\times$) while Qwen reduces by 6.5$\times$ (from 7.8$\times$ to 1.2$\times$)---suggesting that a third epoch would likely narrow the residual gap further. Notably, $\beta$-steering is more effective on Llama (0.791 vs.\ 0.717 at $\beta$\,=\,5), partially compensating for the weaker training-time compression.
807	
808	\paragraph{Architectural differences.}
809	Several architectural differences between Qwen-2.5-7B and Llama-3.1-8B may contribute to the cross-model gap variation. Llama uses Grouped Query Attention (GQA) with 8 KV heads (vs.\ Qwen's full 28-head MHA), which reduces the number of independently steerable attention heads by 3.5$\times$. Llama also uses RoPE with a longer default context (128K tokens vs.\ Qwen's 32K), which may affect how positional information interacts with goal-token attention at different conversation depths. Despite these differences, the qualitative pattern is identical: TF convergence, AR collapse, and SS-mediated recovery, confirming that exposure bias on auxiliary attention losses is architecture-general rather than an artifact of a specific attention implementation.
810	
811	\paragraph{Training dynamics.}
812	The Llama SS training loss trajectory closely mirrors Qwen's during the first two epochs: NTP loss converges within epoch~1 (final NTP loss 0.62 for Llama vs.\ 0.58 for Qwen), while GAR loss continues to decrease throughout epoch~2. The scheduled sampling ratio reaches ${\sim}$0.33 at the end of epoch~2 (vs.\ 0.50 at end of epoch~3 for Qwen), meaning Llama was exposed to less model-generated context during training. This partial exposure is sufficient to achieve meaningful gap compression (11.2$\times$ $\to$ 2.9$\times$) but leaves a larger residual gap than Qwen's full 3-epoch schedule.
813	
814	\begin{table}[h]
815	\centering\small
816	\caption{Scheduled sampling comparison: Qwen-2.5-7B vs.\ Llama-3.1-8B.}
817	\label{tab:llama-vs-qwen-ss}
818	\begin{tabular}{@{}l cc@{}}
819	\toprule
820	\textbf{Metric} & \textbf{Qwen-7B} & \textbf{Llama-8B} \\
821	\midrule
822	SS epochs & 3 & 2 \\
823	TF GAR & 0.498 & 0.477 \\
824	AR GAR ($\beta$\,=\,0) & 0.401 & 0.166 \\
825	TF/AR gap & 1.2$\times$ & 2.9$\times$ \\
826	Baseline TG gap & 7.8$\times$ & 11.2$\times$ \\
827	Gap compression & 6.5$\times$ & 3.9$\times$ \\
828	AR GAR ($\beta$\,=\,5) & 0.717 & 0.791 \\
829	TF PPL & 2.78 & 2.82 \\
830	AR PPL & 1.441 & 1.370 \\
831	\bottomrule
832	\end{tabular}
833	\end{table}
834	
835	\section{Use of AI Assistants}\label{sec:appendix-ai}
836	
837	We used Claude (Anthropic) as an AI coding and writing assistant
838	throughout this work. Specifically:
839	\begin{itemize}
840	    \item \textbf{Code:} drafting experiment scripts, data-processing
841	    pipelines, and analysis utilities; debugging and refactoring.
842	    \item \textbf{Writing:} drafting and revising paper sections,
843	    polishing prose, and reformatting LaTeX.
844	    \item \textbf{Literature:} summarizing related papers to inform
845	    related-work section.
846	\end{itemize}
847	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9e72069-ef39-4e45-b5a5-5ea1de906149",
  "isSidechain": true,
  "promptId": "a3e6062b-fe39-400b-a5a8-e5805ce60227",
  "agentId": "a56f1deb740d009c5",
  "type": "user",
  "uuid": "09d1a097-41b7-4e79-bd85-aad6bf6d6315",
  "sourceToolAssistantUUID": "d9e72069-ef39-4e45-b5a5-5ea1de906149",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-24T18:26:47.207Z_

Now I have read all files. Let me compile the comprehensive acronym audit.

Here is the full acronym/abbreviation audit:

---

## ACRONYM/ABBREVIATION AUDIT REPORT

### Master Table

| # | Acronym | Full Form (if given) | First Use Location | Defined on First Use? | Defined in Abstract? | Status |
|---|---------|---------------------|--------------------|-----------------------|---------------------|--------|
| 1 | **GAR** | Goal Accessibility Ratio | Abstract (line 4) | NO -- used without expansion in Abstract | NO | **NEEDS FIX** |
| 2 | **TF** | Teacher forcing/teacher-forced | Abstract (line 4, implicit "teacher forcing") | NO -- never explicitly expanded | N/A | **NEEDS FIX** |
| 3 | **AR** | Autoregressive | Abstract (line 6, "AR GAR") | NO -- never explicitly expanded | NO | **NEEDS FIX** |
| 4 | **PCGrad** | (Projected Conflicting Gradients) | Abstract (line 6) | NO -- never expanded anywhere in paper | NO | **NEEDS FIX** |
| 5 | **SS** | Scheduled Sampling | Experiments (line 65, first use as "SS") | NO -- abbreviation used without prior formal definition | N/A | **NEEDS FIX** |
| 6 | **NTP** | Next-token prediction | Introduction (line 5) | YES -- "next-token prediction (NTP)" | NO (not used in abstract) | OK |
| 7 | **LoRA** | Low-Rank Adaptation | Introduction (line 7) | NO -- used without expansion; citation given | N/A | **NEEDS FIX** |
| 8 | **TG** | ThreadGate | Experiments table caption (line 17, "TG") and Analysis (line 32) | NO -- used as abbreviation without formal definition | N/A | **NEEDS FIX** |
| 9 | **UG** | Uniform Gate | Table caption abbreviation | Contextually clear from table but never formally defined | N/A | OK (borderline) |
| 10 | **PPL** | Perplexity | Experiments (line 6) | NO -- never expanded | N/A | **NEEDS FIX** |
| 11 | **MSE** | Mean Squared Error | Method (line 44) | NO -- never expanded | N/A | **NEEDS FIX** |
| 12 | **MLP** | Multi-Layer Perceptron | Method (line 27) | NO -- never expanded | N/A | **NEEDS FIX** |
| 13 | **FFN** | Feed-Forward Network | Method (line 24) | NO -- never expanded | N/A | **NEEDS FIX** |
| 14 | **MMLU** | Massive Multitask Language Understanding | Related Work (line 7) | NO -- citation given but no expansion | N/A | **NEEDS FIX** |
| 15 | **LLM** | Large Language Model | Not used explicitly in paper text | N/A | N/A | OK (not used) |
| 16 | **IID** | Independent and Identically Distributed | Experiments (line 6) | NO -- never expanded | N/A | **NEEDS FIX** |
| 17 | **AUC** | Area Under the Curve | Introduction (line 3) | NO -- never expanded | N/A | **NEEDS FIX** |
| 18 | **CI** | Confidence Interval | Experiments table (line 23) | NO -- used in table header only | N/A | OK (standard) |
| 19 | **TRC** | Turn-level Residual Coherence | Analysis (line 28) | YES -- "Turn-level Residual Coherence (TRC)" | N/A | OK |
| 20 | **CoV** | Coefficient of Variation | Analysis (line 32) | NO -- never expanded | N/A | **NEEDS FIX** |
| 21 | **KV** | Key-Value | Appendix (line 211, "28 KV heads") | NO -- never expanded | N/A | OK (standard transformer term) |
| 22 | **GQA** | Grouped Query Attention | Appendix (line 809) | YES -- "Grouped Query Attention (GQA)" | N/A | OK |
| 23 | **MHA** | Multi-Head Attention | Appendix (line 809) | NO -- "28-head MHA" used without expansion | N/A | **NEEDS FIX** |
| 24 | **RoPE** | Rotary Position Embedding | Appendix (line 809) | NO -- never expanded | N/A | **NEEDS FIX** |
| 25 | **GLU** | Gated Linear Unit | Related Work (line 7) | NO -- "GLU-style gating" with citation but no expansion | N/A | **NEEDS FIX** |
| 26 | **NMT** | Neural Machine Translation | Related Work (line 10) | NO -- never expanded | N/A | **NEEDS FIX** |
| 27 | **KL** | Kullback-Leibler | Related Work (line 10, "KL-divergence") | NO -- never expanded | N/A | OK (universally known) |
| 28 | **VRAM** | Video Random Access Memory | Appendix (line 3) | NO -- never expanded | N/A | OK (standard) |
| 29 | **GAR-O** | GAR-ours | Experiments table (line 17) | YES -- defined in table caption | N/A | OK |
| 30 | **GAR-D** | GAR-Dongre | Experiments table (line 17) | YES -- defined in table caption | N/A | OK |
| 31 | **PASTA** | (Process for ASsisting ThA... / acronym from paper) | Related Work (line 7) | NO -- "PASTA" given with citation but no expansion | N/A | **NEEDS FIX** |
| 32 | **CAGrad** | Conflict-Averse Gradient | Related Work (line 7) | NO -- citation given but no expansion | N/A | OK (used only as method name with citation) |
| 33 | **AdamW** | Adam with Weight decay | Experiments (line 5) | NO -- never expanded | N/A | OK (universally known optimizer name) |
| 34 | **STEM** | Science, Technology, Engineering, Mathematics | Appendix (line 700) | NO -- never expanded | N/A | OK (universally known) |
| 35 | **GPU** | Graphics Processing Unit | Throughout | NO -- never expanded | N/A | OK (universally known) |
| 36 | **CDN/SFT/RLHF/DPO/PEFT/EB** | Various | Not used in paper | N/A | N/A | OK (not used) |

---

### Critical Issues Requiring Fixes

#### 1. Abstract: GAR not defined on first use

**File**: `abstract.tex`, line 4
**Current**: `...optimized to GAR\,=\,0.50 under teacher forcing...`
**Problem**: GAR is used without expansion. First expansion appears in Introduction line 3: "Goal Accessibility Ratio (GAR)". For EMNLP, the abstract should be self-contained.
**Fix**: On first use in abstract, expand: "Goal Accessibility Ratio (GAR)"

#### 2. Abstract: AR not defined

**File**: `abstract.tex`, line 6
**Current**: `...AR GAR ($p$\,=\,0.002)...`
**Problem**: "AR" is never formally defined anywhere in the paper. It is used as shorthand for "autoregressive" throughout.
**Fix**: On first use in abstract (line 6), write "autoregressive (AR) GAR" or spell out. Then define again on first use in main text.

#### 3. Abstract: TF not defined

**File**: `abstract.tex`, line 4
**Current**: `...GAR\,=\,0.50 under teacher forcing collapse...`
**Problem**: "TF" is used extensively in the paper (e.g., "TF evaluation", "TF GAR", "TF-AR gap") but the abbreviation is never formally introduced. "teacher forcing" is written out in the abstract but "TF" appears first in Introduction line 12 without definition.
**Fix**: Add "(TF)" after "teacher forcing" on first use in Introduction (line 12 area), or in the abstract where "teacher forcing" appears. Then all subsequent "TF" uses are covered.

#### 4. PCGrad never expanded

**File**: `abstract.tex`, line 6 (first use)
**Current**: `PCGrad eliminates gradient conflict...`
**Problem**: PCGrad is never expanded. It stands for "Projecting Conflicting Gradients". Citation is given later but no full form ever appears.
**Fix**: Not strictly required since it's a proper method name with citation, but for clarity add on first use in main text (Introduction line 7): "PCGrad \citep{yu2020pcgrad}" -- this is already done. For the abstract, spell it out briefly or leave as-is since it has a citation. **Borderline -- acceptable as a method name.**

#### 5. SS abbreviation not formally defined

**File**: `experiments.tex`, line 65 area
**Current**: First use of "SS" as abbreviation: "SS raises mid-turn GAR above 0.36"
**Problem**: "Scheduled sampling" is spelled out in the subsection title and text, but "SS" as abbreviation is never formally introduced with "(SS)".
**Fix**: On first use, write "scheduled sampling (SS)" then use SS thereafter.

#### 6. TG abbreviation not formally defined

**File**: First appears in experiments table caption (line 17) and Analysis (line 32)
**Current**: "TG" used as abbreviation for ThreadGate without formal definition
**Fix**: Add "(TG)" after the first mention of "ThreadGate" where abbreviation will be used, e.g., in table caption: already says "TG vs.\ LoRA-only" etc.

#### 7. LoRA not expanded on first use

**File**: `introduction.tex`, line 7
**Current**: `...LoRA configuration, optimizer...`
**Problem**: LoRA is used without expansion. First use with citation is in `experiments.tex` line 5.
**Fix**: On first use (Introduction line 7), add "Low-Rank Adaptation (LoRA)" or at least ensure the first use in experiments has the expansion.

#### 8. PPL not expanded

**File**: `experiments.tex`, line 6 (first use)
**Current**: `...reporting GAR-ours, GAR-Dongre \citep{dongre2026attention}, and PPL.`
**Problem**: PPL is used without expansion. Perplexity is mentioned in Method line 40 as "perplexity" but PPL abbreviation is never linked to it.
**Fix**: On first use, write "perplexity (PPL)".

#### 9. MSE not expanded

**File**: `method.tex`, line 44
**Current**: `We use MSE rather than cross-entropy...`
**Problem**: MSE is never expanded.
**Fix**: Write "mean squared error (MSE)" on first use.

#### 10. MLP not expanded

**File**: `method.tex`, line 27
**Current**: `...two-layer MLP that takes both content and turn features...`
**Problem**: MLP never expanded.
**Fix**: Write "multi-layer perceptron (MLP)" on first use, or "two-layer feedforward network (MLP)".

#### 11. FFN not expanded

**File**: `method.tex`, line 24
**Current**: `...(self-attention or FFN).`
**Problem**: FFN never expanded.
**Fix**: Write "feed-forward network (FFN)".

#### 12. IID not expanded

**File**: `experiments.tex`, line 6
**Current**: `We evaluate under \emph{IID} (same-distribution UltraChat text)...`
**Problem**: IID/i.i.d. never expanded.
**Fix**: The parenthetical already explains it contextually. For strictness, write "independent and identically distributed (IID)" or just accept that the parenthetical explanation is sufficient. **Borderline -- the parenthetical clarification mitigates this.**

#### 13. AUC not expanded

**File**: `introduction.tex`, line 3
**Current**: `...AUC\,=\,0.98...`
**Problem**: AUC never expanded.
**Fix**: Write "area under the curve (AUC)" on first use.

#### 14. CoV not expanded

**File**: `analysis.tex`, line 32
**Current**: `...the AR distribution is heavy-tailed (CoV\,$>$\,100\%)...`
**Problem**: CoV never expanded.
**Fix**: Write "coefficient of variation (CoV)".

#### 15. MMLU not expanded on first use

**File**: `related_work.tex`, line 7 (first use in main text)
**Current**: `...achieving MMLU \citep{hendrycks2021measuring} $+$2.03...`
**Problem**: MMLU has a citation but no expansion. Full name is "Massive Multitask Language Understanding".
**Fix**: Write "MMLU \citep[Massive Multitask Language Understanding;][]{hendrycks2021measuring}" or "Massive Multitask Language Understanding (MMLU; \citealp{hendrycks2021measuring})".

#### 16. MHA not expanded

**File**: `appendix.tex`, line 809
**Current**: `...Qwen's full 28-head MHA...`
**Problem**: MHA never expanded.
**Fix**: Write "multi-head attention (MHA)" on first use.

#### 17. RoPE not expanded

**File**: `appendix.tex`, line 809
**Current**: `Llama also uses RoPE with a longer default context...`
**Problem**: RoPE never expanded.
**Fix**: Write "Rotary Position Embedding (RoPE)".

#### 18. GLU not expanded

**File**: `related_work.tex`, line 7
**Current**: `...GLU-style gating \citep{dauphin2017language,shazeer2020glu}...`
**Problem**: GLU never expanded.
**Fix**: Write "Gated Linear Unit (GLU)-style gating".

#### 19. NMT not expanded

**File**: `related_work.tex`, line 10
**Current**: `...transformers for single-turn NMT...`
**Problem**: NMT never expanded. "Neural machine translation" never appears.
**Fix**: On first use write "neural machine translation (NMT)".

#### 20. PASTA not expanded

**File**: `related_work.tex`, line 7
**Current**: `...attention steering (PASTA; \citealp{zhang2024tell})...`
**Problem**: PASTA stands for "Post-hoc Attention STeering Approach" but the acronym is never expanded.
**Fix**: Since it's a method name with a citation and contextually described as "attention steering", this is acceptable. The citation handles it. **OK as-is.**

---

### Summary of Required Fixes

**Critical (Abstract self-containment for EMNLP)**:
1. **GAR**: Expand in abstract on first use
2. **AR**: Expand in abstract on first use (and formally define in main text)
3. **TF**: Formally define abbreviation on first use in Introduction (already spelled out in abstract)

**Important (First-use expansion in main text)**:
4. **SS**: Define abbreviation on first use
5. **TG**: Define abbreviation on first use
6. **PPL**: Expand on first use
7. **MSE**: Expand on first use
8. **MLP**: Expand on first use
9. **FFN**: Expand on first use
10. **LoRA**: Expand on first use (Introduction line 7)
11. **AUC**: Expand on first use
12. **CoV**: Expand on first use
13. **NMT**: Expand on first use in Related Work
14. **GLU**: Expand on first use in Related Work
15. **MMLU**: Expand on first use in Related Work

**Minor (Appendix only, lower priority)**:
16. **MHA**: Expand on first use in appendix
17. **RoPE**: Expand on first use in appendix

**Acceptable as-is** (method names with citations, universally known terms):
- PCGrad, PASTA, CAGrad, AdamW, GPU, VRAM, KL, KV, CI, STEM, IID (contextually explained)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09d1a097-41b7-4e79-bd85-aad6bf6d6315",
  "isSidechain": true,
  "agentId": "a56f1deb740d009c5",
  "requestId": "req_011CbMs2hoLntbw8P6K18j6w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eecdc023-e9f0-4460-9376-fcc1d3c5950d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NJFyBRdbYdoBEvPmfCNXP7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1480,
      "cache_read_input_tokens": 75688,
      "output_tokens": 4142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1480
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4142,
          "cache_read_input_tokens": 75688,
          "cache_creation_input_tokens": 1480,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1480,
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
