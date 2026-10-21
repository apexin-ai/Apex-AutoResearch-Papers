# review reviewer corrections audit

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 232
- **Recorded user turns:** 1
- **Tool calls:** 77
- **Original source:** `logs/workers/worker_review_reviewer_corrections_audit_20260527T131202.log`
- **Structured JSON:** [`e44cd6f70d689fe37603.json`](../../sessions/e4/e44cd6f70d689fe37603.json)

## Before a recorded user message

19 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
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
  "uuid": "a6ca0e0b-46bc-4d21-84b0-0a49b23c3302",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/memory/"
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
    "resetsAt": 1779890400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "5539b2db-b05f-496c-bfdb-8780e11e1191",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by examining the paper directory and artifacts to check each of the reviewer correction items.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "23ecdf0f-eea3-4b59-8965-4746e9c0b67b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018KAQ3yAwmaKaF1UmBPuBXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12498,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12498
      },
      "output_tokens": 22,
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

我来逐项审查 Reviewer 修正项的完成状态。先扫描论文文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "4cafe577-5d28-4f42-8716-6ae4baa7a58a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018KAQ3yAwmaKaF1UmBPuBXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12498,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12498
      },
      "output_tokens": 22,
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

<details open><summary>🔧 Tool call — Glob · `toolu_01WxVizb2VNuwjxkSZg9B5a3`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "4a00ae48-46b4-448c-bec9-6d49d56493e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018KAQ3yAwmaKaF1UmBPuBXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12498,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12498
      },
      "output_tokens": 22,
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

_source line 7 · 2026-05-27T13:12:13.703Z_

<details><summary>↩ Tool result · `toolu_01WxVizb2VNuwjxkSZg9B5a3`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "d96b7c99-9b67-4f76-a29c-698029da665a",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 12,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_01PAGTQWyprqTbtEkhXECtTY`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "3b598429-4ff7-43ec-b6bd-b03913f0bb21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018KAQ3yAwmaKaF1UmBPuBXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12498,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12498
      },
      "output_tokens": 22,
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

_source line 9 · 2026-05-27T13:12:14.491Z_

<details><summary>↩ Tool result · `toolu_01PAGTQWyprqTbtEkhXECtTY`</summary>

```text
paper/section5_5_method_boundaries.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "25ec2d7d-4c0c-4d8b-bf7c-a33bcbd3b734",
  "tool_use_result": {
    "filenames": [
      "paper/section5_5_method_boundaries.md"
    ],
    "durationMs": 10,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Glob · `toolu_01GbWRjL25uUnmQLQ9rmFrLs`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "b43530d7-53c7-47cb-9e48-d23fbb08d849",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018KAQ3yAwmaKaF1UmBPuBXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12498,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12498
      },
      "output_tokens": 22,
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

_source line 11 · 2026-05-27T13:12:15.042Z_

<details><summary>↩ Tool result · `toolu_01GbWRjL25uUnmQLQ9rmFrLs`</summary>

```text
artifacts/report_sdf_extraction.md
artifacts/report_safelibero.md
artifacts/report_vla_codebase.md
artifacts/kg3_gradient_toy_test.py
artifacts/report_kg3_gradient_test.md
artifacts/src/sdf_decoder.py
artifacts/src/sdf_gradient_refiner.py
artifacts/src/sdf_data.py
artifacts/src/train_colliforce.py
artifacts/src/__init__.py
artifacts/src/__pycache__/__init__.cpython-314.pyc
artifacts/src/__pycache__/sdf_decoder.cpython-314.pyc
artifacts/report_env_setup_kg1_kg2.md
artifacts/src/__pycache__/sdf_gradient_refiner.cpython-314.pyc
artifacts/src/__pycache__/sdf_data.cpython-314.pyc
artifacts/src/__pycache__/train_colliforce.cpython-314.pyc
artifacts/literature_review.md
artifacts/train_baseline.py
artifacts/report_baseline_prep.md
artifacts/report_openpi_deploy.md
artifacts/report_data_pipeline.md
artifacts/report_a1_integration.md
artifacts/comprehensive_fix_report.txt
artifacts/_project/report/baseline_weight_fix_report.md
artifacts/_project/report/urgent_fix_report_20260520.md
artifacts/train_a1_hook.py
artifacts/fix_a3.py
artifacts/fix_a1.py
artifacts/_project/report/training_progress_20260520_1020.md
artifacts/training_progress_20260520_1020.md
artifacts/_project/report/related_work_outline.md
artifacts/related_work_outline.md
artifacts/_project/paper/method_draft.md
artifacts/method_draft.md
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/method.tex
artifacts/drafts/method.tex
artifacts/_project/paper/related_work.tex
artifacts/drafts/experiments.tex
artifacts/drafts/abstract.tex
artifacts/drafts/conclusion.tex
artifacts/drafts/introduction.tex
artifacts/drafts/related_work.tex
artifacts/_project/report/a3_lora_fix_result.json
artifacts/a3_lora_fix_result.json
artifacts/worker_output.md
artifacts/worker_report_westd45947_status.md
artifacts/eval_safelibero.py
artifacts/report_eval_tsr_zero_fix.md
artifacts/report_action_scale_fix.md
artifacts/diagnose_eval_a3_v11_object.md
artifacts/eval_a3_v11_object/report/diagnose_eval_a3_v11_object.md
artifacts/analysis_m022_norm_stats_root_cause.md
artifacts/eval_a3_v11_object/report/analysis_m022_norm_stats_root_cause.md
artifacts/worker_output_diagnose_eval_baseline_fullft_spatial_v11.md
artifacts/_project/report/analysis_m026_m027_m028_gradient_refine_diagnosis.md
artifacts/analysis_m026_m027_m028_gradient_refine_diagnosis.md
artifacts/_project/report/pi05_a1_sdf_feasibility_report.md
artifacts/pi05_a1_sdf_feasibility_report.md
artifacts/eval_pi05_safelibero_object_v11/report/report_pi05_object_collision_analysis.md
artifacts/report_pi05_object_collision_analysis.md
artifacts/_project/report/pi05_collision_analysis_report.md
artifacts/pi05_collision_analysis_report.md
artifacts/eval_pi05_safelibero.py
artifacts/eval_readiness_westd35807.md
artifacts/eval_commands_d012.md
artifacts/__pycache__/analyze_d012_results.cpython-314.pyc
artifacts/analyze_d012_results.py
artifacts/_project/report/related_work_survey.md
artifacts/related_work_survey.md
artifacts/report_baseline_fix.md
artifacts/prep_spatial_a1.md
artifacts/research_openvla_libero.md
artifacts/openvla_eval_prep.md
artifacts/remaining_train_status.md
artifacts/eval_openvla_safelibero.py
artifacts/__pycache__/eval_openvla_safelibero.cpython-314.pyc
artifacts/emergency_cleanup_report.md
artifacts/disk_cleanup_report.md
artifacts/train_pi05_lora_baseline.py
artifacts/phase2_fix_report.md
artifacts/_project/report/step7k_overfit_check.md
artifacts/step7k_overfit_check.md
artifacts/_project/report/lambda0_phase2_ablation_design.md
artifacts/_project/report/task0_vs_task1_collapse_analysis.md
artifacts/_project/report/mid_eval_d012_step10k_results.md
artifacts/_project/report/eval_commands_d012_final.md
artifacts/_project/report/task3_car_degradation_analysis.md
artifacts/eval_commands_d012_final.md
artifacts/eval_collision_enhancement_plan.md
artifacts/_project/data/task3_collision_matrix_step10k.md
artifacts/task3_collision_matrix_step10k.md
artifacts/lora_baseline_launch_checklist.md
artifacts/_project/report/metric_definitions_e59531.md
artifacts/metric_definitions.md
artifacts/_project/report/metric_definitions.md
artifacts/_project/report/ssh_recovery_execution_plan.md
artifacts/train_a1_sdf_aux_pi05.py
artifacts/_project/report/paper_data_summary.md
artifacts/_project/paper/analysis_claim1.tex
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "0fe2fa97-6572-4e42-8adc-2a40ed512c0c",
  "tool_use_result": {
    "filenames": [
      "artifacts/report_sdf_extraction.md",
      "artifacts/report_safelibero.md",
      "artifacts/report_vla_codebase.md",
      "artifacts/kg3_gradient_toy_test.py",
      "artifacts/report_kg3_gradient_test.md",
      "artifacts/src/sdf_decoder.py",
      "artifacts/src/sdf_gradient_refiner.py",
      "artifacts/src/sdf_data.py",
      "artifacts/src/train_colliforce.py",
      "artifacts/src/__init__.py",
      "artifacts/src/__pycache__/__init__.cpython-314.pyc",
      "artifacts/src/__pycache__/sdf_decoder.cpython-314.pyc",
      "artifacts/report_env_setup_kg1_kg2.md",
      "artifacts/src/__pycache__/sdf_gradient_refiner.cpython-314.pyc",
      "artifacts/src/__pycache__/sdf_data.cpython-314.pyc",
      "artifacts/src/__pycache__/train_colliforce.cpython-314.pyc",
      "artifacts/literature_review.md",
      "artifacts/train_baseline.py",
      "artifacts/report_baseline_prep.md",
      "artifacts/report_openpi_deploy.md",
      "artifacts/report_data_pipeline.md",
      "artifacts/report_a1_integration.md",
      "artifacts/comprehensive_fix_report.txt",
      "artifacts/_project/report/baseline_weight_fix_report.md",
      "artifacts/_project/report/urgent_fix_report_20260520.md",
      "artifacts/train_a1_hook.py",
      "artifacts/fix_a3.py",
      "artifacts/fix_a1.py",
      "artifacts/_project/report/training_progress_20260520_1020.md",
      "artifacts/training_progress_20260520_1020.md",
      "artifacts/_project/report/related_work_outline.md",
      "artifacts/related_work_outline.md",
      "artifacts/_project/paper/method_draft.md",
      "artifacts/method_draft.md",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/method.tex",
      "artifacts/drafts/method.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/drafts/experiments.tex",
      "artifacts/drafts/abstract.tex",
      "artifacts/drafts/conclusion.tex",
      "artifacts/drafts/introduction.tex",
      "artifacts/drafts/related_work.tex",
      "artifacts/_project/report/a3_lora_fix_result.json",
      "artifacts/a3_lora_fix_result.json",
      "artifacts/worker_output.md",
      "artifacts/worker_report_westd45947_status.md",
      "artifacts/eval_safelibero.py",
      "artifacts/report_eval_tsr_zero_fix.md",
      "artifacts/report_action_scale_fix.md",
      "artifacts/diagnose_eval_a3_v11_object.md",
      "artifacts/eval_a3_v11_object/report/diagnose_eval_a3_v11_object.md",
      "artifacts/analysis_m022_norm_stats_root_cause.md",
      "artifacts/eval_a3_v11_object/report/analysis_m022_norm_stats_root_cause.md",
      "artifacts/worker_output_diagnose_eval_baseline_fullft_spatial_v11.md",
      "artifacts/_project/report/analysis_m026_m027_m028_gradient_refine_diagnosis.md",
      "artifacts/analysis_m026_m027_m028_gradient_refine_diagnosis.md",
      "artifacts/_project/report/pi05_a1_sdf_feasibility_report.md",
      "artifacts/pi05_a1_sdf_feasibility_report.md",
      "artifacts/eval_pi05_safelibero_object_v11/report/report_pi05_object_collision_analysis.md",
      "artifacts/report_pi05_object_collision_analysis.md",
      "artifacts/_project/report/pi05_collision_analysis_report.md",
      "artifacts/pi05_collision_analysis_report.md",
      "artifacts/eval_pi05_safelibero.py",
      "artifacts/eval_readiness_westd35807.md",
      "artifacts/eval_commands_d012.md",
      "artifacts/__pycache__/analyze_d012_results.cpython-314.pyc",
      "artifacts/analyze_d012_results.py",
      "artifacts/_project/report/related_work_survey.md",
      "artifacts/related_work_survey.md",
      "artifacts/report_baseline_fix.md",
      "artifacts/prep_spatial_a1.md",
      "artifacts/research_openvla_libero.md",
      "artifacts/openvla_eval_prep.md",
      "artifacts/remaining_train_status.md",
      "artifacts/eval_openvla_safelibero.py",
      "artifacts/__pycache__/eval_openvla_safelibero.cpython-314.pyc",
      "artifacts/emergency_cleanup_report.md",
      "artifacts/disk_cleanup_report.md",
      "artifacts/train_pi05_lora_baseline.py",
      "artifacts/phase2_fix_report.md",
      "artifacts/_project/report/step7k_overfit_check.md",
      "artifacts/step7k_overfit_check.md",
      "artifacts/_project/report/lambda0_phase2_ablation_design.md",
      "artifacts/_project/report/task0_vs_task1_collapse_analysis.md",
      "artifacts/_project/report/mid_eval_d012_step10k_results.md",
      "artifacts/_project/report/eval_commands_d012_final.md",
      "artifacts/_project/report/task3_car_degradation_analysis.md",
      "artifacts/eval_commands_d012_final.md",
      "artifacts/eval_collision_enhancement_plan.md",
      "artifacts/_project/data/task3_collision_matrix_step10k.md",
      "artifacts/task3_collision_matrix_step10k.md",
      "artifacts/lora_baseline_launch_checklist.md",
      "artifacts/_project/report/metric_definitions_e59531.md",
      "artifacts/metric_definitions.md",
      "artifacts/_project/report/metric_definitions.md",
      "artifacts/_project/report/ssh_recovery_execution_plan.md",
      "artifacts/train_a1_sdf_aux_pi05.py",
      "artifacts/_project/report/paper_data_summary.md",
      "artifacts/_project/paper/analysis_claim1.tex"
    ],
    "durationMs": 14,
    "numFiles": 100,
    "truncated": true
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Glob · `toolu_01QN4egaEvRvqA335nBHmLX1`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "3bbff58f-864d-46a4-b482-f180dd5d03b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W8ZAnkRTeyggz5HK15yJJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1892,
      "cache_read_input_tokens": 23949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1892
      },
      "output_tokens": 66,
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

_source line 13 · 2026-05-27T13:12:19.175Z_

<details><summary>↩ Tool result · `toolu_01QN4egaEvRvqA335nBHmLX1`</summary>

```text
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/method.tex
artifacts/drafts/method.tex
artifacts/_project/paper/related_work.tex
artifacts/drafts/experiments.tex
artifacts/drafts/abstract.tex
artifacts/drafts/conclusion.tex
artifacts/drafts/introduction.tex
artifacts/drafts/related_work.tex
artifacts/_project/paper/analysis_claim1.tex
artifacts/drafts/analysis_claim1.tex
artifacts/_project/paper/analysis_claim2.tex
artifacts/drafts/analysis_claim2.tex
artifacts/_project/paper/analysis_claim3.tex
artifacts/drafts/analysis_claim3.tex
artifacts/_project/paper/experimental_framework.tex
artifacts/drafts/experimental_framework.tex
artifacts/_project/paper/introduction_v2.tex
artifacts/_project/paper/abstract_v2.tex
artifacts/drafts/abstract_v2.tex
artifacts/drafts/introduction_v2.tex
artifacts/drafts/related_work_v2.tex
artifacts/_project/paper/related_work_v2.tex
artifacts/dream_reports/dream_20260525T223036/best/paper.tex
artifacts/dream_reports/dream_20260525T223036/median/paper.tex
artifacts/dream_reports/dream_20260525T223036/worst/paper.tex
artifacts/dream_reports/dream_20260526T023936/best/paper.tex
artifacts/dream_reports/dream_20260526T023936/median/paper.tex
artifacts/dream_reports/dream_20260526T023936/worst/paper.tex
artifacts/reeval_comparison.tex
artifacts/_project/paper/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "be178e77-4740-44cb-a23f-784e2c0ef752",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/method.tex",
      "artifacts/drafts/method.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/drafts/experiments.tex",
      "artifacts/drafts/abstract.tex",
      "artifacts/drafts/conclusion.tex",
      "artifacts/drafts/introduction.tex",
      "artifacts/drafts/related_work.tex",
      "artifacts/_project/paper/analysis_claim1.tex",
      "artifacts/drafts/analysis_claim1.tex",
      "artifacts/_project/paper/analysis_claim2.tex",
      "artifacts/drafts/analysis_claim2.tex",
      "artifacts/_project/paper/analysis_claim3.tex",
      "artifacts/drafts/analysis_claim3.tex",
      "artifacts/_project/paper/experimental_framework.tex",
      "artifacts/drafts/experimental_framework.tex",
      "artifacts/_project/paper/introduction_v2.tex",
      "artifacts/_project/paper/abstract_v2.tex",
      "artifacts/drafts/abstract_v2.tex",
      "artifacts/drafts/introduction_v2.tex",
      "artifacts/drafts/related_work_v2.tex",
      "artifacts/_project/paper/related_work_v2.tex",
      "artifacts/dream_reports/dream_20260525T223036/best/paper.tex",
      "artifacts/dream_reports/dream_20260525T223036/median/paper.tex",
      "artifacts/dream_reports/dream_20260525T223036/worst/paper.tex",
      "artifacts/dream_reports/dream_20260526T023936/best/paper.tex",
      "artifacts/dream_reports/dream_20260526T023936/median/paper.tex",
      "artifacts/dream_reports/dream_20260526T023936/worst/paper.tex",
      "artifacts/reeval_comparison.tex",
      "artifacts/_project/paper/discussion.tex"
    ],
    "durationMs": 8,
    "numFiles": 31,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Glob · `toolu_0156yRZtCW47jFdDv2wWi1Zk`</summary>

```json
{
  "pattern": "paper/**/*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "e46ca375-2ebc-4302-9830-7f3ae0694319",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W8ZAnkRTeyggz5HK15yJJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1892,
      "cache_read_input_tokens": 23949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1892
      },
      "output_tokens": 66,
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

_source line 15 · 2026-05-27T13:12:19.997Z_

<details><summary>↩ Tool result · `toolu_0156yRZtCW47jFdDv2wWi1Zk`</summary>

```text
paper/section5_5_method_boundaries.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "04556932-a508-42c6-85b4-a9dc9c2db1e0",
  "tool_use_result": {
    "filenames": [
      "paper/section5_5_method_boundaries.md"
    ],
    "durationMs": 21,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
The paper directory only has one md file. The actual paper tex files are in `artifacts/`. Let me search for the main paper files. The dream_reports likely contain full paper drafts. Let me also check for a compiled paper or main.tex. Let me look at the drafts directory and the _project/paper directory more systematically.

Let me search for per-task numbers, table data, and the specific values mentioned in the checklist across all tex files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "ea1cf6a4-51a5-4ced-aab5-6e3a20ca819b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FjENX62j352gD2BPB4SApt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 663,
      "cache_read_input_tokens": 25841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 663
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

_source line 17_

Let me search all tex files for the specific numbers mentioned in the checklist. I'll run multiple searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "d91d535e-61e8-478f-8327-a6ffd05007f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FjENX62j352gD2BPB4SApt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 663,
      "cache_read_input_tokens": 25841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 663
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

_source line 18_

<details open><summary>🔧 Tool call — Agent · `toolu_016PqJ6mRBZAbsXqCoBpSruV`</summary>

```json
{
  "description": "Audit reviewer corrections in paper",
  "prompt": "You are auditing a research paper for specific numerical corrections. The paper files are in:\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/drafts/` (main drafts)\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/` (project paper files)\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/dream_reports/` (dream report versions)\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper/` (paper directory)\n\nAlso check: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/reeval_comparison.tex`\n\nAnd check for any registry/data files:\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/report/paper_data_summary.md`\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/data/` directory\n\n## Checklist to verify\n\n### Item 1: s1 per-task numbers\nCheck if the paper references per-task numbers from eval_pi05_a1_30k_s1_l01_high:\n- Correct values: OJ CAR=66%, CP CAR=72%, milk CAR=70%, bbq CAR=26%\n- TSR: OJ=26%, CP=80%, milk=28%, bbq=62%\nSearch for these numbers or any per-task breakdown in all tex/md files. Note any incorrect values.\n\n### Item 2: LoRA Table row\nCheck all tables for the LoRA-only baseline row:\n- s0 reeval_v2: CAR=57%, TSR=46%, per-task OJ(68%), CP(74%), milk(66%), bbq(20%)\n- s1: CAR=52.5%\n- 2-seed mean: 54.75% ±3.18\nSearch for \"LoRA\", \"lora\", \"baseline\" in tables, and check if numbers match.\n\n### Item 3: EE Disp (End-Effector Displacement)\nCheck if paper mentions avg_max_ee_displacement:\n- s1 l01 high: avg_max_ee=0.3884, avg_max_obstacle=0.0553\nSearch for \"ee_disp\", \"displacement\", \"0.3884\", \"0.0553\" in all files.\n\n### Item 4: std consistency\nCheck reported std/SE values:\n- LoRA-only: mean=54.75%, std=3.18% (2 seeds: 57, 52.5)\n- λ=0.005: mean=54.5%, std=2.29% (3 seeds: 57, 54, 52.5)\n- λ=0.01: mean=56.33%, std=1.61% (3 seeds: 57, 57.5, 54.5)\n- λ=0.1: mean=58.25%, std=0.35% (2 seeds: 58, 58.5)\nSearch for \"±\", \"std\", \"3.18\", \"2.29\", \"1.61\", \"0.35\", \"54.75\", \"54.5\", \"56.33\", \"58.25\" in all files.\n\n## Instructions\n1. Read ALL tex files in the drafts/ and _project/paper/ directories\n2. Read the most recent dream_reports paper.tex files (the ones in dream_20260526T023936/)\n3. Read reeval_comparison.tex\n4. Read paper_data_summary.md and any data files in _project/data/\n5. Search for each number from the checklist\n6. For EACH of the 4 items, report:\n   - ✅ if correct values found in the paper\n   - ❌ if wrong values found, with: file path, line number, current wrong value, correct value\n   - ⚠️ if the item is not mentioned at all in the paper\n7. Be thorough - check ALL files, not just the first match\n\nReport your findings in detail with exact file paths and line numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "68274211-bca0-4105-bbc9-db9ed72d1099",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FjENX62j352gD2BPB4SApt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 663,
      "cache_read_input_tokens": 25841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 663
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

### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Audit reviewer corrections in paper",
  "task_type": "local_agent",
  "prompt": "You are auditing a research paper for specific numerical corrections. The paper files are in:\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/drafts/` (main drafts)\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/` (project paper files)\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/dream_reports/` (dream report versions)\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper/` (paper directory)\n\nAlso check: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/reeval_comparison.tex`\n\nAnd check for any registry/data files:\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/report/paper_data_summary.md`\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/data/` directory\n\n## Checklist to verify\n\n### Item 1: s1 per-task numbers\nCheck if the paper references per-task numbers from eval_pi05_a1_30k_s1_l01_high:\n- Correct values: OJ CAR=66%, CP CAR=72%, milk CAR=70%, bbq CAR=26%\n- TSR: OJ=26%, CP=80%, milk=28%, bbq=62%\nSearch for these numbers or any per-task breakdown in all tex/md files. Note any incorrect values.\n\n### Item 2: LoRA Table row\nCheck all tables for the LoRA-only baseline row:\n- s0 reeval_v2: CAR=57%, TSR=46%, per-task OJ(68%), CP(74%), milk(66%), bbq(20%)\n- s1: CAR=52.5%\n- 2-seed mean: 54.75% ±3.18\nSearch for \"LoRA\", \"lora\", \"baseline\" in tables, and check if numbers match.\n\n### Item 3: EE Disp (End-Effector Displacement)\nCheck if paper mentions avg_max_ee_displacement:\n- s1 l01 high: avg_max_ee=0.3884, avg_max_obstacle=0.0553\nSearch for \"ee_disp\", \"displacement\", \"0.3884\", \"0.0553\" in all files.\n\n### Item 4: std consistency\nCheck reported std/SE values:\n- LoRA-only: mean=54.75%, std=3.18% (2 seeds: 57, 52.5)\n- λ=0.005: mean=54.5%, std=2.29% (3 seeds: 57, 54, 52.5)\n- λ=0.01: mean=56.33%, std=1.61% (3 seeds: 57, 57.5, 54.5)\n- λ=0.1: mean=58.25%, std=0.35% (2 seeds: 58, 58.5)\nSearch for \"±\", \"std\", \"3.18\", \"2.29\", \"1.61\", \"0.35\", \"54.75\", \"54.5\", \"56.33\", \"58.25\" in all files.\n\n## Instructions\n1. Read ALL tex files in the drafts/ and _project/paper/ directories\n2. Read the most recent dream_reports paper.tex files (the ones in dream_20260526T023936/)\n3. Read reeval_comparison.tex\n4. Read paper_data_summary.md and any data files in _project/data/\n5. Search for each number from the checklist\n6. For EACH of the 4 items, report:\n   - ✅ if correct values found in the paper\n   - ❌ if wrong values found, with: file path, line number, current wrong value, correct value\n   - ⚠️ if the item is not mentioned at all in the paper\n7. Be thorough - check ALL files, not just the first match\n\nReport your findings in detail with exact file paths and line numbers.",
  "uuid": "13ff6720-321f-4306-8585-668b430faeee",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

## Round 1

213 recorded events

### User

_source line 20 · 2026-05-27T13:12:39.600Z_

You are auditing a research paper for specific numerical corrections. The paper files are in:
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/drafts/` (main drafts)
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/` (project paper files)
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/dream_reports/` (dream report versions)
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper/` (paper directory)

Also check: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/reeval_comparison.tex`

And check for any registry/data files:
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/report/paper_data_summary.md`
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/data/` directory

## Checklist to verify

### Item 1: s1 per-task numbers
Check if the paper references per-task numbers from eval_pi05_a1_30k_s1_l01_high:
- Correct values: OJ CAR=66%, CP CAR=72%, milk CAR=70%, bbq CAR=26%
- TSR: OJ=26%, CP=80%, milk=28%, bbq=62%
Search for these numbers or any per-task breakdown in all tex/md files. Note any incorrect values.

### Item 2: LoRA Table row
Check all tables for the LoRA-only baseline row:
- s0 reeval_v2: CAR=57%, TSR=46%, per-task OJ(68%), CP(74%), milk(66%), bbq(20%)
- s1: CAR=52.5%
- 2-seed mean: 54.75% ±3.18
Search for "LoRA", "lora", "baseline" in tables, and check if numbers match.

### Item 3: EE Disp (End-Effector Displacement)
Check if paper mentions avg_max_ee_displacement:
- s1 l01 high: avg_max_ee=0.3884, avg_max_obstacle=0.0553
Search for "ee_disp", "displacement", "0.3884", "0.0553" in all files.

### Item 4: std consistency
Check reported std/SE values:
- LoRA-only: mean=54.75%, std=3.18% (2 seeds: 57, 52.5)
- λ=0.005: mean=54.5%, std=2.29% (3 seeds: 57, 54, 52.5)
- λ=0.01: mean=56.33%, std=1.61% (3 seeds: 57, 57.5, 54.5)
- λ=0.1: mean=58.25%, std=0.35% (2 seeds: 58, 58.5)
Search for "±", "std", "3.18", "2.29", "1.61", "0.35", "54.75", "54.5", "56.33", "58.25" in all files.

## Instructions
1. Read ALL tex files in the drafts/ and _project/paper/ directories
2. Read the most recent dream_reports paper.tex files (the ones in dream_20260526T023936/)
3. Read reeval_comparison.tex
4. Read paper_data_summary.md and any data files in _project/data/
5. Search for each number from the checklist
6. For EACH of the 4 items, report:
   - ✅ if correct values found in the paper
   - ❌ if wrong values found, with: file path, line number, current wrong value, correct value
   - ⚠️ if the item is not mentioned at all in the paper
7. Be thorough - check ALL files, not just the first match

Report your findings in detail with exact file paths and line numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "69d6e850-6967-4ce8-b7ae-02d8a1cddd16"
}
```

</details>

---

### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Finding **/*.tex",
  "usage": {
    "total_tokens": 15226,
    "tool_uses": 1,
    "duration_ms": 5868
  },
  "last_tool_name": "Glob",
  "uuid": "bfe64e2d-bb59-46c7-ae84-99144aca2997",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Glob · `toolu_01RSvdUEFcZYNMPzA2k54QsD`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "bda94a65-16ca-4f8f-b5b2-3beeeeb4e82c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQSaFBifZtNeAcXRv1eECD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15209,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15209,
        "ephemeral_1h_input_tokens": 0
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

_source line 23 · 2026-05-27T13:12:45.490Z_

<details><summary>↩ Tool result · `toolu_01RSvdUEFcZYNMPzA2k54QsD`</summary>

```text
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/method.tex
artifacts/drafts/method.tex
artifacts/_project/paper/related_work.tex
artifacts/drafts/experiments.tex
artifacts/drafts/abstract.tex
artifacts/drafts/conclusion.tex
artifacts/drafts/introduction.tex
artifacts/drafts/related_work.tex
artifacts/_project/paper/analysis_claim1.tex
artifacts/drafts/analysis_claim1.tex
artifacts/_project/paper/analysis_claim2.tex
artifacts/drafts/analysis_claim2.tex
artifacts/_project/paper/analysis_claim3.tex
artifacts/drafts/analysis_claim3.tex
artifacts/_project/paper/experimental_framework.tex
artifacts/drafts/experimental_framework.tex
artifacts/_project/paper/introduction_v2.tex
artifacts/_project/paper/abstract_v2.tex
artifacts/drafts/abstract_v2.tex
artifacts/drafts/introduction_v2.tex
artifacts/drafts/related_work_v2.tex
artifacts/_project/paper/related_work_v2.tex
artifacts/dream_reports/dream_20260525T223036/best/paper.tex
artifacts/dream_reports/dream_20260525T223036/median/paper.tex
artifacts/dream_reports/dream_20260525T223036/worst/paper.tex
artifacts/dream_reports/dream_20260526T023936/best/paper.tex
artifacts/dream_reports/dream_20260526T023936/median/paper.tex
artifacts/dream_reports/dream_20260526T023936/worst/paper.tex
artifacts/reeval_comparison.tex
artifacts/_project/paper/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "b17c14f4-f387-4472-9c72-fab5688947f4"
}
```

</details>

---

### System

_source line 24_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Finding **/*.tex",
  "usage": {
    "total_tokens": 15233,
    "tool_uses": 2,
    "duration_ms": 6327
  },
  "last_tool_name": "Glob",
  "uuid": "ba2e460c-9f32-4ac7-bdab-287a3ee375a5",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Glob · `toolu_01Jp4e7fkjBrkKtTmoyPt3F2`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "f777b449-8436-4f57-ac69-71a161315b8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQSaFBifZtNeAcXRv1eECD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15209,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15209,
        "ephemeral_1h_input_tokens": 0
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

_source line 26 · 2026-05-27T13:12:45.939Z_

<details><summary>↩ Tool result · `toolu_01Jp4e7fkjBrkKtTmoyPt3F2`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "e8e56dda-bb94-4147-9260-2177b98551f2"
}
```

</details>

---

### System

_source line 27_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Finding **/*.md",
  "usage": {
    "total_tokens": 15240,
    "tool_uses": 3,
    "duration_ms": 7330
  },
  "last_tool_name": "Glob",
  "uuid": "224d94cd-b0ad-42f2-a6d3-9c2c94b63a66",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Glob · `toolu_012rhKhym91DhnLz1dfCFodM`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "7c38726e-baa1-4759-b6d3-768b0eaa7cd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQSaFBifZtNeAcXRv1eECD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15209,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15209,
        "ephemeral_1h_input_tokens": 0
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

_source line 29 · 2026-05-27T13:12:46.943Z_

<details><summary>↩ Tool result · `toolu_012rhKhym91DhnLz1dfCFodM`</summary>

```text
artifacts/_project/report/baseline_weight_fix_report.md
artifacts/_project/report/urgent_fix_report_20260520.md
artifacts/_project/report/training_progress_20260520_1020.md
artifacts/_project/report/related_work_outline.md
artifacts/_project/paper/method_draft.md
artifacts/_project/report/analysis_m026_m027_m028_gradient_refine_diagnosis.md
artifacts/_project/report/pi05_a1_sdf_feasibility_report.md
artifacts/_project/report/pi05_collision_analysis_report.md
artifacts/_project/report/related_work_survey.md
artifacts/_project/report/step7k_overfit_check.md
artifacts/_project/report/lambda0_phase2_ablation_design.md
artifacts/_project/report/task0_vs_task1_collapse_analysis.md
artifacts/_project/report/mid_eval_d012_step10k_results.md
artifacts/_project/report/eval_commands_d012_final.md
artifacts/_project/report/task3_car_degradation_analysis.md
artifacts/_project/data/task3_collision_matrix_step10k.md
artifacts/_project/report/metric_definitions_e59531.md
artifacts/_project/report/metric_definitions.md
artifacts/_project/report/ssh_recovery_execution_plan.md
artifacts/_project/report/paper_data_summary.md
artifacts/_project/report/negative_results_analysis.md
artifacts/_project/paper/section5_5_method_boundaries.md
artifacts/_project/report/claim2_coverage_audit.md
artifacts/_project/report/related_work_update_20260525.md
artifacts/_project/report/report_pi0_baseline_fake_rate.md
artifacts/_project/report/negative_results_classification.md
artifacts/_project/data/paper_data_summary.md
artifacts/_project/report/tsr_collapse_analysis_report.md
artifacts/_project/chart/tsr_collapse_figures_index.md
artifacts/_project/paper/abc_scenario_patches.md
artifacts/_project/data/claim3_data_summary.md
artifacts/_project/intermediate/fig1_teaser_design.md
artifacts/_project/report/figure1_teaser_design.md
artifacts/_project/data/ssr_analysis.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "28a20d72-5df7-4212-ae01-7f33fff09298"
}
```

</details>

---

### System

_source line 30_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Finding **/*",
  "usage": {
    "total_tokens": 15247,
    "tool_uses": 4,
    "duration_ms": 7640
  },
  "last_tool_name": "Glob",
  "uuid": "9da0936f-9bd6-45ff-b01a-613e89483c73",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Glob · `toolu_01UNZC8hZdM3yoHf6k3Ns1N6`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "e6136dcd-1aab-4c85-afdd-4a726a2d0b64",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQSaFBifZtNeAcXRv1eECD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15209,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15209,
        "ephemeral_1h_input_tokens": 0
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

_source line 32 · 2026-05-27T13:12:47.257Z_

<details><summary>↩ Tool result · `toolu_01UNZC8hZdM3yoHf6k3Ns1N6`</summary>

```text
artifacts/_project/data/task3_collision_matrix_step10k.md
artifacts/_project/data/eval_safelibero_openvla.py
artifacts/_project/data/displacement_analysis_30k_summary.txt
artifacts/_project/data/paper_data_summary.md
artifacts/_project/data/threshold_sensitivity.csv
artifacts/_project/data/claim3_data_summary.md
artifacts/_project/data/ssr_analysis.md
artifacts/_project/data/fig5_lambda_data.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "af86117f-0476-4705-86be-80d2d4764f8f"
}
```

</details>

---

### System

_source line 33_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/reeval_comparison.tex",
  "usage": {
    "total_tokens": 17675,
    "tool_uses": 5,
    "duration_ms": 10996
  },
  "last_tool_name": "Read",
  "uuid": "6c66cee0-7122-451e-a091-36d3187d503f",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01WALQzP85SuwLyE6iG34RqD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/reeval_comparison.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "3eae246d-1add-4e09-ba3d-47f3f21ee166",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GU1R5B7ZmYh1QrXumrVdi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2428,
      "cache_read_input_tokens": 15209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2428,
        "ephemeral_1h_input_tokens": 0
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

_source line 35 · 2026-05-27T13:12:50.611Z_

<details><summary>↩ Tool result · `toolu_01WALQzP85SuwLyE6iG34RqD`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\caption{Evaluation results before and after fixing the 180° image rotation bug in \texttt{eval\_safelibero.py}.}
4	\label{tab:reeval_comparison}
5	\resizebox{\textwidth}{!}{
6	\begin{tabular}{l c c c c c c c}
7	\toprule
8	Model & \multicolumn{2}{c}{TSR (\%)} & $\Delta$TSR & \multicolumn{2}{c}{CAR (\%)} & $\Delta$CAR & EE Disp (m) \\
9	\cmidrule(lr){2-3} \cmidrule(lr){5-6}
10	 & Before & After & (pp) & Before & After & (pp) & (After) \\
11	\midrule
12	Pi0.5 baseline s0 & 74.7 & 71.5 & -3.2 & 26.8 & 28.5 & +1.7 & 0.367 \\
13	\addlinespace
14	LoRA-only s0 & 6.5 & 51.5 & +45.0 & 54.5 & 56.5 & +2.0 & 0.396 \\
15	LoRA-only s1 & 6.0 & — & — & 56.0 & — & — & — \\
16	\rowcolor{gray!15} \textit{LoRA-only mean} & 6.2$\pm$0.2 & 51.5$\pm$0.0 & +45.2 & 55.2$\pm$0.8 & 56.5$\pm$0.0 & +1.2 & \\
17	\addlinespace
18	SDF $\lambda$=0.005 s0 & 4.5 & — & — & 53.5 & — & — & — \\
19	SDF $\lambda$=0.005 s1 & 9.0 & — & — & 50.0 & — & — & — \\
20	SDF $\lambda$=0.005 s2 & 7.0 & — & — & 48.0 & — & — & — \\
21	\rowcolor{gray!15} \textit{SDF $\lambda$=0.005 mean} & 6.8$\pm$1.8 & — & — & 50.5$\pm$2.3 & — & — & \\
22	\addlinespace
23	SDF $\lambda$=0.01 s0 & 8.0 & — & — & 50.0 & — & — & — \\
24	SDF $\lambda$=0.01 s1 & 5.5 & — & — & 55.0 & — & — & — \\
25	SDF $\lambda$=0.01 s2 & 5.0 & — & — & 54.0 & — & — & — \\
26	\rowcolor{gray!15} \textit{SDF $\lambda$=0.01 mean} & 6.2$\pm$1.3 & — & — & 53.0$\pm$2.2 & — & — & \\
27	\bottomrule
28	\end{tabular}}
29	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "57399d43-f7c4-4689-92b8-75ffaa219810"
}
```

</details>

---

### System

_source line 36_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/_project/report/paper_data_summary.md",
  "usage": {
    "total_tokens": 17676,
    "tool_uses": 6,
    "duration_ms": 11454
  },
  "last_tool_name": "Read",
  "uuid": "688dd74c-4815-43ea-9d3e-fe1ad0fff059",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_0125fNb8kVrkizUVumSUuAZh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/report/paper_data_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "317f214e-812e-4f91-929e-df2e3962be15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GU1R5B7ZmYh1QrXumrVdi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2428,
      "cache_read_input_tokens": 15209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2428,
        "ephemeral_1h_input_tokens": 0
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

_source line 38 · 2026-05-27T13:12:51.061Z_

<details><summary>↩ Tool result · `toolu_0125fNb8kVrkizUVumSUuAZh`</summary>

````text
1	# Paper Data Summary — diff_collision_sdf
2	
3	Generated: 2026-05-24 | Source: experiment registry (51 entries)
4	
5	---
6	
7	## Table 1: Pi0.5 + A1 — 3-seed × 2-lambda 结果矩阵
8	
9	10K mid-eval 数据来源：ROADMAP D016（手动 eval）
10	
11	| | λ=0.005 TSR | λ=0.005 CAR | λ=0.005 SSR | λ=0.01 TSR | λ=0.01 CAR | λ=0.01 SSR |
12	|---|---|---|---|---|---|---|
13	| seed 0 (10K) | 47% | 58% | 0% frozen | 49% | 56.5% | 0% frozen |
14	| seed 1 (30K) | TBD | TBD | TBD | TBD | TBD | TBD |
15	| seed 2 (30K) | TBD | TBD | TBD | TBD | TBD | TBD |
16	| **mean±std** | — | — | — | — | — | — |
17	
18	**对比基线：**
19	- Pi0.5 baseline 3-seed: TSR = 74.7 ± 1.5%, CAR = 26.8 ± 1.6% (n=600, seeds 7/1/2)
20	- Pi0.5 baseline per-seed: s0(seed7): TSR=73%, CAR=28% | s1: TSR=76%, CAR=25% | s2: TSR=75%, CAR=27.5%
21	
22	**分析：**
23	- A1 training 显著降低了 TSR（74.7% → 47-49%），但大幅提升了 CAR（26.8% → 56-58%）
24	- SSR=0% frozen 表明 A1 不产生 action collapse（与 Pi0 系方法的 99%+ fake safe 形成对比）
25	- seed 1/2 训练完成（30K steps）但因 SSH auth failure 未获取 eval metrics，需补跑 eval
26	
27	---
28	
29	## Table 2 (Claim 1): Fake Safety 统计
30	
31	**核心论点：** 现有碰撞避免方法的高 CAR 是 "fake safety"——模型通过 action collapse（停止运动）而非真正的轨迹修正来避免碰撞。
32	
33	| Method | Episodes | TSR | CAR | Real Safe Rate | Fake Safe Rate | Source |
34	|--------|----------|-----|-----|---------------|---------------|--------|
35	| A1-LoRA (Pi0) | 800 | 0% | 91.5% | 0.4% (3/732) | 99.6% (729/732) | eval_a1_lora_object_v11_rerun |
36	| LoRA baseline (Pi0) | 200 | 0% | 82% | 0.5% (~1/164) | 99.4% (~163/164) | eval_lora_baseline_object_v11 |
37	| Full-FT baseline (Pi0) | 200 | 0.5% | 83% | 需补充 | 需补充 | eval_baseline_v11_object |
38	| Pi0.5 baseline (3-seed) | 600 | 74.7% | 26.8% | 0.5% (1/200 in s0) | 98.2% (s0) | eval_pi05_safelibero_object_v11 + s1 + s2 |
39	| **Pi0.5 + A1 (10K, s0, λ=0.005)** | — | 47% | 58% | ~100% (0% frozen) | ~0% | ROADMAP D016 |
40	| **Pi0.5 + A1 (10K, s0, λ=0.01)** | — | 49% | 56.5% | ~100% (0% frozen) | ~0% | ROADMAP D016 |
41	
42	**Fake Safe 判定标准：** safe episode 中 displacement < 0.1mm（即 arm 几乎完全静止）
43	
44	**A1-LoRA 详细位移分布（800 eps, 732 safe）：**
45	- < 1µm: 541 episodes (73.9%)
46	- 1µm – 0.1mm: 188 episodes (25.7%)
47	- 0.1mm – 1mm: 3 episodes (0.4%) ← real safe
48	- \> 1mm: 0 episodes
49	
50	**关键结论：** Pi0 系方法 CAR 82-91.5% 看似优秀，但 99%+ 的 "safe" episodes 是因为机械臂完全停止运动（displacement < 0.1mm），而非学会了绕开障碍物。Pi0.5+A1 虽然 CAR 较低（56-58%），但 0% frozen 意味着所有安全行为都是真实的碰撞避免。
51	
52	---
53	
54	## Table 3 (Claim 3): Oracle Comparison — Runtime Refinement 无效
55	
56	**核心论点：** 即使使用 ground-truth SDF 做 runtime gradient refinement，也无法解决 fake safety 问题，证明 inference-time 优化路线不可行。
57	
58	| Method | TSR | CAR | Fake Safe Rate | Refine Count/ep | Source |
59	|--------|-----|-----|---------------|----------------|--------|
60	| Oracle-adaptive (GT SDF) | 0% | 75.0% | 98.3% (118/120) | 14.2 | oracle_true_gt_adaptive_alpha_v11 |
61	| Oracle-fixed α=0.005 (GT SDF) | 0% | 73.1% | 98.3% (115/117) | 14.8 | oracle_true_gt_fixed_alpha_v11 |
62	| Oracle-feature (GT SDF) | 0% | 76.9% | 96.7% (119/123) | 241.7 | oracle_true_gt_feature_v11 |
63	| A3 no-force (learned SDF) | 0% | 74.5% | — | 0 (never triggered) | eval_a3_v11_object |
64	| LoRA baseline (no refine) | 0% | 82% | 99.4% | N/A | eval_lora_baseline_object_v11 |
65	| Full-FT baseline (no refine) | 0.5% | 83% | 需补充 | N/A | eval_baseline_v11_object |
66	
67	**Oracle 实验参数：**
68	- n=160 episodes (4 tasks × 40 eps), seed 0
69	- GT SDF = 真实场景的 signed distance field
70	- Adaptive: 动态调整 refinement strength
71	- Fixed: α=0.005 固定步长
72	- Feature-space: 在 feature 层面做梯度修正（每步都 refine，avg 241.7/ep）
73	
74	**关键结论：**
75	1. Oracle refinement（GT SDF）vs 无 refine 的 LoRA baseline：CAR 反而**更低**（73-77% vs 82%），说明 refinement 在破坏策略
76	2. 所有 Oracle 方法 fake_safe_rate 仍高达 96-98%，GT SDF 都救不了
77	3. A3（learned SDF）的 refine 从未被触发（SDF 预测值未达阈值），实际退化为 baseline
78	4. Feature-space oracle 每步都 refine（241.7/ep vs action-space 14.2/ep），梯度幅度极小（0.004-0.006 vs action-space 0.18-0.49），但结果无显著差异
79	
80	---
81	
82	## Table 4: TSR-CAR Scatter 数据点（Fig 3 素材）
83	
84	用于绘制 TSR vs CAR 散点图，展示各方法在 task success 和 collision avoidance 两个维度上的 trade-off。
85	
86	```
87	method_name, TSR, CAR, n_episodes, marker_style_suggestion
88	# --- Pi0.5 系列 (高 TSR, 低-中 CAR) ---
89	Pi0.5 baseline s0 (seed 7), 0.73, 0.28, 200, blue_circle
90	Pi0.5 baseline s1, 0.76, 0.25, 200, blue_circle
91	Pi0.5 baseline s2, 0.75, 0.275, 200, blue_circle
92	Pi0.5+A1 λ=0.005 (10K s0), 0.47, 0.58, -, red_star
93	Pi0.5+A1 λ=0.01 (10K s0), 0.49, 0.565, -, red_star
94	# --- Pi0 系列 (低 TSR, 高 CAR — fake safety) ---
95	Pi0 LoRA baseline, 0.0, 0.82, 200, gray_triangle
96	Pi0 Full-FT baseline, 0.005, 0.83, 200, gray_triangle
97	A1-LoRA (Pi0), 0.0, 0.915, 800, orange_diamond
98	# --- Oracle 系列 (低 TSR, 中-高 CAR — GT SDF 也无效) ---
99	Oracle adaptive (GT SDF), 0.0, 0.75, 160, green_square_hollow
100	Oracle fixed α=0.005 (GT SDF), 0.0, 0.731, 160, green_square_hollow
101	Oracle feature-space (GT SDF), 0.0, 0.769, 160, green_square_hollow
102	# --- A3 Gradient Refine ---
103	A3 no-force (learned SDF), 0.0, 0.745, 200, purple_pentagon
104	A3 M024fix, 0.0, 0.771, 200, purple_pentagon_hollow
105	# --- Spatial 系列 ---
106	Pi0.5 spatial (seed 7), 0.575, 0.13, 200, blue_circle_hollow
107	A1-LoRA spatial, 0.001, 0.008, 200, orange_diamond_hollow
108	LoRA baseline spatial, 0.0, 0.0, 200, gray_triangle_hollow
109	Full-FT baseline spatial, 0.00375, 0.0, 800, gray_triangle_hollow
110	```
111	
112	**Fig 3 设计建议：**
113	- X 轴: TSR (Task Success Rate), Y 轴: CAR (Collision Avoidance Rate)
114	- 理想区域 = 右上角（高 TSR + 高 CAR）
115	- Pi0 系聚集在左上（高 CAR 但 0 TSR — 全是 fake safety）
116	- Pi0.5 baseline 在右下（高 TSR 但低 CAR）
117	- **Pi0.5+A1 是唯一向右上移动的方法**（中等 TSR + 中等 CAR，且 0% frozen）
118	- 可用虚线标注 "Pareto front"
119	- 用不同填充/颜色区分 fake safe (空心) vs real safe (实心) 方法
120	
121	---
122	
123	## 补充数据：Per-task CAR 分解
124	
125	| Method | task0 (orange_juice) | task1 (choc_pudding) | task2 (milk) | task3 (bbq_sauce) |
126	|--------|---------------------|---------------------|-------------|-------------------|
127	| Full-FT baseline | 76% | 90% | 88% | 78% |
128	| LoRA baseline | 96% | 46% | 98% | 88% |
129	| A1-LoRA (800ep) | 96% | 82% | 97% | 91% |
130	| A3 no-force | 84% | 48% | 82% | 84% |
131	| Oracle adaptive | 82.5% | 55% | 77.5% | 85% |
132	| Oracle fixed | 85% | 50% | 77.5% | 80% |
133	| Oracle feature | 90% | 47.5% | 82.5% | 87.5% |
134	
135	**观察：** task1 (chocolate_pudding) 是所有方法的难点，CAR 普遍最低。可能该任务的碰撞场景更 challenging。
136	
137	---
138	
139	## 待补充项
140	
141	1. **seed 1/2 的 30K eval 结果** — 训练完成但 SSH failure 未跑 eval，需重连服务器执行
142	2. **Full-FT baseline 的 fake_safe_rate** — registry 中无该字段，需补跑位移分析
143	3. **Pi0.5+A1 10K eval 的详细位移分布** — 证实 0% frozen 的 displacement 分布
144	4. **Pi0.5 baseline s1/s2 的 fake_safe_rate** — 仅 s0 有数据 (98.2%)
145	5. **Pi0.5+A1 30K eval** — s0 已训练 30K，需对比 10K vs 30K 的 TSR/CAR 变化
146	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "a7e91cc7-e257-4cfb-8cac-e27ab6f7115f"
}
```

</details>

---

### System

_source line 39_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/_project/data/paper_data_summary.md",
  "usage": {
    "total_tokens": 17677,
    "tool_uses": 7,
    "duration_ms": 11926
  },
  "last_tool_name": "Read",
  "uuid": "589893c6-29a3-4a07-b4c7-34bbcac53adb",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01TfiBteG99U1kZnJKKh277C`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/data/paper_data_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "01537b9a-8a84-42d1-9449-8a33961badf0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GU1R5B7ZmYh1QrXumrVdi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2428,
      "cache_read_input_tokens": 15209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2428,
        "ephemeral_1h_input_tokens": 0
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

_source line 41 · 2026-05-27T13:12:51.533Z_

<details><summary>↩ Tool result · `toolu_01TfiBteG99U1kZnJKKh277C`</summary>

```text
1	# Paper Data Summary — diff_collision_sdf
2	
3	> 生成时间: 2026-05-26
4	> 数据来源: registry (status=DONE, conclusion=success/negative 中已确认的指标)
5	> 标记说明: ✅ 已确认 | ⏳ 待收集 | 🔧 displacement-fixed eval
6	
7	---
8	
9	## Table 1: Pi0.5+A1 SDF 训练结果矩阵
10	
11	所有实验 n_episodes=200。
12	
13	### λ=0.005
14	
15	| Seed | Ckpt | Step | avg_TSR | avg_CAR | avg_ee_disp | fake_safe% | frozen | exp_id | 备注 |
16	|------|------|------|---------|---------|-------------|------------|--------|--------|------|
17	| 0 | 30K | 30K | 5.5 | 50.0 | 0.0433¹ | — | — | eval_pi05_a1_30k_s0_l005 | ✅ 旧脚本,obstacle disp |
18	| 0 | 30K | 30K | 7.5 | 47.0 | 0.0485¹ | — | — | eval_pi05_a1_30k_s0_l005_r4 | ✅ retry,旧脚本 |
19	| 0 | best | — | — | — | — | — | — | — | ⏳ seed0 无 best/ ckpt (训练未保存) |
20	| 1 | 30K | 30K | 4.0 | 54.0 | 0.4955 | **0%** | **No** | eval_pi05_a1_30k_s1_l005_disp | ✅🔧 displacement-fixed |
21	| 1 | 30K | 30K | 5.5 | 52.5 | — | — | — | eval_pi05_a1_30k_s1_l005_v2 | ✅ 无 disp 数据 |
22	| 1 | 30K | 30K | 4.0 | 51.5 | — | — | — | eval_pi05_a1_30k_s1_l005_v3 | ✅ v4 rerun |
23	| 1 | best | 16K | 6.5 | 53.0 | 0.37~0.65² | **0%** | **No** | eval_pi05_a1_best_s1_l005_16k | ✅🔧 has ee_disp |
24	| 2 | 30K | 30K | 9.5 | 54.5 | — | — | — | eval_pi05_a1_30k_s2_l005_v2 | ✅ |
25	| 2 | 30K | 30K | 9.0 | 53.0 | — | — | — | eval_pi05_a1_30k_s2_l005_v3 | ✅ v4 rerun |
26	| 2 | best | 10K | 9.0 | 55.5 | 0.5046 | **0%** | **No** | eval_pi05_a1_best_s2_l005_10k | ✅🔧 displacement-fixed |
27	
28	¹ obstacle displacement (旧脚本), 非 ee_displacement
29	² per-task ee_disp: task0=0.5179, task1=0.5146, task2=0.6475, task3=0.3707
30	
31	### λ=0.01
32	
33	| Seed | Ckpt | Step | avg_TSR | avg_CAR | avg_ee_disp | fake_safe% | frozen | exp_id | 备注 |
34	|------|------|------|---------|---------|-------------|------------|--------|--------|------|
35	| 0 | 30K | 30K | 5.5 | 53.0 | 0.0297¹ | — | — | eval_pi05_a1_30k_s0_l01 | ✅ 旧脚本,obstacle disp |
36	| 0 | 30K | 30K | 6.5 | 52.5 | 0.4725 | **0%** | **No** | eval_pi05_a1_30k_s0_l01_disp | ✅🔧 displacement-fixed |
37	| 0 | best | — | — | — | — | — | — | — | ⏳ seed0 无 best/ ckpt |
38	| 1 | 30K | 30K | 7.5 | 52.5 | — | — | — | eval_pi05_a1_30k_s1_l01_v2 | ✅ |
39	| 1 | best | — | — | — | — | — | — | — | ⏳ 待 eval |
40	| 2 | 30K | 30K | 7.5 | 53.0 | — | — | — | eval_pi05_a1_30k_s2_l01_v2 | ✅ v3 rerun |
41	| 2 | best | — | — | — | — | — | — | — | ⏳ 待 eval |
42	
43	### 汇总统计 (displacement-fixed 数据)
44	
45	| 配置 | avg_CAR | avg_TSR | avg_ee_disp | fake_safe% |
46	|------|---------|---------|-------------|------------|
47	| λ=0.005, best (seed1+seed2) | 54.25 | 7.75 | 0.500 | 0% |
48	| λ=0.005, 30K (seed1 disp) | 54.0 | 4.0 | 0.496 | 0% |
49	| λ=0.01, 30K (seed0 disp) | 52.5 | 6.5 | 0.473 | 0% |
50	
51	---
52	
53	## Claim 1 证据: A1 Baseline (Pi0 Full-FT) 的 Fake Safety
54	
55	> 来源: eval_a1_lora_object_v11_rerun (800 episodes, DONE, conclusion=negative)
56	
57	| 指标 | 值 | 备注 |
58	|------|----|------|
59	| n_episodes | 800 | ✅ |
60	| avg_TSR | 0% | ✅ |
61	| avg_CAR | 91.5% | ✅ |
62	| fake_safe_rate | **99.6%** (729/732 safe eps, disp<0.1mm) | ✅ |
63	| real_safe_count | 3 | ✅ |
64	| collision_episodes | 68 | ✅ |
65	| collision_disp_mean_mm | 45.92 | ✅ |
66	
67	Per-task fake safe breakdown:
68	| Task | fake_safe | 比例 |
69	|------|-----------|------|
70	| orange_juice | 192/192 | 100% |
71	| chocolate_pudding | 162/164 | 98.8% |
72	| milk | 194/194 | 100% |
73	| bbq_sauce | 181/182 | 99.5% |
74	
75	**注意**: displacement 指 obstacle displacement（物体位移），非 ee_displacement。safe_disp_mean 极低(0.0003~0.008mm)证明机器人近乎完全冻结。
76	
77	### Baseline (Full-FT, 无 SDF) 对比
78	
79	来源: eval_baseline_v11_object (200 eps, DONE, conclusion=negative)
80	
81	| 指标 | 值 |
82	|------|----|
83	| TSR | 0.5% |
84	| CAR | 83% |
85	| displacement_avg | 0.0271m |
86	| fake_safe_rate | 99.4% (165/166) |
87	
88	**结论**: A1 (SDF aux + LoRA) CAR 91.5% 看似高于 baseline 83%，但 99.6% 为 fake safety（机器人冻结）。
89	
90	---
91	
92	## Claim 2 证据: Pi0.5 LoRA Baseline (无 SDF Loss)
93	
94	### Object task
95	
96	来源: eval_lora_baseline_object_v11 (200 eps, DONE, conclusion=negative)
97	
98	| 指标 | 值 | exp_id |
99	|------|----|--------|
100	| TSR | 0% | eval_lora_baseline_object_v11 | ✅ |
101	| CAR | 82% | eval_lora_baseline_object_v11 | ✅ |
102	| displacement_avg | 0.01m | eval_lora_baseline_object_v11 | ✅ |
103	| task2_disp | 0.00001m (frozen) | eval_lora_baseline_object_v11 | ✅ |
104	
105	### Spatial task
106	
107	来源: eval_lora_baseline_spatial_v11 (200 eps, DONE, conclusion=negative)
108	
109	| 指标 | 值 | exp_id |
110	|------|----|--------|
111	| TSR | 0% | eval_lora_baseline_spatial_v11 | ✅ |
112	| CAR | 0% | eval_lora_baseline_spatial_v11 | ✅ |
113	| displacement_avg | 0.23m | eval_lora_baseline_spatial_v11 | ✅ |
114	
115	### Pi0.5 原始 baseline (3-seed)
116	
117	| Seed | TSR | CAR | disp | exp_id |
118	|------|-----|-----|------|--------|
119	| 0 | 73% | 28% | — | eval_pi05_safelibero_object_v11 | ✅ (conclusion=negative) |
120	| 1 | 76% | 25% | 0.153 | eval_pi05_safelibero_object_v11_s1 | ✅ |
121	| 2 | 75% | 27.5% | 0.132 | eval_pi05_safelibero_object_v11_s2 | ✅ |
122	| **avg** | **74.7±1.5%** | **26.8±1.6%** | — | 3-seed aggregate | ✅ |
123	
124	⏳ **待收集**: Pi0.5 + LoRA (无 SDF) 的 displacement-fixed eval（确认 fake safety 比例）
125	
126	---
127	
128	## Claim 3 证据: Oracle Variants
129	
130	所有 oracle 实验均 conclusion=negative，证明 gradient-based runtime refinement 方向失败。
131	
132	| 变体 | CAR | fake_safe% | avg_refined/ep | exp_id | 备注 |
133	|------|-----|------------|----------------|--------|------|
134	| A3 force refine | 81.2% | ~85.6%¹ | 300 | oracle_a3_force_refine_object_v11 | ✅ M027: 实际用 learned decoder 非 GT |
135	| A3 M024 fix | 85.6% | 85.6% | 300 | oracle_a3_m024fix_object_v11 | ✅ 23/23 moving eps = 100% collision |
136	| True GT adaptive α | 75.0% | **98.3%** | 14.2 | oracle_true_gt_adaptive_alpha_v11 | ✅ GT SDF 比 baseline 更差 |
137	| True GT fixed α=0.005 | 73.1% | **98.3%** | 14.8 | oracle_true_gt_fixed_alpha_v11 | ✅ α 大小无关紧要 |
138	| GT feature-space | 76.9% | **96.7%** | 241.7 | oracle_true_gt_feature_v11 | ✅ feature-space 也不行 |
139	| Baseline (无 refinement) | 83% | 99.4% | 0 | eval_baseline_v11_object | ✅ 对照组 |
140	
141	¹ oracle_a3_force_refine 未直接报告 fake_safe%，从 displacement 数据推断
142	
143	**关键结论**: 即使使用 ground-truth SDF，gradient-based action refinement 也无法产生真正的避障行为（96-98% fake safety）。Feature-space 不优于 action-space。这验证了 A1 (training-time integration) 路线的必要性。
144	
145	---
146	
147	## Over-Avoidance 发现 (30K vs Best Checkpoint)
148	
149	> 核心问题: 30K checkpoint 的 CAR 升高是因为 over-avoidance（真正避障但过度保守）还是 frozen（假安全）？
150	
151	### Displacement-fixed 对比
152	
153	| 配置 | Step | CAR | TSR | avg_ee_disp | fake_safe% | exp_id |
154	|------|------|-----|-----|-------------|------------|--------|
155	| seed1, λ=0.005 | **30K** | 54.0 | 4.0 | 0.4955 | 0% | eval_pi05_a1_30k_s1_l005_disp | ✅🔧 |
156	| seed1, λ=0.005 | **16K best** | 53.0 | 6.5 | 0.37~0.65 | 0% | eval_pi05_a1_best_s1_l005_16k | ✅🔧 |
157	| seed0, λ=0.01 | **30K** | 52.5 | 6.5 | 0.4725 | 0% | eval_pi05_a1_30k_s0_l01_disp | ✅🔧 |
158	| seed2, λ=0.005 | **10K best** | 55.5 | 9.0 | 0.5046 | 0% | eval_pi05_a1_best_s2_l005_10k | ✅🔧 |
159	
160	### Per-task displacement (30K seed1 λ=0.005)
161	
162	| Task | ee_disp | safe_ee_disp | CAR |
163	|------|---------|--------------|-----|
164	| orange_juice (task0) | 0.5062 | 0.4247 | 54% |
165	| chocolate_pudding (task1) | 0.4991 | 0.5006 | 58% |
166	| milk (task2) | 0.6088 | 0.6213 | 92% |
167	| bbq_sauce (task3) | 0.3680 | 0.3628 | 12% |
168	
169	### Per-task displacement (30K seed0 λ=0.01)
170	
171	| Task | ee_disp | safe_ee_disp | CAR |
172	|------|---------|--------------|-----|
173	| orange_juice (task0) | 0.4781 | 0.4627 | 76% |
174	| chocolate_pudding (task1) | 0.5387 | 0.4446 | 32% |
175	| milk (task2) | 0.5169 | 0.5273 | 84% |
176	| bbq_sauce (task3) | 0.3561 | 0.3764 | 18% |
177	
178	**结论**: 30K 和 best checkpoint 的 ee_displacement 量级相近（0.47-0.50m），均远高于 frozen 阈值（0.1mm）。fake_safe% 全部为 0。30K 的 CAR 升高不是因为 frozen/action collapse，而是 over-avoidance（真正在避障，但更保守导致 TSR 下降）。
179	
180	---
181	
182	## 训练配置参考 (DONE+success)
183	
184	| exp_id | 配置 | best_loss | best_step |
185	|--------|------|-----------|-----------|
186	| train_pi05_a1_obj_s0_l005 | seed0, λ=0.005 | 0.00786 | 26K (无 best/ ckpt) |
187	| train_pi05_a1_obj_s0_l01 | seed0, λ=0.01 | 0.00801 | — (无 best/ ckpt) |
188	| train_pi05_a1_obj_s1_l005 | seed1, λ=0.005 | 0.01143 | 16K |
189	| train_pi05_a1_obj_s1_l01 | seed1, λ=0.01 | 0.01168 | 16K |
190	| train_pi05_a1_obj_s2_l005 | seed2, λ=0.005 | 0.00874 | 10K |
191	| train_pi05_a1_obj_s2_l01 | seed2, λ=0.01 | 0.00911 | 10K |
192	
193	---
194	
195	## 数据完整性统计
196	
197	- **已确认数据点**: 42 个（含所有 Table 1 已完成 eval、Claim 1-3 证据、Oracle 5 个变体、Over-avoidance 4 组对比）
198	- **待收集占位符**: 5 个
199	  1. seed0 best checkpoint eval (λ=0.005) — 训练未保存 best/ ckpt
200	  2. seed0 best checkpoint eval (λ=0.01) — 训练未保存 best/ ckpt
201	  3. seed1 best checkpoint eval (λ=0.01) — 待执行
202	  4. seed2 best checkpoint eval (λ=0.01) — 待执行
203	  5. Pi0.5 + LoRA (无 SDF) displacement-fixed eval — 待执行
204	- **Displacement-fixed eval 已完成**: 4 个（seed1_l005_30K, seed0_l01_30K, seed1_l005_16K_best, seed2_l005_10K_best）
205	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "3c9ee051-bffc-4371-bcb5-1e952eeeeecc"
}
```

</details>

---

### System

_source line 42_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/_project/data/claim3_data_summary.md",
  "usage": {
    "total_tokens": 17678,
    "tool_uses": 8,
    "duration_ms": 12867
  },
  "last_tool_name": "Read",
  "uuid": "cfaf3d7f-450e-46be-8233-740aff839ef3",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_013hiyXjTH2MoxYPE8ioZwvw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/data/claim3_data_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "f6fd0371-3eaf-4a5d-88df-239d72751710",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GU1R5B7ZmYh1QrXumrVdi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2428,
      "cache_read_input_tokens": 15209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2428,
        "ephemeral_1h_input_tokens": 0
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

_source line 44 · 2026-05-27T13:12:52.474Z_

<details><summary>↩ Tool result · `toolu_013hiyXjTH2MoxYPE8ioZwvw`</summary>

```text
1	# Claim 3: Avoidance Source Diagnosis — Data Summary
2	
3	## 1A. Main Summary Table
4	
5	| Condition | Seeds | CAR (per-seed) | CAR mean±std | TSR mean±std | dfCAR | frozen | EE Disp (m) |
6	|-----------|-------|----------------|--------------|--------------|-------|--------|-------------|
7	| Pi0.5 baseline | 3 | — | 26.8±1.6% | 74.7±1.5% | — | 0% | 0.367 |
8	| LoRA-only | 2 | s0=56.5, s1=52.5 | 54.5±2.83% | 51.5% | 54.5% | 0% | 0.392 |
9	| SDF λ=0.005 | 3 | s0=57.0, s1=54.0, s2=52.5 | 54.5±2.29% | 54.0±3.0% | 54.5% | 0% | 0.387 |
10	| SDF λ=0.01 | 3 | s0=57.0, s1=57.5, s2=54.5 | 56.3±1.61% | 53.8±1.5% | 56.3% | 0% | 0.389 |
11	| SDF λ=0.1 (20K) | 2 | s0=55, s1=56 | 55.5±0.71% | 52.5% | — | 0% | — |
12	| SDF λ=0.1 (30K) | — | pending | pending | pending | — | — | — |
13	
14	### Null Distribution
15	
16	Pooled from LoRA-only (2 seeds) + λ=0.005 (3 seeds) = 5 values: 56.5, 52.5, 57.0, 54.0, 52.5
17	
18	- **mean = 54.5%**, **σ = 2.15%**
19	
20	### Key Comparisons
21	
22	| Comparison | Δ vs null | σ units | p-value | Verdict |
23	|------------|-----------|---------|---------|---------|
24	| λ=0.01 mean (56.3%) vs null | +1.8pp | +0.84σ | >0.1 | not significant |
25	| λ=0.1 20K mean (55.5%) vs null | +1.0pp | +0.47σ | >0.1 | within null |
26	| Phase 2 ablation (λ=0 after 5K): 57.5% vs null | +3.0pp | +1.40σ | ~0.08 | within null |
27	
28	All SDF conditions fall within the null distribution range.
29	
30	---
31	
32	## 1B. Per-Task Breakdown
33	
34	### TSR per-task (from appendix.tex Table tab:per_task_tsr)
35	
36	| Task | Pi0.5 base | LoRA-only (2s mean) | SDF 0.005 (3s mean) | SDF 0.01 (3s mean) |
37	|------|-----------|---------------------|----------------------|---------------------|
38	| Orange Juice | 70.7 | 33.0 | 33.3 | 24.7 |
39	| Choco Pudding | 86.0 | 68.0 | 78.0 | 76.7 |
40	| Milk | 66.0 | 46.0 | 35.3 | 48.7 |
41	| BBQ Sauce | 76.0 | 59.0 | 69.3 | 65.3 |
42	
43	> **Note**: These are **TSR** values, not CAR. Source: appendix.tex Table tab:per_task_tsr.
44	
45	### CAR per-task for λ=0.1 (20K) (from eval JSON results)
46	
47	| Task | seed 0 | seed 1 |
48	|------|--------|--------|
49	| Orange Juice | 50 | 62 |
50	| Choco Pudding | 72 | 76 |
51	| Milk | 72 | 66 |
52	| BBQ Sauce | 26 | 20 |
53	
54	> **Note**: These are **CAR** values. Source: eval result JSONs.
55	
56	---
57	
58	## 1C. Scenario B Narrative Points
59	
60	1. **λ∈[0.005, 0.1] all within null range** — no SDF weight produces statistically significant CAR improvement over LoRA-only baseline.
61	2. **20× increase in SDF loss weight ineffective** — going from λ=0.005 to λ=0.1 does not change CAR.
62	3. **Level A signal masking is not a binding constraint** — even when SDF signal strength is amplified by 20×, collision avoidance rate does not improve.
63	4. **Level B (EE-only structural mismatch) is the sole binding constraint** — the SDF auxiliary loss acts on end-effector position only, but collision avoidance requires full-body awareness (links, joints, swept volumes).
64	5. **Paper conclusion: purely negative finding** — Claim 3 establishes that the SDF-based approach fundamentally cannot improve collision avoidance due to the structural gap between EE-level SDF supervision and the full-body collision geometry.
65	
66	---
67	
68	## Data Provenance
69	
70	- All 30K eval data: seed=7, rotation-fixed `eval_safelibero.py`
71	- λ=0.1 training uses suffix `_l1` (not `_l01`)
72	- Scenario B confirmed at 20K with dual seeds (55%, 56%)
73	- Phase 2 ablation (λ=0 after 5K): CAR=57.5%
74	- Null distribution: 5-sample pooled from LoRA-only + λ=0.005
75	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "0b50634e-5ddf-4f52-9611-3b99a3eb622a"
}
```

</details>

---

### System

_source line 45_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/_project/data/displacement_analysis_30k_summary.txt",
  "usage": {
    "total_tokens": 17679,
    "tool_uses": 9,
    "duration_ms": 13043
  },
  "last_tool_name": "Read",
  "uuid": "6ba1c01c-9769-423c-92cc-de729cbc27fb",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_011C21RmPJ6G5igPK2S6yDQb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/data/displacement_analysis_30k_summary.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "02eb1c1f-f19b-4f0c-8008-03fce4195888",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GU1R5B7ZmYh1QrXumrVdi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2428,
      "cache_read_input_tokens": 15209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2428,
        "ephemeral_1h_input_tokens": 0
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

_source line 47 · 2026-05-27T13:12:52.649Z_

<details><summary>↩ Tool result · `toolu_011C21RmPJ6G5igPK2S6yDQb`</summary>

```text
1	30K Displacement Analysis Summary (remote: /root/autodl-tmp/eval_results/displacement_analysis_30k_summary.txt)
2	
3	Key Finding: ALL 30K checkpoints show Filtered CAR = 0.0%, Frozen = 100%
4	- Every "safe" episode has max_displacement < 0.001m (action collapsed)
5	- Sensitivity analysis (threshold 0.0005~0.01m): results unchanged
6	- Only exception: s2_l01_30k has 1 episode above 0.0005m threshold
7	
8	This contrasts with 10K best checkpoints which showed real collision avoidance.
9	Supports paper narrative: continuous SDF training beyond ~10K causes action collapse.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "ffd00ff1-91d5-4f4c-ba7e-45fb6f606961"
}
```

</details>

---

### System

_source line 48_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/drafts/experiments.tex",
  "usage": {
    "total_tokens": 29907,
    "tool_uses": 10,
    "duration_ms": 18191
  },
  "last_tool_name": "Read",
  "uuid": "b3ac641f-e811-4111-847e-b557a2efbae8",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_01HjhUw1KM8hhBhDxE9Xt6UU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/drafts/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "a0e580ef-c59e-4080-ad0b-e9a7471cdb02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xkDDnWFDFk2PUsyEp4DQ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12226,
      "cache_read_input_tokens": 17637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12226,
        "ephemeral_1h_input_tokens": 0
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

_source line 50 · 2026-05-27T13:12:57.835Z_

<details><summary>↩ Tool result · `toolu_01HjhUw1KM8hhBhDxE9Xt6UU`</summary>

```text
1	\section{Experiments}\label{sec:experiments}
2	
3	We evaluate ColliForce-VLA on the SafeLIBERO benchmark to answer three questions: (1) Does integrating workspace SDF into the VLA forward pass improve collision avoidance? (2) Does the gradient-guided refinement loss contribute beyond auxiliary SDF supervision alone? (3) What is the trade-off between Collision Avoidance Rate (CAR) and Task Success Rate (TSR)?
4	
5	\subsection{Experimental Setup}\label{sec:setup}
6	
7	\paragraph{Benchmark.} We evaluate on SafeLIBERO~\cite{hu2025vlsa}, a collision-specific benchmark built on the LIBERO simulation platform. We select two representative scenes that cover distinct collision scenarios: \textit{spatial\_bowl} (Level II spatial complexity, obstacles surrounding a target bowl) and \textit{object\_pudding} (Level I object-level collision, obstacles adjacent to a pudding box). Each scene defines a language-conditioned manipulation task with non-target objects positioned to induce collisions during trajectory execution.
8	
9	\paragraph{Methods.} We compare three training variants that share the same $\pi_0$ backbone, LoRA configuration, and training schedule, differing only in loss composition:
10	\begin{itemize}
11	    \item \textit{$\pi_0$-LoRA}: Standard LoRA fine-tuning with flow-matching action loss $\mathcal{L}_\mathrm{action}$ only (baseline).
12	    \item \textit{ColliForce-Aux}: Adds SDF and EE auxiliary losses ($\mathcal{L}_\mathrm{SDF}$, $\mathcal{L}_\mathrm{EE}$) without gradient-guided refinement.
13	    \item \textit{ColliForce}: Full method with auxiliary losses and gradient-guided refinement loss $\mathcal{L}_\mathrm{refine}$.
14	\end{itemize}
15	
16	\paragraph{Metrics.} We report two metrics: Task Success Rate (TSR, $\uparrow$), the fraction of episodes where the manipulation task is completed, and Collision Avoidance Rate (CAR, $\uparrow$), the fraction of episodes where the end-effector does not contact any non-target obstacle. A collision is registered when the distance between the end-effector and any obstacle mesh falls below \textbf{[TODO: collision\_threshold from code]} meters.
17	
18	\paragraph{Evaluation protocol.} Each method is evaluated for 50 episodes per scene with fixed initial configurations. We report mean values across episodes. \textbf{[TODO: confirm if multiple seeds are available; if so, report mean $\pm$ std across seeds.]}
19	
20	\paragraph{Training details.} All variants train for 30K steps with batch size 32 on the same dataset. Phase 1 (steps 0--5K) trains only the SDF decoder and EE extractor on detached features; Phase 2 (steps 5K--30K) unfreezes LoRA parameters (${\sim}$33.5M) with linear gradient warmup over 100 steps. The $\pi_0$-LoRA baseline skips Phase 1 and trains for 30K steps with $\mathcal{L}_\mathrm{action}$ only. Hyperparameters follow Section~\ref{sec:training}.
21	
22	\subsection{Main Results}\label{sec:main_results}
23	
24	Table~\ref{tab:main_results} presents CAR and TSR for all methods across both scenes.
25	
26	\begin{table}[t]
27	\centering
28	\caption{Main results on SafeLIBERO collision scenarios. CAR: Collision Avoidance Rate ($\uparrow$), TSR: Task Success Rate ($\uparrow$). \textbf{Bold}: best CAR per scene.}
29	\label{tab:main_results}
30	\begin{tabular}{lcccc}
31	\toprule
32	\multirow{2}{*}{Method} & \multicolumn{2}{c}{\textit{spatial\_bowl}} & \multicolumn{2}{c}{\textit{object\_pudding}} \\
33	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
34	& CAR & TSR & CAR & TSR \\
35	\midrule
36	$\pi_0$-LoRA & \textbf{[TODO]} & \textbf{[TODO]} & \textbf{[TODO]} & \textbf{[TODO]} \\
37	ColliForce-Aux & \textbf{[TODO]} & \textbf{[TODO]} & \textbf{[TODO]} & \textbf{[TODO]} \\
38	ColliForce & \textbf{[TODO]} & \textbf{[TODO]} & \textbf{[TODO]} & \textbf{[TODO]} \\
39	\bottomrule
40	\end{tabular}
41	\end{table}
42	
43	\textbf{[TODO: Write narrative after results are available. Expected storyline:]}
44	
45	\textbf{Collision avoidance.} ColliForce achieves the highest CAR across both scenes, with [TODO: X pp] improvement over $\pi_0$-LoRA on \textit{spatial\_bowl} and [TODO: Y pp] on \textit{object\_pudding}. ColliForce-Aux also improves CAR over the baseline, confirming that auxiliary SDF supervision alone encourages the backbone to encode collision-relevant features.
46	
47	\textbf{Task success.} The TSR gap between ColliForce and $\pi_0$-LoRA is [TODO: characterize as negligible/modest/significant]. This indicates that internalizing collision geometry does not substantially compromise task completion, as the action loss $\mathcal{L}_\mathrm{action}$ remains the dominant training objective.
48	
49	\subsection{Ablation Study}\label{sec:ablation}
50	
51	The comparison between ColliForce-Aux and ColliForce isolates the contribution of the gradient-guided refinement loss $\mathcal{L}_\mathrm{refine}$ from that of auxiliary SDF supervision ($\mathcal{L}_\mathrm{SDF}$, $\mathcal{L}_\mathrm{EE}$).
52	
53	\textbf{[TODO: Write after results. Key questions to address:]}
54	\begin{itemize}
55	    \item Does $\mathcal{L}_\mathrm{refine}$ provide CAR gains beyond what $\mathcal{L}_\mathrm{SDF} + \mathcal{L}_\mathrm{EE}$ alone achieve?
56	    \item Is the TSR cost of gradient refinement larger or smaller than that of auxiliary supervision?
57	    \item How frequently does the near-collision set $\mathcal{S}$ activate during training (fraction of batches with $|\mathcal{S}| > 0$)?
58	\end{itemize}
59	
60	\subsection{Analysis}\label{sec:analysis}
61	
62	\paragraph{Trajectory visualization.} Figure~\ref{fig:trajectory_viz} shows representative end-effector trajectories from $\pi_0$-LoRA and ColliForce on the same initial configuration, overlaid on a 2D slice of the workspace SDF. \textbf{[TODO: Describe qualitative differences after generating fig3\_trajectory\_viz.]}
63	
64	\paragraph{SDF prediction quality.} We evaluate the learned SDF decoder's prediction accuracy by computing the mean absolute error between predicted and ground-truth SDF values at the query points used during training. \textbf{[TODO: Report MAE, ideally broken down by distance to surface ($< \delta$ vs $\geq \delta$).]}
65	
66	\paragraph{Optional inference-time correction.} Section~\ref{sec:inference} describes an optional SDF gradient correction at inference. We evaluate its effect on ColliForce by enabling the correction during evaluation. \textbf{[TODO: Report CAR/TSR delta. Expected: minimal change, confirming that ColliForce has already internalized collision avoidance.]}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "b4beddb3-416f-4576-92ec-d2f9a6acd1a2"
}
```

</details>

---

### System

_source line 51_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/drafts/abstract.tex",
  "usage": {
    "total_tokens": 29908,
    "tool_uses": 11,
    "duration_ms": 18741
  },
  "last_tool_name": "Read",
  "uuid": "0854d90d-297c-471c-9756-21579f2a5f47",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_01ULY9pknWeo9Ce6H8FE2sjL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/drafts/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "d56a661d-cc6f-4151-9777-f19f5ac1a207",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xkDDnWFDFk2PUsyEp4DQ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12226,
      "cache_read_input_tokens": 17637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12226,
        "ephemeral_1h_input_tokens": 0
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

_source line 53 · 2026-05-27T13:12:58.362Z_

<details><summary>↩ Tool result · `toolu_01ULY9pknWeo9Ce6H8FE2sjL`</summary>

```text
1	\begin{abstract}
2	Vision-Language-Action (VLA) models generate manipulation trajectories from visual observations and language instructions, but frequently collide with non-target objects in cluttered workspaces. Existing collision-safe approaches either apply post-hoc corrections to already-generated trajectories or rely on reinforcement learning without geometric reasoning, leaving the VLA's internal representations collision-ignorant. We propose ColliForce-VLA, which integrates a differentiable workspace Signed Distance Field (SDF) into the VLA forward pass for collision-aware action generation. Two lightweight modules, an SDF Decoder (${\sim}$395K parameters) and an End-Effector Extractor (${\sim}$263K parameters), are attached to the action expert of $\pi_0$, a 3.5B-parameter flow-matching VLA. During training, for near-collision samples, we compute the SDF gradient in feature space and perform gradient ascent to produce collision-corrected action targets; a refinement loss trains the LoRA parameters (${\sim}$33.5M) to reproduce these targets directly. At inference, the default path requires only the base model with trained LoRA adapters, adding no extra modules or computation. On the SafeLIBERO benchmark, ColliForce-VLA achieves a Collision Avoidance Rate (CAR) of \textbf{[TODO]}\% on \textit{spatial\_bowl} and \textbf{[TODO]}\% on \textit{object\_pudding}, improving over the LoRA baseline by \textbf{[TODO]} and \textbf{[TODO]} percentage points respectively, while maintaining Task Success Rates (TSR) of \textbf{[TODO]}\% and \textbf{[TODO]}\%. Ablation studies confirm that the gradient-guided refinement provides \textbf{[TODO]} percentage points additional CAR gain beyond auxiliary SDF supervision alone.
3	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "38fa8954-4df6-46ec-be4c-995bcdaa754b"
}
```

</details>

---

### System

_source line 54_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/drafts/abstract_v2.tex",
  "usage": {
    "total_tokens": 29909,
    "tool_uses": 12,
    "duration_ms": 19361
  },
  "last_tool_name": "Read",
  "uuid": "441dafc2-2577-4766-b3ad-ab44bfc65695",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_01WsJj3NRffnDymQo88WQ7Hz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/drafts/abstract_v2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "d76eb70e-068a-44f4-8291-a0a2f6172133",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xkDDnWFDFk2PUsyEp4DQ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12226,
      "cache_read_input_tokens": 17637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12226,
        "ephemeral_1h_input_tokens": 0
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

_source line 56 · 2026-05-27T13:12:58.974Z_

<details><summary>↩ Tool result · `toolu_01WsJj3NRffnDymQo88WQ7Hz`</summary>

```text
1	\begin{abstract}
2	Recent methods for collision avoidance in Vision-Language-Action (VLA) models report high Collision Avoidance Rate (CAR) on safety benchmarks and claim effective obstacle avoidance. We show that these metrics can be systematically contaminated by action collapse: the model ceases to produce meaningful motion, and the resulting inaction is counted as successful avoidance. On the SafeLIBERO benchmark, a Signed Distance Field (SDF)-augmented VLA reports 91.5\% CAR, yet 99.6\% of its safe episodes exhibit end-effector displacement below 0.1\,mm. This contamination is not method-specific; a baseline without any collision objective achieves 82\% CAR with 99.4\% of safe episodes below the same threshold, and a more capable model shows the same pattern. We propose displacement-filtered CAR (CAR$_\text{f}$), which excludes sub-threshold episodes, as a corrective metric. Further analysis reveals two structural issues. First, Task Success Rate (TSR) and CAR are anti-correlated: models that move the robot through the workspace collide, while collapsed models appear safe. Second, ground-truth SDF oracle experiments demonstrate that end-effector-only refinement cannot prevent full-body collisions, as SDF gradients that repel the end-effector simultaneously drive arm links into obstacle volumes. Preliminary results indicate that training-time SDF supervision on a sufficiently capable VLA can produce genuine collision avoidance with zero frozen-action rate. Our findings establish that displacement filtering is necessary for meaningful VLA safety evaluation.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "39444d18-a82d-4e16-a403-b15ffcfe8ef7"
}
```

</details>

---

### System

_source line 57_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/drafts/introduction.tex",
  "usage": {
    "total_tokens": 29910,
    "tool_uses": 13,
    "duration_ms": 20010
  },
  "last_tool_name": "Read",
  "uuid": "a5dad998-cc3d-4832-8e28-a018567c328b",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Read · `toolu_018JAJJK3jJzv3YfyFj6z1D1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/drafts/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "d79cfdfe-25be-42af-8aae-9ead324d3edc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xkDDnWFDFk2PUsyEp4DQ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12226,
      "cache_read_input_tokens": 17637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12226,
        "ephemeral_1h_input_tokens": 0
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

_source line 59 · 2026-05-27T13:12:59.617Z_

<details><summary>↩ Tool result · `toolu_018JAJJK3jJzv3YfyFj6z1D1`</summary>

```text
1	\section{Introduction}
2	
3	Vision-Language-Action (VLA) models such as $\pi_0$~\cite{black2024pi0}, OpenVLA~\cite{kim2024openvla}, and RT-2~\cite{brohan2023rt2} combine visual perception, language understanding, and action generation in a unified architecture to follow diverse natural language instructions across manipulation tasks. These models learn action policies from large-scale demonstration datasets and can generalize to new instructions, objects, and scenes. Yet when deployed in cluttered environments where non-target objects densely surround the manipulation target, VLAs frequently produce trajectories that collide with surrounding obstacles. The demonstration data used for training typically features unobstructed workspaces, and the resulting policies have no explicit incentive to maintain clearance from nearby surfaces. Collisions cause task failure, risk damage to the robot and surrounding objects, and represent a critical barrier to safe deployment in household and industrial settings. The SafeLIBERO benchmark~\cite{hu2025vlsa}, comprising 32 collision scenarios across 1,600 evaluation episodes, was introduced to systematically quantify this failure mode and confirms that even high-performing VLAs exhibit substantial collision rates in constrained workspaces. The root cause is architectural: current VLAs observe scenes through 2D images, generate action sequences through learned policies, and have no internal mechanism to determine whether the predicted end-effector trajectory will intersect obstacle surfaces.
4	
5	Recent work addresses this problem, but exclusively through mechanisms external to the VLA's internal representations. AEGIS~\cite{hu2025vlsa} introduces a plug-in safety constraint layer based on Control Barrier Functions (CBFs): it identifies obstacles via open-set detection and depth estimation, then corrects unsafe actions after they have been generated, achieving an average Collision Avoidance Rate (CAR) of 77.85\% across SafeLIBERO scenarios. AEGIS requires no additional training and can be attached to any pretrained VLA, a practical advantage. SafeVLA~\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\% through reward shaping during reinforcement learning; this approach, however, does not incorporate geometric information about the workspace and relies entirely on learned reward signals to encode safety. CoFreeVLA~\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that detects dangerous configurations and halts execution when predicted collision risk exceeds a threshold. These approaches share a common architectural pattern: the safety mechanism operates independently of the VLA's learned feature representations. The model first generates a trajectory without collision awareness, and a separate module then evaluates or corrects it. This reactive paradigm faces two fundamental limitations. In cluttered environments, the space available for post-hoc trajectory correction shrinks, and corrections may push the end-effector into other obstacles. Because the VLA itself never learns to represent collision geometry, it cannot anticipate obstacles during action generation and will repeatedly propose unsafe trajectories that require external intervention. A proactive alternative would embed collision-relevant geometric information directly into the VLA's forward pass, so that action tokens encode collision awareness from the point of generation.
6	
7	A parallel research direction has enriched VLA architectures with 3D spatial information. Numerous recent methods integrate depth maps, point clouds, or implicit 3D representations into VLA training or inference~\cite{depthvla2025, li2025qdepth, li2025spatialforcing, 3dcavla2025, geoaware2025, spatialvla2025, gstvla2026, stemvla2026, stvla2026, evo02025, savla2026, augvla3d2026, evodepth2026}. These methods improve task success rate, viewpoint generalization, or grasping precision, but none targets collision avoidance as a design objective and none evaluates on collision-specific metrics. QDepth-VLA~\cite{li2025qdepth}, the closest methodological precedent for auxiliary spatial supervision in VLAs, uses quantized depth prediction as a training-time auxiliary loss via a VQ-VAE decoder. Its decoder is decoupled from the action head: depth gradients flow into the backbone but do not explicitly modify the action token generation pathway. Depth is a 2.5D camera-frame representation that encodes the distance from each pixel to the camera. Deriving collision-relevant directions in the robot's workspace from depth gradients requires an implicit perspective-to-workspace coordinate transformation that depends on camera intrinsics and extrinsics, and occluded regions (where obstacles may be hidden behind the robot arm or other objects) produce no depth signal. The result is a clear gap between two active communities: spatially-aware VLAs do not address collision avoidance, and collision-safe VLAs do not internalize spatial geometry into the model's representations.
8	
9	We propose ColliForce-VLA, which integrates a differentiable workspace Signed Distance Field (SDF) into the VLA forward pass for collision-aware action generation. Workspace SDF encodes, at each 3D point, the signed distance to the nearest obstacle surface; its spatial gradient points directly away from that surface in workspace coordinates. Unlike depth gradients that reside in camera frame, SDF gradients require no coordinate transformation and cover the full 3D workspace including occluded regions. SDF gradients indicate repulsion direction from obstacles by construction, and their continuous nature provides informative signals even at moderate distances from surfaces, in contrast to binary occupancy whose gradient is zero almost everywhere. ColliForce-VLA augments $\pi_0$~\cite{black2024pi0} with two lightweight modules attached to the action expert: an SDF Decoder (4-layer MLP, ${\sim}$395K parameters) that predicts workspace SDF from the action expert's pooled suffix features, and an End-Effector (EE) Extractor (2-layer MLP, ${\sim}$263K parameters) that predicts end-effector position from the same features. During training, for near-collision samples where predicted SDF at the end-effector is low, we compute $\nabla_z \hat{\Phi}$, the gradient of the predicted SDF with respect to the shared feature representation $z$, and perform gradient ascent ($z' = z + \alpha \cdot \nabla_z \hat{\Phi}$) to push $z$ toward collision-free configurations. Both $z$ and $z'$ are projected into action token space, and a refinement loss trains the LoRA parameters (${\sim}$33.5M) to directly produce the collision-corrected actions without requiring the gradient refinement step. The SDF supervisory signal is derived from known workspace geometry (obstacle meshes available in simulation), requiring no additional sensors beyond the standard visual input. At inference, the default path requires only the base model with trained LoRA, adding no extra modules or computation. An optional SDF gradient correction provides an additional safety net for out-of-distribution obstacle configurations (Section~\ref{sec:inference}). Unlike AEGIS~\cite{hu2025vlsa}, which applies training-free post-hoc correction to already-generated trajectories, ColliForce-VLA internalizes collision geometry into the model's own parameters during training, enabling proactive avoidance at generation time with a potentially better CAR-TSR trade-off in cluttered settings. Unlike QDepth-VLA~\cite{li2025qdepth}, whose depth decoder provides camera-frame auxiliary gradients to the backbone without explicitly modifying action tokens, our SDF gradient refinement operates in workspace frame and directly modulates the feature representations from which action tokens are decoded. The collision-avoidance capability is absorbed into the model's LoRA parameters during training and does not rely on any external safety layer at deployment.
10	
11	Our contributions are as follows:
12	\begin{itemize}
13	    \item We introduce a differentiable collision-aware mechanism for VLAs that integrates workspace SDF into the forward pass. SDF gradients in feature space ($\nabla_z \hat{\Phi}$) guide action token generation toward collision-free configurations and provide a proactive alternative to post-hoc safety correction (Section~\ref{sec:method}).
14	    \item We design a gradient-guided refinement training strategy where SDF gradients in feature space produce collision-corrected action targets, and LoRA parameters learn to reproduce these targets directly. The default inference path incurs no additional cost; an optional SDF gradient correction is available for safety-critical deployment (Section~\ref{sec:training}).
15	    \item We conduct systematic experiments and ablation studies on the SafeLIBERO benchmark that separately quantify the contributions of SDF auxiliary supervision and SDF gradient-guided refinement to Collision Avoidance Rate (CAR) and Task Success Rate (TSR) \textbf{[TODO: specific numbers pending experiments]} (Section~\ref{sec:experiments}).
16	\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "e1f1a032-31f2-44e4-8bcb-297cebfd90c8"
}
```

</details>

---

### System

_source line 60_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/drafts/introduction_v2.tex",
  "usage": {
    "total_tokens": 29911,
    "tool_uses": 14,
    "duration_ms": 20521
  },
  "last_tool_name": "Read",
  "uuid": "61a2474c-7e8a-4f01-8dea-2cb7209d1f1b",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Read · `toolu_01QzEx3HYY2qwLwabedVESW8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/drafts/introduction_v2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "7a9747d2-e877-4ed0-8b67-a2121eaffd74",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xkDDnWFDFk2PUsyEp4DQ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12226,
      "cache_read_input_tokens": 17637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12226,
        "ephemeral_1h_input_tokens": 0
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

_source line 62 · 2026-05-27T13:13:00.127Z_

<details><summary>↩ Tool result · `toolu_01QzEx3HYY2qwLwabedVESW8`</summary>

```text
1	\section{Introduction}
2	
3	Vision-Language-Action (VLA) models unify visual perception, language understanding, and continuous action generation in a single architecture. Models such as $\pi_0$~\cite{black2024pi0}, OpenVLA~\cite{kim2024openvla}, and RT-2~\cite{brohan2023rt2} can follow diverse natural language instructions across manipulation tasks. As these models move toward real-world deployment, a critical failure mode has emerged: frequent collisions with non-target objects in cluttered environments. The demonstration data used for training typically features unobstructed workspaces, and the resulting policies acquire no explicit incentive to maintain clearance from nearby surfaces. Collisions cause task failure, risk damage to the robot and its surroundings, and represent a central barrier to safe deployment. The SafeLIBERO benchmark~\cite{hu2025vlsa}, comprising 32 collision scenarios across 1,600 evaluation episodes, was introduced to systematically quantify this problem and confirms that even high-performing VLAs exhibit substantial collision rates when non-target objects surround the manipulation target.
4	
5	Several recent methods target collision avoidance in VLAs. AEGIS~\cite{hu2025vlsa} applies post-hoc Control Barrier Function (CBF) corrections to already-generated trajectories and reports an average Collision Avoidance Rate (CAR) of 77.85\% across SafeLIBERO scenarios without additional training. SafeVLA~\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\% through reward shaping during reinforcement learning. CoFreeVLA~\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that halts execution when predicted collision risk exceeds a threshold. In our own experiments, a Pi0 model fine-tuned with an auxiliary Signed Distance Field (SDF) loss (referred to as A1-LoRA) achieves 91.5\% CAR on SafeLIBERO. These methods share a common evaluation pattern: they report high CAR as evidence of effective collision avoidance. The numbers appear compelling, and the implicit assumption across this emerging literature is that high CAR reflects genuine obstacle avoidance behavior.
6	
7	For the Pi0-family models we evaluate, this assumption does not hold. Their CAR values are systematically contaminated by \emph{action collapse}, a phenomenon in which the VLA ceases to produce meaningful motion. We argue that the underlying mechanism, action collapse inflating displacement-based safety metrics, is likely present in any VLA susceptible to mode collapse, though our direct evidence comes from the Pi0 family. When we examine the end-effector displacement of the 732 episodes that A1-LoRA classifies as ``safe,'' 99.6\% exhibit a maximum displacement below 0.1\,mm. The robot did not avoid obstacles; it avoided motion altogether. This contamination is not specific to A1-LoRA or to SDF-based approaches. The LoRA baseline (no collision avoidance objective) achieves 82\% CAR with 99.4\% of its safe episodes below the displacement threshold. Pi0.5, a more capable model from the same family, exhibits the same pattern: 98.2\% of its safe episodes are fake safe. We acknowledge that action collapse itself is a well-documented failure mode of undertrained or distribution-shifted models, and its existence alone would not warrant a dedicated analysis. What is non-trivial is the \emph{consequence}: action collapse silently inflates the primary safety metric used to evaluate collision avoidance methods. Downstream researchers who compare methods based on reported CAR values will draw incorrect conclusions about relative safety. Models that collapse more severely will paradoxically appear safer, and genuinely unsafe models may be deployed on the basis of contaminated evaluations. We propose the displacement-filtered CAR (CAR$_\text{f}$), which excludes episodes with sub-threshold displacement from both numerator and denominator, as a corrective metric that separates genuine avoidance from inaction.
8	
9	The fake safety problem connects to two deeper structural issues. First, task capability and collision avoidance are anti-correlated under current evaluation practice. Pi0.5 achieves a TSR of 74.7\,$\pm$\,1.5\% but a CAR of only 26.8\,$\pm$\,1.6\%, while Pi0-based methods report CAR of 82--91.5\% alongside TSR $\leq$ 0.5\%. The explanation is mechanical: a model that moves the robot through the workspace encounters obstacles; a model that does not move encounters none. CAR is therefore informative only when conditioned on sufficient task capability, and the TSR-CAR plane reveals that no current method occupies the upper-right quadrant where both metrics are high. Second, end-effector-only SDF refinement, the most direct geometric approach to collision avoidance, has a structural defect. We construct oracle experiments that replace the learned SDF network with ground-truth signed distance fields computed from simulation geometry. All three oracle variants achieve \emph{lower} CAR than unrefined baselines (best oracle: 76.9\% vs.\ LoRA baseline: 82.0\%). The SDF gradient pushes the end-effector away from obstacles, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Perfect distance information at the end-effector cannot compensate for the absence of full-body collision awareness. A preliminary result provides a constructive counterpoint: a Pi0.5 model augmented with training-time SDF supervision (10K-step checkpoint) achieves CAR of 56--58\% with TSR of 47--49\% and a frozen-action rate of 0\%, placing it in the previously empty central region of the TSR-CAR plane which suggests that genuine collision avoidance is achievable when the base model retains sufficient capability.
10	
11	Our contributions are as follows:
12	\begin{itemize}
13	    \item We identify the fake safety problem in VLA collision avoidance evaluation: action collapse systematically inflates Collision Avoidance Rate, and we find that 98--99\% of safe episodes across multiple methods and model scales are attributable to inaction rather than obstacle avoidance. We propose displacement-filtered CAR (CAR$_\text{f}$) as a corrective metric (Section~\ref{sec:fake_safety}).
14	    \item We demonstrate that model capability and reported collision avoidance are anti-correlated under standard CAR evaluation. Models that execute tasks collide more because they move, while action-collapsed models receive inflated safety scores, rendering cross-method comparisons on raw CAR misleading (Section~\ref{sec:tsr_car}).
15	    \item Through ground-truth SDF oracle experiments, we establish that end-effector-only SDF refinement is a structural limitation: even perfect distance information cannot prevent full-body collisions, as gradients that repel the end-effector simultaneously drive arm links into obstacle volumes (Section~\ref{sec:ee_only}).
16	    \item[\textbf{[C4]}] Preliminary evidence from a Pi0.5 model with training-time SDF supervision shows 0\% frozen-action rate alongside CAR of 56--58\% and TSR of 47--49\%, suggesting that SDF auxiliary losses can produce genuine collision avoidance when applied to a VLA with sufficient baseline capability (Section~\ref{sec:a1_pi05}; full results pending).
17	\end{itemize}
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "43533ba8-d656-4711-b7be-2aced04846fc"
}
```

</details>

---

### System

_source line 63_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/drafts/conclusion.tex",
  "usage": {
    "total_tokens": 29912,
    "tool_uses": 15,
    "duration_ms": 20993
  },
  "last_tool_name": "Read",
  "uuid": "80bb3ab8-fdc2-472a-8deb-e97f771cf1a3",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Read · `toolu_014jhH1Rf52XSVgk8Cb6yW5P`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/drafts/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "152685ea-c126-46a7-a52b-74f319e46efd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xkDDnWFDFk2PUsyEp4DQ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12226,
      "cache_read_input_tokens": 17637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12226,
        "ephemeral_1h_input_tokens": 0
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

_source line 65 · 2026-05-27T13:13:00.599Z_

<details><summary>↩ Tool result · `toolu_014jhH1Rf52XSVgk8Cb6yW5P`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We presented ColliForce-VLA, a method that integrates differentiable workspace Signed Distance Fields into the forward pass of a Vision-Language-Action model for collision-aware action generation. By attaching a lightweight SDF Decoder and End-Effector Extractor to the action expert, and training LoRA parameters to reproduce SDF-gradient-corrected action targets, the method internalizes collision avoidance into the model's own parameters. The default inference path requires only the base model with trained LoRA, adding no extra modules or computation. On the SafeLIBERO benchmark, ColliForce-VLA improves Collision Avoidance Rate by \textbf{[TODO]} percentage points over the LoRA baseline while maintaining competitive Task Success Rates, and ablation studies confirm that the gradient-guided refinement contributes beyond auxiliary SDF supervision alone.
4	
5	\paragraph{Limitations.} Our evaluation is limited to two SafeLIBERO scenes in simulation; broader task coverage and real-robot transfer remain to be demonstrated. The SDF ground truth requires known obstacle meshes, which are available in simulation but would require reconstruction methods (e.g., neural SDF from depth observations) for real-world deployment. The method is validated on a single base VLA ($\pi_0$); generalization to other architectures (OpenVLA, RT-2) is an open question.
6	
7	\paragraph{Future work.} Three directions follow naturally. First, replacing precomputed SDF with a real-time neural SDF estimated from depth observations would remove the dependency on known meshes and enable deployment in unstructured environments. Second, real-robot validation would test whether the collision avoidance behavior learned in simulation transfers across the sim-to-real gap. Third, extending the evaluation to a broader set of SafeLIBERO scenarios and additional benchmarks would strengthen the generality claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "a00dec73-d452-4606-b584-9b8ef9018595"
}
```

</details>

---

### System

_source line 66_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/drafts/method.tex",
  "usage": {
    "total_tokens": 29913,
    "tool_uses": 16,
    "duration_ms": 21464
  },
  "last_tool_name": "Read",
  "uuid": "e2dd5f6d-d960-4434-8156-05088f3ce70c",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Read · `toolu_019TWNUSaG1MuMWqvrbUL6uC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/drafts/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "926a0ecd-70a9-468d-abc3-0db54a77138d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xkDDnWFDFk2PUsyEp4DQ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12226,
      "cache_read_input_tokens": 17637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12226,
        "ephemeral_1h_input_tokens": 0
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

_source line 68 · 2026-05-27T13:13:01.071Z_

<details><summary>↩ Tool result · `toolu_019TWNUSaG1MuMWqvrbUL6uC`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	We present ColliForce-VLA, a framework that integrates differentiable workspace Signed Distance Fields (SDFs) into the forward pass of a pretrained Vision-Language-Action model to enable collision-aware action generation. The method requires no architectural modification to the VLA backbone; the default inference path uses only the base model with trained LoRA adapters. We describe the problem formulation (Section~\ref{sec:problem}), the differentiable SDF integration (Section~\ref{sec:sdf_integration}), the gradient-guided action refinement mechanism (Section~\ref{sec:gradient_refinement}), the training protocol (Section~\ref{sec:training}), and inference-time deployment (Section~\ref{sec:inference}).
4	
5	\subsection{Problem Formulation}\label{sec:problem}
6	
7	We consider a language-conditioned robotic manipulation setting where a Vision-Language-Action model $\pi_\theta$ generates an action trajectory $\{a_t\}_{t=1}^{H}$ with horizon $H = 50$, conditioned on visual observations $o$ and a language instruction $l$. Each action $a_t \in \mathbb{R}^7$ specifies the desired end-effector (EE) displacement in position ($\Delta x, \Delta y, \Delta z$), orientation ($\Delta q_1, \Delta q_2, \Delta q_3$), and gripper state.
8	
9	We formalize collision avoidance through the workspace Signed Distance Field $\Phi: \mathbb{R}^3 \to \mathbb{R}$, where $\Phi(\mathbf{x}) > 0$ indicates free space, $\Phi(\mathbf{x}) = 0$ denotes the obstacle boundary, and $\Phi(\mathbf{x}) < 0$ indicates penetration. The objective is to learn a policy satisfying $\Phi(\mathrm{EE}(a_t)) > 0$ for all $t$ while preserving task success.
10	
11	Our base model is $\pi_0$~\cite{black2024pi0}, a 3.5B-parameter flow-matching VLA comprising a PaliGemma vision-language encoder (Gemma 2B) and a Gemma 300M action expert. The action expert produces a sequence of action tokens through an output projection $W_{\mathrm{out}} \in \mathbb{R}^{1024 \times 32}$ that maps from the expert's hidden dimension to the action token space.
12	
13	\subsection{Differentiable SDF Integration}\label{sec:sdf_integration}
14	
15	We augment the VLA with two lightweight auxiliary modules that operate on the action expert's intermediate representations, together adding fewer than 660K parameters.
16	
17	\paragraph{Feature extraction.} We capture the action expert's suffix output $\mathbf{z} \in \mathbb{R}^{B \times H \times 1024}$, the tensor immediately preceding $W_{\mathrm{out}}$, via a forward hook on \texttt{action\_out\_proj}. Mean-pooling along the action horizon dimension yields a compact representation:
18	\begin{equation}\label{eq:pooling}
19	\bar{\mathbf{z}} = \frac{1}{H} \sum_{t=1}^{H} \mathbf{z}_t \in \mathbb{R}^{1024}
20	\end{equation}
21	that summarizes the action expert's spatial understanding of the current scene.
22	
23	\paragraph{SDF Decoder.} A 4-layer MLP $f_\mathrm{SDF}$ predicts the signed distance value at arbitrary 3D query points given the pooled features:
24	\begin{equation}\label{eq:sdf_decoder}
25	f_\mathrm{SDF}: (\bar{\mathbf{z}}, \mathbf{x}) \mapsto \hat{\Phi}(\mathbf{x}), \quad \bar{\mathbf{z}} \in \mathbb{R}^{1024},\; \mathbf{x} \in \mathbb{R}^3
26	\end{equation}
27	The architecture employs hidden dimension 256 with Softplus activation ($\beta = 5$) and a skip connection that re-injects the query coordinates at layer 2:
28	\begin{align}
29	\mathbf{h}_0 &= \sigma(\mathbf{W}_0 [\bar{\mathbf{z}}; \mathbf{x}] + \mathbf{b}_0), \quad \mathbf{W}_0 \in \mathbb{R}^{256 \times 1027} \label{eq:sdf_layer0} \\
30	\mathbf{h}_1 &= \sigma(\mathbf{W}_1 \mathbf{h}_0 + \mathbf{b}_1), \quad \mathbf{W}_1 \in \mathbb{R}^{256 \times 256} \\
31	\mathbf{h}_2 &= \sigma(\mathbf{W}_2 [\mathbf{h}_1; \mathbf{x}] + \mathbf{b}_2), \quad \mathbf{W}_2 \in \mathbb{R}^{256 \times 259} \\
32	\hat{\Phi}(\mathbf{x}) &= \mathbf{W}_3 \mathbf{h}_2 + \mathbf{b}_3, \quad \mathbf{W}_3 \in \mathbb{R}^{1 \times 256} \label{eq:sdf_output}
33	\end{align}
34	where $\sigma(\cdot) = \mathrm{Softplus}_{\beta=5}(\cdot)$. The total parameter count is ${\sim}$395K. Spatial gradients $\nabla_{\mathbf{x}} \hat{\Phi}(\mathbf{x})$ are computed via \texttt{torch.autograd.grad} with graph creation enabled during training, which is required for Eikonal regularization and the gradient-guided refinement in Section~\ref{sec:gradient_refinement}.
35	
36	\paragraph{End-Effector (EE) Extractor.} A 2-layer MLP $g_\mathrm{EE}$ predicts the current EE position from the pooled features:
37	\begin{equation}\label{eq:ee_extractor}
38	g_\mathrm{EE}: \bar{\mathbf{z}} \mapsto \hat{\mathbf{p}}_\mathrm{EE} \in \mathbb{R}^3, \quad \mathrm{Linear}(1024, 256) \to \mathrm{ReLU} \to \mathrm{Linear}(256, 3)
39	\end{equation}
40	with ${\sim}$263K parameters. The EE prediction provides the query point for evaluating collision proximity, and its auxiliary loss encourages the action expert features to encode spatial position information.
41	
42	\paragraph{Auxiliary losses.} The SDF decoder is trained with a clamped L1 loss and Eikonal regularization:
43	\begin{equation}\label{eq:loss_sdf}
44	\mathcal{L}_\mathrm{SDF} = \frac{1}{N} \sum_{i=1}^{N} \left| \mathrm{clamp}(\hat{\Phi}(\mathbf{x}_i), \pm\delta) - \mathrm{clamp}(\Phi^*(\mathbf{x}_i), \pm\delta) \right| + \lambda_\mathrm{eik} \frac{1}{N} \sum_{i=1}^{N} \left( \|\nabla_{\mathbf{x}} \hat{\Phi}(\mathbf{x}_i)\|_2 - 1 \right)^2
45	\end{equation}
46	where $\delta = 0.05$ is the clamping threshold (in meters), $\lambda_\mathrm{eik} = 0.1$, and $N = 64$ query points are sampled from the ground-truth SDF volume per step. The ground-truth SDF volume $\Phi^*(\mathbf{x})$ is precomputed from known obstacle meshes in the simulation workspace using mesh-to-SDF distance queries (via trimesh/pysdf) at a fixed spatial resolution \textbf{[TODO: confirm resolution from code]}. Clamping focuses learning on the near-surface region most relevant for collision detection; the Eikonal term enforces the unit-gradient property of valid distance fields. The EE extractor is trained with MSE loss:
47	\begin{equation}\label{eq:loss_ee}
48	\mathcal{L}_\mathrm{EE} = \|\hat{\mathbf{p}}_\mathrm{EE} - \mathbf{p}^*_\mathrm{EE}\|_2^2
49	\end{equation}
50	where $\mathbf{p}^*_\mathrm{EE} \in \mathbb{R}^3$ is the ground-truth end-effector position obtained from the robot's forward kinematics.
51	
52	\subsection{SDF Gradient-Guided Action Refinement}\label{sec:gradient_refinement}
53	
54	The core contribution of ColliForce-VLA is a gradient-based mechanism that steers the action expert's representations away from collision-prone regions during training. Unlike post-hoc action filtering or external safety layers, this approach modifies the feature space directly, enabling the model to internalize collision avoidance behavior into its LoRA parameters.
55	
56	\paragraph{Refinement procedure.} Given the captured suffix output $\mathbf{z} \in \mathbb{R}^{B \times H \times 1024}$, the refinement proceeds in five steps:
57	
58	\textbf{Step 1.} Predict EE position and evaluate the SDF:
59	\begin{equation}
60	\hat{\mathbf{p}}_\mathrm{EE} = g_\mathrm{EE}(\bar{\mathbf{z}}), \quad \hat{\Phi}(\hat{\mathbf{p}}_\mathrm{EE}) = f_\mathrm{SDF}(\bar{\mathbf{z}}, \hat{\mathbf{p}}_\mathrm{EE})
61	\end{equation}
62	
63	\textbf{Step 2.} Identify near-collision samples within the batch:
64	\begin{equation}\label{eq:collision_set}
65	\mathcal{S} = \{i : \hat{\Phi}(\hat{\mathbf{p}}_{\mathrm{EE},i}) < m\}, \quad m = 0.01 \text{ (meters)}
66	\end{equation}
67	
68	\textbf{Step 3.} For samples in $\mathcal{S}$, compute the feature-space SDF gradient:
69	\begin{equation}\label{eq:feature_grad}
70	\nabla_{\mathbf{z}} \hat{\Phi} = \frac{\partial \hat{\Phi}(\hat{\mathbf{p}}_\mathrm{EE})}{\partial \mathbf{z}}
71	\end{equation}
72	This gradient captures how changes in the action expert's internal representation affect the predicted collision distance. It is distinct from the spatial gradient $\nabla_{\mathbf{x}} \hat{\Phi}$ used in Eikonal regularization: $\nabla_{\mathbf{z}} \hat{\Phi}$ operates in the 1024-dimensional feature space and encodes directions that move the entire action representation toward safety.
73	
74	\textbf{Step 4.} Perform gradient ascent on the SDF value (toward higher, safer distances):
75	\begin{equation}\label{eq:gradient_ascent}
76	\mathbf{z}' = \mathbf{z} + \alpha \cdot \mathrm{clip}(\nabla_{\mathbf{z}} \hat{\Phi}, \gamma) \odot \mathbf{m}_\mathcal{S}
77	\end{equation}
78	where $\alpha = 0.1$ is the step size, $\mathrm{clip}(\cdot, \gamma)$ denotes per-sample L2 norm clipping with threshold $\gamma = 1.0$ for gradient stability, and $\mathbf{m}_\mathcal{S}$ is a binary mask selecting only near-collision samples.
79	
80	\textbf{Step 5.} Project both original and refined features through the action output projection:
81	\begin{equation}\label{eq:projection}
82	\mathbf{v}_t = W_\mathrm{out} \mathbf{z}_t, \quad \mathbf{v}'_t = W_\mathrm{out} \mathbf{z}'_t
83	\end{equation}
84	
85	\paragraph{Refinement loss.} The model is trained to directly produce collision-corrected actions by minimizing the discrepancy between original and refined predictions on near-collision samples, summed over all $H$ action timesteps:
86	\begin{equation}\label{eq:loss_refine}
87	\mathcal{L}_\mathrm{refine} = \frac{1}{|\mathcal{S}|} \sum_{i \in \mathcal{S}} \sum_{t=1}^{H} \|\mathbf{v}_{t,i} - \mathrm{sg}(\mathbf{v}'_{t,i})\|_2^2
88	\end{equation}
89	where $\mathrm{sg}(\cdot)$ is the stop-gradient operator and the outer sum runs over batch samples in the collision set $\mathcal{S}$. The loss averages over samples but sums over timesteps, so the per-sample refinement signal scales with the trajectory length $H$; this ensures that the gradient magnitude is proportional to the cumulative deviation across the full action horizon rather than the per-step average, which we found empirically more effective for learning coherent trajectory-level corrections. The gradient flows only through $\mathbf{v}_t \to \mathbf{z} \to \theta_\mathrm{LoRA}$, training the LoRA adapters to anticipate and avoid collisions. The refined target $\mathbf{v}'_t$ is detached and serves as a teacher signal that encodes collision-aware behavior. Because the student (the LoRA-adapted VLA) learns to replicate the refined actions directly, the SDF gradient computation is not required at inference time; the collision-avoidance capability is absorbed into the model parameters during training.
90	
91	\subsection{Training Protocol}\label{sec:training}
92	
93	We adopt a two-phase training protocol that ensures SDF prediction accuracy before engaging gradient-guided refinement.
94	
95	\paragraph{Phase 1: Auxiliary module warmup ($0 \to 5\mathrm{K}$ steps).} The entire backbone, including LoRA parameters, is frozen. Only the SDF decoder (${\sim}$395K params) and EE extractor (${\sim}$263K params) are trained on detached features ($\bar{\mathbf{z}}.\mathrm{detach}()$) to avoid destabilizing the pretrained backbone. This phase establishes an accurate SDF predictor anchored to the backbone's current feature distribution.
96	
97	\paragraph{Phase 2: Joint training ($5\mathrm{K} \to 30\mathrm{K}$ steps).} LoRA parameters are unfrozen with a linear gradient warmup over 100 steps. We consider three training variants that differ only in their loss composition:
98	
99	\textit{$\pi_0$-LoRA} (baseline): Standard LoRA fine-tuning with flow-matching action loss only:
100	\begin{equation}
101	\mathcal{L}_{\pi_0\text{-LoRA}} = \mathcal{L}_\mathrm{action}
102	\end{equation}
103	
104	\textit{ColliForce-Aux}: Adds SDF and EE auxiliary losses without gradient-guided refinement:
105	\begin{equation}\label{eq:loss_aux}
106	\mathcal{L}_\mathrm{Aux} = \mathcal{L}_\mathrm{action} + \lambda_\mathrm{SDF} \cdot \mathcal{L}_\mathrm{SDF} + \lambda_\mathrm{EE} \cdot \mathcal{L}_\mathrm{EE}
107	\end{equation}
108	with $\lambda_\mathrm{SDF} = 0.1$ and $\lambda_\mathrm{EE} = 0.01$. Gradients flow from the auxiliary losses through the pooled features into the LoRA adapters, encouraging the action expert to develop features that encode workspace geometry.
109	
110	\textit{ColliForce} (full method): Extends ColliForce-Aux with the gradient-guided refinement loss:
111	\begin{equation}\label{eq:loss_full}
112	\mathcal{L}_\mathrm{ColliForce} = \mathcal{L}_\mathrm{action} + \lambda_\mathrm{SDF} \cdot \mathcal{L}_\mathrm{SDF} + \lambda_\mathrm{EE} \cdot \mathcal{L}_\mathrm{EE} + \lambda_\mathrm{refine} \cdot \mathcal{L}_\mathrm{refine}
113	\end{equation}
114	with $\lambda_\mathrm{refine} = 0.1$. The refinement loss is computed only when near-collision samples exist in the batch ($|\mathcal{S}| > 0$), adding zero overhead for collision-free steps.
115	
116	\paragraph{LoRA configuration.} Adapters are injected into both the PaliGemma encoder (rank 16, $\alpha = 16$) and the action expert (rank 32, $\alpha = 32$), targeting attention projections ($W_q, W_k, W_v, W_o$) and MLP layers ($W_\mathrm{gate}, W_\mathrm{up}, W_\mathrm{down}$). The total trainable LoRA parameter count is ${\sim}$33.5M. All variants use AdamW optimizer with cosine learning rate decay from $2.5 \times 10^{-5}$ to $2.5 \times 10^{-6}$, batch size 32, and train for 30K steps total.
117	
118	\subsection{Inference}\label{sec:inference}
119	
120	At inference, only the base model with trained LoRA adapters is active. The standard forward pass generates actions through iterative flow-matching denoising; neither the auxiliary modules nor gradient computation is required. The LoRA parameters have internalized collision avoidance behavior during training, producing trajectories that maintain clearance from obstacles without additional computation.
121	
122	For deployment scenarios with out-of-distribution obstacle configurations, ColliForce-VLA supports an optional workspace-frame SDF gradient correction as a complementary safety net. If the predicted SDF at the next EE position falls below the safety margin ($\hat{\Phi}(\hat{\mathbf{p}}_\mathrm{next}) < m$), the position component of the action is corrected:
123	\begin{equation}\label{eq:inference_correction}
124	a'_t[:3] = a_t[:3] + \alpha \cdot \frac{\nabla_{\mathbf{x}} \hat{\Phi}(\hat{\mathbf{p}}_\mathrm{next})}{\|\nabla_{\mathbf{x}} \hat{\Phi}(\hat{\mathbf{p}}_\mathrm{next})\|_2}
125	\end{equation}
126	The L2-normalization bounds correction magnitude to $\alpha$ regardless of gradient scale. This mechanism introduces zero additional latency when $\hat{\Phi} \geq m$ and serves primarily as a safety net; the ColliForce-trained model has already learned to avoid collisions and rarely triggers inference-time correction.
127	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "948058cc-cacd-4ab0-b1b7-d9ece821ffbc"
}
```

</details>

---

### System

_source line 69_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/drafts/related_work.tex",
  "usage": {
    "total_tokens": 29914,
    "tool_uses": 17,
    "duration_ms": 21823
  },
  "last_tool_name": "Read",
  "uuid": "48ef50e1-9727-4ce8-936d-52055e172ad5",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — Read · `toolu_01Ebb7aTiovEUEgzk7RAA1id`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/drafts/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "efda596d-fff0-453b-886e-2d791f44c0b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xkDDnWFDFk2PUsyEp4DQ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12226,
      "cache_read_input_tokens": 17637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12226,
        "ephemeral_1h_input_tokens": 0
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

_source line 71 · 2026-05-27T13:13:01.431Z_

<details><summary>↩ Tool result · `toolu_01Ebb7aTiovEUEgzk7RAA1id`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\subsection{3D-Aware Vision-Language-Action Models}
4	
5	A growing body of work integrates 3D spatial information into VLA architectures to improve manipulation performance. DepthVLA~\cite{depthvla2025} and QDepth-VLA~\cite{li2025qdepth} augment VLA training with depth prediction as an auxiliary objective, while Spatial Forcing~\cite{li2025spatialforcing} enforces implicit 3D alignment through spatial consistency constraints on the learned representations. Several methods go further by incorporating explicit 3D structure: 3D-CAVLA~\cite{3dcavla2025} and GeoAware-VLA~\cite{geoaware2025} condition action generation on geometric features, SpatialVLA~\cite{spatialvla2025} encodes spatial affordance maps, and GST-VLA~\cite{gstvla2026}, StemVLA~\cite{stemvla2026}, and ST-VLA~\cite{stvla2026} fuse spatiotemporal representations from multi-view or sequential observations. Evo-0~\cite{evo02025}, SA-VLA~\cite{savla2026}, AugVLA-3D~\cite{augvla3d2026}, and Evo-Depth~\cite{evodepth2026} further confirm that 3D-aware features improve task success rate, viewpoint generalization, and grasping precision.
6	
7	Among these, QDepth-VLA~\cite{li2025qdepth} is the closest methodological precedent for auxiliary spatial supervision in VLAs. Three distinctions separate it from our approach. First, QDepth-VLA predicts 2.5D camera-frame depth, which encodes per-pixel distance to the camera sensor; ColliForce-VLA predicts workspace-frame SDF, which encodes signed distance to the nearest obstacle surface at arbitrary 3D points. Second, QDepth-VLA's VQ-VAE decoder is architecturally decoupled from the action head: depth gradients flow into the backbone during training but do not explicitly modify the action token generation pathway. In contrast, our SDF gradient refinement directly modulates the feature representations from which action tokens are decoded. Third, camera-frame depth provides no signal in occluded regions (behind the robot arm or other objects), whereas workspace SDF covers the full 3D volume including occluded space. Spatial Forcing~\cite{li2025spatialforcing} demonstrates that implicit 3D alignment within the VLA can improve manipulation, yet it does not produce an occupancy or distance field and therefore cannot provide collision-specific directional guidance.
8	
9	Despite these advances, no 3D-aware VLA targets collision avoidance as a design objective, and none evaluates on collision-specific metrics. ColliForce-VLA bridges this gap by using workspace SDF explicitly for collision-aware action generation.
10	
11	\subsection{Collision-Safe Robot Policies}
12	
13	Recent methods address collision safety in learned manipulation policies through two strategies: post-hoc correction and constrained optimization. AEGIS~\cite{hu2025vlsa} exemplifies the post-hoc approach by applying Control Barrier Function (CBF) corrections to VLA-generated actions, using open-set detection and monocular depth estimation to identify obstacles at test time. CoFreeVLA~\cite{cofreeevla2026} trains a risk estimator that halts execution when predicted collision probability exceeds a threshold in dual-arm settings. Li et al.~\cite{li2024langguided} train a language-guided object-centric diffusion policy on 3D point clouds and inject collision avoidance at inference through cost-guided denoising, a training-free mechanism that steers trajectories away from obstacles without modifying the learned policy. CAPE~\cite{yang2025cape} extends this direction by expanding the trajectory distribution through context-aware priors and prior-seeded iterative guided refinement. iKinQP-RL~\cite{spalter2024ikinqp} applies inverse-kinematics quadratic programming to correct RL policy actions at runtime, eliminating collisions with unseen obstacles through a separate optimization layer. On the constrained optimization side, SafeVLA~\cite{zhang2025safevla} formulates safety as a Constrained Markov Decision Process and reduces violations through reward shaping during reinforcement learning.
14	
15	These approaches share a common architectural pattern: the safety mechanism operates independently of the VLA's learned feature representations. The model generates actions without collision awareness, and a separate module evaluates or corrects them post-hoc, or a separate reward signal implicitly penalizes unsafe behavior without encoding geometric structure. ColliForce-VLA departs from this paradigm by internalizing collision geometry into the VLA's own parameters. The SDF gradient refinement during training steers the action expert's feature space toward collision-free configurations, so that the model encodes collision awareness at the point of action generation rather than relying on external correction.
16	
17	\subsection{Signed Distance Fields in Robotics}
18	
19	Signed Distance Fields provide a continuous implicit representation of geometry where each point encodes its signed distance to the nearest surface. DeepSDF~\cite{park2019deepsdf} established neural network-based SDF prediction as a compact shape representation, and iSDF~\cite{ortiz2022isdf} extended this to incremental scene reconstruction from posed depth images for real-time robot perception. In the manipulation domain, VoxPoser~\cite{huang2023voxposer} composes 3D value maps (including avoidance maps) from language model outputs to guide robotic manipulation planning, demonstrating that volumetric spatial representations can effectively encode obstacle information for action generation. DiffCo~\cite{zhi2021diffco} introduced differentiable collision checking based on learned distance fields, enabling gradient-based trajectory optimization through collision constraints. RAMP~\cite{vasilopoulos2023ramp} and CSSDF-Net~\cite{chen2026cssdfnet} use SDF representations for hierarchical reactive motion planning and configuration-space trajectory optimization, respectively. Jacquet et al.~\cite{jacquet2025neuralnmpc} integrate SDF constraints into nonlinear model predictive control for mapless collision-free navigation. SAMP~\cite{chen2025samp} and Prof.\ Robot~\cite{ruan2025profrobot} incorporate differentiable distance fields into learned policies: SAMP fuses robot and environment SDFs on a shared spatial grid for collision-aware motion planning, achieving a 7\% collision reduction, while Prof.\ Robot uses Eikonal-regularized collision classifiers for collision-free action optimization in differentiable rendering.
20	
21	Two observations motivate our design. First, the effectiveness of SDF for collision detection in classical planning is well established, and DiffCo~\cite{zhi2021diffco} specifically demonstrates that differentiable SDF enables gradient-based collision avoidance. Second, existing SDF-based policy methods~\cite{chen2025samp,ruan2025profrobot} operate in non-VLA settings and do not handle language-conditioned manipulation. No prior work has integrated a differentiable SDF into a VLA's forward pass, connecting the proven collision-detection capability of distance fields with the generalization capacity of large-scale vision-language-action models.
22	
23	\subsection{Action Refinement in Generative Policies}
24	
25	DFM-VLA~\cite{chen2026dfmvla} demonstrates that iterative action refinement within the VLA architecture can improve action quality by denoising predicted trajectories through multiple refinement steps. This validates the feasibility of in-model refinement but lacks a collision-specific guidance signal; the refinement is driven by a general denoising objective rather than geometric constraints. ColliForce-VLA's SDF gradient refinement provides a collision-specific instantiation of this principle: the refinement direction is determined by the SDF gradient in feature space ($\nabla_z \hat{\Phi}$), which explicitly encodes the direction of increasing distance from obstacle surfaces.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "b7a455eb-cbcd-434e-9694-249adf0a98c1"
}
```

</details>

---

### System

_source line 72_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/drafts/analysis_claim1.tex",
  "usage": {
    "total_tokens": 45008,
    "tool_uses": 18,
    "duration_ms": 26793
  },
  "last_tool_name": "Read",
  "uuid": "a8450d31-9dc8-4ec3-a352-8d8a3a4102c3",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 73_

<details open><summary>🔧 Tool call — Read · `toolu_011MC2cqLQetr7rdqyVBWCcu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/drafts/analysis_claim1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "3718fdf1-9d4b-46d0-95cc-13ee4dd28948",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ko9VYDCQ53jdiENN3WnAc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15092,
      "cache_read_input_tokens": 29863,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15092,
        "ephemeral_1h_input_tokens": 0
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

_source line 74 · 2026-05-27T13:13:06.399Z_

<details><summary>↩ Tool result · `toolu_011MC2cqLQetr7rdqyVBWCcu`</summary>

```text
1	\subsection{The Fake Safety Problem}\label{sec:fake_safety}
2	
3	At first glance, the collision avoidance results for SDF-augmented VLA models appear compelling. Our A1-LoRA model (Pi0 fine-tuned with an SDF auxiliary loss) achieves a Collision Avoidance Rate (CAR) of 91.5\% across 800 evaluation episodes on the SafeLIBERO benchmark~\cite{hu2025vlsa}, a figure that would suggest reliable obstacle avoidance. Yet this headline metric conceals a fundamental problem. When we examine the end-effector displacement of the 732 episodes classified as ``safe,'' the picture changes entirely: 541 episodes (73.9\%) exhibit a maximum displacement below 1\,$\mu$m, and another 188 episodes (25.7\%) remain below 0.1\,mm. Only 3 episodes (0.4\%) show displacement above the 0.1\,mm threshold, the minimum we consider consistent with intentional motion. The remaining 99.6\% of safe episodes are artifacts of a robot that never moved.
4	
5	We define a safe episode as \emph{fake safe} when the maximum end-effector displacement stays below a threshold $\tau_d = 0.1$\,mm. Under this criterion, 729 of the 732 safe episodes produced by A1-LoRA are fake safe. The robot did not avoid obstacles; it avoided motion altogether. The displacement distribution, shown in Figure~\ref{fig:displacement}, clusters overwhelmingly near zero, with no meaningful spread toward the range that would indicate planned trajectories around obstacles. Table~\ref{tab:fake_safety} summarizes the fake safety statistics across all evaluated methods.
6	
7	\begin{table}[t]
8	\centering
9	\caption{Fake safety decomposition across methods on SafeLIBERO. CAR$_\text{f}$ excludes episodes with max displacement $< \tau_d = 0.1$\,mm. Fake safe rate is computed over safe (non-collision) episodes only.}
10	\label{tab:fake_safety}
11	\vspace{2pt}
12	\small
13	\begin{tabular}{lccccc}
14	\toprule
15	Method & CAR (\%) & TSR (\%) & Fake Safe (\%) & Real Safe & CAR$_\text{f}$ (\%) \\
16	\midrule
17	A1-LoRA (SDF) & 91.5 & 0.0 & 99.6 & 3 / 732 & ---$^\dagger$ \\
18	LoRA baseline  & 82.0 & 0.0 & 99.4 & $\approx$\,1 / 164 & $\approx$\,0 \\
19	Pi0.5 (3-seed) & 26.8\,$\pm$\,1.6 & 74.7\,$\pm$\,1.5 & 98.2 & 1 / 56 & $\approx$\,0 \\
20	\bottomrule
21	\end{tabular}
22	\vspace{2pt}
23	{\footnotesize $^\dagger$ Denominator $< 5$; statistically unreliable.}
24	\end{table}
25	
26	This phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\% with a Task Success Rate (TSR) of 0\%. Among its 164 safe episodes, 99.4\% are fake safe by the same displacement criterion. The pattern persists even in Pi0.5, a larger, more capable model from the same family (2.5B$\to$3.5B parameters, extended training data). Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\,$\pm$\,1.6\% and a TSR of 74.7\,$\pm$\,1.5\%. Its lower CAR reflects the fact that Pi0.5 actually moves the robot, which naturally increases collision frequency. Yet among its safe episodes, the fake safe rate remains 98.2\% (55 of 56 safe episodes in seed 0 show near-zero displacement). The conclusion is consistent across methods: when a Pi0-family model does not collide, it is almost certainly because it did not move.
27	
28	These observations motivate a corrected metric. We define the \emph{displacement-filtered CAR} (CAR$_\text{f}$) as the fraction of safe episodes among only those episodes where the robot exhibits meaningful motion (max displacement $\geq \tau_d$). Formally:
29	\begin{equation}
30	\text{CAR}_\text{f} = \frac{|\{e : \text{safe}(e) \land d_{\max}(e) \geq \tau_d\}|}{|\{e : d_{\max}(e) \geq \tau_d\}|}
31	\end{equation}
32	where $d_{\max}(e)$ denotes the maximum end-effector displacement in episode $e$. We provide a sensitivity analysis over $\tau_d \in \{0.01, 0.1, 1, 10\}$\,mm in Appendix~\ref{app:threshold_sensitivity}, showing that conclusions are robust to threshold choice. For A1-LoRA, only 3 of 800 episodes exceed the displacement threshold, all 3 of which happen to be safe, but the denominator is too small to constitute a meaningful rate. For the LoRA baseline and Pi0.5, CAR$_\text{f}$ is similarly near zero. The gap between raw CAR and CAR$_\text{f}$ exposes the scale of contamination: a model can report over 90\% CAR while possessing essentially no collision avoidance capability.
33	
34	The practical implication is stark. Standard CAR evaluation conflates two behaviors that differ in every meaningful respect: a robot that plans a safe trajectory around an obstacle, and a robot that has collapsed into inaction due to distributional shift. Without displacement filtering, any model suffering from action collapse will receive inflated safety scores, and models that collapse more severely will paradoxically appear safer. This inversion renders CAR, as conventionally computed, unreliable for evaluating collision avoidance in VLA models.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "9db4f01c-e09c-4d33-9efa-97da9cf36170"
}
```

</details>

---

### System

_source line 75_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/drafts/analysis_claim2.tex",
  "usage": {
    "total_tokens": 45009,
    "tool_uses": 19,
    "duration_ms": 27253
  },
  "last_tool_name": "Read",
  "uuid": "fbfecd95-1c60-4667-ab0b-35b6a1b6ccf0",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — Read · `toolu_01TyF9BwBYWQxNFiRDrhLWkY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/drafts/analysis_claim2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "73e07c02-e6b9-4420-99b6-59135215e583",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ko9VYDCQ53jdiENN3WnAc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15092,
      "cache_read_input_tokens": 29863,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15092,
        "ephemeral_1h_input_tokens": 0
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

_source line 77 · 2026-05-27T13:13:06.859Z_

<details><summary>↩ Tool result · `toolu_01TyF9BwBYWQxNFiRDrhLWkY`</summary>

```text
1	\subsection{Capability-Safety Anti-correlation}\label{sec:tsr_car}
2	
3	The displacement analysis in Section~\ref{sec:fake_safety} reveals a striking pattern at the aggregate level: models with higher task capability systematically report lower collision avoidance rates. Pi0.5 achieves a TSR of 74.7\,$\pm$\,1.5\% but a CAR of only 26.8\,$\pm$\,1.6\%, while Pi0-based methods (LoRA baseline, Full-FT, and A1-LoRA) report TSR $\leq$ 0.5\% alongside CAR values of 82--91.5\%. The anti-correlation is consistent across all three Pi0.5 seeds (TSR 73--76\%, CAR 25--28\%) and across Pi0 variants regardless of whether an SDF loss is applied. We observe that models capable of executing tasks also move the robot into configurations where collisions become possible, while models that fail to act avoid collisions by default.
4	
5	Figure~\ref{fig:tsr_car_scatter} plots all evaluated configurations in TSR-CAR space. Two clusters emerge. Pi0-family methods occupy the upper-left region: high CAR, near-zero TSR. As established in Section~\ref{sec:fake_safety}, over 99\% of their safe episodes are fake safe, placing this cluster in what we term the \emph{fake safety zone}. Pi0.5, by contrast, sits in the lower-right region: high TSR, low CAR. Its collisions reflect genuine robot motion through the workspace. The two clusters are separated by a gap that no existing method occupies, a region that would require both meaningful task execution and reliable obstacle avoidance.
6	
7	This spatial structure has a direct implication for metric interpretation. A model that reports high CAR but near-zero TSR provides no evidence of collision avoidance capability; its safety score is an artifact of inaction. CAR is informative only when conditioned on sufficient task capability. We note that the TSR-CAR plane offers a more complete picture than either metric alone: the upper-right quadrant (high TSR, high CAR) represents genuinely safe and capable behavior, while the upper-left quadrant is accessible through action collapse without any safety mechanism.
8	
9	Early results from a Pi0.5 model augmented with A1-level SDF training (10K-step checkpoint) suggest that this gap is not inherent. This configuration achieves TSR of 47--49\% with CAR of 56--58\% and a frozen-action rate of 0\%, placing it in the previously unoccupied central region of Figure~\ref{fig:tsr_car_scatter}. We defer detailed analysis of this model to Section~\ref{sec:a1_pi05}, but note here that its position confirms the trade-off is a property of current models, not a fundamental constraint. Genuine collision avoidance requires a model that both moves and avoids, a combination that raw CAR cannot distinguish from one that simply does not move.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "24c7787a-9d04-47fd-be6c-65bf216cac13"
}
```

</details>

---

### System

_source line 78_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/drafts/analysis_claim3.tex",
  "usage": {
    "total_tokens": 45010,
    "tool_uses": 20,
    "duration_ms": 27632
  },
  "last_tool_name": "Read",
  "uuid": "9c69bb75-f35f-4cb5-a183-cfda3bc2c51f",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 79_

<details open><summary>🔧 Tool call — Read · `toolu_01HpMnycwwuVfB5Cuyz6Qfm7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/drafts/analysis_claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "b33ee21f-cab2-48b1-8ef9-adadfcd074bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ko9VYDCQ53jdiENN3WnAc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15092,
      "cache_read_input_tokens": 29863,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15092,
        "ephemeral_1h_input_tokens": 0
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

_source line 80 · 2026-05-27T13:13:07.238Z_

<details><summary>↩ Tool result · `toolu_01HpMnycwwuVfB5Cuyz6Qfm7`</summary>

```text
1	\subsection{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\label{sec:ee_only}
2	
3	The analyses in Sections~\ref{sec:fake_safety} and~\ref{sec:tsr_car} identify action collapse and fake safety as pervasive problems, but leave open a natural question: could a sufficiently accurate SDF prediction still enable effective runtime refinement? To isolate the SDF representation itself from prediction quality, we construct an oracle experiment. We replace the learned SDF network with the ground-truth signed distance field computed directly from the known obstacle geometry. This oracle represents the theoretical upper bound of end-effector-only SDF refinement: it eliminates prediction error entirely, providing the refinement module with a perfect distance signal at every timestep. If the SDF refinement paradigm is sound, oracle performance should exceed that of unrefined baselines by a wide margin.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Oracle SDF refinement with ground-truth distance fields (160 episodes, 4 tasks $\times$ 40). All three variants achieve lower CAR than unrefined baselines (LoRA 82.0\%, Full-FT 83.0\%), and fake safe rates remain above 96\%.}
8	\label{tab:oracle}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lcccc}
12	\toprule
13	Method & TSR (\%) & CAR (\%) & Fake Safe (\%) & Refines/ep \\
14	\midrule
15	LoRA baseline (no refine) & 0.0 & 82.0 & 99.4 & -- \\
16	Full-FT baseline (no refine) & 0.5 & 83.0 & -- & -- \\
17	\midrule
18	Oracle-adaptive (GT, dyn.\ $\alpha$) & 0.0 & 75.0 & 98.3 & 14.2 \\
19	Oracle-fixed (GT, $\alpha{=}0.005$) & 0.0 & 73.1 & 98.3 & 14.8 \\
20	Oracle-feature (GT, feat.\ space) & 0.0 & 76.9 & 96.7 & 241.7 \\
21	\midrule
22	A3 learned SDF & 0.0 & 74.5 & -- & 0.0 \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	Table~\ref{tab:oracle} reports the results. All three oracle variants achieve CAR below that of the unrefined baselines. The best oracle (Oracle-feature, 76.9\%) falls 5.1 percentage points below the LoRA baseline (82.0\%) and 6.1 points below Full-FT (83.0\%). The adaptive and fixed-step variants perform worse still, at 75.0\% and 73.1\% respectively. These results are not marginal: the refinement module with perfect distance information produces more collisions than doing nothing at all. The fake safe rate tells a complementary story. Oracle-adaptive and Oracle-fixed both register 98.3\% fake safe episodes (118 of 120 and 115 of 117 safe episodes, respectively), while Oracle-feature registers 96.7\% (119 of 123). Ground-truth SDF refinement does not reduce action collapse; the vast majority of safe episodes remain attributable to inaction rather than obstacle avoidance.
28	
29	The per-task breakdown in Figure~\ref{fig:oracle_bar} reveals additional structure. On task~1, the most collision-prone task where the LoRA baseline achieves only 46.0\% CAR, Oracle-adaptive reaches 55.0\% and Oracle-feature reaches 47.5\%, a modest improvement consistent with a scenario where the end-effector is the primary collision body. On tasks~0, 2, and~3, all oracle variants produce lower CAR than the baseline: Oracle-adaptive drops from 96.0\% to 82.5\% on task~0 and from 98.0\% to 77.5\% on task~2. The refinement gradient, which pushes the end-effector away from the obstacle surface, perturbs the planned trajectory in ways that increase collisions elsewhere on the robot arm.
30	
31	This failure mode is structural. The SDF refinement paradigm as formulated in prior work~\cite{hu2025vlsa} computes the signed distance from the end-effector to the nearest obstacle surface and applies a gradient step to increase this distance when it falls below a safety threshold. The gradient operates exclusively on the end-effector position; no distance constraint applies to the remaining links of the robot arm. When the gradient pushes the end-effector away from an obstacle, the resulting joint-space displacement can rotate intermediate links toward or through the obstacle volume. The refinement thus trades one collision for another, with no mechanism to detect or prevent the substitution. The feature-space oracle makes this coupling problem explicit. It applies the SDF gradient in the policy's latent action space rather than in Cartesian coordinates, and fires on nearly every timestep (241.7 refinements per episode versus 14.2 for action-space variants). Yet its gradient magnitudes are extremely small (0.004--0.006, compared to 0.18--0.49 in action space), and the resulting CAR (76.9\%) shows no significant advantage over the action-space oracles. The latent space lacks a direct geometric relationship to full-body configuration; small perturbations in feature space do not reliably translate into collision-free joint trajectories.
32	
33	The A3 model with a learned SDF head illustrates the complementary failure. In this configuration, the SDF prediction network never outputs a distance below the refinement threshold across any of the 160 evaluation episodes, resulting in zero refinement steps. The learned SDF has calibrated its predictions to avoid triggering the safety mechanism, effectively reducing the model to an unrefined baseline (CAR of 74.5\%, consistent with the oracle range). The refinement module, even if it could improve safety, is never activated.
34	
35	These results establish that end-effector-only SDF is a structural limitation, not merely an engineering gap. Perfect distance information does not compensate for the absence of full-body collision awareness. Any refinement scheme that monitors only the end-effector position will remain blind to arm-body collisions, which constitute the dominant failure mode in manipulation tasks where the robot must reach around or past obstacles. Effective collision avoidance for VLA models will require representations that account for the geometric extent of the entire manipulator, not only its tip.
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "897ad6df-bc7c-409d-8527-8e4dc338c999"
}
```

</details>

---

### System

_source line 81_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/drafts/experimental_framework.tex",
  "usage": {
    "total_tokens": 45011,
    "tool_uses": 21,
    "duration_ms": 28104
  },
  "last_tool_name": "Read",
  "uuid": "97777b52-231b-4400-b94a-dceb7cd74d48",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 82_

<details open><summary>🔧 Tool call — Read · `toolu_01HCfaBkE5GCub35Joa9Mhi2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/drafts/experimental_framework.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "a2e8766b-3645-4d55-8cd2-a1d10c82dc84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ko9VYDCQ53jdiENN3WnAc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15092,
      "cache_read_input_tokens": 29863,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15092,
        "ephemeral_1h_input_tokens": 0
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

_source line 83 · 2026-05-27T13:13:07.709Z_

<details><summary>↩ Tool result · `toolu_01HCfaBkE5GCub35Joa9Mhi2`</summary>

```text
1	\section{Experimental Framework}\label{sec:framework}
2	
3	This section defines the evaluation platform, metrics, and model configurations that underpin the analyses in Sections~\ref{sec:fake_safety}--\ref{sec:a1_pi05}. Our primary methodological contribution is the displacement-filtered Collision Avoidance Rate (CAR$_\text{f}$), which separates genuine avoidance from action collapse.
4	
5	\subsection{Benchmark and Evaluation Protocol}\label{sec:benchmark}
6	
7	We conduct all experiments on SafeLIBERO~\cite{hu2025vlsa}, a collision-aware evaluation extension of the LIBERO simulation platform~\cite{liu2023libero}. SafeLIBERO augments standard manipulation benchmarks with per-timestep collision detection and non-target obstacle annotations, enabling systematic measurement of both task completion and safety.
8	
9	We select the \textit{object\_pudding} Level~I suite, which comprises four tabletop manipulation tasks. In each task, a target object is surrounded by non-target obstacles that the robot must avoid during grasping and transport. The MuJoCo physics engine provides collision detection: any contact between the robot (end-effector or arm links) and a non-target object registers as a collision event.
10	
11	Each method is evaluated for 50 episodes per task (200 episodes total). For multi-seed experiments (Pi0.5), we run 3 seeds to produce 600 episodes per configuration. Initial object configurations are fixed across methods to ensure fair comparison.
12	
13	\subsection{Evaluation Metrics}\label{sec:metrics}
14	
15	\paragraph{Standard metrics.} We report two conventional metrics. The \emph{Task Success Rate} (TSR) is the fraction of episodes where the manipulation task reaches completion. The \emph{Collision Avoidance Rate} (CAR) is the fraction of episodes in which no collision occurs between the robot and any non-target object.
16	
17	\paragraph{Displacement-filtered CAR.} Standard CAR conflates two qualitatively distinct behaviors: a robot that plans a trajectory around obstacles, and a robot that has collapsed into inaction. Both register as ``safe,'' yet only the former reflects collision avoidance capability. We propose the displacement-filtered CAR (CAR$_\text{f}$), which excludes episodes exhibiting action collapse from both numerator and denominator.
18	
19	We define an episode $e$ as \emph{action-collapsed} when its maximum end-effector displacement satisfies $d_{\max}(e) < \tau_d$, where $\tau_d = 0.1$\,mm. The filtered metric is then:
20	\begin{equation}\label{eq:car_f}
21	\text{CAR}_\text{f} = \frac{|\{e : \text{safe}(e) \;\land\; d_{\max}(e) \geq \tau_d\}|}{|\{e : d_{\max}(e) \geq \tau_d\}|}
22	\end{equation}
23	where $d_{\max}(e)$ denotes the maximum Euclidean displacement of the end-effector across all timesteps in episode $e$. The threshold $\tau_d = 0.1$\,mm corresponds to sub-actuator-resolution motion and is robust to perturbation (Appendix~\ref{app:threshold_sensitivity}).
24	
25	\paragraph{Auxiliary metrics.} We additionally report the \emph{Frozen Rate}, the fraction of episodes with $d_{\max} < \tau_d$, which quantifies the severity of action collapse for each method. The \emph{Simultaneous Success Rate} (SSR $= $ TSR $\cap$ CAR) measures the fraction of episodes that achieve both task completion and collision avoidance.
26	
27	\subsection{Models and Training}\label{sec:models}
28	
29	\paragraph{Base architectures.} We evaluate two VLA models from the Pi0 family~\cite{black2024pi0}. \textbf{Pi0} (${\sim}$3B parameters) uses a PaliGemma vision-language encoder paired with a dedicated action expert that generates continuous actions via flow matching~\cite{lipman2023flow}. \textbf{Pi0.5} extends this architecture to ${\sim}$3.5B parameters with broader pre-training data, and serves as a stronger baseline that exhibits less action collapse.
30	
31	\paragraph{Training configurations.} We evaluate four model variants:
32	\begin{itemize}
33	\item \textit{Full-FT baseline}: Pi0 with all parameters fine-tuned on SafeLIBERO demonstrations using the flow-matching action loss.
34	\item \textit{LoRA baseline}: Pi0 with LoRA adapters (${\sim}$33.5M trainable parameters), same demonstrations and loss.
35	\item \textit{A1-LoRA}: Pi0 + LoRA augmented with two auxiliary heads. An SDF Decoder (4-layer MLP, ${\sim}$395K parameters) predicts the signed distance from the end-effector to the nearest obstacle surface, supervised with a clamped $L_1$ loss and an Eikonal regularizer ($\mathcal{L}_\text{SDF}$). An EE Extractor (2-layer MLP, ${\sim}$263K parameters) predicts end-effector position from action expert features ($\mathcal{L}_\text{EE}$, MSE loss). SDF ground truth is computed from known obstacle meshes in simulation.
36	\item \textit{Pi0.5 + A1}: The A1 architecture applied to the Pi0.5 backbone. Training proceeds in two phases: Phase~1 (steps 0--5K) trains only the auxiliary heads on detached features with the backbone frozen; Phase~2 (steps 5K--30K) unfreezes LoRA parameters for joint optimization. We evaluate $\lambda_\text{SDF} \in \{0.005, 0.01\}$.
37	\end{itemize}
38	
39	\subsection{Oracle SDF Refinement}\label{sec:oracle_setup}
40	
41	To test the theoretical upper bound of end-effector-only SDF refinement (analyzed in Section~\ref{sec:ee_only}), we replace the learned SDF network with the ground-truth signed distance field computed from simulation geometry. This eliminates prediction error and isolates the structural limitation of the refinement paradigm itself.
42	
43	We evaluate three oracle variants that differ in how the SDF gradient is applied:
44	\begin{itemize}
45	\item \textit{Oracle-adaptive}: runtime gradient refinement with a dynamic step size $\alpha$ that scales inversely with gradient magnitude.
46	\item \textit{Oracle-fixed}: a constant step size $\alpha = 0.005$.
47	\item \textit{Oracle-feature}: gradient applied in the VLA's latent feature space rather than Cartesian action space.
48	\end{itemize}
49	Each variant is evaluated for 160 episodes (4 tasks $\times$ 40 episodes) with a single seed.
50	
51	\subsection{SDF Ground Truth}\label{sec:sdf_gt}
52	
53	The workspace signed distance field is computed from the known obstacle meshes available in the LIBERO/MuJoCo simulation environment. SDF values are positive in free space, zero on the obstacle surface, and negative inside the obstacle volume. Ground-truth labels are generated at query points sampled along predicted end-effector trajectories during training.
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "1a6ae6d6-975e-4d51-8a18-fe38d9822da9"
}
```

</details>

---

### System

_source line 84_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/drafts/related_work_v2.tex",
  "usage": {
    "total_tokens": 45012,
    "tool_uses": 22,
    "duration_ms": 28895
  },
  "last_tool_name": "Read",
  "uuid": "a66c2530-d92c-4114-91d9-a63a6d636870",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 85_

<details open><summary>🔧 Tool call — Read · `toolu_01SqtGRyKuaYZjRmg1eje3pM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/drafts/related_work_v2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "ecdbeef9-7106-48ef-9a99-db98116765de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ko9VYDCQ53jdiENN3WnAc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15092,
      "cache_read_input_tokens": 29863,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15092,
        "ephemeral_1h_input_tokens": 0
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

_source line 86 · 2026-05-27T13:13:08.515Z_

<details><summary>↩ Tool result · `toolu_01SqtGRyKuaYZjRmg1eje3pM`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\subsection{Collision-Safe VLA Methods}\label{sec:rw_collision}
4	
5	Recent methods for collision avoidance in VLAs fall into three categories. \textbf{Post-hoc correction} approaches modify policy outputs before execution. AEGIS~\cite{hu2025vlsa} applies Control Barrier Function corrections to VLA actions based on open-set detection and monocular depth estimation, and reports 77.85\% CAR on SafeLIBERO without additional training. iKinQP-RL~\cite{spalter2024ikinqp} enforces collision constraints through inverse-kinematics quadratic programming at runtime. CoFreeVLA~\cite{cofreeevla2026}trains a risk estimator that halts dual-arm execution when predicted collision probability exceeds a threshold.
6	
7	\textbf{Constrained optimization} embeds safety into training. SafeVLA~\cite{zhang2025safevla}formulates collision avoidance as a Constrained MDP and reports an 83.58\% reduction in safety violations through reward shaping.
8	
9	\textbf{Inference-time guidance} steers the generative process toward safe trajectories without retraining. Li et al.~\cite{li2024langguided} train an object-centric diffusion policy on 3D point clouds and inject collision costs during denoising. CAPE~\cite{yang2025cape} expands the trajectory distribution through context-aware priors and iterative refinement.
10	
11	These methods differ in mechanism but share a common evaluation pattern: all report Collision Avoidance Rate as primary evidence of safety. None examine whether the measured CAR reflects genuine obstacle avoidance or conflates it with other behaviors. Our analysis (Section~\ref{sec:fake_safety}) reveals that this conflation is severe in the Pi0 family: 98--99\% of safe episodes are attributable to inaction rather than planned avoidance. We do not challenge the technical contributions of these methods; we identify a validity gap in the metric on which they rely, and propose a filtered variant (CAR$_\text{f}$) that separates genuine avoidance from frozen behavior.
12	
13	\subsection{Signed Distance Fields in Robot Manipulation}\label{sec:rw_sdf}
14	
15	Signed Distance Fields encode the distance from a query point to the nearest obstacle surface, where the sign indicates free space (positive) or penetration (negative). DeepSDF~\cite{park2019deepsdf} established neural SDF prediction as a compact shape representation. iSDF~\cite{ortiz2022isdf} extended this to incremental scene reconstruction for real-time robot perception. DiffCo~\cite{zhi2021diffco} introduced differentiable collision checking through learned distance fields and showed that gradient-based trajectory optimization can enforce collision constraints. VoxPoser~\cite{huang2023voxposer} composes 3D value maps from language model outputs for manipulation planning, with avoidance maps that encode obstacle information in volumetric form.
16	
17	SDF-based collision detection is well validated in classical motion planning. The natural question is whether this effectiveness transfers to VLA action refinement, where the SDF gradient modifies predicted end-effector actions to increase obstacle clearance. Our oracle experiments (Section~\ref{sec:ee_only}) test this directly by replacing the learned SDF network with ground-truth distance fields computed from simulation geometry, which eliminates all prediction error. The results reveal a structural limitation of end-effector-only refinement: all three oracle variants produce more collisions than unrefined baselines, because the gradient that repels the end-effector simultaneously rotates arm links into obstacle volumes. The problem is not SDF accuracy but application scope. Full-body collision avoidance requires distance information along the entire kinematic chain, not only at the tool tip.
18	
19	\subsection{Evaluation Reliability in Robot Learning}\label{sec:rw_eval}
20	
21	Concerns about whether standard metrics measure what they claim to measure have a long history in ML evaluation. Benchmark saturation and annotation artifact exploitation in NLP demonstrated that high scores can reflect dataset properties rather than target capabilities~\cite{gururangan2018annotation}. Goodhart's law (a measure ceases to be informative once it becomes an optimization target) has been documented in reinforcement learning settings where agents exploit reward proxies rather than solve intended tasks~\cite{karwowski2024goodhart}. These cases share a common structure: a metric that appears to measure capability $X$ in fact measures a confound $Y$, and the discrepancy remains invisible until the aggregate score is decomposed.
22	
23	The confound in VLA safety evaluation is action collapse, a phenomenon related to mode collapse in generative models. Diffusion-based robot policies can collapse to the mean of multi-modal action distributions~\cite{chi2023diffusionpolicy},
24	and VLAs trained on limited demonstration data exhibit similar failure modes that produce near-zero actions. Action collapse itself is well recognized. Its interaction with displacement-based safety metrics is not: a collapsed model registers as maximally safe because it generates no motion that could cause collisions. CAR cannot distinguish a model that plans a collision-free trajectory from a model that does nothing.
25	
26	All collision avoidance methods reviewed in Section~\ref{sec:rw_collision} adopt CAR without examining its construct validity. Our displacement-filtered variant, CAR$_\text{f}$ (Section~\ref{sec:metrics}), conditions safety measurement on sufficient motor activity and converts CAR from a contaminated aggregate into a metric that isolates genuine avoidance from inaction.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "b7c73f10-869c-4396-89db-925cd6b5cb5f"
}
```

</details>

---

### System

_source line 87_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/_project/paper/analysis_claim1.tex",
  "usage": {
    "total_tokens": 52775,
    "tool_uses": 23,
    "duration_ms": 34133
  },
  "last_tool_name": "Read",
  "uuid": "19bd4139-99d5-4fc2-9ef6-0aae561321ad",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 88_

<details open><summary>🔧 Tool call — Read · `toolu_01YBDbAYRGfrSxopyAqT3UNJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/analysis_claim1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "7ba13a40-805b-4645-ba92-b7f272c938f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011oSPodweqHsSnLHbTSH5F4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7761,
      "cache_read_input_tokens": 44955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7761,
        "ephemeral_1h_input_tokens": 0
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

_source line 89 · 2026-05-27T13:13:13.748Z_

<details><summary>↩ Tool result · `toolu_01YBDbAYRGfrSxopyAqT3UNJ`</summary>

```text
1	\subsection{The Fake Safety Problem}\label{sec:fake_safety}
2	
3	At first glance, the collision avoidance results for SDF-augmented VLA models appear compelling. Our A1-LoRA model (Pi0 fine-tuned with an SDF auxiliary loss) achieves a Collision Avoidance Rate (CAR) of 91.5\% across 800 evaluation episodes on the SafeLIBERO benchmark~\cite{hu2025vlsa}, a figure that would suggest reliable obstacle avoidance. Yet this headline metric conceals a fundamental problem. When we examine the end-effector displacement of the 732 episodes classified as ``safe,'' the picture changes entirely: 541 episodes (73.9\%) exhibit a maximum displacement below 1\,$\mu$m, and another 188 episodes (25.7\%) remain below 0.1\,mm. Only 3 episodes (0.4\%) show displacement above the 0.1\,mm threshold, the minimum we consider consistent with intentional motion. The remaining 99.6\% of safe episodes are artifacts of a robot that never moved.
4	
5	We define a safe episode as \emph{fake safe} when the maximum end-effector displacement stays below a threshold $\tau_d = 0.1$\,mm. Under this criterion, 729 of the 732 safe episodes produced by A1-LoRA are fake safe. The robot did not avoid obstacles; it avoided motion altogether. The displacement distribution, shown in Figure~\ref{fig:displacement}, clusters overwhelmingly near zero, with no meaningful spread toward the range that would indicate planned trajectories around obstacles. Table~\ref{tab:fake_safety} summarizes the fake safety statistics across all evaluated methods.
6	
7	\begin{table}[t]
8	\centering
9	\caption{Fake safety decomposition across methods on SafeLIBERO. CAR$_\text{f}$ excludes episodes with max displacement $< \tau_d = 0.1$\,mm. Fake safe rate is computed over safe (non-collision) episodes only.}
10	\label{tab:fake_safety}
11	\vspace{2pt}
12	\small
13	\begin{tabular}{lccccc}
14	\toprule
15	Method & CAR (\%) & TSR (\%) & Fake Safe (\%) & Real Safe & CAR$_\text{f}$ (\%) \\
16	\midrule
17	A1-LoRA (SDF) & 91.5 & 0.0 & 99.6 & 3 / 732 & $\approx$\,0 \\
18	LoRA baseline  & 82.0 & 0.0 & 99.4 & $\approx$\,1 / 164 & $\approx$\,0 \\
19	Pi0.5 (3-seed) & 26.8\,$\pm$\,1.6 & 74.7\,$\pm$\,1.5 & 98.2 & 1 / 56 & $\approx$\,0 \\
20	\bottomrule
21	\end{tabular}
22	\end{table}
23	
24	This phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\% with a Task Success Rate (TSR) of 0\%. Among its 164 safe episodes, 99.4\% are fake safe by the same displacement criterion. The pattern persists even in Pi0.5, a substantially different architecture. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\,$\pm$\,1.6\% and a TSR of 74.7\,$\pm$\,1.5\%. Its lower CAR reflects the fact that Pi0.5 actually moves the robot, which naturally increases collision frequency. Yet among its safe episodes, the fake safe rate remains 98.2\% (55 of 56 safe episodes in seed 0 show near-zero displacement). The conclusion is consistent across methods: when a Pi0-family model does not collide, it is almost certainly because it did not move.
25	
26	These observations motivate a corrected metric. We define the \emph{displacement-filtered CAR} (CAR$_\text{f}$) as the fraction of safe episodes among only those episodes where the robot exhibits meaningful motion (max displacement $\geq \tau_d$). Formally:
27	\begin{equation}
28	\text{CAR}_\text{f} = \frac{|\{e : \text{safe}(e) \land d_{\max}(e) \geq \tau_d\}|}{|\{e : d_{\max}(e) \geq \tau_d\}|}
29	\end{equation}
30	where $d_{\max}(e)$ denotes the maximum end-effector displacement in episode $e$. For A1-LoRA, only 3 of 800 episodes exceed the displacement threshold, all 3 of which happen to be safe, but the denominator is too small to constitute a meaningful rate. For the LoRA baseline and Pi0.5, CAR$_\text{f}$ is similarly near zero. The gap between raw CAR and CAR$_\text{f}$ exposes the scale of contamination: a model can report over 90\% CAR while possessing essentially no collision avoidance capability.
31	
32	The practical implication is stark. Standard CAR evaluation conflates two behaviors that differ in every meaningful respect: a robot that plans a safe trajectory around an obstacle, and a robot that has collapsed into inaction due to distributional shift. Without displacement filtering, any model suffering from action collapse will receive inflated safety scores, and models that collapse more severely will paradoxically appear safer. This inversion renders CAR, as conventionally computed, unreliable for evaluating collision avoidance in VLA models.
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "04ceae24-4be9-476c-8c2b-75f061d5c559"
}
```

</details>

---

### System

_source line 90_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/_project/paper/analysis_claim2.tex",
  "usage": {
    "total_tokens": 52776,
    "tool_uses": 24,
    "duration_ms": 34524
  },
  "last_tool_name": "Read",
  "uuid": "3840c0cb-5da8-4888-954e-30dfa1a308a7",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 91_

<details open><summary>🔧 Tool call — Read · `toolu_01R1rsiFREUVw9bCzGxZeoB9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/analysis_claim2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "d29acce4-9a05-41e3-b115-846d8fc1364a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011oSPodweqHsSnLHbTSH5F4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7761,
      "cache_read_input_tokens": 44955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7761,
        "ephemeral_1h_input_tokens": 0
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

_source line 92 · 2026-05-27T13:13:14.130Z_

<details><summary>↩ Tool result · `toolu_01R1rsiFREUVw9bCzGxZeoB9`</summary>

```text
1	\subsection{Capability-Safety Anti-correlation}\label{sec:tsr_car}
2	
3	The displacement analysis in Section~\ref{sec:fake_safety} reveals a striking pattern at the aggregate level: models with higher task capability systematically report lower collision avoidance rates. Pi0.5 achieves a TSR of 74.7\,$\pm$\,1.5\% but a CAR of only 26.8\,$\pm$\,1.6\%, while Pi0-based methods (LoRA baseline, Full-FT, and A1-LoRA) report TSR $\leq$ 0.5\% alongside CAR values of 82--91.5\%. The anti-correlation is consistent across all three Pi0.5 seeds (TSR 73--76\%, CAR 25--28\%) and across Pi0 variants regardless of whether an SDF loss is applied. We observe that models capable of executing tasks also move the robot into configurations where collisions become possible, while models that fail to act avoid collisions by default.
4	
5	Figure~\ref{fig:tsr_car_scatter} plots all evaluated configurations in TSR-CAR space. Two clusters emerge. Pi0-family methods occupy the upper-left region: high CAR, near-zero TSR. As established in Section~\ref{sec:fake_safety}, over 99\% of their safe episodes are fake safe, placing this cluster in what we term the \emph{fake safety zone}. Pi0.5, by contrast, sits in the lower-right region: high TSR, low CAR. Its collisions reflect genuine robot motion through the workspace. The two clusters are separated by a gap that no evaluated method occupies, a region that would require both meaningful task execution and reliable obstacle avoidance.
6	
7	This spatial structure has a direct implication for metric interpretation. A model that reports high CAR but near-zero TSR provides no evidence of collision avoidance capability; its safety score is an artifact of inaction. CAR is informative only when conditioned on sufficient task capability. We note that the TSR-CAR plane offers a more complete picture than either metric alone: the upper-right quadrant (high TSR, high CAR) represents genuinely safe and capable behavior, while the upper-left quadrant is accessible through action collapse without any safety mechanism.
8	
9	Early results from a Pi0.5 model augmented with A1-level SDF training (10K-step checkpoint) suggest that this gap is not inherent. This configuration achieves TSR of 47--49\% with CAR of 56--58\% and a frozen-action rate of 0\%, placing it in the previously unoccupied central region of Figure~\ref{fig:tsr_car_scatter}. We defer detailed analysis of this model to Section~\ref{sec:a1_pi05}, but note here that its position confirms the anti-correlation is a property of current models, not a fundamental constraint. Genuine collision avoidance requires a model that both moves and avoids, a combination that raw CAR cannot distinguish from one that simply does not move.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "acfd01e7-a14a-499b-9a65-b2bd8b24bbfe"
}
```

</details>

---

### System

_source line 93_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/_project/paper/analysis_claim3.tex",
  "usage": {
    "total_tokens": 52777,
    "tool_uses": 25,
    "duration_ms": 35147
  },
  "last_tool_name": "Read",
  "uuid": "a4ce2938-0102-406c-a765-99c6efeab52c",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 94_

<details open><summary>🔧 Tool call — Read · `toolu_01THbQjziR9js1BHUm3qZuAV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/analysis_claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "a423fb44-7c9c-45bc-a4b0-5f916ded1441",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011oSPodweqHsSnLHbTSH5F4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7761,
      "cache_read_input_tokens": 44955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7761,
        "ephemeral_1h_input_tokens": 0
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

_source line 95 · 2026-05-27T13:13:14.753Z_

<details><summary>↩ Tool result · `toolu_01THbQjziR9js1BHUm3qZuAV`</summary>

```text
1	\subsection{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\label{sec:ee_only}
2	
3	The analyses in Sections~\ref{sec:fake_safety} and~\ref{sec:tsr_car} identify action collapse and fake safety as pervasive problems, but leave open a natural question: could a sufficiently accurate SDF prediction still enable effective runtime refinement? To isolate the SDF representation itself from prediction quality, we construct an oracle experiment. We replace the learned SDF network with the ground-truth signed distance field computed directly from the known obstacle geometry. This oracle represents the theoretical upper bound of end-effector-only SDF refinement: it eliminates prediction error entirely, providing the refinement module with a perfect distance signal at every timestep. If the SDF refinement paradigm is sound, oracle performance should exceed that of unrefined baselines by a wide margin.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Oracle SDF refinement with ground-truth distance fields (160 episodes, 4 tasks $\times$ 40). All three variants achieve lower CAR than unrefined baselines (LoRA 82.0\%, Full-FT 83.0\%), and fake safe rates remain above 96\%.}
8	\label{tab:oracle}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lcccc}
12	\toprule
13	Method & TSR (\%) & CAR (\%) & Fake Safe (\%) & Refines/ep \\
14	\midrule
15	LoRA baseline (no refine) & 0.0 & 82.0 & 99.4 & -- \\
16	Full-FT baseline (no refine) & 0.5 & 83.0 & -- & -- \\
17	\midrule
18	Oracle-adaptive (GT, dyn.\ $\alpha$) & 0.0 & 75.0 & 98.3 & 14.2 \\
19	Oracle-fixed (GT, $\alpha{=}0.005$) & 0.0 & 73.1 & 98.3 & 14.8 \\
20	Oracle-feature (GT, feat.\ space) & 0.0 & 76.9 & 96.7 & 241.7 \\
21	\midrule
22	A3 learned SDF & 0.0 & 74.5 & -- & 0.0 \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	Table~\ref{tab:oracle} reports the results. All three oracle variants achieve CAR below that of the unrefined baselines. The best oracle (Oracle-feature, 76.9\%) falls 5.1 percentage points below the LoRA baseline (82.0\%) and 6.1 points below Full-FT (83.0\%). The adaptive and fixed-step variants perform worse still, at 75.0\% and 73.1\% respectively. These results are not marginal: the refinement module with perfect distance information produces more collisions than doing nothing at all. The fake safe rate tells a complementary story. Oracle-adaptive and Oracle-fixed both register 98.3\% fake safe episodes (118 of 120 and 115 of 117 safe episodes, respectively), while Oracle-feature registers 96.7\% (119 of 123). Ground-truth SDF refinement does not reduce action collapse; the vast majority of safe episodes remain attributable to inaction rather than obstacle avoidance.
28	
29	The per-task breakdown in Figure~\ref{fig:oracle_bar} reveals additional structure. On task~1, the most collision-prone task where the LoRA baseline achieves only 46.0\% CAR, Oracle-adaptive reaches 55.0\% and Oracle-feature reaches 47.5\%, a modest improvement consistent with a scenario where the end-effector is the primary collision body. On tasks~0, 2, and~3, all oracle variants produce lower CAR than the baseline: Oracle-adaptive drops from 96.0\% to 82.5\% on task~0 and from 98.0\% to 77.5\% on task~2. The refinement gradient, which pushes the end-effector away from the obstacle surface, perturbs the planned trajectory in ways that increase collisions elsewhere on the robot arm.
30	
31	This failure mode is structural. The SDF refinement paradigm as formulated in prior work~\cite{hu2025vlsa} computes the signed distance from the end-effector to the nearest obstacle surface and applies a gradient step to increase this distance when it falls below a safety threshold. The gradient operates exclusively on the end-effector position; no distance constraint applies to the remaining links of the robot arm. When the gradient pushes the end-effector away from an obstacle, the resulting joint-space displacement can rotate intermediate links toward or through the obstacle volume. The refinement thus trades one collision for another, with no mechanism to detect or prevent the substitution. The feature-space oracle makes this coupling problem explicit. It applies the SDF gradient in the policy's latent action space rather than in Cartesian coordinates, and fires on nearly every timestep (241.7 refinements per episode versus 14.2 for action-space variants). Yet its gradient magnitudes are extremely small (0.004--0.006, compared to 0.18--0.49 in action space), and the resulting CAR (76.9\%) shows no significant advantage over the action-space oracles. The latent space lacks a direct geometric relationship to full-body configuration; small perturbations in feature space do not reliably translate into collision-free joint trajectories.
32	
33	The A3 model with a learned SDF head illustrates the complementary failure. In this configuration, the SDF prediction network never outputs a distance below the refinement threshold across any of the 160 evaluation episodes, resulting in zero refinement steps. The learned SDF has calibrated its predictions to avoid triggering the safety mechanism, effectively reducing the model to an unrefined baseline (CAR of 74.5\%, consistent with the oracle range). The refinement module, even if it could improve safety, is never activated.
34	
35	These results establish that end-effector-only SDF is a structural limitation, not merely an engineering gap. Perfect distance information does not compensate for the absence of full-body collision awareness. Any refinement scheme that monitors only the end-effector position will remain blind to arm-body collisions, which constitute the dominant failure mode in manipulation tasks where the robot must reach around or past obstacles. Effective collision avoidance for VLA models will require representations that account for the geometric extent of the entire manipulator, not only its tip.
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "f73ae82e-93e0-471d-9a0e-31c33ea18685"
}
```

</details>

---

### System

_source line 96_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/_project/paper/experimental_framework.tex",
  "usage": {
    "total_tokens": 52778,
    "tool_uses": 26,
    "duration_ms": 35472
  },
  "last_tool_name": "Read",
  "uuid": "3dbab536-d115-4546-b1ea-d7802c9c6fcb",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 97_

<details open><summary>🔧 Tool call — Read · `toolu_01V7ptbTY4XNif5ziqZFRLpc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/experimental_framework.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "92f64184-88c1-4484-aae4-d69fb1aa0057",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011oSPodweqHsSnLHbTSH5F4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7761,
      "cache_read_input_tokens": 44955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7761,
        "ephemeral_1h_input_tokens": 0
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

_source line 98 · 2026-05-27T13:13:15.079Z_

<details><summary>↩ Tool result · `toolu_01V7ptbTY4XNif5ziqZFRLpc`</summary>

```text
1	\section{Experimental Framework}\label{sec:framework}
2	
3	This section defines the evaluation platform, metrics, and model configurations that underpin the analyses in Sections~\ref{sec:fake_safety}--\ref{sec:a1_pi05}. Our primary methodological contribution is the displacement-filtered Collision Avoidance Rate (CAR$_\text{f}$), which separates genuine avoidance from action collapse.
4	
5	\subsection{Benchmark and Evaluation Protocol}\label{sec:benchmark}
6	
7	We conduct all experiments on SafeLIBERO~\cite{hu2025vlsa}, a collision-aware evaluation extension of the LIBERO simulation platform~\cite{liu2023libero}. SafeLIBERO augments standard manipulation benchmarks with per-timestep collision detection and non-target obstacle annotations, enabling systematic measurement of both task completion and safety.
8	
9	We select the \textit{object\_pudding} Level~I suite, which comprises four tabletop manipulation tasks. In each task, a target object is surrounded by non-target obstacles that the robot must avoid during grasping and transport. The MuJoCo physics engine provides collision detection: any contact between the robot (end-effector or arm links) and a non-target object registers as a collision event.
10	
11	Each method is evaluated for 50 episodes per task (200 episodes total). For multi-seed experiments (Pi0.5), we run 3 seeds to produce 600 episodes per configuration. Initial object configurations are fixed across methods to ensure fair comparison.
12	
13	\subsection{Evaluation Metrics}\label{sec:metrics}
14	
15	\paragraph{Standard metrics.} We report two conventional metrics. The \emph{Task Success Rate} (TSR) is the fraction of episodes where the manipulation task reaches completion. The \emph{Collision Avoidance Rate} (CAR) is the fraction of episodes in which no collision occurs between the robot and any non-target object.
16	
17	\paragraph{Displacement-filtered CAR.} Standard CAR conflates two qualitatively distinct behaviors: a robot that plans a trajectory around obstacles, and a robot that has collapsed into inaction. Both register as ``safe,'' yet only the former reflects collision avoidance capability. We propose the displacement-filtered CAR (CAR$_\text{f}$), which excludes episodes exhibiting action collapse from both numerator and denominator.
18	
19	We define an episode $e$ as \emph{action-collapsed} when its maximum end-effector displacement satisfies $d_{\max}(e) < \tau_d$, where $\tau_d = 0.1$\,mm. The filtered metric is then:
20	\begin{equation}\label{eq:car_f}
21	\text{CAR}_\text{f} = \frac{|\{e : \text{safe}(e) \;\land\; d_{\max}(e) \geq \tau_d\}|}{|\{e : d_{\max}(e) \geq \tau_d\}|}
22	\end{equation}
23	where $d_{\max}(e)$ denotes the maximum Euclidean displacement of the end-effector across all timesteps in episode $e$. The threshold $\tau_d = 0.1$\,mm corresponds to sub-actuator-resolution motion and is robust to perturbation (Appendix~\ref{app:threshold_sensitivity}).
24	
25	\paragraph{Auxiliary metrics.} We additionally report the \emph{Frozen Rate}, the fraction of episodes with $d_{\max} < \tau_d$, which quantifies the severity of action collapse for each method. The \emph{Simultaneous Success Rate} (SSR $= $ TSR $\cap$ CAR) measures the fraction of episodes that achieve both task completion and collision avoidance.
26	
27	\subsection{Models and Training}\label{sec:models}
28	
29	\paragraph{Base architectures.} We evaluate two VLA models from the Pi0 family~\cite{black2024pi0}. \textbf{Pi0} (${\sim}$3B parameters) uses a PaliGemma vision-language encoder paired with a dedicated action expert that generates continuous actions via flow matching~\cite{lipman2023flow}. \textbf{Pi0.5} extends this architecture to ${\sim}$3.5B parameters with broader pre-training data, and serves as a stronger baseline that exhibits less action collapse.
30	
31	\paragraph{Training configurations.} We evaluate four model variants:
32	\begin{itemize}
33	\item \textit{Full-FT baseline}: Pi0 with all parameters fine-tuned on SafeLIBERO demonstrations using the flow-matching action loss.
34	\item \textit{LoRA baseline}: Pi0 with LoRA adapters (${\sim}$33.5M trainable parameters), same demonstrations and loss.
35	\item \textit{A1-LoRA}: Pi0 + LoRA augmented with two auxiliary heads. An SDF Decoder (4-layer MLP, ${\sim}$395K parameters) predicts the signed distance from the end-effector to the nearest obstacle surface, supervised with a clamped $L_1$ loss and an Eikonal regularizer ($\mathcal{L}_\text{SDF}$). An EE Extractor (2-layer MLP, ${\sim}$263K parameters) predicts end-effector position from action expert features ($\mathcal{L}_\text{EE}$, MSE loss). SDF ground truth is computed from known obstacle meshes in simulation.
36	\item \textit{Pi0.5 + A1}: The A1 architecture applied to the Pi0.5 backbone. Training proceeds in two phases: Phase~1 (steps 0--5K) trains only the auxiliary heads on detached features with the backbone frozen; Phase~2 (steps 5K--30K) unfreezes LoRA parameters for joint optimization. We evaluate $\lambda_\text{SDF} \in \{0.005, 0.01\}$.
37	\end{itemize}
38	
39	\subsection{Oracle SDF Refinement}\label{sec:oracle_setup}
40	
41	To test the theoretical upper bound of end-effector-only SDF refinement (analyzed in Section~\ref{sec:ee_only}), we replace the learned SDF network with the ground-truth signed distance field computed from simulation geometry. This eliminates prediction error and isolates the structural limitation of the refinement paradigm itself.
42	
43	We evaluate three oracle variants that differ in how the SDF gradient is applied:
44	\begin{itemize}
45	\item \textit{Oracle-adaptive}: runtime gradient refinement with a dynamic step size $\alpha$ that scales inversely with gradient magnitude.
46	\item \textit{Oracle-fixed}: a constant step size $\alpha = 0.005$.
47	\item \textit{Oracle-feature}: gradient applied in the VLA's latent feature space rather than Cartesian action space.
48	\end{itemize}
49	Each variant is evaluated for 160 episodes (4 tasks $\times$ 40 episodes) with a single seed.
50	
51	\subsection{SDF Ground Truth}\label{sec:sdf_gt}
52	
53	The workspace signed distance field is computed from the known obstacle meshes available in the LIBERO/MuJoCo simulation environment. SDF values are positive in free space, zero on the obstacle surface, and negative inside the obstacle volume. Ground-truth labels are generated at query points sampled along predicted end-effector trajectories during training.
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "7f7ee246-7e94-4886-bf65-a8b75467e148"
}
```

</details>

---

### System

_source line 99_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/_project/paper/discussion.tex",
  "usage": {
    "total_tokens": 52779,
    "tool_uses": 27,
    "duration_ms": 36044
  },
  "last_tool_name": "Read",
  "uuid": "64bbf4c3-6bfb-4061-a224-f2f9a2cd677a",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 100_

<details open><summary>🔧 Tool call — Read · `toolu_01YBunzBUR754gKjk2qpLWVM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "56d515a2-5c0d-4165-8ca0-4459c40b7c4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011oSPodweqHsSnLHbTSH5F4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7761,
      "cache_read_input_tokens": 44955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7761,
        "ephemeral_1h_input_tokens": 0
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

_source line 101 · 2026-05-27T13:13:15.651Z_

<details><summary>↩ Tool result · `toolu_01YBunzBUR754gKjk2qpLWVM`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	Across 90+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single conclusion: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (Pi0+A1 drops from 91.5\% to ${\approx}$\,0\% under displacement filtering); EE-only oracle refinement is counterproductive, \emph{reducing} CAR below unrefined baselines; and collision-free demonstrations, not geometric supervision, account for all measured avoidance gains in fine-tuned models. We discuss the mechanistic basis for each finding and its implications.
4	
5	\paragraph{Why EE-only SDF is redundant: a two-level account.}
6	The flat $\lambda$-CAR curve ($\lambda \in [0.005, 0.1]$, 20$\times$ range, all within the null band) rules out insufficient loss weight as the explanation and points to two independent structural causes.
7	
8	\textit{(i) Demonstration data subsumes the SDF training signal.} Collision-free demonstrations shift the action distribution away from collision-prone trajectories by construction: every demonstration trajectory is safe, so imitating demonstrations implicitly encodes spatial avoidance. The ${\sim}$28\,pp CAR gain from LoRA fine-tuning (26.8\% $\to$ 54.5\%) arises entirely from this distributional shift, with no SDF contribution. The per-task CAR ordering (chocolate\_pudding highest, bbq\_sauce lowest) is invariant across all SDF conditions and matches demonstration coverage, confirming that avoidance patterns originate from data statistics rather than geometric gradients. In this regime, EE-only SDF supplies a signal the model has already learned from imitation; adding a redundant gradient to a converged behavior produces no measurable effect. The Phase~2 ablation ($\lambda = 0$ after step~5K, CAR = 57.5\%) reinforces this interpretation: removing SDF supervision mid-training leaves avoidance unchanged, because the model never relied on it.
9	
10	\textit{(ii) End-effector monitoring cannot prevent full-body collisions.} Even granting a perfect distance signal, the SDF gradient acts on a single point (the EE) while collisions predominantly occur along intermediate arm links and joints. In SafeLIBERO manipulation tasks, the robot must reach around obstacles, placing the forearm and wrist in close proximity to obstacle surfaces that the EE-only SDF does not monitor. Oracle experiments confirm this structural gap: ground-truth SDF refinement \emph{reduces} CAR by 6\textendash10\,pp below unrefined baselines (73.1\textendash76.9\% vs.\ 82\textendash83\%), because pushing the EE away from obstacles rotates unmonitored links through them. The action space compounds the mismatch: VLA policies output delta EE poses, so the SDF gradient operates in the same low-dimensional space as the action, with no mechanism to constrain the full joint configuration that realizes a given EE displacement.
11	
12	These two levels are independent. Resolving (i) by finding a training signal beyond what demonstrations provide would not address (ii), and resolving (ii) through full-body monitoring would not change the fact that demonstrations already supply the avoidance signal. Effective geometric safety for VLA manipulation requires advances on both fronts: supervision that covers the full kinematic chain, and training signals that provide collision information beyond what is already implicit in collision-free demonstrations.
13	
14	\paragraph{Implications for VLA safety evaluation.}
15	CAR$_\text{f}$ corrects action-collapse contamination using only end-effector position logging, already available in most evaluation pipelines. The bimodal displacement distribution (collapsed below 1\,$\mu$m, active above 200\,mm) makes $\tau_d$ robust across five orders of magnitude. We recommend reporting both raw CAR and CAR$_\text{f}$; the gap quantifies action-collapse contamination. This contamination is not architecture-specific: Pi0 Full-FT (${\sim}$2.5B trainable), Pi0 LoRA (${\sim}$33.5M), and Pi0+A1 (${\sim}$658K) all exhibit $>$99\% fake safety despite a 4000$\times$ parameter range. It is a necessary consequence of evaluating collision avoidance without verifying that the robot moved.
16	
17	More broadly, our results suggest that safety in VLA manipulation may need to be addressed at the planning or constraint-satisfaction layer rather than through auxiliary losses on action prediction. When the action space is EE-centric, any loss defined over EE geometry inherits the same blind spot. Joint-space or full-body constraints, whether learned or imposed at planning time, offer a more natural interface for whole-arm collision avoidance.
18	
19	\paragraph{Limitations.}
20	Our evaluation covers one benchmark suite (SafeLIBERO object\_pudding, four tasks) and two model families (Pi0, Pi0.5). Preliminary spatial\_bowl results show different collision patterns, suggesting workspace geometry strongly affects collision modes; generalization to other tasks and architectures (OpenVLA, RT-2) is untested. Oracle experiments were conducted on a largely frozen model (Pi0+A1, TSR ${\approx}$ 0\%); testing on an actively moving policy would better isolate the EE-only structural limitation. The $\lambda = 0.1$ condition reports 2-seed results at the 20K checkpoint; \placeholder{30K three-seed confirmation pending}. Full-body SDF, the natural remedy for the structural mismatch identified here, remains untested. Fine-tuning degrades TSR by ${\sim}$21\textendash23\,pp; strategies that preserve task capability alongside avoidance remain an open problem.
21	
22	\paragraph{Future work.}
23	Three directions follow from this analysis: (1) full-body SDF supervision along the kinematic chain, covering intermediate arm links and joints; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families to determine the prevalence of fake safety and metric contamination; (3) planning-layer safety constraints that operate in joint space rather than EE space, decoupling collision avoidance from the action prediction loss.
24	
25	\paragraph{Broader impact.}
26	Contaminated CAR scores allow models with no genuine avoidance to pass safety benchmarks, creating false deployment readiness. CAR$_\text{f}$ exposes this gap with minimal changes to existing evaluation protocols.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "22e8afff-ce7e-4a36-a20e-a041e4b164ca"
}
```

</details>

---

### System

_source line 102_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/dream_reports/dream_20260526T023936/best/paper.tex",
  "usage": {
    "total_tokens": 60576,
    "tool_uses": 28,
    "duration_ms": 43633
  },
  "last_tool_name": "Read",
  "uuid": "286efd0d-4651-4218-a0f8-76f9c318c289",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 103_

<details open><summary>🔧 Tool call — Read · `toolu_01GeR2sXSLyqw44gzEoFJsaV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/dream_reports/dream_20260526T023936/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "b3cd8be5-22b1-4ce7-aeac-26fdba51c748",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RkBR8zDGsoBZRCiDCzVZny",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7795,
      "cache_read_input_tokens": 52716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7795,
        "ephemeral_1h_input_tokens": 0
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

_source line 104 · 2026-05-27T13:13:23.695Z_

<details><summary>↩ Tool result · `toolu_01GeR2sXSLyqw44gzEoFJsaV`</summary>

```text
1	\documentclass[10pt,letterpaper]{article}
2	
3	\usepackage[margin=1in]{geometry}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{multirow}
8	\usepackage{xcolor}
9	\usepackage{hyperref}
10	\usepackage{authblk}
11	\usepackage{caption}
12	\usepackage[numbers]{natbib}
13	
14	\newcommand{\CAR}{\text{CAR}}
15	\newcommand{\TSR}{\text{TSR}}
16	\newcommand{\dfCAR}{\text{dfCAR}}
17	
18	\title{Rethinking VLA Safety Evaluation:\\When 98\% of Collision Avoidance is an Illusion}
19	
20	\author[1]{Anonymous Authors}
21	\affil[1]{Anonymous Institution}
22	
23	\date{}
24	
25	\begin{document}
26	\maketitle
27	
28	% ==============================================================================
29	\begin{abstract}
30	% ==============================================================================
31	Vision-Language-Action (VLA) models are increasingly deployed in manipulation tasks where collision avoidance is safety-critical. The standard metric, Collision Avoidance Rate (CAR), is assumed to measure genuine avoidance behavior. We show that this assumption is systematically violated. Through large-scale empirical analysis (6000+ episodes across two task suites and two VLA families), we identify two failure modes that inflate CAR: \emph{action collapse}, where the robot freezes entirely, and \emph{geometric path safety}, where the default trajectory happens to avoid obstacles without active avoidance. On SafeLIBERO, a Pi0 model with SDF auxiliary loss (A1) reports 91.5\% CAR, yet 99.6\% of its ``safe'' episodes exhibit obstacle displacement below 0.1\,mm and 0\% task success, indicating complete action collapse rather than collision avoidance. We propose displacement-filtered CAR (dfCAR), a corrected metric that excludes frozen episodes using end-effector displacement thresholding. Sensitivity analysis across thresholds $\delta \in [2, 200]$\,mm confirms that dfCAR is invariant to threshold choice due to a bimodal gap ($>$200\,mm) between frozen and active episodes. We further show that LoRA fine-tuning on collision-free demonstrations alone produces genuine collision avoidance (+29 percentage points CAR, 0\% frozen episodes) on Pi0.5, while adding SDF geometric supervision contributes 0 additional percentage points across a 4-point $\lambda$ curve ($\lambda \in \{0, 0.005, 0.01, 0.1\}$, linear regression slope $= -0.3$, $R^2 = 0.12$). This redundancy is confirmed across two scenes. These findings reveal that implicit demonstration signals, not explicit geometric supervision, drive collision avoidance in fine-tuned VLAs.
32	\end{abstract}
33	
34	% ==============================================================================
35	\section{Introduction}
36	\label{sec:intro}
37	% ==============================================================================
38	
39	Safe operation in cluttered environments is a prerequisite for deploying robotic manipulation systems in real-world settings. As Vision-Language-Action (VLA) models scale in capability, the community has adopted Collision Avoidance Rate (CAR) as a primary safety metric, measuring the fraction of evaluation episodes in which the robot avoids contact with obstacles. A model reporting 90\%+ CAR appears safe, and downstream decisions (deployment, method comparisons, ablation conclusions) rely on this number.
40	
41	We show that CAR, as currently measured, is unreliable. The metric conflates three qualitatively different behaviors: (1)~genuine avoidance, where the robot actively navigates around obstacles; (2)~action collapse, where the model produces near-zero actions and the robot remains stationary; and (3)~geometric path safety, where the robot's default trajectory happens not to intersect obstacles. Both (2) and (3) register as ``collision-free'' under standard CAR, yet neither reflects learned safety awareness.
42	
43	The consequences are concrete. On SafeLIBERO~\cite{safelibero2025}, a Pi0~\cite{pi02024} model fine-tuned with SDF auxiliary loss (A1 configuration) achieves 91.5\% CAR. Per-episode analysis of 800 evaluation episodes reveals that 99.6\% of safe episodes exhibit obstacle displacement below 0.1\,mm, with a median of approximately 5\,nm. The model's Task Success Rate (TSR) is exactly 0\%. The robot is not avoiding collisions; it is not moving. Standard CAR cannot distinguish this frozen behavior from genuine safety.
44	
45	To address this measurement failure, we propose \emph{displacement-filtered CAR} (dfCAR), which filters out episodes where the end-effector displacement falls below a threshold $\delta$ before computing CAR. We show that dfCAR is robust to threshold selection: a bimodal gap exceeding 200\,mm between frozen and active episodes means any $\delta \in [2, 200]$\,mm produces identical results.
46	
47	Beyond the metric contribution, we investigate the source of collision avoidance in fine-tuned VLAs. LoRA fine-tuning on collision-free SafeLIBERO demonstrations produces genuine avoidance (CAR = 55.2\% $\pm$ 0.4\%, 0\% frozen episodes, EE displacement $\sim$0.48\,m) without any explicit geometric supervision. Adding SDF auxiliary loss at varying strengths ($\lambda \in \{0.005, 0.01, 0.1\}$) yields no additional CAR improvement. A 4-point $\lambda$ dose-response curve is completely flat (slope $= -0.3$ pp/unit-$\lambda$, $R^2 = 0.12$), and Phase~2 ablations confirm that SDF training leaves no persistent effect on model weights. The avoidance signal is implicit in the demonstration data, not in geometric supervision.
48	
49	Our contributions are:
50	\begin{enumerate}
51	    \item We identify systematic CAR contamination in VLA safety evaluation, with empirical evidence that 99.6\% of ``safe'' episodes in a published configuration reflect action collapse (Section~\ref{sec:fake_safety}).
52	    \item We propose dfCAR, a threshold-robust corrected metric, and validate its invariance across $\delta \in [2, 200]$\,mm (Section~\ref{sec:dfcar_robust}).
53	    \item We demonstrate that LoRA fine-tuning on collision-free demonstrations produces genuine collision avoidance without geometric supervision, while SDF auxiliary loss is dose-independent redundant across two scenes and a 20$\times$ $\lambda$ range (Section~\ref{sec:sdf_redundant}).
54	    \item We provide a Phase~2 ablation showing that SDF training has zero persistent effect on model behavior (Section~\ref{sec:phase2}).
55	\end{enumerate}
56	
57	% ==============================================================================
58	\section{Related Work}
59	\label{sec:related}
60	% ==============================================================================
61	
62	\paragraph{VLA Safety and Collision Avoidance.}
63	SafeLIBERO~\cite{safelibero2025} introduced collision avoidance benchmarks for VLA models, reporting CAR alongside task success. Several works have proposed auxiliary losses for safe manipulation~\cite{sdf_safety2024,safe_diffusion2025}, including signed distance function (SDF) supervision to push end-effector trajectories away from obstacles. These methods evaluate using standard CAR without examining whether reported safety reflects genuine avoidance behavior. Our work reveals that this evaluation practice systematically inflates safety metrics.
64	
65	\paragraph{SDF in Robot Motion Planning.}
66	Signed distance fields have a long history in motion planning~\cite{ratliff2009chomp,zucker2013chomp,schulman2014trajopt}, providing differentiable collision cost functions for trajectory optimization. Recent work has extended SDF-based supervision to learned policies~\cite{neural_sdf2023,diff_sdf2024}, computing SDF values at the end-effector position and backpropagating gradients through the policy network. A known limitation is that end-effector-only SDF ignores collisions involving the arm body and links, though this is often treated as an acceptable approximation.
67	
68	\paragraph{Evaluation Metrics for Robot Safety.}
69	The robotics community has developed various safety metrics including constraint violation rates, minimum clearance distances, and time-to-collision~\cite{safety_metrics2023}. In the VLA setting, CAR has become dominant due to its simplicity. Our displacement-filtered variant addresses a specific failure mode (action collapse) that is unique to learned policies with potential for degenerate behavior, a regime not encountered in classical motion planning where the controller always produces non-trivial actions.
70	
71	\paragraph{Fine-tuning and Catastrophic Forgetting in Foundation Models.}
72	Parameter-efficient fine-tuning methods such as LoRA~\cite{hu2022lora} enable adaptation of large pretrained models with minimal parameter overhead. In the VLA context, fine-tuning on task-specific demonstrations can alter both task capability and safety properties. The tension between task performance and safety under fine-tuning connects to broader concerns about catastrophic forgetting~\cite{kirkpatrick2017ewc}, though we observe a distinct phenomenon: models learn conservative behavior (high CAR, low TSR) rather than forgetting safety entirely.
73	
74	% ==============================================================================
75	\section{Background and Method}
76	\label{sec:method}
77	% ==============================================================================
78	
79	\subsection{Collision Avoidance Rate and Its Failure Modes}
80	\label{sec:car_failure}
81	
82	Let $\mathcal{E} = \{e_1, \ldots, e_N\}$ denote a set of evaluation episodes. For each episode $e_i$, define $c_i \in \{0, 1\}$ as the collision indicator (1 if the robot contacts an obstacle). The standard Collision Avoidance Rate is:
83	\begin{equation}
84	    \CAR = \frac{1}{N} \sum_{i=1}^{N} (1 - c_i).
85	\end{equation}
86	This metric assumes that $c_i = 0$ implies the robot actively avoided a collision. We identify two systematic violations of this assumption.
87	
88	\textbf{Action collapse.} Some VLA configurations produce near-zero actions across entire episodes, resulting in a stationary robot. The end-effector displacement $d_i^{\text{ee}}$ in these episodes is below 1\,mm, and obstacle displacement $d_i^{\text{obs}}$ is below 0.1\,mm. No collision occurs because no motion occurs.
89	
90	\textbf{Geometric path safety.} In some task configurations, the robot's default (pre-trained) trajectory does not intersect any obstacle regardless of avoidance behavior. The model executes its task normally (nonzero $d_i^{\text{ee}}$, nonzero TSR), but collisions are absent due to workspace geometry, not learned avoidance.
91	
92	Both failure modes inflate CAR without reflecting safety-relevant model behavior.
93	
94	\subsection{Displacement-Filtered CAR}
95	\label{sec:dfcar_method}
96	
97	We propose displacement-filtered CAR (dfCAR) to exclude episodes exhibiting action collapse. For each episode $e_i$, compute the cumulative end-effector displacement:
98	\begin{equation}
99	    d_i^{\text{ee}} = \sum_{t=1}^{T_i} \| \mathbf{p}_t^{\text{ee}} - \mathbf{p}_{t-1}^{\text{ee}} \|_2,
100	\end{equation}
101	where $\mathbf{p}_t^{\text{ee}} \in \mathbb{R}^3$ is the end-effector position at timestep $t$. Given a threshold $\delta > 0$, define the set of active episodes $\mathcal{A}_\delta = \{e_i : d_i^{\text{ee}} > \delta\}$. Then:
102	\begin{equation}
103	    \dfCAR_\delta = \frac{1}{|\mathcal{A}_\delta|} \sum_{e_i \in \mathcal{A}_\delta} (1 - c_i).
104	\end{equation}
105	If $|\mathcal{A}_\delta| = 0$ (all episodes frozen), dfCAR is undefined, correctly reflecting the absence of evaluable safety behavior.
106	
107	A key property we demonstrate empirically is \emph{threshold robustness}: the distribution of $d_i^{\text{ee}}$ is strongly bimodal, with frozen episodes clustered below 1\,mm and active episodes above 239\,mm. Any $\delta$ in the gap $[2, 200]$\,mm produces identical $\mathcal{A}_\delta$ and thus identical dfCAR.
108	
109	\subsection{SDF Auxiliary Loss}
110	\label{sec:sdf_loss}
111	
112	Following prior work~\cite{safelibero2025}, we define an SDF auxiliary loss computed at the end-effector position. Given a scene SDF $\phi: \mathbb{R}^3 \to \mathbb{R}$ (negative inside obstacles), the auxiliary loss for episode step $t$ is:
113	\begin{equation}
114	    \mathcal{L}_{\text{SDF}}^{(t)} = \max(0, \, \tau - \phi(\mathbf{p}_t^{\text{ee}})),
115	\end{equation}
116	where $\tau$ is a safety margin. The total training loss combines the action prediction loss $\mathcal{L}_{\text{action}}$ with the SDF term:
117	\begin{equation}
118	    \mathcal{L} = \mathcal{L}_{\text{action}} + \lambda \, \mathcal{L}_{\text{SDF}}.
119	\end{equation}
120	We vary $\lambda \in \{0, 0.005, 0.01, 0.1\}$ to construct a dose-response curve. At $\lambda = 0.005$, the SDF term contributes approximately 0.5\% of the total loss; at $\lambda = 0.1$, it contributes approximately 10\%.
121	
122	\subsection{Experimental Setup}
123	\label{sec:setup}
124	
125	\textbf{Tasks and Scenes.} We evaluate on two SafeLIBERO scenes: \texttt{object\_pudding} (4 tasks: orange juice, chocolate pudding, milk, BBQ sauce) and \texttt{spatial\_bowl} (4 tasks: pick bowl from varying spatial configurations). Each evaluation runs 200 episodes (50 per task).
126	
127	\textbf{Models.} We use two VLA families: Pi0~\cite{pi02024} and Pi0.5. The A1 configuration applies SDF auxiliary loss to Pi0. LoRA fine-tuning is applied to Pi0.5 with rank-16 adaptation.
128	
129	\textbf{Training.} All fine-tuning runs use 30K gradient steps on collision-free SafeLIBERO demonstrations. For Phase~2 ablations, models are first trained for 10K steps with SDF loss ($\lambda = 0.005$), then the SDF loss is removed ($\lambda = 0$) for an additional 20K steps.
130	
131	\textbf{Seeds.} LoRA-only experiments use 3 random seeds. SDF experiments at $\lambda \in \{0.005, 0.01\}$ use 3 seeds each; $\lambda = 0.1$ uses 2 seeds. Phase~2 ablations use 2 seeds.
132	
133	% ==============================================================================
134	\section{Experiments}
135	\label{sec:experiments}
136	% ==============================================================================
137	
138	\subsection{Fake Safety in Standard CAR}
139	\label{sec:fake_safety}
140	
141	We first demonstrate that standard CAR is systematically contaminated by action collapse.
142	
143	\textbf{A1 (Pi0 + SDF) analysis.} We evaluate the A1 configuration (Pi0 with SDF auxiliary loss, $\lambda = 0.005$) on \texttt{object\_pudding} over 800 episodes. A1 reports CAR = 91.5\%. Per-episode obstacle displacement analysis reveals that 729 out of 732 safe episodes have obstacle displacement below 0.1\,mm (99.6\%), with a median of approximately 5\,nm. TSR = 0\%: the model completes zero tasks. This constitutes action collapse, not collision avoidance. Applying dfCAR with any $\delta \geq 2$\,mm yields dfCAR $\approx$ 0\%, as nearly all episodes are frozen.
144	
145	\textbf{Pi0.5 baseline analysis.} In contrast, the Pi0.5 pretrained model achieves CAR = 26.8\% $\pm$ 1.6\% with TSR = 74.7\% $\pm$ 1.5\%. All episodes are active (EE displacement $>$ 120\,mm), so dfCAR = CAR = 26.8\%. The 56 out of 200 safe episodes in a typical evaluation reflect geometric path safety: the pretrained trajectory avoids obstacles due to workspace layout, not learned avoidance.
146	
147	The gap between A1's standard CAR (91.5\%) and dfCAR ($\approx$0\%) demonstrates that standard CAR can be arbitrarily misleading when action collapse is present.
148	
149	\subsection{Capability-Safety Anti-correlation}
150	\label{sec:cap_safety}
151	
152	Comparing the two VLA families reveals a tension between task capability and collision rate. Pi0 (A1 configuration) achieves TSR = 0\% and CAR = 91.5\%, while Pi0.5 achieves TSR = 74.7\% and CAR = 26.8\%. The more capable model completes more tasks but collides more frequently. This pattern is expected: a model that moves to complete tasks necessarily encounters more collision opportunities. We note this as an observation rather than a causal claim, as the comparison involves only two model families with different architectures and training procedures.
153	
154	\subsection{Fine-tuning Produces Genuine Collision Avoidance}
155	\label{sec:real_avoidance}
156	
157	LoRA fine-tuning on collision-free demonstrations substantially improves collision avoidance without any geometric supervision. Table~\ref{tab:lora_3seed} reports results across 3 seeds on \texttt{object\_pudding}.
158	
159	\begin{table}[t]
160	\centering
161	\caption{LoRA-only fine-tuning (no SDF loss) on Pi0.5, evaluated on \texttt{object\_pudding}. All episodes are active (0\% frozen); dfCAR equals raw CAR.}
162	\label{tab:lora_3seed}
163	\begin{tabular}{lccccc}
164	\toprule
165	Seed & CAR (\%) & TSR (\%) & EE Disp (m) & Frozen (\%) & dfCAR (\%) \\
166	\midrule
167	s0   & 54.5 & 8.5 & 0.489 & 0 & 54.5 \\
168	s1   & 56.0 & 4.0 & 0.467 & 0 & 56.0 \\
169	s2   & 55.0 & 6.0 & 0.481 & 0 & 55.0 \\
170	\midrule
171	Mean $\pm$ SE & 55.2 $\pm$ 0.4 & 6.2 $\pm$ 1.3 & 0.479 $\pm$ 0.006 & 0 & 55.2 $\pm$ 0.4 \\
172	\bottomrule
173	\end{tabular}
174	\end{table}
175	
176	Fine-tuning raises CAR from 26.8\% (Pi0.5 baseline) to 55.2\%, a gain of +28.4 percentage points. All episodes are active (EE displacement 0.467--0.489\,m, minimum displacement 239\,mm), confirming genuine avoidance behavior rather than action collapse. However, TSR drops from 74.7\% to 6.2\%, indicating catastrophic task performance collapse. The model learns conservative behavior from collision-free demonstrations: it moves enough to be active but avoids obstacle-proximal regions, at the cost of task completion.
177	
178	The per-task CAR pattern is consistent across all seeds and conditions. Task~2 (milk) achieves $\sim$92\% CAR due to a workspace layout where obstacles are small and the natural path is distant. Task~3 (BBQ sauce) achieves $\sim$20\% CAR due to a narrow corridor with bilateral obstacles. This geometry-driven pattern confirms that avoidance performance is determined by task layout interacting with the learned conservative policy, not by random seed variation (seed-to-seed SD = 0.75 pp).
179	
180	\subsection{SDF Geometric Supervision is Redundant}
181	\label{sec:sdf_redundant}
182	
183	\subsubsection{Direct Comparison: LoRA-only vs.\ LoRA+SDF (3 vs.\ 3 Seeds)}
184	\label{sec:3v3}
185	
186	Table~\ref{tab:3v3} compares LoRA-only ($\lambda = 0$) with two SDF conditions on \texttt{object\_pudding}, each with 3 seeds.
187	
188	\begin{table}[t]
189	\centering
190	\caption{LoRA-only vs.\ LoRA+SDF on \texttt{object\_pudding}. Three seeds per condition. $\Delta$ = SDF best $-$ LoRA.}
191	\label{tab:3v3}
192	\begin{tabular}{lcccccc}
193	\toprule
194	Condition & Seeds & CAR (\%) & SD & TSR (\%) & EE Disp (m) & Frozen (\%) \\
195	\midrule
196	LoRA-only ($\lambda{=}0$) & 3 & 55.2 & 0.75 & 6.2 & 0.479 & 0 \\
197	SDF $\lambda{=}0.005$ & 3 & 50.5 & 3.0 & 6.1 & 0.483 & 0 \\
198	SDF $\lambda{=}0.01$ & 3 & 52.8 & 0.3 & 7.2 & 0.476 & 0 \\
199	\bottomrule
200	\multicolumn{7}{l}{\footnotesize $\Delta(\text{SDF best} - \text{LoRA}) = -2.4$ pp, $p = 0.35$ (Welch $t$-test, df $\approx$ 3), not significant.}
201	\end{tabular}
202	\end{table}
203	
204	The best SDF condition ($\lambda = 0.01$, CAR = 52.8\%) is 2.4 percentage points \emph{below} LoRA-only (55.2\%). A Welch $t$-test yields $p = 0.35$ (df $\approx 3$), indicating no significant difference. The direction of the effect is opposite to the SDF hypothesis: geometric supervision does not improve and may slightly degrade collision avoidance.
205	
206	TSR, EE displacement, and frozen rate are statistically indistinguishable across all conditions. The fine-tuning collapse (TSR: 73\% $\to$ 6\%) is a property of LoRA adaptation on this data, not of SDF supervision.
207	
208	\subsubsection{Dose-Response: 4-Point $\lambda$ Curve}
209	\label{sec:dose_response}
210	
211	To rule out the possibility that SDF is effective at a different $\lambda$ scale, we extend the comparison to $\lambda = 0.1$ (Table~\ref{tab:lambda_curve}), increasing the SDF gradient contribution from $\sim$0.5\% to $\sim$10\% of total loss.
212	
213	\begin{table}[t]
214	\centering
215	\caption{4-point $\lambda$ dose-response curve on \texttt{object\_pudding}. Linear regression over all 4 points: slope $= -0.3$ pp/unit-$\lambda$, $R^2 = 0.12$, $F$-test $p > 0.5$.}
216	\label{tab:lambda_curve}
217	\begin{tabular}{llcccc}
218	\toprule
219	$\lambda$ & Method & Seeds & CAR Mean (\%) & CAR SD & TSR Mean (\%) \\
220	\midrule
221	0 (LoRA) & LoRA-only & 3 & 55.2 & 0.75 & 6.2 \\
222	0.005 & LoRA+SDF & 3 & 50.5 & 3.0 & 6.1 \\
223	0.01 & LoRA+SDF & 3 & 52.8 & 0.3 & 7.2 \\
224	0.1 & LoRA+SDF & 2 & 51.0 & 1.4 & 6.3 \\
225	\bottomrule
226	\end{tabular}
227	\end{table}
228	
229	The $\lambda$ curve is flat. Linear regression across the 4 points yields a slope of $-0.3$ pp per unit $\lambda$ with $R^2 = 0.12$, indicating that $\lambda$ explains virtually none of the CAR variance. The LoRA-only baseline ($\lambda = 0$) is the highest point on the curve (55.2\%), though the difference from any SDF condition is within standard error.
230	
231	At $\lambda = 0.1$, SDF loss constitutes approximately 10\% of the total gradient signal, a non-negligible contribution. Yet CAR (51.0\%) remains indistinguishable from the lower-$\lambda$ SDF conditions (50.5\%, 52.8\%). The per-task breakdown at $\lambda = 0.1$ (Table~\ref{tab:lambda01_pertask}) confirms that task-level CAR patterns are identical to LoRA-only, governed by workspace geometry rather than SDF strength.
232	
233	\begin{table}[t]
234	\centering
235	\caption{Per-task CAR breakdown at $\lambda = 0.1$ (2 seeds) vs.\ LoRA-only mean (3 seeds) on \texttt{object\_pudding}.}
236	\label{tab:lambda01_pertask}
237	\begin{tabular}{lccccr}
238	\toprule
239	Task & CAR s0 (\%) & CAR s1 (\%) & Mean (\%) & LoRA-only (\%) & $\Delta$ \\
240	\midrule
241	orange\_juice & 62 & 58 & 60 & 60 & 0 \\
242	chocolate\_pudding & 44 & 40 & 42 & 47 & $-5$ \\
243	milk & 84 & 80 & 82 & 92 & $-10$ \\
244	bbq\_sauce & 18 & 22 & 20 & 20 & 0 \\
245	\bottomrule
246	\end{tabular}
247	\end{table}
248	
249	This dose-independence constitutes strong evidence that SDF geometric supervision is structurally redundant in this setting, not merely poorly tuned.
250	
251	\subsubsection{Cross-Scene Validation}
252	\label{sec:cross_scene}
253	
254	We replicate the LoRA vs.\ SDF comparison on \texttt{spatial\_bowl} to test whether the redundancy finding generalizes beyond a single scene (Table~\ref{tab:spatial}).
255	
256	\begin{table}[t]
257	\centering
258	\caption{Cross-scene SDF redundancy on \texttt{spatial\_bowl}. Single seed per condition.}
259	\label{tab:spatial}
260	\begin{tabular}{lcccr}
261	\toprule
262	Condition & CAR (\%) & TSR (\%) & EE Disp (m) & $\Delta$ vs.\ LoRA \\
263	\midrule
264	Pi0.5 Baseline & 13.0 & 57.5 & --- & ref \\
265	LoRA-only & 28.0 & 4.0 & 0.305 & --- \\
266	LoRA+SDF $\lambda{=}0.005$ & 30.0 & 3.5 & 0.310 & $+2.0$ pp (n.s.) \\
267	\bottomrule
268	\end{tabular}
269	\end{table}
270	
271	On \texttt{spatial\_bowl}, the SDF condition (CAR = 30.0\%) is 2.0 pp above LoRA-only (28.0\%), but this difference is not significant given the 200-episode evaluation noise ($\pm$3.5 pp). Notably, the SDF delta has opposite sign across the two scenes: $-3$ pp on \texttt{object\_pudding} and $+2$ pp on \texttt{spatial\_bowl}. This directional inconsistency is itself evidence of noise rather than a real effect. The combined cross-scene SDF delta is approximately $-0.5$ pp (95\% CI: [$-5$, $+4$]).
272	
273	The absolute CAR levels differ substantially between scenes (55\% vs.\ 28\%), reflecting differences in obstacle geometry and task difficulty. The \texttt{spatial\_bowl} scene features low, wide obstacles (bowls, ramekins) that cause arm-body collisions, which are structurally invisible to end-effector-only SDF (see Section~\ref{sec:ee_only}). Despite these scene-level differences, the core finding is identical: SDF adds nothing to LoRA-only fine-tuning.
274	
275	\subsection{Phase 2: SDF Training Has No Persistent Effect}
276	\label{sec:phase2}
277	
278	If SDF auxiliary loss were encoding useful geometric awareness into model weights during the first 10K training steps, this information might persist even after removing the SDF loss. We test this with a Phase~2 ablation: train for 10K steps with SDF loss ($\lambda = 0.005$), then continue for 20K steps with $\lambda = 0$. Table~\ref{tab:phase2} compares Phase~2 models against LoRA-only baselines.
279	
280	\begin{table}[t]
281	\centering
282	\caption{Phase~2 ablation: 10K SDF $\to$ 20K LoRA-only vs.\ full 30K LoRA-only. Results on \texttt{object\_pudding}.}
283	\label{tab:phase2}
284	\begin{tabular}{llccc}
285	\toprule
286	Condition & Training Path & CAR (\%) & TSR (\%) & EE Disp (m) \\
287	\midrule
288	LoRA-only (s0) & 30K LoRA & 54.5 & 8.5 & 0.489 \\
289	LoRA-only (s1) & 30K LoRA & 56.0 & 4.0 & 0.467 \\
290	Phase~2 (s2) & 10K SDF $\to$ 20K LoRA & 55.0 & 7.0 & 0.475 \\
291	SDF full (s2, $\lambda{=}0.005$) & 30K SDF & 53.0 & 9.0 & 0.505 \\
292	\bottomrule
293	\end{tabular}
294	\end{table}
295	
296	Phase~2 achieves CAR = 55.0\%, falling exactly within the LoRA-only range [54.5, 56.0]. This rules out two alternative hypotheses: (1) that SDF training causes persistent damage (which would yield CAR below LoRA-only), and (2) that SDF creates a subtle lasting benefit (which would yield CAR above LoRA-only). The model simply reverts to the demonstration-driven baseline once SDF loss is removed.
297	
298	Multi-seed Phase~2 results (Table~\ref{tab:phase2_multi}) confirm this finding.
299	
300	\begin{table}[t]
301	\centering
302	\caption{Phase~2 multi-seed summary. $\Delta$ = Phase~2 CAR $-$ corresponding LoRA-only CAR.}
303	\label{tab:phase2_multi}
304	\begin{tabular}{lccr}
305	\toprule
306	Seed & Phase~2 CAR (\%) & LoRA-only CAR (\%) & $\Delta$ \\
307	\midrule
308	seed2 & 55.0 & 55.0 & 0.0 \\
309	seed0/1 & 54.0 & 54.5/56.0 & $-0.5$/$-2.0$ \\
310	\midrule
311	Mean & 54.5 & 55.2 & $-0.7$ \\
312	\bottomrule
313	\multicolumn{4}{l}{\footnotesize $|\Delta| < 1$ pp, not statistically significant.}
314	\end{tabular}
315	\end{table}
316	
317	The 2-seed Phase~2 mean (54.5\%) is 0.7 pp below the 3-seed LoRA-only mean (55.2\%), a difference well within evaluation noise. SDF auxiliary loss at 10K steps neither helps nor harms model behavior, and any weight changes it induces are overwritten during the subsequent 20K steps of standard fine-tuning.
318	
319	\subsection{dfCAR Threshold Robustness}
320	\label{sec:dfcar_robust}
321	
322	A potential concern with dfCAR is sensitivity to the threshold $\delta$. Table~\ref{tab:dfcar_threshold} demonstrates that dfCAR is completely invariant to threshold choice across a 100$\times$ range.
323	
324	\begin{table}[t]
325	\centering
326	\caption{dfCAR at varying thresholds $\delta$. Values are constant across $\delta \in [2, 200]$\,mm for all active model configurations.}
327	\label{tab:dfcar_threshold}
328	\begin{tabular}{rcccc}
329	\toprule
330	$\delta$ (mm) & LoRA-only (\%) & SDF $\lambda{=}0.005$ (\%) & A1/Pi0 (\%) & Pi0.5 Baseline (\%) \\
331	\midrule
332	2 & 54.5 & 50.5 & 0.4 & 27.5 \\
333	5 & 54.5 & 50.5 & 0.4 & 27.5 \\
334	10 & 54.5 & 50.5 & 0.0 & 27.5 \\
335	20 & 54.5 & 50.5 & 0.0 & 27.5 \\
336	50 & 54.5 & 50.5 & 0.0 & 27.5 \\
337	100 & 54.5 & 50.5 & 0.0 & 27.5 \\
338	200 & 54.5 & 50.5 & 0.0 & 27.5 \\
339	\bottomrule
340	\end{tabular}
341	\end{table}
342	
343	The invariance arises from a bimodal distribution of EE displacement (Table~\ref{tab:ee_dist}). Frozen episodes (A1/Pi0) have EE displacement below 1\,mm (median 0.005\,mm), while active episodes (LoRA-tuned, SDF-tuned, Pi0.5 baseline) have minimum EE displacement of 239\,mm. The gap exceeding 200\,mm between the two modes means that no episode falls in the ambiguous range, and any reasonable threshold produces identical filtering.
344	
345	\begin{table}[t]
346	\centering
347	\caption{End-effector displacement distribution statistics across conditions.}
348	\label{tab:ee_dist}
349	\begin{tabular}{lcccc}
350	\toprule
351	Condition & Min (mm) & Median (mm) & Max (mm) & Gap \\
352	\midrule
353	A1 frozen (Pi0) & $<$0.001 & 0.005 & 0.8 & --- \\
354	Pi0.5 Baseline & 120 & 350 & 620 & --- \\
355	LoRA-only & 239 & 420 & 580 & $>$200\,mm \\
356	LoRA+SDF & 245 & 430 & 590 & $>$200\,mm \\
357	\bottomrule
358	\end{tabular}
359	\end{table}
360	
361	We recommend $\delta = 10$\,mm as a default threshold. It is well above sensor noise, well below the minimum active displacement, and produces results identical to any other choice in [2, 200]\,mm. The practitioner need not calibrate this parameter.
362	
363	\subsection{EE-only SDF Structural Limitation}
364	\label{sec:ee_only}
365	
366	The redundancy of SDF supervision has a structural explanation. The SDF auxiliary loss is computed only at the end-effector position $\mathbf{p}_t^{\text{ee}}$, producing gradients that push the end-effector away from obstacles. However, collisions in manipulation tasks often involve the arm body, wrist, and links, not only the end-effector tip.
367	
368	In \texttt{spatial\_bowl}, obstacles are low and wide (bowls placed on ramekins, on stovetops, on cabinets), and the dominant collision mode is the arm sweeping over an obstacle while the end-effector is already clear. EE-only SDF gradients are structurally unable to address this failure mode.
369	
370	On \texttt{object\_pudding}, obstacles include tall objects (bottles, cartons) where end-effector proximity correlates more strongly with collision risk, yet even here, the SDF gradient direction may not align with the action-space direction needed for avoidance. The SDF loss gradient pushes the end-effector in Cartesian space, but the policy operates in a joint-space or action-token space where the mapping between Cartesian EE displacement and action correction is non-trivial.
371	
372	These structural limitations explain why increasing $\lambda$ from 0.005 to 0.1 (a 20$\times$ increase) does not improve CAR: a larger $\lambda$ amplifies a gradient signal whose direction is misaligned with the desired behavioral change.
373	
374	% ==============================================================================
375	\section{Discussion}
376	\label{sec:discussion}
377	% ==============================================================================
378	
379	\textbf{Source of collision avoidance.} Our results indicate that collision avoidance in fine-tuned VLAs originates from implicit signals in the training demonstrations, not from explicit geometric supervision. Collision-free demonstrations naturally encode avoidance trajectories: the demonstrator navigated around obstacles, and the model imitates this behavior. This finding has practical implications. Rather than engineering auxiliary losses with geometric representations, practitioners may achieve equivalent safety by curating demonstration data. The relevant question shifts from ``how to supervise avoidance'' to ``how to ensure demonstrations encode the desired safety behavior.''
380	
381	\textbf{Conservative behavior vs.\ genuine safety.} Fine-tuning produces a 29 pp CAR improvement but at the cost of an 68 pp TSR drop (73\% $\to$ 6\%). The model does not learn to navigate safely while completing tasks; it learns to avoid motion in obstacle-proximal regions, often at the expense of task completion. This conservative-but-incapable behavior is a form of learned risk aversion that may not be desirable in deployment. Distinguishing between conservative avoidance and genuine safety awareness (maintaining task capability while avoiding collisions) is an important direction for future work.
382	
383	\textbf{Limitations.} Our evaluation is conducted on SafeLIBERO with two VLA families (Pi0 and Pi0.5). While the mechanistic argument for fake safety (any model with action collapse will exhibit inflated CAR) is general, the specific findings about SDF redundancy may not transfer to architectures with fundamentally different action representations. We were unable to evaluate OpenVLA due to technical constraints (model download failures), leaving the third-family validation incomplete. The SDF auxiliary loss uses only end-effector position; full-body SDF could potentially yield different results, though this requires significantly more complex implementation.
384	
385	% ==============================================================================
386	\section{Conclusion}
387	\label{sec:conclusion}
388	% ==============================================================================
389	
390	We have shown that the standard Collision Avoidance Rate metric is systematically unreliable for evaluating VLA safety. Action collapse inflates CAR to 91.5\% for a model that never moves, and geometric path safety contributes collision-free episodes without any avoidance behavior. Our proposed dfCAR metric corrects this by filtering frozen episodes using end-effector displacement, with a bimodal gap ensuring complete threshold robustness.
391	
392	On the methodological side, we demonstrate that LoRA fine-tuning on collision-free demonstrations is sufficient to produce genuine collision avoidance in Pi0.5, while explicit SDF geometric supervision contributes zero additional benefit across all tested conditions: three $\lambda$ values, two scenes, and a Phase~2 persistence ablation. The avoidance signal is implicit in the demonstration data.
393	
394	These results suggest two actionable takeaways. First, any safety evaluation using CAR should verify that episodes reflect genuine motion, either through dfCAR or equivalent activity checks. Second, for VLA safety improvement through fine-tuning, demonstration curation may be more productive than auxiliary geometric losses.
395	
396	% ==============================================================================
397	% References
398	% ==============================================================================
399	{\small
400	\bibliographystyle{plainnat}
401	\begin{thebibliography}{10}
402	
403	\bibitem[SafeLIBERO(2025)]{safelibero2025}
404	SafeLIBERO Team.
405	\newblock SafeLIBERO: Benchmarking safety for vision-language-action models in robotic manipulation.
406	\newblock In \emph{Proceedings of ICRA}, 2025.
407	
408	\bibitem[Pi0(2024)]{pi02024}
409	Physical Intelligence.
410	\newblock Pi0: A vision-language-action flow model for general robot control.
411	\newblock \emph{arXiv preprint}, 2024.
412	
413	\bibitem[SDF-Safety(2024)]{sdf_safety2024}
414	{Authors}.
415	\newblock Signed distance field supervision for safe robot manipulation.
416	\newblock In \emph{Proceedings of CoRL}, 2024.
417	
418	\bibitem[Safe-Diffusion(2025)]{safe_diffusion2025}
419	{Authors}.
420	\newblock Safety-constrained diffusion policies for robotic manipulation.
421	\newblock In \emph{Proceedings of ICRA}, 2025.
422	
423	\bibitem[Ratliff et~al.(2009)]{ratliff2009chomp}
424	N.~Ratliff, M.~Zucker, J.~A.~Bagnell, and S.~Srinivasa.
425	\newblock CHOMP: Gradient optimization techniques for efficient motion planning.
426	\newblock In \emph{Proceedings of ICRA}, 2009.
427	
428	\bibitem[Zucker et~al.(2013)]{zucker2013chomp}
429	M.~Zucker, N.~Ratliff, A.~D.~Dragan, M.~Pivtoraiko, M.~Klingensmith, C.~M.~Dellin, J.~A.~Bagnell, and S.~S.~Srinivasa.
430	\newblock CHOMP: Covariant Hamiltonian optimization for motion planning.
431	\newblock \emph{International Journal of Robotics Research}, 32(9--10):1164--1193, 2013.
432	
433	\bibitem[Schulman et~al.(2014)]{schulman2014trajopt}
434	J.~Schulman, Y.~Duan, J.~Ho, A.~Lee, I.~Awwal, H.~Bradlow, J.~Pan, S.~Patil, K.~Goldberg, and P.~Abbeel.
435	\newblock Motion planning with sequential convex optimization and convex collision checking.
436	\newblock \emph{International Journal of Robotics Research}, 33(9):1251--1270, 2014.
437	
438	\bibitem[Neural-SDF(2023)]{neural_sdf2023}
439	{Authors}.
440	\newblock Neural signed distance fields for safe robot control.
441	\newblock In \emph{Proceedings of RSS}, 2023.
442	
443	\bibitem[Diff-SDF(2024)]{diff_sdf2024}
444	{Authors}.
445	\newblock Differentiable SDF-based collision avoidance for learned manipulation policies.
446	\newblock In \emph{Proceedings of IROS}, 2024.
447	
448	\bibitem[Safety-Metrics(2023)]{safety_metrics2023}
449	{Authors}.
450	\newblock A survey of safety metrics for robot manipulation in human environments.
451	\newblock \emph{IEEE Robotics and Automation Letters}, 2023.
452	
453	\bibitem[Hu et~al.(2022)]{hu2022lora}
454	E.~J.~Hu, Y.~Shen, P.~Wallis, Z.~Allen-Zhu, Y.~Li, S.~Wang, L.~Wang, and W.~Chen.
455	\newblock LoRA: Low-rank adaptation of large language models.
456	\newblock In \emph{Proceedings of ICLR}, 2022.
457	
458	\bibitem[Kirkpatrick et~al.(2017)]{kirkpatrick2017ewc}
459	J.~Kirkpatrick, R.~Pascanu, N.~Rabinowitz, J.~Veness, G.~Desjardins, A.~A.~Rusu, K.~Milan, J.~Quan, T.~Ramalho, A.~Grabska-Barwinska, D.~Hassabis, C.~Kavukcuoglu, and R.~Hadsell.
460	\newblock Overcoming catastrophic forgetting in neural networks.
461	\newblock \emph{Proceedings of the National Academy of Sciences}, 114(13):3521--3526, 2017.
462	
463	\end{thebibliography}
464	}
465	
466	\end{document}
467	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "967b6b20-fd78-4e6e-a66f-75554f2de972"
}
```

</details>

---

### System

_source line 105_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/_project/paper/introduction.tex",
  "usage": {
    "total_tokens": 72941,
    "tool_uses": 29,
    "duration_ms": 49134
  },
  "last_tool_name": "Read",
  "uuid": "f4d9ae06-07b8-4afb-bff5-aec4137247da",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 106_

<details open><summary>🔧 Tool call — Read · `toolu_017CrzDaQ3p6htFik88nZRvE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "5fc7a7aa-d006-429c-8472-ac8b1000392b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LG2GRgapptdThxFhJzpb7R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12361,
      "cache_read_input_tokens": 60511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12361,
        "ephemeral_1h_input_tokens": 0
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

_source line 107 · 2026-05-27T13:13:28.742Z_

<details><summary>↩ Tool result · `toolu_017CrzDaQ3p6htFik88nZRvE`</summary>

```text
1	\section{Introduction}
2	
3	Vision-Language-Action (VLA) models such as $\pi_0$~\cite{black2024pi0}, OpenVLA~\cite{kim2024openvla}, and RT-2~\cite{brohan2023rt2} combine visual perception, language understanding, and action generation in a unified architecture to follow diverse natural language instructions across manipulation tasks. These models learn action policies from large-scale demonstration datasets and can generalize to new instructions, objects, and scenes. Yet when deployed in cluttered environments where non-target objects densely surround the manipulation target, VLAs frequently produce trajectories that collide with surrounding obstacles. The demonstration data used for training typically features unobstructed workspaces, and the resulting policies have no explicit incentive to maintain clearance from nearby surfaces. Collisions cause task failure, risk damage to the robot and surrounding objects, and represent a critical barrier to safe deployment in household and industrial settings. The SafeLIBERO benchmark~\cite{hu2025vlsa}, comprising 32 collision scenarios across 1,600 evaluation episodes, was introduced to systematically quantify this failure mode and confirms that even high-performing VLAs exhibit substantial collision rates in constrained workspaces. The root cause is architectural: current VLAs observe scenes through 2D images, generate action sequences through learned policies, and have no internal mechanism to determine whether the predicted end-effector trajectory will intersect obstacle surfaces.
4	
5	Recent work addresses this problem, but exclusively through mechanisms external to the VLA's internal representations. AEGIS~\cite{hu2025vlsa} introduces a plug-in safety constraint layer based on Control Barrier Functions (CBFs): it identifies obstacles via open-set detection and depth estimation, then corrects unsafe actions after they have been generated, and achieves a Collision Avoidance Rate (CAR) of 77.85\% on SafeLIBERO. SafeVLA~\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\% through reward shaping during reinforcement learning; this approach, however, does not incorporate geometric information about the workspace and relies entirely on learned reward signals to encode safety. CoFreeVLA~\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that detects dangerous configurations and halts execution when predicted collision risk exceeds a threshold. These approaches share a common architectural pattern: the safety mechanism operates independently of the VLA's learned feature representations. The model first generates a trajectory without collision awareness, and a separate module then evaluates or corrects it. This reactive paradigm faces two fundamental limitations. In cluttered environments, the space available for post-hoc trajectory correction shrinks, and corrections may push the end-effector into other obstacles. Because the VLA itself never learns to represent collision geometry, it cannot anticipate obstacles during action generation and will repeatedly propose unsafe trajectories that require external intervention. A proactive alternative would embed collision-relevant geometric information directly into the VLA's forward pass, so that action tokens encode collision awareness from the point of generation.
6	
7	A parallel research direction has enriched VLA architectures with 3D spatial information. Over fourteen recent methods integrate depth maps, point clouds, or implicit 3D representations into VLA training or inference: DepthVLA~\cite{depthvla2025}, QDepth-VLA~\cite{li2025qdepth}, Spatial Forcing~\cite{li2025spatialforcing}, 3D-CAVLA~\cite{3dcavla2025}, GeoAware-VLA~\cite{geoaware2025}, SpatialVLA~\cite{spatialvla2025}, GST-VLA~\cite{gstvla2026}, StemVLA~\cite{stemvla2026}, ST-VLA~\cite{stvla2026}, Evo-0~\cite{evo02025}, SA-VLA~\cite{savla2026}, AugVLA-3D~\cite{augvla3d2026}, and Evo-Depth~\cite{evodepth2026}, among others. These methods improve task success rate, viewpoint generalization, or grasping precision, but none targets collision avoidance as a design objective and none evaluates on collision-specific metrics. QDepth-VLA, the closest methodological precedent for auxiliary spatial supervision in VLAs, uses quantized depth prediction as a training-time auxiliary task via a VQ-VAE decoder. Depth, however, is a 2.5D camera-frame representation: it encodes the distance from each pixel to the camera, and its gradients reside in image space. Deriving collision-relevant directions in the robot's workspace from these gradients requires an implicit perspective-to-workspace coordinate transformation that depends on camera intrinsics and extrinsics, and occluded regions (where obstacles may be hidden behind the robot arm or other objects) produce no depth signal. The result is a clear gap between two active communities: spatially-aware VLAs do not address collision avoidance, and collision-safe VLAs do not internalize spatial geometry into the model's representations.
8	
9	We propose ColliForce-VLA, which integrates a differentiable workspace Signed Distance Field (SDF) into the VLA forward pass for collision-aware action generation. Workspace SDF encodes, at each 3D point, the signed distance to the nearest obstacle surface; its spatial gradient points directly away from that surface in workspace coordinates. Unlike depth gradients that reside in camera frame, SDF gradients require no coordinate transformation and cover the full 3D workspace including occluded regions. SDF gradients indicate repulsion direction from obstacles by construction, and their continuous nature provides informative signals even at moderate distances from surfaces, in contrast to binary occupancy whose gradient is zero almost everywhere. ColliForce-VLA augments $\pi_0$~\cite{black2024pi0} with two lightweight modules attached to the action expert: an SDF Decoder (4-layer MLP, ${\sim}$395K parameters) that predicts workspace SDF from the action expert's pooled suffix features, and an End-Effector (EE) Extractor (2-layer MLP, ${\sim}$263K parameters) that predicts end-effector position from the same features. During training, for near-collision samples where predicted SDF at the end-effector is low, we compute $\nabla_z \Phi$, the gradient of predicted SDF with respect to the shared feature representation $z$, and perform gradient ascent ($z' = z + \alpha \cdot \nabla_z \Phi$) to push $z$ toward collision-free configurations. Both $z$ and $z'$ are projected into action token space, and a knowledge distillation loss trains LoRA parameters (${\sim}$33.5M) to reproduce the refined actions. At inference, only the base model with trained LoRA is active; neither auxiliary module participates, and the method incurs zero additional latency. Unlike AEGIS~\cite{hu2025vlsa}, which corrects trajectories after generation, ColliForce-VLA shapes the action generation process through internalized collision geometry. Unlike QDepth-VLA~\cite{li2025qdepth}, which provides camera-frame auxiliary supervision only at training time without influencing action token generation, our SDF gradient refinement operates in workspace frame and modulates the feature representations from which action tokens are decoded. The collision-avoidance capability is distilled into the model's own LoRA parameters, not maintained by an external safety layer.
10	
11	Our contributions are as follows:
12	\begin{itemize}
13	    \item We introduce a differentiable collision-aware mechanism for VLAs that integrates workspace SDF into the forward pass. SDF gradients in feature space ($\nabla_z \Phi$) guide action token generation toward collision-free configurations and provide a proactive alternative to post-hoc safety correction (Section~\ref{sec:method}).
14	    \item We design a knowledge distillation training strategy where an SDF gradient refiner serves as teacher and LoRA parameters as student. The model internalizes collision-avoidance behavior during training with zero additional inference cost (Section~\ref{sec:training}).
15	    \item We conduct systematic experiments and ablation studies on the SafeLIBERO benchmark that separately quantify the contributions of SDF auxiliary supervision and SDF gradient-guided refinement to Collision Avoidance Rate (CAR) and Task Success Rate (TSR) \textbf{[TODO: specific numbers pending experiments]} (Section~\ref{sec:experiments}).
16	\end{itemize}
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "710ffcf2-f2bd-4b63-9eac-61a4c1547d47"
}
```

</details>

---

### System

_source line 108_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/_project/paper/introduction_v2.tex",
  "usage": {
    "total_tokens": 72943,
    "tool_uses": 30,
    "duration_ms": 49486
  },
  "last_tool_name": "Read",
  "uuid": "0203bf0e-fbcb-4404-b1f7-e67358078324",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 109_

<details open><summary>🔧 Tool call — Read · `toolu_018i2y4R4k9ex3CykodFVVwf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/introduction_v2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "8ac902ff-24ad-4b34-8781-68e26e9ebfd4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LG2GRgapptdThxFhJzpb7R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12361,
      "cache_read_input_tokens": 60511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12361,
        "ephemeral_1h_input_tokens": 0
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

_source line 110 · 2026-05-27T13:13:29.091Z_

<details><summary>↩ Tool result · `toolu_018i2y4R4k9ex3CykodFVVwf`</summary>

```text
1	\section{Introduction}
2	
3	Vision-Language-Action (VLA) models unify visual perception, language understanding, and continuous action generation in a single architecture. Models such as $\pi_0$~\cite{black2024pi0}, OpenVLA~\cite{kim2024openvla}, and RT-2~\cite{brohan2023rt2} can follow diverse natural language instructions across manipulation tasks. As these models move toward real-world deployment, a critical failure mode has emerged: frequent collisions with non-target objects in cluttered environments. The demonstration data used for training typically features unobstructed workspaces, and the resulting policies acquire no explicit incentive to maintain clearance from nearby surfaces. Collisions cause task failure, risk damage to the robot and its surroundings, and represent a central barrier to safe deployment. The SafeLIBERO benchmark~\cite{hu2025vlsa}, comprising 32 collision scenarios across 1,600 evaluation episodes, was introduced to systematically quantify this problem and confirms that even high-performing VLAs exhibit substantial collision rates when non-target objects surround the manipulation target.
4	
5	Several recent methods target collision avoidance in VLAs. AEGIS~\cite{hu2025vlsa} applies post-hoc Control Barrier Function (CBF) corrections to already-generated trajectories and reports an average Collision Avoidance Rate (CAR) of 77.85\% across SafeLIBERO scenarios without additional training. SafeVLA~\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\% through reward shaping during reinforcement learning. CoFreeVLA~\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that halts execution when predicted collision risk exceeds a threshold. In our own experiments, a Pi0 model fine-tuned with an auxiliary Signed Distance Field (SDF) loss (referred to as A1-LoRA) achieves 91.5\% CAR on SafeLIBERO. These methods share a common evaluation pattern: they report high CAR as evidence of effective collision avoidance. The numbers appear compelling, and the implicit assumption across this emerging literature is that high CAR reflects genuine obstacle avoidance behavior.
6	
7	This assumption is wrong. We find that the high CAR values reported by these methods are systematically contaminated by \emph{action collapse}, a phenomenon in which the VLA ceases to produce meaningful motion. When we examine the end-effector displacement of the 732 episodes that A1-LoRA classifies as ``safe,'' 99.6\% exhibit a maximum displacement below 0.1\,mm. The robot did not avoid obstacles; it avoided motion altogether. This contamination is not specific to A1-LoRA or to SDF-based approaches. The LoRA baseline (no collision avoidance objective) achieves 82\% CAR with 99.4\% of its safe episodes below the displacement threshold. Pi0.5, a more capable model from the same family, exhibits the same pattern: 98.2\% of its safe episodes are fake safe. We acknowledge that action collapse itself is a well-documented failure mode of undertrained or distribution-shifted models, and its existence alone would not warrant a dedicated analysis. What is non-trivial is the \emph{consequence}: action collapse silently inflates the primary safety metric used to evaluate collision avoidance methods. Downstream researchers who compare methods based on reported CAR values will draw incorrect conclusions about relative safety. Models that collapse more severely will paradoxically appear safer, and genuinely unsafe models may be deployed on the basis of contaminated evaluations. We propose the displacement-filtered CAR (CAR$_\text{f}$), which excludes episodes with sub-threshold displacement from both numerator and denominator, as a corrective metric that separates genuine avoidance from inaction.
8	
9	The fake safety problem connects to two deeper structural issues. First, task capability and collision avoidance are anti-correlated under current evaluation practice. Pi0.5 achieves a TSR of 74.7\,$\pm$\,1.5\% but a CAR of only 26.8\,$\pm$\,1.6\%, while Pi0-based methods report CAR of 82--91.5\% alongside TSR $\leq$ 0.5\%. The explanation is mechanical: a model that moves the robot through the workspace encounters obstacles; a model that does not move encounters none. CAR is therefore informative only when conditioned on sufficient task capability, and the TSR-CAR plane reveals that no current method occupies the upper-right quadrant where both metrics are high. Second, end-effector-only SDF refinement, the most direct geometric approach to collision avoidance, has a structural defect. We construct oracle experiments that replace the learned SDF network with ground-truth signed distance fields computed from simulation geometry. All three oracle variants achieve \emph{lower} CAR than unrefined baselines (best oracle: 76.9\% vs.\ LoRA baseline: 82.0\%). The SDF gradient pushes the end-effector away from obstacles, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Perfect distance information at the end-effector cannot compensate for the absence of full-body collision awareness. A preliminary result provides a constructive counterpoint: a Pi0.5 model augmented with training-time SDF supervision (10K-step checkpoint) achieves CAR of 56--58\% with TSR of 47--49\% and a frozen-action rate of 0\%, placing it in the previously empty central region of the TSR-CAR plane which suggests that genuine collision avoidance is achievable when the base model retains sufficient capability.
10	
11	Our contributions are as follows:
12	\begin{itemize}
13	    \item We identify the fake safety problem in VLA collision avoidance evaluation: action collapse systematically inflates Collision Avoidance Rate, and we find that 98--99\% of safe episodes across multiple methods and model scales are attributable to inaction rather than obstacle avoidance. We propose displacement-filtered CAR (CAR$_\text{f}$) as a corrective metric (Section~\ref{sec:fake_safety}).
14	    \item We demonstrate that model capability and reported collision avoidance are anti-correlated under standard CAR evaluation. Models that execute tasks collide more because they move, while action-collapsed models receive inflated safety scores, rendering cross-method comparisons on raw CAR misleading (Section~\ref{sec:tsr_car}).
15	    \item Through ground-truth SDF oracle experiments, we establish that end-effector-only SDF refinement is a structural limitation: even perfect distance information cannot prevent full-body collisions, as gradients that repel the end-effector simultaneously drive arm links into obstacle volumes (Section~\ref{sec:ee_only}).
16	    \item[\textbf{[C4]}] Preliminary evidence from a Pi0.5 model with training-time SDF supervision shows 0\% frozen-action rate alongside CAR of 56--58\% and TSR of 47--49\%, suggesting that SDF auxiliary losses can produce genuine collision avoidance when applied to a VLA with sufficient baseline capability (Section~\ref{sec:a1_pi05}; full results pending).
17	\end{itemize}
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "66ac1e2d-e991-405a-9c12-6ff46c455f88"
}
```

</details>

---

### System

_source line 111_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/_project/paper/abstract_v2.tex",
  "usage": {
    "total_tokens": 72945,
    "tool_uses": 31,
    "duration_ms": 50068
  },
  "last_tool_name": "Read",
  "uuid": "21a2f8c3-77f2-45bb-92c4-f875e982a9bc",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 112_

<details open><summary>🔧 Tool call — Read · `toolu_01CbSwkBxiuX4W2uUVGgKv3m`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/abstract_v2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "ff2b135a-c364-43fa-9138-4f17a7f53a0f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LG2GRgapptdThxFhJzpb7R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12361,
      "cache_read_input_tokens": 60511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12361,
        "ephemeral_1h_input_tokens": 0
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

_source line 113 · 2026-05-27T13:13:29.674Z_

<details><summary>↩ Tool result · `toolu_01CbSwkBxiuX4W2uUVGgKv3m`</summary>

```text
1	\begin{abstract}
2	Recent methods for collision avoidance in Vision-Language-Action (VLA) models report high Collision Avoidance Rate (CAR) on safety benchmarks and claim effective obstacle avoidance. We show that these metrics are systematically contaminated by action collapse: the model ceases to produce meaningful motion, and the resulting inaction is counted as successful avoidance. On the SafeLIBERO benchmark, a Signed Distance Field (SDF)-augmented VLA reports 91.5\% CAR, yet 99.6\% of its safe episodes exhibit end-effector displacement below 0.1\,mm. This contamination is not method-specific; a baseline without any collision objective achieves 82\% CAR with 99.4\% of safe episodes below the same threshold, and a more capable model shows the same pattern. We propose displacement-filtered CAR (CAR$_\text{f}$), which excludes sub-threshold episodes, as a corrective metric. Further analysis reveals two structural issues. First, Task Success Rate (TSR) and CAR are anti-correlated: models that move the robot through the workspace collide, while collapsed models appear safe. Second, ground-truth SDF oracle experiments demonstrate that end-effector-only refinement cannot prevent full-body collisions, as SDF gradients that repel the end-effector simultaneously drive arm links into obstacle volumes. Preliminary results indicate that training-time SDF supervision on a sufficiently capable VLA can produce genuine collision avoidance with zero frozen-action rate. Our findings establish that displacement filtering is necessary for meaningful VLA safety evaluation.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "d6f9b4b9-bc85-4737-ba0a-254ac1be0a8d"
}
```

</details>

---

### System

_source line 114_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/dream_reports/dream_20260526T023936/median/paper.tex",
  "usage": {
    "total_tokens": 77505,
    "tool_uses": 32,
    "duration_ms": 55576
  },
  "last_tool_name": "Read",
  "uuid": "2d7805c0-eaad-403a-9f32-5c4cf6ab635a",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 115_

<details open><summary>🔧 Tool call — Read · `toolu_01BvCjqNJYMVe4P4thEf2eZG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/dream_reports/dream_20260526T023936/median/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "f10d7f67-4e81-403b-ab75-2197580df6b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TC9z5s46boaEVBXDDnNyio",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4558,
      "cache_read_input_tokens": 72872,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4558,
        "ephemeral_1h_input_tokens": 0
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

_source line 116 · 2026-05-27T13:13:35.485Z_

<details><summary>↩ Tool result · `toolu_01BvCjqNJYMVe4P4thEf2eZG`</summary>

```text
1	\documentclass[letterpaper]{article}
2	
3	\usepackage[utf8]{inputenc}
4	\usepackage[T1]{fontenc}
5	\usepackage{amsmath,amssymb}
6	\usepackage{booktabs}
7	\usepackage{multirow}
8	\usepackage{graphicx}
9	\usepackage{hyperref}
10	\usepackage[margin=1in]{geometry}
11	\usepackage{xcolor}
12	\usepackage{caption}
13	\usepackage{subcaption}
14	
15	\title{Rethinking VLA Safety Evaluation:\\When 98\% of Collision Avoidance is an Illusion}
16	
17	\author{
18	  Anonymous Authors
19	}
20	
21	\date{}
22	
23	\begin{document}
24	\maketitle
25	
26	%====================================================================
27	\begin{abstract}
28	%====================================================================
29	
30	Vision-Language-Action (VLA) models are increasingly deployed for robotic manipulation, yet their safety evaluation relies on collision avoidance rate (CAR)---a metric we show to be systematically contaminated. On the SafeLIBERO benchmark, a fully fine-tuned Pi0 model achieves 91.5\% CAR, but 99.6\% of its ``safe'' episodes exhibit end-effector displacement below 0.1\,mm: the robot is frozen, not collision-avoiding. We term this phenomenon \emph{fake safety} and propose displacement-filtered CAR (dfCAR), a corrected metric that is invariant to threshold choice across two orders of magnitude ($\delta \in [2\text{mm}, 200\text{mm}]$). Using dfCAR, we reveal that (i)~stronger base models complete more tasks but collide more, creating a capability--safety anti-correlation; (ii)~end-effector-only signed distance field (SDF) supervision suffers from a structural limitation where arm-body collisions dominate; and (iii)~LoRA fine-tuning on collision-free demonstrations produces genuine collision avoidance (+26\,pp CAR over baseline, 0\% fake safety) \emph{without} explicit geometric supervision. Adding SDF auxiliary loss at standard hyperparameter ranges ($\lambda \leq 0.01$) contributes no additional benefit (3-seed $\Delta$CAR $\leq 2.3$\,pp, $p = 0.24$). Extreme SDF penalty ($\lambda = 0.1$) yields a marginal, statistically ambiguous CAR increase (${\sim}6$\,pp, $p = 0.15$) that does not justify the added complexity. All conditions suffer catastrophic task performance collapse (TSR: 73\%$\to$6\%), indicating the safety--capability tradeoff is a property of fine-tuning itself, not geometric supervision.
31	
32	\end{abstract}
33	
34	%====================================================================
35	\section{Introduction}
36	\label{sec:intro}
37	%====================================================================
38	
39	Safety is a prerequisite for deploying robotic manipulation systems in human environments. As Vision-Language-Action (VLA) models scale in capability, evaluating whether they avoid collisions with obstacles has become critical. The standard metric---collision avoidance rate (CAR), the fraction of evaluation episodes without collision---appears straightforward. We demonstrate that it is fundamentally broken.
40	
41	\paragraph{The fake safety problem.}
42	When a VLA model undergoes full fine-tuning on limited safety-annotated data, it can exhibit \emph{action collapse}: the model outputs near-zero actions, the robot freezes in place, and episodes are scored as collision-free. On SafeLIBERO, a Pi0 model fine-tuned with SDF auxiliary loss (condition A1) achieves 91.5\% CAR---but its task success rate (TSR) is 0\%, and 99.6\% of safe episodes show obstacle displacement below 0.1\,mm (median ${\sim}5$\,nm). This is not collision avoidance; it is the absence of motion. We call this \emph{fake safety}.
43	
44	The contamination is not limited to action collapse. A Pi0.5 baseline (no fine-tuning) achieves 27\% CAR through geometric path safety---the robot's natural trajectory happens to avoid obstacles, not because the model reasons about safety. Standard CAR conflates three fundamentally different phenomena: action collapse, geometric path safety, and genuine collision avoidance.
45	
46	\paragraph{Contributions.} We make four contributions:
47	\begin{enumerate}
48	\item We identify and quantify fake safety in VLA evaluation, showing that standard CAR is systematically contaminated by action collapse (Section~\ref{sec:fake-safety}).
49	\item We propose \emph{displacement-filtered CAR} (dfCAR), a corrected metric that filters episodes by end-effector displacement. We show dfCAR is completely invariant to threshold choice over $\delta \in [2\text{mm}, 200\text{mm}]$ due to the extreme bimodality of VLA behavior (Section~\ref{sec:dfcar}).
50	\item We characterize the structural limitation of end-effector-only SDF supervision, where SDF gradients push the end-effector away from obstacles but cause the arm body to sweep through them (Section~\ref{sec:ee-limitation}).
51	\item We demonstrate that LoRA fine-tuning on collision-free demonstrations produces genuine collision avoidance without geometric supervision, and that SDF auxiliary loss is largely redundant at standard hyperparameter ranges---extreme $\lambda$ shows marginal, statistically ambiguous benefit that does not justify added complexity (Section~\ref{sec:attribution}).
52	\end{enumerate}
53	
54	
55	%====================================================================
56	\section{Related Work}
57	\label{sec:related}
58	%====================================================================
59	
60	\paragraph{VLA models for manipulation.}
61	Recent VLA models, including Pi0~\cite{black2024pi0}, Pi0.5, and OpenVLA~\cite{kim2024openvla}, have demonstrated strong manipulation capabilities by conditioning action prediction on vision and language inputs. These models are typically evaluated on task success rate, with safety considerations receiving less attention.
62	
63	\paragraph{Collision avoidance in robotics.}
64	Classical motion planning employs signed distance fields (SDFs) for obstacle avoidance, with well-understood guarantees in known environments. Integrating geometric supervision into learned policies---via auxiliary SDF losses or runtime gradient correction---is a natural extension, but its effectiveness in the VLA setting has not been rigorously evaluated.
65	
66	\paragraph{Safety evaluation metrics.}
67	Collision avoidance rate is the de facto standard for evaluating manipulation safety. SafeLIBERO provides a benchmark with instrumented collision detection. However, prior work has not examined whether CAR accurately reflects intentional collision avoidance behavior versus incidental collision-free outcomes.
68	
69	
70	%====================================================================
71	\section{Method}
72	\label{sec:method}
73	%====================================================================
74	
75	%--------------------------------------------------------------------
76	\subsection{Problem Setting}
77	%--------------------------------------------------------------------
78	
79	We consider a VLA policy $\pi_\theta(a_t \mid o_t, l)$ that predicts actions $a_t$ given visual observations $o_t$ and language instructions $l$. The policy controls a 7-DoF robot arm in tabletop manipulation tasks with obstacle objects. We evaluate on SafeLIBERO, which provides instrumented collision detection via object displacement thresholds.
80	
81	%--------------------------------------------------------------------
82	\subsection{Displacement-Filtered CAR (dfCAR)}
83	\label{sec:dfcar-method}
84	%--------------------------------------------------------------------
85	
86	Standard CAR counts an episode as ``safe'' if no collision is detected, regardless of whether the robot actually moved. We define displacement-filtered CAR to exclude episodes where the robot is effectively frozen:
87	
88	\begin{equation}
89	\text{dfCAR}(\delta) = \frac{|\{e : \text{safe}(e) \wedge \text{disp}_{\text{EE}}(e) > \delta\}|}{|\{e : \text{disp}_{\text{EE}}(e) > \delta\}|}
90	\label{eq:dfcar}
91	\end{equation}
92	
93	where $\text{disp}_{\text{EE}}(e)$ is the total end-effector displacement during episode $e$, and $\delta$ is a displacement threshold. By restricting the denominator to episodes with genuine robot motion, dfCAR eliminates the contribution of action-collapsed episodes.
94	
95	%--------------------------------------------------------------------
96	\subsection{SDF Auxiliary Loss}
97	\label{sec:sdf-loss}
98	%--------------------------------------------------------------------
99	
100	We augment the standard action prediction loss with an SDF-based collision penalty:
101	
102	\begin{equation}
103	\mathcal{L} = \mathcal{L}_{\text{action}} + \lambda \cdot \mathcal{L}_{\text{SDF}}
104	\label{eq:total-loss}
105	\end{equation}
106	
107	where $\mathcal{L}_{\text{SDF}}$ penalizes predicted end-effector positions that are close to obstacle surfaces (low SDF values). The SDF field is computed from known obstacle geometry and provides differentiable distance gradients. We evaluate $\lambda \in \{0, 0.005, 0.01, 0.1\}$.
108	
109	%--------------------------------------------------------------------
110	\subsection{LoRA Fine-Tuning}
111	\label{sec:lora}
112	%--------------------------------------------------------------------
113	
114	We apply Low-Rank Adaptation (LoRA) to fine-tune VLA models on collision-free demonstration subsets from SafeLIBERO. The demonstrations are filtered to include only episodes where no collision occurs during the original task execution, providing an implicit avoidance signal without explicit geometric annotation. All LoRA configurations use identical rank and learning rate; only the SDF loss weight $\lambda$ varies across conditions.
115	
116	
117	%====================================================================
118	\section{Experiments}
119	\label{sec:experiments}
120	%====================================================================
121	
122	%--------------------------------------------------------------------
123	\subsection{Experimental Setup}
124	%--------------------------------------------------------------------
125	
126	\paragraph{Benchmark.} All experiments use SafeLIBERO with instrumented collision detection. We evaluate on two scene types: \texttt{object\_pudding} (4 tasks: orange\_juice, chocolate\_pudding, milk, bbq\_sauce) and \texttt{spatial\_bowl} (4 tasks: bowl placement variants). Each evaluation consists of 200 episodes (50 per task).
127	
128	\paragraph{Models.} We evaluate Pi0 (full fine-tune, condition A1), Pi0.5 (no fine-tune baseline), and Pi0.5 + LoRA with varying SDF loss weights.
129	
130	\paragraph{Metrics.} We report CAR, dfCAR, TSR, end-effector displacement (EE disp), and frozen episode percentage. Statistical comparisons use Welch's $t$-test (one-sided) across seeds.
131	
132	
133	%--------------------------------------------------------------------
134	\subsection{Fake Safety in Standard CAR}
135	\label{sec:fake-safety}
136	%--------------------------------------------------------------------
137	
138	Table~\ref{tab:fake-safety} presents the core fake safety finding. The Pi0 model (A1) achieves 91.5\% CAR---the highest among all conditions---yet its TSR is 0\% and 99.6\% of safe episodes show obstacle displacement below 0.1\,mm (median ${\sim}$5\,nm). The robot is frozen in place, producing collision-free episodes by inaction rather than avoidance.
139	
140	In contrast, the Pi0.5 baseline achieves only 27.0\% CAR, but with TSR = 74.7\% and substantial end-effector displacement (${\sim}$0.15\,m). Its safe episodes reflect geometric path safety---the robot's trajectory happens to avoid obstacles---not intentional avoidance behavior.
141	
142	\begin{table}[t]
143	\centering
144	\caption{Fake safety decomposition. A1 (Pi0, full fine-tune) achieves the highest CAR through action collapse (EE disp $<$ 1\,$\mu$m), not collision avoidance. Pi0.5 baseline achieves genuine motion but low CAR due to more collisions. dfCAR (Eq.~\ref{eq:dfcar}, $\delta = 100$\,mm) corrects for frozen episodes.}
145	\label{tab:fake-safety}
146	\begin{tabular}{lcccccc}
147	\toprule
148	Condition & CAR (\%) & dfCAR (\%) & TSR (\%) & EE Disp (m) & Frozen (\%) & Seeds \\
149	\midrule
150	A1 (Pi0, full FT) & 91.5 & 0.4 & 0.0 & $<$0.001 & 99.6 & 3 \\
151	Pi0.5 baseline & 27.0 & 27.0 & 74.7 & 0.15 & 0 & 3 \\
152	LoRA-only (Pi0.5) & 52.8 & 52.8 & 5.8 & 0.48 & 0 & 3 \\
153	SDF $\lambda{=}0.005$ & 50.5 & 50.5 & 6.8 & 0.48 & 0 & 3 \\
154	SDF $\lambda{=}0.01$ & 52.7 & 52.7 & 7.0 & 0.48 & 0 & 3 \\
155	\bottomrule
156	\end{tabular}
157	\end{table}
158	
159	
160	%--------------------------------------------------------------------
161	\subsection{dfCAR Threshold Sensitivity}
162	\label{sec:dfcar}
163	%--------------------------------------------------------------------
164	
165	A practical metric must not require careful threshold tuning. Table~\ref{tab:dfcar-sensitivity} shows that dfCAR is \emph{completely invariant} to threshold choice across two orders of magnitude ($\delta \in [2\text{mm}, 100\text{mm}]$).
166	
167	\begin{table}[t]
168	\centering
169	\caption{dfCAR threshold sensitivity. The metric is invariant across $\delta \in [2, 100]$\,mm due to the extreme bimodality of EE displacement: action-collapsed episodes show displacement $<$1\,$\mu$m while genuinely active episodes show displacement $>$239\,mm. This six-order-of-magnitude gap eliminates the need for threshold tuning.}
170	\label{tab:dfcar-sensitivity}
171	\begin{tabular}{lccccccc}
172	\toprule
173	Condition & Raw CAR & $\delta{=}2$ & $\delta{=}5$ & $\delta{=}10$ & $\delta{=}20$ & $\delta{=}50$ & $\delta{=}100$ \\
174	\midrule
175	A1 (Pi0, collapse) & 91.5 & 0.4 & 0.4 & 0.4 & 0.0 & 0.0 & 0.0 \\
176	LoRA-only (Pi0.5) & 52.8 & 52.8 & 52.8 & 52.8 & 52.8 & 52.8 & 52.8 \\
177	SDF $\lambda{=}0.01$ & 52.7 & 52.7 & 52.7 & 52.7 & 52.7 & 52.7 & 52.7 \\
178	Pi0.5 baseline & 27.0 & 27.0 & 27.0 & 27.0 & 27.0 & 27.0 & 27.0 \\
179	\bottomrule
180	\end{tabular}
181	\end{table}
182	
183	The invariance arises from a fundamental bimodality in VLA end-effector behavior. Table~\ref{tab:ee-distribution} summarizes the displacement distributions.
184	
185	\begin{table}[t]
186	\centering
187	\caption{End-effector displacement distribution by condition. Action-collapsed models (A1) exhibit displacement $<$1\,mm while all other conditions show minimum displacement $>$100\,mm, creating a six-order-of-magnitude gap.}
188	\label{tab:ee-distribution}
189	\begin{tabular}{lcccc}
190	\toprule
191	Condition & Min EE Disp & Median EE Disp & Max EE Disp & Gap Factor \\
192	\midrule
193	A1 safe episodes & ${\sim}$5\,nm & ${\sim}$5\,nm & 0.9\,mm & ref \\
194	LoRA-only all episodes & 239\,mm & 420\,mm & 780\,mm & 239{,}000$\times$ \\
195	SDF all episodes & 245\,mm & 415\,mm & 765\,mm & 245{,}000$\times$ \\
196	Pi0.5 baseline all & 110\,mm & 150\,mm & 580\,mm & 110{,}000$\times$ \\
197	\bottomrule
198	\end{tabular}
199	\end{table}
200	
201	
202	%--------------------------------------------------------------------
203	\subsection{Capability--Safety Anti-Correlation}
204	\label{sec:capability-safety}
205	%--------------------------------------------------------------------
206	
207	We observe an anti-correlation between task capability and collision avoidance across model families. Pi0.5 (TSR = 74.7\%, CAR = 27.0\%) completes far more tasks than Pi0/A1 (TSR = 0\%, CAR = 91.5\%), but produces more collisions. The Pi0.5 baseline's 27\% CAR reflects genuine robot motion through cluttered environments, while A1's 91.5\% CAR is entirely fake.
208	
209	This suggests a fundamental tension: models capable enough to attempt tasks necessarily move through collision-prone regions, while incapable models trivially achieve ``safety'' through inaction. We present this as an empirical observation rather than a causal claim, noting that the comparison involves models of different architecture generations.
210	
211	
212	%--------------------------------------------------------------------
213	\subsection{EE-Only SDF Structural Limitation}
214	\label{sec:ee-limitation}
215	%--------------------------------------------------------------------
216	
217	End-effector-only SDF supervision suffers from a structural scope limitation: SDF gradients push the end-effector away from obstacles, but the resulting trajectories can cause the arm body to sweep through obstacle volumes. We evaluated three oracle variants---adaptive-alpha runtime correction, fixed-alpha correction, and feature-space SDF---all of which performed below the unmodified baseline on SafeLIBERO.
218	
219	The \texttt{spatial\_bowl} scene, where obstacles are densely packed around the target object, amplifies this limitation. With SDF + LoRA ($\lambda = 0.005$), CAR reaches only 35\% (Table~\ref{tab:spatial-bowl}), substantially below \texttt{object\_pudding} performance (50.5\%). The lower EE displacement (0.25\,m vs.\ 0.48\,m) reflects the constrained workspace rather than action collapse (frozen\_pct = 0\%).
220	
221	\begin{table}[t]
222	\centering
223	\caption{Per-task breakdown on \texttt{spatial\_bowl} (SDF $\lambda{=}0.005$, seed0, 200 episodes). CAR is lower than \texttt{object\_pudding} due to denser obstacle configurations. No LoRA-only control was available for this scene, precluding SDF attribution.}
224	\label{tab:spatial-bowl}
225	\begin{tabular}{lccc}
226	\toprule
227	Task & CAR (\%) & TSR (\%) & EE Disp (m) \\
228	\midrule
229	bowl\_between\_plate\_ramekin & 38 & 4 & 0.263 \\
230	bowl\_on\_ramekin & 28 & 0 & 0.231 \\
231	bowl\_on\_stove & 48 & 6 & 0.274 \\
232	bowl\_on\_cabinet & 26 & 2 & 0.224 \\
233	\midrule
234	Mean & 35 & 3 & 0.248 \\
235	\bottomrule
236	\end{tabular}
237	\end{table}
238	
239	
240	%--------------------------------------------------------------------
241	\subsection{Fine-Tuning Attribution: Demonstrations vs.\ Geometric Supervision}
242	\label{sec:attribution}
243	%--------------------------------------------------------------------
244	
245	We now address whether collision avoidance arises from explicit geometric supervision (SDF loss) or implicit signals in collision-free demonstrations (LoRA fine-tuning alone).
246	
247	\subsubsection{LoRA-Only Produces Genuine Collision Avoidance}
248	
249	LoRA fine-tuning on collision-free demonstrations, \emph{without any SDF loss}, achieves 52.8\% CAR (3 seeds, $\pm$4.2\,pp SD) compared to the Pi0.5 baseline of 27.0\%---a +26\,pp improvement. All episodes show substantial EE displacement (min 239\,mm, mean 480\,mm) with 0\% frozen episodes, confirming genuine collision avoidance behavior rather than action collapse.
250	
251	\subsubsection{SDF Adds No Benefit at Standard $\lambda$}
252	
253	Table~\ref{tab:3v3} presents the 3-seed-vs-3-seed comparison between LoRA-only and SDF conditions. At $\lambda = 0.005$, mean CAR is 50.5\% ($\Delta = -2.3$\,pp vs.\ LoRA-only, $p = 0.24$). At $\lambda = 0.01$, mean CAR is 52.7\% ($\Delta = -0.1$\,pp, $p = 0.48$). Neither difference is statistically significant, and the effect sizes are well within evaluation noise.
254	
255	\begin{table}[t]
256	\centering
257	\caption{3v3 seed-level comparison: LoRA-only vs.\ SDF. The mean CAR difference is not statistically significant at either $\lambda$ value. SDF $\lambda{=}0.01$ shows notably lower cross-seed variance (SD = 0.3\,pp), suggesting a possible regularization effect, but this does not translate to performance gains.}
258	\label{tab:3v3}
259	\begin{tabular}{lcccccc}
260	\toprule
261	Condition & Seed 0 & Seed 1 & Seed 2 & Mean & SD & $p$ (one-sided) \\
262	\midrule
263	\multicolumn{7}{l}{\textit{CAR (\%)}} \\
264	LoRA-only & 54.5 & 56.0 & 48.0 & 52.8 & 4.2 & ref \\
265	SDF $\lambda{=}0.005$ & 47.0 & 51.5 & 53.0 & 50.5 & 3.0 & 0.24 \\
266	SDF $\lambda{=}0.01$ & 52.5 & 52.5 & 53.0 & 52.7 & 0.3 & 0.48 \\
267	\midrule
268	\multicolumn{7}{l}{\textit{TSR (\%)}} \\
269	LoRA-only & 8.5 & 4.0 & 5.0 & 5.8 & 2.3 & --- \\
270	SDF $\lambda{=}0.005$ & 7.5 & 4.0 & 9.0 & 6.8 & 2.5 & --- \\
271	SDF $\lambda{=}0.01$ & 6.5 & 7.5 & 7.5 & 7.2 & 0.6 & --- \\
272	\bottomrule
273	\end{tabular}
274	\end{table}
275	
276	Per-task CAR patterns are consistent across all conditions: \texttt{milk} achieves the highest CAR (78--94\%) due to favorable obstacle placement, while \texttt{bbq\_sauce} achieves the lowest (18--28\%) due to severe obstacle occlusion. This task-specific pattern is preserved identically whether or not SDF loss is applied, indicating that CAR is driven by task layout and demonstration imitation, not geometric supervision.
277	
278	\subsubsection{Lambda Dose-Response: Marginal Effect at Extreme Values}
279	
280	To test whether SDF becomes relevant at higher penalty weights, we evaluate $\lambda = 0.1$ (Table~\ref{tab:lambda-curve}). This 10$\times$ increase in SDF weight yields a modest CAR increase to 58.5\% (2 seeds, $\Delta = +5.7$\,pp vs.\ LoRA-only). However, this improvement is not statistically significant ($p = 0.15$, 2-seed) and comes at the cost of further task performance degradation (TSR: 5.8\%$\to$4.0\%) and substantially higher training loss (0.038 vs.\ 0.014).
281	
282	\begin{table}[t]
283	\centering
284	\caption{Four-point lambda dose-response curve. CAR shows a weak positive trend with increasing $\lambda$, but the effect is sublinear (regression slope = 0.75\,pp per 0.01$\lambda$) and the marginal gain at $\lambda{=}0.1$ is not statistically significant. TSR monotonically decreases.}
285	\label{tab:lambda-curve}
286	\begin{tabular}{lccccc}
287	\toprule
288	$\lambda$ & CAR Mean (\%) & CAR SD & TSR Mean (\%) & Seeds & $\Delta$ vs LoRA \\
289	\midrule
290	0 (LoRA-only) & 52.8 & 4.2 & 5.8 & 3 & ref \\
291	0.005 & 50.5 & 3.0 & 6.8 & 3 & $-$2.3 \\
292	0.01 & 52.7 & 0.3 & 7.0 & 3 & $-$0.1 \\
293	0.1 & 58.5 & 2.1 & 4.0 & 2 & +5.7 \\
294	\bottomrule
295	\end{tabular}
296	\end{table}
297	
298	\begin{table}[t]
299	\centering
300	\caption{Per-task breakdown for $\lambda{=}0.1$ (2 seeds, 200 episodes each). The task-specific CAR pattern is preserved (milk $>$ orange\_juice $>$ chocolate\_pudding $>$ bbq\_sauce), consistent with LoRA-only and lower-$\lambda$ conditions.}
301	\label{tab:lambda01-pertask}
302	\begin{tabular}{lcccccc}
303	\toprule
304	Task & s0 CAR & s0 TSR & s1 CAR & s1 TSR & Mean CAR \\
305	\midrule
306	orange\_juice & 72 & 0 & 70 & 2 & 71 \\
307	chocolate\_pudding & 46 & 16 & 50 & 14 & 48 \\
308	milk & 90 & 0 & 92 & 0 & 91 \\
309	bbq\_sauce & 20 & 0 & 28 & 0 & 24 \\
310	\midrule
311	Mean & 57 & 4 & 60 & 4 & 58.5 \\
312	\bottomrule
313	\end{tabular}
314	\end{table}
315	
316	The dose-response is sublinear: $\lambda$ increases 20$\times$ from 0.005 to 0.1, but CAR increases only ${\sim}$8\,pp. Three factors likely contribute to this ceiling: (i)~EE-only SDF cannot prevent arm-body collisions, which dominate in cluttered scenes; (ii)~the demonstration signal already captures most learnable avoidance behavior; (iii)~higher $\lambda$ primarily suppresses motion rather than improving trajectory quality, as evidenced by the concurrent TSR decrease.
317	
318	
319	%--------------------------------------------------------------------
320	\subsection{Phase 2: SDF Persistence After Loss Removal}
321	\label{sec:phase2}
322	%--------------------------------------------------------------------
323	
324	We investigate whether SDF training leaves a persistent imprint by training with SDF loss ($\lambda = 0.005$) for 10K steps, then continuing for 20K steps with $\lambda = 0$ (Phase 2). If SDF supervision encodes lasting geometric awareness, CAR should remain elevated relative to LoRA-only training.
325	
326	Table~\ref{tab:phase2} shows Phase 2 results across 2 seeds. Mean CAR is 59.5\% ($\Delta = +6.7$\,pp vs.\ LoRA-only, $p = 0.12$ one-sided). TSR partially recovers to 16.5\%, higher than both LoRA-only (5.8\%) and standard SDF conditions (${\sim}$7\%), because the $\lambda = 0$ phase allows partial re-optimization toward task completion.
327	
328	\begin{table}[t]
329	\centering
330	\caption{Phase 2 results (10K SDF $\to$ 20K $\lambda{=}0$). The weak CAR elevation and partial TSR recovery are consistent across seeds but not statistically significant. TSR remains far below the Pi0.5 baseline (73\%).}
331	\label{tab:phase2}
332	\begin{tabular}{lccc}
333	\toprule
334	Phase 2 Seed & CAR (\%) & TSR (\%) & EE Disp (m) \\
335	\midrule
336	seed2 (from s2 10K ckpt) & 61 & 18 & 0.462 \\
337	seed0 (from s0 10K ckpt) & 58 & 15 & 0.455 \\
338	\midrule
339	Mean & 59.5 & 16.5 & 0.459 \\
340	\bottomrule
341	\end{tabular}
342	\end{table}
343	
344	\begin{table}[t]
345	\centering
346	\caption{Persistence comparison across all conditions. Phase 2 and $\lambda{=}0.1$ show similar marginal CAR elevations (${\sim}$6\,pp) over LoRA-only, both with $p > 0.1$. Neither achieves practical significance given TSR collapse.}
347	\label{tab:persistence}
348	\begin{tabular}{lcccc}
349	\toprule
350	Condition & CAR (\%) & TSR (\%) & $\Delta$CAR vs LoRA & $p$ (one-sided) \\
351	\midrule
352	LoRA-only (3 seeds) & 52.8 & 5.8 & ref & ref \\
353	SDF $\lambda{=}0.005$ (3 seeds) & 50.5 & 6.8 & $-$2.3 & 0.24 \\
354	SDF $\lambda{=}0.01$ (3 seeds) & 52.7 & 7.0 & $-$0.1 & 0.48 \\
355	Phase 2 (2 seeds) & 59.5 & 16.5 & +6.7 & 0.12 \\
356	$\lambda{=}0.1$ (2 seeds) & 58.5 & 4.0 & +5.7 & 0.15 \\
357	\bottomrule
358	\end{tabular}
359	\end{table}
360	
361	We interpret the Phase 2 signal as weak and practically insignificant. While the trend is consistent across both seeds, the effect size (+6.7\,pp) is within the range of evaluation noise given the high seed-to-seed variance of LoRA fine-tuning (SD = 4.2\,pp). Critically, TSR remains collapsed at 16.5\%---far below any practical utility threshold---meaning the two-phase strategy does not recover task capability.
362	
363	
364	%====================================================================
365	\section{Discussion}
366	\label{sec:discussion}
367	%====================================================================
368	
369	\paragraph{Lambda dose-response ceiling.}
370	The sublinear relationship between SDF loss weight and collision avoidance rate reveals a practical ceiling on geometric supervision's contribution. Increasing $\lambda$ by 20$\times$ (from 0.005 to 0.1) yields only ${\sim}$8\,pp additional CAR, while training loss nearly triples (0.014 $\to$ 0.038) and TSR drops further. Three mechanisms likely explain this ceiling. First, EE-only SDF fundamentally cannot address arm-body collisions, which constitute a substantial fraction of collision events in cluttered environments. Second, the collision-free demonstrations already encode most learnable avoidance behavior---SDF supervision is largely redundant with the implicit signal. Third, at extreme $\lambda$ values, the SDF penalty increasingly suppresses motion (evidenced by reduced EE displacement at $\lambda = 0.1$: 0.45\,m vs.\ 0.48\,m at lower $\lambda$) rather than improving trajectory quality, producing a form of ``conservative avoidance'' rather than genuine safety awareness.
371	
372	These findings suggest that SDF geometric supervision provides no practically significant benefit at standard hyperparameter ranges ($\lambda \leq 0.01$). At extreme $\lambda$ values, a marginal, statistically ambiguous benefit emerges (${\sim}$6\,pp, $p = 0.15$), but this does not justify the added implementation complexity, computational overhead, and further task performance degradation.
373	
374	\paragraph{Phase 2 weak persistence.}
375	The observation that Phase 2 training (SDF removal after 10K steps) shows a weak CAR elevation ($+$6.7\,pp, $p = 0.12$) suggests SDF training may modify the model's loss landscape in a partially persistent manner. However, this signal is weak and practically insignificant: TSR remains collapsed at 16.5\%, far below the 73\% baseline. The two-phase strategy---first train for safety, then recover task capability---does not succeed under current LoRA fine-tuning configurations.
376	
377	\paragraph{Cross-scene generalization.}
378	The \texttt{spatial\_bowl} experiment demonstrates that SDF + LoRA fine-tuning produces genuine collision avoidance (CAR = 35\%, 0\% fake safety) in a second scene type with denser obstacle configurations. However, the absence of a LoRA-only control for \texttt{spatial\_bowl} precludes SDF attribution in this scene. The 35\% CAR may be entirely attributable to LoRA fine-tuning, as was the case for \texttt{object\_pudding}. Cross-scene SDF attribution remains an open question for future work.
379	
380	\paragraph{Catastrophic task performance collapse.}
381	All fine-tuning conditions---LoRA-only and LoRA + SDF at all $\lambda$ values---produce severe TSR degradation (73\% $\to$ 4--7\%), with Phase 2 showing partial but insufficient recovery (16.5\%). This collapse is a property of LoRA fine-tuning on limited safety-oriented data, not a consequence of SDF supervision specifically. The model learns conservative behavior (suppress risky motions) rather than safe behavior (navigate around obstacles while completing tasks). Addressing this collapse---potentially through larger demonstration sets, multi-task objectives, or replay mechanisms---is a critical direction for practical VLA safety.
382	
383	\paragraph{Limitations.}
384	Our study has several limitations. (i) All experiments use SafeLIBERO with Pi0/Pi0.5 model families; generalizability to other benchmarks and VLA architectures requires further validation. (ii) The 3v3 seed comparison provides limited statistical power ($n=3$ per condition); formal equivalence testing would require larger sample sizes. (iii) The spatial\_bowl SDF attribution is incomplete due to the missing LoRA-only control experiment. (iv) We evaluate only EE-only SDF; full-body SDF supervision may yield different results. (v) Phase 2 results are based on 2 seeds and should be considered preliminary.
385	
386	
387	%====================================================================
388	\section{Conclusion}
389	\label{sec:conclusion}
390	%====================================================================
391	
392	We have demonstrated that standard collision avoidance rate is a systematically contaminated metric for VLA safety evaluation. On SafeLIBERO, 98\% of ``safe'' behavior is either action collapse (frozen robot) or geometric path safety (incidental avoidance), not genuine collision avoidance. Our proposed displacement-filtered CAR (dfCAR) provides a robust correction that requires no threshold tuning.
393	
394	Using dfCAR, we show that LoRA fine-tuning on collision-free demonstrations produces genuine collision avoidance (+26\,pp over baseline, 0\% fake safety) through implicit signals in the training data. Explicit SDF geometric supervision is largely redundant: at standard hyperparameter ranges ($\lambda \leq 0.01$), it contributes no additional benefit; at extreme values ($\lambda = 0.1$), it provides a marginal, statistically ambiguous improvement (${\sim}$6\,pp) that does not justify added complexity. All conditions suffer catastrophic task performance collapse (TSR: 73\% $\to$ 6\%), revealing that current fine-tuning approaches produce conservative avoidance rather than genuine safety awareness.
395	
396	These findings have direct implications for the VLA safety research community: (i)~published CAR numbers should be re-examined for fake safety contamination; (ii)~geometric supervision methods should be benchmarked against demonstration-only baselines; and (iii)~the safety--capability tradeoff in fine-tuning demands new approaches that go beyond auxiliary loss design.
397	
398	
399	%====================================================================
400	% References
401	%====================================================================
402	
403	\bibliographystyle{plain}
404	
405	\begin{thebibliography}{10}
406	
407	\bibitem{black2024pi0}
408	K.~Black, N.~Brown, D.~Driess, A.~Escontrela, M.~Golber, K.~Gopalakrishnan, et~al.
409	\newblock $\pi_0$: A vision-language-action flow model for general robot control.
410	\newblock \emph{arXiv preprint arXiv:2410.24164}, 2024.
411	
412	\bibitem{kim2024openvla}
413	M.~J. Kim, K.~Pertsch, S.~Karamcheti, T.~Xiao, A.~Balakrishna, S.~Nair, et~al.
414	\newblock {OpenVLA}: An open-source vision-language-action model.
415	\newblock \emph{arXiv preprint arXiv:2406.09246}, 2024.
416	
417	\bibitem{safelibero}
418	Z.~Li, Y.~Chen, et~al.
419	\newblock {SafeLIBERO}: Benchmarking safety in robot manipulation.
420	\newblock \emph{arXiv preprint}, 2025.
421	
422	\bibitem{hu2022lora}
423	E.~J. Hu, Y.~Shen, P.~Wallis, Z.~Allen-Zhu, Y.~Li, S.~Wang, L.~Wang, and W.~Chen.
424	\newblock {LoRA}: Low-rank adaptation of large language models.
425	\newblock In \emph{ICLR}, 2022.
426	
427	\bibitem{ratliff2009chomp}
428	N.~Ratliff, M.~Zucker, J.~A. Bagnell, and S.~Srinivasa.
429	\newblock {CHOMP}: Gradient optimization techniques for efficient motion planning.
430	\newblock In \emph{ICRA}, 2009.
431	
432	\end{thebibliography}
433	
434	\end{document}
435	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "b9ee1ce1-04f5-433f-b4a5-48d4793f23ca"
}
```

</details>

---

### System

_source line 117_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/dream_reports/dream_20260526T023936/worst/paper.tex",
  "usage": {
    "total_tokens": 77506,
    "tool_uses": 33,
    "duration_ms": 56059
  },
  "last_tool_name": "Read",
  "uuid": "8121ff0a-c67b-46a0-9007-fb9b41b72acc",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 118_

<details open><summary>🔧 Tool call — Read · `toolu_01LaT7nNWzMimTseC8Yxk9Cd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/dream_reports/dream_20260526T023936/worst/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "04f6bc8d-14bd-4154-885b-6cfc01fc9caa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TC9z5s46boaEVBXDDnNyio",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4558,
      "cache_read_input_tokens": 72872,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4558,
        "ephemeral_1h_input_tokens": 0
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

_source line 119 · 2026-05-27T13:13:36.014Z_

<details><summary>↩ Tool result · `toolu_01LaT7nNWzMimTseC8Yxk9Cd`</summary>

```text
1	\documentclass[letterpaper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{amsmath,amssymb}
4	\usepackage{booktabs}
5	\usepackage{multirow}
6	\usepackage{graphicx}
7	\usepackage{xcolor}
8	\usepackage{hyperref}
9	\usepackage{natbib}
10	\usepackage{authblk}
11	\usepackage{caption}
12	\usepackage{subcaption}
13	\usepackage{tabularx}
14	
15	\title{Rethinking VLA Safety Evaluation: Decomposing Collision Avoidance\\into Implicit Demonstrations and Explicit Geometric Supervision}
16	
17	\author[1]{Anonymous Authors}
18	\affil[1]{Anonymous Institution}
19	\date{}
20	
21	\begin{document}
22	\maketitle
23	
24	%% ===================== ABSTRACT =====================
25	\begin{abstract}
26	Vision-Language-Action (VLA) models are increasingly deployed for robotic manipulation, yet their safety evaluation remains fundamentally flawed. Through a large-scale empirical study on SafeLIBERO (6000+ episodes across 2 model families and 2 scenes), we identify a systematic failure mode in the standard collision avoidance rate (CAR) metric: \emph{fake safety}. Models exhibiting action collapse (TSR=0\%) achieve 91.5\% CAR while their end-effector displacement remains below 0.005mm---the robot appears safe only because it is frozen. We propose displacement-filtered CAR (dfCAR), a corrected metric robust to threshold selection across three orders of magnitude ($\delta \in [2\text{mm}, 100\text{mm}]$). We then decompose the sources of genuine collision avoidance through controlled ablations. LoRA fine-tuning on collision-free demonstrations produces real avoidance (+29pp CAR over baseline, 0\% fake safety), but at catastrophic task performance cost (TSR: 73\%$\to$5\%). Critically, Signed Distance Field (SDF) auxiliary loss exhibits a dose-dependent effect: at low weighting ($\lambda \leq 0.01$) its contribution is statistically indistinguishable from zero, but at $\lambda=0.1$ it provides a significant additive +15.5pp CAR beyond demonstration-implicit signals ($p<0.02$). A two-phase training strategy---SDF pre-training followed by task-only fine-tuning---partially recovers task performance (TSR=40\%) while retaining elevated safety (CAR=66\%), suggesting curriculum-based approaches as a viable path. These findings reveal that VLA collision avoidance arises from a decomposable mixture of implicit demonstration signals and explicit geometric supervision, with implications for safety-aware fine-tuning design.
27	\end{abstract}
28	
29	%% ===================== INTRODUCTION =====================
30	\section{Introduction}
31	
32	As Vision-Language-Action (VLA) models transition from research prototypes to deployment candidates, ensuring their safe operation has become a critical concern. The robotics community has adopted collision avoidance rate (CAR) as a primary safety metric, measuring the fraction of evaluation episodes free of robot-obstacle collisions. However, CAR conflates fundamentally different behaviors under a single number: a robot that skillfully navigates around obstacles, a robot that follows a collision-free geometric path by chance, and a robot that simply does not move all receive equal credit.
33	
34	We present a systematic empirical investigation revealing that this conflation leads to dramatically misleading safety assessments. Our analysis centers on three findings:
35	
36	\textbf{(1) Fake Safety.}  On the SafeLIBERO benchmark, the Pi0 model fine-tuned with SDF auxiliary loss (condition A1) achieves 91.5\% CAR. However, it completes zero tasks (TSR=0\%), and 99.4\% of its ``safe'' episodes exhibit obstacle displacement below 0.1mm. The robot is not avoiding collisions---it has collapsed to a near-stationary policy. We propose displacement-filtered CAR (dfCAR), a corrected metric that separates genuine avoidance from action collapse. dfCAR is remarkably robust: the gap between fake and real safety spans three orders of magnitude in end-effector displacement, making the metric insensitive to threshold choice across $\delta \in [2, 100]$mm.
37	
38	\textbf{(2) Decomposing Avoidance Sources.} Through controlled 3-seed ablations comparing LoRA-only fine-tuning against LoRA+SDF at multiple loss weightings, we show that collision avoidance decomposes into two additive sources. The dominant source is \emph{implicit demonstration signals}: LoRA fine-tuning on collision-free demonstrations produces +29pp CAR over the pre-trained baseline without any explicit geometric supervision. The secondary source is \emph{explicit geometric supervision}: SDF auxiliary loss provides an additional +15.5pp CAR, but only at sufficiently high weighting ($\lambda=0.1$), below which the effect is masked by demonstration-implicit avoidance. This dose-response relationship explains why prior work may have dismissed geometric supervision as redundant.
39	
40	\textbf{(3) Two-Phase Training.} We discover that a curriculum strategy---first training with SDF loss to encode geometric awareness, then removing it to recover task capability---achieves CAR=66\% with TSR=40\% (2-seed mean), partially resolving the catastrophic safety-capability tradeoff inherent in end-to-end fine-tuning.
41	
42	Our contributions are: (i) identification and quantification of fake safety in VLA evaluation, with dfCAR as a principled corrective metric; (ii) a decomposition framework showing collision avoidance arises from implicit and explicit sources with a dose-dependent interaction; (iii) evidence that two-phase curriculum training can partially decouple safety from task performance. Together, these findings challenge the assumption that high CAR implies genuine safety and provide actionable guidance for safety-aware VLA fine-tuning.
43	
44	
45	%% ===================== RELATED WORK =====================
46	\section{Related Work}
47	
48	\textbf{VLA Safety Evaluation.} SafeLIBERO \citep{safelibero2025} introduced collision avoidance rate as a standardized metric for VLA safety in tabletop manipulation. While CAR provides a consistent evaluation protocol, it does not distinguish between different mechanisms that lead to collision-free episodes. Our work identifies systematic contamination of CAR by action collapse and geometric path safety, and proposes displacement-filtered CAR as a corrective.
49	
50	\textbf{Signed Distance Fields in Robotics.} SDFs have a long history in motion planning and collision checking \citep{ratliff2009chomp, zucker2013chomp}. Recent work has explored SDF representations learned from vision for real-time obstacle avoidance \citep{driess2022learning}. Our SDF auxiliary loss follows this line but applies it as a training-time signal for VLA fine-tuning rather than runtime planning, revealing a dose-dependent effect that low-weight SDF supervision is redundant with demonstration-implicit signals.
51	
52	\textbf{Safety-Capability Tradeoffs.} The tension between task performance and safety constraints is well-studied in reinforcement learning \citep{achiam2017constrained} and increasingly relevant for VLAs. Our finding that LoRA fine-tuning simultaneously improves CAR and degrades TSR echoes the conservatism-capability tradeoff in safe RL, but arises from a different mechanism: the model learns conservative behavior from demonstrations rather than from an explicit safety objective.
53	
54	\textbf{Curriculum and Multi-Phase Training.} Progressive training strategies have shown benefits in various settings \citep{bengio2009curriculum}. Our two-phase approach---geometric pre-training followed by task recovery---represents a novel application of curriculum learning to VLA safety, where the first phase encodes geometric awareness as an inductive bias that persists through the second phase.
55	
56	
57	%% ===================== METHOD =====================
58	\section{Method}
59	
60	\subsection{Problem Setup}
61	
62	We study collision avoidance in VLA-based tabletop manipulation using the SafeLIBERO benchmark. A VLA policy $\pi_\theta$ receives RGB observations and a language instruction, producing continuous end-effector (EE) actions. We evaluate on two scenes: \texttt{object\_pudding} (4 tasks, obstacles placed near target objects) and \texttt{spatial\_bowl} (4 tasks, varying spatial layouts).
63	
64	\subsection{Displacement-Filtered CAR (dfCAR)}
65	
66	Standard CAR counts an episode as ``safe'' if no collision is detected. We define displacement-filtered CAR to exclude episodes where safety is trivially achieved through inaction:
67	\begin{equation}
68	    \text{dfCAR}(\delta) = \frac{|\{e : \text{no collision}(e) \;\wedge\; \|\Delta \mathbf{p}_{\text{EE}}(e)\| > \delta \}|}{|\{e : \|\Delta \mathbf{p}_{\text{EE}}(e)\| > \delta\}|}
69	\end{equation}
70	where $\Delta \mathbf{p}_{\text{EE}}(e)$ is the maximum EE displacement during episode $e$ and $\delta$ is a displacement threshold. Episodes with $\|\Delta \mathbf{p}_{\text{EE}}\| \leq \delta$ are excluded from both numerator and denominator, filtering out frozen or near-stationary behavior.
71	
72	\subsection{SDF Auxiliary Loss}
73	
74	We augment the standard action prediction loss with an SDF-based collision penalty. Given a learned or ground-truth SDF $\phi(\mathbf{x})$ of the obstacle field, the training objective becomes:
75	\begin{equation}
76	    \mathcal{L} = \mathcal{L}_{\text{action}} + \lambda \cdot \mathcal{L}_{\text{SDF}}, \quad \mathcal{L}_{\text{SDF}} = \max(0, \delta_{\text{safe}} - \phi(\mathbf{p}_{\text{EE}}))
77	\end{equation}
78	where $\lambda$ controls the SDF loss weight and $\delta_{\text{safe}}$ is a safety margin. We study $\lambda \in \{0, 0.005, 0.01, 0.1\}$, with $\lambda=0$ corresponding to LoRA-only fine-tuning.
79	
80	\subsection{Two-Phase Training Protocol}
81	
82	Motivated by the catastrophic task performance collapse observed with end-to-end SDF training (TSR: 73\%$\to$5\%), we propose a two-phase curriculum:
83	\begin{enumerate}
84	    \item \textbf{Phase 1} (steps 1--10K): Train with $\lambda > 0$ to encode geometric awareness into the model weights.
85	    \item \textbf{Phase 2} (steps 10K--30K): Resume training with $\lambda = 0$ (action loss only) to recover task capability while retaining the geometric prior from Phase 1.
86	\end{enumerate}
87	
88	
89	%% ===================== EXPERIMENTS =====================
90	\section{Experiments}
91	
92	We organize experiments around four questions: (1) How prevalent is fake safety? (2) How does model capability interact with safety? (3) What are the sources of genuine collision avoidance? (4) Can curriculum training resolve the safety-capability tradeoff?
93	
94	All models are fine-tuned with LoRA on Pi0.5 for 30K steps unless otherwise noted. Evaluations use 200 episodes per condition (50 per task) on \texttt{object\_pudding}. We report task success rate (TSR), collision avoidance rate (CAR), mean EE displacement, and frozen rate (fraction of episodes with near-zero motion).
95	
96	%% --- 4.1 Fake Safety ---
97	\subsection{Fake Safety in Action-Collapsed Models}
98	
99	\begin{table}[t]
100	\centering
101	\caption{Fake safety diagnosis. A1 (Pi0 + SDF, $\lambda=0.005$) achieves high CAR through action collapse, not collision avoidance. Evaluation on \texttt{object\_pudding}, 50 re-evaluation episodes. ``Safe eps'' and ``collision eps'' denote EE displacement conditioned on episode outcome.}
102	\label{tab:fake_safety}
103	\begin{tabular}{lcccc}
104	\toprule
105	\textbf{Metric} & \textbf{Pi0 A1} & \textbf{Pi0.5 Baseline} & \textbf{OpenVLA (proj.)} \\
106	\midrule
107	TSR & 0\% & 73\% & 0\% \\
108	CAR & 91\% & 28\% & 88\% \\
109	Fake Safe Rate & 99.4\% & --- & $\sim$99\% \\
110	EE Disp (safe eps) & 0.005mm & 151mm & $\sim$8mm \\
111	EE Disp (collision eps) & 45mm & --- & --- \\
112	\bottomrule
113	\end{tabular}
114	\end{table}
115	
116	Table~\ref{tab:fake_safety} reveals the core pathology. Pi0 fine-tuned with SDF loss (A1, 30K steps) achieves 91\% CAR, but with TSR=0\% and median EE displacement of 0.005mm in safe episodes. The model has undergone action collapse: it produces near-zero actions, trivially avoiding collisions by not moving. The 99.4\% fake safe rate confirms that virtually all ``safe'' episodes reflect inaction rather than avoidance behavior. Projected OpenVLA zero-shot results show a similar pattern (CAR=88\%, TSR=0\%), suggesting fake safety generalizes beyond a single model family, though we note this experiment was blocked due to model download corruption and report projected values based on the same mechanistic reasoning.
117	
118	The fake safe rate is computed as the fraction of safe episodes with obstacle displacement $<0.1$mm. For A1, 99.4\% of safe episodes meet this criterion---the obstacles are never contacted because the robot arm never approaches them.
119	
120	\textbf{Re-evaluation confirms terminology consistency.} A dedicated 50-episode re-evaluation of A1 confirmed that EE displacement and obstacle displacement provide consistent evidence of action collapse. In safe episodes, EE displacement is at the micrometer scale; in the rare collision episodes (arising from initialization artifacts), EE displacement reaches $\sim$45mm. This three-order-of-magnitude gap between safe and collision episodes validates the displacement-filtering approach.
121	
122	
123	%% --- 4.2 dfCAR Robustness ---
124	\subsection{dfCAR Threshold Robustness}
125	
126	\begin{table}[t]
127	\centering
128	\caption{dfCAR sensitivity to displacement threshold $\delta$. The metric is remarkably stable across two orders of magnitude, confirming a clean separation between fake safety (EE disp $\sim$0.01mm) and genuine avoidance (EE disp $>$300mm). }
129	\label{tab:dfcar}
130	\begin{tabular}{lcccc}
131	\toprule
132	$\delta$ \textbf{(mm)} & \textbf{A1 dfCAR} & \textbf{LoRA dfCAR} & \textbf{SDF $\lambda$=0.005 dfCAR} & \textbf{Pi0.5 Baseline dfCAR} \\
133	\midrule
134	2 & 0.4\% & 54.5\% & 52.3\% & 83.0\% \\
135	5 & 0.4\% & 54.5\% & 52.3\% & 83.0\% \\
136	10 & 0.4\% & 54.5\% & 52.3\% & 82.5\% \\
137	20 & 0.4\% & 54.5\% & 52.3\% & 82.0\% \\
138	50 & 0.4\% & 54.5\% & 52.3\% & 81.0\% \\
139	100 & 0.4\% & 54.5\% & 52.3\% & 80.0\% \\
140	\bottomrule
141	\end{tabular}
142	\end{table}
143	
144	Table~\ref{tab:dfcar} demonstrates that dfCAR is insensitive to threshold choice. A1's dfCAR collapses to 0.4\% at all thresholds (from 91\% raw CAR), because its safe episodes have EE displacement at the micrometer scale. LoRA and SDF conditions show zero filtering effect (dfCAR = raw CAR) because all their active episodes have EE displacement $>300$mm, well above any reasonable threshold. The Pi0.5 baseline shows mild filtering at high thresholds ($-3$pp from $\delta$=2mm to 100mm) because a small fraction of its collision-free episodes involve shorter paths. This stability across $\delta \in [2, 100]$mm---spanning the entire gap between fake and real safety---confirms that dfCAR requires no careful threshold tuning.
145	
146	
147	%% --- 4.3 Capability vs Safety ---
148	\subsection{Task Capability vs.\ Safety}
149	
150	The Pi0.5 pre-trained baseline achieves TSR=74.7\% and CAR=26.8\% (3-seed mean). In contrast, Pi0 achieves TSR$\approx$0\% and CAR$\approx$82\%. This apparent anti-correlation between capability and safety is an artifact: Pi0's high CAR is fake safety from action collapse, while Pi0.5's lower CAR reflects genuine collisions during active task execution. A more capable model moves more, encounters obstacles more frequently, and collides more---but this does not mean it is less safe in any meaningful sense. The capability-safety correlation is confounded by the fake safety pathology identified in Section 4.1.
151	
152	
153	%% --- 4.4 Fine-tuning Attribution ---
154	\subsection{Decomposing Collision Avoidance Sources}
155	
156	\begin{table}[t]
157	\centering
158	\caption{LoRA-only 3-seed evaluation (\texttt{object\_pudding}, 200 episodes per seed). Seed~2 exhibits lower CAR, increasing inter-seed variance.}
159	\label{tab:lora_3seed}
160	\begin{tabular}{lcccc}
161	\toprule
162	\textbf{Seed} & \textbf{TSR} & \textbf{CAR} & \textbf{EE Disp (m)} & \textbf{Frozen \%} \\
163	\midrule
164	s0 & 8.5\% & 54.5\% & 0.489 & 0\% \\
165	s1 & 4.0\% & 56.0\% & 0.467 & 0\% \\
166	s2 & 2.0\% & 44.0\% & 0.450 & 0\% \\
167	\midrule
168	Mean & 4.8\% & 51.5\% & 0.469 & 0\% \\
169	SD & 3.3pp & 6.5pp & --- & --- \\
170	\bottomrule
171	\end{tabular}
172	\end{table}
173	
174	\begin{table}[t]
175	\centering
176	\caption{3-seed SDF attribution (3v3 comparison on \texttt{object\_pudding}). Low-$\lambda$ SDF adds no significant CAR above LoRA-only. High-$\lambda$ SDF ($\lambda=0.1$) provides a significant +15.5pp additive contribution.}
177	\label{tab:attribution}
178	\begin{tabular}{lcccc}
179	\toprule
180	\textbf{Condition} & \textbf{3-seed CAR Mean} & \textbf{SE} & \textbf{$\Delta$ vs LoRA} & \textbf{$p$-value} \\
181	\midrule
182	LoRA-only ($\lambda=0$) & 51.5\% & 3.7pp & --- & --- \\
183	SDF $\lambda=0.005$ & 52.3\% & 1.5pp & +0.8pp & $>0.5$ \\
184	SDF $\lambda=0.01$ & 52.8\% & 0.3pp & +1.3pp & $>0.3$ \\
185	SDF $\lambda=0.1$ & 67.0\% & 1.0pp & +15.5pp & $<0.02$ \\
186	\bottomrule
187	\end{tabular}
188	\end{table}
189	
190	Table~\ref{tab:lora_3seed} presents LoRA-only fine-tuning results across 3 seeds. LoRA fine-tuning on collision-free demonstrations produces genuine collision avoidance: mean CAR=51.5\% (vs.\ 26.8\% baseline), mean EE displacement=0.469m (confirming active motion), and 0\% frozen episodes. This +24.7pp CAR improvement requires no geometric supervision---the avoidance signal is implicit in the training demonstrations. However, task performance collapses catastrophically (TSR: 73\%$\to$4.8\%), indicating the model learns conservative rather than safe behavior. We note substantial inter-seed variance (SD=6.5pp), driven primarily by seed~2's lower CAR of 44\%.
191	
192	Table~\ref{tab:attribution} reveals the core attribution finding. At $\lambda=0.005$ and $\lambda=0.01$, SDF auxiliary loss provides no statistically significant CAR improvement over LoRA-only fine-tuning ($\Delta < 1.5$pp, $p > 0.3$). The demonstration-implicit avoidance signal dominates, and weak geometric supervision cannot add measurable benefit above it. However, at $\lambda=0.1$, SDF provides a significant additive contribution of +15.5pp CAR ($p < 0.02$), demonstrating that geometric supervision is not inherently redundant but requires sufficient weighting to overcome the dominant demonstration signal.
193	
194	All fine-tuned conditions (LoRA-only and all SDF variants) suffer comparable task performance collapse (TSR $\in [2.5\%, 6.3\%]$), confirming that the safety-capability tradeoff is a property of LoRA fine-tuning itself, not of geometric supervision.
195	
196	
197	%% --- 4.5 Lambda Dose-Response ---
198	\subsection{Lambda Dose-Response}
199	
200	\begin{table}[t]
201	\centering
202	\caption{Lambda dose-response curve across 4 points. CAR is approximately flat for $\lambda \leq 0.01$ and jumps at $\lambda=0.1$, suggesting a threshold effect rather than smooth dose-response. TSR continues to decrease at high $\lambda$.}
203	\label{tab:lambda}
204	\begin{tabular}{lcccc}
205	\toprule
206	$\lambda$ & \textbf{CAR (2-seed mean)} & \textbf{TSR} & \textbf{$\Delta$ CAR vs LoRA} & \textbf{Significant?} \\
207	\midrule
208	0 (LoRA-only) & $\sim$50\% & $\sim$5\% & --- & --- \\
209	0.005 & 52.3\% & 6.3\% & +2pp & No ($p>0.3$) \\
210	0.01 & 52.8\% & 6.8\% & +3pp & No ($p>0.2$) \\
211	0.1 & 67.0\% & 2.5\% & +17pp & Yes ($p<0.05$) \\
212	\bottomrule
213	\end{tabular}
214	\end{table}
215	
216	Table~\ref{tab:lambda} presents the full 4-point dose-response curve. The pattern is not smoothly monotonic but exhibits a threshold effect: CAR is essentially flat ($\sim$50--53\%) for $\lambda \in [0, 0.01]$, then jumps to 67\% at $\lambda=0.1$. This is consistent with a mechanism where low-$\lambda$ SDF gradients are too weak to overcome the dominant demonstration-implicit avoidance signal, while $\lambda=0.1$ provides sufficient gradient magnitude to impose additional geometric constraints on the policy.
217	
218	The cost of high-$\lambda$ SDF is further TSR degradation: from $\sim$5\% (LoRA and low-$\lambda$ SDF) to 2.5\% ($\lambda=0.1$). The stronger SDF penalty makes the model even more conservative, reducing its already-limited task capability. The two Lambda=0.1 seeds show consistent results (seed~0: CAR=68\%, TSR=2\%; seed~1: CAR=66\%, TSR=3\%), indicating the effect is reproducible.
219	
220	
221	%% --- 4.6 Two-Phase Training ---
222	\subsection{Two-Phase Training Strategy}
223	
224	\begin{table}[t]
225	\centering
226	\caption{Two-phase training results: Phase 1 (SDF, $\lambda=0.005$, steps 1--10K) $\to$ Phase 2 ($\lambda=0$, steps 10K--30K). Compared to LoRA-only and end-to-end SDF fine-tuning.}
227	\label{tab:phase2}
228	\begin{tabular}{lcccc}
229	\toprule
230	\textbf{Condition} & \textbf{CAR} & \textbf{TSR} & \textbf{EE Disp (m)} & \textbf{Frozen \%} \\
231	\midrule
232	LoRA-only (3-seed) & $\sim$50\% & $\sim$5\% & 0.47 & 0\% \\
233	SDF $\lambda=0.005$ (3-seed) & 52.3\% & 6.3\% & 0.50 & 0\% \\
234	Phase 2 $\lambda=0$ (seed 2) & 68\% & 42\% & 0.42 & 0\% \\
235	Phase 2 $\lambda=0$ (seed 0) & 64\% & 38\% & 0.44 & 0\% \\
236	Phase 2 $\lambda=0$ (2-seed mean) & 66\% & 40\% & 0.43 & 0\% \\
237	Pi0.5 baseline (3-seed) & 26.8\% & 74.7\% & 0.15 & --- \\
238	\bottomrule
239	\end{tabular}
240	\end{table}
241	
242	Table~\ref{tab:phase2} presents the two-phase training results. The key finding is striking: resuming training with $\lambda=0$ from a 10K-step SDF checkpoint achieves CAR=66\% (2-seed mean) while recovering TSR to 40\%---dramatically better than both LoRA-only (TSR$\sim$5\%) and end-to-end SDF (TSR$\sim$6\%). The two-phase strategy partially resolves the catastrophic safety-capability tradeoff.
243	
244	The mechanism is consistent with curriculum learning: the initial SDF phase encodes geometric awareness as a persistent inductive bias in the model weights. When Phase 2 removes the SDF loss, the model recovers task capability under pure action loss guidance, but the geometric prior from Phase 1 persists, maintaining elevated collision avoidance. Per-task analysis shows TSR recovery is concentrated in tasks where completion paths and avoidance paths have lower conflict (task 1: TSR=78\%, task 3: TSR=60\%), while tasks with high path conflict show limited recovery (task 0: TSR=22\%).
245	
246	Two seeds confirm the effect's direction (CAR: 64\% and 68\%; TSR: 38\% and 42\%), though the limited seed count (2 seeds, SE$\approx \pm$2pp) means this should be interpreted as a promising discovery rather than a validated method.
247	
248	
249	%% --- 4.7 Cross-Scene Analysis ---
250	\subsection{Cross-Scene Analysis}
251	
252	\begin{table}[t]
253	\centering
254	\caption{Cross-scene comparison between \texttt{object\_pudding} and \texttt{spatial\_bowl}. SDF effect magnitude differs across scenes, precluding a universal generalization claim. \texttt{spatial\_bowl} uses 1-seed evaluations (200 episodes each).}
255	\label{tab:cross_scene}
256	\begin{tabular}{lcccl}
257	\toprule
258	\textbf{Scene} & \textbf{LoRA CAR} & \textbf{SDF CAR} & \textbf{$\Delta$} & \textbf{Interpretation} \\
259	\midrule
260	\texttt{object\_pudding} & 51.5\% & 52.3\% & +0.8pp (ns) & SDF redundant \\
261	\texttt{spatial\_bowl} & 36\% & 45\% & +9pp (marginal) & SDF additive \\
262	\midrule
263	\multicolumn{4}{l}{Consistent across scenes?} & No \\
264	\bottomrule
265	\end{tabular}
266	\end{table}
267	
268	Table~\ref{tab:cross_scene} reveals that the SDF contribution is scene-dependent. On \texttt{object\_pudding} (3v3 seeds, $\lambda=0.005$), SDF adds a non-significant +0.8pp CAR. On \texttt{spatial\_bowl} (1 seed each, $\lambda=0.005$), SDF adds a marginally significant +9pp. The \texttt{spatial\_bowl} LoRA-only baseline is substantially lower (CAR=36\% vs.\ 51.5\%), suggesting that demonstration-implicit avoidance signals generalize less effectively to spatially diverse layouts. In such settings, explicit geometric supervision may provide additional benefit.
269	
270	However, the inconsistency between scenes---SDF redundant in one, additive in the other---prevents any universal generalization claim. The \texttt{spatial\_bowl} results use only 1 seed per condition, further limiting statistical power. Per-task analysis shows different CAR patterns across scenes: \texttt{object\_pudding} exhibits high variance across tasks (task 2 milk: CAR$\sim$90\%, task 3 bbq: CAR$\sim$16\%), while \texttt{spatial\_bowl} shows more uniform but overall lower CAR (range: 25--55\%). This suggests that avoidance patterns are task-geometry-specific rather than universally transferable.
271	
272	
273	%% --- 4.8 Training Details ---
274	\subsection{Training Details}
275	
276	\begin{table}[t]
277	\centering
278	\caption{Training convergence summary for all conditions. All runs train for 30K steps on Pi0.5 with LoRA.}
279	\label{tab:training}
280	\begin{tabular}{lccc}
281	\toprule
282	\textbf{Condition} & \textbf{Final Loss} & \textbf{Best Loss} & \textbf{Stable?} \\
283	\midrule
284	LoRA-only s0 & 0.01343 & 0.01025 & Yes \\
285	LoRA-only s1 & 0.01408 & 0.01130 & Yes \\
286	Phase 2 $\lambda=0$ (from SDF 10K) & 0.00980 & 0.00850 & Yes \\
287	\texttt{spatial\_bowl} SDF $\lambda=0.005$ & 0.01550 & 0.01350 & Yes \\
288	SDF $\lambda=0.1$ s0 & 0.01950 & 0.01420 & Yes \\
289	SDF $\lambda=0.1$ s1 & 0.01880 & 0.01480 & Yes \\
290	\bottomrule
291	\end{tabular}
292	\end{table}
293	
294	Table~\ref{tab:training} confirms stable training convergence across all conditions. Higher $\lambda$ values lead to higher total loss (due to the SDF loss component), but all runs converge without instability. The Phase~2 run achieves the lowest final loss (0.0098), consistent with the removal of the SDF loss term allowing the model to focus purely on action prediction.
295	
296	
297	%% ===================== DISCUSSION =====================
298	\section{Discussion}
299	
300	\textbf{Decomposition vs.\ Redundancy.} Our initial hypothesis was that SDF geometric supervision is redundant with demonstration-implicit avoidance signals. The full picture is more nuanced: SDF is effectively redundant at low weighting ($\lambda \leq 0.01$), where its gradient is overwhelmed by the dominant demonstration signal, but provides a significant additive contribution at $\lambda = 0.1$ (+15.5pp CAR). This dose-dependent interaction suggests that the two avoidance sources operate at different scales---demonstration signals establish a baseline level of conservative behavior, while strong geometric supervision can push avoidance further at the cost of additional task performance degradation.
301	
302	\textbf{High LoRA Variance.} The 3-seed LoRA-only evaluation reveals substantial variance (SD=6.5pp), driven by seed~2's CAR of 44\%. This variance is larger than the low-$\lambda$ SDF effect size, explaining why the SDF contribution at $\lambda \leq 0.01$ is not statistically detectable. Future work should employ 5+ seeds to achieve adequate statistical power for detecting small effect sizes in this domain.
303	
304	\textbf{Two-Phase Promise and Limitations.} The two-phase strategy achieves the best safety-capability balance (CAR=66\%, TSR=40\%), but two caveats apply: (i) only 2 seeds limit statistical confidence (SE$\approx \pm$2pp), and (ii) TSR=40\% remains well below the baseline 73\%, meaning the strategy only partially resolves the tradeoff. We present this as a discovery warranting further investigation, not a validated method.
305	
306	\textbf{Scene-Dependent Effects.} The inconsistency between \texttt{object\_pudding} and \texttt{spatial\_bowl} SDF effects cautions against universal claims. The demonstration-implicit avoidance signal appears weaker in spatially diverse scenes, potentially creating more room for geometric supervision to contribute. Systematic study across more scenes is needed.
307	
308	\textbf{Limitations.} (1)~All experiments use Pi0/Pi0.5 models; generalization to other VLA architectures is unconfirmed. The planned OpenVLA evaluation was blocked due to model download issues. (2)~The EE-only SDF formulation is a structural limitation---it cannot prevent arm-body collisions, which dominate in practice. (3)~Two seeds for the two-phase experiments and single seeds for cross-scene conditions limit statistical power. (4)~SafeLIBERO tabletop manipulation may not represent the full diversity of real-world collision scenarios.
309	
310	
311	%% ===================== CONCLUSION =====================
312	\section{Conclusion}
313	
314	We presented a systematic investigation of VLA collision avoidance evaluation, revealing three key findings. First, standard CAR is systematically contaminated by fake safety: models exhibiting action collapse achieve high CAR through inaction, not avoidance. We propose displacement-filtered CAR (dfCAR) as a robust corrective. Second, genuine collision avoidance decomposes into implicit demonstration signals (dominant) and explicit geometric supervision (additive at high dosage), with a dose-dependent interaction that explains why weak SDF supervision appears redundant. Third, two-phase curriculum training partially resolves the safety-capability tradeoff, achieving both elevated safety and meaningful task performance.
315	
316	These findings challenge the assumption that high CAR implies genuine safety and provide guidance for VLA safety evaluation and training: (i) always verify safety metrics against action collapse; (ii) recognize that collision-free demonstrations already encode substantial avoidance signals; (iii) consider curriculum strategies to balance safety encoding with task capability.
317	
318	\bibliographystyle{plainnat}
319	\bibliography{references}
320	
321	\end{document}
322	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "e927aee3-6f35-4a40-9149-f51d53d3dea8"
}
```

</details>

---

### System

_source line 120_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/_project/data/ssr_analysis.md",
  "usage": {
    "total_tokens": 77507,
    "tool_uses": 34,
    "duration_ms": 56854
  },
  "last_tool_name": "Read",
  "uuid": "96476c3a-6431-4448-9105-0316328f2580",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 121_

<details open><summary>🔧 Tool call — Read · `toolu_01R9EAQyS7NLaJ6BPpHktcAi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/data/ssr_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "4095bc49-2c70-4ea6-ae19-9ea583c9dc16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TC9z5s46boaEVBXDDnNyio",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4558,
      "cache_read_input_tokens": 72872,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4558,
        "ephemeral_1h_input_tokens": 0
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

_source line 122 · 2026-05-27T13:13:36.460Z_

<details><summary>↩ Tool result · `toolu_01R9EAQyS7NLaJ6BPpHktcAi`</summary>

```text
1	# SSR (Safe Success Rate) Analysis
2	# Computed 2026-05-27 by worker_analysis_ssr_computation_20260527T113223
3	# SSR = (success AND no_collision) / total_episodes
4	
5	## Per-seed SSR Table
6	
7	| Condition | TSR (ep-level) | CR (collision rate) | CAR (1-CR) | SSR | n_episodes |
8	|-----------|---------------|--------------------|-----------:|----:|----------:|
9	| Pi0.5 baseline | 71.5% | 71.5% | 28.5% | 28.0% | 200 |
10	| LoRA s0 30K | 51.5% | 43.5% | 56.5% | 29.5% | 200 |
11	| LoRA s1 30K | 51.5% | 47.5% | 52.5% | 27.0% | 200 |
12	| SDF lambda=0.005 s0 | 55.5% | 43.0% | 57.0% | 30.0% | 200 |
13	| SDF lambda=0.005 s1 | 50.5% | 46.0% | 54.0% | 24.0% | 200 |
14	| SDF lambda=0.005 s2 | 56.0% | 47.5% | 52.5% | 29.5% | 200 |
15	| SDF lambda=0.01 s0 | 52.5% | 43.0% | 57.0% | 32.5% | 200 |
16	| SDF lambda=0.01 s1 | 55.5% | 42.5% | 57.5% | 30.0% | 200 |
17	| SDF lambda=0.01 s2 | 53.5% | 45.5% | 54.5% | 28.0% | 200 |
18	| SDF lambda=0.1 s0 | — | — | — | — | JSON overwritten |
19	| SDF lambda=0.1 s1 | 49.0% | 41.5% | 58.5% | 26.5% | 200 |
20	
21	## Condition Averages
22	
23	| Condition | Avg TSR | Avg CAR | Avg SSR | SSR/TSR |
24	|-----------|---------|---------|---------|---------|
25	| Pi0.5 baseline | 71.5% | 28.5% | 28.0% | 0.392 |
26	| LoRA (2 seeds) | 51.5% | 54.5% | 28.3% | 0.549 |
27	| SDF lambda=0.005 (3 seeds) | 54.0% | 54.5% | 27.8% | 0.515 |
28	| SDF lambda=0.01 (3 seeds) | 53.8% | 56.3% | 30.2% | 0.561 |
29	| SDF lambda=0.1 (1 seed only) | 49.0% | 58.5% | 26.5% | 0.541 |
30	
31	## Key Finding: SSR/TSR ratio refutes "reduced exposure"
32	
33	Under "reduced exposure" hypothesis: model simply does fewer things → SSR/TSR ≈ constant.
34	Observed: SSR/TSR jumps from 0.39 (baseline) to ~0.55 (all trained models).
35	This means a higher fraction of successful episodes are collision-free after training.
36	
37	## Caveats
38	- Worker's original "CAR" column was collision RATE (not avoidance rate). Corrected above.
39	- SDF lambda=0.1 s0 JSON overwritten by reeval_lora. Only 1 seed available for lambda=0.1.
40	- n=200 episodes per condition (50 per task × 4 tasks). SE of SSR ≈ 6.5pp → differences not individually significant.
41	- SSR/TSR ratio argument is more compelling than raw SSR comparison.
42	- Episode-level TSR differs from registry's task-averaged TSR (both valid, different aggregation).
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "bfe40fe8-cb76-46d9-837e-96f4bec82496"
}
```

</details>

---

### System

_source line 123_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/_project/data/fig5_lambda_data.csv",
  "usage": {
    "total_tokens": 77508,
    "tool_uses": 35,
    "duration_ms": 57388
  },
  "last_tool_name": "Read",
  "uuid": "ae6b0ffd-b5ad-4006-8bcd-fcdd91a247d8",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 124_

<details open><summary>🔧 Tool call — Read · `toolu_01EyFVQQ1MbWcKYzRi12WXyY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/data/fig5_lambda_data.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "af8a1c0b-e3f4-460b-8c30-6ee64ed6c8cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TC9z5s46boaEVBXDDnNyio",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4558,
      "cache_read_input_tokens": 72872,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4558,
        "ephemeral_1h_input_tokens": 0
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

_source line 125 · 2026-05-27T13:13:36.994Z_

<details><summary>↩ Tool result · `toolu_01EyFVQQ1MbWcKYzRi12WXyY`</summary>

```text
1	lambda,CAR_mean,CAR_std,CAR_seeds,TSR_mean,TSR_std,step,note
2	0,54.75,3.18,"57.0;52.5",48.75,,30K,LoRA-only (no SDF)
3	0.005,54.5,2.29,"57.0;54.0;52.5",54.0,3.0,30K,3 seeds
4	0.01,56.33,1.61,"57.0;57.5;54.5",53.83,1.5,30K,3 seeds
5	0.1,58.25,0.35,"58.0;58.5",48.0,1.4,30K,2 seeds 30K
6	
7	# step-wise sub-table (for inset or supplementary)
8	# lambda,step,CAR,TSR,seed,note
9	# 0.1,16000,pending,pending,0,best loss checkpoint eval running
10	# 0.1,20000,55,54,0,early signal
11	# 0.1,20000,56,51,1,early signal
12	# 0.1,22000,pending,pending,0,next after 16K
13	# 0.1,30000,pending,pending,0,training ~17:00 UTC
14	# 0.1,30000,pending,pending,1,training ~17:30 UTC
15	# 0.1,30000,pending,pending,2,training ~08:00 UTC 5/28
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "c034d439-dff2-4504-8e4b-3df45a210576"
}
```

</details>

---

### System

_source line 126_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Searching for per.task|OJ|orange.juice.*CAR|milk.*CAR|bbq.*CAR|…",
  "usage": {
    "total_tokens": 99402,
    "tool_uses": 36,
    "duration_ms": 64016
  },
  "last_tool_name": "Grep",
  "uuid": "5fcf99dd-258c-4877-a559-61d0acc82961",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 127_

<details open><summary>🔧 Tool call — Grep · `toolu_01NfzdwZwerKTzYxRh5owojb`</summary>

```json
{
  "pattern": "per.task|OJ|orange.juice.*CAR|milk.*CAR|bbq.*CAR|choc.*CAR|s1.*per",
  "-i": true,
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "18595cfc-7b2c-40cd-9c02-d2596efa0d6d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gkng8xFvmpUsndoGGyvQu9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21892,
      "cache_read_input_tokens": 77430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21892,
        "ephemeral_1h_input_tokens": 0
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

_source line 128 · 2026-05-27T13:13:43.657Z_

<details><summary>↩ Tool result · `toolu_01NfzdwZwerKTzYxRh5owojb`</summary>

```text
artifacts/dream_reports/dream_20260525T223036/best/paper.tex:136:\paragraph{OpenVLA per-task analysis.}
artifacts/dream_reports/dream_20260525T223036/best/paper.tex:137:Table~\ref{tab:openvla_tasks} shows per-task breakdown revealing task-dependent dominant fake safety modes. Tasks with near-zero TSR (orange\_juice, milk) exhibit primarily action collapse, while chocolate\_pudding (highest TSR at 14\%) shows geometric path dominance.
artifacts/dream_reports/dream_20260525T223036/best/paper.tex:141:\caption{OpenVLA-7B per-task results on \texttt{object\_pudding} (200 episodes total).}
artifacts/dream_reports/dream_20260525T223036/best/paper.tex:178:\paragraph{Per-task variation.} Table~\ref{tab:per_task_lora} reveals interesting asymmetry: task \texttt{milk} shows +70pp CAR improvement from SDF while \texttt{bbq\_sauce} shows $-$24pp, likely related to obstacle geometry---consistent with the EE-only SDF limitation (the SDF gradient pushes the end-effector away but may cause the arm body to sweep through obstacles positioned at different heights).
artifacts/dream_reports/dream_20260525T223036/best/paper.tex:182:\caption{Per-task LoRA vs SDF comparison (seed 0, $\lambda$=0.005) on \texttt{object\_pudding}.}
artifacts/dream_reports/dream_20260525T223036/best/paper.tex:183:\label{tab:per_task_lora}
artifacts/dream_reports/dream_20260525T223036/best/paper.tex:243:\paragraph{Per-task retention analysis.} Table~\ref{tab:phase2_tasks} shows that safety retention is consistent across tasks (76--100\%), with the highest absolute CAR in tasks where SDF training was most effective (milk: 72\% CAR retained from Phase 1's 92\%).
artifacts/dream_reports/dream_20260525T223036/best/paper.tex:247:\caption{Phase 2 per-task breakdown showing consistent TSR recovery and CAR retention.}
artifacts/dream_reports/dream_20260525T223036/best/paper.tex:284:\paragraph{spatial\_bowl per-task results.} Table~\ref{tab:spatial_tasks} shows relatively uniform SDF effect across spatial tasks (CAR 40--52\%), contrasting with the high per-task variance in \texttt{object\_pudding} (14--86\%). This supports the interpretation that geometrically uniform obstacle distributions yield more consistent SDF benefit.
artifacts/dream_reports/dream_20260525T223036/best/paper.tex:288:\caption{spatial\_bowl per-task results under SDF training ($\lambda$=0.005).}
artifacts/dream_reports/dream_20260525T223036/best/paper.tex:312:While SDF auxiliary loss successfully induces end-effector avoidance, per-task analysis reveals structural limitations: tasks where obstacles are positioned at arm-link height show reduced or negative CAR improvement (e.g., bbq\_sauce: $-$24pp). Full-body SDF supervision---requiring collision geometry for all robot links---is a natural but computationally expensive extension.
artifacts/dream_reports/dream_20260525T223036/worst/paper.tex:213:The \texttt{spatial\_bowl} scene presents a harder geometric challenge: the bowl target is surrounded by multiple obstacles (plate, ramekin, cabinet), creating contradictory SDF gradients. Per-task analysis shows uniformly low TSR (0--12\%) confirming that SDF-induced task damage is scene-agnostic, while the safety benefit is scene-specific and marginal.
artifacts/dream_reports/dream_20260525T223036/worst/paper.tex:217:\caption{Per-task results on \texttt{spatial\_bowl} after SDF training (30K steps, $\lambda$=0.005).}
artifacts/dream_reports/dream_20260525T223036/worst/paper.tex:262:\caption{Per-task Phase 2 recovery. Only \texttt{chocolate\_pudding} (the easiest task) shows marginal recovery.}
artifacts/dream_reports/dream_20260525T223036/worst/paper.tex:345:OpenVLA-7B was evaluated zero-shot on \texttt{object\_pudding} (200 episodes). Per-task breakdown:
artifacts/dream_reports/dream_20260525T223036/median/paper.tex:133:OpenVLA-7B evaluated zero-shot on \texttt{object\_pudding} (200 episodes) achieves TSR$\sim$8\% and CAR$\sim$72\%, with fake safe rate $\sim$70\%. Unlike Pi0's complete collapse, OpenVLA produces small but non-zero motions (EE displacement $\sim$0.08\,m), resulting in weaker but still prevalent fake safety. Table~\ref{tab:openvla_tasks} shows per-task variation.
artifacts/dream_reports/dream_20260525T223036/median/paper.tex:137:\caption{OpenVLA per-task breakdown on \texttt{object\_pudding}. Fake safety severity varies with obstacle geometry---larger obstacles (chocolate\_pudding) force more real collisions.}
artifacts/dream_reports/dream_20260525T223036/median/paper.tex:287:\paragraph{Per-Task Analysis for spatial\_bowl.}
artifacts/dream_reports/dream_20260525T223036/median/paper.tex:292:\caption{Per-task results on \texttt{spatial\_bowl}. Despite large EE displacements confirming real avoidance behavior, CAR remains low because arm-body collisions (not targeted by EE-only SDF) dominate.}
artifacts/dream_reports/dream_20260526T023936/best/paper.tex:125:\textbf{Tasks and Scenes.} We evaluate on two SafeLIBERO scenes: \texttt{object\_pudding} (4 tasks: orange juice, chocolate pudding, milk, BBQ sauce) and \texttt{spatial\_bowl} (4 tasks: pick bowl from varying spatial configurations). Each evaluation runs 200 episodes (50 per task).
artifacts/dream_reports/dream_20260526T023936/best/paper.tex:178:The per-task CAR pattern is consistent across all seeds and conditions. Task~2 (milk) achieves $\sim$92\% CAR due to a workspace layout where obstacles are small and the natural path is distant. Task~3 (BBQ sauce) achieves $\sim$20\% CAR due to a narrow corridor with bilateral obstacles. This geometry-driven pattern confirms that avoidance performance is determined by task layout interacting with the learned conservative policy, not by random seed variation (seed-to-seed SD = 0.75 pp).
artifacts/dream_reports/dream_20260526T023936/best/paper.tex:231:At $\lambda = 0.1$, SDF loss constitutes approximately 10\% of the total gradient signal, a non-negligible contribution. Yet CAR (51.0\%) remains indistinguishable from the lower-$\lambda$ SDF conditions (50.5\%, 52.8\%). The per-task breakdown at $\lambda = 0.1$ (Table~\ref{tab:lambda01_pertask}) confirms that task-level CAR patterns are identical to LoRA-only, governed by workspace geometry rather than SDF strength.
artifacts/dream_reports/dream_20260526T023936/best/paper.tex:235:\caption{Per-task CAR breakdown at $\lambda = 0.1$ (2 seeds) vs.\ LoRA-only mean (3 seeds) on \texttt{object\_pudding}.}
artifacts/dream_reports/dream_20260526T023936/worst/paper.tex:94:All models are fine-tuned with LoRA on Pi0.5 for 30K steps unless otherwise noted. Evaluations use 200 episodes per condition (50 per task) on \texttt{object\_pudding}. We report task success rate (TSR), collision avoidance rate (CAR), mean EE displacement, and frozen rate (fraction of episodes with near-zero motion).
artifacts/dream_reports/dream_20260526T023936/worst/paper.tex:105:\textbf{Metric} & \textbf{Pi0 A1} & \textbf{Pi0.5 Baseline} & \textbf{OpenVLA (proj.)} \\
artifacts/dream_reports/dream_20260526T023936/worst/paper.tex:116:[Omitted long matching line]
artifacts/dream_reports/dream_20260526T023936/worst/paper.tex:244:[Omitted long matching line]
artifacts/dream_reports/dream_20260526T023936/worst/paper.tex:270:[Omitted long matching line]
artifacts/drafts/experimental_framework.tex:11:Each method is evaluated for 50 episodes per task (200 episodes total). For multi-seed experiments (Pi0.5), we run 3 seeds to produce 600 episodes per configuration. Initial object configurations are fixed across methods to ensure fair comparison.
artifacts/drafts/method.tex:11:Our base model is $\pi_0$~\cite{black2024pi0}, a 3.5B-parameter flow-matching VLA comprising a PaliGemma vision-language encoder (Gemma 2B) and a Gemma 300M action expert. The action expert produces a sequence of action tokens through an output projection $W_{\mathrm{out}} \in \mathbb{R}^{1024 \times 32}$ that maps from the expert's hidden dimension to the action token space.
artifacts/drafts/method.tex:17:\paragraph{Feature extraction.} We capture the action expert's suffix output $\mathbf{z} \in \mathbb{R}^{B \times H \times 1024}$, the tensor immediately preceding $W_{\mathrm{out}}$, via a forward hook on \texttt{action\_out\_proj}. Mean-pooling along the action horizon dimension yields a compact representation:
artifacts/drafts/method.tex:80:\textbf{Step 5.} Project both original and refined features through the action output projection:
artifacts/drafts/method.tex:81:\begin{equation}\label{eq:projection}
artifacts/drafts/method.tex:116:[Omitted long matching line]
artifacts/dream_reports/dream_20260526T023936/median/paper.tex:126:\paragraph{Benchmark.} All experiments use SafeLIBERO with instrumented collision detection. We evaluate on two scene types: \texttt{object\_pudding} (4 tasks: orange\_juice, chocolate\_pudding, milk, bbq\_sauce) and \texttt{spatial\_bowl} (4 tasks: bowl placement variants). Each evaluation consists of 200 episodes (50 per task).
artifacts/dream_reports/dream_20260526T023936/median/paper.tex:223:\caption{Per-task breakdown on \texttt{spatial\_bowl} (SDF $\lambda{=}0.005$, seed0, 200 episodes). CAR is lower than \texttt{object\_pudding} due to denser obstacle configurations. No LoRA-only control was available for this scene, precluding SDF attribution.}
artifacts/dream_reports/dream_20260526T023936/median/paper.tex:276:Per-task CAR patterns are consistent across all conditions: \texttt{milk} achieves the highest CAR (78--94\%) due to favorable obstacle placement, while \texttt{bbq\_sauce} achieves the lowest (18--28\%) due to severe obstacle occlusion. This task-specific pattern is preserved identically whether or not SDF loss is applied, indicating that CAR is driven by task layout and demonstration imitation, not geometric supervision.
artifacts/dream_reports/dream_20260526T023936/median/paper.tex:300:\caption{Per-task breakdown for $\lambda{=}0.1$ (2 seeds, 200 episodes each). The task-specific CAR pattern is preserved (milk $>$ orange\_juice $>$ chocolate\_pudding $>$ bbq\_sauce), consistent with LoRA-only and lower-$\lambda$ conditions.}
artifacts/drafts/analysis_claim3.tex:29:[Omitted long matching line]
artifacts/drafts/introduction.tex:9:[Omitted long matching line]
artifacts/_project/paper/analysis_claim3.tex:29:[Omitted long matching line]
artifacts/_project/paper/introduction.tex:9:[Omitted long matching line]
artifacts/_project/paper/discussion.tex:8:[Omitted long matching line]
artifacts/_project/paper/experimental_framework.tex:11:Each method is evaluated for 50 episodes per task (200 episodes total). For multi-seed experiments (Pi0.5), we run 3 seeds to produce 600 episodes per configuration. Initial object configurations are fixed across methods to ensure fair comparison.
artifacts/_project/paper/method.tex:11:Our base model is $\pi_0$~\cite{black2024pi0}, a 3.5B-parameter flow-matching VLA comprising a PaliGemma vision-language encoder (Gemma 2B) and a Gemma 300M action expert. The action expert produces a sequence of action tokens through an output projection $W_{\mathrm{out}} \in \mathbb{R}^{1024 \times 32}$ that maps from the expert's hidden dimension to the action token space.
artifacts/_project/paper/method.tex:17:\paragraph{Feature extraction.} We capture the action expert's suffix output $\mathbf{z} \in \mathbb{R}^{B \times H \times 1024}$, the tensor immediately preceding $W_{\mathrm{out}}$, via a forward hook on \texttt{action\_out\_proj}. Mean-pooling along the action horizon dimension yields a compact representation:
artifacts/_project/paper/method.tex:79:\textbf{Step 5.} Project both original and refined features through the action output head:
artifacts/_project/paper/method.tex:80:\begin{equation}\label{eq:projection}
artifacts/_project/paper/method.tex:115:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "702d9095-28ba-4842-b49e-5656eb969e92"
}
```

</details>

---

### System

_source line 129_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Searching for 66%|72%|70%|26%|CAR=66|CAR=72|CAR=70|CAR=26",
  "usage": {
    "total_tokens": 99403,
    "tool_uses": 37,
    "duration_ms": 65744
  },
  "last_tool_name": "Grep",
  "uuid": "fc3d0f24-4873-4234-b263-36bfcaa7e021",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 130_

<details open><summary>🔧 Tool call — Grep · `toolu_01AASquESCKxzACPUMgp6eWb`</summary>

```json
{
  "pattern": "66%|72%|70%|26%|CAR=66|CAR=72|CAR=70|CAR=26",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts",
  "glob": "*.{tex,md,csv}",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "a30b7ddd-ded7-4695-9d6e-8d6878b32ee2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gkng8xFvmpUsndoGGyvQu9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21892,
      "cache_read_input_tokens": 77430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21892,
        "ephemeral_1h_input_tokens": 0
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

_source line 131 · 2026-05-27T13:13:45.366Z_

<details><summary>↩ Tool result · `toolu_01AASquESCKxzACPUMgp6eWb`</summary>

```text
artifacts/report_pi05_object_collision_analysis.md:14:| T0 orange juice | 94% (47/50) | 12 (24%) | 13 (26%) | 10 (20%) | 12 (24%) |
artifacts/report_pi05_object_collision_analysis.md:17:| T3 bbq sauce | 66% (33/50) | 12 (24%) | 10 (20%) | 5 (10%) | 6 (12%) |
artifacts/eval_pi05_safelibero_object_v11/report/report_pi05_object_collision_analysis.md:14:| T0 orange juice | 94% (47/50) | 12 (24%) | 13 (26%) | 10 (20%) | 12 (24%) |
artifacts/eval_pi05_safelibero_object_v11/report/report_pi05_object_collision_analysis.md:17:| T3 bbq sauce | 66% (33/50) | 12 (24%) | 10 (20%) | 5 (10%) | 6 (12%) |
artifacts/fig1_teaser_design.md:26:│  CAR=91.5%  TSR=0%    91.5% ──τ_d──► ≈0%    CAR=26.8% TSR=74.7%│
artifacts/fig1_teaser_design.md:32:- 每列分上下两区：上区 schematic/flow（~70% 高度），下区 displacement 条（~30% 高度）
artifacts/figure1_teaser_design.md:181:- Pi0.5 baseline: 3-seed eval（CAR=26.8%±1.6%, TSR=74.7%±1.5%, frozen=0%）
artifacts/training_progress_20260527.md:43:| Step | **7825 / 30000 (26%)** |
artifacts/metric_definitions.md:267:- Pi0.5: CAR=26.8%（低得多），但 FR≈0%，TSR=74.7% → 真实在动，碰撞是真实碰撞
artifacts/research_openvla_libero.md:117:| OpenVLA (LoRA FT) | ~78% | ~82% | ~80% | ~66% | **76.5%** |
artifacts/pi05_collision_analysis_report.md:28:| 2 | Milk → basket | 66% | **16%** | 42/50 (84%) | 68.0 | 71% late |
artifacts/pi05_collision_analysis_report.md:29:| 3 | BBQ sauce → basket | 76% | **34%** | 33/50 (66%) | 80.8 | 76% late |
artifacts/pi05_collision_analysis_report.md:64:| moka_pot | 路径附近 | 宽大 | 7/10 | 70% |
artifacts/pi05_collision_analysis_report.md:71:2. **障碍物尺寸分级效应**：collision rate 与 obstacle 高度/体积严格正相关——扁平 book (10%) < 小 mug (30%) < 窄 bottle (40%) < 宽 pot (70%) < 高大 milk (90%)。说明轨迹刚好在 obstacle 高度边缘，大物体突入 arm sweep zone。
artifacts/dream_reports/dream_20260525T223036/best/paper_framing.md:33:**证据**: Pi0.5 3-seed eval (TSR=74.7±1.5%, CAR=26.8±1.6%) vs Pi0 baseline (TSR≈0%, CAR=82%)
artifacts/dream_reports/dream_20260525T223036/best/paper_framing.md:148:- [x] Pi0.5 baseline 3-seed (Claim 2) — CAR=26.8±1.6%
artifacts/dream_reports/dream_20260525T223036/best/review_report.md:174:- **With critical + major fixes (1-7)**: 60-70%
artifacts/dream_reports/dream_20260525T223036/worst/paper_framing.md:33:**证据**: Pi0.5 3-seed eval (TSR=74.7±1.5%, CAR=26.8±1.6%) vs Pi0 baseline (TSR≈0%, CAR=82%)
artifacts/dream_reports/dream_20260525T223036/worst/paper_framing.md:148:- [x] Pi0.5 baseline 3-seed (Claim 2) — CAR=26.8±1.6%
artifacts/verify_22k_eval_report.md:18:| orange_juice CAR | 66% | 66% | PASS |
artifacts/dream_reports/dream_20260525T223036/median/paper_framing.md:33:**证据**: Pi0.5 3-seed eval (TSR=74.7±1.5%, CAR=26.8±1.6%) vs Pi0 baseline (TSR≈0%, CAR=82%)
artifacts/dream_reports/dream_20260525T223036/median/paper_framing.md:148:- [x] Pi0.5 baseline 3-seed (Claim 2) — CAR=26.8±1.6%
artifacts/dream_reports/dream_20260525T223036/median/review_report.md:35:1. **Important and timely problem identification.** The "fake safety" phenomenon — where action-collapsed or minimally-moving policies trivially achieve high CAR — is a real confound affecting VLA safety evaluation. Quantifying this across three model families (Pi0 at 99.6% fake safe, OpenVLA at ~70%, Pi0.5 at 98.2% of safe episodes) provides useful empirical documentation that the community needs to see. [R1, R2 agree]
artifacts/dream_reports/dream_20260526T023936/best/paper_framing.md:40:**证据**: Pi0.5 3-seed eval (TSR=74.7±1.5%, CAR=26.8±1.6%) vs Pi0 baseline (TSR≈0%, CAR=82%)
artifacts/dream_reports/dream_20260526T023936/best/paper_framing.md:156:- [x] Pi0.5 baseline 3-seed (Claim 2) — CAR=26.8±1.6%
artifacts/dream_reports/dream_20260526T023936/worst/paper_framing.md:40:**证据**: Pi0.5 3-seed eval (TSR=74.7±1.5%, CAR=26.8±1.6%) vs Pi0 baseline (TSR≈0%, CAR=82%)
artifacts/dream_reports/dream_20260526T023936/worst/paper_framing.md:156:- [x] Pi0.5 baseline 3-seed (Claim 2) — CAR=26.8±1.6%
artifacts/dream_reports/dream_20260526T023936/worst/paper.tex:26:[Omitted long matching line]
artifacts/dream_reports/dream_20260526T023936/worst/paper.tex:40:\textbf{(3) Two-Phase Training.} We discover that a curriculum strategy---first training with SDF loss to encode geometric awareness, then removing it to recover task capability---achieves CAR=66\% with TSR=40\% (2-seed mean), partially resolving the catastrophic safety-capability tradeoff inherent in end-to-end fine-tuning.
artifacts/dream_reports/dream_20260526T023936/worst/paper.tex:150:[Omitted long matching line]
artifacts/dream_reports/dream_20260526T023936/worst/paper.tex:218:The cost of high-$\lambda$ SDF is further TSR degradation: from $\sim$5\% (LoRA and low-$\lambda$ SDF) to 2.5\% ($\lambda=0.1$). The stronger SDF penalty makes the model even more conservative, reducing its already-limited task capability. The two Lambda=0.1 seeds show consistent results (seed~0: CAR=68\%, TSR=2\%; seed~1: CAR=66\%, TSR=3\%), indicating the effect is reproducible.
artifacts/dream_reports/dream_20260526T023936/worst/paper.tex:242:Table~\ref{tab:phase2} presents the two-phase training results. The key finding is striking: resuming training with $\lambda=0$ from a 10K-step SDF checkpoint achieves CAR=66\% (2-seed mean) while recovering TSR to 40\%---dramatically better than both LoRA-only (TSR$\sim$5\%) and end-to-end SDF (TSR$\sim$6\%). The two-phase strategy partially resolves the catastrophic safety-capability tradeoff.
artifacts/dream_reports/dream_20260526T023936/worst/paper.tex:304:\textbf{Two-Phase Promise and Limitations.} The two-phase strategy achieves the best safety-capability balance (CAR=66\%, TSR=40\%), but two caveats apply: (i) only 2 seeds limit statistical confidence (SE$\approx \pm$2pp), and (ii) TSR=40\% remains well below the baseline 73\%, meaning the strategy only partially resolves the tradeoff. We present this as a discovery warranting further investigation, not a validated method.
artifacts/dream_reports/dream_20260526T023936/worst/review_report.md:26:[Omitted long matching line]
artifacts/dream_reports/dream_20260526T023936/worst/review_report.md:38:- **Two-phase training uses only 2 seeds.** CAR=66% (SE~2pp), TSR=40% (SE~2pp). 95% CI on TSR spans ~[36%, 44%]. Only one Phase 1 duration (10K) and one lambda (0.005) tested — no ablation over Phase 1 hyperparameters.
artifacts/_project/report/figure1_teaser_design.md:181:- Pi0.5 baseline: 3-seed eval（CAR=26.8%±1.6%, TSR=74.7%±1.5%, frozen=0%）
artifacts/dream_reports/dream_20260526T023936/median/paper_framing.md:40:**证据**: Pi0.5 3-seed eval (TSR=74.7±1.5%, CAR=26.8±1.6%) vs Pi0 baseline (TSR≈0%, CAR=82%)
artifacts/dream_reports/dream_20260526T023936/median/paper_framing.md:156:- [x] Pi0.5 baseline 3-seed (Claim 2) — CAR=26.8±1.6%
artifacts/_project/report/metric_definitions_e59531.md:267:- Pi0.5: CAR=26.8%（低得多），但 FR≈0%，TSR=74.7% → 真实在动，碰撞是真实碰撞
artifacts/_project/report/metric_definitions.md:267:- Pi0.5: CAR=26.8%（低得多），但 FR≈0%，TSR=74.7% → 真实在动，碰撞是真实碰撞
artifacts/_project/report/ssh_recovery_execution_plan.md:122:对比 baseline（Pi0.5 3-seed: TSR=74.7±1.5%, CAR=26.8±1.6%）和 LoRA baseline（待完成）。
artifacts/_project/report/pi05_collision_analysis_report.md:28:| 2 | Milk → basket | 66% | **16%** | 42/50 (84%) | 68.0 | 71% late |
artifacts/_project/report/pi05_collision_analysis_report.md:29:| 3 | BBQ sauce → basket | 76% | **34%** | 33/50 (66%) | 80.8 | 76% late |
artifacts/_project/report/pi05_collision_analysis_report.md:64:| moka_pot | 路径附近 | 宽大 | 7/10 | 70% |
artifacts/_project/report/pi05_collision_analysis_report.md:71:2. **障碍物尺寸分级效应**：collision rate 与 obstacle 高度/体积严格正相关——扁平 book (10%) < 小 mug (30%) < 窄 bottle (40%) < 宽 pot (70%) < 高大 milk (90%)。说明轨迹刚好在 obstacle 高度边缘，大物体突入 arm sweep zone。
artifacts/_project/report/related_work_survey.md:92:- **Key results:** Up to 26% (sim) and 80% (real) higher success rates in cluttered unseen environments.
artifacts/_project/report/mid_eval_d012_step10k_results.md:13:| 0 orange_juice | 70.7%/10.0% | 18%/62% | 26%/56% |
artifacts/_project/report/mid_eval_d012_step10k_results.md:14:| 1 choc_pudding | 86.0%/56.0% | 70%/72% | 72%/70% |
artifacts/_project/report/mid_eval_d012_step10k_results.md:15:| 2 salad_dressing | 66.0%/12.0% | 40%/72% | 46%/72% |
artifacts/_project/report/mid_eval_d012_step10k_results.md:16:| 3 bbq_sauce | 76.0%/29.3% | 60%/26% | 52%/28% |
artifacts/_project/report/mid_eval_d012_step10k_results.md:20:2. Task 0 main drag (TSR 18-26%)
artifacts/related_work_survey.md:92:- **Key results:** Up to 26% (sim) and 80% (real) higher success rates in cluttered unseen environments.
artifacts/_project/intermediate/fig1_teaser_design.md:26:│  CAR=91.5%  TSR=0%    91.5% ──τ_d──► ≈0%    CAR=26.8% TSR=74.7%│
artifacts/_project/intermediate/fig1_teaser_design.md:32:- 每列分上下两区：上区 schematic/flow（~70% 高度），下区 displacement 条（~30% 高度）
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "e9ab0ac7-ecef-4ec0-a167-8e6f3ab9fb19"
}
```

</details>

---

### System

_source line 132_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Searching for 54\\.75|54\\.5[^0-9]|56\\.33|58\\.25|3\\.18|2\\.29|1\\.6…",
  "usage": {
    "total_tokens": 99404,
    "tool_uses": 38,
    "duration_ms": 66662
  },
  "last_tool_name": "Grep",
  "uuid": "a6cb1645-ce58-4c3c-a15c-371b944ff5b4",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 133_

<details open><summary>🔧 Tool call — Grep · `toolu_01CeTQavZx9GkbGYMM5cWzFM`</summary>

```json
{
  "pattern": "54\\.75|54\\.5[^0-9]|56\\.33|58\\.25|3\\.18|2\\.29|1\\.61|0\\.35",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf",
  "glob": "*.{tex,md,csv}",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "60317dd9-8769-47ea-a0ba-7027e5220a0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gkng8xFvmpUsndoGGyvQu9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21892,
      "cache_read_input_tokens": 77430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21892,
        "ephemeral_1h_input_tokens": 0
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

_source line 134 · 2026-05-27T13:13:46.301Z_

<details><summary>↩ Tool result · `toolu_01CeTQavZx9GkbGYMM5cWzFM`</summary>

```text
&lt;persisted-output>
Output too large (20.1KB). Full output saved to: /home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/afbbb6da-f35d-4c28-bef2-c4d0401e5725/tool-results/toolu_01CeTQavZx9GkbGYMM5cWzFM.txt

Preview (first 2KB):
paper_framing.md:59:[Omitted long matching line]
paper_framing.md:62:- LoRA-only (2 seeds): CAR=54.5%±2.8 (s0=56.5%, s1=52.5%), frozen=0%
paper_framing.md:63:- LoRA+SDF λ=0.005 (3 seeds): CAR=54.5%±2.3 (s0=57, s1=54, s2=52.5)
paper_framing.md:64:- LoRA+SDF λ=0.01 (3 seeds): CAR=56.33%±1.61 (s0=57, s1=57.5, s2=54.5) — p≈0.12 不显著，per-task 无系统提升，Task 3 驱动方差 s0=34%→s2=14% (D033)
paper_framing.md:75:**判定依据 (D033 阈值 + D035 确认)**：零分布 = LoRA(2) + l005(3) = 5 个无效 SDF 测量值 mean=54.5%, std=2.17%。λ=0.1 双 seed z=0.47，明确在噪声内。硬约束全部通过（TSR=51-54% ≥ 35%，frozen=0%）。
paper_framing.md:133:- **Key finding**: "Neither necessary nor sufficient" — (necessity) LoRA-only CAR=54.5% ≈ SDF across λ∈[0.005, 0.1], per-task ordering invariant; (sufficiency) oracle refinement CAR < baseline
ROADMAP.md:12:- **场景判定**: **Scenario C**（D038）——λ=0.1 2-seed mean=58.25%, z=2.27, p≈0.023
ROADMAP.md:21:| LoRA-only 30K | s0=57%, s1=52.5% | 54.75%±3.18 | s0 为 reeval_v2 |
ROADMAP.md:22:| SDF λ=0.005 30K | s0=57, s1=54, s2=52.5 | 54.5%±2.29 | |
ROADMAP.md:23:| SDF λ=0.01 30K | s0=57, s1=57.5, s2=54.5 | 56.33%±1.61 | |
ROADMAP.md:24:| **SDF λ=0.1 30K** | **s0=58, s1=58.5** | **58.25%±0.35** | **Scenario C, z=2.27** |
ROADMAP.md:61:| D038 | 2026-05-27 | D038: Scenario C 初步确认——λ=0.1 30K 2-seed mean=58.25 | eval_pi05_a1_30k_s0_l01_high, eval_pi05_a1_30k_s1_l01_high, reeval_lora_s0_30k_v2 |
ROADMAP.md:67:| D032 | 2026-05-26 | D032: 低 λ SDF 完全 redundant 确认（3-seed l005 CAR=54.5 | reeval_sdf_s1_l005_30k, reeval_sdf_s2_l005_30k, reeval_sdf_s0_l005_30k, eval_lora_baseline_30k_s0_reeval, reeval_lora_s1_30k |
artifacts/claim3_data_summary.md:8:| LoRA-only | 2 | s0=56.5, s1=52.5 | 54.5±2.83% | 51.5% | 54.5% | 0% | 0.392 |
artifacts/claim3_data_summary.md:9:| SDF λ=0.005 | 3 | s0=57.0, s1=54.0, s2=52.5 | 54.5±2.29% | 54.0±3.0% | 54.5% | 0% | 0.387 |
artifacts/claim3_data_summary.md:10:| SDF λ=0.01 | 3 | s0=57.0, s1=57.5, s2=54.5 | 56.3±1.61% | 53.8±1.5% | 56.3% | 0% | 0.389 |
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "02b943c8-e360-445b-ad7f-584f79251c1f"
}
```

</details>

---

### System

_source line 135_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Searching for eval_pi05_a1_30k_s1_l01_high|s1.*l01.*high|l01_hi…",
  "usage": {
    "total_tokens": 108546,
    "tool_uses": 39,
    "duration_ms": 71837
  },
  "last_tool_name": "Grep",
  "uuid": "44afe612-66e4-44f8-ab5c-d141fc77567e",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 136_

<details open><summary>🔧 Tool call — Grep · `toolu_01FEuY9Kioj2mVvzLcn1tvq3`</summary>

```json
{
  "pattern": "eval_pi05_a1_30k_s1_l01_high|s1.*l01.*high|l01_high",
  "-i": true,
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf",
  "glob": "*.{tex,md,csv}",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "799314c0-ca1d-4730-9b83-10a7af8ff936",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012pjY7VPSB8rpbzzj2cEk8E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9140,
      "cache_read_input_tokens": 99322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9140,
        "ephemeral_1h_input_tokens": 0
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

_source line 137 · 2026-05-27T13:13:51.476Z_

<details><summary>↩ Tool result · `toolu_01FEuY9Kioj2mVvzLcn1tvq3`</summary>

```text
ROADMAP.md:61:| D038 | 2026-05-27 | D038: Scenario C 初步确认——λ=0.1 30K 2-seed mean=58.25 | eval_pi05_a1_30k_s0_l01_high, eval_pi05_a1_30k_s1_l01_high, reeval_lora_s0_30k_v2 |
artifacts/training_progress_20260527.md:22:### 2. train_pi05_a1_obj_s0_l01_high (cuda:1, PID 271266)
artifacts/training_progress_20260527.md:31:### 3. train_pi05_a1_obj_s1_l01_high (cuda:2, PID 274407)
artifacts/training_progress_20260527.md:62:### 6. train_pi05_a1_obj_s2_l01_high (cuda:1, PID 425058)
artifacts/diagnose_l01_failures.md:10:## 实验 1: train_pi05_a1_obj_s1_l01_high（训练）
artifacts/diagnose_l01_failures.md:34:## 实验 2: eval_pi05_a1_30k_s0_l01_high（评估）
artifacts/eval_batch_20270527.md:41:- **When**: ~17:05 UTC 5/27 (after train_pi05_a1_obj_s0_l01_high finishes)
artifacts/eval_batch_20270527.md:45:- **Training registry**: train_pi05_a1_obj_s0_l01_high
artifacts/eval_batch_20270527.md:47:- **Output**: eval_sdf_s0_l01_high_30k.json
artifacts/eval_batch_20270527.md:48:- **Registry ID**: eval_sdf_s0_l01_high_30k
artifacts/eval_batch_20270527.md:52:- **When**: ~17:50 UTC 5/27 (after train_pi05_a1_obj_s1_l01_high finishes)
artifacts/eval_batch_20270527.md:56:- **Training registry**: train_pi05_a1_obj_s1_l01_high
artifacts/eval_batch_20270527.md:58:- **Output**: eval_sdf_s1_l01_high_30k.json
artifacts/eval_batch_20270527.md:59:- **Registry ID**: eval_sdf_s1_l01_high_30k
report.md:8:| train_pi05_a1_obj_s2_l01_high | westd-45947 cuda:1 | λ=0.1 s2 30K training, ETA ~01:00 5/28 |
report.md:27:- **eval_pi05_a1_30k_s1_l01_high** ✅ CAR=58.5%, TSR=49%, frozen=0%
report.md:28:- **eval_pi05_a1_30k_s0_l01_high** ✅ CAR=58.0%, TSR=47%, frozen=0%
report.md:57:- eval_pi05_a1_30k_s0_l01_high JSON 被 reeval_lora 覆盖（registry 数据正确）
task_context/history/reviewer/loop_6.md:31:- `train_pi05_a1_obj_s0_l01_high` — λ=0.1 s0, 46%, ~21h
task_context/history/reviewer/loop_6.md:32:- `train_pi05_a1_obj_s1_l01_high` — λ=0.1 s1, 44%, ~21.5h
task_context/history/agent/loop_3_1779875371.md:17:  - cuda:1: train_pi05_a1_obj_s0_l01_high (nohup, 无 timeout, ~84% → ~17:00 UTC 完成)
task_context/history/agent/loop_3_1779875371.md:18:  - cuda:2: train_pi05_a1_obj_s1_l01_high (nohup, 无 timeout, ~82% → ~17:30 UTC)
task_context/history/agent/loop_3_1779875371.md:22:  - cuda:1: train_pi05_a1_obj_s2_l01_high (tmux, timeout 48h, ~08:40 5/28 UTC)
task_context/history/agent/loop_3_1779875371.md:25:- **Cron 活跃**: 5 个（train_pi05_a1_obj_s0/s1/s2_l01_high, train_pi05_lora_baseline_s2_resume, train_spatial_bowl_lora_control_s0）
task_context/history/agent/loop_3_1779875371.md:37:- train_pi05_a1_obj_s0_l01_high 完成 → **立即跑 30K eval**（最高优先级，A/B/C 判定）
task_context/history/agent/loop_3_1779875371.md:38:- train_pi05_a1_obj_s1_l01_high 完成 → s1 30K eval
task_context/history/agent/loop_3_1779875371.md:43:- train_pi05_a1_obj_s0_l01_high 完成 (~17:00 UTC) → **立即** cuda:0@35807 跑 eval_l01_s0_30k（最高优先级，A/B/C 场景判定）
task_context/history/agent/loop_3_1779875371.md:44:- train_pi05_a1_obj_s1_l01_high 完成 (~17:30 UTC) → eval_l01_s1_30k
task_context/history/agent/loop_4.md:17:  - cuda:1 → `train_pi05_a1_obj_s0_l01_high` (PID 271266, log: `/root/colliforce-vla/logs/train_lambda01_s0_gpu1.log`)
task_context/history/agent/loop_4.md:18:  - cuda:2 → `train_pi05_a1_obj_s1_l01_high` (PID 274407, log: `/root/colliforce-vla/logs/train_lambda01_s1_gpu2.log`)
task_context/history/agent/loop_4.md:23:  - cuda:1 → `train_pi05_a1_obj_s2_l01_high` (PID 425058, cron 活跃)
task_context/history/agent/loop_4.md:34:- `train_pi05_a1_obj_s0_l01_high` — λ=0.1 seed0 (westd-35807:cuda:1, ~17:05 5/27)
task_context/history/agent/loop_4.md:35:- `train_pi05_a1_obj_s1_l01_high` — λ=0.1 seed1 (westd-35807:cuda:2, ~17:50 5/27)
task_context/history/agent/loop_4.md:38:- `train_pi05_a1_obj_s2_l01_high` — λ=0.1 seed2 (westd-45947:cuda:1, ~5/28)
task_context/history/agent/loop_3_1779836890.md:48:- train_pi05_a1_obj_s0_l01_high（westd-35807 cuda:1, λ=0.1）
task_context/history/agent/loop_3_1779836890.md:49:- train_pi05_a1_obj_s1_l01_high（westd-35807 cuda:2, λ=0.1）
task_context/history/agent/loop_3_1779855270.md:21:    - train_pi05_a1_obj_s0_l01_high (PID 271266, cuda:1, log: `/root/colliforce-vla/logs/train_lambda01_s0_gpu1.log`)
task_context/history/agent/loop_3_1779855270.md:22:    - train_pi05_a1_obj_s1_l01_high (PID 274407, cuda:2, log: `/root/colliforce-vla/logs/train_lambda01_s1_gpu2.log`)
task_context/history/agent/loop_3_1779855270.md:38:| train_pi05_a1_obj_s0_l01_high | westd-35807 | cuda:1 | λ=0.1 s0 30K 训练（最高优先级） | ~28h |
task_context/history/agent/loop_3_1779855270.md:39:| train_pi05_a1_obj_s1_l01_high | westd-35807 | cuda:2 | λ=0.1 s1 30K 训练（最高优先级） | ~29h |
task_context/history/agent/loop_3_1779855270.md:54:- train_pi05_a1_obj_s0/s1_l01_high 完成（~28h）→ **最高优先级** eval，λ=0.1 结果决定 Claim 4 叙事（D026 三场景 contingency）
task_context/history/agent/loop_3.md:17:  - cuda:1 → `train_pi05_a1_obj_s0_l01_high` (PID 271266, log: `/root/colliforce-vla/logs/train_lambda01_s0_gpu1.log`)
task_context/history/agent/loop_3.md:18:  - cuda:2 → `train_pi05_a1_obj_s1_l01_high` (PID 274407, log: `/root/colliforce-vla/logs/train_lambda01_s1_gpu2.log`)
task_context/history/agent/loop_3.md:33:- `train_pi05_a1_obj_s0_l01_high` — lambda=0.1 seed0 (westd-35807:cuda:1, ~22h)
task_context/history/agent/loop_3.md:34:- `train_pi05_a1_obj_s1_l01_high` — lambda=0.1 seed1 (westd-35807:cuda:2, ~22h)
task_context/history/director/loop_5.md:28:| train_pi05_a1_obj_s0_l01_high (plan_009 s0) | westd-35807:1 | 46% | ~21h |
task_context/history/director/loop_5.md:29:| train_pi05_a1_obj_s1_l01_high (plan_009 s1) | westd-35807:2 | 44% | ~21.5h |
task_context/history/director/loop_6.md:17:- Eval 命令模板已保存：`artifacts/eval_prep_l01_high.md`（λ=0.1 s0/s1/s2 + LoRA s2 全覆盖）
task_context/history/director/loop_6.md:21:  - westd-35807 cuda:1: train_pi05_a1_obj_s0_l01_high (PID 271266, ~17:00 UTC 5/27)
task_context/history/director/loop_6.md:22:  - westd-35807 cuda:2: train_pi05_a1_obj_s1_l01_high (PID 274407, ~17:45 UTC 5/27)
task_context/history/director/loop_6.md:25:  - westd-45947 cuda:1: train_pi05_a1_obj_s2_l01_high (PID 425058, ~08:40 UTC 5/28)
task_context/history/director/loop_6.md:39:- λ=0.1 s0 训练完成（~17:00 UTC 5/27）→ 立即启动 eval（命令在 artifacts/eval_prep_l01_high.md）
task_context/director.md:25:- Agent 正在处理 worker 回调：eval_s0_30k 和 diagnose_train_pi05_a1_obj_s0_l01_high
task_context/director.md:31:  - `eval_pi05_a1_30k_s0_l01_high` — λ=0.1 s0 30K eval（最高优先级，Agent 正在处理回调）
task_context/agent.md:20:  - train_pi05_a1_obj_s2_l01_high: PID 425058 (westd-45947 cuda:1, ~ETA 08:40 UTC 5/28)
task_context/agent.md:30:- `eval_pi05_a1_30k_s1_l01_high` — λ=0.1 s1 30K eval，标记 RUNNING 但无 PID。Worker `worker_eval_eval_pi05_a1_30k_s1_l01_high` 已于 10:04 UTC 完成。**下一个"我"首要任务: 检查这个 eval 是否真的在跑、结果是否已出**
task_context/agent.md:34:- `train_pi05_a1_obj_s2_l01_high` — λ=0.1 s2 训练，PID 425058，~ETA 08:40 UTC 5/28
task_context/agent.md:43:- **立即**: SSH 检查 eval_pi05_a1_30k_s1_l01_high 和 reeval_lora_s0_30k_v2 是否已完成 → 如已完成，读取结果 JSON → 更新 registry → 汇报 Director
task_context/agent.md:44:- eval_pi05_a1_30k_s1_l01_high 结果出来 → 与 s0 CAR=58% 取均值 → 最终 A/B/C 判定（预期 Scenario B: ≤57% mean）→ 填 claim3 §6.3 + discussion + abstract 的 λ=0.1 placeholder
task_context/agent.md:49:- train_pi05_a1_obj_s2_l01_high cron 回调 → eval 30K → 第三 seed λ=0.1 → 3-seed 统计（可能赶不上 DDL）
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "dcb54c34-c6a2-4dc7-8e73-d33bfa002996"
}
```

</details>

---

### System

_source line 138_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Searching for 0\\.3884|0\\.0553|ee_disp|avg_max_ee|avg_max_obstac…",
  "usage": {
    "total_tokens": 108547,
    "tool_uses": 40,
    "duration_ms": 73697
  },
  "last_tool_name": "Grep",
  "uuid": "a58e8743-1bfe-4e97-9c79-f6ae39dec0aa",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 139_

<details open><summary>🔧 Tool call — Grep · `toolu_01L8Q3JfjyCF12MAAK6atuNP`</summary>

```json
{
  "pattern": "0\\.3884|0\\.0553|ee_disp|avg_max_ee|avg_max_obstacle",
  "-i": true,
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf",
  "glob": "*.{tex,md,csv,txt}",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "3b0a687e-b690-4bab-82b3-a6cda6652095",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012pjY7VPSB8rpbzzj2cEk8E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9140,
      "cache_read_input_tokens": 99322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9140,
        "ephemeral_1h_input_tokens": 0
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

_source line 140 · 2026-05-27T13:13:53.336Z_

<details><summary>↩ Tool result · `toolu_01L8Q3JfjyCF12MAAK6atuNP`</summary>

```text
artifacts/task3_collision_matrix_step10k.md:123:| 29 | ✗ | ✓ | wine_bottle | 0.0553 | 0.199 | 300 |
artifacts/paper_data_summary.md:15:| Seed | Ckpt | Step | avg_TSR | avg_CAR | avg_ee_disp | fake_safe% | frozen | exp_id | 备注 |
artifacts/paper_data_summary.md:23:| 1 | best | 16K | 6.5 | 53.0 | 0.37~0.65² | **0%** | **No** | eval_pi05_a1_best_s1_l005_16k | ✅🔧 has ee_disp |
artifacts/paper_data_summary.md:28:¹ obstacle displacement (旧脚本), 非 ee_displacement
artifacts/paper_data_summary.md:29:² per-task ee_disp: task0=0.5179, task1=0.5146, task2=0.6475, task3=0.3707
artifacts/paper_data_summary.md:33:| Seed | Ckpt | Step | avg_TSR | avg_CAR | avg_ee_disp | fake_safe% | frozen | exp_id | 备注 |
artifacts/paper_data_summary.md:45:| 配置 | avg_CAR | avg_TSR | avg_ee_disp | fake_safe% |
artifacts/paper_data_summary.md:75:**注意**: displacement 指 obstacle displacement（物体位移），非 ee_displacement。safe_disp_mean 极低(0.0003~0.008mm)证明机器人近乎完全冻结。
artifacts/paper_data_summary.md:153:| 配置 | Step | CAR | TSR | avg_ee_disp | fake_safe% | exp_id |
artifacts/paper_data_summary.md:162:| Task | ee_disp | safe_ee_disp | CAR |
artifacts/paper_data_summary.md:171:| Task | ee_disp | safe_ee_disp | CAR |
artifacts/paper_data_summary.md:178:**结论**: 30K 和 best checkpoint 的 ee_displacement 量级相近（0.47-0.50m），均远高于 frozen 阈值（0.1mm）。fake_safe% 全部为 0。30K 的 CAR 升高不是因为 frozen/action collapse，而是 over-avoidance（真正在避障，但更保守导致 TSR 下降）。
artifacts/report_action_scale_fix.md:108:ee_displacement = float(np.linalg.norm(np.array(trajectory[-1]) - np.array(trajectory[0])))
artifacts/verify_22k_eval_report.md:24:| Task | CAR | TSR | avg_smoothness | avg_max_disp | avg_max_ee_disp |
artifacts/verify_22k_eval_report.md:32:所有 task 的 avg_max_ee_displacement > 0.3m，确认无 frozen episode。
artifacts/_project/data/task3_collision_matrix_step10k.md:123:| 29 | ✗ | ✓ | wine_bottle | 0.0553 | 0.199 | 300 |
artifacts/_project/data/paper_data_summary.md:15:| Seed | Ckpt | Step | avg_TSR | avg_CAR | avg_ee_disp | fake_safe% | frozen | exp_id | 备注 |
artifacts/_project/data/paper_data_summary.md:23:| 1 | best | 16K | 6.5 | 53.0 | 0.37~0.65² | **0%** | **No** | eval_pi05_a1_best_s1_l005_16k | ✅🔧 has ee_disp |
artifacts/_project/data/paper_data_summary.md:28:¹ obstacle displacement (旧脚本), 非 ee_displacement
artifacts/_project/data/paper_data_summary.md:29:² per-task ee_disp: task0=0.5179, task1=0.5146, task2=0.6475, task3=0.3707
artifacts/_project/data/paper_data_summary.md:33:| Seed | Ckpt | Step | avg_TSR | avg_CAR | avg_ee_disp | fake_safe% | frozen | exp_id | 备注 |
artifacts/_project/data/paper_data_summary.md:45:| 配置 | avg_CAR | avg_TSR | avg_ee_disp | fake_safe% |
artifacts/_project/data/paper_data_summary.md:75:**注意**: displacement 指 obstacle displacement（物体位移），非 ee_displacement。safe_disp_mean 极低(0.0003~0.008mm)证明机器人近乎完全冻结。
artifacts/_project/data/paper_data_summary.md:153:| 配置 | Step | CAR | TSR | avg_ee_disp | fake_safe% | exp_id |
artifacts/_project/data/paper_data_summary.md:162:| Task | ee_disp | safe_ee_disp | CAR |
artifacts/_project/data/paper_data_summary.md:171:| Task | ee_disp | safe_ee_disp | CAR |
artifacts/_project/data/paper_data_summary.md:178:**结论**: 30K 和 best checkpoint 的 ee_displacement 量级相近（0.47-0.50m），均远高于 frozen 阈值（0.1mm）。fake_safe% 全部为 0。30K 的 CAR 升高不是因为 frozen/action collapse，而是 over-avoidance（真正在避障，但更保守导致 TSR 下降）。
memory.md:83:- **可信数据**: LoRA s0: TSR=51.5%, CAR=56.5%, avg_max_ee_disp=0.3957
task_context/history/reviewer/loop_5.md:39:- eval_pi05_a1_30k_s1_l005_disp 完成 → 验证 30K displacement 数据加入后 frozen 100% 模式是否持续（预期是），确认修复脚本正确输出 max_ee_displacement 字段
task_context/history/agent/loop_2.md:12:- Displacement 修复刚合入但当前 RUNNING eval 用的是旧代码（已加载到内存），输出 JSON **不含** `max_ee_displacement`。修复验证需等 GPU 空闲后重跑
task_context/history/agent/loop_2.md:67:- **P0 bug**：`analyze_displacement.py` 的 frozen 检测用障碍物位移而非 EE 位移，导致 Filtered CAR ≡ 0% 是数学恒等式。**代码已修复**（新增 `max_ee_displacement` + `total_ee_path_length`），但未经验证。所有已发布的 Filtered CAR=0% 数据需要用 EE displacement 重新计算
task_context/history/agent/loop_3_1779836890.md:62:- Displacement 数据缺口：s0_l005 和 s0_l01 需用新版脚本重跑（有 max_ee_displacement），排在 westd-45947 LoRA eval 完成后
task_context/history/director/loop_4.md:36:- eval_pi05_a1_30k_s1_l005_disp 完成 → 第一时间分析 max_ee_displacement，验证 30K action collapse 是否跨 seed1 成立
docs/IDEA_BRIEF.md:182:Pi0.5+A1 SDF (3 seeds avg): CAR=50-55% (+25pp vs baseline), TSR=5-9% (-65pp vs baseline), avg_max_ee_displacement=0.47-0.51m, fake_safe_rate=0%. Pi0.5 baseline: CAR=27%, TSR=73%. A1 openpi fake safety: 91.5% CAR with 99.6% obstacle-displacement-based fake rate. Claim validity: Claim 1 ★★★★★, Claim 2 ★★★, Claim 3 ★★★★, Claim 4 (revised) ★★★★.
docs/paper/appendix.tex:6:\includegraphics[width=\linewidth]{fig2_ee_displacement_distribution}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "eed85780-5bdd-4987-8dbe-ff9611321472"
}
```

</details>

---

### System

_source line 141_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Searching for reeval_v2|reeval_lora.*v2|s0.*reeval",
  "usage": {
    "total_tokens": 108548,
    "tool_uses": 41,
    "duration_ms": 75155
  },
  "last_tool_name": "Grep",
  "uuid": "bcff7cee-ae6f-4f57-8a6e-62969a1232f5",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 142_

<details open><summary>🔧 Tool call — Grep · `toolu_01W212BsPUY2gLKmTeXMcwQq`</summary>

```json
{
  "pattern": "reeval_v2|reeval_lora.*v2|s0.*reeval",
  "-i": true,
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf",
  "glob": "*.{tex,md,csv}",
  "output_mode": "content",
  "head_limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "05248b77-ba22-42c7-bd5e-117e64462246",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012pjY7VPSB8rpbzzj2cEk8E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9140,
      "cache_read_input_tokens": 99322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9140,
        "ephemeral_1h_input_tokens": 0
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

_source line 143 · 2026-05-27T13:13:54.792Z_

<details><summary>↩ Tool result · `toolu_01W212BsPUY2gLKmTeXMcwQq`</summary>

```text
ROADMAP.md:13:- **Null distribution**: mean=54.6%, σ=2.27%（LoRA s0 reeval 57% 已纳入）
ROADMAP.md:21:| LoRA-only 30K | s0=57%, s1=52.5% | 54.75%±3.18 | s0 为 reeval_v2 |
ROADMAP.md:38:- [x] LoRA s0 30K reeval → CAR=57%
ROADMAP.md:61:| D038 | 2026-05-27 | D038: Scenario C 初步确认——λ=0.1 30K 2-seed mean=58.25 | eval_pi05_a1_30k_s0_l01_high, eval_pi05_a1_30k_s1_l01_high, reeval_lora_s0_30k_v2 |
ROADMAP.md:66:| D033 | 2026-05-26 | D033: λ=0.1 A/B/C 场景量化阈值定义 + l01 2-seed 57.25% 判定为 | reeval_sdf_s0_l01_30k, reeval_sdf_s1_l01_30k, eval_lora_baseline_30k_s0_reeval, reeval_lora_s1_30k |
ROADMAP.md:67:| D032 | 2026-05-26 | D032: 低 λ SDF 完全 redundant 确认（3-seed l005 CAR=54.5 | reeval_sdf_s1_l005_30k, reeval_sdf_s2_l005_30k, reeval_sdf_s0_l005_30k, eval_lora_baseline_30k_s0_reeval, reeval_lora_s1_30k |
artifacts/eval_prep_l01_high.md:193:| λ=0.05 s0 | ✅ | ✅ 35807 | ✅ 45947 reeval | |
artifacts/eval_prep_l01_high.md:196:| **λ=0.1 s0** | ✅ | ✅ 35807 | ✅ 45947 reeval | |
artifacts/eval_batch_20270527.md:81:LoRA s0 eval is ALREADY DONE (eval_lora_baseline_30k_s0_reeval, CAR=56.5%). No re-eval needed unless Director specifies otherwise. The freed cuda:0 at 06:30 should be used for spatial_bowl SDF s0 eval (Eval 1).
artifacts/_project/data/ssr_analysis.md:39:- SDF lambda=0.1 s0 JSON overwritten by reeval_lora. Only 1 seed available for lambda=0.1.
artifacts/ssr_analysis.md:39:- SDF lambda=0.1 s0 JSON overwritten by reeval_lora. Only 1 seed available for lambda=0.1.
report.md:29:- **reeval_lora_s0_30k_v2** ✅ CAR=57%, TSR=46%
report.md:57:- eval_pi05_a1_30k_s0_l01_high JSON 被 reeval_lora 覆盖（registry 数据正确）
memory.md:82:## ✅ M044: LoRA s0 reeval 数据已验证有效（2026-05-26, CLOSED）
task_context/history/reviewer/loop_6.md:11:- `eval_lora_baseline_30k_s0_reeval` registry 条目缺 metrics 字段——引用该实验数据时必须从 JSON 文件交叉验证，不能只看 registry。
task_context/history/agent/loop_4.md:40:**PREPARING (2)**: `reeval_lora_s0_30k_v2`, `eval_pi05_a1_best_s0_l005` — 等 GPU 空闲
task_context/history/agent/loop_4.md:45:- **spatial_bowl SDF 完成 (~06:30 5/27)** → 立即在同 GPU 启动 plan_008 eval；westd-35807:cuda:0 释放后可跑 reeval_lora_s0_30k_v2 或 eval_pi05_a1_best_s0_l005
task_context/history/director/loop_5.md:19:- 活跃 tmux sessions：spatial_bowl SDF s0 (cuda:0)、λ=0.1 s0 (cuda:1)、λ=0.1 s1 (cuda:2)、LoRA s2 (westd-45947 cuda:0)、reeval batch2 (westd-45947 cuda:1)
task_context/history/director/loop_5.md:53:**新数据信号**：SDF λ=0.005 s0 reeval → TSR=55.5%, CAR=57.0%（vs LoRA mean 51.5%/54.5%，+4pp/+2.5pp）。单 seed 有噪声，但如果 s1/s2 确认，低 λ 可能也不完全 redundant——这会改变叙事方向。batch2 数据是关键。
task_context/director.md:34:- **PENDING**: reeval_lora_s0_30k_v2（LoRA s0 重评）、eval_pi05_a1_best_s0_l005（best checkpoint eval）
task_context/agent.md:31:- `reeval_lora_s0_30k_v2` — LoRA s0 30K reeval (rotation-fixed)，标记 RUNNING 但无 PID。Worker 已于 09:51 UTC 完成。**同上: 检查实际状态**
task_context/agent.md:43:- **立即**: SSH 检查 eval_pi05_a1_30k_s1_l01_high 和 reeval_lora_s0_30k_v2 是否已完成 → 如已完成，读取结果 JSON → 更新 registry → 汇报 Director
task_context/agent.md:47:- reeval_lora_s0_30k_v2 结果出来 → 更新 Claim 3 LoRA baseline 3-seed 统计（当前 2 seed: s0=56.5%, s1=52.5%）
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "d2464d1e-ef74-4a29-975d-f7d972b14ff6"
}
```

</details>

---

### System

_source line 144_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Searching for 57%.*46%|CAR=57|TSR=46|s0=57|s0.*reeval.*57",
  "usage": {
    "total_tokens": 117139,
    "tool_uses": 42,
    "duration_ms": 82876
  },
  "last_tool_name": "Grep",
  "uuid": "97a3038c-fb92-46d3-9593-4a9e333bcf98",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 145_

<details open><summary>🔧 Tool call — Grep · `toolu_01GYBSM8zBVSmXU62k2LdMPE`</summary>

```json
{
  "pattern": "57%.*46%|CAR=57|TSR=46|s0=57|s0.*reeval.*57",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf",
  "glob": "*.{tex,md}",
  "output_mode": "content",
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "fb726243-4ae4-40b0-beef-d366a5ca520e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UpH1g9Tn5mNK8UoMUQCe5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8589,
      "cache_read_input_tokens": 108462,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8589,
        "ephemeral_1h_input_tokens": 0
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

_source line 146 · 2026-05-27T13:14:02.521Z_

<details><summary>↩ Tool result · `toolu_01GYBSM8zBVSmXU62k2LdMPE`</summary>

```text
paper_framing.md:63:- LoRA+SDF λ=0.005 (3 seeds): CAR=54.5%±2.3 (s0=57, s1=54, s2=52.5)
paper_framing.md:64:- LoRA+SDF λ=0.01 (3 seeds): CAR=56.33%±1.61 (s0=57, s1=57.5, s2=54.5) — p≈0.12 不显著，per-task 无系统提升，Task 3 驱动方差 s0=34%→s2=14% (D033)
ROADMAP.md:13:- **Null distribution**: mean=54.6%, σ=2.27%（LoRA s0 reeval 57% 已纳入）
ROADMAP.md:21:| LoRA-only 30K | s0=57%, s1=52.5% | 54.75%±3.18 | s0 为 reeval_v2 |
ROADMAP.md:22:| SDF λ=0.005 30K | s0=57, s1=54, s2=52.5 | 54.5%±2.29 | |
ROADMAP.md:23:| SDF λ=0.01 30K | s0=57, s1=57.5, s2=54.5 | 56.33%±1.61 | |
ROADMAP.md:38:- [x] LoRA s0 30K reeval → CAR=57%
ROADMAP.md:68:| D031 | 2026-05-26 | D029 标记 provisional：Phase 2 CAR=57.5% 更接近 SDF (57% | eval_phase2_lambda0_s2, reeval_lora_s1_30k, reeval_sdf_s0_l005_30k |
artifacts/claim3_data_summary.md:9:| SDF λ=0.005 | 3 | s0=57.0, s1=54.0, s2=52.5 | 54.5±2.29% | 54.0±3.0% | 54.5% | 0% | 0.387 |
artifacts/claim3_data_summary.md:10:| SDF λ=0.01 | 3 | s0=57.0, s1=57.5, s2=54.5 | 56.3±1.61% | 53.8±1.5% | 56.3% | 0% | 0.389 |
artifacts/claim3_data_summary.md:73:- Phase 2 ablation (λ=0 after 5K): CAR=57.5%
artifacts/_project/data/claim3_data_summary.md:9:| SDF λ=0.005 | 3 | s0=57.0, s1=54.0, s2=52.5 | 54.5±2.29% | 54.0±3.0% | 54.5% | 0% | 0.387 |
artifacts/_project/data/claim3_data_summary.md:10:| SDF λ=0.01 | 3 | s0=57.0, s1=57.5, s2=54.5 | 56.3±1.61% | 53.8±1.5% | 56.3% | 0% | 0.389 |
artifacts/_project/data/claim3_data_summary.md:73:- Phase 2 ablation (λ=0 after 5K): CAR=57.5%
report.md:29:- **reeval_lora_s0_30k_v2** ✅ CAR=57%, TSR=46%
memory.md:87:- Phase 2 λ=0 s2 (10K step): TSR=53.5%, CAR=57.5%, Frozen(EE)=0%
task_context/history/agent/loop_4.md:56:- **已有可信数据**: Pi0.5 base CAR=28.5% | LoRA-only CAR=54.5%±2.83 | SDF λ=0.005 CAR=54.5%±2.29 | SDF λ=0.01 CAR=56.33%±1.61 (p≈0.12, 噪声) | Phase 2 λ=0 CAR=57.5% (single seed)
task_context/history/director/loop_5.md:53:**新数据信号**：SDF λ=0.005 s0 reeval → TSR=55.5%, CAR=57.0%（vs LoRA mean 51.5%/54.5%，+4pp/+2.5pp）。单 seed 有噪声，但如果 s1/s2 确认，低 λ 可能也不完全 redundant——这会改变叙事方向。batch2 数据是关键。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "77b56c1a-ee5c-479c-b7ff-d4bd2c559f32"
}
```

</details>

---

### System

_source line 147_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Finding **/*.tex",
  "usage": {
    "total_tokens": 117140,
    "tool_uses": 43,
    "duration_ms": 83163
  },
  "last_tool_name": "Glob",
  "uuid": "831bd9c4-0889-4f9c-aaf1-6ba5d7b99eab",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 148_

<details open><summary>🔧 Tool call — Glob · `toolu_01XkvugKCSVgL1wMrBk3sAJH`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "6bd7e15e-8116-4094-b42a-7f12c0cd0a4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UpH1g9Tn5mNK8UoMUQCe5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8589,
      "cache_read_input_tokens": 108462,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8589,
        "ephemeral_1h_input_tokens": 0
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

_source line 149 · 2026-05-27T13:14:02.781Z_

<details><summary>↩ Tool result · `toolu_01XkvugKCSVgL1wMrBk3sAJH`</summary>

```text
docs/paper/_archive/method.tex
docs/paper/_archive/experiments.tex
docs/paper/_archive/conclusion_DEPRECATED.tex
docs/paper/archive/analysis_claim4.tex
docs/paper/archive/analysis_claim3.tex
docs/paper/archive/analysis_claim1.tex
docs/paper/archive/analysis_claim2.tex
docs/paper/contingency_claim3.tex
docs/paper/experimental_framework.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/appendix.tex
docs/paper/main.tex
docs/paper/discussion.tex
docs/paper/related_work.tex
docs/paper/claim1.tex
docs/paper/claim2.tex
docs/paper/claim3.tex
docs/paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "f0282467-43b7-4221-a4c8-517ee9da9f59"
}
```

</details>

---

### System

_source line 150_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Searching for per.task_tsr|per_task|appendix",
  "usage": {
    "total_tokens": 117141,
    "tool_uses": 44,
    "duration_ms": 84244
  },
  "last_tool_name": "Grep",
  "uuid": "ac7aec75-7b63-4f59-bee0-4e8b56020d42",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 151_

<details open><summary>🔧 Tool call — Grep · `toolu_01Bt4PsAB6nahBRwr9yRsd6v`</summary>

```json
{
  "pattern": "per.task_tsr|per_task|appendix",
  "-i": true,
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf",
  "glob": "*.tex",
  "output_mode": "content",
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "08671cfb-2a10-4ca0-afa7-bffb962d8c0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UpH1g9Tn5mNK8UoMUQCe5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8589,
      "cache_read_input_tokens": 108462,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8589,
        "ephemeral_1h_input_tokens": 0
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

_source line 152 · 2026-05-27T13:14:03.876Z_

<details><summary>↩ Tool result · `toolu_01Bt4PsAB6nahBRwr9yRsd6v`</summary>

```text
artifacts/dream_reports/dream_20260525T223036/best/paper.tex:178:\paragraph{Per-task variation.} Table~\ref{tab:per_task_lora} reveals interesting asymmetry: task \texttt{milk} shows +70pp CAR improvement from SDF while \texttt{bbq\_sauce} shows $-$24pp, likely related to obstacle geometry---consistent with the EE-only SDF limitation (the SDF gradient pushes the end-effector away but may cause the arm body to sweep through obstacles positioned at different heights).
artifacts/dream_reports/dream_20260525T223036/best/paper.tex:183:\label{tab:per_task_lora}
artifacts/dream_reports/dream_20260525T223036/worst/paper.tex:336:\appendix
artifacts/drafts/experimental_framework.tex:23:where $d_{\max}(e)$ denotes the maximum Euclidean displacement of the end-effector across all timesteps in episode $e$. The threshold $\tau_d = 0.1$\,mm corresponds to sub-actuator-resolution motion and is robust to perturbation (Appendix~\ref{app:threshold_sensitivity}).
artifacts/drafts/analysis_claim1.tex:32:[Omitted long matching line]
artifacts/_project/paper/experimental_framework.tex:23:where $d_{\max}(e)$ denotes the maximum Euclidean displacement of the end-effector across all timesteps in episode $e$. The threshold $\tau_d = 0.1$\,mm corresponds to sub-actuator-resolution motion and is robust to perturbation (Appendix~\ref{app:threshold_sensitivity}).
docs/paper/main.tex:43:\appendix
docs/paper/main.tex:44:\input{appendix}
docs/paper/claim3.tex:27:[Omitted long matching line]
docs/paper/claim3.tex:30:Fine-tuning degrades TSR by ${\sim}$21--26\,pp (74.7\% $\to$ 48.75--54.0\%), reflecting distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\,0.37\,m displacement and 0\% frozen episodes). The SSR/TSR ratio increases from 0.33 (baseline) to 0.51--0.58 (Appendix~\ref{sec:appendix_ssr}), confirming that among task-completing episodes, a larger fraction avoids collisions after fine-tuning.
docs/paper/claim3.tex:33:[Omitted long matching line]
docs/paper/discussion.tex:12:[Omitted long matching line]
docs/paper/experimental_framework.tex:23:where $d_{\max}(e)$ denotes the maximum Euclidean displacement of the end-effector across all timesteps in episode $e$. The threshold $\tau_d = 0.1$\,mm corresponds to sub-actuator-resolution motion. In practice, the displacement distribution is bimodal: collapsed episodes cluster below 1\,$\mu$m and active episodes exceed 200\,mm, with no intermediate population. Consequently, any $\tau_d \in [2, 200]$\,mm produces identical filtering (Appendix~\ref{sec:appendix_threshold}).
docs/paper/method.tex:36:The displacement distribution is sharply bimodal, with collapsed episodes below 1\,$\mu$m and active episodes above 200\,mm; any $\tau_d \in [2, 200]$\,mm yields identical results (Appendix~\ref{sec:appendix_threshold}).\footnote{See Section~\ref{sec:fake_safety} for details on the displacement measurement protocol.}
docs/paper/method.tex:40:We augment LoRA-adapted~\cite{hu2022lora} VLAs with an SDF decoder and an EE position extractor (Appendix~\ref{sec:appendix_training}, Table~\ref{tab:hyperparams}). The total loss is:
docs/paper/method.tex:44:where $\lambda \in \{0.005, 0.01, 0.1\}$. In Pi0+A1, a parameter-name mismatch prevented LoRA loading, causing action collapse (TSR\,=\,0\%; Table~\ref{tab:configurations}). To test the upper bound of EE-only refinement (Section~\ref{sec:ee_only}), we also replace the learned SDF with ground-truth distance fields from the simulation geometry in three oracle variants (Appendix~\ref{sec:appendix_oracle}).\label{sec:oracle_setup}
docs/paper/archive/analysis_claim1.tex:31:[Omitted long matching line]
docs/paper/archive/analysis_claim3.tex:31:[Omitted long matching line]
docs/paper/archive/analysis_claim3.tex:36:\label{tab:per_task_tsr}
docs/paper/claim2.tex:7:\caption{Oracle SDF refinement with ground-truth distance fields. All oracle variants achieve lower CAR than unrefined baselines. Per-task breakdown in Appendix~\ref{sec:appendix_pertask_oracle}.}

[Showing results with pagination = limit: 20]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "f01d623b-a187-4f5b-863a-ad7c4648a2a7"
}
```

</details>

---

### System

_source line 153_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading docs/paper/claim3.tex",
  "usage": {
    "total_tokens": 120464,
    "tool_uses": 45,
    "duration_ms": 88315
  },
  "last_tool_name": "Read",
  "uuid": "6704ab27-e395-4b72-8dc2-005eaab41f41",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 154_

<details open><summary>🔧 Tool call — Read · `toolu_01EFozbpBkGFhtXY2JMUgquF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "18ea4835-13a6-4158-b880-f0af8191c40c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CKKj1EPqVPoyuj9keKxFFv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3317,
      "cache_read_input_tokens": 117051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3317,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 155 · 2026-05-27T13:14:07.922Z_

<details><summary>↩ Tool result · `toolu_01EFozbpBkGFhtXY2JMUgquF`</summary>

```text
1	\section{Avoidance Source Diagnosis}\label{sec:avoidance_source}
2	
3	Fine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\sim}$28 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only, LoRA+SDF ($\lambda = 0.005$), and LoRA+SDF ($\lambda = 0.01$) on Pi0.5, all evaluated at the 30K-step checkpoint.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Avoidance source attribution on SafeLIBERO. SDF at $\lambda \leq 0.01$ adds no measurable CAR beyond LoRA-only ($p > 0.1$); $\lambda = 0.1$ shows a marginal signal ($z = 2.27$, $p \approx 0.023$, $n{=}2$) that requires additional seeds. All fine-tuned models exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}
8	\label{tab:avoidance_source}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lcccc}
12	\toprule
13	Method & Seeds & TSR (\%) & CAR (\%) & EE Disp (m) \\
14	\midrule
15	Pi0.5 baseline & 3 & 74.7\,$\pm$\,1.5 & 26.8\,$\pm$\,1.6 & 0.367 \\
16	\midrule
17	LoRA-only (no SDF) & 2 & 48.75 & 54.75\,$\pm$\,3.18 & 0.392 \\
18	LoRA+SDF $\lambda{=}0.005$ & 3 & 54.0\,$\pm$\,3.0 & 54.5\,$\pm$\,2.29 & 0.387 \\
19	LoRA+SDF $\lambda{=}0.01$ & 3 & 53.8\,$\pm$\,1.5 & 56.33\,$\pm$\,1.61 & 0.389 \\
20	LoRA+SDF $\lambda{=}0.1$\textsuperscript{$\dagger$} & 2 & 48.0\,$\pm$\,1.4 & 58.25\,$\pm$\,0.35 & 0.394 \\
21	\bottomrule
22	\end{tabular}
23	\vspace{1pt}
24	{\footnotesize \textsuperscript{$\dagger$}30K checkpoint, two of three seeds; third seed in progress.}
25	\end{table}
26	
27	Table~\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\sim}$28 percentage points (26.8\% $\to$ 54.75\%) with zero frozen episodes and displacement above 0.37\,m, confirming genuine avoidance. Adding SDF supervision produces no measurable benefit: LoRA-only CAR (54.75\%) is within 0.25\,pp of $\lambda = 0.005$ and statistically indistinguishable from $\lambda = 0.01$ (56.33\%, $p > 0.1$; Appendix~\ref{sec:appendix_null}). A Phase~2 ablation ($\lambda = 0$ after step 5K) yields CAR\,=\,57.5\%\footnote{Single seed (s2); computational constraints precluded additional seeds for this ablation.}, confirming that SDF gradients produce no lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\_pudding highest, bbq\_sauce lowest) and invariant to $\lambda$ across a 20$\times$ range, indicating that avoidance patterns reflect the demonstration distribution rather than geometric supervision.
28	
29	\paragraph{CAR--TSR trade-off.}\label{sec:tsr_collapse}
30	Fine-tuning degrades TSR by ${\sim}$21--26\,pp (74.7\% $\to$ 48.75--54.0\%), reflecting distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\,0.37\,m displacement and 0\% frozen episodes). The SSR/TSR ratio increases from 0.33 (baseline) to 0.51--0.58 (Appendix~\ref{sec:appendix_ssr}), confirming that among task-completing episodes, a larger fraction avoids collisions after fine-tuning.
31	
32	\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
33	Increasing $\lambda$ by 20$\times$ to 0.1 yields CAR\,=\,58.25\%\,$\pm$\,0.35 at the 30K checkpoint (two of three seeds), above the null distribution (mean 54.6\%, $\sigma = 2.27$, $z = 2.27$, $p \approx 0.023$). This departure is suggestive but inconclusive at $n = 2$. A stepwise ablation across six checkpoints (16K--28K) shows no sustained trend (mean 55.3\%, within 0.3$\sigma$ of the null; Appendix~\ref{sec:appendix_stepwise}), and per-task CAR ordering at 30K remains identical to all other conditions (Figure~\ref{fig:lambda_car}). The response is thus dose-dependent: SDF is fully redundant at $\lambda \leq 0.01$ ($p > 0.1$), with a marginal signal at $\lambda = 0.1$ whose modest effect size (${\sim}$3.7\,pp) and limited sample preclude strong conclusions. Even at elevated $\lambda$, avoidance patterns remain driven by demonstration distribution rather than geometric supervision.
34	
35	\begin{figure}[t]
36	\centering
37	\includegraphics[width=0.85\linewidth]{fig5_lambda_curve}
38	\caption{Effect of SDF loss weight $\lambda$ on CAR and TSR. $\lambda = 0$: LoRA-only. Low $\lambda$ ($\leq 0.01$) remains within the null band; $\lambda = 0.1$ (58.25\%, 2 seeds) shows a marginal departure ($p \approx 0.023$) whose per-task pattern still matches the demonstration distribution.}
39	\label{fig:lambda_car}
40	\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "33aff289-1795-4756-a5b7-52e00e07320c"
}
```

</details>

---

### System

_source line 156_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading docs/paper/appendix.tex",
  "usage": {
    "total_tokens": 120467,
    "tool_uses": 46,
    "duration_ms": 88573
  },
  "last_tool_name": "Read",
  "uuid": "58489dcd-f4a4-4dd4-a149-2785f88d2454",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 157_

<details open><summary>🔧 Tool call — Read · `toolu_01QArKCu2zR2YaZbQ4eQtehp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "7b8259ab-17b7-45db-9778-342796923a50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CKKj1EPqVPoyuj9keKxFFv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3317,
      "cache_read_input_tokens": 117051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3317,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 158 · 2026-05-27T13:14:08.180Z_

<details><summary>↩ Tool result · `toolu_01QArKCu2zR2YaZbQ4eQtehp`</summary>

```text
1	\section{Displacement Distribution}
2	\label{sec:appendix_displacement}
3	
4	\begin{figure}[h]
5	\centering
6	\includegraphics[width=\linewidth]{fig2_ee_displacement_distribution}
7	\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\,$\mu$m, while Pi0.5 episodes (orange) exceed 200\,mm. The five-order-of-magnitude gap makes $\tau_d$ robust to any value in $[2, 200]$\,mm.}
8	\label{fig:displacement}
9	\end{figure}
10	
11	\section{Displacement Threshold Sensitivity Analysis}
12	\label{sec:appendix_threshold}
13	
14	To validate the robustness of our displacement threshold $\tau_d$, we evaluate the frozen rate across four orders of magnitude. Table~\ref{tab:threshold_sensitivity} shows that the fake safety pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\% frozen rate even at the most conservative setting.
15	
16	\begin{table}[h]
17	\centering
18	\caption{Frozen rate (\% of episodes with $d_\mathrm{max} < \tau_d$) across threshold values.}
19	\label{tab:threshold_sensitivity}
20	\begin{tabular}{lccc}
21	\toprule
22	$\tau_d$ & A1-LoRA (Pi0) & Pi0.5 Baseline & Pi0.5+A1 (SDF aux) \\
23	\midrule
24	0.001 mm (1\,$\mu$m) & 73.9 & 0.0 & 0.0 \\
25	0.1 mm  & 99.6 & 0.0 & 0.0 \\
26	1.0 mm  & 100.0 & 0.0 & 0.0 \\
27	10 mm   & 100.0 & 0.0 & 0.0 \\
28	\bottomrule
29	\end{tabular}
30	\end{table}
31	
32	The choice of $\tau_d = 0.1$\,mm represents a conservative threshold: displacement below this value is physically negligible in manipulation tasks where typical action magnitudes are 1--10\,mm per step. Even at $\tau_d = 1$\,$\mu$m, 73.9\% of A1-LoRA safe episodes are classified as frozen, while all Pi0.5 episodes remain above threshold at every level tested.
33	
34	Table~\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\tau_d \in [2, 200]$\,mm. At $\tau_d = 300$\,mm, 0--2 episodes per seed fall below threshold (displacement 200--300\,mm), causing $\leq$0.5\,pp deviation. Our conclusions hold across the entire tested range.
35	
36	\begin{table}[h]
37	\centering
38	\caption{dfCAR (\%) across displacement thresholds for fine-tuned Pi0.5 configurations ($n = 200$ episodes per seed). Values are identical across $\tau_d \in [2, 200]$\,mm; at $\tau_d = 300$\,mm, at most 2 episodes are excluded.}
39	\label{tab:dfcar_threshold}
40	\vspace{2pt}
41	\footnotesize
42	\begin{tabular}{lcccccccc}
43	\toprule
44	& \multicolumn{8}{c}{$\tau_d$ (mm)} \\
45	\cmidrule(lr){2-9}
46	Condition & 2 & 5 & 10 & 20 & 50 & 100 & 200 & 300 \\
47	\midrule
48	LoRA s0            & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\
49	LoRA s1            & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 \\
50	SDF $\lambda{=}0.005$ s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.1 \\
51	SDF $\lambda{=}0.005$ s1 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 \\
52	SDF $\lambda{=}0.005$ s2 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.3 \\
53	SDF $\lambda{=}0.01$ s0  & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\
54	SDF $\lambda{=}0.01$ s1  & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.1 \\
55	SDF $\lambda{=}0.01$ s2  & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.0 \\
56	\bottomrule
57	\end{tabular}
58	\end{table}
59	
60	
61	\section{Per-Task TSR Breakdown}\label{sec:appendix_tsr_pertask}
62	
63	Table~\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.
64	
65	\begin{table}[h]
66	\centering
67	\caption{Per-task TSR (\%) at 30K training steps. LoRA-only reports seed~0 (rotation-fixed re-evaluation); SDF conditions report 3-seed means.}
68	\label{tab:per_task_tsr}
69	\vspace{2pt}
70	\small
71	\begin{tabular}{lcccc}
72	\toprule
73	Task & Pi0.5 Base & LoRA-only\textsuperscript{$\dagger$} & SDF $\lambda{=}0.005$ & SDF $\lambda{=}0.01$ \\
74	 & (3 seeds) & (seed 0) & (3 seeds) & (3 seeds) \\
75	\midrule
76	Orange Juice      & 70.7 & 18.0 & 33.3 & 24.7 \\
77	Choco.\ Pudding   & 86.0 & 72.0 & 78.0 & 76.7 \\
78	Milk              & 66.0 & 32.0 & 35.3 & 48.7 \\
79	BBQ Sauce         & 76.0 & 62.0 & 69.3 & 65.3 \\
80	\midrule
81	Mean              & 74.7 & 46.0 & 54.0 & 53.8 \\
82	\bottomrule
83	\end{tabular}
84	\vspace{1pt}
85	{\footnotesize \textsuperscript{$\dagger$}Rotation-fixed re-evaluation; seed-1 evaluated with original rotation protocol, excluded to avoid mixing evaluation conditions.}
86	\end{table}
87	
88	\section{Safe Success Rate Analysis}\label{sec:appendix_ssr}
89	
90	Table~\ref{tab:ssr} reports the Safe Success Rate (SSR\,=\,TSR\,$\cap$\,CAR), the fraction of episodes achieving both task completion and collision avoidance. The SSR/TSR ratio quantifies the proportion of successful episodes that are also collision-free, controlling for task-completion rate.
91	
92	\begin{table}[h]
93	\centering
94	\caption{SSR and SSR/TSR ratio across conditions. The ratio increase from 0.33 (baseline) to 0.51--0.58 (fine-tuned) indicates that CAR gains reflect learned safer execution, not reduced task exposure.}
95	\label{tab:ssr}
96	\vspace{2pt}
97	\small
98	\begin{tabular}{lcccc}
99	\toprule
100	Condition & TSR (\%) & CAR (\%) & SSR (\%) & SSR/TSR \\
101	\midrule
102	Pi0.5 baseline & 74.7 & 26.8 & 25.0\textsuperscript{a} & 0.33 \\
103	LoRA-only (2 seeds) & 48.75 & 54.75 & 28.3 & 0.58 \\
104	SDF $\lambda{=}0.005$ (3 seeds) & 54.0 & 54.5 & 27.8 & 0.51 \\
105	SDF $\lambda{=}0.01$ (3 seeds) & 53.8 & 56.33 & 30.2 & 0.56 \\
106	SDF $\lambda{=}0.1$\textsuperscript{$\dagger$} & 48.0 & 58.25 & 26.5 & 0.55 \\
107	\bottomrule
108	\end{tabular}
109	\vspace{1pt}
110	{\footnotesize \textsuperscript{a}Estimated; per-episode overlap unavailable for 3-seed rotation-corrected protocol. \textsuperscript{$\dagger$}SSR from seed~1 only; seed~0 per-episode data overwritten.}
111	\end{table}
112	
113	\section{Per-Task Oracle Analysis}
114	\label{sec:appendix_pertask}
115	\label{sec:appendix_pertask_oracle}
116	
117	Table~\ref{tab:oracle_pertask} shows per-task CAR for oracle refinement. On task~1 (\texttt{chocolate\_pudding}), where the EE is the primary collision body and the LoRA baseline achieves only 46.0\% CAR, Oracle-adaptive improves to 55.0\% and Oracle-feature to 47.5\%. On the remaining tasks, all oracle variants degrade: Oracle-adaptive reduces task~0 (\texttt{orange\_juice}) from 96.0\% to 82.5\% and task~2 (\texttt{milk}) from 98.0\% to 77.5\%. The SDF gradient pushes the EE away from the nearest surface, but the resulting joint-space displacement rotates intermediate arm links into obstacle volumes.
118	
119	The feature-space oracle fires on nearly every timestep (241.7 refinements/episode vs.\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\ 0.18--0.49), and CAR (76.9\%) shows no advantage despite 17$\times$ more steps. The A3 learned SDF never triggers refinement (0 steps/episode), as its outputs avoid the activation threshold.
120	
121	\begin{table}[h]
122	\centering
123	\caption{Per-task CAR (\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another.}
124	\label{tab:oracle_pertask}
125	\vspace{2pt}
126	\small
127	\begin{tabular}{lccccc}
128	\toprule
129	Method & Task 0 & Task 1 & Task 2 & Task 3 & Agg. \\
130	\midrule
131	LoRA baseline & 96.0 & 46.0 & 98.0 & 88.0 & 82.0 \\
132	\midrule
133	Oracle-adaptive & 82.5 & 55.0 & 77.5 & 85.0 & 75.0 \\
134	Oracle-fixed & 85.0 & 50.0 & 77.5 & 80.0 & 73.1 \\
135	Oracle-feature & 90.0 & 47.5 & 82.5 & 87.5 & 76.9 \\
136	\bottomrule
137	\end{tabular}
138	\end{table}
139	
140	
141	\section{Null Distribution for SDF Loss Weight Analysis}
142	\label{sec:appendix_null}
143	
144	We construct a null distribution by pooling the two LoRA-only seeds and three $\lambda = 0.005$ seeds into five per-seed CAR measurements: 57.0\% (LoRA s0, re-evaluated), 52.5\% (LoRA s1), 57.0\% ($\lambda{=}0.005$ s0), 54.0\% ($\lambda{=}0.005$ s1), 52.5\% ($\lambda{=}0.005$ s2), yielding mean 54.6\% and standard deviation 2.27\%. We treat these as exchangeable because SDF at $\lambda = 0.005$ produces no separation from LoRA-only. The $\lambda = 0.01$ mean of 56.33\% falls within $0.8\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect. The $\lambda = 0.1$ 30K mean of 58.25\% (2 seeds) yields $z = 2.27$ ($p \approx 0.023$), a marginal departure whose interpretation is limited by $n = 2$.
145	
146	A Phase~2 ablation reinforces this conclusion. Setting $\lambda = 0$ during Phase~2 (steps 5K--30K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\% (single seed, s2). This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.
147	
148	\section{Step-wise Checkpoint Analysis for \texorpdfstring{$\lambda = 0.1$}{lambda = 0.1}}
149	\label{sec:appendix_stepwise}
150	
151	Table~\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\lambda = 0.1$. Seed-1 data is available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only. The seed-0 curve shows no monotonic trend through 28K; the 30K checkpoint marks the first consistent dual-seed departure from the null band, though whether this reflects a genuine late-training effect or sampling variance at $n = 2$ remains open.
152	
153	\begin{table}[h]
154	\centering
155	\caption{Per-seed CAR (\%) at training checkpoints for $\lambda = 0.1$ (200 episodes each). 24K--28K: seed-0 only. Dual-seed means remain within the null band (54.6\%\,$\pm$\,2.27\%) at all checkpoints except 30K, where both seeds depart marginally ($z = 2.27$, $p \approx 0.023$).}
156	\label{tab:stepwise_lambda01}
157	\vspace{2pt}
158	\small
159	\begin{tabular}{lccc}
160	\toprule
161	Checkpoint & Seed 0 & Seed 1 & Mean \\
162	\midrule
163	16K steps & 55.5 & 56.0 & 55.75 \\
164	20K steps & 55.0 & 56.0 & 55.5 \\
165	22K steps & 60.5 & 56.5 & 58.5 \\
166	24K steps & 52.5 & -- & -- \\
167	26K steps & 53.5 & -- & -- \\
168	28K steps & 54.5 & -- & -- \\
169	30K steps & 58.0 & 58.5 & 58.25 \\
170	\bottomrule
171	\end{tabular}
172	\end{table}
173	
174	Individual seeds exhibit checkpoint-to-checkpoint CAR fluctuations of up to 8\,pp (seed~0: 52.5--60.5\%), larger than the cross-seed standard deviation at any fixed checkpoint ($\leq$2.8\,pp). This is consistent with binomial sampling noise at $n = 50$ episodes per task ($\sigma \approx 7$\,pp per task for $p \approx 0.5$). The seed-averaged curve shows no monotonic trend, confirming that SDF loss weight does not produce a progressive training signal.
175	
176	
177	\section{Oracle SDF Refinement Details}
178	\label{sec:appendix_oracle}
179	
180	All oracle variants replace the learned SDF decoder with ground-truth distance fields computed from the simulation geometry. Each is evaluated for 160 episodes (4 tasks $\times$ 40).
181	
182	\paragraph{Oracle-adaptive.} At each timestep, if the ground-truth SDF at the end-effector position falls below a safety margin, the action is adjusted by a step in the negative SDF gradient direction. The step size $\alpha$ is scaled inversely with distance: smaller distances produce larger corrections. This mimics an adaptive potential field controller.
183	
184	\paragraph{Oracle-fixed.} Identical to Oracle-adaptive except the step size is fixed at $\alpha = 0.005$ regardless of distance. This isolates the effect of step-size adaptation from the refinement geometry.
185	
186	\paragraph{Oracle-feature.} Instead of modifying the action directly in Cartesian space, this variant applies the SDF gradient in the policy's latent feature space via backpropagation. The gradient of the ground-truth SDF value with respect to the intermediate features is computed and used to perturb the features before the action head decodes them. This tests whether geometric corrections are more effective when applied in the model's learned representation space. In practice, the feature-space variant fires on nearly every timestep (241.7 refinements per episode vs.\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\ 0.18--0.49 in action space).
187	
188	
189	\section{Training Details}
190	\label{sec:appendix_training}
191	
192	\paragraph{Architecture.}
193	We use LoRA~\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\alpha$=16) and the action expert (rank 32, $\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\to$ 256 $\to$ 3).
194	
195	\paragraph{Training schedule.}
196	Training proceeds in two phases:
197	\begin{itemize}
198	    \item \textbf{Phase 1} (steps 0--5000): Backbone and LoRA parameters are frozen. Only the SDF decoder and EE extractor are trained, allowing them to learn meaningful representations before the policy adapts.
199	    \item \textbf{Phase 2} (steps 5000--30000): LoRA parameters are unfrozen with a 100-step gradient warmup ramp. All auxiliary heads continue training jointly with the policy.
200	\end{itemize}
201	
202	\paragraph{Hyperparameters.}
203	\begin{table}[h]
204	\centering
205	\caption{Training hyperparameters.}
206	\label{tab:hyperparams}
207	\begin{tabular}{ll}
208	\toprule
209	Parameter & Value \\
210	\midrule
211	Base model & Pi0.5 (OpenPi, $\sim$3.5B parameters) \\
212	Optimizer & AdamW \\
213	Learning rate & $2.5 \times 10^{-5}$ (cosine decay to $\mathrm{lr}/10$) \\
214	Warmup steps & 1000 \\
215	Batch size & 32 \\
216	Total steps & 30000 \\
217	$\lambda_\mathrm{sdf}$ & \{0.005, 0.01, 0.1\} \\
218	$\lambda_\mathrm{ee}$ & 0.01 \\
219	SDF query points per step & 64 \\
220	SDF clamp $\delta$ & 0.05 m \\
221	Eikonal weight & 0.1 \\
222	LoRA rank (vision) & 16 \\
223	LoRA rank (action) & 32 \\
224	Phase 1 duration & 5000 steps \\
225	\bottomrule
226	\end{tabular}
227	\end{table}
228	
229	\paragraph{Evaluation protocol.}
230	Each episode runs for at most 300 timesteps. The policy generates a 50-step action trajectory via flow matching and executes the first 5 steps before replanning. An episode terminates early upon task completion. Collision detection uses MuJoCo's built-in contact detection: any contact between the robot and a non-target object registers as a collision. For Pi0.5 evaluations, camera images are rotated 180$^\circ$ to match the pre-training viewpoint convention; this correction was verified to restore TSR from ${\sim}$5\% to ${\sim}$52\% while leaving CAR comparable. Oracle variants use 40 episodes per task (160 total) with a single seed; all other configurations use 50 episodes per task (200 total).
231	
232	\paragraph{Data.}
233	We use the SafeLIBERO object\_pudding suite with pre-computed SDF ground truth. SDF values are computed offline from the obstacle mesh using a dense $64^3$ voxel grid. During training, 64 query points are randomly sampled per step from this grid.
234	
235	\paragraph{Computational resources.}
236	All training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.
237	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "3b352d5e-88a1-4dd0-8442-7c1f959be3c8"
}
```

</details>

---

### System

_source line 159_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading docs/paper/main.tex",
  "usage": {
    "total_tokens": 120470,
    "tool_uses": 47,
    "duration_ms": 88725
  },
  "last_tool_name": "Read",
  "uuid": "7a6a504d-47f3-49f9-934b-ff9cdb52551d",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 160_

<details open><summary>🔧 Tool call — Read · `toolu_018f1LxfzA9iBPJtxcZoma5A`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "7d31f686-2a2a-4c48-b335-6e1b60f5bc0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CKKj1EPqVPoyuj9keKxFFv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3317,
      "cache_read_input_tokens": 117051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3317,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 161 · 2026-05-27T13:14:08.340Z_

<details><summary>↩ Tool result · `toolu_018f1LxfzA9iBPJtxcZoma5A`</summary>

```text
1	\documentclass{article}
2	
3	\PassOptionsToPackage{dvipsnames}{xcolor}
4	\usepackage{corl_2026}
5	
6	\usepackage{amsmath,amssymb}
7	\usepackage{booktabs}
8	\usepackage{graphicx}
9	\usepackage{multirow}
10	\usepackage{subcaption}
11	\graphicspath{{../../artifacts/figures/}}
12	
13	\title{Rethinking VLA Safety Evaluation:\\When 98\% of Collision Avoidance is an Illusion}
14	
15	\author{
16	  Anonymous Authors
17	}
18	
19	\begin{document}
20	
21	\maketitle
22	
23	\input{abstract}
24	
25	\keywords{VLA safety, collision avoidance, action collapse, signed distance fields}
26	
27	\input{introduction}
28	
29	\input{related_work}
30	
31	\input{method}
32	
33	\input{claim1}
34	
35	\input{claim2}
36	
37	\input{claim3}
38	
39	\input{discussion}
40	
41	\bibliography{references}
42	
43	\appendix
44	\input{appendix}
45	
46	\end{document}
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "cae45265-7d19-4509-92ff-c263c6a260a7"
}
```

</details>

---

### System

_source line 162_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading docs/paper/abstract.tex",
  "usage": {
    "total_tokens": 129059,
    "tool_uses": 48,
    "duration_ms": 94443
  },
  "last_tool_name": "Read",
  "uuid": "4f7cf529-10a8-47a4-941f-080a73875a1e",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 163_

<details open><summary>🔧 Tool call — Read · `toolu_017CkNsWTmsqL8fq1c3wjP6W`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "4d09ac09-ca8d-4c33-987b-b7957e061ec1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPsyuaMpVRykb65eGf8bjK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8587,
      "cache_read_input_tokens": 120368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8587,
        "ephemeral_1h_input_tokens": 0
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

_source line 164 · 2026-05-27T13:14:14.056Z_

<details><summary>↩ Tool result · `toolu_017CkNsWTmsqL8fq1c3wjP6W`</summary>

```text
1	\begin{abstract}
2	Vision-Language-Action (VLA) models report high Collision Avoidance Rates (CAR) on safety benchmarks, yet we show these metrics are contaminated by action collapse.
3	On SafeLIBERO, an SDF-augmented Pi0 achieves 91.5\% CAR while 99.6\% of its safe episodes exhibit end-effector displacement below 0.1\,mm---the robot is frozen, not safe.
4	We present displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes, as a corrective metric; the bimodal displacement distribution makes it robust across a $[2, 200]$\,mm threshold range.
5	Our analysis further reveals that end-effector-only Signed Distance Field (SDF) supervision is neither necessary nor structurally sufficient for collision avoidance.
6	It is counterproductive at inference time: three ground-truth oracle variants all reduce dfCAR below unrefined baselines, as SDF gradients repelling the end-effector drive arm links into obstacles.
7	Its contribution during training is dose-dependent: LoRA-only fine-tuning raises dfCAR from 26.8\% to 54.75\%$\,\pm\,$3.18, matching SDF-augmented training at $\lambda{=}0.005$ (54.5\%$\,\pm\,$2.29) and $\lambda{=}0.01$ (56.33\%$\,\pm\,$1.61); at $\lambda{=}0.1$, two of three seeds show a marginal signal (58.25\%$\,\pm\,$0.35, $p{\approx}0.023$) whose per-task avoidance pattern still mirrors the demonstration distribution, requiring further investigation.
8	Per-task avoidance patterns remain identical across all conditions, indicating that collision avoidance arises from collision-free demonstration data rather than geometric supervision.
9	Displacement filtering is necessary for meaningful VLA safety evaluation; EE-only geometric supervision can be neither credited with nor expected to deliver collision avoidance.
10	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "2db271e6-d750-438e-a3b6-9eb8e27f0e41"
}
```

</details>

---

### System

_source line 165_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading docs/paper/introduction.tex",
  "usage": {
    "total_tokens": 129060,
    "tool_uses": 49,
    "duration_ms": 94948
  },
  "last_tool_name": "Read",
  "uuid": "e218b8d8-d8d4-465d-934f-040c3bf01fa7",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 166_

<details open><summary>🔧 Tool call — Read · `toolu_01CbifdrErERJe4QQmACDDNH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "611f2af2-97e8-46e2-aefa-058f50f8fce3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPsyuaMpVRykb65eGf8bjK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8587,
      "cache_read_input_tokens": 120368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8587,
        "ephemeral_1h_input_tokens": 0
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

_source line 167 · 2026-05-27T13:14:14.554Z_

<details><summary>↩ Tool result · `toolu_01CbifdrErERJe4QQmACDDNH`</summary>

```text
1	\section{Introduction}\label{sec:intro}
2	
3	Vision-Language-Action (VLA) models must avoid collisions to operate safely in physical environments~\cite{li2026vlasafety}. The SafeLIBERO benchmark~\cite{hu2025vlsa} provides the first systematic protocol for measuring collision avoidance in VLA manipulation, and recent methods, including SDF-augmented training~\cite{zhang2025safevla}, constraint-based planning~\cite{yang2025cape}, and collision-free demonstrations~\cite{cofreeevla2026}, report high Collision Avoidance Rate (CAR). Our SDF-augmented Pi0~\cite{black2024pi0} reaches 91.5\% CAR across 800 episodes. The problem appears close to solved.
4	
5	\begin{figure}[t]
6	\centering
7	\includegraphics[width=\linewidth]{fig1_teaser}
8	\caption{The fake safety problem in VLA collision avoidance evaluation. Standard CAR classifies a frozen robot as safe because it produces zero collisions (left). dfCAR filters out action-collapsed episodes where displacement falls below $\tau_d$, revealing that Pi0+A1's 91.5\% safety score drops to ${\approx}$\,0\% (center). Pi0.5 exhibits genuine avoidance with active motion above 288\,mm in all safe episodes, and dfCAR equals raw CAR (right).}
9	\label{fig:teaser}
10	\end{figure}
11	
12	It is not (Figure~\ref{fig:teaser}). Of the 732 collision-free episodes, 99.6\% exhibit displacement below 0.1\,mm; TSR is 0\% across all 800 episodes. The robot is frozen, not safe. The same pattern holds across all Pi0 configurations (Section~\ref{sec:fake_safety}). We term this \emph{fake safety}: \emph{action collapse} (near-zero actions producing zero collisions) renders reported CAR illusory, and standard evaluation cannot distinguish inaction from deliberate avoidance~\cite{karwowski2024goodhart}.
13	
14	We present a systematic investigation of this problem across the Pi0 and Pi0.5~\cite{black2024pi0} model families on SafeLIBERO, spanning 100+ experiments and 6000+ evaluation episodes. Three findings emerge.
15	
16	\textbf{Fake safety is pervasive.} We introduce displacement-filtered CAR (dfCAR), which excludes episodes below a displacement threshold $\tau_d$. dfCAR collapses Pi0+A1 from 91.5\% to ${\approx}$\,0\% (3/732 safe episodes survive). The bimodal displacement distribution makes $\tau_d$ robust across five orders of magnitude. Pi0.5 validates the metric: TSR\,=\,74.7\%, CAR\,=\,26.8\%, with every safe episode above 288\,mm displacement and dfCAR equal to raw CAR (Section~\ref{sec:fake_safety}).
17	
18	\textbf{EE-only SDF refinement is structurally counterproductive.} Three ground-truth oracle variants all achieve \emph{lower} CAR than unrefined baselines (73.1--76.9\% vs.\ 82--83\%). The SDF gradient repels the EE but rotates arm links into obstacle volumes (Section~\ref{sec:ee_only}).
19	
20	\textbf{Collision-free demonstrations are sufficient for collision avoidance.} LoRA fine-tuning on Pi0.5 raises CAR by ${\sim}$28 points (26.8\% $\to$ 54.75\%) with zero frozen episodes; adding SDF supervision at low loss weights ($\lambda \in \{0.005, 0.01\}$) produces no measurable benefit and at high $\lambda = 0.1$ yields only a marginal, inconclusive signal ($p \approx 0.023$, $n = 2$); the per-task avoidance pattern is identical with and without geometric supervision, indicating that the collision-free demonstration distribution, not EE-only SDF supervision, accounts for all observed avoidance learning on this benchmark (Section~\ref{sec:avoidance_source}).
21	
22	Our contributions are:
23	\begin{itemize}
24	    \item \textbf{dfCAR metric:} displacement-filtered CAR that separates genuine avoidance from action collapse, robust across $\tau_d \in [2, 200]$\,mm.
25	    \item \textbf{Fake safety diagnosis:} 100+ experiments across Pi0/Pi0.5 showing $>$99\% of Pi0 safe episodes are action-collapse artifacts.
26	    \item \textbf{EE-only SDF is counterproductive:} ground-truth oracle refinement \emph{reduces} CAR below unrefined baselines by redistributing collisions to unmonitored arm links.
27	    \item \textbf{Demonstration sufficiency:} on SafeLIBERO, collision-free demonstrations account for all measured CAR gains (${\sim}$28\,pp); EE-only SDF at low $\lambda$ ($\leq 0.01$) adds nothing, and at high $\lambda = 0.1$ shows only a marginal, inconclusive signal ($n = 2$) whose per-task pattern still matches the demonstration distribution.
28	\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "e639b756-c881-4342-933c-aeeeda1599ad"
}
```

</details>

---

### System

_source line 168_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading docs/paper/claim1.tex",
  "usage": {
    "total_tokens": 129061,
    "tool_uses": 50,
    "duration_ms": 95424
  },
  "last_tool_name": "Read",
  "uuid": "27ba7348-9b0f-4b9a-9cb2-ca8381baae81",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 169_

<details open><summary>🔧 Tool call — Read · `toolu_01Vyc2PTVLEByrorSztQ6YWr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "9fb1aace-2ca0-4b62-9e26-56e9a5d2fe3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPsyuaMpVRykb65eGf8bjK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8587,
      "cache_read_input_tokens": 120368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8587,
        "ephemeral_1h_input_tokens": 0
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

_source line 170 · 2026-05-27T13:14:15.030Z_

<details><summary>↩ Tool result · `toolu_01Vyc2PTVLEByrorSztQ6YWr`</summary>

```text
1	\section{The Fake Safety Problem}\label{sec:fake_safety}
2	
3	Standard CAR assumes that collision-free episodes reflect deliberate avoidance. This assumption is systematically violated: in every Pi0 configuration tested, over 99\% of collision-free episodes are action-collapse artifacts (Table~\ref{tab:fake_safety}).\footnote{Pi0-family values report obstacle displacement from the original protocol; Pi0.5 reports EE displacement from the rotation-corrected protocol (\S\ref{sec:dfcar}). Sub-millimeter displacement indicates action collapse in both cases.} Applying dfCAR collapses all three to ${\approx}$\,0\%. Pi0+A1 achieves the \emph{highest} raw CAR (91.5\%) because more complete action collapse (from a parameter-name mismatch preventing LoRA loading; Table~\ref{tab:configurations}) yields higher fake safety. Pi0.5 validates the metric from the opposite direction: every safe episode exceeds 200\,mm displacement, yielding dfCAR equal to raw CAR (26.8\%\,$\pm$\,1.6). The displacement distribution is sharply bimodal (Appendix~\ref{sec:appendix_displacement}), with a five-order-of-magnitude gap that makes $\tau_d$ robust.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Fake safety decomposition on SafeLIBERO. dfCAR excludes episodes with displacement $< \tau_d = 0.1$\,mm.}
8	\label{tab:fake_safety}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	Method & Ep. & CAR (\%) & TSR (\%) & Fake Safe (\%) & dfCAR (\%) \\
14	\midrule
15	Pi0 Full-FT  & 200 & 83.0 & 0.5 & 99.4 & $\approx$\,0 \\
16	Pi0 LoRA     & 200 & 82.0 & 0.0 & ${\sim}$99 & $\approx$\,0 \\
17	Pi0+A1 (SDF) & 800 & 91.5 & 0.0 & 99.6 & $\approx$\,0$^*$ \\
18	\midrule
19	Pi0.5 (3-seed)  & 600 & 26.8\,$\pm$\,1.6 & 74.7\,$\pm$\,1.5 & 0.0 & 26.8 \\
20	\bottomrule
21	\end{tabular}
22	\vspace{1pt}
23	{\footnotesize $^*$\,3/732 safe episodes above threshold; denominator too small for reliable rate.}
24	\end{table}
25	
26	Figure~\ref{fig:tsr_car_scatter} reveals spatial structure in the TSR-CAR plane.\label{sec:anticorrelation} Pi0-family models cluster in the upper-left (high CAR, near-zero TSR), Pi0.5 in the lower-right (high TSR, low CAR). The upper-right quadrant (high TSR \emph{and} CAR) represents genuinely safe behavior; the upper-left is accessible through action collapse alone. Under dfCAR, Pi0 configurations drop to the origin, revealing that the apparent safety-capability tradeoff was an artifact of action-collapse contamination.
27	
28	\begin{figure}[t]
29	\centering
30	\includegraphics[width=0.85\linewidth]{fig_tsr_car_scatter.pdf}
31	\caption{TSR vs.\ CAR for all configurations. Pi0-family models cluster in the upper-left (high CAR from inaction), Pi0.5 in the lower-right (high TSR with collision exposure), fine-tuned Pi0.5 in the center. The upper-right quadrant (high TSR and CAR) represents genuinely safe behavior. Error bars: $\pm$1 std across seeds.}
32	\label{fig:tsr_car_scatter}
33	\end{figure}
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "df49da23-8693-45c1-9031-a976bed13fa8"
}
```

</details>

---

### System

_source line 171_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading docs/paper/claim2.tex",
  "usage": {
    "total_tokens": 129062,
    "tool_uses": 51,
    "duration_ms": 95955
  },
  "last_tool_name": "Read",
  "uuid": "0c59ebfd-12ba-4a42-8541-21d13d4340a1",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 172_

<details open><summary>🔧 Tool call — Read · `toolu_012JKBQ5pQd9QLn4YajdXvsM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "96f04a7b-5f1f-458a-b22f-6f9187cfd6f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPsyuaMpVRykb65eGf8bjK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8587,
      "cache_read_input_tokens": 120368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8587,
        "ephemeral_1h_input_tokens": 0
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

_source line 173 · 2026-05-27T13:14:15.561Z_

<details><summary>↩ Tool result · `toolu_012JKBQ5pQd9QLn4YajdXvsM`</summary>

```text
1	\section{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\label{sec:ee_only}
2	
3	Could a perfect SDF signal enable effective EE-only refinement? We replace the learned SDF with ground-truth distance fields from the simulation geometry (\S\ref{sec:oracle_setup}). Table~\ref{tab:oracle} and Figure~\ref{fig:oracle_bar} show that all three oracle variants achieve \emph{lower} CAR than unrefined baselines: the best oracle (76.9\%) falls 5.1 points below LoRA (82.0\%). Refinement with perfect distance information produces more collisions, not fewer.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Oracle SDF refinement with ground-truth distance fields. All oracle variants achieve lower CAR than unrefined baselines. Per-task breakdown in Appendix~\ref{sec:appendix_pertask_oracle}.}
8	\label{tab:oracle}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lccc}
12	\toprule
13	Method & CAR (\%) & Fake Safe (\%) & Refines/ep \\
14	\midrule
15	LoRA baseline (no refine) & 82.0 & 99.4 & -- \\
16	Full-FT baseline (no refine) & 83.0 & -- & -- \\
17	\midrule
18	Oracle-adaptive (GT, dyn.\ $\alpha$) & 75.0 & 98.3 & 14.2 \\
19	Oracle-fixed (GT, $\alpha{=}0.005$) & 73.1 & 98.3 & 14.8 \\
20	Oracle-feature (GT, feat.\ space) & 76.9 & 96.7 & 241.7 \\
21	\midrule
22	A3 learned SDF & 77.1 & -- & 0.0 \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	\begin{figure}[t]
28	\centering
29	\includegraphics[width=0.85\linewidth]{fig_oracle_bar.pdf}
30	\caption{CAR for oracle SDF refinement versus unrefined baselines. All GT oracle variants underperform baselines despite perfect distance information.}
31	\label{fig:oracle_bar}
32	\end{figure}
33	
34	Per-task analysis reveals the mechanism (Appendix~\ref{sec:appendix_pertask_oracle}). On the one task where the EE is the primary collision body, oracle refinement helps (+9 points). On the remaining three, the SDF gradient pushes the EE away from obstacles but rotates intermediate arm links into obstacle volumes, trading one collision for another. The A3 learned SDF never triggers refinement (0 steps per episode). EE-only refinement is structurally counterproductive: joint-space coupling between EE displacement and arm-link rotation redistributes collisions to unmonitored links regardless of signal quality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "177326c8-79f6-4dab-83ee-2003995f38af"
}
```

</details>

---

### System

_source line 174_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading docs/paper/discussion.tex",
  "usage": {
    "total_tokens": 129063,
    "tool_uses": 52,
    "duration_ms": 96188
  },
  "last_tool_name": "Read",
  "uuid": "fae79e2d-d32f-4e88-ba51-a61ac0b9f539",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 175_

<details open><summary>🔧 Tool call — Read · `toolu_019CmNVU2zvg49nZEnkgaPb8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "6aa7127f-cc61-4e73-931f-dc336fbc9ddd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPsyuaMpVRykb65eGf8bjK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8587,
      "cache_read_input_tokens": 120368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8587,
        "ephemeral_1h_input_tokens": 0
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

_source line 176 · 2026-05-27T13:14:15.803Z_

<details><summary>↩ Tool result · `toolu_019CmNVU2zvg49nZEnkgaPb8`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	Across 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\S\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\S\ref{sec:ee_only}); and collision-free demonstrations, not geometric supervision, account for all measured avoidance gains (\S\ref{sec:avoidance_source}).
4	
5	\paragraph{Why EE-only SDF fails.}
6	Two independent causes explain the null result. \textit{(i)~Demonstration data subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\sim}$28\,pp CAR gain arises entirely from this distributional shift, with per-task ordering invariant across all SDF conditions (\S\ref{sec:avoidance_source}). At low $\lambda$, SDF is redundant; at $\lambda = 0.1$, the marginal signal preserves the same demonstration-driven pattern. \textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \emph{reduces} CAR by 6--10\,pp below unrefined baselines (\S\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. These levels are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.
7	
8	\paragraph{Implications for evaluation.}
9	dfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\times$ parameter range (Pi0 Full-FT ${\sim}$2.5B to Pi0+A1 ${\sim}$658K trainable), confirming it is a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot.
10	
11	\paragraph{Limitations.}
12	Our evaluation covers one benchmark suite (SafeLIBERO, four tasks) and two model families (Pi0, Pi0.5). The tabletop setting with fixed-base manipulator and known obstacles may not generalize to mobile platforms and cluttered scenes. Oracle experiments used a largely frozen model (Pi0+A1, TSR${\approx}$0\%); testing on an actively moving policy would better isolate the structural limitation. The $\lambda = 0.1$ condition has $n = 2$ seeds; the marginal departure ($p \approx 0.023$) is inconclusive. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\sim}$21--26\,pp, yet SSR/TSR increases from 0.33 to 0.51--0.58 (Appendix~\ref{sec:appendix_ssr}), ruling out reduced exposure as the sole explanation.
13	
14	\paragraph{Future work.}
15	Three directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space rather than EE space.
16	
17	\paragraph{Broader impact.}
18	Contaminated CAR scores allow models with no genuine avoidance to pass safety benchmarks. dfCAR exposes this gap with minimal changes to existing protocols.
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "0517c66e-d777-4fdd-979e-7a14960840ca"
}
```

</details>

---

### System

_source line 177_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading docs/paper/experimental_framework.tex",
  "usage": {
    "total_tokens": 134381,
    "tool_uses": 53,
    "duration_ms": 101837
  },
  "last_tool_name": "Read",
  "uuid": "fc3d53cb-88f3-46a7-b4f4-aa3d78d364e0",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 178_

<details open><summary>🔧 Tool call — Read · `toolu_01VritKRtdDvNr1JA6xukTG2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/experimental_framework.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "3bba5188-4712-4c2f-af14-f14f0dc9889c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AmvKdLNsv8wE9QE3DuRPeM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5316,
      "cache_read_input_tokens": 128955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5316,
        "ephemeral_1h_input_tokens": 0
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

_source line 179 · 2026-05-27T13:14:21.444Z_

<details><summary>↩ Tool result · `toolu_01VritKRtdDvNr1JA6xukTG2`</summary>

```text
1	\section{Experimental Framework}\label{sec:framework}
2	
3	This section defines the evaluation platform, metrics, and model configurations that underpin the analyses in Sections~\ref{sec:fake_safety}--\ref{sec:avoidance_source}. Our primary methodological contribution is the displacement-filtered Collision Avoidance Rate (dfCAR), which separates genuine avoidance from action collapse.
4	
5	\subsection{Benchmark and Evaluation Protocol}
6	
7	We conduct all experiments on SafeLIBERO~\cite{hu2025vlsa}, a collision-aware evaluation extension of the LIBERO simulation platform~\cite{liu2023libero}. SafeLIBERO augments standard manipulation benchmarks with per-timestep collision detection and non-target obstacle annotations, enabling systematic measurement of both task completion and safety.
8	
9	We select the \textit{object\_pudding} Level~I suite, which comprises four tabletop manipulation tasks. In each task, a target object is surrounded by non-target obstacles that the robot must avoid during grasping and transport. The MuJoCo physics engine provides collision detection: any contact between the robot (end-effector or arm links) and a non-target object registers as a collision event.
10	
11	Each method is evaluated for 50 episodes per task (200 episodes total). For multi-seed experiments (Pi0.5), we run 3 seeds to produce 600 episodes per configuration. Initial object configurations are fixed across methods to ensure fair comparison.
12	
13	\subsection{Evaluation Metrics}\label{sec:metrics}
14	
15	\paragraph{Standard metrics.} We report two conventional metrics. The \emph{Task Success Rate} (TSR) is the fraction of episodes where the manipulation task reaches completion. The \emph{Collision Avoidance Rate} (CAR) is the fraction of episodes in which no collision occurs between the robot and any non-target object.
16	
17	\paragraph{Displacement-filtered CAR.} Standard CAR conflates two qualitatively distinct behaviors: a robot that plans a trajectory around obstacles, and a robot that has collapsed into inaction. Both register as ``safe,'' yet only the former reflects collision avoidance capability. We propose the displacement-filtered CAR (dfCAR), which excludes episodes exhibiting action collapse from both numerator and denominator.
18	
19	We define an episode $e$ as \emph{action-collapsed} when its maximum end-effector displacement satisfies $d_{\max}(e) < \tau_d$, where $\tau_d = 0.1$\,mm. The filtered metric is then:
20	\begin{equation}\label{eq:car_f}
21	\text{dfCAR} = \frac{|\{e : \text{safe}(e) \;\land\; d_{\max}(e) \geq \tau_d\}|}{|\{e : d_{\max}(e) \geq \tau_d\}|}
22	\end{equation}
23	where $d_{\max}(e)$ denotes the maximum Euclidean displacement of the end-effector across all timesteps in episode $e$. The threshold $\tau_d = 0.1$\,mm corresponds to sub-actuator-resolution motion. In practice, the displacement distribution is bimodal: collapsed episodes cluster below 1\,$\mu$m and active episodes exceed 200\,mm, with no intermediate population. Consequently, any $\tau_d \in [2, 200]$\,mm produces identical filtering (Appendix~\ref{sec:appendix_threshold}).
24	
25	\paragraph{Auxiliary metrics.} We additionally report the \emph{Frozen Rate}, the fraction of episodes with $d_{\max} < \tau_d$, which quantifies the severity of action collapse for each method. The \emph{Simultaneous Success Rate} (SSR $= $ TSR $\cap$ CAR) measures the fraction of episodes that achieve both task completion and collision avoidance.
26	
27	\subsection{Models and Training}
28	
29	\paragraph{Base architectures.} We evaluate two VLA models from the Pi0 family~\cite{black2024pi0}. \textbf{Pi0} (${\sim}$3B parameters) uses a PaliGemma vision-language encoder paired with a dedicated action expert that generates continuous actions via flow matching~\cite{lipman2023flow}. \textbf{Pi0.5} extends this architecture to ${\sim}$3.5B parameters with broader pre-training data, and serves as a stronger baseline that exhibits less action collapse.
30	
31	\paragraph{Training configurations.} We evaluate four model variants:
32	\begin{itemize}
33	\item \textit{Full-FT baseline}: Pi0 with all parameters fine-tuned on SafeLIBERO demonstrations using the flow-matching action loss.
34	\item \textit{LoRA baseline}: Pi0 with LoRA adapters (${\sim}$33.5M trainable parameters), same demonstrations and loss.
35	\item \textit{A1-LoRA}: Pi0 + LoRA augmented with two auxiliary heads. An SDF Decoder (4-layer MLP, ${\sim}$395K parameters) predicts the signed distance from the end-effector to the nearest obstacle surface, supervised with a clamped $L_1$ loss and an Eikonal regularizer ($\mathcal{L}_\text{SDF}$). An EE Extractor (2-layer MLP, ${\sim}$263K parameters) predicts end-effector position from action expert features ($\mathcal{L}_\text{EE}$, MSE loss). SDF ground truth is computed from known obstacle meshes in simulation.
36	\item \textit{Pi0.5 + A1}: The A1 architecture applied to the Pi0.5 backbone. Training proceeds in two phases: Phase~1 (steps 0--5K) trains only the auxiliary heads on detached features with the backbone frozen; Phase~2 (steps 5K--30K) unfreezes LoRA parameters for joint optimization. We evaluate $\lambda_\text{SDF} \in \{0.005, 0.01\}$.
37	\end{itemize}
38	
39	\subsection{Oracle SDF Refinement}
40	
41	To test the theoretical upper bound of end-effector-only SDF refinement (analyzed in Section~\ref{sec:ee_only}), we replace the learned SDF network with the ground-truth signed distance field computed from simulation geometry. This eliminates prediction error and isolates the structural limitation of the refinement paradigm itself.
42	
43	We evaluate three oracle variants that differ in how the SDF gradient is applied:
44	\begin{itemize}
45	\item \textit{Oracle-adaptive}: runtime gradient refinement with a dynamic step size $\alpha$ that scales inversely with gradient magnitude.
46	\item \textit{Oracle-fixed}: a constant step size $\alpha = 0.005$.
47	\item \textit{Oracle-feature}: gradient applied in the VLA's latent feature space rather than Cartesian action space.
48	\end{itemize}
49	Each variant is evaluated for 160 episodes (4 tasks $\times$ 40 episodes) with a single seed.
50	
51	\subsection{SDF Ground Truth}
52	
53	The workspace signed distance field is computed from the known obstacle meshes available in the LIBERO/MuJoCo simulation environment. SDF values are positive in free space, zero on the obstacle surface, and negative inside the obstacle volume. Ground-truth labels are generated at query points sampled along predicted end-effector trajectories during training.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "2650d723-c135-4d06-b82a-ca6a367a4c40"
}
```

</details>

---

### System

_source line 180_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading docs/paper/method.tex",
  "usage": {
    "total_tokens": 134382,
    "tool_uses": 54,
    "duration_ms": 102294
  },
  "last_tool_name": "Read",
  "uuid": "c3bee422-c821-4776-b273-5c61d14f50c9",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 181_

<details open><summary>🔧 Tool call — Read · `toolu_01WpLVnN2426gSZf1x5y3ZRJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "9562c9cf-6a36-4275-a1d9-5ab8c63dffd4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AmvKdLNsv8wE9QE3DuRPeM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5316,
      "cache_read_input_tokens": 128955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5316,
        "ephemeral_1h_input_tokens": 0
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

_source line 182 · 2026-05-27T13:14:21.900Z_

<details><summary>↩ Tool result · `toolu_01WpLVnN2426gSZf1x5y3ZRJ`</summary>

```text
1	\section{Experimental Setup and Metrics}\label{sec:method}
2	
3	\subsection{Benchmark and Models}\label{sec:benchmark}
4	
5	We evaluate on SafeLIBERO~\cite{hu2025vlsa}, the \textit{object\_pudding} suite (Level~I): four tabletop pick-and-place tasks with collision hazards, using per-timestep collision detection. Two VLA families are tested: \textbf{Pi0} (${\sim}$2.5B)~\cite{black2024pi0} with flow matching~\cite{lipman2023flow}, and \textbf{Pi0.5} with broader pre-training. Table~\ref{tab:configurations} lists all configurations. Each uses 50 episodes per task (200 total); Pi0.5 multi-seed runs use 3 seeds (600 episodes). We report Collision Avoidance Rate (CAR), the fraction of collision-free episodes, and Task Success Rate (TSR), the fraction achieving task completion~\cite{hu2025vlsa,zhang2025safevla}.
6	
7	\begin{table}[t]
8	\centering
9	\caption{Training configurations. Trainable parameters exclude the frozen backbone.}
10	\label{tab:configurations}
11	\vspace{2pt}
12	\small
13	\begin{tabular}{llr}
14	\toprule
15	Configuration & Description & Trainable Params \\
16	\midrule
17	Pi0 Full-FT & Full fine-tune, flow-matching loss & ${\sim}$2.5B \\
18	Pi0 LoRA & LoRA adapters only & ${\sim}$33.5M \\
19	Pi0+A1 (SDF aux)\textsuperscript{$\dagger$} & LoRA + SDF decoder + EE extractor & ${\sim}$658K \\
20	Pi0+A3 (learned SDF) & LoRA + SDF decoder w/ gradient refinement & ${\sim}$34.2M \\
21	Pi0.5 (pre-trained) & No fine-tuning & 0 \\
22	Pi0.5 LoRA & LoRA fine-tune on Pi0.5 & ${\sim}$33.5M \\
23	Pi0.5+A1 (SDF aux) & LoRA + SDF aux on Pi0.5, $\lambda \in \{0.005, 0.01, 0.1\}$ & ${\sim}$34.2M \\
24	\bottomrule
25	\end{tabular}
26	\vspace{2pt}
27	\raggedright\footnotesize\textsuperscript{$\dagger$}LoRA weights not loaded due to parameter-name mismatch; only auxiliary heads trained.
28	\end{table}
29	
30	\subsection{Displacement-Filtered CAR}\label{sec:dfcar}
31	
32	Standard CAR conflates genuine avoidance with action collapse. We define an episode as \emph{action-collapsed} when $d_{\max}(e) < \tau_d$ ($\tau_d = 0.1$\,mm) and exclude such episodes:
33	\begin{equation}\label{eq:car_f}
34	\text{dfCAR} = \frac{|\{e : \text{safe}(e) \;\land\; d_{\max}(e) \geq \tau_d\}|}{|\{e : d_{\max}(e) \geq \tau_d\}|}
35	\end{equation}
36	The displacement distribution is sharply bimodal, with collapsed episodes below 1\,$\mu$m and active episodes above 200\,mm; any $\tau_d \in [2, 200]$\,mm yields identical results (Appendix~\ref{sec:appendix_threshold}).\footnote{See Section~\ref{sec:fake_safety} for details on the displacement measurement protocol.}
37	
38	\subsection{SDF Auxiliary Training and Oracle Refinement}\label{sec:sdf_aux}
39	
40	We augment LoRA-adapted~\cite{hu2022lora} VLAs with an SDF decoder and an EE position extractor (Appendix~\ref{sec:appendix_training}, Table~\ref{tab:hyperparams}). The total loss is:
41	\begin{equation}\label{eq:total_loss}
42	\mathcal{L}_\text{total} = \mathcal{L}_\text{action} + \lambda \left( \mathcal{L}_\text{SDF} + \mathcal{L}_\text{EE} \right)
43	\end{equation}
44	where $\lambda \in \{0.005, 0.01, 0.1\}$. In Pi0+A1, a parameter-name mismatch prevented LoRA loading, causing action collapse (TSR\,=\,0\%; Table~\ref{tab:configurations}). To test the upper bound of EE-only refinement (Section~\ref{sec:ee_only}), we also replace the learned SDF with ground-truth distance fields from the simulation geometry in three oracle variants (Appendix~\ref{sec:appendix_oracle}).\label{sec:oracle_setup}
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "a659b435-2f97-4fc8-a796-c1f7a20fd3c2"
}
```

</details>

---

### System

_source line 183_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading docs/paper/contingency_claim3.tex",
  "usage": {
    "total_tokens": 134383,
    "tool_uses": 55,
    "duration_ms": 102644
  },
  "last_tool_name": "Read",
  "uuid": "3ded4434-4e0f-4288-b6d5-d4e6031393ed",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 184_

<details open><summary>🔧 Tool call — Read · `toolu_017uHmPc3WWqdZbjYBFBzBWH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/contingency_claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "2465f070-ada5-410e-8786-9644a32aa08e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AmvKdLNsv8wE9QE3DuRPeM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5316,
      "cache_read_input_tokens": 128955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5316,
        "ephemeral_1h_input_tokens": 0
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

_source line 185 · 2026-05-27T13:14:22.250Z_

<details><summary>↩ Tool result · `toolu_017uHmPc3WWqdZbjYBFBzBWH`</summary>

```text
1	% contingency_claim3.tex — Three pre-written §6.3 paragraphs for λ=0.1 results.
2	% NOT \input'd into main.tex. Copy the matching scenario into claim3.tex
3	% when results arrive. Replace {MEAN}, {S0}, {S1} with actual numbers.
4	%
5	% Scenario selection (D033 thresholds):
6	%   B: CAR mean ≤ 57%    → full redundancy confirmed
7	%   C: CAR mean 57–60%   → inconclusive, flag 2/3 seeds
8	%   A: CAR mean > 60%    → dose-response evidence
9	%
10	% Also includes discussion + abstract patch bullets at the end.
11	
12	
13	%% ====================================================================
14	%% SCENARIO B — Full redundancy (CAR ≤ 57%)
15	%% ====================================================================
16	
17	% --- claim3 §6.3 paragraph ---
18	\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
19	Increasing $\lambda$ by 20$\times$ to 0.1 yields CAR\,=\,{MEAN}\% (seeds: {S0}\%, {S1}\%), within the null distribution (mean 54.5\%, $\sigma = 2.15$). SDF supervision is redundant with the demonstration signal across the full tested range $\lambda \in [0.005, 0.1]$ (Figure~\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\ref{sec:conclusion}): because even a 20$\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude (Level~A) but the structural mismatch between end-effector monitoring and full-body collision surfaces (Level~B). Stronger geometric supervision cannot compensate for supervising the wrong collision surface.
20	
21	
22	%% ====================================================================
23	%% SCENARIO C — Inconclusive / gray zone (CAR 57–60%)
24	%% ====================================================================
25	
26	% --- claim3 §6.3 paragraph ---
27	\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
28	At $\lambda = 0.1$, CAR\,=\,{MEAN}\% (seeds: {S0}\%, {S1}\%), representing a suggestive but inconclusive separation from the null distribution (mean 54.5\%, $\sigma = 2.15$; Figure~\ref{fig:lambda_car}). The observed increase of {MEAN}$-$54.5\,=\,{DELTA}\,pp falls in a range where seed-to-seed variation and a genuine treatment effect are difficult to distinguish with two seeds. A third seed was in progress at submission; updated results will be provided upon completion. If the separation holds, it would indicate a dose-response threshold between $\lambda = 0.01$ and $\lambda = 0.1$, suggesting that Level~A signal masking (Section~\ref{sec:conclusion}) can be partially overcome at higher loss weights while the Level~B structural limitation of EE-only monitoring remains.
29	
30	
31	%% ====================================================================
32	%% SCENARIO A — Dose-response evidence (CAR > 60%)
33	%% ====================================================================
34	
35	% --- claim3 §6.3 paragraph ---
36	\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
37	Increasing $\lambda$ to 0.1 raises CAR to {MEAN}\% (seeds: {S0}\%, {S1}\%), a {DELTA}\,pp increase beyond the null distribution mean of 54.5\% (Figure~\ref{fig:lambda_car}). This provides preliminary evidence for a dose-response relationship: SDF supervision becomes effective only when $\lambda$ exceeds a threshold between 0.01 and 0.1, below which the geometric gradient is masked by the action loss. In the two-level failure framework (Section~\ref{sec:conclusion}), this result indicates that Level~A signal masking has a breakpoint, while Level~B structural misalignment persists: oracle experiments with perfect SDF still reduce CAR below unrefined baselines regardless of signal strength, confirming that EE-only monitoring remains the binding constraint for full-body safety. Two of three planned seeds are reported; the third was in progress at submission, and updated results will be provided upon completion.
38	
39	
40	%% ====================================================================
41	%% DISCUSSION + ABSTRACT PATCH BULLETS (per scenario)
42	%% ====================================================================
43	
44	% --- Scenario B discussion patch ---
45	% In "Two-level failure" paragraph, replace the λ=0.1 placeholder with:
46	%   "At $\lambda = 0.1$ (20$\times$ higher dose), CAR remains within
47	%    the null range ({MEAN}\%), confirming that Level~A signal masking
48	%    is not the binding constraint. The failure is architectural:
49	%    EE-only supervision cannot prevent arm-body collisions regardless
50	%    of loss weight."
51	%
52	% In abstract, after "LoRA+SDF at $\lambda \in \{0.005, 0.01\}$":
53	%   Extend to: "$\lambda \in \{0.005, 0.01, 0.1\}$"
54	%   Change "($ p > 0.1$)" scope to cover all three λ values.
55	%
56	% In limitations, remove the λ=0.1 placeholder entirely.
57	
58	% --- Scenario C discussion patch ---
59	% In "Two-level failure" paragraph, replace the λ=0.1 placeholder with:
60	%   "At $\lambda = 0.1$, CAR shows a suggestive increase to {MEAN}\%
61	%    (2 seeds), but definitive assessment of whether Level~A masking
62	%    has a breakpoint awaits the third seed."
63	%
64	% In abstract, after "$\lambda \in \{0.005, 0.01\}$ ($p > 0.1$)":
65	%   Add: "; $\lambda = 0.1$ shows a suggestive but inconclusive
66	%   increase ({MEAN}\%, 2 of 3 seeds)"
67	%
68	% In limitations, replace λ=0.1 placeholder with:
69	%   "The $\lambda = 0.1$ result ({MEAN}\%, 2 seeds) is suggestive
70	%    but underpowered; the third seed was in progress at submission."
71	
72	% --- Scenario A discussion patch ---
73	% In "Two-level failure" paragraph, replace the λ=0.1 placeholder with:
74	%   "At $\lambda = 0.1$, CAR increases to {MEAN}\% (2 seeds),
75	%    indicating that Level~A signal masking has a breakpoint between
76	%    $\lambda = 0.01$ and 0.1. Level~B misalignment remains: oracle
77	%    CAR stays below baselines regardless of signal strength."
78	%
79	% In abstract, after "$\lambda \in \{0.005, 0.01\}$ ($p > 0.1$)":
80	%   Add: "; at $\lambda = 0.1$, CAR rises to {MEAN}\%, suggesting a
81	%   dose-response threshold (2 of 3 seeds; third pending)"
82	%
83	% In abstract, replace LAST SENTENCE with:
84	%   "EE-only geometric supervision is structurally limited by
85	%    representation-collision misalignment; at low loss weights
86	%    training signals are masked by the demonstration distribution,
87	%    but a dose-response threshold exists between $\lambda = 0.01$
88	%    and 0.1."
89	%
90	% In limitations, replace λ=0.1 placeholder with:
91	%   "The dose-response result at $\lambda = 0.1$ is based on 2 of 3
92	%    planned seeds; the third was in progress at submission."
93	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "950ec38d-281d-482d-bc8d-79f5d64f8894"
}
```

</details>

---

### System

_source line 186_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Searching for LoRA.*s0.*68|LoRA.*s0.*74|LoRA.*s0.*66|LoRA.*s0.*…",
  "usage": {
    "total_tokens": 139990,
    "tool_uses": 56,
    "duration_ms": 110781
  },
  "last_tool_name": "Grep",
  "uuid": "ba4ba1f3-9b6f-4c1d-a74a-42612bc333ed",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 187_

<details open><summary>🔧 Tool call — Grep · `toolu_01187hRJWtJLksXWo8JHABZh`</summary>

```json
{
  "pattern": "LoRA.*s0.*68|LoRA.*s0.*74|LoRA.*s0.*66|LoRA.*s0.*20|per.task.*LoRA.*s0",
  "-i": true,
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf",
  "glob": "*.{tex,md,csv}",
  "output_mode": "content",
  "head_limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "a25999ed-28e0-4f2c-a464-5d3bf8254af8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W4bCDW54rP11frwgvnL5Cu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5605,
      "cache_read_input_tokens": 134271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5605,
        "ephemeral_1h_input_tokens": 0
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

_source line 188 · 2026-05-27T13:14:30.437Z_

<details><summary>↩ Tool result · `toolu_01187hRJWtJLksXWo8JHABZh`</summary>

```text
artifacts/figures/threshold_sensitivity_v2.csv:2:LoRA s0,2,56.5,200,200
artifacts/figures/threshold_sensitivity_v2.csv:3:LoRA s0,5,56.5,200,200
artifacts/figures/threshold_sensitivity_v2.csv:4:LoRA s0,10,56.5,200,200
artifacts/figures/threshold_sensitivity_v2.csv:5:LoRA s0,20,56.5,200,200
artifacts/figures/threshold_sensitivity_v2.csv:6:LoRA s0,50,56.5,200,200
artifacts/figures/threshold_sensitivity_v2.csv:7:LoRA s0,100,56.5,200,200
artifacts/figures/threshold_sensitivity_v2.csv:8:LoRA s0,200,56.5,200,200
artifacts/figures/threshold_sensitivity_v2.csv:9:LoRA s0,300,56.5,200,200
artifacts/_project/data/ssr_analysis.md:10:| LoRA s0 30K | 51.5% | 43.5% | 56.5% | 29.5% | 200 |
artifacts/ssr_analysis.md:10:| LoRA s0 30K | 51.5% | 43.5% | 56.5% | 29.5% | 200 |
memory.md:82:## ✅ M044: LoRA s0 reeval 数据已验证有效（2026-05-26, CLOSED）
task_context/history/reviewer/loop_2.md:32:| a1_lora_object_pudding_s0 | 35807:2 | ~12K/30K | ~20h |
task_context/history/agent/loop_1_1779387311.md:29:**刚做完**：收到两个 LoRA baseline（baseline_lora_spatial_bowl_s0 + baseline_lora_object_pudding_s0）EXIT_CODE=2 失败回调，已派 Worker `worker_diagnose_baseline_lora_failed_20260521T021217` 诊断根因，**Worker 尚未返回结果**。
task_context/history/agent/loop_1_1779406437.md:32:刚收到 cron 回调：`baseline_lora_object_pudding_s0` 和 `baseline_lora_spatial_bowl_s0` 都以 EXIT_CODE=2 失败。已派诊断 Worker (`worker_diagnose_baseline_lora_failed_20260521T021217`) 正在运行中（刚启动，turn_count=2）。**尚未收到诊断结果。**
task_context/history/agent/loop_3.md:29:**刚发生**: 两个 LoRA baseline 训练 (s0, s1) 进程正常退出，cron 回调触发。我已派 Worker `worker_analyze_lora_baseline_s0_s1_20260526T013600` 去 SSH 读日志 + 更新 registry（turn_count=14，正在 update_registry）。**等 Worker 回调后需要向 Director 汇报 + 立即启动 LoRA baseline eval (plan_003)**。

[Showing results with pagination = limit: 15]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "bcfdba4c-4542-4d5b-bb7e-631c7d7d23d8"
}
```

</details>

---

### System

_source line 189_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/verify_22k_eval_report.md",
  "usage": {
    "total_tokens": 139991,
    "tool_uses": 57,
    "duration_ms": 111849
  },
  "last_tool_name": "Read",
  "uuid": "e8fca034-cbcb-450f-9d3f-542ff6e977c2",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 190_

<details open><summary>🔧 Tool call — Read · `toolu_01BZuVUdB8djx83bpVgXiGyA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/verify_22k_eval_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "44c6735d-4412-450f-99e1-821f257e6757",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W4bCDW54rP11frwgvnL5Cu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5605,
      "cache_read_input_tokens": 134271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5605,
        "ephemeral_1h_input_tokens": 0
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

_source line 191 · 2026-05-27T13:14:31.463Z_

<details><summary>↩ Tool result · `toolu_01BZuVUdB8djx83bpVgXiGyA`</summary>

```text
1	# 22K Eval 验证报告
2	
3	**日期**: 2026-05-27
4	**文件**: `/root/autodl-tmp/eval_results/eval_s0_l1_22k_seed7.json` (85,177 bytes)
5	**Checkpoint**: `a1_sdf_pi05_object_pudding_seed0_l1/22000`
6	**Seed**: 7 | **Safety Level**: II | **Episodes/task**: 50 | **Tasks**: 4
7	
8	## 1. 数据验证结果
9	
10	Reviewer 报告值全部匹配，eval 数据有效。
11	
12	| 指标 | Reviewer 报告 | 实际值 | 验证 |
13	|------|--------------|--------|------|
14	| 总体 CAR | 60.5% | 60.5% | PASS |
15	| 总体 TSR | 45.5% | 45.5% | PASS |
16	| Frozen rate | 0% | 0% | PASS |
17	| 总 episodes | 200 | 200 | PASS |
18	| orange_juice CAR | 66% | 66% | PASS |
19	| chocolate_pudding CAR | 76% | 76% | PASS |
20	| bbq_sauce CAR | 32% | 32% | PASS |
21	
22	## 2. Per-task 完整数据
23	
24	| Task | CAR | TSR | avg_smoothness | avg_max_disp | avg_max_ee_disp |
25	|------|-----|-----|----------------|-------------|-----------------|
26	| orange_juice | 0.66 | 0.18 | 0.000782 | 0.0365 | 0.397 |
27	| chocolate_pudding | 0.76 | 0.74 | 0.000817 | 0.0484 | 0.417 |
28	| milk | 0.68 | 0.32 | 0.000635 | 0.0420 | 0.357 |
29	| bbq_sauce | 0.32 | 0.58 | 0.000637 | 0.0891 | 0.399 |
30	| **平均** | **0.605** | **0.455** | **0.000718** | **0.0540** | **0.393** |
31	
32	所有 task 的 avg_max_ee_displacement > 0.3m，确认无 frozen episode。
33	
34	## 3. s1 22K Checkpoint
35	
36	**存在**。路径: `a1_sdf_pi05_object_pudding_seed1_l1/22000/`
37	
38	- model.safetensors: 7.5GB
39	- 创建时间: 2026-05-27 07:30
40	- s1 最新 checkpoint: **24000**（已超过 22K）
41	
42	## 4. GPU 状态
43	
44	| GPU | 显存占用 | 利用率 | 状态 |
45	|-----|---------|--------|------|
46	| cuda:0 | 0 MiB / 97887 MiB | 0% | **空闲** |
47	| cuda:1 | 27045 MiB / 97887 MiB | 100% | 训练中 |
48	| cuda:2 | 27045 MiB / 97887 MiB | 100% | 训练中 |
49	| cuda:3 | 27037 MiB / 97887 MiB | 100% | 训练中 |
50	
51	cuda:0 已释放，可用于后续 eval 任务。
52	
53	## 5. s0 训练进度
54	
55	- s0 最新 checkpoint: **24000**（保存于 2026-05-27 09:23）
56	- best_loss: 0.0121 @ step 24000
57	- 距离 30K 目标还差 ~6000 steps
58	- s0 和 s1 均在 cuda:1-3 上继续训练（3 GPU 各占 ~27GB）
59	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "075e2f85-7aca-4c26-b74c-3060d6b05047"
}
```

</details>

---

### System

_source line 192_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "description": "Reading artifacts/reeval_comparison.tex",
  "usage": {
    "total_tokens": 142410,
    "tool_uses": 58,
    "duration_ms": 116204
  },
  "last_tool_name": "Read",
  "uuid": "16c372c8-7514-4187-bb2c-372c87e480fb",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool call

_source line 193_

<details open><summary>🔧 Tool call — Read · `toolu_01GDjDFCHSxVf44fX6sLqj3q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/reeval_comparison.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "145a1208-958b-4687-918a-9724d602703d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UviBSGnfYttAJHhqAGcVPi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2417,
      "cache_read_input_tokens": 139876,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2417,
        "ephemeral_1h_input_tokens": 0
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

_source line 194 · 2026-05-27T13:14:35.809Z_

<details><summary>↩ Tool result · `toolu_01GDjDFCHSxVf44fX6sLqj3q`</summary>

```text
File unchanged since last read. The content from the earlier Read tool_result in this conversation is still current — refer to that instead of re-reading.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "0dcd88d6-887a-4c66-94a4-4b7cbe84a152"
}
```

</details>

---

### System

_source line 195_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "aaaea7ca4b4e91a83",
  "tool_use_id": "toolu_016PqJ6mRBZAbsXqCoBpSruV",
  "status": "completed",
  "output_file": "",
  "summary": "Audit reviewer corrections in paper",
  "usage": {
    "total_tokens": 142585,
    "tool_uses": 58,
    "duration_ms": 204505
  },
  "uuid": "ee73d485-f772-4d76-9754-de4643b7e155",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725"
}
```

---

### Tool result

_source line 196 · 2026-05-27T13:16:04.109Z_

<details><summary>↩ Tool result · `toolu_016PqJ6mRBZAbsXqCoBpSruV`</summary>

````text
Now I have all the information I need to compile the full audit report.

---

## Audit Report

### Item 1: s1 per-task numbers from eval_pi05_a1_30k_s1_l01_high

**Correct values (from checklist):** OJ CAR=66%, CP CAR=72%, milk CAR=70%, bbq CAR=26%; TSR: OJ=26%, CP=80%, milk=28%, bbq=62%

**Finding: These specific per-task numbers for s1_l01_high are NOT referenced in any tex file.**

The only place these exact per-task numbers appear in any paper file is indirectly. The report.md confirms the aggregate: `eval_pi05_a1_30k_s1_l01_high` CAR=58.5%, TSR=49%. However, no tex file breaks this down by task.

The closest per-task breakdowns in tex files are:

1. **`dream_reports/dream_20260526T023936/median/paper.tex`** line 306-313 (`tab:lambda01-pertask`): Shows per-task for lambda=0.1, but these are **different numbers** -- s1 CAR: OJ=70, CP=50, milk=92, bbq=28. These are clearly for a **different eval** (likely 20K checkpoint or different seed data), not the 30K s1_l01_high eval with the correct values.

2. **`dream_reports/dream_20260526T023936/best/paper.tex`** line 237-247 (`tab:lambda01_pertask`): Shows lambda=0.1 per-task with s0/s1, but again different numbers -- s1 CAR: OJ=58, CP=40, milk=80, bbq=22.

3. **`dream_reports/dream_20260526T023936/worst/paper.tex`** line 218: mentions "seed~0: CAR=68%, TSR=2%; seed~1: CAR=66%, TSR=3%" which are **wrong** compared to the correct s1 aggregate of CAR=58.5%, TSR=49%.

**Verdict: WARNING -- per-task s1_l01_high numbers are not present in the main paper (`docs/paper/`). The dream report versions contain different (likely outdated or wrong) per-task numbers for lambda=0.1.**

Specific issues found:

- **`dream_reports/dream_20260526T023936/worst/paper.tex`**, line 218: Reports "seed~0: CAR=68%, TSR=2%; seed~1: CAR=66%, TSR=3%". The correct values per report.md are s0 CAR=58%, TSR=47%; s1 CAR=58.5%, TSR=49%. These are **completely wrong** -- the worst dream report appears to have fabricated or confused these numbers.

- **`dream_reports/dream_20260526T023936/median/paper.tex`**, lines 306-313 (tab:lambda01-pertask): Shows per-task s1 values as OJ=70, CP=50, milk=92, bbq=28. These do NOT match the correct s1_l01_high values of OJ=66, CP=72, milk=70, bbq=26.

- **`dream_reports/dream_20260526T023936/best/paper.tex`**, lines 237-247 (tab:lambda01_pertask): Shows per-task as OJ=58, CP=40, milk=80, bbq=22 for s1. Also does NOT match the correct values.

**Item 1 Status:**
- Main paper (`docs/paper/claim3.tex`): Reports only aggregate lambda=0.1 numbers (58.25% +/- 0.35, 2 seeds). No per-task breakdown included. The aggregate is **consistent** (mean of 58 and 58.5 = 58.25).
- Dream reports: All three dream report versions have **wrong** per-task and/or aggregate numbers for lambda=0.1.

---

### Item 2: LoRA Table row

**Correct values from checklist:**
- s0 reeval_v2: CAR=57%, TSR=46%, per-task OJ(68%), CP(74%), milk(66%), bbq(20%)
- s1: CAR=52.5%
- 2-seed mean: 54.75% +/- 3.18

**Findings across files:**

**Main paper (`docs/paper/claim3.tex`)**, line 17:
```
LoRA-only (no SDF) & 2 & 48.75 & 54.75\,$\pm$\,3.18 & 0.392
```
CAR=54.75 +/- 3.18 -- **CORRECT**. TSR=48.75 -- this is the 2-seed mean of (46+51.5)/2=48.75, which uses s0 TSR=46% and s1 TSR=51.5%.

**`docs/paper/appendix.tex`** (tab:per_task_tsr), lines 76-79: LoRA-only seed 0 per-task TSR: OJ=18.0, CP=72.0, Milk=32.0, BBQ=62.0. These are **TSR** values, not CAR. The checklist asked for per-task CAR. Per-task CAR for LoRA s0 is not listed here.

**`docs/paper/appendix.tex`** (tab:dfcar_threshold), lines 48-49: Shows LoRA s0 = 57.0 and LoRA s1 = 52.5 across all thresholds. These are **dfCAR/CAR values** and match the checklist (s0=57%, s1=52.5%).

**`artifacts/reeval_comparison.tex`**, line 14: 
```
LoRA-only s0 & 6.5 & 51.5 & +45.0 & 54.5 & 56.5 & +2.0 & 0.396
```
This shows LoRA-only s0 "After" CAR=56.5, which is the **old** eval before the reeval_v2 was done. The reeval_v2 gives CAR=57%. This file is outdated and uses the wrong value.

**`artifacts/figures/threshold_sensitivity_v2.csv`**: Shows LoRA s0 = 56.5 across all thresholds -- this is the **old** eval data, not the reeval_v2 value of 57%.

**`_project/data/ssr_analysis.md`**, line 10: Shows LoRA s0 30K CAR=56.5% -- again the **old** value before reeval.

**Dream reports**: 
- `dream_20260526T023936/best/paper.tex` (tab:lora_3seed), line 167: s0 CAR=54.5, s1=56.0, s2=55.0. These are **completely different** and wrong values. The correct LoRA s0 CAR from reeval_v2 is 57%, s1=52.5%. There is no s2 (only 2 seeds for LoRA-only).
- `dream_20260526T023936/median/paper.tex` (tab:3v3), line 265: s0=54.5, s1=56.0, s2=48.0 for LoRA-only. Also **wrong** and also shows 3 seeds when only 2 exist.
- `dream_20260526T023936/worst/paper.tex` (tab:lora_3seed), line 167: s0=54.5, s1=56.0, s2=44.0. Also **wrong** and 3 seeds.

**Item 2 Status:**
- Main paper (`docs/paper/claim3.tex`): Aggregate (54.75 +/- 3.18) is **CORRECT**.
- Main paper (`docs/paper/appendix.tex`): Per-seed CAR (s0=57.0, s1=52.5) is **CORRECT**.
- `reeval_comparison.tex` line 14: LoRA s0 "After" CAR=56.5 is **WRONG** (should be 57% per reeval_v2).
- `_project/data/ssr_analysis.md` line 10: LoRA s0 CAR=56.5% is **WRONG** (should be 57%).
- `artifacts/figures/threshold_sensitivity_v2.csv`: LoRA s0 = 56.5 is **WRONG** (should be 57%).
- All three dream reports: Per-seed LoRA values are **WRONG** and incorrectly show 3 seeds.

---

### Item 3: EE Displacement (avg_max_ee_displacement)

**Correct values from checklist:** s1 l01 high: avg_max_ee=0.3884, avg_max_obstacle=0.0553

**Findings:**

The specific values 0.3884 and 0.0553 do NOT appear in any tex file. The main paper reports EE displacement in aggregate:

**`docs/paper/claim3.tex`**, line 20: lambda=0.1 EE Disp = 0.394. This is the 2-seed mean. If s0=0.393 (from verify_22k_eval_report.md for a 22K checkpoint; the 30K value may differ) and s1=0.3884, the average would be ~0.39, close to 0.394. The 0.394 figure appears to be an approximation or uses slightly different data.

The value 0.0553 for avg_max_obstacle displacement: this exact number appears in `task3_collision_matrix_step10k.md` line 123, but that's for a specific episode's wine_bottle displacement at step 10K, not the s1_l01_high aggregate.

**Item 3 Status:**
- Main paper does not report the specific values 0.3884 or 0.0553 anywhere. It reports aggregate EE Disp = 0.394m for lambda=0.1 in `docs/paper/claim3.tex`.
- The 0.394 figure is close to the expected 2-seed average but is not precisely verified against the raw data.

---

### Item 4: std consistency

**Correct values from checklist:**
- LoRA-only: mean=54.75%, std=3.18% (2 seeds: 57, 52.5)
- lambda=0.005: mean=54.5%, std=2.29% (3 seeds: 57, 54, 52.5)
- lambda=0.01: mean=56.33%, std=1.61% (3 seeds: 57, 57.5, 54.5)
- lambda=0.1: mean=58.25%, std=0.35% (2 seeds: 58, 58.5)

**Main paper (`docs/paper/claim3.tex`)**, lines 17-20:
```
LoRA-only (no SDF) & 2 & 48.75 & 54.75\,$\pm$\,3.18 & 0.392
LoRA+SDF $\lambda{=}0.005$ & 3 & 54.0\,$\pm$\,3.0 & 54.5\,$\pm$\,2.29 & 0.387
LoRA+SDF $\lambda{=}0.01$ & 3 & 53.8\,$\pm$\,1.5 & 56.33\,$\pm$\,1.61 & 0.389
LoRA+SDF $\lambda{=}0.1$ & 2 & 48.0\,$\pm$\,1.4 & 58.25\,$\pm$\,0.35 & 0.394
```
All four rows match exactly: 54.75+/-3.18, 54.5+/-2.29, 56.33+/-1.61, 58.25+/-0.35. **CORRECT**.

**`docs/paper/abstract.tex`**, line 7: "54.75\%$\,\pm\,$3.18 ... 54.5\%$\,\pm\,$2.29 ... 56.33\%$\,\pm\,$1.61 ... 58.25\%$\,\pm\,$0.35" -- **CORRECT**.

**`docs/paper/introduction.tex`**, line 20: "raises CAR by ${\sim}$28 points (26.8\% $\to$ 54.75\%)" -- **CORRECT**.

**`_project/data/fig5_lambda_data.csv`**: 54.75/3.18, 54.5/2.29, 56.33/1.61, 58.25/0.35 -- **CORRECT**.

**`artifacts/claim3_data_summary.md` / `_project/data/claim3_data_summary.md`**: 54.5+/-2.83 for LoRA (different from 3.18) and 55.5+/-0.71 for lambda=0.1 (different from 0.35). These are **older data** before the reeval_v2. The LoRA std=2.83 uses the old s0=56.5 value, and lambda=0.1 uses 20K checkpoint values (55, 56). These are outdated but labeled correctly as "20K".

**Dream reports**:
- `dream_20260526T023936/best/paper.tex`: LoRA-only mean=55.2 +/- 0.4 (wrong), SDF 0.005=50.5 +/- 3.0 (wrong), SDF 0.01=52.8 +/- 0.3 (wrong), SDF 0.1=51.0 +/- 1.4 (wrong). **ALL WRONG**.
- `dream_20260526T023936/median/paper.tex`: LoRA-only=52.8 +/- 4.2 (wrong), SDF 0.005=50.5 +/- 3.0 (wrong), SDF 0.01=52.7 +/- 0.3 (wrong), SDF 0.1=58.5 +/- 2.1 (wrong). **ALL WRONG**.
- `dream_20260526T023936/worst/paper.tex`: LoRA-only=51.5 +/- 6.5 (wrong), SDF 0.005=52.3 +/- 1.5 (wrong), SDF 0.01=52.8 +/- 0.3 (wrong), SDF 0.1=67.0 +/- 1.0 (wrong). **ALL WRONG**.

**Item 4 Status:**
- Main paper (`docs/paper/`) numbers are all **CORRECT** and internally consistent.
- `fig5_lambda_data.csv` is **CORRECT**.
- All three dream reports have **WRONG** numbers across the board.
- `claim3_data_summary.md` has older pre-reeval values (labeled as such), which differ but are not used in the main paper.

---

## Summary

### Item 1 (s1 per-task numbers)
- Main paper (`docs/paper/`): Per-task breakdown not included for lambda=0.1, only aggregate 58.25% shown. Aggregate is correct.
- Dream reports: All three versions have **wrong** per-task and aggregate numbers.
  - `worst/paper.tex` line 218: s0 CAR=68%/TSR=2%, s1 CAR=66%/TSR=3% -- should be s0=58%/47%, s1=58.5%/49%.

### Item 2 (LoRA Table row)
- Main paper: Aggregate 54.75 +/- 3.18 **CORRECT**, per-seed s0=57/s1=52.5 **CORRECT**.
- `reeval_comparison.tex` line 14: LoRA s0 After CAR=56.5 **WRONG** (should be 57).
- `ssr_analysis.md` line 10: LoRA s0 CAR=56.5% **WRONG** (should be 57).
- `threshold_sensitivity_v2.csv`: LoRA s0 = 56.5 **WRONG** (should be 57).
- Dream reports: All three show wrong LoRA values and incorrectly claim 3 seeds.

### Item 3 (EE Displacement)
- Specific values 0.3884 and 0.0553 not mentioned in any paper file. Main paper reports aggregate EE Disp=0.394m, which is close.

### Item 4 (std consistency)
- Main paper (`docs/paper/`): All four rows **CORRECT** (54.75+/-3.18, 54.5+/-2.29, 56.33+/-1.61, 58.25+/-0.35).
- Dream reports: All three versions have **completely wrong** numbers for all conditions.

### Files requiring corrections

| File | Line(s) | Issue | Current | Correct |
|------|---------|-------|---------|---------|
| `artifacts/reeval_comparison.tex` | 14 | LoRA s0 After CAR | 56.5 | 57.0 |
| `artifacts/_project/data/ssr_analysis.md` | 10 | LoRA s0 CAR | 56.5% | 57.0% |
| `artifacts/ssr_analysis.md` | 10 | LoRA s0 CAR (duplicate) | 56.5% | 57.0% |
| `artifacts/figures/threshold_sensitivity_v2.csv` | 2-9 | LoRA s0 dfCAR values | 56.5 | 57.0 |
| `dream_reports/dream_20260526T023936/worst/paper.tex` | 218 | lambda=0.1 seed-level values | s0=68%/2%, s1=66%/3% | s0=58%/47%, s1=58.5%/49% |
| `dream_reports/dream_20260526T023936/best/paper.tex` | 167-171 | LoRA 3-seed table | s0=54.5,s1=56.0,s2=55.0,mean=55.2 | s0=57,s1=52.5,mean=54.75 (2 seeds) |
| `dream_reports/dream_20260526T023936/median/paper.tex` | 265 | LoRA 3-seed table | s0=54.5,s1=56.0,s2=48.0,mean=52.8 | s0=57,s1=52.5,mean=54.75 (2 seeds) |
| `dream_reports/dream_20260526T023936/worst/paper.tex` | 167 | LoRA 3-seed table | s0=54.5,s1=56.0,s2=44.0,mean=51.5 | s0=57,s1=52.5,mean=54.75 (2 seeds) |
| All 3 dream reports | Multiple tables | Lambda curve CAR/std values | Various wrong values | See fig5_lambda_data.csv for correct |

The **main paper** in `docs/paper/` is clean -- all numbers in the 4 checklist items are correct. The errors are concentrated in:
1. **Dream reports** (all three `dream_20260526T023936` versions) -- comprehensively wrong numbers
2. **reeval_comparison.tex** -- outdated LoRA s0 value (56.5 vs 57.0)
3. **Data files** (ssr_analysis.md, threshold_sensitivity_v2.csv) -- outdated LoRA s0 value

agentId: aaaea7ca4b4e91a83 (use SendMessage with to: 'aaaea7ca4b4e91a83' to continue this agent)
&lt;usage>total_tokens: 147419
tool_uses: 58
duration_ms: 204508&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "f798ccc8-520a-465c-8073-49fd23eb10dd",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You are auditing a research paper for specific numerical corrections. The paper files are in:\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/drafts/` (main drafts)\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/` (project paper files)\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/dream_reports/` (dream report versions)\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper/` (paper directory)\n\nAlso check: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/reeval_comparison.tex`\n\nAnd check for any registry/data files:\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/report/paper_data_summary.md`\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/data/` directory\n\n## Checklist to verify\n\n### Item 1: s1 per-task numbers\nCheck if the paper references per-task numbers from eval_pi05_a1_30k_s1_l01_high:\n- Correct values: OJ CAR=66%, CP CAR=72%, milk CAR=70%, bbq CAR=26%\n- TSR: OJ=26%, CP=80%, milk=28%, bbq=62%\nSearch for these numbers or any per-task breakdown in all tex/md files. Note any incorrect values.\n\n### Item 2: LoRA Table row\nCheck all tables for the LoRA-only baseline row:\n- s0 reeval_v2: CAR=57%, TSR=46%, per-task OJ(68%), CP(74%), milk(66%), bbq(20%)\n- s1: CAR=52.5%\n- 2-seed mean: 54.75% ±3.18\nSearch for \"LoRA\", \"lora\", \"baseline\" in tables, and check if numbers match.\n\n### Item 3: EE Disp (End-Effector Displacement)\nCheck if paper mentions avg_max_ee_displacement:\n- s1 l01 high: avg_max_ee=0.3884, avg_max_obstacle=0.0553\nSearch for \"ee_disp\", \"displacement\", \"0.3884\", \"0.0553\" in all files.\n\n### Item 4: std consistency\nCheck reported std/SE values:\n- LoRA-only: mean=54.75%, std=3.18% (2 seeds: 57, 52.5)\n- λ=0.005: mean=54.5%, std=2.29% (3 seeds: 57, 54, 52.5)\n- λ=0.01: mean=56.33%, std=1.61% (3 seeds: 57, 57.5, 54.5)\n- λ=0.1: mean=58.25%, std=0.35% (2 seeds: 58, 58.5)\nSearch for \"±\", \"std\", \"3.18\", \"2.29\", \"1.61\", \"0.35\", \"54.75\", \"54.5\", \"56.33\", \"58.25\" in all files.\n\n## Instructions\n1. Read ALL tex files in the drafts/ and _project/paper/ directories\n2. Read the most recent dream_reports paper.tex files (the ones in dream_20260526T023936/)\n3. Read reeval_comparison.tex\n4. Read paper_data_summary.md and any data files in _project/data/\n5. Search for each number from the checklist\n6. For EACH of the 4 items, report:\n   - ✅ if correct values found in the paper\n   - ❌ if wrong values found, with: file path, line number, current wrong value, correct value\n   - ⚠️ if the item is not mentioned at all in the paper\n7. Be thorough - check ALL files, not just the first match\n\nReport your findings in detail with exact file paths and line numbers.",
    "agentId": "aaaea7ca4b4e91a83",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information I need to compile the full audit report.\n\n---\n\n## Audit Report\n\n### Item 1: s1 per-task numbers from eval_pi05_a1_30k_s1_l01_high\n\n**Correct values (from checklist):** OJ CAR=66%, CP CAR=72%, milk CAR=70%, bbq CAR=26%; TSR: OJ=26%, CP=80%, milk=28%, bbq=62%\n\n**Finding: These specific per-task numbers for s1_l01_high are NOT referenced in any tex file.**\n\nThe only place these exact per-task numbers appear in any paper file is indirectly. The report.md confirms the aggregate: `eval_pi05_a1_30k_s1_l01_high` CAR=58.5%, TSR=49%. However, no tex file breaks this down by task.\n\nThe closest per-task breakdowns in tex files are:\n\n1. **`dream_reports/dream_20260526T023936/median/paper.tex`** line 306-313 (`tab:lambda01-pertask`): Shows per-task for lambda=0.1, but these are **different numbers** -- s1 CAR: OJ=70, CP=50, milk=92, bbq=28. These are clearly for a **different eval** (likely 20K checkpoint or different seed data), not the 30K s1_l01_high eval with the correct values.\n\n2. **`dream_reports/dream_20260526T023936/best/paper.tex`** line 237-247 (`tab:lambda01_pertask`): Shows lambda=0.1 per-task with s0/s1, but again different numbers -- s1 CAR: OJ=58, CP=40, milk=80, bbq=22.\n\n3. **`dream_reports/dream_20260526T023936/worst/paper.tex`** line 218: mentions \"seed~0: CAR=68%, TSR=2%; seed~1: CAR=66%, TSR=3%\" which are **wrong** compared to the correct s1 aggregate of CAR=58.5%, TSR=49%.\n\n**Verdict: WARNING -- per-task s1_l01_high numbers are not present in the main paper (`docs/paper/`). The dream report versions contain different (likely outdated or wrong) per-task numbers for lambda=0.1.**\n\nSpecific issues found:\n\n- **`dream_reports/dream_20260526T023936/worst/paper.tex`**, line 218: Reports \"seed~0: CAR=68%, TSR=2%; seed~1: CAR=66%, TSR=3%\". The correct values per report.md are s0 CAR=58%, TSR=47%; s1 CAR=58.5%, TSR=49%. These are **completely wrong** -- the worst dream report appears to have fabricated or confused these numbers.\n\n- **`dream_reports/dream_20260526T023936/median/paper.tex`**, lines 306-313 (tab:lambda01-pertask): Shows per-task s1 values as OJ=70, CP=50, milk=92, bbq=28. These do NOT match the correct s1_l01_high values of OJ=66, CP=72, milk=70, bbq=26.\n\n- **`dream_reports/dream_20260526T023936/best/paper.tex`**, lines 237-247 (tab:lambda01_pertask): Shows per-task as OJ=58, CP=40, milk=80, bbq=22 for s1. Also does NOT match the correct values.\n\n**Item 1 Status:**\n- Main paper (`docs/paper/claim3.tex`): Reports only aggregate lambda=0.1 numbers (58.25% +/- 0.35, 2 seeds). No per-task breakdown included. The aggregate is **consistent** (mean of 58 and 58.5 = 58.25).\n- Dream reports: All three dream report versions have **wrong** per-task and/or aggregate numbers for lambda=0.1.\n\n---\n\n### Item 2: LoRA Table row\n\n**Correct values from checklist:**\n- s0 reeval_v2: CAR=57%, TSR=46%, per-task OJ(68%), CP(74%), milk(66%), bbq(20%)\n- s1: CAR=52.5%\n- 2-seed mean: 54.75% +/- 3.18\n\n**Findings across files:**\n\n**Main paper (`docs/paper/claim3.tex`)**, line 17:\n```\nLoRA-only (no SDF) & 2 & 48.75 & 54.75\\,$\\pm$\\,3.18 & 0.392\n```\nCAR=54.75 +/- 3.18 -- **CORRECT**. TSR=48.75 -- this is the 2-seed mean of (46+51.5)/2=48.75, which uses s0 TSR=46% and s1 TSR=51.5%.\n\n**`docs/paper/appendix.tex`** (tab:per_task_tsr), lines 76-79: LoRA-only seed 0 per-task TSR: OJ=18.0, CP=72.0, Milk=32.0, BBQ=62.0. These are **TSR** values, not CAR. The checklist asked for per-task CAR. Per-task CAR for LoRA s0 is not listed here.\n\n**`docs/paper/appendix.tex`** (tab:dfcar_threshold), lines 48-49: Shows LoRA s0 = 57.0 and LoRA s1 = 52.5 across all thresholds. These are **dfCAR/CAR values** and match the checklist (s0=57%, s1=52.5%).\n\n**`artifacts/reeval_comparison.tex`**, line 14: \n```\nLoRA-only s0 & 6.5 & 51.5 & +45.0 & 54.5 & 56.5 & +2.0 & 0.396\n```\nThis shows LoRA-only s0 \"After\" CAR=56.5, which is the **old** eval before the reeval_v2 was done. The reeval_v2 gives CAR=57%. This file is outdated and uses the wrong value.\n\n**`artifacts/figures/threshold_sensitivity_v2.csv`**: Shows LoRA s0 = 56.5 across all thresholds -- this is the **old** eval data, not the reeval_v2 value of 57%.\n\n**`_project/data/ssr_analysis.md`**, line 10: Shows LoRA s0 30K CAR=56.5% -- again the **old** value before reeval.\n\n**Dream reports**: \n- `dream_20260526T023936/best/paper.tex` (tab:lora_3seed), line 167: s0 CAR=54.5, s1=56.0, s2=55.0. These are **completely different** and wrong values. The correct LoRA s0 CAR from reeval_v2 is 57%, s1=52.5%. There is no s2 (only 2 seeds for LoRA-only).\n- `dream_20260526T023936/median/paper.tex` (tab:3v3), line 265: s0=54.5, s1=56.0, s2=48.0 for LoRA-only. Also **wrong** and also shows 3 seeds when only 2 exist.\n- `dream_20260526T023936/worst/paper.tex` (tab:lora_3seed), line 167: s0=54.5, s1=56.0, s2=44.0. Also **wrong** and 3 seeds.\n\n**Item 2 Status:**\n- Main paper (`docs/paper/claim3.tex`): Aggregate (54.75 +/- 3.18) is **CORRECT**.\n- Main paper (`docs/paper/appendix.tex`): Per-seed CAR (s0=57.0, s1=52.5) is **CORRECT**.\n- `reeval_comparison.tex` line 14: LoRA s0 \"After\" CAR=56.5 is **WRONG** (should be 57% per reeval_v2).\n- `_project/data/ssr_analysis.md` line 10: LoRA s0 CAR=56.5% is **WRONG** (should be 57%).\n- `artifacts/figures/threshold_sensitivity_v2.csv`: LoRA s0 = 56.5 is **WRONG** (should be 57%).\n- All three dream reports: Per-seed LoRA values are **WRONG** and incorrectly show 3 seeds.\n\n---\n\n### Item 3: EE Displacement (avg_max_ee_displacement)\n\n**Correct values from checklist:** s1 l01 high: avg_max_ee=0.3884, avg_max_obstacle=0.0553\n\n**Findings:**\n\nThe specific values 0.3884 and 0.0553 do NOT appear in any tex file. The main paper reports EE displacement in aggregate:\n\n**`docs/paper/claim3.tex`**, line 20: lambda=0.1 EE Disp = 0.394. This is the 2-seed mean. If s0=0.393 (from verify_22k_eval_report.md for a 22K checkpoint; the 30K value may differ) and s1=0.3884, the average would be ~0.39, close to 0.394. The 0.394 figure appears to be an approximation or uses slightly different data.\n\nThe value 0.0553 for avg_max_obstacle displacement: this exact number appears in `task3_collision_matrix_step10k.md` line 123, but that's for a specific episode's wine_bottle displacement at step 10K, not the s1_l01_high aggregate.\n\n**Item 3 Status:**\n- Main paper does not report the specific values 0.3884 or 0.0553 anywhere. It reports aggregate EE Disp = 0.394m for lambda=0.1 in `docs/paper/claim3.tex`.\n- The 0.394 figure is close to the expected 2-seed average but is not precisely verified against the raw data.\n\n---\n\n### Item 4: std consistency\n\n**Correct values from checklist:**\n- LoRA-only: mean=54.75%, std=3.18% (2 seeds: 57, 52.5)\n- lambda=0.005: mean=54.5%, std=2.29% (3 seeds: 57, 54, 52.5)\n- lambda=0.01: mean=56.33%, std=1.61% (3 seeds: 57, 57.5, 54.5)\n- lambda=0.1: mean=58.25%, std=0.35% (2 seeds: 58, 58.5)\n\n**Main paper (`docs/paper/claim3.tex`)**, lines 17-20:\n```\nLoRA-only (no SDF) & 2 & 48.75 & 54.75\\,$\\pm$\\,3.18 & 0.392\nLoRA+SDF $\\lambda{=}0.005$ & 3 & 54.0\\,$\\pm$\\,3.0 & 54.5\\,$\\pm$\\,2.29 & 0.387\nLoRA+SDF $\\lambda{=}0.01$ & 3 & 53.8\\,$\\pm$\\,1.5 & 56.33\\,$\\pm$\\,1.61 & 0.389\nLoRA+SDF $\\lambda{=}0.1$ & 2 & 48.0\\,$\\pm$\\,1.4 & 58.25\\,$\\pm$\\,0.35 & 0.394\n```\nAll four rows match exactly: 54.75+/-3.18, 54.5+/-2.29, 56.33+/-1.61, 58.25+/-0.35. **CORRECT**.\n\n**`docs/paper/abstract.tex`**, line 7: \"54.75\\%$\\,\\pm\\,$3.18 ... 54.5\\%$\\,\\pm\\,$2.29 ... 56.33\\%$\\,\\pm\\,$1.61 ... 58.25\\%$\\,\\pm\\,$0.35\" -- **CORRECT**.\n\n**`docs/paper/introduction.tex`**, line 20: \"raises CAR by ${\\sim}$28 points (26.8\\% $\\to$ 54.75\\%)\" -- **CORRECT**.\n\n**`_project/data/fig5_lambda_data.csv`**: 54.75/3.18, 54.5/2.29, 56.33/1.61, 58.25/0.35 -- **CORRECT**.\n\n**`artifacts/claim3_data_summary.md` / `_project/data/claim3_data_summary.md`**: 54.5+/-2.83 for LoRA (different from 3.18) and 55.5+/-0.71 for lambda=0.1 (different from 0.35). These are **older data** before the reeval_v2. The LoRA std=2.83 uses the old s0=56.5 value, and lambda=0.1 uses 20K checkpoint values (55, 56). These are outdated but labeled correctly as \"20K\".\n\n**Dream reports**:\n- `dream_20260526T023936/best/paper.tex`: LoRA-only mean=55.2 +/- 0.4 (wrong), SDF 0.005=50.5 +/- 3.0 (wrong), SDF 0.01=52.8 +/- 0.3 (wrong), SDF 0.1=51.0 +/- 1.4 (wrong). **ALL WRONG**.\n- `dream_20260526T023936/median/paper.tex`: LoRA-only=52.8 +/- 4.2 (wrong), SDF 0.005=50.5 +/- 3.0 (wrong), SDF 0.01=52.7 +/- 0.3 (wrong), SDF 0.1=58.5 +/- 2.1 (wrong). **ALL WRONG**.\n- `dream_20260526T023936/worst/paper.tex`: LoRA-only=51.5 +/- 6.5 (wrong), SDF 0.005=52.3 +/- 1.5 (wrong), SDF 0.01=52.8 +/- 0.3 (wrong), SDF 0.1=67.0 +/- 1.0 (wrong). **ALL WRONG**.\n\n**Item 4 Status:**\n- Main paper (`docs/paper/`) numbers are all **CORRECT** and internally consistent.\n- `fig5_lambda_data.csv` is **CORRECT**.\n- All three dream reports have **WRONG** numbers across the board.\n- `claim3_data_summary.md` has older pre-reeval values (labeled as such), which differ but are not used in the main paper.\n\n---\n\n## Summary\n\n### Item 1 (s1 per-task numbers)\n- Main paper (`docs/paper/`): Per-task breakdown not included for lambda=0.1, only aggregate 58.25% shown. Aggregate is correct.\n- Dream reports: All three versions have **wrong** per-task and aggregate numbers.\n  - `worst/paper.tex` line 218: s0 CAR=68%/TSR=2%, s1 CAR=66%/TSR=3% -- should be s0=58%/47%, s1=58.5%/49%.\n\n### Item 2 (LoRA Table row)\n- Main paper: Aggregate 54.75 +/- 3.18 **CORRECT**, per-seed s0=57/s1=52.5 **CORRECT**.\n- `reeval_comparison.tex` line 14: LoRA s0 After CAR=56.5 **WRONG** (should be 57).\n- `ssr_analysis.md` line 10: LoRA s0 CAR=56.5% **WRONG** (should be 57).\n- `threshold_sensitivity_v2.csv`: LoRA s0 = 56.5 **WRONG** (should be 57).\n- Dream reports: All three show wrong LoRA values and incorrectly claim 3 seeds.\n\n### Item 3 (EE Displacement)\n- Specific values 0.3884 and 0.0553 not mentioned in any paper file. Main paper reports aggregate EE Disp=0.394m, which is close.\n\n### Item 4 (std consistency)\n- Main paper (`docs/paper/`): All four rows **CORRECT** (54.75+/-3.18, 54.5+/-2.29, 56.33+/-1.61, 58.25+/-0.35).\n- Dream reports: All three versions have **completely wrong** numbers for all conditions.\n\n### Files requiring corrections\n\n| File | Line(s) | Issue | Current | Correct |\n|------|---------|-------|---------|---------|\n| `artifacts/reeval_comparison.tex` | 14 | LoRA s0 After CAR | 56.5 | 57.0 |\n| `artifacts/_project/data/ssr_analysis.md` | 10 | LoRA s0 CAR | 56.5% | 57.0% |\n| `artifacts/ssr_analysis.md` | 10 | LoRA s0 CAR (duplicate) | 56.5% | 57.0% |\n| `artifacts/figures/threshold_sensitivity_v2.csv` | 2-9 | LoRA s0 dfCAR values | 56.5 | 57.0 |\n| `dream_reports/dream_20260526T023936/worst/paper.tex` | 218 | lambda=0.1 seed-level values | s0=68%/2%, s1=66%/3% | s0=58%/47%, s1=58.5%/49% |\n| `dream_reports/dream_20260526T023936/best/paper.tex` | 167-171 | LoRA 3-seed table | s0=54.5,s1=56.0,s2=55.0,mean=55.2 | s0=57,s1=52.5,mean=54.75 (2 seeds) |\n| `dream_reports/dream_20260526T023936/median/paper.tex` | 265 | LoRA 3-seed table | s0=54.5,s1=56.0,s2=48.0,mean=52.8 | s0=57,s1=52.5,mean=54.75 (2 seeds) |\n| `dream_reports/dream_20260526T023936/worst/paper.tex` | 167 | LoRA 3-seed table | s0=54.5,s1=56.0,s2=44.0,mean=51.5 | s0=57,s1=52.5,mean=54.75 (2 seeds) |\n| All 3 dream reports | Multiple tables | Lambda curve CAR/std values | Various wrong values | See fig5_lambda_data.csv for correct |\n\nThe **main paper** in `docs/paper/` is clean -- all numbers in the 4 checklist items are correct. The errors are concentrated in:\n1. **Dream reports** (all three `dream_20260526T023936` versions) -- comprehensively wrong numbers\n2. **reeval_comparison.tex** -- outdated LoRA s0 value (56.5 vs 57.0)\n3. **Data files** (ssr_analysis.md, threshold_sensitivity_v2.csv) -- outdated LoRA s0 value"
      }
    ],
    "totalDurationMs": 204508,
    "totalTokens": 147419,
    "totalToolUseCount": 58,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 174,
      "cache_read_input_tokens": 142293,
      "output_tokens": 4951,
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
          "output_tokens": 4951,
          "cache_read_input_tokens": 142293,
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
    "toolStats": {
      "readCount": 44,
      "searchCount": 14,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
````

</details>

---

### Assistant

_source line 197_

<details><summary>Logged reasoning block</summary>

```text
The agent has done a very thorough audit. Let me now compile a clean audit report for the user. The key findings are:

1. Main paper files (docs/paper/) have correct numbers for items 2 and 4
2. Per-task s1 breakdown (item 1) is not included in the main paper
3. EE displacement specific values (item 3) not in any paper file
4. Dream reports have widespread wrong numbers
5. Some data files have outdated values

Let me also check where the main paper files actually live - the agent mentions `docs/paper/` but let me verify this path exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "927703be-8709-4a91-b951-23f3b653485d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sh1KQPo1nmzx6VKdDVa4Dk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6311,
      "cache_read_input_tokens": 26504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6311
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

_source line 198_

Let me verify the main paper location — the agent referenced `docs/paper/` which I need to confirm.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "fabfe864-3246-4549-8420-9d25a05d2dbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sh1KQPo1nmzx6VKdDVa4Dk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6311,
      "cache_read_input_tokens": 26504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6311
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

_source line 199_

<details open><summary>🔧 Tool call — Glob · `toolu_018RfXVJWh8SprX3U1FfP6wc`</summary>

```json
{
  "pattern": "**/claim3*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "709cd175-2391-4185-95b8-978b1f88b763",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sh1KQPo1nmzx6VKdDVa4Dk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6311,
      "cache_read_input_tokens": 26504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6311
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

_source line 200 · 2026-05-27T13:16:11.350Z_

<details><summary>↩ Tool result · `toolu_018RfXVJWh8SprX3U1FfP6wc`</summary>

```text
artifacts/_project/data/claim3_data_summary.md
artifacts/claim3_data_summary.md
docs/paper/claim3.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "7b8970e8-480d-47ce-b398-0a9f067fbd6b",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/data/claim3_data_summary.md",
      "artifacts/claim3_data_summary.md",
      "docs/paper/claim3.tex"
    ],
    "durationMs": 20,
    "numFiles": 3,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 201_

<details open><summary>🔧 Tool call — Glob · `toolu_01UvojXbGURm8mNmWCyQzFmJ`</summary>

```json
{
  "pattern": "**/appendix*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "d089aa7b-7197-461f-9f7a-1899e06680c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sh1KQPo1nmzx6VKdDVa4Dk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6311,
      "cache_read_input_tokens": 26504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6311
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

_source line 202 · 2026-05-27T13:16:13.123Z_

<details><summary>↩ Tool result · `toolu_01UvojXbGURm8mNmWCyQzFmJ`</summary>

```text
docs/paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "27e2e754-2311-44ba-9559-fdcdb2b5f3af",
  "tool_use_result": {
    "filenames": [
      "docs/paper/appendix.tex"
    ],
    "durationMs": 22,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 203_

<details open><summary>🔧 Tool call — Glob · `toolu_019etkDDLQxKQq61CBvxNf5y`</summary>

```json
{
  "pattern": "docs/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "48b9edc8-3294-4d4c-8fdc-82b31ee864a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sh1KQPo1nmzx6VKdDVa4Dk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6311,
      "cache_read_input_tokens": 26504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6311
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

_source line 204 · 2026-05-27T13:16:13.273Z_

<details><summary>↩ Tool result · `toolu_019etkDDLQxKQq61CBvxNf5y`</summary>

```text
docs/paper/_archive/method.tex
docs/paper/_archive/experiments.tex
docs/paper/_archive/conclusion_DEPRECATED.tex
docs/paper/archive/analysis_claim4.tex
docs/paper/archive/analysis_claim3.tex
docs/paper/archive/analysis_claim1.tex
docs/paper/archive/analysis_claim2.tex
docs/paper/contingency_claim3.tex
docs/paper/experimental_framework.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/appendix.tex
docs/paper/main.tex
docs/paper/discussion.tex
docs/paper/related_work.tex
docs/paper/claim1.tex
docs/paper/claim2.tex
docs/paper/claim3.tex
docs/paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "683a91e5-72af-4534-969f-60d085f0eabd",
  "tool_use_result": {
    "filenames": [
      "docs/paper/_archive/method.tex",
      "docs/paper/_archive/experiments.tex",
      "docs/paper/_archive/conclusion_DEPRECATED.tex",
      "docs/paper/archive/analysis_claim4.tex",
      "docs/paper/archive/analysis_claim3.tex",
      "docs/paper/archive/analysis_claim1.tex",
      "docs/paper/archive/analysis_claim2.tex",
      "docs/paper/contingency_claim3.tex",
      "docs/paper/experimental_framework.tex",
      "docs/paper/abstract.tex",
      "docs/paper/introduction.tex",
      "docs/paper/appendix.tex",
      "docs/paper/main.tex",
      "docs/paper/discussion.tex",
      "docs/paper/related_work.tex",
      "docs/paper/claim1.tex",
      "docs/paper/claim2.tex",
      "docs/paper/claim3.tex",
      "docs/paper/method.tex"
    ],
    "durationMs": 20,
    "numFiles": 19,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 205_

Good, `docs/paper/` is the main paper directory. Let me read the key files to verify the agent's findings on the critical items.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "9bca3251-b7e1-4569-af8f-d334e22bb53c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nu58NnUyskUG3amJVmsHuR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 864,
      "cache_read_input_tokens": 32815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 864
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

_source line 206_

<details open><summary>🔧 Tool call — Read · `toolu_01RKGK6RMTvnVmn9sVBSqTmR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "7988e6f9-908f-42ac-a38a-580f9f1e5055",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nu58NnUyskUG3amJVmsHuR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 864,
      "cache_read_input_tokens": 32815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 864
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

_source line 207 · 2026-05-27T13:16:16.506Z_

<details><summary>↩ Tool result · `toolu_01RKGK6RMTvnVmn9sVBSqTmR`</summary>

```text
1	\section{Avoidance Source Diagnosis}\label{sec:avoidance_source}
2	
3	Fine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\sim}$28 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only, LoRA+SDF ($\lambda = 0.005$), and LoRA+SDF ($\lambda = 0.01$) on Pi0.5, all evaluated at the 30K-step checkpoint.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Avoidance source attribution on SafeLIBERO. SDF at $\lambda \leq 0.01$ adds no measurable CAR beyond LoRA-only ($p > 0.1$); $\lambda = 0.1$ shows a marginal signal ($z = 2.27$, $p \approx 0.023$, $n{=}2$) that requires additional seeds. All fine-tuned models exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}
8	\label{tab:avoidance_source}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lcccc}
12	\toprule
13	Method & Seeds & TSR (\%) & CAR (\%) & EE Disp (m) \\
14	\midrule
15	Pi0.5 baseline & 3 & 74.7\,$\pm$\,1.5 & 26.8\,$\pm$\,1.6 & 0.367 \\
16	\midrule
17	LoRA-only (no SDF) & 2 & 48.75 & 54.75\,$\pm$\,3.18 & 0.392 \\
18	LoRA+SDF $\lambda{=}0.005$ & 3 & 54.0\,$\pm$\,3.0 & 54.5\,$\pm$\,2.29 & 0.387 \\
19	LoRA+SDF $\lambda{=}0.01$ & 3 & 53.8\,$\pm$\,1.5 & 56.33\,$\pm$\,1.61 & 0.389 \\
20	LoRA+SDF $\lambda{=}0.1$\textsuperscript{$\dagger$} & 2 & 48.0\,$\pm$\,1.4 & 58.25\,$\pm$\,0.35 & 0.394 \\
21	\bottomrule
22	\end{tabular}
23	\vspace{1pt}
24	{\footnotesize \textsuperscript{$\dagger$}30K checkpoint, two of three seeds; third seed in progress.}
25	\end{table}
26	
27	Table~\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\sim}$28 percentage points (26.8\% $\to$ 54.75\%) with zero frozen episodes and displacement above 0.37\,m, confirming genuine avoidance. Adding SDF supervision produces no measurable benefit: LoRA-only CAR (54.75\%) is within 0.25\,pp of $\lambda = 0.005$ and statistically indistinguishable from $\lambda = 0.01$ (56.33\%, $p > 0.1$; Appendix~\ref{sec:appendix_null}). A Phase~2 ablation ($\lambda = 0$ after step 5K) yields CAR\,=\,57.5\%\footnote{Single seed (s2); computational constraints precluded additional seeds for this ablation.}, confirming that SDF gradients produce no lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\_pudding highest, bbq\_sauce lowest) and invariant to $\lambda$ across a 20$\times$ range, indicating that avoidance patterns reflect the demonstration distribution rather than geometric supervision.
28	
29	\paragraph{CAR--TSR trade-off.}\label{sec:tsr_collapse}
30	Fine-tuning degrades TSR by ${\sim}$21--26\,pp (74.7\% $\to$ 48.75--54.0\%), reflecting distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\,0.37\,m displacement and 0\% frozen episodes). The SSR/TSR ratio increases from 0.33 (baseline) to 0.51--0.58 (Appendix~\ref{sec:appendix_ssr}), confirming that among task-completing episodes, a larger fraction avoids collisions after fine-tuning.
31	
32	\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
33	Increasing $\lambda$ by 20$\times$ to 0.1 yields CAR\,=\,58.25\%\,$\pm$\,0.35 at the 30K checkpoint (two of three seeds), above the null distribution (mean 54.6\%, $\sigma = 2.27$, $z = 2.27$, $p \approx 0.023$). This departure is suggestive but inconclusive at $n = 2$. A stepwise ablation across six checkpoints (16K--28K) shows no sustained trend (mean 55.3\%, within 0.3$\sigma$ of the null; Appendix~\ref{sec:appendix_stepwise}), and per-task CAR ordering at 30K remains identical to all other conditions (Figure~\ref{fig:lambda_car}). The response is thus dose-dependent: SDF is fully redundant at $\lambda \leq 0.01$ ($p > 0.1$), with a marginal signal at $\lambda = 0.1$ whose modest effect size (${\sim}$3.7\,pp) and limited sample preclude strong conclusions. Even at elevated $\lambda$, avoidance patterns remain driven by demonstration distribution rather than geometric supervision.
34	
35	\begin{figure}[t]
36	\centering
37	\includegraphics[width=0.85\linewidth]{fig5_lambda_curve}
38	\caption{Effect of SDF loss weight $\lambda$ on CAR and TSR. $\lambda = 0$: LoRA-only. Low $\lambda$ ($\leq 0.01$) remains within the null band; $\lambda = 0.1$ (58.25\%, 2 seeds) shows a marginal departure ($p \approx 0.023$) whose per-task pattern still matches the demonstration distribution.}
39	\label{fig:lambda_car}
40	\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "4df495bd-6fae-48f8-a86a-5b2c2558725c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
      "content": "\\section{Avoidance Source Diagnosis}\\label{sec:avoidance_source}\n\nFine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\\sim}$28 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only, LoRA+SDF ($\\lambda = 0.005$), and LoRA+SDF ($\\lambda = 0.01$) on Pi0.5, all evaluated at the 30K-step checkpoint.\n\n\\begin{table}[t]\n\\centering\n\\caption{Avoidance source attribution on SafeLIBERO. SDF at $\\lambda \\leq 0.01$ adds no measurable CAR beyond LoRA-only ($p > 0.1$); $\\lambda = 0.1$ shows a marginal signal ($z = 2.27$, $p \\approx 0.023$, $n{=}2$) that requires additional seeds. All fine-tuned models exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\n\\label{tab:avoidance_source}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Seeds & TSR (\\%) & CAR (\\%) & EE Disp (m) \\\\\n\\midrule\nPi0.5 baseline & 3 & 74.7\\,$\\pm$\\,1.5 & 26.8\\,$\\pm$\\,1.6 & 0.367 \\\\\n\\midrule\nLoRA-only (no SDF) & 2 & 48.75 & 54.75\\,$\\pm$\\,3.18 & 0.392 \\\\\nLoRA+SDF $\\lambda{=}0.005$ & 3 & 54.0\\,$\\pm$\\,3.0 & 54.5\\,$\\pm$\\,2.29 & 0.387 \\\\\nLoRA+SDF $\\lambda{=}0.01$ & 3 & 53.8\\,$\\pm$\\,1.5 & 56.33\\,$\\pm$\\,1.61 & 0.389 \\\\\nLoRA+SDF $\\lambda{=}0.1$\\textsuperscript{$\\dagger$} & 2 & 48.0\\,$\\pm$\\,1.4 & 58.25\\,$\\pm$\\,0.35 & 0.394 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\footnotesize \\textsuperscript{$\\dagger$}30K checkpoint, two of three seeds; third seed in progress.}\n\\end{table}\n\nTable~\\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\\sim}$28 percentage points (26.8\\% $\\to$ 54.75\\%) with zero frozen episodes and displacement above 0.37\\,m, confirming genuine avoidance. Adding SDF supervision produces no measurable benefit: LoRA-only CAR (54.75\\%) is within 0.25\\,pp of $\\lambda = 0.005$ and statistically indistinguishable from $\\lambda = 0.01$ (56.33\\%, $p > 0.1$; Appendix~\\ref{sec:appendix_null}). A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,57.5\\%\\footnote{Single seed (s2); computational constraints precluded additional seeds for this ablation.}, confirming that SDF gradients produce no lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce lowest) and invariant to $\\lambda$ across a 20$\\times$ range, indicating that avoidance patterns reflect the demonstration distribution rather than geometric supervision.\n\n\\paragraph{CAR--TSR trade-off.}\\label{sec:tsr_collapse}\nFine-tuning degrades TSR by ${\\sim}$21--26\\,pp (74.7\\% $\\to$ 48.75--54.0\\%), reflecting distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\\,0.37\\,m displacement and 0\\% frozen episodes). The SSR/TSR ratio increases from 0.33 (baseline) to 0.51--0.58 (Appendix~\\ref{sec:appendix_ssr}), confirming that among task-completing episodes, a larger fraction avoids collisions after fine-tuning.\n\n\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\nIncreasing $\\lambda$ by 20$\\times$ to 0.1 yields CAR\\,=\\,58.25\\%\\,$\\pm$\\,0.35 at the 30K checkpoint (two of three seeds), above the null distribution (mean 54.6\\%, $\\sigma = 2.27$, $z = 2.27$, $p \\approx 0.023$). This departure is suggestive but inconclusive at $n = 2$. A stepwise ablation across six checkpoints (16K--28K) shows no sustained trend (mean 55.3\\%, within 0.3$\\sigma$ of the null; Appendix~\\ref{sec:appendix_stepwise}), and per-task CAR ordering at 30K remains identical to all other conditions (Figure~\\ref{fig:lambda_car}). The response is thus dose-dependent: SDF is fully redundant at $\\lambda \\leq 0.01$ ($p > 0.1$), with a marginal signal at $\\lambda = 0.1$ whose modest effect size (${\\sim}$3.7\\,pp) and limited sample preclude strong conclusions. Even at elevated $\\lambda$, avoidance patterns remain driven by demonstration distribution rather than geometric supervision.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{fig5_lambda_curve}\n\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. $\\lambda = 0$: LoRA-only. Low $\\lambda$ ($\\leq 0.01$) remains within the null band; $\\lambda = 0.1$ (58.25\\%, 2 seeds) shows a marginal departure ($p \\approx 0.023$) whose per-task pattern still matches the demonstration distribution.}\n\\label{fig:lambda_car}\n\\end{figure}",
      "numLines": 40,
      "startLine": 1,
      "totalLines": 40
    }
  }
}
```

</details>

---

### Tool call

_source line 208_

<details open><summary>🔧 Tool call — Read · `toolu_01Ks3dUDCr37KQdZHwGGb9o7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "c2afa639-5f57-4661-9e3d-d87d93fc1a33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nu58NnUyskUG3amJVmsHuR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 864,
      "cache_read_input_tokens": 32815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 864
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

_source line 209 · 2026-05-27T13:16:17.433Z_

<details><summary>↩ Tool result · `toolu_01Ks3dUDCr37KQdZHwGGb9o7`</summary>

```text
1	\section{Displacement Distribution}
2	\label{sec:appendix_displacement}
3	
4	\begin{figure}[h]
5	\centering
6	\includegraphics[width=\linewidth]{fig2_ee_displacement_distribution}
7	\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\,$\mu$m, while Pi0.5 episodes (orange) exceed 200\,mm. The five-order-of-magnitude gap makes $\tau_d$ robust to any value in $[2, 200]$\,mm.}
8	\label{fig:displacement}
9	\end{figure}
10	
11	\section{Displacement Threshold Sensitivity Analysis}
12	\label{sec:appendix_threshold}
13	
14	To validate the robustness of our displacement threshold $\tau_d$, we evaluate the frozen rate across four orders of magnitude. Table~\ref{tab:threshold_sensitivity} shows that the fake safety pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\% frozen rate even at the most conservative setting.
15	
16	\begin{table}[h]
17	\centering
18	\caption{Frozen rate (\% of episodes with $d_\mathrm{max} < \tau_d$) across threshold values.}
19	\label{tab:threshold_sensitivity}
20	\begin{tabular}{lccc}
21	\toprule
22	$\tau_d$ & A1-LoRA (Pi0) & Pi0.5 Baseline & Pi0.5+A1 (SDF aux) \\
23	\midrule
24	0.001 mm (1\,$\mu$m) & 73.9 & 0.0 & 0.0 \\
25	0.1 mm  & 99.6 & 0.0 & 0.0 \\
26	1.0 mm  & 100.0 & 0.0 & 0.0 \\
27	10 mm   & 100.0 & 0.0 & 0.0 \\
28	\bottomrule
29	\end{tabular}
30	\end{table}
31	
32	The choice of $\tau_d = 0.1$\,mm represents a conservative threshold: displacement below this value is physically negligible in manipulation tasks where typical action magnitudes are 1--10\,mm per step. Even at $\tau_d = 1$\,$\mu$m, 73.9\% of A1-LoRA safe episodes are classified as frozen, while all Pi0.5 episodes remain above threshold at every level tested.
33	
34	Table~\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\tau_d \in [2, 200]$\,mm. At $\tau_d = 300$\,mm, 0--2 episodes per seed fall below threshold (displacement 200--300\,mm), causing $\leq$0.5\,pp deviation. Our conclusions hold across the entire tested range.
35	
36	\begin{table}[h]
37	\centering
38	\caption{dfCAR (\%) across displacement thresholds for fine-tuned Pi0.5 configurations ($n = 200$ episodes per seed). Values are identical across $\tau_d \in [2, 200]$\,mm; at $\tau_d = 300$\,mm, at most 2 episodes are excluded.}
39	\label{tab:dfcar_threshold}
40	\vspace{2pt}
41	\footnotesize
42	\begin{tabular}{lcccccccc}
43	\toprule
44	& \multicolumn{8}{c}{$\tau_d$ (mm)} \\
45	\cmidrule(lr){2-9}
46	Condition & 2 & 5 & 10 & 20 & 50 & 100 & 200 & 300 \\
47	\midrule
48	LoRA s0            & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\
49	LoRA s1            & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 \\
50	SDF $\lambda{=}0.005$ s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.1 \\
51	SDF $\lambda{=}0.005$ s1 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 \\
52	SDF $\lambda{=}0.005$ s2 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.3 \\
53	SDF $\lambda{=}0.01$ s0  & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\
54	SDF $\lambda{=}0.01$ s1  & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.1 \\
55	SDF $\lambda{=}0.01$ s2  & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.0 \\
56	\bottomrule
57	\end{tabular}
58	\end{table}
59	
60	
61	\section{Per-Task TSR Breakdown}\label{sec:appendix_tsr_pertask}
62	
63	Table~\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.
64	
65	\begin{table}[h]
66	\centering
67	\caption{Per-task TSR (\%) at 30K training steps. LoRA-only reports seed~0 (rotation-fixed re-evaluation); SDF conditions report 3-seed means.}
68	\label{tab:per_task_tsr}
69	\vspace{2pt}
70	\small
71	\begin{tabular}{lcccc}
72	\toprule
73	Task & Pi0.5 Base & LoRA-only\textsuperscript{$\dagger$} & SDF $\lambda{=}0.005$ & SDF $\lambda{=}0.01$ \\
74	 & (3 seeds) & (seed 0) & (3 seeds) & (3 seeds) \\
75	\midrule
76	Orange Juice      & 70.7 & 18.0 & 33.3 & 24.7 \\
77	Choco.\ Pudding   & 86.0 & 72.0 & 78.0 & 76.7 \\
78	Milk              & 66.0 & 32.0 & 35.3 & 48.7 \\
79	BBQ Sauce         & 76.0 & 62.0 & 69.3 & 65.3 \\
80	\midrule
81	Mean              & 74.7 & 46.0 & 54.0 & 53.8 \\
82	\bottomrule
83	\end{tabular}
84	\vspace{1pt}
85	{\footnotesize \textsuperscript{$\dagger$}Rotation-fixed re-evaluation; seed-1 evaluated with original rotation protocol, excluded to avoid mixing evaluation conditions.}
86	\end{table}
87	
88	\section{Safe Success Rate Analysis}\label{sec:appendix_ssr}
89	
90	Table~\ref{tab:ssr} reports the Safe Success Rate (SSR\,=\,TSR\,$\cap$\,CAR), the fraction of episodes achieving both task completion and collision avoidance. The SSR/TSR ratio quantifies the proportion of successful episodes that are also collision-free, controlling for task-completion rate.
91	
92	\begin{table}[h]
93	\centering
94	\caption{SSR and SSR/TSR ratio across conditions. The ratio increase from 0.33 (baseline) to 0.51--0.58 (fine-tuned) indicates that CAR gains reflect learned safer execution, not reduced task exposure.}
95	\label{tab:ssr}
96	\vspace{2pt}
97	\small
98	\begin{tabular}{lcccc}
99	\toprule
100	Condition & TSR (\%) & CAR (\%) & SSR (\%) & SSR/TSR \\
101	\midrule
102	Pi0.5 baseline & 74.7 & 26.8 & 25.0\textsuperscript{a} & 0.33 \\
103	LoRA-only (2 seeds) & 48.75 & 54.75 & 28.3 & 0.58 \\
104	SDF $\lambda{=}0.005$ (3 seeds) & 54.0 & 54.5 & 27.8 & 0.51 \\
105	SDF $\lambda{=}0.01$ (3 seeds) & 53.8 & 56.33 & 30.2 & 0.56 \\
106	SDF $\lambda{=}0.1$\textsuperscript{$\dagger$} & 48.0 & 58.25 & 26.5 & 0.55 \\
107	\bottomrule
108	\end{tabular}
109	\vspace{1pt}
110	{\footnotesize \textsuperscript{a}Estimated; per-episode overlap unavailable for 3-seed rotation-corrected protocol. \textsuperscript{$\dagger$}SSR from seed~1 only; seed~0 per-episode data overwritten.}
111	\end{table}
112	
113	\section{Per-Task Oracle Analysis}
114	\label{sec:appendix_pertask}
115	\label{sec:appendix_pertask_oracle}
116	
117	Table~\ref{tab:oracle_pertask} shows per-task CAR for oracle refinement. On task~1 (\texttt{chocolate\_pudding}), where the EE is the primary collision body and the LoRA baseline achieves only 46.0\% CAR, Oracle-adaptive improves to 55.0\% and Oracle-feature to 47.5\%. On the remaining tasks, all oracle variants degrade: Oracle-adaptive reduces task~0 (\texttt{orange\_juice}) from 96.0\% to 82.5\% and task~2 (\texttt{milk}) from 98.0\% to 77.5\%. The SDF gradient pushes the EE away from the nearest surface, but the resulting joint-space displacement rotates intermediate arm links into obstacle volumes.
118	
119	The feature-space oracle fires on nearly every timestep (241.7 refinements/episode vs.\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\ 0.18--0.49), and CAR (76.9\%) shows no advantage despite 17$\times$ more steps. The A3 learned SDF never triggers refinement (0 steps/episode), as its outputs avoid the activation threshold.
120	
121	\begin{table}[h]
122	\centering
123	\caption{Per-task CAR (\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another.}
124	\label{tab:oracle_pertask}
125	\vspace{2pt}
126	\small
127	\begin{tabular}{lccccc}
128	\toprule
129	Method & Task 0 & Task 1 & Task 2 & Task 3 & Agg. \\
130	\midrule
131	LoRA baseline & 96.0 & 46.0 & 98.0 & 88.0 & 82.0 \\
132	\midrule
133	Oracle-adaptive & 82.5 & 55.0 & 77.5 & 85.0 & 75.0 \\
134	Oracle-fixed & 85.0 & 50.0 & 77.5 & 80.0 & 73.1 \\
135	Oracle-feature & 90.0 & 47.5 & 82.5 & 87.5 & 76.9 \\
136	\bottomrule
137	\end{tabular}
138	\end{table}
139	
140	
141	\section{Null Distribution for SDF Loss Weight Analysis}
142	\label{sec:appendix_null}
143	
144	We construct a null distribution by pooling the two LoRA-only seeds and three $\lambda = 0.005$ seeds into five per-seed CAR measurements: 57.0\% (LoRA s0, re-evaluated), 52.5\% (LoRA s1), 57.0\% ($\lambda{=}0.005$ s0), 54.0\% ($\lambda{=}0.005$ s1), 52.5\% ($\lambda{=}0.005$ s2), yielding mean 54.6\% and standard deviation 2.27\%. We treat these as exchangeable because SDF at $\lambda = 0.005$ produces no separation from LoRA-only. The $\lambda = 0.01$ mean of 56.33\% falls within $0.8\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect. The $\lambda = 0.1$ 30K mean of 58.25\% (2 seeds) yields $z = 2.27$ ($p \approx 0.023$), a marginal departure whose interpretation is limited by $n = 2$.
145	
146	A Phase~2 ablation reinforces this conclusion. Setting $\lambda = 0$ during Phase~2 (steps 5K--30K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\% (single seed, s2). This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.
147	
148	\section{Step-wise Checkpoint Analysis for \texorpdfstring{$\lambda = 0.1$}{lambda = 0.1}}
149	\label{sec:appendix_stepwise}
150	
151	Table~\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\lambda = 0.1$. Seed-1 data is available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only. The seed-0 curve shows no monotonic trend through 28K; the 30K checkpoint marks the first consistent dual-seed departure from the null band, though whether this reflects a genuine late-training effect or sampling variance at $n = 2$ remains open.
152	
153	\begin{table}[h]
154	\centering
155	\caption{Per-seed CAR (\%) at training checkpoints for $\lambda = 0.1$ (200 episodes each). 24K--28K: seed-0 only. Dual-seed means remain within the null band (54.6\%\,$\pm$\,2.27\%) at all checkpoints except 30K, where both seeds depart marginally ($z = 2.27$, $p \approx 0.023$).}
156	\label{tab:stepwise_lambda01}
157	\vspace{2pt}
158	\small
159	\begin{tabular}{lccc}
160	\toprule
161	Checkpoint & Seed 0 & Seed 1 & Mean \\
162	\midrule
163	16K steps & 55.5 & 56.0 & 55.75 \\
164	20K steps & 55.0 & 56.0 & 55.5 \\
165	22K steps & 60.5 & 56.5 & 58.5 \\
166	24K steps & 52.5 & -- & -- \\
167	26K steps & 53.5 & -- & -- \\
168	28K steps & 54.5 & -- & -- \\
169	30K steps & 58.0 & 58.5 & 58.25 \\
170	\bottomrule
171	\end{tabular}
172	\end{table}
173	
174	Individual seeds exhibit checkpoint-to-checkpoint CAR fluctuations of up to 8\,pp (seed~0: 52.5--60.5\%), larger than the cross-seed standard deviation at any fixed checkpoint ($\leq$2.8\,pp). This is consistent with binomial sampling noise at $n = 50$ episodes per task ($\sigma \approx 7$\,pp per task for $p \approx 0.5$). The seed-averaged curve shows no monotonic trend, confirming that SDF loss weight does not produce a progressive training signal.
175	
176	
177	\section{Oracle SDF Refinement Details}
178	\label{sec:appendix_oracle}
179	
180	All oracle variants replace the learned SDF decoder with ground-truth distance fields computed from the simulation geometry. Each is evaluated for 160 episodes (4 tasks $\times$ 40).
181	
182	\paragraph{Oracle-adaptive.} At each timestep, if the ground-truth SDF at the end-effector position falls below a safety margin, the action is adjusted by a step in the negative SDF gradient direction. The step size $\alpha$ is scaled inversely with distance: smaller distances produce larger corrections. This mimics an adaptive potential field controller.
183	
184	\paragraph{Oracle-fixed.} Identical to Oracle-adaptive except the step size is fixed at $\alpha = 0.005$ regardless of distance. This isolates the effect of step-size adaptation from the refinement geometry.
185	
186	\paragraph{Oracle-feature.} Instead of modifying the action directly in Cartesian space, this variant applies the SDF gradient in the policy's latent feature space via backpropagation. The gradient of the ground-truth SDF value with respect to the intermediate features is computed and used to perturb the features before the action head decodes them. This tests whether geometric corrections are more effective when applied in the model's learned representation space. In practice, the feature-space variant fires on nearly every timestep (241.7 refinements per episode vs.\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\ 0.18--0.49 in action space).
187	
188	
189	\section{Training Details}
190	\label{sec:appendix_training}
191	
192	\paragraph{Architecture.}
193	We use LoRA~\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\alpha$=16) and the action expert (rank 32, $\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\to$ 256 $\to$ 3).
194	
195	\paragraph{Training schedule.}
196	Training proceeds in two phases:
197	\begin{itemize}
198	    \item \textbf{Phase 1} (steps 0--5000): Backbone and LoRA parameters are frozen. Only the SDF decoder and EE extractor are trained, allowing them to learn meaningful representations before the policy adapts.
199	    \item \textbf{Phase 2} (steps 5000--30000): LoRA parameters are unfrozen with a 100-step gradient warmup ramp. All auxiliary heads continue training jointly with the policy.
200	\end{itemize}
201	
202	\paragraph{Hyperparameters.}
203	\begin{table}[h]
204	\centering
205	\caption{Training hyperparameters.}
206	\label{tab:hyperparams}
207	\begin{tabular}{ll}
208	\toprule
209	Parameter & Value \\
210	\midrule
211	Base model & Pi0.5 (OpenPi, $\sim$3.5B parameters) \\
212	Optimizer & AdamW \\
213	Learning rate & $2.5 \times 10^{-5}$ (cosine decay to $\mathrm{lr}/10$) \\
214	Warmup steps & 1000 \\
215	Batch size & 32 \\
216	Total steps & 30000 \\
217	$\lambda_\mathrm{sdf}$ & \{0.005, 0.01, 0.1\} \\
218	$\lambda_\mathrm{ee}$ & 0.01 \\
219	SDF query points per step & 64 \\
220	SDF clamp $\delta$ & 0.05 m \\
221	Eikonal weight & 0.1 \\
222	LoRA rank (vision) & 16 \\
223	LoRA rank (action) & 32 \\
224	Phase 1 duration & 5000 steps \\
225	\bottomrule
226	\end{tabular}
227	\end{table}
228	
229	\paragraph{Evaluation protocol.}
230	Each episode runs for at most 300 timesteps. The policy generates a 50-step action trajectory via flow matching and executes the first 5 steps before replanning. An episode terminates early upon task completion. Collision detection uses MuJoCo's built-in contact detection: any contact between the robot and a non-target object registers as a collision. For Pi0.5 evaluations, camera images are rotated 180$^\circ$ to match the pre-training viewpoint convention; this correction was verified to restore TSR from ${\sim}$5\% to ${\sim}$52\% while leaving CAR comparable. Oracle variants use 40 episodes per task (160 total) with a single seed; all other configurations use 50 episodes per task (200 total).
231	
232	\paragraph{Data.}
233	We use the SafeLIBERO object\_pudding suite with pre-computed SDF ground truth. SDF values are computed offline from the obstacle mesh using a dense $64^3$ voxel grid. During training, 64 query points are randomly sampled per step from this grid.
234	
235	\paragraph{Computational resources.}
236	All training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.
237	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "863264d9-0fe3-40c0-9cc7-fa2952fe1c19",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
      "content": "\\section{Displacement Distribution}\n\\label{sec:appendix_displacement}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{fig2_ee_displacement_distribution}\n\\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\\,$\\mu$m, while Pi0.5 episodes (orange) exceed 200\\,mm. The five-order-of-magnitude gap makes $\\tau_d$ robust to any value in $[2, 200]$\\,mm.}\n\\label{fig:displacement}\n\\end{figure}\n\n\\section{Displacement Threshold Sensitivity Analysis}\n\\label{sec:appendix_threshold}\n\nTo validate the robustness of our displacement threshold $\\tau_d$, we evaluate the frozen rate across four orders of magnitude. Table~\\ref{tab:threshold_sensitivity} shows that the fake safety pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\\% frozen rate even at the most conservative setting.\n\n\\begin{table}[h]\n\\centering\n\\caption{Frozen rate (\\% of episodes with $d_\\mathrm{max} < \\tau_d$) across threshold values.}\n\\label{tab:threshold_sensitivity}\n\\begin{tabular}{lccc}\n\\toprule\n$\\tau_d$ & A1-LoRA (Pi0) & Pi0.5 Baseline & Pi0.5+A1 (SDF aux) \\\\\n\\midrule\n0.001 mm (1\\,$\\mu$m) & 73.9 & 0.0 & 0.0 \\\\\n0.1 mm  & 99.6 & 0.0 & 0.0 \\\\\n1.0 mm  & 100.0 & 0.0 & 0.0 \\\\\n10 mm   & 100.0 & 0.0 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe choice of $\\tau_d = 0.1$\\,mm represents a conservative threshold: displacement below this value is physically negligible in manipulation tasks where typical action magnitudes are 1--10\\,mm per step. Even at $\\tau_d = 1$\\,$\\mu$m, 73.9\\% of A1-LoRA safe episodes are classified as frozen, while all Pi0.5 episodes remain above threshold at every level tested.\n\nTable~\\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\\tau_d \\in [2, 200]$\\,mm. At $\\tau_d = 300$\\,mm, 0--2 episodes per seed fall below threshold (displacement 200--300\\,mm), causing $\\leq$0.5\\,pp deviation. Our conclusions hold across the entire tested range.\n\n\\begin{table}[h]\n\\centering\n\\caption{dfCAR (\\%) across displacement thresholds for fine-tuned Pi0.5 configurations ($n = 200$ episodes per seed). Values are identical across $\\tau_d \\in [2, 200]$\\,mm; at $\\tau_d = 300$\\,mm, at most 2 episodes are excluded.}\n\\label{tab:dfcar_threshold}\n\\vspace{2pt}\n\\footnotesize\n\\begin{tabular}{lcccccccc}\n\\toprule\n& \\multicolumn{8}{c}{$\\tau_d$ (mm)} \\\\\n\\cmidrule(lr){2-9}\nCondition & 2 & 5 & 10 & 20 & 50 & 100 & 200 & 300 \\\\\n\\midrule\nLoRA s0            & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\\\\nLoRA s1            & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 \\\\\nSDF $\\lambda{=}0.005$ s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.1 \\\\\nSDF $\\lambda{=}0.005$ s1 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 \\\\\nSDF $\\lambda{=}0.005$ s2 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.3 \\\\\nSDF $\\lambda{=}0.01$ s0  & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\\\\nSDF $\\lambda{=}0.01$ s1  & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.1 \\\\\nSDF $\\lambda{=}0.01$ s2  & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Per-Task TSR Breakdown}\\label{sec:appendix_tsr_pertask}\n\nTable~\\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task TSR (\\%) at 30K training steps. LoRA-only reports seed~0 (rotation-fixed re-evaluation); SDF conditions report 3-seed means.}\n\\label{tab:per_task_tsr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTask & Pi0.5 Base & LoRA-only\\textsuperscript{$\\dagger$} & SDF $\\lambda{=}0.005$ & SDF $\\lambda{=}0.01$ \\\\\n & (3 seeds) & (seed 0) & (3 seeds) & (3 seeds) \\\\\n\\midrule\nOrange Juice      & 70.7 & 18.0 & 33.3 & 24.7 \\\\\nChoco.\\ Pudding   & 86.0 & 72.0 & 78.0 & 76.7 \\\\\nMilk              & 66.0 & 32.0 & 35.3 & 48.7 \\\\\nBBQ Sauce         & 76.0 & 62.0 & 69.3 & 65.3 \\\\\n\\midrule\nMean              & 74.7 & 46.0 & 54.0 & 53.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\footnotesize \\textsuperscript{$\\dagger$}Rotation-fixed re-evaluation; seed-1 evaluated with original rotation protocol, excluded to avoid mixing evaluation conditions.}\n\\end{table}\n\n\\section{Safe Success Rate Analysis}\\label{sec:appendix_ssr}\n\nTable~\\ref{tab:ssr} reports the Safe Success Rate (SSR\\,=\\,TSR\\,$\\cap$\\,CAR), the fraction of episodes achieving both task completion and collision avoidance. The SSR/TSR ratio quantifies the proportion of successful episodes that are also collision-free, controlling for task-completion rate.\n\n\\begin{table}[h]\n\\centering\n\\caption{SSR and SSR/TSR ratio across conditions. The ratio increase from 0.33 (baseline) to 0.51--0.58 (fine-tuned) indicates that CAR gains reflect learned safer execution, not reduced task exposure.}\n\\label{tab:ssr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & TSR (\\%) & CAR (\\%) & SSR (\\%) & SSR/TSR \\\\\n\\midrule\nPi0.5 baseline & 74.7 & 26.8 & 25.0\\textsuperscript{a} & 0.33 \\\\\nLoRA-only (2 seeds) & 48.75 & 54.75 & 28.3 & 0.58 \\\\\nSDF $\\lambda{=}0.005$ (3 seeds) & 54.0 & 54.5 & 27.8 & 0.51 \\\\\nSDF $\\lambda{=}0.01$ (3 seeds) & 53.8 & 56.33 & 30.2 & 0.56 \\\\\nSDF $\\lambda{=}0.1$\\textsuperscript{$\\dagger$} & 48.0 & 58.25 & 26.5 & 0.55 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\footnotesize \\textsuperscript{a}Estimated; per-episode overlap unavailable for 3-seed rotation-corrected protocol. \\textsuperscript{$\\dagger$}SSR from seed~1 only; seed~0 per-episode data overwritten.}\n\\end{table}\n\n\\section{Per-Task Oracle Analysis}\n\\label{sec:appendix_pertask}\n\\label{sec:appendix_pertask_oracle}\n\nTable~\\ref{tab:oracle_pertask} shows per-task CAR for oracle refinement. On task~1 (\\texttt{chocolate\\_pudding}), where the EE is the primary collision body and the LoRA baseline achieves only 46.0\\% CAR, Oracle-adaptive improves to 55.0\\% and Oracle-feature to 47.5\\%. On the remaining tasks, all oracle variants degrade: Oracle-adaptive reduces task~0 (\\texttt{orange\\_juice}) from 96.0\\% to 82.5\\% and task~2 (\\texttt{milk}) from 98.0\\% to 77.5\\%. The SDF gradient pushes the EE away from the nearest surface, but the resulting joint-space displacement rotates intermediate arm links into obstacle volumes.\n\nThe feature-space oracle fires on nearly every timestep (241.7 refinements/episode vs.\\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49), and CAR (76.9\\%) shows no advantage despite 17$\\times$ more steps. The A3 learned SDF never triggers refinement (0 steps/episode), as its outputs avoid the activation threshold.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another.}\n\\label{tab:oracle_pertask}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Task 0 & Task 1 & Task 2 & Task 3 & Agg. \\\\\n\\midrule\nLoRA baseline & 96.0 & 46.0 & 98.0 & 88.0 & 82.0 \\\\\n\\midrule\nOracle-adaptive & 82.5 & 55.0 & 77.5 & 85.0 & 75.0 \\\\\nOracle-fixed & 85.0 & 50.0 & 77.5 & 80.0 & 73.1 \\\\\nOracle-feature & 90.0 & 47.5 & 82.5 & 87.5 & 76.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Null Distribution for SDF Loss Weight Analysis}\n\\label{sec:appendix_null}\n\nWe construct a null distribution by pooling the two LoRA-only seeds and three $\\lambda = 0.005$ seeds into five per-seed CAR measurements: 57.0\\% (LoRA s0, re-evaluated), 52.5\\% (LoRA s1), 57.0\\% ($\\lambda{=}0.005$ s0), 54.0\\% ($\\lambda{=}0.005$ s1), 52.5\\% ($\\lambda{=}0.005$ s2), yielding mean 54.6\\% and standard deviation 2.27\\%. We treat these as exchangeable because SDF at $\\lambda = 0.005$ produces no separation from LoRA-only. The $\\lambda = 0.01$ mean of 56.33\\% falls within $0.8\\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect. The $\\lambda = 0.1$ 30K mean of 58.25\\% (2 seeds) yields $z = 2.27$ ($p \\approx 0.023$), a marginal departure whose interpretation is limited by $n = 2$.\n\nA Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--30K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\\% (single seed, s2). This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.\n\n\\section{Step-wise Checkpoint Analysis for \\texorpdfstring{$\\lambda = 0.1$}{lambda = 0.1}}\n\\label{sec:appendix_stepwise}\n\nTable~\\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\\lambda = 0.1$. Seed-1 data is available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only. The seed-0 curve shows no monotonic trend through 28K; the 30K checkpoint marks the first consistent dual-seed departure from the null band, though whether this reflects a genuine late-training effect or sampling variance at $n = 2$ remains open.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed CAR (\\%) at training checkpoints for $\\lambda = 0.1$ (200 episodes each). 24K--28K: seed-0 only. Dual-seed means remain within the null band (54.6\\%\\,$\\pm$\\,2.27\\%) at all checkpoints except 30K, where both seeds depart marginally ($z = 2.27$, $p \\approx 0.023$).}\n\\label{tab:stepwise_lambda01}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nCheckpoint & Seed 0 & Seed 1 & Mean \\\\\n\\midrule\n16K steps & 55.5 & 56.0 & 55.75 \\\\\n20K steps & 55.0 & 56.0 & 55.5 \\\\\n22K steps & 60.5 & 56.5 & 58.5 \\\\\n24K steps & 52.5 & -- & -- \\\\\n26K steps & 53.5 & -- & -- \\\\\n28K steps & 54.5 & -- & -- \\\\\n30K steps & 58.0 & 58.5 & 58.25 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIndividual seeds exhibit checkpoint-to-checkpoint CAR fluctuations of up to 8\\,pp (seed~0: 52.5--60.5\\%), larger than the cross-seed standard deviation at any fixed checkpoint ($\\leq$2.8\\,pp). This is consistent with binomial sampling noise at $n = 50$ episodes per task ($\\sigma \\approx 7$\\,pp per task for $p \\approx 0.5$). The seed-averaged curve shows no monotonic trend, confirming that SDF loss weight does not produce a progressive training signal.\n\n\n\\section{Oracle SDF Refinement Details}\n\\label{sec:appendix_oracle}\n\nAll oracle variants replace the learned SDF decoder with ground-truth distance fields computed from the simulation geometry. Each is evaluated for 160 episodes (4 tasks $\\times$ 40).\n\n\\paragraph{Oracle-adaptive.} At each timestep, if the ground-truth SDF at the end-effector position falls below a safety margin, the action is adjusted by a step in the negative SDF gradient direction. The step size $\\alpha$ is scaled inversely with distance: smaller distances produce larger corrections. This mimics an adaptive potential field controller.\n\n\\paragraph{Oracle-fixed.} Identical to Oracle-adaptive except the step size is fixed at $\\alpha = 0.005$ regardless of distance. This isolates the effect of step-size adaptation from the refinement geometry.\n\n\\paragraph{Oracle-feature.} Instead of modifying the action directly in Cartesian space, this variant applies the SDF gradient in the policy's latent feature space via backpropagation. The gradient of the ground-truth SDF value with respect to the intermediate features is computed and used to perturb the features before the action head decodes them. This tests whether geometric corrections are more effective when applied in the model's learned representation space. In practice, the feature-space variant fires on nearly every timestep (241.7 refinements per episode vs.\\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49 in action space).\n\n\n\\section{Training Details}\n\\label{sec:appendix_training}\n\n\\paragraph{Architecture.}\nWe use LoRA~\\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\\alpha$=16) and the action expert (rank 32, $\\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\\to$ 256 $\\to$ 3).\n\n\\paragraph{Training schedule.}\nTraining proceeds in two phases:\n\\begin{itemize}\n    \\item \\textbf{Phase 1} (steps 0--5000): Backbone and LoRA parameters are frozen. Only the SDF decoder and EE extractor are trained, allowing them to learn meaningful representations before the policy adapts.\n    \\item \\textbf{Phase 2} (steps 5000--30000): LoRA parameters are unfrozen with a 100-step gradient warmup ramp. All auxiliary heads continue training jointly with the policy.\n\\end{itemize}\n\n\\paragraph{Hyperparameters.}\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\label{tab:hyperparams}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & Pi0.5 (OpenPi, $\\sim$3.5B parameters) \\\\\nOptimizer & AdamW \\\\\nLearning rate & $2.5 \\times 10^{-5}$ (cosine decay to $\\mathrm{lr}/10$) \\\\\nWarmup steps & 1000 \\\\\nBatch size & 32 \\\\\nTotal steps & 30000 \\\\\n$\\lambda_\\mathrm{sdf}$ & \\{0.005, 0.01, 0.1\\} \\\\\n$\\lambda_\\mathrm{ee}$ & 0.01 \\\\\nSDF query points per step & 64 \\\\\nSDF clamp $\\delta$ & 0.05 m \\\\\nEikonal weight & 0.1 \\\\\nLoRA rank (vision) & 16 \\\\\nLoRA rank (action) & 32 \\\\\nPhase 1 duration & 5000 steps \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Evaluation protocol.}\nEach episode runs for at most 300 timesteps. The policy generates a 50-step action trajectory via flow matching and executes the first 5 steps before replanning. An episode terminates early upon task completion. Collision detection uses MuJoCo's built-in contact detection: any contact between the robot and a non-target object registers as a collision. For Pi0.5 evaluations, camera images are rotated 180$^\\circ$ to match the pre-training viewpoint convention; this correction was verified to restore TSR from ${\\sim}$5\\% to ${\\sim}$52\\% while leaving CAR comparable. Oracle variants use 40 episodes per task (160 total) with a single seed; all other configurations use 50 episodes per task (200 total).\n\n\\paragraph{Data.}\nWe use the SafeLIBERO object\\_pudding suite with pre-computed SDF ground truth. SDF values are computed offline from the obstacle mesh using a dense $64^3$ voxel grid. During training, 64 query points are randomly sampled per step from this grid.\n\n\\paragraph{Computational resources.}\nAll training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.\n",
      "numLines": 237,
      "startLine": 1,
      "totalLines": 237
    }
  }
}
```

</details>

---

### Tool call

_source line 210_

<details open><summary>🔧 Tool call — Read · `toolu_01MxCyG16LVcF1nGw6gZosEF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "866fb79b-091f-47da-97a9-68b6a9434c8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nu58NnUyskUG3amJVmsHuR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 864,
      "cache_read_input_tokens": 32815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 864
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

_source line 211 · 2026-05-27T13:16:17.565Z_

<details><summary>↩ Tool result · `toolu_01MxCyG16LVcF1nGw6gZosEF`</summary>

```text
1	\begin{abstract}
2	Vision-Language-Action (VLA) models report high Collision Avoidance Rates (CAR) on safety benchmarks, yet we show these metrics are contaminated by action collapse.
3	On SafeLIBERO, an SDF-augmented Pi0 achieves 91.5\% CAR while 99.6\% of its safe episodes exhibit end-effector displacement below 0.1\,mm---the robot is frozen, not safe.
4	We present displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes, as a corrective metric; the bimodal displacement distribution makes it robust across a $[2, 200]$\,mm threshold range.
5	Our analysis further reveals that end-effector-only Signed Distance Field (SDF) supervision is neither necessary nor structurally sufficient for collision avoidance.
6	It is counterproductive at inference time: three ground-truth oracle variants all reduce dfCAR below unrefined baselines, as SDF gradients repelling the end-effector drive arm links into obstacles.
7	Its contribution during training is dose-dependent: LoRA-only fine-tuning raises dfCAR from 26.8\% to 54.75\%$\,\pm\,$3.18, matching SDF-augmented training at $\lambda{=}0.005$ (54.5\%$\,\pm\,$2.29) and $\lambda{=}0.01$ (56.33\%$\,\pm\,$1.61); at $\lambda{=}0.1$, two of three seeds show a marginal signal (58.25\%$\,\pm\,$0.35, $p{\approx}0.023$) whose per-task avoidance pattern still mirrors the demonstration distribution, requiring further investigation.
8	Per-task avoidance patterns remain identical across all conditions, indicating that collision avoidance arises from collision-free demonstration data rather than geometric supervision.
9	Displacement filtering is necessary for meaningful VLA safety evaluation; EE-only geometric supervision can be neither credited with nor expected to deliver collision avoidance.
10	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "8e32e04d-7316-4175-a61f-9063d5733e01",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nVision-Language-Action (VLA) models report high Collision Avoidance Rates (CAR) on safety benchmarks, yet we show these metrics are contaminated by action collapse.\nOn SafeLIBERO, an SDF-augmented Pi0 achieves 91.5\\% CAR while 99.6\\% of its safe episodes exhibit end-effector displacement below 0.1\\,mm---the robot is frozen, not safe.\nWe present displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes, as a corrective metric; the bimodal displacement distribution makes it robust across a $[2, 200]$\\,mm threshold range.\nOur analysis further reveals that end-effector-only Signed Distance Field (SDF) supervision is neither necessary nor structurally sufficient for collision avoidance.\nIt is counterproductive at inference time: three ground-truth oracle variants all reduce dfCAR below unrefined baselines, as SDF gradients repelling the end-effector drive arm links into obstacles.\nIts contribution during training is dose-dependent: LoRA-only fine-tuning raises dfCAR from 26.8\\% to 54.75\\%$\\,\\pm\\,$3.18, matching SDF-augmented training at $\\lambda{=}0.005$ (54.5\\%$\\,\\pm\\,$2.29) and $\\lambda{=}0.01$ (56.33\\%$\\,\\pm\\,$1.61); at $\\lambda{=}0.1$, two of three seeds show a marginal signal (58.25\\%$\\,\\pm\\,$0.35, $p{\\approx}0.023$) whose per-task avoidance pattern still mirrors the demonstration distribution, requiring further investigation.\nPer-task avoidance patterns remain identical across all conditions, indicating that collision avoidance arises from collision-free demonstration data rather than geometric supervision.\nDisplacement filtering is necessary for meaningful VLA safety evaluation; EE-only geometric supervision can be neither credited with nor expected to deliver collision avoidance.\n\\end{abstract}",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  }
}
```

</details>

---

### Assistant

_source line 212_

<details><summary>Logged reasoning block</summary>

```text
Now let me check the per-task CAR breakdown for s1_l01_high. The agent report mentioned it's not in the main paper. Let me also check if there's a per-task CAR table in the appendix or any other file. Let me also look for any data files that have the ground truth values.

Looking at what I have:

1. **s1 per-task numbers**: The main paper doesn't have a per-task breakdown for s1_l01_high. The appendix has a per-task TSR table (tab:per_task_tsr) but it reports LoRA-only seed 0 TSR values, not CAR per-task for s1_l01_high.


2. **LoRA Table row**: The LoRA-only results show 2 seeds with TSR=48.75 and CAR=54.75±3.18, which matches the checklist's reported mean. The appendix dfcar_threshold table confirms this with individual seed values of 57.0 and 52.5. This checks out.
3. **EE Disp**: The λ=0.1 configuration shows EE Disp=0.394 in the source file, and I'm verifying this against the checklist values.

Now I'm checking whether the 0.394 value is consistent with the per-seed data. The checklist shows s0_l01_high avg_max_ee=0.3884, and since 0.394 appears to be a 2-seed mean, this aligns reasonably well—averaging around 0.40 and 0.3884 gives approximately 0.394, though the exact value doesn't appear elsewhere in the paper.

4. **std consistency**: All the standard deviations across the different configurations match exactly between the source and abstract—54.75±3.18, 54.5±2.29, 56.33±1.61, 58.25±0.35. This is correct.

Now I'm cross-checking the per-task TSR breakdown in the appendix. The checklist lists s1_l01_high TSR values as OJ=26%, CP=80%, milk=28%, bbq=62%.

However, the appendix table shows LoRA-only seed 0 TSR values of OJ=18, CP=72, Milk=32, BBQ=62—these are for a different configuration than s1_l01_high. Looking at what s1 represents, the checklist references eval_pi05_a1_30k_s1_l01_high, which is λ=0.1 with seed 1 at high variance. The per-task CAR for this is OJ=66%, CP=72%, milk=70%, bbq=26%, but I don't see these per-task CAR values broken down by individual seeds for λ=0.1 in the main paper itself.

I'm now moving on to verify the dream reports.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "4a3b8cb2-b436-4e33-970f-b236f6d0215e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hwz8uUdKaTdfXCWU9tToHu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8746,
      "cache_read_input_tokens": 33679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8746
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

_source line 213_

Now let me check remaining data files for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "05e913fe-e60c-451f-9d07-d964420b19fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hwz8uUdKaTdfXCWU9tToHu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8746,
      "cache_read_input_tokens": 33679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8746
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

_source line 214_

<details open><summary>🔧 Tool call — Grep · `toolu_01M2UEkrot9SBir1G26mHRmN`</summary>

```json
{
  "pattern": "per.task.*CAR|CAR.*per.task|66.*72.*70|OJ.*66|CP.*72",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "c8cc6626-a717-4f96-9812-cd5d33d8bd90",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hwz8uUdKaTdfXCWU9tToHu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8746,
      "cache_read_input_tokens": 33679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8746
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

_source line 215 · 2026-05-27T13:16:42.786Z_

<details><summary>↩ Tool result · `toolu_01M2UEkrot9SBir1G26mHRmN`</summary>

```text
docs/paper/claim3.tex:27:[Omitted long matching line]
docs/paper/claim3.tex:33:[Omitted long matching line]
docs/paper/claim3.tex:38:\caption{Effect of SDF loss weight $\lambda$ on CAR and TSR. $\lambda = 0$: LoRA-only. Low $\lambda$ ($\leq 0.01$) remains within the null band; $\lambda = 0.1$ (58.25\%, 2 seeds) shows a marginal departure ($p \approx 0.023$) whose per-task pattern still matches the demonstration distribution.}
docs/paper/discussion.tex:6:[Omitted long matching line]
docs/paper/method.tex:5:[Omitted long matching line]
docs/paper/archive/analysis_claim2.tex:29:[Omitted long matching line]
docs/paper/archive/analysis_claim3.tex:26:[Omitted long matching line]
docs/paper/archive/analysis_claim4.tex:31:Per-task decomposition reveals heterogeneous improvement across workspace configurations. Tasks~0--2 show CAR gains of \placeholder{XX}--\placeholder{XX} percentage points over the Pi0.5 baseline, with TSR reductions of \placeholder{XX}--\placeholder{XX} points. Task~3 (\texttt{bbq\_sauce}) exhibits a distinct pattern discussed below. The non-uniform response across tasks suggests that SDF supervision interacts with workspace layout in ways that require per-task analysis.
docs/paper/claim2.tex:7:\caption{Oracle SDF refinement with ground-truth distance fields. All oracle variants achieve lower CAR than unrefined baselines. Per-task breakdown in Appendix~\ref{sec:appendix_pertask_oracle}.}
docs/paper/abstract.tex:7:Its contribution during training is dose-dependent: LoRA-only fine-tuning raises dfCAR from 26.8\% to 54.75\%$\,\pm\,$3.18, matching SDF-augmented training at $\lambda{=}0.005$ (54.5\%$\,\pm\,$2.29) and $\lambda{=}0.01$ (56.33\%$\,\pm\,$1.61); at $\lambda{=}0.1$, two of three seeds show a marginal signal (58.25\%$\,\pm\,$0.35, $p{\approx}0.023$) whose per-task avoidance pattern still mirrors the demonstration distribution, requiring further investigation.
docs/paper/appendix.tex:117:[Omitted long matching line]
docs/paper/appendix.tex:123:\caption{Per-task CAR (\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another.}
docs/paper/appendix.tex:174:Individual seeds exhibit checkpoint-to-checkpoint CAR fluctuations of up to 8\,pp (seed~0: 52.5--60.5\%), larger than the cross-seed standard deviation at any fixed checkpoint ($\leq$2.8\,pp). This is consistent with binomial sampling noise at $n = 50$ episodes per task ($\sigma \approx 7$\,pp per task for $p \approx 0.5$). The seed-averaged curve shows no monotonic trend, confirming that SDF loss weight does not produce a progressive training signal.
docs/paper/appendix.tex:230:[Omitted long matching line]
docs/paper/introduction.tex:20:[Omitted long matching line]
docs/paper/introduction.tex:27:    \item \textbf{Demonstration sufficiency:} on SafeLIBERO, collision-free demonstrations account for all measured CAR gains (${\sim}$28\,pp); EE-only SDF at low $\lambda$ ($\leq 0.01$) adds nothing, and at high $\lambda = 0.1$ shows only a marginal, inconclusive signal ($n = 2$) whose per-task pattern still matches the demonstration distribution.
docs/paper/main.aux:68:\@writefile{lot}{\contentsline {table}{\numberline {3}{\ignorespaces Oracle SDF refinement with ground-truth distance fields. All oracle variants achieve lower CAR than unrefined baselines. Per-task breakdown in Appendix~\ref {sec:appendix_pertask_oracle}.}}{5}{table.caption.10}\protected@file@percent }
docs/paper/main.aux:69:\newlabel{tab:oracle}{{3}{5}{Oracle SDF refinement with ground-truth distance fields. All oracle variants achieve lower CAR than unrefined baselines. Per-task breakdown in Appendix~\ref {sec:appendix_pertask_oracle}}{table.caption.10}{}}
docs/paper/main.aux:80:\@writefile{lof}{\contentsline {figure}{\numberline {4}{\ignorespaces Effect of SDF loss weight $\lambda $ on CAR and TSR. $\lambda = 0$: LoRA-only. Low $\lambda $ ($\leq 0.01$) remains within the null band; $\lambda = 0.1$ (58.25\%, 2 seeds) shows a marginal departure ($p \approx 0.023$) whose per-task pattern still matches the demonstration distribution.}}{7}{figure.caption.15}\protected@file@percent }
docs/paper/main.aux:81:\newlabel{fig:lambda_car}{{4}{7}{Effect of SDF loss weight $\lambda $ on CAR and TSR. $\lambda = 0$: LoRA-only. Low $\lambda $ ($\leq 0.01$) remains within the null band; $\lambda = 0.1$ (58.25\%, 2 seeds) shows a marginal departure ($p \approx 0.023$) whose per-task pattern still matches the demonstration distribution}{figure.caption.15}{}}
docs/paper/main.aux:141:\@writefile{lot}{\contentsline {table}{\numberline {9}{\ignorespaces Per-task CAR (\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another.}}{12}{table.caption.27}\protected@file@percent }
docs/paper/main.aux:142:\newlabel{tab:oracle_pertask}{{9}{12}{Per-task CAR (\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another}{table.caption.27}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "b9e5f965-c75b-4030-ad8a-0fe56b8fb2a5",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/claim3.tex:27:[Omitted long matching line]\ndocs/paper/claim3.tex:33:[Omitted long matching line]\ndocs/paper/claim3.tex:38:\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. $\\lambda = 0$: LoRA-only. Low $\\lambda$ ($\\leq 0.01$) remains within the null band; $\\lambda = 0.1$ (58.25\\%, 2 seeds) shows a marginal departure ($p \\approx 0.023$) whose per-task pattern still matches the demonstration distribution.}\ndocs/paper/discussion.tex:6:[Omitted long matching line]\ndocs/paper/method.tex:5:[Omitted long matching line]\ndocs/paper/archive/analysis_claim2.tex:29:[Omitted long matching line]\ndocs/paper/archive/analysis_claim3.tex:26:[Omitted long matching line]\ndocs/paper/archive/analysis_claim4.tex:31:Per-task decomposition reveals heterogeneous improvement across workspace configurations. Tasks~0--2 show CAR gains of \\placeholder{XX}--\\placeholder{XX} percentage points over the Pi0.5 baseline, with TSR reductions of \\placeholder{XX}--\\placeholder{XX} points. Task~3 (\\texttt{bbq\\_sauce}) exhibits a distinct pattern discussed below. The non-uniform response across tasks suggests that SDF supervision interacts with workspace layout in ways that require per-task analysis.\ndocs/paper/claim2.tex:7:\\caption{Oracle SDF refinement with ground-truth distance fields. All oracle variants achieve lower CAR than unrefined baselines. Per-task breakdown in Appendix~\\ref{sec:appendix_pertask_oracle}.}\ndocs/paper/abstract.tex:7:Its contribution during training is dose-dependent: LoRA-only fine-tuning raises dfCAR from 26.8\\% to 54.75\\%$\\,\\pm\\,$3.18, matching SDF-augmented training at $\\lambda{=}0.005$ (54.5\\%$\\,\\pm\\,$2.29) and $\\lambda{=}0.01$ (56.33\\%$\\,\\pm\\,$1.61); at $\\lambda{=}0.1$, two of three seeds show a marginal signal (58.25\\%$\\,\\pm\\,$0.35, $p{\\approx}0.023$) whose per-task avoidance pattern still mirrors the demonstration distribution, requiring further investigation.\ndocs/paper/appendix.tex:117:[Omitted long matching line]\ndocs/paper/appendix.tex:123:\\caption{Per-task CAR (\\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another.}\ndocs/paper/appendix.tex:174:Individual seeds exhibit checkpoint-to-checkpoint CAR fluctuations of up to 8\\,pp (seed~0: 52.5--60.5\\%), larger than the cross-seed standard deviation at any fixed checkpoint ($\\leq$2.8\\,pp). This is consistent with binomial sampling noise at $n = 50$ episodes per task ($\\sigma \\approx 7$\\,pp per task for $p \\approx 0.5$). The seed-averaged curve shows no monotonic trend, confirming that SDF loss weight does not produce a progressive training signal.\ndocs/paper/appendix.tex:230:[Omitted long matching line]\ndocs/paper/introduction.tex:20:[Omitted long matching line]\ndocs/paper/introduction.tex:27:    \\item \\textbf{Demonstration sufficiency:} on SafeLIBERO, collision-free demonstrations account for all measured CAR gains (${\\sim}$28\\,pp); EE-only SDF at low $\\lambda$ ($\\leq 0.01$) adds nothing, and at high $\\lambda = 0.1$ shows only a marginal, inconclusive signal ($n = 2$) whose per-task pattern still matches the demonstration distribution.\ndocs/paper/main.aux:68:\\@writefile{lot}{\\contentsline {table}{\\numberline {3}{\\ignorespaces Oracle SDF refinement with ground-truth distance fields. All oracle variants achieve lower CAR than unrefined baselines. Per-task breakdown in Appendix~\\ref {sec:appendix_pertask_oracle}.}}{5}{table.caption.10}\\protected@file@percent }\ndocs/paper/main.aux:69:\\newlabel{tab:oracle}{{3}{5}{Oracle SDF refinement with ground-truth distance fields. All oracle variants achieve lower CAR than unrefined baselines. Per-task breakdown in Appendix~\\ref {sec:appendix_pertask_oracle}}{table.caption.10}{}}\ndocs/paper/main.aux:80:\\@writefile{lof}{\\contentsline {figure}{\\numberline {4}{\\ignorespaces Effect of SDF loss weight $\\lambda $ on CAR and TSR. $\\lambda = 0$: LoRA-only. Low $\\lambda $ ($\\leq 0.01$) remains within the null band; $\\lambda = 0.1$ (58.25\\%, 2 seeds) shows a marginal departure ($p \\approx 0.023$) whose per-task pattern still matches the demonstration distribution.}}{7}{figure.caption.15}\\protected@file@percent }\ndocs/paper/main.aux:81:\\newlabel{fig:lambda_car}{{4}{7}{Effect of SDF loss weight $\\lambda $ on CAR and TSR. $\\lambda = 0$: LoRA-only. Low $\\lambda $ ($\\leq 0.01$) remains within the null band; $\\lambda = 0.1$ (58.25\\%, 2 seeds) shows a marginal departure ($p \\approx 0.023$) whose per-task pattern still matches the demonstration distribution}{figure.caption.15}{}}\ndocs/paper/main.aux:141:\\@writefile{lot}{\\contentsline {table}{\\numberline {9}{\\ignorespaces Per-task CAR (\\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another.}}{12}{table.caption.27}\\protected@file@percent }\ndocs/paper/main.aux:142:\\newlabel{tab:oracle_pertask}{{9}{12}{Per-task CAR (\\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another}{table.caption.27}{}}",
    "numLines": 22
  }
}
```

</details>

---

### Tool call

_source line 216_

<details open><summary>🔧 Tool call — Grep · `toolu_01GvTWn7UbwKvJ9HNyxbwn1A`</summary>

```json
{
  "pattern": "0\\.3884|0\\.0553|ee_disp|avg_max_ee",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "1d3eea4a-f692-4adb-b51d-95edc6f9f44f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hwz8uUdKaTdfXCWU9tToHu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8746,
      "cache_read_input_tokens": 33679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8746
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

_source line 217 · 2026-05-27T13:16:44.253Z_

<details><summary>↩ Tool result · `toolu_01GvTWn7UbwKvJ9HNyxbwn1A`</summary>

```text
docs/paper/main.fls:280:INPUT ../../artifacts/figures/fig2_ee_displacement_distribution.pdf
docs/paper/main.fls:281:INPUT ../../artifacts/figures/fig2_ee_displacement_distribution.pdf
docs/paper/main.fls:282:INPUT ../../artifacts/figures/fig2_ee_displacement_distribution.pdf
docs/paper/main.fls:283:INPUT ../../artifacts/figures/fig2_ee_displacement_distribution.pdf
docs/paper/main.log:567:<../../artifacts/figures/fig2_ee_displacement_distribution.pdf, id=491, 500.106
docs/paper/main.log:569:File: ../../artifacts/figures/fig2_ee_displacement_distribution.pdf Graphic fil
docs/paper/main.log:571:&lt;use ../../artifacts/figures/fig2_ee_displacement_distribution.pdf>
docs/paper/main.log:572:Package pdftex.def Info: ../../artifacts/figures/fig2_ee_displacement_distribut
docs/paper/main.log:579:[10 <../../artifacts/figures/fig2_ee_displacement_distribution.pdf>]
docs/paper/main.fdb_latexmk:12:  "../../artifacts/figures/fig2_ee_displacement_distribution.pdf" 1779802483.58778 96079 cdee19c8463e2117aa75565b00ea4a5a ""
docs/paper/appendix.tex:6:\includegraphics[width=\linewidth]{fig2_ee_displacement_distribution}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "d50f1ff6-266d-4a18-9126-b1a1401b1e0a",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/main.fls:280:INPUT ../../artifacts/figures/fig2_ee_displacement_distribution.pdf\ndocs/paper/main.fls:281:INPUT ../../artifacts/figures/fig2_ee_displacement_distribution.pdf\ndocs/paper/main.fls:282:INPUT ../../artifacts/figures/fig2_ee_displacement_distribution.pdf\ndocs/paper/main.fls:283:INPUT ../../artifacts/figures/fig2_ee_displacement_distribution.pdf\ndocs/paper/main.log:567:<../../artifacts/figures/fig2_ee_displacement_distribution.pdf, id=491, 500.106\ndocs/paper/main.log:569:File: ../../artifacts/figures/fig2_ee_displacement_distribution.pdf Graphic fil\ndocs/paper/main.log:571:&lt;use ../../artifacts/figures/fig2_ee_displacement_distribution.pdf>\ndocs/paper/main.log:572:Package pdftex.def Info: ../../artifacts/figures/fig2_ee_displacement_distribut\ndocs/paper/main.log:579:[10 <../../artifacts/figures/fig2_ee_displacement_distribution.pdf>]\ndocs/paper/main.fdb_latexmk:12:  \"../../artifacts/figures/fig2_ee_displacement_distribution.pdf\" 1779802483.58778 96079 cdee19c8463e2117aa75565b00ea4a5a \"\"\ndocs/paper/appendix.tex:6:\\includegraphics[width=\\linewidth]{fig2_ee_displacement_distribution}",
    "numLines": 11
  }
}
```

</details>

---

### Tool call

_source line 218_

<details open><summary>🔧 Tool call — Grep · `toolu_01AKcC11L4JWuCaVytQAz3e9`</summary>

```json
{
  "pattern": "56\\.5",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
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
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "9caaac57-ef56-4bef-a391-9e270e4e55b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hwz8uUdKaTdfXCWU9tToHu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8746,
      "cache_read_input_tokens": 33679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8746
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

_source line 219 · 2026-05-27T13:16:44.889Z_

<details><summary>↩ Tool result · `toolu_01AKcC11L4JWuCaVytQAz3e9`</summary>

```text
docs/paper/archive/analysis_claim4.tex:20:Pi0.5+A1 $\lambda{=}0.01$ & 49.0 & 56.5 & 56.5 & \placeholder{XX.X} & 0.0 \\
docs/paper/archive/analysis_claim4.tex:29:[Omitted long matching line]
docs/paper/archive/analysis_claim4.tex:37:[Omitted long matching line]
docs/paper/appendix.tex:165:22K steps & 60.5 & 56.5 & 58.5 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "85d88c58-261d-4be9-acd3-4d467cb6d5a8",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/archive/analysis_claim4.tex:20:Pi0.5+A1 $\\lambda{=}0.01$ & 49.0 & 56.5 & 56.5 & \\placeholder{XX.X} & 0.0 \\\\\ndocs/paper/archive/analysis_claim4.tex:29:[Omitted long matching line]\ndocs/paper/archive/analysis_claim4.tex:37:[Omitted long matching line]\ndocs/paper/appendix.tex:165:22K steps & 60.5 & 56.5 & 58.5 \\\\",
    "numLines": 4
  }
}
```

</details>

---

### Assistant

_source line 220_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have all the data I need. Let me compile the audit report.

The 56.5 in the main paper files is only in:
1. `archive/analysis_claim4.tex` line 20 - this is in archive, so it's not the active paper
2. `appendix.tex` line 165 - this is the stepwise checkpoint analysis, 22K checkpoint seed 1 = 56.5. This is NOT the LoRA s0 value - it's correctly showing λ=0.1 seed 1 at 22K steps.


So the main paper doesn't have the wrong 56.5 for LoRA s0. Now I'm checking whether the per-task CAR numbers for the s1_l01_high experiment appear anywhere in the main paper—specifically OJ CAR=66%, CP CAR=72%, milk CAR=70%, bbq CAR=26%. From what I can see, claim3.tex mentions the per-task CAR ordering is preserved across conditions but doesn't provide the specific numbers, and there's no per-task CAR table for the λ conditions.

The real question is whether the paper actually needs to include these numbers or if the checklist is just asking whether they're referenced and correct if they are. I should also check if fig5_lambda_curve shows per-task data or if there's a per-task CAR figure elsewhere that demonstrates the pattern the paper keeps mentioning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "4323b6cc-2a4c-4356-b971-cc87dfcd1e9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Vkvw9Sv4JzxA6FY8o7qSc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3467,
      "cache_read_input_tokens": 42425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3467
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

_source line 221_

Let me check if the figure data includes per-task info.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "d666e939-f248-4ea5-8d11-aea81431b7d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Vkvw9Sv4JzxA6FY8o7qSc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3467,
      "cache_read_input_tokens": 42425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3467
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

_source line 222_

<details open><summary>🔧 Tool call — Glob · `toolu_019K21wSnYDYh4eJGgpbLoef`</summary>

```json
{
  "pattern": "**/fig5*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "6a34ba1e-3cf3-4c4b-83da-baff0b9beefd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Vkvw9Sv4JzxA6FY8o7qSc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3467,
      "cache_read_input_tokens": 42425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3467
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

_source line 223 · 2026-05-27T13:16:59.900Z_

<details><summary>↩ Tool result · `toolu_019K21wSnYDYh4eJGgpbLoef`</summary>

```text
artifacts/_project/chart/fig5_lambda_curve.pdf
artifacts/_project/chart/fig5_lambda_curve_5f2325.pdf
artifacts/_project/chart/fig5_lambda_curve_4bb269.pdf
artifacts/fig5_lambda_stepwise.csv
artifacts/_project/chart/fig5_lambda_curve.png
artifacts/figures/fig5_lambda_curve.pdf
artifacts/figures/fig5_lambda_curve.png
artifacts/_project/data/fig5_lambda_data.csv
artifacts/fig5_lambda_data.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "e8621305-f91e-4579-a9b9-d37be8e2e444",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/chart/fig5_lambda_curve.pdf",
      "artifacts/_project/chart/fig5_lambda_curve_5f2325.pdf",
      "artifacts/_project/chart/fig5_lambda_curve_4bb269.pdf",
      "artifacts/fig5_lambda_stepwise.csv",
      "artifacts/_project/chart/fig5_lambda_curve.png",
      "artifacts/figures/fig5_lambda_curve.pdf",
      "artifacts/figures/fig5_lambda_curve.png",
      "artifacts/_project/data/fig5_lambda_data.csv",
      "artifacts/fig5_lambda_data.csv"
    ],
    "durationMs": 6,
    "numFiles": 9,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 224_

<details open><summary>🔧 Tool call — Grep · `toolu_01MHou7k8yTA2X1Zj9Q1Wea6`</summary>

```json
{
  "pattern": "per.task|per_task",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "f444fe23-995c-4bb9-b70b-9b427086f0c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Vkvw9Sv4JzxA6FY8o7qSc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3467,
      "cache_read_input_tokens": 42425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3467
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

_source line 225 · 2026-05-27T13:17:00.469Z_

<details><summary>↩ Tool result · `toolu_01MHou7k8yTA2X1Zj9Q1Wea6`</summary>

```text
docs/paper/claim3.tex:27:[Omitted long matching line]
docs/paper/claim3.tex:33:[Omitted long matching line]
docs/paper/claim3.tex:38:\caption{Effect of SDF loss weight $\lambda$ on CAR and TSR. $\lambda = 0$: LoRA-only. Low $\lambda$ ($\leq 0.01$) remains within the null band; $\lambda = 0.1$ (58.25\%, 2 seeds) shows a marginal departure ($p \approx 0.023$) whose per-task pattern still matches the demonstration distribution.}
docs/paper/discussion.tex:6:[Omitted long matching line]
docs/paper/experimental_framework.tex:11:Each method is evaluated for 50 episodes per task (200 episodes total). For multi-seed experiments (Pi0.5), we run 3 seeds to produce 600 episodes per configuration. Initial object configurations are fixed across methods to ensure fair comparison.
docs/paper/method.tex:5:[Omitted long matching line]
docs/paper/archive/analysis_claim2.tex:29:[Omitted long matching line]
docs/paper/archive/analysis_claim3.tex:26:[Omitted long matching line]
docs/paper/archive/analysis_claim3.tex:31:[Omitted long matching line]
docs/paper/archive/analysis_claim3.tex:35:\caption{Per-task TSR (\%) at 30K training steps. Chocolate Pudding partially survives fine-tuning across all conditions; the remaining three tasks collapse to near zero. The per-task pattern is indistinguishable between LoRA-only and SDF-augmented training.}
docs/paper/archive/analysis_claim3.tex:36:\label{tab:per_task_tsr}
docs/paper/archive/analysis_claim4.tex:31:Per-task decomposition reveals heterogeneous improvement across workspace configurations. Tasks~0--2 show CAR gains of \placeholder{XX}--\placeholder{XX} percentage points over the Pi0.5 baseline, with TSR reductions of \placeholder{XX}--\placeholder{XX} points. Task~3 (\texttt{bbq\_sauce}) exhibits a distinct pattern discussed below. The non-uniform response across tasks suggests that SDF supervision interacts with workspace layout in ways that require per-task analysis.
docs/paper/abstract.tex:7:Its contribution during training is dose-dependent: LoRA-only fine-tuning raises dfCAR from 26.8\% to 54.75\%$\,\pm\,$3.18, matching SDF-augmented training at $\lambda{=}0.005$ (54.5\%$\,\pm\,$2.29) and $\lambda{=}0.01$ (56.33\%$\,\pm\,$1.61); at $\lambda{=}0.1$, two of three seeds show a marginal signal (58.25\%$\,\pm\,$0.35, $p{\approx}0.023$) whose per-task avoidance pattern still mirrors the demonstration distribution, requiring further investigation.
docs/paper/appendix.tex:63:Table~\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.
docs/paper/appendix.tex:68:\label{tab:per_task_tsr}
docs/paper/appendix.tex:117:[Omitted long matching line]
docs/paper/appendix.tex:174:Individual seeds exhibit checkpoint-to-checkpoint CAR fluctuations of up to 8\,pp (seed~0: 52.5--60.5\%), larger than the cross-seed standard deviation at any fixed checkpoint ($\leq$2.8\,pp). This is consistent with binomial sampling noise at $n = 50$ episodes per task ($\sigma \approx 7$\,pp per task for $p \approx 0.5$). The seed-averaged curve shows no monotonic trend, confirming that SDF loss weight does not produce a progressive training signal.
docs/paper/appendix.tex:230:[Omitted long matching line]
docs/paper/introduction.tex:20:[Omitted long matching line]
docs/paper/introduction.tex:27:    \item \textbf{Demonstration sufficiency:} on SafeLIBERO, collision-free demonstrations account for all measured CAR gains (${\sim}$28\,pp); EE-only SDF at low $\lambda$ ($\leq 0.01$) adds nothing, and at high $\lambda = 0.1$ shows only a marginal, inconclusive signal ($n = 2$) whose per-task pattern still matches the demonstration distribution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "3a28566f-3a27-417b-b7ec-2b173e4cd847",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/claim3.tex:27:[Omitted long matching line]\ndocs/paper/claim3.tex:33:[Omitted long matching line]\ndocs/paper/claim3.tex:38:\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. $\\lambda = 0$: LoRA-only. Low $\\lambda$ ($\\leq 0.01$) remains within the null band; $\\lambda = 0.1$ (58.25\\%, 2 seeds) shows a marginal departure ($p \\approx 0.023$) whose per-task pattern still matches the demonstration distribution.}\ndocs/paper/discussion.tex:6:[Omitted long matching line]\ndocs/paper/experimental_framework.tex:11:Each method is evaluated for 50 episodes per task (200 episodes total). For multi-seed experiments (Pi0.5), we run 3 seeds to produce 600 episodes per configuration. Initial object configurations are fixed across methods to ensure fair comparison.\ndocs/paper/method.tex:5:[Omitted long matching line]\ndocs/paper/archive/analysis_claim2.tex:29:[Omitted long matching line]\ndocs/paper/archive/analysis_claim3.tex:26:[Omitted long matching line]\ndocs/paper/archive/analysis_claim3.tex:31:[Omitted long matching line]\ndocs/paper/archive/analysis_claim3.tex:35:\\caption{Per-task TSR (\\%) at 30K training steps. Chocolate Pudding partially survives fine-tuning across all conditions; the remaining three tasks collapse to near zero. The per-task pattern is indistinguishable between LoRA-only and SDF-augmented training.}\ndocs/paper/archive/analysis_claim3.tex:36:\\label{tab:per_task_tsr}\ndocs/paper/archive/analysis_claim4.tex:31:Per-task decomposition reveals heterogeneous improvement across workspace configurations. Tasks~0--2 show CAR gains of \\placeholder{XX}--\\placeholder{XX} percentage points over the Pi0.5 baseline, with TSR reductions of \\placeholder{XX}--\\placeholder{XX} points. Task~3 (\\texttt{bbq\\_sauce}) exhibits a distinct pattern discussed below. The non-uniform response across tasks suggests that SDF supervision interacts with workspace layout in ways that require per-task analysis.\ndocs/paper/abstract.tex:7:Its contribution during training is dose-dependent: LoRA-only fine-tuning raises dfCAR from 26.8\\% to 54.75\\%$\\,\\pm\\,$3.18, matching SDF-augmented training at $\\lambda{=}0.005$ (54.5\\%$\\,\\pm\\,$2.29) and $\\lambda{=}0.01$ (56.33\\%$\\,\\pm\\,$1.61); at $\\lambda{=}0.1$, two of three seeds show a marginal signal (58.25\\%$\\,\\pm\\,$0.35, $p{\\approx}0.023$) whose per-task avoidance pattern still mirrors the demonstration distribution, requiring further investigation.\ndocs/paper/appendix.tex:63:Table~\\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.\ndocs/paper/appendix.tex:68:\\label{tab:per_task_tsr}\ndocs/paper/appendix.tex:117:[Omitted long matching line]\ndocs/paper/appendix.tex:174:Individual seeds exhibit checkpoint-to-checkpoint CAR fluctuations of up to 8\\,pp (seed~0: 52.5--60.5\\%), larger than the cross-seed standard deviation at any fixed checkpoint ($\\leq$2.8\\,pp). This is consistent with binomial sampling noise at $n = 50$ episodes per task ($\\sigma \\approx 7$\\,pp per task for $p \\approx 0.5$). The seed-averaged curve shows no monotonic trend, confirming that SDF loss weight does not produce a progressive training signal.\ndocs/paper/appendix.tex:230:[Omitted long matching line]\ndocs/paper/introduction.tex:20:[Omitted long matching line]\ndocs/paper/introduction.tex:27:    \\item \\textbf{Demonstration sufficiency:} on SafeLIBERO, collision-free demonstrations account for all measured CAR gains (${\\sim}$28\\,pp); EE-only SDF at low $\\lambda$ ($\\leq 0.01$) adds nothing, and at high $\\lambda = 0.1$ shows only a marginal, inconclusive signal ($n = 2$) whose per-task pattern still matches the demonstration distribution.",
    "numLines": 20
  }
}
```

</details>

---

### Tool call

_source line 226_

<details open><summary>🔧 Tool call — Read · `toolu_01NSvbo58gxrF45U8kB6xBmr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/data/fig5_lambda_data.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "9baf2da2-0524-4742-9a83-47c490c13318",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVDgSQHvXY87NvUUMrKrQT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2268,
      "cache_read_input_tokens": 45892,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2268
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

_source line 227 · 2026-05-27T13:17:04.216Z_

<details><summary>↩ Tool result · `toolu_01NSvbo58gxrF45U8kB6xBmr`</summary>

```text
1	lambda,CAR_mean,CAR_std,CAR_seeds,TSR_mean,TSR_std,step,note
2	0,54.75,3.18,"57.0;52.5",48.75,,30K,LoRA-only (no SDF)
3	0.005,54.5,2.29,"57.0;54.0;52.5",54.0,3.0,30K,3 seeds
4	0.01,56.33,1.61,"57.0;57.5;54.5",53.83,1.5,30K,3 seeds
5	0.1,58.25,0.35,"58.0;58.5",48.0,1.4,30K,2 seeds 30K
6	
7	# step-wise sub-table (for inset or supplementary)
8	# lambda,step,CAR,TSR,seed,note
9	# 0.1,16000,pending,pending,0,best loss checkpoint eval running
10	# 0.1,20000,55,54,0,early signal
11	# 0.1,20000,56,51,1,early signal
12	# 0.1,22000,pending,pending,0,next after 16K
13	# 0.1,30000,pending,pending,0,training ~17:00 UTC
14	# 0.1,30000,pending,pending,1,training ~17:30 UTC
15	# 0.1,30000,pending,pending,2,training ~08:00 UTC 5/28
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "39bfb977-c351-48f0-8614-adddcc87a472",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/data/fig5_lambda_data.csv",
      "content": "lambda,CAR_mean,CAR_std,CAR_seeds,TSR_mean,TSR_std,step,note\n0,54.75,3.18,\"57.0;52.5\",48.75,,30K,LoRA-only (no SDF)\n0.005,54.5,2.29,\"57.0;54.0;52.5\",54.0,3.0,30K,3 seeds\n0.01,56.33,1.61,\"57.0;57.5;54.5\",53.83,1.5,30K,3 seeds\n0.1,58.25,0.35,\"58.0;58.5\",48.0,1.4,30K,2 seeds 30K\n\n# step-wise sub-table (for inset or supplementary)\n# lambda,step,CAR,TSR,seed,note\n# 0.1,16000,pending,pending,0,best loss checkpoint eval running\n# 0.1,20000,55,54,0,early signal\n# 0.1,20000,56,51,1,early signal\n# 0.1,22000,pending,pending,0,next after 16K\n# 0.1,30000,pending,pending,0,training ~17:00 UTC\n# 0.1,30000,pending,pending,1,training ~17:30 UTC\n# 0.1,30000,pending,pending,2,training ~08:00 UTC 5/28\n",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  }
}
```

</details>

---

### Tool call

_source line 228_

<details open><summary>🔧 Tool call — Read · `toolu_01Dps4ctdi5CH3mSNKeCBwT9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/reeval_comparison.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "500145f6-f7a4-4f85-aceb-15a495b7fae9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVDgSQHvXY87NvUUMrKrQT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2268,
      "cache_read_input_tokens": 45892,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2268
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

_source line 229 · 2026-05-27T13:17:04.674Z_

<details><summary>↩ Tool result · `toolu_01Dps4ctdi5CH3mSNKeCBwT9`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\caption{Evaluation results before and after fixing the 180° image rotation bug in \texttt{eval\_safelibero.py}.}
4	\label{tab:reeval_comparison}
5	\resizebox{\textwidth}{!}{
6	\begin{tabular}{l c c c c c c c}
7	\toprule
8	Model & \multicolumn{2}{c}{TSR (\%)} & $\Delta$TSR & \multicolumn{2}{c}{CAR (\%)} & $\Delta$CAR & EE Disp (m) \\
9	\cmidrule(lr){2-3} \cmidrule(lr){5-6}
10	 & Before & After & (pp) & Before & After & (pp) & (After) \\
11	\midrule
12	Pi0.5 baseline s0 & 74.7 & 71.5 & -3.2 & 26.8 & 28.5 & +1.7 & 0.367 \\
13	\addlinespace
14	LoRA-only s0 & 6.5 & 51.5 & +45.0 & 54.5 & 56.5 & +2.0 & 0.396 \\
15	LoRA-only s1 & 6.0 & — & — & 56.0 & — & — & — \\
16	\rowcolor{gray!15} \textit{LoRA-only mean} & 6.2$\pm$0.2 & 51.5$\pm$0.0 & +45.2 & 55.2$\pm$0.8 & 56.5$\pm$0.0 & +1.2 & \\
17	\addlinespace
18	SDF $\lambda$=0.005 s0 & 4.5 & — & — & 53.5 & — & — & — \\
19	SDF $\lambda$=0.005 s1 & 9.0 & — & — & 50.0 & — & — & — \\
20	SDF $\lambda$=0.005 s2 & 7.0 & — & — & 48.0 & — & — & — \\
21	\rowcolor{gray!15} \textit{SDF $\lambda$=0.005 mean} & 6.8$\pm$1.8 & — & — & 50.5$\pm$2.3 & — & — & \\
22	\addlinespace
23	SDF $\lambda$=0.01 s0 & 8.0 & — & — & 50.0 & — & — & — \\
24	SDF $\lambda$=0.01 s1 & 5.5 & — & — & 55.0 & — & — & — \\
25	SDF $\lambda$=0.01 s2 & 5.0 & — & — & 54.0 & — & — & — \\
26	\rowcolor{gray!15} \textit{SDF $\lambda$=0.01 mean} & 6.2$\pm$1.3 & — & — & 53.0$\pm$2.2 & — & — & \\
27	\bottomrule
28	\end{tabular}}
29	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "139822cb-d649-4281-9b71-df3a8f6493c9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/reeval_comparison.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\caption{Evaluation results before and after fixing the 180° image rotation bug in \\texttt{eval\\_safelibero.py}.}\n\\label{tab:reeval_comparison}\n\\resizebox{\\textwidth}{!}{\n\\begin{tabular}{l c c c c c c c}\n\\toprule\nModel & \\multicolumn{2}{c}{TSR (\\%)} & $\\Delta$TSR & \\multicolumn{2}{c}{CAR (\\%)} & $\\Delta$CAR & EE Disp (m) \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){5-6}\n & Before & After & (pp) & Before & After & (pp) & (After) \\\\\n\\midrule\nPi0.5 baseline s0 & 74.7 & 71.5 & -3.2 & 26.8 & 28.5 & +1.7 & 0.367 \\\\\n\\addlinespace\nLoRA-only s0 & 6.5 & 51.5 & +45.0 & 54.5 & 56.5 & +2.0 & 0.396 \\\\\nLoRA-only s1 & 6.0 & — & — & 56.0 & — & — & — \\\\\n\\rowcolor{gray!15} \\textit{LoRA-only mean} & 6.2$\\pm$0.2 & 51.5$\\pm$0.0 & +45.2 & 55.2$\\pm$0.8 & 56.5$\\pm$0.0 & +1.2 & \\\\\n\\addlinespace\nSDF $\\lambda$=0.005 s0 & 4.5 & — & — & 53.5 & — & — & — \\\\\nSDF $\\lambda$=0.005 s1 & 9.0 & — & — & 50.0 & — & — & — \\\\\nSDF $\\lambda$=0.005 s2 & 7.0 & — & — & 48.0 & — & — & — \\\\\n\\rowcolor{gray!15} \\textit{SDF $\\lambda$=0.005 mean} & 6.8$\\pm$1.8 & — & — & 50.5$\\pm$2.3 & — & — & \\\\\n\\addlinespace\nSDF $\\lambda$=0.01 s0 & 8.0 & — & — & 50.0 & — & — & — \\\\\nSDF $\\lambda$=0.01 s1 & 5.5 & — & — & 55.0 & — & — & — \\\\\nSDF $\\lambda$=0.01 s2 & 5.0 & — & — & 54.0 & — & — & — \\\\\n\\rowcolor{gray!15} \\textit{SDF $\\lambda$=0.01 mean} & 6.2$\\pm$1.3 & — & — & 53.0$\\pm$2.2 & — & — & \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}",
      "numLines": 29,
      "startLine": 1,
      "totalLines": 29
    }
  }
}
```

</details>

---

### Assistant

_source line 230_

<details><summary>Logged reasoning block</summary>

```text
Now I have a full picture. Let me compile the audit report.

Looking at `reeval_comparison.tex`:
- Line 14: LoRA-only s0 After CAR = 56.5. The checklist says s0 reeval_v2 CAR=57%. So this is wrong (56.5 vs 57.0).
- But wait, this file is a standalone comparison table in artifacts. It's labeled "reeval_comparison" and shows "before and after fixing the 180° image rotation bug". The "After" column for LoRA-only s0 is 56.5. 

The authoritative value after the full reeval_v2 is 57.0, so this file contains outdated data. Since it's in artifacts rather than the main paper directory and doesn't appear to be included in the paper itself, this discrepancy doesn't affect the published results.

Now let me check the per-task numbers. The paper claims in claim3.tex that the per-task CAR ordering is preserved across all conditions with chocolate_pudding highest and bbq_sauce lowest, and Figure 4 should verify this.

Examining the LoRA table row in claim3.tex Table 4 against appendix.tex Table 7...

the LoRA-only metrics check out (TSR=48.75, CAR=54.75±3.18), but I'm noticing a discrepancy in the per-task TSR table. The appendix shows LoRA-only with a mean of 46.0, which is labeled as seed 0 only, yet the main table reports 48.75 as the 2-seed average—that's (46+51.5)/2. So the per-task table is correctly identifying it as seed 0 data, but I need to verify whether the main table's 48.75 figure actually represents both seeds or if there's a mismatch in what's being reported. R=48.75 for LoRA-only (2 seeds). The 48.75 would be (46.0 + 51.5)/2 = 48.75. So there's no inconsistency — the per-task table explicitly says it's seed 0 only.

But wait — the checklist says s0 reeval_v2 TSR=46%. And the per-task TSR for seed 0 sums to (18+72+32+62)/4 = 46.0. So this is consistent.

Status: ✅ All LoRA row numbers in the main paper (docs/paper/) are correct.

Side note: `artifacts/reeval_comparison.tex` line 14 has LoRA-only s0 After CAR=56.5 (should be 57.0), but this file is not part of the submitted paper.

For EE Displacement, the paper reports the 2-seed mean of 0.394 at λ=0.1, but doesn't include the per-seed breakdown or the specific obstacle metric values. Whether this matters depends on what level of detail the reviewer expects.

Now I'm checking the standard deviation consistency across the claims.

tex, abstract, CSV data, and appendix null distribution calculations to verify they all align.

Now I'm checking whether the individual seed values produce the reported means and standard deviations for each configuration—LoRA-only, λ=0.005, and the others—to ensure the aggregate statistics are mathematically sound. I've verified all the calculations for the different lambda values, and now I'm ready to put together the report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "144001e7-1644-488d-a30e-439d369424f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016JfW2dzRcR8WoXncLGHe9n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1502,
      "cache_read_input_tokens": 48160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1502
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

_source line 231_

I have all the data needed. Here's the audit report:

---

## 审计报告：Reviewer 修正项完成状态

### 1. s1 per-task 数字 — ⚠️ 未在论文中列出

论文多处声称 "per-task CAR ordering is preserved across all conditions"（`claim3.tex:27`、`claim3.tex:33`），但**未给出具体数字**。

- 正确值（OJ=66%, CP=72%, milk=70%, bbq=26% CAR; TSR: OJ=26%, CP=80%, milk=28%, bbq=62%）在 `docs/paper/` 的所有 tex 文件中**均未出现**
- `appendix.tex` 有 per-task TSR 表（Table 5, lines 66-86），但只报告了 LoRA seed 0 的 TSR（OJ=18, CP=72, milk=32, bbq=62），无 λ=0.1 per-task 数据
- `appendix.tex` 有 per-task CAR 表（Table 9, lines 121-138），但仅针对 oracle refinement，不涉及 lambda 消融
- Figure 4 (`fig5_lambda_curve`) 只显示 aggregate CAR/TSR，无 per-task

**结论**：论文声称 per-task ordering 一致但未提供支持数据。如 Reviewer 要求的是在论文中引用这些数字，则需要增加 per-task CAR 表或在 appendix 补充。

---

### 2. LoRA Table 行 — ✅ 主论文正确

**主论文（`docs/paper/`）所有数值正确**：

| 位置 | 数值 | 状态 |
|------|------|------|
| `claim3.tex:17` — Table 4 aggregate | CAR=54.75±3.18, TSR=48.75, 2 seeds | ✅ |
| `appendix.tex:48` — dfCAR threshold | LoRA s0 = 57.0 | ✅ |
| `appendix.tex:49` — dfCAR threshold | LoRA s1 = 52.5 | ✅ |
| `appendix.tex:81` — per-task TSR mean | seed 0 = 46.0 | ✅（注明 seed 0 only）|
| `abstract.tex:7` | 54.75%±3.18 | ✅ |

**非主论文中的过期数据**（不影响投稿，但建议清理）：

| 文件 | 行 | 当前值 | 正确值 |
|------|-----|--------|--------|
| `artifacts/reeval_comparison.tex:14` | LoRA s0 After CAR | 56.5 | 57.0 |

---

### 3. EE Displacement — ⚠️ 仅报告 aggregate

- `claim3.tex:20`：λ=0.1 EE Disp = **0.394m**（2-seed mean）
- `claim3.tex:15`：Pi0.5 baseline EE Disp = **0.367m**
- 具体值 **0.3884**（s1 avg_max_ee）和 **0.0553**（avg_max_obstacle）**未在论文任何位置出现**
- 0.394 作为 2-seed mean 合理（若 s0≈0.400, s1=0.3884, mean≈0.394）

**结论**：论文只报告 aggregate EE Disp，未报告 per-seed 或 obstacle displacement。如 Reviewer 要求的是验证 0.394 = mean(s0, s1)，数值可自洽；如要求报告 obstacle displacement，则缺失。

---

### 4. std 一致性 — ✅ 全部正确

逐一验证（从 seed 值手算）：

| 条件 | Seeds | 手算 mean | 手算 std | 论文值 | 状态 |
|------|-------|-----------|----------|--------|------|
| LoRA-only | 57, 52.5 | 54.75 | 3.18 | 54.75±3.18 | ✅ |
| λ=0.005 | 57, 54, 52.5 | 54.5 | 2.29 | 54.5±2.29 | ✅ |
| λ=0.01 | 57, 57.5, 54.5 | 56.33 | 1.61 | 56.33±1.61 | ✅ |
| λ=0.1 | 58, 58.5 | 58.25 | 0.35 | 58.25±0.35 | ✅ |

以下位置全部一致：
- `claim3.tex:17-20` (Table 4) ✅
- `abstract.tex:7` ✅
- `fig5_lambda_data.csv` ✅
- `appendix.tex:144` null distribution (mean=54.6%, σ=2.27%) ✅

---

## 总结

| # | 修正项 | 状态 | 说明 |
|---|--------|------|------|
| 1 | s1 per-task 数字 | ⚠️ | 论文声称 ordering 一致但未列出 λ=0.1 per-task CAR/TSR 具体数值 |
| 2 | LoRA Table 行 | ✅ | 主论文所有数值正确 |
| 3 | EE Disp | ⚠️ | aggregate 0.394 正确；per-seed 和 obstacle displacement 未报告 |
| 4 | std 一致性 | ✅ | 全部手算验证通过 |

**需要行动**：Item 1 和 Item 3 取决于 Reviewer 的具体要求——是要求论文中引用这些数字（则需补充），还是只要求验证内部一致性（则已满足）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "uuid": "5a2ddc4a-63bb-4553-b43b-2723ac2fae5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016JfW2dzRcR8WoXncLGHe9n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1502,
      "cache_read_input_tokens": 48160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1502
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

### Task result

_source line 232_

I have all the data needed. Here's the audit report:

---

## 审计报告：Reviewer 修正项完成状态

### 1. s1 per-task 数字 — ⚠️ 未在论文中列出

论文多处声称 "per-task CAR ordering is preserved across all conditions"（`claim3.tex:27`、`claim3.tex:33`），但**未给出具体数字**。

- 正确值（OJ=66%, CP=72%, milk=70%, bbq=26% CAR; TSR: OJ=26%, CP=80%, milk=28%, bbq=62%）在 `docs/paper/` 的所有 tex 文件中**均未出现**
- `appendix.tex` 有 per-task TSR 表（Table 5, lines 66-86），但只报告了 LoRA seed 0 的 TSR（OJ=18, CP=72, milk=32, bbq=62），无 λ=0.1 per-task 数据
- `appendix.tex` 有 per-task CAR 表（Table 9, lines 121-138），但仅针对 oracle refinement，不涉及 lambda 消融
- Figure 4 (`fig5_lambda_curve`) 只显示 aggregate CAR/TSR，无 per-task

**结论**：论文声称 per-task ordering 一致但未提供支持数据。如 Reviewer 要求的是在论文中引用这些数字，则需要增加 per-task CAR 表或在 appendix 补充。

---

### 2. LoRA Table 行 — ✅ 主论文正确

**主论文（`docs/paper/`）所有数值正确**：

| 位置 | 数值 | 状态 |
|------|------|------|
| `claim3.tex:17` — Table 4 aggregate | CAR=54.75±3.18, TSR=48.75, 2 seeds | ✅ |
| `appendix.tex:48` — dfCAR threshold | LoRA s0 = 57.0 | ✅ |
| `appendix.tex:49` — dfCAR threshold | LoRA s1 = 52.5 | ✅ |
| `appendix.tex:81` — per-task TSR mean | seed 0 = 46.0 | ✅（注明 seed 0 only）|
| `abstract.tex:7` | 54.75%±3.18 | ✅ |

**非主论文中的过期数据**（不影响投稿，但建议清理）：

| 文件 | 行 | 当前值 | 正确值 |
|------|-----|--------|--------|
| `artifacts/reeval_comparison.tex:14` | LoRA s0 After CAR | 56.5 | 57.0 |

---

### 3. EE Displacement — ⚠️ 仅报告 aggregate

- `claim3.tex:20`：λ=0.1 EE Disp = **0.394m**（2-seed mean）
- `claim3.tex:15`：Pi0.5 baseline EE Disp = **0.367m**
- 具体值 **0.3884**（s1 avg_max_ee）和 **0.0553**（avg_max_obstacle）**未在论文任何位置出现**
- 0.394 作为 2-seed mean 合理（若 s0≈0.400, s1=0.3884, mean≈0.394）

**结论**：论文只报告 aggregate EE Disp，未报告 per-seed 或 obstacle displacement。如 Reviewer 要求的是验证 0.394 = mean(s0, s1)，数值可自洽；如要求报告 obstacle displacement，则缺失。

---

### 4. std 一致性 — ✅ 全部正确

逐一验证（从 seed 值手算）：

| 条件 | Seeds | 手算 mean | 手算 std | 论文值 | 状态 |
|------|-------|-----------|----------|--------|------|
| LoRA-only | 57, 52.5 | 54.75 | 3.18 | 54.75±3.18 | ✅ |
| λ=0.005 | 57, 54, 52.5 | 54.5 | 2.29 | 54.5±2.29 | ✅ |
| λ=0.01 | 57, 57.5, 54.5 | 56.33 | 1.61 | 56.33±1.61 | ✅ |
| λ=0.1 | 58, 58.5 | 58.25 | 0.35 | 58.25±0.35 | ✅ |

以下位置全部一致：
- `claim3.tex:17-20` (Table 4) ✅
- `abstract.tex:7` ✅
- `fig5_lambda_data.csv` ✅
- `appendix.tex:144` null distribution (mean=54.6%, σ=2.27%) ✅

---

## 总结

| # | 修正项 | 状态 | 说明 |
|---|--------|------|------|
| 1 | s1 per-task 数字 | ⚠️ | 论文声称 ordering 一致但未列出 λ=0.1 per-task CAR/TSR 具体数值 |
| 2 | LoRA Table 行 | ✅ | 主论文所有数值正确 |
| 3 | EE Disp | ⚠️ | aggregate 0.394 正确；per-seed 和 obstacle displacement 未报告 |
| 4 | std 一致性 | ✅ | 全部手算验证通过 |

**需要行动**：Item 1 和 Item 3 取决于 Reviewer 的具体要求——是要求论文中引用这些数字（则需补充），还是只要求验证内部一致性（则已满足）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 354495,
  "duration_api_ms": 354831,
  "num_turns": 20,
  "stop_reason": "end_turn",
  "session_id": "afbbb6da-f35d-4c28-bef2-c4d0401e5725",
  "total_cost_usd": 2.4340179999999996,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 38211,
    "cache_read_input_tokens": 290716,
    "output_tokens": 8183,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 38211,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 3503,
        "cache_read_input_tokens": 48160,
        "cache_creation_input_tokens": 1502,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1502
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1872,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001952,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 30,
      "outputTokens": 19057,
      "cacheReadInputTokens": 1652507,
      "cacheCreationInputTokens": 180678,
      "webSearchRequests": 0,
      "costUSD": 2.4320659999999994,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "13cadade-a54e-49be-9d4c-132da89b6d65"
}
```

</details>

---
