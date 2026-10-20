# Research conversation: You are auditing a research paper for numerical accuracy before submission. Verify every number in the following appendi

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ac1babd70c733d821.jsonl`
- **Structured JSON:** [`6b18c25fcd845b0ad507.json`](../../sessions/6b/6b18c25fcd845b0ad507.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

17 recorded events

### User

_source line 1 · 2026-05-24T04:33:31.634Z_

You are auditing a research paper for numerical accuracy before submission. Verify every number in the following appendix .tex files against the registry data I'll provide. For each number, report: [file:line] number → [source exp_id] value → ✅ or ❌ (actual value X).

FILES TO CHECK (read each one):
1. /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_zs_crossmodel.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_downstream_analysis.tex
3. /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_tcr.tex
4. /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_wikievents_pilot.tex
5. /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_gollie_comparison.tex

REGISTRY DATA for verification:

**Zero-shot cross-model (SciERC):**
- phase2_scierc_unconstrained (Qwen ZS): DR=15.37%, RV=1.39%, ET=0.40%, CF=0.08%, R_F1=8.23%, E_F1=31.01%
- phase2_scierc_full_s1 (Qwen ZS S1): DR=0.93%, CF=9.90%, R_F1=8.36%, E_F1=30.98%
- llama_scierc_unconstrained: DR=13.34%, RV=0.55%, CF=6 (count), R_F1=2.68% (0.0268), E_F1=23.56% (0.2356)
- llama_scierc_full_s1: DR=0.08%, CF=6.56%, R_F1=2.54% (0.0254), E_F1=23.49% (0.2349)
- w6_mistral_scierc_unconstrained: DR=56.94%, ET=1.5%, CF=56.87%, R_F1=3.66% (0.0366), E_F1=27.28% (0.2728)
- w6_mistral_scierc_constrained: DR=13.40%, CF=1.27%, R_F1=3.67% (0.0367), E_F1=27.46% (0.2746)

**Zero-shot cross-model (DocRED):**
- phase2_docred_unconstrained (Qwen ZS): DR=18.46%, RV=29.66%, ET=2.48%, CF=0.10%, R_F1=7.74%, E_F1=58.15%
- phase2_docred_full_s1 (Qwen ZS S1): DR=10.21%, CF=2.57%, R_F1=8.23%, E_F1=59.37%
- llama_docred_unconstrained: DR=26.07%, RV=16.03%, ET=0.13%, CF=0.17%, R_F1=5.98%, E_F1=55.65%
- llama_docred_full_s1 (mt6144): DR=2.57%, CF=12.13%, R_F1=6.25%, E_F1=55.04%
- w6_mistral_docred_unconstrained: DR=57.42%, RV=42.35%, ET=7.58%, CF=24.78%, R_F1=4.34% (0.0434), E_F1=48.51% (0.4851)
- w6_mistral_docred_constrained: DR=33.20%, CF=0.19%, R_F1=5.52%, E_F1=50.59%

**Post-hoc filtering:**
- posthoc_filtering_baseline: scierc reject=16.8%, docred reject=48.1%
- w8_ft_posthoc_baseline: mistral_docred reject=73.73%

**Fine-tuning composability:**
- w5_lora_scierc_unconstrained_eval (Qwen FT): DR=1.95%, CF=0, R_F1=43.86% (0.4386), E_F1=67.05% (0.6705)
- w5_lora_scierc_constrained_eval (Qwen FT S1): DR=0%, CF=1.18%, R_F1=43.77% (0.4377), E_F1=67.05% (0.6705)
- w5_llama_lora_scierc_unconstrained_eval: DR=1.11%, CF=0, R_F1=45.45% (0.4545), E_F1=67.76% (0.6776)
- w5_llama_lora_scierc_constrained_eval: DR=0.09%, CF=0.46%, R_F1=45.47% (0.4547), E_F1=67.76% (0.6776)
- w5_qwen_docred_lora_unconstrained_eval: DR=0.76%, RV=0.27%, CF=0.12%, R_F1=40.86%, E_F1=82.15%
- w5_qwen_docred_lora_constrained_eval: DR=0.01%, CF=0.41%, R_F1=40.56%, E_F1=81.43%
- w5_llama_docred_lora_unconstrained_eval: DR=0.49%, RV=0.15%, CF=0.08%, R_F1=43.72%, E_F1=83.93%
- w5_llama_docred_lora_constrained_eval: DR=0.21%, CF=0.21%, R_F1=43.78%, E_F1=83.94%

**DocRED DR reductions (zero-shot):**
- Qwen: 18.46→10.21 = 44.7% reduction
- Llama: 26.07→2.57 = 90.1% reduction  
- Mistral: 57.42→33.20 = 42.2% reduction

**SciERC DR reductions (zero-shot):**
- Qwen: 15.37→0.93 = 93.9% reduction
- Llama: 13.34→0.08 = 99.4% reduction
- Mistral: 56.94→13.40 = 76.5% reduction

**TCR:**
- d065_tcr_pilot: All CF eliminated across 10 configs. DR delta max on SciERC=0.28pp, on DocRED lora=0.14pp.
- d065_tcr_full: all_cf_eliminated=True, docred_zs_70b_dr_delta=4.2, scierc_all_dr_delta_max=0.28

**WikiEvents:**
- ee_qwen_wikievents_unconstrained: EV=24%, RoV=74.9%, CF=0, parse=218/246
- ee_qwen_wikievents_constrained_v3: EV=0%, RoV=0%, CF=21.1%, parse=206/246
- ee_llama_wikievents_unconstrained: EV=10.5%, RoV=88.8%, CF=0, parse=226/246
- ee_llama_wikievents_constrained_v3: EV=0%, RoV=0%, CF=17.2%, parse=207/246
- ee_mistral_wikievents_unconstrained: EV=37.3%, RoV=63.9%, CF=0, parse=194/246
- ee_mistral_wikievents_constrained_v3: EV=0%, RoV=0%, CF=14.9%, parse=218/246
- p1_ee_ft_composability_r5: unconstrained rov=38.31%, ac=2.68%; full_s1 rov=0%, ac=0%

**GoLLIE:**
- d063_gollie_violation_rate: DR=0, RV=0, ET=0, CF=0.67%, E_F1=9.17, R_F1=0, pred_rels=7 (5 in sf2), empty_docs=45%
- sf2_gollie_scierc_violation: GoLLIE_ZS DR=0, CF=0.83%, R_F1=0, pred_rels=5

Report ALL discrepancies found. Check every number.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4ef057c6-ed80-4dae-9126-cc738ba56a17",
  "agentId": "ac1babd70c733d821",
  "type": "user",
  "uuid": "c8be6a75-057a-4772-b7c6-d0f32afa9fd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-24T04:33:31.641Z_

```json
{
  "parentUuid": "c8be6a75-057a-4772-b7c6-d0f32afa9fd7",
  "isSidechain": true,
  "agentId": "ac1babd70c733d821",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
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
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
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
  "uuid": "f8bd6394-fdf6-4d32-ab9d-0c576726634f",
  "timestamp": "2026-05-24T04:33:31.641Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

---

### Assistant

_source line 3 · 2026-05-24T04:33:35.359Z_



I'll read all five appendix files and then cross-reference every number against the registry data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8bd6394-fdf6-4d32-ab9d-0c576726634f",
  "isSidechain": true,
  "agentId": "ac1babd70c733d821",
  "requestId": "req_011CbLmasLGJdU3rVFYYG6ii",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14edb648-1243-4ecf-bfc6-64f97ab8fffc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ct66TgqyPs49MwYRnTkQ5f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23314,
      "cache_read_input_tokens": 7347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23314,
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

_source line 4 · 2026-05-24T04:33:38.457Z_

<details open><summary>🔧 Tool call — Read · `toolu_018rdfy1a7mfUgzsdB4uzdjJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_zs_crossmodel.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14edb648-1243-4ecf-bfc6-64f97ab8fffc",
  "isSidechain": true,
  "agentId": "ac1babd70c733d821",
  "requestId": "req_011CbLmasLGJdU3rVFYYG6ii",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71bb2422-f248-42ae-8b03-d58869263704",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ct66TgqyPs49MwYRnTkQ5f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23314,
      "cache_read_input_tokens": 7347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23314,
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

_source line 5 · 2026-05-24T04:33:38.463Z_

<details open><summary>🔧 Tool call — Read · `toolu_014d8hn7SuTxFU48f5jgdYu2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_downstream_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71bb2422-f248-42ae-8b03-d58869263704",
  "isSidechain": true,
  "agentId": "ac1babd70c733d821",
  "requestId": "req_011CbLmasLGJdU3rVFYYG6ii",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbcee293-5d80-464f-9f31-318d28ee6ff4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ct66TgqyPs49MwYRnTkQ5f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23314,
      "cache_read_input_tokens": 7347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23314,
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

_source line 6 · 2026-05-24T04:33:38.468Z_

<details><summary>↩ Tool result · `toolu_018rdfy1a7mfUgzsdB4uzdjJ`</summary>

```text
1	% Appendix: Zero-Shot Cross-Model and Cross-Dataset Details
2	% Moved from main text §5.2--§5.3 per reviewer guidance to focus main text on fine-tuned results.
3	
4	\section{Zero-Shot Cross-Model Validation}
5	\label{app:cross-model-zs}
6	
7	\begin{table}[h]
8	\centering
9	\small
10	\setlength{\tabcolsep}{3.4pt}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{@{}ll rrrr r@{}}
13	\toprule
14	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
15	& \textbf{R-F1} \\
16	\cmidrule(lr){3-6} \cmidrule(l){7-7}
17	\textbf{Dataset} & \textbf{Model}
18	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
19	  & $\uparrow$ \\
20	\midrule
21	\multirow{6}{*}{SciERC}
22	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
23	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
24	  \cmidrule(l){2-7}
25	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
26	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
27	  \cmidrule(l){2-7}
28	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
29	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
30	\midrule
31	\multirow{6}{*}{DocRED}
32	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
33	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
34	  \cmidrule(l){2-7}
35	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
36	  & Llama (S1)  &  2.55 &  0    & 0    & 12.02& 6.27 \\
37	  \cmidrule(l){2-7}
38	  & Mistral (U) & 57.42 & 42.35 & 7.58 & 24.78 & 4.34 \\
39	  & Mistral (S1)& 33.20 &  0    & 0    & 0.19  & 5.52 \\
40	\bottomrule
41	\end{tabular}}%
42	\caption{Three-model zero-shot validation. U: unconstrained; S1: full two-layer.
43	Parse failures: Llama DocRED 9.1\%; others $\leq$1.1\%.
44	$^\dagger$Mistral: poor zero-shot calibration causes pervasive type inconsistencies.
45	F1 $\times$100.}
46	\label{tab:cross-model}
47	\end{table}
48	
49	\paragraph{Cross-model results.}
50	RV and ET reach $\leq$0.03\% for all models on both datasets.
51	DR drops 76--99\% on SciERC and 42--90\% on DocRED; R-F1 improves in 5/6 settings.
52	CF direction depends on calibration: S1 introduces CF for calibrated models (up to 12.02\%) but reduces it for Mistral (56.87\%\,$\to$\,1.27\%); fine-tuning resolves both (\S\ref{sec:composability}).
53	Post-hoc filtering achieves DR${=}$0\% but at 15--74\% rejection rates (Appendix~\ref{app:posthoc-extended}).
54	
55	\paragraph{Cross-dataset validation on DocRED.}
56	\label{sec:docred-results}
57	DocRED (96 relations, 14$\times$ SciERC scale) validates the pattern under a larger, more restrictive ontology (Table~\ref{tab:docred-ablation}).
58	S1 reduces DR from 18.46\% to 10.21\% ($\downarrow$45\%), eliminates RV (29.66\%\,$\to$\,0.03\%) and ET, with R-F1 $+$0.49\,pp ($p < 0.001$).
59	The lower DR reduction (45\% vs.\ 94\% on SciERC) reflects DocRED's tighter constraints, which trigger more grammar-first fallback (\S\ref{sec:greedy-limitation}).
60	Grammar-only \emph{increases} DR (18.46\%\,$\to$\,26.17\%) via \textit{latent violation surfacing}: grammar forces OOV$\to$valid relation mapping, exposing type violations previously masked by vocabulary errors---a distinct cross-dataset confirmation of the scale-dependent layer interaction.
61	Fine-tuning reduces residual DR to $\leq$\,0.21\% (Table~\ref{tab:composability}; residual decomposition in Appendix~\ref{app:residual-dr-analysis}).
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71bb2422-f248-42ae-8b03-d58869263704",
  "isSidechain": true,
  "promptId": "4ef057c6-ed80-4dae-9126-cc738ba56a17",
  "agentId": "ac1babd70c733d821",
  "type": "user",
  "uuid": "b42f5270-5f85-41c4-9790-0b4ffd4931b6",
  "sourceToolAssistantUUID": "71bb2422-f248-42ae-8b03-d58869263704",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-24T04:33:38.470Z_

<details><summary>↩ Tool result · `toolu_014d8hn7SuTxFU48f5jgdYu2`</summary>

```text
1	\paragraph{Downstream impact of violation removal.}
2	\label{app:downstream-impact}
3	
4	A natural concern with schema-constrained decoding is whether enforcing ontological validity removes \emph{lucky violations}---predictions that happen to be correct (true positives) yet violate the schema.
5	To quantify this trade-off, we audit all true-positive relation triples produced by unconstrained fine-tuned models and check whether any of them carry a domain--range (DR) violation, i.e., an entity-type pair \mbox{$\langle h_\tau, t_\tau \rangle$} not sanctioned by the ontology for that relation.
6	
7	\begin{table}[h]
8	\centering
9	\small
10	\begin{tabular}{llrrrl}
11	\toprule
12	\textbf{Dataset} & \textbf{Model} & \textbf{TP} & \textbf{Lucky} & \textbf{\%\,TP} & \textbf{R drop} \\
13	\midrule
14	SciERC & Qwen-LoRA  & 461  & 4 & 0.87\% & 0.41\,pp \\
15	SciERC & Llama-LoRA & 467  & 5 & 1.07\% & 0.51\,pp \\
16	DocRED & Qwen-LoRA  & 5746 & 1 & 0.02\% & 0.01\,pp \\
17	DocRED & Llama-LoRA & 6226 & 1 & 0.02\% & 0.01\,pp \\
18	\bottomrule
19	\end{tabular}
20	\caption{Lucky violations: true-positive triples that carry a domain--range violation. \textbf{Lucky} counts such triples; \textbf{R drop} is the recall decrease (in percentage points) if they were removed.}
21	\label{tab:lucky-violations-detail}
22	\end{table}
23	
24	Across all four configurations, lucky violations account for at most 1.07\% of true positives (5 out of 467 on SciERC with Llama-LoRA) and as few as 0.02\% on DocRED.
25	The corresponding recall drop is negligible---at most 0.51 percentage points---while the vast majority of violated triples that constraints remove are false positives.
26	For example, on DocRED with Qwen-LoRA, constraints eliminate 164 schema-violating predictions but only 1 of them is actually correct; the other 163 are errors that would pollute a downstream knowledge graph.
27	
28	Inspecting the lucky violations qualitatively, they arise from borderline entity-type assignments rather than genuine schema gaps.
29	On SciERC, the recurring pattern involves \textsc{Metric}-typed entities (e.g., BLEU, NIST) appearing as heads of \texttt{Hyponym-of} relations, a pair absent from the training ontology because these metrics are rarely annotated as hyponyms.
30	On DocRED, the single lucky violation stems from an entity typed as \textsc{Misc} instead of \textsc{Org} (``Assassin's Creed Unity''), making its \texttt{developer} relation invalid under the schema despite being factually correct.
31	
32	These findings confirm that schema-constrained decoding introduces a minimal recall cost while providing a substantial precision gain.
33	Retaining these few lucky violations would allow schema-invalid triples into the knowledge graph, undermining the structural guarantees that motivate constrained decoding in the first place.
34	The net effect is overwhelmingly positive: constraints act as a high-precision filter that removes far more erroneous triples than correct ones.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbcee293-5d80-464f-9f31-318d28ee6ff4",
  "isSidechain": true,
  "promptId": "4ef057c6-ed80-4dae-9126-cc738ba56a17",
  "agentId": "ac1babd70c733d821",
  "type": "user",
  "uuid": "a5264d0a-20f3-4fcc-8e9b-2ee28685016b",
  "sourceToolAssistantUUID": "bbcee293-5d80-464f-9f31-318d28ee6ff4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-24T04:33:39.347Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EZuWHjGEmTce455HCB8Lgu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_tcr.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5264d0a-20f3-4fcc-8e9b-2ee28685016b",
  "isSidechain": true,
  "agentId": "ac1babd70c733d821",
  "requestId": "req_011CbLmasLGJdU3rVFYYG6ii",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3fa1f6b0-a799-4048-aa84-be696722d684",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ct66TgqyPs49MwYRnTkQ5f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23314,
      "cache_read_input_tokens": 7347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23314,
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

_source line 9 · 2026-05-24T04:33:39.352Z_

<details><summary>↩ Tool result · `toolu_01EZuWHjGEmTce455HCB8Lgu`</summary>

```text
1	% Appendix: Post-hoc Type Consistency Resolution (TCR)
2	% exp_ids: d065_tcr_pilot (all 10 configs)
3	
4	\section{Post-hoc Type Consistency Resolution}
5	\label{app:tcr}
6	
7	S1 enforces domain/range constraints per-triple but does not enforce global entity type consensus, leaving residual CF violations where the same entity receives different types across triples.
8	We evaluate a post-hoc resolution step (TCR): for each entity with conflicting type assignments, TCR selects the type that maximizes satisfaction count across all relations referencing that entity, subject to domain/range constraints.
9	Unlike naive majority voting (which ignores relational constraints and increases DR), TCR is constraint-aware: candidate types are scored by how many of the entity's relational contexts they satisfy.
10	TCR runs after S1 decoding completes and has access to the full document context.
11	
12	% ──────────────────────────────────────────
13	%  Table: TCR results on SciERC
14	% ──────────────────────────────────────────
15	\begin{table}[h]
16	\centering
17	\small
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}ll rr rr r r@{}}
20	\toprule
21	& & \multicolumn{2}{c}{\textbf{CF (\%)}} & \multicolumn{2}{c}{\textbf{DR (\%)}} & \textbf{$\Delta$E-F1} & \textbf{Fund.} \\
22	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-7} \cmidrule(l){8-8}
23	\textbf{Config} & \textbf{Model} & Pre & Post & Pre & Post & (pp) & (\%) \\
24	\midrule
25	\multirow{3}{*}{Zero-shot}
26	  & Qwen    & 9.75 & \textbf{0} & 0.93  & 1.21  & $-$1.29 & 2.04 \\
27	  & Llama   & 6.40 & \textbf{0} & 0.08  & 0.30  & $-$1.78 & 1.85 \\
28	  & Mistral & 0.67 & \textbf{0} & 13.36 & 12.87 & $+$0.05 & 0 \\
29	\midrule
30	\multirow{2}{*}{LoRA}
31	  & Qwen    & 1.19 & \textbf{0} & 0     & 0     & $-$0.75 & 0 \\
32	  & Llama   & 0.46 & \textbf{0} & 0.09  & 0.09  & $-$0.18 & 0 \\
33	\bottomrule
34	\end{tabular}}
35	\caption{TCR on SciERC ($\bar{\kappa}{=}0.333$, 551 docs).
36	Pre/Post: before/after TCR.
37	$\Delta$E-F1: entity F1 change (F1$\times$100).
38	Fund.: percentage of conflicting entities where no single type satisfies all relational constraints (fundamental conflicts).
39	TCR eliminates all CF with DR increases $\leq$0.28\,pp; fundamental conflicts are 0--2\%.}
40	\label{tab:tcr-scierc}
41	\end{table}
42	
43	% ──────────────────────────────────────────
44	%  Table: TCR results on DocRED
45	% ──────────────────────────────────────────
46	\begin{table}[h]
47	\centering
48	\small
49	\resizebox{\columnwidth}{!}{%
50	\begin{tabular}{@{}ll rr rr r r@{}}
51	\toprule
52	& & \multicolumn{2}{c}{\textbf{CF (\%)}} & \multicolumn{2}{c}{\textbf{DR (\%)}} & \textbf{$\Delta$E-F1} & \textbf{Fund.} \\
53	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-7} \cmidrule(l){8-8}
54	\textbf{Config} & \textbf{Model} & Pre & Post & Pre & Post & (pp) & (\%) \\
55	\midrule
56	\multirow{3}{*}{Zero-shot}
57	  & Qwen    & 13.11 & \textbf{0} & 10.21 & 11.74 & $-$3.44 & 13.52 \\
58	  & Llama   & 23.71 & \textbf{0} &  2.55 & 11.93 & $-$5.21 & 22.78 \\
59	  & 70B     & 11.61 & \textbf{0} &  0    &  4.20 & $-$5.98 & 18.26 \\
60	\midrule
61	\multirow{2}{*}{LoRA}
62	  & Qwen    &  0.42 & \textbf{0} &  0.01 &  0.14 & $-$0.16 & 12.16 \\
63	  & Llama   &  0.36 & \textbf{0} &  0.21 &  0.20 & $-$0.17 & 11.59 \\
64	\bottomrule
65	\end{tabular}}
66	\caption{TCR on DocRED ($\bar{\kappa}{=}0.842$, 998 docs).
67	Under zero-shot, TCR introduces substantial DR regressions (up to $+$9.38\,pp for Llama) and E-F1 drops (up to $-$5.98\,pp for 70B).
68	Fundamental conflict rates are 12--23\%, an order of magnitude higher than SciERC.
69	Under LoRA, low baseline CF (0.36--0.42\%) limits both TCR impact and DR cost.}
70	\label{tab:tcr-docred}
71	\end{table}
72	
73	\paragraph{Analysis.}
74	TCR effectiveness varies inversely with schema constraint tightness $\bar{\kappa}$ (descriptive pattern across two schemas).
75	On SciERC ($\bar{\kappa}{=}0.333$), fundamental conflicts constitute 0--2\% of type disagreements: most conflicts are resolvable because the loose schema admits many valid type pairs, and TCR can find a type satisfying all relational contexts.
76	DR increases are bounded ($\leq$0.28\,pp), and E-F1 cost is modest ($\leq$1.78\,pp in zero-shot, $\leq$0.75\,pp under LoRA).
77	On DocRED ($\bar{\kappa}{=}0.842$), 13--23\% of conflicts are fundamental: the tight schema renders most type pairs invalid, so unifying an entity's type across all its relational contexts inevitably violates some domain/range constraints.
78	This produces severe DR regressions under zero-shot (Llama: 2.55\%$\to$11.93\%; 70B: 0\%$\to$4.20\%), where baseline CF is high enough that many entities require resolution.
79	Under LoRA, baseline CF is already low (0.36--0.42\%), limiting both the scope for TCR improvement and the DR cost.
80	
81	This $\bar{\kappa}$-dependent boundary is consistent with the constraint tightness analysis in \S\ref{sec:composition}: $\bar{\kappa}$ characterizes not only the decoding-time DR residual regime but also the feasibility of post-hoc type resolution.
82	Beam search (\S\ref{sec:beam-results}) resolves CF and DR simultaneously across all $\bar{\kappa}$ values (SciERC and DocRED (998 docs): DR$\to$0\% for calibrated models), making it the preferred approach for high-tightness schemas.
83	TCR is a zero-cost complement for low-tightness schemas where beam search latency (1.39$\times$) is undesirable.
84	Integrating TCR into the decoding loop would require global optimization over all generated triples, conflicting with the autoregressive generation paradigm.
85	TCR is complementary to OntoCoDec---it addresses CF (which OntoCoDec's per-triple enforcement cannot prevent) while OntoCoDec addresses DR (which post-hoc correction cannot guarantee).
86	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fa1f6b0-a799-4048-aa84-be696722d684",
  "isSidechain": true,
  "promptId": "4ef057c6-ed80-4dae-9126-cc738ba56a17",
  "agentId": "ac1babd70c733d821",
  "type": "user",
  "uuid": "5054f091-6321-4ef3-9d33-127123285a09",
  "sourceToolAssistantUUID": "3fa1f6b0-a799-4048-aa84-be696722d684",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-24T04:33:39.692Z_

<details open><summary>🔧 Tool call — Read · `toolu_015t7Qyb6bPQp52accHUkxdc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_wikievents_pilot.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5054f091-6321-4ef3-9d33-127123285a09",
  "isSidechain": true,
  "agentId": "ac1babd70c733d821",
  "requestId": "req_011CbLmasLGJdU3rVFYYG6ii",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f57efb6c-048a-402e-901e-afb84eef0624",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ct66TgqyPs49MwYRnTkQ5f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23314,
      "cache_read_input_tokens": 7347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23314,
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

_source line 11 · 2026-05-24T04:33:39.697Z_

<details><summary>↩ Tool result · `toolu_015t7Qyb6bPQp52accHUkxdc`</summary>

```text
1	% Appendix: WikiEvents Event Extraction Pilot (moved from §5 main text)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\section{WikiEvents Event Extraction Pilot}
8	\label{app:wikievents-pilot}
9	
10	We apply OntoCoDec to event extraction (EE) on WikiEvents~\cite{li2021document,lu2021text2event} (56 event types, 80 roles, 27 entity types, 245 constraints; Appendix~\ref{app:wikievents}) without modification.
11	Violations extend to EV (event vocabulary), RoV (role vocabulary), and AC (argument constraint, analogous to DR).
12	
13	% ──────────────────────────────────────────
14	%  Table: WikiEvents three-model comparison (v3 final)
15	%  exp_ids: ee_{qwen,llama,mistral}_wikievents_{unconstrained,grammar_only,constrained_v3}
16	% ──────────────────────────────────────────
17	\begin{table}[h]
18	\centering
19	\small
20	\setlength{\tabcolsep}{2.8pt}
21	\resizebox{\columnwidth}{!}{%
22	\begin{tabular}{@{}ll rrrr rr@{}}
23	\toprule
24	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
25	& \multicolumn{2}{c}{\textbf{F1}} \\
26	\cmidrule(lr){3-6} \cmidrule(l){7-8}
27	\textbf{Model} & \textbf{Mode}
28	  & EV\,$\downarrow$ & RoV\,$\downarrow$ & AC & CF
29	  & Trig.\,$\uparrow$ & Ent.\,$\uparrow$ \\
30	\midrule
31	\multirow{3}{*}{Qwen3-8B}
32	  & Unconstr.\ & 24.0 & 74.9 & 0.3 & 0 & 11.8 & 0 \\
33	  & Grammar    & \textbf{0} & 76.1 & 8.2 & --- & --- & --- \\
34	  & S1    & \textbf{0} & \textbf{0} & 2.1 & 21.1 & 13.4 & 14.1 \\
35	\midrule
36	\multirow{3}{*}{\shortstack[l]{Llama\\3.1-8B}}
37	  & Unconstr.\ & 10.5 & 88.8 & 0.1 & 0 & 5.7 & 0 \\
38	  & Grammar    & \textbf{0} & 77.0 & 8.8 & --- & --- & --- \\
39	  & S1    & \textbf{0} & \textbf{0} & 3.8 & 17.2 & 7.5 & 17.6 \\
40	\midrule
41	\multirow{3}{*}{\shortstack[l]{Mistral\\7B}}
42	  & Unconstr.\ & 37.3 & 63.9 & 0 & 0 & 2.4 & 0 \\
43	  & Grammar    & \textbf{0} & 64.0 & 13.8 & --- & --- & --- \\
44	  & S1    & \textbf{0} & \textbf{0} & 1.3 & 14.9 & 3.9 & 11.7 \\
45	\bottomrule
46	\end{tabular}}%
47	\caption{WikiEvents EE results (zero-shot, $n{=}246$ documents).
48	Violation rates over parsed documents.
49	\textemdash{} indicates not applicable (grammar-only has no semantic-layer metrics).
50	F1 (\%). $n{=}20$ test documents for fine-tuning; MDE${\approx}\pm$5.0\,pp; results are directional only.}
51	\label{tab:wikievents}
52	\end{table}
53	
54	\paragraph{Results.}
55	Unconstrained EE produces extreme vocabulary violations (EV+RoV $>$85\%; Table~\ref{tab:wikievents}), with entity F1\,=\,0 because the parser cannot process off-schema output.
56	S1 eliminates EV and RoV across all models, validating tokenizer-agnostic design across byte-level BPE and SentencePiece.
57	Grammar-only eliminates EV but leaves RoV at 64--77\% and surfaces latent AC (8--14\%), consistent with DocRED's pattern (\S\ref{sec:docred-results}).
58	Residual AC (1.3--3.8\%) traces to semantically similar types; CF rises to 15--21\% due to EE's multi-argument entity reuse.
59	Unlike RE, EE shows measurable F1 gains: entity F1 0\%\,$\to$\,12--18\%, trigger F1 $+$1.5--1.8\,pp.
60	
61	% exp_ids: p1_ee_ft_qwen_wikievents_r5, p1_ee_ft_llama_wikievents_r5
62	\paragraph{Composability with fine-tuning (preliminary, $n{=}20$).}
63	On the full official test split (20 documents; 194/20/20~\cite{li2021document}), LoRA + S1 eliminates RoV (Qwen 38.31\%\,$\to$\,0\%, Llama 8.8\%\,$\to$\,0\%) and reduces AC to $\leq$0.8\%, with argument F1 within $\pm$1.1\,pp; trigger F1 shifts ($-$5.4/$-$0.6\,pp) have wide CIs consistent with n${=}$20.
64	CF remains low (0.77--1.18\%); per-document variance is high (Arg-F1 std/mean ${>}$\,0.5), confirming sufficient power to detect violation elimination but not small F1 differences (power analysis in Appendix~\ref{app:power-analysis-full}).
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f57efb6c-048a-402e-901e-afb84eef0624",
  "isSidechain": true,
  "promptId": "4ef057c6-ed80-4dae-9126-cc738ba56a17",
  "agentId": "ac1babd70c733d821",
  "type": "user",
  "uuid": "c564c706-85be-4228-9d05-3dd6c64dfd5a",
  "sourceToolAssistantUUID": "f57efb6c-048a-402e-901e-afb84eef0624",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-24T04:33:40.130Z_

<details open><summary>🔧 Tool call — Read · `toolu_012x65X3WMpjhUBNeNtUottL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_gollie_comparison.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c564c706-85be-4228-9d05-3dd6c64dfd5a",
  "isSidechain": true,
  "agentId": "ac1babd70c733d821",
  "requestId": "req_011CbLmasLGJdU3rVFYYG6ii",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "613490be-d2f9-4f0b-b2bd-a198fda718b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ct66TgqyPs49MwYRnTkQ5f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23314,
      "cache_read_input_tokens": 7347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23314,
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

_source line 13 · 2026-05-24T04:33:40.135Z_

<details><summary>↩ Tool result · `toolu_012x65X3WMpjhUBNeNtUottL`</summary>

```text
1	% Appendix: GoLLIE Comparison (D4 response)
2	% exp_ids: gollie_7b_scierc_zs_100, ontcodec_qwen_ft_s1_scierc_100, ontcodec_llama_ft_s1_scierc_100
3	
4	\section{GoLLIE Comparison}
5	\label{app:gollie-comparison}
6	
7	GoLLIE~\cite{sainz2024gollie} and OntoCoDec represent complementary paradigms for schema compliance in IE:
8	
9	\begin{itemize}[nosep,leftmargin=*]
10	\item \emph{Training-time internalization} (GoLLIE, KnowCoder): Schema knowledge is encoded into model parameters via annotation-guideline-aware training. This achieves compliance through learned generation patterns but cannot guarantee zero violations at inference time, and requires schema-specific retraining when ontologies evolve.
11	\item \emph{Runtime constraint enforcement} (OntoCoDec): Schema constraints are compiled into decoding-time masks applied to any generative model. This provides formal enforcement without schema-specific training, but operates per-triple and cannot resolve cross-triple type consistency (CF) within a single pass.
12	\end{itemize}
13	
14	The two approaches are orthogonal: OntoCoDec can be composed with GoLLIE or similar training-based systems to provide runtime enforcement guarantees atop learned schema compliance.
15	Direct numerical comparison is methodologically constrained by incompatible evaluation settings (code-style schema encoding vs.\ natural language prompting, different model families and sizes); a controlled comparison would require running both approaches on the same model with matched prompting, which we leave to future work.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "613490be-d2f9-4f0b-b2bd-a198fda718b7",
  "isSidechain": true,
  "promptId": "4ef057c6-ed80-4dae-9126-cc738ba56a17",
  "agentId": "ac1babd70c733d821",
  "type": "user",
  "uuid": "7aadee1e-f993-4735-833d-327005369295",
  "sourceToolAssistantUUID": "613490be-d2f9-4f0b-b2bd-a198fda718b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-24T04:33:45.433Z_

Now let me read the rest of the GoLLIE comparison file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7aadee1e-f993-4735-833d-327005369295",
  "isSidechain": true,
  "agentId": "ac1babd70c733d821",
  "requestId": "req_011CbLmbVsDFpAqfU5R2aAx7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57ac9e3d-8c57-4df1-ab37-3878dbc2e07e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UnCP99M8W4EXfn7MgmwE11",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8494,
      "cache_read_input_tokens": 30661,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8494,
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

_source line 15 · 2026-05-24T04:33:47.240Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KCsJytAqEZMQFXi7bFwGFQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_gollie_comparison.tex",
  "offset": 16
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57ac9e3d-8c57-4df1-ab37-3878dbc2e07e",
  "isSidechain": true,
  "agentId": "ac1babd70c733d821",
  "requestId": "req_011CbLmbVsDFpAqfU5R2aAx7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c40ef411-a352-4151-a11e-382103fb4c27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UnCP99M8W4EXfn7MgmwE11",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8494,
      "cache_read_input_tokens": 30661,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8494
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 30661,
          "cache_creation_input_tokens": 8494,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8494,
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

_source line 16 · 2026-05-24T04:33:47.244Z_

<details><summary>↩ Tool result · `toolu_01KCsJytAqEZMQFXi7bFwGFQ`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (16). The file has 16 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c40ef411-a352-4151-a11e-382103fb4c27",
  "isSidechain": true,
  "promptId": "4ef057c6-ed80-4dae-9126-cc738ba56a17",
  "agentId": "ac1babd70c733d821",
  "type": "user",
  "uuid": "8a6f9d37-765c-41cf-9f18-2db9281617fb",
  "sourceToolAssistantUUID": "c40ef411-a352-4151-a11e-382103fb4c27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-24T04:35:52.872Z_

The GoLLIE file is only 16 lines and contains no numerical data tables — only qualitative discussion. Now I'll do the systematic audit.

---

## AUDIT REPORT

### File 1: `appendix_zs_crossmodel.tex`

**SciERC rows:**

| Line | Number | Exp ID | Registry | Verdict |
|---|---|---|---|---|
| 22 | Qwen (U): DR=15.37, RV=1.39, ET=0.40, CF=0.08, R-F1=8.23 | phase2_scierc_unconstrained | DR=15.37%, RV=1.39%, ET=0.40%, CF=0.08%, R_F1=8.23% | ✅ all match |
| 23 | Qwen (S1): DR=0.93, RV=0, ET=0, CF=9.90, R-F1=8.36 | phase2_scierc_full_s1 | DR=0.93%, CF=9.90%, R_F1=8.36% | ✅ |
| 25 | Llama (U): DR=13.34, RV=0.55, ET=0, CF=0.24, R-F1=2.68 | llama_scierc_unconstrained | DR=13.34%, RV=0.55%, R_F1=2.68% | ❌ **CF=0.24 in paper, but registry says CF=6 (count, not rate)**. The registry value "CF=6" is a count, not a percentage. Need clarification — if 6 is a count and total triples denominator yields 0.24%, this may be correct but cannot be verified from registry data as given. **Flagged as unverifiable.** |
| 26 | Llama (S1): DR=0.08, RV=0, ET=0, CF=6.56, R-F1=2.54 | llama_scierc_full_s1 | DR=0.08%, CF=6.56%, R_F1=2.54% | ✅ |
| 28 | Mistral (U): DR=56.94, RV=0, ET=1.50, CF=56.87, R-F1=3.66 | w6_mistral_scierc_unconstrained | DR=56.94%, ET=1.5%, CF=56.87%, R_F1=3.66% | ✅ |
| 29 | Mistral (S1): DR=13.40, RV=0, ET=0, CF=1.27, R-F1=3.67 | w6_mistral_scierc_constrained | DR=13.40%, CF=1.27%, R_F1=3.67% | ✅ |

**DocRED rows:**

| Line | Number | Exp ID | Registry | Verdict |
|---|---|---|---|---|
| 32 | Qwen (U): DR=18.46, RV=29.66, ET=2.48, CF=0.10, R-F1=7.74 | phase2_docred_unconstrained | DR=18.46%, RV=29.66%, ET=2.48%, CF=0.10%, R_F1=7.74% | ✅ |
| 33 | Qwen (S1): DR=10.21, RV=0.03, ET=0, CF=2.57, R-F1=8.23 | phase2_docred_full_s1 | DR=10.21%, CF=2.57%, R_F1=8.23% | ✅ (RV=0.03 not in registry data provided but not contradicted) |
| 35 | Llama (U): DR=26.07, RV=16.03, ET=0.13, CF=0.17, R-F1=5.98 | llama_docred_unconstrained | DR=26.07%, RV=16.03%, ET=0.13%, CF=0.17%, R_F1=5.98% | ✅ |
| 36 | Llama (S1): DR=2.55, RV=0, ET=0, CF=12.02, R-F1=6.27 | llama_docred_full_s1 (mt6144) | DR=2.57%, CF=12.13%, R_F1=6.25% | ❌ **Three mismatches: DR=2.55 (paper) vs 2.57 (registry); CF=12.02 (paper) vs 12.13 (registry); R-F1=6.27 (paper) vs 6.25 (registry)** |
| 38 | Mistral (U): DR=57.42, RV=42.35, ET=7.58, CF=24.78, R-F1=4.34 | w6_mistral_docred_unconstrained | DR=57.42%, RV=42.35%, ET=7.58%, CF=24.78%, R_F1=4.34% | ✅ |
| 39 | Mistral (S1): DR=33.20, RV=0, ET=0, CF=0.19, R-F1=5.52 | w6_mistral_docred_constrained | DR=33.20%, CF=0.19%, R_F1=5.52% | ✅ |

**Prose claims in appendix_zs_crossmodel.tex:**

- [Line 51] "DR drops 76--99% on SciERC": Registry says Qwen 93.9%, Llama 99.4%, Mistral 76.5% → range 76.5–99.4% → "76–99%" ✅
- [Line 51] "42--90% on DocRED": Registry says Qwen 44.7%, Llama 90.1%, Mistral 42.2% → range 42.2–90.1% → "42–90%" ✅
- [Line 52] "CF...up to 12.02%": Paper uses 12.02% but registry says 12.13% → ❌ **should be 12.13%**
- [Line 52] "56.87%→1.27%": Registry confirms both → ✅
- [Line 53] "15--74% rejection rates": Registry shows posthoc scierc reject=16.8%, docred reject=48.1%, mistral_docred reject=73.73%. Range 16.8–73.73% → "15–74%" is approximate. ✅ (rounded range)
- [Line 58] "DR from 18.46% to 10.21% (↓45%)": Registry says 44.7% reduction → "45%" ❌ **Paper says 45%, registry says 44.7%** (rounding acceptable? 44.7 rounds to 45 — borderline, but the paper uses integer rounding here, so this is arguably acceptable)
- [Line 58] "RV 29.66%→0.03%": 29.66% matches registry. 0.03% not in provided registry data but appears in the table. ✅ (consistent with own table)
- [Line 58] "R-F1 +0.49 pp": 8.23 - 7.74 = 0.49 → ✅
- [Line 59] "45% vs 94% on SciERC": Registry says 93.9% for Qwen SciERC → "94%" ✅ (rounded)
- [Line 60] "18.46%→26.17%": 26.17% is the grammar-only result, not in the provided registry data. **Cannot verify.**

---

### File 2: `appendix_downstream_analysis.tex`

This file contains Table `tab:lucky-violations-detail` with TP counts, lucky violation counts, and recall drops. **None of these numbers (461, 4, 0.87%, 0.41pp, 467, 5, 1.07%, 0.51pp, 5746, 1, 0.02%, 0.01pp, 6226, 1, 0.02%, 0.01pp) appear in the provided registry data.** Cannot verify — these appear to come from a separate downstream analysis not included in the registry excerpt provided.

- [Line 26] "constraints eliminate 164 schema-violating predictions but only 1 of them is actually correct": Not in registry data. **Cannot verify.**

**Internal consistency checks:**
- 4/461 = 0.868% ≈ 0.87% ✅
- 5/467 = 1.071% ≈ 1.07% ✅
- 1/5746 = 0.0174% ≈ 0.02% ✅
- 1/6226 = 0.0161% ≈ 0.02% ✅

Internal math is consistent.

---

### File 3: `appendix_tcr.tex`

**SciERC TCR table (lines 25-32):**

The TCR data comes from d065_tcr_pilot / d065_tcr_full. The registry says "All CF eliminated across 10 configs. DR delta max on SciERC=0.28pp." The table shows Post CF=0 for all rows ✅ and the caption says "DR increases ≤0.28 pp" ✅.

Specific DR numbers in the table (Pre/Post columns): Most of these granular per-config numbers are not in the provided registry excerpt. The Pre-DR values should match the corresponding S1 experiments:

- [Line 26] Qwen ZS Pre-DR=0.93: matches phase2_scierc_full_s1 DR=0.93% ✅
- [Line 26] Qwen ZS Pre-CF=9.75: Registry says CF=9.90% for phase2_scierc_full_s1 → ❌ **CF=9.75 in paper vs 9.90 in registry**. (Note: TCR Pre-CF may differ from S1 CF if computed on different subset. Flagged.)
- [Line 27] Llama ZS Pre-DR=0.08: matches llama_scierc_full_s1 DR=0.08% ✅
- [Line 27] Llama ZS Pre-CF=6.40: Registry says llama_scierc_full_s1 CF=6.56% → ❌ **CF=6.40 in paper vs 6.56 in registry**
- [Line 28] Mistral ZS Pre-DR=13.36: Registry says w6_mistral_scierc_constrained DR=13.40% → ❌ **DR=13.36 in paper vs 13.40 in registry**
- [Line 28] Mistral ZS Pre-CF=0.67: Registry says w6_mistral_scierc_constrained CF=1.27% → ❌ **CF=0.67 in paper vs 1.27 in registry**
- [Line 31] Qwen LoRA Pre-CF=1.19: Registry says w5_lora_scierc_constrained_eval CF=1.18% → ❌ **CF=1.19 in paper vs 1.18 in registry** (very small discrepancy)
- [Line 31] Qwen LoRA Pre-DR=0: Registry says w5_lora_scierc_constrained_eval DR=0% ✅
- [Line 32] Llama LoRA Pre-CF=0.46: Registry says w5_llama_lora_scierc_constrained_eval CF=0.46% ✅
- [Line 32] Llama LoRA Pre-DR=0.09: Registry says w5_llama_lora_scierc_constrained_eval DR=0.09% ✅

**DocRED TCR table (lines 56-63):**

- [Line 57] Qwen ZS Pre-DR=10.21: matches phase2_docred_full_s1 DR=10.21% ✅
- [Line 57] Qwen ZS Pre-CF=13.11: Registry says phase2_docred_full_s1 CF=2.57% → ❌ **CF=13.11 in paper vs 2.57 in registry**. (Note: TCR Pre-CF may be a different metric or computed differently. Very large discrepancy — likely these are different measurements, with TCR counting entity-level CF rather than triple-level CF.)
- [Line 58] Llama ZS Pre-DR=2.55: Registry says llama_docred_full_s1 DR=2.57% → ❌ **DR=2.55 in paper vs 2.57 in registry** (same discrepancy as in table 1)
- [Line 58] Llama ZS Pre-CF=23.71: Registry says llama_docred_full_s1 CF=12.13% → ❌ **CF=23.71 in paper vs 12.13 in registry** (again likely different CF measurement level)
- [Line 59] 70B Pre-DR=0, CF=11.61: Not in provided registry data (no 70B experiment in provided data). **Cannot verify.**
- [Line 59] 70B Post-DR=4.20: Registry says d065_tcr_full docred_zs_70b_dr_delta=4.2 → 0+4.2=4.2 ✅
- [Line 62] Qwen LoRA Pre-CF=0.42: Registry says w5_qwen_docred_lora_constrained_eval CF=0.41% → ❌ **CF=0.42 in paper vs 0.41 in registry**
- [Line 62] Qwen LoRA Pre-DR=0.01: Registry says w5_qwen_docred_lora_constrained_eval DR=0.01% ✅
- [Line 63] Llama LoRA Pre-CF=0.36: Registry says w5_llama_docred_lora_constrained_eval CF=0.21% → ❌ **CF=0.36 in paper vs 0.21 in registry**
- [Line 63] Llama LoRA Pre-DR=0.21: Registry says w5_llama_docred_lora_constrained_eval DR=0.21% ✅

**TCR Prose claims:**

- [Line 39] "DR increases ≤0.28 pp": Registry d065_tcr_pilot SciERC DR delta max=0.28pp ✅
- [Line 67] "up to +9.38 pp for Llama": 11.93 - 2.55 = 9.38 ✅ (internally consistent, though base DR=2.55 vs registry 2.57)
- [Line 67] "up to -5.98 pp for 70B": matches table row ✅ (internal consistency)
- [Line 76] "≤1.78 pp in zero-shot": Looking at SciERC ZS ΔE-F1: Qwen -1.29, Llama -1.78, Mistral +0.05 → max magnitude = 1.78 ✅
- [Line 76] "≤0.75 pp under LoRA": SciERC LoRA ΔE-F1: Qwen -0.75, Llama -0.18 → max = 0.75 ✅
- [Line 78] "Llama: 2.55%→11.93%": internal table match ✅ (but base 2.55 vs registry 2.57)
- [Line 78] "70B: 0%→4.20%": internal table match ✅
- [Line 79] "0.36--0.42%": internal table match ✅ (but both CF values differ from registry)
- [Line 83] "1.39×" beam search latency: Not in provided registry. **Cannot verify.**

---

### File 4: `appendix_wikievents_pilot.tex`

**WikiEvents table (lines 31-44):**

| Line | Number | Exp ID | Registry | Verdict |
|---|---|---|---|---|
| 32 | Qwen Unconstr: EV=24.0, RoV=74.9, AC=0.3, CF=0 | ee_qwen_wikievents_unconstrained | EV=24%, RoV=74.9%, CF=0 | ✅ (AC=0.3 not in registry but not contradicted) |
| 34 | Qwen S1: EV=0, RoV=0, AC=2.1, CF=21.1 | ee_qwen_wikievents_constrained_v3 | EV=0%, RoV=0%, CF=21.1% | ✅ (AC=2.1 not provided but not contradicted) |
| 37 | Llama Unconstr: EV=10.5, RoV=88.8, AC=0.1, CF=0 | ee_llama_wikievents_unconstrained | EV=10.5%, RoV=88.8%, CF=0 | ✅ |
| 39 | Llama S1: EV=0, RoV=0, AC=3.8, CF=17.2 | ee_llama_wikievents_constrained_v3 | EV=0%, RoV=0%, CF=17.2% | ✅ |
| 42 | Mistral Unconstr: EV=37.3, RoV=63.9, AC=0, CF=0 | ee_mistral_wikievents_unconstrained | EV=37.3%, RoV=63.9%, CF=0 | ✅ |
| 44 | Mistral S1: EV=0, RoV=0, AC=1.3, CF=14.9 | ee_mistral_wikievents_constrained_v3 | EV=0%, RoV=0%, CF=14.9% | ✅ |

**WikiEvents prose:**

- [Line 55] "EV+RoV >85%": Qwen 24+74.9=98.9, Llama 10.5+88.8=99.3, Mistral 37.3+63.9=101.2 → all >85% ✅
- [Line 57] "RoV at 64--77%": Grammar rows show 76.1, 77.0, 64.0 → range 64.0-77.0 ✅
- [Line 57] "surfaces latent AC (8--14%)": Grammar rows show 8.2, 8.8, 13.8 → "8--14%" ✅
- [Line 58] "Residual AC (1.3--3.8%)": S1 rows show Qwen 2.1, Llama 3.8, Mistral 1.3 → range 1.3-3.8 ✅
- [Line 58] "CF rises to 15--21%": S1 CF: 21.1, 17.2, 14.9 → range 14.9-21.1. Paper says "15--21%". ❌ **Lower bound is 14.9%, not 15%** (rounding 14.9→15 is aggressive)
- [Line 59] "entity F1 0%→12--18%": S1 entity F1: Qwen 14.1, Llama 17.6, Mistral 11.7 → range 11.7-17.6. Paper says "12--18%". ❌ **Lower bound is 11.7%, not 12%** (rounding 11.7→12 is aggressive)
- [Line 59] "trigger F1 +1.5--1.8 pp": Unconstr trigger: Qwen 11.8, Llama 5.7, Mistral 2.4. S1 trigger: 13.4, 7.5, 3.9. Deltas: +1.6, +1.8, +1.5 → "1.5--1.8" ✅
- [Line 63] "Qwen 38.31%→0%": Registry p1_ee_ft_composability_r5 unconstrained rov=38.31%, full_s1 rov=0% ✅
- [Line 63] "Llama 8.8%→0%": Paper says unconstrained Llama RoV=8.8%. Registry p1_ee_ft_composability_r5 doesn't specify per-model FT RoV for Llama, but ZS Llama unconstr RoV=88.8%. The "8.8%" for FT Llama is not in registry data provided. **Cannot verify** (likely a different FT experiment).
- [Line 63] "AC to ≤0.8%": Registry says p1_ee_ft_composability_r5 full_s1 ac=0% → ≤0.8% is a weaker claim, technically consistent ✅
- [Line 47] "n=246": Registry shows parse=218/246, 206/246 etc. Total docs = 246 ✅

**Parse counts not shown in table but registry has them:**
- Registry: Qwen unconstr parse=218/246, Qwen constrained parse=206/246; Llama unconstr parse=226/246, Llama constrained parse=207/246; Mistral unconstr parse=194/246, Mistral constrained parse=218/246. These are not in the table but the table notes "Violation rates over parsed documents" which is consistent.

---

### File 5: `appendix_gollie_comparison.tex`

This file contains **no numerical data** — it is purely qualitative text comparing GoLLIE and OntoCoDec paradigms. No numbers to verify.

---

## SUMMARY OF ALL DISCREPANCIES

### Confirmed mismatches (paper vs registry):

1. **[appendix_zs_crossmodel.tex:36] Llama DocRED S1 DR=2.55** → registry says **2.57** ❌
2. **[appendix_zs_crossmodel.tex:36] Llama DocRED S1 CF=12.02** → registry says **12.13** ❌
3. **[appendix_zs_crossmodel.tex:36] Llama DocRED S1 R-F1=6.27** → registry says **6.25** ❌
4. **[appendix_zs_crossmodel.tex:52] "up to 12.02%"** → should be **12.13%** (follows from #2) ❌
5. **[appendix_tcr.tex:26] Qwen SciERC ZS Pre-CF=9.75** → registry phase2_scierc_full_s1 CF=**9.90** ❌
6. **[appendix_tcr.tex:27] Llama SciERC ZS Pre-CF=6.40** → registry llama_scierc_full_s1 CF=**6.56** ❌
7. **[appendix_tcr.tex:28] Mistral SciERC ZS Pre-DR=13.36** → registry w6_mistral_scierc_constrained DR=**13.40** ❌
8. **[appendix_tcr.tex:28] Mistral SciERC ZS Pre-CF=0.67** → registry w6_mistral_scierc_constrained CF=**1.27** ❌
9. **[appendix_tcr.tex:31] Qwen LoRA SciERC Pre-CF=1.19** → registry w5_lora_scierc_constrained_eval CF=**1.18** ❌ (minor)
10. **[appendix_tcr.tex:57] Qwen DocRED ZS Pre-CF=13.11** → registry phase2_docred_full_s1 CF=**2.57** ❌ (very large gap — likely different CF measurement granularity: entity-level vs triple-level)
11. **[appendix_tcr.tex:58] Llama DocRED ZS Pre-DR=2.55** → registry llama_docred_full_s1 DR=**2.57** ❌ (same as #1)
12. **[appendix_tcr.tex:58] Llama DocRED ZS Pre-CF=23.71** → registry llama_docred_full_s1 CF=**12.13** ❌ (very large gap — same entity-level vs triple-level issue as #10)
13. **[appendix_tcr.tex:62] Qwen DocRED LoRA Pre-CF=0.42** → registry w5_qwen_docred_lora_constrained_eval CF=**0.41** ❌ (minor)
14. **[appendix_tcr.tex:63] Llama DocRED LoRA Pre-CF=0.36** → registry w5_llama_docred_lora_constrained_eval CF=**0.21** ❌

### Aggressive rounding (borderline):

15. **[appendix_wikievents_pilot.tex:58] "CF rises to 15--21%"** — actual range is 14.9–21.1%, so lower bound 14.9 rounded to 15 (borderline)
16. **[appendix_wikievents_pilot.tex:59] "entity F1 0%→12--18%"** — actual range is 11.7–17.6%, so bounds rounded (borderline)
17. **[appendix_zs_crossmodel.tex:58] "↓45%"** — registry says 44.7% reduction (acceptable rounding)

### Likely measurement-level differences (not true errors but need clarification):

Items #5-8 and #10, #12, #14 in the TCR table show CF values that differ systematically from the cross-model table. The TCR experiment likely computes CF at a different granularity (entity-level type conflicts vs triple-level CF rate). **These are not necessarily errors but the paper should clarify the measurement difference**, especially since:
- TCR SciERC Mistral Pre-CF=0.67 vs cross-model table CF=1.27 (0.60pp gap)
- TCR DocRED Qwen Pre-CF=13.11 vs cross-model table CF=2.57 (10.54pp gap)
- TCR DocRED Llama Pre-CF=23.71 vs cross-model table CF=12.13 (11.58pp gap)

### Flagged (unverifiable from provided registry):

- [appendix_zs_crossmodel.tex:25] Llama SciERC CF=0.24 — registry gives CF=6 (count), cannot verify rate
- [appendix_downstream_analysis.tex] All lucky violation numbers (TP counts, lucky counts, recall drops) — not in registry
- [appendix_tcr.tex:59] 70B experiment — not in provided registry
- [appendix_tcr.tex:83] Beam search 1.39× latency — not in provided registry
- [appendix_wikievents_pilot.tex:63] Llama FT RoV=8.8% — not in provided registry

### Clean files:

- `appendix_gollie_comparison.tex` — no numbers, nothing to verify
- `appendix_downstream_analysis.tex` — internal math checks out; source data not in provided registry

### Critical items requiring immediate fix:

The three Llama DocRED S1 values in the cross-model table (items #1-3) are the most concerning because they appear in the main results table and are clearly wrong vs registry: **DR 2.55→2.57, CF 12.02→12.13, R-F1 6.27→6.25**. The prose reference to "up to 12.02%" (#4) follows from the same error.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a6f9d37-765c-41cf-9f18-2db9281617fb",
  "isSidechain": true,
  "agentId": "ac1babd70c733d821",
  "requestId": "req_011CbLmc2JYLTGrEGAveswUM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f71ccbb8-89e0-49ae-b5a2-17d61cda2d00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RxeT9zZf6dDuaVKGWAN4ZP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 174,
      "cache_read_input_tokens": 39155,
      "output_tokens": 7040,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 174
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7040,
          "cache_read_input_tokens": 39155,
          "cache_creation_input_tokens": 174,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 174,
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
