# Research conversation: Read ALL appendix LaTeX files from the paper and extract EVERY numerical value (percentages, F1, accuracy, p-values, eff

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 81
- **Recorded user turns:** 1
- **Tool calls:** 38
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aa2265d384aeafb01.jsonl`
- **Structured JSON:** [`2ea12080c80818c0f6cb.json`](../../sessions/2e/2ea12080c80818c0f6cb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

81 recorded events

### User

_source line 1 · 2026-05-25T20:38:24.161Z_

Read ALL appendix LaTeX files from the paper and extract EVERY numerical value (percentages, F1, accuracy, p-values, effect sizes, counts, etc.) along with context. For each number note: (1) file/line, (2) exact value, (3) what it measures.

Files are all under /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/. Read ALL files starting with "appendix_":
- appendix_ablation.tex
- appendix_confusion_matrix.tex
- appendix_cross_model_detail.tex
- appendix_cross_temp.tex
- appendix_dataset_stats.tex
- appendix_downstream.tex
- appendix_feature_correlation.tex
- appendix_generator_subsets.tex
- appendix_human_edit.tex
- appendix_prompt_type.tex
- appendix_qualitative_examples.tex
- appendix_temperature_stability.tex
- appendix_classifier.tex
- appendix_ddr_validation.tex
- appendix_iterative_comparison.tex
- appendix_qlora.tex
- appendix_feature_candidates.tex
- appendix_lofo.tex
- appendix_variance_decomposition.tex
- appendix_length.tex
- appendix_error_analysis.tex
- appendix_nll_distribution.tex
- appendix_9gen_scale.tex
- appendix_ddr_causality.tex
- appendix_convergence.tex
- appendix_instruct.tex
- appendix_seed_control.tex
- appendix_transfer.tex
- appendix_tost.tex
- appendix_tost_bootstrap.tex
- appendix_domain.tex
- appendix_finer_depth.tex
- appendix_decoding_strategy.tex
- appendix_feature_distributions.tex
- appendix_ai_assistants.tex
- ethics.tex
- related_work.tex

Return a complete structured inventory grouped by file. Be exhaustive - don't skip any number.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "a3966e67-69a0-40d9-9f80-aeae5f36aa8f",
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

_source line 2 · 2026-05-25T20:38:24.164Z_

```json
{
  "parentUuid": "a3966e67-69a0-40d9-9f80-aeae5f36aa8f",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
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
  "uuid": "8d1beceb-8fe3-4f35-b46f-6488c1039cab",
  "timestamp": "2026-05-25T20:38:24.164Z",
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

_source line 3 · 2026-05-25T20:38:27.441Z_



I'll read all the appendix files systematically. Let me start by reading them in parallel batches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d1beceb-8fe3-4f35-b46f-6488c1039cab",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPvyHq5t92TK9Th4dJme",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c9a10d4-76d9-441f-bae3-79e20c1f1588",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YK13M7MYPPP6A7yNDkoNGq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25482,
      "cache_read_input_tokens": 9183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25482,
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

_source line 4 · 2026-05-25T20:38:28.563Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0192icBPpw4piAm9JPa2STtW`</summary>

```json
{
  "pattern": "appendix_*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c9a10d4-76d9-441f-bae3-79e20c1f1588",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPvyHq5t92TK9Th4dJme",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf226ff7-3b61-4c5b-a176-cc1d42286d61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YK13M7MYPPP6A7yNDkoNGq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25482,
      "cache_read_input_tokens": 9183,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 25482
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 130,
          "cache_read_input_tokens": 9183,
          "cache_creation_input_tokens": 25482,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 25482,
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

_source line 5 · 2026-05-25T20:38:28.575Z_

<details><summary>↩ Tool result · `toolu_0192icBPpw4piAm9JPa2STtW`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ablation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_confusion_matrix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_temp.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_dataset_stats.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_downstream.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_correlation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_generator_subsets.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_human_edit.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_prompt_type.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qualitative_examples.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_temperature_stability.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_distributions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ai_assistants.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ddr_validation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_iterative_comparison.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_candidates.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_lofo.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_variance_decomposition.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_length.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_nll_distribution.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_9gen_scale.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ddr_causality.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_convergence.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_seed_control.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_transfer.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_tost.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_tost_bootstrap.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_domain.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_finer_depth.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_decoding_strategy.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf226ff7-3b61-4c5b-a176-cc1d42286d61",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "2d6700cb-5ee3-4494-852e-a9094da38fc4",
  "sourceToolAssistantUUID": "cf226ff7-3b61-4c5b-a176-cc1d42286d61",
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

_source line 6 · 2026-05-25T20:38:34.354Z_

Let me read all files in parallel batches. I'll use the base path `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/` for brevity.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d6700cb-5ee3-4494-852e-a9094da38fc4",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPvych9ULhCCCo2gQdCJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "217cb626-9b26-4748-ab6f-f947ae605a2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8UTxZxSJzRKzEkvd1BY1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2520,
      "cache_read_input_tokens": 34665,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2520,
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

_source line 7 · 2026-05-25T20:38:35.457Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YXZYGa91xQ1TVtupzgheUj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ablation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "217cb626-9b26-4748-ab6f-f947ae605a2e",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPvych9ULhCCCo2gQdCJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8607ca33-7e53-44df-8544-0fe84c3cfe67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8UTxZxSJzRKzEkvd1BY1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2520,
      "cache_read_input_tokens": 34665,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2520,
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

### Tool result

_source line 8 · 2026-05-25T20:38:35.463Z_

<details><summary>↩ Tool result · `toolu_01YXZYGa91xQ1TVtupzgheUj`</summary>

```text
1	This appendix presents feature ablation results supporting the complementarity analysis in \S\ref{sec:results-differential}.
2	
3	\begin{table}[t]
4	\centering
5	\footnotesize
6	\caption{Feature ablation (8-gen, 10-fold stratified CV, 3-class). Full $>$ surface (+8.5\,pp) and Full $>$ reference (+6.0\,pp) confirms complementarity.}
7	\label{tab:ablation}
8	\begingroup
9	\renewcommand{\arraystretch}{1.15}
10	\begin{tabular}{lcc}
11	\toprule
12	\textbf{Feature set} & \textbf{F1} & \textbf{Top feature (imp.)} \\
13	\midrule
14	Full (7 features)     & 0.773 & hapax\_ratio (0.35) \\
15	Surface only (2)      & 0.688 & hapax\_ratio (0.41) \\
16	Reference only (5)    & 0.713 & entropy\_mean (0.27) \\
17	\bottomrule
18	\end{tabular}
19	\endgroup
20	\end{table}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8607ca33-7e53-44df-8544-0fe84c3cfe67",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "45d2d8c5-ebc5-415e-8b8e-d6e502e08ecc",
  "sourceToolAssistantUUID": "8607ca33-7e53-44df-8544-0fe84c3cfe67",
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

_source line 9 · 2026-05-25T20:38:35.790Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UDCzEE9gyavaukg2mvKbXS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_confusion_matrix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45d2d8c5-ebc5-415e-8b8e-d6e502e08ecc",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPvych9ULhCCCo2gQdCJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3acaaf65-19ec-4145-a0a1-8204864fcd50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8UTxZxSJzRKzEkvd1BY1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2520,
      "cache_read_input_tokens": 34665,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2520,
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

### Tool result

_source line 10 · 2026-05-25T20:38:35.798Z_

<details><summary>↩ Tool result · `toolu_01UDCzEE9gyavaukg2mvKbXS`</summary>

```text
1	Table~\ref{tab:confusion} reports the aggregated confusion matrix from the original six-generator subset (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B) under leave-one-generator-out (LOGO) evaluation, collapsed to three ordinal classes: gen-0 (human), gen-1 (first-generation), and gen-2+ (depth $\geq$ 2).
2	The later-added Llama-3.2-3B and Mistral-7B-v0.3 are evaluated in the full 8-generator LOGO results (Table~\ref{tab:logo-results}).
3	
4	\begin{table}[ht]
5	\centering
6	\small
7	\caption{Aggregated 3-class confusion matrix from 6-generator LOGO evaluation ($N=27{,}529$). Each cell shows count and row-normalized percentage. Gen-0 is near-perfectly identified. Gen-1 errors are asymmetric: misclassification as gen-2+ (18.8\%) is 3$\times$ more frequent than as gen-0 (6.2\%). Gen-1 text already carries detectable recursive distortion.}
8	\label{tab:confusion}
9	\resizebox{\linewidth}{!}{%
10	\begin{tabular}{lccc}
11	\toprule
12	& \textbf{Pred gen-0} & \textbf{Pred gen-1} & \textbf{Pred gen-2+} \\
13	\midrule
14	\textbf{True gen-0} & 5{,}937 (99.4\%) & 35 (0.6\%) & 0 (0.0\%) \\
15	\textbf{True gen-1} & 368 (6.2\%) & 4{,}437 (75.0\%) & 1{,}113 (18.8\%) \\
16	\textbf{True gen-2+} & 464 (3.0\%) & 3{,}646 (23.3\%) & 11{,}529 (73.7\%) \\
17	\bottomrule
18	\end{tabular}}
19	\end{table}
20	
21	Figure~\ref{fig:confusion-heatmap} provides a heatmap visualization of the confusion matrix.
22	The row-normalized view highlights near-perfect gen-0 classification (99.4\% recall), gen-1 confusion primarily with gen-2+ (18.8\%) rather than gen-0 (6.2\%), and gen-2+ misclassification predominantly into gen-1 (23.3\%), consistent with DDR predictions.
23	
24	\begin{figure}[H]
25	\centering
26	\includegraphics[width=\columnwidth, trim=0 0 344pt 0, clip]{fig_appendix_confusion.pdf}\\[-2pt]
27	{\small (a) Raw counts}
28	\caption{3-class LOGO confusion matrix ($N$\,=\,27{,}529). Gen-0 achieves near-perfect classification; the primary confusion axis is gen-1 $\leftrightarrow$ gen-2+.}
29	\label{fig:confusion-heatmap}
30	\end{figure}
31	
32	\begin{figure}[H]
33	\addtocounter{figure}{-1}
34	\centering
35	\includegraphics[width=\columnwidth, trim=344pt 0 0 0, clip]{fig_appendix_confusion.pdf}\\[-2pt]
36	{\small (b) Row-normalized recall percentages}
37	\caption{(Continued) Row-normalized view of the confusion matrix.}
38	\end{figure}
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3acaaf65-19ec-4145-a0a1-8204864fcd50",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "ac07a0d9-8d3f-4756-a18d-0989a24bf84e",
  "sourceToolAssistantUUID": "3acaaf65-19ec-4145-a0a1-8204864fcd50",
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

_source line 11 · 2026-05-25T20:38:36.261Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Wi7uhSCTeKiwqjjhDPFH13`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac07a0d9-8d3f-4756-a18d-0989a24bf84e",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPvych9ULhCCCo2gQdCJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5640008a-db72-458f-ac10-16e3c62a6796",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8UTxZxSJzRKzEkvd1BY1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2520,
      "cache_read_input_tokens": 34665,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2520,
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

### Tool result

_source line 12 · 2026-05-25T20:38:36.266Z_

<details><summary>↩ Tool result · `toolu_01Wi7uhSCTeKiwqjjhDPFH13`</summary>

```text
1	This appendix reports per-generator breakdowns for the cross-model chain evaluation described in \S\ref{sec:results-classification}.
2	
3	\begin{table}[ht]
4	\centering
5	\footnotesize
6	\caption{Cross-model chain per-class performance (generator-level leave-one-out, $N$\,=\,2{,}964, $n_{\text{generators}}$\,=\,5: Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B). Macro F1\,=\,0.831 under class balancing; under natural class distribution, macro F1\,=\,0.789. Binary F1 (gen-1 vs.\ gen-2+)\,=\,0.830 (95\% CI [.818, .841], case-level bootstrap, $n$\,=\,2{,}000). Cross-model chains avoid the gen-0 seed sharing issue present in single-generator LOGO.}
7	\label{tab:cross-model-perclass}
8	\begin{tabular}{lcccc}
9	\toprule
10	\textbf{Class} & \textbf{Prec.} & \textbf{Rec.} & \textbf{F1} & \textbf{95\% CI} \\
11	\midrule
12	gen-0   & 0.921 & 0.948 & 0.935 & [.923, .946] \\
13	gen-1   & 0.737 & 0.803 & 0.768 & [.748, .788] \\
14	gen-2+  & 0.842 & 0.742 & 0.789 & [.768, .809] \\
15	\midrule
16	\textbf{Macro} & --- & --- & \textbf{0.831} & [.817, .844] \\
17	\bottomrule
18	\end{tabular}
19	\end{table}
20	
21	\paragraph{Variance decomposition.}
22	A two-way ANOVA (generator $\times$ depth) on cross-model chain features ($n{=}3{,}778$, depths 1--4) confirms that generator identity contributes negligible variance: partial $\eta^2_{\text{gen}} < 1\%$ for all seven features (range 0.05\%--0.90\%, mean 0.37\%), while depth accounts for 15.3\%--29.9\% of variance in drifting features.
23	The generator$\times$depth interaction is also $< 1\%$.
24	This confirms that the F1\,=\,0.830 cross-model advantage reflects depth signal rather than generator diversity accumulation: mixing generators across chain steps does not introduce a confounding generator-identity cue.
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5640008a-db72-458f-ac10-16e3c62a6796",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "55fc6400-95dc-4b69-abbe-0cf4baee3b07",
  "sourceToolAssistantUUID": "5640008a-db72-458f-ac10-16e3c62a6796",
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

_source line 13 · 2026-05-25T20:38:37.186Z_

<details open><summary>🔧 Tool call — Read · `toolu_014wp6zjqh3BLCjCicApGpE9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_temp.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55fc6400-95dc-4b69-abbe-0cf4baee3b07",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPvych9ULhCCCo2gQdCJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0403d84c-d791-48c7-90f5-d8f50cd266ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8UTxZxSJzRKzEkvd1BY1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2520,
      "cache_read_input_tokens": 34665,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2520,
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

### Tool result

_source line 14 · 2026-05-25T20:38:37.190Z_

<details><summary>↩ Tool result · `toolu_014wp6zjqh3BLCjCicApGpE9`</summary>

```text
1	Figure~\ref{fig:cross-temp} shows cross-temperature transfer results for the 6-generator LOGO pipeline.
2	We evaluate four train$\rightarrow$test temperature conditions using Qwen3-1.7B data regenerated at $t{=}1.0$ (remaining five generators retain $t{=}0.7$).\footnote{The $t{=}1.0$ data uses top-$p{=}0.95$ (vs.\ $p{=}0.9$ for other configurations); this difference may contribute to the observed degradation beyond the temperature effect alone.}
3	
4	\begin{figure}[H]
5	\centering
6	\includegraphics[width=\columnwidth]{fig_appendix_cross_temp.pdf}
7	\caption{Cross-temperature transfer evaluation (6-gen LOGO). (a) Overall F1 by train$\rightarrow$test temperature condition. Matched conditions (0.7$\rightarrow$0.7, 1.0$\rightarrow$1.0) outperform cross-temperature transfer, with 0.7$\rightarrow$1.0 showing the largest degradation ($-6.6$\,pp in 3-class F1). (b) Per-generator 3-class F1 heatmap: Qwen3-1.7B shows dramatic degradation under cross-temperature conditions (0.418) while other generators remain stable. The temperature mismatch disproportionately affects the generator whose data was regenerated.}
8	\label{fig:cross-temp}
9	\end{figure}
10	
11	Key observations from the cross-temperature analysis:
12	
13	\begin{enumerate}[nosep]
14	\item \textbf{Matched-temperature robustness}: Both $t{=}0.7$ and $t{=}1.0$ matched conditions yield comparable performance (3-class F1: 0.789 vs.\ 0.726), with the gap attributable to weaker depth signal at high temperature rather than classifier degradation.
15	
16	\item \textbf{Asymmetric transfer}: Training at $t{=}1.0$ and testing at $t{=}0.7$ (F1\,=\,0.791) transfers well, but the reverse (0.7$\rightarrow$1.0, F1\,=\,0.723) degrades. This asymmetry reflects the information structure: features learned from high-variance (high-temperature) data generalize to low-variance settings, but not vice versa.
17	
18	\item \textbf{Generator-specific vulnerability}: Qwen3-1.7B, the only generator with temperature-mismatched test data, drops to F1\,=\,0.418 under cross-temperature conditions while all other generators maintain F1 $>$ 0.76. This confirms that depth features are calibrated to the specific decoding regime.
19	
20	\item \textbf{Binary transfer for the mismatched generator}: For Qwen3-1.7B (the only generator with actual temperature mismatch), binary F1 drops from 0.948 to 0.713 under 0.7$\rightarrow$1.0 transfer but recovers in the reverse direction (1.0$\rightarrow$0.7: 0.948), consistent with the asymmetric pattern in Item 2. The aggregate binary range (0.900--0.958) is inflated by five generators whose data is identical across conditions.
21	\end{enumerate}
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0403d84c-d791-48c7-90f5-d8f50cd266ad",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "4c54199d-256c-4c48-ab97-ab62ac59f31f",
  "sourceToolAssistantUUID": "0403d84c-d791-48c7-90f5-d8f50cd266ad",
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

_source line 15 · 2026-05-25T20:38:37.659Z_

<details open><summary>🔧 Tool call — Read · `toolu_018QQhpxgaHGYy5Ee9L3NNkn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_dataset_stats.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c54199d-256c-4c48-ab97-ab62ac59f31f",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPvych9ULhCCCo2gQdCJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "492b0d02-f2d7-456f-98b7-e39bdb3b6ab7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8UTxZxSJzRKzEkvd1BY1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2520,
      "cache_read_input_tokens": 34665,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2520,
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

### Tool result

_source line 16 · 2026-05-25T20:38:37.662Z_

<details><summary>↩ Tool result · `toolu_018QQhpxgaHGYy5Ee9L3NNkn`</summary>

```text
1	\section{Dataset Statistics}
2	\label{app:dataset-stats}
3	
4	Table~\ref{tab:dataset-stats} reports per-generator sample counts after filtering (removing generation failures, exact duplicates, and passages shorter than 50 whitespace tokens).
5	Under the 3-class evaluation scheme, the dataset contains 7{,}963 gen-0 samples (21.5\%), 7{,}896 gen-1 (21.3\%), and 21{,}199 gen-2+ (57.2\%, combining depths 2--4).
6	The gen-2+ majority reflects the chain structure (three deeper depths per chain vs.\ one each for gen-0 and gen-1); class-balanced sampling is applied during evaluation.
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\caption[Per-generator sample counts]{Per-generator sample counts after filtering (8 generators, 5 families). Each generator starts from ${\sim}$1{,}000 shared Wikipedia seeds and produces chains of depth 4 (5 texts per chain). Attrition varies by generator due to differing generation failure rates.\protect\footnotemark}
12	\label{tab:dataset-stats}
13	\begin{tabular}{llcc}
14	\toprule
15	\textbf{Generator} & \textbf{Family} & \textbf{Params} & \textbf{Samples} \\
16	\midrule
17	Pythia-1B       & Pythia  & 1.0B & 4{,}555 \\
18	Pythia-2.8B     & Pythia  & 2.8B & 4{,}609 \\
19	OLMo-2-1B      & OLMo    & 1.5B & 4{,}713 \\
20	Qwen3-0.6B     & Qwen    & 0.6B & 4{,}538 \\
21	Qwen3-1.7B     & Qwen    & 1.7B & 4{,}617 \\
22	Qwen3-8B       & Qwen    & 8.2B & 4{,}497 \\
23	Llama-3.2-3B   & Llama   & 3.2B & 4{,}680 \\
24	Mistral-7B-v0.3 & Mistral & 7.0B & 4{,}849 \\
25	\midrule
26	\multicolumn{3}{l}{\textbf{Total}} & \textbf{37{,}058} \\
27	\bottomrule
28	\end{tabular}
29	\end{table}
30	\footnotetext{Table~\ref{tab:baselines} evaluates on a subset of 34{,}131 samples for which all detector scores (FastDetectGPT, Binoculars, LD-Score, Avg-LogProb) are available.}
31	
32	Figure~\ref{fig:violin} shows the full distribution of each feature across five generation depths (0--4), pooled across all eight generators ($N$\,=\,37{,}058).
33	The violin plots confirm the DDR pattern: drifting features (entropy mean, TTR, hapax ratio) show progressive narrowing and location shift, while shape features (entropy max, tail decay) maintain approximately constant distributions across depths.
34	
35	\begin{figure*}[!htbp]
36	\centering
37	\includegraphics[width=\textwidth]{fig_appendix_violin.pdf}
38	\caption{Feature distributions by generation depth (violin plots, $N$\,=\,37{,}058). Drifting features (entropy mean, TTR, hapax ratio: $|\rho| > 0.60$) show clear location shifts and narrowing with increasing depth. Shape features (entropy max, tail decay: $|\rho| < 0.10$) remain approximately stationary. Quartile lines indicate median and interquartile range.}
39	\label{fig:violin}
40	\end{figure*}
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "492b0d02-f2d7-456f-98b7-e39bdb3b6ab7",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "f74acfdc-2191-454c-a7e3-286b29f989df",
  "sourceToolAssistantUUID": "492b0d02-f2d7-456f-98b7-e39bdb3b6ab7",
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

_source line 17 · 2026-05-25T20:38:38.599Z_

<details open><summary>🔧 Tool call — Read · `toolu_01D38VnWuazfpCgRw6PYYvE9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_downstream.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f74acfdc-2191-454c-a7e3-286b29f989df",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPvych9ULhCCCo2gQdCJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "505a5d05-9255-4d46-a6fe-9ee073cb29e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8UTxZxSJzRKzEkvd1BY1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2520,
      "cache_read_input_tokens": 34665,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2520,
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

### Tool result

_source line 18 · 2026-05-25T20:38:38.604Z_

<details><summary>↩ Tool result · `toolu_01D38VnWuazfpCgRw6PYYvE9`</summary>

```text
1	Can depth-aware data curation improve downstream language model quality?
2	We fine-tune OLMo-2-0425-1B on five data variants (3 seeds each) and evaluate perplexity on a held-out test set (Table~\ref{tab:downstream}).
3	
4	\begin{table}[ht]
5	\centering
6	\small
7	\caption{Downstream fine-tuning perplexity (OLMo-2-0425-1B, mean $\pm$ std across 3 seeds). At equal sample count, random subsampling (2.367) outperforms depth-aware curation (depth 0--1: 2.387, binary-filtered: 2.389).}
8	\label{tab:downstream}
9	\begin{tabular}{lrc}
10	\toprule
11	\textbf{Variant} & \textbf{$n$} & \textbf{Test PPL} \\
12	\midrule
13	All depths            & 12{,}299 & 2.335 $\pm$ 0.000 \\
14	Size-matched (random) & 3{,}951  & 2.367 $\pm$ 0.000 \\
15	Depth 0--1 only       & 3{,}951  & 2.387 $\pm$ 0.001 \\
16	Binary-filtered       & 3{,}951  & 2.389 $\pm$ 0.000 \\
17	Depth 0 only          & 797      & 2.681 $\pm$ 0.001 \\
18	\bottomrule
19	\end{tabular}
20	\end{table}
21	
22	The results are unambiguous: data quantity dominates depth composition.
23	Training on all 12{,}299 samples yields the lowest perplexity (2.335).
24	At equal sample count ($n$\,=\,3{,}951), random subsampling (2.367) \emph{outperforms} both depth-stratified selection (depth 0--1: 2.387) and binary detection filtering (2.389).
25	Cross-seed variance is below 0.002 across all variants, which confirms the robustness of this null result.
26	
27	Restricting training to human-only text (depth 0, $n$\,=\,797) produces a sharp perplexity increase to 2.681, driven primarily by the 5$\times$ reduction in data volume rather than depth composition per se.
28	
29	\paragraph{Equivalence testing.}
30	We apply a two one-sided $t$-test (TOST) with a $\pm$2\% relative margin (equivalence bounds $\pm$0.047 on the ppl scale) to formally assess whether the depth-aware and random subsampling conditions produce practically indistinguishable perplexity.
31	At equal sample count ($n$\,=\,3{,}951): size-matched (random) ppl\,=\,2.367 vs.\ depth 0--1 ppl\,=\,2.387, $\Delta$\,=\,0.020.
32	TOST confirms equivalence ($p = 1.1 \times 10^{-4}$); the two curation strategies yield practically indistinguishable downstream quality within the $\pm$2\% margin.
33	Cross-seed standard deviation is below 0.001 for both variants.
34	
35	Comparing the full dataset ($n$\,=\,12{,}299, ppl\,=\,2.335) against the depth-filtered subset ($n$\,=\,3{,}951, ppl\,=\,2.387): TOST \emph{rejects} equivalence (minimum equivalence margin\,=\,0.053, exceeding the $\pm$2\% bound), which confirms that data quantity drives perplexity reduction beyond what depth-aware selection can recover.
36	
37	Knowing the generation depth of a document does not, by itself, make it more or less useful for training; at fixed sample count, depth-aware curation is statistically equivalent to uninformed random subsampling.
38	
39	\subsection*{Margin Sensitivity Analysis}
40	
41	To assess the robustness of the equivalence conclusion to margin choice, we repeat the TOST procedure across multiple equivalence margins \cite{lakens_equivalence}, following the recommendation to report sensitivity across plausible bounds rather than relying on a single threshold (Table~\ref{tab:tost-margins}).
42	
43	\begin{table}[ht]
44	\centering
45	\small
46	\caption{TOST equivalence testing across multiple margins. ``Equiv?'' indicates whether equivalence is established at $\alpha = 0.05$.}
47	\label{tab:tost-margins}
48	\resizebox{\linewidth}{!}{%
49	\begin{tabular}{llcc}
50	\toprule
51	\textbf{Comparison} & \textbf{Margin} & \textbf{Equiv?} & \textbf{TOST $p$} \\
52	\midrule
53	Full (12{,}299) vs.\ Random (3{,}951) & $\pm$1\% & No & 1.0 \\
54	                                        & $\pm$2\% & Yes & $1 \times 10^{-6}$ \\
55	                                        & $\pm$3\% & Yes & $< 10^{-10}$ \\
56	                                        & $\pm$5\% & Yes & $< 10^{-10}$ \\
57	\midrule
58	Full (12{,}299) vs.\ Depth 0--1 (3{,}951) & $\pm$1\% & No & 1.0 \\
59	                                            & $\pm$2\% & No & 1.0 \\
60	                                            & $\pm$3\% & Yes & $< 10^{-10}$ \\
61	                                            & $\pm$5\% & Yes & $< 10^{-10}$ \\
62	\bottomrule
63	\end{tabular}}
64	\end{table}
65	
66	The full dataset vs.\ random subsample comparison passes equivalence at the $\pm$2\% margin ($p = 10^{-6}$), while the full vs.\ depth 0--1 comparison requires a $\pm$3\% margin.
67	In absolute terms, perplexity differences are small: $\Delta$\,=\,0.032 (full vs.\ random, 1.4\% of baseline) and $\Delta$\,=\,0.052 (full vs.\ depth 0--1, 2.2\% of baseline).
68	
69	Cohen's $d$ values are 86.0 (full vs.\ random) and 119.7 (full vs.\ depth 0--1).
70	These appear large but are unreliable: with only $n$\,=\,3 seeds per condition, the pooled standard deviation is extremely small ($<$0.001), artificially inflating $d$.
71	The inflated effect sizes reflect low seed-level variance (confirming reproducibility) rather than practically meaningful perplexity differences.
72	The TOST framework with pre-specified relative margins provides a more appropriate assessment than Cohen's $d$ in this low-seed regime.
73	However, with only $n{=}3$ seeds per condition, the TOST results have limited generalizability: the test is valid given observed variance but the conclusion generalizes over only three random seeds. We characterize this as a preliminary observation rather than a definitive null result.
74	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "505a5d05-9255-4d46-a6fe-9ee073cb29e6",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "1981f217-2b7b-4a3a-9ab2-6abe29f5bad6",
  "sourceToolAssistantUUID": "505a5d05-9255-4d46-a6fe-9ee073cb29e6",
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

_source line 19 · 2026-05-25T20:38:39.071Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AVyJg9jfSRzmpiwmjCf3pP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_correlation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1981f217-2b7b-4a3a-9ab2-6abe29f5bad6",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPvych9ULhCCCo2gQdCJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2cc7777-47f7-4070-bb19-7b817d501c00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8UTxZxSJzRKzEkvd1BY1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2520,
      "cache_read_input_tokens": 34665,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2520,
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

### Tool result

_source line 20 · 2026-05-25T20:38:39.075Z_

<details><summary>↩ Tool result · `toolu_01AVyJg9jfSRzmpiwmjCf3pP`</summary>

```text
1	\section{Feature Correlation Matrix}
2	\label{sec:appendix-feature-correlation}
3	
4	This appendix documents inter-feature correlations and the PCA analysis referenced in \S\ref{sec:results-differential}.
5	
6	\begin{table}[t]
7	\centering
8	\caption{Pearson correlation matrix of the seven depth features ($N=27{,}529$).}
9	\label{tab:feature-corr}
10	\resizebox{\columnwidth}{!}{%
11	\begin{tabular}{lrrrrrrr}
12	\toprule
13	 & $\bar{H}$ & $\sigma_H$ & $H_{\min}$ & $H_{\max}$ & $\tau$ & TTR & Hapax \\
14	\midrule
15	$\bar{H}$ & \textemdash & 0.49 & 0.31 & 0.01 & 0.07 & \textbf{0.86} & \textbf{0.81} \\
16	$\sigma_H$ & 0.49 & \textemdash & $-$0.15 & 0.16 & 0.26 & 0.43 & 0.34 \\
17	$H_{\min}$ & 0.31 & $-$0.15 & \textemdash & $-$0.04 & 0.01 & 0.20 & 0.23 \\
18	$H_{\max}$ & 0.01 & 0.16 & $-$0.04 & \textemdash & $-$0.08 & $-$0.13 & $-$0.15 \\
19	$\tau$ & 0.07 & 0.26 & 0.01 & $-$0.08 & \textemdash & 0.13 & 0.14 \\
20	TTR & \textbf{0.86} & 0.43 & 0.20 & $-$0.13 & 0.13 & \textemdash & \textbf{0.97} \\
21	Hapax & \textbf{0.81} & 0.34 & 0.23 & $-$0.15 & 0.14 & \textbf{0.97} & \textemdash \\
22	\bottomrule
23	\end{tabular}}
24	\end{table}
25	
26	TTR and hapax ratio are near-perfectly correlated ($r=0.97$), and both correlate strongly with mean entropy ($r=0.86$ and $0.81$).
27	These three drifting features form a tightly coupled cluster: PCA on the standardized drifting-feature subset shows that a single principal component explains 92.3\% of their joint variance, with near-uniform loadings (0.56--0.59). These three features thus share a single latent dimension.
28	Full 7-feature PCA yields PC1 (44.4\% variance) loading on the drifting triplet (0.53--0.55) and PC2 (18.3\% variance) capturing entropy distributional shape (entropy std vs.\ entropy min contrast).
29	In contrast, $H_{\max}$, $\tau$ (tail decay), and $H_{\min}$ show weak pairwise correlations with all other features ($|r| < 0.27$); these features capture independent aspects of the token-probability distribution.
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2cc7777-47f7-4070-bb19-7b817d501c00",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "cd59496a-dbcb-415d-8679-15b32a4d423b",
  "sourceToolAssistantUUID": "e2cc7777-47f7-4070-bb19-7b817d501c00",
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

_source line 21 · 2026-05-25T20:38:40.072Z_

<details open><summary>🔧 Tool call — Read · `toolu_01V8bfuJpYVd4QUCXjy54SVR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_generator_subsets.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd59496a-dbcb-415d-8679-15b32a4d423b",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPvych9ULhCCCo2gQdCJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9f679db-a06c-4fda-8e28-f8e0a38b8775",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8UTxZxSJzRKzEkvd1BY1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2520,
      "cache_read_input_tokens": 34665,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2520,
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

### Tool result

_source line 22 · 2026-05-25T20:38:40.081Z_

<details><summary>↩ Tool result · `toolu_01V8bfuJpYVd4QUCXjy54SVR`</summary>

```text
1	Table~\ref{tab:gen-subsets} summarizes the generator subsets used across experiments.
2	
3	\begin{table}[ht]
4	\centering
5	\small
6	\caption{Generator subsets by experiment type.}
7	\label{tab:gen-subsets}
8	\resizebox{\linewidth}{!}{%
9	\begin{tabular}{lcl}
10	\toprule
11	\textbf{Experiment} & $\boldsymbol{N}$ & \textbf{Generators} \\
12	\midrule
13	Main LOGO (Table~\ref{tab:logo-results}) & 8 & All: Py-2.8B/1B, OLMo, Qw-1.7B/0.6B/8B, Llama, Mistral \\
14	Cross-model chains (Table~\ref{tab:cross-ref}) & 5 & Py-2.8B/1B, OLMo, Qw-1.7B/0.6B \\
15	QLoRA (Table~\ref{tab:qlora}) & 6 & Py-2.8B/1B, OLMo, Qw-1.7B/0.6B/8B \\
16	Temperature ablation (Table~\ref{tab:sampling-ablation}) & 4 & Py-2.8B, OLMo, Qw-1.7B/0.6B \\
17	Prompt-type (Appendix~\ref{app:prompt-type}) & 1 & Py-2.8B only \\
18	Cross-domain (Table~\ref{tab:domain}) & 3 & Py-1B, Qw-1.7B, Mistral \\
19	Instruct (Table~\ref{tab:instruct}) & 3 & OLMo, Qw-1.7B, Llama \\
20	Downstream (Appendix~\ref{app:downstream}) & 5 & Py-2.8B/1B, OLMo, Qw-1.7B/0.6B \\
21	\bottomrule
22	\end{tabular}}
23	\end{table}
24	
25	The 5-generator set was the initial development subset; Qwen3-8B was added for scale evaluation, and Llama-3.2-3B and Mistral-7B-v0.3 were added last for family-diversity testing.
26	Subset differences reflect chronological expansion rather than selective reporting.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9f679db-a06c-4fda-8e28-f8e0a38b8775",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "2dd8ac4a-655b-4223-b03d-579f8fe5c05f",
  "sourceToolAssistantUUID": "f9f679db-a06c-4fda-8e28-f8e0a38b8775",
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

_source line 23 · 2026-05-25T20:38:40.558Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HidN2QVmP2BWxc8H3vxh6S`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_human_edit.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dd8ac4a-655b-4223-b03d-579f8fe5c05f",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPvych9ULhCCCo2gQdCJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27ae1e4d-7b15-4af1-a4bd-01c882af850e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8UTxZxSJzRKzEkvd1BY1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2520,
      "cache_read_input_tokens": 34665,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2520,
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

### Tool result

_source line 24 · 2026-05-25T20:38:40.569Z_

<details><summary>↩ Tool result · `toolu_01HidN2QVmP2BWxc8H3vxh6S`</summary>

```text
1	We assess robustness to post-generation text modification by randomly replacing words at varying rates and re-evaluating the 8-generator LOGO pipeline (Table~\ref{tab:human-edit}).
2	Random word replacement represents a worst-case perturbation: real human editing preserves semantic coherence, so practical degradation is expected to be substantially lower than these estimates.
3	
4	\begin{table}[ht]
5	\centering
6	\small
7	\caption{Robustness to random word replacement under 8-gen LOGO evaluation (binary: gen-1 vs.\ gen-2+). Bootstrap 95\% CIs on binary F1 ($n$\,=\,1000).}
8	\label{tab:human-edit}
9	\resizebox{\linewidth}{!}{%
10	\begin{tabular}{lccc}
11	\toprule
12	\textbf{Perturbation rate} & \textbf{Binary F1} & \textbf{95\% CI} & \textbf{3-class F1} \\
13	\midrule
14	0\% (baseline) & 0.695 & [0.680, 0.710] & 0.737 \\
15	5\%            & 0.650 & [0.635, 0.666] & 0.641 \\
16	10\%           & 0.614 & [0.599, 0.629] & 0.492 \\
17	20\%           & 0.591 & [0.576, 0.605] & 0.367 \\
18	\bottomrule
19	\end{tabular}}
20	\end{table}
21	
22	Binary depth discrimination (gen-1 vs.\ gen-2+) degrades sublinearly: the first 5\% replacement causes the largest drop ($-$4.6\,pp), with diminishing marginal impact thereafter ($-$3.6\,pp for 5\%$\to$10\%, $-$2.3\,pp for 10\%$\to$20\%).
23	At 10\% replacement, binary F1 remains 0.614, well above the 0.50 random baseline, which indicates that depth signal survives moderate perturbation.
24	
25	Three-class classification is more sensitive (0.737$\to$0.367 at 20\%), because distinguishing gen-0 from gen-1 relies heavily on lexical diversity features (TTR, hapax ratio) that are directly disrupted by word replacement.
26	The binary metric, which excludes gen-0, is inherently more robust since it depends primarily on reference-model entropy features distributed across many tokens.
27	
28	\paragraph{Feature subset degradation.}
29	Table~\ref{tab:feature-degrade} compares perturbation robustness of the full 7-feature ensemble against an entropy-only subset (5 reference-model features).
30	The higher unperturbed binary F1 of the entropy-only subset (0.833 vs.\ 0.695) reflects the strong discriminability of reference-model features for the coarse binary task (gen-1 vs.\ gen-2+); however, lexical features are essential for the finer-grained ordinal task (3-class F1: 0.737 vs.\ 0.688) and provide greater robustness under perturbation.
31	At 20\% replacement, the 7-feature ensemble surpasses entropy-only on binary F1 (0.591 vs.\ 0.566), despite starting from a lower baseline.
32	Random word replacement drastically alters per-token context and makes entropy features (computed over the full token sequence) extremely sensitive to noise.
33	Lexical features (TTR, hapax ratio), as document-level summary statistics, are more stable under per-word perturbation and act as stabilizers in the full ensemble.
34	The crossover confirms that degradation in the full feature set reflects genuine signal disruption rather than a lexical-feature artifact.
35	
36	\begin{table}[ht]
37	\centering
38	\small
39	\caption{Feature subset degradation under random word replacement (8-gen LOGO). Entropy-only: 5 reference-model features; 7-feature: full ensemble including lexical features.}
40	\label{tab:feature-degrade}
41	\resizebox{\linewidth}{!}{%
42	\begin{tabular}{lcccc}
43	\toprule
44	\textbf{Perturb.} & \textbf{Ent-only Bin} & \textbf{7-feat Bin} & \textbf{Ent-only 3-cl} & \textbf{7-feat 3-cl} \\
45	\midrule
46	0\%  & 0.833 & 0.695 & 0.688 & 0.737 \\
47	5\%  & 0.736 & 0.650 & 0.539 & 0.641 \\
48	10\% & 0.657 & 0.614 & 0.427 & 0.492 \\
49	20\% & 0.566 & 0.591 & 0.314 & 0.367 \\
50	\bottomrule
51	\end{tabular}}
52	\end{table}
53	
54	\paragraph{Baseline comparison.}
55	Table~\ref{tab:baseline-robustness} compares robustness across detection methods under identical perturbation conditions (8-gen LOGO, binary: gen-1 vs.\ gen-2+).
56	
57	\begin{table}[ht]
58	\centering
59	\small
60	\caption{Baseline robustness under random word replacement (8-gen LOGO, binary F1). Bold indicates highest F1 at each perturbation rate. (Baseline scores use default XGBoost settings; trends are consistent with the unified configuration in Table~\ref{tab:baselines}.)}
61	\label{tab:baseline-robustness}
62	\begin{tabular}{lcccc}
63	\toprule
64	\textbf{Method} & \textbf{0\%} & \textbf{5\%} & \textbf{10\%} & \textbf{20\%} \\
65	\midrule
66	7-feature ensemble & \textbf{0.695} & 0.650 & 0.614 & 0.591 \\
67	LD-Score           & 0.677 & \textbf{0.673} & \textbf{0.677} & \textbf{0.671} \\
68	Avg-LogProb        & 0.682 & 0.419 & 0.335 & 0.375 \\
69	FastDetectGPT      & 0.571 & 0.437 & 0.468 & 0.514 \\
70	Binoculars\textsuperscript{\dag}         & 0.500 & 0.461 & 0.446 & 0.425 \\
71	\bottomrule
72	\end{tabular}
73	
74	\vspace{2pt}
75	{\footnotesize \textsuperscript{\dag}Binoculars operates at chance level on this binary task; its degradation figures are not meaningful.}
76	\end{table}
77	
78	The 7-feature ensemble achieves the highest unperturbed binary F1 (0.695), but LD-Score surpasses it under perturbation due to near-zero degradation ($-$0.6\,pp across the full 0\%$\to$20\% range).
79	FastDetectGPT and Avg-LogProb exhibit non-monotonic degradation at higher perturbation rates, likely because severe perturbation introduces distributional artifacts that these token-level methods detect as anomalous.
80	Avg-LogProb is the most fragile overall ($-$34.7\,pp at 10\%), while FastDetectGPT drops sharply at 5\% ($-$13.4\,pp) before partially recovering.
81	LD-Score is nearly invariant to perturbation, consistent with its reliance on corpus-level distributional divergence rather than per-token likelihoods.
82	The 7-feature ensemble offers the highest starting performance among single-reference methods, with sublinear degradation ($-$10.4\,pp at 20\%).
83	
84	\paragraph{LLM-simulated sentence regeneration.}
85	To test robustness under semantically coherent editing, we use Qwen3-0.6B-Base to randomly regenerate 1--3 sentences per passage (avg 1.69 sentences, ${\sim}$50\% edit distance) and re-evaluate the 8-gen LOGO pipeline.
86	Binary F1 drops from 0.692 to 0.647 ($-$4.5\,pp, 6.5\% relative); 3-class F1 drops from 0.739 to 0.667 ($-$7.1\,pp, 9.7\% relative).
87	The binary degradation ($-$4.5\,pp) is nearly identical to that caused by 5\% random word replacement ($-$4.6\,pp), despite the LLM rephrase altering ${\sim}$50\% of characters.
88	This asymmetry arises because LLM-generated replacements preserve the underlying statistical signature of the generation process (entropy dynamics, depth-accumulated distributional drift), whereas random word substitution directly destroys local statistical signals.
89	Depth profiling thus captures deep generative structure that survives semantic-preserving edits.
90	
91	\paragraph{Seed complexity.}
92	Performance is stable across seed text complexity: stratifying seeds by vocabulary richness (TTR terciles) yields maximum F1 variation of 1.1\,pp across groups.
93	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27ae1e4d-7b15-4af1-a4bd-01c882af850e",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "55a39874-fbe1-4fc6-8322-f81b7f3d8989",
  "sourceToolAssistantUUID": "27ae1e4d-7b15-4af1-a4bd-01c882af850e",
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

_source line 25 · 2026-05-25T20:38:40.890Z_

<details open><summary>🔧 Tool call — Read · `toolu_013nRNFGaGQJNvWyKgvQr9h8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_prompt_type.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55a39874-fbe1-4fc6-8322-f81b7f3d8989",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPvych9ULhCCCo2gQdCJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a2267bb-5255-47a5-bb19-8f7c509f736f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8UTxZxSJzRKzEkvd1BY1a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2520,
      "cache_read_input_tokens": 34665,
      "output_tokens": 854,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2520
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 854,
          "cache_read_input_tokens": 34665,
          "cache_creation_input_tokens": 2520,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2520,
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

_source line 26 · 2026-05-25T20:38:40.895Z_

<details><summary>↩ Tool result · `toolu_013nRNFGaGQJNvWyKgvQr9h8`</summary>

```text
1	We evaluate depth profiling under three prompt types using Pythia-2.8B. Each uses 995 seeds $\times$ 5 depths. The exact templates are:
2	
3	\begin{tcolorbox}[colback=yellow!5!white, colframe=gray!50, title=Prompt Templates, breakable, fonttitle=\bfseries\small]
4	\textbf{Continuation:} \texttt{Continue the following text: \{text\}}\\[4pt]
5	\textbf{Elaboration:} \texttt{Elaborate on the following text: \{text\}}\\[4pt]
6	\textbf{Inspired rewriting:} \texttt{Write a new passage inspired by the following text: \{text\}}
7	\end{tcolorbox}
8	
9	\paragraph{Within-prompt-type classification.}
10	5-fold CV macro-F1: continuation 0.78, rewriting 0.74, elaboration 0.73. All three prompt types exhibit the same differential depth response pattern: drifting features (hapax ratio, TTR, entropy mean) show consistent monotonic trends, while near-stationary features (entropy max, tail decay) change by less than 5\%.
11	
12	\paragraph{Cross-prompt-type transfer (LOPTO).}
13	Leave-one-prompt-type-out evaluation yields average F1\,=\,0.753, which confirms that depth signal transfers across prompt types. Feature decay rates differ: continuation shows the strongest drift (16.9\% per depth step), followed by rewriting (6.1\%) and elaboration (1.4\%), consistent with continuation chains applying less semantic constraint on the output.
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a2267bb-5255-47a5-bb19-8f7c509f736f",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "9b68ac70-e83c-4ac8-90a7-e91821213c8e",
  "sourceToolAssistantUUID": "3a2267bb-5255-47a5-bb19-8f7c509f736f",
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

_source line 27 · 2026-05-25T20:38:50.033Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Af8h1qEY5NuvQBxhi9mn5S`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qualitative_examples.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b68ac70-e83c-4ac8-90a7-e91821213c8e",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPvzXfZavqSsV5ZghBKu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "174298e6-0fe5-4953-b468-cd0c2e45a579",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUPSvoeobfQAAfbFh7jiwN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11566,
      "cache_read_input_tokens": 37185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11566,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 28 · 2026-05-25T20:38:50.038Z_

<details><summary>↩ Tool result · `toolu_01Af8h1qEY5NuvQBxhi9mn5S`</summary>

```text
1	\section{Qualitative Examples}
2	\label{app:qualitative}
3	
4	Table~\ref{tab:qualitative-text} presents an example generation chain from seed 120 (Pythia-2.8B, continuation prompt), illustrating how text evolves across recursive generation steps.
5	Table~\ref{tab:qualitative-features} reports the corresponding 7-feature values. Central-tendency features ($\bar{H}$, TTR, hapax ratio) drift monotonically while shape features ($H_{\max}$, tail decay) remain near-stationary, consistent with the differential depth response pattern.
6	
7	\begin{table}[t]
8	\centering
9	\caption{Example text chain from seed 120 (Pythia-2.8B, continuation prompt). Gen-0 is the original Wikipedia passage; gen-1 and gen-2 are successive LLM continuations. Text is truncated for space.}
10	\label{tab:qualitative-text}
11	\small
12	\begin{tabular}{p{0.90\columnwidth}}
13	\toprule
14	\textbf{Gen-0 (Wikipedia seed)} \\
15	\midrule
16	Aquarius is an equatorial constellation of the zodiac, between Capricornus and Pisces. Its name is Latin for ``water-carrier'' or ``cup-carrier''. Aquarius is one of the oldest of the recognized constellations along the zodiac (the Sun's apparent path). It was one of the 48 constellations listed by the 2nd century astronomer Ptolemy, and it remains one of the 88 modern constellations. It is found in a region often called the Sea due to its profusion of constellations with watery associations such as Cetus the whale, Pisces the fish, and Eridanus the river. [\ldots] \\
17	\midrule
18	\textbf{Gen-1} \\
19	\midrule
20	Babylonian astrology and was also depicted in ancient Egyptian art. In Greek mythology, Aquarius is the son of Poseidon and Gaia. He is also the god of the sea and the sky, the god of travelers, and the guardian of the underworld. In Roman mythology, Aquarius is the son of Saturn and the nymph Egeria, and the god of the sea. In Jewish mythology, Aquarius is the son of the God of the Air and the Goddess of the Moon. In Chinese mythology, Aquarius is the son of the God of the Sky and the Goddess of the Earth. [\ldots] \\
21	\midrule
22	\textbf{Gen-2} \\
23	\midrule
24	God of the Sky and the Goddess of the Earth. In the ancient Greek mythology, Aquarius is the son of the God of the Sky and the Goddess of the Earth. In the Hindu mythology, Aquarius is the son of the God of the Sky and the Goddess of the Earth. In the ancient Egyptian mythology, Aquarius is the son of the God of the Sky and the Goddess of the Earth. [\ldots] \\
25	\bottomrule
26	\end{tabular}
27	\end{table}
28	
29	\begin{table}[t]
30	\centering
31	\caption{Feature values for the chain in Table~\ref{tab:qualitative-text}. Drifting features ($\bar{H}$, TTR, hapax) show monotonic degradation; shape features ($H_{\max}$, tail decay) remain stable (range $<$2\% and $<$4\% respectively).}
32	\label{tab:qualitative-features}
33	\small
34	\resizebox{\linewidth}{!}{%
35	\begin{tabular}{lrrr}
36	\toprule
37	Feature & Gen-0 & Gen-1 & Gen-2 \\
38	\midrule
39	$\bar{H}$ (entropy mean) & 2.720 & 2.206 & 0.780 \\
40	$\sigma_H$ (entropy std) & 1.772 & 1.816 & 1.517 \\
41	$H_{\min}$ (entropy min) & 0.002 & 0.005 & 0.000 \\
42	$H_{\max}$ (entropy max) & 7.000 & 7.016 & 6.926 \\
43	tail decay & $-$0.00227 & $-$0.00231 & $-$0.00223 \\
44	TTR & 0.659 & 0.272 & 0.081 \\
45	hapax ratio & 0.561 & 0.183 & 0.005 \\
46	\bottomrule
47	\end{tabular}}
48	\end{table}
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "174298e6-0fe5-4953-b468-cd0c2e45a579",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "cdd1dc67-9f26-4383-a674-f25db9cc7af3",
  "sourceToolAssistantUUID": "174298e6-0fe5-4953-b468-cd0c2e45a579",
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

_source line 29 · 2026-05-25T20:38:50.872Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ESYJzQCQ3kSvRts272c3tt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_temperature_stability.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdd1dc67-9f26-4383-a674-f25db9cc7af3",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPvzXfZavqSsV5ZghBKu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34953ca5-da1c-49f7-b98c-b921761eca13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUPSvoeobfQAAfbFh7jiwN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11566,
      "cache_read_input_tokens": 37185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11566,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 30 · 2026-05-25T20:38:50.877Z_

<details><summary>↩ Tool result · `toolu_01ESYJzQCQ3kSvRts272c3tt`</summary>

```text
1	To assess whether the DDR three-way partition generalizes beyond the default temperature ($\tau{=}0.7$), we computed per-feature Cohen's $d$ (generation~1 vs.\ generation~2+) at $\tau \in \{0.5, 0.7, 0.9\}$ for all four generators in the temperature ablation (12 conditions total; Table~\ref{tab:ddr-temp-stability}).
2	
3	\begin{table}[H]
4	\centering
5	\small
6	\caption{Mean $|d|$ (gen-1 vs.\ gen-2+) across 4 generators at each temperature. Partition labels: \textbf{D}rifting ($|d|>0.5$), \textbf{I}ntermediate ($0.1{<}|d|{<}0.5$), near-\textbf{S}tationary ($|d|{<}0.1$). Boldface marks features that shift from their $\tau{=}0.7$ partition.}
7	\label{tab:ddr-temp-stability}
8	\resizebox{\linewidth}{!}{%
9	\begin{tabular}{lccc l}
10	\toprule
11	\textbf{Feature} & $\boldsymbol{\tau{=}0.5}$ & $\boldsymbol{\tau{=}0.7}$ & $\boldsymbol{\tau{=}0.9}$ & \textbf{Group} \\
12	\midrule
13	Entropy mean  & 1.39\,\textsuperscript{D} & 1.10\,\textsuperscript{D} & 0.58\,\textsuperscript{D} & Drifting \\
14	TTR           & 1.00\,\textsuperscript{D} & 0.85\,\textsuperscript{D} & \textbf{0.45}\,\textsuperscript{I} & Drifting \\
15	Hapax ratio   & 0.87\,\textsuperscript{D} & 0.75\,\textsuperscript{D} & \textbf{0.42}\,\textsuperscript{I} & Drifting \\
16	\midrule
17	Entropy std   & \textbf{0.84}\,\textsuperscript{D} & 0.52\,\textsuperscript{D} & \textbf{0.20}\,\textsuperscript{I} & Intermediate \\
18	\midrule
19	Entropy max   & 0.06\,\textsuperscript{S} & 0.09\,\textsuperscript{S} & \textbf{0.11}\,\textsuperscript{I} & Stationary \\
20	Tail decay    & 0.07\,\textsuperscript{S} & \textbf{0.12}\,\textsuperscript{I} & \textbf{0.15}\,\textsuperscript{I} & Stationary \\
21	Entropy min   & 0.04\,\textsuperscript{S} & 0.06\,\textsuperscript{S} & 0.04\,\textsuperscript{S} & Stationary \\
22	\bottomrule
23	\end{tabular}}
24	\end{table}
25	
26	The partition anchors are robust: entropy mean remains drifting in all 12 conditions, TTR in 10/12, and hapax ratio in 9/12; entropy min and entropy max stay near-stationary in 10/12 and 9/12 conditions, respectively.
27	The two boundary features are more temperature-sensitive: entropy std is drifting at $\tau{=}0.5$ for all generators but falls to intermediate at $\tau{=}0.9$ for three of four, while tail decay fluctuates between near-stationary and intermediate across generators.
28	Effect sizes compress monotonically with temperature: for the fixed drifting set (entropy mean, TTR, hapax ratio), mean $|d|$ drops from 1.09 at $\tau{=}0.5$ to 0.90 at $\tau{=}0.7$ to 0.48 at $\tau{=}0.9$, shifting individual features across partition boundaries at high temperature without altering the qualitative hierarchy: lexical diversity features drift fastest, entropy extrema remain stable across all conditions tested.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34953ca5-da1c-49f7-b98c-b921761eca13",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "ccfaa446-5302-4749-95b5-7cf52ba608ad",
  "sourceToolAssistantUUID": "34953ca5-da1c-49f7-b98c-b921761eca13",
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

_source line 31 · 2026-05-25T20:38:51.819Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QSuaezbqG1Ym2Q8xtTTKtU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccfaa446-5302-4749-95b5-7cf52ba608ad",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPvzXfZavqSsV5ZghBKu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd327844-3793-41bb-abdc-03291dfa8647",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUPSvoeobfQAAfbFh7jiwN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11566,
      "cache_read_input_tokens": 37185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11566,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 32 · 2026-05-25T20:38:51.825Z_

<details><summary>↩ Tool result · `toolu_01QSuaezbqG1Ym2Q8xtTTKtU`</summary>

```text
1	\looseness=-1 To verify that the depth signal resides in the features rather than the classifier,
2	we repeat the 6-generator LOGO evaluation using Logistic Regression and Random Forest
3	in place of XGBoost (Table~\ref{tab:alt-classifier}).
4	All other settings (the same 7 features, 3-class labels, and class-balanced downsampling) are
5	kept identical. For Logistic Regression we apply standard scaling to the features.
6	
7	\begin{table}[ht]
8	\centering
9	\caption{LOGO macro-F1 across three classifiers. Each column shows the held-out generator F1. (6-generator LOGO; 3-class.)}
10	\label{tab:alt-classifier}
11	\small
12	\resizebox{\linewidth}{!}{%
13	\begin{tabular}{lc cccccc}
14	\toprule
15	Classifier & Avg F1 & OLMo-2 & Py-1B & Py-2.8B & Qw-0.6B & Qw-1.7B & Qw-8B \\
16	\midrule
17	XGBoost          & 0.789 & 0.764 & 0.856 & 0.804 & 0.824 & 0.806 & 0.683 \\
18	Random Forest    & 0.790 & 0.764 & 0.856 & 0.804 & 0.825 & 0.807 & 0.684 \\
19	Logistic Regr.   & 0.725 & 0.719 & 0.781 & 0.740 & 0.745 & 0.743 & 0.624 \\
20	\bottomrule
21	\end{tabular}}
22	\end{table}
23	
24	\looseness=-1 Both tree-based classifiers achieve LOGO F1 $\approx 0.79$,
25	and even a linear model reaches $0.725$, well above the $0.33$ chance baseline for
26	three classes.
27	The per-generator ranking is also consistent across classifiers
28	(Pythia-1B easiest, Qwen3-8B hardest),
29	confirming that discriminative power originates in the entropy and lexical features,
30	not in classifier capacity.
31	Ordinal-specific methods (CORAL \cite{coral_ordinal}, Frank-Hall \cite{frank_hall_ordinal}) achieve comparable F1 with overlapping CIs, which confirms that 3-class granularity provides insufficient resolution for ranking-aware losses to improve over standard multiclass classification.
32	
33	\paragraph{XGBoost hyperparameter sensitivity.}
34	To verify that performance is not an artifact of hyperparameter selection, we vary \texttt{max\_depth} $\in \{3, 4, 6, 8\}$ while keeping all other settings fixed (Table~\ref{tab:xgb-sensitivity}).
35	
36	\begin{table}[ht]
37	\centering
38	\small
39	\caption{XGBoost \texttt{max\_depth} sensitivity (8-gen LOGO). 3-class F1 varies by only 2.0\,pp; binary F1 (gen-1 vs.\ gen-2+) is effectively invariant ($\leq$0.1\,pp).}
40	\label{tab:xgb-sensitivity}
41	\begin{tabular}{lcc}
42	\toprule
43	\textbf{max\_depth} & \textbf{3-class F1} & \textbf{Binary F1} \\
44	\midrule
45	3 & 0.752 & 0.700 \\
46	4 & 0.759 & 0.699 \\
47	6 & 0.769 & 0.700 \\
48	8 & 0.772 & 0.699 \\
49	\bottomrule
50	\end{tabular}
51	\end{table}
52	
53	\looseness=-1 3-class F1 increases monotonically with tree depth but the total range is only 2.0\,pp (0.752--0.772); binary F1 is effectively invariant (0.699--0.700).
54	The default \texttt{max\_depth}\,=\,6 used throughout the paper lies within 0.3\,pp of the best 3-class setting; the reported results are not sensitive to this choice.
55	
56	\begin{figure}[t]
57	\centering
58	\includegraphics[width=\columnwidth]{fig_appendix_confusion.pdf}
59	\caption{3-class LOGO confusion matrix ($N$\,=\,27{,}529). (a)~Raw counts. (b)~Row-normalized recall percentages. Gen-0 achieves near-perfect classification; the primary confusion axis is gen-1 $\leftrightarrow$ gen-2+.}
60	\label{fig:confusion-heatmap}
61	\end{figure}
62	
63	\subsection*{Sampling Sensitivity Analysis}
64	\label{app:sampling-sensitivity}
65	
66	\looseness=-1 To assess robustness to decoding temperature, we regenerate continuation chains at $t \in \{0.5, 0.9\}$ with fixed nucleus $p{=}0.9$ (matching the default) for four generators spanning three model families: Pythia-2.8B, OLMo-2-1B, Qwen3-1.7B, and Qwen3-0.6B (Table~\ref{tab:sampling-ablation}).
67	
68	\begin{table}[ht]
69	\centering
70	\caption{Depth classification under varying temperature (fixed top-$p$\,=\,0.9). Binary: gen-1 vs.\ gen-2+. LOGO evaluation; 95\% bootstrap CIs.$^{\ast}$$^{\dagger}$}
71	\label{tab:sampling-ablation}
72	\small
73	\resizebox{\linewidth}{!}{%
74	\begin{tabular}{llcc c}
75	\toprule
76	Model & Temp & LOGO Binary F1 & 95\% CI & $\rho$(ent.\ mean) \\
77	\midrule
78	Pythia-2.8B$^{\dagger}$ & 0.5  & \textbf{0.814} & [.798, .828] & $-0.58$ \\
79	Pythia-2.8B$^{\dagger}$ & 0.7  & 0.740 & [.725, .755] & $-0.60$ \\
80	Pythia-2.8B$^{\dagger}$ & 0.9  & 0.480 & [.465, .498] & $-0.30$ \\
81	\midrule
82	OLMo-2-1B & 0.5  & \textbf{0.783} & [.768, .798] & $-0.72$ \\
83	OLMo-2-1B & 0.7  & 0.695 & [.679, .711] & $-0.60$ \\
84	OLMo-2-1B & 0.9  & 0.453 & [.437, .469] & $-0.26$ \\
85	\midrule
86	Qwen3-1.7B$^{\dagger}$ & 0.5  & 0.751 & --- & $-0.60$ \\
87	Qwen3-1.7B$^{\dagger}$ & 0.7  & 0.751 & --- & $-0.60$ \\
88	Qwen3-1.7B$^{\dagger}$ & 0.9  & 0.566 & --- & $-0.37$ \\
89	\midrule
90	Qwen3-0.6B & 0.5  & 0.711 & [.694, .729] & $-0.67$ \\
91	Qwen3-0.6B & 0.7  & 0.691 & [.673, .709] & $-0.60$ \\
92	Qwen3-0.6B & 0.9  & 0.598 & [.582, .615] & $-0.29$ \\
93	\bottomrule
94	\end{tabular}}
95	\end{table}
96	\noindent\begin{minipage}{\columnwidth}
97	\scriptsize $^{\ast}$OLMo temperature experiments use OLMo-2-0425-1B (April 2025 release); the original OLMo-2-1B-hf weights are no longer publicly available.\par\vspace{1pt}
98	$^{\dagger}$Pythia-2.8B and Qwen3-1.7B use 6-generator LOGO (pre-expansion); OLMo-2-1B and Qwen3-0.6B use 8-generator LOGO. Within-model comparisons are unaffected.
99	\end{minipage}\vspace{4pt}
100	
101	\looseness=-1 Temperature sensitivity is asymmetric and model-dependent. High-temperature degradation ($t{=}0.9$) is universal: all four generators lose $9.3$--$26.0$\,pp in binary F1, with entropy mean's $|\rho|$ weakening to $0.26$--$0.37$ (vs.\ $0.58$--$0.72$ at $t{=}0.5$). Low-temperature improvement ($t{=}0.5$) is model-dependent: Pythia-2.8B and OLMo-2-1B gain $+7.4$ and $+8.8$\,pp respectively, while both Qwen models show negligible change ($0$--$2.0$\,pp). This split tracks model family rather than scale: Qwen3-0.6B (smallest) and Qwen3-1.7B both plateau, while OLMo-2-1B (similar scale to Qwen3-1.7B) benefits substantially. One possible explanation is that Qwen models produce more peaked output distributions at $t{=}0.7$, leaving less room for low-temperature compression to sharpen the depth signal.
102	
103	\looseness=-1 The method operates reliably within $t \in [0.5, 0.7]$ across all tested models. Degradation onset at $t{=}0.9$ defines the practical upper bound, consistent with the hypothesis that elevated temperature injects sufficient randomness to flatten the distributional drift that DDR exploits (\S\ref{sec:discussion}).
104	
105	\subsection*{Per-Generator Performance}
106	
107	Figure~\ref{fig:per-gen} visualizes per-generator LOGO performance.
108	Pythia models (1B, 2.8B) achieve highest F1, while larger models (Mistral-7B, Qwen3-8B) show degradation.
109	The scale effect (larger models $\rightarrow$ lower F1) is consistent with higher-capacity models generating text statistically closer to human writing.
110	
111	\begin{figure*}[t]
112	\centering
113	\includegraphics[width=\textwidth]{fig_appendix_per_gen.pdf}
114	\caption{Per-generator LOGO performance. (a)~Binary and 3-class F1, sorted by binary F1. Dashed lines: pool average. (b)~6-generator LOGO detail heatmap across model families.}
115	\label{fig:per-gen}
116	\end{figure*}
117	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd327844-3793-41bb-abdc-03291dfa8647",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "a11cfe1a-363f-4659-a17b-f43b82decbc3",
  "sourceToolAssistantUUID": "cd327844-3793-41bb-abdc-03291dfa8647",
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

_source line 33 · 2026-05-25T20:38:52.494Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QwDwMsf1ykp3Lv2tkVZrqm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ddr_validation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a11cfe1a-363f-4659-a17b-f43b82decbc3",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPvzXfZavqSsV5ZghBKu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51f00ffe-5c3d-4621-8e9d-ac23c0d574fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUPSvoeobfQAAfbFh7jiwN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11566,
      "cache_read_input_tokens": 37185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11566,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 34 · 2026-05-25T20:38:52.499Z_

<details><summary>↩ Tool result · `toolu_01QwDwMsf1ykp3Lv2tkVZrqm`</summary>

```text
1	\begin{figure}[t]
2	\centering
3	\includegraphics[width=0.85\columnwidth]{fig_ddr_scatter.pdf}
4	\caption{DDR partition in pooled ($|\rho|$, Cohen's $d$) space. Drifting features (red) cluster at high $|\rho|$ and $d$; near-stationary features (blue) cluster near the origin; entropy std (purple) occupies a sole intermediate position. Dashed lines: TOST equivalence bound ($d{=}0.20$) and $|\rho|{=}0.30$. Diamond marker: entropy min (pooled $|\rho|{=}0.40$ reflects the gen-0/gen-1 boundary; gen-1 vs.\ gen-2+ $d{=}0.03$).}
5	\label{fig:ddr-scatter}
6	\end{figure}
7	
8	\subsection*{Data-Driven Clustering}
9	
10	To assess the DDR partition structure and determine whether the drifting/non-drifting split is data-driven, we apply $k$-means clustering ($k \in \{2,3,4,5\}$) to the seven features in standardized $(|\rho|, d)$ space (Table~\ref{tab:clustering}).
11	
12	\begin{table}[ht]
13	\centering
14	\small
15	\caption{$k$-means clustering of 7 features in $(|\rho|, d)$ space.}
16	\label{tab:clustering}
17	\resizebox{\linewidth}{!}{%
18	\begin{tabular}{ccp{5.5cm}}
19	\toprule
20	$k$ & Silhouette & Clusters \\
21	\midrule
22	2 & \textbf{0.660} & \{$\bar{H}$, TTR, hapax\} $\mid$ \{$\sigma_H$, $H_{\min}$, $H_{\max}$, tail\} \\
23	3 & 0.532 & \{$\bar{H}$, TTR, hapax\} $\mid$ \{$\sigma_H$, $H_{\max}$, tail\} $\mid$ \{$H_{\min}$\} \\
24	4 & 0.527 & \{$\bar{H}$, TTR, hapax\} $\mid$ \{$H_{\max}$, tail\} $\mid$ \{$\sigma_H$\} $\mid$ \{$H_{\min}$\} \\
25	\bottomrule
26	\end{tabular}}
27	\end{table}
28	
29	The primary drifting/non-drifting split ($k{=}2$, silhouette\,=\,0.660) is the strongest cluster structure.
30	At $k{=}3$, entropy min forms its own cluster rather than joining the near-stationary group because its pooled $|\rho|{=}0.40$ (driven by the gen-0/gen-1 boundary) places it far from other near-stationary features in $\rho$ space.
31	The 3/1/3 DDR partition resolves this by using the gen-1 vs.\ gen-2+ Cohen's $d$ ($d{=}0.03$) to place entropy min in the near-stationary group, a domain-informed refinement that unsupervised clustering cannot recover from pooled statistics alone.
32	At $k{=}4$ (silhouette\,=\,0.527), entropy std separates from the near-stationary group, consistent with its intermediate DDR classification.
33	
34	\paragraph{Exhaustive partition enumeration.}
35	To confirm that the three-vs-four split is optimal rather than incidental, we enumerate all $\binom{7}{3}{=}35$ possible ways to assign three features to a ``drifting'' group and the remaining four to ``non-drifting,'' computing the silhouette score for each partition in standardized $(|\rho|, d)$ space.
36	The observed DDR partition (\{entropy mean, TTR, hapax ratio\}) achieves the highest silhouette (0.660), with a gap of 0.18 to the second-ranked split; 20 of 35 partitions produce negative silhouette scores.
37	
38	\paragraph{Per-generator replication.}
39	To rule out the possibility that the pooled silhouette is an artifact of mixing heterogeneous generators, we repeat the $(|\rho|, d)$ clustering independently for each of the eight generators.
40	Every generator recovers the identical \{$\bar{H}$, TTR, hapax\} vs.\ \{$\sigma_H$, $H_{\min}$, $H_{\max}$, tail\} partition, with silhouette scores ranging from 0.505 (Pythia-1B) to 0.760 (Mistral-7B-v0.3; mean\,=\,0.651).
41	No generator falls below the 0.50 moderate-structure threshold. The two-cluster structure is a per-generator property rather than a pooling artifact.
42	
43	\subsection*{TOST Equivalence Bound Sensitivity}
44	\label{app:tost-sensitivity}
45	
46	Table~\ref{tab:tost-sensitivity} shows the fraction of generators for which each feature passes the TOST equivalence test (gen-1 vs.\ gen-2+, $\alpha{=}0.05$) at three equivalence bounds $\varepsilon$.
47	
48	\begin{table}[ht]
49	\centering
50	\small
51	\caption{TOST equivalence pass rate across 8 generators at varying $\varepsilon$.}
52	\label{tab:tost-sensitivity}
53	\resizebox{\linewidth}{!}{%
54	\begin{tabular}{llccc}
55	\toprule
56	\textbf{DDR Zone} & \textbf{Feature} & $\boldsymbol{\varepsilon{=}0.15}$ & $\boldsymbol{\varepsilon{=}0.20}$ & $\boldsymbol{\varepsilon{=}0.25}$ \\
57	\midrule
58	\multirow{3}{*}{Drifting} & $\bar{H}$ (ent.\ mean) & 0/8 & 0/8 & 0/8 \\
59	 & TTR & 0/8 & 0/8 & 0/8 \\
60	 & hapax ratio & 0/8 & 0/8 & 0/8 \\
61	\midrule
62	Intermediate & $\sigma_H$ (ent.\ std) & 0/8 & 0/8 & 0/8 \\
63	\midrule
64	\multirow{3}{*}{Near-stat.} & $H_{\min}$ (ent.\ min) & 7/8 & 8/8 & 8/8 \\
65	 & $H_{\max}$ (ent.\ max) & 6/8 & 6/8 & 6/8 \\
66	 & tail decay & 4/8 & 4/8 & 7/8 \\
67	\bottomrule
68	\end{tabular}}
69	\end{table}
70	
71	The partition is robust to the equivalence bound: drifting features reject equivalence at all $\varepsilon$ for all generators, while entropy min passes even at the stricter bound $\varepsilon{=}0.15$ (7/8 generators).
72	Tail decay is the most $\varepsilon$-sensitive near-stationary feature, passing 4/8 at $\varepsilon{=}0.20$ but 7/8 at $\varepsilon{=}0.25$; the four non-passing generators show $|d|{=}0.15$--$0.22$, still well below the drifting threshold ($d > 0.50$).
73	Entropy max is stable across all three bounds (6/8), with the two failures (Pythia-1B $d{=}0.21$, Pythia-2.8B $d{=}0.25$) reflecting same-family reference affinity with the Pythia-410M reference model.
74	
75	\paragraph{TOST margin rationale.}
76	We adopt $\varepsilon{=}0.20$ as the primary equivalence bound, corresponding to Cohen's ``small effect'' threshold ($d{=}0.20$; \citealp{cohen1988statistical}).
77	This choice reflects a principled smallest effect size of interest (SESOI): effects below $d{=}0.20$ are conventionally negligible and unlikely to carry practical discriminative value for depth classification.
78	The bound is conservative relative to the drifting--stationary gap ($d_{\min}^{\text{drift}}{=}0.74$ vs.\ $\varepsilon{=}0.20$, a $3.7{\times}$ margin); the equivalence test thus has adequate power to confirm near-stationarity without risk of misclassifying genuinely drifting features.
79	As Table~\ref{tab:tost-sensitivity} shows, conclusions are qualitatively identical at $\varepsilon{=}0.15$ and $\varepsilon{=}0.25$; the partition is insensitive to the specific bound choice.
80	LOFO analysis independently corroborates this boundary: near-stationary features contribute ${<}2$\,pp marginal importance (Appendix~\ref{app:lofo}), empirically validating $\varepsilon{=}0.20$ as a task-relevant threshold.
81	
82	\paragraph{Threshold sensitivity.}
83	To address concerns about the sensitivity of the drifting-boundary threshold,
84	we sweep $|d|$ from $0.10$ to $0.80$ in increments of $0.05$ and record the
85	resulting binary partition (drifting vs.\ stationary) along with the silhouette
86	score in standardized $(|\rho|, d)$ space.
87	Across the entire range, only \emph{three} distinct partitions emerge,
88	reflecting natural gaps between feature clusters rather than threshold artifacts.
89	The three-feature drifting set (entropy mean, TTR, hapax ratio)
90	is stable across $|d| \in [0.50,\, 0.75]$ with a silhouette of $0.660$ (the
91	peak value in the sweep).
92	Including the intermediate feature entropy std ($d{=}0.46$) yields a
93	4/3 partition stable across $|d| \in [0.10,\, 0.45]$ (silhouette\,=\,0.451).
94	The partition used in our analysis corresponds to the peak-silhouette region,
95	confirming that the drifting/stationary boundary reflects a natural gap in the
96	$(|\rho|, d)$ landscape rather than an artifact of a particular
97	threshold choice.
98	
99	\paragraph{Partition stability across $\varepsilon$ thresholds.}
100	\label{app:epsilon-sweep}
101	
102	The DDR partition classifies features as non-stationary ($d \geq \varepsilon$) or stationary ($d < \varepsilon$) based on pooled Cohen's $d$ (\S\ref{sec:results-differential}).
103	Table~\ref{tab:epsilon-sweep} reports the critical $\varepsilon$ at which each feature's classification changes; the three drifting and three near-stationary features maintain their classification for all $\varepsilon \in [0.10, 0.75]$.
104	
105	\begin{table}[ht]
106	\centering
107	\small
108	\caption{Partition stability under varying $\varepsilon$. Critical threshold: the $\varepsilon$ above which a feature is reclassified as stationary. The drifting/near-stationary split is invariant for $\varepsilon \in [0.10, 0.75]$; only entropy std ($d{=}0.46$) changes at $\varepsilon > 0.46$.}
109	\label{tab:epsilon-sweep}
110	\resizebox{\linewidth}{!}{%
111	\begin{tabular}{llcc}
112	\toprule
113	\textbf{DDR Zone} & \textbf{Feature} & \textbf{Pooled $d$} & \textbf{Stationary at $\varepsilon >$} \\
114	\midrule
115	\multirow{3}{*}{Drifting} & $\bar{H}$ (ent.\ mean) & 1.05 & 1.05 \\
116	 & TTR & 0.81 & 0.81 \\
117	 & hapax ratio & 0.74 & 0.74 \\
118	\midrule
119	Intermediate & $\sigma_H$ (ent.\ std) & 0.46 & 0.46 \\
120	\midrule
121	\multirow{3}{*}{Near-stat.} & $H_{\max}$ (ent.\ max) & 0.06 & 0.06 \\
122	 & tail decay & 0.09 & 0.09 \\
123	 & $H_{\min}$ (ent.\ min) & 0.016 & 0.016 \\
124	\bottomrule
125	\end{tabular}}
126	\end{table}
127	
128	\noindent The 3/1/3 partition is stable across $\varepsilon \in [0.10, 0.75]$: the three drifting features remain non-stationary at all $\varepsilon < 0.74$, the three near-stationary features remain stationary at all $\varepsilon > 0.09$, and only entropy std changes classification (becoming stationary at $\varepsilon > 0.46$). It is the sole threshold-sensitive feature.
129	The minimum gap between adjacent zone boundaries ($d_{\text{hapax}} - d_{\sigma_H} = 0.28$) exceeds typical effect-size estimation uncertainty and provides a margin against sampling noise.
130	
131	\subsection*{Holdout Generator Split Validation}
132	\label{app:holdout-split}
133	
134	To confirm the DDR partition is not an artifact of the specific generator pool, we split the eight generators into disjoint selection (4) and validation (4) sets, compute per-subset pooled $(|\rho|, d)$, and check whether all seven features receive the same zone assignment in both subsets.
135	We evaluate two complementary splits to avoid dependence on a single partition:
136	Split~A selects \{Pythia-2.8B, Qwen3-1.7B, OLMo, Mistral\} (validation: Pythia-1B, Qwen3-0.6B, Qwen3-8B, Llama);
137	Split~B selects \{Pythia-1B, Qwen3-0.6B, OLMo, Mistral\} (validation: Pythia-2.8B, Qwen3-1.7B, Qwen3-8B, Llama).
138	
139	\begin{table}[ht]
140	\centering
141	\small
142	\caption{Holdout split validation of the DDR partition. Selection (sel) and validation (val) $|\rho|$ and $d$ for two disjoint 4/4 generator splits. Zone assignment is identical across all four subsets for every feature.}
143	\label{tab:holdout-split}
144	\resizebox{\linewidth}{!}{%
145	\begin{tabular}{llcccccc}
146	\toprule
147	& & \multicolumn{3}{c}{\textbf{Split A}} & \multicolumn{3}{c}{\textbf{Split B}} \\
148	\cmidrule(lr){3-5} \cmidrule(lr){6-8}
149	\textbf{Zone} & \textbf{Feature} & sel $|\rho|$ & val $|\rho|$ & $\Delta|\rho|$ & sel $|\rho|$ & val $|\rho|$ & $\Delta|\rho|$ \\
150	\midrule
151	\multirow{3}{*}{Drifting} & $\bar{H}$ (ent.\ mean) & 0.60 & 0.58 & 0.02 & 0.60 & 0.58 & 0.02 \\
152	 & TTR & 0.61 & 0.59 & 0.02 & 0.60 & 0.59 & 0.01 \\
153	 & hapax ratio & 0.62 & 0.60 & 0.02 & 0.62 & 0.61 & 0.01 \\
154	\midrule
155	Intermediate & $\sigma_H$ (ent.\ std) & 0.19 & 0.21 & 0.02 & 0.22 & 0.17 & 0.05 \\
156	\midrule
157	\multirow{3}{*}{Near-stat.} & $H_{\min}$ (ent.\ min) & 0.39 & 0.36 & 0.03 & 0.38 & 0.37 & 0.01 \\
158	 & $H_{\max}$ (ent.\ max) & 0.05 & 0.05 & 0.00 & 0.04 & 0.06 & 0.02 \\
159	 & tail decay & 0.10 & 0.08 & 0.02 & 0.11 & 0.07 & 0.04 \\
160	\bottomrule
161	\end{tabular}}
162	\end{table}
163	
164	Under simple joint $(|\rho|, d)$ thresholds, both splits produce a 3/2/2 partition: entropy min is classified as a second intermediate feature due to its elevated pooled $|\rho|$ (0.36--0.39).
165	However, entropy min's binary (gen-1 vs.\ gen-2+) $d$ values are uniformly below 0.06 across all four split${\times}$subset combinations, consistent with near-stationarity on the task-relevant metric; its pooled $|\rho|$ reflects change concentrated at the gen-0/gen-1 boundary rather than sustained drift.
166	Five of seven features are unambiguously classified under any reasonable criterion; entropy min's boundary status is resolved by the binary-task $d$ criterion.
167	
168	Selection and validation subsets produce identical partitions in both splits (Table~\ref{tab:holdout-split}; Figure~\ref{fig:holdout-scatter}).
169	The maximum $\Delta|\rho|$ between selection and validation is 0.05 (entropy std, Split~B), and the minimum gap between adjacent zones remains $>$0.15 in all subsets.
170	
171	\begin{figure}[t]
172	\centering
173	\includegraphics[width=\linewidth]{fig_ddr_holdout_split.pdf}
174	\caption{Holdout split validation in $(|\rho|, d)$ space. Filled markers: selection set; hollow: validation set. Zone assignments are identical across subsets; selection/validation pairs cluster tightly for all features.}
175	\label{fig:holdout-scatter}
176	\end{figure}
177	
178	\subsection*{Heteroscedasticity Sensitivity}
179	\label{app:heteroscedasticity}
180	
181	Levene tests reject equal variance between gen-1 and gen-2+ for drifting features ($p < 10^{-10}$; variance ratios 1.86--2.21).
182	To verify that the DDR partition is robust to this heteroscedasticity, we supplement pooled Cohen's $d$ with Glass's $\Delta$ (using the gen-1 standard deviation as denominator) and Cliff's $\delta$ (a non-parametric ordinal effect size; Table~\ref{tab:effect-sizes}).
183	
184	\begin{table}[ht]
185	\centering
186	\small
187	\caption{Effect size comparison (gen-1 vs.\ gen-2+, $N$\,=\,29{,}095). Glass's $\Delta$ uses the gen-1 SD as denominator; Cliff's $\delta$ thresholds follow Romano et al.\ (2006): $|\delta| < 0.147$ negligible, $< 0.33$ small, $< 0.474$ medium, otherwise large.}
188	\label{tab:effect-sizes}
189	\begin{tabular}{llrrr}
190	\toprule
191	\textbf{Zone} & \textbf{Feature} & \textbf{$|d|$} & \textbf{$|\Delta|$} & \textbf{$|\delta|$} \\
192	\midrule
193	\multirow{3}{*}{Drifting} & ent.\ mean & 1.054 & 1.410 & 0.587 \\
194	 & TTR & 0.814 & 1.116 & 0.510 \\
195	 & hapax ratio & 0.735 & 0.936 & 0.528 \\
196	\midrule
197	Intermediate & ent.\ std & 0.457 & 0.605 & 0.295 \\
198	\midrule
199	\multirow{3}{*}{Near-stat.} & tail decay & 0.087 & 0.099 & 0.072 \\
200	 & ent.\ max & 0.062 & 0.065 & 0.021 \\
201	 & ent.\ min & 0.016 & 0.015 & 0.354$^{\dagger}$ \\
202	\bottomrule
203	\end{tabular}
204	\end{table}
205	
206	\noindent Effect sizes in Table~\ref{tab:effect-sizes} are computed on the binary task (gen-1 vs.\ gen-2+); the main text (\S\ref{sec:results-differential}) reports 3-class pooled $d$ values (e.g., hapax ratio $d{=}0.74$), which are slightly larger because the gen-0/gen-1 contrast contributes additional separation.
207	Glass's $\Delta$ amplifies drifting effects (1.41 vs.\ 1.05 for entropy mean) because gen-2+ variance exceeds gen-1 variance (ratio 2.08); pooled Cohen's $d$ is therefore conservative.
208	Near-stationary features remain negligible under both parametric metrics ($|\Delta| \leq 0.099$).
209	The minimum drifting-to-maximum-near-stationary gap is $9.5\times$ under Glass's $\Delta$ (0.936\,/\,0.099); heteroscedasticity does not erode the partition.
210	Cliff's $\delta$ classifies all drifting features as ``large'' ($|\delta| > 0.474$) and entropy std as ``small'' ($|\delta|{=}0.295$), consistent with the parametric partition.
211	
212	\noindent $^{\dagger}$Entropy min's elevated Cliff's $\delta$ (0.354, ``medium'') reflects distributional shape asymmetry between gen-1 and gen-2+ that rank-based statistics detect but location measures do not (Cohen's $d{=}0.016$, Glass's $\Delta{=}0.015$).
213	This is consistent with its documented boundary status (\S\ref{sec:results-differential}): the gen-0/gen-1 transition produces rank-order shifts that persist into deeper generations without affecting the mean.
214	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51f00ffe-5c3d-4621-8e9d-ac23c0d574fc",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "ea47b4d8-1c51-4e85-9c55-45b1a938fe76",
  "sourceToolAssistantUUID": "51f00ffe-5c3d-4621-8e9d-ac23c0d574fc",
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

_source line 35 · 2026-05-25T20:38:52.787Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RHoScvERU5dcs4eNbaXP5z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_iterative_comparison.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea47b4d8-1c51-4e85-9c55-45b1a938fe76",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPvzXfZavqSsV5ZghBKu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf26788d-6d2a-42d6-aac4-98e56ddaef39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUPSvoeobfQAAfbFh7jiwN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11566,
      "cache_read_input_tokens": 37185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11566,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 36 · 2026-05-25T20:38:52.792Z_

<details><summary>↩ Tool result · `toolu_01RHoScvERU5dcs4eNbaXP5z`</summary>

```text
1	\begin{table*}[!t]
2	\centering
3	\small
4	\caption{Comparison with concurrent iterative-generation studies. All three examine how repeated LLM inference transforms text, but differ in chain operator, analytic lens, and downstream goal.}
5	\label{tab:iterative-comparison}
6	\resizebox{\textwidth}{!}{%
7	\begin{tabular}{@{}l p{2.2cm} p{2.4cm} p{2.4cm} p{2.0cm} c p{3.4cm}@{}}
8	\toprule
9	\textbf{Study} & \textbf{Chain Type} & \textbf{Feature Space} & \textbf{Analysis Goal} & \textbf{Generator Scale} & \textbf{Steps} & \textbf{Core Insight} \\
10	\midrule
11	\citet{broken_telephone}
12	  & Back-translation (6 bridge langs); rephrasing (ablation)
13	  & Surface overlap (BLEU, ROUGE, METEOR, ChrF, BERTScore) + atomic factuality (FActScore)
14	  & Factuality degradation rate across iterations
15	  & 7--9B (3 open models)
16	  & 100
17	  & Factual accuracy decays progressively; rate governed by source--bridge linguistic distance \\
18	\addlinespace
19	\citet{markovian_chains}
20	  & Rephrasing + round-trip translation
21	  & String recurrence time, distinct-output count, similarity plateau (METEOR), KL contraction
22	  & Convergence \& diversity dynamics of inference-time Markov chains
23	  & 7--8B (3 open + GPT-4o-mini)
24	  & 50
25	  & Greedy decoding collapses to 1--4 recurrent outputs; sampling sustains 10--20\,+ realizations \\
26	\addlinespace
27	\textbf{Ours}
28	  & Open-ended continuation (no meaning-preserving constraint)
29	  & Token-level NLL statistics (location, scale, shape) + lexical diversity
30	  & Depth classification + DDR decomposition into generator \& depth effects
31	  & 0.6--8B (8 models)
32	  & 5
33	  & NLL location drifts monotonically with depth while shape remains invariant, enabling per-generator depth profiling \\
34	\bottomrule
35	\end{tabular}}
36	\end{table*}
37	
38	Table~\ref{tab:iterative-comparison} compares this work with two concurrent studies on iterative LLM generation.
39	All three examine how repeated inference transforms text, but differ in chain operator, analytic lens, and downstream goal.
40	Our continuation-chain setting permits richer depth signal and enables the location/shape decomposition that defines DDR.
41	
42	\paragraph{Finding-level connections.}
43	\citet{broken_telephone}'s factuality degradation under back-translation chains parallels DDR's location drift: both document monotonic loss of input-specific information with iteration depth, though the former measures semantic content loss while DDR captures distributional compression in the NLL feature space.
44	Their finding that degradation rate scales with source--bridge linguistic distance mirrors our observation that elaboration prompts attenuate DDR (Appendix~\ref{app:prompt-type}): tighter semantic constraints slow both factuality decay and distributional drift.
45	
46	\citet{markovian_chains}'s convergence dynamics under greedy decoding (collapse to 1--4 recurrent outputs within 50 steps) aligns with our greedy-decoding experiment where the DDR partition persists: shape features remain near-stationary (mean $|d|{=}0.05$) while location drift is maintained (mean $d{=}0.94$; Appendix~\ref{app:decoding-strategy}). This confirms that DDR is an empirical regularity of autoregressive generation independent of sampling stochasticity.
47	Their KL contraction analysis complements DDR: where they quantify \emph{how fast} the output distribution contracts, DDR decomposes \emph{what} contracts (location) from what is preserved (shape).
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf26788d-6d2a-42d6-aac4-98e56ddaef39",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "ac060429-fd32-4ada-a6dc-794737676c2b",
  "sourceToolAssistantUUID": "bf26788d-6d2a-42d6-aac4-98e56ddaef39",
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

_source line 37 · 2026-05-25T20:38:53.252Z_

<details open><summary>🔧 Tool call — Read · `toolu_011RZXaaiHDqgmTwoc8Fe6jD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac060429-fd32-4ada-a6dc-794737676c2b",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPvzXfZavqSsV5ZghBKu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "072b14da-e8a3-4d17-9d40-041fadb396bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUPSvoeobfQAAfbFh7jiwN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11566,
      "cache_read_input_tokens": 37185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11566,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 38 · 2026-05-25T20:38:53.256Z_

<details><summary>↩ Tool result · `toolu_011RZXaaiHDqgmTwoc8Fe6jD`</summary>

```text
1	To assess whether depth signal extends beyond handcrafted features, we fine-tune a pretrained language model end-to-end as a depth classifier using QLoRA \cite{qlora}.
2	
3	\paragraph{Setup.}
4	We fine-tune Qwen3-0.6B-Base with LoRA rank 16, learning rate $2 \times 10^{-4}$, and 3 epochs, framing depth estimation as 5-class sequence classification (gen-0 through gen-4).\footnote{Evaluated on a 4-generator subset (Pythia-1B, OLMo-2-1B, Qwen3-0.6B, Qwen3-1.7B) using 5-fold stratified CV; XGBoost 3-class F1\,=\,0.805 under the same protocol. We expect 8-generator training to further improve given additional diversity; the comparison direction is preserved.}
5	For 3-class evaluation, we collapse predictions into gen-0\,/\,gen-1\,/\,gen-2+ post hoc.
6	All results use 5-fold stratified cross-validation on the 4-generator subset.
7	
8	\begin{table}[ht]
9	\centering
10	\small
11	\caption{QLoRA end-to-end depth classification vs.\ XGBoost on handcrafted features, under 5-fold stratified CV (4-generator subset).}
12	\label{tab:qlora}
13	\resizebox{\linewidth}{!}{%
14	\begin{tabular}{lccc}
15	\toprule
16	\textbf{Method} & \textbf{5-class F1} & \textbf{3-class F1} & \textbf{Per-class F1 (5-class)} \\
17	\midrule
18	XGBoost (7 features) & 0.497 $\pm$ 0.008 & 0.805 $\pm$ 0.008 & --- \\
19	QLoRA (Qwen3-0.6B)   & 0.583 $\pm$ 0.010 & 0.905 $\pm$ 0.003 & 0.999\,/\,0.796\,/\,0.413\,/\,0.259\,/\,0.447 \\
20	\bottomrule
21	\end{tabular}}
22	\end{table}
23	
24	\paragraph{Results.}
25	QLoRA achieves 3-class F1\,=\,0.905 ($\pm$0.003) under 5-fold stratified CV on a 4-generator subset, a +10.0\,pp improvement over the same-subset XGBoost baseline (0.805).
26	On 5-class evaluation, QLoRA reaches F1\,=\,0.583 ($\pm$0.010) vs.\ 0.497 for XGBoost (+8.6\,pp), with the largest gains at gen-1 (0.796 vs.\ 0.650) and gen-2 (0.413 vs.\ 0.267).
27	The gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\,=\,0.259), consistent with the feature-level analysis in \S\ref{sec:discussion}.
28	
29	\paragraph{Hyperparameter robustness.}
30	A second run with LoRA rank 32 and seed 123 yields 5-class F1\,=\,0.587 ($\pm$0.005) and 3-class F1\,=\,0.905 ($\pm$0.004), which confirms stability across hyperparameter and seed variation ($\Delta < 1$\,pp on both metrics).
31	
32	\paragraph{Implications.}
33	The substantial 3-class improvement demonstrates that raw token embeddings contain depth signal beyond what summary statistics capture; the seven handcrafted features are a strong but lossy compression of the full distributional information.
34	End-to-end fine-tuning exploits token-level patterns (e.g., positional regularities, n-gram repetitions) that aggregate features cannot represent.
35	This confirms that the depth signal documented in our main analysis is real and exploitable beyond engineered features, while the handcrafted approach retains practical advantages: interpretability, computational efficiency (no GPU inference), and the ability to reveal the differential depth response pattern that motivates the task formulation.
36	The QLoRA ceiling thus represents an information-asymmetric upper bound rather than a competing method: it consumes the full token sequence (0.6B parameters, GPU inference) whereas the 7-feature ensemble distills the signal into interpretable scalars that expose \emph{why} depth is detectable, a decomposition that end-to-end models cannot provide.
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "072b14da-e8a3-4d17-9d40-041fadb396bc",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "8581fb73-740a-43e1-a042-7889231dfc0c",
  "sourceToolAssistantUUID": "072b14da-e8a3-4d17-9d40-041fadb396bc",
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

_source line 39 · 2026-05-25T20:38:54.268Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y3zdMxJaoNTWRMTeJogGfX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_candidates.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8581fb73-740a-43e1-a042-7889231dfc0c",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPvzXfZavqSsV5ZghBKu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c86039d-3335-48fd-8163-524a48b1a0e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUPSvoeobfQAAfbFh7jiwN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11566,
      "cache_read_input_tokens": 37185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11566,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 40 · 2026-05-25T20:38:54.273Z_

<details><summary>↩ Tool result · `toolu_01Y3zdMxJaoNTWRMTeJogGfX`</summary>

```text
1	To verify that the seven retained features are not an arbitrary subset, we screened six additional NLL-distributional statistics as candidate features: median, 90th percentile (p90), interquartile range (IQR), coefficient of variation (CV), skewness, and kurtosis.
2	Table~\ref{tab:candidate-features} reports their DDR coordinates, classification impact, and correlation with retained features.
3	
4	\begin{table}[ht]
5	\centering
6	\small
7	\caption{Candidate feature screening. All six candidates fall in the drifting DDR zone and correlate strongly ($|r| > 0.65$) with existing features. Adding any combination to the baseline degrades or leaves unchanged LOGO 3-class F1; LOFO $\Delta > 0$ indicates that removing the candidate \emph{improves} classification.}
8	\label{tab:candidate-features}
9	\resizebox{\linewidth}{!}{%
10	\begin{tabular}{lccccl}
11	\toprule
12	\textbf{Candidate} & $|\rho|$ & $d$ & \textbf{LOFO} $\Delta$\textbf{F1} & $|r|_{\max}$ & \textbf{Most correlated} \\
13	\midrule
14	median    & 0.685 & 0.794 & $+$0.008 & 0.960 & entropy\_mean \\
15	p90       & 0.693 & 0.960 & $+$0.000 & 0.937 & entropy\_mean \\
16	IQR       & 0.708 & 1.079 & $+$0.007 & 0.908 & entropy\_std \\
17	CV        & 0.633 & 0.980 & $-$0.000 & 0.761 & entropy\_mean \\
18	skewness  & 0.651 & 0.940 & $+$0.010 & 0.780 & entropy\_mean \\
19	kurtosis  & 0.635 & 0.769 & $-$0.003 & 0.650 & entropy\_mean \\
20	\bottomrule
21	\end{tabular}}
22	\end{table}
23	
24	\looseness=-1 All six candidates occupy the drifting zone ($|\rho| > 0.63$, $d > 0.77$), overlapping with entropy mean, TTR, and hapax ratio; none introduces a new axis of depth-dependent variation.
25	Three candidates (median, $r{=}0.96$; p90, $r{=}0.94$; IQR, $r{=}0.91$) are near-perfect linear proxies of existing features.
26	Adding all six to the 6-feature baseline\footnote{Tail decay requires full-vocabulary logits unavailable in the token-NLL subset used for this analysis; we report 6-feature baselines for fair comparison.} reduces 3-class LOGO F1 from 0.733 to 0.722, consistent with overfitting from redundant inputs.
27	LOFO analysis on the extended 12-feature set confirms that removing skewness ($+$0.010), median ($+$0.008), or IQR ($+$0.007) \emph{improves} classification; these features inject noise rather than signal.
28	The retained seven features span three complementary DDR zones (drifting, intermediate, near-stationary) and two modalities (reference-model NLL, surface lexical diversity); additional distributional statistics provide no incremental information.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c86039d-3335-48fd-8163-524a48b1a0e2",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "7f87a908-b386-41d5-888d-ef970ec4d115",
  "sourceToolAssistantUUID": "6c86039d-3335-48fd-8163-524a48b1a0e2",
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

_source line 41 · 2026-05-25T20:38:54.673Z_

<details open><summary>🔧 Tool call — Read · `toolu_014XEfjj2Edzc8LBa75KHDVB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_lofo.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f87a908-b386-41d5-888d-ef970ec4d115",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPvzXfZavqSsV5ZghBKu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bff99886-489b-4f69-b38c-cd65d82b61f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUPSvoeobfQAAfbFh7jiwN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11566,
      "cache_read_input_tokens": 37185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11566,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 42 · 2026-05-25T20:38:54.678Z_

<details><summary>↩ Tool result · `toolu_014XEfjj2Edzc8LBa75KHDVB`</summary>

```text
1	\looseness=-1 We complement the permutation importance analysis (\S\ref{sec:results-differential}) with a leave-one-feature-out ablation. Each row drops one of the seven features and re-evaluates the full 6-gen LOGO protocol; $\Delta$ is the change relative to the full 7-feature ensemble (F1\,=\,0.789).
2	
3	\begin{table}[ht]
4	\centering
5	\small
6	\caption{Leave-one-feature-out ablation (6-gen LOGO). Each row drops one feature and re-evaluates with the LOGO protocol. Sorted by impact magnitude.}
7	\label{tab:lofo}
8	\begin{tabular}{lcc}
9	\toprule
10	\textbf{Dropped feature} & \textbf{LOGO F1} & $\boldsymbol{\Delta}$ \textbf{vs Full} \\
11	\midrule
12	entropy\_max    & 0.774 & $-$1.50\,pp \\
13	entropy\_mean   & 0.783 & $-$0.63\,pp \\
14	ttr             & 0.784 & $-$0.55\,pp \\
15	hapax\_ratio    & 0.785 & $-$0.42\,pp \\
16	tail\_decay     & 0.786 & $-$0.33\,pp \\
17	entropy\_std    & 0.786 & $-$0.29\,pp \\
18	entropy\_min    & 0.789 & $+$0.01\,pp \\
19	\midrule
20	Full (7 features) & 0.789 & --- \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	\paragraph{Analysis.}
26	\looseness=-1 Entropy\_max causes the largest degradation when removed ($-$1.5\,pp), despite ranking only fourth in permutation importance (split frequency 0.063). This indicates that entropy\_max provides unique signal (capturing the most surprising token under the reference model) that is not redundant with other features.
27	Conversely, entropy\_min is fully redundant ($\Delta$\,=\,+0.01\,pp), consistent with its near-zero permutation importance (0.015).
28	Six of seven features contribute positively to the ensemble, which confirms that the 7-feature design is not over-specified.
29	
30	\looseness=-1 To verify that feature importance generalizes beyond the original 6-generator subset, we repeat the LOFO analysis on the full 8-generator set (37,058 samples, 10-fold stratified CV). Table~\ref{tab:lofo-8gen} confirms consistent rankings: \texttt{entropy\_max} remains the most impactful feature ($\Delta=-0.019$), followed by \texttt{entropy\_mean} ($\Delta=-0.012$). All seven features contribute positively, with no feature becoming redundant upon dataset expansion.
31	
32	\paragraph{Minimal sufficient subset.}
33	\looseness=-1 To assess feature redundancy, we evaluate all $\binom{7}{2}{=}21$ two-feature subsets under 10-fold stratified CV (8-gen, 3-class).
34	The best pair is \{entropy\_mean, entropy\_max\}, achieving F1\,=\,0.68 (one drifting and one stationary feature), which captures 88\% of the full-ensemble performance (0.771) and confirms that the DDR partition's two components are individually informative.
35	Adding the remaining five features yields +9.1\,pp; the full set provides meaningful complementarity beyond the minimal core. Nevertheless, the two-feature result demonstrates that the depth signal is not an artifact of feature-set size.
36	
37	\begin{table}[ht]
38	\centering
39	\small
40	\caption{Leave-one-feature-out importance on the full 8-generator set (37,058 samples). Ranking is consistent with the 6-generator subset (Table~\ref{tab:lofo}).}
41	\label{tab:lofo-8gen}
42	\begin{tabular}{lcc}
43	\toprule
44	\textbf{Configuration} & \textbf{3-class F1} & $\boldsymbol{\Delta}$ \\
45	\midrule
46	Full (7 features) & 0.771 & --- \\
47	\midrule
48	$-$ entropy\_max    & 0.752 & $-$0.019 \\
49	$-$ entropy\_mean   & 0.759 & $-$0.012 \\
50	$-$ entropy\_std    & 0.763 & $-$0.007 \\
51	$-$ ttr             & 0.764 & $-$0.007 \\
52	$-$ hapax\_ratio    & 0.765 & $-$0.005 \\
53	$-$ entropy\_min    & 0.766 & $-$0.005 \\
54	$-$ tail\_decay     & 0.767 & $-$0.004 \\
55	\bottomrule
56	\end{tabular}
57	\end{table}
58	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bff99886-489b-4f69-b38c-cd65d82b61f4",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "99f47baa-7602-495a-a666-8ea1a6049f5f",
  "sourceToolAssistantUUID": "bff99886-489b-4f69-b38c-cd65d82b61f4",
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

_source line 43 · 2026-05-25T20:38:55.766Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HUVvxaEuzzYzLg3hsDAQHM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_variance_decomposition.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99f47baa-7602-495a-a666-8ea1a6049f5f",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPvzXfZavqSsV5ZghBKu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c7ea582-67f2-4c34-9e07-0ee4fda1f9a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUPSvoeobfQAAfbFh7jiwN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11566,
      "cache_read_input_tokens": 37185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11566,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 44 · 2026-05-25T20:38:55.771Z_

<details><summary>↩ Tool result · `toolu_01HUVvxaEuzzYzLg3hsDAQHM`</summary>

```text
1	\subsection{Variance Decomposition}
2	\label{app:variance-decomposition}
3	
4	To quantify the mechanistic structure underlying DDR, we decompose each feature's variance into depth, generator, interaction, and residual components via two-way ANOVA (Type~II; Table~\ref{tab:anova_decomposition}).
5	
6	\begin{table}[ht]
7	\centering
8	\caption{Two-way ANOVA variance decomposition (classical $\eta^2$; proportions of total SS) for depth $\times$ generator ($N$\,=\,37{,}058). Location features show dominant depth effects ($\eta^2_{\text{depth}} {=} 0.34$--$0.37$); shape features are depth-invariant ($\eta^2_{\text{depth}} < 0.01$). All effects $p < 10^{-6}$.}
9	\label{tab:anova_decomposition}
10	\small
11	\begin{tabular}{@{}l cccc@{}}
12	\toprule
13	Feature & $\eta^2_{\text{depth}}$ & $\eta^2_{\text{gen}}$ & $\eta^2_{\text{int}}$ & $\eta^2_{\text{resid}}$ \\
14	\midrule
15	\multicolumn{5}{@{}l}{\textit{Location (drifting)}} \\
16	\quad Ent.\ Mean & \textbf{0.341} & 0.022 & 0.010 & 0.627 \\
17	\quad TTR & \textbf{0.370} & 0.024 & 0.007 & 0.599 \\
18	\quad Hapax Ratio & \textbf{0.364} & 0.017 & 0.006 & 0.612 \\
19	\addlinespace
20	\multicolumn{5}{@{}l}{\textit{Shape (near-stationary)}} \\
21	\quad Ent.\ Max & 0.007 & 0.002 & 0.003 & 0.988 \\
22	\quad Ent.\ Min & 0.002 & 0.001 & 0.001 & 0.996 \\
23	\quad Tail Decay & 0.002 & 0.023 & 0.009 & 0.967 \\
24	\addlinespace
25	\multicolumn{5}{@{}l}{\textit{Intermediate}} \\
26	\quad Ent.\ Std & 0.054 & 0.020 & 0.011 & 0.915 \\
27	\bottomrule
28	\end{tabular}
29	\end{table}
30	
31	% Figure moved to main text (Figure~\ref{fig:variance-decomp} in \S\ref{sec:discussion})
32	
33	The depth factor explains 34--37\% of location-feature variance but $<$1\% of shape-feature variance, a ${>}48\times$ ratio that quantifies the DDR partition as a systematic depth$\times$feature-type interaction rather than a post-hoc grouping.
34	Generator identity contributes comparably across both groups ($\eta^2_{\text{gen}} {=} 0.02$); the asymmetry is specific to depth, not generator.
35	Interaction terms are uniformly small ($\eta^2_{\text{int}} < 0.011$); the depth effect on location features operates consistently across generators.
36	
37	Exponential convergence fitting ($f(d) {=} a \cdot e^{-\lambda d} + c$) on per-generator depth trajectories corroborates this: location features converge with moderate rates ($\lambda {=} 0.40 \pm 0.26$, $R^2 {=} 0.99$), consistent with contraction toward a generator-specific fixed point under iterated autoregressive generation, while shape features show degenerate fits ($\lambda {=} 5.3 \pm 8.4$, $R^2 {=} 0.73$) reflecting their flat trajectories.
38	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c7ea582-67f2-4c34-9e07-0ee4fda1f9a1",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "4e8e553e-637b-4fba-a51e-19b9d45b897d",
  "sourceToolAssistantUUID": "0c7ea582-67f2-4c34-9e07-0ee4fda1f9a1",
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

_source line 45 · 2026-05-25T20:38:55.829Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JrN9jhbmcxe39ZJVCSjmzD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_length.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e8e553e-637b-4fba-a51e-19b9d45b897d",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPvzXfZavqSsV5ZghBKu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f5d2130-63f1-4937-8dc7-60b70a144b59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUPSvoeobfQAAfbFh7jiwN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11566,
      "cache_read_input_tokens": 37185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11566,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 46 · 2026-05-25T20:38:55.837Z_

<details><summary>↩ Tool result · `toolu_01JrN9jhbmcxe39ZJVCSjmzD`</summary>

```text
1	% Appendix — Length Confound Analysis
2	% Data source: 8-generator LOGO corpus (37,058 samples)
3	
4	Surface diversity features (TTR, hapax ratio) mechanically depend on text length:
5	shorter texts yield higher type-token ratios by construction.
6	If generation depth systematically shortens text, observed depth trends could be length artifacts rather than genuine distributional shifts.
7	We investigate with three complementary analyses.
8	
9	\paragraph{(a) Length--depth correlation.}
10	Spearman rank correlation between word count and generation depth is weak across all eight generators ($|\rho| < 0.14$); depth does not systematically shorten or lengthen text in our corpus.
11	
12	\paragraph{(b) Length--feature correlations.}
13	While length--depth correlation is weak, individual features show moderate length dependence:
14	tail\_decay ($|\rho| = 0.38$), hapax\_ratio ($|\rho| = 0.30$), and TTR ($|\rho| = 0.29$).
15	Reference-model features show weaker length correlations (entropy\_mean $|\rho| = 0.09$, entropy\_std $|\rho| = 0.18$).
16	This motivates the length-matched evaluation below: if length mediates some depth--feature association, controlling for length will reduce classification performance.
17	
18	\paragraph{(c) Length-matched classification.}
19	We subsample the dataset so that word-count distributions are equalized across depth classes (gen-0\,/\,gen-1\,/\,gen-2+), then retrain the binary XGBoost classifier under pooled LOGO (8-fold).
20	Length-matched binary F1\,=\,0.724, down from 0.770 on the unmatched set ($\Delta$\,=\,$-$0.046).
21	The matched subset is smaller than the full corpus; a random-subsample control at equal $N$ (below) isolates the deconfounding effect from the sample-size reduction.
22	To distinguish this from a sample-size effect, we run a random-subsample control at equal $N$ without length matching: F1\,=\,0.767, which confirms that the 0.046 drop reflects genuine length deconfounding rather than reduced data.
23	
24	\paragraph{Conclusion.}
25	Length accounts for approximately 6\% of discriminative performance ($\Delta$\,=\,0.046 out of 0.770).
26	The majority of the depth signal is length-independent: length-matched F1 (0.724) remains far above chance and substantially above all individual detection baselines (\S\ref{sec:results-baselines}).
27	Surface features (TTR, hapax\_ratio) partially co-vary with length, but their depth-discriminative contribution persists after length control, consistent with generation-induced vocabulary compression operating independently of text truncation.
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f5d2130-63f1-4937-8dc7-60b70a144b59",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "172a7571-6c52-4000-b75b-7170f9ba19cd",
  "sourceToolAssistantUUID": "5f5d2130-63f1-4937-8dc7-60b70a144b59",
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

_source line 47 · 2026-05-25T20:39:00.533Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WPAS9bRvhyWjx16UYgvsqn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "172a7571-6c52-4000-b75b-7170f9ba19cd",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPw1djxp7BCowZmerZNF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbb04954-a845-4116-9ec7-daf1ab34b3a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJMVXXwsvvrr4M22bQEiyu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18984,
      "cache_read_input_tokens": 48751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18984,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 48 · 2026-05-25T20:39:00.544Z_

<details><summary>↩ Tool result · `toolu_01WPAS9bRvhyWjx16UYgvsqn`</summary>

```text
1	We analyze misclassification patterns in the binary LOGO task (gen-1 vs.\ gen-2+) across 29,095 test samples (overall error rate 28.1\%).
2	
3	\paragraph{Error asymmetry.}
4	The error distribution is highly asymmetric: 86.2\% of errors are false negatives (gen-2+ predicted as gen-1), while only 13.8\% are false positives (Table~\ref{tab:error-analysis}).
5	The classifier systematically under-predicts depth, consistent with the DDR pattern: shallow gen-2+ samples that have not yet accumulated sufficient distributional drift are indistinguishable from gen-1.
6	Among generators, Mistral-7B shows the highest error rate (45.0\%), while Pythia-1B is easiest (18.2\%). Larger models produce gen-2+ text closer to the gen-1 distribution.
7	
8	\begin{table}[ht]
9	\centering
10	\small
11	\caption{Binary classification error analysis (gen-1 vs.\ gen-2+) under LOGO cross-validation. FP: gen-1 misclassified as gen-2+; FN: gen-2+ misclassified as gen-1. Errors are dominated by false negatives (86.2\%).}
12	\label{tab:error-analysis}
13	\begin{tabular}{lrrrr}
14	\toprule
15	\textbf{Generator} & $N$ & \textbf{FP} & \textbf{FN} & \textbf{Err.\%} \\
16	\midrule
17	Pythia-1B & 3560 & 188 & 460 & 18.2 \\
18	Pythia-2.8B & 3614 & 129 & 737 & 24.0 \\
19	OLMo-2-1B & 3718 & 154 & 900 & 28.3 \\
20	Qwen3-0.6B & 3542 & 234 & 511 & 21.0 \\
21	Qwen3-1.7B & 3621 & 175 & 639 & 22.5 \\
22	Qwen3-8B & 3502 & 93 & 1104 & 34.2 \\
23	Llama-3.2-3B & 3685 & 82 & 1030 & 30.2 \\
24	Mistral-7B & 3853 & 75 & 1659 & 45.0 \\
25	\midrule
26	\textbf{Overall} & 29095 & 1130 & 7040 & 28.1 \\
27	\bottomrule
28	\end{tabular}
29	\end{table}
30	
31	\paragraph{Per-depth error rates.}
32	Error rates decrease monotonically with depth (Table~\ref{tab:error-depth}): depth-2 samples are the primary failure point (48.4\% error rate), followed by depth-3 (29.2\%) and depth-4 (20.3\%).
33	The monotonic decrease confirms that deeper generations accumulate progressively stronger depth signatures; the gen-1$\to$gen-2 transition is the hardest boundary.
34	
35	\begin{table}[ht]
36	\centering
37	\small
38	\caption{Error rate by generation depth in binary classification. Depth-2 exhibits the highest misclassification rate (48.4\%); the gen-1$\to$gen-2 transition is the primary confusion boundary.}
39	\label{tab:error-depth}
40	\begin{tabular}{crrrl}
41	\toprule
42	\textbf{Depth} & $N$ & \textbf{Errors} & \textbf{Rate (\%)} & \textbf{Type} \\
43	\midrule
44	1 & 7896 & 1130 & 14.3 & FP \\
45	2 & 7512 & 3637 & 48.4 & FN \\
46	3 & 7032 & 2051 & 29.2 & FN \\
47	4 & 6655 & 1352 & 20.3 & FN \\
48	\bottomrule
49	\end{tabular}
50	\end{table}
51	
52	\paragraph{Feature-level explanation.}
53	Misclassified samples occupy the overlap zone between gen-1 and gen-2+ distributions (Table~\ref{tab:error-features}): they exhibit elevated entropy ($\bar{H}$: 2.26 vs.\ 1.57, $p<10^{-300}$) and lexical diversity (TTR: 0.464 vs.\ 0.302), retaining gen-1-like characteristics.
54	In contrast, shape features show no discriminating power: entropy max ($p = \text{n.s.}$) and tail decay ($p = \text{n.s.}$), consistent with the DDR pattern (\S\ref{sec:results-differential}).
55	
56	\begin{table}[ht]
57	\centering
58	\small
59	\caption{Feature comparison between correctly and incorrectly classified samples. Misclassified samples show substantially higher entropy and lexical diversity but no difference in shape features.}
60	\label{tab:error-features}
61	\begin{tabular}{lcccl}
62	\toprule
63	\textbf{Feature} & \textbf{Correct} & \textbf{Incorrect} & $\Delta$ & $p$ \\
64	\midrule
65	$\bar{H}$ & 1.5700 & 2.2618 & +0.6918 & $<10^{-300}$ $^{***}$ \\
66	$\sigma_H$ & 1.6227 & 1.7413 & +0.1186 & $<10^{-300}$ $^{***}$ \\
67	$H_{\min}$ & 0.0281 & 0.0330 & +0.0049 & 1.0e-294 $^{***}$ \\
68	$H_{\max}$ & 7.5255 & 7.5251 & -0.0004 & n.s. \\
69	$\beta_{\mathrm{tail}}$ & -0.0023 & -0.0023 & +0.0000 & n.s. \\
70	TTR & 0.3024 & 0.4635 & +0.1612 & $<10^{-300}$ $^{***}$ \\
71	Hapax & 0.1760 & 0.3131 & +0.1371 & $<10^{-300}$ $^{***}$ \\
72	\bottomrule
73	\end{tabular}
74	\end{table}
75	
76	\paragraph{3-class confusion matrix.}
77	Table~\ref{tab:confusion-3class} shows the aggregated confusion matrix: gen-0 is near-perfectly classified ($>$99\%), while gen-1 and gen-2+ exhibit substantial cross-contamination (30.2\% of gen-2+ predicted as gen-1), consistent with the binary error analysis.
78	
79	\begin{table}[ht]
80	\centering
81	\small
82	\caption{Aggregated 3-class confusion matrix (\%) across 8-fold LOGO. Gen-0 is near-perfectly classified, while gen-2+ is frequently confused with gen-1.}
83	\label{tab:confusion-3class}
84	\begin{tabular}{l|ccc}
85	\toprule
86	 & \multicolumn{3}{c}{\textbf{Predicted}} \\
87	\textbf{True} & gen-0 & gen-1 & gen-2+ \\
88	\midrule
89	gen-0 & 99.2 & 0.8 & 0.1 \\
90	gen-1 & 7.3 & 78.4 & 14.3 \\
91	gen-2+ & 3.0 & 30.2 & 66.7 \\
92	\bottomrule
93	\end{tabular}
94	\end{table}
95	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbb04954-a845-4116-9ec7-daf1ab34b3a5",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "0ff29497-1a0a-4ca7-be32-2656f24e41b9",
  "sourceToolAssistantUUID": "bbb04954-a845-4116-9ec7-daf1ab34b3a5",
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

_source line 49 · 2026-05-25T20:39:01.577Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XZYLty3xsZoq96cRsbH98i`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_nll_distribution.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ff29497-1a0a-4ca7-be32-2656f24e41b9",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPw1djxp7BCowZmerZNF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37b29bdd-b610-4d63-9583-cf1a7cd10c8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJMVXXwsvvrr4M22bQEiyu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18984,
      "cache_read_input_tokens": 48751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18984,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 50 · 2026-05-25T20:39:01.582Z_

<details><summary>↩ Tool result · `toolu_01XZYLty3xsZoq96cRsbH98i`</summary>

```text
1	% section header and label in main.tex
2	
3	\begin{figure}[t]
4	\centering
5	\includegraphics[width=\columnwidth]{fig_appendix_nll_distribution.pdf}
6	\caption{Token-level NLL distribution by generation depth, aggregated across all 8 generators (Pythia-410M reference model). Dashed lines indicate median NLL per depth. The systematic leftward shift demonstrates that deeper-generation text is increasingly predictable.}
7	\label{fig:nll-dist}
8	\end{figure}
9	
10	Figure~\ref{fig:nll-dist} plots the kernel density of per-token NLL across depths~0--4 (8 generators, 25 texts/depth, ${\sim}$236k tokens, Pythia-410M reference).
11	The distributions shift leftward as depth increases: median NLL drops from 1.64~nats (gen-0) to 0.02 (gen-4). Recursively generated text becomes increasingly predictable.
12	This monotonic compression provides a mechanistic explanation for the entropy-based features driving the depth classifier.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37b29bdd-b610-4d63-9583-cf1a7cd10c8a",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "58c7d9bf-a503-46e2-a1e0-423c0c890da9",
  "sourceToolAssistantUUID": "37b29bdd-b610-4d63-9583-cf1a7cd10c8a",
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

_source line 51 · 2026-05-25T20:39:01.957Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P7LAPh6ox9doyJvnicsWLP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_9gen_scale.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58c7d9bf-a503-46e2-a1e0-423c0c890da9",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPw1djxp7BCowZmerZNF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ded10e24-bb64-4492-bd8e-779d9c47c996",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJMVXXwsvvrr4M22bQEiyu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18984,
      "cache_read_input_tokens": 48751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18984,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 52 · 2026-05-25T20:39:01.961Z_

<details><summary>↩ Tool result · `toolu_01P7LAPh6ox9doyJvnicsWLP`</summary>

```text
1	\subsection{9-Generator Scale Evaluation}\label{app:9gen-scale}
2	
3	This analysis extends the 8-generator LOGO evaluation to nine generators by adding Gemma-2-2B, a model from a previously unrepresented architecture family (Gemma).
4	All results use class-balanced LOGO; the 8-gen averages here (0.770/0.701) differ slightly from Table~\ref{tab:logo-results} (0.762/0.694), which uses an unfiltered protocol.
5	Table~\ref{tab:9gen-logo} reports per-generator LOGO performance under this expanded set.
6	
7	\begin{table}[ht]
8	\centering
9	\caption{9-generator LOGO evaluation. Each row holds out the listed generator at test time. 3-class: gen-0\,/\,gen-1\,/\,gen-2+; binary: gen-1 vs.\ gen-2+. 95\% bootstrap CIs in brackets.}
10	\label{tab:9gen-logo}
11	\small
12	\resizebox{\linewidth}{!}{%
13	\begin{tabular}{llr cc cc}
14	\toprule
15	\textbf{Generator} & \textbf{Family} & \textbf{Params} & \textbf{3-class F1} & \textbf{95\% CI} & \textbf{Binary F1} & \textbf{95\% CI} \\
16	\midrule
17	Pythia-1B       & Pythia  & 1.0B & 0.857 & [0.848, 0.866] & 0.785 & --- \\
18	Qwen3-0.6B      & Qwen    & 0.6B & 0.819 & [0.807, 0.830] & 0.743 & --- \\
19	Pythia-2.8B     & Pythia  & 2.8B & 0.812 & [0.801, 0.822] & 0.728 & --- \\
20	Qwen3-1.7B      & Qwen    & 1.7B & 0.811 & [0.800, 0.823] & 0.746 & --- \\
21	OLMo-2-1B       & OLMo    & 1.5B & 0.773 & [0.762, 0.784] & 0.692 & --- \\
22	Llama-3.2-3B    & Llama   & 3.2B & 0.759 & [0.748, 0.770] & 0.680 & --- \\
23	Qwen3-8B        & Qwen    & 8.2B & 0.696 & [0.683, 0.709] & 0.647 & [0.631, 0.664] \\
24	Gemma-2-2B      & Gemma   & 2.6B & 0.628 & [0.622, 0.634] & 0.440 & [0.432, 0.449] \\
25	Mistral-7B      & Mistral & 7.0B & 0.605 & [0.593, 0.617] & 0.534 & --- \\
26	\midrule
27	\textbf{Average (9-gen)} & & & \textbf{0.751} & & \textbf{0.666} & \\
28	\textbf{Average (8-gen)} & & & \textbf{0.770} & & \textbf{0.701} & \\
29	\bottomrule
30	\end{tabular}}
31	\end{table}
32	
33	\begin{figure}[t]
34	\centering
35	\includegraphics[width=\columnwidth]{fig_appendix_9gen_scale.pdf}
36	\caption{Per-generator 3-class LOGO F1 for the 9-generator evaluation. Gemma-2-2B (orange) is the weakest held-out generator. Dashed line: 9-gen average (0.751). Parameter counts shown in parentheses.}
37	\label{fig:9gen-scale}
38	\end{figure}
39	
40	\paragraph{Overall comparison.}
41	Adding Gemma-2-2B reduces the mean 3-class LOGO F1 from 0.770 (8-gen) to 0.751 (9-gen), a drop of $\Delta = -0.019$.
42	The per-generator F1 values for the original eight generators shift by at most $[-0.011, +0.002]$; the inclusion of Gemma data in training does not destabilize existing generalization patterns.
43	
44	\paragraph{Gemma-2-2B anomaly.}
45	Gemma-2-2B is the weakest held-out generator: 3-class F1\,=\,0.628, binary F1\,=\,0.440.
46	Per-class breakdown reveals a striking asymmetry: gen-0 F1\,=\,0.991 and gen-2+ F1\,=\,0.856, but gen-1 F1\,=\,0.036; the classifier almost entirely fails to identify first-generation Gemma continuations.
47	This is not a data-quality artifact: the Gemma-2-2B partition contains 4{,}957 instances with a balanced depth distribution ($\sim$990 per level).
48	A plausible explanation is that Gemma-2's first-generation continuations occupy a region of feature space highly similar to human-written text (gen-0), causing systematic misclassification of gen-1 as gen-0 or gen-2+.
49	This constitutes an architecture-specific generalization limitation rather than a systemic failure of the depth profiling approach.
50	Several architectural differences may explain this behavior: (a)~Gemma-2's distinct attention mechanism and SentencePiece tokenizer with a larger vocabulary may produce first-generation continuations whose feature-space signature closely resembles human text, causing systematic gen-0/gen-1 confusion; (b)~this anomaly does not affect DDR's validity for the remaining eight generators, where per-generator F1 shifts by at most 0.011 upon Gemma inclusion.
51	
52	\paragraph{Scale effect.}
53	A clear parameter-count gradient emerges across the nine generators: three of four sub-1.7B generators achieve F1\,$>$\,0.81 (OLMo-2-1B at 0.773 is the exception), mid-range models (2--3B) cluster at 0.63--0.81, and large models (7B+) fall to 0.60--0.70.
54	Qwen3-8B (8.2B parameters) achieves 3-class F1\,=\,0.696 under the 9-gen split, compared to 0.701 in the class-balanced 8-gen evaluation; this small difference reflects the changed training composition rather than a property of the Qwen3-8B generator itself.
55	
56	\paragraph{14B-parameter evidence.}
57	Preliminary evidence from a 14.7B generator (Qwen3-14B-Base) confirms that the DDR partition persists at larger scale: Cohen's $d$ for drifting features remains in the large-effect range ($d{=}0.78$--$1.12$), though Spearman $|\rho|$ attenuates by 21--35\%, with entropy mean falling just below the drifting threshold ($|\rho|{=}0.39 < 0.40$, $d{=}0.78$).
58	This scale-dependent signal compression is consistent with larger models producing more self-typical outputs that narrow inter-depth contrasts; the partition structure is preserved even as absolute effect sizes compress.
59	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ded10e24-bb64-4492-bd8e-779d9c47c996",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "1967cd80-7510-43b1-9a58-ff62c58b4171",
  "sourceToolAssistantUUID": "ded10e24-bb64-4492-bd8e-779d9c47c996",
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

_source line 53 · 2026-05-25T20:39:02.962Z_

<details open><summary>🔧 Tool call — Read · `toolu_018DUc7tRhQ5zppJzhJVbohJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ddr_causality.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1967cd80-7510-43b1-9a58-ff62c58b4171",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPw1djxp7BCowZmerZNF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "454a576c-7160-4e9e-bba5-2c8224a2d00f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJMVXXwsvvrr4M22bQEiyu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18984,
      "cache_read_input_tokens": 48751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18984,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 54 · 2026-05-25T20:39:02.968Z_

<details><summary>↩ Tool result · `toolu_018DUc7tRhQ5zppJzhJVbohJ`</summary>

```text
1	This appendix validates the causal predictive power of DDR features through three complementary analyses: permutation importance, Granger causality, and feature intervention.
2	
3	\paragraph{Permutation Importance.}
4	Table~\ref{tab:perm-importance} reports the mean F1 drop when each feature's values are randomly shuffled across the test set (baseline F1\,=\,0.771).
5	Drifting features dominate: their average F1 drop (0.187) is $5.5\times$ larger than the near-stationary average (0.034). Location-shift features, not shape features, drive depth classification.
6	
7	\begin{table}[ht]
8	\centering
9	\small
10	\caption{Permutation importance (8-gen LOGO). Each feature is shuffled independently; the resulting F1 drop quantifies marginal importance. Drifting features average $0.187$ vs.\ near-stationary $0.034$ ($5.5\times$).}
11	\label{tab:perm-importance}
12	\resizebox{\linewidth}{!}{%
13	\begin{tabular}{llcr}
14	\toprule
15	\textbf{Feature} & \textbf{Group} & \textbf{Mean F1 Drop} & \textbf{Rank} \\
16	\midrule
17	hapax\_ratio  & Drifting      & 0.235 & 1 \\
18	entropy\_mean & Drifting      & 0.170 & 2 \\
19	ttr           & Drifting      & 0.156 & 3 \\
20	entropy\_max  & Near-stat.    & 0.070 & 4 \\
21	entropy\_std  & Intermediate  & 0.057 & 5 \\
22	entropy\_min  & Near-stat.    & 0.019 & 6 \\
23	tail\_decay   & Near-stat.    & 0.014 & 7 \\
24	\bottomrule
25	\end{tabular}}
26	\end{table}
27	
28	\paragraph{Granger Causality.}
29	Table~\ref{tab:granger} reports Fisher-combined $p$-values from panel Granger causality tests (lag\,=\,1) across 8 generators ($N$\,=\,29{,}095).
30	Six of seven features exhibit significant Granger causality ($p < 0.001$), meaning past feature values predict future depth beyond what past depth alone explains.
31	The sole exception is entropy\_min ($p$\,=\,0.375). This provides additional evidence for its near-stationary classification: it carries neither large marginal importance (Table~\ref{tab:perm-importance}, rank 7) nor temporal predictive direction.
32	
33	\begin{table}[ht]
34	\centering
35	\small
36	\caption{Granger causality (Fisher combined across 8 generators, lag\,=\,1, $N$\,=\,29{,}095). $\Delta R^2$ is reported where available.}
37	\label{tab:granger}
38	\resizebox{\linewidth}{!}{%
39	\begin{tabular}{lccc}
40	\toprule
41	\textbf{Feature} & \textbf{Combined $p$} & $\boldsymbol{\Delta R^2}$ & \textbf{Significant} \\
42	\midrule
43	entropy\_std  & $< 0.001$ & 0.031 & Yes \\
44	hapax\_ratio  & $< 0.001$ & ---   & Yes \\
45	ttr           & $< 0.001$ & ---   & Yes \\
46	entropy\_mean & $< 0.001$ & ---   & Yes \\
47	entropy\_max  & $< 0.001$ & ---   & Yes \\
48	tail\_decay   & $< 0.001$ & ---   & Yes \\
49	entropy\_min  & $0.375$   & ---   & No  \\
50	\bottomrule
51	\end{tabular}}
52	\end{table}
53	
54	\paragraph{Key Findings.}
55	\begin{enumerate}[nosep,leftmargin=*]
56	\item \textbf{Drifting dominance.} The $5.5\times$ permutation-importance gap confirms that drifting features (entropy\_mean, ttr, hapax\_ratio) are the primary depth signal carriers, consistent with the DDR partition derived from convergence analysis (\S\ref{sec:results-differential}).
57	
58	\item \textbf{Entropy\_min lacks causal direction.} Beyond its small effect size (F1 drop\,=\,0.019), entropy\_min is the only feature without significant Granger causality ($p$\,=\,0.375). This strengthens the near-stationary classification: the feature is neither marginally important nor temporally predictive.
59	
60	\item \textbf{Entropy\_max asymmetry.} Entropy\_max ranks fourth in permutation importance (F1 drop\,=\,0.070) but produces the largest degradation in the counterfactual intervention ($-$2.0\,pp). It provides unique signal not redundant with other features; its causal contribution exceeds its marginal importance.
61	
62	\item \textbf{Mistral heterogeneity.} In per-generator Granger tests, Mistral-7B shows non-significant hapax\_ratio and ttr ($p > 0.4$), though Fisher combination across generators remains significant. This generator-specific attenuation partly explains Mistral's lowest LOGO F1 (0.605) and suggests that DDR depth signatures are weaker in models with heavier repetition penalties.
63	\end{enumerate}
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "454a576c-7160-4e9e-bba5-2c8224a2d00f",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "710df9a6-b71d-436c-a200-94a48ff953cc",
  "sourceToolAssistantUUID": "454a576c-7160-4e9e-bba5-2c8224a2d00f",
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

_source line 55 · 2026-05-25T20:39:03.538Z_

<details open><summary>🔧 Tool call — Read · `toolu_015J1DGR7eYDZmSbxU7xKBK7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_convergence.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "710df9a6-b71d-436c-a200-94a48ff953cc",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPw1djxp7BCowZmerZNF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6d1fc7c-3f5b-4729-ab5b-11b6be176b5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJMVXXwsvvrr4M22bQEiyu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18984,
      "cache_read_input_tokens": 48751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18984,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 56 · 2026-05-25T20:39:03.542Z_

<details><summary>↩ Tool result · `toolu_015J1DGR7eYDZmSbxU7xKBK7`</summary>

```text
1	Figure~\ref{fig:convergence} (main text) visualizes per-feature convergence trajectories across generation depths 0--4, averaged over 8 generators; each feature is expressed as Cohen's $d$ relative to depth~0.
2	Drifting features (hapax ratio, TTR, entropy mean) and the intermediate feature (entropy std) diverge monotonically; lexical diversity features (TTR, hapax ratio) form a fast-convergence group ($|d| > 2$ by depth~2), while entropy mean and entropy std drift more slowly.
3	Near-stationary features (entropy max, tail decay, entropy min) remain within $|d| < 0.25$ across all depths, consistent with location stability.
4	Shaded bands indicate $\pm 1$ standard deviation across generators.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6d1fc7c-3f5b-4729-ab5b-11b6be176b5a",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "7121dbb8-e157-4289-b4b6-cacce887349e",
  "sourceToolAssistantUUID": "a6d1fc7c-3f5b-4729-ab5b-11b6be176b5a",
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

_source line 57 · 2026-05-25T20:39:04.334Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EaL5Y1NVVQWtD43j1oDV4F`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7121dbb8-e157-4289-b4b6-cacce887349e",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPw1djxp7BCowZmerZNF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3d9b10c-33e1-4f33-a11c-c5e378bf3057",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJMVXXwsvvrr4M22bQEiyu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18984,
      "cache_read_input_tokens": 48751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18984,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 58 · 2026-05-25T20:39:04.337Z_

<details><summary>↩ Tool result · `toolu_01EaL5Y1NVVQWtD43j1oDV4F`</summary>

```text
1	\subsection*{Instruction-Tuned Model Results}
2	
3	Table~\ref{tab:instruct} summarizes depth classification under instruction tuning for three model families.
4	All results use within-model 5-fold CV on single-generator chains; LOGO evaluation is available for two models but uses earlier generator subsets (5--6 generators), so cross-model numbers are not directly comparable across rows.
5	
6	\begin{table}[ht]
7	\centering
8	\small
9	\caption{Depth classification: base vs.\ instruction-tuned models (within-model 5-fold CV). $\rho$: Spearman correlation of entropy mean with depth. Rev.: number of features (out of 7) whose $\rho$ reverses sign under instruction tuning.}
10	\label{tab:instruct}
11	\resizebox{\linewidth}{!}{%
12	\begin{tabular}{lcc cc cc c}
13	\toprule
14	& \multicolumn{2}{c}{\textbf{3-class F1}} & \multicolumn{2}{c}{\textbf{Binary F1}} & \multicolumn{2}{c}{$\boldsymbol{\rho}$\textbf{(ent.\ mean)}} & \\
15	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
16	\textbf{Model} & Base & Instruct & Base & Instruct & Base & Instruct & \textbf{Rev.} \\
17	\midrule
18	OLMo-2-1B       & 0.754 & 0.575 & 0.845 & 0.813 & $-$0.64 & $+$0.48 & 6/7 \\
19	Qwen3-1.7B      & 0.769 & 0.732 & 0.861 & 0.875 & $-$0.60 & $+$0.48 & 6/7 \\
20	Llama-3.2-3B    & 0.742 & 0.544 & 0.849 & 0.838 & $-$0.63 & $+$0.23 & 3/7 \\
21	\bottomrule
22	\end{tabular}}
23	\end{table}
24	
25	Instruction tuning degrades 3-class F1 by 3.7--19.9\,pp across all three families, while binary F1 (gen-1 vs.\ gen-2+) changes remain small ($|\Delta| \leq 3.2$\,pp).
26	The asymmetry indicates that instruction tuning primarily disrupts the gen-0/gen-1 boundary (human vs.\ first-generation), consistent with RLHF shifting the output distribution away from human-like text.
27	Entropy-mean $\rho$ reverses sign for all three models ($-0.60$--$-0.64$ base $\rightarrow$ $+0.23$--$+0.48$ instruct), and 6 of 7 features reverse for OLMo and Qwen vs.\ 3 of 7 for Llama.
28	This pattern is consistent with instruction tuning shifting the generation attractor rather than eliminating iterative dynamics (\S\ref{sec:discussion}).
29	
30	\paragraph{Retraining on instruction-tuned data.}
31	To test whether the depth signal persists under instruction tuning with reversed polarity, we retrain the XGBoost classifier on instruction-tuned feature data (Table~\ref{tab:instruct-retrain}).
32	
33	\begin{table}[ht]
34	\centering
35	\small
36	\caption{Classification recovery under instruction-tuned retraining (binary-only: gen-1 vs.\ gen-2+, gen-0 excluded from training and evaluation). Base$\rightarrow$Inst: base-trained classifier tested on instruct data. Note: Table~\ref{tab:instruct} reports higher instruct binary F1 (e.g., OLMo 0.813) because it uses 3-class training with binary evaluation, where gen-0 in training helps the classifier learn the feature space.}
37	\label{tab:instruct-retrain}
38	\begin{tabular}{lccc}
39	\toprule
40	\textbf{Model} & \textbf{Base$\rightarrow$Inst} & \textbf{Retrained} & \textbf{$\Delta$} \\
41	\midrule
42	OLMo-2-1B-Inst   & 0.321 & 0.590 & $+$0.269 \\
43	Qwen3-1.7B-Inst  & 0.500 & 0.660 & $+$0.160 \\
44	Qwen3-0.6B-Inst  & 0.532 & 0.600 & $+$0.068 \\
45	\bottomrule
46	\end{tabular}
47	\end{table}
48	
49	Retraining recovers substantial within-model performance ($+$6.8--26.9\,pp), but the retrained F1 (0.590--0.660) remains below base-model levels (0.69--0.72). Instruction tuning compresses depth signal beyond what retraining on reversed-polarity features can fully recover.
50	
51	\paragraph{DDR structure under instruction tuning.}
52	$k{=}2$ clustering in $(|\rho|, d)$ space on pooled instruct features yields silhouette\,=\,0.372 (vs.\ 0.660 for base models); the clean drifting/non-drifting partition is substantially compressed.
53	The compression is model-dependent: OLMo-Instruct shows near-zero $|\rho|$ for TTR and hapax (0.006, 0.025), while Qwen instruct models retain moderate correlations ($|\rho|{=}0.48$--$0.53$).
54	Cross-condition transfer is near chance in both directions (base$\rightarrow$instruct binary F1\,=\,0.490; instruct$\rightarrow$base F1\,=\,0.454), with the asymmetry ($-$0.036) suggesting that instruct-trained features generalize even less to base distributions than the reverse.
55	These results indicate that instruction tuning compresses the feature-space structure underlying DDR rather than simply reversing feature directions (Figure~\ref{fig:instruct-ddr}).
56	
57	\begin{figure}[t]
58	\centering
59	\includegraphics[width=\columnwidth]{fig_appendix_instruct_ddr.pdf}
60	\caption{DDR partition under base vs.\ instruction-tuned models. (a)~Base models (silhouette\,=\,0.660): clear drifting/non-drifting separation. (b)~Instruction-tuned models (silhouette\,=\,0.372): all features compress toward zero, collapsing the partition; entropy max shifts from near-stationary to intermediate; formerly drifting features (hapax, TTR) lose most of their effect size. Bars show pooled $|d|$; markers show individual generators.}
61	\label{fig:instruct-ddr}
62	\end{figure}
63	
64	\paragraph{Reference model sensitivity.}
65	One hypothesis for the instruct degradation is reference-model mismatch: the base Pythia-410M reference may produce systematically biased NLL estimates on instruction-tuned outputs, masking depth-dependent variation.
66	To test this, we replace the reference with Qwen3-0.6B-Instruct and recompute all features on the two instruct generators.
67	The hypothesis is partially rejected: Qwen3-1.7B-Instruct shows mixed changes (entropy max $d$: $0.51 \to 0.08$, becoming near-stationary; entropy std $d$: $1.07 \to 1.51$, increasing), while OLMo-Instruct loses nearly all depth signal (entropy mean $d$: $1.33 \to 0.02$; tail decay $d$: $0.60 \to 0.06$).
68	The model-dependent heterogeneity rules out reference mismatch as a universal explanation for instruct DDR degradation. Alignment fundamentally reshapes the generation dynamics rather than introducing a correctable measurement artifact.
69	
70	\paragraph{End-to-end instruct classification.}
71	To test whether depth signal persists at the token level despite summary-statistic degradation, we apply the QLoRA end-to-end classifier (Appendix~\ref{app:qlora}) to instruction-tuned data using within-model 5-fold stratified CV (Table~\ref{tab:instruct-qlora}).
72	
73	\begin{table}[ht]
74	\centering
75	\small
76	\caption{End-to-end QLoRA vs.\ XGBoost on instruction-tuned data (within-model 5-fold CV, Qwen3-0.6B backbone). Base QLoRA rows shown for reference only; instruct sets ($N{\approx}4.4$--$5.0$K) are approximately twice the base sets ($N{\approx}2.3$K), so cross-condition comparison is confounded by training set size.}
77	\label{tab:instruct-qlora}
78	\resizebox{\linewidth}{!}{%
79	\begin{tabular}{lccccc}
80	\toprule
81	& \multicolumn{2}{c}{\textbf{3-class F1}} & & \\
82	\cmidrule(lr){2-3}
83	\textbf{Model} & XGB & QLoRA & $\boldsymbol{\Delta}$ & \textbf{$N$} \\
84	\midrule
85	OLMo-2-1B-Inst   & 0.575 & 0.888\,$\pm$\,0.007 & $+$31.3\,pp & 4{,}429 \\
86	Qwen3-1.7B-Inst  & 0.732 & 0.907\,$\pm$\,0.008 & $+$17.5\,pp & 4{,}963 \\
87	\midrule
88	OLMo-2-1B (base) &       & 0.859\,$\pm$\,0.004 &             & 2{,}379 \\
89	Qwen3-1.7B (base)&       & 0.904\,$\pm$\,0.009 &             & 2{,}291 \\
90	\bottomrule
91	\end{tabular}}
92	\end{table}
93	
94	The XGBoost-to-QLoRA gap on the same instruct data is substantial ($+$17.5 to $+$31.3\,pp). Depth signal persists at the token level under instruction tuning but is inaccessible to the seven summary statistics; the degradation reported in Table~\ref{tab:instruct} reflects a feature-level limitation rather than signal absence.
95	Note that instruct samples are approximately twice the base count used here (Table~\ref{tab:instruct-qlora}), so the instruct-vs-base QLoRA comparison is confounded by training set size; the meaningful comparison is QLoRA-vs-XGBoost on the same instruct data.
96	All results use within-model 5-fold CV, not cross-generator LOGO, limiting generalization claims.
97	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3d9b10c-33e1-4f33-a11c-c5e378bf3057",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "c6a821d4-368c-4b8e-978b-e5f288186c37",
  "sourceToolAssistantUUID": "c3d9b10c-33e1-4f33-a11c-c5e378bf3057",
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

_source line 59 · 2026-05-25T20:39:04.805Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PHXp3gjUexCWsZbM828Ets`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_seed_control.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6a821d4-368c-4b8e-978b-e5f288186c37",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPw1djxp7BCowZmerZNF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "752d1f17-e5ad-449e-9f79-5dddca84f8d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJMVXXwsvvrr4M22bQEiyu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18984,
      "cache_read_input_tokens": 48751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18984,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 60 · 2026-05-25T20:39:04.810Z_

<details><summary>↩ Tool result · `toolu_01PHXp3gjUexCWsZbM828Ets`</summary>

```text
1	\section{Independent-Seed Control}
2	\label{app:seed-control}
3	
4	\begingroup\setlength{\parskip}{2pt plus 1pt}
5	
6	To test for topic-level leakage from shared seeds across generators, we construct an independent-seed evaluation where Pythia-2.8B and OLMo-2-1B use completely disjoint Wikipedia seed pools (500 seeds each, zero overlap).
7	Each generator produces depth-0 through depth-4 chains on its own seed pool; features are extracted with the same Pythia-410M reference model.
8	We then train a 7-feature XGBoost classifier on one generator's data and test on the other, in both directions.
9	
10	\begin{table}[ht]
11	\centering
12	\small
13	\caption{Independent-seed cross-generator evaluation (binary: gen-1 vs.\ gen-2+). Disjoint seed pools eliminate any possibility of topic-based leakage. The average independent-seed F1 (0.680) is within 1.4\,pp of the shared-seed LOGO baseline (0.694). The classifier thus captures generative degradation patterns rather than seed-specific topic content.}
14	\label{tab:seed-control}
15	\resizebox{\linewidth}{!}{%
16	\renewcommand{\arraystretch}{1.15}%
17	\begin{tabular}{lcc}
18	\toprule
19	\textbf{Setting} & \textbf{Binary F1} & \textbf{95\% CI} \\
20	\midrule
21	Pythia-2.8B $\rightarrow$ OLMo-2-1B & 0.695 & [0.673, 0.717] \\
22	OLMo-2-1B $\rightarrow$ Pythia-2.8B & 0.666 & [0.643, 0.689] \\
23	\midrule
24	Independent-seed average & 0.680 & --- \\
25	Shared-seed LOGO (reference) & 0.694 & [0.688, 0.700] \\
26	\bottomrule
27	\end{tabular}}
28	\end{table}
29	
30	The small gap ($-$1.4\,pp) between independent-seed and shared-seed evaluation falls within bootstrap confidence intervals, and both directions individually exceed 0.66.
31	Combined with the seed-level demeaning control (\S\ref{sec:results-classification}), these results provide converging evidence that depth classification is driven by distributional properties of recursive generation, not topic identity.
32	
33	\paragraph{Semantic similarity analysis.}
34	Embedding cosine similarity between consecutive depth steps increases monotonically (Figure~\ref{fig:semantic-sim}): 0$\rightarrow$1 (0.622), 1$\rightarrow$2 (0.683), 2$\rightarrow$3 (0.801), 3$\rightarrow$4 (0.859).
35	Deeper generations are thus \emph{more} semantically similar to their inputs, yet the classifier still distinguishes depth classes. The depth signal resides in distributional rather than topical properties.
36	Prompt type modulates the baseline similarity level (continuation 0.717 $<$ elaboration 0.809 $\approx$ rewriting 0.808), plausibly because semantic-preservation constraints reduce topic drift while leaving the distributional location shift intact.
37	
38	\begin{figure}[t]
39	\centering
40	\includegraphics[width=0.9\columnwidth]{fig_appendix_semantic_sim.pdf}
41	\caption{Embedding cosine similarity between consecutive depth steps. Deeper generations become increasingly similar to their inputs, yet the classifier still distinguishes depth classes. Dotted lines: prompt-type baselines.}
42	\label{fig:semantic-sim}
43	\end{figure}
44	
45	\endgroup
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "752d1f17-e5ad-449e-9f79-5dddca84f8d9",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "d21325b6-cc1e-45bd-a92e-a52b5eeda609",
  "sourceToolAssistantUUID": "752d1f17-e5ad-449e-9f79-5dddca84f8d9",
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

_source line 61 · 2026-05-25T20:39:05.278Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FigBdVpiZ3MqNHswEEM6Z6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_transfer.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d21325b6-cc1e-45bd-a92e-a52b5eeda609",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPw1djxp7BCowZmerZNF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d29dcf2-0fba-4e3f-9d73-5cba402a4395",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJMVXXwsvvrr4M22bQEiyu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18984,
      "cache_read_input_tokens": 48751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18984,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 62 · 2026-05-25T20:39:05.281Z_

<details><summary>↩ Tool result · `toolu_01FigBdVpiZ3MqNHswEEM6Z6`</summary>

```text
1	To isolate the depth signal from generator identity, we train a binary classifier (gen-1 vs.\ gen-2+) on each of the eight generators independently and evaluate on all others.
2	Table~\ref{tab:transfer} reports the full 8$\times$8 transfer matrix; Figure~\ref{fig:transfer-heatmap} (main text) visualizes it as a heatmap.
3	Note that these classifiers are trained with a binary objective, whereas the LOGO classifiers in Table~\ref{tab:logo-results} are trained on a 3-class task and evaluated on the binary subtask; the two setups are therefore not directly comparable.
4	
5	\begin{table}[ht]
6	\centering
7	\scriptsize
8	\setlength{\tabcolsep}{3pt}
9	\caption{Cross-generator binary F1 transfer matrix (gen-1 vs.\ gen-2+). Each row trains on one generator; each column evaluates on another. Diagonal entries (\underline{underlined}) are within-generator. All 56 off-diagonal pairs exceed chance (0.5). Classifiers use the same 7-feature XGBoost configuration as LOGO but are trained with a binary objective.}
10	\label{tab:transfer}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{l|cccccccc}
13	\toprule
14	\textbf{Train $\backslash$ Test} & \textbf{Py-2.8B} & \textbf{Py-1B} & \textbf{Qw-0.6B} & \textbf{Qw-1.7B} & \textbf{Qw-8B} & \textbf{OLMo-1B} & \textbf{Ll-3B} & \textbf{Mi-7B} \\
15	\midrule
16	Py-2.8B  & \underline{0.985} & 0.873 & 0.823 & 0.833 & 0.741 & 0.829 & 0.815 & 0.712 \\
17	Py-1B    & 0.834 & \underline{0.987} & 0.828 & 0.821 & 0.704 & 0.778 & 0.764 & 0.620 \\
18	Qw-0.6B  & 0.786 & 0.846 & \underline{0.991} & 0.851 & 0.786 & 0.795 & 0.760 & 0.680 \\
19	Qw-1.7B  & 0.794 & 0.839 & 0.859 & \underline{0.989} & 0.790 & 0.817 & 0.798 & 0.717 \\
20	Qw-8B   & 0.811 & 0.836 & 0.853 & 0.855 & \underline{0.984} & 0.848 & 0.839 & 0.790 \\
21	OLMo-1B  & 0.811 & 0.827 & 0.837 & 0.852 & 0.803 & \underline{0.988} & 0.828 & 0.763 \\
22	Ll-3B    & 0.856 & 0.860 & 0.845 & 0.851 & 0.798 & 0.851 & \underline{0.987} & 0.787 \\
23	Mi-7B    & 0.834 & 0.837 & 0.837 & 0.845 & 0.817 & 0.849 & 0.851 & \underline{0.969} \\
24	\bottomrule
25	\end{tabular}}
26	\end{table}
27	
28	All 56 off-diagonal transfer pairs yield F1 above chance, with a mean of 0.810 (95\% bootstrap CI [0.796, 0.822]; one-sample $t=46.58$, $p < 10^{-10}$).
29	Transfer is strongest within families (e.g., Py-2.8B$\to$Py-1B: 0.87) and weakest for Py-1B$\to$Mi-7B (0.62), consistent with the scale and reference-affinity effects discussed in \S\ref{sec:results-differential}.
30	These results confirm that depth signatures generalize across architectures, parameter scales, and model families. Generator identity is not a primary confound.
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d29dcf2-0fba-4e3f-9d73-5cba402a4395",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "b8b882df-3ca3-4117-9835-5e5e35da97c1",
  "sourceToolAssistantUUID": "3d29dcf2-0fba-4e3f-9d73-5cba402a4395",
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

_source line 63 · 2026-05-25T20:39:06.223Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BDDmiV36rT9oMtcRcAyFNo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_tost.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8b882df-3ca3-4117-9835-5e5e35da97c1",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPw1djxp7BCowZmerZNF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "43cb538d-75d6-4d76-bf33-de14d0a70885",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJMVXXwsvvrr4M22bQEiyu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18984,
      "cache_read_input_tokens": 48751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18984,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 64 · 2026-05-25T20:39:06.227Z_

<details><summary>↩ Tool result · `toolu_01BDDmiV36rT9oMtcRcAyFNo`</summary>

```text
1	\section{Per-Generator Equivalence Testing}
2	\label{app:tost}
3	
4	\begingroup\setlength{\parskip}{2pt plus 1pt}
5	
6	To confirm that the near-stationary classification is not a pooling artifact, we apply two one-sided $t$-tests (TOST) \cite{lakens_equivalence} for each feature within each generator separately (gen-1 vs.\ gen-2+, equivalence bound $|d| < 0.20$).
7	We adopt Cohen's conventional small effect size ($d{=}0.20$) \cite{cohen1988statistical} as the smallest effect of practical significance (SESOI): effects below this threshold are unlikely to be practically meaningful for depth discrimination.
8	LOFO analysis independently supports this choice: removing any near-stationary feature changes classification F1 by $\leq$1.5\,pp (Appendix~\ref{app:lofo}), linking the statistical threshold to classification irrelevance.
9	Sensitivity analysis at $\varepsilon \in \{0.15, 0.20, 0.25\}$ confirms the partition is robust to the bound choice (Appendix~\ref{app:tost-sensitivity}); bootstrap resampling ($B{=}1{,}000$) shows 100\% rejection stability for all near-stationary features (Appendix~\ref{app:tost-bootstrap}); and the partition is invariant across $\varepsilon \in [0.10, 0.75]$ (Appendix~\ref{app:epsilon-sweep}).
10	Table~\ref{tab:tost-per-gen} reports observed $|d|$; \checkmark{} marks features for which the TOST null hypothesis (non-equivalence) is rejected at $\alpha = 0.05$.
11	
12	\begin{figure}[t]
13	\centering
14	\includegraphics[width=\columnwidth]{fig_appendix_tost_heatmap.pdf}
15	\caption{TOST equivalence heatmap. Cohen's $d$ (gen-1 vs.\ gen-2+) per generator and feature. Asterisks (*) mark TOST equivalence at $\varepsilon{=}0.20$. Drifting features (red, left) show uniformly large $d$; near-stationary features (blue, right) cluster near zero.}
16	\label{fig:tost-heatmap}
17	\end{figure}
18	
19	Entropy min passes equivalence for all eight generators; entropy max passes for six of eight (exceeding $\varepsilon$ only for Pythia-1B and Pythia-2.8B, where $|d| \approx 0.21$--$0.25$); tail decay passes for four of eight.
20	All drifting and intermediate features fail equivalence uniformly, with $|d|$ ranging from 0.23 (entropy std, Mistral) to 1.40 (entropy mean, Pythia-1B).
21	The partition is robust at the individual-generator level, with entropy min as the most consistently stationary feature.
22	Figure~\ref{fig:ddr-scatter} visualizes the DDR partition in ($|\rho|$, $d$) space; the three groups are separated by clear gaps.
23	
24	\endgroup
25	
26	\begin{table}[ht]
27	\centering
28	\footnotesize
29	\caption{Per-generator TOST equivalence ($\varepsilon{=}|d|{<}0.20$, gen-1 vs.\ gen-2+). Observed $|d|$; \checkmark{} = equivalent ($p_{\mathrm{TOST}} < 0.05$). Features grouped by DDR partition.}
30	\label{tab:tost-per-gen}
31	\resizebox{\columnwidth}{!}{%
32	\renewcommand{\arraystretch}{1.20}%
33	\begin{tabular}{l ccc c ccc}
34	\toprule
35	& \multicolumn{3}{c}{\textbf{Drifting}} & \textbf{Int.} & \multicolumn{3}{c}{\textbf{Near-stationary}} \\
36	\cmidrule(lr){2-4} \cmidrule(lr){5-5} \cmidrule(lr){6-8}
37	\textbf{Generator} & $\bar{H}$ & TTR & hapax & $\sigma_H$ & $H_{\max}$ & tail & $H_{\min}$ \\
38	\midrule
39	Pythia-2.8B  & 1.20 & 0.77 & 0.67 & 0.39 & 0.25          & 0.07\,\checkmark & 0.03\,\checkmark \\
40	Pythia-1B    & 1.40 & 0.80 & 0.65 & 0.53 & 0.21          & 0.08\,\checkmark & 0.02\,\checkmark \\
41	Qwen3-1.7B  & 1.12 & 0.93 & 0.83 & 0.52 & 0.02\,\checkmark & 0.09\,\checkmark & 0.05\,\checkmark \\
42	Llama-3.2-3B & 1.15 & 1.04 & 0.98 & 0.50 & 0.01\,\checkmark & 0.19          & 0.01\,\checkmark \\
43	OLMo-2-1B   & 1.19 & 1.08 & 1.00 & 0.61 & 0.06\,\checkmark & 0.22          & 0.07\,\checkmark \\
44	Qwen3-8B    & 0.86 & 0.71 & 0.66 & 0.37 & 0.04\,\checkmark & 0.15          & 0.01\,\checkmark \\
45	Qwen3-0.6B  & 0.92 & 0.63 & 0.50 & 0.56 & 0.01\,\checkmark & 0.08\,\checkmark & 0.10\,\checkmark \\
46	Mistral-7B   & 0.89 & 0.82 & 0.82 & 0.23 & 0.00\,\checkmark & 0.16          & 0.04\,\checkmark \\
47	\midrule
48	\textbf{Equiv.\ count} & 0/8 & 0/8 & 0/8 & 0/8 & 6/8 & 4/8 & 8/8 \\
49	\bottomrule
50	\end{tabular}}
51	\end{table}
52	
53	
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43cb538d-75d6-4d76-bf33-de14d0a70885",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "422f9d21-3888-47f3-a102-383acfb0686b",
  "sourceToolAssistantUUID": "43cb538d-75d6-4d76-bf33-de14d0a70885",
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

_source line 65 · 2026-05-25T20:39:06.628Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VHGwnd68BYBDthcmscVJfJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_tost_bootstrap.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "422f9d21-3888-47f3-a102-383acfb0686b",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPw1djxp7BCowZmerZNF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "272bca72-e26f-4126-b11e-2a071dccde30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJMVXXwsvvrr4M22bQEiyu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18984,
      "cache_read_input_tokens": 48751,
      "output_tokens": 797,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18984
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 797,
          "cache_read_input_tokens": 48751,
          "cache_creation_input_tokens": 18984,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18984,
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

_source line 66 · 2026-05-25T20:39:06.635Z_

<details><summary>↩ Tool result · `toolu_01VHGwnd68BYBDthcmscVJfJ`</summary>

```text
1	\subsection{TOST Bootstrap Stability}\label{app:tost-bootstrap}
2	
3	To verify that the equivalence conclusions in \S\ref{app:tost} are not sensitive to sample composition, we assess their stability under bootstrap resampling.
4	For each of four representative features, we run 1{,}000 bootstrap iterations (base seed\,=\,42): each iteration independently resamples with replacement from the gen-1 and gen-2+ pools, recomputes Cohen's $d$ and the TOST $p$-value (equivalence margin $|d| < 0.20$).
5	
6	\begin{table}[ht]
7	\centering
8	\footnotesize
9	\caption{Bootstrap stability of TOST equivalence ($B{=}1{,}000$, margin $|d|{<}0.20$). Rejection rate = fraction of bootstrap iterations where TOST rejects non-equivalence at $\alpha{=}0.05$.}
10	\label{tab:tost-bootstrap}
11	\resizebox{\linewidth}{!}{%
12	\begin{tabular}{l c c c}
13	\toprule
14	\textbf{Feature} & \textbf{Rejection rate} & \textbf{Median $d$} & \textbf{$d$ 95\% CI} \\
15	\midrule
16	entropy\_max  & 100\% (1000/1000) & 0.062  & [0.037, 0.088] \\
17	entropy\_min  & 100\% (1000/1000) & $-$0.016 & [$-$0.042, 0.011] \\
18	tail\_decay   & 100\% (1000/1000) & 0.088  & [0.065, 0.111] \\
19	\midrule
20	entropy\_std  & 0\% (0/1000)      & 0.458  & [0.435, 0.479] \\
21	\bottomrule
22	\end{tabular}}
23	\end{table}
24	
25	All three near-stationary features achieve a 100\% rejection rate across 1{,}000 bootstrap iterations, and their effect-size 95\% CIs fall entirely within the $\pm 0.20$ equivalence margin.
26	Entropy std, included as an intermediate control, is never rejected (0\%), with its CI $[0.435, 0.479]$ lying entirely outside the margin.
27	No feature exhibits boundary-crossing: the classification of each feature is unanimous across all bootstrap samples. The equivalence conclusions are robust to resampling variability.
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "272bca72-e26f-4126-b11e-2a071dccde30",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "00f88a84-b810-481a-b37a-7bb876183d27",
  "sourceToolAssistantUUID": "272bca72-e26f-4126-b11e-2a071dccde30",
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

_source line 67 · 2026-05-25T20:39:11.299Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CjCbhJsD6yzGb7RfWM2LFr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_domain.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00f88a84-b810-481a-b37a-7bb876183d27",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPw2RghNbwqRy5jFkM6q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9bcb1a0e-a68c-4625-abce-d173cf168a7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyRp9FQpTwvkUXDS9LDkrZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14901,
      "cache_read_input_tokens": 67735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14901,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 68 · 2026-05-25T20:39:11.305Z_

<details><summary>↩ Tool result · `toolu_01CjCbhJsD6yzGb7RfWM2LFr`</summary>

```text
1	This pilot study evaluates whether depth signal generalizes beyond Wikipedia by constructing generation chains from three additional domains: News articles, Academic abstracts, and Code documentation.
2	For each domain, we sample 200 seed texts and generate chains of depth 3 using three generators (Pythia-1B, Qwen3-1.7B, Mistral-7B).
3	The same 7-feature ensemble and LOGO protocol are applied.
4	
5	\noindent\textbf{Important caveat:} Cross-domain generation used $t{=}1.0$, top-$p{=}1.0$, which falls outside the method's reliable operating range ($t \leq 0.7$; Appendix~\ref{app:sampling-sensitivity}). Domain and temperature effects are therefore confounded in the results below; the cross-domain signal may partly reflect temperature-induced distributional divergence rather than domain generalization alone.
6	
7	\begin{table}[ht]
8	\centering
9	\small
10	\caption{Cross-domain depth classification under LOGO evaluation (binary: gen-1 vs.\ gen-2+). Three generators $\times$ 200 seeds per domain. Bootstrap 95\% CIs ($n$\,=\,1000).}
11	\label{tab:domain}
12	\begin{tabular}{lccc}
13	\toprule
14	\textbf{Domain} & \textbf{Binary F1} & \textbf{95\% CI} & \textbf{3-class F1} \\
15	\midrule
16	Code           & 0.754 & [0.737, 0.770] & 0.634 \\
17	News           & 0.746 & [0.726, 0.764] & 0.652 \\
18	Academic       & 0.739 & [0.720, 0.757] & 0.622 \\
19	\bottomrule
20	\end{tabular}
21	\end{table}
22	
23	All three non-Wikipedia domains achieve binary F1 $>$ 0.73 under leave-one-generator-out evaluation. Depth signal is not an artifact of Wikipedia text properties.
24	The Code-domain 3-class F1 (0.634) likely reflects domain mismatch in the Wikipedia-trained reference model (Pythia-410M), whose NLL estimates may be less discriminative for code syntax; these cross-domain results are preliminary.
25	
26	\paragraph{Domain $\times$ temperature interaction.}
27	Cross-domain generation used $t{=}1.0$, top-$p{=}1.0$ (vs.\ the main experiment's $t{=}0.7$, top-$p{=}0.9$).
28	Supplementary evaluation at $t{=}0.7$ reveals a domain $\times$ temperature interaction: the main Wikipedia experiment favors lower temperature (depth signal degrades monotonically with rising temperature; Appendix~\ref{app:sampling-sensitivity}), while cross-domain evaluation favors higher temperature ($t{=}1.0$ yields +3 to +11\,pp over $t{=}0.7$; News 0.746 vs.\ 0.712, Academic 0.739 vs.\ 0.628, Code 0.754 vs.\ 0.687).
29	This asymmetry likely reflects reference-model calibration: Pythia-410M, trained predominantly on web text, detects subtle per-step drift in Wikipedia but requires larger distributional divergence (produced by higher temperature) to detect depth signal in out-of-distribution domains.
30	This finding suggests that reference model selection is a key factor for cross-domain deployment of depth profiling.
31	
32	\paragraph{3-class inversion as DDR evidence.}
33	In the cross-domain setting, 3-class F1 (0.62--0.65) falls below binary F1 (0.74--0.75), reversing the pattern observed in the main experiment (3-class 0.762 $>$ binary 0.694).
34	This inversion reflects degraded gen-0 vs.\ gen-1 separation: the Pythia-410M reference model is calibrated to Wikipedia text, so its baseline entropy estimates are less discriminative for out-of-domain human text and compresses the feature distance between gen-0 and gen-1.
35	The binary task (gen-1 vs.\ gen-2+) is unaffected because both classes are generated under identical domain and decoding conditions; recursive drift is a relative change that does not depend on absolute calibration.
36	This pattern provides additional evidence that DDR captures base-model generation dynamics rather than domain-specific text properties: depth signal remains robust even when the human-vs-machine boundary becomes less distinct.
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bcb1a0e-a68c-4625-abce-d173cf168a7b",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "20315a41-e425-4dcf-a950-4ab2eb63cc15",
  "sourceToolAssistantUUID": "9bcb1a0e-a68c-4625-abce-d173cf168a7b",
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

_source line 69 · 2026-05-25T20:39:12.115Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RQwSupcTneU7HVRqh4KceR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_finer_depth.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20315a41-e425-4dcf-a950-4ab2eb63cc15",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPw2RghNbwqRy5jFkM6q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "392f7746-5c99-4823-979b-591160f75d01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyRp9FQpTwvkUXDS9LDkrZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14901,
      "cache_read_input_tokens": 67735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14901,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 70 · 2026-05-25T20:39:12.119Z_

<details><summary>↩ Tool result · `toolu_01RQwSupcTneU7HVRqh4KceR`</summary>

```text
1	We evaluate finer-grained 5-class depth classification (gen-0 through gen-4) using the same 7-feature ensemble and LOGO protocol described in \S\ref{sec:method}.
2	
3	\begin{table}[ht]
4	\centering
5	\small
6	\caption{5-class LOGO evaluation. Each row holds out one generator for testing, training on the remaining five.}
7	\label{tab:5class-logo}
8	\resizebox{\linewidth}{!}{%
9	\begin{tabular}{lcccc}
10	\toprule
11	\textbf{Held-out Generator} & \textbf{Macro F1} & \textbf{Weighted F1} & \textbf{Accuracy} \\
12	\midrule
13	OLMo-2-1B       & 0.484 & 0.506 & 0.524 \\
14	Pythia-1B        & 0.543 & 0.568 & 0.575 \\
15	Pythia-2.8B      & 0.523 & 0.540 & 0.560 \\
16	Qwen3-0.6B      & 0.513 & 0.521 & 0.546 \\
17	Qwen3-1.7B      & 0.510 & 0.536 & 0.548 \\
18	Qwen3-8B        & 0.434 & 0.455 & 0.493 \\
19	\midrule
20	\textbf{Average} & \textbf{0.501 $\pm$ 0.038} & \textbf{0.521} & \textbf{0.541} \\
21	\bottomrule
22	\end{tabular}}
23	\end{table}
24	
25	\begin{table}[ht]
26	\centering
27	\small
28	\caption{Per-class F1 averaged across all six LOGO folds.}
29	\label{tab:5class-perclass}
30	\resizebox{\linewidth}{!}{%
31	\begin{tabular}{lccccc}
32	\toprule
33	\textbf{Metric} & \textbf{Gen-0} & \textbf{Gen-1} & \textbf{Gen-2} & \textbf{Gen-3} & \textbf{Gen-4} \\
34	\midrule
35	Avg F1      & 0.921 & 0.634 & 0.268 & 0.259 & 0.423 \\
36	\bottomrule
37	\end{tabular}}
38	\end{table}
39	
40	\paragraph{Analysis.}
41	Moving from 3-class (gen-0 / gen-1 / gen-2+) to 5-class classification reduces LOGO macro F1 to approximately 0.50 (six-generator subset; the 3-class baseline for this subset is comparable to the 8-generator result of 0.762 in Table~\ref{tab:logo-results}).
42	The degradation is concentrated in the middle depths: gen-2 and gen-3 achieve only 0.268 and 0.259 F1, respectively.
43	The aggregated confusion matrix reveals that 36.5\% of true gen-2 samples are misclassified as gen-1, while 37.8\% of true gen-3 samples are predicted as gen-4.
44	Adjacent depths (gen-2$\leftrightarrow$gen-3, gen-3$\leftrightarrow$gen-4) account for the majority of errors, consistent with the intuition that deeper recursive generations converge in surface-level statistical signatures.
45	Gen-0 (human text) remains highly distinguishable (F1 = 0.921), and gen-1 retains moderate separability (F1 = 0.634).
46	Shape features that are near-stationary in the 3-class setting become substantially more important under 5-class evaluation: permutation importance of entropy\_std increases by 93\% and tail\_decay by 400\% relative to 3-class, yet these gains are insufficient to resolve adjacent depths.
47	These results support the 3-class grouping adopted in the main paper: collapsing gen-2+ preserves the most informative boundary (human vs.\ first-generation vs.\ deeper recursion) while avoiding the noise introduced by near-identical adjacent depths.
48	
49	\paragraph{Classifier comparison.}
50	To verify that 5-class degradation reflects feature-level limitations rather than classifier choice, we evaluate four alternatives under the same protocol: HistGradientBoosting (macro F1\,=\,0.501, 95\% bootstrap CI [0.496, 0.506]), random forest (0.476), logistic regression (0.447), and Frank-Hall ordinal reduction (0.451).
51	All classifiers perform comparably to the default XGBoost ensemble (0.501); classifier capacity is not the bottleneck.
52	The gen-2/gen-3 boundary is the primary failure mode across all methods: these two classes are effectively inseparable with the current feature set. This establishes 3-class granularity as the practical ceiling for surface and entropy features.
53	At the 3-class level, ordinal-specific methods (CORAL ordinal regression, Frank-Hall reduction) similarly fail to improve over multiclass XGBoost (\S\ref{sec:results}), which confirms that the bottleneck is feature separability across all granularities, not the modeling of label ordinality.
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "392f7746-5c99-4823-979b-591160f75d01",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "ae9f2346-0446-4858-ae16-586a818365c6",
  "sourceToolAssistantUUID": "392f7746-5c99-4823-979b-591160f75d01",
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

_source line 71 · 2026-05-25T20:39:13.228Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XeQGZiJb4mGmLFVfxmrFSb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_decoding_strategy.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae9f2346-0446-4858-ae16-586a818365c6",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPw2RghNbwqRy5jFkM6q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32ea03d5-4fa0-42ca-a559-2e82253a8587",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyRp9FQpTwvkUXDS9LDkrZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14901,
      "cache_read_input_tokens": 67735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14901,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 72 · 2026-05-25T20:39:13.232Z_

<details><summary>↩ Tool result · `toolu_01XeQGZiJb4mGmLFVfxmrFSb`</summary>

```text
1	% Decoding Strategy Robustness
2	To verify that DDR shape stability is not an artifact of nucleus sampling ($p{=}0.9$, $\tau{=}0.7$),
3	we repeat the generation chain experiment under two alternative decoding strategies:
4	greedy decoding ($\tau{=}0$) and top-$k$ sampling ($k{=}50$, $\tau{=}0.7$).
5	All eight generators spanning five architectural families produce ${\sim}$1{,}000 chains of depth 0--4 per strategy,
6	yielding ${\sim}$5{,}000 texts per generator--strategy combination.
7	
8	Table~\ref{tab:decoding-shape} reports Cohen's $d$ (gen-1 vs.\ gen-2+) for the three shape features across strategies;
9	Table~\ref{tab:decoding-drift} provides the corresponding values for drifting and intermediate features.
10	
11	\begin{table}[ht]
12	\centering
13	\small
14	\caption{Shape-feature Cohen's $d$ (gen-1 vs.\ gen-2+) under three decoding strategies per generator.
15	Values below 0.20 indicate negligible drift.
16	Shape features are expected to remain near-stationary across strategies if DDR is decoding-agnostic.}
17	\label{tab:decoding-shape}
18	\resizebox{\linewidth}{!}{%
19	\begin{tabular}{ll ccc ccc ccc}
20	\toprule
21	& & \multicolumn{3}{c}{entropy\_max} & \multicolumn{3}{c}{entropy\_min} & \multicolumn{3}{c}{tail\_decay} \\
22	\cmidrule(lr){3-5} \cmidrule(lr){6-8} \cmidrule(lr){9-11}
23	Family & Generator & Nuc. & Gr. & Top-$k$ & Nuc. & Gr. & Top-$k$ & Nuc. & Gr. & Top-$k$ \\
24	\midrule
25	Pythia  & 2.8B    & 0.25 & 0.09 & 0.26 & 0.03 & 0.08 & 0.04 & 0.07 & 0.07 & 0.12 \\
26	        & 1B      & 0.21 & 0.12 & 0.27 & 0.02 & 0.04 & 0.04 & 0.08 & 0.04 & 0.18 \\
27	OLMo    & 2-1B    & 0.06 & 0.03 & 0.01 & 0.07 & 0.03 & 0.01 & 0.22 & 0.03 & 0.22 \\
28	Qwen3   & 0.6B    & 0.01 & 0.09 & 0.02 & 0.10 & 0.02 & 0.10 & 0.08 & 0.03 & 0.13 \\
29	        & 1.7B    & 0.02 & 0.08 & 0.03 & 0.05 & 0.01 & 0.03 & 0.09 & 0.04 & 0.14 \\
30	        & 8B      & 0.04 & 0.01 & 0.05 & 0.01 & 0.06 & 0.07 & 0.15 & 0.08 & 0.17 \\
31	Llama   & 3.2-3B  & 0.01 & 0.06 & 0.08 & 0.01 & 0.07 & 0.03 & 0.19 & 0.04 & 0.20 \\
32	Mistral & 7B-v0.3 & 0.00 & 0.01 & 0.06 & 0.04 & 0.02 & 0.01 & 0.16 & 0.14 & 0.12 \\
33	\midrule
34	\multicolumn{2}{l}{\textbf{Mean}} & \textbf{0.08}$^{8/8}$ & \textbf{0.06}$^{8/8}$ & \textbf{0.10}$^{8/8}$ & \textbf{0.04}$^{8/8}$ & \textbf{0.04}$^{8/8}$ & \textbf{0.04}$^{8/8}$ & \textbf{0.13}$^{8/8}$ & \textbf{0.06}$^{8/8}$ & \textbf{0.16}$^{8/8}$ \\
35	\bottomrule
36	\end{tabular}}
37	\end{table}
38	
39	\begin{table}[ht]
40	\centering
41	\small
42	\caption{Drifting- and intermediate-feature Cohen's $d$ (gen-1 vs.\ gen-2+) under three decoding strategies per generator.
43	Drifting features are expected to maintain large $d$ regardless of strategy.}
44	\label{tab:decoding-drift}
45	\resizebox{\linewidth}{!}{%
46	\begin{tabular}{ll ccc ccc ccc ccc}
47	\toprule
48	& & \multicolumn{3}{c}{entropy\_mean} & \multicolumn{3}{c}{TTR} & \multicolumn{3}{c}{hapax\_ratio} & \multicolumn{3}{c}{entropy\_std} \\
49	\cmidrule(lr){3-5} \cmidrule(lr){6-8} \cmidrule(lr){9-11} \cmidrule(lr){12-14}
50	Family & Generator & Nuc. & Gr. & Top-$k$ & Nuc. & Gr. & Top-$k$ & Nuc. & Gr. & Top-$k$ & Nuc. & Gr. & Top-$k$ \\
51	\midrule
52	Pythia  & 2.8B    & 1.20 & 1.43 & 0.70 & 0.77 & 0.98 & 0.41 & 0.67 & 0.87 & 0.37 & 0.39 & 0.93 & 0.10 \\
53	        & 1B      & 1.40 & 0.98 & 0.83 & 0.80 & 0.64 & 0.41 & 0.65 & 0.53 & 0.34 & 0.53 & 0.91 & 0.13 \\
54	OLMo    & 2-1B    & 1.19 & 1.29 & 0.73 & 1.08 & 0.89 & 0.70 & 1.00 & 0.80 & 0.69 & 0.61 & 0.95 & 0.35 \\
55	Qwen3   & 0.6B    & 0.92 & 0.82 & 0.80 & 0.63 & 0.51 & 0.58 & 0.50 & 0.46 & 0.52 & 0.56 & 0.72 & 0.30 \\
56	        & 1.7B    & 1.12 & 1.03 & 0.99 & 0.93 & 0.74 & 0.85 & 0.83 & 0.68 & 0.80 & 0.52 & 0.78 & 0.32 \\
57	        & 8B      & 0.86 & 0.98 & 0.76 & 0.71 & 0.76 & 0.68 & 0.66 & 0.76 & 0.64 & 0.37 & 0.71 & 0.27 \\
58	Llama   & 3.2-3B  & 1.15 & 1.46 & 0.77 & 1.04 & 1.27 & 0.73 & 0.98 & 1.26 & 0.71 & 0.50 & 1.01 & 0.21 \\
59	Mistral & 7B-v0.3 & 0.89 & 1.31 & 0.70 & 0.82 & 1.04 & 0.64 & 0.82 & 1.03 & 0.67 & 0.23 & 0.62 & 0.15 \\
60	\midrule
61	\multicolumn{2}{l}{\textbf{Mean}} & \textbf{1.09}$^{8/8}$ & \textbf{1.16}$^{8/8}$ & \textbf{0.79}$^{8/8}$ & \textbf{0.85}$^{8/8}$ & \textbf{0.85}$^{8/8}$ & \textbf{0.63}$^{8/8}$ & \textbf{0.76}$^{8/8}$ & \textbf{0.80}$^{8/8}$ & \textbf{0.59}$^{8/8}$ & \textbf{0.46}$^{8/8}$ & \textbf{0.83}$^{8/8}$ & \textbf{0.23}$^{8/8}$ \\
62	\bottomrule
63	\end{tabular}}
64	\end{table}
65	
66	
67	\begin{figure*}[t]
68	\centering
69	\includegraphics[width=\textwidth]{fig_appendix_decoding.pdf}
70	\caption{Decoding strategy robustness. \textbf{(a)} Mean Cohen's $d$ (gen-1 vs.\ gen-2+) across three decoding strategies. Drifting features maintain large $d$ across all strategies; shape features remain below the stationarity threshold ($d < 0.15$). Reference lines mark drifting ($d{=}0.50$) and stationary ($d{=}0.15$) thresholds. \textbf{(b)} Per-generator mean shape-feature $|d|$: all generators stay near-stationary under all three strategies.}
71	\label{fig:decoding-robustness}
72	\end{figure*}
73	
74	Under greedy decoding ($\tau{=}0$), shape features remain near-stationary across all eight generators
75	(mean $|d|{=}$\textbf{0.05}, max \textbf{0.14}), while core drifting features maintain large effects
76	(mean $d{=}$\textbf{0.94}). This confirms that DDR is an empirical regularity of autoregressive generation
77	independent of sampling truncation.
78	Top-$k$ sampling ($k{=}50$) partially attenuates the partition.
79	Shape features show boundary violations in 4/8 generators under top-$k$; however, these generators exhibit comparable or higher violations under nucleus sampling (Pythia entropy\_max: 0.21--0.25 nucleus vs.\ 0.26--0.27 top-$k$; OLMo tail\_decay: 0.22 under both). These are model-intrinsic boundary effects rather than strategy-induced degradation.
80	Core drifting effect sizes weaken (mean $d{=}$\textbf{0.67} vs.\ \textbf{0.90} under nucleus).
81	This modulation is consistent with the mechanistic account in \S\ref{sec:discussion}:
82	top-$k$ truncation introduces a fixed-width selection window that interacts differently
83	with depth-compressed distributions than nucleus sampling's probability-mass truncation,
84	partially blurring the location/shape boundary.
85	The core DDR partition (drifting features carrying depth signal while shape features
86	provide cross-generator reference) remains intact under both greedy and nucleus sampling
87	and is attenuated but recognizable under top-$k$.
88	Entropy\_std exhibits strong strategy dependence (greedy mean $d{=}$0.83; nucleus 0.46; top-$k$ 0.23). Its depth sensitivity is modulated by the token-selection mechanism: deterministic greedy selection amplifies entropy variance across depths, while top-$k$'s fixed window compresses it. This further supports its classification as an intermediate rather than core feature.
89	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32ea03d5-4fa0-42ca-a559-2e82253a8587",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "8c21f75f-3a72-4df3-9ce7-e3699a3bf307",
  "sourceToolAssistantUUID": "32ea03d5-4fa0-42ca-a559-2e82253a8587",
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

_source line 73 · 2026-05-25T20:39:13.703Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DaYtHjx1abbVMR3M9WsTRR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_distributions.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c21f75f-3a72-4df3-9ce7-e3699a3bf307",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPw2RghNbwqRy5jFkM6q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6526e93f-ae12-496d-9777-f68736b75dfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyRp9FQpTwvkUXDS9LDkrZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14901,
      "cache_read_input_tokens": 67735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14901,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 74 · 2026-05-25T20:39:13.714Z_

<details><summary>↩ Tool result · `toolu_01DaYtHjx1abbVMR3M9WsTRR`</summary>

```text
1	\subsection*{DDR Trend Lines}
2	
3	Figure~\ref{fig:ddr-trends} extends the main-text DDR trajectory plot (Figure~\ref{fig:ddr-trajectory}) by showing per-feature depth trends with individual generator traces overlaid.
4	$R^2$ values are computed from ordinary least-squares regression on depth-level means (five points per generator, one per depth 0--4), not per-sample regression; the annotated Spearman $\rho$ provides the complementary per-sample monotonicity measure.
5	
6	\begin{figure}[H]
7	\centering
8	\includegraphics[width=\columnwidth]{fig_appendix_ddr_trends.pdf}
9	\caption{Per-feature depth trends. Bold line: pooled mean ($\pm$1.96\,SE shading) across all generators, colored by DDR zone (blue: drifting, wine: intermediate, amber: near-stationary). Thin traces: individual generators. Spearman $\rho$ and linear $R^2$ are annotated per panel.}
10	\label{fig:ddr-trends}
11	\end{figure}
12	
13	\subsection*{UMAP Embedding}
14	
15	Figure~\ref{fig:umap} shows a 2D UMAP projection of the 7-feature space (7{,}500 stratified samples, StandardScaler normalization, $k$\,=\,30 neighbors, min\_dist\,=\,0.3).
16	Panel~(a) reveals a depth gradient from gen-0 through gen-4, with progressive overlap at deeper generations consistent with the convergence that motivates the gen-2+ class collapse.
17	Panel~(b) shows the 3-class view: gen-0 forms a separable cluster, while gen-1 and gen-2+ overlap substantially, explaining the classification difficulty at this boundary.
18	
19	\begin{figure}[H]
20	\centering
21	\includegraphics[width=\columnwidth, trim=0 0 356pt 0, clip]{fig_appendix_umap.pdf}\\[-2pt]
22	{\small (a) Colored by raw generation depth (0--4)}\\[6pt]
23	\includegraphics[width=\columnwidth, trim=356pt 0 0 0, clip]{fig_appendix_umap.pdf}\\[-2pt]
24	{\small (b) Colored by 3-class label}
25	\caption{UMAP 2D projection of the 7-feature space ($N$\,=\,7{,}500 stratified sample). (a) A gradient structure emerges, with deeper depths converging. (b) Gen-0 separates clearly; gen-1 and gen-2+ overlap, consistent with the high false-negative rate at the gen-1/gen-2+ boundary.}
26	\label{fig:umap}
27	\end{figure}
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6526e93f-ae12-496d-9777-f68736b75dfa",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "9a1ad8c0-205f-4a46-acf2-96c3db35ffdf",
  "sourceToolAssistantUUID": "6526e93f-ae12-496d-9777-f68736b75dfa",
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

_source line 75 · 2026-05-25T20:39:14.282Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YH5sEki1xCwrmdhvFvCBdY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ai_assistants.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a1ad8c0-205f-4a46-acf2-96c3db35ffdf",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPw2RghNbwqRy5jFkM6q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c9062f0-fde1-439d-8cda-14a4f1489202",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyRp9FQpTwvkUXDS9LDkrZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14901,
      "cache_read_input_tokens": 67735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14901,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 76 · 2026-05-25T20:39:14.286Z_

<details><summary>↩ Tool result · `toolu_01YH5sEki1xCwrmdhvFvCBdY`</summary>

```text
1	This paper was produced with the assistance of AI writing tools for drafting and editing.
2	All scientific claims, experimental designs, and analyses were conducted by the authors.
3	The authors take full responsibility for the content of this work.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c9062f0-fde1-439d-8cda-14a4f1489202",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "512aa92a-f081-4d7c-8ebd-736007307e0b",
  "sourceToolAssistantUUID": "2c9062f0-fde1-439d-8cda-14a4f1489202",
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

_source line 77 · 2026-05-25T20:39:14.928Z_

<details open><summary>🔧 Tool call — Read · `toolu_012ULUqaYjLyLyMvQ5i8Kxwx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "512aa92a-f081-4d7c-8ebd-736007307e0b",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPw2RghNbwqRy5jFkM6q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ab0208c-d0db-4359-a20a-cc1f6c3405d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyRp9FQpTwvkUXDS9LDkrZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14901,
      "cache_read_input_tokens": 67735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14901,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 78 · 2026-05-25T20:39:14.933Z_

<details><summary>↩ Tool result · `toolu_012ULUqaYjLyLyMvQ5i8Kxwx`</summary>

```text
1	\section*{Ethics Statement}
2	\label{sec:ethics}
3	
4	All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.
5	Our method estimates the generation depth of a text passage (how many recursive generation steps it has undergone), not the identity of its author.
6	Individual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal.
7	We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).
8	We encourage deployment in data governance pipelines where provenance transparency, rather than content removal, is the objective.
9	All code, data, and trained models will be released upon publication.
10	
11	\paragraph{Licenses.}
12	All generator models are publicly available under permissive licenses (Apache 2.0 for Pythia, OLMo, and Mistral; Qwen License for Qwen3; Llama Community License for Llama 3.2).
13	Wikipedia seed passages are distributed under CC BY-SA 3.0.
14	
15	\paragraph{Compute budget.}
16	All experiments were conducted on 4$\times$ NVIDIA RTX 5090 GPUs (32\,GB each), totaling approximately 62 GPU-hours.
17	
18	\paragraph{Software.}
19	Experiments used Python 3.12.3, PyTorch 2.10.0 (CUDA 12.8), Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0, NumPy 2.2.6, pandas 3.0.2, and SciPy 1.17.1.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ab0208c-d0db-4359-a20a-cc1f6c3405d7",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "8674bfd1-a2ba-4011-94d1-b1843e5ab958",
  "sourceToolAssistantUUID": "4ab0208c-d0db-4359-a20a-cc1f6c3405d7",
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

_source line 79 · 2026-05-25T20:39:15.227Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GdpQvJTXfCMSAGuD4Dvf7x`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8674bfd1-a2ba-4011-94d1-b1843e5ab958",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPw2RghNbwqRy5jFkM6q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e98c40a-8dc0-426d-bae6-3b735d8cace2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyRp9FQpTwvkUXDS9LDkrZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14901,
      "cache_read_input_tokens": 67735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14901,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 80 · 2026-05-25T20:39:15.231Z_

<details><summary>↩ Tool result · `toolu_01GdpQvJTXfCMSAGuD4Dvf7x`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{AI-generated text detection.}
5	\looseness=-1 Detection methods span zero-shot scoring \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt}, learned classifiers \cite{ghostbuster,ld_score,reliable_detection}, and surprisal-based approaches \cite{diveye,xu_spectrum_detection}; see \citet{wu_survey_2025} for a survey.
6	Recent work moves beyond binary detection---multi-generator attribution \cite{semeval2024_task8}, collaboration roles \cite{beyond_binary}, joint detection-attribution \cite{two_birds}---but all taxonomize by \emph{source} or \emph{production mode}, not recursive generation \emph{depth}.
7	Recent work reframes detection as an out-of-distribution problem \cite{human_texts_outliers}; depth profiling differs in targeting ordinal depth rather than binary membership, with cross-generator transfer as the evaluation axis.
8	We introduce ordinal depth classification \cite{gutierrez_ordinal_survey,coral_ordinal} as a complementary task; repurposing existing detection scores as depth predictors reveals high cross-generator variance (binary F1\,=\,0.54--0.71; Table~\ref{tab:baselines}).
9	
10	\paragraph{Model collapse and iterative generation.}
11	\looseness=-1 Self-consuming generative models lose distributional coverage via training-loop parameter updates \cite{self_consuming_mad,curse_of_recursion,strong_model_collapse,dohmatob_tale_of_tails,schaeffer_collapse_position}; we instead examine \emph{inference chains} where parameters are fixed.
12	Concurrent iterative-generation studies document complementary phenomena: paraphrasing chains show factuality degradation \cite{broken_telephone}, Markovian analysis bounds distinguishable depth to ${\sim}$3 classes \cite{markovian_chains}, and attractor cycle evidence emerges \cite{attractor_cycles}.
13	DDR differs in chain type (non-paraphrastic continuation), analysis lens (location/shape decomposition identifying what is \emph{preserved}), and downstream utility (shape stability enables cross-generator classification without calibration); a detailed comparison appears in Appendix~\ref{app:iterative-comparison}.
14	
15	\paragraph{Diversity, stylometry, and provenance.}
16	\looseness=-1 Declining lexical diversity under recursive generation \cite{curious_decline,writing_diversity} aligns with the monotonic TTR and hapax ratio decline we observe; these classical stylometric features \cite{stamatatos_survey} constitute DDR's drifting component.
17	Data curation relies on quality signals \cite{dsir,ccnet}; generation depth offers a complementary provenance axis.
18	Watermarking \cite{watermark_llm,synthid_text} requires generator cooperation and degrades across multi-step chains \cite{chainwash}; our post-hoc approach requires no generation-time modification.
19	Our NLL tail analysis extends probability-based membership inference \cite{min_k_percent,koike_mia_detection} from binary membership to ordinal depth.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e98c40a-8dc0-426d-bae6-3b735d8cace2",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "aa2265d384aeafb01",
  "type": "user",
  "uuid": "3e860a16-3bc8-4edb-b8c4-48b854e96999",
  "sourceToolAssistantUUID": "8e98c40a-8dc0-426d-bae6-3b735d8cace2",
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

_source line 81 · 2026-05-25T20:46:07.686Z_

Now I have read all files. Let me compile the complete inventory.

---

## Complete Numerical Value Inventory by File

---

### appendix_ablation.tex

| Line | Value | Measure |
|------|-------|---------|
| 6 | +8.5 pp | Full > surface feature set F1 improvement |
| 6 | +6.0 pp | Full > reference feature set F1 improvement |
| 14 | 0.773 | Full (7 features) F1, 8-gen 10-fold stratified CV, 3-class |
| 14 | 0.35 | hapax_ratio importance (top feature in full set) |
| 15 | 0.688 | Surface only (2 features) F1 |
| 15 | 0.41 | hapax_ratio importance (top feature in surface-only set) |
| 16 | 0.713 | Reference only (5 features) F1 |
| 16 | 0.27 | entropy_mean importance (top feature in reference-only set) |

---

### appendix_confusion_matrix.tex

| Line | Value | Measure |
|------|-------|---------|
| 7 | 27,529 | Total sample count N for 6-generator LOGO evaluation |
| 7 | 18.8% | Gen-1 misclassified as gen-2+ (row-normalized) |
| 7 | 6.2% | Gen-1 misclassified as gen-0 (row-normalized) |
| 7 | 3x | Ratio of gen-1→gen-2+ vs gen-1→gen-0 misclassification |
| 14 | 5,937 | True gen-0 predicted as gen-0 (count) |
| 14 | 99.4% | True gen-0 predicted as gen-0 (row-normalized %) |
| 14 | 35 | True gen-0 predicted as gen-1 (count) |
| 14 | 0.6% | True gen-0 predicted as gen-1 (row-normalized %) |
| 14 | 0 | True gen-0 predicted as gen-2+ (count) |
| 14 | 0.0% | True gen-0 predicted as gen-2+ (row-normalized %) |
| 15 | 368 | True gen-1 predicted as gen-0 (count) |
| 15 | 6.2% | True gen-1 predicted as gen-0 (row-normalized %) |
| 15 | 4,437 | True gen-1 predicted as gen-1 (count) |
| 15 | 75.0% | True gen-1 predicted as gen-1 (row-normalized %) |
| 15 | 1,113 | True gen-1 predicted as gen-2+ (count) |
| 15 | 18.8% | True gen-1 predicted as gen-2+ (row-normalized %) |
| 16 | 464 | True gen-2+ predicted as gen-0 (count) |
| 16 | 3.0% | True gen-2+ predicted as gen-0 (row-normalized %) |
| 16 | 3,646 | True gen-2+ predicted as gen-1 (count) |
| 16 | 23.3% | True gen-2+ predicted as gen-1 (row-normalized %) |
| 16 | 11,529 | True gen-2+ predicted as gen-2+ (count) |
| 16 | 73.7% | True gen-2+ predicted as gen-2+ (row-normalized %) |
| 22 | 99.4% | Gen-0 recall |
| 22 | 18.8% | Gen-1 confusion with gen-2+ |
| 22 | 6.2% | Gen-1 confusion with gen-0 |
| 22 | 23.3% | Gen-2+ misclassification into gen-1 |
| 28 | 27,529 | N for confusion matrix |

---

### appendix_cross_model_detail.tex

| Line | Value | Measure |
|------|-------|---------|
| 6 | 2,964 | Sample count N for cross-model evaluation |
| 6 | 5 | Number of generators |
| 6 | 0.831 | Macro F1 under class balancing |
| 6 | 0.789 | Macro F1 under natural class distribution |
| 6 | 0.830 | Binary F1 (gen-1 vs gen-2+) |
| 6 | [.818, .841] | 95% CI for binary F1 |
| 6 | 2,000 | Number of bootstrap samples |
| 12 | 0.921 | gen-0 precision |
| 12 | 0.948 | gen-0 recall |
| 12 | 0.935 | gen-0 F1 |
| 12 | [.923, .946] | gen-0 95% CI |
| 13 | 0.737 | gen-1 precision |
| 13 | 0.803 | gen-1 recall |
| 13 | 0.768 | gen-1 F1 |
| 13 | [.748, .788] | gen-1 95% CI |
| 14 | 0.842 | gen-2+ precision |
| 14 | 0.742 | gen-2+ recall |
| 14 | 0.789 | gen-2+ F1 |
| 14 | [.768, .809] | gen-2+ 95% CI |
| 16 | 0.831 | Macro F1 |
| 16 | [.817, .844] | Macro 95% CI |
| 22 | 3,778 | Sample count for ANOVA |
| 22 | <1% | Partial eta-squared for generator identity (all 7 features) |
| 22 | 0.05%--0.90% | Range of partial eta-squared for generator |
| 22 | 0.37% | Mean partial eta-squared for generator |
| 22 | 15.3%--29.9% | Depth variance explained in drifting features |
| 22 | <1% | Generator x depth interaction |
| 24 | 0.830 | Cross-model F1 advantage |

---

### appendix_cross_temp.tex

| Line | Value | Measure |
|------|-------|---------|
| 2 | 1.0 | Regenerated temperature for Qwen3-1.7B |
| 2 | 0.7 | Default temperature for other generators |
| 2 | 0.95 | Top-p for t=1.0 data |
| 2 | 0.9 | Top-p for other configurations |
| 7 | -6.6 pp | Largest F1 degradation (0.7→1.0 transfer, 3-class) |
| 7 | 0.418 | Qwen3-1.7B F1 under cross-temperature conditions |
| 14 | 0.789 | 3-class F1 for t=0.7 matched condition |
| 14 | 0.726 | 3-class F1 for t=1.0 matched condition |
| 16 | 0.791 | F1 for train t=1.0 / test t=0.7 |
| 16 | 0.723 | F1 for train t=0.7 / test t=1.0 |
| 18 | 0.418 | Qwen3-1.7B F1 under cross-temperature |
| 18 | 0.76 | Minimum F1 for other generators |
| 20 | 0.948 | Qwen3-1.7B binary F1 (matched condition) |
| 20 | 0.713 | Qwen3-1.7B binary F1 under 0.7→1.0 transfer |
| 20 | 0.948 | Qwen3-1.7B binary F1 under 1.0→0.7 transfer |
| 20 | 0.900--0.958 | Aggregate binary F1 range |

---

### appendix_dataset_stats.tex

| Line | Value | Measure |
|------|-------|---------|
| 4 | 50 | Minimum whitespace token threshold for filtering |
| 5 | 7,963 | gen-0 sample count |
| 5 | 21.5% | gen-0 proportion |
| 5 | 7,896 | gen-1 sample count |
| 5 | 21.3% | gen-1 proportion |
| 5 | 21,199 | gen-2+ sample count |
| 5 | 57.2% | gen-2+ proportion |
| 11 | ~1,000 | Shared Wikipedia seeds per generator |
| 17 | 1.0B | Pythia-1B parameter count |
| 17 | 4,555 | Pythia-1B sample count |
| 18 | 2.8B | Pythia-2.8B parameter count |
| 18 | 4,609 | Pythia-2.8B sample count |
| 19 | 1.5B | OLMo-2-1B parameter count |
| 19 | 4,713 | OLMo-2-1B sample count |
| 20 | 0.6B | Qwen3-0.6B parameter count |
| 20 | 4,538 | Qwen3-0.6B sample count |
| 21 | 1.7B | Qwen3-1.7B parameter count |
| 21 | 4,617 | Qwen3-1.7B sample count |
| 22 | 8.2B | Qwen3-8B parameter count |
| 22 | 4,497 | Qwen3-8B sample count |
| 23 | 3.2B | Llama-3.2-3B parameter count |
| 23 | 4,680 | Llama-3.2-3B sample count |
| 24 | 7.0B | Mistral-7B parameter count |
| 24 | 4,849 | Mistral-7B sample count |
| 26 | 37,058 | Total sample count |
| 30 | 34,131 | Subset with all detector scores available |
| 32 | 37,058 | N for violin plots |
| 38 | 0.60 | Drifting feature |rho| threshold (>0.60) |
| 38 | 0.10 | Shape feature |rho| threshold (<0.10) |

---

### appendix_downstream.tex

| Line | Value | Measure |
|------|-------|---------|
| 2 | 3 | Number of seeds per variant |
| 7 | 2.367 | Random subsampling test perplexity |
| 7 | 2.387 | Depth 0-1 test perplexity |
| 7 | 2.389 | Binary-filtered test perplexity |
| 13 | 12,299 | Sample count for all-depths variant |
| 13 | 2.335 | All-depths test perplexity |
| 13 | 0.000 | Standard deviation (all-depths) |
| 14 | 3,951 | Sample count for size-matched variants |
| 14 | 2.367 | Size-matched random test perplexity |
| 14 | 0.000 | Std for size-matched random |
| 15 | 3,951 | Sample count for depth 0-1 |
| 15 | 2.387 | Depth 0-1 test perplexity |
| 15 | 0.001 | Std for depth 0-1 |
| 16 | 3,951 | Sample count for binary-filtered |
| 16 | 2.389 | Binary-filtered test perplexity |
| 16 | 0.000 | Std for binary-filtered |
| 17 | 797 | Sample count for depth-0 only |
| 17 | 2.681 | Depth-0 only test perplexity |
| 17 | 0.001 | Std for depth-0 only |
| 23 | 12,299 | All samples count |
| 23 | 2.335 | Lowest perplexity |
| 24 | 3,951 | Size-matched count |
| 24 | 2.367 | Random subsampling PPL |
| 24 | 2.387 | Depth 0-1 PPL |
| 24 | 2.389 | Binary-filtered PPL |
| 25 | 0.002 | Maximum cross-seed variance |
| 27 | 797 | Depth-0 only count |
| 27 | 2.681 | Depth-0 only PPL |
| 27 | 5x | Data volume reduction factor |
| 30 | +/-2% | Relative margin for TOST |
| 30 | +/-0.047 | Absolute equivalence bounds on PPL scale |
| 31 | 3,951 | Equal sample count |
| 31 | 2.367 | Random PPL |
| 31 | 2.387 | Depth 0-1 PPL |
| 31 | 0.020 | Delta between conditions |
| 32 | 1.1 x 10^-4 | TOST p-value |
| 33 | 0.001 | Max cross-seed std |
| 35 | 12,299 | Full dataset N |
| 35 | 2.335 | Full dataset PPL |
| 35 | 3,951 | Filtered subset N |
| 35 | 2.387 | Filtered subset PPL |
| 35 | 0.053 | Minimum equivalence margin for full vs filtered |
| 53 | 1.0 | TOST p for Full vs Random at +/-1% |
| 54 | 1 x 10^-6 | TOST p for Full vs Random at +/-2% |
| 55 | <10^-10 | TOST p for Full vs Random at +/-3% |
| 56 | <10^-10 | TOST p for Full vs Random at +/-5% |
| 58 | 1.0 | TOST p for Full vs Depth 0-1 at +/-1% |
| 59 | 1.0 | TOST p for Full vs Depth 0-1 at +/-2% |
| 60 | <10^-10 | TOST p for Full vs Depth 0-1 at +/-3% |
| 61 | <10^-10 | TOST p for Full vs Depth 0-1 at +/-5% |
| 66 | 10^-6 | TOST p for full vs random at +/-2% |
| 67 | 0.032 | Delta full vs random (absolute PPL) |
| 67 | 1.4% | Delta full vs random (relative to baseline) |
| 67 | 0.052 | Delta full vs depth 0-1 (absolute) |
| 67 | 2.2% | Delta full vs depth 0-1 (relative) |
| 69 | 86.0 | Cohen's d (full vs random) |
| 69 | 119.7 | Cohen's d (full vs depth 0-1) |
| 70 | 3 | Seeds per condition |
| 70 | <0.001 | Pooled standard deviation |
| 73 | 3 | Seeds per condition (repeated) |

---

### appendix_feature_correlation.tex

| Line | Value | Measure |
|------|-------|---------|
| 8 | 27,529 | N for Pearson correlation matrix |
| 15 | 0.49 | r(H_mean, H_std) |
| 15 | 0.31 | r(H_mean, H_min) |
| 15 | 0.01 | r(H_mean, H_max) |
| 15 | 0.07 | r(H_mean, tail_decay) |
| 15 | 0.86 | r(H_mean, TTR) |
| 15 | 0.81 | r(H_mean, hapax) |
| 16 | -0.15 | r(H_std, H_min) |
| 16 | 0.16 | r(H_std, H_max) |
| 16 | 0.26 | r(H_std, tail_decay) |
| 16 | 0.43 | r(H_std, TTR) |
| 16 | 0.34 | r(H_std, hapax) |
| 17 | -0.04 | r(H_min, H_max) |
| 17 | 0.01 | r(H_min, tail_decay) |
| 17 | 0.20 | r(H_min, TTR) |
| 17 | 0.23 | r(H_min, hapax) |
| 18 | -0.08 | r(H_max, tail_decay) |
| 18 | -0.13 | r(H_max, TTR) |
| 18 | -0.15 | r(H_max, hapax) |
| 19 | 0.13 | r(tail_decay, TTR) |
| 19 | 0.14 | r(tail_decay, hapax) |
| 20 | 0.97 | r(TTR, hapax) |
| 26 | 0.97 | TTR-hapax correlation |
| 26 | 0.86 | TTR-entropy_mean correlation |
| 26 | 0.81 | hapax-entropy_mean correlation |
| 27 | 92.3% | PCA variance explained by PC1 (drifting subset) |
| 27 | 0.56--0.59 | PC1 loading range (drifting subset) |
| 28 | 44.4% | PC1 variance (full 7-feature PCA) |
| 28 | 0.53--0.55 | PC1 loading range (full 7-feature) |
| 28 | 18.3% | PC2 variance (full 7-feature PCA) |
| 29 | 0.27 | Maximum pairwise |r| among shape features |

---

### appendix_generator_subsets.tex

| Line | Value | Measure |
|------|-------|---------|
| 12 | 8 | Number of generators in Main LOGO |
| 14 | 5 | Number of generators in cross-model chains |
| 15 | 6 | Number of generators in QLoRA |
| 16 | 4 | Number of generators in temperature ablation |
| 17 | 1 | Number of generators in prompt-type |
| 18 | 3 | Number of generators in cross-domain |
| 19 | 3 | Number of generators in instruct |
| 20 | 5 | Number of generators in downstream |

---

### appendix_human_edit.tex

| Line | Value | Measure |
|------|-------|---------|
| 7 | 1000 | Bootstrap iterations for 95% CIs |
| 14 | 0.695 | Binary F1 at 0% perturbation (baseline) |
| 14 | [0.680, 0.710] | 95% CI at 0% |
| 14 | 0.737 | 3-class F1 at 0% |
| 15 | 0.650 | Binary F1 at 5% perturbation |
| 15 | [0.635, 0.666] | 95% CI at 5% |
| 15 | 0.641 | 3-class F1 at 5% |
| 16 | 0.614 | Binary F1 at 10% perturbation |
| 16 | [0.599, 0.629] | 95% CI at 10% |
| 16 | 0.492 | 3-class F1 at 10% |
| 17 | 0.591 | Binary F1 at 20% perturbation |
| 17 | [0.576, 0.605] | 95% CI at 20% |
| 17 | 0.367 | 3-class F1 at 20% |
| 22 | -4.6 pp | Drop from 0% to 5% binary F1 |
| 22 | -3.6 pp | Drop from 5% to 10% |
| 22 | -2.3 pp | Drop from 10% to 20% |
| 23 | 0.614 | Binary F1 at 10% |
| 23 | 0.50 | Random baseline |
| 25 | 0.737→0.367 | 3-class F1 range at 20% |
| 30 | 0.833 | Entropy-only binary F1 at 0% |
| 30 | 0.695 | 7-feature binary F1 at 0% |
| 30 | 0.688 | Entropy-only 3-class F1 at 0% |
| 31 | 0.591 | 7-feature binary F1 at 20% |
| 31 | 0.566 | Entropy-only binary F1 at 20% |
| 46 | 0.833 | Ent-only Bin 0% |
| 46 | 0.695 | 7-feat Bin 0% |
| 46 | 0.688 | Ent-only 3-cl 0% |
| 46 | 0.737 | 7-feat 3-cl 0% |
| 47 | 0.736 | Ent-only Bin 5% |
| 47 | 0.650 | 7-feat Bin 5% |
| 47 | 0.539 | Ent-only 3-cl 5% |
| 47 | 0.641 | 7-feat 3-cl 5% |
| 48 | 0.657 | Ent-only Bin 10% |
| 48 | 0.614 | 7-feat Bin 10% |
| 48 | 0.427 | Ent-only 3-cl 10% |
| 48 | 0.492 | 7-feat 3-cl 10% |
| 49 | 0.566 | Ent-only Bin 20% |
| 49 | 0.591 | 7-feat Bin 20% |
| 49 | 0.314 | Ent-only 3-cl 20% |
| 49 | 0.367 | 7-feat 3-cl 20% |
| 66 | 0.695 | 7-feature ensemble binary F1 at 0% |
| 66 | 0.650 | 7-feature at 5% |
| 66 | 0.614 | 7-feature at 10% |
| 66 | 0.591 | 7-feature at 20% |
| 67 | 0.677 | LD-Score at 0% |
| 67 | 0.673 | LD-Score at 5% |
| 67 | 0.677 | LD-Score at 10% |
| 67 | 0.671 | LD-Score at 20% |
| 68 | 0.682 | Avg-LogProb at 0% |
| 68 | 0.419 | Avg-LogProb at 5% |
| 68 | 0.335 | Avg-LogProb at 10% |
| 68 | 0.375 | Avg-LogProb at 20% |
| 69 | 0.571 | FastDetectGPT at 0% |
| 69 | 0.437 | FastDetectGPT at 5% |
| 69 | 0.468 | FastDetectGPT at 10% |
| 69 | 0.514 | FastDetectGPT at 20% |
| 70 | 0.500 | Binoculars at 0% |
| 70 | 0.461 | Binoculars at 5% |
| 70 | 0.446 | Binoculars at 10% |
| 70 | 0.425 | Binoculars at 20% |
| 78 | 0.695 | 7-feature highest unperturbed binary F1 |
| 78 | -0.6 pp | LD-Score degradation 0%→20% |
| 80 | -34.7 pp | Avg-LogProb degradation at 10% |
| 80 | -13.4 pp | FastDetectGPT drop at 5% |
| 82 | -10.4 pp | 7-feature ensemble degradation at 20% |
| 85 | 1.69 | Avg sentences regenerated per passage |
| 85 | ~50% | Edit distance from LLM regeneration |
| 86 | 0.692 | Binary F1 before LLM regeneration |
| 86 | 0.647 | Binary F1 after LLM regeneration |
| 86 | -4.5 pp | Binary F1 drop from LLM regeneration |
| 86 | 6.5% | Relative binary drop |
| 86 | 0.739 | 3-class F1 before LLM regeneration |
| 86 | 0.667 | 3-class F1 after LLM regeneration |
| 86 | -7.1 pp | 3-class F1 drop from LLM regeneration |
| 86 | 9.7% | Relative 3-class drop |
| 87 | -4.5 pp | Binary degradation (LLM rephrase) |
| 87 | -4.6 pp | Binary degradation (5% random word replacement) |
| 87 | ~50% | Characters altered by LLM rephrase |
| 92 | 1.1 pp | Max F1 variation across seed TTR terciles |

---

### appendix_prompt_type.tex

| Line | Value | Measure |
|------|-------|---------|
| 1 | 995 | Number of seeds per prompt type |
| 1 | 5 | Number of depths per chain |
| 10 | 0.78 | Continuation 5-fold CV macro-F1 |
| 10 | 0.74 | Rewriting 5-fold CV macro-F1 |
| 10 | 0.73 | Elaboration 5-fold CV macro-F1 |
| 10 | 5% | Near-stationary feature max change |
| 13 | 0.753 | LOPTO average F1 |
| 13 | 16.9% | Continuation feature decay rate per depth step |
| 13 | 6.1% | Rewriting feature decay rate per depth step |
| 13 | 1.4% | Elaboration feature decay rate per depth step |

---

### appendix_qualitative_examples.tex

| Line | Value | Measure |
|------|-------|---------|
| 32 | <2% | Range for H_max across chain (shape feature) |
| 32 | <4% | Range for tail decay across chain (shape feature) |
| 39 | 2.720 | Gen-0 entropy mean |
| 39 | 2.206 | Gen-1 entropy mean |
| 39 | 0.780 | Gen-2 entropy mean |
| 40 | 1.772 | Gen-0 entropy std |
| 40 | 1.816 | Gen-1 entropy std |
| 40 | 1.517 | Gen-2 entropy std |
| 41 | 0.002 | Gen-0 entropy min |
| 41 | 0.005 | Gen-1 entropy min |
| 41 | 0.000 | Gen-2 entropy min |
| 42 | 7.000 | Gen-0 entropy max |
| 42 | 7.016 | Gen-1 entropy max |
| 42 | 6.926 | Gen-2 entropy max |
| 43 | -0.00227 | Gen-0 tail decay |
| 43 | -0.00231 | Gen-1 tail decay |
| 43 | -0.00223 | Gen-2 tail decay |
| 44 | 0.659 | Gen-0 TTR |
| 44 | 0.272 | Gen-1 TTR |
| 44 | 0.081 | Gen-2 TTR |
| 45 | 0.561 | Gen-0 hapax ratio |
| 45 | 0.183 | Gen-1 hapax ratio |
| 45 | 0.005 | Gen-2 hapax ratio |

---

### appendix_temperature_stability.tex

| Line | Value | Measure |
|------|-------|---------|
| 1 | 12 | Total conditions (features x generators x temps) |
| 13 | 1.39 | Entropy mean mean |d| at t=0.5 |
| 13 | 1.10 | Entropy mean mean |d| at t=0.7 |
| 13 | 0.58 | Entropy mean mean |d| at t=0.9 |
| 14 | 1.00 | TTR mean |d| at t=0.5 |
| 14 | 0.85 | TTR mean |d| at t=0.7 |
| 14 | 0.45 | TTR mean |d| at t=0.9 |
| 15 | 0.87 | Hapax ratio mean |d| at t=0.5 |
| 15 | 0.75 | Hapax ratio mean |d| at t=0.7 |
| 15 | 0.42 | Hapax ratio mean |d| at t=0.9 |
| 17 | 0.84 | Entropy std mean |d| at t=0.5 |
| 17 | 0.52 | Entropy std mean |d| at t=0.7 |
| 17 | 0.20 | Entropy std mean |d| at t=0.9 |
| 19 | 0.06 | Entropy max mean |d| at t=0.5 |
| 19 | 0.09 | Entropy max mean |d| at t=0.7 |
| 19 | 0.11 | Entropy max mean |d| at t=0.9 |
| 20 | 0.07 | Tail decay mean |d| at t=0.5 |
| 20 | 0.12 | Tail decay mean |d| at t=0.7 |
| 20 | 0.15 | Tail decay mean |d| at t=0.9 |
| 21 | 0.04 | Entropy min mean |d| at t=0.5 |
| 21 | 0.06 | Entropy min mean |d| at t=0.7 |
| 21 | 0.04 | Entropy min mean |d| at t=0.9 |
| 26 | 10/12 | Conditions where TTR is drifting |
| 26 | 9/12 | Conditions where hapax is drifting |
| 26 | 10/12 | Conditions where entropy min is near-stationary |
| 26 | 9/12 | Conditions where entropy max is near-stationary |
| 28 | 1.09 | Mean |d| drifting set at t=0.5 |
| 28 | 0.90 | Mean |d| drifting set at t=0.7 |
| 28 | 0.48 | Mean |d| drifting set at t=0.9 |

---

### appendix_classifier.tex

| Line | Value | Measure |
|------|-------|---------|
| 16 | 0.789 | XGBoost avg LOGO F1 (6-gen, 3-class) |
| 16 | 0.764 | XGBoost F1 for OLMo-2 |
| 16 | 0.856 | XGBoost F1 for Py-1B |
| 16 | 0.804 | XGBoost F1 for Py-2.8B |
| 16 | 0.824 | XGBoost F1 for Qw-0.6B |
| 16 | 0.806 | XGBoost F1 for Qw-1.7B |
| 16 | 0.683 | XGBoost F1 for Qw-8B |
| 17 | 0.790 | Random Forest avg F1 |
| 17 | 0.764 | RF F1 for OLMo-2 |
| 17 | 0.856 | RF F1 for Py-1B |
| 17 | 0.804 | RF F1 for Py-2.8B |
| 17 | 0.825 | RF F1 for Qw-0.6B |
| 17 | 0.807 | RF F1 for Qw-1.7B |
| 17 | 0.684 | RF F1 for Qw-8B |
| 18 | 0.725 | Logistic Regression avg F1 |
| 18 | 0.719 | LR F1 for OLMo-2 |
| 18 | 0.781 | LR F1 for Py-1B |
| 18 | 0.740 | LR F1 for Py-2.8B |
| 18 | 0.745 | LR F1 for Qw-0.6B |
| 18 | 0.743 | LR F1 for Qw-1.7B |
| 18 | 0.624 | LR F1 for Qw-8B |
| 24 | 0.79 | Tree-based classifier LOGO F1 |
| 25 | 0.725 | Linear model F1 |
| 25 | 0.33 | Chance baseline for 3 classes |
| 39 | 2.0 pp | 3-class F1 total variation across max_depth |
| 39 | 0.1 pp | Binary F1 maximum variation |
| 45 | 0.752 | 3-class F1 at max_depth=3 |
| 45 | 0.700 | Binary F1 at max_depth=3 |
| 46 | 0.759 | 3-class F1 at max_depth=4 |
| 46 | 0.699 | Binary F1 at max_depth=4 |
| 47 | 0.769 | 3-class F1 at max_depth=6 |
| 47 | 0.700 | Binary F1 at max_depth=6 |
| 48 | 0.772 | 3-class F1 at max_depth=8 |
| 48 | 0.699 | Binary F1 at max_depth=8 |
| 53 | 0.752--0.772 | 3-class F1 range |
| 53 | 0.699--0.700 | Binary F1 range |
| 54 | 0.3 pp | Distance of default max_depth=6 from best |
| 59 | 27,529 | N for confusion matrix |
| 66 | 0.9 | Nucleus sampling p |
| 78 | 0.814 | Pythia-2.8B binary F1 at t=0.5 |
| 78 | [.798, .828] | 95% CI |
| 78 | -0.58 | rho(ent. mean) at t=0.5 |
| 79 | 0.740 | Pythia-2.8B binary F1 at t=0.7 |
| 79 | [.725, .755] | 95% CI |
| 79 | -0.60 | rho at t=0.7 |
| 80 | 0.480 | Pythia-2.8B binary F1 at t=0.9 |
| 80 | [.465, .498] | 95% CI |
| 80 | -0.30 | rho at t=0.9 |
| 82 | 0.783 | OLMo-2-1B binary F1 at t=0.5 |
| 82 | [.768, .798] | 95% CI |
| 82 | -0.72 | rho at t=0.5 |
| 83 | 0.695 | OLMo-2-1B binary F1 at t=0.7 |
| 83 | [.679, .711] | 95% CI |
| 83 | -0.60 | rho at t=0.7 |
| 84 | 0.453 | OLMo-2-1B binary F1 at t=0.9 |
| 84 | [.437, .469] | 95% CI |
| 84 | -0.26 | rho at t=0.9 |
| 86 | 0.751 | Qwen3-1.7B binary F1 at t=0.5 |
| 86 | -0.60 | rho at t=0.5 |
| 87 | 0.751 | Qwen3-1.7B binary F1 at t=0.7 |
| 87 | -0.60 | rho at t=0.7 |
| 88 | 0.566 | Qwen3-1.7B binary F1 at t=0.9 |
| 88 | -0.37 | rho at t=0.9 |
| 90 | 0.711 | Qwen3-0.6B binary F1 at t=0.5 |
| 90 | [.694, .729] | 95% CI |
| 90 | -0.67 | rho at t=0.5 |
| 91 | 0.691 | Qwen3-0.6B binary F1 at t=0.7 |
| 91 | [.673, .709] | 95% CI |
| 91 | -0.60 | rho at t=0.7 |
| 92 | 0.598 | Qwen3-0.6B binary F1 at t=0.9 |
| 92 | [.582, .615] | 95% CI |
| 92 | -0.29 | rho at t=0.9 |
| 101 | 9.3--26.0 pp | Binary F1 loss range at t=0.9 |
| 101 | 0.26--0.37 | rho range at t=0.9 |
| 101 | 0.58--0.72 | rho range at t=0.5 |
| 101 | +7.4 pp | Pythia-2.8B gain at t=0.5 |
| 101 | +8.8 pp | OLMo-2-1B gain at t=0.5 |
| 101 | 0--2.0 pp | Qwen model change at t=0.5 |

---

### appendix_ddr_validation.tex

| Line | Value | Measure |
|------|-------|---------|
| 4 | 0.20 | TOST equivalence bound (d) |
| 4 | 0.30 | rho threshold |
| 4 | 0.40 | Entropy min pooled |rho| |
| 4 | 0.03 | Entropy min gen-1 vs gen-2+ d |
| 10 | 0.660 | Silhouette score at k=2 |
| 23 | 0.660 | Silhouette at k=2 (best) |
| 24 | 0.532 | Silhouette at k=3 |
| 25 | 0.527 | Silhouette at k=4 |
| 29 | 0.660 | Primary split silhouette |
| 30 | 0.40 | Entropy min pooled |rho| |
| 31 | 0.03 | Entropy min gen-1 vs gen-2+ d |
| 32 | 0.527 | Silhouette at k=4 |
| 36 | 35 | Number of possible 3/4 partitions (C(7,3)) |
| 36 | 0.660 | Highest silhouette (observed DDR partition) |
| 36 | 0.18 | Gap to second-ranked split |
| 36 | 20 | Partitions with negative silhouette |
| 40 | 0.505 | Minimum per-generator silhouette (Pythia-1B) |
| 40 | 0.760 | Maximum per-generator silhouette (Mistral-7B) |
| 40 | 0.651 | Mean per-generator silhouette |
| 41 | 0.50 | Moderate-structure threshold |
| 46 | 0.05 | TOST alpha |
| 58 | 0/8 | H_mean TOST pass at eps=0.15 |
| 58 | 0/8 | H_mean TOST pass at eps=0.20 |
| 58 | 0/8 | H_mean TOST pass at eps=0.25 |
| 59 | 0/8 | TTR TOST pass at eps=0.15 |
| 59 | 0/8 | TTR TOST pass at eps=0.20 |
| 59 | 0/8 | TTR TOST pass at eps=0.25 |
| 60 | 0/8 | hapax TOST pass at eps=0.15 |
| 60 | 0/8 | hapax TOST pass at eps=0.20 |
| 60 | 0/8 | hapax TOST pass at eps=0.25 |
| 62 | 0/8 | ent_std TOST pass at eps=0.15 |
| 62 | 0/8 | ent_std TOST pass at eps=0.20 |
| 62 | 0/8 | ent_std TOST pass at eps=0.25 |
| 64 | 7/8 | H_min TOST pass at eps=0.15 |
| 64 | 8/8 | H_min TOST pass at eps=0.20 |
| 64 | 8/8 | H_min TOST pass at eps=0.25 |
| 65 | 6/8 | H_max TOST pass at eps=0.15 |
| 65 | 6/8 | H_max TOST pass at eps=0.20 |
| 65 | 6/8 | H_max TOST pass at eps=0.25 |
| 66 | 4/8 | tail_decay TOST pass at eps=0.15 |
| 66 | 4/8 | tail_decay TOST pass at eps=0.20 |
| 66 | 7/8 | tail_decay TOST pass at eps=0.25 |
| 71 | 7/8 | Entropy min pass rate at eps=0.15 |
| 72 | 0.15--0.22 | Non-passing tail decay d range |
| 72 | 0.50 | Drifting threshold |
| 73 | 0.21 | Pythia-1B H_max d |
| 73 | 0.25 | Pythia-2.8B H_max d |
| 76 | 0.20 | Primary equivalence bound |
| 78 | 0.74 | Minimum drifting d |
| 78 | 0.20 | Equivalence bound |
| 78 | 3.7x | Margin between drifting min and bound |
| 80 | <2 pp | Near-stationary LOFO marginal importance |
| 86 | 0.10--0.80 | Threshold sweep range for |d| |
| 86 | 0.05 | Sweep increment |
| 88 | 3 | Number of distinct partitions in sweep |
| 91 | 0.660 | Peak silhouette (3-feature drifting set) |
| 93 | 0.46 | Entropy std d |
| 93 | 0.451 | Silhouette for 4/3 partition |
| 108 | 0.46 | Entropy std reclassification threshold |
| 115 | 1.05 | Ent mean pooled d |
| 116 | 0.81 | TTR pooled d |
| 117 | 0.74 | Hapax ratio pooled d |
| 119 | 0.46 | Ent std pooled d |
| 121 | 0.06 | Ent max pooled d |
| 122 | 0.09 | Tail decay pooled d |
| 123 | 0.016 | Ent min pooled d |
| 128 | 0.74 | Min drifting pooled d |
| 128 | 0.09 | Max near-stationary pooled d |
| 129 | 0.28 | Minimum gap between adjacent zones (hapax - ent_std) |
| 136 | 4 | Generators per split (selection set) |
| 136 | 4 | Generators per split (validation set) |
| 151 | 0.60 | H_mean sel |rho| Split A |
| 151 | 0.58 | H_mean val |rho| Split A |
| 151 | 0.02 | H_mean delta |rho| Split A |
| 151 | 0.60 | H_mean sel |rho| Split B |
| 151 | 0.58 | H_mean val |rho| Split B |
| 151 | 0.02 | H_mean delta |rho| Split B |
| 152 | 0.61 | TTR sel |rho| Split A |
| 152 | 0.59 | TTR val |rho| Split A |
| 152 | 0.02 | TTR delta Split A |
| 152 | 0.60 | TTR sel |rho| Split B |
| 152 | 0.59 | TTR val |rho| Split B |
| 152 | 0.01 | TTR delta Split B |
| 153 | 0.62 | Hapax sel |rho| Split A |
| 153 | 0.60 | Hapax val |rho| Split A |
| 153 | 0.02 | Hapax delta Split A |
| 153 | 0.62 | Hapax sel |rho| Split B |
| 153 | 0.61 | Hapax val |rho| Split B |
| 153 | 0.01 | Hapax delta Split B |
| 155 | 0.19 | Ent std sel |rho| Split A |
| 155 | 0.21 | Ent std val |rho| Split A |
| 155 | 0.02 | Ent std delta Split A |
| 155 | 0.22 | Ent std sel |rho| Split B |
| 155 | 0.17 | Ent std val |rho| Split B |
| 155 | 0.05 | Ent std delta Split B |
| 157 | 0.39 | H_min sel |rho| Split A |
| 157 | 0.36 | H_min val |rho| Split A |
| 157 | 0.03 | H_min delta Split A |
| 157 | 0.38 | H_min sel |rho| Split B |
| 157 | 0.37 | H_min val |rho| Split B |
| 157 | 0.01 | H_min delta Split B |
| 158 | 0.05 | H_max sel |rho| Split A |
| 158 | 0.05 | H_max val |rho| Split A |
| 158 | 0.00 | H_max delta Split A |
| 158 | 0.04 | H_max sel |rho| Split B |
| 158 | 0.06 | H_max val |rho| Split B |
| 158 | 0.02 | H_max delta Split B |
| 159 | 0.10 | Tail sel |rho| Split A |
| 159 | 0.08 | Tail val |rho| Split A |
| 159 | 0.02 | Tail delta Split A |
| 159 | 0.11 | Tail sel |rho| Split B |
| 159 | 0.07 | Tail val |rho| Split B |
| 159 | 0.04 | Tail delta Split B |
| 164 | 0.36--0.39 | Entropy min pooled |rho| range across subsets |
| 164 | 0.06 | Entropy min binary d (uniformly below) |
| 169 | 0.05 | Maximum delta |rho| between sel and val |
| 169 | >0.15 | Minimum gap between adjacent zones (all subsets) |
| 181 | <10^-10 | Levene test p-value for drifting features |
| 181 | 1.86--2.21 | Variance ratios for drifting features |
| 187 | 29,095 | N for effect size comparison |
| 192 | 1.054 | Ent mean |d| |
| 192 | 1.410 | Ent mean |Delta| (Glass's) |
| 192 | 0.587 | Ent mean |delta| (Cliff's) |
| 193 | 0.814 | TTR |d| |
| 193 | 1.116 | TTR |Delta| |
| 193 | 0.510 | TTR |delta| |
| 194 | 0.735 | Hapax |d| |
| 194 | 0.936 | Hapax |Delta| |
| 194 | 0.528 | Hapax |delta| |
| 197 | 0.457 | Ent std |d| |
| 197 | 0.605 | Ent std |Delta| |
| 197 | 0.295 | Ent std |delta| |
| 199 | 0.087 | Tail decay |d| |
| 199 | 0.099 | Tail decay |Delta| |
| 199 | 0.072 | Tail decay |delta| |
| 200 | 0.062 | Ent max |d| |
| 200 | 0.065 | Ent max |Delta| |
| 200 | 0.021 | Ent max |delta| |
| 201 | 0.016 | Ent min |d| |
| 201 | 0.015 | Ent min |Delta| |
| 201 | 0.354 | Ent min |delta| (Cliff's, "medium") |
| 206 | 0.74 | Hapax ratio pooled d (main text 3-class) |
| 207 | 1.41 | Glass's Delta for ent mean |
| 207 | 1.05 | Cohen's d for ent mean |
| 207 | 2.08 | Variance ratio gen-2+/gen-1 for ent mean |
| 208 | 0.099 | Maximum Glass's Delta among near-stationary |
| 209 | 9.5x | Gap ratio under Glass's Delta (0.936/0.099) |
| 210 | 0.474 | Cliff's delta "large" threshold |
| 210 | 0.295 | Ent std Cliff's delta ("small") |
| 212 | 0.354 | Ent min Cliff's delta ("medium") |
| 212 | 0.016 | Ent min Cohen's d |
| 212 | 0.015 | Ent min Glass's Delta |

---

### appendix_iterative_comparison.tex

| Line | Value | Measure |
|------|-------|---------|
| 16 | 7--9B | Generator scale (Broken Telephone) |
| 16 | 3 | Open models (Broken Telephone) |
| 16 | 100 | Chain steps (Broken Telephone) |
| 24 | 7--8B | Generator scale (Markovian Chains) |
| 24 | 3+1 | Models (3 open + GPT-4o-mini) |
| 24 | 50 | Chain steps (Markovian Chains) |
| 24 | 1--4 | Recurrent outputs under greedy decoding |
| 24 | 10--20+ | Realizations under sampling |
| 32 | 0.6--8B | Generator scale (Ours) |
| 32 | 8 | Models (Ours) |
| 32 | 5 | Chain steps (Ours) |
| 46 | 0.05 | Mean |d| for shape features (greedy decoding) |
| 46 | 0.94 | Mean d for location drift (greedy decoding) |

---

### appendix_qlora.tex

| Line | Value | Measure |
|------|-------|---------|
| 4 | 16 | LoRA rank |
| 4 | 2 x 10^-4 | Learning rate |
| 4 | 3 | Number of epochs |
| 4 | 5 | Number of classes |
| 4 | 4 | Number of generators in subset |
| 4 | 0.805 | XGBoost 3-class F1 under same protocol |
| 18 | 0.497 | XGBoost 5-class F1 |
| 18 | 0.008 | XGBoost 5-class F1 std |
| 18 | 0.805 | XGBoost 3-class F1 |
| 18 | 0.008 | XGBoost 3-class F1 std |
| 19 | 0.583 | QLoRA 5-class F1 |
| 19 | 0.010 | QLoRA 5-class F1 std |
| 19 | 0.905 | QLoRA 3-class F1 |
| 19 | 0.003 | QLoRA 3-class F1 std |
| 19 | 0.999 | QLoRA per-class F1 gen-0 |
| 19 | 0.796 | QLoRA per-class F1 gen-1 |
| 19 | 0.413 | QLoRA per-class F1 gen-2 |
| 19 | 0.259 | QLoRA per-class F1 gen-3 |
| 19 | 0.447 | QLoRA per-class F1 gen-4 |
| 25 | 0.905 | QLoRA 3-class F1 |
| 25 | 0.003 | QLoRA 3-class std |
| 25 | +10.0 pp | Improvement over XGBoost (3-class) |
| 25 | 0.805 | XGBoost baseline |
| 26 | 0.583 | QLoRA 5-class F1 |
| 26 | 0.010 | QLoRA 5-class std |
| 26 | 0.497 | XGBoost 5-class F1 |
| 26 | +8.6 pp | Improvement (5-class) |
| 26 | 0.796 | QLoRA gen-1 F1 |
| 26 | 0.650 | XGBoost gen-1 F1 |
| 26 | 0.413 | QLoRA gen-2 F1 |
| 26 | 0.267 | XGBoost gen-2 F1 |
| 27 | 0.259 | Gen-3 F1 (primary failure mode) |
| 30 | 32 | Alternative LoRA rank |
| 30 | 123 | Alternative seed |
| 30 | 0.587 | Alternative 5-class F1 |
| 30 | 0.005 | Alternative 5-class std |
| 30 | 0.905 | Alternative 3-class F1 |
| 30 | 0.004 | Alternative 3-class std |
| 30 | <1 pp | Delta across hyperparameter/seed variation |

---

### appendix_feature_candidates.tex

| Line | Value | Measure |
|------|-------|---------|
| 14 | 0.685 | median |rho| |
| 14 | 0.794 | median d |
| 14 | +0.008 | median LOFO delta F1 |
| 14 | 0.960 | median max |r| with existing features |
| 15 | 0.693 | p90 |rho| |
| 15 | 0.960 | p90 d |
| 15 | +0.000 | p90 LOFO delta F1 |
| 15 | 0.937 | p90 max |r| |
| 16 | 0.708 | IQR |rho| |
| 16 | 1.079 | IQR d |
| 16 | +0.007 | IQR LOFO delta F1 |
| 16 | 0.908 | IQR max |r| |
| 17 | 0.633 | CV |rho| |
| 17 | 0.980 | CV d |
| 17 | -0.000 | CV LOFO delta F1 |
| 17 | 0.761 | CV max |r| |
| 18 | 0.651 | skewness |rho| |
| 18 | 0.940 | skewness d |
| 18 | +0.010 | skewness LOFO delta F1 |
| 18 | 0.780 | skewness max |r| |
| 19 | 0.635 | kurtosis |rho| |
| 19 | 0.769 | kurtosis d |
| 19 | -0.003 | kurtosis LOFO delta F1 |
| 19 | 0.650 | kurtosis max |r| |
| 24 | 0.63 | Minimum |rho| across candidates |
| 24 | 0.77 | Minimum d across candidates |
| 25 | 0.96 | median-entropy_mean correlation |
| 25 | 0.94 | p90-entropy_mean correlation |
| 25 | 0.91 | IQR-entropy_std correlation |
| 26 | 0.733 | 6-feature baseline LOGO F1 |
| 26 | 0.722 | 12-feature LOGO F1 (with candidates added) |
| 27 | +0.010 | LOFO improvement from removing skewness |
| 27 | +0.008 | LOFO improvement from removing median |
| 27 | +0.007 | LOFO improvement from removing IQR |

---

### appendix_lofo.tex

| Line | Value | Measure |
|------|-------|---------|
| 1 | 0.789 | Full 7-feature ensemble F1 (6-gen LOGO baseline) |
| 12 | 0.774 | F1 without entropy_max |
| 12 | -1.50 pp | Delta vs full |
| 13 | 0.783 | F1 without entropy_mean |
| 13 | -0.63 pp | Delta vs full |
| 14 | 0.784 | F1 without ttr |
| 14 | -0.55 pp | Delta vs full |
| 15 | 0.785 | F1 without hapax_ratio |
| 15 | -0.42 pp | Delta vs full |
| 16 | 0.786 | F1 without tail_decay |
| 16 | -0.33 pp | Delta vs full |
| 17 | 0.786 | F1 without entropy_std |
| 17 | -0.29 pp | Delta vs full |
| 18 | 0.789 | F1 without entropy_min |
| 18 | +0.01 pp | Delta vs full |
| 20 | 0.789 | Full (7 features) F1 |
| 26 | -1.5 pp | entropy_max degradation when removed |
| 26 | 0.063 | entropy_max split frequency (permutation importance rank 4) |
| 27 | +0.01 pp | entropy_min delta (fully redundant) |
| 27 | 0.015 | entropy_min permutation importance |
| 30 | 37,058 | 8-gen dataset size |
| 30 | -0.019 | entropy_max delta (8-gen LOFO) |
| 30 | -0.012 | entropy_mean delta (8-gen LOFO) |
| 33 | 21 | Number of 2-feature subsets (C(7,2)) |
| 34 | 0.68 | Best 2-feature subset F1 ({ent_mean, ent_max}) |
| 34 | 88% | Fraction of full ensemble performance captured |
| 34 | 0.771 | Full ensemble F1 (8-gen) |
| 35 | +9.1 pp | Gain from adding remaining 5 features |
| 46 | 0.771 | Full (7 features) 3-class F1 (8-gen) |
| 48 | 0.752 | F1 minus entropy_max (8-gen) |
| 48 | -0.019 | Delta |
| 49 | 0.759 | F1 minus entropy_mean (8-gen) |
| 49 | -0.012 | Delta |
| 50 | 0.763 | F1 minus entropy_std (8-gen) |
| 50 | -0.007 | Delta |
| 51 | 0.764 | F1 minus ttr (8-gen) |
| 51 | -0.007 | Delta |
| 52 | 0.765 | F1 minus hapax_ratio (8-gen) |
| 52 | -0.005 | Delta |
| 53 | 0.766 | F1 minus entropy_min (8-gen) |
| 53 | -0.005 | Delta |
| 54 | 0.767 | F1 minus tail_decay (8-gen) |
| 54 | -0.004 | Delta |

---

### appendix_variance_decomposition.tex

| Line | Value | Measure |
|------|-------|---------|
| 8 | 37,058 | N for 2-way ANOVA |
| 8 | 0.34--0.37 | eta-squared depth for location features |
| 8 | <0.01 | eta-squared depth for shape features |
| 8 | <10^-6 | p-values for all effects |
| 16 | 0.341 | eta-sq depth for entropy mean |
| 16 | 0.022 | eta-sq gen for entropy mean |
| 16 | 0.010 | eta-sq interaction for entropy mean |
| 16 | 0.627 | eta-sq residual for entropy mean |
| 17 | 0.370 | eta-sq depth for TTR |
| 17 | 0.024 | eta-sq gen for TTR |
| 17 | 0.007 | eta-sq interaction for TTR |
| 17 | 0.599 | eta-sq residual for TTR |
| 18 | 0.364 | eta-sq depth for hapax ratio |
| 18 | 0.017 | eta-sq gen for hapax |
| 18 | 0.006 | eta-sq interaction for hapax |
| 18 | 0.612 | eta-sq residual for hapax |
| 21 | 0.007 | eta-sq depth for ent max |
| 21 | 0.002 | eta-sq gen for ent max |
| 21 | 0.003 | eta-sq interaction for ent max |
| 21 | 0.988 | eta-sq residual for ent max |
| 22 | 0.002 | eta-sq depth for ent min |
| 22 | 0.001 | eta-sq gen for ent min |
| 22 | 0.001 | eta-sq interaction for ent min |
| 22 | 0.996 | eta-sq residual for ent min |
| 23 | 0.002 | eta-sq depth for tail decay |
| 23 | 0.023 | eta-sq gen for tail decay |
| 23 | 0.009 | eta-sq interaction for tail decay |
| 23 | 0.967 | eta-sq residual for tail decay |
| 26 | 0.054 | eta-sq depth for ent std |
| 26 | 0.020 | eta-sq gen for ent std |
| 26 | 0.011 | eta-sq interaction for ent std |
| 26 | 0.915 | eta-sq residual for ent std |
| 33 | 34--37% | Depth variance for location features |
| 33 | <1% | Depth variance for shape features |
| 33 | >48x | Ratio (depth explained variance location/shape) |
| 34 | 0.02 | eta-sq gen (comparable across groups) |
| 35 | <0.011 | Maximum interaction term |
| 37 | 0.40 | Convergence rate lambda (location features, mean) |
| 37 | 0.26 | Lambda std |
| 37 | 0.99 | R-squared for location features |
| 37 | 5.3 | Lambda for shape features |
| 37 | 8.4 | Lambda std for shape features |
| 37 | 0.73 | R-squared for shape features |

---

### appendix_length.tex

| Line | Value | Measure |
|------|-------|---------|
| 10 | <0.14 | Max |rho| between word count and depth (all 8 generators) |
| 14 | 0.38 | tail_decay length-feature |rho| |
| 14 | 0.30 | hapax_ratio length-feature |rho| |
| 14 | 0.29 | TTR length-feature |rho| |
| 15 | 0.09 | entropy_mean length-feature |rho| |
| 15 | 0.18 | entropy_std length-feature |rho| |
| 20 | 0.724 | Length-matched binary F1 |
| 20 | 0.770 | Unmatched binary F1 |
| 20 | -0.046 | Delta from length matching |
| 22 | 0.767 | Random-subsample control F1 (equal N, no length matching) |
| 22 | 0.046 | Confirmed deconfounding effect |
| 25 | 6% | Fraction of performance attributable to length (0.046/0.770) |
| 25 | 0.046 | Length confound delta |
| 25 | 0.770 | Total performance |
| 26 | 0.724 | Length-matched F1 |

---

### appendix_error_analysis.tex

| Line | Value | Measure |
|------|-------|---------|
| 1 | 29,095 | Test samples for binary LOGO |
| 1 | 28.1% | Overall error rate |
| 4 | 86.2% | Fraction of errors that are FN |
| 4 | 13.8% | Fraction of errors that are FP |
| 6 | 45.0% | Mistral-7B error rate (highest) |
| 6 | 18.2% | Pythia-1B error rate (lowest) |
| 14 | 3560 | Pythia-1B N |
| 14 | 188 | Pythia-1B FP |
| 14 | 460 | Pythia-1B FN |
| 14 | 18.2 | Pythia-1B error % |
| 15 | 3614 | Pythia-2.8B N |
| 15 | 129 | Pythia-2.8B FP |
| 15 | 737 | Pythia-2.8B FN |
| 15 | 24.0 | Pythia-2.8B error % |
| 16 | 3718 | OLMo N |
| 16 | 154 | OLMo FP |
| 16 | 900 | OLMo FN |
| 16 | 28.3 | OLMo error % |
| 17 | 3542 | Qwen3-0.6B N |
| 17 | 234 | Qwen3-0.6B FP |
| 17 | 511 | Qwen3-0.6B FN |
| 17 | 21.0 | Qwen3-0.6B error % |
| 18 | 3621 | Qwen3-1.7B N |
| 18 | 175 | Qwen3-1.7B FP |
| 18 | 639 | Qwen3-1.7B FN |
| 18 | 22.5 | Qwen3-1.7B error % |
| 19 | 3502 | Qwen3-8B N |
| 19 | 93 | Qwen3-8B FP |
| 19 | 1104 | Qwen3-8B FN |
| 19 | 34.2 | Qwen3-8B error % |
| 20 | 3685 | Llama N |
| 20 | 82 | Llama FP |
| 20 | 1030 | Llama FN |
| 20 | 30.2 | Llama error % |
| 21 | 3853 | Mistral N |
| 21 | 75 | Mistral FP |
| 21 | 1659 | Mistral FN |
| 21 | 45.0 | Mistral error % |
| 23 | 29095 | Overall N |
| 23 | 1130 | Overall FP |
| 23 | 7040 | Overall FN |
| 23 | 28.1 | Overall error % |
| 32 | 48.4% | Depth-2 error rate |
| 32 | 29.2% | Depth-3 error rate |
| 32 | 20.3% | Depth-4 error rate |
| 40 | 7896 | Depth-1 N |
| 40 | 1130 | Depth-1 errors |
| 40 | 14.3 | Depth-1 error rate % |
| 41 | 7512 | Depth-2 N |
| 41 | 3637 | Depth-2 errors |
| 41 | 48.4 | Depth-2 error rate % |
| 42 | 7032 | Depth-3 N |
| 42 | 2051 | Depth-3 errors |
| 42 | 29.2 | Depth-3 error rate % |
| 43 | 6655 | Depth-4 N |
| 43 | 1352 | Depth-4 errors |
| 43 | 20.3 | Depth-4 error rate % |
| 53 | 2.26 | Misclassified mean entropy (H_bar) |
| 53 | 1.57 | Correctly classified mean entropy |
| 53 | <10^-300 | p-value for entropy difference |
| 53 | 0.464 | Misclassified TTR |
| 53 | 0.302 | Correctly classified TTR |
| 65 | 1.5700 | Correct H_bar |
| 65 | 2.2618 | Incorrect H_bar |
| 65 | +0.6918 | Delta H_bar |
| 65 | <10^-300 | p-value |
| 66 | 1.6227 | Correct H_std |
| 66 | 1.7413 | Incorrect H_std |
| 66 | +0.1186 | Delta H_std |
| 66 | <10^-300 | p-value |
| 67 | 0.0281 | Correct H_min |
| 67 | 0.0330 | Incorrect H_min |
| 67 | +0.0049 | Delta H_min |
| 67 | 1.0e-294 | p-value |
| 68 | 7.5255 | Correct H_max |
| 68 | 7.5251 | Incorrect H_max |
| 68 | -0.0004 | Delta H_max |
| 69 | -0.0023 | Correct tail decay |
| 69 | -0.0023 | Incorrect tail decay |
| 69 | +0.0000 | Delta tail decay |
| 70 | 0.3024 | Correct TTR |
| 70 | 0.4635 | Incorrect TTR |
| 70 | +0.1612 | Delta TTR |
| 70 | <10^-300 | p-value |
| 71 | 0.1760 | Correct Hapax |
| 71 | 0.3131 | Incorrect Hapax |
| 71 | +0.1371 | Delta Hapax |
| 71 | <10^-300 | p-value |
| 77 | >99% | Gen-0 classification accuracy |
| 77 | 30.2% | Gen-2+ predicted as gen-1 |
| 89 | 99.2 | True gen-0 → pred gen-0 % |
| 89 | 0.8 | True gen-0 → pred gen-1 % |
| 89 | 0.1 | True gen-0 → pred gen-2+ % |
| 90 | 7.3 | True gen-1 → pred gen-0 % |
| 90 | 78.4 | True gen-1 → pred gen-1 % |
| 90 | 14.3 | True gen-1 → pred gen-2+ % |
| 91 | 3.0 | True gen-2+ → pred gen-0 % |
| 91 | 30.2 | True gen-2+ → pred gen-1 % |
| 91 | 66.7 | True gen-2+ → pred gen-2+ % |

---

### appendix_nll_distribution.tex

| Line | Value | Measure |
|------|-------|---------|
| 10 | 25 | Texts per depth per generator |
| 10 | ~236k | Total tokens |
| 11 | 1.64 | Median NLL at gen-0 (nats) |
| 11 | 0.02 | Median NLL at gen-4 (nats) |

---

### appendix_9gen_scale.tex

| Line | Value | Measure |
|------|-------|---------|
| 4 | 0.770 | 8-gen avg 3-class F1 (class-balanced) |
| 4 | 0.701 | 8-gen avg binary F1 (class-balanced) |
| 4 | 0.762 | 8-gen avg 3-class F1 (unfiltered, Table logo-results) |
| 4 | 0.694 | 8-gen avg binary F1 (unfiltered) |
| 17 | 0.857 | Pythia-1B 3-class F1 (9-gen) |
| 17 | [0.848, 0.866] | 95% CI |
| 17 | 0.785 | Pythia-1B binary F1 |
| 18 | 0.819 | Qwen3-0.6B 3-class F1 |
| 18 | [0.807, 0.830] | 95% CI |
| 18 | 0.743 | Qwen3-0.6B binary F1 |
| 19 | 0.812 | Pythia-2.8B 3-class F1 |
| 19 | [0.801, 0.822] | 95% CI |
| 19 | 0.728 | Pythia-2.8B binary F1 |
| 20 | 0.811 | Qwen3-1.7B 3-class F1 |
| 20 | [0.800, 0.823] | 95% CI |
| 20 | 0.746 | Qwen3-1.7B binary F1 |
| 21 | 0.773 | OLMo-2-1B 3-class F1 |
| 21 | [0.762, 0.784] | 95% CI |
| 21 | 0.692 | OLMo-2-1B binary F1 |
| 22 | 0.759 | Llama-3.2-3B 3-class F1 |
| 22 | [0.748, 0.770] | 95% CI |
| 22 | 0.680 | Llama binary F1 |
| 23 | 0.696 | Qwen3-8B 3-class F1 |
| 23 | [0.683, 0.709] | 95% CI |
| 23 | 0.647 | Qwen3-8B binary F1 |
| 23 | [0.631, 0.664] | Binary 95% CI |
| 24 | 0.628 | Gemma-2-2B 3-class F1 |
| 24 | [0.622, 0.634] | 95% CI |
| 24 | 0.440 | Gemma-2-2B binary F1 |
| 24 | [0.432, 0.449] | Binary 95% CI |
| 25 | 0.605 | Mistral-7B 3-class F1 |
| 25 | [0.593, 0.617] | 95% CI |
| 25 | 0.534 | Mistral binary F1 |
| 27 | 0.751 | 9-gen average 3-class F1 |
| 27 | 0.666 | 9-gen average binary F1 |
| 28 | 0.770 | 8-gen average 3-class F1 |
| 28 | 0.701 | 8-gen average binary F1 |
| 41 | -0.019 | Delta mean 3-class F1 (9-gen minus 8-gen) |
| 42 | [-0.011, +0.002] | Per-generator F1 shift range upon Gemma inclusion |
| 45 | 0.628 | Gemma 3-class F1 |
| 45 | 0.440 | Gemma binary F1 |
| 46 | 0.991 | Gemma gen-0 F1 |
| 46 | 0.856 | Gemma gen-2+ F1 |
| 46 | 0.036 | Gemma gen-1 F1 |
| 48 | 4,957 | Gemma partition instances |
| 48 | ~990 | Instances per depth level |
| 50 | 0.011 | Maximum per-gen F1 shift upon Gemma inclusion |
| 53 | 0.81 | F1 threshold for sub-1.7B generators |
| 53 | 0.773 | OLMo-2-1B F1 (exception) |
| 53 | 0.63--0.81 | Mid-range model F1 cluster |
| 53 | 0.60--0.70 | Large model F1 range |
| 54 | 0.696 | Qwen3-8B 3-class F1 (9-gen) |
| 54 | 0.701 | Qwen3-8B class-balanced 8-gen F1 |
| 57 | 14.7B | Qwen3-14B parameter count |
| 57 | 0.78--1.12 | Drifting features Cohen's d range at 14B |
| 57 | 21--35% | Spearman |rho| attenuation |
| 57 | 0.39 | Entropy mean |rho| at 14B |
| 57 | 0.40 | Drifting threshold |
| 57 | 0.78 | Entropy mean d at 14B |

---

### appendix_ddr_causality.tex

| Line | Value | Measure |
|------|-------|---------|
| 4 | 0.771 | Baseline F1 for permutation importance |
| 5 | 0.187 | Average F1 drop for drifting features |
| 5 | 5.5x | Ratio drifting / near-stationary importance |
| 5 | 0.034 | Average F1 drop for near-stationary features |
| 17 | 0.235 | hapax_ratio permutation F1 drop (rank 1) |
| 18 | 0.170 | entropy_mean permutation F1 drop (rank 2) |
| 19 | 0.156 | ttr permutation F1 drop (rank 3) |
| 20 | 0.070 | entropy_max permutation F1 drop (rank 4) |
| 21 | 0.057 | entropy_std permutation F1 drop (rank 5) |
| 22 | 0.019 | entropy_min permutation F1 drop (rank 6) |
| 23 | 0.014 | tail_decay permutation F1 drop (rank 7) |
| 29 | 29,095 | N for Granger causality |
| 43 | <0.001 | Granger p for entropy_std |
| 43 | 0.031 | Granger delta R-squared for entropy_std |
| 44 | <0.001 | Granger p for hapax_ratio |
| 45 | <0.001 | Granger p for ttr |
| 46 | <0.001 | Granger p for entropy_mean |
| 47 | <0.001 | Granger p for entropy_max |
| 48 | <0.001 | Granger p for tail_decay |
| 49 | 0.375 | Granger p for entropy_min (not significant) |
| 58 | 0.019 | entropy_min F1 drop |
| 58 | 0.375 | entropy_min Granger p |
| 60 | 0.070 | entropy_max F1 drop |
| 60 | -2.0 pp | entropy_max counterfactual intervention |
| 62 | >0.4 | Mistral hapax/ttr non-significant Granger p |
| 62 | 0.605 | Mistral lowest LOGO F1 |

---

### appendix_convergence.tex

| Line | Value | Measure |
|------|-------|---------|
| 2 | >2 | Lexical diversity features |d| by depth 2 |
| 3 | <0.25 | Near-stationary features max |d| across all depths |

---

### appendix_instruct.tex

| Line | Value | Measure |
|------|-------|---------|
| 18 | 0.754 | OLMo-2-1B base 3-class F1 |
| 18 | 0.575 | OLMo-2-1B instruct 3-class F1 |
| 18 | 0.845 | OLMo base binary F1 |
| 18 | 0.813 | OLMo instruct binary F1 |
| 18 | -0.64 | OLMo base rho(ent mean) |
| 18 | +0.48 | OLMo instruct rho(ent mean) |
| 18 | 6/7 | OLMo features with reversed rho |
| 19 | 0.769 | Qwen3-1.7B base 3-class F1 |
| 19 | 0.732 | Qwen3-1.7B instruct 3-class F1 |
| 19 | 0.861 | Qwen3-1.7B base binary F1 |
| 19 | 0.875 | Qwen3-1.7B instruct binary F1 |
| 19 | -0.60 | Qwen3-1.7B base rho |
| 19 | +0.48 | Qwen3-1.7B instruct rho |
| 19 | 6/7 | Qwen features reversed |
| 20 | 0.742 | Llama-3.2-3B base 3-class F1 |
| 20 | 0.544 | Llama instruct 3-class F1 |
| 20 | 0.849 | Llama base binary F1 |
| 20 | 0.838 | Llama instruct binary F1 |
| 20 | -0.63 | Llama base rho |
| 20 | +0.23 | Llama instruct rho |
| 20 | 3/7 | Llama features reversed |
| 25 | 3.7--19.9 pp | 3-class F1 degradation range |
| 25 | 3.2 pp | Max binary F1 change |
| 27 | -0.60 to -0.64 | Base rho range |
| 27 | +0.23 to +0.48 | Instruct rho range |
| 42 | 0.321 | OLMo base→instruct binary F1 |
| 42 | 0.590 | OLMo retrained binary F1 |
| 42 | +0.269 | OLMo retraining delta |
| 43 | 0.500 | Qwen3-1.7B base→instruct binary F1 |
| 43 | 0.660 | Qwen3-1.7B retrained binary F1 |
| 43 | +0.160 | Qwen3-1.7B retraining delta |
| 44 | 0.532 | Qwen3-0.6B base→instruct binary F1 |
| 44 | 0.600 | Qwen3-0.6B retrained binary F1 |
| 44 | +0.068 | Qwen3-0.6B retraining delta |
| 49 | +6.8--26.9 pp | Retraining recovery range |
| 49 | 0.590--0.660 | Retrained F1 range |
| 49 | 0.69--0.72 | Base-model F1 level |
| 52 | 0.372 | Instruct k=2 silhouette |
| 52 | 0.660 | Base k=2 silhouette |
| 53 | 0.006 | OLMo-Instruct TTR |rho| |
| 53 | 0.025 | OLMo-Instruct hapax |rho| |
| 53 | 0.48--0.53 | Qwen instruct |rho| range |
| 54 | 0.490 | base→instruct binary F1 cross-condition |
| 54 | 0.454 | instruct→base binary F1 cross-condition |
| 54 | -0.036 | Asymmetry |
| 67 | 0.51 | Qwen instruct ent max d (old reference) |
| 67 | 0.08 | Qwen instruct ent max d (instruct reference) |
| 67 | 1.07 | Qwen instruct ent std d (old reference) |
| 67 | 1.51 | Qwen instruct ent std d (instruct reference) |
| 67 | 1.33 | OLMo instruct ent mean d (old reference) |
| 67 | 0.02 | OLMo instruct ent mean d (instruct reference) |
| 67 | 0.60 | OLMo instruct tail decay d (old reference) |
| 67 | 0.06 | OLMo instruct tail decay d (instruct reference) |
| 85 | 0.575 | OLMo-Inst XGB 3-class F1 |
| 85 | 0.888 | OLMo-Inst QLoRA 3-class F1 |
| 85 | 0.007 | OLMo-Inst QLoRA std |
| 85 | +31.3 pp | OLMo XGB-to-QLoRA gap |
| 85 | 4,429 | OLMo-Inst N |
| 86 | 0.732 | Qwen3-1.7B-Inst XGB 3-class F1 |
| 86 | 0.907 | Qwen3-1.7B-Inst QLoRA 3-class F1 |
| 86 | 0.008 | Qwen3-1.7B-Inst QLoRA std |
| 86 | +17.5 pp | Qwen XGB-to-QLoRA gap |
| 86 | 4,963 | Qwen3-1.7B-Inst N |
| 88 | 0.859 | OLMo base QLoRA F1 |
| 88 | 0.004 | OLMo base QLoRA std |
| 88 | 2,379 | OLMo base N |
| 89 | 0.904 | Qwen3-1.7B base QLoRA F1 |
| 89 | 0.009 | Qwen3-1.7B base QLoRA std |
| 89 | 2,291 | Qwen3-1.7B base N |
| 94 | +17.5 to +31.3 pp | XGBoost-to-QLoRA instruct gap range |

---

### appendix_seed_control.tex

| Line | Value | Measure |
|------|-------|---------|
| 6 | 500 | Seeds per generator (disjoint pools) |
| 13 | 0.694 | Shared-seed LOGO baseline binary F1 |
| 21 | 0.695 | Pythia→OLMo independent-seed binary F1 |
| 21 | [0.673, 0.717] | 95% CI |
| 22 | 0.666 | OLMo→Pythia independent-seed binary F1 |
| 22 | [0.643, 0.689] | 95% CI |
| 24 | 0.680 | Independent-seed average binary F1 |
| 25 | 0.694 | Shared-seed LOGO reference |
| 25 | [0.688, 0.700] | 95% CI |
| 30 | -1.4 pp | Gap between independent and shared seed |
| 30 | 0.66 | Minimum direction F1 |
| 34 | 0.622 | Cosine similarity step 0→1 |
| 34 | 0.683 | Cosine similarity step 1→2 |
| 34 | 0.801 | Cosine similarity step 2→3 |
| 34 | 0.859 | Cosine similarity step 3→4 |
| 36 | 0.717 | Continuation prompt similarity baseline |
| 36 | 0.809 | Elaboration prompt similarity baseline |
| 36 | 0.808 | Rewriting prompt similarity baseline |

---

### appendix_transfer.tex

| Line | Value | Measure |
|------|-------|---------|
| 16 | 0.985 | Py-2.8B self-transfer binary F1 |
| 16 | 0.873 | Py-2.8B→Py-1B |
| 16 | 0.823 | Py-2.8B→Qw-0.6B |
| 16 | 0.833 | Py-2.8B→Qw-1.7B |
| 16 | 0.741 | Py-2.8B→Qw-8B |
| 16 | 0.829 | Py-2.8B→OLMo |
| 16 | 0.815 | Py-2.8B→Llama |
| 16 | 0.712 | Py-2.8B→Mistral |
| 17 | 0.834 | Py-1B→Py-2.8B |
| 17 | 0.987 | Py-1B self |
| 17 | 0.828 | Py-1B→Qw-0.6B |
| 17 | 0.821 | Py-1B→Qw-1.7B |
| 17 | 0.704 | Py-1B→Qw-8B |
| 17 | 0.778 | Py-1B→OLMo |
| 17 | 0.764 | Py-1B→Llama |
| 17 | 0.620 | Py-1B→Mistral |
| 18 | 0.786 | Qw-0.6B→Py-2.8B |
| 18 | 0.846 | Qw-0.6B→Py-1B |
| 18 | 0.991 | Qw-0.6B self |
| 18 | 0.851 | Qw-0.6B→Qw-1.7B |
| 18 | 0.786 | Qw-0.6B→Qw-8B |
| 18 | 0.795 | Qw-0.6B→OLMo |
| 18 | 0.760 | Qw-0.6B→Llama |
| 18 | 0.680 | Qw-0.6B→Mistral |
| 19 | 0.794 | Qw-1.7B→Py-2.8B |
| 19 | 0.839 | Qw-1.7B→Py-1B |
| 19 | 0.859 | Qw-1.7B→Qw-0.6B |
| 19 | 0.989 | Qw-1.7B self |
| 19 | 0.790 | Qw-1.7B→Qw-8B |
| 19 | 0.817 | Qw-1.7B→OLMo |
| 19 | 0.798 | Qw-1.7B→Llama |
| 19 | 0.717 | Qw-1.7B→Mistral |
| 20 | 0.811 | Qw-8B→Py-2.8B |
| 20 | 0.836 | Qw-8B→Py-1B |
| 20 | 0.853 | Qw-8B→Qw-0.6B |
| 20 | 0.855 | Qw-8B→Qw-1.7B |
| 20 | 0.984 | Qw-8B self |
| 20 | 0.848 | Qw-8B→OLMo |
| 20 | 0.839 | Qw-8B→Llama |
| 20 | 0.790 | Qw-8B→Mistral |
| 21 | 0.811 | OLMo→Py-2.8B |
| 21 | 0.827 | OLMo→Py-1B |
| 21 | 0.837 | OLMo→Qw-0.6B |
| 21 | 0.852 | OLMo→Qw-1.7B |
| 21 | 0.803 | OLMo→Qw-8B |
| 21 | 0.988 | OLMo self |
| 21 | 0.828 | OLMo→Llama |
| 21 | 0.763 | OLMo→Mistral |
| 22 | 0.856 | Llama→Py-2.8B |
| 22 | 0.860 | Llama→Py-1B |
| 22 | 0.845 | Llama→Qw-0.6B |
| 22 | 0.851 | Llama→Qw-1.7B |
| 22 | 0.798 | Llama→Qw-8B |
| 22 | 0.851 | Llama→OLMo |
| 22 | 0.987 | Llama self |
| 22 | 0.787 | Llama→Mistral |
| 23 | 0.834 | Mistral→Py-2.8B |
| 23 | 0.837 | Mistral→Py-1B |
| 23 | 0.837 | Mistral→Qw-0.6B |
| 23 | 0.845 | Mistral→Qw-1.7B |
| 23 | 0.817 | Mistral→Qw-8B |
| 23 | 0.849 | Mistral→OLMo |
| 23 | 0.851 | Mistral→Llama |
| 23 | 0.969 | Mistral self |
| 28 | 56 | Off-diagonal transfer pairs |
| 28 | 0.810 | Mean off-diagonal F1 |
| 28 | [0.796, 0.822] | 95% bootstrap CI |
| 28 | 46.58 | One-sample t-statistic |
| 28 | <10^-10 | p-value |
| 29 | 0.87 | Py-2.8B→Py-1B (strongest within-family) |
| 29 | 0.62 | Py-1B→Mistral (weakest transfer) |

---

### appendix_tost.tex

| Line | Value | Measure |
|------|-------|---------|
| 6 | 0.20 | Equivalence bound (|d|) |
| 7 | 0.20 | Cohen's small effect SESOI |
| 8 | 1.5 pp | Max LOFO change for near-stationary features |
| 9 | 0.15, 0.20, 0.25 | Sensitivity analysis epsilon values |
| 9 | 1,000 | Bootstrap iterations |
| 9 | 100% | Bootstrap rejection stability for near-stationary features |
| 9 | 0.10--0.75 | Epsilon invariance range |
| 19 | 0.21--0.25 | Pythia d range for H_max (exceeding epsilon) |
| 20 | 0.23 | Entropy std minimum d (Mistral) |
| 20 | 1.40 | Entropy mean max d (Pythia-1B) |
| 39 | 1.20 | Py-2.8B H_mean d |
| 39 | 0.77 | Py-2.8B TTR d |
| 39 | 0.67 | Py-2.8B hapax d |
| 39 | 0.39 | Py-2.8B H_std d |
| 39 | 0.25 | Py-2.8B H_max d |
| 39 | 0.07 | Py-2.8B tail d (equiv) |
| 39 | 0.03 | Py-2.8B H_min d (equiv) |
| 40 | 1.40 | Py-1B H_mean d |
| 40 | 0.80 | Py-1B TTR d |
| 40 | 0.65 | Py-1B hapax d |
| 40 | 0.53 | Py-1B H_std d |
| 40 | 0.21 | Py-1B H_max d |
| 40 | 0.08 | Py-1B tail d (equiv) |
| 40 | 0.02 | Py-1B H_min d (equiv) |
| 41 | 1.12 | Qw-1.7B H_mean d |
| 41 | 0.93 | Qw-1.7B TTR d |
| 41 | 0.83 | Qw-1.7B hapax d |
| 41 | 0.52 | Qw-1.7B H_std d |
| 41 | 0.02 | Qw-1.7B H_max d (equiv) |
| 41 | 0.09 | Qw-1.7B tail d (equiv) |
| 41 | 0.05 | Qw-1.7B H_min d (equiv) |
| 42 | 1.15 | Llama H_mean d |
| 42 | 1.04 | Llama TTR d |
| 42 | 0.98 | Llama hapax d |
| 42 | 0.50 | Llama H_std d |
| 42 | 0.01 | Llama H_max d (equiv) |
| 42 | 0.19 | Llama tail d |
| 42 | 0.01 | Llama H_min d (equiv) |
| 43 | 1.19 | OLMo H_mean d |
| 43 | 1.08 | OLMo TTR d |
| 43 | 1.00 | OLMo hapax d |
| 43 | 0.61 | OLMo H_std d |
| 43 | 0.06 | OLMo H_max d (equiv) |
| 43 | 0.22 | OLMo tail d |
| 43 | 0.07 | OLMo H_min d (equiv) |
| 44 | 0.86 | Qw-8B H_mean d |
| 44 | 0.71 | Qw-8B TTR d |
| 44 | 0.66 | Qw-8B hapax d |
| 44 | 0.37 | Qw-8B H_std d |
| 44 | 0.04 | Qw-8B H_max d (equiv) |
| 44 | 0.15 | Qw-8B tail d |
| 44 | 0.01 | Qw-8B H_min d (equiv) |
| 45 | 0.92 | Qw-0.6B H_mean d |
| 45 | 0.63 | Qw-0.6B TTR d |
| 45 | 0.50 | Qw-0.6B hapax d |
| 45 | 0.56 | Qw-0.6B H_std d |
| 45 | 0.01 | Qw-0.6B H_max d (equiv) |
| 45 | 0.08 | Qw-0.6B tail d (equiv) |
| 45 | 0.10 | Qw-0.6B H_min d (equiv) |
| 46 | 0.89 | Mistral H_mean d |
| 46 | 0.82 | Mistral TTR d |
| 46 | 0.82 | Mistral hapax d |
| 46 | 0.23 | Mistral H_std d |
| 46 | 0.00 | Mistral H_max d (equiv) |
| 46 | 0.16 | Mistral tail d |
| 46 | 0.04 | Mistral H_min d (equiv) |
| 48 | 0/8 | H_mean equiv count |
| 48 | 0/8 | TTR equiv count |
| 48 | 0/8 | hapax equiv count |
| 48 | 0/8 | H_std equiv count |
| 48 | 6/8 | H_max equiv count |
| 48 | 4/8 | tail equiv count |
| 48 | 8/8 | H_min equiv count |

---

### appendix_tost_bootstrap.tex

| Line | Value | Measure |
|------|-------|---------|
| 4 | 1,000 | Bootstrap iterations |
| 4 | 42 | Base seed |
| 4 | 0.20 | Equivalence margin |
| 4 | 0.05 | TOST alpha |
| 12 | 100% (1000/1000) | entropy_max rejection rate |
| 12 | 0.062 | entropy_max median d |
| 12 | [0.037, 0.088] | entropy_max d 95% CI |
| 13 | 100% (1000/1000) | entropy_min rejection rate |
| 13 | -0.016 | entropy_min median d |
| 13 | [-0.042, 0.011] | entropy_min d 95% CI |
| 14 | 100% (1000/1000) | tail_decay rejection rate |
| 14 | 0.088 | tail_decay median d |
| 14 | [0.065, 0.111] | tail_decay d 95% CI |
| 16 | 0% (0/1000) | entropy_std rejection rate |
| 16 | 0.458 | entropy_std median d |
| 16 | [0.435, 0.479] | entropy_std d 95% CI |
| 25 | 100% | Rejection rate for all near-stationary features |
| 25 | +/-0.20 | Equivalence margin |
| 26 | 0% | entropy_std rejection rate |
| 26 | [0.435, 0.479] | entropy_std CI outside margin |

---

### appendix_domain.tex

| Line | Value | Measure |
|------|-------|---------|
| 3 | 200 | Seeds per domain |
| 3 | 3 | Depth of chains |
| 3 | 3 | Number of generators |
| 5 | 1.0 | Temperature for cross-domain generation |
| 5 | 1.0 | Top-p for cross-domain generation |
| 5 | 0.7 | Method's reliable temperature limit |
| 16 | 0.754 | Code binary F1 |
| 16 | [0.737, 0.770] | Code 95% CI |
| 16 | 0.634 | Code 3-class F1 |
| 17 | 0.746 | News binary F1 |
| 17 | [0.726, 0.764] | News 95% CI |
| 17 | 0.652 | News 3-class F1 |
| 18 | 0.739 | Academic binary F1 |
| 18 | [0.720, 0.757] | Academic 95% CI |
| 18 | 0.622 | Academic 3-class F1 |
| 23 | 0.73 | Minimum binary F1 across non-Wikipedia domains |
| 28 | 0.7 | Main experiment temperature |
| 28 | 0.9 | Main experiment top-p |
| 28 | +3 to +11 pp | Temperature advantage for cross-domain at t=1.0 |
| 28 | 0.746 | News F1 at t=1.0 |
| 28 | 0.712 | News F1 at t=0.7 |
| 28 | 0.739 | Academic F1 at t=1.0 |
| 28 | 0.628 | Academic F1 at t=0.7 |
| 28 | 0.754 | Code F1 at t=1.0 |
| 28 | 0.687 | Code F1 at t=0.7 |
| 33 | 0.62--0.65 | Cross-domain 3-class F1 range |
| 33 | 0.74--0.75 | Cross-domain binary F1 range |
| 33 | 0.762 | Main experiment 3-class F1 |
| 33 | 0.694 | Main experiment binary F1 |

---

### appendix_finer_depth.tex

| Line | Value | Measure |
|------|-------|---------|
| 13 | 0.484 | OLMo-2-1B 5-class macro F1 |
| 13 | 0.506 | OLMo weighted F1 |
| 13 | 0.524 | OLMo accuracy |
| 14 | 0.543 | Pythia-1B macro F1 |
| 14 | 0.568 | Pythia-1B weighted F1 |
| 14 | 0.575 | Pythia-1B accuracy |
| 15 | 0.523 | Pythia-2.8B macro F1 |
| 15 | 0.540 | Pythia-2.8B weighted F1 |
| 15 | 0.560 | Pythia-2.8B accuracy |
| 16 | 0.513 | Qwen3-0.6B macro F1 |
| 16 | 0.521 | Qwen3-0.6B weighted F1 |
| 16 | 0.546 | Qwen3-0.6B accuracy |
| 17 | 0.510 | Qwen3-1.7B macro F1 |
| 17 | 0.536 | Qwen3-1.7B weighted F1 |
| 17 | 0.548 | Qwen3-1.7B accuracy |
| 18 | 0.434 | Qwen3-8B macro F1 |
| 18 | 0.455 | Qwen3-8B weighted F1 |
| 18 | 0.493 | Qwen3-8B accuracy |
| 20 | 0.501 | Average 5-class macro F1 |
| 20 | 0.038 | Std of 5-class macro F1 |
| 20 | 0.521 | Average weighted F1 |
| 20 | 0.541 | Average accuracy |
| 35 | 0.921 | Gen-0 per-class F1 |
| 35 | 0.634 | Gen-1 per-class F1 |
| 35 | 0.268 | Gen-2 per-class F1 |
| 35 | 0.259 | Gen-3 per-class F1 |
| 35 | 0.423 | Gen-4 per-class F1 |
| 41 | 0.50 | Approximate LOGO macro F1 (5-class) |
| 41 | 0.762 | 3-class baseline from Table logo-results |
| 42 | 0.268 | Gen-2 F1 |
| 42 | 0.259 | Gen-3 F1 |
| 43 | 36.5% | True gen-2 misclassified as gen-1 |
| 43 | 37.8% | True gen-3 predicted as gen-4 |
| 45 | 0.921 | Gen-0 F1 |
| 45 | 0.634 | Gen-1 F1 |
| 46 | 93% | Entropy_std permutation importance increase (5-class vs 3-class) |
| 46 | 400% | Tail_decay importance increase |
| 50 | 0.501 | HistGradientBoosting macro F1 |
| 50 | [0.496, 0.506] | 95% bootstrap CI |
| 50 | 0.476 | Random forest macro F1 |
| 50 | 0.447 | Logistic regression macro F1 |
| 50 | 0.451 | Frank-Hall ordinal macro F1 |
| 51 | 0.501 | XGBoost macro F1 |

---

### appendix_decoding_strategy.tex

| Line | Value | Measure |
|------|-------|---------|
| 3 | 0.9 | Nucleus sampling p |
| 3 | 0.7 | Temperature (tau) |
| 4 | 50 | Top-k value |
| 6 | ~1,000 | Chains per generator-strategy combination |
| 6 | ~5,000 | Texts per generator-strategy combination |
| (Table decoding-shape, lines 25-34) | All Cohen's d values for shape features by generator and strategy - see full table above | Shape feature d values (gen-1 vs gen-2+) |
| 34 | 0.08 | Mean entropy_max d (nucleus) |
| 34 | 0.06 | Mean entropy_max d (greedy) |
| 34 | 0.10 | Mean entropy_max d (top-k) |
| 34 | 0.04 | Mean entropy_min d (nucleus) |
| 34 | 0.04 | Mean entropy_min d (greedy) |
| 34 | 0.04 | Mean entropy_min d (top-k) |
| 34 | 0.13 | Mean tail_decay d (nucleus) |
| 34 | 0.06 | Mean tail_decay d (greedy) |
| 34 | 0.16 | Mean tail_decay d (top-k) |
| (Table decoding-drift, lines 52-61) | All Cohen's d values for drifting features by generator and strategy - see full table above | Drifting feature d values (gen-1 vs gen-2+) |
| 61 | 1.09 | Mean entropy_mean d (nucleus) |
| 61 | 1.16 | Mean entropy_mean d (greedy) |
| 61 | 0.79 | Mean entropy_mean d (top-k) |
| 61 | 0.85 | Mean TTR d (nucleus) |
| 61 | 0.85 | Mean TTR d (greedy) |
| 61 | 0.63 | Mean TTR d (top-k) |
| 61 | 0.76 | Mean hapax d (nucleus) |
| 61 | 0.80 | Mean hapax d (greedy) |
| 61 | 0.59 | Mean hapax d (top-k) |
| 61 | 0.46 | Mean entropy_std d (nucleus) |
| 61 | 0.83 | Mean entropy_std d (greedy) |
| 61 | 0.23 | Mean entropy_std d (top-k) |
| 70 | 0.50 | Drifting threshold |
| 70 | 0.15 | Stationary threshold |
| 75 | 0.05 | Mean shape d (greedy) |
| 75 | 0.14 | Max shape d (greedy) |
| 76 | 0.94 | Mean drifting d (greedy) |
| 78 | 0.21--0.25 | Pythia nucleus entropy_max d |
| 79 | 0.26--0.27 | Pythia top-k entropy_max d |
| 79 | 0.22 | OLMo tail_decay d (both nucleus and top-k) |
| 80 | 0.67 | Mean drifting d (top-k) |
| 80 | 0.90 | Mean drifting d (nucleus) |
| 88 | 0.83 | Entropy_std greedy mean d |
| 88 | 0.46 | Entropy_std nucleus mean d |
| 88 | 0.23 | Entropy_std top-k mean d |

---

### appendix_feature_distributions.tex (DDR Trend Lines / UMAP)

| Line | Value | Measure |
|------|-------|---------|
| 15 | 7,500 | UMAP sample count |
| 15 | 30 | UMAP k-neighbors |
| 15 | 0.3 | UMAP min_dist |

---

### appendix_ai_assistants.tex

No numerical values. Contains only a disclosure statement about AI writing tool usage.

---

### ethics.tex

| Line | Value | Measure |
|------|-------|---------|
| 16 | 4 | Number of NVIDIA RTX 5090 GPUs |
| 16 | 32 GB | GPU memory per card |
| 16 | 62 | Total GPU-hours |

---

### related_work.tex

| Line | Value | Measure |
|------|-------|---------|
| 8 | 0.54--0.71 | Binary F1 range for existing detection scores as depth predictors |
| 13 | ~3 | Distinguishable depth classes (from Markovian analysis) |

---

**Summary totals**: Across all 37 files, there are approximately **900+ distinct numerical values** covering F1 scores, Cohen's d effect sizes, Spearman correlations, p-values, sample counts, confidence intervals, ANOVA eta-squared, perplexity values, TOST equivalence tests, silhouette scores, permutation importances, confusion matrix percentages, error rates, and model/dataset parameters. The most numerically dense files are `appendix_ddr_validation.tex`, `appendix_human_edit.tex`, `appendix_classifier.tex`, `appendix_error_analysis.tex`, `appendix_tost.tex`, and `appendix_transfer.tex`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e860a16-3bc8-4edb-b8c4-48b854e96999",
  "isSidechain": true,
  "agentId": "aa2265d384aeafb01",
  "requestId": "req_011CbPw34PK4uhyyyDuXiXob",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fec754c2-e92e-4c73-95ef-d7f66f006bae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SRqWG95iBLnRXUDdhSWxT1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8663,
      "cache_read_input_tokens": 82636,
      "output_tokens": 31334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8663
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 31334,
          "cache_read_input_tokens": 82636,
          "cache_creation_input_tokens": 8663,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8663,
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
