# Research conversation: In the paper directory at /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/, search 

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 2
- **Tool calls:** 26
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a8040b0d4a0e1337c.jsonl`
- **Structured JSON:** [`af81abb832a8271d8117.json`](../../sessions/af/af81abb832a8271d8117.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

57 recorded events

### User

_source line 1 · 2026-05-25T10:16:08.167Z_

In the paper directory at /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/, search all .tex files for \includegraphics commands to map figure numbers to their source image files. I need to know specifically:
1. Which image file is used for Figure 7 (instruction retention bar chart)
2. Which image file is used for Figure 14 (training loss curves - NTP/GAR/Total Loss)
3. Which image file is used for Figure 23 (Per-turn AR GAR decay on Llama)
4. Which image file is used for Figure 22 (Per-turn AR GAR-ours across Qwen configs)

Also find where Table 22 is defined (the per-turn autoregressive GAR-ours table on Llama).

Additionally, find what page the main text ends on - specifically where Section 7 (Conclusion) ends and Section 8 (Limitations) begins, to understand how much text needs to be cut to fit 8 pages.

Report the exact filenames of included images and the tex file + line numbers where they appear. Be thorough - check all .tex files in the paper/ directory and its subdirectories.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "9633eab9-ebd9-4135-bf35-7866a68c09ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-25T10:16:08.177Z_

```json
{
  "parentUuid": "9633eab9-ebd9-4135-bf35-7866a68c09ff",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
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
  "uuid": "36acf59b-009e-43e3-92aa-076546508fcb",
  "timestamp": "2026-05-25T10:16:08.177Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

---

### Assistant

_source line 3 · 2026-05-25T10:16:11.326Z_



I'll search all .tex files in the paper directory for `\includegraphics` commands and the specific figures/tables requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36acf59b-009e-43e3-92aa-076546508fcb",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7X6WkCo6PrefUep9L4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7af9330-1ac9-43a7-a606-02121a4e9337",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XhdgMzoCPWP2irqij1GA7J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34328,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34328,
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

_source line 4 · 2026-05-25T10:16:12.421Z_

<details open><summary>🔧 Tool call — Glob · `toolu_015KQYoWG98WUkpnpWPqSQZS`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7af9330-1ac9-43a7-a606-02121a4e9337",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7X6WkCo6PrefUep9L4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b62cf97-01af-4f7d-af31-e9b3d734402c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XhdgMzoCPWP2irqij1GA7J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34328,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34328,
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

_source line 5 · 2026-05-25T10:16:12.448Z_

<details><summary>↩ Tool result · `toolu_015KQYoWG98WUkpnpWPqSQZS`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b62cf97-01af-4f7d-af31-e9b3d734402c",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "eefa0ce0-221c-4e99-a11b-fff8500e5f57",
  "sourceToolAssistantUUID": "4b62cf97-01af-4f7d-af31-e9b3d734402c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-25T10:16:13.107Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01MA5t2J3TBzgFuzqbuBT5Fv`</summary>

```json
{
  "pattern": "\\\\includegraphics",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eefa0ce0-221c-4e99-a11b-fff8500e5f57",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7X6WkCo6PrefUep9L4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4906f93c-8201-490f-b3b7-e6911472f25e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XhdgMzoCPWP2irqij1GA7J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34328,
      "cache_read_input_tokens": 0,
      "output_tokens": 291,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 34328
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 291,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 34328,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 34328,
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

_source line 7 · 2026-05-25T10:16:13.130Z_

<details><summary>↩ Tool result · `toolu_01MA5t2J3TBzgFuzqbuBT5Fv`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:25:  \includegraphics[width=\columnwidth]{fig_ss_multiseed.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:38:  \includegraphics[width=\columnwidth]{fig3_gate_shift.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex:18:  \includegraphics[width=\columnwidth]{fig5_attention_steering.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex:33:  \includegraphics[width=\columnwidth]{fig_ss_gap_compression.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex:23:  \includegraphics[width=\columnwidth]{fig4_attention_heatmap.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:80:  \includegraphics[width=\columnwidth]{fig_instruction_retention.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:198:  \includegraphics[width=\columnwidth]{fig_crossmodel.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:240:\includegraphics[width=\columnwidth]{fig_gate_profile_heatmap.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:251:\includegraphics[width=\columnwidth]{fig_gate_profile_crossmodel.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:262:\includegraphics[width=\columnwidth]{fig_ar_gar_perturn.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:273:  \includegraphics[width=\columnwidth]{fig_bootstrap_ci.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:284:\includegraphics[width=\columnwidth]{fig_gate_distribution.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:295:\includegraphics[width=\columnwidth]{fig_training_loss_curves.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:329:  \includegraphics[width=\columnwidth]{fig_steering_standalone.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:376:  \includegraphics[width=\columnwidth]{fig_ss_training_dynamics.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:440:  \includegraphics[width=\columnwidth,height=0.42\textheight,keepaspectratio]{fig2_training_pcgrad.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:457:\includegraphics[width=0.95\textwidth]{fig_gradient_conflict_heatmap.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:495:\includegraphics[width=\columnwidth]{fig_eb_scaling.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:508:\includegraphics[width=\columnwidth]{fig_kl_ar_gar_curves.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:515:\includegraphics[width=\columnwidth]{fig_kl_ar_gar_bar.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:655:  \includegraphics[width=\columnwidth]{fig_perturn_qwen_detail.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:664:  \includegraphics[width=\columnwidth]{fig_perturn_llama_detail.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:693:  \includegraphics[width=\columnwidth]{fig_gar_robustness_grouped.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:712:  \includegraphics[width=\columnwidth]{fig_mmlu_comparison.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:759:  \includegraphics[width=0.75\textwidth]{fig_training_curves_6panel.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:780:  \includegraphics[width=\columnwidth]{fig_steering_perturn_4panel.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex:11:  \includegraphics[width=\textwidth]{fig1_headline.pdf}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4906f93c-8201-490f-b3b7-e6911472f25e",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "590c0f7e-aa2c-4a8b-bd5c-44db99dc1f2e",
  "sourceToolAssistantUUID": "4906f93c-8201-490f-b3b7-e6911472f25e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-25T10:16:16.071Z_

Now let me find the specific figures by reading the relevant sections of the appendix where figures 7, 14, 22, 23 are defined, and also search for Table 22.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "590c0f7e-aa2c-4a8b-bd5c-44db99dc1f2e",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7XTrtTFN97CBnCx8YW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4aa6a415-c674-4d93-9cd6-42706aa03815",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168Rory111Ve4Kh46gjsnFF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3367,
      "cache_read_input_tokens": 34328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3367,
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

_source line 9 · 2026-05-25T10:16:17.006Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Uvmx19xbyqRhuWPiLYUDmq`</summary>

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
  "parentUuid": "4aa6a415-c674-4d93-9cd6-42706aa03815",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7XTrtTFN97CBnCx8YW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "159cb891-be3d-4425-b4d0-32a039fe7e28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168Rory111Ve4Kh46gjsnFF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3367,
      "cache_read_input_tokens": 34328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3367,
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

_source line 10 · 2026-05-25T10:16:17.440Z_

<details><summary>↩ Tool result · reported error · `toolu_01Uvmx19xbyqRhuWPiLYUDmq`</summary>

```text
File content (26109 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "159cb891-be3d-4425-b4d0-32a039fe7e28",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "d36388cc-5771-421b-8162-40111cc2599e",
  "toolUseResult": "Error: File content (26109 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "159cb891-be3d-4425-b4d0-32a039fe7e28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T10:16:18.517Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01PcGMpPr9zDP8gXBv9cE6Pv`</summary>

```json
{
  "pattern": "Figure\\s*(7|14|22|23)\\b|\\\\label\\{fig:|\\\\caption",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d36388cc-5771-421b-8162-40111cc2599e",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7XTrtTFN97CBnCx8YW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4bffbc9d-e4be-45be-a68f-af64240dde77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168Rory111Ve4Kh46gjsnFF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3367,
      "cache_read_input_tokens": 34328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3367,
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

_source line 12 · 2026-05-25T10:16:18.539Z_

<details><summary>↩ Tool result · `toolu_01PcGMpPr9zDP8gXBv9cE6Pv`</summary>

```text
7:\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\dagger$ apply only to ThreadGate and its ablations.}
49:\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}
81:  \caption{Instruction retention by constraint category under $\beta$\,=\,3 steering. Content constraints benefit most (+23.8\,pp); format and count constraints are unaffected.}
82:  \label{fig:ir-bar}
87:\caption{Instruction retention by constraint category ($\beta$\,=\,3 steering on ThreadGate checkpoint). Content constraints benefit most from increased goal attention.}
115:\caption{AR GAR-ours on $N$\,=\,5 ten-turn conversations. The gating advantage observed in Table~\ref{tab:four-way} ($N$\,=\,50, mean 3.6 turns) diminishes with conversation length.}
145:\caption{Consolidated statistical tests. All AR comparisons use $N$\,=\,50 conversations (39 with $\geq$3 turns); gate conditioning uses 28 layers.}
179:\caption{Llama-3.1-8B-Instruct complete results. TF: teacher-forced ($N$\,=\,50); AR: autoregressive ($N$\,=\,20 for Base/TG/LoRA-only, $N$\,=\,50 for SS). Median is more representative due to heavy-tailed AR distributions (SS uses mean only).}
199:  \caption{Cross-architecture validation. (a)~The TF-AR gap persists on Llama-3.1-8B (27$\times$ by median), exceeding Qwen's 8$\times$. (b)~Gate profiles on normalized depth: Qwen dips at early layers, Llama at late layers; architecture-dependent patterns, but both converge toward identity.}
200:  \label{fig:crossmodel}
217:\caption{Cross-model NTP--GAR gradient interaction. Gradients are near-orthogonal on both architectures; NTP magnitude dominates GAR by 15--26$\times$.}
241:\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\times$ 5 conditions) and Llama-3.1-8B (32 layers $\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}
242:\label{fig:gate-heatmap}
252:\caption{Side-by-side gate profiles for Qwen-2.5-7B and Llama-3.1-8B. Qwen dips at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719). Both models learn layer-selective gating but with architecture-dependent patterns.}
253:\label{fig:gate-crossmodel}
263:\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\% (turn 1$\to$10), Llama base drops 90\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}
264:\label{fig:ar-gar-perturn}
274:  \caption{Bootstrap CI distributions for AR GAR-ours (ThreadGate vs.\ LoRA-only, $N$\,=\,50, 10K resamples). Distributions overlap substantially, consistent with the modest effect size ($r$\,=\,0.454).}
275:  \label{fig:bootstrap-ci}
285:\caption{Per-layer gate value distributions for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\sim$0.94--0.96), confirming minimal modulation from the gating mechanism.}
286:\label{fig:gate-distribution}
296:\caption{NTP, GAR, and total loss trajectories. GAR loss collapses to near-zero within the first epoch across all variants, while NTP loss converges normally.}
297:\label{fig:training-loss}
304:\caption{Full attention steering results across evaluation settings.
330:  \caption{Detailed $\beta$-steering trade-off ($N$\,=\,50). GAR-ours (top) increases monotonically with $\beta$; PPL (bottom) remains stable below $\beta$\,=\,3 (9\% cost), then rises sharply. The $\beta$\,=\,3 operating point (circled) achieves 8.7$\times$ GAR recovery while crossing the TF baseline, representing the optimal trade-off.}
331:  \label{fig:steering-standalone}
340:\caption{Per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct. Min values (L1, L5) in bold.}
377:  \caption{Scheduled sampling training dynamics: sampling ratio $\rho$ ramps linearly from 0 to 0.3 (left axis); GAR loss (right axis) shows higher early-epoch variance due to stochastic context mixing.}
378:  \label{fig:ss-dynamics}
385:\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (96\,GB VRAM).}
420:\caption{Qualitative effect of $\beta$-steering on instruction following across conversation turns. System prompt: ``Always respond in exactly three bullet points.'' ThreadGate checkpoint, 4-turn conversation.}
441:  \caption{(a)~Training GAR convergence to target ($\tau$\,=\,0.5). (b)~PCGrad removes gradient conflict but $\mathcal{L}_\text{GAR}$ still collapses, confirming that gradient direction conflict is not the primary cause (\S\ref{subsec:pcgrad}).}
442:  \label{fig:training-pcgrad}
458:\caption{Per-layer cosine similarity between NTP and GAR gradients across training epochs. (a)~Standard training: conflict decreases from 79\% to 68\% of layers as GAR loss vanishes. (b)~PCGrad training: projection reduces conflict more slowly (79\%$\to$71\%) but does not improve AR GAR, ruling out gradient direction conflict as the primary cause (\S\ref{subsec:pcgrad}).}
459:\label{fig:gradient-heatmap}
468:\caption{Training and evaluation data characteristics. All data from UltraChat \citep{ding2023ultrachat}.}
496:\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\sim}$1.3$\times$) is the only variant near parity. Llama gaps ($\sim$27$\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\times$ (3.6 turns) to 31$\times$ (10 turns).}
497:\label{fig:eb-scaling}
509:\caption{Per-turn AR GAR trajectories for six Qwen-2.5-7B configurations (turns 1--5). All models show monotonic decay; Scheduled Sampling retains far higher GAR throughout (0.53$\to$0.39), while the remaining five variants cluster below 0.13 and decay rapidly.}
510:\label{fig:kl_ar_gar_curves}
516:\caption{Mid-turn AR GAR comparison across six training configurations. Ranking from highest to lowest: Scheduled Sampling (0.423), ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), Base (0.019).}
517:\label{fig:kl_ar_gar_bar}
528:\caption{Per-head TF-AR divergence statistics for Base and ThreadGate (Qwen-2.5-7B, 30 conversations). TG trains more concentrated goal attention under TF, but these high-GAR heads shift most under AR ($r$\,=\,0.743).}
553:\caption{Mid-turn GAR under four alternative definitions ($N$\,=\,50 conversations). ThreadGate only improves query-position-specific definitions (last-token, goal-only); Scheduled Sampling raises all four definitions above 0.36.}
577:\caption{MMLU 5-shot accuracy on Qwen-2.5-7B-Instruct. All fine-tuned variants remain within 0.8\,pp of the base LoRA-only checkpoint.}
605:\caption{Cross-scale $\beta$-steering on Qwen-2.5-1.5B ($N$\,=\,50, AR). PPL is median due to catastrophic Base outlier at $\beta$\,=\,3. TG eliminates outliers across all $\beta$ values.}
656:  \caption{Per-turn AR GAR-ours across six Qwen-2.5-7B configurations. Scheduled sampling (green) retains far higher GAR than all other variants, which cluster below 0.13 and decay rapidly.}
657:  \label{fig:perturn-qwen-detail}
665:  \caption{Per-turn AR GAR decay on Llama-3.1-8B. (a)~Three-way comparison (Base, TG, LoRA-only; $N$\,=\,20, 4 turns). (b)~Extended Base decay profile ($N$\,=\,5, 10 turns), showing 90\% decline.}
666:  \label{fig:perturn-llama-detail}
694:  \caption{Mid-turn GAR across four token-position definitions. SS raises all four above 0.36; TG only improves last-token and goal-only.}
695:  \label{fig:gar-robust-grouped}
713:  \caption{MMLU 5-shot accuracy by category across training configurations. All variants remain within 1.2\,pp of the LoRA-only baseline across all categories.}
714:  \label{fig:mmlu-comparison}
760:  \caption{Training loss curves for all five Qwen conditions. NTP loss (left) converges to ${\sim}$0.93 across variants; GAR loss (center) collapses within epoch~1; total loss (right) is NTP-dominated. Training-time behavior is indistinguishable; the failure emerges only at inference.}
761:  \label{fig:training-6panel}
781:  \caption{Per-turn GAR under four $\beta$-steering strengths. At $\beta$\,=\,0, monotonic decay; at $\beta$\,=\,3, partial recovery with residual decay; at $\beta$\,=\,5, sustained high GAR; at $\beta$\,=\,10, saturation with catastrophic PPL.}
782:  \label{fig:steering-4panel}
794:\caption{$\beta$-steering on Llama-3.1-8B SS model ($N$\,=\,50, $T$\,=\,4).}
816:\caption{Scheduled sampling comparison: Qwen-2.5-7B vs.\ Llama-3.1-8B.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bffbc9d-e4be-45be-a68f-af64240dde77",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "34e72a2d-9864-4523-bc45-8099454845b9",
  "sourceToolAssistantUUID": "4bffbc9d-e4be-45be-a68f-af64240dde77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T10:16:19.793Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Tbm8pyi6bGJtLsVKyCsgBg`</summary>

```json
{
  "pattern": "Table\\s*22|\\\\label\\{tab:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34e72a2d-9864-4523-bc45-8099454845b9",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7XTrtTFN97CBnCx8YW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6337ade-303c-4a6e-802e-6b6a779c5eb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168Rory111Ve4Kh46gjsnFF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3367,
      "cache_read_input_tokens": 34328,
      "output_tokens": 464,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3367
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 464,
          "cache_read_input_tokens": 34328,
          "cache_creation_input_tokens": 3367,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3367,
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

_source line 14 · 2026-05-25T10:16:19.806Z_

<details><summary>↩ Tool result · `toolu_01Tbm8pyi6bGJtLsVKyCsgBg`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex:7:\label{tab:four-way}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:8:\label{tab:hyperparams}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:50:\label{tab:loss-iterations}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:88:\label{tab:ir-results}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:116:\label{tab:n5-ar}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:146:\label{tab:stat-tests}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:180:\label{tab:llama-full}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:218:\label{tab:gradient-crossmodel}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:307:\label{tab:steering-full}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:341:\label{tab:gate-profile}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:386:\label{tab:cost}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:421:\label{tab:examples}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:469:\label{tab:data-stats}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:529:\label{tab:kl-perhead}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:554:\label{tab:gar-robust}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:578:\label{tab:mmlu}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:606:\label{tab:1.5b-steering}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:795:\label{tab:llama-ss-steering}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:817:\label{tab:llama-vs-qwen-ss}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6337ade-303c-4a6e-802e-6b6a779c5eb8",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "a1b32261-d677-496e-b891-1d7d0146f273",
  "sourceToolAssistantUUID": "b6337ade-303c-4a6e-802e-6b6a779c5eb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-25T10:16:24.818Z_

Now let me look at the figure/table numbering. Since LaTeX auto-numbers, I need to count the figure and table labels in order. Let me also check the main text figures and find the conclusion/limitations boundary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1b32261-d677-496e-b891-1d7d0146f273",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7XxZJCgCDDCeAqLJvE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a61eaa65-93d8-4876-aae3-4f3e38624990",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SUjxioGKhqNcvhudgbdPYs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4411,
      "cache_read_input_tokens": 37695,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4411,
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

_source line 16 · 2026-05-25T10:16:26.190Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01HAeXhX5LPJsxUVSDsie7Yc`</summary>

```json
{
  "pattern": "\\\\label\\{fig:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a61eaa65-93d8-4876-aae3-4f3e38624990",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7XxZJCgCDDCeAqLJvE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e4480a49-e339-4290-9e01-3d894f944a2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SUjxioGKhqNcvhudgbdPYs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4411,
      "cache_read_input_tokens": 37695,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4411,
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

_source line 17 · 2026-05-25T10:16:26.217Z_

<details><summary>↩ Tool result · `toolu_01HAeXhX5LPJsxUVSDsie7Yc`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:27:  \label{fig:ss-multiseed}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:40:  \label{fig:gate-shift}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex:20:  \label{fig:steering-recovery}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex:35:  \label{fig:ss-gap}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex:25:  \label{fig:attention-heatmap}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:82:  \label{fig:ir-bar}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:200:  \label{fig:crossmodel}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:242:\label{fig:gate-heatmap}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:253:\label{fig:gate-crossmodel}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:264:\label{fig:ar-gar-perturn}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:275:  \label{fig:bootstrap-ci}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:286:\label{fig:gate-distribution}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:297:\label{fig:training-loss}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:331:  \label{fig:steering-standalone}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:378:  \label{fig:ss-dynamics}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:442:  \label{fig:training-pcgrad}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:459:\label{fig:gradient-heatmap}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:497:\label{fig:eb-scaling}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:510:\label{fig:kl_ar_gar_curves}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:517:\label{fig:kl_ar_gar_bar}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:657:  \label{fig:perturn-qwen-detail}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:666:  \label{fig:perturn-llama-detail}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:695:  \label{fig:gar-robust-grouped}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:714:  \label{fig:mmlu-comparison}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:761:  \label{fig:training-6panel}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:782:  \label{fig:steering-4panel}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex:13:  \label{fig:headline}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4480a49-e339-4290-9e01-3d894f944a2d",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "50cd0adc-03f2-4409-9eb9-76357cb17a37",
  "sourceToolAssistantUUID": "e4480a49-e339-4290-9e01-3d894f944a2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-25T10:16:26.697Z_

<details open><summary>🔧 Tool call — Read · `toolu_0159D8gxZRMJUDwzkjfZskjK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50cd0adc-03f2-4409-9eb9-76357cb17a37",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7XxZJCgCDDCeAqLJvE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f4ca2ab-62b7-4570-82d4-5b0af73684d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SUjxioGKhqNcvhudgbdPYs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4411,
      "cache_read_input_tokens": 37695,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4411,
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

_source line 19 · 2026-05-25T10:16:26.706Z_

<details><summary>↩ Tool result · `toolu_0159D8gxZRMJUDwzkjfZskjK`</summary>

```text
1	\enlargethispage{\baselineskip}
2	\section{Conclusion}\label{sec:conclusion}
3	
4	\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\,=\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\beta$-steering recovers GAR above the TF baseline, confirming attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\sim}$1.3$\times$ (Qwen) and ${\sim}$2.9$\times$ (Llama), generalizing across architectures and seeds---the first such transfer to auxiliary attention objectives in multi-turn transformers.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f4ca2ab-62b7-4570-82d4-5b0af73684d0",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "a483ac72-34de-4097-bc11-26297686d230",
  "sourceToolAssistantUUID": "4f4ca2ab-62b7-4570-82d4-5b0af73684d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-25T10:16:27.200Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SXehpuCKchLGmaBLdwMHXA`</summary>

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
  "parentUuid": "a483ac72-34de-4097-bc11-26297686d230",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7XxZJCgCDDCeAqLJvE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62408834-83f7-47ec-ab10-a95dfe4496fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SUjxioGKhqNcvhudgbdPYs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4411,
      "cache_read_input_tokens": 37695,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4411,
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

_source line 21 · 2026-05-25T10:16:27.208Z_

<details><summary>↩ Tool result · `toolu_01SXehpuCKchLGmaBLdwMHXA`</summary>

```text
1	\section{Limitations}\label{sec:limitations}
2	
3	Our findings are demonstrated on two model families (Qwen-2.5-7B and Llama-3.1-8B) and a single dataset (UltraChat, 8K conversations); generalization to other domains (e.g., code, reasoning) is untested. Most configurations use a single seed (scheduled sampling validated on three seeds; \S\ref{subsec:ss}), and quality assessment relies on PPL rather than comprehensive benchmarks \citep{hendrycks2021measuring,lin2022truthfulqa}. LoRA rank is fixed at 16 throughout; higher ranks (32/64) might provide more capacity for the gating mechanism, potentially affecting the magnitude of the TF-AR gap, though unlikely its direction given the consistency across all five configurations. We test only one auxiliary loss family (GAR with MSE target $\tau$\,=\,0.5); head-specific or layer-specific losses may exhibit different sensitivity to exposure bias. We do not experimentally compare against split-softmax \citep{li2024measuring} or Rhea \citep{hong2025rhea}, which operate at inference time; such comparisons would clarify the practical trade-off between training-time and inference-time interventions. The PCGrad exclusion addresses gradient conflict only; magnitude imbalance \citep{chen2018gradnorm} and Nash equilibrium approaches \citep{navon2022nash} remain untested. Use of AI assistants is disclosed in Appendix~\ref{sec:appendix-ai}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62408834-83f7-47ec-ab10-a95dfe4496fe",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "7ede35ad-83cc-4e67-b5a8-8ec337467b6e",
  "sourceToolAssistantUUID": "62408834-83f7-47ec-ab10-a95dfe4496fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-25T10:16:27.569Z_

<details open><summary>🔧 Tool call — Read · `toolu_019KqvxugU9qS137Jb5vmbUm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ede35ad-83cc-4e67-b5a8-8ec337467b6e",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7XxZJCgCDDCeAqLJvE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc08e4a1-e1ca-44a8-9096-053e32366ca2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SUjxioGKhqNcvhudgbdPYs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4411,
      "cache_read_input_tokens": 37695,
      "output_tokens": 439,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4411
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 439,
          "cache_read_input_tokens": 37695,
          "cache_creation_input_tokens": 4411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4411,
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

_source line 23 · 2026-05-25T10:16:27.578Z_

<details><summary>↩ Tool result · `toolu_019KqvxugU9qS137Jb5vmbUm`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{url}
16	\usepackage{subcaption}
17	\usepackage{placeins}
18	\usepackage{alphalph}
19	
20	\graphicspath{{../figures/paper/}{../artifacts/}}
21	
22	\title{Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\input{sections/abstract}
30	\input{sections/introduction}
31	\input{sections/related_work}
32	\input{sections/method}
33	\input{sections/experiments}
34	\input{sections/analysis}
35	\input{sections/discussion}
36	\input{sections/conclusion}
37	\input{sections/limitations}
38	
39	\FloatBarrier
40	\bibliography{references}
41	
42	\appendix
43	\renewcommand{\thesection}{\AlphAlph{\value{section}}}
44	\input{sections/appendix}
45	
46	\end{document}
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc08e4a1-e1ca-44a8-9096-053e32366ca2",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "3837cdc6-9127-4f25-8e54-b1a11783776d",
  "sourceToolAssistantUUID": "fc08e4a1-e1ca-44a8-9096-053e32366ca2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-25T10:16:31.908Z_

Now let me also look at the introduction.tex for the headline figure (Figure 1), and read the key appendix sections around the per-turn tables to find Table 22. Let me also look for tables in order to count them.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3837cdc6-9127-4f25-8e54-b1a11783776d",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7YXhr3Pb55FY3gRGVd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "163ced6d-5dd9-4856-934c-a18813448672",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WQzMGRdK7xuURGta2AJim2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3090,
      "cache_read_input_tokens": 42106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3090,
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

_source line 25 · 2026-05-25T10:16:32.872Z_

<details open><summary>🔧 Tool call — Grep · `toolu_016NdT3pK2KYfkp5mXnwWKAA`</summary>

```json
{
  "pattern": "\\\\label\\{tab:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "163ced6d-5dd9-4856-934c-a18813448672",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7YXhr3Pb55FY3gRGVd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ffb64c5-f24a-4a8c-88ad-34e8f6676843",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WQzMGRdK7xuURGta2AJim2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3090,
      "cache_read_input_tokens": 42106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3090,
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

_source line 26 · 2026-05-25T10:16:32.895Z_

<details><summary>↩ Tool result · `toolu_016NdT3pK2KYfkp5mXnwWKAA`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex:7:\label{tab:four-way}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:8:\label{tab:hyperparams}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:50:\label{tab:loss-iterations}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:88:\label{tab:ir-results}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:116:\label{tab:n5-ar}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:146:\label{tab:stat-tests}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:180:\label{tab:llama-full}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:218:\label{tab:gradient-crossmodel}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:307:\label{tab:steering-full}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:341:\label{tab:gate-profile}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:386:\label{tab:cost}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:421:\label{tab:examples}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:469:\label{tab:data-stats}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:529:\label{tab:kl-perhead}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:554:\label{tab:gar-robust}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:578:\label{tab:mmlu}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:606:\label{tab:1.5b-steering}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:795:\label{tab:llama-ss-steering}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:817:\label{tab:llama-vs-qwen-ss}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ffb64c5-f24a-4a8c-88ad-34e8f6676843",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "ece3c77c-bfe1-4c76-8bce-943d39628c75",
  "sourceToolAssistantUUID": "0ffb64c5-f24a-4a8c-88ad-34e8f6676843",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-25T10:16:33.568Z_

<details open><summary>🔧 Tool call — Read · `toolu_0178aHw79GMdHhAvTgF6Ec4K`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 620,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ece3c77c-bfe1-4c76-8bce-943d39628c75",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7YXhr3Pb55FY3gRGVd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b950f633-55b5-4006-9691-841e0cd0ff79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WQzMGRdK7xuURGta2AJim2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3090,
      "cache_read_input_tokens": 42106,
      "output_tokens": 335,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3090
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 335,
          "cache_read_input_tokens": 42106,
          "cache_creation_input_tokens": 3090,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3090,
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

_source line 28 · 2026-05-25T10:16:33.576Z_

<details><summary>↩ Tool result · `toolu_0178aHw79GMdHhAvTgF6Ec4K`</summary>

```text
620	\end{tabular}
621	\end{table}
622	
623	The steering pattern mirrors the 7B results: $\beta$\,=\,5 recovers GAR to 0.657--0.715 ($p < 0.001$), confirming that attention misallocation is the proximal cause of GAR collapse across scales. At $\beta$\,=\,0, TG shows a small but significant GAR advantage ($p$\,=\,0.005); at $\beta$\,=\,3, the TG--Base difference is not statistically significant ($p$\,=\,0.815), unlike the 7B pattern where TG consistently outperforms Base. This scale-specific difference may reflect the 1.5B model's limited capacity to maintain learned routing at intermediate steering strengths. ThreadGate does provide a stability advantage---zero catastrophic PPL outliers vs.\ one in Base---suggesting that residual gating regularizes attention distributions even when aggregate GAR is comparable.
624	
625	\section{Per-Seed Detailed Results}\label{sec:appendix-perseed}
626	
627	Tables~\ref{tab:perseed-ss} and~\ref{tab:perseed-tg} report full per-seed breakdowns for the two multi-seed configurations, providing evidence that our main findings are robust to random initialization.
628	
629	\paragraph{Scheduled sampling (3 seeds).} TF GAR-ours averages $0.517\pm0.032$ across seeds under the held-out protocol (Table~\ref{tab:perseed-ss}); under IID evaluation, TF is more stable ($0.499\pm0.003$), with the held-out variance driven by seed~123's higher value on the larger $N$\,=\,200 sample. AR GAR shows meaningful variance (std\,=\,0.047): seed 42 produces the lowest AR GAR (0.347, gap 1.4$\times$), seed 123 is intermediate (0.423, gap 1.3$\times$), and seed 456 is highest (0.433, gap 1.2$\times$). This variance is expected: AR evaluation involves free-form generation where small differences in learned attention patterns can compound across turns. The variance is asymmetric---all seeds remain well above the non-SS baseline (0.064)---so the qualitative conclusion (SS provides order-of-magnitude improvement) holds across seeds. At $\beta$\,=\,5, the cross-seed variance nearly vanishes ($0.717\pm0.001$), confirming that strong steering converges to a seed-independent attention equilibrium that overwhelms initialization differences.
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
662	\begin{figure}[t]
663	  \centering
664	  \includegraphics[width=\columnwidth]{fig_perturn_llama_detail.pdf}
665	  \caption{Per-turn AR GAR decay on Llama-3.1-8B. (a)~Three-way comparison (Base, TG, LoRA-only; $N$\,=\,20, 4 turns). (b)~Extended Base decay profile ($N$\,=\,5, 10 turns), showing 90\% decline.}
666	  \label{fig:perturn-llama-detail}
667	\end{figure}
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b950f633-55b5-4006-9691-841e0cd0ff79",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "430883c2-e1cc-4e84-9bdf-a70e5dc4b2ea",
  "sourceToolAssistantUUID": "b950f633-55b5-4006-9691-841e0cd0ff79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-25T10:16:37.142Z_

Now I need to count figures and tables in order to map numbers to labels. Let me also check if there are any external .tex files included in the appendix, and find the per-turn tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "430883c2-e1cc-4e84-9bdf-a70e5dc4b2ea",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7YyLCz3mShNBix2Ei8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b49d58f7-5562-4921-b72f-218ec797390c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYLWkpNS252w1TctbpwPpY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5524,
      "cache_read_input_tokens": 45196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5524,
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

_source line 30 · 2026-05-25T10:16:39.552Z_

<details open><summary>🔧 Tool call — Grep · `toolu_011jZEZ853Ld9yisazGsZMej`</summary>

```json
{
  "pattern": "\\\\input\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b49d58f7-5562-4921-b72f-218ec797390c",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7YyLCz3mShNBix2Ei8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91b96208-b8c1-4d21-aca4-59f25effb160",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYLWkpNS252w1TctbpwPpY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5524,
      "cache_read_input_tokens": 45196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5524,
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

_source line 31 · 2026-05-25T10:16:39.564Z_

<details><summary>↩ Tool result · `toolu_011jZEZ853Ld9yisazGsZMej`</summary>

```text
205:\input{../artifacts/appendix_expansion/tab_crossmodel_detail.tex}
635:\input{../artifacts/appendix_expansion/tab_perseed_ss.tex}
637:\input{../artifacts/appendix_expansion/tab_perseed_tg.tex}
651:\input{../artifacts/appendix_expansion/tab_perturn_qwen.tex}
660:\input{../artifacts/appendix_expansion/tab_perturn_llama.tex}
679:\input{../artifacts/appendix_expansion/tab_dataset_stats.tex}
689:\input{../artifacts/appendix_expansion/tab_gar_robustness.tex}
708:\input{../artifacts/appendix_expansion/tab_mmlu_detail.tex}
729:\input{../artifacts/appendix_expansion/tab_qwen15b_results.tex}
745:\input{../artifacts/appendix_expansion/tab_statistical_tests.tex}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91b96208-b8c1-4d21-aca4-59f25effb160",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "8c2537e0-9d8d-4ac6-8bb9-ba9ea1e7b98d",
  "sourceToolAssistantUUID": "91b96208-b8c1-4d21-aca4-59f25effb160",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-25T10:16:41.014Z_

<details open><summary>🔧 Tool call — Grep · `toolu_014yegUhjdUYBdf627tzzBUT`</summary>

```json
{
  "pattern": "\\\\label\\{tab:|\\\\label\\{fig:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c2537e0-9d8d-4ac6-8bb9-ba9ea1e7b98d",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7YyLCz3mShNBix2Ei8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "490645ba-4c97-489c-9527-c72ce2827668",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYLWkpNS252w1TctbpwPpY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5524,
      "cache_read_input_tokens": 45196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5524,
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

_source line 33 · 2026-05-25T10:16:41.030Z_

<details><summary>↩ Tool result · `toolu_014yegUhjdUYBdf627tzzBUT`</summary>

```text
7:\label{tab:four-way}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "490645ba-4c97-489c-9527-c72ce2827668",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "884b1efb-7fa0-4c86-936f-2dbaeb6acfb0",
  "sourceToolAssistantUUID": "490645ba-4c97-489c-9527-c72ce2827668",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-25T10:16:42.090Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01GHjzJFj7XUAH1h2zMNHTT4`</summary>

```json
{
  "pattern": "\\\\label\\{tab:|\\\\label\\{fig:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "884b1efb-7fa0-4c86-936f-2dbaeb6acfb0",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7YyLCz3mShNBix2Ei8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1efa96e-ee93-4060-b477-bb0ea09387ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYLWkpNS252w1TctbpwPpY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5524,
      "cache_read_input_tokens": 45196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5524,
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

_source line 35 · 2026-05-25T10:16:42.103Z_

<details><summary>↩ Tool result · `toolu_01GHjzJFj7XUAH1h2zMNHTT4`</summary>

```text
20:  \label{fig:steering-recovery}
35:  \label{fig:ss-gap}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1efa96e-ee93-4060-b477-bb0ea09387ab",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "0f42ed2b-83ac-4a1d-abd5-9aff2f747f05",
  "sourceToolAssistantUUID": "d1efa96e-ee93-4060-b477-bb0ea09387ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-25T10:16:43.369Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01DNG5CSAqhU8dW7VHTvHNmJ`</summary>

```json
{
  "pattern": "\\\\label\\{tab:|\\\\label\\{fig:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f42ed2b-83ac-4a1d-abd5-9aff2f747f05",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7YyLCz3mShNBix2Ei8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33637f64-62bf-44f9-85e1-17d22818d5f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYLWkpNS252w1TctbpwPpY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5524,
      "cache_read_input_tokens": 45196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5524,
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

_source line 37 · 2026-05-25T10:16:43.389Z_

<details><summary>↩ Tool result · `toolu_01DNG5CSAqhU8dW7VHTvHNmJ`</summary>

```text
27:  \label{fig:ss-multiseed}
40:  \label{fig:gate-shift}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33637f64-62bf-44f9-85e1-17d22818d5f3",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "2149b292-512d-4b01-bfb9-ff663c21d821",
  "sourceToolAssistantUUID": "33637f64-62bf-44f9-85e1-17d22818d5f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-25T10:16:43.932Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01BWnJ32BK3mh7n84RXuQQmV`</summary>

```json
{
  "pattern": "\\\\label\\{tab:|\\\\label\\{fig:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2149b292-512d-4b01-bfb9-ff663c21d821",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7YyLCz3mShNBix2Ei8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "400546e6-7cd7-4898-998d-ce4e9553f109",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYLWkpNS252w1TctbpwPpY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5524,
      "cache_read_input_tokens": 45196,
      "output_tokens": 750,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5524
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 750,
          "cache_read_input_tokens": 45196,
          "cache_creation_input_tokens": 5524,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5524,
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

_source line 39 · 2026-05-25T10:16:43.949Z_

<details><summary>↩ Tool result · `toolu_01BWnJ32BK3mh7n84RXuQQmV`</summary>

```text
25:  \label{fig:attention-heatmap}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "400546e6-7cd7-4898-998d-ce4e9553f109",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "f07dea16-bdb2-45dc-973d-26895385f35e",
  "sourceToolAssistantUUID": "400546e6-7cd7-4898-998d-ce4e9553f109",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-25T10:16:47.430Z_

Now let me check the external table files for additional labels, especially the per-turn and per-seed tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f07dea16-bdb2-45dc-973d-26895385f35e",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7ZjigdyMWcM18XUThh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "120d3ae8-f6b4-4582-b076-3102c7869383",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uc7LyC8NigvNLMAEEszznX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1178,
      "cache_read_input_tokens": 50720,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1178,
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

_source line 41 · 2026-05-25T10:16:47.920Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Fc9CdXkeRpqQBYm36T48Tw`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "120d3ae8-f6b4-4582-b076-3102c7869383",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7ZjigdyMWcM18XUThh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "339ea01c-b81d-4bba-acfd-a46c5959c9b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uc7LyC8NigvNLMAEEszznX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1178,
      "cache_read_input_tokens": 50720,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1178
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 130,
          "cache_read_input_tokens": 50720,
          "cache_creation_input_tokens": 1178,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1178,
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

_source line 42 · 2026-05-25T10:16:47.936Z_

<details><summary>↩ Tool result · `toolu_01Fc9CdXkeRpqQBYm36T48Tw`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_gar_robustness.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_statistical_tests.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_llama.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_qwen.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_mmlu_detail.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_qwen15b_results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_dataset_stats.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "339ea01c-b81d-4bba-acfd-a46c5959c9b5",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "b626e7bf-772f-444b-a6ad-238fbb0d9215",
  "sourceToolAssistantUUID": "339ea01c-b81d-4bba-acfd-a46c5959c9b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-25T10:16:53.027Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Nruva5WRY9HMgX96v1ajNZ`</summary>

```json
{
  "pattern": "\\\\label\\{tab:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b626e7bf-772f-444b-a6ad-238fbb0d9215",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7a2XimX6mMuTjkKZuv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "513750ce-577d-4ee0-8a8b-f9fc25a28aff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UK9MD3REoWqM5zGk5oQpau",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 51898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 708,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
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

_source line 44 · 2026-05-25T10:16:53.047Z_

<details><summary>↩ Tool result · `toolu_01Nruva5WRY9HMgX96v1ajNZ`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_llama.tex:9:\label{tab:perturn-llama}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex:9:\label{tab:perseed-tg}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_gar_robustness.tex:6:\label{tab:gar_robustness}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex:8:\label{tab:perseed-ss}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_dataset_stats.tex:6:\label{tab:dataset_stats}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_qwen.tex:7:\label{tab:perturn-qwen}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_qwen15b_results.tex:6:\label{tab:qwen15b_results}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_statistical_tests.tex:10:\label{tab:statistical_tests}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex:12:\label{tab:crossmodel-detail}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_mmlu_detail.tex:6:\label{tab:mmlu_detail}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "513750ce-577d-4ee0-8a8b-f9fc25a28aff",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "63f3bf68-abc9-42d1-ab9f-a54a5051038a",
  "sourceToolAssistantUUID": "513750ce-577d-4ee0-8a8b-f9fc25a28aff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-25T10:16:55.992Z_

Now let me also read the rest of the appendix to find any remaining figures/tables (after line 720).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63f3bf68-abc9-42d1-ab9f-a54a5051038a",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7aQiDPUEY9iEAVi593",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1cd2b522-e3b0-4c77-8ad5-7ccf5731f511",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BP3zjYe6pFShVStmygowr9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 52606,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 781,
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

_source line 46 · 2026-05-25T10:16:56.761Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Pg4Nk5oHjX2o1Ha4KhsurT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 720,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cd2b522-e3b0-4c77-8ad5-7ccf5731f511",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7aQiDPUEY9iEAVi593",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2039042d-95cd-43f2-8113-afebd08bb0d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BP3zjYe6pFShVStmygowr9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 52606,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 781
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 149,
          "cache_read_input_tokens": 52606,
          "cache_creation_input_tokens": 781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 781,
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

_source line 47 · 2026-05-25T10:16:56.768Z_

<details><summary>↩ Tool result · `toolu_01Pg4Nk5oHjX2o1Ha4KhsurT`</summary>

```text
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
759	  \includegraphics[width=0.75\textwidth]{fig_training_curves_6panel.pdf}
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
778	\begin{figure}[t]
779	  \centering
780	  \includegraphics[width=\columnwidth]{fig_steering_perturn_4panel.pdf}
781	  \caption{Per-turn GAR under four $\beta$-steering strengths. At $\beta$\,=\,0, monotonic decay; at $\beta$\,=\,3, partial recovery with residual decay; at $\beta$\,=\,5, sustained high GAR; at $\beta$\,=\,10, saturation with catastrophic PPL.}
782	  \label{fig:steering-4panel}
783	\end{figure}
784	
785	\section{Llama-3.1-8B Scheduled Sampling Details}\label{sec:appendix-llama-ss}
786	
787	Llama-3.1-8B-Instruct was trained with scheduled sampling using the same protocol as Qwen (\S\ref{sec:appendix-ss}), with one key difference: training was stopped at 2 epochs (${\sim}$14{,}400 steps) instead of 3, because Llama's per-step wall-clock time was ${\sim}$4$\times$ slower than Qwen on the same hardware (624 steps/h vs.\ ${\sim}$2{,}400 steps/h for Qwen). This is attributable to different vocabulary sizes (Llama 128K vs.\ Qwen 152K tokens) and attention implementation. The 2-epoch checkpoint was selected based on convergence of TF GAR (0.477, within 0.02 of Qwen's 3-epoch value 0.498).
788	
789	\paragraph{$\beta$-steering on Llama SS.}
790	Table~\ref{tab:llama-ss-steering} reports $\beta$-steering results on the Llama SS model. Unlike Qwen, $\beta$\,=\,3 does not trigger recovery on Llama (GAR 0.173 vs.\ 0.166 at $\beta$\,=\,0). At $\beta$\,=\,5, GAR reaches 0.791---higher than Qwen's 0.717---suggesting that Llama's attention distribution is more responsive to the additive bias at higher steering strengths, possibly because the lower baseline AR GAR leaves more headroom for steering to exploit.
791	
792	\begin{table}[h]
793	\centering\small
794	\caption{$\beta$-steering on Llama-3.1-8B SS model ($N$\,=\,50, $T$\,=\,4).}
795	\label{tab:llama-ss-steering}
796	\begin{tabular}{@{}l ccc@{}}
797	\toprule
798	& $\beta$\,=\,0 & $\beta$\,=\,3 & $\beta$\,=\,5 \\
799	\midrule
800	AR GAR & 0.166 & 0.173 & 0.791 \\
801	\bottomrule
802	\end{tabular}
803	\end{table}
804	
805	\paragraph{Cross-model comparison.}
806	Table~\ref{tab:llama-vs-qwen-ss} compares scheduled sampling across both architectures. Both models show large gap compression relative to their ThreadGate baselines, but the residual gap on Llama (2.9$\times$) is larger than Qwen's (1.2$\times$). We attribute this to training duration: Llama received only 2 epochs of scheduled sampling exposure versus Qwen's 3 epochs. Llama reduces its median-based gap by 9.3$\times$ (from 27$\times$ to 2.9$\times$) while Qwen reduces by 6.5$\times$ (from 7.8$\times$ to 1.2$\times$), suggesting that a third epoch would likely narrow the residual gap further. Notably, $\beta$-steering is more effective on Llama (0.791 vs.\ 0.717 at $\beta$\,=\,5), partially compensating for the weaker training-time compression.
807	
808	\paragraph{Architectural differences.}
809	Several architectural differences between Qwen-2.5-7B and Llama-3.1-8B may contribute to the cross-model gap variation. Llama uses Grouped Query Attention (GQA) with 8 KV heads (vs.\ Qwen's full 28-head multi-head attention, MHA), which reduces the number of independently steerable attention heads by 3.5$\times$. Llama also uses Rotary Position Embedding (RoPE) with a longer default context (128K tokens vs.\ Qwen's 32K), which may affect how positional information interacts with goal-token attention at different conversation depths. Despite these differences, the qualitative pattern is identical: TF convergence, AR collapse, and SS-mediated recovery, confirming that exposure bias on auxiliary attention losses is architecture-general rather than an artifact of a specific attention implementation.
810	
811	\paragraph{Training dynamics.}
812	The Llama SS training loss trajectory closely mirrors Qwen's during the first two epochs: NTP loss converges within epoch~1 (final NTP loss 0.62 for Llama vs.\ 0.58 for Qwen), while GAR loss continues to decrease throughout epoch~2. The scheduled sampling ratio reaches ${\sim}$0.20 at the end of epoch~2 (vs.\ 0.30 at end of epoch~3 for Qwen), meaning Llama was exposed to less model-generated context during training. This partial exposure is sufficient to achieve meaningful gap compression (27$\times$ $\to$ 2.9$\times$ by median) but leaves a larger residual gap than Qwen's full 3-epoch schedule.
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
826	Baseline TG gap & 7.8$\times$ & 27$\times$ (median) \\
827	Gap compression & 6.5$\times$ & 9.3$\times$ \\
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
  "parentUuid": "2039042d-95cd-43f2-8113-afebd08bb0d7",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "79e2f4d7-019e-4bbb-9d6b-41e8627ce707",
  "sourceToolAssistantUUID": "2039042d-95cd-43f2-8113-afebd08bb0d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-25T10:17:00.088Z_

Now I have all the data needed. Let me also check the `discussion.tex` file for any additional figures/tables in the main text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79e2f4d7-019e-4bbb-9d6b-41e8627ce707",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7agaCewqU2BCu9kJy8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56f73f10-af44-4a97-a911-a2130404b878",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PuDFahHuBNrVg1phZmfydG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5088,
      "cache_read_input_tokens": 53387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5088,
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

_source line 49 · 2026-05-25T10:17:03.014Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01CGhdgCX7esVmwyLh2grsg6`</summary>

```json
{
  "pattern": "\\\\label\\{tab:|\\\\label\\{fig:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56f73f10-af44-4a97-a911-a2130404b878",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7agaCewqU2BCu9kJy8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d47393ae-120a-41e5-ac58-35f627411404",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PuDFahHuBNrVg1phZmfydG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5088,
      "cache_read_input_tokens": 53387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5088,
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

_source line 50 · 2026-05-25T10:17:03.036Z_

<details><summary>↩ Tool result · `toolu_01CGhdgCX7esVmwyLh2grsg6`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d47393ae-120a-41e5-ac58-35f627411404",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "22fda0b9-18f1-4610-bab3-659dd81f3b05",
  "sourceToolAssistantUUID": "d47393ae-120a-41e5-ac58-35f627411404",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-25T10:17:03.597Z_

<details open><summary>🔧 Tool call — Grep · `toolu_013GhQVvHTqdHWtSjZMkhmjp`</summary>

```json
{
  "pattern": "\\\\label\\{tab:|\\\\label\\{fig:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22fda0b9-18f1-4610-bab3-659dd81f3b05",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7agaCewqU2BCu9kJy8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d86ade8-72e1-45c9-a300-bba60562fde9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PuDFahHuBNrVg1phZmfydG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5088,
      "cache_read_input_tokens": 53387,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5088
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 318,
          "cache_read_input_tokens": 53387,
          "cache_creation_input_tokens": 5088,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5088,
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

_source line 52 · 2026-05-25T10:17:03.615Z_

<details><summary>↩ Tool result · `toolu_013GhQVvHTqdHWtSjZMkhmjp`</summary>

```text
13:  \label{fig:headline}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d86ade8-72e1-45c9-a300-bba60562fde9",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "9cb158d3-9a76-467f-9950-c00392e2c22b",
  "sourceToolAssistantUUID": "6d86ade8-72e1-45c9-a300-bba60562fde9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-25T10:17:06.863Z_

Now let me check the compiled PDF to find page numbers. Let me look for the PDF.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cb158d3-9a76-467f-9950-c00392e2c22b",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7bBpbdqgWGj7CSbaKB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d874a473-c741-49d6-b293-fc98885cb918",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdiCM9WiqEkJWFNaPMP45j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 391,
      "cache_read_input_tokens": 58475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 391,
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

_source line 54 · 2026-05-25T10:17:07.280Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Mqq8Qg9A8UUMJeGkCdQ8C1`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d874a473-c741-49d6-b293-fc98885cb918",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7bBpbdqgWGj7CSbaKB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a995a405-6f49-4892-b95c-2bfc635aa57d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdiCM9WiqEkJWFNaPMP45j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 391,
      "cache_read_input_tokens": 58475,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 391
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 121,
          "cache_read_input_tokens": 58475,
          "cache_creation_input_tokens": 391,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 391,
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

_source line 55 · 2026-05-25T10:17:07.298Z_

<details><summary>↩ Tool result · `toolu_01Mqq8Qg9A8UUMJeGkCdQ8C1`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/fig2_training_pcgrad.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_figure_backups/20260524_071403/fig2_training_pcgrad.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/fig3_gate_shift.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_figure_backups/20260524_071403/fig3_gate_shift.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/fig5_attention_steering.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/fig1_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a995a405-6f49-4892-b95c-2bfc635aa57d",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "b14f93b2-fd2c-4c69-ba63-3a9664a1bc2e",
  "sourceToolAssistantUUID": "a995a405-6f49-4892-b95c-2bfc635aa57d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-25T10:17:10.622Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T6CqEcKWFzVkG6hVsQoZYy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.pdf",
  "pages": "7-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b14f93b2-fd2c-4c69-ba63-3a9664a1bc2e",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7bTY9kCxiWXH4gMdC8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d64e2016-f343-44e0-a598-b37240b1da0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013wDZ9zv5W4jGBAnE9Zok61",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 437,
      "cache_read_input_tokens": 58866,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 437
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 58866,
          "cache_creation_input_tokens": 437,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 437,
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

_source line 57 · 2026-05-25T10:17:10.990Z_

<details><summary>↩ Tool result · `toolu_01T6CqEcKWFzVkG6hVsQoZYy`</summary>

```text
PDF pages extracted: 4 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.pdf (1019.3KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d64e2016-f343-44e0-a598-b37240b1da0f",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "e07e37ea-9591-4c16-9be3-6431d8ee0152",
  "sourceToolAssistantUUID": "d64e2016-f343-44e0-a598-b37240b1da0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

## Round 2

10 recorded events

### User

_source line 58 · 2026-05-25T10:17:10.989Z_

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e07e37ea-9591-4c16-9be3-6431d8ee0152",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "isMeta": true,
  "uuid": "8e7a5add-ac02-45f6-84f5-e6b96bb54dc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-25T10:17:26.270Z_



Now I have all the information needed. Let me compile the complete figure and table numbering by tracing through the document order.

## Figure Numbering (in document order)

The paper uses `\appendix` with `\AlphAlph` for section numbering, but figures and tables continue with Arabic numerals throughout. Here is the complete ordered list:

**Main text figures:**
1. **Figure 1** — `fig:headline` — `fig1_headline.pdf` (introduction.tex:11-13)
2. **Figure 2** — `fig:attention-heatmap` — `fig4_attention_heatmap.pdf` (method.tex:23-25)
3. **Figure 3** — `fig:steering-recovery` — `fig5_attention_steering.pdf` (experiments.tex:18-20)
4. **Figure 4** — `fig:ss-gap` — `fig_ss_gap_compression.pdf` (experiments.tex:33-35)
5. **Figure 5** — `fig:ss-multiseed` — `fig_ss_multiseed.pdf` (analysis.tex:25-27)
6. **Figure 6** — `fig:gate-shift` — `fig3_gate_shift.pdf` (analysis.tex:38-40)

**Appendix figures (continuing numbering):**
7. **Figure 7** — `fig:ir-bar` — **`fig_instruction_retention.pdf`** (appendix.tex:80-82)
8. **Figure 8** — `fig:crossmodel` — `fig_crossmodel.pdf` (appendix.tex:198-200)
9. **Figure 9** — `fig:gate-heatmap` — `fig_gate_profile_heatmap.pdf` (appendix.tex:240-242)
10. **Figure 10** — `fig:gate-crossmodel` — `fig_gate_profile_crossmodel.pdf` (appendix.tex:251-253)
11. **Figure 11** — `fig:ar-gar-perturn` — `fig_ar_gar_perturn.pdf` (appendix.tex:262-264)
12. **Figure 12** — `fig:bootstrap-ci` — `fig_bootstrap_ci.pdf` (appendix.tex:273-275)
13. **Figure 13** — `fig:gate-distribution` — `fig_gate_distribution.pdf` (appendix.tex:284-286)
14. **Figure 14** — `fig:training-loss` — **`fig_training_loss_curves.pdf`** (appendix.tex:295-297)
15. **Figure 15** — `fig:steering-standalone` — `fig_steering_perturn_4panel.pdf`... wait, let me recheck.

Let me re-read the specific lines around 329 and 376 more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e7a5add-ac02-45f6-84f5-e6b96bb54dc4",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7bj8WeJ4Dh3RwZT18F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95db91f7-8854-489a-b34f-53e20b05e89f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BdF6usdsBoh269DZMUhP3P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5226,
      "cache_read_input_tokens": 59303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5226,
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

_source line 60 · 2026-05-25T10:17:27.878Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R5y3VQYH2ZcyJA4wXVdSHn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 300,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95db91f7-8854-489a-b34f-53e20b05e89f",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7bj8WeJ4Dh3RwZT18F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57a0dca5-b461-493a-875c-8d849cfbbe50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BdF6usdsBoh269DZMUhP3P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5226,
      "cache_read_input_tokens": 59303,
      "output_tokens": 809,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5226
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 809,
          "cache_read_input_tokens": 59303,
          "cache_creation_input_tokens": 5226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5226,
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

_source line 61 · 2026-05-25T10:17:27.885Z_

<details><summary>↩ Tool result · `toolu_01R5y3VQYH2ZcyJA4wXVdSHn`</summary>

```text
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
  "parentUuid": "57a0dca5-b461-493a-875c-8d849cfbbe50",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "f4a1dea5-4ed9-4be3-b0de-6b6f804971ac",
  "sourceToolAssistantUUID": "57a0dca5-b461-493a-875c-8d849cfbbe50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-25T10:17:32.446Z_

Now let me also check the table that contains the steering table (around line 302) which appears between figures. I also need to check some lines around the per-turn tables to understand their numbering. Let me also check the `tab_perturn_llama.tex` file to confirm the label for Table 22.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4a1dea5-4ed9-4be3-b0de-6b6f804971ac",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7cyfQt7dFSG47GLX2M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d0b155e-6d01-4ad7-9e37-35ea9fe2d088",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HwNb3QA65DQHnD8si4CFYk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3780,
      "cache_read_input_tokens": 64529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3780,
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

_source line 63 · 2026-05-25T10:17:33.118Z_

<details open><summary>🔧 Tool call — Read · `toolu_019Jqc86qDKPWzo7uGLyJngc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_llama.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d0b155e-6d01-4ad7-9e37-35ea9fe2d088",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7cyfQt7dFSG47GLX2M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a9add2b-bec2-4a38-974f-a8aec22f8788",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HwNb3QA65DQHnD8si4CFYk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3780,
      "cache_read_input_tokens": 64529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3780,
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

_source line 64 · 2026-05-25T10:17:33.123Z_

<details><summary>↩ Tool result · `toolu_019Jqc86qDKPWzo7uGLyJngc`</summary>

```text
1	% Per-turn AR GAR-ours for Llama-3.1-8B-Instruct
2	% Panel (a): N=20, T=4 (eval_llama_ar_n20) — reliable estimates
3	% Panel (b): Base only, N=5, T=10 (llama_phase1_gar_diag) — decay profile
4	\begin{table*}[t]
5	\centering
6	\caption{Per-turn autoregressive GAR-ours ($\beta{=}0$) on Llama-3.1-8B-Instruct.
7	(a)~Three-way comparison using $N{=}20$ conversations ($T{=}4$ turns).
8	(b)~Base model decay profile ($N{=}5$, $T{=}10$).}
9	\label{tab:perturn-llama}
10	\small
11	\begin{subtable}[t]{0.48\textwidth}
12	\centering
13	\caption{$N{=}20$, $T{=}4$}
14	\begin{tabular}{@{}l cccc@{}}
15	\toprule
16	\textbf{Config.} & \textbf{T1} & \textbf{T2} & \textbf{T3} & \textbf{T4} \\
17	\midrule
18	Base      & .028 & .013 & .009 & .008 \\
19	TG        & .041 & .042 & .049 & .038 \\
20	LoRA-only & .033 & .049 & .025 & .031 \\
21	\bottomrule
22	\end{tabular}
23	\end{subtable}
24	\hfill
25	\begin{subtable}[t]{0.38\textwidth}
26	\centering
27	\caption{Base decay ($N{=}5$, $T{=}10$)}
28	\begin{tabular}{@{}cc@{}}
29	\toprule
30	\textbf{Turn} & \textbf{GAR-ours} \\
31	\midrule
32	1  & .026 \\
33	2  & .018 \\
34	3  & .009 \\
35	4  & .006 \\
36	5  & .006 \\
37	6  & .004 \\
38	7  & .004 \\
39	8  & .004 \\
40	9  & .005 \\
41	10 & .003 \\
42	\bottomrule
43	\end{tabular}
44	\end{subtable}
45	\end{table*}
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a9add2b-bec2-4a38-974f-a8aec22f8788",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "3ffb64cb-058e-4e2e-a4e8-08e0d51321f4",
  "sourceToolAssistantUUID": "9a9add2b-bec2-4a38-974f-a8aec22f8788",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-25T10:17:33.615Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GLjCmrEUPcMcPmUwCxZ1zg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_qwen.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ffb64cb-058e-4e2e-a4e8-08e0d51321f4",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7cyfQt7dFSG47GLX2M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a80d7cb-e630-4936-bae6-ddbd31cf890c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HwNb3QA65DQHnD8si4CFYk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3780,
      "cache_read_input_tokens": 64529,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3780
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 248,
          "cache_read_input_tokens": 64529,
          "cache_creation_input_tokens": 3780,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3780,
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

_source line 66 · 2026-05-25T10:17:33.621Z_

<details><summary>↩ Tool result · `toolu_01GLjCmrEUPcMcPmUwCxZ1zg`</summary>

```text
1	% Per-turn AR GAR-ours for Qwen2.5-7B-Instruct, 6-way comparison
2	% Source: d048_final_ar, beta=0, N=50 gen-mode, n_valid~39
3	% Only turns 1--5 shown (later turns have survivor bias from variable-length generation)
4	\begin{table}[t]
5	\centering
6	\caption{Per-turn autoregressive GAR-ours ($\beta{=}0$) on Qwen2.5-7B-Instruct across six training configurations. Values represent average GAR over ${\sim}39$ valid conversations in free-form generation mode.}
7	\label{tab:perturn-qwen}
8	\resizebox{\columnwidth}{!}{
9	\begin{tabular}{@{}l ccccc@{}}
10	\toprule
11	\textbf{Configuration} & \textbf{Turn 1} & \textbf{Turn 2} & \textbf{Turn 3} & \textbf{Turn 4} & \textbf{Turn 5} \\
12	\midrule
13	Base         & .085 & .032 & .021 & .013 & .004 \\
14	ThreadGate   & .130 & .073 & .059 & .043 & .066 \\
15	PCGrad       & .090 & .038 & .028 & .029 & .027 \\
16	UG           & .113 & .056 & .033 & .020 & .016 \\
17	LoRA-only    & .107 & .059 & .030 & .049 & .040 \\
18	SS           & \textbf{.458} & \textbf{.381} & \textbf{.344} & \textbf{.370} & \textbf{.365} \\
19	\bottomrule
20	\end{tabular}}
21	\end{table}
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a80d7cb-e630-4936-bae6-ddbd31cf890c",
  "isSidechain": true,
  "promptId": "8bc37590-ec7e-4855-bf68-d566f33e8b27",
  "agentId": "a8040b0d4a0e1337c",
  "type": "user",
  "uuid": "1106fc8c-c4d3-43d9-a2c6-7ee0e440d337",
  "sourceToolAssistantUUID": "8a80d7cb-e630-4936-bae6-ddbd31cf890c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-25T10:18:10.383Z_

Now I have everything needed. Let me compile the complete ordered numbering of all tables and figures to identify the exact numbers requested.

Here are the complete results:

---

## Figure-to-Image Mapping

Figures are numbered sequentially across main text and appendix. Complete ordered list of all 27 figures:

| # | Label | Image File | Location |
|---|-------|-----------|----------|
| 1 | `fig:headline` | `fig1_headline.pdf` | introduction.tex:11 |
| 2 | `fig:attention-heatmap` | `fig4_attention_heatmap.pdf` | method.tex:23 |
| 3 | `fig:steering-recovery` | `fig5_attention_steering.pdf` | experiments.tex:18 |
| 4 | `fig:ss-gap` | `fig_ss_gap_compression.pdf` | experiments.tex:33 |
| 5 | `fig:ss-multiseed` | `fig_ss_multiseed.pdf` | analysis.tex:25 |
| 6 | `fig:gate-shift` | `fig3_gate_shift.pdf` | analysis.tex:38 |
| 7 | `fig:ir-bar` | `fig_instruction_retention.pdf` | appendix.tex:80 |
| 8 | `fig:crossmodel` | `fig_crossmodel.pdf` | appendix.tex:198 |
| 9 | `fig:gate-heatmap` | `fig_gate_profile_heatmap.pdf` | appendix.tex:240 |
| 10 | `fig:gate-crossmodel` | `fig_gate_profile_crossmodel.pdf` | appendix.tex:251 |
| 11 | `fig:ar-gar-perturn` | `fig_ar_gar_perturn.pdf` | appendix.tex:262 |
| 12 | `fig:bootstrap-ci` | `fig_bootstrap_ci.pdf` | appendix.tex:273 |
| 13 | `fig:gate-distribution` | `fig_gate_distribution.pdf` | appendix.tex:284 |
| 14 | `fig:training-loss` | `fig_training_loss_curves.pdf` | appendix.tex:295 |
| 15 | `fig:steering-standalone` | `fig_steering_standalone.pdf` | appendix.tex:329 |
| 16 | `fig:ss-dynamics` | `fig_ss_training_dynamics.pdf` | appendix.tex:376 |
| 17 | `fig:training-pcgrad` | `fig2_training_pcgrad.pdf` | appendix.tex:440 |
| 18 | `fig:gradient-heatmap` | `fig_gradient_conflict_heatmap.pdf` | appendix.tex:457 |
| 19 | `fig:eb-scaling` | `fig_eb_scaling.pdf` | appendix.tex:495 |
| 20 | `fig:kl_ar_gar_curves` | `fig_kl_ar_gar_curves.pdf` | appendix.tex:508 |
| 21 | `fig:kl_ar_gar_bar` | `fig_kl_ar_gar_bar.pdf` | appendix.tex:515 |
| 22 | `fig:perturn-qwen-detail` | `fig_perturn_qwen_detail.pdf` | appendix.tex:655 |
| 23 | `fig:perturn-llama-detail` | `fig_perturn_llama_detail.pdf` | appendix.tex:664 |
| 24 | `fig:gar-robust-grouped` | `fig_gar_robustness_grouped.pdf` | appendix.tex:693 |
| 25 | `fig:mmlu-comparison` | `fig_mmlu_comparison.pdf` | appendix.tex:712 |
| 26 | `fig:training-6panel` | `fig_training_curves_6panel.pdf` | appendix.tex:759 |
| 27 | `fig:steering-4panel` | `fig_steering_perturn_4panel.pdf` | appendix.tex:780 |

---

## Answers to Specific Questions

**1. Figure 7 (instruction retention bar chart)**
- Image file: **`fig_instruction_retention.pdf`**
- Defined at: `appendix.tex` line 80 (`\includegraphics`), label `fig:ir-bar` at line 82

**2. Figure 14 (training loss curves - NTP/GAR/Total Loss)**
- Image file: **`fig_training_loss_curves.pdf`**
- Defined at: `appendix.tex` line 295 (`\includegraphics`), label `fig:training-loss` at line 297

**3. Figure 23 (Per-turn AR GAR decay on Llama)**
- Image file: **`fig_perturn_llama_detail.pdf`**
- Defined at: `appendix.tex` line 664 (`\includegraphics`), label `fig:perturn-llama-detail` at line 666

**4. Figure 22 (Per-turn AR GAR-ours across Qwen configs)**
- Image file: **`fig_perturn_qwen_detail.pdf`**
- Defined at: `appendix.tex` line 655 (`\includegraphics`), label `fig:perturn-qwen-detail` at line 657

**5. Table 22 (per-turn autoregressive GAR-ours on Llama)**

Tables are also numbered sequentially. Counting all table labels in document order:
1. `tab:four-way` (related_work.tex:7)
2. `tab:hyperparams` (appendix.tex:8)
3. `tab:loss-iterations` (appendix.tex:50)
4. `tab:ir-results` (appendix.tex:88)
5. `tab:n5-ar` (appendix.tex:116)
6. `tab:stat-tests` (appendix.tex:146)
7. `tab:llama-full` (appendix.tex:180)
8. `tab:crossmodel-detail` (via `tab_crossmodel_detail.tex`, input at appendix.tex:205)
9. `tab:gradient-crossmodel` (appendix.tex:218)
10. `tab:steering-full` (appendix.tex:307)
11. `tab:gate-profile` (appendix.tex:341)
12. `tab:cost` (appendix.tex:386)
13. `tab:examples` (appendix.tex:421)
14. `tab:data-stats` (appendix.tex:469)
15. `tab:kl-perhead` (appendix.tex:529)
16. `tab:gar-robust` (appendix.tex:554)
17. `tab:mmlu` (appendix.tex:578)
18. `tab:1.5b-steering` (appendix.tex:606)
19. `tab:perseed-ss` (via `tab_perseed_ss.tex`, input at appendix.tex:635)
20. `tab:perseed-tg` (via `tab_perseed_tg.tex`, input at appendix.tex:637)
21. `tab:perturn-qwen` (via `tab_perturn_qwen.tex`, input at appendix.tex:651)
22. **`tab:perturn-llama`** (via `tab_perturn_llama.tex`, input at appendix.tex:660)

**Table 22** is `tab:perturn-llama`, defined in `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_llama.tex` (line 9 for the label), included into the paper via `\input{../artifacts/appendix_expansion/tab_perturn_llama.tex}` at `appendix.tex` line 660.

---

## Page Layout: Conclusion and Limitations

From the rendered PDF:
- **Section 7 (Conclusion)** starts on **page 8** (right column, line 567) and is a single paragraph ending on page 9 (line 580).
- **Section 8 (Limitations)** starts on **page 9** (line 581) and ends around line 607.
- **References** begin on page 9 (line 608).
- The EMNLP 8-page limit covers main text only. The main text (Sections 1-7 Conclusion) ends partway through **page 8** (right column). Section 8 (Limitations) does NOT count toward the 8-page limit per EMNLP rules. So the paper currently fits within the 8-page limit -- Conclusion ends on page 9 but given the two-column layout and the fact that page 8 already has Discussion (Section 6) and the start of Conclusion (Section 7), **the main text (through Conclusion) spans approximately 8.5 pages**. The Limitations paragraph starts at the top of page 9 left column area (line 581), meaning the main text overflows by roughly half a page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1106fc8c-c4d3-43d9-a2c6-7ee0e440d337",
  "isSidechain": true,
  "agentId": "a8040b0d4a0e1337c",
  "requestId": "req_011CbP7dQ8KTqZSUDbNo32Rb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d5533f6-ee62-4069-bf8b-cd7fac77f09d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0127UAybMWkYShQ5zojxjY8G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1530,
      "cache_read_input_tokens": 68309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1530,
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
