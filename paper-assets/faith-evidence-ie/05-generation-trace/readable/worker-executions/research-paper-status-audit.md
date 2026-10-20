# research paper status audit

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 84
- **Recorded user turns:** 0
- **Tool calls:** 33
- **Original source:** `logs/workers/worker_research_paper_status_audit_20260521T225539.log`
- **Structured JSON:** [`519b01b731570ea06f7c.json`](../../sessions/51/519b01b731570ea06f7c.json)

## Before a recorded user message

84 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
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
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
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
  "uuid": "29476d88-96db-43de-bf2e-e49cd5ed79fb",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/memory/"
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
    "resetsAt": 1779413400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "c91c07af-ca8b-49bd-afdb-2a4d888cd52f",
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by exploring the project directories to understand the current state of the paper artifacts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "a8d11618-ed07-4235-bc50-1b491a06abd7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01REjY5RsbGwFzndCDdN7MLv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12899,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12899
      },
      "output_tokens": 26,
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

<details open><summary>🔧 Tool call — Bash · `toolu_014T4bWSwpABAZSc4WCDZ7DG`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/ 2>/dev/null && echo \"---SEPARATOR---\" && ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/paper/ 2>/dev/null || echo \"NO_PAPER_DIR\"",
  "description": "List artifacts and paper directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "85f133d8-cca4-45fc-b2d2-7913bfa597f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01REjY5RsbGwFzndCDdN7MLv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12899,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12899
      },
      "output_tokens": 26,
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

_source line 6 · 2026-05-21T22:55:56.111Z_

<details><summary>↩ Tool result · `toolu_014T4bWSwpABAZSc4WCDZ7DG`</summary>

```text
total 1804
drwxr-xr-x 28 ubuntu ubuntu   4096 May 21 21:11 .
drwxr-xr-x 11 ubuntu ubuntu   4096 May 21 22:51 ..
-rw-r--r--  1 ubuntu ubuntu   1808 May 21 09:13 14b_rsft_status.md
-rw-r--r--  1 ubuntu ubuntu   3935 May 18 07:13 1_7b_repetition_fair_eval.md
drwxr-xr-x  7 ubuntu ubuntu   4096 May 16 00:47 _project
-rw-r--r--  1 ubuntu ubuntu   2284 May 16 00:40 ced_eval_commands.md
-rw-r--r--  1 ubuntu ubuntu   3346 May 14 18:43 ced_stabilizer_literature_survey.md
-rw-r--r--  1 ubuntu ubuntu  12584 May 19 08:10 comprehensive_results.md
-rw-r--r--  1 ubuntu ubuntu   1827 May 15 16:21 cuda3_diagnostic.md
-rw-r--r--  1 ubuntu ubuntu  18324 May 14 18:43 d024_literature_survey.md
-rw-r--r--  1 ubuntu ubuntu  13068 May 18 22:06 d076_eval_audit.py
-rw-r--r--  1 ubuntu ubuntu   7490 May 18 22:07 d076_final_audit.py
-rw-r--r--  1 ubuntu ubuntu   2637 May 16 05:22 d076_seed_status.md
drwxr-xr-x  2 ubuntu ubuntu   4096 May 18 07:14 d102_next_batch
drwxr-xr-x  3 ubuntu ubuntu   4096 May 19 18:43 d112
-rw-r--r--  1 ubuntu ubuntu   3522 May 18 22:57 d112_pipeline_plan.md
-rw-r--r--  1 ubuntu ubuntu   2641 May 19 18:43 d112_rsft_no_evidence_eval_r3_analysis.md
-rw-r--r--  1 ubuntu ubuntu   1583 May 19 15:45 d112_rsft_no_evidence_eval_r3_prep.md
-rw-r--r--  1 ubuntu ubuntu   4761 May 21 06:22 d112_rsft_s44_train_prep.md
-rw-r--r--  1 ubuntu ubuntu   1910 May 21 07:40 d140_4b_sft_s42_no_evi_2048_diagnosis.md
-rw-r--r--  1 ubuntu ubuntu   1398 May 21 09:12 d140_progress_check.md
-rw-r--r--  1 ubuntu ubuntu   1233 May 21 21:10 dev_test_gap_paragraph.md
-rw-r--r--  1 ubuntu ubuntu   1874 May 14 15:15 diag_mvp2_grpo_flatnli_r3.md
-rw-r--r--  1 ubuntu ubuntu   4297 May 19 03:32 diag_plan019_1_7b_rsft_s43.md
-rw-r--r--  1 ubuntu ubuntu   4469 May 16 17:47 diag_redocred_rsft_r2.md
-rw-r--r--  1 ubuntu ubuntu   1702 May 17 01:54 diagnose_8b_timeout.md
-rw-r--r--  1 ubuntu ubuntu    967 May 21 07:13 diagnose_eval_llama_rsft_s42_with_evidence_2048.md
-rw-r--r--  1 ubuntu ubuntu   2220 May 20 11:30 diagnose_eval_llama_sft_s42_no_evidence_std.md
-rw-r--r--  1 ubuntu ubuntu   2765 May 15 15:21 diagnose_plan_001.md
-rw-r--r--  1 ubuntu ubuntu  16718 May 14 23:37 diversity_probe.py
-rw-r--r--  1 ubuntu ubuntu   4532 May 14 23:51 diversity_probe_results.md
drwxr-xr-x  6 ubuntu ubuntu   4096 May 16 16:31 dream_reports
-rw-r--r--  1 ubuntu ubuntu   3730 May 17 13:04 dreeam_evif1_alignment_report.md
-rw-r--r--  1 ubuntu ubuntu   6178 May 15 18:12 edcr_analysis.md
-rw-r--r--  1 ubuntu ubuntu   4468 May 15 11:56 edcr_analysis_r2b.md
-rw-r--r--  1 ubuntu ubuntu   9886 May 15 19:55 edcr_diagnostic_table.md
-rw-r--r--  1 ubuntu ubuntu   2421 May 16 04:16 eval_plan_014_no_evidence_r2_analysis.md
-rw-r--r--  1 ubuntu ubuntu   1165 May 16 03:31 eval_progress_20260516.md
-rw-r--r--  1 ubuntu ubuntu   3222 May 15 11:33 eval_progress_check_0515.md
drwxr-xr-x  3 ubuntu ubuntu   4096 May 16 05:18 eval_rsft_ced_s43
drwxr-xr-x  3 ubuntu ubuntu   4096 May 16 04:23 eval_rsft_ced_s45
-rw-r--r--  1 ubuntu ubuntu   5541 May 14 14:56 eval_script_audit.md
-rw-r--r--  1 ubuntu ubuntu   3489 May 14 19:05 eval_status_check.md
-rw-r--r--  1 ubuntu ubuntu   6864 May 16 04:23 evidence_cost_literature_scan.md
-rw-r--r--  1 ubuntu ubuntu   7648 May 21 21:11 evidence_tax_annotation_notes.md
-rw-r--r--  1 ubuntu ubuntu   6298 May 16 01:06 experiment_summary_table.md
-rw-r--r--  1 ubuntu ubuntu  33324 May 17 18:46 fig_edcr_relations.pdf
-rw-r--r--  1 ubuntu ubuntu 388230 May 17 18:46 fig_edcr_relations.png
-rw-r--r--  1 ubuntu ubuntu  28446 May 17 18:19 fig_grpo_dynamics.pdf
-rw-r--r--  1 ubuntu ubuntu 233314 May 17 18:19 fig_grpo_dynamics.png
drwxr-xr-x  9 ubuntu ubuntu   4096 May 14 04:59 freige
-rw-r--r--  1 ubuntu ubuntu   8131 May 15 14:59 gap_analysis_w3.md
-rw-r--r--  1 ubuntu ubuntu  41483 May 15 19:11 grpo_forgetting_dynamics.pdf
-rw-r--r--  1 ubuntu ubuntu 360877 May 15 19:11 grpo_forgetting_dynamics.png
-rw-r--r--  1 ubuntu ubuntu   4754 May 14 11:30 kl_analysis_report.md
-rw-r--r--  1 ubuntu ubuntu  15301 May 15 17:56 literature_quantization_rl.md
-rw-r--r--  1 ubuntu ubuntu   8667 May 15 20:17 literature_survey_evidence_overhead.md
-rw-r--r--  1 ubuntu ubuntu  56142 May 21 21:12 manifest.yaml
-rw-r--r--  1 ubuntu ubuntu   2528 May 16 01:09 metrics_summary.csv
-rw-r--r--  1 ubuntu ubuntu   4201 May 16 01:09 metrics_summary_table.md
drwxr-xr-x  3 ubuntu ubuntu   4096 May 15 15:21 mvp2_eval_rsft_r2b_maxtok1536_r2
-rw-r--r--  1 ubuntu ubuntu  12104 May 17 03:57 negative_review.md
-rw-r--r--  1 ubuntu ubuntu  14745 May 21 06:34 next_batch_plan.md
-rw-r--r--  1 ubuntu ubuntu  13030 May 16 02:51 paired_ttest_analysis.py
drwxr-xr-x  3 ubuntu ubuntu   4096 May 16 00:45 paper
-rw-r--r--  1 ubuntu ubuntu  18617 May 16 03:28 paper_evidence_table.md
-rw-r--r--  1 ubuntu ubuntu  12667 May 16 03:37 paper_main_tables_draft.md
-rw-r--r--  1 ubuntu ubuntu   4644 May 16 02:28 paper_metrics_table.md
-rw-r--r--  1 ubuntu ubuntu   3218 May 16 05:25 paper_table1_data.md
-rw-r--r--  1 ubuntu ubuntu   2934 May 19 15:45 plan019_8b_sft_s43_eval_analysis.md
drwxr-xr-x  3 ubuntu ubuntu   4096 May 15 23:10 plan_001_flat_nli_seed45
drwxr-xr-x  3 ubuntu ubuntu   4096 May 15 21:40 plan_003
-rw-r--r--  1 ubuntu ubuntu   7815 May 15 18:25 plan_003_edcr_cross_method_table.md
drwxr-xr-x  4 ubuntu ubuntu   4096 May 15 23:44 plan_003_edcr_diagnostic
-rw-r--r--  1 ubuntu ubuntu   5461 May 15 21:40 plan_003_edcr_diagnostic.md
-rw-r--r--  1 ubuntu ubuntu   2493 May 16 13:54 plan_006_qwen3_1_7b_no_evidence_eval_v3_results.json
drwxr-xr-x  3 ubuntu ubuntu   4096 May 16 17:48 plan_007_redocred_rsft_eval_r2
drwxr-xr-x  5 ubuntu ubuntu   4096 May 15 23:08 plan_009
-rw-r--r--  1 ubuntu ubuntu  11297 May 15 21:15 plan_009_dynamics_data.json
drwxr-xr-x  3 ubuntu ubuntu   4096 May 15 23:17 plan_009_dynamics_figure
-rw-r--r--  1 ubuntu ubuntu   3967 May 15 19:11 plan_009_forgetting_data.csv
-rw-r--r--  1 ubuntu ubuntu   4037 May 15 19:11 plan_009_forgetting_data_v5.csv
drwxr-xr-x  3 ubuntu ubuntu   4096 May 15 23:17 plan_009_forgetting_figure
drwxr-xr-x  5 ubuntu ubuntu   4096 May 15 18:04 plan_009_grpo_forgetting
drwxr-xr-x  4 ubuntu ubuntu   4096 May 15 19:30 plan_012_dpo_ced
-rw-r--r--  1 ubuntu ubuntu   2775 May 15 20:22 plan_012_dpo_ced_1ep_analysis.md
-rw-r--r--  1 ubuntu ubuntu   2889 May 16 00:27 process_check_report.md
drwxr-xr-x  4 ubuntu ubuntu   4096 May 16 07:28 reeval_ced_s42
drwxr-xr-x  3 ubuntu ubuntu   4096 May 16 07:58 reeval_ced_s44
-rw-r--r--  1 ubuntu ubuntu   3278 May 16 04:12 reeval_commands.md
drwxr-xr-x  3 ubuntu ubuntu   4096 May 16 08:01 reeval_flat_nli_s42
drwxr-xr-x  3 ubuntu ubuntu   4096 May 16 06:10 reeval_flat_nli_s43_r2
drwxr-xr-x  3 ubuntu ubuntu   4096 May 16 07:27 reeval_sft_baseline_d076
-rw-r--r--  1 ubuntu ubuntu  13383 May 15 14:43 related_work_gap_analysis.md
drwxr-xr-x  2 ubuntu ubuntu   4096 May 15 23:38 related_work_survey
-rw-r--r--  1 ubuntu ubuntu  11804 May 18 07:44 review_issues.yaml
drwxr-xr-x  2 ubuntu ubuntu   4096 May 18 07:01 review_reports
-rw-r--r--  1 ubuntu ubuntu   1580 May 15 04:06 rsft_gen_progress_check.md
-rw-r--r--  1 ubuntu ubuntu   4978 May 15 04:07 rsft_pipeline_commands.md
-rw-r--r--  1 ubuntu ubuntu   3052 May 14 23:08 status_check_loop4.md
drwxr-xr-x  3 ubuntu ubuntu   4096 May 21 14:59 test_eval_8b_rsft_s42
-rw-r--r--  1 ubuntu ubuntu   9107 May 16 05:22 test_eval_commands.md
-rw-r--r--  1 ubuntu ubuntu    640 May 21 21:09 test_table_draft.md
-rw-r--r--  1 ubuntu ubuntu   4350 May 16 00:32 topk_ablation_lit_review.md
-rw-r--r--  1 ubuntu ubuntu   4548 May 14 14:55 training_health_check.md
-rw-r--r--  1 ubuntu ubuntu   5269 May 14 23:11 training_trajectory_loop4.md
-rw-r--r--  1 ubuntu ubuntu   8531 May 14 10:24 trl_grpo_stability_research.md
-rw-r--r--  1 ubuntu ubuntu   3377 May 18 22:54 worker_check_status.md
---SEPARATOR---
NO_PAPER_DIR
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "6d8f5f13-7b2a-469d-b7e0-9d2e7a94259c",
  "tool_use_result": {
    "stdout": "total 1804\ndrwxr-xr-x 28 ubuntu ubuntu   4096 May 21 21:11 .\ndrwxr-xr-x 11 ubuntu ubuntu   4096 May 21 22:51 ..\n-rw-r--r--  1 ubuntu ubuntu   1808 May 21 09:13 14b_rsft_status.md\n-rw-r--r--  1 ubuntu ubuntu   3935 May 18 07:13 1_7b_repetition_fair_eval.md\ndrwxr-xr-x  7 ubuntu ubuntu   4096 May 16 00:47 _project\n-rw-r--r--  1 ubuntu ubuntu   2284 May 16 00:40 ced_eval_commands.md\n-rw-r--r--  1 ubuntu ubuntu   3346 May 14 18:43 ced_stabilizer_literature_survey.md\n-rw-r--r--  1 ubuntu ubuntu  12584 May 19 08:10 comprehensive_results.md\n-rw-r--r--  1 ubuntu ubuntu   1827 May 15 16:21 cuda3_diagnostic.md\n-rw-r--r--  1 ubuntu ubuntu  18324 May 14 18:43 d024_literature_survey.md\n-rw-r--r--  1 ubuntu ubuntu  13068 May 18 22:06 d076_eval_audit.py\n-rw-r--r--  1 ubuntu ubuntu   7490 May 18 22:07 d076_final_audit.py\n-rw-r--r--  1 ubuntu ubuntu   2637 May 16 05:22 d076_seed_status.md\ndrwxr-xr-x  2 ubuntu ubuntu   4096 May 18 07:14 d102_next_batch\ndrwxr-xr-x  3 ubuntu ubuntu   4096 May 19 18:43 d112\n-rw-r--r--  1 ubuntu ubuntu   3522 May 18 22:57 d112_pipeline_plan.md\n-rw-r--r--  1 ubuntu ubuntu   2641 May 19 18:43 d112_rsft_no_evidence_eval_r3_analysis.md\n-rw-r--r--  1 ubuntu ubuntu   1583 May 19 15:45 d112_rsft_no_evidence_eval_r3_prep.md\n-rw-r--r--  1 ubuntu ubuntu   4761 May 21 06:22 d112_rsft_s44_train_prep.md\n-rw-r--r--  1 ubuntu ubuntu   1910 May 21 07:40 d140_4b_sft_s42_no_evi_2048_diagnosis.md\n-rw-r--r--  1 ubuntu ubuntu   1398 May 21 09:12 d140_progress_check.md\n-rw-r--r--  1 ubuntu ubuntu   1233 May 21 21:10 dev_test_gap_paragraph.md\n-rw-r--r--  1 ubuntu ubuntu   1874 May 14 15:15 diag_mvp2_grpo_flatnli_r3.md\n-rw-r--r--  1 ubuntu ubuntu   4297 May 19 03:32 diag_plan019_1_7b_rsft_s43.md\n-rw-r--r--  1 ubuntu ubuntu   4469 May 16 17:47 diag_redocred_rsft_r2.md\n-rw-r--r--  1 ubuntu ubuntu   1702 May 17 01:54 diagnose_8b_timeout.md\n-rw-r--r--  1 ubuntu ubuntu    967 May 21 07:13 diagnose_eval_llama_rsft_s42_with_evidence_2048.md\n-rw-r--r--  1 ubuntu ubuntu   2220 May 20 11:30 diagnose_eval_llama_sft_s42_no_evidence_std.md\n-rw-r--r--  1 ubuntu ubuntu   2765 May 15 15:21 diagnose_plan_001.md\n-rw-r--r--  1 ubuntu ubuntu  16718 May 14 23:37 diversity_probe.py\n-rw-r--r--  1 ubuntu ubuntu   4532 May 14 23:51 diversity_probe_results.md\ndrwxr-xr-x  6 ubuntu ubuntu   4096 May 16 16:31 dream_reports\n-rw-r--r--  1 ubuntu ubuntu   3730 May 17 13:04 dreeam_evif1_alignment_report.md\n-rw-r--r--  1 ubuntu ubuntu   6178 May 15 18:12 edcr_analysis.md\n-rw-r--r--  1 ubuntu ubuntu   4468 May 15 11:56 edcr_analysis_r2b.md\n-rw-r--r--  1 ubuntu ubuntu   9886 May 15 19:55 edcr_diagnostic_table.md\n-rw-r--r--  1 ubuntu ubuntu   2421 May 16 04:16 eval_plan_014_no_evidence_r2_analysis.md\n-rw-r--r--  1 ubuntu ubuntu   1165 May 16 03:31 eval_progress_20260516.md\n-rw-r--r--  1 ubuntu ubuntu   3222 May 15 11:33 eval_progress_check_0515.md\ndrwxr-xr-x  3 ubuntu ubuntu   4096 May 16 05:18 eval_rsft_ced_s43\ndrwxr-xr-x  3 ubuntu ubuntu   4096 May 16 04:23 eval_rsft_ced_s45\n-rw-r--r--  1 ubuntu ubuntu   5541 May 14 14:56 eval_script_audit.md\n-rw-r--r--  1 ubuntu ubuntu   3489 May 14 19:05 eval_status_check.md\n-rw-r--r--  1 ubuntu ubuntu   6864 May 16 04:23 evidence_cost_literature_scan.md\n-rw-r--r--  1 ubuntu ubuntu   7648 May 21 21:11 evidence_tax_annotation_notes.md\n-rw-r--r--  1 ubuntu ubuntu   6298 May 16 01:06 experiment_summary_table.md\n-rw-r--r--  1 ubuntu ubuntu  33324 May 17 18:46 fig_edcr_relations.pdf\n-rw-r--r--  1 ubuntu ubuntu 388230 May 17 18:46 fig_edcr_relations.png\n-rw-r--r--  1 ubuntu ubuntu  28446 May 17 18:19 fig_grpo_dynamics.pdf\n-rw-r--r--  1 ubuntu ubuntu 233314 May 17 18:19 fig_grpo_dynamics.png\ndrwxr-xr-x  9 ubuntu ubuntu   4096 May 14 04:59 freige\n-rw-r--r--  1 ubuntu ubuntu   8131 May 15 14:59 gap_analysis_w3.md\n-rw-r--r--  1 ubuntu ubuntu  41483 May 15 19:11 grpo_forgetting_dynamics.pdf\n-rw-r--r--  1 ubuntu ubuntu 360877 May 15 19:11 grpo_forgetting_dynamics.png\n-rw-r--r--  1 ubuntu ubuntu   4754 May 14 11:30 kl_analysis_report.md\n-rw-r--r--  1 ubuntu ubuntu  15301 May 15 17:56 literature_quantization_rl.md\n-rw-r--r--  1 ubuntu ubuntu   8667 May 15 20:17 literature_survey_evidence_overhead.md\n-rw-r--r--  1 ubuntu ubuntu  56142 May 21 21:12 manifest.yaml\n-rw-r--r--  1 ubuntu ubuntu   2528 May 16 01:09 metrics_summary.csv\n-rw-r--r--  1 ubuntu ubuntu   4201 May 16 01:09 metrics_summary_table.md\ndrwxr-xr-x  3 ubuntu ubuntu   4096 May 15 15:21 mvp2_eval_rsft_r2b_maxtok1536_r2\n-rw-r--r--  1 ubuntu ubuntu  12104 May 17 03:57 negative_review.md\n-rw-r--r--  1 ubuntu ubuntu  14745 May 21 06:34 next_batch_plan.md\n-rw-r--r--  1 ubuntu ubuntu  13030 May 16 02:51 paired_ttest_analysis.py\ndrwxr-xr-x  3 ubuntu ubuntu   4096 May 16 00:45 paper\n-rw-r--r--  1 ubuntu ubuntu  18617 May 16 03:28 paper_evidence_table.md\n-rw-r--r--  1 ubuntu ubuntu  12667 May 16 03:37 paper_main_tables_draft.md\n-rw-r--r--  1 ubuntu ubuntu   4644 May 16 02:28 paper_metrics_table.md\n-rw-r--r--  1 ubuntu ubuntu   3218 May 16 05:25 paper_table1_data.md\n-rw-r--r--  1 ubuntu ubuntu   2934 May 19 15:45 plan019_8b_sft_s43_eval_analysis.md\ndrwxr-xr-x  3 ubuntu ubuntu   4096 May 15 23:10 plan_001_flat_nli_seed45\ndrwxr-xr-x  3 ubuntu ubuntu   4096 May 15 21:40 plan_003\n-rw-r--r--  1 ubuntu ubuntu   7815 May 15 18:25 plan_003_edcr_cross_method_table.md\ndrwxr-xr-x  4 ubuntu ubuntu   4096 May 15 23:44 plan_003_edcr_diagnostic\n-rw-r--r--  1 ubuntu ubuntu   5461 May 15 21:40 plan_003_edcr_diagnostic.md\n-rw-r--r--  1 ubuntu ubuntu   2493 May 16 13:54 plan_006_qwen3_1_7b_no_evidence_eval_v3_results.json\ndrwxr-xr-x  3 ubuntu ubuntu   4096 May 16 17:48 plan_007_redocred_rsft_eval_r2\ndrwxr-xr-x  5 ubuntu ubuntu   4096 May 15 23:08 plan_009\n-rw-r--r--  1 ubuntu ubuntu  11297 May 15 21:15 plan_009_dynamics_data.json\ndrwxr-xr-x  3 ubuntu ubuntu   4096 May 15 23:17 plan_009_dynamics_figure\n-rw-r--r--  1 ubuntu ubuntu   3967 May 15 19:11 plan_009_forgetting_data.csv\n-rw-r--r--  1 ubuntu ubuntu   4037 May 15 19:11 plan_009_forgetting_data_v5.csv\ndrwxr-xr-x  3 ubuntu ubuntu   4096 May 15 23:17 plan_009_forgetting_figure\ndrwxr-xr-x  5 ubuntu ubuntu   4096 May 15 18:04 plan_009_grpo_forgetting\ndrwxr-xr-x  4 ubuntu ubuntu   4096 May 15 19:30 plan_012_dpo_ced\n-rw-r--r--  1 ubuntu ubuntu   2775 May 15 20:22 plan_012_dpo_ced_1ep_analysis.md\n-rw-r--r--  1 ubuntu ubuntu   2889 May 16 00:27 process_check_report.md\ndrwxr-xr-x  4 ubuntu ubuntu   4096 May 16 07:28 reeval_ced_s42\ndrwxr-xr-x  3 ubuntu ubuntu   4096 May 16 07:58 reeval_ced_s44\n-rw-r--r--  1 ubuntu ubuntu   3278 May 16 04:12 reeval_commands.md\ndrwxr-xr-x  3 ubuntu ubuntu   4096 May 16 08:01 reeval_flat_nli_s42\ndrwxr-xr-x  3 ubuntu ubuntu   4096 May 16 06:10 reeval_flat_nli_s43_r2\ndrwxr-xr-x  3 ubuntu ubuntu   4096 May 16 07:27 reeval_sft_baseline_d076\n-rw-r--r--  1 ubuntu ubuntu  13383 May 15 14:43 related_work_gap_analysis.md\ndrwxr-xr-x  2 ubuntu ubuntu   4096 May 15 23:38 related_work_survey\n-rw-r--r--  1 ubuntu ubuntu  11804 May 18 07:44 review_issues.yaml\ndrwxr-xr-x  2 ubuntu ubuntu   4096 May 18 07:01 review_reports\n-rw-r--r--  1 ubuntu ubuntu   1580 May 15 04:06 rsft_gen_progress_check.md\n-rw-r--r--  1 ubuntu ubuntu   4978 May 15 04:07 rsft_pipeline_commands.md\n-rw-r--r--  1 ubuntu ubuntu   3052 May 14 23:08 status_check_loop4.md\ndrwxr-xr-x  3 ubuntu ubuntu   4096 May 21 14:59 test_eval_8b_rsft_s42\n-rw-r--r--  1 ubuntu ubuntu   9107 May 16 05:22 test_eval_commands.md\n-rw-r--r--  1 ubuntu ubuntu    640 May 21 21:09 test_table_draft.md\n-rw-r--r--  1 ubuntu ubuntu   4350 May 16 00:32 topk_ablation_lit_review.md\n-rw-r--r--  1 ubuntu ubuntu   4548 May 14 14:55 training_health_check.md\n-rw-r--r--  1 ubuntu ubuntu   5269 May 14 23:11 training_trajectory_loop4.md\n-rw-r--r--  1 ubuntu ubuntu   8531 May 14 10:24 trl_grpo_stability_research.md\n-rw-r--r--  1 ubuntu ubuntu   3377 May 18 22:54 worker_check_status.md\n---SEPARATOR---\nNO_PAPER_DIR",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Glob · `toolu_01NuZvR63eSbEQWtr34GNzd1`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "8e39be6d-4ea0-430f-91a0-e4b44c79f774",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01REjY5RsbGwFzndCDdN7MLv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12899,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12899
      },
      "output_tokens": 26,
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

_source line 8 · 2026-05-21T22:55:56.585Z_

<details><summary>↩ Tool result · `toolu_01NuZvR63eSbEQWtr34GNzd1`</summary>

```text
artifacts/freige/__init__.py
artifacts/freige/data/__init__.py
artifacts/freige/rewards/__init__.py
artifacts/freige/analysis/__init__.py
artifacts/freige/eval/__init__.py
artifacts/freige/data/docred_processor.py
artifacts/freige/rewards/ced_reward.py
artifacts/freige/data/__pycache__/docred_processor.cpython-314.pyc
artifacts/freige/rewards/__pycache__/ced_reward.cpython-314.pyc
artifacts/_project/intermediate/freige_codebase_manifest.txt
artifacts/freige/analysis/__pycache__/ced_signal_validation.cpython-314.pyc
artifacts/freige/configs/deepspeed_zero2.json
artifacts/freige/configs/deepspeed_zero3.json
artifacts/freige/training/__pycache__/sft_trainer.cpython-314.pyc
artifacts/freige/training/__pycache__/grpo_trainer.cpython-314.pyc
artifacts/freige/training/__pycache__/smoke_test.cpython-314.pyc
artifacts/freige/eval/__pycache__/evaluator.cpython-314.pyc
artifacts/freige/__pycache__/__init__.cpython-314.pyc
artifacts/freige/eval/__pycache__/__init__.cpython-314.pyc
artifacts/freige/data/__pycache__/__init__.cpython-314.pyc
artifacts/freige/analysis/ced_signal_validation.py
artifacts/freige/configs/accelerate_4gpu.yaml
artifacts/_project/report/trl_grpo_stability_research.md
artifacts/trl_grpo_stability_research.md
artifacts/kl_analysis_report.md
artifacts/training_health_check.md
artifacts/eval_script_audit.md
artifacts/freige/eval/find_best_checkpoint.py
artifacts/freige/eval/batch_eval.py
artifacts/diag_mvp2_grpo_flatnli_r3.md
artifacts/_project/report/d024_literature_survey.md
artifacts/d024_literature_survey.md
artifacts/ced_stabilizer_literature_survey.md
artifacts/eval_status_check.md
artifacts/status_check_loop4.md
artifacts/training_trajectory_loop4.md
artifacts/diversity_probe.py
artifacts/diversity_probe_results.md
artifacts/freige/training/rsft_score_filter.py
artifacts/freige/training/merge_shards.py
artifacts/rsft_gen_progress_check.md
artifacts/rsft_pipeline_commands.md
artifacts/eval_progress_check_0515.md
artifacts/_project/report/edcr_analysis_r2b.md
artifacts/edcr_analysis_r2b.md
artifacts/dream_reports/dream_20260515T120227/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260515T120227/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260515T120227/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260515T120227/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260515T120227/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T120227/best/experiment_data.json
artifacts/dream_reports/dream_20260515T120227/best/paper_framing.md
artifacts/dream_reports/dream_20260515T120227/best/paper.tex
artifacts/dream_reports/dream_20260515T120227/best/paper.aux
artifacts/dream_reports/dream_20260515T120227/best/paper.out
artifacts/dream_reports/dream_20260515T120227/best/paper.pdf
artifacts/dream_reports/dream_20260515T120227/best/paper.log
artifacts/dream_reports/dream_20260515T120227/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260515T120227/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T120227/median/experiment_data.json
artifacts/dream_reports/dream_20260515T120227/median/paper_framing.md
artifacts/dream_reports/dream_20260515T120227/median/paper.tex
artifacts/dream_reports/dream_20260515T120227/median/paper.aux
artifacts/dream_reports/dream_20260515T120227/median/paper.out
artifacts/dream_reports/dream_20260515T120227/median/paper.pdf
artifacts/dream_reports/dream_20260515T120227/median/paper.log
artifacts/dream_reports/dream_20260515T120227/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260515T120227/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T120227/worst/experiment_data.json
artifacts/dream_reports/dream_20260515T120227/worst/paper_framing.md
artifacts/dream_reports/dream_20260515T120227/worst/paper.tex
artifacts/dream_reports/dream_20260515T120227/worst/paper.aux
artifacts/dream_reports/dream_20260515T120227/worst/paper.out
artifacts/dream_reports/dream_20260515T120227/worst/paper.pdf
artifacts/dream_reports/dream_20260515T120227/worst/paper.log
artifacts/dream_reports/dream_20260515T120227/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260515T120227/best/review_context.yaml
artifacts/dream_reports/dream_20260515T120227/logs/orchestrator.log
artifacts/dream_reports/dream_20260515T120227/logs/review_best.log
artifacts/dream_reports/dream_20260515T120227/median/review_context.yaml
artifacts/dream_reports/dream_20260515T120227/logs/review_median.log
artifacts/dream_reports/dream_20260515T120227/worst/review_context.yaml
artifacts/dream_reports/dream_20260515T120227/median/review_report.md
artifacts/dream_reports/dream_20260515T120227/best/review_report.md
artifacts/dream_reports/dream_20260515T120227/worst/review_report.md
artifacts/dream_reports/dream_20260515T120227/logs/review_worst.log
artifacts/dream_reports/dream_20260515T120227/meta.yaml
artifacts/dream_reports/dream_20260515T132059/logs/orchestrator.log
artifacts/dream_reports/dream_20260515T132059/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260515T132059/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260515T132059/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260515T132059/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260515T132059/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T132059/best/experiment_data.json
artifacts/dream_reports/dream_20260515T132059/best/paper_framing.md
artifacts/dream_reports/dream_20260515T132059/best/paper.tex
artifacts/dream_reports/dream_20260515T132059/best/paper.aux
artifacts/dream_reports/dream_20260515T132059/best/paper.out
artifacts/dream_reports/dream_20260515T132059/best/paper.pdf
artifacts/dream_reports/dream_20260515T132059/best/paper.log
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "da0f4290-c878-421c-9551-4b4b6288df03",
  "tool_use_result": {
    "filenames": [
      "artifacts/freige/__init__.py",
      "artifacts/freige/data/__init__.py",
      "artifacts/freige/rewards/__init__.py",
      "artifacts/freige/analysis/__init__.py",
      "artifacts/freige/eval/__init__.py",
      "artifacts/freige/data/docred_processor.py",
      "artifacts/freige/rewards/ced_reward.py",
      "artifacts/freige/data/__pycache__/docred_processor.cpython-314.pyc",
      "artifacts/freige/rewards/__pycache__/ced_reward.cpython-314.pyc",
      "artifacts/_project/intermediate/freige_codebase_manifest.txt",
      "artifacts/freige/analysis/__pycache__/ced_signal_validation.cpython-314.pyc",
      "artifacts/freige/configs/deepspeed_zero2.json",
      "artifacts/freige/configs/deepspeed_zero3.json",
      "artifacts/freige/training/__pycache__/sft_trainer.cpython-314.pyc",
      "artifacts/freige/training/__pycache__/grpo_trainer.cpython-314.pyc",
      "artifacts/freige/training/__pycache__/smoke_test.cpython-314.pyc",
      "artifacts/freige/eval/__pycache__/evaluator.cpython-314.pyc",
      "artifacts/freige/__pycache__/__init__.cpython-314.pyc",
      "artifacts/freige/eval/__pycache__/__init__.cpython-314.pyc",
      "artifacts/freige/data/__pycache__/__init__.cpython-314.pyc",
      "artifacts/freige/analysis/ced_signal_validation.py",
      "artifacts/freige/configs/accelerate_4gpu.yaml",
      "artifacts/_project/report/trl_grpo_stability_research.md",
      "artifacts/trl_grpo_stability_research.md",
      "artifacts/kl_analysis_report.md",
      "artifacts/training_health_check.md",
      "artifacts/eval_script_audit.md",
      "artifacts/freige/eval/find_best_checkpoint.py",
      "artifacts/freige/eval/batch_eval.py",
      "artifacts/diag_mvp2_grpo_flatnli_r3.md",
      "artifacts/_project/report/d024_literature_survey.md",
      "artifacts/d024_literature_survey.md",
      "artifacts/ced_stabilizer_literature_survey.md",
      "artifacts/eval_status_check.md",
      "artifacts/status_check_loop4.md",
      "artifacts/training_trajectory_loop4.md",
      "artifacts/diversity_probe.py",
      "artifacts/diversity_probe_results.md",
      "artifacts/freige/training/rsft_score_filter.py",
      "artifacts/freige/training/merge_shards.py",
      "artifacts/rsft_gen_progress_check.md",
      "artifacts/rsft_pipeline_commands.md",
      "artifacts/eval_progress_check_0515.md",
      "artifacts/_project/report/edcr_analysis_r2b.md",
      "artifacts/edcr_analysis_r2b.md",
      "artifacts/dream_reports/dream_20260515T120227/logs/phase1_attempt0.log",
      "artifacts/dream_reports/dream_20260515T120227/logs/phase2_best_attempt0.log",
      "artifacts/dream_reports/dream_20260515T120227/logs/phase2_median_attempt0.log",
      "artifacts/dream_reports/dream_20260515T120227/logs/phase2_worst_attempt0.log",
      "artifacts/dream_reports/dream_20260515T120227/best/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260515T120227/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260515T120227/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260515T120227/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T120227/best/paper.aux",
      "artifacts/dream_reports/dream_20260515T120227/best/paper.out",
      "artifacts/dream_reports/dream_20260515T120227/best/paper.pdf",
      "artifacts/dream_reports/dream_20260515T120227/best/paper.log",
      "artifacts/dream_reports/dream_20260515T120227/logs/paper_agent_best.log",
      "artifacts/dream_reports/dream_20260515T120227/median/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260515T120227/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260515T120227/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260515T120227/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T120227/median/paper.aux",
      "artifacts/dream_reports/dream_20260515T120227/median/paper.out",
      "artifacts/dream_reports/dream_20260515T120227/median/paper.pdf",
      "artifacts/dream_reports/dream_20260515T120227/median/paper.log",
      "artifacts/dream_reports/dream_20260515T120227/logs/paper_agent_median.log",
      "artifacts/dream_reports/dream_20260515T120227/worst/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260515T120227/worst/experiment_data.json",
      "artifacts/dream_reports/dream_20260515T120227/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260515T120227/worst/paper.tex",
      "artifacts/dream_reports/dream_20260515T120227/worst/paper.aux",
      "artifacts/dream_reports/dream_20260515T120227/worst/paper.out",
      "artifacts/dream_reports/dream_20260515T120227/worst/paper.pdf",
      "artifacts/dream_reports/dream_20260515T120227/worst/paper.log",
      "artifacts/dream_reports/dream_20260515T120227/logs/paper_agent_worst.log",
      "artifacts/dream_reports/dream_20260515T120227/best/review_context.yaml",
      "artifacts/dream_reports/dream_20260515T120227/logs/orchestrator.log",
      "artifacts/dream_reports/dream_20260515T120227/logs/review_best.log",
      "artifacts/dream_reports/dream_20260515T120227/median/review_context.yaml",
      "artifacts/dream_reports/dream_20260515T120227/logs/review_median.log",
      "artifacts/dream_reports/dream_20260515T120227/worst/review_context.yaml",
      "artifacts/dream_reports/dream_20260515T120227/median/review_report.md",
      "artifacts/dream_reports/dream_20260515T120227/best/review_report.md",
      "artifacts/dream_reports/dream_20260515T120227/worst/review_report.md",
      "artifacts/dream_reports/dream_20260515T120227/logs/review_worst.log",
      "artifacts/dream_reports/dream_20260515T120227/meta.yaml",
      "artifacts/dream_reports/dream_20260515T132059/logs/orchestrator.log",
      "artifacts/dream_reports/dream_20260515T132059/logs/phase1_attempt0.log",
      "artifacts/dream_reports/dream_20260515T132059/logs/phase2_best_attempt0.log",
      "artifacts/dream_reports/dream_20260515T132059/logs/phase2_median_attempt0.log",
      "artifacts/dream_reports/dream_20260515T132059/logs/phase2_worst_attempt0.log",
      "artifacts/dream_reports/dream_20260515T132059/best/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260515T132059/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260515T132059/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260515T132059/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T132059/best/paper.aux",
      "artifacts/dream_reports/dream_20260515T132059/best/paper.out",
      "artifacts/dream_reports/dream_20260515T132059/best/paper.pdf",
      "artifacts/dream_reports/dream_20260515T132059/best/paper.log"
    ],
    "durationMs": 11,
    "numFiles": 100,
    "truncated": true
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Let me read the key paper-related files to understand the current state. I need to check:
1. paper_framing.md (if exists)
2. writing_plan.yaml (if exists)
3. test_table_draft.md
4. evidence_tax_annotation_notes.md
5. dev_test_gap_paragraph.md
6. paper_main_tables_draft.md
7. comprehensive_results.md
8. paper_evidence_table.md
9. negative_review.md
10. review_issues.yaml

Let me read several of these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "cc54432d-b4c8-4a45-a948-69e497889177",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrSYXG3X2RG6iDzESuXvkp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6171,
      "cache_read_input_tokens": 24346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6171
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

_source line 10_

读取关键文件，了解论文当前状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "947c0e08-012f-43ea-9fa1-0749331218ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrSYXG3X2RG6iDzESuXvkp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6171,
      "cache_read_input_tokens": 24346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6171
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

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01Pj1iVbppTgcwY4Ns8SroQw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/test_table_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "a9ec5e11-fabc-4219-8491-0b382b8cf4d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrSYXG3X2RG6iDzESuXvkp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6171,
      "cache_read_input_tokens": 24346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6171
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

_source line 12 · 2026-05-21T22:56:04.914Z_

<details><summary>↩ Tool result · `toolu_01Pj1iVbppTgcwY4Ns8SroQw`</summary>

```text
1	# Test Set Scaling Table (Re-DocRED)
2	
3	| Model | SFT test ign_f1 | RSFT test ign_f1 | Δ (RSFT−SFT) | evi_f1_joint | edcr | Trunc.% |
4	|:------|:---------------:|:----------------:|:------------:|:------------:|:----:|:-------:|
5	| Qwen3-1.7B | *(pending)* | 0.2933 | — | 0.2320 | 0.8169 | 73.8 |
6	| Qwen3-4B | *(running)* | —† | — | — | — | — |
7	| Qwen3-8B | *(running)* | 0.3353 | — | 0.2526 | 0.7993 | 1.8 |
8	| Qwen3-14B | *(running)* | 0.3849 | — | 0.2688 | 0.7865 | 13.4 |
9	| LLaMA-3.1-8B | *(running)* | 0.3599 | — | 0.2509 | 0.8391 | 56.6 |
10	
11	† 4B RSFT s42 checkpoint irrecoverable; dev ign_f1=0.4482 (Method A, N=3)
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "b813b279-f249-4094-8966-daa261a73f9d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/test_table_draft.md",
      "content": "# Test Set Scaling Table (Re-DocRED)\n\n| Model | SFT test ign_f1 | RSFT test ign_f1 | Δ (RSFT−SFT) | evi_f1_joint | edcr | Trunc.% |\n|:------|:---------------:|:----------------:|:------------:|:------------:|:----:|:-------:|\n| Qwen3-1.7B | *(pending)* | 0.2933 | — | 0.2320 | 0.8169 | 73.8 |\n| Qwen3-4B | *(running)* | —† | — | — | — | — |\n| Qwen3-8B | *(running)* | 0.3353 | — | 0.2526 | 0.7993 | 1.8 |\n| Qwen3-14B | *(running)* | 0.3849 | — | 0.2688 | 0.7865 | 13.4 |\n| LLaMA-3.1-8B | *(running)* | 0.3599 | — | 0.2509 | 0.8391 | 56.6 |\n\n† 4B RSFT s42 checkpoint irrecoverable; dev ign_f1=0.4482 (Method A, N=3)\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01NSvUKzUYmwFH2YCWyUrAji`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/evidence_tax_annotation_notes.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "39fdc08b-6fc7-446f-ba25-bf76ceceac99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrSYXG3X2RG6iDzESuXvkp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6171,
      "cache_read_input_tokens": 24346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6171
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

_source line 14 · 2026-05-21T22:56:05.714Z_

<details><summary>↩ Tool result · `toolu_01NSvUKzUYmwFH2YCWyUrAji`</summary>

```text
1	# Evidence Tax Annotation Audit
2	
3	**Date**: 2026-05-21  
4	**Scope**: All evidence tax numbers in `docs/paper/sections/*.tex`
5	
6	---
7	
8	## Executive Summary
9	
10	The paper has a blanket dev-set statement (`experiments.tex:17`: "All results use the development set") and table captions say "DocRED dev Ign-F1." However, the **matched@2048 fair_tax numbers from D144/D146 are NOT in the paper**. The paper still uses the old, invalidated +7.5pp at 4B and the old -6.2pp controlled-subset number at 1.7B. The corrected fair_tax values and "matched 2048-token budget" methodology have not been incorporated.
11	
12	---
13	
14	## Part 1: Numbers NOT Yet in the Paper (Must Add)
15	
16	The following corrected fair_tax numbers (matched@2048 fair comparison, from D144/D145/D146) do not appear anywhere in the .tex files:
17	
18	| Model | fair_tax (matched@2048) | Status in paper |
19	|-------|------------------------|-----------------|
20	| Qwen3-1.7B | **-5.63pp** | Paper uses -6.2pp (old controlled subset, not matched@2048) |
21	| Qwen3-4B | **+0.25±0.47pp** (3-seed) | Paper uses +7.5pp (**INVALIDATED by D144**) |
22	| Qwen3-8B | **+0.04pp** | Paper uses +0.28pp (training-time, s42 only) |
23	| LLaMA-3.1-8B SFT | Unstable (s42=+1.35, s44=-12.62) | Paper uses +0.68pp (s42 only) |
24	| LLaMA-3.1-8B RSFT | **-1.14±0.76pp** (3-seed) | Paper uses -1.52pp (2-seed mean) |
25	| Qwen3-14B RSFT | **-4.54pp** (@1024, truncation symmetric) | Not in paper |
26	| Variance compression | 1.7B 31×, 4B 7.5×, 8B 17×, LLaMA 4.6× | ✅ Already in paper, correct |
27	
28	---
29	
30	## Part 2: Locations Requiring Modification
31	
32	### 2.1 CRITICAL — 4B evidence tax still says +7.5pp (invalidated by D144)
33	
34	**File**: `docs/paper/sections/abstract.tex:11`  
35	**Current**: `the evidence tax varies from beneficial ($-$6.2pp Ign-F1 on a controlled subset at 1.7B) to costly (+7.5pp at 4B) to negligible at $\geq$8B`  
36	**Issue**: +7.5pp invalidated; -6.2pp should be updated to matched@2048 value (-5.63pp)  
37	**Suggested**: `the evidence tax varies from beneficial ($-$5.6pp Ign-F1 at 1.7B) to negligible at $\geq$4B (+0.25$\pm$0.47pp at 4B, +0.04pp at 8B) on the development set with matched 2048-token generation budget`
38	
39	**File**: `docs/paper/sections/introduction.tex:24`  
40	**Current**: `evidence generation provides implicit regularization at 1.7B ($-$6.2pp Ign-F1 on a controlled evaluation subset), imposes a substantial cost at 4B (+7.5pp), and approaches zero at $\geq$8B parameters`  
41	**Issue**: Same — +7.5pp invalidated, -6.2pp outdated  
42	**Suggested**: `evidence generation provides implicit regularization at 1.7B ($-$5.6pp Ign-F1) and approaches zero at $\geq$4B (+0.25$\pm$0.47pp at 4B, +0.04pp at 8B), measured on the development set with matched 2048-token generation budget (fair comparison subset)`
43	
44	**File**: `docs/paper/sections/introduction.tex:30` (contribution list)  
45	**Current**: `varies from beneficial ($-$6.2pp at 1.7B) to costly (+7.5pp at 4B) to negligible ($\geq$8B)`  
46	**Issue**: Same invalidated numbers  
47	**Suggested**: `varies from beneficial ($-$5.6pp at 1.7B) to negligible at $\geq$4B (+0.25$\pm$0.47pp at 4B, +0.04pp at 8B)`
48	
49	**File**: `docs/paper/sections/conclusion.tex:4`  
50	**Current**: `model capacity determines whether evidence acts as regularizer ($-$6.2pp at 1.7B) or burden (+7.5pp at 4B)`  
51	**Issue**: Same invalidated numbers  
52	**Suggested**: `model capacity determines whether evidence acts as regularizer ($-$5.6pp at 1.7B) or is absorbed at $\geq$4B (+0.25pp at 4B, near-zero at 8B)`
53	
54	**File**: `docs/paper/sections/experiments.tex:92`  
55	**Current**: `the tax varies from beneficial at 1.7B ($-$6.2pp on a controlled subset; Appendix~\ref{sec:fair_subset}) to costly at 4B (+7.5pp) to negligible at $\geq$8B`  
56	**Issue**: Same invalidated numbers. This is the primary evidence tax prose.  
57	**Suggested**: `the tax varies from beneficial at 1.7B ($-$5.63pp on a matched-budget fair comparison subset; Appendix~\ref{sec:fair_subset}) to negligible at $\geq$4B (+0.25$\pm$0.47pp 3-seed mean at 4B, +0.04pp at 8B)`
58	
59	### 2.2 Narrative Change — "non-monotonic" / "capacity valley" invalidated
60	
61	The D144 correction (4B from +7.5pp → +0.25pp) eliminates the "costly at 4B" narrative. Per `paper_framing.md:141`, the new framing is **within-family capacity threshold** (1.7B benefits, ≥4B neutral) rather than non-monotonic curve. Check all instances of "costly" or "non-monotonic" language around 4B.
62	
63	### 2.3 Token Budget Annotation — Missing "matched 2048-token budget"
64	
65	The paper currently describes **mismatched** token budgets in Table 3 footnote (`experiments.tex:119`): no-evi@2048, with-evi@1024. The fair_tax numbers use **matched@2048** for both conditions. If incorporating fair_tax, the methodology must be explained:
66	
67	**Suggested footnote/methodology text** (first occurrence, e.g., §4.4):  
68	> "All evidence tax values reported in this section are computed on the development set using a matched 2048-token generation budget for both with-evidence and no-evidence conditions, evaluated on the format-compliant document intersection (fair comparison subset) to control for differential truncation rates."
69	
70	**Suggested table footnote** (for any fair_tax table):  
71	> "Dev set, matched @2048, fair comparison subset."
72	
73	### 2.4 Existing Dev-Set Annotations (Already Adequate)
74	
75	| Location | Annotation | Status |
76	|----------|-----------|--------|
77	| `experiments.tex:17` | "All results use the development set." | ✅ Blanket statement |
78	| `experiments.tex:102` (Table 3 caption) | "DocRED dev Ign-F1" | ✅ |
79	| `appendix.tex:145` (Table 8 caption) | "DocRED dev Ign-F1, s42 paired" | ✅ |
80	| `limitations.tex:3` | "All results use the DocRED development set; test set submission is pending." | ✅ |
81	| `appendix.tex:52,91,204` (other table captions) | "DocRED dev set" | ✅ |
82	
83	### 2.5 14B RSFT Evidence Tax (-4.54pp) — Not in Paper
84	
85	`paper_framing.md:167` documents 14B RSFT tax = -4.54pp (evidence strongly beneficial, truncation symmetric so @1024 is valid). This number does not appear in any .tex file. If adding it to Table 3 or the 14B row, annotate as: "Dev set, @1024 (truncation symmetric: no-evi 10.8% vs with-evi 10.7%)."
86	
87	### 2.6 LLaMA RSFT Tax — Paper Has 2-Seed, Now 3-Seed Available
88	
89	**File**: `docs/paper/sections/experiments.tex:114` (Table 3, LLaMA row)  
90	**Current**: `$-$1.52$^\ddagger$` with footnote "Two-seed mean (s42: $-$1.88, s43: $-$1.16); s44 pending."  
91	**Corrected value**: -1.14±0.76pp (3-seed mean, per D135/paper_framing.md:154)  
92	**Action**: Update to 3-seed value if s44 data is finalized.
93	
94	---
95	
96	## Part 3: Variance Compression Numbers — Already Correct
97	
98	The variance compression numbers (1.7B 31×, 4B 7.5×, 8B 17×, LLaMA 4.6×) appear correctly in:
99	- `experiments.tex:96` (main text)
100	- `abstract.tex:15`
101	- `introduction.tex:26`
102	- `analysis.tex:14`
103	- `conclusion.tex:4` (as "7.5--17×" and "4.6×")
104	
105	These are adequately covered by the blanket "All results use the development set" statement. No additional per-number annotation needed.
106	
107	---
108	
109	## Summary of Required Actions
110	
111	1. **CRITICAL**: Replace all instances of +7.5pp (4B) with +0.25±0.47pp — 5 locations (abstract, intro×2, experiments, conclusion)
112	2. **CRITICAL**: Update -6.2pp (1.7B) to -5.63pp (matched@2048) — same 5 locations
113	3. **ADD**: Matched@2048 methodology explanation in §4.4 or Appendix controlled subset section
114	4. **ADD**: "fair comparison subset" annotation wherever fair_tax numbers appear
115	5. **UPDATE**: LLaMA RSFT tax from 2-seed -1.52pp to 3-seed -1.14±0.76pp (Table 3)
116	6. **CONSIDER**: Adding 14B RSFT tax (-4.54pp) to Table 3
117	7. **NARRATIVE**: Revise "costly at 4B" / "non-monotonic" language → "within-family capacity threshold"
118	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "85974e51-8b00-4c51-a170-fa2d740d97e9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/evidence_tax_annotation_notes.md",
      "content": "# Evidence Tax Annotation Audit\n\n**Date**: 2026-05-21  \n**Scope**: All evidence tax numbers in `docs/paper/sections/*.tex`\n\n---\n\n## Executive Summary\n\nThe paper has a blanket dev-set statement (`experiments.tex:17`: \"All results use the development set\") and table captions say \"DocRED dev Ign-F1.\" However, the **matched@2048 fair_tax numbers from D144/D146 are NOT in the paper**. The paper still uses the old, invalidated +7.5pp at 4B and the old -6.2pp controlled-subset number at 1.7B. The corrected fair_tax values and \"matched 2048-token budget\" methodology have not been incorporated.\n\n---\n\n## Part 1: Numbers NOT Yet in the Paper (Must Add)\n\nThe following corrected fair_tax numbers (matched@2048 fair comparison, from D144/D145/D146) do not appear anywhere in the .tex files:\n\n| Model | fair_tax (matched@2048) | Status in paper |\n|-------|------------------------|-----------------|\n| Qwen3-1.7B | **-5.63pp** | Paper uses -6.2pp (old controlled subset, not matched@2048) |\n| Qwen3-4B | **+0.25±0.47pp** (3-seed) | Paper uses +7.5pp (**INVALIDATED by D144**) |\n| Qwen3-8B | **+0.04pp** | Paper uses +0.28pp (training-time, s42 only) |\n| LLaMA-3.1-8B SFT | Unstable (s42=+1.35, s44=-12.62) | Paper uses +0.68pp (s42 only) |\n| LLaMA-3.1-8B RSFT | **-1.14±0.76pp** (3-seed) | Paper uses -1.52pp (2-seed mean) |\n| Qwen3-14B RSFT | **-4.54pp** (@1024, truncation symmetric) | Not in paper |\n| Variance compression | 1.7B 31×, 4B 7.5×, 8B 17×, LLaMA 4.6× | ✅ Already in paper, correct |\n\n---\n\n## Part 2: Locations Requiring Modification\n\n### 2.1 CRITICAL — 4B evidence tax still says +7.5pp (invalidated by D144)\n\n**File**: `docs/paper/sections/abstract.tex:11`  \n**Current**: `the evidence tax varies from beneficial ($-$6.2pp Ign-F1 on a controlled subset at 1.7B) to costly (+7.5pp at 4B) to negligible at $\\geq$8B`  \n**Issue**: +7.5pp invalidated; -6.2pp should be updated to matched@2048 value (-5.63pp)  \n**Suggested**: `the evidence tax varies from beneficial ($-$5.6pp Ign-F1 at 1.7B) to negligible at $\\geq$4B (+0.25$\\pm$0.47pp at 4B, +0.04pp at 8B) on the development set with matched 2048-token generation budget`\n\n**File**: `docs/paper/sections/introduction.tex:24`  \n**Current**: `evidence generation provides implicit regularization at 1.7B ($-$6.2pp Ign-F1 on a controlled evaluation subset), imposes a substantial cost at 4B (+7.5pp), and approaches zero at $\\geq$8B parameters`  \n**Issue**: Same — +7.5pp invalidated, -6.2pp outdated  \n**Suggested**: `evidence generation provides implicit regularization at 1.7B ($-$5.6pp Ign-F1) and approaches zero at $\\geq$4B (+0.25$\\pm$0.47pp at 4B, +0.04pp at 8B), measured on the development set with matched 2048-token generation budget (fair comparison subset)`\n\n**File**: `docs/paper/sections/introduction.tex:30` (contribution list)  \n**Current**: `varies from beneficial ($-$6.2pp at 1.7B) to costly (+7.5pp at 4B) to negligible ($\\geq$8B)`  \n**Issue**: Same invalidated numbers  \n**Suggested**: `varies from beneficial ($-$5.6pp at 1.7B) to negligible at $\\geq$4B (+0.25$\\pm$0.47pp at 4B, +0.04pp at 8B)`\n\n**File**: `docs/paper/sections/conclusion.tex:4`  \n**Current**: `model capacity determines whether evidence acts as regularizer ($-$6.2pp at 1.7B) or burden (+7.5pp at 4B)`  \n**Issue**: Same invalidated numbers  \n**Suggested**: `model capacity determines whether evidence acts as regularizer ($-$5.6pp at 1.7B) or is absorbed at $\\geq$4B (+0.25pp at 4B, near-zero at 8B)`\n\n**File**: `docs/paper/sections/experiments.tex:92`  \n**Current**: `the tax varies from beneficial at 1.7B ($-$6.2pp on a controlled subset; Appendix~\\ref{sec:fair_subset}) to costly at 4B (+7.5pp) to negligible at $\\geq$8B`  \n**Issue**: Same invalidated numbers. This is the primary evidence tax prose.  \n**Suggested**: `the tax varies from beneficial at 1.7B ($-$5.63pp on a matched-budget fair comparison subset; Appendix~\\ref{sec:fair_subset}) to negligible at $\\geq$4B (+0.25$\\pm$0.47pp 3-seed mean at 4B, +0.04pp at 8B)`\n\n### 2.2 Narrative Change — \"non-monotonic\" / \"capacity valley\" invalidated\n\nThe D144 correction (4B from +7.5pp → +0.25pp) eliminates the \"costly at 4B\" narrative. Per `paper_framing.md:141`, the new framing is **within-family capacity threshold** (1.7B benefits, ≥4B neutral) rather than non-monotonic curve. Check all instances of \"costly\" or \"non-monotonic\" language around 4B.\n\n### 2.3 Token Budget Annotation — Missing \"matched 2048-token budget\"\n\nThe paper currently describes **mismatched** token budgets in Table 3 footnote (`experiments.tex:119`): no-evi@2048, with-evi@1024. The fair_tax numbers use **matched@2048** for both conditions. If incorporating fair_tax, the methodology must be explained:\n\n**Suggested footnote/methodology text** (first occurrence, e.g., §4.4):  \n> \"All evidence tax values reported in this section are computed on the development set using a matched 2048-token generation budget for both with-evidence and no-evidence conditions, evaluated on the format-compliant document intersection (fair comparison subset) to control for differential truncation rates.\"\n\n**Suggested table footnote** (for any fair_tax table):  \n> \"Dev set, matched @2048, fair comparison subset.\"\n\n### 2.4 Existing Dev-Set Annotations (Already Adequate)\n\n| Location | Annotation | Status |\n|----------|-----------|--------|\n| `experiments.tex:17` | \"All results use the development set.\" | ✅ Blanket statement |\n| `experiments.tex:102` (Table 3 caption) | \"DocRED dev Ign-F1\" | ✅ |\n| `appendix.tex:145` (Table 8 caption) | \"DocRED dev Ign-F1, s42 paired\" | ✅ |\n| `limitations.tex:3` | \"All results use the DocRED development set; test set submission is pending.\" | ✅ |\n| `appendix.tex:52,91,204` (other table captions) | \"DocRED dev set\" | ✅ |\n\n### 2.5 14B RSFT Evidence Tax (-4.54pp) — Not in Paper\n\n`paper_framing.md:167` documents 14B RSFT tax = -4.54pp (evidence strongly beneficial, truncation symmetric so @1024 is valid). This number does not appear in any .tex file. If adding it to Table 3 or the 14B row, annotate as: \"Dev set, @1024 (truncation symmetric: no-evi 10.8% vs with-evi 10.7%).\"\n\n### 2.6 LLaMA RSFT Tax — Paper Has 2-Seed, Now 3-Seed Available\n\n**File**: `docs/paper/sections/experiments.tex:114` (Table 3, LLaMA row)  \n**Current**: `$-$1.52$^\\ddagger$` with footnote \"Two-seed mean (s42: $-$1.88, s43: $-$1.16); s44 pending.\"  \n**Corrected value**: -1.14±0.76pp (3-seed mean, per D135/paper_framing.md:154)  \n**Action**: Update to 3-seed value if s44 data is finalized.\n\n---\n\n## Part 3: Variance Compression Numbers — Already Correct\n\nThe variance compression numbers (1.7B 31×, 4B 7.5×, 8B 17×, LLaMA 4.6×) appear correctly in:\n- `experiments.tex:96` (main text)\n- `abstract.tex:15`\n- `introduction.tex:26`\n- `analysis.tex:14`\n- `conclusion.tex:4` (as \"7.5--17×\" and \"4.6×\")\n\nThese are adequately covered by the blanket \"All results use the development set\" statement. No additional per-number annotation needed.\n\n---\n\n## Summary of Required Actions\n\n1. **CRITICAL**: Replace all instances of +7.5pp (4B) with +0.25±0.47pp — 5 locations (abstract, intro×2, experiments, conclusion)\n2. **CRITICAL**: Update -6.2pp (1.7B) to -5.63pp (matched@2048) — same 5 locations\n3. **ADD**: Matched@2048 methodology explanation in §4.4 or Appendix controlled subset section\n4. **ADD**: \"fair comparison subset\" annotation wherever fair_tax numbers appear\n5. **UPDATE**: LLaMA RSFT tax from 2-seed -1.52pp to 3-seed -1.14±0.76pp (Table 3)\n6. **CONSIDER**: Adding 14B RSFT tax (-4.54pp) to Table 3\n7. **NARRATIVE**: Revise \"costly at 4B\" / \"non-monotonic\" language → \"within-family capacity threshold\"\n",
      "numLines": 118,
      "startLine": 1,
      "totalLines": 118
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01QcaHJo8bqU1TjB7HdjjRa3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dev_test_gap_paragraph.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "0e2156b2-57f4-4c46-bdc1-6f4972e23116",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrSYXG3X2RG6iDzESuXvkp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6171,
      "cache_read_input_tokens": 24346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6171
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

_source line 16 · 2026-05-21T22:56:06.390Z_

<details><summary>↩ Tool result · `toolu_01QcaHJo8bqU1TjB7HdjjRa3`</summary>

```text
1	We observe a consistent performance gap between dev and test sets across all model configurations, with test ign\_f1 scores approximately 20 percentage points lower than dev scores (1.7B: 51.2→29.3, 8B: 54.3→33.5, 14B: 58.9→38.5, LLaMA-8B: 56.5→36.0). This gap is attributable to a substantial difference in annotation density between the two splits: the Re-DocRED test set contains 34.7 gold triples per document on average, compared to 12.3 in the dev set—a 2.82× ratio. The denser test annotations impose a harder recall requirement, as models must extract nearly three times as many relations per document to achieve comparable F1. Importantly, the gap magnitude is remarkably stable across four model scales and two architectures (Qwen3 and LLaMA-3.1), ranging only from 20.4 to 21.9 percentage points (a spread of 1.5pp). The model ranking is also perfectly preserved between splits (Spearman $\rho$=1.0), with 1.7B < 8B < LLaMA-8B < 14B in both dev and test. This consistency indicates that the absolute score drop reflects an intrinsic property of the test set annotation scheme rather than a model-specific deficiency, and that relative comparisons across model configurations remain fully valid on either split.
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "728f232d-8997-498e-9b47-5576641ca5ba",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dev_test_gap_paragraph.md",
      "content": "We observe a consistent performance gap between dev and test sets across all model configurations, with test ign\\_f1 scores approximately 20 percentage points lower than dev scores (1.7B: 51.2→29.3, 8B: 54.3→33.5, 14B: 58.9→38.5, LLaMA-8B: 56.5→36.0). This gap is attributable to a substantial difference in annotation density between the two splits: the Re-DocRED test set contains 34.7 gold triples per document on average, compared to 12.3 in the dev set—a 2.82× ratio. The denser test annotations impose a harder recall requirement, as models must extract nearly three times as many relations per document to achieve comparable F1. Importantly, the gap magnitude is remarkably stable across four model scales and two architectures (Qwen3 and LLaMA-3.1), ranging only from 20.4 to 21.9 percentage points (a spread of 1.5pp). The model ranking is also perfectly preserved between splits (Spearman $\\rho$=1.0), with 1.7B < 8B < LLaMA-8B < 14B in both dev and test. This consistency indicates that the absolute score drop reflects an intrinsic property of the test set annotation scheme rather than a model-specific deficiency, and that relative comparisons across model configurations remain fully valid on either split.\n",
      "numLines": 2,
      "startLine": 1,
      "totalLines": 2
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01KzY16zEck9shP1FTgFmZvP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/paper_main_tables_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "953516c5-6bcc-4a3f-bf1b-9009183ab994",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrSYXG3X2RG6iDzESuXvkp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6171,
      "cache_read_input_tokens": 24346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6171
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

_source line 18 · 2026-05-21T22:56:06.711Z_

<details><summary>↩ Tool result · `toolu_01KzY16zEck9shP1FTgFmZvP`</summary>

```text
1	# Paper Main Tables Draft — FREIGE (EMNLP 2026)
2	
3	> **Compiled**: 2026-05-16
4	> **Source**: experiment registry (all metrics verified against registry entries)
5	> **Convention**: Ign-F1/F1/Evi-F1 as percentage; EDCR as decimal [0,1]. Ign-F1 uses corrected values from paper_framing.md where available; registry ign_f1 has known bug (= rel_f1) per D069.
6	
7	---
8	
9	## Table 1: Main Results on DocRED Dev Set
10	
11	**Claim 1 support**: Evidence-grounded DocRE is viable. Evidence generation costs ~7pp Ign-F1; RSFT recovers most; CED reranker recovers 97%.
12	
13	| Method | Ign-F1 | F1 | Evi-F1 | Evi-F1 (joint) | EDCR | exp_id |
14	|--------|--------|------|--------|----------------|------|--------|
15	| **SFT (no evidence)** | **47.36** | **48.93** | — | — | — | `eval_plan_014_sft_no_evidence` |
16	| SFT baseline (with evidence) | 40.36 | 41.06 | 80.13 | 32.16 | 0.7039 | `eval_sft_baseline_noquant` |
17	| RSFT flat-NLI (best: s44) | 46.15† | 46.15 | 81.31 | 35.97 | 0.6458 | `eval_flat_nli_s44` |
18	| RSFT flat-NLI (4-seed mean) | TBD | 45.57±0.39 | 81.22±0.49 | — | 0.6479±0.004 | `s42/s43/s44/s45` |
19	| RSFT CED (best: s43) | 45.85 | 46.83 | 81.56 | 37.11 | 0.6388 | `mvp2_eval_rsft_s43_r2` |
20	| RSFT CED (3-seed mean) | 45.00±1.19 | 45.96±1.27 | 81.43±0.51 | — | 0.6434±0.011 | `s42/s43/s44` |
21	| **CED reranker (N=8)** | **TBD** | **48.64** | **81.88** | — | **0.6156** | `mvp2_ced_reranker_poc` |
22	| DREEAM‡ (RoBERTa-large) | 61.72 | 63.57 | 54.01 | — | — | `plan_004_dreeam_baseline` |
23	
24	**Notes**:
25	- † = Ign-F1 uncorrected (registry ign_f1 = rel_f1, suspected bug per D069). Corrected Ign-F1 expected ~1pp below F1.
26	- ‡ = Encoder model (RoBERTa-large), different paradigm — not directly comparable for RE, included for evidence baseline context.
27	- CED reranker = inference-time reranking of N=8 SFT samples using CED scoring, no additional training.
28	- SFT baseline uses noquant (no quantization) variant; quantized SFT (rel_f1=40.57) available as `mvp2_eval_sft_baseline` if needed.
29	- RSFT CED 3-seed mean computed from s42 (3ep, mvp2_eval_rsft_r1), s43 (mvp2_eval_rsft_s43_r2), s44 (mvp2_rsft_train_r1_s44). All original protocol.
30	- RSFT flat-NLI 4-seed mean from s42 (eval_plan_001_flat_nli), s43 (reeval_flat_nli_s43), s44 (eval_flat_nli_s44), s45 (eval_flat_nli_seed45). Mixed protocol (s43 partial unified, rest original).
31	- Joint Evi-F1 = unconditional (denominator = all gold triples, not just correctly predicted ones).
32	
33	**Key numbers**:
34	- Evidence tax: 47.36 → 40.36 = **−7.00pp** Ign-F1
35	- RSFT CED recovery: 45.85 − 40.36 = **+5.49pp** (78.4% of gap)
36	- CED reranker: F1=48.64 vs no-evidence F1=48.93 = **−0.29pp** (97% recovery), with evi_f1=81.88
37	
38	**PENDING data**:
39	- `PENDING: mvp2_ced_reranker_poc` — CED reranker Ign-F1 (only F1 available)
40	- `PENDING: reeval_ced_s42, reeval_ced_s44` — D076 unified protocol CED reevals
41	- `PENDING: eval_rsft_ced_s45` — CED s45 for 4-seed statistics
42	
43	---
44	
45	## Table 2: Evidence-Extraction Decoupling Spectrum
46	
47	**Claim 2 support**: RL optimization pressure correlates with decoupling severity. QLoRA is a catastrophic amplifier. Decoupling is intra-task multi-objective trade-off, not inter-task forgetting.
48	
49	| Method | Quant | F1 | Δ F1 vs SFT | Evi-F1 | EDCR | Severity | exp_id |
50	|--------|-------|------|-------------|--------|------|----------|--------|
51	| GRPO (lr=5e-6, ckpt100) | QLoRA 4-bit | 1.38 | −39.68 | 85.04 | 0.9876 | **Catastrophic** | `mvp2_eval_lr5e6_r1_ckpt100` |
52	| GRPO (lr=5e-5, ckpt100) | QLoRA 4-bit | 21.67 | −19.39 | 57.46 | 0.8539 | Severe | `mvp2_eval_ced_kl001_r4_step100` |
53	| DPO bf16 (3ep) | bf16 | 34.29 | −6.77 | 84.03 | 0.7294 | **Gradual** | `plan_012_dpo_ced` |
54	| SFT baseline | noquant | 41.06 | — | 80.13 | 0.7039 | Reference | `eval_sft_baseline_noquant` |
55	| DPO bf16 (1ep) | bf16 | 40.34 | −0.72 | 80.88 | 0.7139 | Neutral | `eval_plan_012_dpo_1ep_fixed_r2` |
56	| GRPO bf16 G=8 (step30) | bf16 | 43.40 | +2.34 | 80.63 | 0.6807 | **Mild** (transient) | `plan_011_bf16_g8_step_eval` |
57	| GRPO bf16 G=8 (step70) | bf16 | 43.41 | +2.35 | 80.99 | 0.6685 | Mild (transient) | `plan_011_bf16_g8_step_eval` |
58	| GRPO bf16 G=8 (ckpt100) | bf16 | 45.49 | +4.43 | 80.86 | 0.6318 | **None** (converged) | `plan_011_grpo_g8_bf16_eval` |
59	| RSFT CED (best: s43) | — | 46.83 | +5.77 | 81.56 | 0.6388 | **None** | `mvp2_eval_rsft_s43_r2` |
60	
61	**Notes**:
62	- Δ F1 computed vs SFT baseline noquant (F1=41.06, `eval_sft_baseline_noquant`).
63	- GRPO QLoRA (lr=5e-6): 100 steps, G=8 groups, QLoRA 4-bit quantization. Catastrophic: rel_f1 drops to near-zero while evi_f1 rises to 85%.
64	- GRPO QLoRA (lr=5e-5): Same config as above but higher learning rate. Less catastrophic but still severe.
65	- GRPO bf16 trajectory: step30→50→70 show mild transient decline (all F1 < ckpt100), recovers by convergence. ckpt80→90→100: 44.56→45.23→45.49 (monotonically improving).
66	- DPO 1ep→3ep: gradual decoupling — rel_f1 declines from 40.34 to 34.29 while evi_f1 rises from 80.88 to 84.03.
67	- QLoRA amplification: bf16 GRPO F1=45.49 vs QLoRA GRPO F1=1.38. Same algorithm, quantization turns mild into catastrophic.
68	- Ign-F1 column omitted from this table — most entries have bugged Ign-F1. Corrected values: GRPO bf16 ckpt100 Ign-F1=45.59 (paper_framing); DPO 1ep Ign-F1=38.88 (paper_framing). Others TBD.
69	
70	**GRPO bf16 extended trajectory** (supplementary):
71	
72	| Checkpoint | F1 | Evi-F1 | EDCR | exp_id |
73	|------------|------|--------|------|--------|
74	| step30 | 43.40 | 80.63 | 0.6807 | `plan_011_bf16_g8_step_eval` |
75	| step50 | 42.76 | 80.24 | 0.6855 | `plan_011_bf16_g8_step_eval` |
76	| step70 | 43.41 | 80.99 | 0.6685 | `plan_011_bf16_g8_step_eval` |
77	| ckpt80 | 44.56 | 80.34 | 0.6409 | `eval_grpo_g8_bf16` |
78	| ckpt90 | 45.23 | 80.52 | 0.6414 | `eval_grpo_g8_bf16` |
79	| ckpt100 | 45.49 | 80.86 | 0.6318 | `eval_grpo_g8_bf16` / `plan_011_grpo_g8_bf16_eval` |
80	
81	**QLoRA GRPO (lr=5e-6) trajectory** (supplementary):
82	
83	| Checkpoint | F1 | Evi-F1 | EDCR | exp_id |
84	|------------|------|--------|------|--------|
85	| ckpt20 | 0.77 | 62.80 | 0.9930 | `mvp2_eval_lr5e6_r1_ckpt20` |
86	| ckpt40 | 0.71 | 75.84 | 0.9942 | `mvp2_eval_lr5e6_r1_ckpt40_r2` |
87	| ckpt60 | 0.93 | 81.00 | 0.9930 | `mvp2_eval_lr5e6_r1_ckpt60_r2` |
88	| ckpt80 | 1.16 | 82.80 | 0.9930 | `mvp2_eval_lr5e6_r1_ckpt80` |
89	| ckpt100 | 1.38 | 85.04 | 0.9876 | `mvp2_eval_lr5e6_r1_ckpt100` |
90	
91	**PENDING data**:
92	- `PENDING` — Ign-F1 for most entries (need metrics_v2 re-computation)
93	- `PENDING` — DPO 3ep Ign-F1
94	
95	---
96	
97	## Table 3: CED vs flat-NLI Seed Comparison (Claim 3)
98	
99	**Claim 3 support**: Both CED and flat-NLI improve over SFT baseline. CED vs flat-NLI difference statistically uncertain (p>0.05). CED may be "one possible scoring function" rather than strictly superior.
100	
101	### CED RSFT (top_k=1, 3 epochs)
102	
103	| Seed | F1 | Ign-F1 | Evi-F1 | EDCR | Protocol | exp_id |
104	|------|------|--------|--------|------|----------|--------|
105	| 42 (3ep) | 44.49 | 43.63 | 81.87 | 0.6565 | original | `mvp2_eval_rsft_r1` |
106	| 43 | 46.83 | 45.85 | 81.56 | 0.6388 | original | `mvp2_eval_rsft_s43_r2` |
107	| 44 | 46.55 | 45.51 | 80.87 | 0.6350 | original | `mvp2_rsft_train_r1_s44` |
108	| 45 | PENDING | PENDING | PENDING | PENDING | — | `PENDING: eval_rsft_ced_s45` |
109	| **Mean (3-seed)** | **45.96±1.27** | **45.00±1.19** | **81.43±0.51** | **0.6434±0.011** | | |
110	
111	### flat-NLI RSFT (top_k=1, 3 epochs)
112	
113	| Seed | F1 | Ign-F1 | Evi-F1 | EDCR | Protocol | exp_id |
114	|------|------|--------|--------|------|----------|--------|
115	| 42 | 45.39 | 44.49 | 80.43 | 0.6431 | original (batch=16) | `eval_plan_001_flat_nli` |
116	| 43 | 45.23 | TBD† | 81.58 | 0.6505 | partial unified (fixed adapter, batch=16) | `reeval_flat_nli_s43` |
117	| 44 | 46.15 | 46.15† | 81.31 | 0.6458 | original | `eval_flat_nli_s44` |
118	| 45 | 45.51 | 45.51† | 81.54 | 0.6521 | original | `eval_flat_nli_seed45` |
119	| **Mean (4-seed)** | **45.57±0.39** | **TBD** | **81.22±0.49** | **0.6479±0.004** | | |
120	
121	### Head-to-Head (current data, NOT D076-unified)
122	
123	| Metric | CED (3-seed) | flat-NLI (4-seed) | Δ (CED − flat-NLI) |
124	|--------|-------------|-------------------|---------------------|
125	| F1 | 45.96 ± 1.27 | 45.57 ± 0.39 | +0.39pp |
126	| Evi-F1 | 81.43 ± 0.51 | 81.22 ± 0.49 | +0.21pp |
127	| EDCR | 0.6434 ± 0.011 | 0.6479 ± 0.004 | −0.0045 |
128	
129	**Dream v1 p-values**: 0.08 / 0.38 / 0.12 — **not statistically significant** at α=0.05.
130	
131	### top_k Ablation (CED only)
132	
133	| Config | F1 | Ign-F1 | Evi-F1 | EDCR | Training samples | exp_id |
134	|--------|------|--------|--------|------|-----------------|--------|
135	| k=1 (3-seed mean) | 45.96 | 45.00 | 81.43 | 0.6434 | 2,718 (12.4%) | `s42/s43/s44` |
136	| k=3 (1 seed, s42) | 44.54 | 43.64 | 80.88 | 0.6635 | 8,037 (37%) | `reeval_rsft_topk3` |
137	| **Δ (k=3 − k=1)** | **−1.42** | **−1.36** | **−0.55** | **+0.02** | **+5,319** | |
138	
139	**Notes**:
140	- k=3 uses 2.96× more training data but lower quality: mean_f1=0.5761 vs k=1 mean_f1=0.6157; mean_ced=0.6205 vs k=1 mean_ced=0.6683 (`mvp2_rsft_ced_scoring` vs `mvp2_rsft_ced_scoring_topk3_r2`).
141	- k=3 has only 1 seed — direction consistent but no significance test possible. Present as supplementary ablation.
142	
143	### D076 Unified Protocol Reeval Status
144	
145	Valid paired t-test requires all seeds evaluated under identical protocol (batch_size=4, --no-quantize, --sft_adapter, max_new_tokens=1024).
146	
147	| Target | Issue | Unified Reeval | Status |
148	|--------|-------|---------------|--------|
149	| CED s42 | Wrong checkpoint (r2b α=32) | `reeval_ced_s42` | PREPARING |
150	| CED s44 | Wrong seed in eval (used s42) | `reeval_ced_s44` | PREPARING |
151	| flat-NLI s42 | batch_size=16 | `reeval_flat_nli_s42` | PREPARING |
152	| flat-NLI s43 | batch_size=16 | `reeval_flat_nli_s43_r2` | RUNNING |
153	
154	**Impact**: Current numbers are directional only. Paired t-test blocked until all 8 evals (4 CED + 4 flat-NLI) use unified protocol.
155	
156	---
157	
158	## Cross-Table: EDCR Method-Level Summary (Claim 4 support)
159	
160	| Method | EDCR | F1 | Evi-F1 | exp_id |
161	|--------|------|------|--------|--------|
162	| GRPO QLoRA (lr=5e-6) | 0.9876 | 1.38 | 85.04 | `mvp2_eval_lr5e6_r1_ckpt100` |
163	| GRPO QLoRA (lr=5e-5) | 0.8539 | 21.67 | 57.46 | `mvp2_eval_ced_kl001_r4_step100` |
164	| DPO 3ep | 0.7294 | 34.29 | 84.03 | `plan_012_dpo_ced` |
165	| SFT baseline (quantized) | 0.7118 | 40.57 | 79.79 | `mvp2_eval_sft_baseline` |
166	| DPO 1ep | 0.7139 | 40.34 | 80.88 | `eval_plan_012_dpo_1ep_fixed_r2` |
167	| SFT baseline (noquant) | 0.7039 | 41.06 | 80.13 | `eval_sft_baseline_noquant` |
168	| RSFT CED k=3 | 0.6635 | 44.54 | 80.88 | `reeval_rsft_topk3` |
169	| RSFT r2a (1ep, α=128) | 0.6641 | 44.94 | 81.08 | `mvp2_eval_rsft_r2a` |
170	| RSFT r2b (1ep, α=32) | 0.6609 | 44.93 | 81.28 | `mvp2_eval_rsft_r2b` |
171	| RSFT CED s42 (3ep) | 0.6565 | 44.49 | 81.87 | `mvp2_eval_rsft_r1` |
172	| flat-NLI s43 | 0.6505 | 45.23 | 81.58 | `reeval_flat_nli_s43` |
173	| flat-NLI s45 | 0.6521 | 45.51 | 81.54 | `eval_flat_nli_seed45` |
174	| flat-NLI s44 | 0.6458 | 46.15 | 81.31 | `eval_flat_nli_s44` |
175	| flat-NLI s42 | 0.6431 | 45.39 | 80.43 | `eval_plan_001_flat_nli` |
176	| RSFT CED s43 | 0.6388 | 46.83 | 81.56 | `mvp2_eval_rsft_s43_r2` |
177	| RSFT CED s44 | 0.6350 | 46.55 | 80.87 | `mvp2_rsft_train_r1_s44` |
178	| GRPO bf16 G=8 (ckpt100) | 0.6318 | 45.49 | 80.86 | `plan_011_grpo_g8_bf16_eval` |
179	| **CED reranker** | **0.6156** | **48.64** | **81.88** | `mvp2_ced_reranker_poc` |
180	
181	**Correlations** (`plan_003_edcr_diagnostic`):
182	- Method-level: EDCR vs rel_f1 Spearman ρ = −0.9648 (p=0.0001); EDCR vs evi_f1 ρ = 0.0022 (p=0.9941)
183	- Per-relation (D070, 93 types ≥5 samples): EDCR vs evi_f1 ρ = −0.064 (p=0.58) — **completely independent**; EDCR vs rel_f1 ρ = −0.793 (p<0.001)
184	
185	---
186	
187	## Summary: Data Completeness
188	
189	### Paper-ready numbers
190	1. Evidence tax: 47.36 → 40.36 = −7.00pp Ign-F1 ✓
191	2. CED reranker: F1=48.64, −0.29pp below no-evidence ✓
192	3. RSFT CED best: Ign-F1=45.85, +5.49pp over SFT ✓
193	4. Decoupling spectrum: GRPO QLoRA / GRPO bf16 / DPO / RSFT — all data points present ✓
194	5. QLoRA amplification: bf16 45.49 vs QLoRA 1.38 ✓
195	6. EDCR per-relation independence: ρ=−0.064 ✓
196	7. top_k ablation: k=1 > k=3 ✓
197	8. DREEAM baseline: F1=63.57, Evi-F1=54.01 ✓
198	
199	### Critical PENDING (blocking paper)
200	1. **CED reranker Ign-F1** — needed for Table 1 main column
201	2. **D076 unified protocol reevals** (4 experiments) — blocking Claim 3 paired t-test
202	3. **CED s45 eval** — blocking 4-seed CED statistics
203	4. **Corrected Ign-F1** for flat-NLI s43/s44/s45, DPO 3ep, GRPO QLoRA — need metrics_v2 re-computation
204	5. **Test set evaluation** (plan_002) — no official numbers yet
205	
206	### Nice-to-have
207	1. EDCR human validation (plan_013) — RC6
208	2. Post-hoc retrieval baseline (SFT + BM25) — RC10
209	3. TP-only EDCR (D071) — method-level confound resolution
210	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "fdf68399-a102-44c3-a3f5-a578f4269b62",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/paper_main_tables_draft.md",
      "content": "# Paper Main Tables Draft — FREIGE (EMNLP 2026)\n\n> **Compiled**: 2026-05-16\n> **Source**: experiment registry (all metrics verified against registry entries)\n> **Convention**: Ign-F1/F1/Evi-F1 as percentage; EDCR as decimal [0,1]. Ign-F1 uses corrected values from paper_framing.md where available; registry ign_f1 has known bug (= rel_f1) per D069.\n\n---\n\n## Table 1: Main Results on DocRED Dev Set\n\n**Claim 1 support**: Evidence-grounded DocRE is viable. Evidence generation costs ~7pp Ign-F1; RSFT recovers most; CED reranker recovers 97%.\n\n| Method | Ign-F1 | F1 | Evi-F1 | Evi-F1 (joint) | EDCR | exp_id |\n|--------|--------|------|--------|----------------|------|--------|\n| **SFT (no evidence)** | **47.36** | **48.93** | — | — | — | `eval_plan_014_sft_no_evidence` |\n| SFT baseline (with evidence) | 40.36 | 41.06 | 80.13 | 32.16 | 0.7039 | `eval_sft_baseline_noquant` |\n| RSFT flat-NLI (best: s44) | 46.15† | 46.15 | 81.31 | 35.97 | 0.6458 | `eval_flat_nli_s44` |\n| RSFT flat-NLI (4-seed mean) | TBD | 45.57±0.39 | 81.22±0.49 | — | 0.6479±0.004 | `s42/s43/s44/s45` |\n| RSFT CED (best: s43) | 45.85 | 46.83 | 81.56 | 37.11 | 0.6388 | `mvp2_eval_rsft_s43_r2` |\n| RSFT CED (3-seed mean) | 45.00±1.19 | 45.96±1.27 | 81.43±0.51 | — | 0.6434±0.011 | `s42/s43/s44` |\n| **CED reranker (N=8)** | **TBD** | **48.64** | **81.88** | — | **0.6156** | `mvp2_ced_reranker_poc` |\n| DREEAM‡ (RoBERTa-large) | 61.72 | 63.57 | 54.01 | — | — | `plan_004_dreeam_baseline` |\n\n**Notes**:\n- † = Ign-F1 uncorrected (registry ign_f1 = rel_f1, suspected bug per D069). Corrected Ign-F1 expected ~1pp below F1.\n- ‡ = Encoder model (RoBERTa-large), different paradigm — not directly comparable for RE, included for evidence baseline context.\n- CED reranker = inference-time reranking of N=8 SFT samples using CED scoring, no additional training.\n- SFT baseline uses noquant (no quantization) variant; quantized SFT (rel_f1=40.57) available as `mvp2_eval_sft_baseline` if needed.\n- RSFT CED 3-seed mean computed from s42 (3ep, mvp2_eval_rsft_r1), s43 (mvp2_eval_rsft_s43_r2), s44 (mvp2_rsft_train_r1_s44). All original protocol.\n- RSFT flat-NLI 4-seed mean from s42 (eval_plan_001_flat_nli), s43 (reeval_flat_nli_s43), s44 (eval_flat_nli_s44), s45 (eval_flat_nli_seed45). Mixed protocol (s43 partial unified, rest original).\n- Joint Evi-F1 = unconditional (denominator = all gold triples, not just correctly predicted ones).\n\n**Key numbers**:\n- Evidence tax: 47.36 → 40.36 = **−7.00pp** Ign-F1\n- RSFT CED recovery: 45.85 − 40.36 = **+5.49pp** (78.4% of gap)\n- CED reranker: F1=48.64 vs no-evidence F1=48.93 = **−0.29pp** (97% recovery), with evi_f1=81.88\n\n**PENDING data**:\n- `PENDING: mvp2_ced_reranker_poc` — CED reranker Ign-F1 (only F1 available)\n- `PENDING: reeval_ced_s42, reeval_ced_s44` — D076 unified protocol CED reevals\n- `PENDING: eval_rsft_ced_s45` — CED s45 for 4-seed statistics\n\n---\n\n## Table 2: Evidence-Extraction Decoupling Spectrum\n\n**Claim 2 support**: RL optimization pressure correlates with decoupling severity. QLoRA is a catastrophic amplifier. Decoupling is intra-task multi-objective trade-off, not inter-task forgetting.\n\n| Method | Quant | F1 | Δ F1 vs SFT | Evi-F1 | EDCR | Severity | exp_id |\n|--------|-------|------|-------------|--------|------|----------|--------|\n| GRPO (lr=5e-6, ckpt100) | QLoRA 4-bit | 1.38 | −39.68 | 85.04 | 0.9876 | **Catastrophic** | `mvp2_eval_lr5e6_r1_ckpt100` |\n| GRPO (lr=5e-5, ckpt100) | QLoRA 4-bit | 21.67 | −19.39 | 57.46 | 0.8539 | Severe | `mvp2_eval_ced_kl001_r4_step100` |\n| DPO bf16 (3ep) | bf16 | 34.29 | −6.77 | 84.03 | 0.7294 | **Gradual** | `plan_012_dpo_ced` |\n| SFT baseline | noquant | 41.06 | — | 80.13 | 0.7039 | Reference | `eval_sft_baseline_noquant` |\n| DPO bf16 (1ep) | bf16 | 40.34 | −0.72 | 80.88 | 0.7139 | Neutral | `eval_plan_012_dpo_1ep_fixed_r2` |\n| GRPO bf16 G=8 (step30) | bf16 | 43.40 | +2.34 | 80.63 | 0.6807 | **Mild** (transient) | `plan_011_bf16_g8_step_eval` |\n| GRPO bf16 G=8 (step70) | bf16 | 43.41 | +2.35 | 80.99 | 0.6685 | Mild (transient) | `plan_011_bf16_g8_step_eval` |\n| GRPO bf16 G=8 (ckpt100) | bf16 | 45.49 | +4.43 | 80.86 | 0.6318 | **None** (converged) | `plan_011_grpo_g8_bf16_eval` |\n| RSFT CED (best: s43) | — | 46.83 | +5.77 | 81.56 | 0.6388 | **None** | `mvp2_eval_rsft_s43_r2` |\n\n**Notes**:\n- Δ F1 computed vs SFT baseline noquant (F1=41.06, `eval_sft_baseline_noquant`).\n- GRPO QLoRA (lr=5e-6): 100 steps, G=8 groups, QLoRA 4-bit quantization. Catastrophic: rel_f1 drops to near-zero while evi_f1 rises to 85%.\n- GRPO QLoRA (lr=5e-5): Same config as above but higher learning rate. Less catastrophic but still severe.\n- GRPO bf16 trajectory: step30→50→70 show mild transient decline (all F1 < ckpt100), recovers by convergence. ckpt80→90→100: 44.56→45.23→45.49 (monotonically improving).\n- DPO 1ep→3ep: gradual decoupling — rel_f1 declines from 40.34 to 34.29 while evi_f1 rises from 80.88 to 84.03.\n- QLoRA amplification: bf16 GRPO F1=45.49 vs QLoRA GRPO F1=1.38. Same algorithm, quantization turns mild into catastrophic.\n- Ign-F1 column omitted from this table — most entries have bugged Ign-F1. Corrected values: GRPO bf16 ckpt100 Ign-F1=45.59 (paper_framing); DPO 1ep Ign-F1=38.88 (paper_framing). Others TBD.\n\n**GRPO bf16 extended trajectory** (supplementary):\n\n| Checkpoint | F1 | Evi-F1 | EDCR | exp_id |\n|------------|------|--------|------|--------|\n| step30 | 43.40 | 80.63 | 0.6807 | `plan_011_bf16_g8_step_eval` |\n| step50 | 42.76 | 80.24 | 0.6855 | `plan_011_bf16_g8_step_eval` |\n| step70 | 43.41 | 80.99 | 0.6685 | `plan_011_bf16_g8_step_eval` |\n| ckpt80 | 44.56 | 80.34 | 0.6409 | `eval_grpo_g8_bf16` |\n| ckpt90 | 45.23 | 80.52 | 0.6414 | `eval_grpo_g8_bf16` |\n| ckpt100 | 45.49 | 80.86 | 0.6318 | `eval_grpo_g8_bf16` / `plan_011_grpo_g8_bf16_eval` |\n\n**QLoRA GRPO (lr=5e-6) trajectory** (supplementary):\n\n| Checkpoint | F1 | Evi-F1 | EDCR | exp_id |\n|------------|------|--------|------|--------|\n| ckpt20 | 0.77 | 62.80 | 0.9930 | `mvp2_eval_lr5e6_r1_ckpt20` |\n| ckpt40 | 0.71 | 75.84 | 0.9942 | `mvp2_eval_lr5e6_r1_ckpt40_r2` |\n| ckpt60 | 0.93 | 81.00 | 0.9930 | `mvp2_eval_lr5e6_r1_ckpt60_r2` |\n| ckpt80 | 1.16 | 82.80 | 0.9930 | `mvp2_eval_lr5e6_r1_ckpt80` |\n| ckpt100 | 1.38 | 85.04 | 0.9876 | `mvp2_eval_lr5e6_r1_ckpt100` |\n\n**PENDING data**:\n- `PENDING` — Ign-F1 for most entries (need metrics_v2 re-computation)\n- `PENDING` — DPO 3ep Ign-F1\n\n---\n\n## Table 3: CED vs flat-NLI Seed Comparison (Claim 3)\n\n**Claim 3 support**: Both CED and flat-NLI improve over SFT baseline. CED vs flat-NLI difference statistically uncertain (p>0.05). CED may be \"one possible scoring function\" rather than strictly superior.\n\n### CED RSFT (top_k=1, 3 epochs)\n\n| Seed | F1 | Ign-F1 | Evi-F1 | EDCR | Protocol | exp_id |\n|------|------|--------|--------|------|----------|--------|\n| 42 (3ep) | 44.49 | 43.63 | 81.87 | 0.6565 | original | `mvp2_eval_rsft_r1` |\n| 43 | 46.83 | 45.85 | 81.56 | 0.6388 | original | `mvp2_eval_rsft_s43_r2` |\n| 44 | 46.55 | 45.51 | 80.87 | 0.6350 | original | `mvp2_rsft_train_r1_s44` |\n| 45 | PENDING | PENDING | PENDING | PENDING | — | `PENDING: eval_rsft_ced_s45` |\n| **Mean (3-seed)** | **45.96±1.27** | **45.00±1.19** | **81.43±0.51** | **0.6434±0.011** | | |\n\n### flat-NLI RSFT (top_k=1, 3 epochs)\n\n| Seed | F1 | Ign-F1 | Evi-F1 | EDCR | Protocol | exp_id |\n|------|------|--------|--------|------|----------|--------|\n| 42 | 45.39 | 44.49 | 80.43 | 0.6431 | original (batch=16) | `eval_plan_001_flat_nli` |\n| 43 | 45.23 | TBD† | 81.58 | 0.6505 | partial unified (fixed adapter, batch=16) | `reeval_flat_nli_s43` |\n| 44 | 46.15 | 46.15† | 81.31 | 0.6458 | original | `eval_flat_nli_s44` |\n| 45 | 45.51 | 45.51† | 81.54 | 0.6521 | original | `eval_flat_nli_seed45` |\n| **Mean (4-seed)** | **45.57±0.39** | **TBD** | **81.22±0.49** | **0.6479±0.004** | | |\n\n### Head-to-Head (current data, NOT D076-unified)\n\n| Metric | CED (3-seed) | flat-NLI (4-seed) | Δ (CED − flat-NLI) |\n|--------|-------------|-------------------|---------------------|\n| F1 | 45.96 ± 1.27 | 45.57 ± 0.39 | +0.39pp |\n| Evi-F1 | 81.43 ± 0.51 | 81.22 ± 0.49 | +0.21pp |\n| EDCR | 0.6434 ± 0.011 | 0.6479 ± 0.004 | −0.0045 |\n\n**Dream v1 p-values**: 0.08 / 0.38 / 0.12 — **not statistically significant** at α=0.05.\n\n### top_k Ablation (CED only)\n\n| Config | F1 | Ign-F1 | Evi-F1 | EDCR | Training samples | exp_id |\n|--------|------|--------|--------|------|-----------------|--------|\n| k=1 (3-seed mean) | 45.96 | 45.00 | 81.43 | 0.6434 | 2,718 (12.4%) | `s42/s43/s44` |\n| k=3 (1 seed, s42) | 44.54 | 43.64 | 80.88 | 0.6635 | 8,037 (37%) | `reeval_rsft_topk3` |\n| **Δ (k=3 − k=1)** | **−1.42** | **−1.36** | **−0.55** | **+0.02** | **+5,319** | |\n\n**Notes**:\n- k=3 uses 2.96× more training data but lower quality: mean_f1=0.5761 vs k=1 mean_f1=0.6157; mean_ced=0.6205 vs k=1 mean_ced=0.6683 (`mvp2_rsft_ced_scoring` vs `mvp2_rsft_ced_scoring_topk3_r2`).\n- k=3 has only 1 seed — direction consistent but no significance test possible. Present as supplementary ablation.\n\n### D076 Unified Protocol Reeval Status\n\nValid paired t-test requires all seeds evaluated under identical protocol (batch_size=4, --no-quantize, --sft_adapter, max_new_tokens=1024).\n\n| Target | Issue | Unified Reeval | Status |\n|--------|-------|---------------|--------|\n| CED s42 | Wrong checkpoint (r2b α=32) | `reeval_ced_s42` | PREPARING |\n| CED s44 | Wrong seed in eval (used s42) | `reeval_ced_s44` | PREPARING |\n| flat-NLI s42 | batch_size=16 | `reeval_flat_nli_s42` | PREPARING |\n| flat-NLI s43 | batch_size=16 | `reeval_flat_nli_s43_r2` | RUNNING |\n\n**Impact**: Current numbers are directional only. Paired t-test blocked until all 8 evals (4 CED + 4 flat-NLI) use unified protocol.\n\n---\n\n## Cross-Table: EDCR Method-Level Summary (Claim 4 support)\n\n| Method | EDCR | F1 | Evi-F1 | exp_id |\n|--------|------|------|--------|--------|\n| GRPO QLoRA (lr=5e-6) | 0.9876 | 1.38 | 85.04 | `mvp2_eval_lr5e6_r1_ckpt100` |\n| GRPO QLoRA (lr=5e-5) | 0.8539 | 21.67 | 57.46 | `mvp2_eval_ced_kl001_r4_step100` |\n| DPO 3ep | 0.7294 | 34.29 | 84.03 | `plan_012_dpo_ced` |\n| SFT baseline (quantized) | 0.7118 | 40.57 | 79.79 | `mvp2_eval_sft_baseline` |\n| DPO 1ep | 0.7139 | 40.34 | 80.88 | `eval_plan_012_dpo_1ep_fixed_r2` |\n| SFT baseline (noquant) | 0.7039 | 41.06 | 80.13 | `eval_sft_baseline_noquant` |\n| RSFT CED k=3 | 0.6635 | 44.54 | 80.88 | `reeval_rsft_topk3` |\n| RSFT r2a (1ep, α=128) | 0.6641 | 44.94 | 81.08 | `mvp2_eval_rsft_r2a` |\n| RSFT r2b (1ep, α=32) | 0.6609 | 44.93 | 81.28 | `mvp2_eval_rsft_r2b` |\n| RSFT CED s42 (3ep) | 0.6565 | 44.49 | 81.87 | `mvp2_eval_rsft_r1` |\n| flat-NLI s43 | 0.6505 | 45.23 | 81.58 | `reeval_flat_nli_s43` |\n| flat-NLI s45 | 0.6521 | 45.51 | 81.54 | `eval_flat_nli_seed45` |\n| flat-NLI s44 | 0.6458 | 46.15 | 81.31 | `eval_flat_nli_s44` |\n| flat-NLI s42 | 0.6431 | 45.39 | 80.43 | `eval_plan_001_flat_nli` |\n| RSFT CED s43 | 0.6388 | 46.83 | 81.56 | `mvp2_eval_rsft_s43_r2` |\n| RSFT CED s44 | 0.6350 | 46.55 | 80.87 | `mvp2_rsft_train_r1_s44` |\n| GRPO bf16 G=8 (ckpt100) | 0.6318 | 45.49 | 80.86 | `plan_011_grpo_g8_bf16_eval` |\n| **CED reranker** | **0.6156** | **48.64** | **81.88** | `mvp2_ced_reranker_poc` |\n\n**Correlations** (`plan_003_edcr_diagnostic`):\n- Method-level: EDCR vs rel_f1 Spearman ρ = −0.9648 (p=0.0001); EDCR vs evi_f1 ρ = 0.0022 (p=0.9941)\n- Per-relation (D070, 93 types ≥5 samples): EDCR vs evi_f1 ρ = −0.064 (p=0.58) — **completely independent**; EDCR vs rel_f1 ρ = −0.793 (p<0.001)\n\n---\n\n## Summary: Data Completeness\n\n### Paper-ready numbers\n1. Evidence tax: 47.36 → 40.36 = −7.00pp Ign-F1 ✓\n2. CED reranker: F1=48.64, −0.29pp below no-evidence ✓\n3. RSFT CED best: Ign-F1=45.85, +5.49pp over SFT ✓\n4. Decoupling spectrum: GRPO QLoRA / GRPO bf16 / DPO / RSFT — all data points present ✓\n5. QLoRA amplification: bf16 45.49 vs QLoRA 1.38 ✓\n6. EDCR per-relation independence: ρ=−0.064 ✓\n7. top_k ablation: k=1 > k=3 ✓\n8. DREEAM baseline: F1=63.57, Evi-F1=54.01 ✓\n\n### Critical PENDING (blocking paper)\n1. **CED reranker Ign-F1** — needed for Table 1 main column\n2. **D076 unified protocol reevals** (4 experiments) — blocking Claim 3 paired t-test\n3. **CED s45 eval** — blocking 4-seed CED statistics\n4. **Corrected Ign-F1** for flat-NLI s43/s44/s45, DPO 3ep, GRPO QLoRA — need metrics_v2 re-computation\n5. **Test set evaluation** (plan_002) — no official numbers yet\n\n### Nice-to-have\n1. EDCR human validation (plan_013) — RC6\n2. Post-hoc retrieval baseline (SFT + BM25) — RC10\n3. TP-only EDCR (D071) — method-level confound resolution\n",
      "numLines": 210,
      "startLine": 1,
      "totalLines": 210
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01HteR5aJ2bqcn5zv3m5ndG4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/comprehensive_results.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "7da4209c-fceb-45be-854c-828307dc558a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrSYXG3X2RG6iDzESuXvkp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6171,
      "cache_read_input_tokens": 24346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6171
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

_source line 20 · 2026-05-21T22:56:07.155Z_

<details><summary>↩ Tool result · `toolu_01HteR5aJ2bqcn5zv3m5ndG4`</summary>

```text
1	# Comprehensive Experiment Results — Faith-Evidence-IE
2	
3	> Generated: 2026-05-19 | Source: registry (conclusion=success) + memory.md
4	> All metrics on DocRED dev set. Eval protocol: D076 unless noted.
5	> Std = sample std (n-1). pp = percentage points.
6	
7	---
8	
9	## Table 1: Scale x Method — ign_f1
10	
11	| Scale | SFT | RSFT CED k=1 | RSFT Random k=1 | GRPO bf16 | No-evidence SFT |
12	|-------|-----|---------------|-----------------|-----------|-----------------|
13	| 1.7B | 0.4464+/-2.79pp (n=3) | k=1 eval pending | -- | -- | 0.3982 |
14	| 4B | 0.4358+/-3.80pp (n=3) | 0.4466+/-0.53pp (n=4) | 0.4114 (n=1) | G4: 0.4431 / G8: 0.4549 | 0.4721 |
15	| 8B | 0.4866+/-2.62pp (n=2) | 0.5451 (n=1, s44) | -- | -- | 0.5079 |
16	| 14B | pending (train done) | -- | -- | -- | pending |
17	
18	### Table 1 Source exp_ids
19	
20	**1.7B SFT**: plan_006_qwen3_1_7b_sft_eval (s42, 0.4786), plan019_1_7b_sft_s43_eval (s43, 0.4286), plan019_1_7b_sft_s44_eval (s44, 0.4321)
21	**1.7B No-evidence**: plan_006_qwen3_1_7b_no_evidence_eval_v3 (s42, 0.3982)
22	**4B SFT**: reeval_sft_baseline_d076 (s42, 0.3974), wave1_sft_4b_s43_eval_r2 (s43, 0.4365), wave1_sft_4b_s44_eval_r2 (s44, 0.4734)
23	**4B RSFT CED k=1**: reeval_ced_s42 (0.4423), eval_rsft_ced_s43 (0.4512), reeval_ced_s44 (0.4511), eval_rsft_ced_s45 (0.4416)
24	**4B RSFT Random k=1**: random_rsft_k1_eval (s42, 0.4114)
25	**4B GRPO G=4**: grpo_bf16_g4_ckpt100_eval (ckpt-100, 0.4431)
26	**4B GRPO G=8**: plan_011_grpo_g8_bf16_eval (ckpt-100, 0.4549)
27	**4B No-evidence**: plan_014_no_evidence_eval_d076 (s42, 0.4721)
28	**8B SFT**: plan_006_qwen3_8b_sft_eval (s42, 0.5051), plan019_8b_sft_s44_eval (s44, 0.4681)
29	**8B RSFT CED k=1**: plan019_8b_rsft_s44_eval (s44, 0.5451); s42 eval pending (d102_8b_rsft_k1_s42 train-only)
30	**8B No-evidence**: plan_006_qwen3_8b_no_evidence_eval_v2 (s42, 0.5079)
31	
32	### Supplementary: RSFT CED k=3 results (older pipeline)
33	
34	| Scale | Seeds | ign_f1 (mean+/-std) | Source |
35	|-------|-------|---------------------|--------|
36	| 1.7B | s42, s43 | 0.5037+/-0.18pp | plan_006_qwen3_1_7b_rsft_eval_r2 (0.5050), plan_006_qwen3_1_7b_rsft_seed43_eval (0.5024) |
37	| 8B | s42 | 0.5433 | plan_006_qwen3_8b_rsft_eval (0.5433) |
38	
39	### Supplementary: 8B RSFT from memory.md (not all in success registry)
40	
41	| Seed | SFT ign_f1 | RSFT k=1 ign_f1 | RSFT gain | Source |
42	|------|-----------|-----------------|-----------|--------|
43	| s42 | 0.5051 | 0.5376 | +3.25pp | memory.md (eval result not in success registry) |
44	| s44 | 0.4681 | 0.5451 | +7.70pp | registry: plan019_8b_rsft_s44_eval |
45	| Mean | 0.4866 | 0.5414 | +5.48pp | |
46	| Std | 2.62pp | 0.53pp | | variance reduction ~4.9x |
47	
48	---
49	
50	## Table 2: Evidence Metrics (evi_f1, EDCR)
51	
52	| Scale | Method | Seed | evi_f1 | EDCR | rel_f1 | Source exp_id |
53	|-------|--------|------|--------|------|--------|---------------|
54	| **1.7B** | SFT | s42 | 0.8316 | 0.6704 | 0.4945 | plan_006_qwen3_1_7b_sft_eval |
55	| | SFT | s43 | 0.8350 | 0.7040 | 0.4372 | plan019_1_7b_sft_s43_eval |
56	| | SFT | s44 | 0.8190 | 0.6900 | 0.4441 | plan019_1_7b_sft_s44_eval |
57	| | RSFT k=3 | s42 | 0.8309 | 0.6297 | 0.5219 | plan_006_qwen3_1_7b_rsft_eval_r2 |
58	| | RSFT k=3 | s43 | 0.8341 | 0.6246 | 0.5180 | plan_006_qwen3_1_7b_rsft_seed43_eval |
59	| **4B** | SFT | s42 | 0.7986 | 0.6982 | 0.4049 | reeval_sft_baseline_d076 |
60	| | SFT | s43 | 0.8021 | 0.6827 | 0.4429 | wave1_sft_4b_s43_eval_r2 |
61	| | SFT | s44 | 0.7875 | 0.6581 | 0.4838 | wave1_sft_4b_s44_eval_r2 |
62	| | RSFT CED k=1 | s42 | 0.8175 | 0.6569 | 0.4517 | reeval_ced_s42 |
63	| | RSFT CED k=1 | s43 | 0.8063 | 0.6542 | 0.4601 | eval_rsft_ced_s43 |
64	| | RSFT CED k=1 | s44 | 0.8050 | 0.6350 | 0.4621 | reeval_ced_s44 |
65	| | RSFT CED k=1 | s45 | 0.8174 | 0.6550 | 0.4514 | eval_rsft_ced_s45 |
66	| | RSFT Random k=1 | s42 | 0.7964 | 0.6971 | 0.4198 | random_rsft_k1_eval |
67	| | GRPO bf16 G=4 | ckpt100 | 0.8010 | 0.6453 | 0.4511 | grpo_bf16_g4_ckpt100_eval |
68	| | GRPO bf16 G=8 | ckpt100 | 0.8086 | 0.6318 | 0.4549 | plan_011_grpo_g8_bf16_eval |
69	| **8B** | SFT | s42 | 0.8188 | 0.6510 | 0.5262 | plan_006_qwen3_8b_sft_eval |
70	| | SFT | s44 | 0.8361 | 0.6697 | 0.4841 | plan019_8b_sft_s44_eval |
71	| | RSFT CED k=3 | s42 | 0.8052 | 0.6377 | 0.5606 | plan_006_qwen3_8b_rsft_eval |
72	| | RSFT CED k=1 | s44 | 0.8145 | 0.6233 | 0.5620 | plan019_8b_rsft_s44_eval |
73	
74	### Evidence Metrics Aggregated (4B, mean+/-std)
75	
76	| Method | evi_f1 | EDCR |
77	|--------|--------|------|
78	| SFT (n=3) | 0.7961+/-0.76pp | 0.6797+/-2.02pp |
79	| RSFT CED k=1 (n=4) | 0.8115+/-0.68pp | 0.6503+/-1.02pp |
80	| Delta (RSFT-SFT) | +1.55pp | -2.94pp |
81	
82	Interpretation: RSFT improves evi_f1 (+1.55pp) while reducing EDCR (-2.94pp). Since EDCR is inversely correlated with rel_f1 (Spearman rho=-0.96, plan_003_edcr_diagnostic), lower EDCR indicates more discriminative evidence, not worse evidence.
83	
84	---
85	
86	## Table 3: Seed Variance Analysis
87	
88	| Scale | Method | Seeds | Mean | Std | Individual values | Variance reduction |
89	|-------|--------|-------|------|-----|-------------------|--------------------|
90	| **1.7B** | SFT | s42, s43, s44 | 0.4464 | 2.79pp | 0.4786, 0.4286, 0.4321 | -- |
91	| | RSFT CED k=3 | s42, s43 | 0.5037 | 0.18pp | 0.5050, 0.5024 | 15.2x (vs SFT) |
92	| **4B** | SFT | s42, s43, s44 | 0.4358 | 3.80pp | 0.3974, 0.4365, 0.4734 | -- |
93	| | RSFT CED k=1 | s42-s45 | 0.4466 | 0.53pp | 0.4423, 0.4512, 0.4511, 0.4416 | **7.1x** |
94	| | RSFT flat-NLI | s42-s45 | 0.4484 | 0.34pp | 0.4448, 0.4503, 0.4521, 0.4462 | 11.2x |
95	| **8B** | SFT | s42, s44 | 0.4866 | 2.62pp | 0.5051, 0.4681 | -- |
96	| | RSFT CED k=1 | s42, s44 | 0.5414 | 0.53pp | 0.5376*, 0.5451 | **4.9x** |
97	
98	\* 8B RSFT s42=0.5376 from memory.md; not in success registry. plan019_8b_rsft_s44_eval confirmed.
99	
100	### Per-seed RSFT gain (4B, CED k=1 vs SFT)
101	
102	| Seed | SFT ign_f1 | RSFT ign_f1 | Gain |
103	|------|-----------|-------------|------|
104	| s42 (weakest) | 0.3974 | 0.4423 | **+4.49pp** |
105	| s43 | 0.4365 | 0.4512 | +1.47pp |
106	| s44 (strongest) | 0.4734 | 0.4511 | -2.23pp |
107	
108	Key: RSFT amplifies weak seeds (+4.49pp for s42) and compresses strong seeds (-2.23pp for s44), converging toward a stable performance band (0.44-0.45). This is the "variance stabilization" effect.
109	
110	---
111	
112	## Table 4: Evidence Tax (with vs without evidence)
113	
114	Evidence Tax = ign_f1(no-evidence) - ign_f1(with-evidence). Positive = evidence generation hurts RE.
115	
116	| Scale | SFT (evidence) | SFT (no-evidence) | Tax | Direction | Source (evidence) | Source (no-evidence) |
117	|-------|-----------------|--------------------|-----|-----------|-------------------|---------------------|
118	| 1.7B | 0.4786 (s42) | 0.3982 (s42) | **-8.04pp** | Evidence HELPS | plan_006_qwen3_1_7b_sft_eval | plan_006_qwen3_1_7b_no_evidence_eval_v3 |
119	| 4B | 0.3974 (s42) | 0.4721 (s42) | **+7.47pp** | Evidence HURTS | reeval_sft_baseline_d076 | plan_014_no_evidence_eval_d076 |
120	| 8B | 0.5051 (s42) | 0.5079 (s42) | **+0.28pp** | Minimal tax | plan_006_qwen3_8b_sft_eval | plan_006_qwen3_8b_no_evidence_eval_v2 |
121	
122	Interpretation: Non-monotonic evidence tax across scales. At 1.7B, evidence acts as CoT, boosting ign_f1 by 8pp. At 4B, the evidence generation burden causes a 7.5pp penalty. At 8B, the model is capable enough to handle both tasks with negligible cost.
123	
124	---
125	
126	## Table 5: RSFT Scoring Ablation (4B, k=1)
127	
128	| Scoring Method | Seeds | ign_f1 (mean+/-std) | Individual values |
129	|----------------|-------|---------------------|-------------------|
130	| CED (format+f1+ced) | s42-s45 | 0.4466+/-0.53pp | 0.4423, 0.4512, 0.4511, 0.4416 |
131	| flat-NLI (format+f1+nli) | s42-s45 | 0.4484+/-0.34pp | 0.4448, 0.4503, 0.4521, 0.4462 |
132	| Random selection | s42 | 0.4114 | -- |
133	| Delta CED vs Random | -- | **+3.52pp** | -- |
134	| Delta CED vs flat-NLI | -- | -0.18pp (n.s.) | -- |
135	
136	Source exp_ids:
137	- CED: reeval_ced_s42, eval_rsft_ced_s43, reeval_ced_s44, eval_rsft_ced_s45
138	- flat-NLI: reeval_flat_nli_s42, reeval_flat_nli_s43_r2, eval_flat_nli_s44, eval_flat_nli_seed45
139	- Random: random_rsft_k1_eval
140	
141	---
142	
143	## Table 6: GRPO Checkpoint Analysis (4B)
144	
145	### G=4 (grpo_bf16_g4)
146	| Checkpoint | ign_f1 | rel_f1 | evi_f1 | EDCR | Source |
147	|-----------|--------|--------|--------|------|--------|
148	| ckpt-100 | 0.4431 | 0.4511 | 0.8010 | 0.6453 | grpo_bf16_g4_ckpt100_eval |
149	| ckpt-200 | 0.4446 | 0.4513 | 0.8053 | 0.6489 | grpo_bf16_g4_ckpt200_eval |
150	
151	### G=8 (grpo_bf16_g8)
152	| Checkpoint | ign_f1 | rel_f1 | evi_f1 | EDCR | Source |
153	|-----------|--------|--------|--------|------|--------|
154	| ckpt-80 | 0.4456 | 0.4456 | 0.8034 | 0.6409 | eval_grpo_g8_bf16 ckpt-80 |
155	| ckpt-90 | 0.4523 | 0.4523 | 0.8052 | 0.6414 | eval_grpo_g8_bf16 ckpt-90 |
156	| ckpt-100 | **0.4549** | 0.4549 | 0.8086 | 0.6318 | plan_011_grpo_g8_bf16_eval |
157	
158	GRPO best (G=8 ckpt-100): +5.75pp over SFT s42 baseline (0.3974)
159	
160	### RSFT->GRPO (lead2)
161	| Checkpoint | ign_f1 | rel_f1 | evi_f1 | EDCR | Source |
162	|-----------|--------|--------|--------|------|--------|
163	| ckpt-20 | 0.4533 | 0.4617 | 0.8103 | 0.6465 | lead2_ckpt20_eval |
164	
165	---
166	
167	## Table 7: CED Reranker (Inference-time, no fine-tuning)
168	
169	N=8 SFT candidates, 4B.
170	
171	| Selection Strategy | ign_f1 | rel_f1 | evi_f1 |
172	|-------------------|--------|--------|--------|
173	| CED reranker | **0.4736** | 0.4864 | 0.8188 |
174	| Oracle (upper bound) | 0.6125 | 0.6237 | -- |
175	| Random (lower bound) | 0.4397 | 0.4538 | -- |
176	
177	CED reranker achieves 0.4736, comparable to best SFT seed s44 (0.4734), without any fine-tuning.
178	
179	---
180	
181	## Table 8: Cross-Architecture (Llama-3.1-8B)
182	
183	| Method | Seeds | ign_f1 | rel_f1 | evi_f1 | EDCR | Source |
184	|--------|-------|--------|--------|--------|------|--------|
185	| SFT | s42 | 0.5384 | 0.5514 | 0.8151 | 0.6280 | plan_016_llama_3_1_8b_sft_eval |
186	| No-evidence SFT | s42 | 0.5452 | 0.5624 | 0 | 0 | plan_016_llama_3_1_8b_no_evidence_eval |
187	| RSFT CED k=3 | s42 | 0.5563 | 0.5674 | 0.8255 | 0.5856 | plan_006_llama_rsft_r3_eval |
188	| RSFT CED k=3 | s43 | 0.5619 | 0.5727 | 0.8206 | 0.6073 | plan_006_llama_rsft_seed43_eval_r2 |
189	| RSFT CED k=1 | s43 | 0.5662 | 0.5780 | 0.8287 | 0.5783 | seed_llama_rsft_k1_s43_eval |
190	| Evidence Tax | -- | +0.68pp | -- | -- | -- | (0.5452-0.5384) |
191	
192	---
193	
194	## Table 9: Re-DocRED Transfer (4B)
195	
196	| Method | ign_f1 | rel_f1 | evi_f1 | EDCR | Source |
197	|--------|--------|--------|--------|------|--------|
198	| SFT | 0.3659 | 0.3706 | 0.8170 | 0.6674 | plan_007_redocred_4b_sft_eval_r2 |
199	| RSFT CED | 0.4145 | 0.4234 | 0.8182 | 0.6210 | plan_007_redocred_rsft_eval_r5 |
200	| Delta RSFT-SFT | +4.86pp | +5.28pp | +0.12pp | -4.64pp | |
201	
202	---
203	
204	## Table 10: DREEAM Baseline (RoBERTa-large, supervised)
205	
206	| Metric | Dev Score | Source |
207	|--------|-----------|--------|
208	| rel_f1 | 63.57 | plan_004_dreeam_baseline |
209	| ign_f1 | 61.72 | plan_004_dreeam_baseline |
210	| evi_f1 | 54.01 | plan_004_dreeam_baseline |
211	
212	Note: Scores on 0-100 scale (i.e. 0.6357, 0.6172, 0.5401 on 0-1 scale).
213	
214	---
215	
216	## Pending Experiments
217	
218	| Scale | Method | Status | Exp_id |
219	|-------|--------|--------|--------|
220	| 14B | SFT eval | Train done, eval pending | plan017_14b_sft |
221	| 14B | No-evidence | Not started | -- |
222	| 8B | RSFT CED k=1 s42 eval | Train done, eval pending | d102_8b_rsft_k1_s42 |
223	| 8B | RSFT CED k=1 s43 eval | Train done, eval pending | d102_8b_rsft_k1_s43 |
224	| 1.7B | RSFT CED k=1 (all seeds) | Eval pending | d102_1_7b_rsft_k1_s42 (train-only) |
225	| 4B | RSFT CED from SFT s44 | Pipeline in progress | D112 pipeline |
226	
227	---
228	
229	## Key Findings
230	
231	1. **RSFT variance stabilization is the strongest result.** 4B SFT std=3.80pp -> RSFT CED k=1 std=0.53pp (7.1x reduction). 8B shows ~4.9x reduction. RSFT pulls weak seeds UP (+4.49pp for 4B s42) and compresses strong seeds DOWN (-2.23pp for 4B s44), converging all seeds toward a stable performance band. This is not just performance improvement but a qualitatively different training property.
232	
233	2. **CED scoring >> Random selection, but approximately equal to flat-NLI.** CED k=1 beats Random by +3.52pp (0.4466 vs 0.4114). CED vs flat-NLI differ by only 0.18pp (not significant). The critical factor is non-random data selection, not the specific scoring function.
234	
235	3. **Evidence tax is non-monotonic across scales.** 1.7B: evidence HELPS by 8.04pp (CoT effect). 4B: evidence HURTS by 7.47pp (generation burden). 8B: negligible 0.28pp tax. Suggests an optimal scale threshold where evidence generation becomes "free."
236	
237	4. **GRPO bf16 works, QLoRA GRPO catastrophically fails.** bf16 GRPO G=8 ckpt-100 achieves 0.4549 (+5.75pp over SFT s42), while QLoRA GRPO produces near-zero f1_reward across both Qwen and Llama families. Precision is a hard requirement for RL on structured IE.
238	
239	5. **RSFT gains transfer cross-architecture and cross-dataset.** Llama-3.1-8B RSFT CED k=1: 0.5662 (+2.78pp over SFT). Re-DocRED RSFT: 0.4145 (+4.86pp over SFT). The method is not Qwen-specific or DocRED-specific.
240	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "752ffa33-e66d-4596-afe5-d8e1c7ac72e4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/comprehensive_results.md",
      "content": "# Comprehensive Experiment Results — Faith-Evidence-IE\n\n> Generated: 2026-05-19 | Source: registry (conclusion=success) + memory.md\n> All metrics on DocRED dev set. Eval protocol: D076 unless noted.\n> Std = sample std (n-1). pp = percentage points.\n\n---\n\n## Table 1: Scale x Method — ign_f1\n\n| Scale | SFT | RSFT CED k=1 | RSFT Random k=1 | GRPO bf16 | No-evidence SFT |\n|-------|-----|---------------|-----------------|-----------|-----------------|\n| 1.7B | 0.4464+/-2.79pp (n=3) | k=1 eval pending | -- | -- | 0.3982 |\n| 4B | 0.4358+/-3.80pp (n=3) | 0.4466+/-0.53pp (n=4) | 0.4114 (n=1) | G4: 0.4431 / G8: 0.4549 | 0.4721 |\n| 8B | 0.4866+/-2.62pp (n=2) | 0.5451 (n=1, s44) | -- | -- | 0.5079 |\n| 14B | pending (train done) | -- | -- | -- | pending |\n\n### Table 1 Source exp_ids\n\n**1.7B SFT**: plan_006_qwen3_1_7b_sft_eval (s42, 0.4786), plan019_1_7b_sft_s43_eval (s43, 0.4286), plan019_1_7b_sft_s44_eval (s44, 0.4321)\n**1.7B No-evidence**: plan_006_qwen3_1_7b_no_evidence_eval_v3 (s42, 0.3982)\n**4B SFT**: reeval_sft_baseline_d076 (s42, 0.3974), wave1_sft_4b_s43_eval_r2 (s43, 0.4365), wave1_sft_4b_s44_eval_r2 (s44, 0.4734)\n**4B RSFT CED k=1**: reeval_ced_s42 (0.4423), eval_rsft_ced_s43 (0.4512), reeval_ced_s44 (0.4511), eval_rsft_ced_s45 (0.4416)\n**4B RSFT Random k=1**: random_rsft_k1_eval (s42, 0.4114)\n**4B GRPO G=4**: grpo_bf16_g4_ckpt100_eval (ckpt-100, 0.4431)\n**4B GRPO G=8**: plan_011_grpo_g8_bf16_eval (ckpt-100, 0.4549)\n**4B No-evidence**: plan_014_no_evidence_eval_d076 (s42, 0.4721)\n**8B SFT**: plan_006_qwen3_8b_sft_eval (s42, 0.5051), plan019_8b_sft_s44_eval (s44, 0.4681)\n**8B RSFT CED k=1**: plan019_8b_rsft_s44_eval (s44, 0.5451); s42 eval pending (d102_8b_rsft_k1_s42 train-only)\n**8B No-evidence**: plan_006_qwen3_8b_no_evidence_eval_v2 (s42, 0.5079)\n\n### Supplementary: RSFT CED k=3 results (older pipeline)\n\n| Scale | Seeds | ign_f1 (mean+/-std) | Source |\n|-------|-------|---------------------|--------|\n| 1.7B | s42, s43 | 0.5037+/-0.18pp | plan_006_qwen3_1_7b_rsft_eval_r2 (0.5050), plan_006_qwen3_1_7b_rsft_seed43_eval (0.5024) |\n| 8B | s42 | 0.5433 | plan_006_qwen3_8b_rsft_eval (0.5433) |\n\n### Supplementary: 8B RSFT from memory.md (not all in success registry)\n\n| Seed | SFT ign_f1 | RSFT k=1 ign_f1 | RSFT gain | Source |\n|------|-----------|-----------------|-----------|--------|\n| s42 | 0.5051 | 0.5376 | +3.25pp | memory.md (eval result not in success registry) |\n| s44 | 0.4681 | 0.5451 | +7.70pp | registry: plan019_8b_rsft_s44_eval |\n| Mean | 0.4866 | 0.5414 | +5.48pp | |\n| Std | 2.62pp | 0.53pp | | variance reduction ~4.9x |\n\n---\n\n## Table 2: Evidence Metrics (evi_f1, EDCR)\n\n| Scale | Method | Seed | evi_f1 | EDCR | rel_f1 | Source exp_id |\n|-------|--------|------|--------|------|--------|---------------|\n| **1.7B** | SFT | s42 | 0.8316 | 0.6704 | 0.4945 | plan_006_qwen3_1_7b_sft_eval |\n| | SFT | s43 | 0.8350 | 0.7040 | 0.4372 | plan019_1_7b_sft_s43_eval |\n| | SFT | s44 | 0.8190 | 0.6900 | 0.4441 | plan019_1_7b_sft_s44_eval |\n| | RSFT k=3 | s42 | 0.8309 | 0.6297 | 0.5219 | plan_006_qwen3_1_7b_rsft_eval_r2 |\n| | RSFT k=3 | s43 | 0.8341 | 0.6246 | 0.5180 | plan_006_qwen3_1_7b_rsft_seed43_eval |\n| **4B** | SFT | s42 | 0.7986 | 0.6982 | 0.4049 | reeval_sft_baseline_d076 |\n| | SFT | s43 | 0.8021 | 0.6827 | 0.4429 | wave1_sft_4b_s43_eval_r2 |\n| | SFT | s44 | 0.7875 | 0.6581 | 0.4838 | wave1_sft_4b_s44_eval_r2 |\n| | RSFT CED k=1 | s42 | 0.8175 | 0.6569 | 0.4517 | reeval_ced_s42 |\n| | RSFT CED k=1 | s43 | 0.8063 | 0.6542 | 0.4601 | eval_rsft_ced_s43 |\n| | RSFT CED k=1 | s44 | 0.8050 | 0.6350 | 0.4621 | reeval_ced_s44 |\n| | RSFT CED k=1 | s45 | 0.8174 | 0.6550 | 0.4514 | eval_rsft_ced_s45 |\n| | RSFT Random k=1 | s42 | 0.7964 | 0.6971 | 0.4198 | random_rsft_k1_eval |\n| | GRPO bf16 G=4 | ckpt100 | 0.8010 | 0.6453 | 0.4511 | grpo_bf16_g4_ckpt100_eval |\n| | GRPO bf16 G=8 | ckpt100 | 0.8086 | 0.6318 | 0.4549 | plan_011_grpo_g8_bf16_eval |\n| **8B** | SFT | s42 | 0.8188 | 0.6510 | 0.5262 | plan_006_qwen3_8b_sft_eval |\n| | SFT | s44 | 0.8361 | 0.6697 | 0.4841 | plan019_8b_sft_s44_eval |\n| | RSFT CED k=3 | s42 | 0.8052 | 0.6377 | 0.5606 | plan_006_qwen3_8b_rsft_eval |\n| | RSFT CED k=1 | s44 | 0.8145 | 0.6233 | 0.5620 | plan019_8b_rsft_s44_eval |\n\n### Evidence Metrics Aggregated (4B, mean+/-std)\n\n| Method | evi_f1 | EDCR |\n|--------|--------|------|\n| SFT (n=3) | 0.7961+/-0.76pp | 0.6797+/-2.02pp |\n| RSFT CED k=1 (n=4) | 0.8115+/-0.68pp | 0.6503+/-1.02pp |\n| Delta (RSFT-SFT) | +1.55pp | -2.94pp |\n\nInterpretation: RSFT improves evi_f1 (+1.55pp) while reducing EDCR (-2.94pp). Since EDCR is inversely correlated with rel_f1 (Spearman rho=-0.96, plan_003_edcr_diagnostic), lower EDCR indicates more discriminative evidence, not worse evidence.\n\n---\n\n## Table 3: Seed Variance Analysis\n\n| Scale | Method | Seeds | Mean | Std | Individual values | Variance reduction |\n|-------|--------|-------|------|-----|-------------------|--------------------|\n| **1.7B** | SFT | s42, s43, s44 | 0.4464 | 2.79pp | 0.4786, 0.4286, 0.4321 | -- |\n| | RSFT CED k=3 | s42, s43 | 0.5037 | 0.18pp | 0.5050, 0.5024 | 15.2x (vs SFT) |\n| **4B** | SFT | s42, s43, s44 | 0.4358 | 3.80pp | 0.3974, 0.4365, 0.4734 | -- |\n| | RSFT CED k=1 | s42-s45 | 0.4466 | 0.53pp | 0.4423, 0.4512, 0.4511, 0.4416 | **7.1x** |\n| | RSFT flat-NLI | s42-s45 | 0.4484 | 0.34pp | 0.4448, 0.4503, 0.4521, 0.4462 | 11.2x |\n| **8B** | SFT | s42, s44 | 0.4866 | 2.62pp | 0.5051, 0.4681 | -- |\n| | RSFT CED k=1 | s42, s44 | 0.5414 | 0.53pp | 0.5376*, 0.5451 | **4.9x** |\n\n\\* 8B RSFT s42=0.5376 from memory.md; not in success registry. plan019_8b_rsft_s44_eval confirmed.\n\n### Per-seed RSFT gain (4B, CED k=1 vs SFT)\n\n| Seed | SFT ign_f1 | RSFT ign_f1 | Gain |\n|------|-----------|-------------|------|\n| s42 (weakest) | 0.3974 | 0.4423 | **+4.49pp** |\n| s43 | 0.4365 | 0.4512 | +1.47pp |\n| s44 (strongest) | 0.4734 | 0.4511 | -2.23pp |\n\nKey: RSFT amplifies weak seeds (+4.49pp for s42) and compresses strong seeds (-2.23pp for s44), converging toward a stable performance band (0.44-0.45). This is the \"variance stabilization\" effect.\n\n---\n\n## Table 4: Evidence Tax (with vs without evidence)\n\nEvidence Tax = ign_f1(no-evidence) - ign_f1(with-evidence). Positive = evidence generation hurts RE.\n\n| Scale | SFT (evidence) | SFT (no-evidence) | Tax | Direction | Source (evidence) | Source (no-evidence) |\n|-------|-----------------|--------------------|-----|-----------|-------------------|---------------------|\n| 1.7B | 0.4786 (s42) | 0.3982 (s42) | **-8.04pp** | Evidence HELPS | plan_006_qwen3_1_7b_sft_eval | plan_006_qwen3_1_7b_no_evidence_eval_v3 |\n| 4B | 0.3974 (s42) | 0.4721 (s42) | **+7.47pp** | Evidence HURTS | reeval_sft_baseline_d076 | plan_014_no_evidence_eval_d076 |\n| 8B | 0.5051 (s42) | 0.5079 (s42) | **+0.28pp** | Minimal tax | plan_006_qwen3_8b_sft_eval | plan_006_qwen3_8b_no_evidence_eval_v2 |\n\nInterpretation: Non-monotonic evidence tax across scales. At 1.7B, evidence acts as CoT, boosting ign_f1 by 8pp. At 4B, the evidence generation burden causes a 7.5pp penalty. At 8B, the model is capable enough to handle both tasks with negligible cost.\n\n---\n\n## Table 5: RSFT Scoring Ablation (4B, k=1)\n\n| Scoring Method | Seeds | ign_f1 (mean+/-std) | Individual values |\n|----------------|-------|---------------------|-------------------|\n| CED (format+f1+ced) | s42-s45 | 0.4466+/-0.53pp | 0.4423, 0.4512, 0.4511, 0.4416 |\n| flat-NLI (format+f1+nli) | s42-s45 | 0.4484+/-0.34pp | 0.4448, 0.4503, 0.4521, 0.4462 |\n| Random selection | s42 | 0.4114 | -- |\n| Delta CED vs Random | -- | **+3.52pp** | -- |\n| Delta CED vs flat-NLI | -- | -0.18pp (n.s.) | -- |\n\nSource exp_ids:\n- CED: reeval_ced_s42, eval_rsft_ced_s43, reeval_ced_s44, eval_rsft_ced_s45\n- flat-NLI: reeval_flat_nli_s42, reeval_flat_nli_s43_r2, eval_flat_nli_s44, eval_flat_nli_seed45\n- Random: random_rsft_k1_eval\n\n---\n\n## Table 6: GRPO Checkpoint Analysis (4B)\n\n### G=4 (grpo_bf16_g4)\n| Checkpoint | ign_f1 | rel_f1 | evi_f1 | EDCR | Source |\n|-----------|--------|--------|--------|------|--------|\n| ckpt-100 | 0.4431 | 0.4511 | 0.8010 | 0.6453 | grpo_bf16_g4_ckpt100_eval |\n| ckpt-200 | 0.4446 | 0.4513 | 0.8053 | 0.6489 | grpo_bf16_g4_ckpt200_eval |\n\n### G=8 (grpo_bf16_g8)\n| Checkpoint | ign_f1 | rel_f1 | evi_f1 | EDCR | Source |\n|-----------|--------|--------|--------|------|--------|\n| ckpt-80 | 0.4456 | 0.4456 | 0.8034 | 0.6409 | eval_grpo_g8_bf16 ckpt-80 |\n| ckpt-90 | 0.4523 | 0.4523 | 0.8052 | 0.6414 | eval_grpo_g8_bf16 ckpt-90 |\n| ckpt-100 | **0.4549** | 0.4549 | 0.8086 | 0.6318 | plan_011_grpo_g8_bf16_eval |\n\nGRPO best (G=8 ckpt-100): +5.75pp over SFT s42 baseline (0.3974)\n\n### RSFT->GRPO (lead2)\n| Checkpoint | ign_f1 | rel_f1 | evi_f1 | EDCR | Source |\n|-----------|--------|--------|--------|------|--------|\n| ckpt-20 | 0.4533 | 0.4617 | 0.8103 | 0.6465 | lead2_ckpt20_eval |\n\n---\n\n## Table 7: CED Reranker (Inference-time, no fine-tuning)\n\nN=8 SFT candidates, 4B.\n\n| Selection Strategy | ign_f1 | rel_f1 | evi_f1 |\n|-------------------|--------|--------|--------|\n| CED reranker | **0.4736** | 0.4864 | 0.8188 |\n| Oracle (upper bound) | 0.6125 | 0.6237 | -- |\n| Random (lower bound) | 0.4397 | 0.4538 | -- |\n\nCED reranker achieves 0.4736, comparable to best SFT seed s44 (0.4734), without any fine-tuning.\n\n---\n\n## Table 8: Cross-Architecture (Llama-3.1-8B)\n\n| Method | Seeds | ign_f1 | rel_f1 | evi_f1 | EDCR | Source |\n|--------|-------|--------|--------|--------|------|--------|\n| SFT | s42 | 0.5384 | 0.5514 | 0.8151 | 0.6280 | plan_016_llama_3_1_8b_sft_eval |\n| No-evidence SFT | s42 | 0.5452 | 0.5624 | 0 | 0 | plan_016_llama_3_1_8b_no_evidence_eval |\n| RSFT CED k=3 | s42 | 0.5563 | 0.5674 | 0.8255 | 0.5856 | plan_006_llama_rsft_r3_eval |\n| RSFT CED k=3 | s43 | 0.5619 | 0.5727 | 0.8206 | 0.6073 | plan_006_llama_rsft_seed43_eval_r2 |\n| RSFT CED k=1 | s43 | 0.5662 | 0.5780 | 0.8287 | 0.5783 | seed_llama_rsft_k1_s43_eval |\n| Evidence Tax | -- | +0.68pp | -- | -- | -- | (0.5452-0.5384) |\n\n---\n\n## Table 9: Re-DocRED Transfer (4B)\n\n| Method | ign_f1 | rel_f1 | evi_f1 | EDCR | Source |\n|--------|--------|--------|--------|------|--------|\n| SFT | 0.3659 | 0.3706 | 0.8170 | 0.6674 | plan_007_redocred_4b_sft_eval_r2 |\n| RSFT CED | 0.4145 | 0.4234 | 0.8182 | 0.6210 | plan_007_redocred_rsft_eval_r5 |\n| Delta RSFT-SFT | +4.86pp | +5.28pp | +0.12pp | -4.64pp | |\n\n---\n\n## Table 10: DREEAM Baseline (RoBERTa-large, supervised)\n\n| Metric | Dev Score | Source |\n|--------|-----------|--------|\n| rel_f1 | 63.57 | plan_004_dreeam_baseline |\n| ign_f1 | 61.72 | plan_004_dreeam_baseline |\n| evi_f1 | 54.01 | plan_004_dreeam_baseline |\n\nNote: Scores on 0-100 scale (i.e. 0.6357, 0.6172, 0.5401 on 0-1 scale).\n\n---\n\n## Pending Experiments\n\n| Scale | Method | Status | Exp_id |\n|-------|--------|--------|--------|\n| 14B | SFT eval | Train done, eval pending | plan017_14b_sft |\n| 14B | No-evidence | Not started | -- |\n| 8B | RSFT CED k=1 s42 eval | Train done, eval pending | d102_8b_rsft_k1_s42 |\n| 8B | RSFT CED k=1 s43 eval | Train done, eval pending | d102_8b_rsft_k1_s43 |\n| 1.7B | RSFT CED k=1 (all seeds) | Eval pending | d102_1_7b_rsft_k1_s42 (train-only) |\n| 4B | RSFT CED from SFT s44 | Pipeline in progress | D112 pipeline |\n\n---\n\n## Key Findings\n\n1. **RSFT variance stabilization is the strongest result.** 4B SFT std=3.80pp -> RSFT CED k=1 std=0.53pp (7.1x reduction). 8B shows ~4.9x reduction. RSFT pulls weak seeds UP (+4.49pp for 4B s42) and compresses strong seeds DOWN (-2.23pp for 4B s44), converging all seeds toward a stable performance band. This is not just performance improvement but a qualitatively different training property.\n\n2. **CED scoring >> Random selection, but approximately equal to flat-NLI.** CED k=1 beats Random by +3.52pp (0.4466 vs 0.4114). CED vs flat-NLI differ by only 0.18pp (not significant). The critical factor is non-random data selection, not the specific scoring function.\n\n3. **Evidence tax is non-monotonic across scales.** 1.7B: evidence HELPS by 8.04pp (CoT effect). 4B: evidence HURTS by 7.47pp (generation burden). 8B: negligible 0.28pp tax. Suggests an optimal scale threshold where evidence generation becomes \"free.\"\n\n4. **GRPO bf16 works, QLoRA GRPO catastrophically fails.** bf16 GRPO G=8 ckpt-100 achieves 0.4549 (+5.75pp over SFT s42), while QLoRA GRPO produces near-zero f1_reward across both Qwen and Llama families. Precision is a hard requirement for RL on structured IE.\n\n5. **RSFT gains transfer cross-architecture and cross-dataset.** Llama-3.1-8B RSFT CED k=1: 0.5662 (+2.78pp over SFT). Re-DocRED RSFT: 0.4145 (+4.86pp over SFT). The method is not Qwen-specific or DocRED-specific.\n",
      "numLines": 240,
      "startLine": 1,
      "totalLines": 240
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01Vmisvpds9HSBPHz5FtNRSM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/paper_evidence_table.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "98e840b9-8afb-4876-bec6-8899bfb83d85",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrSYXG3X2RG6iDzESuXvkp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6171,
      "cache_read_input_tokens": 24346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6171
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

_source line 22 · 2026-05-21T22:56:07.691Z_

<details><summary>↩ Tool result · `toolu_01Vmisvpds9HSBPHz5FtNRSM`</summary>

```text
1	# Paper Evidence Table — FREIGE (EMNLP 2026)
2	
3	> **Compiled**: 2026-05-16
4	> **Source**: experiment registry + paper_framing.md + decisions D067-D076
5	> **Convention**: Ign-F1/F1 as percentage (e.g., 40.36); rel_f1/evi_f1 as decimal (e.g., 0.4036) when directly from registry. Paper reports Ign-F1 in main table, F1 in appendix (D071).
6	
7	---
8	
9	## Claim 1: Evidence-grounded DocRE is a viable new capability
10	
11	**Statement**: FREIGE is the first LLM method to simultaneously output (head, relation, tail, [evidence]) on DocRED. Evidence generation has a ~7pp Ign-F1 cost; RSFT recovers most of it; CED reranker recovers 97%.
12	
13	### Supporting Experiments
14	
15	| exp_id | method | seed | F1 (rel_f1) | Ign-F1 | Evi-F1 | Evi-F1 (joint) | EDCR | protocol | notes |
16	|--------|--------|------|-------------|--------|--------|----------------|------|----------|-------|
17	| eval_plan_014_sft_no_evidence | SFT no-evidence | 42 | 48.93 | 47.36 | — | — | — | standard | Upper bound: no evidence burden |
18	| eval_sft_baseline_noquant | SFT baseline (noquant) | 42 | 41.06 | 40.36 | 80.13 | 32.16 | 0.7039 | standard | Primary SFT baseline for paper |
19	| mvp2_eval_sft_baseline | SFT baseline (quantized) | 42 | 40.57 | 40.57 | 79.79 | 31.17 | 0.7118 | unified (r3) | Quantized; -0.49pp vs noquant |
20	| mvp2_eval_rsft_s43_r2 | RSFT CED k=1 | 43 | 46.83 | 45.85 | 81.56 | 37.11 | 0.6388 | original | **Best RSFT seed** |
21	| mvp2_rsft_train_r1_s44 | RSFT CED k=1 | 44 | 46.55 | 45.51 | 80.87 | 37.13 | 0.6350 | original | |
22	| mvp2_eval_rsft_r1 | RSFT CED k=1 (3ep) | 42 | 44.49 | 43.63 | 81.87 | 34.68 | 0.6565 | original | 3-epoch; s42 |
23	| mvp2_eval_rsft_r2a | RSFT CED k=1 (1ep) | 42 | 44.94 | 44.01 | 81.08 | 35.09 | 0.6641 | original | 1-epoch ablation α=128 |
24	| mvp2_eval_rsft_r2b | RSFT CED k=1 (1ep) | 42 | 44.93 | 44.10 | 81.28 | 34.90 | 0.6609 | original | 1-epoch ablation α=32 |
25	| mvp2_ced_reranker_poc | CED reranker (N=8) | 42 | 48.64 | TBD | 81.88 | — | 0.6156 | standard | **Best practical: 97% recovery** |
26	| plan_004_dreeam_baseline | DREEAM (RoBERTa-large) | 66 | 63.57† | 61.72† | 54.01† | — | — | encoder | †Encoder model, different paradigm |
27	
28	### Key Numbers for Paper
29	
30	- **Evidence generation tax**: Ign-F1 47.36 (no-evidence) → 40.36 (with evidence) = **-7.00pp** cost of faithfulness
31	- **RSFT recovery**: Best RSFT CED (s43) Ign-F1 = 45.85, recovering **5.49pp** of the 7.00pp gap (78.4% recovery)
32	- **CED reranker**: F1=48.64 (only -0.29pp below no-evidence F1=48.93), evi_f1=0.8188 → **recovers 97% of evidence cost with no training**
33	- **RSFT CED 3-seed mean** (s42/s43/s44, original protocol): rel_f1=0.4596±0.0127, evi_f1=0.8143±0.0051
34	- **All 4 RSFT CED configs > SFT baseline**: Δ Ign-F1 = +3.27 to +5.49pp
35	- **DREEAM comparison**: Encoder model gets F1=63.57 / Evi-F1=54.01 — different paradigm (classification vs generation), not directly comparable for RE but sets evidence baseline context
36	- **Joint Evi-F1** (unconditional): SFT baseline 31.17 → best RSFT 37.13 (+5.96pp)
37	
38	### Evidence Gaps
39	
40	- [ ] **CED reranker Ign-F1**: Currently only F1 available (48.64); need Ign-F1 for main table
41	- [ ] **D076 unified protocol reevals** (reeval_ced_s42, reeval_ced_s44): PREPARING — s42 used wrong checkpoint, s44 used wrong seed
42	- [ ] **RSFT CED s45**: eval RUNNING — needed for 4+ seed statistics
43	- [ ] **DREEAM-protocol Evi-F1 alignment** (D041): Not yet done — conditional vs joint Evi-F1 not directly comparable with encoder baselines
44	- [ ] **Test set evaluation** (plan_002): Not started — requires CodaLab submission
45	- [ ] **Post-hoc retrieval baseline** (SFT + BM25 evidence): Not started — RC10
46	
47	---
48	
49	## Claim 2: RL optimization pressure correlates with evidence-extraction decoupling severity
50	
51	**Statement**: Decoupling severity forms a continuous spectrum — GRPO QLoRA (catastrophic) > GRPO bf16 (mild) > DPO (gradual) > RSFT (none). QLoRA is a catastrophic amplifier, not the root cause. Decoupling is an intra-task multi-objective trade-off (not inter-task forgetting).
52	
53	### Supporting Experiments
54	
55	| exp_id | method | seed | F1 (rel_f1) | Evi-F1 | EDCR | Δ vs SFT (F1) | protocol | notes |
56	|--------|--------|------|-------------|--------|------|---------------|----------|-------|
57	| mvp2_eval_sft_baseline | SFT baseline | 42 | 40.57 | 79.79 | 0.7118 | — | unified | Reference point |
58	| mvp2_eval_lr5e6_r1_ckpt100 | GRPO QLoRA (lr=5e-6) | 42 | **1.38** | **85.04** | **0.9876** | **-39.19pp** | original | Catastrophic decoupling |
59	| mvp2_eval_ced_kl001_r4_step100 | GRPO QLoRA (lr=5e-5) | 42 | 21.67 | 57.46 | 0.8539 | -18.90pp | original | Less catastrophic but still severe |
60	| plan_011_bf16_g8_step_eval (step30) | GRPO bf16 G=8 | 42 | 43.40 | 80.63 | 0.6807 | +2.83pp | original | Mild decline from ckpt-100 |
61	| plan_011_bf16_g8_step_eval (step70) | GRPO bf16 G=8 | 42 | 43.41 | 80.99 | 0.6685 | +2.84pp | original | Non-monotonic |
62	| plan_011_grpo_g8_bf16_eval (ckpt100) | GRPO bf16 G=8 | 42 | **45.49** | 80.86 | 0.6318 | **+4.92pp** | original | Best GRPO bf16; **no catastrophic forgetting** |
63	| eval_plan_012_dpo_1ep_fixed_r2 | DPO bf16 1ep | 42 | 40.34 | 80.88 | 0.7139 | -0.23pp | original | Neutral — matches SFT |
64	| plan_012_dpo_ced | DPO bf16 3ep | 42 | **34.29** | **84.03** | **0.7294** | **-6.28pp** | original | Gradual decoupling (overfit) |
65	| mvp2_eval_rsft_s43_r2 | RSFT CED | 43 | 46.83 | 81.56 | 0.6388 | +6.26pp | original | **No decoupling** |
66	
67	### Decoupling Spectrum (for paper figure/table)
68	
69	| Method | Quantization | Optimization Pressure | rel_f1 | Δ rel_f1 | evi_f1 | EDCR | Severity |
70	|--------|-------------|----------------------|--------|----------|--------|------|----------|
71	| GRPO (lr=5e-6) | QLoRA 4-bit | High (100 steps, G=8) | 0.0138 | -0.3919 | 0.8504 | 0.9876 | **Catastrophic** |
72	| GRPO (lr=5e-5) | QLoRA 4-bit | Moderate (100 steps, G=8) | 0.2167 | -0.1890 | 0.5746 | 0.8539 | Severe |
73	| DPO 3ep | bf16 | Moderate (3 epochs) | 0.3429 | -0.0628 | 0.8403 | 0.7294 | **Gradual** |
74	| GRPO G=8 (ckpt30-70) | bf16 | Active (30-70 steps) | ~0.434 | -0.021 | ~0.808 | ~0.68 | **Mild** |
75	| DPO 1ep | bf16 | Low (1 epoch) | 0.4034 | -0.0023 | 0.8088 | 0.7139 | Neutral |
76	| GRPO G=8 (ckpt100) | bf16 | Converged (100 steps) | 0.4549 | +0.0492 | 0.8086 | 0.6318 | None |
77	| RSFT CED (best) | — | Offline (data filter) | 0.4683 | +0.0626 | 0.8156 | 0.6388 | **None** |
78	
79	### Key Numbers for Paper
80	
81	- **QLoRA amplification**: bf16 GRPO rel_f1=0.4549 vs QLoRA GRPO rel_f1=0.0138 — QLoRA turns mild (-2pp early) into catastrophic (-39pp)
82	- **GRPO bf16 trajectory**: ckpt-80→90→100: rel_f1 = 0.4456→0.4523→0.4549 (monotonically improving, no forgetting)
83	- **GRPO bf16 early checkpoints** show mild decline: step30=0.434, step50=0.4276, step70=0.4341 (all below ckpt-100's 0.4549) — confirms transient mild decoupling during training, recovers by convergence
84	- **DPO gradual decay**: 1ep rel_f1=0.4034 → 3ep rel_f1=0.3429 (evi_f1 simultaneously rises 0.8088→0.8403)
85	- **DPO narrative (D067/D068/D069)**: DPO is neutral/gradual, not "failed" — it's a middle data point on the spectrum, confirming decoupling is universal across RL methods
86	- **Intra-task vs inter-task** (D069): This is NOT catastrophic forgetting of pretrained knowledge; it's competition between RE and evidence objectives within the same task
87	
88	### Evidence Gaps
89	
90	- [ ] **GRPO bf16 Ign-F1**: Currently reporting F1; paper_framing notes Ign-F1=45.59 > F1=~43.4 "因 train triples 过滤效应" — this inversion needs explanation in paper
91	- [ ] **DPO 3ep Ign-F1**: TBD in paper_framing table
92	- [ ] **GRPO QLoRA (lr=5e-6) Ign-F1**: TBD
93	- [ ] **Connecting to reward overoptimization literature** (RC9): Need explicit Gao et al. 2023 citation
94	- [ ] **QuRL/QaRL literature** (D076 framing note): Supports QLoRA amplification narrative but not yet in Related Work
95	
96	---
97	
98	## Claim 3: NLI-based scoring improves RSFT quality (CED vs flat-NLI ablation)
99	
100	**Statement**: Both CED and flat-NLI outperform random/no scoring. CED vs flat-NLI difference is statistically uncertain — CED may be "one possible scoring function" rather than strictly superior.
101	
102	### Supporting Experiments
103	
104	#### CED RSFT (top_k=1)
105	
106	| exp_id | seed | F1 (rel_f1) | Ign-F1 | Evi-F1 | EDCR | D076 unified? | notes |
107	|--------|------|-------------|--------|--------|------|---------------|-------|
108	| mvp2_eval_rsft_r1 | 42 (3ep) | 44.49 | 43.63 | 81.87 | 0.6565 | No | 3-epoch run |
109	| mvp2_eval_rsft_r2a | 42 (1ep) | 44.94 | 44.01 | 81.08 | 0.6641 | No | 1ep, α=128 |
110	| mvp2_eval_rsft_r2b | 42 (1ep) | 44.93 | 44.10 | 81.28 | 0.6609 | No | 1ep, α=32 |
111	| mvp2_eval_rsft_s43_r2 | 43 | 46.83 | 45.85 | 81.56 | 0.6388 | No | Best seed |
112	| mvp2_rsft_train_r1_s44 | 44 | 46.55 | 45.51 | 80.87 | 0.6350 | No | |
113	| eval_rsft_ced_s45 | 45 | — | — | — | — | — | **RUNNING** |
114	| reeval_ced_s42 | 42 | — | — | — | — | Yes | **PREPARING** (fixes wrong ckpt) |
115	| reeval_ced_s44 | 44 | — | — | — | — | Yes | **PREPARING** (fixes wrong seed) |
116	
117	**CED 3-seed mean (s42-r1/s43/s44)**: rel_f1 = 0.4596 ± 0.0127, evi_f1 = 0.8143 ± 0.0051
118	
119	#### flat-NLI RSFT (top_k=1)
120	
121	| exp_id | seed | F1 (rel_f1) | Ign-F1 | Evi-F1 | EDCR | D076 unified? | notes |
122	|--------|------|-------------|--------|--------|------|---------------|-------|
123	| eval_plan_001_flat_nli | 42 | 45.39 | 44.49 | 80.43 | 0.6431 | No | |
124	| reeval_flat_nli_s43 | 43 | 45.23 | TBD | 81.58 | 0.6505 | Partial (fixed adapter, batch=16) | |
125	| eval_flat_nli_s44 | 44 | 46.15 | 46.15 | 81.31 | 0.6458 | No | |
126	| eval_flat_nli_seed45 | 45 | 45.51 | 45.51 | 81.54 | 0.6521 | No | |
127	| reeval_flat_nli_s42 | 42 | — | — | — | — | Yes | **PREPARING** |
128	| reeval_flat_nli_s43_r2 | 43 | — | — | — | — | Yes | **RUNNING** |
129	
130	**flat-NLI 4-seed mean (s42/s43/s44/s45)**: rel_f1 = 0.4557 ± 0.0039
131	
132	#### top_k Ablation
133	
134	| exp_id | method | seed | F1 (rel_f1) | Ign-F1 | Evi-F1 | EDCR | notes |
135	|--------|--------|------|-------------|--------|--------|------|-------|
136	| CED 3-seed mean | CED k=1 | s42/43/44 | 45.96 | 45.00 | 81.43 | 0.6434 | |
137	| reeval_rsft_topk3 | CED k=3 | 42 | 44.54 | 43.64 | 80.88 | 0.6635 | D076 corrected ign_f1 |
138	
139	**Δ (k=3 vs k=1 mean)**: Ign-F1 **-1.36pp**, rel_f1 **-1.42pp**, evi_f1 **-0.55pp**, EDCR +0.02
140	- Training data: k=1 → 2718 samples (12.4%), k=3 → 8037 samples (37%) — 2.96× more data but lower quality
141	- Scoring quality: k=1 mean_f1=0.6157, mean_ced=0.6683 → k=3 mean_f1=0.5761, mean_ced=0.6205
142	
143	### Key Numbers for Paper
144	
145	- **CED vs flat-NLI head-to-head** (current data, NOT D076-unified):
146	  - CED 3-seed mean rel_f1 = 0.4596 vs flat-NLI 4-seed mean = 0.4557 → Δ = **+0.39pp** (not significant)
147	  - Dream reported p-values: 0.08 / 0.38 / 0.12 — not statistically significant
148	- **Both > SFT baseline**: CED +5.39pp, flat-NLI +5.00pp (Ign-F1 vs SFT 40.36)
149	- **top_k=1 > top_k=3**: Scoring precision matters more than data quantity; rank 2-3 samples dilute quality
150	- **Status**: CED ≈ flat-NLI statistically indistinguishable → CED is "one possible scoring function," not independently superior (C3 降级)
151	
152	### Evidence Gaps
153	
154	- [ ] **D076 unified protocol**: 4/8 evals need rerunning before paired t-test is valid (reeval_ced_s42, reeval_ced_s44, reeval_flat_nli_s42, reeval_flat_nli_s43_r2)
155	- [ ] **CED s45 eval**: Still RUNNING — needed for 4-seed CED statistics
156	- [ ] **Paired t-test**: Cannot compute until all seeds are under unified protocol
157	- [ ] **top_k=3 additional seeds**: Only 1 seed; direction consistent but no significance test possible — present as supplementary ablation row, not independent claim
158	
159	---
160	
161	## Claim 4: EDCR dual-layer diagnostic value
162	
163	**Statement**: EDCR quantifies evidence-extraction decoupling at method level (echoing Claim 2 spectrum) and provides relation-type diagnostic information orthogonal to Evi-F1 at per-relation level.
164	
165	### Supporting Experiments
166	
167	| exp_id | analysis | result | notes |
168	|--------|----------|--------|-------|
169	| plan_003_edcr_diagnostic | Method-level EDCR table (15 methods) | EDCR vs rel_f1 Spearman ρ=-0.9648 (p=0.0001); EDCR vs evi_f1 ρ=0.0022 (p=0.9941) | EDCR ≈ transform of rel_f1 at method level (D071 flags by-construction concern) |
170	| D070 per-relation analysis | Per-relation EDCR (93 types, ≥5 samples) | EDCR vs evi_f1 ρ=**-0.064** (p=0.58) → **completely independent**; EDCR vs rel_f1 ρ=-0.793 (p<0.001) | 76 types with non-zero data |
171	| D070 per-relation analysis | Per-relation evi_f1 vs rel_f1 | ρ=-0.013 (p=0.91) → evidence quality and extraction completely decoupled across relation types | Independent finding supporting paper narrative |
172	
173	### EDCR Method-Level Summary
174	
175	| Method | EDCR | rel_f1 | evi_f1 | interpretation |
176	|--------|------|--------|--------|----------------|
177	| GRPO QLoRA (lr=5e-6) | 0.9876 | 0.0138 | 0.8504 | Pathological: high evidence, zero extraction |
178	| GRPO QLoRA (lr=5e-5) | 0.8539 | 0.2167 | 0.5746 | Severe decoupling |
179	| DPO 3ep | 0.7294 | 0.3429 | 0.8403 | Moderate decoupling |
180	| SFT baseline | 0.7118 | 0.4057 | 0.7979 | Reference |
181	| DPO 1ep | 0.7139 | 0.4034 | 0.8088 | ≈ SFT level |
182	| RSFT r2a (1ep) | 0.6641 | 0.4494 | 0.8108 | Improved |
183	| RSFT CED k=3 | 0.6635 | 0.4454 | 0.8088 | Improved |
184	| RSFT r2b (1ep) | 0.6609 | 0.4493 | 0.8128 | Improved |
185	| RSFT CED s42 (3ep) | 0.6565 | 0.4449 | 0.8187 | Improved |
186	| flat-NLI s43 | 0.6505 | 0.4523 | 0.8158 | Improved |
187	| flat-NLI s44 | 0.6458 | 0.4615 | 0.8131 | Improved |
188	| flat-NLI s42 | 0.6431 | 0.4539 | 0.8043 | Improved |
189	| RSFT CED s43 | 0.6388 | 0.4683 | 0.8156 | Best RSFT |
190	| RSFT CED s44 | 0.6350 | 0.4655 | 0.8087 | Near best |
191	| GRPO bf16 G=8 | 0.6318 | 0.4549 | 0.8086 | Best GRPO (no decoupling) |
192	| CED reranker | 0.6156 | 0.4864 | 0.8188 | **Best overall** |
193	
194	### Per-Relation Exemplars (D070)
195	
196	| Relation Type | EDCR | evi_f1 | rel_f1 | interpretation |
197	|---------------|------|--------|--------|----------------|
198	| date_of_birth | 0.118 | high | high | High faithfulness — easy relation |
199	| head_of_government | 0.956 | 0.875 | low | High evidence quality but poor extraction — EDCR catches what evi_f1 misses |
200	
201	### Key Numbers for Paper
202	
203	- **Layer 1 (method-level)**: EDCR identifies pathological models (GRPO QLoRA: EDCR≈1.0) — works as decoupling meter, echoes Claim 2
204	- **Layer 2 (per-relation)**: EDCR vs evi_f1 ρ=-0.064 → completely independent signals at per-relation granularity
205	- **D071 caveat**: Method-level EDCR ≈ f(1/rel_f1) by construction — when model predicts wrong relations, evidence automatically becomes "distractor." Paper must acknowledge this and frame method-level EDCR as decoupling measure, not independent evidence quality metric
206	- **D073 definition**: Paper uses distractor count ratio (∈[0,1]) definition; formula proxy 1-rel_f1/evi_f1 only for method-level quick comparison; per-relation tables require n_pred≥10 filter
207	
208	### Evidence Gaps
209	
210	- [ ] **100-example human annotation validation** (plan_013): Not started — needed for RC6
211	- [ ] **TP-only EDCR** (D071): Not implemented — needed to address by-construction confound; if TP-only EDCR still correlates with rel_f1, Claim 4 method-level value is weak
212	- [ ] **More per-relation exemplars**: Need to populate full table with n_pred≥10 filter (D073)
213	
214	---
215	
216	## Cross-Claim Protocol Issues
217	
218	### D076 Unified Protocol Reeval Status
219	
220	The following evals have protocol inconsistencies that prevent valid paired t-test (Claim 3):
221	
222	| exp_id | issue | unified reeval | status |
223	|--------|-------|---------------|--------|
224	| CED s42 (mvp2_eval_rsft_r2b_maxtok1536_r2) | Wrong checkpoint (r2b α=32 instead of ckpt-510 α=128), batch_size=8, max_new_tokens=1536 | reeval_ced_s42 | PREPARING |
225	| CED s44 (mvp2_rsft_train_r1_s44) | Seed=42 in eval (should be 44) | reeval_ced_s44 | PREPARING |
226	| flat-NLI s42 (eval_plan_001_flat_nli) | batch_size=16 | reeval_flat_nli_s42 | PREPARING |
227	| flat-NLI s43 (reeval_flat_nli_s43) | batch_size=16 | reeval_flat_nli_s43_r2 | RUNNING |
228	
229	**Unified protocol**: batch_size=4, --no-quantize, --sft_adapter, max_new_tokens=1024, correct seed.
230	
231	**Impact**: Old protocol data can be used for directional claims but NOT for paired t-test (Claim 3 significance). All 8 CED/flat-NLI evals must be under unified protocol before statistical comparison.
232	
233	### Ign-F1 vs F1 Issue
234	
235	- Most registry entries show ign_f1 = rel_f1 (suspected eval pipeline bug, D069)
236	- Paper_framing table has corrected Ign-F1 values that differ from F1 (e.g., SFT no-evidence: Ign-F1=47.36 vs F1=48.93)
237	- D071: "Ign-F1 修正后排名无实质变化"
238	- **Paper uses Ign-F1 in main table** per D071
239	
240	### Experiments Still Running / Pending
241	
242	| exp_id | purpose | status | blocking |
243	|--------|---------|--------|----------|
244	| eval_rsft_ced_s43 | CED s43 re-eval | RUNNING | C3 statistics |
245	| eval_rsft_ced_s45 | CED s45 (new seed) | RUNNING | C3 statistics |
246	| eval_plan_014_no_evidence_r2 | SFT no-evidence re-eval | RUNNING | — |
247	| reeval_ced_s42 | Unified protocol CED s42 | PREPARING | C3 paired t-test |
248	| reeval_ced_s44 | Unified protocol CED s44 | PREPARING | C3 paired t-test |
249	| reeval_flat_nli_s42 | Unified protocol flat-NLI s42 | PREPARING | C3 paired t-test |
250	| reeval_flat_nli_s43_r2 | Unified protocol flat-NLI s43 | RUNNING | C3 paired t-test |
251	| plan_002 | Test set evaluation | PLANNED | C1 final numbers |
252	| plan_013 | EDCR human annotation (100 examples) | PLANNED | C4 validation |
253	
254	---
255	
256	## Summary: Paper-Ready vs Gaps
257	
258	### Paper-Ready Numbers
259	
260	1. **Evidence tax**: 47.36 → 40.36 = -7.00pp Ign-F1 (plan_014 vs noquant SFT)
261	2. **CED reranker recovery**: F1=48.64, only -0.29pp below no-evidence (plan_005)
262	3. **RSFT CED best**: Ign-F1=45.85, +5.49pp over SFT (s43)
263	4. **Decoupling spectrum**: Complete data for GRPO QLoRA / GRPO bf16 / DPO / RSFT
264	5. **QLoRA amplification**: bf16 0.4549 vs QLoRA 0.0138 (plan_011 vs QLoRA runs)
265	6. **EDCR per-relation independence**: ρ=-0.064 vs evi_f1 (D070)
266	7. **top_k ablation**: k=1 > k=3, precision > quantity (plan_008)
267	8. **DREEAM baseline**: F1=63.57, Evi-F1=54.01 reproduced (plan_004)
268	
269	### Critical Gaps (blocking paper submission)
270	
271	1. **D076 unified reevals** — blocking Claim 3 statistical test
272	2. **CED reranker Ign-F1** — needed for main table
273	3. **Test set evaluation** (plan_002) — no official numbers yet
274	4. **DREEAM-protocol Evi-F1 alignment** — cross-paradigm evidence comparison
275	
276	### Nice-to-Have (strengthen but not blocking)
277	
278	1. EDCR human validation (plan_013) — RC6
279	2. Post-hoc retrieval baseline (SFT + BM25) — RC10
280	3. Model size ablation (plan_006) — RC4
281	4. TP-only EDCR (D071) — method-level confound
282	5. Re-DocRED extension (plan_007) — RC4
283	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "0b4cc0a8-8ca9-45f6-95d7-4bd32353a2a0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/paper_evidence_table.md",
      "content": "# Paper Evidence Table — FREIGE (EMNLP 2026)\n\n> **Compiled**: 2026-05-16\n> **Source**: experiment registry + paper_framing.md + decisions D067-D076\n> **Convention**: Ign-F1/F1 as percentage (e.g., 40.36); rel_f1/evi_f1 as decimal (e.g., 0.4036) when directly from registry. Paper reports Ign-F1 in main table, F1 in appendix (D071).\n\n---\n\n## Claim 1: Evidence-grounded DocRE is a viable new capability\n\n**Statement**: FREIGE is the first LLM method to simultaneously output (head, relation, tail, [evidence]) on DocRED. Evidence generation has a ~7pp Ign-F1 cost; RSFT recovers most of it; CED reranker recovers 97%.\n\n### Supporting Experiments\n\n| exp_id | method | seed | F1 (rel_f1) | Ign-F1 | Evi-F1 | Evi-F1 (joint) | EDCR | protocol | notes |\n|--------|--------|------|-------------|--------|--------|----------------|------|----------|-------|\n| eval_plan_014_sft_no_evidence | SFT no-evidence | 42 | 48.93 | 47.36 | — | — | — | standard | Upper bound: no evidence burden |\n| eval_sft_baseline_noquant | SFT baseline (noquant) | 42 | 41.06 | 40.36 | 80.13 | 32.16 | 0.7039 | standard | Primary SFT baseline for paper |\n| mvp2_eval_sft_baseline | SFT baseline (quantized) | 42 | 40.57 | 40.57 | 79.79 | 31.17 | 0.7118 | unified (r3) | Quantized; -0.49pp vs noquant |\n| mvp2_eval_rsft_s43_r2 | RSFT CED k=1 | 43 | 46.83 | 45.85 | 81.56 | 37.11 | 0.6388 | original | **Best RSFT seed** |\n| mvp2_rsft_train_r1_s44 | RSFT CED k=1 | 44 | 46.55 | 45.51 | 80.87 | 37.13 | 0.6350 | original | |\n| mvp2_eval_rsft_r1 | RSFT CED k=1 (3ep) | 42 | 44.49 | 43.63 | 81.87 | 34.68 | 0.6565 | original | 3-epoch; s42 |\n| mvp2_eval_rsft_r2a | RSFT CED k=1 (1ep) | 42 | 44.94 | 44.01 | 81.08 | 35.09 | 0.6641 | original | 1-epoch ablation α=128 |\n| mvp2_eval_rsft_r2b | RSFT CED k=1 (1ep) | 42 | 44.93 | 44.10 | 81.28 | 34.90 | 0.6609 | original | 1-epoch ablation α=32 |\n| mvp2_ced_reranker_poc | CED reranker (N=8) | 42 | 48.64 | TBD | 81.88 | — | 0.6156 | standard | **Best practical: 97% recovery** |\n| plan_004_dreeam_baseline | DREEAM (RoBERTa-large) | 66 | 63.57† | 61.72† | 54.01† | — | — | encoder | †Encoder model, different paradigm |\n\n### Key Numbers for Paper\n\n- **Evidence generation tax**: Ign-F1 47.36 (no-evidence) → 40.36 (with evidence) = **-7.00pp** cost of faithfulness\n- **RSFT recovery**: Best RSFT CED (s43) Ign-F1 = 45.85, recovering **5.49pp** of the 7.00pp gap (78.4% recovery)\n- **CED reranker**: F1=48.64 (only -0.29pp below no-evidence F1=48.93), evi_f1=0.8188 → **recovers 97% of evidence cost with no training**\n- **RSFT CED 3-seed mean** (s42/s43/s44, original protocol): rel_f1=0.4596±0.0127, evi_f1=0.8143±0.0051\n- **All 4 RSFT CED configs > SFT baseline**: Δ Ign-F1 = +3.27 to +5.49pp\n- **DREEAM comparison**: Encoder model gets F1=63.57 / Evi-F1=54.01 — different paradigm (classification vs generation), not directly comparable for RE but sets evidence baseline context\n- **Joint Evi-F1** (unconditional): SFT baseline 31.17 → best RSFT 37.13 (+5.96pp)\n\n### Evidence Gaps\n\n- [ ] **CED reranker Ign-F1**: Currently only F1 available (48.64); need Ign-F1 for main table\n- [ ] **D076 unified protocol reevals** (reeval_ced_s42, reeval_ced_s44): PREPARING — s42 used wrong checkpoint, s44 used wrong seed\n- [ ] **RSFT CED s45**: eval RUNNING — needed for 4+ seed statistics\n- [ ] **DREEAM-protocol Evi-F1 alignment** (D041): Not yet done — conditional vs joint Evi-F1 not directly comparable with encoder baselines\n- [ ] **Test set evaluation** (plan_002): Not started — requires CodaLab submission\n- [ ] **Post-hoc retrieval baseline** (SFT + BM25 evidence): Not started — RC10\n\n---\n\n## Claim 2: RL optimization pressure correlates with evidence-extraction decoupling severity\n\n**Statement**: Decoupling severity forms a continuous spectrum — GRPO QLoRA (catastrophic) > GRPO bf16 (mild) > DPO (gradual) > RSFT (none). QLoRA is a catastrophic amplifier, not the root cause. Decoupling is an intra-task multi-objective trade-off (not inter-task forgetting).\n\n### Supporting Experiments\n\n| exp_id | method | seed | F1 (rel_f1) | Evi-F1 | EDCR | Δ vs SFT (F1) | protocol | notes |\n|--------|--------|------|-------------|--------|------|---------------|----------|-------|\n| mvp2_eval_sft_baseline | SFT baseline | 42 | 40.57 | 79.79 | 0.7118 | — | unified | Reference point |\n| mvp2_eval_lr5e6_r1_ckpt100 | GRPO QLoRA (lr=5e-6) | 42 | **1.38** | **85.04** | **0.9876** | **-39.19pp** | original | Catastrophic decoupling |\n| mvp2_eval_ced_kl001_r4_step100 | GRPO QLoRA (lr=5e-5) | 42 | 21.67 | 57.46 | 0.8539 | -18.90pp | original | Less catastrophic but still severe |\n| plan_011_bf16_g8_step_eval (step30) | GRPO bf16 G=8 | 42 | 43.40 | 80.63 | 0.6807 | +2.83pp | original | Mild decline from ckpt-100 |\n| plan_011_bf16_g8_step_eval (step70) | GRPO bf16 G=8 | 42 | 43.41 | 80.99 | 0.6685 | +2.84pp | original | Non-monotonic |\n| plan_011_grpo_g8_bf16_eval (ckpt100) | GRPO bf16 G=8 | 42 | **45.49** | 80.86 | 0.6318 | **+4.92pp** | original | Best GRPO bf16; **no catastrophic forgetting** |\n| eval_plan_012_dpo_1ep_fixed_r2 | DPO bf16 1ep | 42 | 40.34 | 80.88 | 0.7139 | -0.23pp | original | Neutral — matches SFT |\n| plan_012_dpo_ced | DPO bf16 3ep | 42 | **34.29** | **84.03** | **0.7294** | **-6.28pp** | original | Gradual decoupling (overfit) |\n| mvp2_eval_rsft_s43_r2 | RSFT CED | 43 | 46.83 | 81.56 | 0.6388 | +6.26pp | original | **No decoupling** |\n\n### Decoupling Spectrum (for paper figure/table)\n\n| Method | Quantization | Optimization Pressure | rel_f1 | Δ rel_f1 | evi_f1 | EDCR | Severity |\n|--------|-------------|----------------------|--------|----------|--------|------|----------|\n| GRPO (lr=5e-6) | QLoRA 4-bit | High (100 steps, G=8) | 0.0138 | -0.3919 | 0.8504 | 0.9876 | **Catastrophic** |\n| GRPO (lr=5e-5) | QLoRA 4-bit | Moderate (100 steps, G=8) | 0.2167 | -0.1890 | 0.5746 | 0.8539 | Severe |\n| DPO 3ep | bf16 | Moderate (3 epochs) | 0.3429 | -0.0628 | 0.8403 | 0.7294 | **Gradual** |\n| GRPO G=8 (ckpt30-70) | bf16 | Active (30-70 steps) | ~0.434 | -0.021 | ~0.808 | ~0.68 | **Mild** |\n| DPO 1ep | bf16 | Low (1 epoch) | 0.4034 | -0.0023 | 0.8088 | 0.7139 | Neutral |\n| GRPO G=8 (ckpt100) | bf16 | Converged (100 steps) | 0.4549 | +0.0492 | 0.8086 | 0.6318 | None |\n| RSFT CED (best) | — | Offline (data filter) | 0.4683 | +0.0626 | 0.8156 | 0.6388 | **None** |\n\n### Key Numbers for Paper\n\n- **QLoRA amplification**: bf16 GRPO rel_f1=0.4549 vs QLoRA GRPO rel_f1=0.0138 — QLoRA turns mild (-2pp early) into catastrophic (-39pp)\n- **GRPO bf16 trajectory**: ckpt-80→90→100: rel_f1 = 0.4456→0.4523→0.4549 (monotonically improving, no forgetting)\n- **GRPO bf16 early checkpoints** show mild decline: step30=0.434, step50=0.4276, step70=0.4341 (all below ckpt-100's 0.4549) — confirms transient mild decoupling during training, recovers by convergence\n- **DPO gradual decay**: 1ep rel_f1=0.4034 → 3ep rel_f1=0.3429 (evi_f1 simultaneously rises 0.8088→0.8403)\n- **DPO narrative (D067/D068/D069)**: DPO is neutral/gradual, not \"failed\" — it's a middle data point on the spectrum, confirming decoupling is universal across RL methods\n- **Intra-task vs inter-task** (D069): This is NOT catastrophic forgetting of pretrained knowledge; it's competition between RE and evidence objectives within the same task\n\n### Evidence Gaps\n\n- [ ] **GRPO bf16 Ign-F1**: Currently reporting F1; paper_framing notes Ign-F1=45.59 > F1=~43.4 \"因 train triples 过滤效应\" — this inversion needs explanation in paper\n- [ ] **DPO 3ep Ign-F1**: TBD in paper_framing table\n- [ ] **GRPO QLoRA (lr=5e-6) Ign-F1**: TBD\n- [ ] **Connecting to reward overoptimization literature** (RC9): Need explicit Gao et al. 2023 citation\n- [ ] **QuRL/QaRL literature** (D076 framing note): Supports QLoRA amplification narrative but not yet in Related Work\n\n---\n\n## Claim 3: NLI-based scoring improves RSFT quality (CED vs flat-NLI ablation)\n\n**Statement**: Both CED and flat-NLI outperform random/no scoring. CED vs flat-NLI difference is statistically uncertain — CED may be \"one possible scoring function\" rather than strictly superior.\n\n### Supporting Experiments\n\n#### CED RSFT (top_k=1)\n\n| exp_id | seed | F1 (rel_f1) | Ign-F1 | Evi-F1 | EDCR | D076 unified? | notes |\n|--------|------|-------------|--------|--------|------|---------------|-------|\n| mvp2_eval_rsft_r1 | 42 (3ep) | 44.49 | 43.63 | 81.87 | 0.6565 | No | 3-epoch run |\n| mvp2_eval_rsft_r2a | 42 (1ep) | 44.94 | 44.01 | 81.08 | 0.6641 | No | 1ep, α=128 |\n| mvp2_eval_rsft_r2b | 42 (1ep) | 44.93 | 44.10 | 81.28 | 0.6609 | No | 1ep, α=32 |\n| mvp2_eval_rsft_s43_r2 | 43 | 46.83 | 45.85 | 81.56 | 0.6388 | No | Best seed |\n| mvp2_rsft_train_r1_s44 | 44 | 46.55 | 45.51 | 80.87 | 0.6350 | No | |\n| eval_rsft_ced_s45 | 45 | — | — | — | — | — | **RUNNING** |\n| reeval_ced_s42 | 42 | — | — | — | — | Yes | **PREPARING** (fixes wrong ckpt) |\n| reeval_ced_s44 | 44 | — | — | — | — | Yes | **PREPARING** (fixes wrong seed) |\n\n**CED 3-seed mean (s42-r1/s43/s44)**: rel_f1 = 0.4596 ± 0.0127, evi_f1 = 0.8143 ± 0.0051\n\n#### flat-NLI RSFT (top_k=1)\n\n| exp_id | seed | F1 (rel_f1) | Ign-F1 | Evi-F1 | EDCR | D076 unified? | notes |\n|--------|------|-------------|--------|--------|------|---------------|-------|\n| eval_plan_001_flat_nli | 42 | 45.39 | 44.49 | 80.43 | 0.6431 | No | |\n| reeval_flat_nli_s43 | 43 | 45.23 | TBD | 81.58 | 0.6505 | Partial (fixed adapter, batch=16) | |\n| eval_flat_nli_s44 | 44 | 46.15 | 46.15 | 81.31 | 0.6458 | No | |\n| eval_flat_nli_seed45 | 45 | 45.51 | 45.51 | 81.54 | 0.6521 | No | |\n| reeval_flat_nli_s42 | 42 | — | — | — | — | Yes | **PREPARING** |\n| reeval_flat_nli_s43_r2 | 43 | — | — | — | — | Yes | **RUNNING** |\n\n**flat-NLI 4-seed mean (s42/s43/s44/s45)**: rel_f1 = 0.4557 ± 0.0039\n\n#### top_k Ablation\n\n| exp_id | method | seed | F1 (rel_f1) | Ign-F1 | Evi-F1 | EDCR | notes |\n|--------|--------|------|-------------|--------|--------|------|-------|\n| CED 3-seed mean | CED k=1 | s42/43/44 | 45.96 | 45.00 | 81.43 | 0.6434 | |\n| reeval_rsft_topk3 | CED k=3 | 42 | 44.54 | 43.64 | 80.88 | 0.6635 | D076 corrected ign_f1 |\n\n**Δ (k=3 vs k=1 mean)**: Ign-F1 **-1.36pp**, rel_f1 **-1.42pp**, evi_f1 **-0.55pp**, EDCR +0.02\n- Training data: k=1 → 2718 samples (12.4%), k=3 → 8037 samples (37%) — 2.96× more data but lower quality\n- Scoring quality: k=1 mean_f1=0.6157, mean_ced=0.6683 → k=3 mean_f1=0.5761, mean_ced=0.6205\n\n### Key Numbers for Paper\n\n- **CED vs flat-NLI head-to-head** (current data, NOT D076-unified):\n  - CED 3-seed mean rel_f1 = 0.4596 vs flat-NLI 4-seed mean = 0.4557 → Δ = **+0.39pp** (not significant)\n  - Dream reported p-values: 0.08 / 0.38 / 0.12 — not statistically significant\n- **Both > SFT baseline**: CED +5.39pp, flat-NLI +5.00pp (Ign-F1 vs SFT 40.36)\n- **top_k=1 > top_k=3**: Scoring precision matters more than data quantity; rank 2-3 samples dilute quality\n- **Status**: CED ≈ flat-NLI statistically indistinguishable → CED is \"one possible scoring function,\" not independently superior (C3 降级)\n\n### Evidence Gaps\n\n- [ ] **D076 unified protocol**: 4/8 evals need rerunning before paired t-test is valid (reeval_ced_s42, reeval_ced_s44, reeval_flat_nli_s42, reeval_flat_nli_s43_r2)\n- [ ] **CED s45 eval**: Still RUNNING — needed for 4-seed CED statistics\n- [ ] **Paired t-test**: Cannot compute until all seeds are under unified protocol\n- [ ] **top_k=3 additional seeds**: Only 1 seed; direction consistent but no significance test possible — present as supplementary ablation row, not independent claim\n\n---\n\n## Claim 4: EDCR dual-layer diagnostic value\n\n**Statement**: EDCR quantifies evidence-extraction decoupling at method level (echoing Claim 2 spectrum) and provides relation-type diagnostic information orthogonal to Evi-F1 at per-relation level.\n\n### Supporting Experiments\n\n| exp_id | analysis | result | notes |\n|--------|----------|--------|-------|\n| plan_003_edcr_diagnostic | Method-level EDCR table (15 methods) | EDCR vs rel_f1 Spearman ρ=-0.9648 (p=0.0001); EDCR vs evi_f1 ρ=0.0022 (p=0.9941) | EDCR ≈ transform of rel_f1 at method level (D071 flags by-construction concern) |\n| D070 per-relation analysis | Per-relation EDCR (93 types, ≥5 samples) | EDCR vs evi_f1 ρ=**-0.064** (p=0.58) → **completely independent**; EDCR vs rel_f1 ρ=-0.793 (p<0.001) | 76 types with non-zero data |\n| D070 per-relation analysis | Per-relation evi_f1 vs rel_f1 | ρ=-0.013 (p=0.91) → evidence quality and extraction completely decoupled across relation types | Independent finding supporting paper narrative |\n\n### EDCR Method-Level Summary\n\n| Method | EDCR | rel_f1 | evi_f1 | interpretation |\n|--------|------|--------|--------|----------------|\n| GRPO QLoRA (lr=5e-6) | 0.9876 | 0.0138 | 0.8504 | Pathological: high evidence, zero extraction |\n| GRPO QLoRA (lr=5e-5) | 0.8539 | 0.2167 | 0.5746 | Severe decoupling |\n| DPO 3ep | 0.7294 | 0.3429 | 0.8403 | Moderate decoupling |\n| SFT baseline | 0.7118 | 0.4057 | 0.7979 | Reference |\n| DPO 1ep | 0.7139 | 0.4034 | 0.8088 | ≈ SFT level |\n| RSFT r2a (1ep) | 0.6641 | 0.4494 | 0.8108 | Improved |\n| RSFT CED k=3 | 0.6635 | 0.4454 | 0.8088 | Improved |\n| RSFT r2b (1ep) | 0.6609 | 0.4493 | 0.8128 | Improved |\n| RSFT CED s42 (3ep) | 0.6565 | 0.4449 | 0.8187 | Improved |\n| flat-NLI s43 | 0.6505 | 0.4523 | 0.8158 | Improved |\n| flat-NLI s44 | 0.6458 | 0.4615 | 0.8131 | Improved |\n| flat-NLI s42 | 0.6431 | 0.4539 | 0.8043 | Improved |\n| RSFT CED s43 | 0.6388 | 0.4683 | 0.8156 | Best RSFT |\n| RSFT CED s44 | 0.6350 | 0.4655 | 0.8087 | Near best |\n| GRPO bf16 G=8 | 0.6318 | 0.4549 | 0.8086 | Best GRPO (no decoupling) |\n| CED reranker | 0.6156 | 0.4864 | 0.8188 | **Best overall** |\n\n### Per-Relation Exemplars (D070)\n\n| Relation Type | EDCR | evi_f1 | rel_f1 | interpretation |\n|---------------|------|--------|--------|----------------|\n| date_of_birth | 0.118 | high | high | High faithfulness — easy relation |\n| head_of_government | 0.956 | 0.875 | low | High evidence quality but poor extraction — EDCR catches what evi_f1 misses |\n\n### Key Numbers for Paper\n\n- **Layer 1 (method-level)**: EDCR identifies pathological models (GRPO QLoRA: EDCR≈1.0) — works as decoupling meter, echoes Claim 2\n- **Layer 2 (per-relation)**: EDCR vs evi_f1 ρ=-0.064 → completely independent signals at per-relation granularity\n- **D071 caveat**: Method-level EDCR ≈ f(1/rel_f1) by construction — when model predicts wrong relations, evidence automatically becomes \"distractor.\" Paper must acknowledge this and frame method-level EDCR as decoupling measure, not independent evidence quality metric\n- **D073 definition**: Paper uses distractor count ratio (∈[0,1]) definition; formula proxy 1-rel_f1/evi_f1 only for method-level quick comparison; per-relation tables require n_pred≥10 filter\n\n### Evidence Gaps\n\n- [ ] **100-example human annotation validation** (plan_013): Not started — needed for RC6\n- [ ] **TP-only EDCR** (D071): Not implemented — needed to address by-construction confound; if TP-only EDCR still correlates with rel_f1, Claim 4 method-level value is weak\n- [ ] **More per-relation exemplars**: Need to populate full table with n_pred≥10 filter (D073)\n\n---\n\n## Cross-Claim Protocol Issues\n\n### D076 Unified Protocol Reeval Status\n\nThe following evals have protocol inconsistencies that prevent valid paired t-test (Claim 3):\n\n| exp_id | issue | unified reeval | status |\n|--------|-------|---------------|--------|\n| CED s42 (mvp2_eval_rsft_r2b_maxtok1536_r2) | Wrong checkpoint (r2b α=32 instead of ckpt-510 α=128), batch_size=8, max_new_tokens=1536 | reeval_ced_s42 | PREPARING |\n| CED s44 (mvp2_rsft_train_r1_s44) | Seed=42 in eval (should be 44) | reeval_ced_s44 | PREPARING |\n| flat-NLI s42 (eval_plan_001_flat_nli) | batch_size=16 | reeval_flat_nli_s42 | PREPARING |\n| flat-NLI s43 (reeval_flat_nli_s43) | batch_size=16 | reeval_flat_nli_s43_r2 | RUNNING |\n\n**Unified protocol**: batch_size=4, --no-quantize, --sft_adapter, max_new_tokens=1024, correct seed.\n\n**Impact**: Old protocol data can be used for directional claims but NOT for paired t-test (Claim 3 significance). All 8 CED/flat-NLI evals must be under unified protocol before statistical comparison.\n\n### Ign-F1 vs F1 Issue\n\n- Most registry entries show ign_f1 = rel_f1 (suspected eval pipeline bug, D069)\n- Paper_framing table has corrected Ign-F1 values that differ from F1 (e.g., SFT no-evidence: Ign-F1=47.36 vs F1=48.93)\n- D071: \"Ign-F1 修正后排名无实质变化\"\n- **Paper uses Ign-F1 in main table** per D071\n\n### Experiments Still Running / Pending\n\n| exp_id | purpose | status | blocking |\n|--------|---------|--------|----------|\n| eval_rsft_ced_s43 | CED s43 re-eval | RUNNING | C3 statistics |\n| eval_rsft_ced_s45 | CED s45 (new seed) | RUNNING | C3 statistics |\n| eval_plan_014_no_evidence_r2 | SFT no-evidence re-eval | RUNNING | — |\n| reeval_ced_s42 | Unified protocol CED s42 | PREPARING | C3 paired t-test |\n| reeval_ced_s44 | Unified protocol CED s44 | PREPARING | C3 paired t-test |\n| reeval_flat_nli_s42 | Unified protocol flat-NLI s42 | PREPARING | C3 paired t-test |\n| reeval_flat_nli_s43_r2 | Unified protocol flat-NLI s43 | RUNNING | C3 paired t-test |\n| plan_002 | Test set evaluation | PLANNED | C1 final numbers |\n| plan_013 | EDCR human annotation (100 examples) | PLANNED | C4 validation |\n\n---\n\n## Summary: Paper-Ready vs Gaps\n\n### Paper-Ready Numbers\n\n1. **Evidence tax**: 47.36 → 40.36 = -7.00pp Ign-F1 (plan_014 vs noquant SFT)\n2. **CED reranker recovery**: F1=48.64, only -0.29pp below no-evidence (plan_005)\n3. **RSFT CED best**: Ign-F1=45.85, +5.49pp over SFT (s43)\n4. **Decoupling spectrum**: Complete data for GRPO QLoRA / GRPO bf16 / DPO / RSFT\n5. **QLoRA amplification**: bf16 0.4549 vs QLoRA 0.0138 (plan_011 vs QLoRA runs)\n6. **EDCR per-relation independence**: ρ=-0.064 vs evi_f1 (D070)\n7. **top_k ablation**: k=1 > k=3, precision > quantity (plan_008)\n8. **DREEAM baseline**: F1=63.57, Evi-F1=54.01 reproduced (plan_004)\n\n### Critical Gaps (blocking paper submission)\n\n1. **D076 unified reevals** — blocking Claim 3 statistical test\n2. **CED reranker Ign-F1** — needed for main table\n3. **Test set evaluation** (plan_002) — no official numbers yet\n4. **DREEAM-protocol Evi-F1 alignment** — cross-paradigm evidence comparison\n\n### Nice-to-Have (strengthen but not blocking)\n\n1. EDCR human validation (plan_013) — RC6\n2. Post-hoc retrieval baseline (SFT + BM25) — RC10\n3. Model size ablation (plan_006) — RC4\n4. TP-only EDCR (D071) — method-level confound\n5. Re-DocRED extension (plan_007) — RC4\n",
      "numLines": 283,
      "startLine": 1,
      "totalLines": 283
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
Now let me check if there's a paper_framing.md and writing_plan.yaml, and look at the actual LaTeX paper directory structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "e957f8b3-d7f0-40e2-b4ad-98d0228ea349",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016C4SVNyGRHHxnS3sFs4hnE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26539,
      "cache_read_input_tokens": 30517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 26539
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

_source line 24_

<details open><summary>🔧 Tool call — Glob · `toolu_01PNphodJuzLoQSNXNBJUnJ5`</summary>

```json
{
  "pattern": "**/paper_framing*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "3b0352bb-8c32-4e37-bc24-2a1a1b03befc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016C4SVNyGRHHxnS3sFs4hnE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26539,
      "cache_read_input_tokens": 30517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 26539
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

_source line 25 · 2026-05-21T22:56:13.569Z_

<details><summary>↩ Tool result · `toolu_01PNphodJuzLoQSNXNBJUnJ5`</summary>

```text
artifacts/dream_reports/dream_20260515T120227/best/paper_framing.md
artifacts/dream_reports/dream_20260515T120227/median/paper_framing.md
artifacts/dream_reports/dream_20260515T120227/worst/paper_framing.md
artifacts/dream_reports/dream_20260515T132059/best/paper_framing.md
artifacts/dream_reports/dream_20260515T132059/median/paper_framing.md
artifacts/dream_reports/dream_20260515T132059/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T105318/best/paper_framing.md
artifacts/dream_reports/dream_20260516T105318/median/paper_framing.md
artifacts/dream_reports/dream_20260516T105318/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T155803/best/paper_framing.md
artifacts/dream_reports/dream_20260516T155803/median/paper_framing.md
artifacts/dream_reports/dream_20260516T155803/worst/paper_framing.md
paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "6a1ff96d-5d9b-42e3-a515-8e3e2e333e2d",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260515T120227/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260515T120227/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260515T120227/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260515T132059/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260515T132059/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260515T132059/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T105318/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T105318/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T105318/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T155803/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T155803/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T155803/worst/paper_framing.md",
      "paper_framing.md"
    ],
    "durationMs": 35,
    "numFiles": 13,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Glob · `toolu_01V2PejDofsu3EfJi3FtkrFU`</summary>

```json
{
  "pattern": "**/writing_plan*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "dc88c539-5263-4e97-bcc0-5141653d8508",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016C4SVNyGRHHxnS3sFs4hnE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26539,
      "cache_read_input_tokens": 30517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 26539
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

_source line 27 · 2026-05-21T22:56:14.144Z_

<details><summary>↩ Tool result · `toolu_01V2PejDofsu3EfJi3FtkrFU`</summary>

```text
writing_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "e9a33c0b-5699-4500-bd9a-c905a99f6590",
  "tool_use_result": {
    "filenames": [
      "writing_plan.yaml"
    ],
    "durationMs": 36,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Glob · `toolu_01D3WoFwJJj74kC9ZP8MEHbd`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "6aea536b-59be-4e2b-bc2b-bfa9643bee74",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016C4SVNyGRHHxnS3sFs4hnE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26539,
      "cache_read_input_tokens": 30517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 26539
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

_source line 29 · 2026-05-21T22:56:14.775Z_

<details><summary>↩ Tool result · `toolu_01D3WoFwJJj74kC9ZP8MEHbd`</summary>

```text
artifacts/dream_reports/dream_20260515T120227/best/paper.tex
artifacts/dream_reports/dream_20260515T120227/median/paper.tex
artifacts/dream_reports/dream_20260515T120227/worst/paper.tex
artifacts/dream_reports/dream_20260515T132059/best/paper.tex
artifacts/dream_reports/dream_20260515T132059/median/paper.tex
artifacts/dream_reports/dream_20260515T132059/worst/paper.tex
artifacts/dream_reports/dream_20260516T105318/best/paper.tex
artifacts/dream_reports/dream_20260516T105318/median/paper.tex
artifacts/dream_reports/dream_20260516T105318/worst/paper.tex
artifacts/dream_reports/dream_20260516T155803/best/paper.tex
artifacts/dream_reports/dream_20260516T155803/median/paper.tex
artifacts/dream_reports/dream_20260516T155803/worst/paper.tex
docs/paper/acl-style/acl_lualatex.tex
docs/paper/acl-style/acl_latex.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/introduction.tex
docs/paper/main.tex
docs/paper/sections/method.tex
docs/paper/sections/analysis.tex
docs/paper/sections/related_work.tex
docs/paper/sections/experiments.tex
docs/paper/sections/appendix.tex
docs/paper/sections/limitations.tex
docs/paper/sections/abstract.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "2ea69ff2-46bf-4e77-8f4f-8ab597f212f3",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260515T120227/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T120227/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T120227/worst/paper.tex",
      "artifacts/dream_reports/dream_20260515T132059/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T132059/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T132059/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T105318/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T105318/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T105318/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T155803/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T155803/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T155803/worst/paper.tex",
      "docs/paper/acl-style/acl_lualatex.tex",
      "docs/paper/acl-style/acl_latex.tex",
      "artifacts/_project/paper/experiments.tex",
      "artifacts/_project/paper/method.tex",
      "artifacts/_project/paper/introduction.tex",
      "docs/paper/main.tex",
      "docs/paper/sections/method.tex",
      "docs/paper/sections/analysis.tex",
      "docs/paper/sections/related_work.tex",
      "docs/paper/sections/experiments.tex",
      "docs/paper/sections/appendix.tex",
      "docs/paper/sections/limitations.tex",
      "docs/paper/sections/abstract.tex",
      "docs/paper/sections/conclusion.tex",
      "docs/paper/sections/introduction.tex"
    ],
    "durationMs": 27,
    "numFiles": 27,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01EkUXxAyMkSWL5zt1v6iCQh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/comprehensive_results.md",
  "offset": 225
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "2314a7e3-82be-4d32-b65c-78fc76611f5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016C4SVNyGRHHxnS3sFs4hnE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26539,
      "cache_read_input_tokens": 30517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 26539
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

_source line 31 · 2026-05-21T22:56:15.651Z_

<details><summary>↩ Tool result · `toolu_01EkUXxAyMkSWL5zt1v6iCQh`</summary>

```text
225	| 4B | RSFT CED from SFT s44 | Pipeline in progress | D112 pipeline |
226	
227	---
228	
229	## Key Findings
230	
231	1. **RSFT variance stabilization is the strongest result.** 4B SFT std=3.80pp -> RSFT CED k=1 std=0.53pp (7.1x reduction). 8B shows ~4.9x reduction. RSFT pulls weak seeds UP (+4.49pp for 4B s42) and compresses strong seeds DOWN (-2.23pp for 4B s44), converging all seeds toward a stable performance band. This is not just performance improvement but a qualitatively different training property.
232	
233	2. **CED scoring >> Random selection, but approximately equal to flat-NLI.** CED k=1 beats Random by +3.52pp (0.4466 vs 0.4114). CED vs flat-NLI differ by only 0.18pp (not significant). The critical factor is non-random data selection, not the specific scoring function.
234	
235	3. **Evidence tax is non-monotonic across scales.** 1.7B: evidence HELPS by 8.04pp (CoT effect). 4B: evidence HURTS by 7.47pp (generation burden). 8B: negligible 0.28pp tax. Suggests an optimal scale threshold where evidence generation becomes "free."
236	
237	4. **GRPO bf16 works, QLoRA GRPO catastrophically fails.** bf16 GRPO G=8 ckpt-100 achieves 0.4549 (+5.75pp over SFT s42), while QLoRA GRPO produces near-zero f1_reward across both Qwen and Llama families. Precision is a hard requirement for RL on structured IE.
238	
239	5. **RSFT gains transfer cross-architecture and cross-dataset.** Llama-3.1-8B RSFT CED k=1: 0.5662 (+2.78pp over SFT). Re-DocRED RSFT: 0.4145 (+4.86pp over SFT). The method is not Qwen-specific or DocRED-specific.
240	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "bbe2c952-ea02-4497-9da7-224c91c28a4d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/comprehensive_results.md",
      "content": "| 4B | RSFT CED from SFT s44 | Pipeline in progress | D112 pipeline |\n\n---\n\n## Key Findings\n\n1. **RSFT variance stabilization is the strongest result.** 4B SFT std=3.80pp -> RSFT CED k=1 std=0.53pp (7.1x reduction). 8B shows ~4.9x reduction. RSFT pulls weak seeds UP (+4.49pp for 4B s42) and compresses strong seeds DOWN (-2.23pp for 4B s44), converging all seeds toward a stable performance band. This is not just performance improvement but a qualitatively different training property.\n\n2. **CED scoring >> Random selection, but approximately equal to flat-NLI.** CED k=1 beats Random by +3.52pp (0.4466 vs 0.4114). CED vs flat-NLI differ by only 0.18pp (not significant). The critical factor is non-random data selection, not the specific scoring function.\n\n3. **Evidence tax is non-monotonic across scales.** 1.7B: evidence HELPS by 8.04pp (CoT effect). 4B: evidence HURTS by 7.47pp (generation burden). 8B: negligible 0.28pp tax. Suggests an optimal scale threshold where evidence generation becomes \"free.\"\n\n4. **GRPO bf16 works, QLoRA GRPO catastrophically fails.** bf16 GRPO G=8 ckpt-100 achieves 0.4549 (+5.75pp over SFT s42), while QLoRA GRPO produces near-zero f1_reward across both Qwen and Llama families. Precision is a hard requirement for RL on structured IE.\n\n5. **RSFT gains transfer cross-architecture and cross-dataset.** Llama-3.1-8B RSFT CED k=1: 0.5662 (+2.78pp over SFT). Re-DocRED RSFT: 0.4145 (+4.86pp over SFT). The method is not Qwen-specific or DocRED-specific.\n",
      "numLines": 16,
      "startLine": 225,
      "totalLines": 240
    }
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_012WVcMz3YoKfWKSjxwPrMY9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/negative_review.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "a535b6fb-7e59-4189-be5f-d23b532e7c69",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016C4SVNyGRHHxnS3sFs4hnE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26539,
      "cache_read_input_tokens": 30517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 26539
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

_source line 33 · 2026-05-21T22:56:16.168Z_

<details><summary>↩ Tool result · `toolu_012WVcMz3YoKfWKSjxwPrMY9`</summary>

```text
1	# Negative 实验系统性复盘
2	
3	> 18 个 conclusion=negative 实验，按 Group 合并分析。SFT baseline: rel_f1=0.4057 (Qwen3-4B, DocRED dev)。
4	
5	---
6	
7	## Group 1: GRPO lr5e6 全轨迹 (5 evals)
8	
9	**实验**: mvp2_eval_lr5e6_r1_ckpt20 / ckpt40_r2 / ckpt60_r2 / ckpt80 / ckpt100
10	
11	**一句话**: lr=5e-6 无法挽救 GRPO+QLoRA 灾难性遗忘，200 步全程 rel_f1 < 0.014。
12	
13	### 1. 证伪了什么？
14	
15	**假设**: "ced_kl001_r4 (lr=5e-5) 的灾难性遗忘源于学习率过高，降到 5e-6 可恢复关系抽取能力。"
16	
17	证伪。lr 降 10x 后 rel_f1 从 max 0.217 (lr5e-5) 进一步恶化到 max 0.014 (lr5e-6)。遗忘在 step 20 即已发生且不可恢复。
18	
19	### 2. 当时怎么处理的？
20	
21	- D030: ckpt-20 FAIL 后扩展到全 checkpoint 轨迹评估
22	- D031: ckpt-40 更差后判死 GRPO+QLoRA 方向，pivot 到离线 RL (RSFT/DPO)
23	- D032: kill 训练释放 GPU
24	- D033: 全 6 checkpoint 确认，记为论文 negative result
25	
26	### 3. 处理是否正确？
27	
28	正确。此时已有两个 LR（5e-5 和 5e-6）的完整证据链，且后续 bf16 实验 (plan_011) 证实根因是 QLoRA 量化而非 GRPO 本身。Pivot 到 RSFT 是正确决策。
29	
30	**遗漏诊断**: lr5e6 的 evi_f1 从 0.628 单调升至 0.850（超 SFT 0.798），说明 CED reward 确实在驱动证据能力提升。如果当时就意识到这是"单侧学习"（evidence 学到了但 relation 崩了），可以更早形成 decoupling claim 的 framing。
31	
32	### 4. 推导链是否完整？
33	
34	完整。lr5e-6 → lr5e-5 → bf16 (plan_011) 形成了完整的消融链，最终确认 QLoRA quantization 是 catastrophic forgetting 的根因 (D052: Δ=+23.8pp)。
35	
36	---
37	
38	## Group 2: GRPO Mode Collapse (3 experiments)
39	
40	### mvp2_grpo_ced_r5 — CED reward 被 shortcut hack
41	
42	**证伪假设**: "CED reward (format×0.3, f1×3.0, ced×1.0) 在 kl_coef=0 下可稳定训练。"
43	
44	证伪。模型发现极短输出（34 tokens）即可获得 ced_reward≈0.99 + format_reward=0.3，完全放弃关系抽取。
45	
46	**处理**: D014 提出 F1 门控（CED reward 仅在有有效 triple 时计算），D16 kill 释放 GPU。但 D020 发现 F1 门控从未实现，直到 ced_kl001_r4 才在 kl_coef=0.01 下跑出结果。
47	
48	**处理正确性**: 部分正确。F1 门控方案合理但执行延迟。后续 ced_kl001_r4 用 kl_coef=0.01 替代了缺失的 F1 门控，但两者是互补的——F1 门控从未被真正测试。
49	
50	### mvp2_grpo_extract_r3 — Extraction-only reward 停滞
51	
52	**证伪假设**: "纯 extraction reward (format×0.3, f1×3.0) 可建立 stable GRPO baseline。"
53	
54	证伪。num_gen=4 + kl_coef=0 导致 4 个输出完全相同 → reward_std=0 → 梯度消失。从 step 520+ grad_norm=0，训练实际已冻结。
55	
56	**处理**: D17/D22/D23 kill 并记录 ablation 结论（CED dense signal 是 GRPO 训练必需的）。
57	
58	**处理正确性**: 正确，但可追问：如果 extract_r3 用 num_gen=8 + kl_coef=0.01 会怎样？D020 配置下 extract_r4 仍在 step 10 后 f1_reward=0（D22），说明 extraction-only reward 本质上信号密度不足。
59	
60	### mvp2_grpo_flatnli_r6 — Flat-NLI collapse
61	
62	**证伪假设**: "Flat-NLI reward 在 D020 稳定配置 (kl=0.01, G=8) 下可维持训练。"
63	
64	证伪。Step 25 即 frac_zero_std=0.9，f1/NLI reward 全零，仅 format hacking。
65	
66	**处理**: D24/D25 kill，确立 "三路对比仅 CED 存活" 的 ablation 结论。
67	
68	**处理正确性**: 正确。三路 reward ablation (CED/extract-only/flat-NLI) 在同一配置下的对比是干净的实验设计。
69	
70	**Group 2 整体遗漏**: 所有 mode collapse 实验用的 num_gen=4 或 kl=0 配置偏极端。但 D020 配置 (G=8, kl=0.01) 下 extract-only 和 flat-NLI 仍 collapse 而 CED 存活，说明 CED reward 的信息密度确实是关键差异。无遗漏。
71	
72	---
73	
74	## Group 3: CED Reward Hacking (3 evals)
75	
76	**实验**: mvp2_eval_ced_kl001_r4_early (step50) / step90 / step100
77	
78	**一句话**: CED reward 训练曲线上升但 eval F1 崩塌，经典 reward hacking + QLoRA 灾难性遗忘。
79	
80	### 1. 证伪了什么？
81	
82	**假设**: "CED reward + kl_coef=0.01 + G=8 + lr=5e-5 可以在避免 mode collapse 的同时提升任务指标。"
83	
84	证伪。训练 reward 从 0.3 升至 1.37，但 eval rel_f1 max=0.217（SFT=0.4057），EDCR=0.86 (高) 但 recall 崩塌。模型学会了少预测以获高 EDCR。
85	
86	### 2. 当时怎么处理的？
87	
88	- D26/D27: 诊断为 lr=5e-5 过高 + CED recall shortcut
89	- 启动 P0 (lr=5e-6) 和 P0+P1 (recall penalty)
90	- P0+P1 因 recall penalty 梯度爆炸被 kill (D28/D29)
91	- P0 也全线失败（见 Group 1）
92	- 最终 D31 pivot 到离线 RL
93	
94	### 3. 处理是否正确？
95	
96	部分正确。Pivot 是对的，但诊断归因不够精确——当时归因为 "lr 过高" 和 "CED recall shortcut"，后来 plan_011 证明真正根因是 QLoRA quantization (D52)。如果当时直接尝试 bf16 训练而非 lr sweep，可以节省约 12h GPU 时间。
97	
98	### 4. 推导链是否完整？
99	
100	完整（通过后续 plan_011 补全）。lr5e-5 → lr5e-6 → bf16 → 确认 quantization 是根因。recall penalty 方向被正确放弃（梯度不稳定）。
101	
102	---
103	
104	## Group 4: DPO Failures (4 records, 3 独立实验)
105	
106	### plan_012_dpo_ced (3 epochs) — 严重过拟合
107	
108	**证伪假设**: "DPO+CED preference pairs (β=0.1, 3ep, 2666 pairs) 可以替代 online GRPO。"
109	
110	证伪。rewards_accuracy=1.0, margins 9x 膨胀, rel_f1=0.3429（低于 SFT baseline 6.3pp）。
111	
112	**处理**: 识别为过拟合 confound，重训 1 epoch。
113	
114	### plan_012_dpo_ced_1ep / eval_plan_012_dpo_ced_1ep — 1ep 灾难性崩塌（后证实为 bug）
115	
116	**证伪假设**: 原以为证伪 "1 epoch DPO 可消除过拟合问题"。
117	
118	**实际**: rel_f1=0.0022 是 eval bug（缺 --sft_adapter 参数）。D064 发现后重跑。
119	
120	### eval_plan_012_dpo_1ep_fixed_r2 — DPO 1ep = SFT（无提升）
121	
122	**证伪假设**: "DPO+CED preference learning 可以改善 SFT baseline。"
123	
124	证伪。修复后 rel_f1=0.4034，vs SFT=0.4057 (Δ=-0.23pp)。DPO 1ep 中性，无正向收益。
125	
126	### 处理
127	
128	- D61: 关闭 DPO 线（基于 bug eval）
129	- D63/D64: 发现 --sft_adapter bug，重跑
130	- D67/D68: 修正叙事为 "DPO 中性/轻度退化"
131	
132	### 处理正确性
133	
134	**遗漏**: 
135	1. DPO 3ep rel_f1=0.3429 + evi_f1=0.8403 呈现与 GRPO 一致的 decoupling 方向（rel↓ evi↑），这在 D62/D69 被正确识别为跨方法系统性现象。
136	2. **未探索**: β 调参（0.1 可能过大）、更少 epochs（0.5ep?）、不同 pair 构造策略。但考虑到 1ep 已经是中性结果，DPO 路线被正确放弃。
137	
138	### 推导链完整性
139	
140	完整。1ep→3ep 的非单调退化 + bug 修复后中性结果 = DPO 对此任务无效。作为 RL spectrum 数据点有论文价值。
141	
142	---
143	
144	## Group 5: RSFT top_k=3
145	
146	### reeval_rsft_topk3
147	
148	**证伪假设**: "RSFT 取 top_k=3 (更多训练数据) 优于 top_k=1。"
149	
150	证伪。rel_f1=0.4454 vs CED RSFT top_k=1 约 0.46 (低约 1.5pp)。更多样本引入噪声。
151	
152	**处理**: 记为 negative，保留 top_k=1 作为最优策略。
153	
154	**处理正确性**: 正确。但有一个未探索方向：top_k=1 with higher CED threshold（只取 CED score 极高的样本）可能进一步提升质量。当前 top_k=1 实质是 "per-doc best CED score sample"，但未对绝对 CED 分数做 threshold 过滤。
155	
156	**推导链**: 基本完整。top_k=3 vs top_k=1 的对比清晰。D078 进一步确认 CED vs flat-NLI 统计不可区分。
157	
158	---
159	
160	## Group 6: Truncation Diagnosis
161	
162	### mvp2_eval_rsft_r2b_maxtok1536_r2
163	
164	**证伪假设**: "EDCR 偏低 (0.66) 是因为输出被 1024 token 截断，增加 max_tokens 可显著改善。"
165	
166	证伪。1536 tokens 后 truncated 179→146 (-33)，EDCR 0.6609→0.6740 (+0.013)，效果微乎其微。Distractor citation 是 RSFT 模型的真实行为。
167	
168	**处理**: 确认 EDCR 偏高是 RSFT 固有局限（模型 spray-and-pray 引用），不再追求 truncation 修复。
169	
170	**处理正确性**: 正确。此实验干净地隔离了 truncation vs distractor 两个因素。
171	
172	**遗漏**: 后续未直接用 CED-as-reranker 尝试去除 distractor citations（在推理时过滤低 CED 分的 evidence）。D037 曾提出此方案但因 RSFT eval bug 被搁置，修复后未再跟进。
173	
174	---
175	
176	## Group 7: Cross-dataset Transfer
177	
178	### plan_007_redocred_rsft_eval_r2
179	
180	**证伪假设**: "CED-RSFT improvements on DocRED transfer to Re-DocRED。"
181	
182	F1=0.0025 (catastrophic)，但 Evi-F1=0.8837 正常。
183	
184	**处理**: 诊断为 pipeline bug（adapter loading / prompt format / relation label mapping）。后续 r4/r5 修复后成功（SFT baseline Re-DocRED Ign-F1=0.3659, D080）。
185	
186	**处理正确性**: 正确。Evi-F1 正常排除了模型彻底崩坏的可能，明确指向 pipeline 问题。
187	
188	**推导链**: 完整。r2 bug → 修复 → r4/r5 成功。
189	
190	---
191	
192	## 最终总结：被忽视的方法改进线索
193	
194	### 线索 1: RSFT + 推理时 CED Reranking（去除 Distractor Citations）
195	
196	**来源**: Group 6 (truncation diagnosis) + D037 (CED-as-reranker 被搁置)
197	
198	**线索**: RSFT 模型 EDCR=0.66 是因为 spray-and-pray 式引用 distractor sentences。当前方案接受这个行为不做处理。但 CED 本身是强判别器（MVP-1: accuracy 81.5%, margin 0.48），可以在推理时对每个 predicted triple 的 evidence sentences 逐条做 NLI 过滤，去除 CED score 低于 threshold 的 citations。
199	
200	**为什么有潜力**: 
201	- 不需要额外训练，纯推理时增强
202	- CED 判别能力已验证
203	- EDCR 从 0.66 提升到 0.80+ 是合理预期（参考 GRPO 训练后 EDCR 约 0.85-0.99）
204	- 可以作为论文的 inference-time component，与 RSFT training-time 互补
205	
206	**建议验证**: 对 RSFT 输出的每个 triple 的 evidence list，用 DeBERTa NLI 逐条评分，去除 entailment score < tau 的 sentences。评估 EDCR 变化和 Evi-F1 变化。成本：约 30min 推理时间，无训练开销。
207	
208	### 线索 2: bf16 GRPO → RSFT 两阶段训练
209	
210	**来源**: Group 1 (GRPO evi_f1 单调提升) + D51 (bf16 GRPO rel_f1=0.4549)
211	
212	**线索**: bf16 GRPO (plan_011) 达到 rel_f1=0.4549 + evi_f1=0.8086，与 RSFT (0.46 + 0.81) 基本平齐。两者各有优势：GRPO 优化 reward 信号（包括 CED 对 evidence 质量的直接监督），RSFT 通过数据筛选保持训练稳定性。未尝试过的组合：SFT → RSFT (筛选高质量样本) → 短程 bf16 GRPO (进一步优化 evidence 质量)。
213	
214	**为什么有潜力**:
215	- RSFT 后模型已有良好的 rel_f1 基础，短程 GRPO 不太可能导致灾难性遗忘
216	- GRPO 对 evidence quality 的优化是在线的（可以利用 CED 做 per-step feedback），RSFT 是离线的（只能用固定 CED 阈值）
217	- bf16 已证明无 catastrophic forgetting
218	
219	**建议验证**: 从 RSFT checkpoint 开始，bf16 GRPO 20-50 步（低 lr=1e-6），只用 CED reward（不加 f1 reward 避免冲突），评估 EDCR 是否显著提升且 rel_f1 不退化。
220	
221	### 线索 3: DPO 数据质量问题——pair 构造策略可能是失败根因
222	
223	**来源**: Group 4 (DPO 1ep 中性，3ep 退化)
224	
225	**线索**: 当前 DPO pairs 构造为 "CED top-1 = chosen, CED bottom-1 = rejected"。但 D078 证明 CED vs flat-NLI 统计不可区分，且 CED 在 data selection 上无显著优势。这意味着 DPO pairs 的 preference signal 本身可能太弱——chosen 和 rejected 在关系抽取质量上可能差异不大，仅在 evidence 质量上有差异。DPO 因此只学到了 evidence 偏好（evi_f1 上升）而对 relation extraction 无正向信号（rel_f1 不变或下降）。
226	
227	**为什么有潜力**: 如果改用 rel_f1-based pair construction（chosen = 关系抽取 F1 高的样本，rejected = F1 低的样本，同时要求两者 format 正确），DPO 的 preference signal 直接对准关系抽取任务，而非 evidence 质量。这可能打破当前 "DPO 只优化 evidence 无法提升 relation" 的困局。
228	
229	**建议验证**: 从现有 RSFT candidates (8 generations per doc) 中重新构造 pairs：chosen = max(rel_f1) sample, rejected = min(rel_f1) sample（要求两者 format_ok）。用相同 DPO 配置 (beta=0.1, 1ep) 训练。如果 rel_f1 > 0.42 (超过 SFT+DPO-CED 的 0.4034)，说明 pair 构造是关键变量。
230	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "40a5e75b-789c-4734-9cf0-33b248dbf629",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/negative_review.md",
      "content": "# Negative 实验系统性复盘\n\n> 18 个 conclusion=negative 实验，按 Group 合并分析。SFT baseline: rel_f1=0.4057 (Qwen3-4B, DocRED dev)。\n\n---\n\n## Group 1: GRPO lr5e6 全轨迹 (5 evals)\n\n**实验**: mvp2_eval_lr5e6_r1_ckpt20 / ckpt40_r2 / ckpt60_r2 / ckpt80 / ckpt100\n\n**一句话**: lr=5e-6 无法挽救 GRPO+QLoRA 灾难性遗忘，200 步全程 rel_f1 < 0.014。\n\n### 1. 证伪了什么？\n\n**假设**: \"ced_kl001_r4 (lr=5e-5) 的灾难性遗忘源于学习率过高，降到 5e-6 可恢复关系抽取能力。\"\n\n证伪。lr 降 10x 后 rel_f1 从 max 0.217 (lr5e-5) 进一步恶化到 max 0.014 (lr5e-6)。遗忘在 step 20 即已发生且不可恢复。\n\n### 2. 当时怎么处理的？\n\n- D030: ckpt-20 FAIL 后扩展到全 checkpoint 轨迹评估\n- D031: ckpt-40 更差后判死 GRPO+QLoRA 方向，pivot 到离线 RL (RSFT/DPO)\n- D032: kill 训练释放 GPU\n- D033: 全 6 checkpoint 确认，记为论文 negative result\n\n### 3. 处理是否正确？\n\n正确。此时已有两个 LR（5e-5 和 5e-6）的完整证据链，且后续 bf16 实验 (plan_011) 证实根因是 QLoRA 量化而非 GRPO 本身。Pivot 到 RSFT 是正确决策。\n\n**遗漏诊断**: lr5e6 的 evi_f1 从 0.628 单调升至 0.850（超 SFT 0.798），说明 CED reward 确实在驱动证据能力提升。如果当时就意识到这是\"单侧学习\"（evidence 学到了但 relation 崩了），可以更早形成 decoupling claim 的 framing。\n\n### 4. 推导链是否完整？\n\n完整。lr5e-6 → lr5e-5 → bf16 (plan_011) 形成了完整的消融链，最终确认 QLoRA quantization 是 catastrophic forgetting 的根因 (D052: Δ=+23.8pp)。\n\n---\n\n## Group 2: GRPO Mode Collapse (3 experiments)\n\n### mvp2_grpo_ced_r5 — CED reward 被 shortcut hack\n\n**证伪假设**: \"CED reward (format×0.3, f1×3.0, ced×1.0) 在 kl_coef=0 下可稳定训练。\"\n\n证伪。模型发现极短输出（34 tokens）即可获得 ced_reward≈0.99 + format_reward=0.3，完全放弃关系抽取。\n\n**处理**: D014 提出 F1 门控（CED reward 仅在有有效 triple 时计算），D16 kill 释放 GPU。但 D020 发现 F1 门控从未实现，直到 ced_kl001_r4 才在 kl_coef=0.01 下跑出结果。\n\n**处理正确性**: 部分正确。F1 门控方案合理但执行延迟。后续 ced_kl001_r4 用 kl_coef=0.01 替代了缺失的 F1 门控，但两者是互补的——F1 门控从未被真正测试。\n\n### mvp2_grpo_extract_r3 — Extraction-only reward 停滞\n\n**证伪假设**: \"纯 extraction reward (format×0.3, f1×3.0) 可建立 stable GRPO baseline。\"\n\n证伪。num_gen=4 + kl_coef=0 导致 4 个输出完全相同 → reward_std=0 → 梯度消失。从 step 520+ grad_norm=0，训练实际已冻结。\n\n**处理**: D17/D22/D23 kill 并记录 ablation 结论（CED dense signal 是 GRPO 训练必需的）。\n\n**处理正确性**: 正确，但可追问：如果 extract_r3 用 num_gen=8 + kl_coef=0.01 会怎样？D020 配置下 extract_r4 仍在 step 10 后 f1_reward=0（D22），说明 extraction-only reward 本质上信号密度不足。\n\n### mvp2_grpo_flatnli_r6 — Flat-NLI collapse\n\n**证伪假设**: \"Flat-NLI reward 在 D020 稳定配置 (kl=0.01, G=8) 下可维持训练。\"\n\n证伪。Step 25 即 frac_zero_std=0.9，f1/NLI reward 全零，仅 format hacking。\n\n**处理**: D24/D25 kill，确立 \"三路对比仅 CED 存活\" 的 ablation 结论。\n\n**处理正确性**: 正确。三路 reward ablation (CED/extract-only/flat-NLI) 在同一配置下的对比是干净的实验设计。\n\n**Group 2 整体遗漏**: 所有 mode collapse 实验用的 num_gen=4 或 kl=0 配置偏极端。但 D020 配置 (G=8, kl=0.01) 下 extract-only 和 flat-NLI 仍 collapse 而 CED 存活，说明 CED reward 的信息密度确实是关键差异。无遗漏。\n\n---\n\n## Group 3: CED Reward Hacking (3 evals)\n\n**实验**: mvp2_eval_ced_kl001_r4_early (step50) / step90 / step100\n\n**一句话**: CED reward 训练曲线上升但 eval F1 崩塌，经典 reward hacking + QLoRA 灾难性遗忘。\n\n### 1. 证伪了什么？\n\n**假设**: \"CED reward + kl_coef=0.01 + G=8 + lr=5e-5 可以在避免 mode collapse 的同时提升任务指标。\"\n\n证伪。训练 reward 从 0.3 升至 1.37，但 eval rel_f1 max=0.217（SFT=0.4057），EDCR=0.86 (高) 但 recall 崩塌。模型学会了少预测以获高 EDCR。\n\n### 2. 当时怎么处理的？\n\n- D26/D27: 诊断为 lr=5e-5 过高 + CED recall shortcut\n- 启动 P0 (lr=5e-6) 和 P0+P1 (recall penalty)\n- P0+P1 因 recall penalty 梯度爆炸被 kill (D28/D29)\n- P0 也全线失败（见 Group 1）\n- 最终 D31 pivot 到离线 RL\n\n### 3. 处理是否正确？\n\n部分正确。Pivot 是对的，但诊断归因不够精确——当时归因为 \"lr 过高\" 和 \"CED recall shortcut\"，后来 plan_011 证明真正根因是 QLoRA quantization (D52)。如果当时直接尝试 bf16 训练而非 lr sweep，可以节省约 12h GPU 时间。\n\n### 4. 推导链是否完整？\n\n完整（通过后续 plan_011 补全）。lr5e-5 → lr5e-6 → bf16 → 确认 quantization 是根因。recall penalty 方向被正确放弃（梯度不稳定）。\n\n---\n\n## Group 4: DPO Failures (4 records, 3 独立实验)\n\n### plan_012_dpo_ced (3 epochs) — 严重过拟合\n\n**证伪假设**: \"DPO+CED preference pairs (β=0.1, 3ep, 2666 pairs) 可以替代 online GRPO。\"\n\n证伪。rewards_accuracy=1.0, margins 9x 膨胀, rel_f1=0.3429（低于 SFT baseline 6.3pp）。\n\n**处理**: 识别为过拟合 confound，重训 1 epoch。\n\n### plan_012_dpo_ced_1ep / eval_plan_012_dpo_ced_1ep — 1ep 灾难性崩塌（后证实为 bug）\n\n**证伪假设**: 原以为证伪 \"1 epoch DPO 可消除过拟合问题\"。\n\n**实际**: rel_f1=0.0022 是 eval bug（缺 --sft_adapter 参数）。D064 发现后重跑。\n\n### eval_plan_012_dpo_1ep_fixed_r2 — DPO 1ep = SFT（无提升）\n\n**证伪假设**: \"DPO+CED preference learning 可以改善 SFT baseline。\"\n\n证伪。修复后 rel_f1=0.4034，vs SFT=0.4057 (Δ=-0.23pp)。DPO 1ep 中性，无正向收益。\n\n### 处理\n\n- D61: 关闭 DPO 线（基于 bug eval）\n- D63/D64: 发现 --sft_adapter bug，重跑\n- D67/D68: 修正叙事为 \"DPO 中性/轻度退化\"\n\n### 处理正确性\n\n**遗漏**: \n1. DPO 3ep rel_f1=0.3429 + evi_f1=0.8403 呈现与 GRPO 一致的 decoupling 方向（rel↓ evi↑），这在 D62/D69 被正确识别为跨方法系统性现象。\n2. **未探索**: β 调参（0.1 可能过大）、更少 epochs（0.5ep?）、不同 pair 构造策略。但考虑到 1ep 已经是中性结果，DPO 路线被正确放弃。\n\n### 推导链完整性\n\n完整。1ep→3ep 的非单调退化 + bug 修复后中性结果 = DPO 对此任务无效。作为 RL spectrum 数据点有论文价值。\n\n---\n\n## Group 5: RSFT top_k=3\n\n### reeval_rsft_topk3\n\n**证伪假设**: \"RSFT 取 top_k=3 (更多训练数据) 优于 top_k=1。\"\n\n证伪。rel_f1=0.4454 vs CED RSFT top_k=1 约 0.46 (低约 1.5pp)。更多样本引入噪声。\n\n**处理**: 记为 negative，保留 top_k=1 作为最优策略。\n\n**处理正确性**: 正确。但有一个未探索方向：top_k=1 with higher CED threshold（只取 CED score 极高的样本）可能进一步提升质量。当前 top_k=1 实质是 \"per-doc best CED score sample\"，但未对绝对 CED 分数做 threshold 过滤。\n\n**推导链**: 基本完整。top_k=3 vs top_k=1 的对比清晰。D078 进一步确认 CED vs flat-NLI 统计不可区分。\n\n---\n\n## Group 6: Truncation Diagnosis\n\n### mvp2_eval_rsft_r2b_maxtok1536_r2\n\n**证伪假设**: \"EDCR 偏低 (0.66) 是因为输出被 1024 token 截断，增加 max_tokens 可显著改善。\"\n\n证伪。1536 tokens 后 truncated 179→146 (-33)，EDCR 0.6609→0.6740 (+0.013)，效果微乎其微。Distractor citation 是 RSFT 模型的真实行为。\n\n**处理**: 确认 EDCR 偏高是 RSFT 固有局限（模型 spray-and-pray 引用），不再追求 truncation 修复。\n\n**处理正确性**: 正确。此实验干净地隔离了 truncation vs distractor 两个因素。\n\n**遗漏**: 后续未直接用 CED-as-reranker 尝试去除 distractor citations（在推理时过滤低 CED 分的 evidence）。D037 曾提出此方案但因 RSFT eval bug 被搁置，修复后未再跟进。\n\n---\n\n## Group 7: Cross-dataset Transfer\n\n### plan_007_redocred_rsft_eval_r2\n\n**证伪假设**: \"CED-RSFT improvements on DocRED transfer to Re-DocRED。\"\n\nF1=0.0025 (catastrophic)，但 Evi-F1=0.8837 正常。\n\n**处理**: 诊断为 pipeline bug（adapter loading / prompt format / relation label mapping）。后续 r4/r5 修复后成功（SFT baseline Re-DocRED Ign-F1=0.3659, D080）。\n\n**处理正确性**: 正确。Evi-F1 正常排除了模型彻底崩坏的可能，明确指向 pipeline 问题。\n\n**推导链**: 完整。r2 bug → 修复 → r4/r5 成功。\n\n---\n\n## 最终总结：被忽视的方法改进线索\n\n### 线索 1: RSFT + 推理时 CED Reranking（去除 Distractor Citations）\n\n**来源**: Group 6 (truncation diagnosis) + D037 (CED-as-reranker 被搁置)\n\n**线索**: RSFT 模型 EDCR=0.66 是因为 spray-and-pray 式引用 distractor sentences。当前方案接受这个行为不做处理。但 CED 本身是强判别器（MVP-1: accuracy 81.5%, margin 0.48），可以在推理时对每个 predicted triple 的 evidence sentences 逐条做 NLI 过滤，去除 CED score 低于 threshold 的 citations。\n\n**为什么有潜力**: \n- 不需要额外训练，纯推理时增强\n- CED 判别能力已验证\n- EDCR 从 0.66 提升到 0.80+ 是合理预期（参考 GRPO 训练后 EDCR 约 0.85-0.99）\n- 可以作为论文的 inference-time component，与 RSFT training-time 互补\n\n**建议验证**: 对 RSFT 输出的每个 triple 的 evidence list，用 DeBERTa NLI 逐条评分，去除 entailment score < tau 的 sentences。评估 EDCR 变化和 Evi-F1 变化。成本：约 30min 推理时间，无训练开销。\n\n### 线索 2: bf16 GRPO → RSFT 两阶段训练\n\n**来源**: Group 1 (GRPO evi_f1 单调提升) + D51 (bf16 GRPO rel_f1=0.4549)\n\n**线索**: bf16 GRPO (plan_011) 达到 rel_f1=0.4549 + evi_f1=0.8086，与 RSFT (0.46 + 0.81) 基本平齐。两者各有优势：GRPO 优化 reward 信号（包括 CED 对 evidence 质量的直接监督），RSFT 通过数据筛选保持训练稳定性。未尝试过的组合：SFT → RSFT (筛选高质量样本) → 短程 bf16 GRPO (进一步优化 evidence 质量)。\n\n**为什么有潜力**:\n- RSFT 后模型已有良好的 rel_f1 基础，短程 GRPO 不太可能导致灾难性遗忘\n- GRPO 对 evidence quality 的优化是在线的（可以利用 CED 做 per-step feedback），RSFT 是离线的（只能用固定 CED 阈值）\n- bf16 已证明无 catastrophic forgetting\n\n**建议验证**: 从 RSFT checkpoint 开始，bf16 GRPO 20-50 步（低 lr=1e-6），只用 CED reward（不加 f1 reward 避免冲突），评估 EDCR 是否显著提升且 rel_f1 不退化。\n\n### 线索 3: DPO 数据质量问题——pair 构造策略可能是失败根因\n\n**来源**: Group 4 (DPO 1ep 中性，3ep 退化)\n\n**线索**: 当前 DPO pairs 构造为 \"CED top-1 = chosen, CED bottom-1 = rejected\"。但 D078 证明 CED vs flat-NLI 统计不可区分，且 CED 在 data selection 上无显著优势。这意味着 DPO pairs 的 preference signal 本身可能太弱——chosen 和 rejected 在关系抽取质量上可能差异不大，仅在 evidence 质量上有差异。DPO 因此只学到了 evidence 偏好（evi_f1 上升）而对 relation extraction 无正向信号（rel_f1 不变或下降）。\n\n**为什么有潜力**: 如果改用 rel_f1-based pair construction（chosen = 关系抽取 F1 高的样本，rejected = F1 低的样本，同时要求两者 format 正确），DPO 的 preference signal 直接对准关系抽取任务，而非 evidence 质量。这可能打破当前 \"DPO 只优化 evidence 无法提升 relation\" 的困局。\n\n**建议验证**: 从现有 RSFT candidates (8 generations per doc) 中重新构造 pairs：chosen = max(rel_f1) sample, rejected = min(rel_f1) sample（要求两者 format_ok）。用相同 DPO 配置 (beta=0.1, 1ep) 训练。如果 rel_f1 > 0.42 (超过 SFT+DPO-CED 的 0.4034)，说明 pair 构造是关键变量。\n",
      "numLines": 230,
      "startLine": 1,
      "totalLines": 230
    }
  }
}
```

</details>

---

### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the paper_framing.md and writing_plan.yaml from the project root, and also look at the actual LaTeX sections to understand their current state.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "1e736e4c-a853-4e71-ba05-04dbfceb29cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011LisBVkhEpt9B3zNskyRp2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7841,
      "cache_read_input_tokens": 57056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7841
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

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_01CV5zUo7YTaDwo7crPNuWJX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/writing_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "3c2b871c-3232-405a-ab31-6cfed94b28d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011LisBVkhEpt9B3zNskyRp2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7841,
      "cache_read_input_tokens": 57056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7841
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

_source line 36 · 2026-05-21T22:56:21.987Z_

<details><summary>↩ Tool result · `toolu_01CV5zUo7YTaDwo7crPNuWJX`</summary>

```text
1	meta:
2	  venue: emnlp-2026
3	  submission_type: long
4	  review_system: arr_july
5	  deadline: "2026-07-15"
6	  template:
7	    source: "github.com/acl-org/acl-style-files (official)"
8	    local_path: "projects/faith-evidence-ie/docs/paper/acl-style/"
9	    documentclass: "\\documentclass[11pt]{article}"
10	    options: "\\usepackage[review]{acl}"
11	    template_note: "Official ACL style files cloned 2026-05-17. EMNLP uses identical template."
12	  page_limits:
13	    main_text: 8
14	    references: unlimited
15	    appendix: unlimited
16	  title_candidates:
17	    - "Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction"
18	    - "The Cost of Faithfulness: Evidence-Extraction Trade-offs in Generative Document Relation Extraction"
19	    - "FREIGE: Faithful Evidence-Grounded Document-Level Relation Extraction via Rejection Sampling Fine-Tuning"
20	  preferred_title: 1
21	  visualization:
22	    preferred_tool: matplotlib
23	
24	# ============================================================
25	# PAPER OUTLINE
26	# ============================================================
27	paper_outline:
28	  abstract:
29	    word_budget: 220
30	    key_message: >
31	      Evidence-grounded DocRE 新任务；系统比较 GRPO/DPO/RSFT 三范式；
32	      发现 decoupling spectrum（RL pressure 与 decoupling severity 正相关）；
33	      evidence tax 是 scale-dependent 的（1.7B +6.2pp benefit, 4B -7.0pp cost, 8B ≈0）；
34	      RSFT+NLI scoring 是唯一有效路线；EDCR 双层诊断
35	    must_include:
36	      - task definition (evidence-grounded DocRE, generative LLM qualifier)
37	      - three paradigms compared
38	      - decoupling spectrum core finding
39	      - scale-dependent evidence tax with concrete numbers
40	      - RSFT effectiveness delta vs SFT
41	      - EDCR diagnostic mention
42	    dependencies: [introduction, experiments, method]
43	
44	  introduction:
45	    word_budget: 1200
46	    structure: five_paragraph
47	    paragraphs:
48	      - topic: "LLM DocRE progress but no evidence"
49	        word_budget: 200
50	      - topic: "Why verifiable evidence matters for deployment"
51	        word_budget: 150
52	      - topic: "Encoder retrieval ≠ generative production (SAIS/DREEAM distinction)"
53	        word_budget: 200
54	      - topic: "Our insight: 3 paradigms → decoupling spectrum + scale-dependent tax + RSFT solution"
55	        word_budget: 350
56	      - topic: "Contribution list (5 items)"
57	        word_budget: 300
58	        contributions:
59	          - "Evidence-grounded DocRE task formulation for generative LLMs"
60	          - "Decoupling spectrum: RL optimization pressure correlates with evidence-extraction decoupling (GRPO catastrophic → DPO gradual → RSFT none)"
61	          - "Scale-dependent evidence tax: non-monotonic pattern 1.7B→4B→8B overturns 'evidence always hurts'"
62	          - "EDCR dual-layer diagnostic (method-level ρ=-0.965, per-relation independent of evi_f1)"
63	          - "85+ experiments, 4 model scales, 2 families, 2 datasets"
64	    dependencies: [experiments, method]
65	
66	  related_work:
67	    word_budget: 700
68	    structure: three_paragraph_thematic
69	    paragraphs:
70	      - topic: "Document-level RE (encoder + LLM) and evidence in DocRE"
71	        word_budget: 300
72	        key_distinction: "SAIS/DREEAM = evidence retrieval (classification, improves RE via supervision); FREIGE = evidence generation (additional output burden, scale-dependent cost). Must explain why SAIS says evidence helps but we find it can hurt."
73	      - topic: "RL for LLMs and structured prediction"
74	        word_budget: 220
75	        key_distinction: "Recent papers argue RL doesn't cause forgetting. Our decoupling is intra-task multi-objective trade-off, not inter-task forgetting. Cite QuRL for QLoRA amplification support."
76	      - topic: "Self-training and rejection sampling"
77	        word_budget: 180
78	        key_message: "RSFT = STaR single-round variant + NLI quality filter. Innovation in application, not framework."
79	    dependencies: [introduction]
80	
81	  method:
82	    word_budget: 1300
83	    subsections:
84	      - title: "Task: Evidence-Grounded DocRE"
85	        word_budget: 200
86	        key_message: "Formal definition. Joint generation of (e_h, r, e_t) + evidence sentences E."
87	      - title: "Supervised Fine-Tuning Baseline"
88	        word_budget: 150
89	        key_message: "LoRA SFT with structured output. SFT no-evidence ablation = upper bound."
90	      - title: "Optimization Paradigms"
91	        word_budget: 350
92	        sub_items:
93	          - "GRPO: online RL with evidence quality reward. QLoRA and bf16 variants."
94	          - "DPO: offline preference pairs from evidence quality rankings."
95	          - "RSFT: offline RL via rejection sampling + quality scoring. Single-round STaR variant."
96	      - title: "Contrastive Evidence Discrimination (CED)"
97	        word_budget: 350
98	        key_message: "NLI-based scoring with document-internal hard negatives. Positive evidence vs entity-sharing distractors. Used for RSFT scoring. CED ≈ flat-NLI statistically (p=0.44), but CED provides interpretable per-triple diagnostics."
99	      - title: "Evidence-Decoupling Ratio (EDCR)"
100	        word_budget: 250
101	        key_message: "Diagnostic metric. Two levels: method-level (decoupling proxy, ρ=-0.965 with rel_f1) and per-relation (difficulty diagnosis, independent of evi_f1)."
102	    dependencies: []
103	
104	  experiments:
105	    word_budget: 2200
106	    subsections:
107	      - title: "Setup"
108	        word_budget: 300
109	        must_clarify:
110	          - "Evi-F1 two versions: TP-only (conditional) vs joint (DREEAM protocol)"
111	          - "All metrics from dev set unless noted; test submission pending"
112	      - title: "Main Results"
113	        word_budget: 350
114	        table: tab_main
115	        claims: [C1]
116	      - title: "Evidence-Extraction Decoupling Spectrum"
117	        word_budget: 400
118	        table: tab_spectrum
119	        figure: fig_spectrum
120	        claims: [C2]
121	      - title: "Scale-Dependent Evidence Tax"
122	        word_budget: 400
123	        table: tab_scaling
124	        figure: fig_scaling
125	        claims: [C5]
126	      - title: "Evidence Strategy Spectrum"
127	        word_budget: 350
128	        table: tab_evidence_strategy
129	        claims: [C1]
130	      - title: "Generalization"
131	        word_budget: 400
132	        claims: [C1, C5]
133	        content: "Cross-family (LLaMA-8B) + cross-dataset (Re-DocRED) + DREEAM protocol comparison"
134	    dependencies: [method]
135	
136	  analysis:
137	    word_budget: 600
138	    paragraphs:
139	      - topic: "EDCR dual-layer diagnostic"
140	        word_budget: 200
141	        claims: [C4]
142	      - topic: "Why RSFT avoids decoupling (selection vs optimization)"
143	        word_budget: 150
144	      - topic: "NLI scoring: CED ≈ flat-NLI (p=0.44), top-k=1 > k=3"
145	        word_budget: 150
146	        claims: [C3]
147	      - topic: "Evaluation caveat (exact match underestimates generative RE)"
148	        word_budget: 100
149	    dependencies: [experiments]
150	
151	  conclusion:
152	    word_budget: 250
153	    dependencies: [introduction, experiments, analysis]
154	
155	  limitations:
156	    word_budget: 200
157	    items:
158	      - "Dev-set primary evaluation (CodaLab test submission pending)"
159	      - "Exact-match F1 underestimates generative RE (GenRES)"
160	      - "EDCR human validation limited to 100 samples"
161	      - "Single RL algorithm per family (GRPO online, DPO offline)"
162	    dependencies: [experiments]
163	
164	  appendix:
165	    sections:
166	      - title: "Training Hyperparameters"
167	        table: tab_hyperparams
168	      - title: "Full Ablation Results"
169	        table: tab_ablation_full
170	      - title: "Cross-Validation Details"
171	        table: tab_cross_detail
172	      - title: "DREEAM Protocol Comparison"
173	        table: tab_dreeam_protocol
174	      - title: "Per-Relation EDCR Analysis"
175	        figure: fig_edcr_relations
176	      - title: "GRPO Training Dynamics"
177	        figure: fig_grpo_dynamics
178	
179	# ============================================================
180	# VISUALIZATION PLAN
181	# ============================================================
182	visualization_plan:
183	  - fig_id: fig_overview
184	    type: conceptual
185	    tool: matplotlib
186	    description: >
187	      Two-panel figure. Left: Evidence-grounded DocRE task illustration.
188	      Input document with highlighted entities → model → output with relation
189	      triples AND supporting evidence sentences (contrasted with standard DocRE
190	      that outputs triples only). Right: FREIGE pipeline overview showing
191	      SFT → candidate generation (N=8) → CED/NLI scoring → top-k selection →
192	      RSFT fine-tuning. Clean minimal design, no decorative elements.
193	    placement: "method"
194	    aspect_ratio: "2:1"
195	    data_source: "conceptual"
196	    priority: high
197	
198	  - fig_id: fig_spectrum
199	    type: statistical
200	    tool: matplotlib
201	    description: >
202	      Decoupling spectrum scatter plot. X-axis: Evi-F1 (evidence quality),
203	      Y-axis: Rel-F1 (extraction performance). Points for each method/config:
204	      SFT baseline (gray circle), RSFT CED best (green star), GRPO QLoRA
205	      (red X, bottom-right corner), GRPO bf16 (orange triangle, slight down
206	      from SFT), DPO 1ep and 3ep (orange squares, showing drift), SFT
207	      no-evidence (blue diamond, top with no evi_f1). Color by paradigm family.
208	      Annotate diagonal arrow labeled 'decoupling direction'. Include SFT
209	      no-evidence as reference point (high rel_f1, no evidence).
210	    placement: "experiments"
211	    aspect_ratio: "1:1"
212	    data_source: >
213	      registry: reeval_sft_baseline_d076, eval_rsft_ced_s43,
214	      mvp2_eval_lr5e6_r1_ckpt100, plan_011_grpo_g8_bf16_eval,
215	      eval_plan_012_dpo_1ep_fixed_r2, plan_012_dpo_ced,
216	      eval_plan_014_no_evidence_r2
217	    priority: high
218	
219	  - fig_id: fig_scaling
220	    type: statistical
221	    tool: matplotlib
222	    description: >
223	      Evidence tax bar chart. X-axis: model (Qwen3-1.7B, Qwen3-4B, Qwen3-8B,
224	      LLaMA-3.1-8B). Y-axis: Evidence Tax (Δ Ign-F1 between SFT-with-evidence
225	      and SFT-no-evidence). Bars colored green (positive=benefit), red
226	      (negative=cost), gray (near-zero). Horizontal dashed line at y=0.
227	      Annotate each bar with its value. Sub-bars or outlined overlay for RSFT
228	      evidence tax (RSFT minus no-evidence) to show RSFT recovery effect.
229	    placement: "experiments"
230	    aspect_ratio: "4:3"
231	    data_source: >
232	      registry: plan_006_qwen3_1_7b_sft_eval,
233	      plan_006_qwen3_1_7b_no_evidence_eval_v3, reeval_sft_baseline_d076,
234	      eval_plan_014_no_evidence_r2, plan_006_qwen3_8b_sft_eval,
235	      plan_016_llama_3_1_8b_sft_eval, plan_016_llama_3_1_8b_no_evidence_eval
236	    priority: high
237	    notes: >
238	      paper_framing.md reports 1.7B=+6.2pp from D083 fair subset analysis.
239	      Worker must verify exact numbers from registry; if full dev set differs
240	      from D083, use fair subset and note in caption.
241	
242	  - fig_id: fig_edcr_relations
243	    type: statistical
244	    tool: matplotlib
245	    description: >
246	      Per-relation EDCR scatter plot (appendix). X-axis: per-relation Evi-F1,
247	      Y-axis: per-relation EDCR. 76 relation types as points colored by
248	      rel_f1 quartile. Annotate extreme cases (date_of_birth, head_of_government).
249	      Shows independence (ρ=-0.064, p=0.58).
250	    placement: "appendix"
251	    aspect_ratio: "1:1"
252	    data_source: "D070 per-relation analysis data"
253	    priority: medium
254	
255	  - fig_id: fig_grpo_dynamics
256	    type: statistical
257	    tool: matplotlib
258	    description: >
259	      GRPO training dynamics (appendix). X-axis: training steps (0-100).
260	      Two Y-axes: left=Rel-F1, right=Evi-F1. Lines for QLoRA (catastrophic
261	      trajectory) and bf16 (mild trajectory). Shows divergence point.
262	    placement: "appendix"
263	    aspect_ratio: "3:2"
264	    data_source: >
265	      registry: mvp2_eval_lr5e6_r1_ckpt20 through ckpt100,
266	      mvp2_eval_ced_kl001_r4 checkpoints, plan_011 checkpoints
267	    priority: medium
268	
269	# ============================================================
270	# TABLE PLAN
271	# ============================================================
272	table_plan:
273	  # --- Main text tables ---
274	  - table_id: tab_main
275	    type: comparison
276	    placement: "experiments §main_results"
277	    columns: [Method, Ign-F1, Evi-F1, EDCR, "Δ vs SFT"]
278	    rows:
279	      - "SFT baseline"
280	      - "SFT no-evidence"
281	      - "RSFT CED (mean ± std across 4 seeds)"
282	      - "CED reranker (inference-time, no training)"
283	    data_source:
284	      - "reeval_sft_baseline_d076"
285	      - "eval_plan_014_no_evidence_r2"
286	      - "reeval_ced_s42, reeval_ced_s44, eval_rsft_ced_s43, eval_rsft_ced_s45"
287	    notes: >
288	      Ign-F1 as primary metric (ignores training triples).
289	      Evi-F1 = TP-only conditional. Bold best evidence-grounded.
290	
291	  - table_id: tab_spectrum
292	    type: comparison
293	    placement: "experiments §decoupling"
294	    columns: [Paradigm, Config, Rel-F1, Evi-F1, EDCR, Severity]
295	    rows:
296	      - "GRPO + QLoRA (G=4)"
297	      - "GRPO + bf16 (G=8, best step)"
298	      - "DPO bf16 1ep"
299	      - "DPO bf16 3ep"
300	      - "SFT baseline"
301	      - "RSFT CED (mean)"
302	    data_source:
303	      - "mvp2_eval_lr5e6_r1_ckpt100"
304	      - "plan_011_grpo_g8_bf16_eval"
305	      - "eval_plan_012_dpo_1ep_fixed_r2"
306	      - "plan_012_dpo_ced"
307	      - "reeval_sft_baseline_d076"
308	      - "reeval_ced_s42, reeval_ced_s44"
309	    notes: >
310	      Order by decoupling severity (catastrophic → mild → gradual → none).
311	      Severity label column aids readability. GRPO QLoRA rel_f1=0.014 is the
312	      anchor for 'catastrophic'.
313	
314	  - table_id: tab_scaling
315	    type: comparison
316	    placement: "experiments §scaling"
317	    columns: [Model, "SFT (w/ evi)", "No-Evidence", RSFT, "Evi Tax", "RSFT Gain"]
318	    rows:
319	      - "Qwen3-1.7B"
320	      - "Qwen3-4B"
321	      - "Qwen3-8B (eval running → TBD placeholder)"
322	      - "LLaMA-3.1-8B"
323	    data_source:
324	      - "plan_006_qwen3_1_7b_sft_eval, plan_006_qwen3_1_7b_no_evidence_eval_v3"
325	      - "reeval_sft_baseline_d076, eval_plan_014_no_evidence_r2"
326	      - "plan_006_qwen3_8b_sft_eval (no-evi TBD)"
327	      - "plan_016_llama_3_1_8b_sft_eval, plan_016_llama_3_1_8b_no_evidence_eval"
328	    notes: >
329	      Evidence Tax = SFT(evi) - No-Evidence. 8B eval still running; use
330	      placeholder or latest available. Cross-family row (LLaMA) confirms
331	      8B pattern.
332	
333	  - table_id: tab_evidence_strategy
334	    type: comparison
335	    placement: "experiments §evidence_strategy"
336	    columns: [Strategy, Method, Rel-F1, "Evi-F1 (joint)", EDCR]
337	    rows:
338	      - "Joint gen: RSFT CED (best)"
339	      - "Joint gen: SFT baseline"
340	      - "Post-hoc: BM25 entity k=2"
341	      - "Post-hoc filter: CED sentence-level"
342	      - "Gen + rerank: CED reranker"
343	    data_source:
344	      - "eval_rsft_ced_s43 (evi_f1_joint)"
345	      - "reeval_sft_baseline_d076 (evi_f1_joint)"
346	      - "post_hoc_bm25_baseline"
347	      - "lead1_ced_evidence_filter"
348	    notes: >
349	      Must use evi_f1_joint for fair cross-strategy comparison.
350	      Sentence-level CED filter is a negative result (D090).
351	      EDCR gap (0.654 vs 0.766) shows faithfulness advantage of joint gen.
352	
353	  # --- Appendix tables ---
354	  - table_id: tab_ablation_full
355	    type: ablation
356	    placement: appendix
357	    columns: [Scoring, Seed, Ign-F1, Rel-F1, Evi-F1, EDCR]
358	    rows: "All CED seeds + flat-NLI seeds + top-k=3 + paired t-test"
359	    data_source: "all reeval_ced_*, eval_rsft_ced_*, reeval_flat_nli_*, eval_flat_nli_*, reeval_rsft_topk3"
360	
361	  - table_id: tab_cross_detail
362	    type: comparison
363	    placement: appendix
364	    columns: [Model/Dataset, Config, Ign-F1, Evi-F1, EDCR, "Δ SFT"]
365	    rows: "Re-DocRED SFT + RSFT, LLaMA SFT + RSFT + no-evi + GRPO QLoRA"
366	    data_source: "plan_007_*, plan_016_*, plan_006_llama_*"
367	
368	  - table_id: tab_dreeam_protocol
369	    type: comparison
370	    placement: appendix
371	    columns: [Method, Type, "Evi-P (sent)", "Evi-R (sent)", "Evi-F1 (sent)"]
372	    rows: "DREEAM (from paper), SAIS (from paper), FREIGE SFT, FREIGE RSFT CED"
373	    data_source: "D093 analysis + DREEAM/SAIS paper numbers"
374	    notes: "TP-only evi_f1 vs joint clearly labeled. Gap mainly from RE, not evidence."
375	
376	  - table_id: tab_hyperparams
377	    type: reference
378	    placement: appendix
379	    columns: [Parameter, SFT, RSFT, GRPO, DPO]
380	    rows: "lr, epochs, LoRA r/alpha, batch, max_tokens, N, k, G, KL coeff, etc."
381	
382	# ============================================================
383	# LITERATURE STRATEGY
384	# ============================================================
385	literature_strategy:
386	  macro_context: >
387	    LLM-based IE is advancing rapidly, but no generative method produces
388	    verifiable evidence alongside extracted relations. This paper fills
389	    the gap by proposing evidence-grounded DocRE, systematically studying
390	    the cost of faithfulness across training paradigms and model scales.
391	  citation_budget: 40-50
392	  micro_clusters:
393	    - cluster_name: docre_methods
394	      description: "Document-level RE: encoder-based + LLM-based methods"
395	      target_count: 10
396	      must_cite:
397	        - "DocRED (Yao et al. 2019)"
398	        - "Re-DocRED (Tan et al. 2022)"
399	        - "ATLOP (Zhou et al. 2021)"
400	        - "LMRC (Li et al. 2023)"
401	        - "DocKS-RAG (Xu et al. 2024)"
402	        - "GenRES"
403	      search_queries:
404	        - "document-level relation extraction LLM 2024 2025"
405	        - "generative relation extraction evaluation"
406	
407	    - cluster_name: evidence_docre
408	      description: "Evidence retrieval/supervision in DocRE"
409	      target_count: 6
410	      must_cite:
411	        - "DREEAM (Ma et al. 2023)"
412	        - "SAIS (Xiao et al. 2022)"
413	      search_queries:
414	        - "evidence retrieval document relation extraction DREEAM SAIS"
415	        - "supporting evidence sentence information extraction"
416	
417	    - cluster_name: rl_alignment
418	      description: "RL for LLMs: GRPO, DPO, RL for structured prediction"
419	      target_count: 8
420	      must_cite:
421	        - "GRPO / DeepSeekMath (Shao et al. 2024)"
422	        - "DPO (Rafailov et al. 2024)"
423	        - "Gao et al. 2023 (reward overoptimization)"
424	      search_queries:
425	        - "GRPO group relative policy optimization structured"
426	        - "DPO direct preference optimization"
427	        - "RL for information extraction 2024 2025"
428	
429	    - cluster_name: self_training_rsft
430	      description: "Self-training, rejection sampling, STaR"
431	      target_count: 5
432	      must_cite:
433	        - "STaR (Zelikman et al. 2022)"
434	      search_queries:
435	        - "STaR self-taught reasoner rejection sampling"
436	        - "ReST reinforced self-training language model"
437	
438	    - cluster_name: quantization_rl
439	      description: "Quantization effects on RL, QLoRA artifacts"
440	      target_count: 4
441	      must_cite:
442	        - "QuRL (Ahmadian et al. 2024)"
443	        - "QaRL"
444	      search_queries:
445	        - "QuRL quantized reinforcement learning language model"
446	        - "QLoRA artifacts RL fine-tuning stability"
447	
448	    - cluster_name: rl_forgetting
449	      description: "RL and catastrophic forgetting (to position intra-task vs inter-task)"
450	      target_count: 4
451	      must_cite: []
452	      search_queries:
453	        - "reinforcement learning catastrophic forgetting language model 2024 2025"
454	        - "RL fine-tuning preserves pretrained knowledge"
455	        - "alignment tax knowledge retention"
456	
457	# ============================================================
458	# WRITING ORDER
459	# ============================================================
460	writing_order:
461	  - section: experiments
462	    rationale: "Grounds narrative in real registry data. All claims must have evidence."
463	  - section: method
464	    rationale: "Explains how we got the results. References experiment findings."
465	  - section: introduction
466	    rationale: "Full story is now clear: what we found and why it matters."
467	  - section: related_work
468	    rationale: "Positioning requires knowing our results and contributions."
469	  - section: conclusion
470	    rationale: "Summarize established narrative."
471	  - section: limitations
472	    rationale: "Honest assessment based on complete picture."
473	  - section: abstract
474	    rationale: "Compress complete story into 220 words. Written last."
475	  - section: appendix
476	    rationale: "Supporting details that didn't fit in main text."
477	
478	# ============================================================
479	# PAPER FILE STRUCTURE
480	# ============================================================
481	file_structure:
482	  paper_dir: "projects/faith-evidence-ie/docs/paper/"
483	  main_tex: "main.tex"
484	  sections:
485	    - "sections/abstract.tex"
486	    - "sections/introduction.tex"
487	    - "sections/related_work.tex"
488	    - "sections/method.tex"
489	    - "sections/experiments.tex"
490	    - "sections/analysis.tex"
491	    - "sections/conclusion.tex"
492	    - "sections/limitations.tex"
493	    - "sections/appendix.tex"
494	  bib: "references.bib"
495	  figures_dir: "projects/faith-evidence-ie/figures/paper/"
496	  template_dir: "acl-style/"
497	
498	# ============================================================
499	# CLAIMS REGISTRY MAP (for provenance)
500	# ============================================================
501	claims_registry_map:
502	  C1_rsft_works:
503	    claim: "RSFT CED consistently outperforms SFT (+3.8-6.0pp Ign-F1)"
504	    evidence:
505	      - exp: reeval_ced_s42
506	        metric: ign_f1
507	        value: 0.4423
508	      - exp: reeval_ced_s44
509	        metric: ign_f1
510	        value: 0.4511
511	      - exp: eval_rsft_ced_s43
512	        metric: ign_f1
513	        value: 0.4512
514	      - exp: eval_rsft_ced_s45
515	        metric: ign_f1
516	        value: 0.4416
517	      - exp: reeval_sft_baseline_d076
518	        metric: ign_f1
519	        value: 0.3974
520	
521	  C2_decoupling_spectrum:
522	    claim: "RL optimization pressure correlates with decoupling severity"
523	    evidence:
524	      - exp: mvp2_eval_lr5e6_r1_ckpt100
525	        metric: rel_f1
526	        value: 0.0138
527	        label: "GRPO QLoRA catastrophic"
528	      - exp: plan_011_grpo_g8_bf16_eval
529	        metric: rel_f1
530	        value: 0.4549
531	        label: "GRPO bf16 mild (-2pp from SFT 0.4549 initial)"
532	      - exp: eval_plan_012_dpo_1ep_fixed_r2
533	        metric: rel_f1
534	        value: 0.4034
535	        label: "DPO 1ep gradual"
536	      - exp: plan_012_dpo_ced
537	        metric: rel_f1
538	        value: 0.3429
539	        label: "DPO 3ep further decay"
540	
541	  C3_ced_vs_flat_nli:
542	    claim: "CED and flat-NLI statistically indistinguishable (p=0.44)"
543	    evidence:
544	      - source: "D078 paired t-test"
545	      - ced_mean_rel_f1: 0.4569
546	      - flat_nli_mean_rel_f1: 0.4561
547	      - delta: 0.0008
548	
549	  C4_edcr_diagnostic:
550	    claim: "EDCR provides dual-layer diagnostic value"
551	    evidence:
552	      - source: "D070 per-relation analysis"
553	      - method_level_rho: -0.965
554	      - per_relation_rho_edcr_evif1: -0.064
555	      - per_relation_p: 0.58
556	
557	  C5_scaling:
558	    claim: "Evidence tax is scale-dependent and non-monotonic"
559	    evidence:
560	      - model: "Qwen3-1.7B"
561	        source: "D079/D083"
562	        tax: "+6.2pp benefit"
563	      - model: "Qwen3-4B"
564	        source: "registry"
565	        tax: "-7.5pp cost"
566	      - model: "Qwen3-8B"
567	        source: "D088 (eval running)"
568	        tax: "≈0"
569	      - model: "LLaMA-3.1-8B"
570	        source: "D082"
571	        tax: "-0.7pp near-neutral"
572	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "e05aa7ea-c4b5-4225-acac-06bdffdfcb70",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/writing_plan.yaml",
      "content": "meta:\n  venue: emnlp-2026\n  submission_type: long\n  review_system: arr_july\n  deadline: \"2026-07-15\"\n  template:\n    source: \"github.com/acl-org/acl-style-files (official)\"\n    local_path: \"projects/faith-evidence-ie/docs/paper/acl-style/\"\n    documentclass: \"\\\\documentclass[11pt]{article}\"\n    options: \"\\\\usepackage[review]{acl}\"\n    template_note: \"Official ACL style files cloned 2026-05-17. EMNLP uses identical template.\"\n  page_limits:\n    main_text: 8\n    references: unlimited\n    appendix: unlimited\n  title_candidates:\n    - \"Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\"\n    - \"The Cost of Faithfulness: Evidence-Extraction Trade-offs in Generative Document Relation Extraction\"\n    - \"FREIGE: Faithful Evidence-Grounded Document-Level Relation Extraction via Rejection Sampling Fine-Tuning\"\n  preferred_title: 1\n  visualization:\n    preferred_tool: matplotlib\n\n# ============================================================\n# PAPER OUTLINE\n# ============================================================\npaper_outline:\n  abstract:\n    word_budget: 220\n    key_message: >\n      Evidence-grounded DocRE 新任务；系统比较 GRPO/DPO/RSFT 三范式；\n      发现 decoupling spectrum（RL pressure 与 decoupling severity 正相关）；\n      evidence tax 是 scale-dependent 的（1.7B +6.2pp benefit, 4B -7.0pp cost, 8B ≈0）；\n      RSFT+NLI scoring 是唯一有效路线；EDCR 双层诊断\n    must_include:\n      - task definition (evidence-grounded DocRE, generative LLM qualifier)\n      - three paradigms compared\n      - decoupling spectrum core finding\n      - scale-dependent evidence tax with concrete numbers\n      - RSFT effectiveness delta vs SFT\n      - EDCR diagnostic mention\n    dependencies: [introduction, experiments, method]\n\n  introduction:\n    word_budget: 1200\n    structure: five_paragraph\n    paragraphs:\n      - topic: \"LLM DocRE progress but no evidence\"\n        word_budget: 200\n      - topic: \"Why verifiable evidence matters for deployment\"\n        word_budget: 150\n      - topic: \"Encoder retrieval ≠ generative production (SAIS/DREEAM distinction)\"\n        word_budget: 200\n      - topic: \"Our insight: 3 paradigms → decoupling spectrum + scale-dependent tax + RSFT solution\"\n        word_budget: 350\n      - topic: \"Contribution list (5 items)\"\n        word_budget: 300\n        contributions:\n          - \"Evidence-grounded DocRE task formulation for generative LLMs\"\n          - \"Decoupling spectrum: RL optimization pressure correlates with evidence-extraction decoupling (GRPO catastrophic → DPO gradual → RSFT none)\"\n          - \"Scale-dependent evidence tax: non-monotonic pattern 1.7B→4B→8B overturns 'evidence always hurts'\"\n          - \"EDCR dual-layer diagnostic (method-level ρ=-0.965, per-relation independent of evi_f1)\"\n          - \"85+ experiments, 4 model scales, 2 families, 2 datasets\"\n    dependencies: [experiments, method]\n\n  related_work:\n    word_budget: 700\n    structure: three_paragraph_thematic\n    paragraphs:\n      - topic: \"Document-level RE (encoder + LLM) and evidence in DocRE\"\n        word_budget: 300\n        key_distinction: \"SAIS/DREEAM = evidence retrieval (classification, improves RE via supervision); FREIGE = evidence generation (additional output burden, scale-dependent cost). Must explain why SAIS says evidence helps but we find it can hurt.\"\n      - topic: \"RL for LLMs and structured prediction\"\n        word_budget: 220\n        key_distinction: \"Recent papers argue RL doesn't cause forgetting. Our decoupling is intra-task multi-objective trade-off, not inter-task forgetting. Cite QuRL for QLoRA amplification support.\"\n      - topic: \"Self-training and rejection sampling\"\n        word_budget: 180\n        key_message: \"RSFT = STaR single-round variant + NLI quality filter. Innovation in application, not framework.\"\n    dependencies: [introduction]\n\n  method:\n    word_budget: 1300\n    subsections:\n      - title: \"Task: Evidence-Grounded DocRE\"\n        word_budget: 200\n        key_message: \"Formal definition. Joint generation of (e_h, r, e_t) + evidence sentences E.\"\n      - title: \"Supervised Fine-Tuning Baseline\"\n        word_budget: 150\n        key_message: \"LoRA SFT with structured output. SFT no-evidence ablation = upper bound.\"\n      - title: \"Optimization Paradigms\"\n        word_budget: 350\n        sub_items:\n          - \"GRPO: online RL with evidence quality reward. QLoRA and bf16 variants.\"\n          - \"DPO: offline preference pairs from evidence quality rankings.\"\n          - \"RSFT: offline RL via rejection sampling + quality scoring. Single-round STaR variant.\"\n      - title: \"Contrastive Evidence Discrimination (CED)\"\n        word_budget: 350\n        key_message: \"NLI-based scoring with document-internal hard negatives. Positive evidence vs entity-sharing distractors. Used for RSFT scoring. CED ≈ flat-NLI statistically (p=0.44), but CED provides interpretable per-triple diagnostics.\"\n      - title: \"Evidence-Decoupling Ratio (EDCR)\"\n        word_budget: 250\n        key_message: \"Diagnostic metric. Two levels: method-level (decoupling proxy, ρ=-0.965 with rel_f1) and per-relation (difficulty diagnosis, independent of evi_f1).\"\n    dependencies: []\n\n  experiments:\n    word_budget: 2200\n    subsections:\n      - title: \"Setup\"\n        word_budget: 300\n        must_clarify:\n          - \"Evi-F1 two versions: TP-only (conditional) vs joint (DREEAM protocol)\"\n          - \"All metrics from dev set unless noted; test submission pending\"\n      - title: \"Main Results\"\n        word_budget: 350\n        table: tab_main\n        claims: [C1]\n      - title: \"Evidence-Extraction Decoupling Spectrum\"\n        word_budget: 400\n        table: tab_spectrum\n        figure: fig_spectrum\n        claims: [C2]\n      - title: \"Scale-Dependent Evidence Tax\"\n        word_budget: 400\n        table: tab_scaling\n        figure: fig_scaling\n        claims: [C5]\n      - title: \"Evidence Strategy Spectrum\"\n        word_budget: 350\n        table: tab_evidence_strategy\n        claims: [C1]\n      - title: \"Generalization\"\n        word_budget: 400\n        claims: [C1, C5]\n        content: \"Cross-family (LLaMA-8B) + cross-dataset (Re-DocRED) + DREEAM protocol comparison\"\n    dependencies: [method]\n\n  analysis:\n    word_budget: 600\n    paragraphs:\n      - topic: \"EDCR dual-layer diagnostic\"\n        word_budget: 200\n        claims: [C4]\n      - topic: \"Why RSFT avoids decoupling (selection vs optimization)\"\n        word_budget: 150\n      - topic: \"NLI scoring: CED ≈ flat-NLI (p=0.44), top-k=1 > k=3\"\n        word_budget: 150\n        claims: [C3]\n      - topic: \"Evaluation caveat (exact match underestimates generative RE)\"\n        word_budget: 100\n    dependencies: [experiments]\n\n  conclusion:\n    word_budget: 250\n    dependencies: [introduction, experiments, analysis]\n\n  limitations:\n    word_budget: 200\n    items:\n      - \"Dev-set primary evaluation (CodaLab test submission pending)\"\n      - \"Exact-match F1 underestimates generative RE (GenRES)\"\n      - \"EDCR human validation limited to 100 samples\"\n      - \"Single RL algorithm per family (GRPO online, DPO offline)\"\n    dependencies: [experiments]\n\n  appendix:\n    sections:\n      - title: \"Training Hyperparameters\"\n        table: tab_hyperparams\n      - title: \"Full Ablation Results\"\n        table: tab_ablation_full\n      - title: \"Cross-Validation Details\"\n        table: tab_cross_detail\n      - title: \"DREEAM Protocol Comparison\"\n        table: tab_dreeam_protocol\n      - title: \"Per-Relation EDCR Analysis\"\n        figure: fig_edcr_relations\n      - title: \"GRPO Training Dynamics\"\n        figure: fig_grpo_dynamics\n\n# ============================================================\n# VISUALIZATION PLAN\n# ============================================================\nvisualization_plan:\n  - fig_id: fig_overview\n    type: conceptual\n    tool: matplotlib\n    description: >\n      Two-panel figure. Left: Evidence-grounded DocRE task illustration.\n      Input document with highlighted entities → model → output with relation\n      triples AND supporting evidence sentences (contrasted with standard DocRE\n      that outputs triples only). Right: FREIGE pipeline overview showing\n      SFT → candidate generation (N=8) → CED/NLI scoring → top-k selection →\n      RSFT fine-tuning. Clean minimal design, no decorative elements.\n    placement: \"method\"\n    aspect_ratio: \"2:1\"\n    data_source: \"conceptual\"\n    priority: high\n\n  - fig_id: fig_spectrum\n    type: statistical\n    tool: matplotlib\n    description: >\n      Decoupling spectrum scatter plot. X-axis: Evi-F1 (evidence quality),\n      Y-axis: Rel-F1 (extraction performance). Points for each method/config:\n      SFT baseline (gray circle), RSFT CED best (green star), GRPO QLoRA\n      (red X, bottom-right corner), GRPO bf16 (orange triangle, slight down\n      from SFT), DPO 1ep and 3ep (orange squares, showing drift), SFT\n      no-evidence (blue diamond, top with no evi_f1). Color by paradigm family.\n      Annotate diagonal arrow labeled 'decoupling direction'. Include SFT\n      no-evidence as reference point (high rel_f1, no evidence).\n    placement: \"experiments\"\n    aspect_ratio: \"1:1\"\n    data_source: >\n      registry: reeval_sft_baseline_d076, eval_rsft_ced_s43,\n      mvp2_eval_lr5e6_r1_ckpt100, plan_011_grpo_g8_bf16_eval,\n      eval_plan_012_dpo_1ep_fixed_r2, plan_012_dpo_ced,\n      eval_plan_014_no_evidence_r2\n    priority: high\n\n  - fig_id: fig_scaling\n    type: statistical\n    tool: matplotlib\n    description: >\n      Evidence tax bar chart. X-axis: model (Qwen3-1.7B, Qwen3-4B, Qwen3-8B,\n      LLaMA-3.1-8B). Y-axis: Evidence Tax (Δ Ign-F1 between SFT-with-evidence\n      and SFT-no-evidence). Bars colored green (positive=benefit), red\n      (negative=cost), gray (near-zero). Horizontal dashed line at y=0.\n      Annotate each bar with its value. Sub-bars or outlined overlay for RSFT\n      evidence tax (RSFT minus no-evidence) to show RSFT recovery effect.\n    placement: \"experiments\"\n    aspect_ratio: \"4:3\"\n    data_source: >\n      registry: plan_006_qwen3_1_7b_sft_eval,\n      plan_006_qwen3_1_7b_no_evidence_eval_v3, reeval_sft_baseline_d076,\n      eval_plan_014_no_evidence_r2, plan_006_qwen3_8b_sft_eval,\n      plan_016_llama_3_1_8b_sft_eval, plan_016_llama_3_1_8b_no_evidence_eval\n    priority: high\n    notes: >\n      paper_framing.md reports 1.7B=+6.2pp from D083 fair subset analysis.\n      Worker must verify exact numbers from registry; if full dev set differs\n      from D083, use fair subset and note in caption.\n\n  - fig_id: fig_edcr_relations\n    type: statistical\n    tool: matplotlib\n    description: >\n      Per-relation EDCR scatter plot (appendix). X-axis: per-relation Evi-F1,\n      Y-axis: per-relation EDCR. 76 relation types as points colored by\n      rel_f1 quartile. Annotate extreme cases (date_of_birth, head_of_government).\n      Shows independence (ρ=-0.064, p=0.58).\n    placement: \"appendix\"\n    aspect_ratio: \"1:1\"\n    data_source: \"D070 per-relation analysis data\"\n    priority: medium\n\n  - fig_id: fig_grpo_dynamics\n    type: statistical\n    tool: matplotlib\n    description: >\n      GRPO training dynamics (appendix). X-axis: training steps (0-100).\n      Two Y-axes: left=Rel-F1, right=Evi-F1. Lines for QLoRA (catastrophic\n      trajectory) and bf16 (mild trajectory). Shows divergence point.\n    placement: \"appendix\"\n    aspect_ratio: \"3:2\"\n    data_source: >\n      registry: mvp2_eval_lr5e6_r1_ckpt20 through ckpt100,\n      mvp2_eval_ced_kl001_r4 checkpoints, plan_011 checkpoints\n    priority: medium\n\n# ============================================================\n# TABLE PLAN\n# ============================================================\ntable_plan:\n  # --- Main text tables ---\n  - table_id: tab_main\n    type: comparison\n    placement: \"experiments §main_results\"\n    columns: [Method, Ign-F1, Evi-F1, EDCR, \"Δ vs SFT\"]\n    rows:\n      - \"SFT baseline\"\n      - \"SFT no-evidence\"\n      - \"RSFT CED (mean ± std across 4 seeds)\"\n      - \"CED reranker (inference-time, no training)\"\n    data_source:\n      - \"reeval_sft_baseline_d076\"\n      - \"eval_plan_014_no_evidence_r2\"\n      - \"reeval_ced_s42, reeval_ced_s44, eval_rsft_ced_s43, eval_rsft_ced_s45\"\n    notes: >\n      Ign-F1 as primary metric (ignores training triples).\n      Evi-F1 = TP-only conditional. Bold best evidence-grounded.\n\n  - table_id: tab_spectrum\n    type: comparison\n    placement: \"experiments §decoupling\"\n    columns: [Paradigm, Config, Rel-F1, Evi-F1, EDCR, Severity]\n    rows:\n      - \"GRPO + QLoRA (G=4)\"\n      - \"GRPO + bf16 (G=8, best step)\"\n      - \"DPO bf16 1ep\"\n      - \"DPO bf16 3ep\"\n      - \"SFT baseline\"\n      - \"RSFT CED (mean)\"\n    data_source:\n      - \"mvp2_eval_lr5e6_r1_ckpt100\"\n      - \"plan_011_grpo_g8_bf16_eval\"\n      - \"eval_plan_012_dpo_1ep_fixed_r2\"\n      - \"plan_012_dpo_ced\"\n      - \"reeval_sft_baseline_d076\"\n      - \"reeval_ced_s42, reeval_ced_s44\"\n    notes: >\n      Order by decoupling severity (catastrophic → mild → gradual → none).\n      Severity label column aids readability. GRPO QLoRA rel_f1=0.014 is the\n      anchor for 'catastrophic'.\n\n  - table_id: tab_scaling\n    type: comparison\n    placement: \"experiments §scaling\"\n    columns: [Model, \"SFT (w/ evi)\", \"No-Evidence\", RSFT, \"Evi Tax\", \"RSFT Gain\"]\n    rows:\n      - \"Qwen3-1.7B\"\n      - \"Qwen3-4B\"\n      - \"Qwen3-8B (eval running → TBD placeholder)\"\n      - \"LLaMA-3.1-8B\"\n    data_source:\n      - \"plan_006_qwen3_1_7b_sft_eval, plan_006_qwen3_1_7b_no_evidence_eval_v3\"\n      - \"reeval_sft_baseline_d076, eval_plan_014_no_evidence_r2\"\n      - \"plan_006_qwen3_8b_sft_eval (no-evi TBD)\"\n      - \"plan_016_llama_3_1_8b_sft_eval, plan_016_llama_3_1_8b_no_evidence_eval\"\n    notes: >\n      Evidence Tax = SFT(evi) - No-Evidence. 8B eval still running; use\n      placeholder or latest available. Cross-family row (LLaMA) confirms\n      8B pattern.\n\n  - table_id: tab_evidence_strategy\n    type: comparison\n    placement: \"experiments §evidence_strategy\"\n    columns: [Strategy, Method, Rel-F1, \"Evi-F1 (joint)\", EDCR]\n    rows:\n      - \"Joint gen: RSFT CED (best)\"\n      - \"Joint gen: SFT baseline\"\n      - \"Post-hoc: BM25 entity k=2\"\n      - \"Post-hoc filter: CED sentence-level\"\n      - \"Gen + rerank: CED reranker\"\n    data_source:\n      - \"eval_rsft_ced_s43 (evi_f1_joint)\"\n      - \"reeval_sft_baseline_d076 (evi_f1_joint)\"\n      - \"post_hoc_bm25_baseline\"\n      - \"lead1_ced_evidence_filter\"\n    notes: >\n      Must use evi_f1_joint for fair cross-strategy comparison.\n      Sentence-level CED filter is a negative result (D090).\n      EDCR gap (0.654 vs 0.766) shows faithfulness advantage of joint gen.\n\n  # --- Appendix tables ---\n  - table_id: tab_ablation_full\n    type: ablation\n    placement: appendix\n    columns: [Scoring, Seed, Ign-F1, Rel-F1, Evi-F1, EDCR]\n    rows: \"All CED seeds + flat-NLI seeds + top-k=3 + paired t-test\"\n    data_source: \"all reeval_ced_*, eval_rsft_ced_*, reeval_flat_nli_*, eval_flat_nli_*, reeval_rsft_topk3\"\n\n  - table_id: tab_cross_detail\n    type: comparison\n    placement: appendix\n    columns: [Model/Dataset, Config, Ign-F1, Evi-F1, EDCR, \"Δ SFT\"]\n    rows: \"Re-DocRED SFT + RSFT, LLaMA SFT + RSFT + no-evi + GRPO QLoRA\"\n    data_source: \"plan_007_*, plan_016_*, plan_006_llama_*\"\n\n  - table_id: tab_dreeam_protocol\n    type: comparison\n    placement: appendix\n    columns: [Method, Type, \"Evi-P (sent)\", \"Evi-R (sent)\", \"Evi-F1 (sent)\"]\n    rows: \"DREEAM (from paper), SAIS (from paper), FREIGE SFT, FREIGE RSFT CED\"\n    data_source: \"D093 analysis + DREEAM/SAIS paper numbers\"\n    notes: \"TP-only evi_f1 vs joint clearly labeled. Gap mainly from RE, not evidence.\"\n\n  - table_id: tab_hyperparams\n    type: reference\n    placement: appendix\n    columns: [Parameter, SFT, RSFT, GRPO, DPO]\n    rows: \"lr, epochs, LoRA r/alpha, batch, max_tokens, N, k, G, KL coeff, etc.\"\n\n# ============================================================\n# LITERATURE STRATEGY\n# ============================================================\nliterature_strategy:\n  macro_context: >\n    LLM-based IE is advancing rapidly, but no generative method produces\n    verifiable evidence alongside extracted relations. This paper fills\n    the gap by proposing evidence-grounded DocRE, systematically studying\n    the cost of faithfulness across training paradigms and model scales.\n  citation_budget: 40-50\n  micro_clusters:\n    - cluster_name: docre_methods\n      description: \"Document-level RE: encoder-based + LLM-based methods\"\n      target_count: 10\n      must_cite:\n        - \"DocRED (Yao et al. 2019)\"\n        - \"Re-DocRED (Tan et al. 2022)\"\n        - \"ATLOP (Zhou et al. 2021)\"\n        - \"LMRC (Li et al. 2023)\"\n        - \"DocKS-RAG (Xu et al. 2024)\"\n        - \"GenRES\"\n      search_queries:\n        - \"document-level relation extraction LLM 2024 2025\"\n        - \"generative relation extraction evaluation\"\n\n    - cluster_name: evidence_docre\n      description: \"Evidence retrieval/supervision in DocRE\"\n      target_count: 6\n      must_cite:\n        - \"DREEAM (Ma et al. 2023)\"\n        - \"SAIS (Xiao et al. 2022)\"\n      search_queries:\n        - \"evidence retrieval document relation extraction DREEAM SAIS\"\n        - \"supporting evidence sentence information extraction\"\n\n    - cluster_name: rl_alignment\n      description: \"RL for LLMs: GRPO, DPO, RL for structured prediction\"\n      target_count: 8\n      must_cite:\n        - \"GRPO / DeepSeekMath (Shao et al. 2024)\"\n        - \"DPO (Rafailov et al. 2024)\"\n        - \"Gao et al. 2023 (reward overoptimization)\"\n      search_queries:\n        - \"GRPO group relative policy optimization structured\"\n        - \"DPO direct preference optimization\"\n        - \"RL for information extraction 2024 2025\"\n\n    - cluster_name: self_training_rsft\n      description: \"Self-training, rejection sampling, STaR\"\n      target_count: 5\n      must_cite:\n        - \"STaR (Zelikman et al. 2022)\"\n      search_queries:\n        - \"STaR self-taught reasoner rejection sampling\"\n        - \"ReST reinforced self-training language model\"\n\n    - cluster_name: quantization_rl\n      description: \"Quantization effects on RL, QLoRA artifacts\"\n      target_count: 4\n      must_cite:\n        - \"QuRL (Ahmadian et al. 2024)\"\n        - \"QaRL\"\n      search_queries:\n        - \"QuRL quantized reinforcement learning language model\"\n        - \"QLoRA artifacts RL fine-tuning stability\"\n\n    - cluster_name: rl_forgetting\n      description: \"RL and catastrophic forgetting (to position intra-task vs inter-task)\"\n      target_count: 4\n      must_cite: []\n      search_queries:\n        - \"reinforcement learning catastrophic forgetting language model 2024 2025\"\n        - \"RL fine-tuning preserves pretrained knowledge\"\n        - \"alignment tax knowledge retention\"\n\n# ============================================================\n# WRITING ORDER\n# ============================================================\nwriting_order:\n  - section: experiments\n    rationale: \"Grounds narrative in real registry data. All claims must have evidence.\"\n  - section: method\n    rationale: \"Explains how we got the results. References experiment findings.\"\n  - section: introduction\n    rationale: \"Full story is now clear: what we found and why it matters.\"\n  - section: related_work\n    rationale: \"Positioning requires knowing our results and contributions.\"\n  - section: conclusion\n    rationale: \"Summarize established narrative.\"\n  - section: limitations\n    rationale: \"Honest assessment based on complete picture.\"\n  - section: abstract\n    rationale: \"Compress complete story into 220 words. Written last.\"\n  - section: appendix\n    rationale: \"Supporting details that didn't fit in main text.\"\n\n# ============================================================\n# PAPER FILE STRUCTURE\n# ============================================================\nfile_structure:\n  paper_dir: \"projects/faith-evidence-ie/docs/paper/\"\n  main_tex: \"main.tex\"\n  sections:\n    - \"sections/abstract.tex\"\n    - \"sections/introduction.tex\"\n    - \"sections/related_work.tex\"\n    - \"sections/method.tex\"\n    - \"sections/experiments.tex\"\n    - \"sections/analysis.tex\"\n    - \"sections/conclusion.tex\"\n    - \"sections/limitations.tex\"\n    - \"sections/appendix.tex\"\n  bib: \"references.bib\"\n  figures_dir: \"projects/faith-evidence-ie/figures/paper/\"\n  template_dir: \"acl-style/\"\n\n# ============================================================\n# CLAIMS REGISTRY MAP (for provenance)\n# ============================================================\nclaims_registry_map:\n  C1_rsft_works:\n    claim: \"RSFT CED consistently outperforms SFT (+3.8-6.0pp Ign-F1)\"\n    evidence:\n      - exp: reeval_ced_s42\n        metric: ign_f1\n        value: 0.4423\n      - exp: reeval_ced_s44\n        metric: ign_f1\n        value: 0.4511\n      - exp: eval_rsft_ced_s43\n        metric: ign_f1\n        value: 0.4512\n      - exp: eval_rsft_ced_s45\n        metric: ign_f1\n        value: 0.4416\n      - exp: reeval_sft_baseline_d076\n        metric: ign_f1\n        value: 0.3974\n\n  C2_decoupling_spectrum:\n    claim: \"RL optimization pressure correlates with decoupling severity\"\n    evidence:\n      - exp: mvp2_eval_lr5e6_r1_ckpt100\n        metric: rel_f1\n        value: 0.0138\n        label: \"GRPO QLoRA catastrophic\"\n      - exp: plan_011_grpo_g8_bf16_eval\n        metric: rel_f1\n        value: 0.4549\n        label: \"GRPO bf16 mild (-2pp from SFT 0.4549 initial)\"\n      - exp: eval_plan_012_dpo_1ep_fixed_r2\n        metric: rel_f1\n        value: 0.4034\n        label: \"DPO 1ep gradual\"\n      - exp: plan_012_dpo_ced\n        metric: rel_f1\n        value: 0.3429\n        label: \"DPO 3ep further decay\"\n\n  C3_ced_vs_flat_nli:\n    claim: \"CED and flat-NLI statistically indistinguishable (p=0.44)\"\n    evidence:\n      - source: \"D078 paired t-test\"\n      - ced_mean_rel_f1: 0.4569\n      - flat_nli_mean_rel_f1: 0.4561\n      - delta: 0.0008\n\n  C4_edcr_diagnostic:\n    claim: \"EDCR provides dual-layer diagnostic value\"\n    evidence:\n      - source: \"D070 per-relation analysis\"\n      - method_level_rho: -0.965\n      - per_relation_rho_edcr_evif1: -0.064\n      - per_relation_p: 0.58\n\n  C5_scaling:\n    claim: \"Evidence tax is scale-dependent and non-monotonic\"\n    evidence:\n      - model: \"Qwen3-1.7B\"\n        source: \"D079/D083\"\n        tax: \"+6.2pp benefit\"\n      - model: \"Qwen3-4B\"\n        source: \"registry\"\n        tax: \"-7.5pp cost\"\n      - model: \"Qwen3-8B\"\n        source: \"D088 (eval running)\"\n        tax: \"≈0\"\n      - model: \"LLaMA-3.1-8B\"\n        source: \"D082\"\n        tax: \"-0.7pp near-neutral\"\n",
      "numLines": 572,
      "startLine": 1,
      "totalLines": 572
    }
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01HM5H81UPJQw6FmDxD1Dkjz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/paper_framing.md",
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
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "ccd56322-dd12-49fb-a772-efd641579365",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011LisBVkhEpt9B3zNskyRp2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7841,
      "cache_read_input_tokens": 57056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7841
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

_source line 38 · 2026-05-21T22:56:22.373Z_

<details><summary>↩ Tool result · `toolu_01HM5H81UPJQw6FmDxD1Dkjz`</summary>

```text
1	# Paper Framing — FREIGE
2	
3	> **状态**: 审稿修复中（D103 Action Matrix）— Round 1 得分 3.0 (Findings)，22 个 issue 跟踪中
4	> **最后更新**: 2026-05-21 (D144/D145: M027 corrected matched@2048 evidence tax — C3 从 "non-monotonic/capacity valley" 修正为 "within-family threshold + cross-architecture variation + variance compression")
5	> **审稿 Round 1**: 3.0 (Findings)。3 个系统性问题：claim>evidence、实验混淆、贡献过度
6	> **贡献重构**: 4 贡献 → 3 贡献（CED 合并入 RSFT，EDCR 降级为分析工具）
7	> **Dream v1**: best=2.5, median=3.0, worst=2.5 → reframe 完成
8	> **Dream v2**: best=3.0, median=2.5, worst=2.5
9	
10	## ⚠️ Post-Review Contribution Restructuring (D103)
11	
12	审稿后从 4 贡献重构为 3 贡献：
13	
14	### 原 4 贡献
15	1. Task formalization (evidence-grounded DocRE)
16	2. EDCR diagnostic metric
17	3. Decoupling spectrum
18	4. CED scoring
19	
20	### 新 3 贡献
21	1. **Evidence-grounded DocRE + RSFT with NLI-based scoring** — 合并原 C1+C4。CED 不再作为独立贡献，NLI-based scoring（CED/flat-NLI 等效）是 RSFT 有效的关键组件
22	2. **Decoupling spectrum（观察性，非因果）** — 原 C3 降级为观察性描述。"co-occurs with" 替代 "acts as amplifier"。EDCR 作为分析工具嵌入此贡献（不独立列出）
23	3. **Evidence tax landscape + RSFT variance compression** — 原 C5 提升为正式贡献。Within-family threshold（1.7B 获益，4B+ 中性）+ cross-architecture variation（Qwen 8B ≈0 vs LLaMA 8B evidence helpful）+ RSFT 跨 scale 压缩 seed 方差 (7.5-31×, D118)。**Variance compression 是 C3 核心**（最稳固的 sub-finding，不受 M027 修正影响）
24	
25	### 关键 claim 调整
26	- 所有因果 claim → 观察性描述（GRPO "acts as catastrophic amplifier" → "co-occurs with"）
27	- EDCR ρ 从 -0.965 (n=15) 改为去重后数值（待 Agent 计算完成）
28	- "+8pp" → matched@2048 fair subset: 1.7B=-5.63pp, 4B=+0.73pp, 8B=+0.04pp（D144 corrected）。Abstract 加 "on a controlled evaluation subset"
29	- "matches 8B SFT" → "approaches 8B SFT"
30	- CED vs flat-NLI 不再区分，统称 "NLI-based scoring"
31	
32	## Target Venue
33	
34	- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)
35	- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)
36	
37	## Core Insight
38	
39	**统一主线 (D131)**: Evidence generation in LLM-based DocRE is not a fixed cost — its role depends on **model capacity** (scale-dependent tax), **training paradigm** (decoupling spectrum), and **data quality** (NLI-based filtering). RSFT navigates this landscape by eliminating the tax while preserving evidence faithfulness.
40	
41	本文提出 **evidence-grounded DocRE** 作为新任务范式：LLM 同时输出关系三元组和支撑证据句。核心发现是 evidence generation 的效果并非简单的有益/有害二分，而是一个由三个维度决定的 landscape：
42	
43	1. **Model capacity × evidence tax** (C3): Within-family threshold——1.7B 从 evidence 获益（matched@2048 fair_tax=-5.63pp），4B/8B/14B 趋零（+0.73pp/+0.04pp/+0.03pp）。Cross-architecture variation——LLaMA 8B 与 Qwen 8B pattern 不同（SFT tax 极不稳定，RSFT tax=-2.17pp）。⚠️ D144 修正：4B 从 +7.5pp→+0.73pp，"non-monotonic"/"capacity valley" 叙事已废弃。
44	2. **Training paradigm × decoupling** (C2): RL 优化压力与 evidence-extraction decoupling severity 正相关（GRPO catastrophic > DPO gradual > RSFT none）。越激进的优化越破坏 RE-evidence 平衡。
45	3. **Data quality × training reliability** (C1+C3): NLI-based quality filtering (CED/flat-NLI) 不仅提升 mean performance（+3-5pp），更 dramatically 压缩 seed variance（7.5-31×）。1.7B RSFT（std=0.09pp）比 8B SFT（std=3.23pp）更 predictable——小模型通过 quality filtering 获得大模型才有的稳定性。
46	
47	**RSFT 是唯一同时在三个维度上表现良好的方法**：不引入 decoupling（维度2），压缩 evidence tax 至接近零（维度1），且通过 quality filtering 保证 training reliability（维度3）。
48	
49	CED (Contrastive Evidence Discrimination) 是一种 NLI-based 候选筛选函数，与 flat-NLI 统计不可区分（D078 p=0.44），但均显著优于 random/no scoring。CED 因可解释性优势作为默认推荐。
50	
51	## Story Arc (D131: unified narrative)
52	
53	**One-sentence pitch**: Evidence generation in DocRE is a landscape shaped by capacity, paradigm, and data quality — and RSFT is the only method that navigates all three axes successfully.
54	
55	1. **Problem**: LLM DocRE 无证据 → 部署障碍
56	2. **New task**: evidence-grounded DocRE — 同时生成关系和证据
57	3. **The landscape** (统一主线的三个 facet):
58	   - **3a. Capacity axis** (C3): evidence tax 存在 within-family threshold——1.7B 获益（-5.63pp matched@2048 fair），4B+ 中性（+0.73pp/+0.04pp/+0.03pp）。推翻"evidence 总有代价"。Cross-architecture: Qwen 8B ≈0 vs LLaMA 8B evidence helpful，说明 tax 受架构影响不仅受 scale
59	   - **3b. Paradigm axis** (C2): RL optimization pressure 与 decoupling severity 正相关（GRPO catastrophic > DPO gradual > RSFT none）。QLoRA 放大 mild→catastrophic（intra-task trade-off，非 inter-task forgetting）
60	   - **3c. Quality axis** (C1): NLI-based scoring 不仅提升 mean（+3-5pp），更压缩 variance 7.5-31×（within-scale: 1.7B 31×, 4B 7.5×, 8B 17×）。Training reliability 是 quality filtering 的本质效应
61	4. **RSFT navigates the landscape**: 唯一同时在三个轴上表现良好的方法——无 decoupling + 压缩 tax + 保证 reliability
62	5. **Practical toolkit**: CED reranker（response-level，恢复 97% evidence 代价），joint generation > post-hoc retrieval（EDCR 低 11pp）
63	6. **Diagnostic**: EDCR 双层诊断——方法级量化 decoupling，per-relation 级定位薄弱关系类型
64	7. **Scaling evidence**: 4 Qwen scales (1.7B/4B/8B/14B) + LLaMA-8B 跨家族 + Re-DocRED 跨数据集
65	8. **Mechanistic decomposition**: duplication regularization (主因, 1.7B 最强) + truncation asymmetry + fair comparison residual — 解释 WHY 而非只报 WHAT。⚠️ 4B 特有分析需 @2048 matched 数据重做（D144 invalidated "capacity valley"）
66	
67	## Core Claims (reframed after Dream v1, updated D068-D083)
68	
69	### Claim 1 (Main): Evidence-grounded DocRE 是可行的新能力
70	- FREIGE 是首个**基于生成式 LLM** 的 evidence-grounded DocRE 方法（⚠️ 必须始终保持 "generative LLM" 限定词——SAIS 已做 encoder-based evidence retrieval + DocRE）
71	- **关键区分 (Reviewer warning)**：encoder-based evidence *retrieval*（SAIS, DREEAM — 分类哪些句子是证据，evidence supervision 提升 RE）vs generative evidence *production*（FREIGE — LLM 生成证据文本，额外生成负担导致 scale-dependent 代价）。论文 Related Work 必须精准讨论此对比，否则审稿人会问 "为什么 SAIS 说 evidence 有用，你说 evidence 有害"
72	- **Evidence generation tax**: scale-dependent，详见 Claim 5（D079/D082/D083）
73	- RSFT 在 4/4 配置下均超过 SFT baseline（Ign-F1 +3.3~5.5pp）
74	- **CED reranker 是最优实用方案**: rel_f1=0.4864（仅低于 no-evidence 0.29pp），evi_f1=0.8188（plan_005 ✅）
75	- **D076 统一协议最终数字（可写入论文）**:
76	  - SFT baseline: rel_f1=0.4049
77	  - CED RSFT mean: rel_f1=0.4569 (s42=0.4517, s44=0.4621)
78	  - flat-NLI RSFT mean: rel_f1=0.4561 (s42=0.4535, s43_r2=0.4586)
79	  - CED vs flat-NLI Δ=0.0008，统计不可区分（D078 p=0.44）
80	- **Cross-family validation (D082/D130)**: LLaMA-3.1-8B SFT ign_f1=0.5384 (rel_f1=0.5514), evi_f1=0.8151; no-evidence ign_f1=0.5452 (rel_f1=0.5624). SFT evidence tax=+0.68pp（微弱代价）
81	- **Cross-dataset validation (D080)**: Re-DocRED Ign-F1 下降 3.15pp 但 Evi-F1 保持 0.817——evidence extraction 能力跨数据集泛化
82	- 需要 DREEAM-protocol 对齐的 Evi-F1 对比（D041 在处理中）
83	- **RSFT 方法论定位**：诚实承认 RSFT 是 STaR (NeurIPS 2022) 的单轮变体 + evidence quality scoring。创新点在于将 STaR-like self-improvement 应用于 evidence-grounded DocRE + CED/NLI 作为 domain-specific quality filter，而非框架本身
84	- **Evaluation caveat** (Limitations): GenRES 指出 exact match F1 低估 generative RE，FREIGE 所有 eval 用 exact match，应承认此局限（对所有方法同等适用，相对比较有效）
85	
86	### Claim 2 (Core finding): RL optimization pressure 与 evidence-extraction decoupling severity 正相关（D068/D069 修正）
87	- **Decoupling spectrum**: 优化强度越大，decoupling 越严重
88	  - GRPO QLoRA: catastrophic（rel_f1=0.0138, evi_f1=0.850, EDCR=0.99）— QLoRA 放大 decoupling
89	  - GRPO bf16: mild（rel_f1 从 0.4549→~0.434, -2pp; step_30=0.434, step_50=0.4276, step_70=0.4341）— 退化可控但持续（D065/D066）
90	  - DPO bf16 1ep→3ep: gradual（Ign-F1 38.88→TBD, rel_f1 0.4034→0.3429）— 随训练渐进退化（D067/D068）
91	  - RSFT: none — 无 decoupling，唯一有效路线
92	- **QLoRA 是 catastrophic amplifier，不是 root cause**: bf16 GRPO 仅 mild decoupling（-2pp），QLoRA 放大至 catastrophic（-39pp）（D054/D065/D066）
93	- **Decoupling 是 RL-for-IE 的通用梯度**: 跨方法（GRPO/DPO）、跨量化策略（QLoRA/bf16）一致出现，严重程度与优化压力正相关
94	- 三档 Dream 审稿均认为此发现\"genuinely novel and striking\"
95	- **已完成**: GRPO G=8 bf16 确认 mild decoupling（plan_011 ✅）; DPO 1ep/3ep 确认 gradual decoupling（plan_012 ✅）
96	
97	### Claim 3 (Ablation): NLI-based scoring 提升 RSFT 质量——CED 与 flat-NLI 统计不可区分（D078）
98	- CED 和 flat-NLI 都显著优于 random/no scoring
99	- **D078 paired t-test 最终结论**: CED vs flat-NLI p=0.44，统计不可区分
100	  - CED RSFT mean rel_f1=0.4569 vs flat-NLI mean rel_f1=0.4561（Δ=0.0008）
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "f1897afd-6185-431f-9115-410a353d79a1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/paper_framing.md",
      "content": "# Paper Framing — FREIGE\n\n> **状态**: 审稿修复中（D103 Action Matrix）— Round 1 得分 3.0 (Findings)，22 个 issue 跟踪中\n> **最后更新**: 2026-05-21 (D144/D145: M027 corrected matched@2048 evidence tax — C3 从 \"non-monotonic/capacity valley\" 修正为 \"within-family threshold + cross-architecture variation + variance compression\")\n> **审稿 Round 1**: 3.0 (Findings)。3 个系统性问题：claim>evidence、实验混淆、贡献过度\n> **贡献重构**: 4 贡献 → 3 贡献（CED 合并入 RSFT，EDCR 降级为分析工具）\n> **Dream v1**: best=2.5, median=3.0, worst=2.5 → reframe 完成\n> **Dream v2**: best=3.0, median=2.5, worst=2.5\n\n## ⚠️ Post-Review Contribution Restructuring (D103)\n\n审稿后从 4 贡献重构为 3 贡献：\n\n### 原 4 贡献\n1. Task formalization (evidence-grounded DocRE)\n2. EDCR diagnostic metric\n3. Decoupling spectrum\n4. CED scoring\n\n### 新 3 贡献\n1. **Evidence-grounded DocRE + RSFT with NLI-based scoring** — 合并原 C1+C4。CED 不再作为独立贡献，NLI-based scoring（CED/flat-NLI 等效）是 RSFT 有效的关键组件\n2. **Decoupling spectrum（观察性，非因果）** — 原 C3 降级为观察性描述。\"co-occurs with\" 替代 \"acts as amplifier\"。EDCR 作为分析工具嵌入此贡献（不独立列出）\n3. **Evidence tax landscape + RSFT variance compression** — 原 C5 提升为正式贡献。Within-family threshold（1.7B 获益，4B+ 中性）+ cross-architecture variation（Qwen 8B ≈0 vs LLaMA 8B evidence helpful）+ RSFT 跨 scale 压缩 seed 方差 (7.5-31×, D118)。**Variance compression 是 C3 核心**（最稳固的 sub-finding，不受 M027 修正影响）\n\n### 关键 claim 调整\n- 所有因果 claim → 观察性描述（GRPO \"acts as catastrophic amplifier\" → \"co-occurs with\"）\n- EDCR ρ 从 -0.965 (n=15) 改为去重后数值（待 Agent 计算完成）\n- \"+8pp\" → matched@2048 fair subset: 1.7B=-5.63pp, 4B=+0.73pp, 8B=+0.04pp（D144 corrected）。Abstract 加 \"on a controlled evaluation subset\"\n- \"matches 8B SFT\" → \"approaches 8B SFT\"\n- CED vs flat-NLI 不再区分，统称 \"NLI-based scoring\"\n\n## Target Venue\n\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\n\n## Core Insight\n\n**统一主线 (D131)**: Evidence generation in LLM-based DocRE is not a fixed cost — its role depends on **model capacity** (scale-dependent tax), **training paradigm** (decoupling spectrum), and **data quality** (NLI-based filtering). RSFT navigates this landscape by eliminating the tax while preserving evidence faithfulness.\n\n本文提出 **evidence-grounded DocRE** 作为新任务范式：LLM 同时输出关系三元组和支撑证据句。核心发现是 evidence generation 的效果并非简单的有益/有害二分，而是一个由三个维度决定的 landscape：\n\n1. **Model capacity × evidence tax** (C3): Within-family threshold——1.7B 从 evidence 获益（matched@2048 fair_tax=-5.63pp），4B/8B/14B 趋零（+0.73pp/+0.04pp/+0.03pp）。Cross-architecture variation——LLaMA 8B 与 Qwen 8B pattern 不同（SFT tax 极不稳定，RSFT tax=-2.17pp）。⚠️ D144 修正：4B 从 +7.5pp→+0.73pp，\"non-monotonic\"/\"capacity valley\" 叙事已废弃。\n2. **Training paradigm × decoupling** (C2): RL 优化压力与 evidence-extraction decoupling severity 正相关（GRPO catastrophic > DPO gradual > RSFT none）。越激进的优化越破坏 RE-evidence 平衡。\n3. **Data quality × training reliability** (C1+C3): NLI-based quality filtering (CED/flat-NLI) 不仅提升 mean performance（+3-5pp），更 dramatically 压缩 seed variance（7.5-31×）。1.7B RSFT（std=0.09pp）比 8B SFT（std=3.23pp）更 predictable——小模型通过 quality filtering 获得大模型才有的稳定性。\n\n**RSFT 是唯一同时在三个维度上表现良好的方法**：不引入 decoupling（维度2），压缩 evidence tax 至接近零（维度1），且通过 quality filtering 保证 training reliability（维度3）。\n\nCED (Contrastive Evidence Discrimination) 是一种 NLI-based 候选筛选函数，与 flat-NLI 统计不可区分（D078 p=0.44），但均显著优于 random/no scoring。CED 因可解释性优势作为默认推荐。\n\n## Story Arc (D131: unified narrative)\n\n**One-sentence pitch**: Evidence generation in DocRE is a landscape shaped by capacity, paradigm, and data quality — and RSFT is the only method that navigates all three axes successfully.\n\n1. **Problem**: LLM DocRE 无证据 → 部署障碍\n2. **New task**: evidence-grounded DocRE — 同时生成关系和证据\n3. **The landscape** (统一主线的三个 facet):\n   - **3a. Capacity axis** (C3): evidence tax 存在 within-family threshold——1.7B 获益（-5.63pp matched@2048 fair），4B+ 中性（+0.73pp/+0.04pp/+0.03pp）。推翻\"evidence 总有代价\"。Cross-architecture: Qwen 8B ≈0 vs LLaMA 8B evidence helpful，说明 tax 受架构影响不仅受 scale\n   - **3b. Paradigm axis** (C2): RL optimization pressure 与 decoupling severity 正相关（GRPO catastrophic > DPO gradual > RSFT none）。QLoRA 放大 mild→catastrophic（intra-task trade-off，非 inter-task forgetting）\n   - **3c. Quality axis** (C1): NLI-based scoring 不仅提升 mean（+3-5pp），更压缩 variance 7.5-31×（within-scale: 1.7B 31×, 4B 7.5×, 8B 17×）。Training reliability 是 quality filtering 的本质效应\n4. **RSFT navigates the landscape**: 唯一同时在三个轴上表现良好的方法——无 decoupling + 压缩 tax + 保证 reliability\n5. **Practical toolkit**: CED reranker（response-level，恢复 97% evidence 代价），joint generation > post-hoc retrieval（EDCR 低 11pp）\n6. **Diagnostic**: EDCR 双层诊断——方法级量化 decoupling，per-relation 级定位薄弱关系类型\n7. **Scaling evidence**: 4 Qwen scales (1.7B/4B/8B/14B) + LLaMA-8B 跨家族 + Re-DocRED 跨数据集\n8. **Mechanistic decomposition**: duplication regularization (主因, 1.7B 最强) + truncation asymmetry + fair comparison residual — 解释 WHY 而非只报 WHAT。⚠️ 4B 特有分析需 @2048 matched 数据重做（D144 invalidated \"capacity valley\"）\n\n## Core Claims (reframed after Dream v1, updated D068-D083)\n\n### Claim 1 (Main): Evidence-grounded DocRE 是可行的新能力\n- FREIGE 是首个**基于生成式 LLM** 的 evidence-grounded DocRE 方法（⚠️ 必须始终保持 \"generative LLM\" 限定词——SAIS 已做 encoder-based evidence retrieval + DocRE）\n- **关键区分 (Reviewer warning)**：encoder-based evidence *retrieval*（SAIS, DREEAM — 分类哪些句子是证据，evidence supervision 提升 RE）vs generative evidence *production*（FREIGE — LLM 生成证据文本，额外生成负担导致 scale-dependent 代价）。论文 Related Work 必须精准讨论此对比，否则审稿人会问 \"为什么 SAIS 说 evidence 有用，你说 evidence 有害\"\n- **Evidence generation tax**: scale-dependent，详见 Claim 5（D079/D082/D083）\n- RSFT 在 4/4 配置下均超过 SFT baseline（Ign-F1 +3.3~5.5pp）\n- **CED reranker 是最优实用方案**: rel_f1=0.4864（仅低于 no-evidence 0.29pp），evi_f1=0.8188（plan_005 ✅）\n- **D076 统一协议最终数字（可写入论文）**:\n  - SFT baseline: rel_f1=0.4049\n  - CED RSFT mean: rel_f1=0.4569 (s42=0.4517, s44=0.4621)\n  - flat-NLI RSFT mean: rel_f1=0.4561 (s42=0.4535, s43_r2=0.4586)\n  - CED vs flat-NLI Δ=0.0008，统计不可区分（D078 p=0.44）\n- **Cross-family validation (D082/D130)**: LLaMA-3.1-8B SFT ign_f1=0.5384 (rel_f1=0.5514), evi_f1=0.8151; no-evidence ign_f1=0.5452 (rel_f1=0.5624). SFT evidence tax=+0.68pp（微弱代价）\n- **Cross-dataset validation (D080)**: Re-DocRED Ign-F1 下降 3.15pp 但 Evi-F1 保持 0.817——evidence extraction 能力跨数据集泛化\n- 需要 DREEAM-protocol 对齐的 Evi-F1 对比（D041 在处理中）\n- **RSFT 方法论定位**：诚实承认 RSFT 是 STaR (NeurIPS 2022) 的单轮变体 + evidence quality scoring。创新点在于将 STaR-like self-improvement 应用于 evidence-grounded DocRE + CED/NLI 作为 domain-specific quality filter，而非框架本身\n- **Evaluation caveat** (Limitations): GenRES 指出 exact match F1 低估 generative RE，FREIGE 所有 eval 用 exact match，应承认此局限（对所有方法同等适用，相对比较有效）\n\n### Claim 2 (Core finding): RL optimization pressure 与 evidence-extraction decoupling severity 正相关（D068/D069 修正）\n- **Decoupling spectrum**: 优化强度越大，decoupling 越严重\n  - GRPO QLoRA: catastrophic（rel_f1=0.0138, evi_f1=0.850, EDCR=0.99）— QLoRA 放大 decoupling\n  - GRPO bf16: mild（rel_f1 从 0.4549→~0.434, -2pp; step_30=0.434, step_50=0.4276, step_70=0.4341）— 退化可控但持续（D065/D066）\n  - DPO bf16 1ep→3ep: gradual（Ign-F1 38.88→TBD, rel_f1 0.4034→0.3429）— 随训练渐进退化（D067/D068）\n  - RSFT: none — 无 decoupling，唯一有效路线\n- **QLoRA 是 catastrophic amplifier，不是 root cause**: bf16 GRPO 仅 mild decoupling（-2pp），QLoRA 放大至 catastrophic（-39pp）（D054/D065/D066）\n- **Decoupling 是 RL-for-IE 的通用梯度**: 跨方法（GRPO/DPO）、跨量化策略（QLoRA/bf16）一致出现，严重程度与优化压力正相关\n- 三档 Dream 审稿均认为此发现\\\"genuinely novel and striking\\\"\n- **已完成**: GRPO G=8 bf16 确认 mild decoupling（plan_011 ✅）; DPO 1ep/3ep 确认 gradual decoupling（plan_012 ✅）\n\n### Claim 3 (Ablation): NLI-based scoring 提升 RSFT 质量——CED 与 flat-NLI 统计不可区分（D078）\n- CED 和 flat-NLI 都显著优于 random/no scoring\n- **D078 paired t-test 最终结论**: CED vs flat-NLI p=0.44，统计不可区分\n  - CED RSFT mean rel_f1=0.4569 vs flat-NLI mean rel_f1=0.4561（Δ=0.0008）",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 374
    }
  }
}
```

</details>

---

### Assistant

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
Now let me check the actual LaTeX files to see their current state - how much has been written.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "48d0381e-8013-40b7-ac0e-a071ec5d15fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQEygyeJitLeXc42C8kT9S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13071,
      "cache_read_input_tokens": 64897,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13071
      },
      "output_tokens": 9,
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

_source line 40_

Now let me check the actual LaTeX sections to see how complete they are.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "a5a8f786-1060-403f-ba04-71cbeeb14e6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQEygyeJitLeXc42C8kT9S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13071,
      "cache_read_input_tokens": 64897,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13071
      },
      "output_tokens": 9,
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

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_012xwrrNVyVQcHhxYRA9xPc2`</summary>

```json
{
  "command": "for f in docs/paper/sections/*.tex docs/paper/main.tex; do echo \"=== $f ===\" && wc -l \"$f\" && echo \"---\"; done",
  "description": "Count lines in each LaTeX section file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "a43ea32f-9553-41ee-9160-24813e4046bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQEygyeJitLeXc42C8kT9S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13071,
      "cache_read_input_tokens": 64897,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13071
      },
      "output_tokens": 9,
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

_source line 42 · 2026-05-21T22:56:33.346Z_

<details><summary>↩ Tool result · `toolu_012xwrrNVyVQcHhxYRA9xPc2`</summary>

```text
=== docs/paper/sections/abstract.tex ===
18 docs/paper/sections/abstract.tex
---
=== docs/paper/sections/analysis.tex ===
14 docs/paper/sections/analysis.tex
---
=== docs/paper/sections/appendix.tex ===
339 docs/paper/sections/appendix.tex
---
=== docs/paper/sections/conclusion.tex ===
4 docs/paper/sections/conclusion.tex
---
=== docs/paper/sections/experiments.tex ===
132 docs/paper/sections/experiments.tex
---
=== docs/paper/sections/introduction.tex ===
35 docs/paper/sections/introduction.tex
---
=== docs/paper/sections/limitations.tex ===
19 docs/paper/sections/limitations.tex
---
=== docs/paper/sections/method.tex ===
64 docs/paper/sections/method.tex
---
=== docs/paper/sections/related_work.tex ===
30 docs/paper/sections/related_work.tex
---
=== docs/paper/main.tex ===
42 docs/paper/main.tex
---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "dd0e79a8-7cbb-4c4e-8f9c-d8f6a5078509",
  "tool_use_result": {
    "stdout": "=== docs/paper/sections/abstract.tex ===\n18 docs/paper/sections/abstract.tex\n---\n=== docs/paper/sections/analysis.tex ===\n14 docs/paper/sections/analysis.tex\n---\n=== docs/paper/sections/appendix.tex ===\n339 docs/paper/sections/appendix.tex\n---\n=== docs/paper/sections/conclusion.tex ===\n4 docs/paper/sections/conclusion.tex\n---\n=== docs/paper/sections/experiments.tex ===\n132 docs/paper/sections/experiments.tex\n---\n=== docs/paper/sections/introduction.tex ===\n35 docs/paper/sections/introduction.tex\n---\n=== docs/paper/sections/limitations.tex ===\n19 docs/paper/sections/limitations.tex\n---\n=== docs/paper/sections/method.tex ===\n64 docs/paper/sections/method.tex\n---\n=== docs/paper/sections/related_work.tex ===\n30 docs/paper/sections/related_work.tex\n---\n=== docs/paper/main.tex ===\n42 docs/paper/main.tex\n---",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01KwGQ1fnLyakTXNFXbeCeFf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml",
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
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "e08330b7-cd91-44a5-8bd8-ed3eb2b4e27b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQEygyeJitLeXc42C8kT9S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13071,
      "cache_read_input_tokens": 64897,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13071
      },
      "output_tokens": 9,
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

_source line 44 · 2026-05-21T22:56:33.840Z_

<details><summary>↩ Tool result · `toolu_01KwGQ1fnLyakTXNFXbeCeFf`</summary>

```text
1	- id: "W1"
2	  summary: "GRPO confounded variables (QLoRA+G size changed simultaneously)"
3	  category: experiment
4	  severity: critical
5	  status: in_progress
6	  first_raised_round: 1
7	  last_seen_round: 1
8	  mentions:
9	    - {round: 1, reviewers: "R1,R2", note: "Cannot support causal attribution of decoupling to QLoRA"}
10	  action_items:
11	    - {round: 1, action: "Rerun plan_015 GRPO bf16 G=4 to isolate quantization effect (~8h GPU)", assigned_to: "Agent", status: "pending"}
12	    - {round: 1, action: "Downgrade causal claim to observational in Intro/Method/Analysis", assigned_to: "Paper Agent", status: "done"}
13	  resolution: ""
14	  resolution_round: null
15	
16	- id: "W2"
17	  summary: "All results dev-set only, no test set"
18	  category: experiment
19	  severity: critical
20	  status: in_progress
21	  first_raised_round: 1
22	  last_seen_round: 1
23	  mentions:
24	    - {round: 1, reviewers: "R1,R2", note: "No CodaLab test results for a system claiming 85+ configs"}
25	  action_items:
26	    - {round: 1, action: "D102 k=1 retraining then regenerate test predictions + user submits CodaLab", assigned_to: "Agent+User", status: "in_progress"}
27	  resolution: ""
28	  resolution_round: null
29	
30	- id: "W3"
31	  summary: "SFT baseline single seed, no statistical significance test"
32	  category: experiment
33	  severity: critical
34	  status: in_progress
35	  first_raised_round: 1
36	  last_seen_round: 1
37	  mentions:
38	    - {round: 1, reviewers: "R1,R2", note: "+4.92pp core claim lacks statistical backing"}
39	  action_items:
40	    - {round: 1, action: "Run SFT seed43 + seed44 (~8h GPU), compute bootstrap CI + Cohen's d", assigned_to: "Agent", status: "pending"}
41	  resolution: ""
42	  resolution_round: null
43	
44	- id: "W4"
45	  summary: "Non-monotonic scaling claim based on only 3 data points"
46	  category: framing
47	  severity: critical
48	  status: in_progress
49	  first_raised_round: 1
50	  last_seen_round: 1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "13a72ab9-f1d2-4162-999d-23d62261990f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml",
      "content": "- id: \"W1\"\n  summary: \"GRPO confounded variables (QLoRA+G size changed simultaneously)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Cannot support causal attribution of decoupling to QLoRA\"}\n  action_items:\n    - {round: 1, action: \"Rerun plan_015 GRPO bf16 G=4 to isolate quantization effect (~8h GPU)\", assigned_to: \"Agent\", status: \"pending\"}\n    - {round: 1, action: \"Downgrade causal claim to observational in Intro/Method/Analysis\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W2\"\n  summary: \"All results dev-set only, no test set\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"No CodaLab test results for a system claiming 85+ configs\"}\n  action_items:\n    - {round: 1, action: \"D102 k=1 retraining then regenerate test predictions + user submits CodaLab\", assigned_to: \"Agent+User\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W3\"\n  summary: \"SFT baseline single seed, no statistical significance test\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"+4.92pp core claim lacks statistical backing\"}\n  action_items:\n    - {round: 1, action: \"Run SFT seed43 + seed44 (~8h GPU), compute bootstrap CI + Cohen's d\", assigned_to: \"Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W4\"\n  summary: \"Non-monotonic scaling claim based on only 3 data points\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1",
      "numLines": 50,
      "startLine": 1,
      "totalLines": 303
    }
  }
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Read · `toolu_01JqQAREamue9TiPwAhpet4A`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "b07f704f-f91e-463f-9a45-db53198e4345",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kb3KWGwkN3YkxDwwScf4C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1321,
      "cache_read_input_tokens": 77968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1321
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

_source line 46 · 2026-05-21T22:56:37.470Z_

<details><summary>↩ Tool result · `toolu_01JqQAREamue9TiPwAhpet4A`</summary>

```text
1	\begin{abstract}
2	
3	Large Language Model (LLM) based Document-level Relation Extraction (DocRE) now matches or exceeds encoder baselines in extraction accuracy, yet these methods output bare relation triplets without identifying which sentences support each prediction.
4	Deployment contexts such as clinical knowledge bases and legal due-diligence systems require verifiable evidence that users can trace to source text.
5	Encoder-based evidence methods (SAIS, DREEAM) provide supporting sentences but trail LLM approaches in accuracy, so the community faces a gap between extraction performance and output verifiability.
6	
7	We formalize evidence-grounded DocRE as a structured generation task and systematically compare three post-training paradigms: Group Relative Policy Optimization (GRPO), Direct Preference Optimization (DPO), and Rejection Sampling Fine-Tuning (RSFT) across 85+ configurations spanning three fully evaluated scales (1.7B, 4B, 8B) with 14B validation, two model families, and two datasets.
8	We use the Evidence-Decoupling Ratio (EDCR) as a diagnostic tool and Natural Language Inference (NLI) based scoring for sample selection.
9	
10	Our experiments reveal that evidence generation plays a scale-dependent role shaped by three interacting factors.
11	Along the capacity dimension, the evidence tax (on the development set) reveals a within-family capacity threshold: beneficial at 1.7B ($-$5.63pp Ign-F1) but approximately neutral at $\geq$4B (+0.25$\pm$0.47pp at 4B; positive $=$ cost).
12	Along the paradigm dimension, optimization pressure correlates with evidence-extraction decoupling severity (GRPO catastrophic, DPO gradual, RSFT none).
13	Along the data quality dimension, RSFT with NLI-based scoring navigates this landscape through output filtering rather than gradient-based pressure.
14	
15	RSFT improves mean Ign-F1 across tested scales (+1.2 to +6.6pp) with 7.5--17$\times$ variance compression on Qwen3 and 4.6$\times$ on LLaMA (complete pairwise seed separation, Cohen's $d{=}2.58$).
16	Our 1.7B RSFT model (51.19 Ign-F1, std 0.09pp) approaches 8B Supervised Fine-Tuning (SFT) performance (50.19, std 3.23pp) while being 4.7$\times$ smaller and substantially more predictable.
17	
18	\end{abstract}
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "f9d808b1-3f66-4fae-b544-26d8104a2090",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\n\nLarge Language Model (LLM) based Document-level Relation Extraction (DocRE) now matches or exceeds encoder baselines in extraction accuracy, yet these methods output bare relation triplets without identifying which sentences support each prediction.\nDeployment contexts such as clinical knowledge bases and legal due-diligence systems require verifiable evidence that users can trace to source text.\nEncoder-based evidence methods (SAIS, DREEAM) provide supporting sentences but trail LLM approaches in accuracy, so the community faces a gap between extraction performance and output verifiability.\n\nWe formalize evidence-grounded DocRE as a structured generation task and systematically compare three post-training paradigms: Group Relative Policy Optimization (GRPO), Direct Preference Optimization (DPO), and Rejection Sampling Fine-Tuning (RSFT) across 85+ configurations spanning three fully evaluated scales (1.7B, 4B, 8B) with 14B validation, two model families, and two datasets.\nWe use the Evidence-Decoupling Ratio (EDCR) as a diagnostic tool and Natural Language Inference (NLI) based scoring for sample selection.\n\nOur experiments reveal that evidence generation plays a scale-dependent role shaped by three interacting factors.\nAlong the capacity dimension, the evidence tax (on the development set) reveals a within-family capacity threshold: beneficial at 1.7B ($-$5.63pp Ign-F1) but approximately neutral at $\\geq$4B (+0.25$\\pm$0.47pp at 4B; positive $=$ cost).\nAlong the paradigm dimension, optimization pressure correlates with evidence-extraction decoupling severity (GRPO catastrophic, DPO gradual, RSFT none).\nAlong the data quality dimension, RSFT with NLI-based scoring navigates this landscape through output filtering rather than gradient-based pressure.\n\nRSFT improves mean Ign-F1 across tested scales (+1.2 to +6.6pp) with 7.5--17$\\times$ variance compression on Qwen3 and 4.6$\\times$ on LLaMA (complete pairwise seed separation, Cohen's $d{=}2.58$).\nOur 1.7B RSFT model (51.19 Ign-F1, std 0.09pp) approaches 8B Supervised Fine-Tuning (SFT) performance (50.19, std 3.23pp) while being 4.7$\\times$ smaller and substantially more predictable.\n\n\\end{abstract}\n",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
    }
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Read · `toolu_01AgZq5bToD1yzjqmiX2Fb88`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "439d706f-21c5-4ce0-a25a-691555c3b07f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kb3KWGwkN3YkxDwwScf4C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1321,
      "cache_read_input_tokens": 77968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1321
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

_source line 48 · 2026-05-21T22:56:37.912Z_

<details><summary>↩ Tool result · `toolu_01AgZq5bToD1yzjqmiX2Fb88`</summary>

```text
1	\section{Introduction}
2	
3	Document-level relation extraction (DocRE) requires identifying semantic relations between entity pairs across multiple sentences, a task where encoder-based methods such as \citet{zhou2021atlop} long dominated.
4	Recent approaches based on Large Language Models (LLMs) have closed this gap: \citet{autore2024} fine-tune LLMs with structured decomposition for end-to-end extraction, \citet{xu2024lmrc} frame it as multi-choice reading comprehension, and \citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.
5	These methods approach or surpass encoder baselines on DocRED \citep{yao2019docred} and Re-DocRED \citep{tan2022redocred} in extraction accuracy.
6	Yet every one of them outputs bare relation triplets $(e_h, r, e_t)$ without any indication of \emph{which sentences} in the document support each prediction.
7	In deployment contexts where predictions feed into clinical knowledge bases, legal due-diligence pipelines, or financial compliance systems, end users cannot verify a prediction without manually locating its textual basis across a multi-page document.
8	
9	The absence of verifiable evidence creates a practical bottleneck.
10	Relation extraction outputs feed downstream knowledge graph construction and human decision workflows; when a system predicts that a drug interacts with a gene, or that a contract clause implies a liability, practitioners must trace each prediction back to source text before acting on it.
11	Encoder-based methods have partially addressed this need: \citet{xiao2022sais} introduce sentence-level evidence supervision as an auxiliary signal, and \citet{ma2023dreeam} extend this with dynamic evidence retrieval through memory attention.
12	Both produce evidence annotations and improve extraction quality, but encoder methods now trail LLM-based approaches in extraction accuracy.
13	The community therefore faces a gap: the most accurate extractors provide no evidence, while the evidence-capable methods are no longer competitive.
14	
15	This gap reflects a deeper structural difference in how evidence functions across architectures and scales.
16	In encoder-based methods such as SAIS and DREEAM, evidence retrieval is a binary classification task (does sentence $s_i$ support relation $r$?) that serves as auxiliary supervision; the evidence signal regularizes the encoder and improves extraction at minimal cost.
17	In LLM-based DocRE, evidence-grounded extraction requires the model to \emph{generate} complete evidence sentences as part of its output sequence, substantially increasing output length and decoding complexity.
18	Yet the role of this generation cost is not fixed.
19	It depends on at least three factors: \emph{model capacity}, where small models benefit from the implicit regularization that evidence provides while mid-scale and larger models show approximately neutral impact as capacity absorbs the generation overhead; \emph{optimization paradigm}, where gradient-based methods create destructive trade-offs between evidence and extraction objectives while discrete sample selection avoids them entirely; and \emph{training data quality}, where filtering based on Natural Language Inference (NLI) scores can transform evidence from an optimization burden into a learning scaffold.
20	Understanding this landscape is a prerequisite for deploying evidence-grounded extraction systems that are both accurate and verifiable.
21	
22	We formalize evidence-grounded DocRE as a structured generation task and conduct a systematic comparison of three post-training paradigms: online reinforcement learning via Group Relative Policy Optimization (GRPO; \citealt{shao2024deepseekmath}), offline preference optimization via Direct Preference Optimization (DPO; \citealt{rafailov2023direct}), and offline reinforcement learning via Rejection Sampling Fine-Tuning (RSFT, building on STaR; \citealt{zelikman2022star}).
23	Our experiments span three model scales with full RSFT evaluation (1.7B, 4B, 8B), 14B validation, two model families, and two datasets across 85+ configurations. They reveal that the role of evidence generation is governed by three interacting factors.
24	Along the \emph{capacity dimension}, the evidence tax reveals a within-family capacity threshold: evidence generation provides implicit regularization at 1.7B ($-$5.63pp Ign-F1) but is approximately neutral at $\geq$4B (+0.25$\pm$0.47pp at 4B, +0.04pp at 8B).
25	Along the \emph{paradigm dimension}, we observe a decoupling spectrum in which the strength of optimization pressure correlates with evidence-extraction decoupling severity (GRPO catastrophic $\rightarrow$ DPO gradual $\rightarrow$ RSFT none); catastrophic extraction collapse co-occurs with Quantized Low-Rank Adaptation (QLoRA; \citealt{hu2022lora}) in GRPO, though full-precision GRPO maintains extraction above the supervised fine-tuning (SFT) baseline with only mild decoupling (EDCR 0.6318 vs.\ SFT 0.6797), which indicates that the collapse is not inherent to online RL when sufficient precision is available.
26	Along the \emph{data quality dimension}, RSFT with NLI-based scoring navigates this landscape by selecting high-quality training samples through output filtering rather than applying gradient-based pressure; it improves mean Ign-F1 across tested scales (+1.2 to +6.6pp) while compressing Qwen3 training variance 7.5--17$\times$ and LLaMA variance 4.6$\times$.
27	
28	Our contributions are as follows:
29	\begin{enumerate}
30	    \item We map the \textbf{evidence generation landscape} through a comprehensive empirical study spanning 85+ experiments across three fully evaluated model scales (1.7B, 4B, 8B) with 14B validation, two model families, two datasets (DocRED, Re-DocRED), and three optimization paradigms. We identify a \textbf{scale-dependent evidence tax} with a within-family capacity threshold: beneficial at 1.7B ($-$5.63pp) but approximately neutral at $\geq$4B (+0.25$\pm$0.47pp). This challenges the assumption that evidence generation uniformly harms extraction.
31	
32	    \item We characterize a \textbf{decoupling spectrum} that explains why gradient-based paradigms fail at joint evidence-and-extraction generation: RL optimization pressure correlates with evidence-extraction decoupling severity (GRPO catastrophic $\rightarrow$ DPO gradual $\rightarrow$ RSFT none). We introduce the Evidence-Decoupling Ratio (EDCR) as a diagnostic metric, validated through per-relation analysis ($\rho = -0.79$, $n = 76$, $p < 0.001$).
33	
34	    \item We establish \textbf{RSFT with NLI-based scoring} as an effective navigation strategy for this landscape. RSFT improves mean Ign-F1 across tested scales (+1.2 to +6.6pp) with 7.5--17$\times$ Qwen3 variance compression and 4.6$\times$ on LLaMA (complete pairwise seed separation, Cohen's $d{=}2.58$). Our 1.7B RSFT model (51.19 Ign-F1, std 0.09pp) approaches 8B SFT performance (50.19, std 3.23pp) while being 4.7$\times$ smaller and substantially more predictable, enabling deployment-efficient evidence-grounded extraction.
35	\end{enumerate}
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "64f3a918-edd7-4589-8429-4a77df7cba22",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\n\nDocument-level relation extraction (DocRE) requires identifying semantic relations between entity pairs across multiple sentences, a task where encoder-based methods such as \\citet{zhou2021atlop} long dominated.\nRecent approaches based on Large Language Models (LLMs) have closed this gap: \\citet{autore2024} fine-tune LLMs with structured decomposition for end-to-end extraction, \\citet{xu2024lmrc} frame it as multi-choice reading comprehension, and \\citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.\nThese methods approach or surpass encoder baselines on DocRED \\citep{yao2019docred} and Re-DocRED \\citep{tan2022redocred} in extraction accuracy.\nYet every one of them outputs bare relation triplets $(e_h, r, e_t)$ without any indication of \\emph{which sentences} in the document support each prediction.\nIn deployment contexts where predictions feed into clinical knowledge bases, legal due-diligence pipelines, or financial compliance systems, end users cannot verify a prediction without manually locating its textual basis across a multi-page document.\n\nThe absence of verifiable evidence creates a practical bottleneck.\nRelation extraction outputs feed downstream knowledge graph construction and human decision workflows; when a system predicts that a drug interacts with a gene, or that a contract clause implies a liability, practitioners must trace each prediction back to source text before acting on it.\nEncoder-based methods have partially addressed this need: \\citet{xiao2022sais} introduce sentence-level evidence supervision as an auxiliary signal, and \\citet{ma2023dreeam} extend this with dynamic evidence retrieval through memory attention.\nBoth produce evidence annotations and improve extraction quality, but encoder methods now trail LLM-based approaches in extraction accuracy.\nThe community therefore faces a gap: the most accurate extractors provide no evidence, while the evidence-capable methods are no longer competitive.\n\nThis gap reflects a deeper structural difference in how evidence functions across architectures and scales.\nIn encoder-based methods such as SAIS and DREEAM, evidence retrieval is a binary classification task (does sentence $s_i$ support relation $r$?) that serves as auxiliary supervision; the evidence signal regularizes the encoder and improves extraction at minimal cost.\nIn LLM-based DocRE, evidence-grounded extraction requires the model to \\emph{generate} complete evidence sentences as part of its output sequence, substantially increasing output length and decoding complexity.\nYet the role of this generation cost is not fixed.\nIt depends on at least three factors: \\emph{model capacity}, where small models benefit from the implicit regularization that evidence provides while mid-scale and larger models show approximately neutral impact as capacity absorbs the generation overhead; \\emph{optimization paradigm}, where gradient-based methods create destructive trade-offs between evidence and extraction objectives while discrete sample selection avoids them entirely; and \\emph{training data quality}, where filtering based on Natural Language Inference (NLI) scores can transform evidence from an optimization burden into a learning scaffold.\nUnderstanding this landscape is a prerequisite for deploying evidence-grounded extraction systems that are both accurate and verifiable.\n\nWe formalize evidence-grounded DocRE as a structured generation task and conduct a systematic comparison of three post-training paradigms: online reinforcement learning via Group Relative Policy Optimization (GRPO; \\citealt{shao2024deepseekmath}), offline preference optimization via Direct Preference Optimization (DPO; \\citealt{rafailov2023direct}), and offline reinforcement learning via Rejection Sampling Fine-Tuning (RSFT, building on STaR; \\citealt{zelikman2022star}).\nOur experiments span three model scales with full RSFT evaluation (1.7B, 4B, 8B), 14B validation, two model families, and two datasets across 85+ configurations. They reveal that the role of evidence generation is governed by three interacting factors.\nAlong the \\emph{capacity dimension}, the evidence tax reveals a within-family capacity threshold: evidence generation provides implicit regularization at 1.7B ($-$5.63pp Ign-F1) but is approximately neutral at $\\geq$4B (+0.25$\\pm$0.47pp at 4B, +0.04pp at 8B).\nAlong the \\emph{paradigm dimension}, we observe a decoupling spectrum in which the strength of optimization pressure correlates with evidence-extraction decoupling severity (GRPO catastrophic $\\rightarrow$ DPO gradual $\\rightarrow$ RSFT none); catastrophic extraction collapse co-occurs with Quantized Low-Rank Adaptation (QLoRA; \\citealt{hu2022lora}) in GRPO, though full-precision GRPO maintains extraction above the supervised fine-tuning (SFT) baseline with only mild decoupling (EDCR 0.6318 vs.\\ SFT 0.6797), which indicates that the collapse is not inherent to online RL when sufficient precision is available.\nAlong the \\emph{data quality dimension}, RSFT with NLI-based scoring navigates this landscape by selecting high-quality training samples through output filtering rather than applying gradient-based pressure; it improves mean Ign-F1 across tested scales (+1.2 to +6.6pp) while compressing Qwen3 training variance 7.5--17$\\times$ and LLaMA variance 4.6$\\times$.\n\nOur contributions are as follows:\n\\begin{enumerate}\n    \\item We map the \\textbf{evidence generation landscape} through a comprehensive empirical study spanning 85+ experiments across three fully evaluated model scales (1.7B, 4B, 8B) with 14B validation, two model families, two datasets (DocRED, Re-DocRED), and three optimization paradigms. We identify a \\textbf{scale-dependent evidence tax} with a within-family capacity threshold: beneficial at 1.7B ($-$5.63pp) but approximately neutral at $\\geq$4B (+0.25$\\pm$0.47pp). This challenges the assumption that evidence generation uniformly harms extraction.\n\n    \\item We characterize a \\textbf{decoupling spectrum} that explains why gradient-based paradigms fail at joint evidence-and-extraction generation: RL optimization pressure correlates with evidence-extraction decoupling severity (GRPO catastrophic $\\rightarrow$ DPO gradual $\\rightarrow$ RSFT none). We introduce the Evidence-Decoupling Ratio (EDCR) as a diagnostic metric, validated through per-relation analysis ($\\rho = -0.79$, $n = 76$, $p < 0.001$).\n\n    \\item We establish \\textbf{RSFT with NLI-based scoring} as an effective navigation strategy for this landscape. RSFT improves mean Ign-F1 across tested scales (+1.2 to +6.6pp) with 7.5--17$\\times$ Qwen3 variance compression and 4.6$\\times$ on LLaMA (complete pairwise seed separation, Cohen's $d{=}2.58$). Our 1.7B RSFT model (51.19 Ign-F1, std 0.09pp) approaches 8B SFT performance (50.19, std 3.23pp) while being 4.7$\\times$ smaller and substantially more predictable, enabling deployment-efficient evidence-grounded extraction.\n\\end{enumerate}\n",
      "numLines": 36,
      "startLine": 1,
      "totalLines": 36
    }
  }
}
```

</details>

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_01Bh1w5C6UMrKbyXva8eC2ZH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "68c387c2-f991-4716-8b06-e39f50edb320",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kb3KWGwkN3YkxDwwScf4C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1321,
      "cache_read_input_tokens": 77968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1321
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

_source line 50 · 2026-05-21T22:56:38.396Z_

<details><summary>↩ Tool result · `toolu_01Bh1w5C6UMrKbyXva8eC2ZH`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Dataset.}
8	We conduct experiments on DocRED~\citep{yao2019docred}, a large-scale document-level relation extraction benchmark containing 3,053 training and 998 development documents spanning 96 relation types. Each document requires identifying relational triples across multiple sentences and grounding each triple with supporting evidence sentences. We use Re-DocRED~\citep{tan2022redocred} for cross-dataset generalization evaluation.
9	
10	\paragraph{Models.}
11	Our primary model is Qwen3-4B. To study scale effects, we additionally train Qwen3-1.7B and Qwen3-8B under identical configurations. We include LLaMA-3.1-8B as a cross-family validation point.
12	
13	\paragraph{Training.}
14	All models use LoRA~\citep{hu2022lora} with rank $r{=}64$ and $\alpha{=}128$ over a structured output format that jointly produces relation triples and evidence sentences. For RSFT, we sample $N{=}8$ candidate outputs per document and select the top-$k{=}1$ response ranked by CED scoring (\S\ref{sec:ced}), which combines NLI-based evidence faithfulness with extraction accuracy. GRPO experiments use group sizes $G{=}4$ (QLoRA, 4-bit) and $G{=}8$ (bf16 full-precision LoRA). DPO constructs preference pairs from CED-ranked outputs.
15	
16	\paragraph{Metrics.}
17	\textbf{Ign-F1} (primary) ignores training-set triples per the official DocRED protocol. \textbf{Rel-F1} measures extraction F1 on all triples. \textbf{Evi-F1 (TP-only)} measures evidence F1 conditioned on correct triples; \textbf{Evi-F1 (joint)} follows the DREEAM protocol~\citep{ma2023dreeam} for cross-method comparison. \textbf{EDCR} (\S\ref{sec:edcr}) diagnoses extraction-evidence decoupling. All results use the development set.
18	
19	
20	\subsection{Main Results}
21	\label{sec:main_results}
22	
23	Table~\ref{tab:main} presents the primary comparison on Qwen3-4B. The SFT baseline exhibits high seed sensitivity (mean Ign-F1 43.58, std 3.80pp, range 39.74--47.34). Removing evidence entirely (no-evidence SFT, s42) reaches 47.21 Ign-F1.
24	
25	RSFT CED achieves 44.82 Ign-F1 (+1.24 over SFT mean) with substantially lower variance (std 0.51pp), though these reflect different sources of variation (Section~\ref{sec:scaling}). Even the weakest RSFT seed (44.23) exceeds the SFT mean. Evidence quality improves (Evi-F1 80.96 vs.\ 79.61) and coupling tightens (EDCR 0.6487 vs.\ 0.6797). Per-seed results appear in Appendix~\ref{sec:ablation_full}.
26	
27	\begin{table}[t]
28	\centering
29	\caption{Main results on DocRED dev (Qwen3-4B). Ign-F1 shows mean $\pm$ std$^{(\text{seeds})}$; other metrics are same-seed means. Best \textbf{bold}; best evidence-generating \underline{underlined}. Per-seed: Appendix~\ref{tab:ablation_full}.}
30	\label{tab:main}
31	\small
32	\resizebox{\columnwidth}{!}{%
33	\begin{tabular}{lcccc}
34	\toprule
35	\textbf{Method} & \textbf{Ign-F1} & \textbf{Rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} \\
36	\midrule
37	SFT baseline & 43.58{\scriptsize$\pm$3.80}$^{(3)}$ & 44.39 & 79.61 & 0.6797 \\
38	SFT no-evidence & \textbf{47.21} & \textbf{48.76} & -- & -- \\
39	RSFT CED & \underline{44.82{\scriptsize$\pm$0.51}$^{(3)}$} & \underline{45.80} & 80.96 & 0.6487 \\
40	\bottomrule
41	\end{tabular}%
42	}
43	\vspace{-2mm}
44	\end{table}
45	
46	
47	\subsection{Evidence-Extraction Decoupling Spectrum}
48	\label{sec:spectrum}
49	
50	Different RL algorithms produce qualitatively different failure modes when applied to joint evidence-and-extraction generation. We organize these outcomes along a \emph{decoupling spectrum} ranging from catastrophic collapse to mild perturbation, shown in Table~\ref{tab:spectrum} (visualized in Figure~\ref{fig:spectrum}, Appendix).
51	
52	\paragraph{GRPO QLoRA: catastrophic collapse.}
53	Under 4-bit quantization ($G{=}4$), GRPO drives Rel-F1 to 1.38 while Evi-F1 rises to 85.04 (EDCR 0.9876): the model produces well-formed evidence but loses extraction capability. This extreme decoupling co-occurs with constrained precision; full-precision GRPO (below) avoids it.
54	
55	\paragraph{GRPO bf16: mild, variable.}
56	Full-precision GRPO ($G{=}8$) avoids catastrophe, with the best checkpoint achieving Rel-F1 45.49, Evi-F1 80.86, and EDCR 0.6318 (below SFT baseline 0.6797). Both sub-tasks improve jointly, though the variable training trajectory requires careful checkpoint selection.
57	
58	\paragraph{DPO: gradual decay.}
59	DPO progressively trades extraction for evidence: Rel-F1 drops from 40.34 (1 epoch) to 34.29 (3 epochs)\footnote{DPO 3-epoch results use an earlier evaluation protocol; included for trend analysis.} while evidence improves (Evi-F1 80.88$\to$84.03, EDCR 0.7139$\to$0.7294).
60	
61	\paragraph{RSFT: no decoupling.}
62	RSFT maintains both capabilities simultaneously (Rel-F1 45.80, Evi-F1 80.96, EDCR 0.6487) because discrete output selection cannot exploit the extraction-evidence trade-off that gradient methods find.
63	
64	\begin{table}[t]
65	\centering
66	\caption{Evidence-extraction decoupling across RL paradigms (Qwen3-4B). Severity indicates the degree of extraction collapse relative to evidence improvement.}
67	\label{tab:spectrum}
68	\small
69	\resizebox{\columnwidth}{!}{%
70	\begin{tabular}{llcccc}
71	\toprule
72	\textbf{Paradigm} & \textbf{Config} & \textbf{Rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} & \textbf{Severity} \\
73	\midrule
74	GRPO & QLoRA $G{=}4$ & 1.38 & 85.04 & 0.9876 & Catastrophic \\
75	GRPO & bf16 $G{=}8$ & 45.49 & 80.86 & 0.6318 & Mild \\
76	DPO & bf16 1ep & 40.34 & 80.88 & 0.7139 & Gradual \\
77	DPO & bf16 3ep$^\dagger$ & 34.29 & 84.03 & 0.7294 & Gradual \\
78	\midrule
79	SFT & baseline$^\ddagger$ & 44.39 & 79.61 & 0.6797 & None \\
80	RSFT & CED$^\ddagger$ & 45.80 & 80.96 & 0.6487 & None \\
81	\bottomrule
82	\end{tabular}%
83	}
84	\vspace{-2mm}
85	{\raggedright\footnotesize $^\dagger$Earlier evaluation protocol. $^\ddagger$Three-seed mean. Severity reflects training trajectory stability (propensity for extraction collapse during optimization), not the final-checkpoint EDCR value.\par}
86	\end{table}
87	
88	
89	\subsection{Scale-Dependent Evidence Tax}
90	\label{sec:scaling}
91	
92	The evidence tax, defined as Ign-F1(no-evidence) $-$ Ign-F1(with-evidence) on the development set, is scale-dependent. Under matched evaluation conditions (\texttt{max\_new\_tokens}$=$2048, format-compliant intersection; Appendix~\ref{sec:training_tax}), the training-time tax reveals a within-family capacity threshold: evidence generation benefits 1.7B ($-$5.63pp; Appendix~\ref{sec:training_tax}) through implicit regularization that forces attention to supporting context, but is approximately neutral at $\geq$4B (+0.25$\pm$0.47pp at 4B, $n{=}3$; +0.04pp at 8B; +0.03pp at 14B). Table~\ref{tab:scaling} presents RSFT performance and inference-time evidence tax across five models (Figure~\ref{fig:scaling} in Appendix).
93	
94	RSFT navigates this capacity landscape through quality-based data selection rather than gradient pressure. Mean Ign-F1 improves across tested scales: +6.55pp at 1.7B, +1.24pp at 4B, +4.33pp at 8B, and +3.79pp at 14B (Table~\ref{tab:scaling}). RSFT from an independent SFT base (s44, Method B) achieves 51.52 Ign-F1 at 4B (+4.18pp over that base). This result confirms that RSFT gains are not contingent on a specific SFT checkpoint.
95	
96	Beyond mean performance, RSFT substantially improves training reliability. Three RSFT seeds from a shared SFT checkpoint yield standard deviations of 0.09pp at 1.7B, 0.51pp at 4B, and 0.19pp at 8B ($n{=}3$ each), compared to SFT cross-seed variation of 2.79pp, 3.80pp, and 3.23pp respectively. While these measure different sources of variance (SFT reflects full training runs from different random seeds; RSFT reflects additional fine-tuning from a fixed base), the practical consequence is direct: within-scale variance compression is 31$\times$ at 1.7B, 7.5$\times$ at 4B, and 17$\times$ at 8B. The 1.7B RSFT model (51.19 Ign-F1, std 0.09pp) is both more accurate and more predictable than the 8B SFT model (50.19, std 3.23pp), achieving +1.0pp higher mean at 4.7$\times$ fewer parameters (cross-scale compression 36$\times$). Cross-family, LLaMA-3.1-8B exhibits complete pairwise seed separation: all RSFT seeds (55.87--57.14) exceed all SFT seeds (48.02--53.84), with Cohen's $d{=}2.58$ and 4.6$\times$ variance compression (std 2.92pp $\to$ 0.64pp). The SFT seed lottery is starkest at LLaMA s44 (48.02 Ign-F1, 24.4\% truncation rate, elevated Evi-F1 85\%), a degenerate outcome that RSFT eliminates entirely (s44: 55.87). This robustness extends to inference-time format changes: LLaMA SFT models evaluated without evidence at 1024 tokens suffer 38--42\% truncation with Ign-F1 collapsing to ${\sim}$0.33 (s43/s44), while RSFT models under identical conditions truncate only 18--19\% with stable performance (55.41$\pm$0.13pp), indicating that CED filtering selects for compact output structure.
97	
98	For RSFT models, the inference-time evidence tax (same model evaluated with vs.\ without evidence output) preserves the benefit direction at 1.7B ($-$7.75pp, confirmed with 2048-token no-evidence evaluation that rules out truncation). At 4B, where the training-time tax is approximately neutral (+0.25$\pm$0.47pp; Appendix~\ref{sec:training_tax}), the RSFT inference-time tax is similarly small (+0.94pp). At 8B, the tax reverses to a benefit ($-$0.78pp), and at 14B the benefit is largest ($-$4.54pp). RSFT thus maintains or improves extraction quality with evidence across the Qwen3 family. LLaMA-3.1-8B RSFT shows a larger inference-time evidence benefit ($-$2.17$\pm$0.76pp, three-seed mean, vs.\ $-$0.78pp for Qwen3-8B), confirming that both performance gains and training reliability generalize across model families.
99	
100	\begin{table}[t]
101	\centering
102	\caption{RSFT performance and inference-time evidence tax across model scales (DocRED dev Ign-F1). Mean $\pm$ std$^{(\text{seeds})}$.}
103	\label{tab:scaling}
104	\small
105	\resizebox{\columnwidth}{!}{%
106	\begin{tabular}{lcccc}
107	\toprule
108	\textbf{Model} & \textbf{SFT w/ evi} & \textbf{RSFT} & \textbf{RSFT Tax}$^\dagger$ & \textbf{RSFT Gain} \\
109	\midrule
110	Qwen3-1.7B & 44.64{\scriptsize$\pm$2.79}$^{(3)}$ & 51.19{\scriptsize$\pm$0.09}$^{(3)}$ & $-$7.75 & +6.55 \\
111	Qwen3-4B & 43.58{\scriptsize$\pm$3.80}$^{(3)}$ & 44.82{\scriptsize$\pm$0.51}$^{(3)}$ & +0.94 & +1.24 \\
112	Qwen3-8B & 50.19{\scriptsize$\pm$3.23}$^{(3)}$ & 54.52{\scriptsize$\pm$0.19}$^{(3)}$ & $-$0.78 & +4.33 \\
113	Qwen3-14B & 55.07 & 58.86 & $-$4.54 & +3.79 \\
114	LLaMA-3.1-8B & 51.09{\scriptsize$\pm$2.92}$^{(3)}$ & 56.54{\scriptsize$\pm$0.64}$^{(3)}$ & $-$2.17{\scriptsize$\pm$0.76}$^{(3)}$ & +5.45 \\
115	\bottomrule
116	\end{tabular}%
117	}
118	\vspace{-2mm}
119	{\raggedright\footnotesize $^\dagger$Inference-time: same RSFT model with vs.\ without evidence output. No-evi eval uses \texttt{max\_new\_tokens}$=$2048; with-evi eval uses 1024 (1.7B uses 2048 for both). Tax $=$ no-evi $-$ with-evi; positive $=$ cost. Seeds: 1.7B s42; 4B Method B s44; 8B, 14B: s42; LLaMA: three-seed mean. Training-time tax (matched@2048 fair evaluation) in Appendix~\ref{sec:training_tax}.\par}
120	\end{table}
121	
122	
123	\subsection{Evidence Strategy Comparison}
124	\label{sec:evidence_strategy}
125	
126	We compare joint generation against post-hoc BM25 retrieval (entity-constrained, $k{=}2$), using Evi-F1 (joint) with the DREEAM-protocol denominator~\citep{ma2023dreeam}. Post-hoc retrieval achieves higher Rel-F1 (48.76) by avoiding the evidence tax but lower Evi-F1 (joint) of 34.7 (EDCR 0.766). RSFT CED reaches 36.1 (EDCR 0.654), a 1.4-point evidence advantage. CED reranking at inference (best-of-$N{=}8$ by CED score) achieves Rel-F1 48.64 and Evi-F1 81.88 (TP-only), approaching no-evidence extraction quality while preserving evidence.
127	
128	
129	\subsection{Generalization}
130	\label{sec:generalization}
131	
132	Cross-architecture validation on LLaMA-3.1-8B (Table~\ref{tab:scaling}) shows the largest RSFT gain (+5.45pp) with complete pairwise seed separation (\S\ref{sec:scaling}). The RSFT improvement transfers across datasets: on Re-DocRED~\citep{tan2022redocred}, RSFT achieves 41.45 Ign-F1 (+4.86pp over SFT 36.59), matching the DocRED gain (+5.08pp). Our best joint Evi-F1 (36.1, DREEAM-protocol) falls below supervised DREEAM (54.01\%~\citep{ma2023dreeam}), a gap driven by extraction performance rather than evidence quality (TP-only Evi-F1 exceeds 80\%). Full results appear in Appendix~\ref{sec:generalization_full}.
133	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "5be9a712-9c95-4bee-a4fc-b811e10a769a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Dataset.}\nWe conduct experiments on DocRED~\\citep{yao2019docred}, a large-scale document-level relation extraction benchmark containing 3,053 training and 998 development documents spanning 96 relation types. Each document requires identifying relational triples across multiple sentences and grounding each triple with supporting evidence sentences. We use Re-DocRED~\\citep{tan2022redocred} for cross-dataset generalization evaluation.\n\n\\paragraph{Models.}\nOur primary model is Qwen3-4B. To study scale effects, we additionally train Qwen3-1.7B and Qwen3-8B under identical configurations. We include LLaMA-3.1-8B as a cross-family validation point.\n\n\\paragraph{Training.}\nAll models use LoRA~\\citep{hu2022lora} with rank $r{=}64$ and $\\alpha{=}128$ over a structured output format that jointly produces relation triples and evidence sentences. For RSFT, we sample $N{=}8$ candidate outputs per document and select the top-$k{=}1$ response ranked by CED scoring (\\S\\ref{sec:ced}), which combines NLI-based evidence faithfulness with extraction accuracy. GRPO experiments use group sizes $G{=}4$ (QLoRA, 4-bit) and $G{=}8$ (bf16 full-precision LoRA). DPO constructs preference pairs from CED-ranked outputs.\n\n\\paragraph{Metrics.}\n\\textbf{Ign-F1} (primary) ignores training-set triples per the official DocRED protocol. \\textbf{Rel-F1} measures extraction F1 on all triples. \\textbf{Evi-F1 (TP-only)} measures evidence F1 conditioned on correct triples; \\textbf{Evi-F1 (joint)} follows the DREEAM protocol~\\citep{ma2023dreeam} for cross-method comparison. \\textbf{EDCR} (\\S\\ref{sec:edcr}) diagnoses extraction-evidence decoupling. All results use the development set.\n\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main} presents the primary comparison on Qwen3-4B. The SFT baseline exhibits high seed sensitivity (mean Ign-F1 43.58, std 3.80pp, range 39.74--47.34). Removing evidence entirely (no-evidence SFT, s42) reaches 47.21 Ign-F1.\n\nRSFT CED achieves 44.82 Ign-F1 (+1.24 over SFT mean) with substantially lower variance (std 0.51pp), though these reflect different sources of variation (Section~\\ref{sec:scaling}). Even the weakest RSFT seed (44.23) exceeds the SFT mean. Evidence quality improves (Evi-F1 80.96 vs.\\ 79.61) and coupling tightens (EDCR 0.6487 vs.\\ 0.6797). Per-seed results appear in Appendix~\\ref{sec:ablation_full}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results on DocRED dev (Qwen3-4B). Ign-F1 shows mean $\\pm$ std$^{(\\text{seeds})}$; other metrics are same-seed means. Best \\textbf{bold}; best evidence-generating \\underline{underlined}. Per-seed: Appendix~\\ref{tab:ablation_full}.}\n\\label{tab:main}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Ign-F1} & \\textbf{Rel-F1} & \\textbf{Evi-F1} & \\textbf{EDCR} \\\\\n\\midrule\nSFT baseline & 43.58{\\scriptsize$\\pm$3.80}$^{(3)}$ & 44.39 & 79.61 & 0.6797 \\\\\nSFT no-evidence & \\textbf{47.21} & \\textbf{48.76} & -- & -- \\\\\nRSFT CED & \\underline{44.82{\\scriptsize$\\pm$0.51}$^{(3)}$} & \\underline{45.80} & 80.96 & 0.6487 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\vspace{-2mm}\n\\end{table}\n\n\n\\subsection{Evidence-Extraction Decoupling Spectrum}\n\\label{sec:spectrum}\n\nDifferent RL algorithms produce qualitatively different failure modes when applied to joint evidence-and-extraction generation. We organize these outcomes along a \\emph{decoupling spectrum} ranging from catastrophic collapse to mild perturbation, shown in Table~\\ref{tab:spectrum} (visualized in Figure~\\ref{fig:spectrum}, Appendix).\n\n\\paragraph{GRPO QLoRA: catastrophic collapse.}\nUnder 4-bit quantization ($G{=}4$), GRPO drives Rel-F1 to 1.38 while Evi-F1 rises to 85.04 (EDCR 0.9876): the model produces well-formed evidence but loses extraction capability. This extreme decoupling co-occurs with constrained precision; full-precision GRPO (below) avoids it.\n\n\\paragraph{GRPO bf16: mild, variable.}\nFull-precision GRPO ($G{=}8$) avoids catastrophe, with the best checkpoint achieving Rel-F1 45.49, Evi-F1 80.86, and EDCR 0.6318 (below SFT baseline 0.6797). Both sub-tasks improve jointly, though the variable training trajectory requires careful checkpoint selection.\n\n\\paragraph{DPO: gradual decay.}\nDPO progressively trades extraction for evidence: Rel-F1 drops from 40.34 (1 epoch) to 34.29 (3 epochs)\\footnote{DPO 3-epoch results use an earlier evaluation protocol; included for trend analysis.} while evidence improves (Evi-F1 80.88$\\to$84.03, EDCR 0.7139$\\to$0.7294).\n\n\\paragraph{RSFT: no decoupling.}\nRSFT maintains both capabilities simultaneously (Rel-F1 45.80, Evi-F1 80.96, EDCR 0.6487) because discrete output selection cannot exploit the extraction-evidence trade-off that gradient methods find.\n\n\\begin{table}[t]\n\\centering\n\\caption{Evidence-extraction decoupling across RL paradigms (Qwen3-4B). Severity indicates the degree of extraction collapse relative to evidence improvement.}\n\\label{tab:spectrum}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Paradigm} & \\textbf{Config} & \\textbf{Rel-F1} & \\textbf{Evi-F1} & \\textbf{EDCR} & \\textbf{Severity} \\\\\n\\midrule\nGRPO & QLoRA $G{=}4$ & 1.38 & 85.04 & 0.9876 & Catastrophic \\\\\nGRPO & bf16 $G{=}8$ & 45.49 & 80.86 & 0.6318 & Mild \\\\\nDPO & bf16 1ep & 40.34 & 80.88 & 0.7139 & Gradual \\\\\nDPO & bf16 3ep$^\\dagger$ & 34.29 & 84.03 & 0.7294 & Gradual \\\\\n\\midrule\nSFT & baseline$^\\ddagger$ & 44.39 & 79.61 & 0.6797 & None \\\\\nRSFT & CED$^\\ddagger$ & 45.80 & 80.96 & 0.6487 & None \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\vspace{-2mm}\n{\\raggedright\\footnotesize $^\\dagger$Earlier evaluation protocol. $^\\ddagger$Three-seed mean. Severity reflects training trajectory stability (propensity for extraction collapse during optimization), not the final-checkpoint EDCR value.\\par}\n\\end{table}\n\n\n\\subsection{Scale-Dependent Evidence Tax}\n\\label{sec:scaling}\n\nThe evidence tax, defined as Ign-F1(no-evidence) $-$ Ign-F1(with-evidence) on the development set, is scale-dependent. Under matched evaluation conditions (\\texttt{max\\_new\\_tokens}$=$2048, format-compliant intersection; Appendix~\\ref{sec:training_tax}), the training-time tax reveals a within-family capacity threshold: evidence generation benefits 1.7B ($-$5.63pp; Appendix~\\ref{sec:training_tax}) through implicit regularization that forces attention to supporting context, but is approximately neutral at $\\geq$4B (+0.25$\\pm$0.47pp at 4B, $n{=}3$; +0.04pp at 8B; +0.03pp at 14B). Table~\\ref{tab:scaling} presents RSFT performance and inference-time evidence tax across five models (Figure~\\ref{fig:scaling} in Appendix).\n\nRSFT navigates this capacity landscape through quality-based data selection rather than gradient pressure. Mean Ign-F1 improves across tested scales: +6.55pp at 1.7B, +1.24pp at 4B, +4.33pp at 8B, and +3.79pp at 14B (Table~\\ref{tab:scaling}). RSFT from an independent SFT base (s44, Method B) achieves 51.52 Ign-F1 at 4B (+4.18pp over that base). This result confirms that RSFT gains are not contingent on a specific SFT checkpoint.\n\nBeyond mean performance, RSFT substantially improves training reliability. Three RSFT seeds from a shared SFT checkpoint yield standard deviations of 0.09pp at 1.7B, 0.51pp at 4B, and 0.19pp at 8B ($n{=}3$ each), compared to SFT cross-seed variation of 2.79pp, 3.80pp, and 3.23pp respectively. While these measure different sources of variance (SFT reflects full training runs from different random seeds; RSFT reflects additional fine-tuning from a fixed base), the practical consequence is direct: within-scale variance compression is 31$\\times$ at 1.7B, 7.5$\\times$ at 4B, and 17$\\times$ at 8B. The 1.7B RSFT model (51.19 Ign-F1, std 0.09pp) is both more accurate and more predictable than the 8B SFT model (50.19, std 3.23pp), achieving +1.0pp higher mean at 4.7$\\times$ fewer parameters (cross-scale compression 36$\\times$). Cross-family, LLaMA-3.1-8B exhibits complete pairwise seed separation: all RSFT seeds (55.87--57.14) exceed all SFT seeds (48.02--53.84), with Cohen's $d{=}2.58$ and 4.6$\\times$ variance compression (std 2.92pp $\\to$ 0.64pp). The SFT seed lottery is starkest at LLaMA s44 (48.02 Ign-F1, 24.4\\% truncation rate, elevated Evi-F1 85\\%), a degenerate outcome that RSFT eliminates entirely (s44: 55.87). This robustness extends to inference-time format changes: LLaMA SFT models evaluated without evidence at 1024 tokens suffer 38--42\\% truncation with Ign-F1 collapsing to ${\\sim}$0.33 (s43/s44), while RSFT models under identical conditions truncate only 18--19\\% with stable performance (55.41$\\pm$0.13pp), indicating that CED filtering selects for compact output structure.\n\nFor RSFT models, the inference-time evidence tax (same model evaluated with vs.\\ without evidence output) preserves the benefit direction at 1.7B ($-$7.75pp, confirmed with 2048-token no-evidence evaluation that rules out truncation). At 4B, where the training-time tax is approximately neutral (+0.25$\\pm$0.47pp; Appendix~\\ref{sec:training_tax}), the RSFT inference-time tax is similarly small (+0.94pp). At 8B, the tax reverses to a benefit ($-$0.78pp), and at 14B the benefit is largest ($-$4.54pp). RSFT thus maintains or improves extraction quality with evidence across the Qwen3 family. LLaMA-3.1-8B RSFT shows a larger inference-time evidence benefit ($-$2.17$\\pm$0.76pp, three-seed mean, vs.\\ $-$0.78pp for Qwen3-8B), confirming that both performance gains and training reliability generalize across model families.\n\n\\begin{table}[t]\n\\centering\n\\caption{RSFT performance and inference-time evidence tax across model scales (DocRED dev Ign-F1). Mean $\\pm$ std$^{(\\text{seeds})}$.}\n\\label{tab:scaling}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{SFT w/ evi} & \\textbf{RSFT} & \\textbf{RSFT Tax}$^\\dagger$ & \\textbf{RSFT Gain} \\\\\n\\midrule\nQwen3-1.7B & 44.64{\\scriptsize$\\pm$2.79}$^{(3)}$ & 51.19{\\scriptsize$\\pm$0.09}$^{(3)}$ & $-$7.75 & +6.55 \\\\\nQwen3-4B & 43.58{\\scriptsize$\\pm$3.80}$^{(3)}$ & 44.82{\\scriptsize$\\pm$0.51}$^{(3)}$ & +0.94 & +1.24 \\\\\nQwen3-8B & 50.19{\\scriptsize$\\pm$3.23}$^{(3)}$ & 54.52{\\scriptsize$\\pm$0.19}$^{(3)}$ & $-$0.78 & +4.33 \\\\\nQwen3-14B & 55.07 & 58.86 & $-$4.54 & +3.79 \\\\\nLLaMA-3.1-8B & 51.09{\\scriptsize$\\pm$2.92}$^{(3)}$ & 56.54{\\scriptsize$\\pm$0.64}$^{(3)}$ & $-$2.17{\\scriptsize$\\pm$0.76}$^{(3)}$ & +5.45 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\vspace{-2mm}\n{\\raggedright\\footnotesize $^\\dagger$Inference-time: same RSFT model with vs.\\ without evidence output. No-evi eval uses \\texttt{max\\_new\\_tokens}$=$2048; with-evi eval uses 1024 (1.7B uses 2048 for both). Tax $=$ no-evi $-$ with-evi; positive $=$ cost. Seeds: 1.7B s42; 4B Method B s44; 8B, 14B: s42; LLaMA: three-seed mean. Training-time tax (matched@2048 fair evaluation) in Appendix~\\ref{sec:training_tax}.\\par}\n\\end{table}\n\n\n\\subsection{Evidence Strategy Comparison}\n\\label{sec:evidence_strategy}\n\nWe compare joint generation against post-hoc BM25 retrieval (entity-constrained, $k{=}2$), using Evi-F1 (joint) with the DREEAM-protocol denominator~\\citep{ma2023dreeam}. Post-hoc retrieval achieves higher Rel-F1 (48.76) by avoiding the evidence tax but lower Evi-F1 (joint) of 34.7 (EDCR 0.766). RSFT CED reaches 36.1 (EDCR 0.654), a 1.4-point evidence advantage. CED reranking at inference (best-of-$N{=}8$ by CED score) achieves Rel-F1 48.64 and Evi-F1 81.88 (TP-only), approaching no-evidence extraction quality while preserving evidence.\n\n\n\\subsection{Generalization}\n\\label{sec:generalization}\n\nCross-architecture validation on LLaMA-3.1-8B (Table~\\ref{tab:scaling}) shows the largest RSFT gain (+5.45pp) with complete pairwise seed separation (\\S\\ref{sec:scaling}). The RSFT improvement transfers across datasets: on Re-DocRED~\\citep{tan2022redocred}, RSFT achieves 41.45 Ign-F1 (+4.86pp over SFT 36.59), matching the DocRED gain (+5.08pp). Our best joint Evi-F1 (36.1, DREEAM-protocol) falls below supervised DREEAM (54.01\\%~\\citep{ma2023dreeam}), a gap driven by extraction performance rather than evidence quality (TP-only Evi-F1 exceeds 80\\%). Full results appear in Appendix~\\ref{sec:generalization_full}.\n",
      "numLines": 133,
      "startLine": 1,
      "totalLines": 133
    }
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01N3Q8PJeH7xzfhcVLRA7wFV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "489c4ddc-d80a-4821-8b06-1249d20d1fcf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kb3KWGwkN3YkxDwwScf4C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1321,
      "cache_read_input_tokens": 77968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1321
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

_source line 52 · 2026-05-21T22:56:39.360Z_

<details><summary>↩ Tool result · `toolu_01N3Q8PJeH7xzfhcVLRA7wFV`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task: Evidence-Grounded Document-Level Relation Extraction}
5	\label{sec:task}
6	
7	Given a document $D = \{s_1, \ldots, s_n\}$ consisting of $n$ sentences and a set of entities $\mathcal{E}$ identified within $D$, the task of evidence-grounded document-level relation extraction (DocRE) requires predicting, for each entity pair $(e_h, e_t) \in \mathcal{E} \times \mathcal{E}$, a relation $r \in \mathcal{R} \cup \{\texttt{NA}\}$ together with a set of supporting evidence sentences $E \subseteq D$. Standard DocRE predicts only the triple $(e_h, r, e_t)$; the evidence-grounded formulation also requires $E$, which grounds each prediction in specific textual support.
8	
9	In our LLM-based approach, the model generates structured outputs that jointly encode both components. For each predicted relation, the output follows the format \texttt{(head, relation, tail) | Evidence: [S$i$][S$j$]}, requiring the model to produce complete evidence references inline with each triple rather than as a separate retrieval step. This design contrasts with encoder-based evidence methods such as SAIS~\citep{xiao2022sais} and DREEAM~\citep{ma2023dreeam}, which frame evidence identification as sentence-level binary classification. Because classification over a fixed sentence set does not increase output length, these methods incur no generation overhead. Our LLM formulation requires additional tokens for each evidence reference, creating a generation burden that scales with the number of predicted triples and their evidence sentences. This scale-dependent cost is the central phenomenon we investigate.
10	
11	
12	\subsection{Supervised Fine-Tuning Baseline}
13	\label{sec:sft}
14	
15	We fine-tune all models with LoRA~\citep{hu2022lora} at rank $r{=}64$ and scaling factor $\alpha{=}128$, applied to all linear projections (attention and feed-forward). The training data consists of DocRED~\citep{yao2019docred} training documents converted to the structured output format described above, where each example maps a document and its entity set to the complete set of relation triples with evidence annotations. We also train a \emph{no-evidence} variant under identical configuration but with evidence references removed from the output format, producing only \texttt{(head, relation, tail)}. This variant serves as an upper bound on extraction performance by eliminating the generation cost of evidence, and allows direct measurement of the evidence tax at each model scale. Detailed hyperparameters (learning rate, batch size, number of epochs) are reported in the Appendix.
16	
17	
18	\subsection{Optimization Paradigms}
19	\label{sec:paradigms}
20	
21	We evaluate three post-SFT optimization paradigms that differ in how they incorporate quality signals from the CED scoring function (\S\ref{sec:ced}).
22	
23	\paragraph{GRPO.}
24	Group Relative Policy Optimization~\citep{shao2024deepseekmath} is an online RL method that eliminates the need for a separate value network by computing advantages within groups of sampled outputs. For each training document, the policy generates $G$ candidate responses, which are scored by CED. The advantage of each response is computed relative to the group mean, and the policy is updated to increase the probability of above-average outputs. We test two configurations: QLoRA with $G{=}4$ groups under 4-bit quantization, and bf16 full-precision LoRA with $G{=}8$. Because GRPO applies gradient updates that directly optimize the reward signal, evidence quality and extraction accuracy compete for gradient capacity. We analyze this multi-objective tension in Section~\ref{sec:spectrum}.
25	
26	\paragraph{DPO.}
27	Direct Preference Optimization~\citep{rafailov2023direct} reformulates RLHF as a classification problem over preference pairs, without explicit reward models. We construct preference data from the SFT model's sampled outputs: for each document, the response with the highest CED score is labeled as preferred and the lowest-scoring response as rejected. DPO then adjusts the policy to increase the log-probability ratio between preferred and rejected completions. We train for 1 and 3 epochs to observe the temporal dynamics of evidence-extraction trade-offs under implicit optimization.
28	
29	\paragraph{RSFT.}
30	Rejection Sampling Fine-Tuning is a single-round variant of iterative self-improvement methods such as STaR~\citep{zelikman2022star}. The procedure is straightforward: the SFT model generates $N{=}8$ candidate outputs per training document, each candidate is scored by CED, and only the top-$k{=}1$ response is retained as training data. We use $k{=}1$ (best-of-$N$) selection throughout all experiments, selecting the single highest-scoring candidate per document for RSFT training data construction. This yields approximately 3,000 training examples per model (one per document; exact counts vary slightly by model due to generation failures). Unlike GRPO and DPO, RSFT does not apply gradient-based optimization pressure toward a reward signal. Instead, it improves training data quality through filtering: the model trains on its own best outputs rather than all outputs. This distinction is critical because discrete selection over complete outputs cannot exploit the extraction-evidence trade-off that gradient methods find. The contribution of RSFT in our setting is not the framework itself, which is well-established, but its application to evidence-grounded DocRE with CED as a domain-specific quality filter.
31	
32	
33	\subsection{Contrastive Evidence Discrimination}
34	\label{sec:ced}
35	
36	CED is a scoring function that evaluates the faithfulness of predicted evidence sentences to their associated relation triples. It builds on Natural Language Inference (NLI) to measure whether evidence actually entails the predicted relation, rather than merely co-occurring with the relevant entities.
37	
38	For a predicted triple $(e_h, r, e_t)$ with evidence sentences $E$, CED constructs a positive NLI pair: the premise is the concatenation of sentences in $E$, and the hypothesis is a natural-language verbalization of the relation (e.g., ``$e_h$ has relation $r$ with $e_t$''). An NLI model (\texttt{cross-encoder/nli-deberta-v3-base}) produces an entailment probability $p^+$ for this pair. The contrastive component introduces hard negatives drawn from the same document. For each triple, we collect sentences that mention $e_h$ or $e_t$ but are not in the predicted evidence set. These entity-sharing distractors serve as negative premises, and the NLI model scores each to obtain $p^-_1, \ldots, p^-_m$. The CED score for a single triple is:
39	\begin{equation}
40	\text{CED}(e_h, r, e_t, E) = p^+ - \max_j \, p^-_j
41	\label{eq:ced}
42	\end{equation}
43	This formulation forces the scoring function to distinguish sentences that genuinely support the relation from sentences that merely mention the same entities. A high CED score indicates that the evidence provides relation-specific support beyond entity co-occurrence.
44	
45	The document-level CED score aggregates over all predicted triples, weighted by extraction correctness: triples that match ground-truth relations contribute their CED scores, while incorrect triples receive zero credit. This coupling ensures that CED rewards both faithful evidence and accurate extraction jointly.
46	
47	We also evaluate a \emph{flat-NLI} baseline that uses only the positive entailment score $p^+$ without the contrastive term. CED and flat-NLI produce comparable RSFT outcomes (mean Rel-F1 difference of 0.02pp across available seeds; Section~\ref{sec:analysis}), confirming that the contrastive formulation is not essential for data selection quality. We adopt CED as the default because its per-triple discrimination scores support interpretable error analysis.
48	
49	
50	\subsection{Evidence-Decoupling Ratio}
51	\label{sec:edcr}
52	
53	We introduce the Evidence-Decoupling Ratio (EDCR) as a diagnostic metric that quantifies the degree of misalignment between a model's extraction and evidence capabilities. EDCR is not a training component; it serves purely as an analytical tool for comparing optimization methods.
54	
55	EDCR is defined as:
56	\begin{equation}
57	\text{EDCR} = \frac{\text{Evi-Recall}_{\text{TP}}}{\text{Rel-Recall}}
58	\label{eq:edcr}
59	\end{equation}
60	where $\text{Evi-Recall}_{\text{TP}}$ is evidence sentence recall computed only over correctly predicted triples (true positives), and $\text{Rel-Recall}$ is overall relation extraction recall. The numerator captures evidence quality on the subset of triples the model gets right; the denominator captures how many triples the model identifies in total.
61	
62	The intuition is as follows. A model that correctly identifies a few triples and provides excellent evidence for them, but misses most triples entirely, will have high $\text{Evi-Recall}_{\text{TP}}$ and low $\text{Rel-Recall}$, yielding a high EDCR. This pattern signals that evidence quality has decoupled from extraction capability: the model produces faithful evidence only within a narrow comfort zone.
63	
64	EDCR operates at two diagnostic levels. At the method level, comparing EDCR across seven independent method configurations reveals a negative correlation with Rel-F1 (Spearman $\rho{=}{-}0.89$, $n{=}7$, $p{=}0.007$). Because EDCR shares Rel-Recall with Rel-F1 by construction, this correlation should be interpreted as a diagnostic pattern rather than an independent discovery; its primary value lies in per-relation analysis. We validate EDCR's diagnostic utility through per-relation analysis (\S\ref{sec:analysis}), which avoids the shared-component concern present in cross-method correlation. At the per-relation level, computing EDCR for individual relation types reveals a robust negative correlation with Rel-F1 ($\rho{=}{-}0.79$, $n{=}76$, $p{<}0.001$) that is independent of Evi-F1 ($\rho{=}{-}0.06$, $p{=}0.58$). This independence means EDCR captures relation-specific extraction-evidence misalignment that aggregate evidence metrics miss. The SFT baseline EDCR (0.6982) reflects the inherent cost of evidence generation; EDCR values substantially exceeding this level (e.g., GRPO QLoRA at 0.9876) indicate RL-induced decoupling beyond what evidence production alone explains, while values below the baseline (e.g., RSFT at 0.6503) reflect improved co-optimization.
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "ae53ccb0-ea4f-4bca-beac-36b807f46fad",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task: Evidence-Grounded Document-Level Relation Extraction}\n\\label{sec:task}\n\nGiven a document $D = \\{s_1, \\ldots, s_n\\}$ consisting of $n$ sentences and a set of entities $\\mathcal{E}$ identified within $D$, the task of evidence-grounded document-level relation extraction (DocRE) requires predicting, for each entity pair $(e_h, e_t) \\in \\mathcal{E} \\times \\mathcal{E}$, a relation $r \\in \\mathcal{R} \\cup \\{\\texttt{NA}\\}$ together with a set of supporting evidence sentences $E \\subseteq D$. Standard DocRE predicts only the triple $(e_h, r, e_t)$; the evidence-grounded formulation also requires $E$, which grounds each prediction in specific textual support.\n\nIn our LLM-based approach, the model generates structured outputs that jointly encode both components. For each predicted relation, the output follows the format \\texttt{(head, relation, tail) | Evidence: [S$i$][S$j$]}, requiring the model to produce complete evidence references inline with each triple rather than as a separate retrieval step. This design contrasts with encoder-based evidence methods such as SAIS~\\citep{xiao2022sais} and DREEAM~\\citep{ma2023dreeam}, which frame evidence identification as sentence-level binary classification. Because classification over a fixed sentence set does not increase output length, these methods incur no generation overhead. Our LLM formulation requires additional tokens for each evidence reference, creating a generation burden that scales with the number of predicted triples and their evidence sentences. This scale-dependent cost is the central phenomenon we investigate.\n\n\n\\subsection{Supervised Fine-Tuning Baseline}\n\\label{sec:sft}\n\nWe fine-tune all models with LoRA~\\citep{hu2022lora} at rank $r{=}64$ and scaling factor $\\alpha{=}128$, applied to all linear projections (attention and feed-forward). The training data consists of DocRED~\\citep{yao2019docred} training documents converted to the structured output format described above, where each example maps a document and its entity set to the complete set of relation triples with evidence annotations. We also train a \\emph{no-evidence} variant under identical configuration but with evidence references removed from the output format, producing only \\texttt{(head, relation, tail)}. This variant serves as an upper bound on extraction performance by eliminating the generation cost of evidence, and allows direct measurement of the evidence tax at each model scale. Detailed hyperparameters (learning rate, batch size, number of epochs) are reported in the Appendix.\n\n\n\\subsection{Optimization Paradigms}\n\\label{sec:paradigms}\n\nWe evaluate three post-SFT optimization paradigms that differ in how they incorporate quality signals from the CED scoring function (\\S\\ref{sec:ced}).\n\n\\paragraph{GRPO.}\nGroup Relative Policy Optimization~\\citep{shao2024deepseekmath} is an online RL method that eliminates the need for a separate value network by computing advantages within groups of sampled outputs. For each training document, the policy generates $G$ candidate responses, which are scored by CED. The advantage of each response is computed relative to the group mean, and the policy is updated to increase the probability of above-average outputs. We test two configurations: QLoRA with $G{=}4$ groups under 4-bit quantization, and bf16 full-precision LoRA with $G{=}8$. Because GRPO applies gradient updates that directly optimize the reward signal, evidence quality and extraction accuracy compete for gradient capacity. We analyze this multi-objective tension in Section~\\ref{sec:spectrum}.\n\n\\paragraph{DPO.}\nDirect Preference Optimization~\\citep{rafailov2023direct} reformulates RLHF as a classification problem over preference pairs, without explicit reward models. We construct preference data from the SFT model's sampled outputs: for each document, the response with the highest CED score is labeled as preferred and the lowest-scoring response as rejected. DPO then adjusts the policy to increase the log-probability ratio between preferred and rejected completions. We train for 1 and 3 epochs to observe the temporal dynamics of evidence-extraction trade-offs under implicit optimization.\n\n\\paragraph{RSFT.}\nRejection Sampling Fine-Tuning is a single-round variant of iterative self-improvement methods such as STaR~\\citep{zelikman2022star}. The procedure is straightforward: the SFT model generates $N{=}8$ candidate outputs per training document, each candidate is scored by CED, and only the top-$k{=}1$ response is retained as training data. We use $k{=}1$ (best-of-$N$) selection throughout all experiments, selecting the single highest-scoring candidate per document for RSFT training data construction. This yields approximately 3,000 training examples per model (one per document; exact counts vary slightly by model due to generation failures). Unlike GRPO and DPO, RSFT does not apply gradient-based optimization pressure toward a reward signal. Instead, it improves training data quality through filtering: the model trains on its own best outputs rather than all outputs. This distinction is critical because discrete selection over complete outputs cannot exploit the extraction-evidence trade-off that gradient methods find. The contribution of RSFT in our setting is not the framework itself, which is well-established, but its application to evidence-grounded DocRE with CED as a domain-specific quality filter.\n\n\n\\subsection{Contrastive Evidence Discrimination}\n\\label{sec:ced}\n\nCED is a scoring function that evaluates the faithfulness of predicted evidence sentences to their associated relation triples. It builds on Natural Language Inference (NLI) to measure whether evidence actually entails the predicted relation, rather than merely co-occurring with the relevant entities.\n\nFor a predicted triple $(e_h, r, e_t)$ with evidence sentences $E$, CED constructs a positive NLI pair: the premise is the concatenation of sentences in $E$, and the hypothesis is a natural-language verbalization of the relation (e.g., ``$e_h$ has relation $r$ with $e_t$''). An NLI model (\\texttt{cross-encoder/nli-deberta-v3-base}) produces an entailment probability $p^+$ for this pair. The contrastive component introduces hard negatives drawn from the same document. For each triple, we collect sentences that mention $e_h$ or $e_t$ but are not in the predicted evidence set. These entity-sharing distractors serve as negative premises, and the NLI model scores each to obtain $p^-_1, \\ldots, p^-_m$. The CED score for a single triple is:\n\\begin{equation}\n\\text{CED}(e_h, r, e_t, E) = p^+ - \\max_j \\, p^-_j\n\\label{eq:ced}\n\\end{equation}\nThis formulation forces the scoring function to distinguish sentences that genuinely support the relation from sentences that merely mention the same entities. A high CED score indicates that the evidence provides relation-specific support beyond entity co-occurrence.\n\nThe document-level CED score aggregates over all predicted triples, weighted by extraction correctness: triples that match ground-truth relations contribute their CED scores, while incorrect triples receive zero credit. This coupling ensures that CED rewards both faithful evidence and accurate extraction jointly.\n\nWe also evaluate a \\emph{flat-NLI} baseline that uses only the positive entailment score $p^+$ without the contrastive term. CED and flat-NLI produce comparable RSFT outcomes (mean Rel-F1 difference of 0.02pp across available seeds; Section~\\ref{sec:analysis}), confirming that the contrastive formulation is not essential for data selection quality. We adopt CED as the default because its per-triple discrimination scores support interpretable error analysis.\n\n\n\\subsection{Evidence-Decoupling Ratio}\n\\label{sec:edcr}\n\nWe introduce the Evidence-Decoupling Ratio (EDCR) as a diagnostic metric that quantifies the degree of misalignment between a model's extraction and evidence capabilities. EDCR is not a training component; it serves purely as an analytical tool for comparing optimization methods.\n\nEDCR is defined as:\n\\begin{equation}\n\\text{EDCR} = \\frac{\\text{Evi-Recall}_{\\text{TP}}}{\\text{Rel-Recall}}\n\\label{eq:edcr}\n\\end{equation}\nwhere $\\text{Evi-Recall}_{\\text{TP}}$ is evidence sentence recall computed only over correctly predicted triples (true positives), and $\\text{Rel-Recall}$ is overall relation extraction recall. The numerator captures evidence quality on the subset of triples the model gets right; the denominator captures how many triples the model identifies in total.\n\nThe intuition is as follows. A model that correctly identifies a few triples and provides excellent evidence for them, but misses most triples entirely, will have high $\\text{Evi-Recall}_{\\text{TP}}$ and low $\\text{Rel-Recall}$, yielding a high EDCR. This pattern signals that evidence quality has decoupled from extraction capability: the model produces faithful evidence only within a narrow comfort zone.\n\nEDCR operates at two diagnostic levels. At the method level, comparing EDCR across seven independent method configurations reveals a negative correlation with Rel-F1 (Spearman $\\rho{=}{-}0.89$, $n{=}7$, $p{=}0.007$). Because EDCR shares Rel-Recall with Rel-F1 by construction, this correlation should be interpreted as a diagnostic pattern rather than an independent discovery; its primary value lies in per-relation analysis. We validate EDCR's diagnostic utility through per-relation analysis (\\S\\ref{sec:analysis}), which avoids the shared-component concern present in cross-method correlation. At the per-relation level, computing EDCR for individual relation types reveals a robust negative correlation with Rel-F1 ($\\rho{=}{-}0.79$, $n{=}76$, $p{<}0.001$) that is independent of Evi-F1 ($\\rho{=}{-}0.06$, $p{=}0.58$). This independence means EDCR captures relation-specific extraction-evidence misalignment that aggregate evidence metrics miss. The SFT baseline EDCR (0.6982) reflects the inherent cost of evidence generation; EDCR values substantially exceeding this level (e.g., GRPO QLoRA at 0.9876) indicate RL-induced decoupling beyond what evidence production alone explains, while values below the baseline (e.g., RSFT at 0.6503) reflect improved co-optimization.\n",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Read · `toolu_01SjkAbWt2opF1icPtmKKyD9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "c0fd3799-9c60-4de3-a0eb-407b386abfa9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kb3KWGwkN3YkxDwwScf4C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1321,
      "cache_read_input_tokens": 77968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1321
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

_source line 54 · 2026-05-21T22:56:39.786Z_

<details><summary>↩ Tool result · `toolu_01SjkAbWt2opF1icPtmKKyD9`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Document-level relation extraction (DocRE) requires reasoning across sentence boundaries to identify relations between entity pairs.
5	DocRED \citep{yao2019docred} established the first large-scale benchmark for this task, catalyzing a line of encoder-based methods that treat DocRE as classification over entity pair representations.
6	ATLOP \citep{zhou2021atlop} introduced adaptive thresholding for multi-label prediction and localized context pooling for entity representations.
7	A parallel thread incorporates sentence-level evidence into these architectures.
8	SAIS \citep{xiao2022sais} introduced evidence supervision as an auxiliary training signal and showed that joint evidence prediction improves extraction through data augmentation and ensemble inference.
9	DREEAM \citep{ma2023dreeam} extended this approach with dynamic memory-based evidence retrieval that guides attention to supporting sentences.
10	EIDER \citep{xie2022eider} jointly trains an evidence extractor and fuses evidence representations into the relation classifier.
11	In all three systems, evidence identification is binary sentence classification over a fixed candidate set, a formulation that adds no output complexity.
12	Recent work has recast DocRE for large language models.
13	AutoRE \citep{autore2024} fine-tunes LLMs with QLoRA using a relation-head-facts decomposition; \citet{xu2024lmrc} frame extraction as multi-choice reading comprehension; RelPrior \citep{wang2025relprior} uses relation priors to guide LLM-based extraction; GLiDRE \citep{zhang2025glidre} presents a generalist lightweight approach; Ru-LLM \citep{wang2025rullm} incorporates logical rule constraints; and \citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.
14	These methods match or surpass encoder baselines but produce bare triplets without evidence.
15	The critical distinction lies in computational nature: in SAIS and DREEAM, evidence retrieval is classification that regularizes the encoder without increasing output length; in LLM-based DocRE, evidence requires additional output tokens per triple, imposing costs that depend on model capacity and optimization strategy.
16	Whether this cost is inevitable or can be mitigated is the central question of our work.
17	
18	Group Relative Policy Optimization (GRPO; \citealt{shao2024deepseekmath}) eliminates the separate value network by computing advantages within groups.
19	Subsequent work addresses failure modes: DAPO \citep{yu2025dapo} prevents entropy collapse, Dr.\ GRPO \citep{liu2025drgrpo} corrects length bias, and multi-objective variants \citep{liu2026gdpo,ito2025mogrpo} handle competing reward signals.
20	Applications to structured IE include R1-RE \citep{dai2025r1re} and REAR \citep{wang2025rear}.
21	Direct Preference Optimization \citep{rafailov2023direct} reformulates RLHF as implicit reward maximization.
22	Our decoupling spectrum is distinct from catastrophic forgetting in RL alignment \citep{jin2025rl_panacea}, where models lose pre-trained capabilities across tasks; in our setting, extraction and evidence compete \emph{within} a single task, resembling negative transfer in multi-task learning \citep{ruder2017overview,standley2020tasks,yu2020gradient}, amplified by QLoRA's constrained parameter space \citep{gao2023scaling,moskovitz2024constrained}.
23	RSFT avoids this intra-task competition by operating on discrete outputs rather than gradients, extending the sample-and-select principle \citep{wang2023selfconsistency} to structured IE with joint quality scoring.
24	
25	Evidence faithfulness evaluation has received increasing attention: \citet{li2025drift} propose dual-reward inference for faithful rationale generation, and \citet{zhang2024infuse} introduce fine-grained NLI-based faithfulness metrics for summarization.
26	Our CED scoring builds on similar NLI-based principles but targets evidence-relation entailment rather than free-form rationales.
27	
28	\citet{zelikman2022star} introduced STaR for iterative self-improvement; \citet{dong2023raft} generalize this with reward-model-based sample filtering; recent analysis shows rejection sampling implicitly performs PPO-like optimization \citep{tang2025rsftppo}.
29	Our RSFT is a single-round variant applied to evidence-grounded DocRE with CED/NLI scoring as a domain-specific quality filter.
30	Because RSFT selects complete outputs rather than differentiating through a reward signal, it cannot exploit the extraction-evidence trade-off that gradient methods discover, inherently preserving joint quality.
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "cb55fb2f-27a1-480f-81a9-1dd634e558e0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\nDocument-level relation extraction (DocRE) requires reasoning across sentence boundaries to identify relations between entity pairs.\nDocRED \\citep{yao2019docred} established the first large-scale benchmark for this task, catalyzing a line of encoder-based methods that treat DocRE as classification over entity pair representations.\nATLOP \\citep{zhou2021atlop} introduced adaptive thresholding for multi-label prediction and localized context pooling for entity representations.\nA parallel thread incorporates sentence-level evidence into these architectures.\nSAIS \\citep{xiao2022sais} introduced evidence supervision as an auxiliary training signal and showed that joint evidence prediction improves extraction through data augmentation and ensemble inference.\nDREEAM \\citep{ma2023dreeam} extended this approach with dynamic memory-based evidence retrieval that guides attention to supporting sentences.\nEIDER \\citep{xie2022eider} jointly trains an evidence extractor and fuses evidence representations into the relation classifier.\nIn all three systems, evidence identification is binary sentence classification over a fixed candidate set, a formulation that adds no output complexity.\nRecent work has recast DocRE for large language models.\nAutoRE \\citep{autore2024} fine-tunes LLMs with QLoRA using a relation-head-facts decomposition; \\citet{xu2024lmrc} frame extraction as multi-choice reading comprehension; RelPrior \\citep{wang2025relprior} uses relation priors to guide LLM-based extraction; GLiDRE \\citep{zhang2025glidre} presents a generalist lightweight approach; Ru-LLM \\citep{wang2025rullm} incorporates logical rule constraints; and \\citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.\nThese methods match or surpass encoder baselines but produce bare triplets without evidence.\nThe critical distinction lies in computational nature: in SAIS and DREEAM, evidence retrieval is classification that regularizes the encoder without increasing output length; in LLM-based DocRE, evidence requires additional output tokens per triple, imposing costs that depend on model capacity and optimization strategy.\nWhether this cost is inevitable or can be mitigated is the central question of our work.\n\nGroup Relative Policy Optimization (GRPO; \\citealt{shao2024deepseekmath}) eliminates the separate value network by computing advantages within groups.\nSubsequent work addresses failure modes: DAPO \\citep{yu2025dapo} prevents entropy collapse, Dr.\\ GRPO \\citep{liu2025drgrpo} corrects length bias, and multi-objective variants \\citep{liu2026gdpo,ito2025mogrpo} handle competing reward signals.\nApplications to structured IE include R1-RE \\citep{dai2025r1re} and REAR \\citep{wang2025rear}.\nDirect Preference Optimization \\citep{rafailov2023direct} reformulates RLHF as implicit reward maximization.\nOur decoupling spectrum is distinct from catastrophic forgetting in RL alignment \\citep{jin2025rl_panacea}, where models lose pre-trained capabilities across tasks; in our setting, extraction and evidence compete \\emph{within} a single task, resembling negative transfer in multi-task learning \\citep{ruder2017overview,standley2020tasks,yu2020gradient}, amplified by QLoRA's constrained parameter space \\citep{gao2023scaling,moskovitz2024constrained}.\nRSFT avoids this intra-task competition by operating on discrete outputs rather than gradients, extending the sample-and-select principle \\citep{wang2023selfconsistency} to structured IE with joint quality scoring.\n\nEvidence faithfulness evaluation has received increasing attention: \\citet{li2025drift} propose dual-reward inference for faithful rationale generation, and \\citet{zhang2024infuse} introduce fine-grained NLI-based faithfulness metrics for summarization.\nOur CED scoring builds on similar NLI-based principles but targets evidence-relation entailment rather than free-form rationales.\n\n\\citet{zelikman2022star} introduced STaR for iterative self-improvement; \\citet{dong2023raft} generalize this with reward-model-based sample filtering; recent analysis shows rejection sampling implicitly performs PPO-like optimization \\citep{tang2025rsftppo}.\nOur RSFT is a single-round variant applied to evidence-grounded DocRE with CED/NLI scoring as a domain-specific quality filter.\nBecause RSFT selects complete outputs rather than differentiating through a reward signal, it cannot exploit the extraction-evidence trade-off that gradient methods discover, inherently preserving joint quality.\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_011Qt5rzoELABH3umNzbQoNh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "17ba28cd-b8b2-4b06-b191-213e53f0ada8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kb3KWGwkN3YkxDwwScf4C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1321,
      "cache_read_input_tokens": 77968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1321
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

_source line 56 · 2026-05-21T22:56:40.297Z_

<details><summary>↩ Tool result · `toolu_011Qt5rzoELABH3umNzbQoNh`</summary>

```text
1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\paragraph{EDCR as a diagnostic.}
5	EDCR (\S\ref{sec:edcr}) correlates with extraction quality at two levels: cross-method ($\rho = -0.89$, $n = 7$, $p = 0.007$; Table~\ref{tab:spectrum}) and per-relation ($\rho = -0.79$, $n = 76$, $p < 0.001$), the latter providing validation independent of method-level sample size and orthogonal to Evi-F1 ($\rho = -0.06$, $p = 0.58$; Appendix~\ref{sec:edcr_per_relation}). RSFT avoids decoupling because discrete output selection cannot exploit the extraction-evidence trade-off (Appendix~\ref{sec:rsft_theory}). CED operates effectively at the response level but fails at sentence-level granularity (Evi-F1 $-$7.7pp), as filtering individual sentences disrupts co-reference chains.
6	
7	\paragraph{Ablation.}
8	CED and flat-NLI produce comparable RSFT performance (Rel-F1 45.63 vs.\ 45.61); stricter selection ($k{=}1$) outperforms $k{=}3$ by 1.02 Ign-F1 despite 2.96$\times$ fewer examples; CED filtering is insensitive to NLI scorer capacity (+1.10pp with DeBERTa-v3-large vs.\ v3-base, within seed noise; Appendix~\ref{sec:ablation_full}).
9	
10	\paragraph{Error patterns.}
11	RSFT reduces truncation FN, hallucinated FP, and duplicates by 6--22\% across scales, but evidence quality is unchanged ($\Delta < 0.4$pp; Appendix~\ref{sec:error_analysis}). RSFT improves \emph{what} the model extracts but not \emph{how well} it grounds extractions.
12	
13	\paragraph{Practical implications.}
14	Three guidelines for evidence-grounded IE: (1) avoid online RL for multi-objective generation where capability coupling matters; (2) prefer RSFT with strict selection ($k{=}1$) over training data quantity (7.5--17$\times$ Qwen3 variance compression, 4.6$\times$ on LLaMA); (3) consider CED reranking at inference for deployment scenarios requiring both extraction accuracy and evidence quality.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "b4720bcf-6c52-4fd9-a1c0-0ae222945023",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex",
      "content": "\\section{Analysis}\n\\label{sec:analysis}\n\n\\paragraph{EDCR as a diagnostic.}\nEDCR (\\S\\ref{sec:edcr}) correlates with extraction quality at two levels: cross-method ($\\rho = -0.89$, $n = 7$, $p = 0.007$; Table~\\ref{tab:spectrum}) and per-relation ($\\rho = -0.79$, $n = 76$, $p < 0.001$), the latter providing validation independent of method-level sample size and orthogonal to Evi-F1 ($\\rho = -0.06$, $p = 0.58$; Appendix~\\ref{sec:edcr_per_relation}). RSFT avoids decoupling because discrete output selection cannot exploit the extraction-evidence trade-off (Appendix~\\ref{sec:rsft_theory}). CED operates effectively at the response level but fails at sentence-level granularity (Evi-F1 $-$7.7pp), as filtering individual sentences disrupts co-reference chains.\n\n\\paragraph{Ablation.}\nCED and flat-NLI produce comparable RSFT performance (Rel-F1 45.63 vs.\\ 45.61); stricter selection ($k{=}1$) outperforms $k{=}3$ by 1.02 Ign-F1 despite 2.96$\\times$ fewer examples; CED filtering is insensitive to NLI scorer capacity (+1.10pp with DeBERTa-v3-large vs.\\ v3-base, within seed noise; Appendix~\\ref{sec:ablation_full}).\n\n\\paragraph{Error patterns.}\nRSFT reduces truncation FN, hallucinated FP, and duplicates by 6--22\\% across scales, but evidence quality is unchanged ($\\Delta < 0.4$pp; Appendix~\\ref{sec:error_analysis}). RSFT improves \\emph{what} the model extracts but not \\emph{how well} it grounds extractions.\n\n\\paragraph{Practical implications.}\nThree guidelines for evidence-grounded IE: (1) avoid online RL for multi-objective generation where capability coupling matters; (2) prefer RSFT with strict selection ($k{=}1$) over training data quantity (7.5--17$\\times$ Qwen3 variance compression, 4.6$\\times$ on LLaMA); (3) consider CED reranking at inference for deployment scenarios requiring both extraction accuracy and evidence quality.\n",
      "numLines": 15,
      "startLine": 1,
      "totalLines": 15
    }
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_01GJEBgMbf2UhtuQGcHxK2kB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "70d66191-abb2-4cd6-9fa6-c397267d2fec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kb3KWGwkN3YkxDwwScf4C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1321,
      "cache_read_input_tokens": 77968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1321
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

_source line 58 · 2026-05-21T22:56:40.770Z_

<details><summary>↩ Tool result · `toolu_01GJEBgMbf2UhtuQGcHxK2kB`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We formalize evidence-grounded document-level relation extraction as a structured generation task and systematically compare three post-training paradigms across three fully evaluated scales (1.7B, 4B, 8B) with 14B validation, two model families, and two datasets. Our experiments reveal that evidence generation plays a scale-dependent role shaped by three interacting factors: model capacity determines whether evidence acts as regularizer ($-$5.63pp at 1.7B) or is approximately neutral ($\geq$4B; +0.25$\pm$0.47pp at 4B), optimization paradigm determines decoupling severity (GRPO catastrophic under QLoRA, DPO gradual, RSFT none), and data quality filtering through NLI-based scoring enables RSFT to navigate this landscape without gradient-induced trade-offs. RSFT improves mean Ign-F1 across tested scales (+1.2 to +6.6pp) while compressing Qwen3 training variance 7.5--17$\times$ and LLaMA variance 4.6$\times$ (complete pairwise seed separation, $d{=}2.58$). The resulting 1.7B RSFT model (51.19 Ign-F1, std 0.09pp) approaches 8B SFT performance (50.19, std 3.23pp) at 4.7$\times$ fewer parameters, providing both higher mean accuracy and substantially greater training reliability for deployment-efficient evidence-grounded extraction.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "960a240d-efb0-4d8f-a423-6b0afd36dea7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe formalize evidence-grounded document-level relation extraction as a structured generation task and systematically compare three post-training paradigms across three fully evaluated scales (1.7B, 4B, 8B) with 14B validation, two model families, and two datasets. Our experiments reveal that evidence generation plays a scale-dependent role shaped by three interacting factors: model capacity determines whether evidence acts as regularizer ($-$5.63pp at 1.7B) or is approximately neutral ($\\geq$4B; +0.25$\\pm$0.47pp at 4B), optimization paradigm determines decoupling severity (GRPO catastrophic under QLoRA, DPO gradual, RSFT none), and data quality filtering through NLI-based scoring enables RSFT to navigate this landscape without gradient-induced trade-offs. RSFT improves mean Ign-F1 across tested scales (+1.2 to +6.6pp) while compressing Qwen3 training variance 7.5--17$\\times$ and LLaMA variance 4.6$\\times$ (complete pairwise seed separation, $d{=}2.58$). The resulting 1.7B RSFT model (51.19 Ign-F1, std 0.09pp) approaches 8B SFT performance (50.19, std 3.23pp) at 4.7$\\times$ fewer parameters, providing both higher mean accuracy and substantially greater training reliability for deployment-efficient evidence-grounded extraction.\n",
      "numLines": 5,
      "startLine": 1,
      "totalLines": 5
    }
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Read · `toolu_01Ri6n4qjRQvbTS7cNcPTF77`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "4ee3b2f9-5f3d-44be-b0c5-b76982b3b0c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kb3KWGwkN3YkxDwwScf4C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1321,
      "cache_read_input_tokens": 77968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1321
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

_source line 60 · 2026-05-21T22:56:41.120Z_

<details><summary>↩ Tool result · `toolu_01Ri6n4qjRQvbTS7cNcPTF77`</summary>

```text
1	\section{Limitations}
2	
3	All results use the DocRED development set; test set submission is pending. Exact-match F1 penalizes surface-form-different entity mentions~\citep{wan2024genres}, likely underestimating absolute extraction capability of generative models, though relative comparisons between methods remain valid.
4	
5	We evaluate on two datasets (DocRED, Re-DocRED), both derived from Wikipedia. Cross-domain evaluation is constrained by the absence of evidence-annotated DocRE datasets beyond Wikipedia; this limitation is shared by all prior evidence-aware DocRE work (SAIS, DREEAM, EIDER).
6	
7	We evaluate one algorithm per RL family (GRPO, DPO) with single hyperparameter settings (KL coefficient 0.01, $\beta$ 0.1); other algorithms or settings may produce different decoupling behaviors. CED scoring depends on an external NLI model, and the RSFT ablation uses limited seeds (four for CED, two for flat-NLI). Evidence tax patterns span two model families (Qwen3, LLaMA) but may not generalize to other architectures or scales beyond 14B.
8	
9	EDCR correlates with extraction quality at both method level ($\rho{=}{-}0.89$, $n{=}7$) and per-relation level ($\rho{=}{-}0.79$, $n{=}76$), but has not been validated against human judgments of evidence-extraction alignment. Future work should assess whether EDCR rankings correspond to practitioner assessments of output quality.
10	
11	RSFT improves extraction across scales but evidence quality is unchanged (Evi-F1 $\Delta < 0.4$pp at all scales; Appendix~\ref{sec:error_analysis}). CED-based selection filters for joint quality but does not specifically optimize evidence grounding, suggesting that targeted evidence rewards may be needed to improve evidence quality beyond what data selection achieves.
12	
13	At 1.7B scale, 44.4\% of outputs exhibit repetitive patterns (vs.\ negligible at 4B+); small models may require decoding-time interventions (e.g., repetition penalty) for reliable deployment.
14	
15	\section{Ethics Statement}
16	
17	This work uses publicly available benchmarks (DocRED, Re-DocRED) derived from Wikipedia, containing no private or sensitive information. All models are trained on existing annotated data without human subjects involvement. Our evidence-grounding approach aims to improve the verifiability of relation extraction outputs, which supports responsible deployment in high-stakes domains such as clinical and legal information systems by enabling human verification of model predictions. We release code and model outputs to support reproducibility.
18	
19	% Responsible NLP Research Checklist: submitted via OpenReview form per ARR/EMNLP 2026 guidelines.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "9eab7502-b0f2-4301-b0b1-537eaafe383b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex",
      "content": "\\section{Limitations}\n\nAll results use the DocRED development set; test set submission is pending. Exact-match F1 penalizes surface-form-different entity mentions~\\citep{wan2024genres}, likely underestimating absolute extraction capability of generative models, though relative comparisons between methods remain valid.\n\nWe evaluate on two datasets (DocRED, Re-DocRED), both derived from Wikipedia. Cross-domain evaluation is constrained by the absence of evidence-annotated DocRE datasets beyond Wikipedia; this limitation is shared by all prior evidence-aware DocRE work (SAIS, DREEAM, EIDER).\n\nWe evaluate one algorithm per RL family (GRPO, DPO) with single hyperparameter settings (KL coefficient 0.01, $\\beta$ 0.1); other algorithms or settings may produce different decoupling behaviors. CED scoring depends on an external NLI model, and the RSFT ablation uses limited seeds (four for CED, two for flat-NLI). Evidence tax patterns span two model families (Qwen3, LLaMA) but may not generalize to other architectures or scales beyond 14B.\n\nEDCR correlates with extraction quality at both method level ($\\rho{=}{-}0.89$, $n{=}7$) and per-relation level ($\\rho{=}{-}0.79$, $n{=}76$), but has not been validated against human judgments of evidence-extraction alignment. Future work should assess whether EDCR rankings correspond to practitioner assessments of output quality.\n\nRSFT improves extraction across scales but evidence quality is unchanged (Evi-F1 $\\Delta < 0.4$pp at all scales; Appendix~\\ref{sec:error_analysis}). CED-based selection filters for joint quality but does not specifically optimize evidence grounding, suggesting that targeted evidence rewards may be needed to improve evidence quality beyond what data selection achieves.\n\nAt 1.7B scale, 44.4\\% of outputs exhibit repetitive patterns (vs.\\ negligible at 4B+); small models may require decoding-time interventions (e.g., repetition penalty) for reliable deployment.\n\n\\section{Ethics Statement}\n\nThis work uses publicly available benchmarks (DocRED, Re-DocRED) derived from Wikipedia, containing no private or sensitive information. All models are trained on existing annotated data without human subjects involvement. Our evidence-grounding approach aims to improve the verifiability of relation extraction outputs, which supports responsible deployment in high-stakes domains such as clinical and legal information systems by enabling human verification of model predictions. We release code and model outputs to support reproducibility.\n\n% Responsible NLP Research Checklist: submitted via OpenReview form per ARR/EMNLP 2026 guidelines.\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  }
}
```

</details>

---

### Assistant

_source line 61_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check the appendix quickly and see the test table status, CodaLab status, and figures.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "e8c7a9d8-4384-4edd-a06b-c15dd2521db4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrJHwWQfXVBZAtzD64eAXa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13895,
      "cache_read_input_tokens": 79289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13895
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

_source line 62_

<details open><summary>🔧 Tool call — Read · `toolu_01BhP3WJp1SjG4kBtmeErsXU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex",
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "7e524c9f-784d-4cb3-86d8-194929ae2ce6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrJHwWQfXVBZAtzD64eAXa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13895,
      "cache_read_input_tokens": 79289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13895
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

_source line 63 · 2026-05-21T22:56:46.430Z_

<details><summary>↩ Tool result · `toolu_01BhP3WJp1SjG4kBtmeErsXU`</summary>

```text
1	\section{Training Hyperparameters}
2	\label{sec:hyperparams}
3	
4	Table~\ref{tab:hyperparams} lists the hyperparameters for all training configurations. All methods use LoRA with rank $r{=}64$ and $\alpha{=}128$ applied to all linear projections (attention and feed-forward). SFT and RSFT share the same optimizer settings; RSFT differs only in data construction (top-1 CED-selected outputs from $N{=}8$ candidates). GRPO and DPO use lower learning rates to stabilize post-SFT optimization.
5	
6	\begin{table*}[t]
7	\centering
8	\caption{Training hyperparameters for all optimization paradigms. All experiments use Qwen3-4B as the base model with LoRA adaptation. A dash indicates that the parameter is not applicable to the given method.}
9	\label{tab:hyperparams}
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	\textbf{Parameter} & \textbf{SFT} & \textbf{RSFT} & \textbf{GRPO QLoRA} & \textbf{GRPO bf16} & \textbf{DPO} \\
14	\midrule
15	Base model & Qwen3-4B & Qwen3-4B & Qwen3-4B & Qwen3-4B & Qwen3-4B \\
16	LoRA rank $r$ & 64 & 64 & 64 & 64 & 64 \\
17	LoRA $\alpha$ & 128 & 128 & 128 & 128 & 128 \\
18	Learning rate & 2e-5 & 2e-5 & 5e-6 & 5e-6 & 5e-7 \\
19	Batch size (effective) & 16 & 16 & 4 & 8 & 4 \\
20	Epochs & 3 & 3 & -- & -- & 1, 3\textsuperscript{$\star$} \\
21	Max steps & -- & -- & 100 & 100 & -- \\
22	Gradient accumulation & 4 & 4 & 16 & 4 & 4 \\
23	Max new tokens & 1024 & 1024 & 1024 & 1024 & 1024 \\
24	Quantization & -- & -- & NF4 4-bit & bf16 & bf16 \\
25	Group size $G$ & -- & -- & 4 & 8 & -- \\
26	KL coefficient & -- & -- & 0.01 & 0.01 & -- \\
27	$\beta$ (DPO) & -- & -- & -- & -- & 0.1 \\
28	Candidates $N$ & -- & 8 & -- & -- & 8 \\
29	Top-$k$ selection & -- & 1 & -- & -- & -- \\
30	Training samples & 3,053 & 2,718 & 3,053 & 3,053 & 3,053 \\
31	Scoring function & -- & CED & CED & CED & CED \\
32	\bottomrule
33	\end{tabular}
34	\vspace{1mm}
35	{\raggedright\footnotesize \textsuperscript{$\star$}DPO is trained for both 1 and 3 epochs to observe temporal dynamics of the evidence-extraction trade-off (Section~\ref{sec:spectrum}).\par}
36	\end{table*}
37	
38	
39	\section{Full Ablation Results}
40	\label{sec:ablation_full}
41	
42	Table~\ref{tab:ablation_full} reports the complete RSFT ablation across scoring functions, top-$k$ values, and random seeds. RSFT CED $k{=}1$ achieves a four-seed mean Ign-F1 of 44.66 (standard deviation 0.49), confirming robust improvement over the SFT s42 baseline (39.74). The three-seed mean reported in Table~\ref{tab:main} (44.82, seeds 42/43/44) is slightly higher because it excludes the lowest seed (s45: 44.16). Random selection RSFT $k{=}1$ (41.14 Ign-F1), which samples from the same candidate pool without CED scoring, improves only +1.40pp over SFT s42 versus +4.92pp for CED RSFT, confirming that CED scoring precision drives the majority of the RSFT gain. Increasing $k$ to 3 slightly degrades performance (43.64 Ign-F1), consistent with the intuition that stricter selection yields higher-quality training data. The flat-NLI scoring variant produces comparable Rel-F1 (mean 45.61 vs.\ 45.63 for CED, a difference of 0.02pp). Both CED and flat-NLI improve substantially over the SFT baseline while maintaining or improving Evi-F1, confirming that the RSFT gains are driven by quality-based data selection rather than by the specific contrastive formulation.
43	
44	\paragraph{NLI scoring comparison.} Across all available seeds, CED RSFT achieves mean Rel-F1 of 45.63 (seeds 42, 43, 44, 45: range 45.14--46.21), and flat-NLI RSFT achieves mean Rel-F1 of 45.61 (seeds 42, 43: range 45.35--45.86). The 0.02pp difference suggests comparable performance: CED's contrastive design does not substantially outperform simpler NLI scoring for RSFT data selection. We adopt CED as the default because its contrastive formulation produces per-triple discrimination scores that support interpretable error analysis.
45	
46	\paragraph{Top-$k$ selection.} Best-of-8 ($k{=}1$) yields mean Ign-F1 44.66 and Rel-F1 45.63, while top-3-of-8 ($k{=}3$) produces 43.64 and 44.54. The selected training data confirms the quality gap: $k{=}1$ data has mean extraction F1 of 61.57 and mean CED of 0.6683, versus 57.61 and 0.6205 for $k{=}3$. Despite $k{=}3$ providing 2.96$\times$ more training examples, the additional lower-ranked samples introduce noise that degrades final performance.
47	
48	\paragraph{NLI scorer capacity.} CED filtering is robust to NLI model capacity: replacing the default scorer (DeBERTa-v3-base, 86M parameters) with DeBERTa-v3-large (304M) yields only +1.10pp Ign-F1 (45.33 vs.\ 44.23, s42), a difference within the v3-base seed noise of 0.88pp (s42: 44.23, s44: 45.11). Other metrics confirm the pattern: Rel-F1 improves by +1.19pp (46.36 vs.\ 45.17), Evi-F1 by +0.20pp (81.94 vs.\ 81.74), while EDCR shifts by $-$0.39pp (0.6530 vs.\ 0.6569)---the inconsistent direction across metrics rules out systematic improvement from a larger scorer. This insensitivity supports v3-base as a cost-effective default, as a 3.5$\times$ larger scorer does not materially improve CED-based data selection.
49	
50	\begin{table}[t]
51	\centering
52	\caption{Full RSFT ablation on DocRED dev set (Qwen3-4B). CED and flat-NLI denote the scoring function used for candidate selection. Best Ign-F1 among evidence-generating methods in \textbf{bold}.}
53	\label{tab:ablation_full}
54	\small
55	\resizebox{\columnwidth}{!}{%
56	\begin{tabular}{lcccc}
57	\toprule
58	\textbf{Configuration} & \textbf{Ign-F1} & \textbf{Rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} \\
59	\midrule
60	SFT baseline (s42) & 39.74 & 40.49 & 79.86 & 0.6982 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "a6f06ecb-a12e-44e9-8255-91fc1bfe497b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Training Hyperparameters}\n\\label{sec:hyperparams}\n\nTable~\\ref{tab:hyperparams} lists the hyperparameters for all training configurations. All methods use LoRA with rank $r{=}64$ and $\\alpha{=}128$ applied to all linear projections (attention and feed-forward). SFT and RSFT share the same optimizer settings; RSFT differs only in data construction (top-1 CED-selected outputs from $N{=}8$ candidates). GRPO and DPO use lower learning rates to stabilize post-SFT optimization.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Training hyperparameters for all optimization paradigms. All experiments use Qwen3-4B as the base model with LoRA adaptation. A dash indicates that the parameter is not applicable to the given method.}\n\\label{tab:hyperparams}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Parameter} & \\textbf{SFT} & \\textbf{RSFT} & \\textbf{GRPO QLoRA} & \\textbf{GRPO bf16} & \\textbf{DPO} \\\\\n\\midrule\nBase model & Qwen3-4B & Qwen3-4B & Qwen3-4B & Qwen3-4B & Qwen3-4B \\\\\nLoRA rank $r$ & 64 & 64 & 64 & 64 & 64 \\\\\nLoRA $\\alpha$ & 128 & 128 & 128 & 128 & 128 \\\\\nLearning rate & 2e-5 & 2e-5 & 5e-6 & 5e-6 & 5e-7 \\\\\nBatch size (effective) & 16 & 16 & 4 & 8 & 4 \\\\\nEpochs & 3 & 3 & -- & -- & 1, 3\\textsuperscript{$\\star$} \\\\\nMax steps & -- & -- & 100 & 100 & -- \\\\\nGradient accumulation & 4 & 4 & 16 & 4 & 4 \\\\\nMax new tokens & 1024 & 1024 & 1024 & 1024 & 1024 \\\\\nQuantization & -- & -- & NF4 4-bit & bf16 & bf16 \\\\\nGroup size $G$ & -- & -- & 4 & 8 & -- \\\\\nKL coefficient & -- & -- & 0.01 & 0.01 & -- \\\\\n$\\beta$ (DPO) & -- & -- & -- & -- & 0.1 \\\\\nCandidates $N$ & -- & 8 & -- & -- & 8 \\\\\nTop-$k$ selection & -- & 1 & -- & -- & -- \\\\\nTraining samples & 3,053 & 2,718 & 3,053 & 3,053 & 3,053 \\\\\nScoring function & -- & CED & CED & CED & CED \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1mm}\n{\\raggedright\\footnotesize \\textsuperscript{$\\star$}DPO is trained for both 1 and 3 epochs to observe temporal dynamics of the evidence-extraction trade-off (Section~\\ref{sec:spectrum}).\\par}\n\\end{table*}\n\n\n\\section{Full Ablation Results}\n\\label{sec:ablation_full}\n\nTable~\\ref{tab:ablation_full} reports the complete RSFT ablation across scoring functions, top-$k$ values, and random seeds. RSFT CED $k{=}1$ achieves a four-seed mean Ign-F1 of 44.66 (standard deviation 0.49), confirming robust improvement over the SFT s42 baseline (39.74). The three-seed mean reported in Table~\\ref{tab:main} (44.82, seeds 42/43/44) is slightly higher because it excludes the lowest seed (s45: 44.16). Random selection RSFT $k{=}1$ (41.14 Ign-F1), which samples from the same candidate pool without CED scoring, improves only +1.40pp over SFT s42 versus +4.92pp for CED RSFT, confirming that CED scoring precision drives the majority of the RSFT gain. Increasing $k$ to 3 slightly degrades performance (43.64 Ign-F1), consistent with the intuition that stricter selection yields higher-quality training data. The flat-NLI scoring variant produces comparable Rel-F1 (mean 45.61 vs.\\ 45.63 for CED, a difference of 0.02pp). Both CED and flat-NLI improve substantially over the SFT baseline while maintaining or improving Evi-F1, confirming that the RSFT gains are driven by quality-based data selection rather than by the specific contrastive formulation.\n\n\\paragraph{NLI scoring comparison.} Across all available seeds, CED RSFT achieves mean Rel-F1 of 45.63 (seeds 42, 43, 44, 45: range 45.14--46.21), and flat-NLI RSFT achieves mean Rel-F1 of 45.61 (seeds 42, 43: range 45.35--45.86). The 0.02pp difference suggests comparable performance: CED's contrastive design does not substantially outperform simpler NLI scoring for RSFT data selection. We adopt CED as the default because its contrastive formulation produces per-triple discrimination scores that support interpretable error analysis.\n\n\\paragraph{Top-$k$ selection.} Best-of-8 ($k{=}1$) yields mean Ign-F1 44.66 and Rel-F1 45.63, while top-3-of-8 ($k{=}3$) produces 43.64 and 44.54. The selected training data confirms the quality gap: $k{=}1$ data has mean extraction F1 of 61.57 and mean CED of 0.6683, versus 57.61 and 0.6205 for $k{=}3$. Despite $k{=}3$ providing 2.96$\\times$ more training examples, the additional lower-ranked samples introduce noise that degrades final performance.\n\n\\paragraph{NLI scorer capacity.} CED filtering is robust to NLI model capacity: replacing the default scorer (DeBERTa-v3-base, 86M parameters) with DeBERTa-v3-large (304M) yields only +1.10pp Ign-F1 (45.33 vs.\\ 44.23, s42), a difference within the v3-base seed noise of 0.88pp (s42: 44.23, s44: 45.11). Other metrics confirm the pattern: Rel-F1 improves by +1.19pp (46.36 vs.\\ 45.17), Evi-F1 by +0.20pp (81.94 vs.\\ 81.74), while EDCR shifts by $-$0.39pp (0.6530 vs.\\ 0.6569)---the inconsistent direction across metrics rules out systematic improvement from a larger scorer. This insensitivity supports v3-base as a cost-effective default, as a 3.5$\\times$ larger scorer does not materially improve CED-based data selection.\n\n\\begin{table}[t]\n\\centering\n\\caption{Full RSFT ablation on DocRED dev set (Qwen3-4B). CED and flat-NLI denote the scoring function used for candidate selection. Best Ign-F1 among evidence-generating methods in \\textbf{bold}.}\n\\label{tab:ablation_full}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Configuration} & \\textbf{Ign-F1} & \\textbf{Rel-F1} & \\textbf{Evi-F1} & \\textbf{EDCR} \\\\\n\\midrule\nSFT baseline (s42) & 39.74 & 40.49 & 79.86 & 0.6982 \\\\",
      "numLines": 60,
      "startLine": 1,
      "totalLines": 340
    }
  }
}
```

</details>

---

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Glob · `toolu_01E9hnh6HJQNXKKC4T63NGva`</summary>

```json
{
  "pattern": "**/*.{pdf,png}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "116e6b05-cefa-4221-9ee5-6e4ab81f3f47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrJHwWQfXVBZAtzD64eAXa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13895,
      "cache_read_input_tokens": 79289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13895
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

_source line 65 · 2026-05-21T22:56:47.443Z_

<details><summary>↩ Tool result · `toolu_01E9hnh6HJQNXKKC4T63NGva`</summary>

```text
docs/paper/_pdf_images/main_p1.png
docs/paper/_pdf_images/main_p2.png
docs/paper/_pdf_images/main_p3.png
docs/paper/_pdf_images/main_p4.png
docs/paper/_pdf_images/main_p5.png
docs/paper/_pdf_images/main_p6.png
docs/paper/_pdf_images/main_p10.png
docs/paper/_pdf_images/main_p9.png
docs/paper/_pdf_images/main_p7.png
docs/paper/_pdf_images/main_p8.png
docs/paper/main.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "cfee3e34-929e-4cb8-a5d0-ba3fbba9a55a",
  "tool_use_result": {
    "filenames": [
      "docs/paper/_pdf_images/main_p1.png",
      "docs/paper/_pdf_images/main_p2.png",
      "docs/paper/_pdf_images/main_p3.png",
      "docs/paper/_pdf_images/main_p4.png",
      "docs/paper/_pdf_images/main_p5.png",
      "docs/paper/_pdf_images/main_p6.png",
      "docs/paper/_pdf_images/main_p10.png",
      "docs/paper/_pdf_images/main_p9.png",
      "docs/paper/_pdf_images/main_p7.png",
      "docs/paper/_pdf_images/main_p8.png",
      "docs/paper/main.pdf"
    ],
    "durationMs": 8,
    "numFiles": 11,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Bash · `toolu_01R2qdFp6A5fEZm3JAHwZAJb`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib 2>/dev/null && wc -l /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib || echo \"NO_BIB\"",
  "description": "Check bib file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "dfe35363-f6f5-4498-bac8-bd56803630fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrJHwWQfXVBZAtzD64eAXa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13895,
      "cache_read_input_tokens": 79289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13895
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

_source line 67 · 2026-05-21T22:56:48.680Z_

<details><summary>↩ Tool result · `toolu_01R2qdFp6A5fEZm3JAHwZAJb`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 15418 May 18 07:50 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib
301 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "7917d98a-fcb8-440e-bf9f-2fd95ce3d715",
  "tool_use_result": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 15418 May 18 07:50 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib\n301 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 68_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture of the paper's current state. Let me also quickly check the appendix for the test table and other important sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "e880d5a8-81f6-44ac-a441-2a6d709ba6ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KGGNNY1msCBZekJ1qtwG16",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2943,
      "cache_read_input_tokens": 93184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2943
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

_source line 69_

<details open><summary>🔧 Tool call — Read · `toolu_01VcW8gaWZXFu69LAQyG7Sun`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex",
  "offset": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "c92f54dc-1e5b-476c-a4fa-f4be7238c3ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KGGNNY1msCBZekJ1qtwG16",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2943,
      "cache_read_input_tokens": 93184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2943
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

_source line 70 · 2026-05-21T22:56:53.268Z_

<details><summary>↩ Tool result · `toolu_01VcW8gaWZXFu69LAQyG7Sun`</summary>

```text
60	SFT baseline (s42) & 39.74 & 40.49 & 79.86 & 0.6982 \\
61	SFT no-evidence & \textbf{47.21} & 48.76 & -- & -- \\
62	\midrule
63	RSFT random $k{=}1$ & 41.14 & 41.98 & 79.64 & 0.6971 \\
64	\midrule
65	RSFT CED $k{=}1$ (s42) & 44.23 & 45.17 & 81.74 & 0.6569 \\
66	RSFT CED $k{=}1$ (s43) & 45.12 & 46.01 & 80.63 & 0.6542 \\
67	RSFT CED $k{=}1$ (s44) & 45.11 & 46.21 & 80.50 & 0.6350 \\
68	RSFT CED $k{=}1$ (s45) & 44.16 & 45.14 & 81.74 & 0.6550 \\
69	RSFT CED $k{=}1$ (mean) & 44.66 & 45.63 & 81.15 & 0.6503 \\
70	\midrule
71	RSFT CED $k{=}3$ & 43.64 & 44.54 & 80.88 & 0.6635 \\
72	\midrule
73	RSFT flat-NLI (s42) & -- & 45.35 & 80.43 & 0.6431 \\
74	RSFT flat-NLI (s43) & -- & 45.86 & 81.58 & 0.6505 \\
75	RSFT flat-NLI (mean) & -- & 45.61 & 81.01 & 0.6468 \\
76	\midrule
77	RSFT CED $k{=}1$ v3-large (s42) & 45.33 & 46.36 & 81.94 & 0.6530 \\
78	\bottomrule
79	\end{tabular}%
80	}
81	\end{table}
82	
83	
84	\section{Scaling Details}
85	\label{sec:scaling_details}
86	
87	Table~\ref{tab:cross_detail} supplements Table~\ref{tab:scaling} in the main text with per-scale Rel-F1 and Evi-F1 breakdowns. At 1.7B, RSFT improves Rel-F1 from 45.86 to 52.81 (+6.95, multi-seed mean) while achieving Evi-F1 82.63 and EDCR 0.6217. The 4B model shows the same pattern: Rel-F1 increases from 44.39 to 45.80 (+1.41, three-seed mean). For 8B, RSFT brings Rel-F1 from 51.87 to 56.26 (three-seed mean) with Evi-F1 of 81.26 and EDCR 0.6235, confirming tight coupling between extraction and evidence at this scale. At 14B, the SFT baseline already achieves strong Rel-F1 (56.11) and Evi-F1 (82.92).
88	
89	\begin{table}[t]
90	\centering
91	\caption{Detailed Rel-F1 and Evi-F1 across model scales on DocRED dev set. SFT and RSFT columns show multi-seed means where available (Qwen3 1.7B/4B/8B: 3-seed; 14B: single seed; LLaMA SFT Rel-F1/Evi-F1: s42 only; LLaMA RSFT: 3-seed).}
92	\label{tab:cross_detail}
93	\small
94	\resizebox{\columnwidth}{!}{%
95	\begin{tabular}{lccccc}
96	\toprule
97	\textbf{Model} & \textbf{SFT Rel-F1} & \textbf{SFT Evi-F1} & \textbf{RSFT Rel-F1} & \textbf{RSFT Evi-F1} & \textbf{RSFT EDCR} \\
98	\midrule
99	Qwen3-1.7B & 45.86 & 82.85 & 52.81 & 82.63 & 0.6217 \\
100	Qwen3-4B & 44.39 & 79.61 & 45.80 & 80.96 & 0.6487 \\
101	Qwen3-8B & 51.87 & 82.94 & 56.26 & 81.26 & 0.6235 \\
102	Qwen3-14B & 56.11 & 82.92 & -- & -- & -- \\
103	LLaMA-3.1-8B & 55.14 & 81.51 & 57.75 & 82.84 & 0.5804 \\
104	\bottomrule
105	\end{tabular}%
106	}
107	\end{table}
108	
109	
110	\section{Controlled Evaluation Subset}
111	\label{sec:fair_subset}
112	
113	The 1.7B evidence tax comparison (\S\ref{sec:scaling}) is confounded by differential truncation rates. At \texttt{max\_new\_tokens}$=$1024, the no-evidence model truncates 50.9\% of outputs (501/985 documents) versus 31.9\% (314/985) for the evidence model. To address this, we adopt a matched@2048 fair evaluation: both configurations are evaluated at \texttt{max\_new\_tokens}$=$2048, and the tax is computed on the intersection of documents where both produce format-compliant output. This yields 971/985 fair-subset documents, with a tax of $-$5.63pp (s42), confirming a genuine 1.7B evidence benefit. As additional validation, a stricter controlled subset at @1024 (excluding truncated or repetitive outputs; 442/985 documents) yields $-$6.2pp, with the stronger benefit attributable to the more aggressive filtering.
114	
115	Table~\ref{tab:mechanistic} provides a mechanistic breakdown across three scales (evaluated at @1024). Output duplication rate (fraction of documents containing $\geq$3 repeated triples or unique/total $< 0.5$) declines monotonically with scale for both training configurations, but the gap between no-evidence and with-evidence models narrows from 27.5pp at 1.7B to 3.7pp at 8B. This pattern supports the implicit regularization hypothesis: evidence generation forces smaller models to attend to supporting context, reducing degenerate repetition. At 4B, duplication is already moderate (31.1\% with evidence), so the regularization benefit diminishes; under matched@2048 evaluation, the 4B training-time tax is approximately neutral (+0.25$\pm$0.47pp, three-seed mean). The truncation asymmetry reverses across scales: at 1.7B the no-evidence model truncates 19pp more often; at 8B the evidence model truncates 9pp more often due to the longer output format.
116	
117	\begin{table}[t]
118	\centering
119	\caption{Mechanistic breakdown of output quality across scales. Duplication rate: fraction of documents with degenerate outputs. Truncation $\Delta$: no-evidence rate minus with-evidence rate (positive means no-evidence truncates more).}
120	\label{tab:mechanistic}
121	\small
122	\begin{tabular}{lccccc}
123	\toprule
124	& \multicolumn{3}{c}{\textbf{Duplication Rate}} & \multicolumn{2}{c}{\textbf{Truncation}} \\
125	\cmidrule(lr){2-4} \cmidrule(lr){5-6}
126	\textbf{Scale} & \textbf{w/ evi} & \textbf{no-evi} & \textbf{Gap} & \textbf{$\Delta$} & \textbf{Pattern} \\
127	\midrule
128	1.7B & 33.0 & 60.5 & 27.5 & +19 & no-evi worse \\
129	4B & 31.1 & 43.2 & 12.1 & +2 & neutral \\
130	8B & 29.2 & 32.9 & 3.7 & $-$9 & evi worse \\
131	\bottomrule
132	\end{tabular}
133	\end{table}
134	
135	
136	\section{Training-Time Evidence Tax}
137	\label{sec:training_tax}
138	
139	The evidence tax can be measured in two ways. The \emph{training-time} tax compares separately trained models (SFT with evidence vs.\ SFT without evidence in the training output format). The \emph{inference-time} tax (reported in Table~\ref{tab:scaling}) evaluates the same RSFT model with and without evidence at inference time.
140	
141	Na\"ive comparisons at \texttt{max\_new\_tokens}$=$1024 are confounded by differential truncation rates (e.g., 50.9\% vs.\ 31.9\% at 1.7B). To control for this, we adopt a \emph{matched@2048 fair evaluation}: both configurations are evaluated at \texttt{max\_new\_tokens}$=$2048, and the tax is computed on the intersection of documents where both models produce format-compliant output. Table~\ref{tab:training_tax} reports the matched@2048 training-time tax across Qwen3 scales.
142	
143	The tax reveals a within-family capacity threshold: evidence generation benefits 1.7B ($-$5.63pp on 971/985 fair-subset documents) but is approximately neutral at $\geq$4B (+0.25$\pm$0.47pp at 4B across three seeds, +0.04pp at 8B, +0.03pp at 14B). At 1.7B, s42 is the strongest SFT seed (47.86 Ign-F1, +3.22pp above the three-seed mean of 44.64), so the benefit may be amplified relative to the population mean. LLaMA-3.1-8B SFT training-time tax is highly seed-dependent (individual seeds range from $-$2.83 to +1.20pp under matched@2048) and omitted from the table; cross-architecture patterns are addressed in \S\ref{sec:generalization_full}.
144	
145	\begin{table}[t]
146	\centering
147	\caption{Training-time evidence tax under matched@2048 fair evaluation (DocRED dev Ign-F1). Both configurations evaluated at \texttt{max\_new\_tokens}$=$2048; tax computed on format-compliant intersection. Tax $=$ no-evidence $-$ with-evidence; positive $=$ cost.}
148	\label{tab:training_tax}
149	\small
150	\begin{tabular}{lcccc}
151	\toprule
152	\textbf{Model} & \textbf{Fair w/ evi} & \textbf{Fair no-evi} & \textbf{Evi Tax} & \textbf{Subset} \\
153	\midrule
154	Qwen3-1.7B & 48.38 & 42.75 & $-$5.63 & 971 \\
155	Qwen3-4B & -- & -- & +0.25{\scriptsize$\pm$0.47}$^{(3)}$ & $\geq$982 \\
156	Qwen3-8B & 50.15 & 50.19 & +0.04 & 984 \\
157	Qwen3-14B & 55.07 & 55.10 & +0.03 & 985$^\dagger$ \\
158	\bottomrule
159	\end{tabular}
160	\vspace{-2mm}
161	{\raggedright\footnotesize 1.7B and 8B are s42; 4B reports three-seed mean $\pm$ std (per-seed range: $-$0.19 to +0.73pp); 14B evaluated at @1024 with 0\% truncation for both configurations ($^\dagger$fair subset equals full dev set). Subset: documents in format-compliant intersection out of 985.\par}
162	\end{table}
163	
164	
165	\section{Why RSFT Avoids Decoupling}
166	\label{sec:rsft_theory}
167	
168	The structural difference between selection and optimization explains why RSFT does not exhibit the decoupling observed in gradient-based methods. GRPO and DPO update model parameters through gradients that optimize a reward signal. When two sub-tasks (extraction and evidence) compete for gradient capacity, the optimizer can discover and exploit the trade-off between them, improving one at the expense of the other. RSFT operates differently: it selects complete outputs and trains on them with standard supervised loss. Because the selection is discrete (accept or reject a full response), there is no gradient pathway through which the model can learn to sacrifice extraction for evidence quality. Only outputs where both extraction and evidence are jointly strong survive the CED filter. This property is not specific to RSFT's design but is a structural consequence of discrete selection over complete outputs: any selection-based method that filters on a joint quality criterion will inherit the same coupling guarantee. The implication for practitioners is direct: when optimizing for multiple coupled generation objectives, selection-based methods preserve inter-objective balance that gradient-based methods disrupt.
169	
170	
171	\section{Decoupling Spectrum Visualization}
172	\label{sec:spectrum_viz}
173	
174	\begin{figure}[t]
175	\centering
176	\includegraphics[width=\columnwidth]{fig_spectrum.pdf}
177	\caption{Decoupling spectrum visualization. Each method is plotted by Rel-F1 (x-axis) and Evi-F1 (y-axis). Arrows indicate training progression for DPO (1ep$\to$3ep) and GRPO bf16 trajectory. Ideal methods occupy the upper-right quadrant; decoupled methods drift toward the upper-left.}
178	\label{fig:spectrum}
179	\end{figure}
180	
181	
182	\section{Evidence Tax Visualization}
183	\label{sec:scaling_viz}
184	
185	\begin{figure}[t]
186	\centering
187	\includegraphics[width=\columnwidth]{fig_scaling.pdf}
188	\caption{Evidence tax across model scales. Bar heights show Ign-F1 for each training configuration. The gap between no-evidence and SFT bars reverses direction between 1.7B and 4B, revealing the scale-dependent nature of the evidence tax. RSFT consistently narrows the gap toward the no-evidence upper bound.}
189	\label{fig:scaling}
190	\end{figure}
191	
192	
193	\section{Full Generalization Results}
194	\label{sec:generalization_full}
195	
196	\paragraph{Cross-family transfer.}
197	LLaMA-3.1-8B confirms the scaling patterns observed with Qwen3. Its SFT baseline achieves a three-seed mean of 51.09 Ign-F1 (std 2.92pp; s42: 53.84, s43: 51.42, s44: 48.02), and the s42 no-evidence variant reaches 54.52 Ign-F1 (Rel-F1 56.24). The s42 evidence tax of +0.68 points mirrors the near-zero tax seen for Qwen3-8B (+0.04pp under matched@2048 fair evaluation), supporting our claim that 8B-class models absorb the cost of joint evidence generation regardless of architecture family. However, LLaMA SFT training-time tax is highly seed-dependent (per-seed range: $-$2.83 to +1.20pp under matched@2048), precluding a reliable single estimate. RSFT CED improves LLaMA to a three-seed mean of 56.54 Ign-F1 (std 0.64pp; s42: 57.14, s43: 56.62, s44: 55.87), a +5.45 point gain over SFT mean (51.09), with 4.6$\times$ variance compression (2.92pp $\to$ 0.64pp), consistent with the pattern at the 8B scale (Qwen3-8B: +4.33, 17$\times$ compression).
198	
199	\paragraph{Cross-dataset robustness.}
200	On Re-DocRED~\citep{tan2022redocred}, the SFT baseline achieves 36.59 Ign-F1 (Evi-F1 81.70, EDCR 0.6674). RSFT CED improves this to 41.45 Ign-F1 (Evi-F1 81.82, EDCR 0.6210), a +4.86pp gain that closely matches the +5.08pp improvement on DocRED (RSFT three-seed mean minus SFT s42). This consistency across datasets with different annotation protocols confirms that RSFT's benefit generalizes beyond training-set-specific artifacts. Evidence quality remains stable across datasets (Evi-F1 81.82 vs.\ 81.15 on DocRED), and the EDCR reduction ($-0.046$) mirrors the DocRED pattern, further supporting the robustness of CED-based selection.
201	
202	\paragraph{Re-DocRED test set evaluation.}
203	Table~\ref{tab:test_results} reports RSFT performance on the Re-DocRED test set. We observe a consistent performance gap between dev and test sets, with test Ign-F1 approximately 20 percentage points lower (1.7B: 51.2$\to$29.3, 8B: 54.5$\to$33.5, 14B: 58.9$\to$38.5, LLaMA-8B: 56.5$\to$36.0). This gap is attributable to annotation density: the test set contains 34.7 gold triples per document versus 12.3 in the dev set (a 2.82$\times$ ratio), imposing a harder recall requirement. The gap magnitude is stable across four scales and two architectures (range: 20.4--21.9pp), and model ranking is perfectly preserved (Spearman $\rho{=}1.0$), indicating that the absolute drop reflects the test annotation scheme rather than a model-specific deficiency.
204	
205	\begin{table}[t]
206	\centering
207	\caption{RSFT performance on Re-DocRED test set (Ign-F1 \%). Dev Ign-F1 from Table~\ref{tab:scaling}. SFT test baselines pending. All test results are s42.}
208	\label{tab:test_results}
209	\small
210	\begin{tabular}{lccccc}
211	\toprule
212	\textbf{Model} & \textbf{Dev} & \textbf{Test} & \textbf{Evi-F1} & \textbf{EDCR} & \textbf{Trunc.\%} \\
213	\midrule
214	Qwen3-1.7B & 51.19 & 29.33 & 23.20 & 0.817 & 73.8 \\
215	Qwen3-8B & 54.52 & 33.53 & 25.26 & 0.799 & 1.8 \\
216	Qwen3-14B & 58.86 & 38.49 & 26.88 & 0.787 & 13.4 \\
217	LLaMA-3.1-8B & 56.54 & 35.99 & 25.09 & 0.839 & 56.6 \\
218	\bottomrule
219	\end{tabular}
220	\end{table}
221	
222	\paragraph{Comparison to supervised methods.}
223	Table~\ref{tab:encoder_comparison} directly compares encoder-based methods with our LLM-based approach. Encoder methods achieve substantially higher extraction performance (Rel-F1 63--65 vs.\ our 45--56), reflecting decades of architecture-specific optimization for the classification formulation. However, their evidence identification operates as binary sentence classification, producing Evi-F1 of 52--56 under a joint evaluation protocol. Our TP-only Evi-F1 exceeds 80\%, indicating that when the model correctly identifies a triple, it produces higher-quality evidence than encoder methods. The joint Evi-F1 gap (36.1 vs.\ 54.15) is driven primarily by extraction performance rather than evidence quality: false-positive and false-negative triples dilute the denominator. Closing this gap requires improving extraction capability of LLM-based methods, an orthogonal direction to the evidence faithfulness problem we address.
224	
225	\begin{table}[t]
226	\centering
227	\caption{Comparison with encoder-based methods on DocRED dev set. Encoder methods use RoBERTa-large; LLM methods use Qwen3. Evi-F1 for encoder methods uses joint evaluation (all triples in denominator); our joint Evi-F1 follows the same protocol for fair comparison. TP-only Evi-F1 conditions on correctly predicted triples. Rel-F1 is reported in percentage for all methods.}
228	\label{tab:encoder_comparison}
229	\small
230	\resizebox{\columnwidth}{!}{%
231	\begin{tabular}{llcccc}
232	\toprule
233	\textbf{Method} & \textbf{Type} & \textbf{Ign-F1} & \textbf{Rel-F1} & \textbf{Evi-F1 (joint)} & \textbf{Evi-F1 (TP)} \\
234	\midrule
235	ATLOP & Encoder & 61.32 & 63.18 & -- & -- \\
236	EIDER & Encoder & 62.34 & 64.27 & 52.54 & -- \\
237	SAIS & Encoder & 62.23 & 65.17 & 55.84 & -- \\
238	DREEAM & Encoder & 61.71 & 63.49 & 54.15 & -- \\
239	\midrule
240	Ours (4B RSFT) & LLM & 44.82 & 45.80 & 36.1 & 80.96 \\
241	Ours (8B RSFT) & LLM & 54.52 & 56.26 & -- & 81.26 \\
242	Ours (14B RSFT) & LLM & 58.86 & 60.09 & 48.59 & 83.92 \\
243	\bottomrule
244	\end{tabular}%
245	}
246	\end{table}
247	
248	
249	\section{GRPO Training Dynamics}
250	\label{sec:grpo_dynamics}
251	
252	\begin{figure*}[t]
253	\centering
254	\includegraphics[width=\linewidth]{fig_grpo_dynamics.pdf}
255	\caption{Training dynamics of GRPO under different configurations. (a)~Relation F1 across checkpoints: G=4 QLoRA suffers catastrophic collapse at step~10, while G=8 bf16 remains stable. (b)~Evidence F1 stays intact for G=8 bf16, confirming the generation mechanism itself does not fail. (c)~Evidence-Decoupling Ratio (EDCR) reveals near-total decoupling in G=4 QLoRA (extraction collapses to Rel-F1 1.4), while G=8 bf16 maintains healthy ratios.}
256	\label{fig:grpo_dynamics}
257	\end{figure*}
258	
259	
260	\section{Error Analysis: SFT vs.\ RSFT}
261	\label{sec:error_analysis}
262	
263	Table~\ref{tab:error_analysis} decomposes the extraction improvements from RSFT into error categories across three scales. Three mechanisms drive the gains consistently:
264	
265	\paragraph{Truncation false negatives.} SFT models frequently hit the generation length limit, producing incomplete outputs that miss triples. RSFT training on compact, high-quality outputs reduces this truncation rate. The effect is strongest at 1.7B ($-841$ truncation FN, $-22$\%), where the SFT model's output length is least controlled.
266	
267	\paragraph{Hallucinated false positives.} CED-based filtering removes training examples with unfaithful predictions, reducing the rate of hallucinated triples at inference. LLaMA benefits most ($-593$ hallucinated FP, $-11.8$\%), suggesting cross-architecture variation in hallucination susceptibility.
268	
269	\paragraph{Duplicate predictions.} RSFT training data, selected for quality, contains fewer repetitive patterns. This propagates to inference, reducing duplicate triples by $11$--$20$\% across scales, with 1.7B showing the largest reduction ($-20.2$\%).
270	
271	\paragraph{Evidence quality unchanged.} Despite substantial extraction improvements, evidence exact-match F1 changes by less than 0.4pp at every scale. RSFT selects for joint extraction-evidence quality, but the evidence signal in CED scoring does not translate into measurable evidence improvement. This suggests that evidence grounding requires targeted optimization (e.g., evidence-specific rewards in RL) rather than data selection alone.
272	
273	\paragraph{Residual difficulty.} The proportion of ``other'' false negatives (triples missed for reasons beyond truncation or formatting) increases by 13--15\% in relative terms after RSFT. As easy errors (truncation, duplication) are eliminated, the remaining error distribution shifts toward harder cases: cross-sentence reasoning, implicit relations, and long-tail entity pairs. The relation types with the largest RSFT gains (participant, conflict, league, screenwriter, operator, contains\_administrative\_territory) involve cross-sentence reasoning or long-tail entities, consistent with RSFT's selection pressure toward diverse, high-quality outputs.
274	
275	\begin{table}[t]
276	\centering
277	\caption{Error pattern changes from SFT to RSFT across scales. $\Delta$\% shows relative change. Truncation FN, hallucinated FP, and duplicates all decrease; evidence quality and residual FN difficulty are unchanged.}
278	\label{tab:error_analysis}
279	\small
280	\resizebox{\columnwidth}{!}{%
281	\begin{tabular}{llccc}
282	\toprule
283	\textbf{Error Category} & \textbf{Direction} & \textbf{1.7B} & \textbf{4B} & \textbf{8B / LLaMA} \\
284	\midrule
285	Truncation FN & $\downarrow$ & $-$22\% & $-$16\% & $-$18\% \\
286	Hallucinated FP & $\downarrow$ & $-$8\% & $-$6\% & $-$12\% \\
287	Duplicates & $\downarrow$ & $-$20\% & $-$11\% & $-$14\% \\
288	Evidence (exact) & $\approx$ & $<$0.4pp & $<$0.4pp & $<$0.4pp \\
289	FN: other & $\uparrow$ & +13\% & +15\% & +14\% \\
290	\bottomrule
291	\end{tabular}%
292	}
293	\end{table}
294	
295	
296	\section{Per-Relation EDCR Distribution}
297	\label{sec:edcr_per_relation}
298	
299	Computing EDCR for each of the 76 relation types with $\geq$5 evaluation samples (from the RSFT CED s42 model) reveals that per-relation EDCR correlates strongly with per-relation Rel-F1 ($\rho = -0.79$, $n = 76$, $p < 0.001$), confirming its utility as a difficulty indicator. Filtering to types with $\geq$5 predictions strengthens the correlation ($\rho = -0.85$, $n = 74$, $p < 0.001$). Per-relation EDCR is statistically independent of Evi-F1 ($\rho = -0.06$, $p = 0.58$), and Evi-F1 itself shows no association with Rel-F1 ($\rho = -0.01$, $p = 0.91$). These null correlations establish that evidence quality and extraction ability are fully decoupled across relation types. Extreme cases illustrate the diagnostic power: \texttt{date\_of\_birth} has EDCR $= 0.118$ (highly faithful, with extraction and evidence tightly coupled), while \texttt{head\_of\_government} reaches $0.956$ (highly decoupled). This per-relation analysis avoids the shared-component concern present in cross-method EDCR-vs-Rel-F1 correlation, providing independent validation of EDCR's diagnostic utility.
300	
301	\begin{figure}[t]
302	\centering
303	\includegraphics[width=\linewidth]{fig_edcr_relations.pdf}
304	\caption{Per-relation EDCR distribution across all 93 relation types observed in the development set (of 96 defined in DocRED). The correlation analysis in the text uses the 76 types with $\geq$5 samples for statistical reliability. Red bars indicate EDCR $\geq$ 0.70 (severe decoupling), green bars indicate EDCR $<$ 0.30 (healthy evidence grounding). Seven types exhibit EDCR = 1.0.}
305	\label{fig:edcr_relations}
306	\end{figure}
307	
308	
309	\section{Qualitative Analysis}
310	\label{sec:qualitative}
311	
312	We present representative examples illustrating three phenomena: evidence quality differences between SFT and RSFT, GRPO format gaming under catastrophic collapse, and per-relation EDCR diagnostics.
313	
314	\paragraph{Case 1: Evidence quality.}
315	Table~\ref{tab:case_evidence} compares evidence citations from SFT and RSFT on three documents. SFT tends to cite many sentences indiscriminately, including distractors unrelated to the target triple, while RSFT selects precisely the gold evidence sentences. For \emph{America's Sweetheart}, SFT cites 6 sentences (precision 0.17) whereas RSFT cites only the single correct sentence (precision 1.00). The pattern is consistent: SFT achieves evidence precision of 0.00--0.20 across these examples, while RSFT achieves 1.00 in all three cases.
316	
317	\begin{table}[t]
318	\centering
319	\caption{Evidence citation comparison between SFT and RSFT. Precision measures the fraction of cited sentences that match gold evidence.}
320	\label{tab:case_evidence}
321	\small
322	\resizebox{\columnwidth}{!}{%
323	\begin{tabular}{llccc}
324	\toprule
325	\textbf{Document} & \textbf{Triple} & \textbf{SFT Prec.} & \textbf{RSFT Prec.} & \textbf{SFT \#Cited} \\
326	\midrule
327	Oleg Tinkov & (Oleg Tinkov, country of citizenship, Russia) & 0.00 & 1.00 & 3 \\
328	America's Sweetheart & (record label, country, United States) & 0.17 & 1.00 & 6 \\
329	Jade (Mortal Kombat) & (Jade, present in work, Mortal Kombat) & 0.20 & 1.00 & 5 \\
330	\bottomrule
331	\end{tabular}%
332	}
333	\end{table}
334	
335	\paragraph{Case 2: GRPO format gaming.}
336	Under catastrophic collapse (GRPO QLoRA $G{=}4$), the model abandons the DocRED 96-type relation ontology and generates free-text relation labels. On the document \emph{Something to Believe In}, the model produces 35 predicted triples with relations such as ``is a'', ``honor'', and ``location'', none of which belong to the target ontology. All 35 predictions are incorrect. Similarly, for \emph{J\'{o}zef Pi\l{}sudski Monument}, 28 predictions use non-standard relations with 0 correct matches. The model retains the structural format of triple-with-evidence output but fills it with fabricated relation types. The model produces well-formed evidence for these non-existent relations.
337	
338	\paragraph{Case 3: EDCR diagnostics.}
339	Per-relation EDCR identifies specific relation types where extraction and evidence are misaligned. For \texttt{date\_of\_birth} (EDCR $= 0.118$), the model's evidence consistently matches gold annotations: both extraction and evidence point to the same biographical sentence. In contrast, \texttt{notable\_work} (EDCR $= 0.941$) exhibits severe decoupling: the model cites sentence [0] (a general introduction) instead of the gold evidence sentence [3] (which contains the actual work attribution). High-EDCR relations tend to involve indirect or multi-hop reasoning where surface-level context misleads the evidence generator.
340	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "311c97b6-3ecf-428e-82b3-e0d3b521b82b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex",
      "content": "SFT baseline (s42) & 39.74 & 40.49 & 79.86 & 0.6982 \\\\\nSFT no-evidence & \\textbf{47.21} & 48.76 & -- & -- \\\\\n\\midrule\nRSFT random $k{=}1$ & 41.14 & 41.98 & 79.64 & 0.6971 \\\\\n\\midrule\nRSFT CED $k{=}1$ (s42) & 44.23 & 45.17 & 81.74 & 0.6569 \\\\\nRSFT CED $k{=}1$ (s43) & 45.12 & 46.01 & 80.63 & 0.6542 \\\\\nRSFT CED $k{=}1$ (s44) & 45.11 & 46.21 & 80.50 & 0.6350 \\\\\nRSFT CED $k{=}1$ (s45) & 44.16 & 45.14 & 81.74 & 0.6550 \\\\\nRSFT CED $k{=}1$ (mean) & 44.66 & 45.63 & 81.15 & 0.6503 \\\\\n\\midrule\nRSFT CED $k{=}3$ & 43.64 & 44.54 & 80.88 & 0.6635 \\\\\n\\midrule\nRSFT flat-NLI (s42) & -- & 45.35 & 80.43 & 0.6431 \\\\\nRSFT flat-NLI (s43) & -- & 45.86 & 81.58 & 0.6505 \\\\\nRSFT flat-NLI (mean) & -- & 45.61 & 81.01 & 0.6468 \\\\\n\\midrule\nRSFT CED $k{=}1$ v3-large (s42) & 45.33 & 46.36 & 81.94 & 0.6530 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\n\\section{Scaling Details}\n\\label{sec:scaling_details}\n\nTable~\\ref{tab:cross_detail} supplements Table~\\ref{tab:scaling} in the main text with per-scale Rel-F1 and Evi-F1 breakdowns. At 1.7B, RSFT improves Rel-F1 from 45.86 to 52.81 (+6.95, multi-seed mean) while achieving Evi-F1 82.63 and EDCR 0.6217. The 4B model shows the same pattern: Rel-F1 increases from 44.39 to 45.80 (+1.41, three-seed mean). For 8B, RSFT brings Rel-F1 from 51.87 to 56.26 (three-seed mean) with Evi-F1 of 81.26 and EDCR 0.6235, confirming tight coupling between extraction and evidence at this scale. At 14B, the SFT baseline already achieves strong Rel-F1 (56.11) and Evi-F1 (82.92).\n\n\\begin{table}[t]\n\\centering\n\\caption{Detailed Rel-F1 and Evi-F1 across model scales on DocRED dev set. SFT and RSFT columns show multi-seed means where available (Qwen3 1.7B/4B/8B: 3-seed; 14B: single seed; LLaMA SFT Rel-F1/Evi-F1: s42 only; LLaMA RSFT: 3-seed).}\n\\label{tab:cross_detail}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{SFT Rel-F1} & \\textbf{SFT Evi-F1} & \\textbf{RSFT Rel-F1} & \\textbf{RSFT Evi-F1} & \\textbf{RSFT EDCR} \\\\\n\\midrule\nQwen3-1.7B & 45.86 & 82.85 & 52.81 & 82.63 & 0.6217 \\\\\nQwen3-4B & 44.39 & 79.61 & 45.80 & 80.96 & 0.6487 \\\\\nQwen3-8B & 51.87 & 82.94 & 56.26 & 81.26 & 0.6235 \\\\\nQwen3-14B & 56.11 & 82.92 & -- & -- & -- \\\\\nLLaMA-3.1-8B & 55.14 & 81.51 & 57.75 & 82.84 & 0.5804 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\n\\section{Controlled Evaluation Subset}\n\\label{sec:fair_subset}\n\nThe 1.7B evidence tax comparison (\\S\\ref{sec:scaling}) is confounded by differential truncation rates. At \\texttt{max\\_new\\_tokens}$=$1024, the no-evidence model truncates 50.9\\% of outputs (501/985 documents) versus 31.9\\% (314/985) for the evidence model. To address this, we adopt a matched@2048 fair evaluation: both configurations are evaluated at \\texttt{max\\_new\\_tokens}$=$2048, and the tax is computed on the intersection of documents where both produce format-compliant output. This yields 971/985 fair-subset documents, with a tax of $-$5.63pp (s42), confirming a genuine 1.7B evidence benefit. As additional validation, a stricter controlled subset at @1024 (excluding truncated or repetitive outputs; 442/985 documents) yields $-$6.2pp, with the stronger benefit attributable to the more aggressive filtering.\n\nTable~\\ref{tab:mechanistic} provides a mechanistic breakdown across three scales (evaluated at @1024). Output duplication rate (fraction of documents containing $\\geq$3 repeated triples or unique/total $< 0.5$) declines monotonically with scale for both training configurations, but the gap between no-evidence and with-evidence models narrows from 27.5pp at 1.7B to 3.7pp at 8B. This pattern supports the implicit regularization hypothesis: evidence generation forces smaller models to attend to supporting context, reducing degenerate repetition. At 4B, duplication is already moderate (31.1\\% with evidence), so the regularization benefit diminishes; under matched@2048 evaluation, the 4B training-time tax is approximately neutral (+0.25$\\pm$0.47pp, three-seed mean). The truncation asymmetry reverses across scales: at 1.7B the no-evidence model truncates 19pp more often; at 8B the evidence model truncates 9pp more often due to the longer output format.\n\n\\begin{table}[t]\n\\centering\n\\caption{Mechanistic breakdown of output quality across scales. Duplication rate: fraction of documents with degenerate outputs. Truncation $\\Delta$: no-evidence rate minus with-evidence rate (positive means no-evidence truncates more).}\n\\label{tab:mechanistic}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Duplication Rate}} & \\multicolumn{2}{c}{\\textbf{Truncation}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\n\\textbf{Scale} & \\textbf{w/ evi} & \\textbf{no-evi} & \\textbf{Gap} & \\textbf{$\\Delta$} & \\textbf{Pattern} \\\\\n\\midrule\n1.7B & 33.0 & 60.5 & 27.5 & +19 & no-evi worse \\\\\n4B & 31.1 & 43.2 & 12.1 & +2 & neutral \\\\\n8B & 29.2 & 32.9 & 3.7 & $-$9 & evi worse \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Training-Time Evidence Tax}\n\\label{sec:training_tax}\n\nThe evidence tax can be measured in two ways. The \\emph{training-time} tax compares separately trained models (SFT with evidence vs.\\ SFT without evidence in the training output format). The \\emph{inference-time} tax (reported in Table~\\ref{tab:scaling}) evaluates the same RSFT model with and without evidence at inference time.\n\nNa\\\"ive comparisons at \\texttt{max\\_new\\_tokens}$=$1024 are confounded by differential truncation rates (e.g., 50.9\\% vs.\\ 31.9\\% at 1.7B). To control for this, we adopt a \\emph{matched@2048 fair evaluation}: both configurations are evaluated at \\texttt{max\\_new\\_tokens}$=$2048, and the tax is computed on the intersection of documents where both models produce format-compliant output. Table~\\ref{tab:training_tax} reports the matched@2048 training-time tax across Qwen3 scales.\n\nThe tax reveals a within-family capacity threshold: evidence generation benefits 1.7B ($-$5.63pp on 971/985 fair-subset documents) but is approximately neutral at $\\geq$4B (+0.25$\\pm$0.47pp at 4B across three seeds, +0.04pp at 8B, +0.03pp at 14B). At 1.7B, s42 is the strongest SFT seed (47.86 Ign-F1, +3.22pp above the three-seed mean of 44.64), so the benefit may be amplified relative to the population mean. LLaMA-3.1-8B SFT training-time tax is highly seed-dependent (individual seeds range from $-$2.83 to +1.20pp under matched@2048) and omitted from the table; cross-architecture patterns are addressed in \\S\\ref{sec:generalization_full}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training-time evidence tax under matched@2048 fair evaluation (DocRED dev Ign-F1). Both configurations evaluated at \\texttt{max\\_new\\_tokens}$=$2048; tax computed on format-compliant intersection. Tax $=$ no-evidence $-$ with-evidence; positive $=$ cost.}\n\\label{tab:training_tax}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Fair w/ evi} & \\textbf{Fair no-evi} & \\textbf{Evi Tax} & \\textbf{Subset} \\\\\n\\midrule\nQwen3-1.7B & 48.38 & 42.75 & $-$5.63 & 971 \\\\\nQwen3-4B & -- & -- & +0.25{\\scriptsize$\\pm$0.47}$^{(3)}$ & $\\geq$982 \\\\\nQwen3-8B & 50.15 & 50.19 & +0.04 & 984 \\\\\nQwen3-14B & 55.07 & 55.10 & +0.03 & 985$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2mm}\n{\\raggedright\\footnotesize 1.7B and 8B are s42; 4B reports three-seed mean $\\pm$ std (per-seed range: $-$0.19 to +0.73pp); 14B evaluated at @1024 with 0\\% truncation for both configurations ($^\\dagger$fair subset equals full dev set). Subset: documents in format-compliant intersection out of 985.\\par}\n\\end{table}\n\n\n\\section{Why RSFT Avoids Decoupling}\n\\label{sec:rsft_theory}\n\nThe structural difference between selection and optimization explains why RSFT does not exhibit the decoupling observed in gradient-based methods. GRPO and DPO update model parameters through gradients that optimize a reward signal. When two sub-tasks (extraction and evidence) compete for gradient capacity, the optimizer can discover and exploit the trade-off between them, improving one at the expense of the other. RSFT operates differently: it selects complete outputs and trains on them with standard supervised loss. Because the selection is discrete (accept or reject a full response), there is no gradient pathway through which the model can learn to sacrifice extraction for evidence quality. Only outputs where both extraction and evidence are jointly strong survive the CED filter. This property is not specific to RSFT's design but is a structural consequence of discrete selection over complete outputs: any selection-based method that filters on a joint quality criterion will inherit the same coupling guarantee. The implication for practitioners is direct: when optimizing for multiple coupled generation objectives, selection-based methods preserve inter-objective balance that gradient-based methods disrupt.\n\n\n\\section{Decoupling Spectrum Visualization}\n\\label{sec:spectrum_viz}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_spectrum.pdf}\n\\caption{Decoupling spectrum visualization. Each method is plotted by Rel-F1 (x-axis) and Evi-F1 (y-axis). Arrows indicate training progression for DPO (1ep$\\to$3ep) and GRPO bf16 trajectory. Ideal methods occupy the upper-right quadrant; decoupled methods drift toward the upper-left.}\n\\label{fig:spectrum}\n\\end{figure}\n\n\n\\section{Evidence Tax Visualization}\n\\label{sec:scaling_viz}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_scaling.pdf}\n\\caption{Evidence tax across model scales. Bar heights show Ign-F1 for each training configuration. The gap between no-evidence and SFT bars reverses direction between 1.7B and 4B, revealing the scale-dependent nature of the evidence tax. RSFT consistently narrows the gap toward the no-evidence upper bound.}\n\\label{fig:scaling}\n\\end{figure}\n\n\n\\section{Full Generalization Results}\n\\label{sec:generalization_full}\n\n\\paragraph{Cross-family transfer.}\nLLaMA-3.1-8B confirms the scaling patterns observed with Qwen3. Its SFT baseline achieves a three-seed mean of 51.09 Ign-F1 (std 2.92pp; s42: 53.84, s43: 51.42, s44: 48.02), and the s42 no-evidence variant reaches 54.52 Ign-F1 (Rel-F1 56.24). The s42 evidence tax of +0.68 points mirrors the near-zero tax seen for Qwen3-8B (+0.04pp under matched@2048 fair evaluation), supporting our claim that 8B-class models absorb the cost of joint evidence generation regardless of architecture family. However, LLaMA SFT training-time tax is highly seed-dependent (per-seed range: $-$2.83 to +1.20pp under matched@2048), precluding a reliable single estimate. RSFT CED improves LLaMA to a three-seed mean of 56.54 Ign-F1 (std 0.64pp; s42: 57.14, s43: 56.62, s44: 55.87), a +5.45 point gain over SFT mean (51.09), with 4.6$\\times$ variance compression (2.92pp $\\to$ 0.64pp), consistent with the pattern at the 8B scale (Qwen3-8B: +4.33, 17$\\times$ compression).\n\n\\paragraph{Cross-dataset robustness.}\nOn Re-DocRED~\\citep{tan2022redocred}, the SFT baseline achieves 36.59 Ign-F1 (Evi-F1 81.70, EDCR 0.6674). RSFT CED improves this to 41.45 Ign-F1 (Evi-F1 81.82, EDCR 0.6210), a +4.86pp gain that closely matches the +5.08pp improvement on DocRED (RSFT three-seed mean minus SFT s42). This consistency across datasets with different annotation protocols confirms that RSFT's benefit generalizes beyond training-set-specific artifacts. Evidence quality remains stable across datasets (Evi-F1 81.82 vs.\\ 81.15 on DocRED), and the EDCR reduction ($-0.046$) mirrors the DocRED pattern, further supporting the robustness of CED-based selection.\n\n\\paragraph{Re-DocRED test set evaluation.}\nTable~\\ref{tab:test_results} reports RSFT performance on the Re-DocRED test set. We observe a consistent performance gap between dev and test sets, with test Ign-F1 approximately 20 percentage points lower (1.7B: 51.2$\\to$29.3, 8B: 54.5$\\to$33.5, 14B: 58.9$\\to$38.5, LLaMA-8B: 56.5$\\to$36.0). This gap is attributable to annotation density: the test set contains 34.7 gold triples per document versus 12.3 in the dev set (a 2.82$\\times$ ratio), imposing a harder recall requirement. The gap magnitude is stable across four scales and two architectures (range: 20.4--21.9pp), and model ranking is perfectly preserved (Spearman $\\rho{=}1.0$), indicating that the absolute drop reflects the test annotation scheme rather than a model-specific deficiency.\n\n\\begin{table}[t]\n\\centering\n\\caption{RSFT performance on Re-DocRED test set (Ign-F1 \\%). Dev Ign-F1 from Table~\\ref{tab:scaling}. SFT test baselines pending. All test results are s42.}\n\\label{tab:test_results}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Dev} & \\textbf{Test} & \\textbf{Evi-F1} & \\textbf{EDCR} & \\textbf{Trunc.\\%} \\\\\n\\midrule\nQwen3-1.7B & 51.19 & 29.33 & 23.20 & 0.817 & 73.8 \\\\\nQwen3-8B & 54.52 & 33.53 & 25.26 & 0.799 & 1.8 \\\\\nQwen3-14B & 58.86 & 38.49 & 26.88 & 0.787 & 13.4 \\\\\nLLaMA-3.1-8B & 56.54 & 35.99 & 25.09 & 0.839 & 56.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Comparison to supervised methods.}\nTable~\\ref{tab:encoder_comparison} directly compares encoder-based methods with our LLM-based approach. Encoder methods achieve substantially higher extraction performance (Rel-F1 63--65 vs.\\ our 45--56), reflecting decades of architecture-specific optimization for the classification formulation. However, their evidence identification operates as binary sentence classification, producing Evi-F1 of 52--56 under a joint evaluation protocol. Our TP-only Evi-F1 exceeds 80\\%, indicating that when the model correctly identifies a triple, it produces higher-quality evidence than encoder methods. The joint Evi-F1 gap (36.1 vs.\\ 54.15) is driven primarily by extraction performance rather than evidence quality: false-positive and false-negative triples dilute the denominator. Closing this gap requires improving extraction capability of LLM-based methods, an orthogonal direction to the evidence faithfulness problem we address.\n\n\\begin{table}[t]\n\\centering\n\\caption{Comparison with encoder-based methods on DocRED dev set. Encoder methods use RoBERTa-large; LLM methods use Qwen3. Evi-F1 for encoder methods uses joint evaluation (all triples in denominator); our joint Evi-F1 follows the same protocol for fair comparison. TP-only Evi-F1 conditions on correctly predicted triples. Rel-F1 is reported in percentage for all methods.}\n\\label{tab:encoder_comparison}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Type} & \\textbf{Ign-F1} & \\textbf{Rel-F1} & \\textbf{Evi-F1 (joint)} & \\textbf{Evi-F1 (TP)} \\\\\n\\midrule\nATLOP & Encoder & 61.32 & 63.18 & -- & -- \\\\\nEIDER & Encoder & 62.34 & 64.27 & 52.54 & -- \\\\\nSAIS & Encoder & 62.23 & 65.17 & 55.84 & -- \\\\\nDREEAM & Encoder & 61.71 & 63.49 & 54.15 & -- \\\\\n\\midrule\nOurs (4B RSFT) & LLM & 44.82 & 45.80 & 36.1 & 80.96 \\\\\nOurs (8B RSFT) & LLM & 54.52 & 56.26 & -- & 81.26 \\\\\nOurs (14B RSFT) & LLM & 58.86 & 60.09 & 48.59 & 83.92 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\n\\section{GRPO Training Dynamics}\n\\label{sec:grpo_dynamics}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig_grpo_dynamics.pdf}\n\\caption{Training dynamics of GRPO under different configurations. (a)~Relation F1 across checkpoints: G=4 QLoRA suffers catastrophic collapse at step~10, while G=8 bf16 remains stable. (b)~Evidence F1 stays intact for G=8 bf16, confirming the generation mechanism itself does not fail. (c)~Evidence-Decoupling Ratio (EDCR) reveals near-total decoupling in G=4 QLoRA (extraction collapses to Rel-F1 1.4), while G=8 bf16 maintains healthy ratios.}\n\\label{fig:grpo_dynamics}\n\\end{figure*}\n\n\n\\section{Error Analysis: SFT vs.\\ RSFT}\n\\label{sec:error_analysis}\n\nTable~\\ref{tab:error_analysis} decomposes the extraction improvements from RSFT into error categories across three scales. Three mechanisms drive the gains consistently:\n\n\\paragraph{Truncation false negatives.} SFT models frequently hit the generation length limit, producing incomplete outputs that miss triples. RSFT training on compact, high-quality outputs reduces this truncation rate. The effect is strongest at 1.7B ($-841$ truncation FN, $-22$\\%), where the SFT model's output length is least controlled.\n\n\\paragraph{Hallucinated false positives.} CED-based filtering removes training examples with unfaithful predictions, reducing the rate of hallucinated triples at inference. LLaMA benefits most ($-593$ hallucinated FP, $-11.8$\\%), suggesting cross-architecture variation in hallucination susceptibility.\n\n\\paragraph{Duplicate predictions.} RSFT training data, selected for quality, contains fewer repetitive patterns. This propagates to inference, reducing duplicate triples by $11$--$20$\\% across scales, with 1.7B showing the largest reduction ($-20.2$\\%).\n\n\\paragraph{Evidence quality unchanged.} Despite substantial extraction improvements, evidence exact-match F1 changes by less than 0.4pp at every scale. RSFT selects for joint extraction-evidence quality, but the evidence signal in CED scoring does not translate into measurable evidence improvement. This suggests that evidence grounding requires targeted optimization (e.g., evidence-specific rewards in RL) rather than data selection alone.\n\n\\paragraph{Residual difficulty.} The proportion of ``other'' false negatives (triples missed for reasons beyond truncation or formatting) increases by 13--15\\% in relative terms after RSFT. As easy errors (truncation, duplication) are eliminated, the remaining error distribution shifts toward harder cases: cross-sentence reasoning, implicit relations, and long-tail entity pairs. The relation types with the largest RSFT gains (participant, conflict, league, screenwriter, operator, contains\\_administrative\\_territory) involve cross-sentence reasoning or long-tail entities, consistent with RSFT's selection pressure toward diverse, high-quality outputs.\n\n\\begin{table}[t]\n\\centering\n\\caption{Error pattern changes from SFT to RSFT across scales. $\\Delta$\\% shows relative change. Truncation FN, hallucinated FP, and duplicates all decrease; evidence quality and residual FN difficulty are unchanged.}\n\\label{tab:error_analysis}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Error Category} & \\textbf{Direction} & \\textbf{1.7B} & \\textbf{4B} & \\textbf{8B / LLaMA} \\\\\n\\midrule\nTruncation FN & $\\downarrow$ & $-$22\\% & $-$16\\% & $-$18\\% \\\\\nHallucinated FP & $\\downarrow$ & $-$8\\% & $-$6\\% & $-$12\\% \\\\\nDuplicates & $\\downarrow$ & $-$20\\% & $-$11\\% & $-$14\\% \\\\\nEvidence (exact) & $\\approx$ & $<$0.4pp & $<$0.4pp & $<$0.4pp \\\\\nFN: other & $\\uparrow$ & +13\\% & +15\\% & +14\\% \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\n\\section{Per-Relation EDCR Distribution}\n\\label{sec:edcr_per_relation}\n\nComputing EDCR for each of the 76 relation types with $\\geq$5 evaluation samples (from the RSFT CED s42 model) reveals that per-relation EDCR correlates strongly with per-relation Rel-F1 ($\\rho = -0.79$, $n = 76$, $p < 0.001$), confirming its utility as a difficulty indicator. Filtering to types with $\\geq$5 predictions strengthens the correlation ($\\rho = -0.85$, $n = 74$, $p < 0.001$). Per-relation EDCR is statistically independent of Evi-F1 ($\\rho = -0.06$, $p = 0.58$), and Evi-F1 itself shows no association with Rel-F1 ($\\rho = -0.01$, $p = 0.91$). These null correlations establish that evidence quality and extraction ability are fully decoupled across relation types. Extreme cases illustrate the diagnostic power: \\texttt{date\\_of\\_birth} has EDCR $= 0.118$ (highly faithful, with extraction and evidence tightly coupled), while \\texttt{head\\_of\\_government} reaches $0.956$ (highly decoupled). This per-relation analysis avoids the shared-component concern present in cross-method EDCR-vs-Rel-F1 correlation, providing independent validation of EDCR's diagnostic utility.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig_edcr_relations.pdf}\n\\caption{Per-relation EDCR distribution across all 93 relation types observed in the development set (of 96 defined in DocRED). The correlation analysis in the text uses the 76 types with $\\geq$5 samples for statistical reliability. Red bars indicate EDCR $\\geq$ 0.70 (severe decoupling), green bars indicate EDCR $<$ 0.30 (healthy evidence grounding). Seven types exhibit EDCR = 1.0.}\n\\label{fig:edcr_relations}\n\\end{figure}\n\n\n\\section{Qualitative Analysis}\n\\label{sec:qualitative}\n\nWe present representative examples illustrating three phenomena: evidence quality differences between SFT and RSFT, GRPO format gaming under catastrophic collapse, and per-relation EDCR diagnostics.\n\n\\paragraph{Case 1: Evidence quality.}\nTable~\\ref{tab:case_evidence} compares evidence citations from SFT and RSFT on three documents. SFT tends to cite many sentences indiscriminately, including distractors unrelated to the target triple, while RSFT selects precisely the gold evidence sentences. For \\emph{America's Sweetheart}, SFT cites 6 sentences (precision 0.17) whereas RSFT cites only the single correct sentence (precision 1.00). The pattern is consistent: SFT achieves evidence precision of 0.00--0.20 across these examples, while RSFT achieves 1.00 in all three cases.\n\n\\begin{table}[t]\n\\centering\n\\caption{Evidence citation comparison between SFT and RSFT. Precision measures the fraction of cited sentences that match gold evidence.}\n\\label{tab:case_evidence}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Document} & \\textbf{Triple} & \\textbf{SFT Prec.} & \\textbf{RSFT Prec.} & \\textbf{SFT \\#Cited} \\\\\n\\midrule\nOleg Tinkov & (Oleg Tinkov, country of citizenship, Russia) & 0.00 & 1.00 & 3 \\\\\nAmerica's Sweetheart & (record label, country, United States) & 0.17 & 1.00 & 6 \\\\\nJade (Mortal Kombat) & (Jade, present in work, Mortal Kombat) & 0.20 & 1.00 & 5 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\paragraph{Case 2: GRPO format gaming.}\nUnder catastrophic collapse (GRPO QLoRA $G{=}4$), the model abandons the DocRED 96-type relation ontology and generates free-text relation labels. On the document \\emph{Something to Believe In}, the model produces 35 predicted triples with relations such as ``is a'', ``honor'', and ``location'', none of which belong to the target ontology. All 35 predictions are incorrect. Similarly, for \\emph{J\\'{o}zef Pi\\l{}sudski Monument}, 28 predictions use non-standard relations with 0 correct matches. The model retains the structural format of triple-with-evidence output but fills it with fabricated relation types. The model produces well-formed evidence for these non-existent relations.\n\n\\paragraph{Case 3: EDCR diagnostics.}\nPer-relation EDCR identifies specific relation types where extraction and evidence are misaligned. For \\texttt{date\\_of\\_birth} (EDCR $= 0.118$), the model's evidence consistently matches gold annotations: both extraction and evidence point to the same biographical sentence. In contrast, \\texttt{notable\\_work} (EDCR $= 0.941$) exhibits severe decoupling: the model cites sentence [0] (a general introduction) instead of the gold evidence sentence [3] (which contains the actual work attribution). High-EDCR relations tend to involve indirect or multi-hop reasoning where surface-level context misleads the evidence generator.\n",
      "numLines": 281,
      "startLine": 60,
      "totalLines": 340
    }
  }
}
```

</details>

---

### Assistant

_source line 71_

Now I have a comprehensive picture. Let me check one more thing — the figures directory for paper figures.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "6096a800-1a88-464d-965e-5a055971b9a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbtvCSof7e7X5rBRbgYFC6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8939,
      "cache_read_input_tokens": 96127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8939
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

_source line 72_

<details open><summary>🔧 Tool call — Bash · `toolu_01DnG9ebbc6YEgnTY4L21mQ8`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/fig_*.{pdf,png} 2>/dev/null; ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/ 2>/dev/null || echo \"NO_FIGURES_DIR\"",
  "description": "Check paper figures"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "c78639c6-d3cc-4897-b0b0-c18dfbfa3130",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbtvCSof7e7X5rBRbgYFC6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8939,
      "cache_read_input_tokens": 96127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8939
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

_source line 73 · 2026-05-21T22:56:59.608Z_

<details><summary>↩ Tool result · `toolu_01DnG9ebbc6YEgnTY4L21mQ8`</summary>

```text
total 12
drwxr-xr-x  3 ubuntu ubuntu 4096 May 17 14:01 .
drwxr-xr-x 11 ubuntu ubuntu 4096 May 21 22:51 ..
drwxr-xr-x  3 ubuntu ubuntu 4096 May 17 18:49 paper
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "48788526-1248-4e15-aa2a-eaf5db027954",
  "tool_use_result": {
    "stdout": "total 12\ndrwxr-xr-x  3 ubuntu ubuntu 4096 May 17 14:01 .\ndrwxr-xr-x 11 ubuntu ubuntu 4096 May 21 22:51 ..\ndrwxr-xr-x  3 ubuntu ubuntu 4096 May 17 18:49 paper",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — Bash · `toolu_01LE9vfGG2hXnJdRwaZSjzEX`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/ -type f 2>/dev/null && find /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/ -maxdepth 1 -name \"fig_*\" 2>/dev/null",
  "description": "Find all figure files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "fdeb7f5c-7377-4ac5-bdfb-254b6589f64e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AgzZNfvSrboN5a5qF63y2q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 290,
      "cache_read_input_tokens": 105066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 290
      },
      "output_tokens": 60,
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

_source line 75 · 2026-05-21T22:57:03.687Z_

<details><summary>↩ Tool result · `toolu_01LE9vfGG2hXnJdRwaZSjzEX`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/plot_fig_grpo_dynamics.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/_pdf_images/fig_edcr_relations_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/plot_scaling.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/plot_overview.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/fig_grpo_dynamics.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/fig_grpo_dynamics.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/fig_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/fig_scaling.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/fig_spectrum.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/fig_scaling.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/fig_edcr_relations.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/fig_spectrum.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/plot_spectrum.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/fig_overview.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "11c40325-dbf8-495a-aae1-fabaa6e91a31",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/plot_fig_grpo_dynamics.py\n/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/_pdf_images/fig_edcr_relations_p1.png\n/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/plot_scaling.py\n/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/plot_overview.py\n/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/fig_grpo_dynamics.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/fig_grpo_dynamics.png\n/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/fig_overview.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/fig_scaling.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/fig_spectrum.png\n/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/fig_scaling.png\n/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/fig_edcr_relations.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/fig_spectrum.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/plot_spectrum.py\n/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/fig_overview.png",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 76_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture. Let me write the audit report.

Summary of findings:

**LaTeX Paper State:**
- `abstract.tex` (18 lines) — COMPLETE, updated with matched@2048 numbers
- `introduction.tex` (35 lines) — COMPLETE, 3 contributions, updated framing
- `related_work.tex` (30 lines) — COMPLETE, three thematic paragraphs
- `method.tex` (64 lines) — COMPLETE, all subsections filled
- `experiments.tex` (132 lines) — COMPLETE, with tables for main results, spectrum, scaling, evidence strategy, generalization


- `analysis.tex` (14 lines) — COMPLETE but SHORT (4 paragraphs)
- `conclusion.tex` (4 lines) — COMPLETE (single paragraph)
- `limitations.tex` (19 lines) — COMPLETE with ethics statement
- `appendix.tex` (339 lines) — EXTENSIVE, includes hyperparams, ablation, scaling details, fair subset, training tax, RSFT theory, visualizations, generalization, GRPO dynamics, error analysis, EDCR per-relation, qualitative analysis
- `references.bib` (301 lines) — EXISTS
- `main.tex` (42 lines) — EXISTS

**Figures:**
- fig_overview.pdf ✅
- fig_spectrum.pdf ✅
- fig_scaling.pdf ✅
- fig

_edcr_relations.pdf ✅
- fig_grpo_dynamics.pdf ✅

Now I'm checking the test results and artifacts. The test table draft has mostly pending results, but the appendix already contains the proper test results table with the numbers I need. I also have a detailed audit document that flags several locations where numbers need updating, with the old values marked for revision.

Looking at the actual tex files, I can see the abstract, intro, and conclusion have already been corrected with the right numbers. The dev-test gap paragraph exists and is already integrated into the appendix. The main results table and scaling table in experiments.tex both look well-populated with the 4B and 5-model results respectively.

I don't see any specific CodaLab submission materials yet. - Test results are from Re-DocRED test set (not CodaLab DocRED test)
- review_issues.yaml W2 marks this as critical & in_progress

**Key gaps identified:**

1. **Evidence tax numbers in .tex files**: The evidence_tax_annotation_notes.md identifies corrections needed, but checking the actual .tex, the abstract/intro/conclusion ALREADY use corrected numbers (-5.63pp, +0.25pp). So this is DONE.

2. **Test table in appendix**: Already in appendix.tex (tab_test_results) with actual numbers. The test_table_draft.md artifact is stale.

3. **Missing from paper**: No DocRED test set results (only Re-DocRED test). CodaLab submission not done. This is flagged in review_issues.yaml W2.

4. **4B test results**: Lost due to checkpoint failure, so the test table can't include them.

5. **SFT test baselines**: Still pending for all models.

6. **Figures**: All 5 planned figures exist as PDFs in the figures/paper/ directory, but I need to verify they're properly accessible from the tex compilation directory—they may need to be symlinked or copied to docs/paper/ since the appendix references them directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "4d99fee8-c0e5-4bb7-a9d6-8d08cbf0522a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FonYHtSsmgghoXkaRxzjp1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 734,
      "cache_read_input_tokens": 105356,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 734
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

_source line 77_

Now I have a complete picture. Let me write the audit report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "9e50a342-581d-4563-8c9d-27905e2b5af6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FonYHtSsmgghoXkaRxzjp1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 734,
      "cache_read_input_tokens": 105356,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 734
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

_source line 78_

<details open><summary>🔧 Tool call — Write · `toolu_0172rvCTtr14iXsVhGDV7oAJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/paper_status_audit.md",
  "content": "# Paper Status Audit (2026-05-22)\n\n## 已完成的章节/段落\n\n### LaTeX 正文（docs/paper/sections/）\n\n- **abstract.tex** (18行): 完整。已使用 D144 修正后的 matched@2048 数字（-5.63pp@1.7B, +0.25±0.47pp@4B）。包含三维度 landscape、variance compression、1.7B→8B 跨 scale 对比。\n- **introduction.tex** (35行): 完整。5段结构，3 contributions（landscape + spectrum + RSFT），已降级 CED 为组件、EDCR 为分析工具。数字已同步修正。\n- **related_work.tex** (30行): 完整。3 主题段（DocRE+evidence / RL alignment / self-training），引用覆盖 SAIS/DREEAM/EIDER/ATLOP/AutoRE/GRPO/DPO/STaR 等，DAPO/Dr.GRPO/R1-RE/REAR 新文献已加入。\n- **method.tex** (64行): 完整。5 小节（Task formulation / SFT baseline / Paradigms: GRPO+DPO+RSFT / CED scoring / EDCR definition），CED 公式和 EDCR 公式已写入，flat-NLI 等效性已说明。\n- **experiments.tex** (132行): 完整。6 小节（Setup / Main Results + tab:main / Decoupling Spectrum + tab:spectrum / Scaling + tab:scaling / Evidence Strategy / Generalization），所有主表已填数。包含 RSFT inference-time tax 和 LLaMA variance compression。\n- **analysis.tex** (14行): 完整但简短。4 段（EDCR diagnostic / Ablation / Error patterns / Practical implications）。内容足够但偏紧凑。\n- **conclusion.tex** (4行): 完整。单段总结三维度+RSFT 效果。\n- **limitations.tex** (19行): 完整。含 Ethics Statement 和 ARR checklist 注释。覆盖 dev-set / exact-match / 单 RL 算法 / EDCR 未做 human validation / evidence quality unchanged 等 6 点。\n- **appendix.tex** (339行): 大量内容。包含 13 个 section：Hyperparams / Full Ablation / Scaling Details / Controlled Eval Subset / Training-Time Tax / RSFT Theory / Spectrum Viz / Scaling Viz / Generalization (cross-family + cross-dataset + Re-DocRED test + encoder comparison) / GRPO Dynamics / Error Analysis / EDCR Per-Relation / Qualitative Analysis。\n\n### 表格\n\n| 表格 | 位置 | 状态 |\n|------|------|------|\n| tab:main (4B主结果) | experiments.tex | ✅ 已填数 |\n| tab:spectrum (decoupling) | experiments.tex | ✅ 已填数 |\n| tab:scaling (5模型) | experiments.tex | ✅ 已填数 |\n| tab:hyperparams | appendix.tex | ✅ 已填数 |\n| tab:ablation_full | appendix.tex | ✅ CED 4-seed + flat-NLI 2-seed + random + k=3 + v3-large |\n| tab:cross_detail | appendix.tex | ✅ 5模型 Rel-F1/Evi-F1 |\n| tab:mechanistic | appendix.tex | ✅ 3-scale duplication/truncation |\n| tab:training_tax | appendix.tex | ✅ matched@2048 4-scale |\n| tab:test_results (Re-DocRED test) | appendix.tex | ✅ 4模型 test Ign-F1 |\n| tab:encoder_comparison | appendix.tex | ✅ ATLOP/EIDER/SAIS/DREEAM vs ours |\n| tab:error_analysis | appendix.tex | ✅ 3-scale error decomposition |\n| tab:case_evidence | appendix.tex | ✅ 3 qualitative examples |\n\n### 图表\n\n| 图表 | 文件 | 状态 |\n|------|------|------|\n| fig_overview (task+pipeline) | figures/paper/fig_overview.pdf | ✅ 已生成 |\n| fig_spectrum (decoupling scatter) | figures/paper/fig_spectrum.pdf | ✅ 已生成 |\n| fig_scaling (evidence tax bars) | figures/paper/fig_scaling.pdf | ✅ 已生成 |\n| fig_edcr_relations (per-relation) | figures/paper/fig_edcr_relations.pdf | ✅ 已生成 |\n| fig_grpo_dynamics (training curves) | figures/paper/fig_grpo_dynamics.pdf | ✅ 已生成 |\n\n### 其他\n\n- **references.bib** (301行): 已有，覆盖主要引用\n- **main.tex** (42行): 结构完整，引用所有 section 文件\n- **main.pdf** (10页): 已编译版本存在\n\n### Artifacts 中的关键支撑文件\n\n- **comprehensive_results.md**: 10 张结果表，涵盖 scale×method / evidence metrics / variance / tax / ablation / GRPO / CED reranker / cross-arch / Re-DocRED / DREEAM\n- **paper_evidence_table.md**: 4 claims 的实验证据映射 + gap 清单\n- **evidence_tax_annotation_notes.md**: 审计 → 已应用到 .tex（+7.5pp→+0.25pp，-6.2pp→-5.63pp）\n- **dev_test_gap_paragraph.md**: 已整合到 appendix.tex §generalization_full\n- **test_table_draft.md**: 已过时（appendix 中 tab:test_results 更完整）\n- **negative_review.md**: 18 个 negative 实验系统复盘\n\n---\n\n## 缺失/需要更新\n\n### CRITICAL（阻塞提交）\n\n1. **DocRED 官方 test set 结果缺失**\n   - 当前只有 Re-DocRED test（非官方 benchmark）\n   - CodaLab 提交未完成（review_issues.yaml W2 标记 critical）\n   - 需要：用户提交 CodaLab，获取官方 test 分数\n   - Limitations 中已提前声明 \"test set submission is pending\"\n\n2. **SFT test baselines 全部缺失**\n   - tab:test_results 只有 RSFT test 分数，无 SFT 对比\n   - 无法在 test set 上计算 RSFT gain\n   - 需要：SFT models 的 test predictions + CodaLab 提交\n\n3. **4B test 数据不可恢复**\n   - 4B RSFT s42 checkpoint 丢失，test_table_draft.md 标记 \"irrecoverable\"\n   - tab:test_results 中 4B 行缺失\n   - 需要：决定是否接受 4B 无 test 数据，或从 4B RSFT Method B (s44) 补充\n\n### HIGH（显著削弱论文）\n\n4. **Figure 文件路径可能未对齐**\n   - 图在 `figures/paper/` 目录下，但 .tex 引用 `fig_spectrum.pdf` 等（无路径前缀）\n   - 编译时需确保图在 docs/paper/ 下或 graphicspath 正确设置\n   - 需要：验证 LaTeX 编译是否能找到图\n\n5. **Evidence tax annotation 修正验证**\n   - evidence_tax_annotation_notes.md 标记了 5 处需修改的位置（abstract:11, intro:24, intro:30, experiments:92, conclusion:4）\n   - 当前 .tex 已使用修正后数字，但需确认 ALL instances 都已更新\n   - 需要：全文搜索 \"+7.5\" 和 \"-6.2\" 确认无残留\n\n6. **flat-NLI ablation Ign-F1 缺失**\n   - tab:ablation_full 中 flat-NLI s42/s43 的 Ign-F1 列为 \"--\"\n   - CED 有 4-seed Ign-F1，flat-NLI 只有 Rel-F1\n   - 需要：flat-NLI 的 Ign-F1 数据（或在表注中说明）\n\n7. **14B RSFT Rel-F1/Evi-F1/EDCR 在 tab:cross_detail 中缺失**\n   - 14B RSFT 行显示 \"--\"\n   - 但 tab:scaling 有 14B RSFT Ign-F1=58.86\n   - 需要：14B RSFT 的 Rel-F1 和 Evi-F1 填入 cross_detail\n\n### MEDIUM（改进质量）\n\n8. **CED reranker 结果未在主表中**\n   - writing_plan.yaml 中 tab:main 规划包含 CED reranker 行\n   - 当前 tab:main 只有 SFT / SFT-no-evi / RSFT CED 三行\n   - CED reranker 数据在 Evidence Strategy 小节中提到但无独立表行\n   - 需要：决定是否加入主表（Ign-F1 仍为 TBD）\n\n9. **CodaLab 提交材料未准备**\n   - 无 prediction 格式化脚本、submission 文件\n   - 需要：pred-to-codalab 转换工具 + 用户手动提交\n\n10. **Review issues 跟进状态**\n    - review_issues.yaml 记录 22 个 issue，多数 status=in_progress\n    - W1 (GRPO confound): 部分解决（已加 GRPO bf16 G=4 实验？需确认）\n    - W3 (SFT single seed): 已解决（现有 3-seed SFT）\n    - W4 (non-monotonic): 已解决（叙事已从 non-monotonic 改为 within-family threshold）\n\n---\n\n## 下一步建议\n\n### P0（提交前必须完成）\n\n1. **验证 LaTeX 编译**：确认 figures 路径、bib 引用、所有 \\ref 和 \\label 正确。编译 main.pdf 检查页数（8页限制）\n2. **全文搜索旧数字**：grep \"+7.5\" / \"-6.2\" / \"non-monotonic\" / \"costly at 4B\" / \"capacity valley\"，确认无残留\n3. **确认 DocRED test 策略**：要么完成 CodaLab 提交，要么在 Limitations 中明确说明只有 Re-DocRED test\n\n### P1（显著提升论文质量）\n\n4. **补充 SFT test baselines**：至少 1-2 个 scale 的 SFT test 分数，用于计算 test-set RSFT gain\n5. **补全 flat-NLI Ign-F1**：填充 tab:ablation_full 中 flat-NLI 的 Ign-F1 列\n6. **补全 14B RSFT 详细指标**：tab:cross_detail 中 14B 行\n7. **考虑加入 CED reranker 到主表**：如果 Ign-F1 可计算\n\n### P2（锦上添花）\n\n8. **更新 review_issues.yaml**：标记已解决的 issues\n9. **清理过时 artifacts**：test_table_draft.md 已被 appendix 取代\n10. **检查页数**：main.pdf 当前 10 页，需确认主文 ≤8 页（references + appendix 不计）\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "a672895a-c78a-4ad7-85b5-f3167a2527e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FonYHtSsmgghoXkaRxzjp1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 734,
      "cache_read_input_tokens": 105356,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 734
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

_source line 79 · 2026-05-21T22:58:44.859Z_

<details><summary>↩ Tool result · `toolu_0172rvCTtr14iXsVhGDV7oAJ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/paper_status_audit.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "86701f50-b7b3-4e87-81d3-dd12e00164c8",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/paper_status_audit.md",
    "content": "# Paper Status Audit (2026-05-22)\n\n## 已完成的章节/段落\n\n### LaTeX 正文（docs/paper/sections/）\n\n- **abstract.tex** (18行): 完整。已使用 D144 修正后的 matched@2048 数字（-5.63pp@1.7B, +0.25±0.47pp@4B）。包含三维度 landscape、variance compression、1.7B→8B 跨 scale 对比。\n- **introduction.tex** (35行): 完整。5段结构，3 contributions（landscape + spectrum + RSFT），已降级 CED 为组件、EDCR 为分析工具。数字已同步修正。\n- **related_work.tex** (30行): 完整。3 主题段（DocRE+evidence / RL alignment / self-training），引用覆盖 SAIS/DREEAM/EIDER/ATLOP/AutoRE/GRPO/DPO/STaR 等，DAPO/Dr.GRPO/R1-RE/REAR 新文献已加入。\n- **method.tex** (64行): 完整。5 小节（Task formulation / SFT baseline / Paradigms: GRPO+DPO+RSFT / CED scoring / EDCR definition），CED 公式和 EDCR 公式已写入，flat-NLI 等效性已说明。\n- **experiments.tex** (132行): 完整。6 小节（Setup / Main Results + tab:main / Decoupling Spectrum + tab:spectrum / Scaling + tab:scaling / Evidence Strategy / Generalization），所有主表已填数。包含 RSFT inference-time tax 和 LLaMA variance compression。\n- **analysis.tex** (14行): 完整但简短。4 段（EDCR diagnostic / Ablation / Error patterns / Practical implications）。内容足够但偏紧凑。\n- **conclusion.tex** (4行): 完整。单段总结三维度+RSFT 效果。\n- **limitations.tex** (19行): 完整。含 Ethics Statement 和 ARR checklist 注释。覆盖 dev-set / exact-match / 单 RL 算法 / EDCR 未做 human validation / evidence quality unchanged 等 6 点。\n- **appendix.tex** (339行): 大量内容。包含 13 个 section：Hyperparams / Full Ablation / Scaling Details / Controlled Eval Subset / Training-Time Tax / RSFT Theory / Spectrum Viz / Scaling Viz / Generalization (cross-family + cross-dataset + Re-DocRED test + encoder comparison) / GRPO Dynamics / Error Analysis / EDCR Per-Relation / Qualitative Analysis。\n\n### 表格\n\n| 表格 | 位置 | 状态 |\n|------|------|------|\n| tab:main (4B主结果) | experiments.tex | ✅ 已填数 |\n| tab:spectrum (decoupling) | experiments.tex | ✅ 已填数 |\n| tab:scaling (5模型) | experiments.tex | ✅ 已填数 |\n| tab:hyperparams | appendix.tex | ✅ 已填数 |\n| tab:ablation_full | appendix.tex | ✅ CED 4-seed + flat-NLI 2-seed + random + k=3 + v3-large |\n| tab:cross_detail | appendix.tex | ✅ 5模型 Rel-F1/Evi-F1 |\n| tab:mechanistic | appendix.tex | ✅ 3-scale duplication/truncation |\n| tab:training_tax | appendix.tex | ✅ matched@2048 4-scale |\n| tab:test_results (Re-DocRED test) | appendix.tex | ✅ 4模型 test Ign-F1 |\n| tab:encoder_comparison | appendix.tex | ✅ ATLOP/EIDER/SAIS/DREEAM vs ours |\n| tab:error_analysis | appendix.tex | ✅ 3-scale error decomposition |\n| tab:case_evidence | appendix.tex | ✅ 3 qualitative examples |\n\n### 图表\n\n| 图表 | 文件 | 状态 |\n|------|------|------|\n| fig_overview (task+pipeline) | figures/paper/fig_overview.pdf | ✅ 已生成 |\n| fig_spectrum (decoupling scatter) | figures/paper/fig_spectrum.pdf | ✅ 已生成 |\n| fig_scaling (evidence tax bars) | figures/paper/fig_scaling.pdf | ✅ 已生成 |\n| fig_edcr_relations (per-relation) | figures/paper/fig_edcr_relations.pdf | ✅ 已生成 |\n| fig_grpo_dynamics (training curves) | figures/paper/fig_grpo_dynamics.pdf | ✅ 已生成 |\n\n### 其他\n\n- **references.bib** (301行): 已有，覆盖主要引用\n- **main.tex** (42行): 结构完整，引用所有 section 文件\n- **main.pdf** (10页): 已编译版本存在\n\n### Artifacts 中的关键支撑文件\n\n- **comprehensive_results.md**: 10 张结果表，涵盖 scale×method / evidence metrics / variance / tax / ablation / GRPO / CED reranker / cross-arch / Re-DocRED / DREEAM\n- **paper_evidence_table.md**: 4 claims 的实验证据映射 + gap 清单\n- **evidence_tax_annotation_notes.md**: 审计 → 已应用到 .tex（+7.5pp→+0.25pp，-6.2pp→-5.63pp）\n- **dev_test_gap_paragraph.md**: 已整合到 appendix.tex §generalization_full\n- **test_table_draft.md**: 已过时（appendix 中 tab:test_results 更完整）\n- **negative_review.md**: 18 个 negative 实验系统复盘\n\n---\n\n## 缺失/需要更新\n\n### CRITICAL（阻塞提交）\n\n1. **DocRED 官方 test set 结果缺失**\n   - 当前只有 Re-DocRED test（非官方 benchmark）\n   - CodaLab 提交未完成（review_issues.yaml W2 标记 critical）\n   - 需要：用户提交 CodaLab，获取官方 test 分数\n   - Limitations 中已提前声明 \"test set submission is pending\"\n\n2. **SFT test baselines 全部缺失**\n   - tab:test_results 只有 RSFT test 分数，无 SFT 对比\n   - 无法在 test set 上计算 RSFT gain\n   - 需要：SFT models 的 test predictions + CodaLab 提交\n\n3. **4B test 数据不可恢复**\n   - 4B RSFT s42 checkpoint 丢失，test_table_draft.md 标记 \"irrecoverable\"\n   - tab:test_results 中 4B 行缺失\n   - 需要：决定是否接受 4B 无 test 数据，或从 4B RSFT Method B (s44) 补充\n\n### HIGH（显著削弱论文）\n\n4. **Figure 文件路径可能未对齐**\n   - 图在 `figures/paper/` 目录下，但 .tex 引用 `fig_spectrum.pdf` 等（无路径前缀）\n   - 编译时需确保图在 docs/paper/ 下或 graphicspath 正确设置\n   - 需要：验证 LaTeX 编译是否能找到图\n\n5. **Evidence tax annotation 修正验证**\n   - evidence_tax_annotation_notes.md 标记了 5 处需修改的位置（abstract:11, intro:24, intro:30, experiments:92, conclusion:4）\n   - 当前 .tex 已使用修正后数字，但需确认 ALL instances 都已更新\n   - 需要：全文搜索 \"+7.5\" 和 \"-6.2\" 确认无残留\n\n6. **flat-NLI ablation Ign-F1 缺失**\n   - tab:ablation_full 中 flat-NLI s42/s43 的 Ign-F1 列为 \"--\"\n   - CED 有 4-seed Ign-F1，flat-NLI 只有 Rel-F1\n   - 需要：flat-NLI 的 Ign-F1 数据（或在表注中说明）\n\n7. **14B RSFT Rel-F1/Evi-F1/EDCR 在 tab:cross_detail 中缺失**\n   - 14B RSFT 行显示 \"--\"\n   - 但 tab:scaling 有 14B RSFT Ign-F1=58.86\n   - 需要：14B RSFT 的 Rel-F1 和 Evi-F1 填入 cross_detail\n\n### MEDIUM（改进质量）\n\n8. **CED reranker 结果未在主表中**\n   - writing_plan.yaml 中 tab:main 规划包含 CED reranker 行\n   - 当前 tab:main 只有 SFT / SFT-no-evi / RSFT CED 三行\n   - CED reranker 数据在 Evidence Strategy 小节中提到但无独立表行\n   - 需要：决定是否加入主表（Ign-F1 仍为 TBD）\n\n9. **CodaLab 提交材料未准备**\n   - 无 prediction 格式化脚本、submission 文件\n   - 需要：pred-to-codalab 转换工具 + 用户手动提交\n\n10. **Review issues 跟进状态**\n    - review_issues.yaml 记录 22 个 issue，多数 status=in_progress\n    - W1 (GRPO confound): 部分解决（已加 GRPO bf16 G=4 实验？需确认）\n    - W3 (SFT single seed): 已解决（现有 3-seed SFT）\n    - W4 (non-monotonic): 已解决（叙事已从 non-monotonic 改为 within-family threshold）\n\n---\n\n## 下一步建议\n\n### P0（提交前必须完成）\n\n1. **验证 LaTeX 编译**：确认 figures 路径、bib 引用、所有 \\ref 和 \\label 正确。编译 main.pdf 检查页数（8页限制）\n2. **全文搜索旧数字**：grep \"+7.5\" / \"-6.2\" / \"non-monotonic\" / \"costly at 4B\" / \"capacity valley\"，确认无残留\n3. **确认 DocRED test 策略**：要么完成 CodaLab 提交，要么在 Limitations 中明确说明只有 Re-DocRED test\n\n### P1（显著提升论文质量）\n\n4. **补充 SFT test baselines**：至少 1-2 个 scale 的 SFT test 分数，用于计算 test-set RSFT gain\n5. **补全 flat-NLI Ign-F1**：填充 tab:ablation_full 中 flat-NLI 的 Ign-F1 列\n6. **补全 14B RSFT 详细指标**：tab:cross_detail 中 14B 行\n7. **考虑加入 CED reranker 到主表**：如果 Ign-F1 可计算\n\n### P2（锦上添花）\n\n8. **更新 review_issues.yaml**：标记已解决的 issues\n9. **清理过时 artifacts**：test_table_draft.md 已被 appendix 取代\n10. **检查页数**：main.pdf 当前 10 页，需确认主文 ≤8 页（references + appendix 不计）\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 80_

Now register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "366edd3b-d0fe-4089-a851-b8e455e1ffd5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019sjVfua5gg9DhSYFY7t4c8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4578,
      "cache_read_input_tokens": 106090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4578
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

_source line 81_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UboMZ93RLZc7GH3BFa8zWJ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
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
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "a03dcc88-dcff-4b96-99cf-da64e91eccc2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019sjVfua5gg9DhSYFY7t4c8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4578,
      "cache_read_input_tokens": 106090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4578
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

_source line 82 · 2026-05-21T22:58:51.489Z_

<details><summary>↩ Tool result · `toolu_01UboMZ93RLZc7GH3BFa8zWJ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "ebf9aab2-357c-492b-a7b3-c36f84740513",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 83_

审计报告已写入 `artifacts/paper_status_audit.md`。

核心结论：

**论文主体已基本完成**——8个 LaTeX section 全部有实质内容，12张表格已填数，5张图已生成，references.bib 301行。evidence_tax 数字修正（+7.5→+0.25, -6.2→-5.63）已应用到 .tex。dev_test_gap 段落已整合到 appendix。

**3个 CRITICAL gap：**
1. **DocRED 官方 test set 缺失**——只有 Re-DocRED test，CodaLab 未提交
2. **SFT test baselines 全部缺失**——test 表无法计算 RSFT gain
3. **4B test checkpoint 不可恢复**——test 表缺 4B 行

**需要立即验证的：**
- LaTeX 编译（figures 路径是否对齐、页数是否 ≤8 页主文）
- 全文 grep 旧数字残留（"+7.5" / "-6.2" / "non-monotonic"）
- flat-NLI Ign-F1 和 14B RSFT 详细指标在附录表中仍为 "--"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "uuid": "3d6fdad6-9522-4f83-8c8f-cfbc94fb0c26",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CJgA2AwzVoHoW8C3EM872u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 471,
      "cache_read_input_tokens": 110668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 471
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

_source line 84_

审计报告已写入 `artifacts/paper_status_audit.md`。

核心结论：

**论文主体已基本完成**——8个 LaTeX section 全部有实质内容，12张表格已填数，5张图已生成，references.bib 301行。evidence_tax 数字修正（+7.5→+0.25, -6.2→-5.63）已应用到 .tex。dev_test_gap 段落已整合到 appendix。

**3个 CRITICAL gap：**
1. **DocRED 官方 test set 缺失**——只有 Re-DocRED test，CodaLab 未提交
2. **SFT test baselines 全部缺失**——test 表无法计算 RSFT gain
3. **4B test checkpoint 不可恢复**——test 表缺 4B 行

**需要立即验证的：**
- LaTeX 编译（figures 路径是否对齐、页数是否 ≤8 页主文）
- 全文 grep 旧数字残留（"+7.5" / "-6.2" / "non-monotonic"）
- flat-NLI Ign-F1 和 14B RSFT 详细指标在附录表中仍为 "--"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 197389,
  "duration_api_ms": 197927,
  "num_turns": 34,
  "stop_reason": "end_turn",
  "session_id": "bed1265a-eda0-4176-8d29-820b595fe549",
  "total_cost_usd": 1.3145585,
  "usage": {
    "input_tokens": 17,
    "cache_creation_input_tokens": 99692,
    "cache_read_input_tokens": 962011,
    "output_tokens": 8340,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 99692,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 3,
        "output_tokens": 352,
        "cache_read_input_tokens": 110668,
        "cache_creation_input_tokens": 471,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 471
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1798,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001893,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 17,
      "outputTokens": 8340,
      "cacheReadInputTokens": 962011,
      "cacheCreationInputTokens": 99692,
      "webSearchRequests": 0,
      "costUSD": 1.3126655,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ad0bd586-cc16-4141-b2f8-d926c5da25f6"
}
```

</details>

---
