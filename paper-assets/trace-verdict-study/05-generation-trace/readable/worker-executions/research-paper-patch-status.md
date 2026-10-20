# research paper patch status

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/workers/worker_research_paper_patch_status_20260518T014706.log`
- **Structured JSON:** [`4b9d8c2c8d49fab8cde8.json`](../../sessions/4b/4b9d8c2c8d49fab8cde8.json)

## Before a recorded user message

37 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
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
  "uuid": "62939f75-a477-4ce0-ae04-37010ea98327",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/memory/"
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
    "resetsAt": 1779086400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "7b52a36f-8d40-4d4e-86e2-aac0e8d2b806",
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to check the current state of their paper to see what budget curve and head-tail data has been written in. According to the project constraints (C001), the paper .tex files are on the server at `/root/trace-verdict-study/docs/paper/`. Let me first check what's available locally and on the server.

Let me start by checking the local project directory structure and then read the paper files from the server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "98464051-b383-45a3-8a0c-52669c5d3920",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018esgiviHaxiBSw6vUnJep5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12994,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12994
      },
      "output_tokens": 34,
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

检查论文当前状态，确认 budget curve 和 head-tail 数据的写入情况。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "fe148019-a083-4163-aca0-e1d63f3870bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018esgiviHaxiBSw6vUnJep5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12994,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12994
      },
      "output_tokens": 34,
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

<details open><summary>🔧 Tool call — Glob · `toolu_013WPsK7NBxDMCyoV3kHMLpp`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "0c21bad0-0cb0-416f-a08f-dc48437e2568",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018esgiviHaxiBSw6vUnJep5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12994,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12994
      },
      "output_tokens": 34,
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

_source line 7 · 2026-05-18T01:47:18.397Z_

<details><summary>↩ Tool result · `toolu_013WPsK7NBxDMCyoV3kHMLpp`</summary>

```text
artifacts/dream_reports/dream_20260515T013018/best/paper.tex
artifacts/dream_reports/dream_20260515T013018/median/paper.tex
artifacts/dream_reports/dream_20260515T013018/worst/paper.tex
artifacts/dream_reports/dream_20260515T084908/best/paper.tex
artifacts/dream_reports/dream_20260515T084908/median/paper.tex
artifacts/dream_reports/dream_20260515T084908/worst/paper.tex
artifacts/_project/paper/related_work.tex
artifacts/per_class_breakdown.tex
artifacts/_project/paper/section3_experimental_setup_d4f1e8.tex
artifacts/_project/paper/section3_experimental_setup.tex
artifacts/_project/paper/ethics_statement.tex
artifacts/_project/paper/ethics_statement_77cf5f.tex
artifacts/_project/paper/arr_checklist.tex
artifacts/_project/paper/main_results_tables.tex
artifacts/_project/paper/main_results_tables_d8c8b6.tex
artifacts/paper_tables/main_results_tables.tex
artifacts/_project/paper/experiments.tex
artifacts/dream_reports/dream_20260516T105259/best/paper.tex
artifacts/dream_reports/dream_20260516T105259/median/paper.tex
artifacts/dream_reports/dream_20260516T105259/worst/paper.tex
artifacts/dream_reports/dream_20260516T155731/best/paper.tex
artifacts/dream_reports/dream_20260516T155731/median/paper.tex
artifacts/dream_reports/dream_20260516T155731/worst/paper.tex
docs/paper/arr_checklist.tex
docs/paper/method.tex
docs/paper/conclusion.tex
docs/paper/main.tex
docs/paper/related_work.tex
docs/paper/introduction.tex
docs/paper/appendix.tex
docs/paper/experiments.tex
docs/paper/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "b5374642-dfd6-4647-8b16-60918c5b0971",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260515T013018/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T013018/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T013018/worst/paper.tex",
      "artifacts/dream_reports/dream_20260515T084908/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T084908/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T084908/worst/paper.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/per_class_breakdown.tex",
      "artifacts/_project/paper/section3_experimental_setup_d4f1e8.tex",
      "artifacts/_project/paper/section3_experimental_setup.tex",
      "artifacts/_project/paper/ethics_statement.tex",
      "artifacts/_project/paper/ethics_statement_77cf5f.tex",
      "artifacts/_project/paper/arr_checklist.tex",
      "artifacts/_project/paper/main_results_tables.tex",
      "artifacts/_project/paper/main_results_tables_d8c8b6.tex",
      "artifacts/paper_tables/main_results_tables.tex",
      "artifacts/_project/paper/experiments.tex",
      "artifacts/dream_reports/dream_20260516T105259/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T105259/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T105259/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T155731/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T155731/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T155731/worst/paper.tex",
      "docs/paper/arr_checklist.tex",
      "docs/paper/method.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/main.tex",
      "docs/paper/related_work.tex",
      "docs/paper/introduction.tex",
      "docs/paper/appendix.tex",
      "docs/paper/experiments.tex",
      "docs/paper/discussion.tex"
    ],
    "durationMs": 16,
    "numFiles": 32,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_01WbMzD4fa8fnEZLcS31m8tE`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "05b45597-1404-4bc1-9312-a1d48c5189d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018esgiviHaxiBSw6vUnJep5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12994,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12994
      },
      "output_tokens": 34,
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

_source line 9 · 2026-05-18T01:47:18.506Z_

<details><summary>↩ Tool result · `toolu_01WbMzD4fa8fnEZLcS31m8tE`</summary>

```text
task_context/history/director/loop_1.md
task_context/history/agent/loop_1.md
docs/IDEA_BRIEF.md
artifacts/dream_reports/dream_20260515T013018/best/paper_framing.md
artifacts/dream_reports/dream_20260515T013018/median/paper_framing.md
task_context/history/agent/loop_2.md
task_context/history/reviewer/loop_1.md
artifacts/dream_reports/dream_20260515T013018/worst/paper_framing.md
artifacts/dream_reports/dream_20260515T013018/best/review_report.md
artifacts/dream_reports/dream_20260515T013018/median/review_report.md
artifacts/dream_reports/dream_20260515T013018/worst/review_report.md
.claude/sessions/agent_9c2cd44d/CLAUDE.md
.claude/sessions/agent_9c2cd44d/AGENTS.md
.claude/sessions/agent_6bb99313/CLAUDE.md
.claude/sessions/agent_6bb99313/AGENTS.md
task_context/history/director/loop_2.md
task_context/history/agent/loop_3.md
.claude/sessions/agent_42a1e69e/CLAUDE.md
.claude/sessions/agent_42a1e69e/AGENTS.md
task_context/history/agent/loop_2_1778837550.md
artifacts/report_training_progress.md
artifacts/plan_001_literature_linkage.md
artifacts/dream_reports/dream_20260515T084908/best/paper_framing.md
artifacts/dream_reports/dream_20260515T084908/median/paper_framing.md
artifacts/dream_reports/dream_20260515T084908/worst/paper_framing.md
artifacts/dream_reports/dream_20260515T084908/best/review_report.md
task_context/history/agent/loop_4.md
artifacts/dream_reports/dream_20260515T084908/median/review_report.md
artifacts/dream_reports/dream_20260515T084908/worst/review_report.md
artifacts/_project/intermediate/results_table_draft.md
artifacts/results_table_draft.md
task_context/history/reviewer/loop_2.md
task_context/history/director/loop_3.md
task_context/history/agent/loop_4_1778846671.md
task_context/history/agent/loop_4_1778849725.md
artifacts/_project/intermediate/literature_survey_20260515.md
task_context/history/director/loop_4.md
task_context/history/agent/loop_5.md
artifacts/deepseek_vota_fail_recall_analysis.md
task_context/history/agent/loop_5_1778856729.md
artifacts/literature_scan_20260515/scan_report.md
artifacts/_project/report/scan_report.md
artifacts/deepseek_vota_seed42/report/analysis.md
task_context/history/reviewer/loop_3.md
task_context/history/agent/loop_5_1778859339.md
task_context/history/agent/loop_5_1778860256.md
task_context/history/agent/loop_5_1778861007.md
task_context/history/agent/loop_6.md
task_context/history/director/loop_5.md
task_context/history/agent/loop_6_1778862695.md
task_context/history/agent/loop_6_1778863429.md
task_context/history/agent/loop_6_1778868664.md
artifacts/cross_model_analysis/cross_model_comparison.md
artifacts/_project/report/cross_model_comparison.md
artifacts/_project/paper/paper_framing_draft_v2.md
artifacts/paper_framing_draft_v2.md
artifacts/exception_only_seed_cross_analysis.md
task_context/history/agent/loop_6_1778869503.md
task_context/history/agent/loop_6_1778869904.md
task_context/history/agent/loop_5_1778870366.md
task_context/history/director/loop_6.md
task_context/history/agent/loop_6_1778872025.md
artifacts/exception_only_ci_verification.md
task_context/history/reviewer/loop_4.md
task_context/history/agent/loop_7.md
task_context/history/agent/loop_6_1778873128.md
task_context/history/agent/loop_7_1778873812.md
task_context/history/agent/loop_7_1778874063.md
task_context/history/agent/loop_7_1778874716.md
artifacts/_project/report/irreducible_error_analysis_d045d9.md
artifacts/_project/report/irreducible_error_analysis.md
artifacts/irreducible_error_analysis.md
task_context/history/agent/loop_7_1778878774.md
docs/claim1_variants.md
task_context/history/agent/loop_7_1778879106.md
task_context/history/agent/loop_7_1778880776.md
artifacts/_project/data/paper_data_tables.md
artifacts/paper_data_tables.md
artifacts/_project/report/claim2_evidence_brief.md
task_context/history/agent/loop_7_1778881043.md
task_context/history/agent/loop_7_1778881415.md
artifacts/gpu_status_20260516_0540.md
task_context/history/agent/loop_7_1778883113.md
task_context/history/agent/loop_8.md
task_context/history/agent/loop_8_1778884586.md
task_context/history/agent/loop_7_1778885280.md
task_context/history/agent/loop_8_1778885897.md
artifacts/_project/report/d030_eval_audit_report.md
task_context/history/agent/loop_8_1778886114.md
task_context/history/agent/loop_8_1778887670.md
artifacts/_project/report/debugbench_data_audit.md
artifacts/_project/data/debugbench_vota_ae_only_data.md
artifacts/debugbench_exception_bug_fix/report/debugbench_exception_bug_analysis.md
artifacts/_project/report/debugbench_data_validation_post_fix.md
task_context/history/agent/loop_8_1778890111.md
artifacts/full_trace_256tok_seed42/report/analysis.md
task_context/history/reviewer/loop_5.md
task_context/history/agent/loop_8_1778890690.md
task_context/history/agent/loop_8_1778893240.md
task_context/history/agent/loop_8_1778893258.md
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "b16796c5-3bf4-447a-99c6-54669d245493",
  "tool_use_result": {
    "filenames": [
      "task_context/history/director/loop_1.md",
      "task_context/history/agent/loop_1.md",
      "docs/IDEA_BRIEF.md",
      "artifacts/dream_reports/dream_20260515T013018/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260515T013018/median/paper_framing.md",
      "task_context/history/agent/loop_2.md",
      "task_context/history/reviewer/loop_1.md",
      "artifacts/dream_reports/dream_20260515T013018/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260515T013018/best/review_report.md",
      "artifacts/dream_reports/dream_20260515T013018/median/review_report.md",
      "artifacts/dream_reports/dream_20260515T013018/worst/review_report.md",
      ".claude/sessions/agent_9c2cd44d/CLAUDE.md",
      ".claude/sessions/agent_9c2cd44d/AGENTS.md",
      ".claude/sessions/agent_6bb99313/CLAUDE.md",
      ".claude/sessions/agent_6bb99313/AGENTS.md",
      "task_context/history/director/loop_2.md",
      "task_context/history/agent/loop_3.md",
      ".claude/sessions/agent_42a1e69e/CLAUDE.md",
      ".claude/sessions/agent_42a1e69e/AGENTS.md",
      "task_context/history/agent/loop_2_1778837550.md",
      "artifacts/report_training_progress.md",
      "artifacts/plan_001_literature_linkage.md",
      "artifacts/dream_reports/dream_20260515T084908/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260515T084908/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260515T084908/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260515T084908/best/review_report.md",
      "task_context/history/agent/loop_4.md",
      "artifacts/dream_reports/dream_20260515T084908/median/review_report.md",
      "artifacts/dream_reports/dream_20260515T084908/worst/review_report.md",
      "artifacts/_project/intermediate/results_table_draft.md",
      "artifacts/results_table_draft.md",
      "task_context/history/reviewer/loop_2.md",
      "task_context/history/director/loop_3.md",
      "task_context/history/agent/loop_4_1778846671.md",
      "task_context/history/agent/loop_4_1778849725.md",
      "artifacts/_project/intermediate/literature_survey_20260515.md",
      "task_context/history/director/loop_4.md",
      "task_context/history/agent/loop_5.md",
      "artifacts/deepseek_vota_fail_recall_analysis.md",
      "task_context/history/agent/loop_5_1778856729.md",
      "artifacts/literature_scan_20260515/scan_report.md",
      "artifacts/_project/report/scan_report.md",
      "artifacts/deepseek_vota_seed42/report/analysis.md",
      "task_context/history/reviewer/loop_3.md",
      "task_context/history/agent/loop_5_1778859339.md",
      "task_context/history/agent/loop_5_1778860256.md",
      "task_context/history/agent/loop_5_1778861007.md",
      "task_context/history/agent/loop_6.md",
      "task_context/history/director/loop_5.md",
      "task_context/history/agent/loop_6_1778862695.md",
      "task_context/history/agent/loop_6_1778863429.md",
      "task_context/history/agent/loop_6_1778868664.md",
      "artifacts/cross_model_analysis/cross_model_comparison.md",
      "artifacts/_project/report/cross_model_comparison.md",
      "artifacts/_project/paper/paper_framing_draft_v2.md",
      "artifacts/paper_framing_draft_v2.md",
      "artifacts/exception_only_seed_cross_analysis.md",
      "task_context/history/agent/loop_6_1778869503.md",
      "task_context/history/agent/loop_6_1778869904.md",
      "task_context/history/agent/loop_5_1778870366.md",
      "task_context/history/director/loop_6.md",
      "task_context/history/agent/loop_6_1778872025.md",
      "artifacts/exception_only_ci_verification.md",
      "task_context/history/reviewer/loop_4.md",
      "task_context/history/agent/loop_7.md",
      "task_context/history/agent/loop_6_1778873128.md",
      "task_context/history/agent/loop_7_1778873812.md",
      "task_context/history/agent/loop_7_1778874063.md",
      "task_context/history/agent/loop_7_1778874716.md",
      "artifacts/_project/report/irreducible_error_analysis_d045d9.md",
      "artifacts/_project/report/irreducible_error_analysis.md",
      "artifacts/irreducible_error_analysis.md",
      "task_context/history/agent/loop_7_1778878774.md",
      "docs/claim1_variants.md",
      "task_context/history/agent/loop_7_1778879106.md",
      "task_context/history/agent/loop_7_1778880776.md",
      "artifacts/_project/data/paper_data_tables.md",
      "artifacts/paper_data_tables.md",
      "artifacts/_project/report/claim2_evidence_brief.md",
      "task_context/history/agent/loop_7_1778881043.md",
      "task_context/history/agent/loop_7_1778881415.md",
      "artifacts/gpu_status_20260516_0540.md",
      "task_context/history/agent/loop_7_1778883113.md",
      "task_context/history/agent/loop_8.md",
      "task_context/history/agent/loop_8_1778884586.md",
      "task_context/history/agent/loop_7_1778885280.md",
      "task_context/history/agent/loop_8_1778885897.md",
      "artifacts/_project/report/d030_eval_audit_report.md",
      "task_context/history/agent/loop_8_1778886114.md",
      "task_context/history/agent/loop_8_1778887670.md",
      "artifacts/_project/report/debugbench_data_audit.md",
      "artifacts/_project/data/debugbench_vota_ae_only_data.md",
      "artifacts/debugbench_exception_bug_fix/report/debugbench_exception_bug_analysis.md",
      "artifacts/_project/report/debugbench_data_validation_post_fix.md",
      "task_context/history/agent/loop_8_1778890111.md",
      "artifacts/full_trace_256tok_seed42/report/analysis.md",
      "task_context/history/reviewer/loop_5.md",
      "task_context/history/agent/loop_8_1778890690.md",
      "task_context/history/agent/loop_8_1778893240.md",
      "task_context/history/agent/loop_8_1778893258.md"
    ],
    "durationMs": 20,
    "numFiles": 100,
    "truncated": true
  }
}
```

</details>

---

### Assistant

_source line 10_

本地有 `docs/paper/` 目录。根据 C001 约束，真源在服务器上，但本地也有副本。先读本地的 experiments.tex 和相关文件来快速审计。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "c519745e-6d4d-4ec2-ac4e-dc124f29ac6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UN4WtbzQNNJFf2q7USMiMu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2622,
      "cache_read_input_tokens": 24835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2622
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

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01JgKfq88G8h8ffohkFr5MmP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "5d188258-afe9-4834-b3af-78ed8f837553",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UN4WtbzQNNJFf2q7USMiMu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2622,
      "cache_read_input_tokens": 24835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2622
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

_source line 12 · 2026-05-18T01:47:22.944Z_

<details><summary>↩ Tool result · `toolu_01JgKfq88G8h8ffohkFr5MmP`</summary>

```text
1	\section{Experiments}
2	
3	We evaluate across two research questions:
4	(1)~Do Tier~1 exception signals generalize across models?
5	(2)~What is the relative contribution of each trace component?
6	All experiments use $N{=}1{,}190$ test samples; accuracy is reported with Wilson 95\% CIs.
7	Pairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42); all differences are significant at $p{<}0.0001$ unless noted.
8	
9	\subsection{Cross-Model Comparison}
10	\label{sec:cross_model}
11	
12	Table~\ref{tab:cross_model} compares four models spanning an 8.7$\times$ parameter range (1.5B--13B) and three architecture families (Qwen, DeepSeek, CodeLlama) under key conditions.
13	
14	\begin{table}[t]
15	\centering
16	\caption{Cross-model verdict accuracy (\%, $N{=}1{,}190$). Bold: best accuracy per model. Multi-seed entries show mean$\pm$std (3 seeds). $^\dag$2/3 seeds; one seed excluded due to LoRA initialization failure (91.09\%, fail recall = 70.5\%; see Appendix~\ref{sec:training_dynamics}). \texttt{ae\_only} and \texttt{loop\_only} ablations tested on Qwen-7B (3 seeds) to isolate component contributions; cross-model validation focused on the primary conditions. Full CIs in Appendix~\ref{sec:full_results}.}
17	\label{tab:cross_model}
18	\small
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{lcccc}
21	\toprule
22	\textbf{Condition} & \textbf{Qwen-7B} & \textbf{Qwen-1.5B} & \textbf{CL-13B} & \textbf{DS-6.7B} \\
23	\midrule
24	exception\_only & \textbf{99.83}{\scriptsize$\pm$0.00} & \textbf{99.83} & \textbf{99.89}{\scriptsize$\pm$0.10} & \textbf{99.33}$^\dag$ \\
25	ae\_only & 99.64{\scriptsize$\pm$0.49} & --- & --- & --- \\
26	VOTA & 99.41 & 99.58 & 98.57 & 84.45 \\
27	no\_trace & 75.13 & 67.31 & 76.50 & 73.36 \\
28	\midrule
29	Majority baseline & \multicolumn{4}{c}{71.51} \\
30	\bottomrule
31	\end{tabular}%
32	}
33	\end{table}
34	
35	\paragraph{Exception dominance across families.}
36	Under \texttt{exception\_only}, the Qwen and CodeLlama families achieve ${\geq}$99.83\% (mean): Qwen-7B (99.83\%$\pm$0.00, 3 seeds), Qwen-1.5B (99.83\%), and CodeLlama-13B (99.89\%$\pm$0.10, 3 seeds; seed 123 achieves 100\%).
37	DeepSeek-6.7B reaches 99.33\% on 2/3 seeds with one LoRA-sensitivity outlier at 91.09\% (seed 123; fail recall = 70.5\%); even the outlier outperforms VOTA (84.45\%) by 6.64pp.
38	Excluding the DeepSeek outlier, the cross-model range is 0.56pp (99.33--99.89\%), the tightest of any condition.
39	
40	\paragraph{Scale invariance of exception signals.}
41	Exception-based accuracy is shared by models spanning 1.5B to 13B parameters (8.7$\times$): both Qwen-1.5B and CodeLlama-13B achieve 99.83\%+ on the same representation.
42	CodeLlama-13B seed 123 achieves 100\% (0/1190 errors), confirming that Qwen's two persistent errors (from \texttt{GeneratorExit}; Appendix~\ref{sec:irreducible}) are high-probability convergence artifacts rather than hard data limitations.
43	In contrast, \texttt{no\_trace} scales monotonically with capacity: 67.31\% (1.5B) $\to$ 75.13\% (7B) $\to$ 76.50\% (13B), a 9.19pp range that exception events completely eliminate (Figure~\ref{fig:cross_scale}).
44	
45	\begin{figure}[t]
46	\centering
47	\includegraphics[width=\columnwidth]{fig3_cross_model_gap}
48	\caption{Verdict accuracy vs.\ model scale. \texttt{exception\_only} maintains ${\geq}$99.33\% regardless of scale (1.5B--13B), while \texttt{no\_trace} shows monotonic scale sensitivity (+9.19pp from 1.5B to 13B). The \texttt{nomarker} condition (format markers removed) shows no degradation at smaller scale (${\sim}$97.7--97.8\%).}
49	\label{fig:cross_scale}
50	\end{figure}
51	
52	\paragraph{VOTA cross-family variation.}
53	VOTA accuracy varies across families: 99.58\% (Qwen-1.5B) $>$ 99.41\% (Qwen-7B) $>$ 98.57\% (CodeLlama-13B; \texttt{codellama13b\_vota\_seed42}, CI [97.9, 99.2]) $\gg$ 84.45\% (DeepSeek-6.7B).
54	The CodeLlama result (17 errors) narrows the gap: among models without tokenizer-driven truncation, the VOTA range is only 1.01pp (98.57--99.58\%), suggesting that the 14.96pp DeepSeek deficit is primarily a truncation artifact rather than an inherent model capability limitation (91.7\% of DeepSeek training samples were affected; Appendix~\ref{sec:tokenizer_analysis}).
55	In contrast, \texttt{exception\_only} inputs are compact (median 150 tokens, mean 398 due to verbose fail-class exceptions), making the cross-model comparison clean.
56	
57	\subsection{Component Ablation}
58	\label{sec:ablation}
59	
60	We restrict \texttt{ae\_only} and \texttt{loop\_only} ablations to Qwen-7B, as these component-level analyses target the trace composition mechanism rather than cross-model generalization.
61	Table~\ref{tab:ablation} decomposes VOTA on Qwen-2.5-7B (seed=42) and reveals a two-tier hierarchy.
62	
63	\begin{table}[t]
64	\centering
65	\caption{Component ablation on Qwen-2.5-7B ($N{=}1{,}190$). Tier~1 signals achieve near-perfect accuracy; combining them (VOTA) slightly dilutes performance. $^\dag$\texttt{ae\_only}: 3-seed mean 99.64\% ($\pm$0.49; seeds 42: 99.92, 123: 99.08, 456: 99.92). \texttt{exception\_only}: 99.83\% ($\pm$0.00, 3 seeds), more stable ($\sigma{=}$0 vs.\ $\sigma{=}$0.49).}
66	\label{tab:ablation}
67	\small
68	\resizebox{\columnwidth}{!}{%
69	\begin{tabular}{llccc}
70	\toprule
71	\textbf{Condition} & \textbf{Components} & \textbf{Acc (\%)} & \textbf{95\% CI} & \textbf{Tier} \\
72	\midrule
73	ae\_only & assertion-point & 99.64$^\dag$ & [99.26, 99.87] & 1 \\
74	exception\_only & exception events & \textbf{99.83} & [99.58, 100.00] & 1 \\
75	VOTA & exc+ae+loop & 99.41 & [98.82, 99.83] & --- \\
76	VOTA\_no\_ae & exc+loop & 99.41 & [98.90, 99.80] & --- \\
77	loop\_only & loop compression & 85.63 & [83.53, 87.56] & 2 \\
78	full\_trace & complete trace & 81.76 & [79.70, 83.90] & --- \\
79	no\_trace & none & 75.13 & [72.77, 77.48] & --- \\
80	\midrule
81	Regex (best) & exc.\ type regex & 93.61 & --- & --- \\
82	3-shot (Qwen-7B) & in-context learning & 90.84 & --- & --- \\
83	Zero-shot (4 models) & prompting & 51.0--93.5 & --- & --- \\
84	\bottomrule
85	\end{tabular}%
86	}
87	\end{table}
88	
89	Tier~1 signals are individually sufficient: \texttt{ae\_only} (3-seed mean 99.64\% $\pm$ 0.49) and \texttt{exception\_only} (99.83\% $\pm$ 0.00) both exceed VOTA ($p{=}0.01$), implying that combining signals introduces noise; \texttt{exception\_only} is more stable across seeds ($\sigma{=}$0 vs.\ $\sigma{=}$0.49).
90	Removing assertion points has no effect (\texttt{VOTA\_no\_ae} = 99.41\%), confirming exception dominance.
91	Tier~2 \texttt{loop\_only} (85.63\%) improves 10.50pp over \texttt{no\_trace} ($p{<}0.0001$) but falls far short of Tier~1.
92	\paragraph{Rule-based baseline comparison.}
93	The strongest non-trivial regex heuristic (B4: exception class name matching) achieves 93.61\% accuracy (F1=0.876), trailing SFT \texttt{exception\_only} (99.83\%, F1=0.997) by 6.22pp (McNemar $p{<}0.001$).
94	The gap concentrates on caught-exception boundary cases: regex flags all exception events as failures, while SFT learns to distinguish caught exceptions (benign, inside \texttt{try/except}) from uncaught faults, correctly resolving 6/8 boundary samples (Appendix~\ref{sec:regex_baselines}).
95	Across trace formats, SFT consistently outperforms the best applicable regex, from +3.62pp (\texttt{no\_trace} over majority baseline) to +23.86pp (VOTA), with the largest gains on formats requiring semantic interpretation (Appendix~\ref{sec:regex_baselines}).
96	
97	\paragraph{Zero-shot and few-shot LLM baselines.}
98	Zero-shot prompting spans 51.0--93.5\% across four models (CodeLlama-13B: 51.01\%, Qwen-7B: 89.08\%, DeepSeek-6.7B: 90.59\%, Qwen-1.5B: 93.45\%), a 42.44pp range that SFT compresses to 0.56pp (99.33--99.89\%).
99	Zero-shot performance does not correlate with model size: Qwen-1.5B (93.45\%) outperforms both Qwen-7B (89.08\%) and CodeLlama-13B (51.01\%), indicating that pretraining data distribution, not capacity, determines zero-shot verdict ability.
100	CodeLlama-13B drops below the majority baseline (71.51\%), showing extreme fail bias (72.4\% of predictions are \texttt{fail}).
101	Three-shot in-context learning on Qwen-7B (90.84\%, fail recall = 80.53\%) improves only 1.76pp over zero-shot and still trails both the regex heuristic (93.61\%) and SFT by 8.99pp, confirming that a few examples cannot substitute for task-specific fine-tuning.
102	SFT normalizes this cross-architecture variance, closing a 6--49pp gap to ${\geq}$99.33\% across all models with 4,720 training samples (Appendix~\ref{sec:zeroshot_cross_model}).
103	
104	\subsection{Format Marker Ablation}
105	\label{sec:nomarker}
106	
107	The \texttt{exception\_only} format includes a \texttt{[No exception data in trace]} marker in all pass-class samples (regex baseline B5 exploits this for 99.33\% accuracy; Appendix~\ref{sec:regex_baselines}).
108	To quantify the marker's contribution, we retrain with all format markers removed (\texttt{nomarker} condition).
109	
110	Qwen-7B 3-seed mean: 97.65\% $\pm$ 0.96 (seeds 42/123/456: 96.55/98.32/98.07\%), a drop of 2.18pp from \texttt{exception\_only} (99.83\%).
111	Qwen-1.5B: 97.82\%, drop of 2.01pp.
112	The marker contribution (${\sim}$2pp) accounts for only ${\sim}$9\% of the total exception lift over \texttt{no\_trace} (24.70pp on 7B).
113	Exception events thus provide two signal layers that show no degradation at smaller scale: structural markers (${\sim}$2pp, regex-learnable) and semantic exception content (${\sim}$22pp, requiring SFT to distinguish caught from uncaught exceptions).
114	
115	\subsection{Information Density Decomposition}
116	\label{sec:density}
117	
118	The 17.65pp gap between \texttt{full\_trace} (81.76\%) and VOTA (99.41\%) decomposes via \texttt{full\_trace\_label\_only}, which retains the full trace but masks all trace tokens from the loss.
119	
120	\begin{table}[t]
121	\centering
122	\caption{Approximate information density decomposition: gradient dilution (${\sim}$26\%) vs.\ information overload (${\sim}$74\%).}
123	\label{tab:density}
124	\small
125	\begin{tabular}{lccc}
126	\toprule
127	\textbf{Condition} & \textbf{Acc (\%)} & \textbf{$\Delta$ vs.\ full\_trace} & \textbf{Gap explained} \\
128	\midrule
129	full\_trace & 81.76 & --- & --- \\
130	label\_only & 86.22 & +4.46pp & 26\% \\
131	VOTA & 99.41 & +17.65pp & 100\% \\
132	\bottomrule
133	\end{tabular}
134	\end{table}
135	
136	Gradient dilution accounts for approximately 26\% of the gap (+4.46pp, $p{<}0.0001$, bootstrap 95\% CI $[{+}2.35, {+}6.55]$): when the model no longer wastes gradient updates on predicting trace tokens, accuracy improves even with identical input.
137	The remaining ${\sim}$74\% (+13.19pp) reflects information overload at inference: the model receives thousands of irrelevant trace lines that compete for attention with the diagnostic signal, regardless of loss design.
138	This asymmetry implies that trace compression methods should prioritize \emph{content selection} (removing irrelevant lines) over \emph{loss engineering} (masking non-target tokens), as the larger bottleneck is what the model sees, not how it is trained.
139	The two factors may interact, so this decomposition is approximate.
140	
141	\subsection{Additional Analyses}
142	\label{sec:additional}
143	
144	\paragraph{Trace length ablation.}
145	\label{sec:trace_length}
146	Varying the head-truncated trace token budget (256--no limit) on Qwen-7B yields accuracy in a narrow 77.2\%--81.8\% band with a non-monotonic pattern: 1024-token prefixes (77.23\%) underperform 512-token prefixes (80.42\%, $p{=}0.002$), because mid-length prefixes retain enough irrelevant content to mislead the model while discarding diagnostic events near the trace terminus (Appendix~\ref{sec:trace_length_full}).
147	This non-monotonicity is specific to head-truncation; under tail-truncation, accuracy increases monotonically for two of three models (Table~\ref{tab:tail_cross_model} in Appendix), with only DeepSeek showing a mild architecture-specific reversal at tail-1024$\to$tail-2048 ($-$1.5pp).
148	
149	\paragraph{Truncation direction and budget curve.}
150	Tail-truncation (retaining the last $k$ tokens) dramatically outperforms head-truncation across all three models: tail-2048 exceeds head-2048 by 15.5--22.6pp, with the gap widening at smaller scale (Qwen-1.5B: +22.6pp vs.\ Qwen-7B: +15.5pp; Appendix~\ref{sec:trace_length_full}, Table~\ref{tab:head_vs_tail}).
151	
152	A full cross-model budget sweep reveals a sharp phase transition at 256$\to$512 tail tokens: all three models jump +14.7--23.0pp in a single budget doubling, crossing from near-baseline (${\sim}$73--79\%) to near-ceiling (${\sim}$94--96\%).
153	The threshold aligns with the typical exception traceback length (${\sim}$500 tokens): below it, the diagnostic event is truncated; above it, the event is captured regardless of architecture or scale.
154	Beyond 512 tokens, all models converge into a tight 96.5--96.6\% band at tail-1024, eliminating the 6.3pp cross-model spread observed at tail-256 (Table~\ref{tab:tail_cross_model}).
155	\texttt{tail\_2048} captures 95--98\% of \texttt{exception\_only}'s accuracy across all tested configurations.
156	The residual 2--5pp gap confirms that semantic extraction (identifying exception type and message) still outperforms positional extraction (retaining a fixed window containing non-diagnostic lines).
157	
158	\paragraph{Calibration.}
159	\label{sec:calibration}
160	Calibration mirrors the tier hierarchy: \texttt{exception\_only} ECE = 0.0027 vs.\ \texttt{no\_trace} ECE = 0.171, a 63$\times$ gap (Appendix~\ref{sec:calibration_full}).
161	
162	\paragraph{Error orthogonality.}
163	\texttt{exception\_only}'s 2 errors have zero overlap with all other conditions' error sets (Jaccard = 0.000), confirming it operates on an independent signal dimension (Appendix~\ref{sec:error_overlap}).
164	
165	\paragraph{Exception type breakdown.}
166	A per-exception-type breakdown (Appendix~\ref{sec:exception_type}) confirms that all standard exception types achieve 100\% accuracy; the only failures arise from \texttt{GeneratorExit}, a benign \texttt{BaseException} subclass.
167	
168	\paragraph{Cross-dataset generalization.}
169	\label{sec:debugbench}
170	On DebugBench \citep{tian2024debugbench} ($N{=}426$), the ranking is preserved: \texttt{exception\_only} 100\%, VOTA 99.77\%, \texttt{no\_trace} 96.71\%; narrow margins reflect a ceiling effect from structurally distinctive mutations (Appendix~\ref{sec:debugbench_full}).
171	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "ae5a4d83-4dae-4044-92ed-0a6f5e105665",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\nWe evaluate across two research questions:\n(1)~Do Tier~1 exception signals generalize across models?\n(2)~What is the relative contribution of each trace component?\nAll experiments use $N{=}1{,}190$ test samples; accuracy is reported with Wilson 95\\% CIs.\nPairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42); all differences are significant at $p{<}0.0001$ unless noted.\n\n\\subsection{Cross-Model Comparison}\n\\label{sec:cross_model}\n\nTable~\\ref{tab:cross_model} compares four models spanning an 8.7$\\times$ parameter range (1.5B--13B) and three architecture families (Qwen, DeepSeek, CodeLlama) under key conditions.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model verdict accuracy (\\%, $N{=}1{,}190$). Bold: best accuracy per model. Multi-seed entries show mean$\\pm$std (3 seeds). $^\\dag$2/3 seeds; one seed excluded due to LoRA initialization failure (91.09\\%, fail recall = 70.5\\%; see Appendix~\\ref{sec:training_dynamics}). \\texttt{ae\\_only} and \\texttt{loop\\_only} ablations tested on Qwen-7B (3 seeds) to isolate component contributions; cross-model validation focused on the primary conditions. Full CIs in Appendix~\\ref{sec:full_results}.}\n\\label{tab:cross_model}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Qwen-7B} & \\textbf{Qwen-1.5B} & \\textbf{CL-13B} & \\textbf{DS-6.7B} \\\\\n\\midrule\nexception\\_only & \\textbf{99.83}{\\scriptsize$\\pm$0.00} & \\textbf{99.83} & \\textbf{99.89}{\\scriptsize$\\pm$0.10} & \\textbf{99.33}$^\\dag$ \\\\\nae\\_only & 99.64{\\scriptsize$\\pm$0.49} & --- & --- & --- \\\\\nVOTA & 99.41 & 99.58 & 98.57 & 84.45 \\\\\nno\\_trace & 75.13 & 67.31 & 76.50 & 73.36 \\\\\n\\midrule\nMajority baseline & \\multicolumn{4}{c}{71.51} \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\paragraph{Exception dominance across families.}\nUnder \\texttt{exception\\_only}, the Qwen and CodeLlama families achieve ${\\geq}$99.83\\% (mean): Qwen-7B (99.83\\%$\\pm$0.00, 3 seeds), Qwen-1.5B (99.83\\%), and CodeLlama-13B (99.89\\%$\\pm$0.10, 3 seeds; seed 123 achieves 100\\%).\nDeepSeek-6.7B reaches 99.33\\% on 2/3 seeds with one LoRA-sensitivity outlier at 91.09\\% (seed 123; fail recall = 70.5\\%); even the outlier outperforms VOTA (84.45\\%) by 6.64pp.\nExcluding the DeepSeek outlier, the cross-model range is 0.56pp (99.33--99.89\\%), the tightest of any condition.\n\n\\paragraph{Scale invariance of exception signals.}\nException-based accuracy is shared by models spanning 1.5B to 13B parameters (8.7$\\times$): both Qwen-1.5B and CodeLlama-13B achieve 99.83\\%+ on the same representation.\nCodeLlama-13B seed 123 achieves 100\\% (0/1190 errors), confirming that Qwen's two persistent errors (from \\texttt{GeneratorExit}; Appendix~\\ref{sec:irreducible}) are high-probability convergence artifacts rather than hard data limitations.\nIn contrast, \\texttt{no\\_trace} scales monotonically with capacity: 67.31\\% (1.5B) $\\to$ 75.13\\% (7B) $\\to$ 76.50\\% (13B), a 9.19pp range that exception events completely eliminate (Figure~\\ref{fig:cross_scale}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_cross_model_gap}\n\\caption{Verdict accuracy vs.\\ model scale. \\texttt{exception\\_only} maintains ${\\geq}$99.33\\% regardless of scale (1.5B--13B), while \\texttt{no\\_trace} shows monotonic scale sensitivity (+9.19pp from 1.5B to 13B). The \\texttt{nomarker} condition (format markers removed) shows no degradation at smaller scale (${\\sim}$97.7--97.8\\%).}\n\\label{fig:cross_scale}\n\\end{figure}\n\n\\paragraph{VOTA cross-family variation.}\nVOTA accuracy varies across families: 99.58\\% (Qwen-1.5B) $>$ 99.41\\% (Qwen-7B) $>$ 98.57\\% (CodeLlama-13B; \\texttt{codellama13b\\_vota\\_seed42}, CI [97.9, 99.2]) $\\gg$ 84.45\\% (DeepSeek-6.7B).\nThe CodeLlama result (17 errors) narrows the gap: among models without tokenizer-driven truncation, the VOTA range is only 1.01pp (98.57--99.58\\%), suggesting that the 14.96pp DeepSeek deficit is primarily a truncation artifact rather than an inherent model capability limitation (91.7\\% of DeepSeek training samples were affected; Appendix~\\ref{sec:tokenizer_analysis}).\nIn contrast, \\texttt{exception\\_only} inputs are compact (median 150 tokens, mean 398 due to verbose fail-class exceptions), making the cross-model comparison clean.\n\n\\subsection{Component Ablation}\n\\label{sec:ablation}\n\nWe restrict \\texttt{ae\\_only} and \\texttt{loop\\_only} ablations to Qwen-7B, as these component-level analyses target the trace composition mechanism rather than cross-model generalization.\nTable~\\ref{tab:ablation} decomposes VOTA on Qwen-2.5-7B (seed=42) and reveals a two-tier hierarchy.\n\n\\begin{table}[t]\n\\centering\n\\caption{Component ablation on Qwen-2.5-7B ($N{=}1{,}190$). Tier~1 signals achieve near-perfect accuracy; combining them (VOTA) slightly dilutes performance. $^\\dag$\\texttt{ae\\_only}: 3-seed mean 99.64\\% ($\\pm$0.49; seeds 42: 99.92, 123: 99.08, 456: 99.92). \\texttt{exception\\_only}: 99.83\\% ($\\pm$0.00, 3 seeds), more stable ($\\sigma{=}$0 vs.\\ $\\sigma{=}$0.49).}\n\\label{tab:ablation}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Components} & \\textbf{Acc (\\%)} & \\textbf{95\\% CI} & \\textbf{Tier} \\\\\n\\midrule\nae\\_only & assertion-point & 99.64$^\\dag$ & [99.26, 99.87] & 1 \\\\\nexception\\_only & exception events & \\textbf{99.83} & [99.58, 100.00] & 1 \\\\\nVOTA & exc+ae+loop & 99.41 & [98.82, 99.83] & --- \\\\\nVOTA\\_no\\_ae & exc+loop & 99.41 & [98.90, 99.80] & --- \\\\\nloop\\_only & loop compression & 85.63 & [83.53, 87.56] & 2 \\\\\nfull\\_trace & complete trace & 81.76 & [79.70, 83.90] & --- \\\\\nno\\_trace & none & 75.13 & [72.77, 77.48] & --- \\\\\n\\midrule\nRegex (best) & exc.\\ type regex & 93.61 & --- & --- \\\\\n3-shot (Qwen-7B) & in-context learning & 90.84 & --- & --- \\\\\nZero-shot (4 models) & prompting & 51.0--93.5 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nTier~1 signals are individually sufficient: \\texttt{ae\\_only} (3-seed mean 99.64\\% $\\pm$ 0.49) and \\texttt{exception\\_only} (99.83\\% $\\pm$ 0.00) both exceed VOTA ($p{=}0.01$), implying that combining signals introduces noise; \\texttt{exception\\_only} is more stable across seeds ($\\sigma{=}$0 vs.\\ $\\sigma{=}$0.49).\nRemoving assertion points has no effect (\\texttt{VOTA\\_no\\_ae} = 99.41\\%), confirming exception dominance.\nTier~2 \\texttt{loop\\_only} (85.63\\%) improves 10.50pp over \\texttt{no\\_trace} ($p{<}0.0001$) but falls far short of Tier~1.\n\\paragraph{Rule-based baseline comparison.}\nThe strongest non-trivial regex heuristic (B4: exception class name matching) achieves 93.61\\% accuracy (F1=0.876), trailing SFT \\texttt{exception\\_only} (99.83\\%, F1=0.997) by 6.22pp (McNemar $p{<}0.001$).\nThe gap concentrates on caught-exception boundary cases: regex flags all exception events as failures, while SFT learns to distinguish caught exceptions (benign, inside \\texttt{try/except}) from uncaught faults, correctly resolving 6/8 boundary samples (Appendix~\\ref{sec:regex_baselines}).\nAcross trace formats, SFT consistently outperforms the best applicable regex, from +3.62pp (\\texttt{no\\_trace} over majority baseline) to +23.86pp (VOTA), with the largest gains on formats requiring semantic interpretation (Appendix~\\ref{sec:regex_baselines}).\n\n\\paragraph{Zero-shot and few-shot LLM baselines.}\nZero-shot prompting spans 51.0--93.5\\% across four models (CodeLlama-13B: 51.01\\%, Qwen-7B: 89.08\\%, DeepSeek-6.7B: 90.59\\%, Qwen-1.5B: 93.45\\%), a 42.44pp range that SFT compresses to 0.56pp (99.33--99.89\\%).\nZero-shot performance does not correlate with model size: Qwen-1.5B (93.45\\%) outperforms both Qwen-7B (89.08\\%) and CodeLlama-13B (51.01\\%), indicating that pretraining data distribution, not capacity, determines zero-shot verdict ability.\nCodeLlama-13B drops below the majority baseline (71.51\\%), showing extreme fail bias (72.4\\% of predictions are \\texttt{fail}).\nThree-shot in-context learning on Qwen-7B (90.84\\%, fail recall = 80.53\\%) improves only 1.76pp over zero-shot and still trails both the regex heuristic (93.61\\%) and SFT by 8.99pp, confirming that a few examples cannot substitute for task-specific fine-tuning.\nSFT normalizes this cross-architecture variance, closing a 6--49pp gap to ${\\geq}$99.33\\% across all models with 4,720 training samples (Appendix~\\ref{sec:zeroshot_cross_model}).\n\n\\subsection{Format Marker Ablation}\n\\label{sec:nomarker}\n\nThe \\texttt{exception\\_only} format includes a \\texttt{[No exception data in trace]} marker in all pass-class samples (regex baseline B5 exploits this for 99.33\\% accuracy; Appendix~\\ref{sec:regex_baselines}).\nTo quantify the marker's contribution, we retrain with all format markers removed (\\texttt{nomarker} condition).\n\nQwen-7B 3-seed mean: 97.65\\% $\\pm$ 0.96 (seeds 42/123/456: 96.55/98.32/98.07\\%), a drop of 2.18pp from \\texttt{exception\\_only} (99.83\\%).\nQwen-1.5B: 97.82\\%, drop of 2.01pp.\nThe marker contribution (${\\sim}$2pp) accounts for only ${\\sim}$9\\% of the total exception lift over \\texttt{no\\_trace} (24.70pp on 7B).\nException events thus provide two signal layers that show no degradation at smaller scale: structural markers (${\\sim}$2pp, regex-learnable) and semantic exception content (${\\sim}$22pp, requiring SFT to distinguish caught from uncaught exceptions).\n\n\\subsection{Information Density Decomposition}\n\\label{sec:density}\n\nThe 17.65pp gap between \\texttt{full\\_trace} (81.76\\%) and VOTA (99.41\\%) decomposes via \\texttt{full\\_trace\\_label\\_only}, which retains the full trace but masks all trace tokens from the loss.\n\n\\begin{table}[t]\n\\centering\n\\caption{Approximate information density decomposition: gradient dilution (${\\sim}$26\\%) vs.\\ information overload (${\\sim}$74\\%).}\n\\label{tab:density}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Acc (\\%)} & \\textbf{$\\Delta$ vs.\\ full\\_trace} & \\textbf{Gap explained} \\\\\n\\midrule\nfull\\_trace & 81.76 & --- & --- \\\\\nlabel\\_only & 86.22 & +4.46pp & 26\\% \\\\\nVOTA & 99.41 & +17.65pp & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGradient dilution accounts for approximately 26\\% of the gap (+4.46pp, $p{<}0.0001$, bootstrap 95\\% CI $[{+}2.35, {+}6.55]$): when the model no longer wastes gradient updates on predicting trace tokens, accuracy improves even with identical input.\nThe remaining ${\\sim}$74\\% (+13.19pp) reflects information overload at inference: the model receives thousands of irrelevant trace lines that compete for attention with the diagnostic signal, regardless of loss design.\nThis asymmetry implies that trace compression methods should prioritize \\emph{content selection} (removing irrelevant lines) over \\emph{loss engineering} (masking non-target tokens), as the larger bottleneck is what the model sees, not how it is trained.\nThe two factors may interact, so this decomposition is approximate.\n\n\\subsection{Additional Analyses}\n\\label{sec:additional}\n\n\\paragraph{Trace length ablation.}\n\\label{sec:trace_length}\nVarying the head-truncated trace token budget (256--no limit) on Qwen-7B yields accuracy in a narrow 77.2\\%--81.8\\% band with a non-monotonic pattern: 1024-token prefixes (77.23\\%) underperform 512-token prefixes (80.42\\%, $p{=}0.002$), because mid-length prefixes retain enough irrelevant content to mislead the model while discarding diagnostic events near the trace terminus (Appendix~\\ref{sec:trace_length_full}).\nThis non-monotonicity is specific to head-truncation; under tail-truncation, accuracy increases monotonically for two of three models (Table~\\ref{tab:tail_cross_model} in Appendix), with only DeepSeek showing a mild architecture-specific reversal at tail-1024$\\to$tail-2048 ($-$1.5pp).\n\n\\paragraph{Truncation direction and budget curve.}\nTail-truncation (retaining the last $k$ tokens) dramatically outperforms head-truncation across all three models: tail-2048 exceeds head-2048 by 15.5--22.6pp, with the gap widening at smaller scale (Qwen-1.5B: +22.6pp vs.\\ Qwen-7B: +15.5pp; Appendix~\\ref{sec:trace_length_full}, Table~\\ref{tab:head_vs_tail}).\n\nA full cross-model budget sweep reveals a sharp phase transition at 256$\\to$512 tail tokens: all three models jump +14.7--23.0pp in a single budget doubling, crossing from near-baseline (${\\sim}$73--79\\%) to near-ceiling (${\\sim}$94--96\\%).\nThe threshold aligns with the typical exception traceback length (${\\sim}$500 tokens): below it, the diagnostic event is truncated; above it, the event is captured regardless of architecture or scale.\nBeyond 512 tokens, all models converge into a tight 96.5--96.6\\% band at tail-1024, eliminating the 6.3pp cross-model spread observed at tail-256 (Table~\\ref{tab:tail_cross_model}).\n\\texttt{tail\\_2048} captures 95--98\\% of \\texttt{exception\\_only}'s accuracy across all tested configurations.\nThe residual 2--5pp gap confirms that semantic extraction (identifying exception type and message) still outperforms positional extraction (retaining a fixed window containing non-diagnostic lines).\n\n\\paragraph{Calibration.}\n\\label{sec:calibration}\nCalibration mirrors the tier hierarchy: \\texttt{exception\\_only} ECE = 0.0027 vs.\\ \\texttt{no\\_trace} ECE = 0.171, a 63$\\times$ gap (Appendix~\\ref{sec:calibration_full}).\n\n\\paragraph{Error orthogonality.}\n\\texttt{exception\\_only}'s 2 errors have zero overlap with all other conditions' error sets (Jaccard = 0.000), confirming it operates on an independent signal dimension (Appendix~\\ref{sec:error_overlap}).\n\n\\paragraph{Exception type breakdown.}\nA per-exception-type breakdown (Appendix~\\ref{sec:exception_type}) confirms that all standard exception types achieve 100\\% accuracy; the only failures arise from \\texttt{GeneratorExit}, a benign \\texttt{BaseException} subclass.\n\n\\paragraph{Cross-dataset generalization.}\n\\label{sec:debugbench}\nOn DebugBench \\citep{tian2024debugbench} ($N{=}426$), the ranking is preserved: \\texttt{exception\\_only} 100\\%, VOTA 99.77\\%, \\texttt{no\\_trace} 96.71\\%; narrow margins reflect a ceiling effect from structurally distinctive mutations (Appendix~\\ref{sec:debugbench_full}).\n",
      "numLines": 171,
      "startLine": 1,
      "totalLines": 171
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_015Z5cULykMoLfX7PQt2UgTi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "0f87e49e-d35e-4801-a5dc-e005bf5b5366",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UN4WtbzQNNJFf2q7USMiMu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2622,
      "cache_read_input_tokens": 24835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2622
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

_source line 14 · 2026-05-18T01:47:23.157Z_

<details><summary>↩ Tool result · `toolu_015Z5cULykMoLfX7PQt2UgTi`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[review]{acl}
3	% \usepackage{acl}  % uncomment for camera-ready (remove [review])
4	\usepackage{times,latexsym}
5	\usepackage{amsmath,amssymb}
6	\usepackage{graphicx}
7	\graphicspath{{../../figures/paper/}}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	
12	\title{Exception Events Are All You Need: \\Component Ablation for Trace-Based Verdict Prediction}
13	\author{Anonymous ACL submission}
14	
15	\begin{document}
16	\maketitle
17	
18	\begin{abstract}
19	Execution traces are increasingly used to enhance code language models, but which trace components matter for downstream tasks remains poorly understood.
20	We present the first systematic component ablation of trace representations for verdict prediction (classifying whether a test passes or fails) across four models spanning three architecture families and 1.5B to 13B parameters.
21	Exception events alone achieve ${\geq}$99.33\% accuracy across all four models (${\geq}$99.83\% on three of four; one seed reaches 100\%), while a code-only baseline shows 9.19pp scale sensitivity (67.3--76.5\%).
22	Adding more trace information actively hurts: a multi-component representation underperforms exception-only, and the full-trace gap approximately decomposes into information overload (${\sim}$74\%) and gradient dilution (${\sim}$26\%).
23	Tail-truncation experiments reveal that diagnostic signal concentrates near the trace terminus (in a localized window, not the absolute end), recovering 86\% of the gap to exception-only.
24	A format-marker ablation confirms ${\sim}$91\% of the exception signal is semantic (learned by SFT to distinguish caught from uncaught exceptions) rather than format-driven.
25	These results reveal a two-tier diagnostic hierarchy: Tier~1 signals (exception events, assertion points) individually achieve ${\geq}$99\%, while Tier~2 (loop compression) reaches 85.6\%.
26	Cross-dataset evaluation on DebugBench ($N{=}426$) confirms generalization, with exception-only achieving 100\%.
27	We reframe verdict prediction as fault detection: the minimal sufficient signal is a compact exception event (median 150 tokens) that is scale-invariant, architecture-independent, and deployable in token-constrained settings.
28	\end{abstract}
29	
30	\input{introduction}
31	\input{method}
32	\input{experiments}
33	\input{discussion}
34	\input{related_work}
35	\input{conclusion}
36	
37	\section*{Limitations}
38	
39	Our study has several limitations.
40	First, our primary experiments use a single dataset (591 problems from HumanEval and MBPP-sanitized); while a cross-dataset evaluation on DebugBench (\S\ref{sec:debugbench}) confirms that exception dominance generalizes to synthetically injected bugs, generalization to other languages, larger codebases, or real-world fault distributions remains untested.
41	Second, while we evaluate four models spanning 1.5B to 13B parameters across three architecture families, all are code-specialized; generalization to general-purpose models or larger scales remains untested.
42	Third, DeepSeek \texttt{exception\_only} exhibits seed-dependent variance: 2/3 seeds achieve 99.33\% while seed 123 yields 91.09\% ($\sigma{=}4.76$pp, $n{=}3$), which we hypothesize reflects LoRA initialization sensitivity in DeepSeek-Coder, though direct evidence is lacking (fail recall = 70.5\% for the outlier vs.\ 100\% for others).
43	Qwen \texttt{exception\_only} shows perfect seed robustness ($\sigma{=}0$, $n{=}3$), but Qwen \texttt{ae\_only} also exhibits seed variance ($\sigma{=}$0.40pp; seed 123 = 99.08\% vs.\ seeds 42/456 = 99.92\%), though far smaller than DeepSeek's ($\sigma{=}$4.76pp).
44	Whether training stabilization techniques can eliminate DeepSeek's seed sensitivity is unexplored; other conditions use a single seed.
45	Fourth, the initial DeepSeek \texttt{full\_trace} run was invalidated by context overflow; a re-run with extended context yields 79.16\% (CI [76.80\%, 81.30\%]), 2.60pp below Qwen (Table~\ref{tab:cross_model}).
46	Fifth, the candidate solutions were generated by Qwen-2.5-Coder-7B-Instruct, which also serves as one of our evaluation models; this does not affect verdict prediction but may influence the pass/fail distribution.
47	Sixth, self-familiarity bias may inflate absolute accuracy: both Qwen-2.5-Coder and DeepSeek-Coder were likely exposed to HumanEval and MBPP solutions during pretraining, so the models may partially recognize solutions rather than purely reasoning from trace signals; our cross-dataset evaluation on DebugBench mitigates but does not eliminate this concern.
48	Seventh, the error distribution in our test set may not reflect real-world fault distributions: exceptions (especially \texttt{TypeError}, \texttt{ValueError}) dominate LLM-generated failures, but production code may exhibit a broader spectrum of silent logic errors where no exception is raised, potentially reducing the effectiveness of exception-based verdict prediction.
49	Finally, our analysis is limited to verdict prediction; whether exception dominance extends to other classification tasks or generation tasks is an open question.
50	
51	\section*{Ethics Statement}
52	
53	This work uses publicly available benchmarks (HumanEval, MBPP-sanitized, DebugBench) and does not involve human subjects, crowdsourced annotations, or personally identifiable information.
54	All models evaluated are open-source and publicly accessible.
55	Training uses parameter-efficient LoRA fine-tuning on two RTX PRO 6000 Blackwell GPUs, with each experiment using a single GPU and total compute under 20 GPU-hours across all experiments, resulting in minimal environmental impact.
56	We do not foresee direct negative societal impacts from this work; verdict prediction is a developer-facing tool for automated testing.
57	
58	\bibliography{references}
59	
60	\appendix
61	\input{appendix}
62	
63	\end{document}
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "5d73812b-2e0d-4eb7-b235-b74003d336c7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex",
      "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[review]{acl}\n% \\usepackage{acl}  % uncomment for camera-ready (remove [review])\n\\usepackage{times,latexsym}\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\graphicspath{{../../figures/paper/}}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\n\\title{Exception Events Are All You Need: \\\\Component Ablation for Trace-Based Verdict Prediction}\n\\author{Anonymous ACL submission}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nExecution traces are increasingly used to enhance code language models, but which trace components matter for downstream tasks remains poorly understood.\nWe present the first systematic component ablation of trace representations for verdict prediction (classifying whether a test passes or fails) across four models spanning three architecture families and 1.5B to 13B parameters.\nException events alone achieve ${\\geq}$99.33\\% accuracy across all four models (${\\geq}$99.83\\% on three of four; one seed reaches 100\\%), while a code-only baseline shows 9.19pp scale sensitivity (67.3--76.5\\%).\nAdding more trace information actively hurts: a multi-component representation underperforms exception-only, and the full-trace gap approximately decomposes into information overload (${\\sim}$74\\%) and gradient dilution (${\\sim}$26\\%).\nTail-truncation experiments reveal that diagnostic signal concentrates near the trace terminus (in a localized window, not the absolute end), recovering 86\\% of the gap to exception-only.\nA format-marker ablation confirms ${\\sim}$91\\% of the exception signal is semantic (learned by SFT to distinguish caught from uncaught exceptions) rather than format-driven.\nThese results reveal a two-tier diagnostic hierarchy: Tier~1 signals (exception events, assertion points) individually achieve ${\\geq}$99\\%, while Tier~2 (loop compression) reaches 85.6\\%.\nCross-dataset evaluation on DebugBench ($N{=}426$) confirms generalization, with exception-only achieving 100\\%.\nWe reframe verdict prediction as fault detection: the minimal sufficient signal is a compact exception event (median 150 tokens) that is scale-invariant, architecture-independent, and deployable in token-constrained settings.\n\\end{abstract}\n\n\\input{introduction}\n\\input{method}\n\\input{experiments}\n\\input{discussion}\n\\input{related_work}\n\\input{conclusion}\n\n\\section*{Limitations}\n\nOur study has several limitations.\nFirst, our primary experiments use a single dataset (591 problems from HumanEval and MBPP-sanitized); while a cross-dataset evaluation on DebugBench (\\S\\ref{sec:debugbench}) confirms that exception dominance generalizes to synthetically injected bugs, generalization to other languages, larger codebases, or real-world fault distributions remains untested.\nSecond, while we evaluate four models spanning 1.5B to 13B parameters across three architecture families, all are code-specialized; generalization to general-purpose models or larger scales remains untested.\nThird, DeepSeek \\texttt{exception\\_only} exhibits seed-dependent variance: 2/3 seeds achieve 99.33\\% while seed 123 yields 91.09\\% ($\\sigma{=}4.76$pp, $n{=}3$), which we hypothesize reflects LoRA initialization sensitivity in DeepSeek-Coder, though direct evidence is lacking (fail recall = 70.5\\% for the outlier vs.\\ 100\\% for others).\nQwen \\texttt{exception\\_only} shows perfect seed robustness ($\\sigma{=}0$, $n{=}3$), but Qwen \\texttt{ae\\_only} also exhibits seed variance ($\\sigma{=}$0.40pp; seed 123 = 99.08\\% vs.\\ seeds 42/456 = 99.92\\%), though far smaller than DeepSeek's ($\\sigma{=}$4.76pp).\nWhether training stabilization techniques can eliminate DeepSeek's seed sensitivity is unexplored; other conditions use a single seed.\nFourth, the initial DeepSeek \\texttt{full\\_trace} run was invalidated by context overflow; a re-run with extended context yields 79.16\\% (CI [76.80\\%, 81.30\\%]), 2.60pp below Qwen (Table~\\ref{tab:cross_model}).\nFifth, the candidate solutions were generated by Qwen-2.5-Coder-7B-Instruct, which also serves as one of our evaluation models; this does not affect verdict prediction but may influence the pass/fail distribution.\nSixth, self-familiarity bias may inflate absolute accuracy: both Qwen-2.5-Coder and DeepSeek-Coder were likely exposed to HumanEval and MBPP solutions during pretraining, so the models may partially recognize solutions rather than purely reasoning from trace signals; our cross-dataset evaluation on DebugBench mitigates but does not eliminate this concern.\nSeventh, the error distribution in our test set may not reflect real-world fault distributions: exceptions (especially \\texttt{TypeError}, \\texttt{ValueError}) dominate LLM-generated failures, but production code may exhibit a broader spectrum of silent logic errors where no exception is raised, potentially reducing the effectiveness of exception-based verdict prediction.\nFinally, our analysis is limited to verdict prediction; whether exception dominance extends to other classification tasks or generation tasks is an open question.\n\n\\section*{Ethics Statement}\n\nThis work uses publicly available benchmarks (HumanEval, MBPP-sanitized, DebugBench) and does not involve human subjects, crowdsourced annotations, or personally identifiable information.\nAll models evaluated are open-source and publicly accessible.\nTraining uses parameter-efficient LoRA fine-tuning on two RTX PRO 6000 Blackwell GPUs, with each experiment using a single GPU and total compute under 20 GPU-hours across all experiments, resulting in minimal environmental impact.\nWe do not foresee direct negative societal impacts from this work; verdict prediction is a developer-facing tool for automated testing.\n\n\\bibliography{references}\n\n\\appendix\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 64,
      "startLine": 1,
      "totalLines": 64
    }
  }
}
```

</details>

---

### Assistant

_source line 15_

现在读 appendix 检查 tail budget curve 表格和 head-tail 对比表格是否存在。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "42be5ba0-a9be-4ea6-bfb3-570592d3c2ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7QMRBB37qnGCTTU6ro5DJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7244,
      "cache_read_input_tokens": 27457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7244
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

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_013FEgLUMdLK7e4hDMXDeyfv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "69cb8bc3-d724-4892-9302-4c5921b82611",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7QMRBB37qnGCTTU6ro5DJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7244,
      "cache_read_input_tokens": 27457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7244
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

_source line 17 · 2026-05-18T01:47:33.578Z_

<details><summary>↩ Tool result · `toolu_013FEgLUMdLK7e4hDMXDeyfv`</summary>

```text
1	\section{Per-Class Performance Breakdown}
2	\label{sec:per_class}
3	
4	Table~\ref{tab:per_class} reports per-class precision, recall, and F1 for all experimental conditions.
5	
6	\begin{table*}[t]
7	\centering
8	\caption{Per-class precision, recall, and F1 for all experimental conditions (seed 42). DeepSeek VOTA achieves 100\% fail precision but only 45.4\% fail recall, indicating systematic bias toward predicting \texttt{pass}. DeepSeek \texttt{exception\_only} seed 42 achieves 100\% fail recall, but seed 123 drops to 70.5\% (see Table~\ref{tab:full_deepseek}).}
9	\label{tab:per_class}
10	\small
11	\begin{tabular}{llccccccc}
12	\toprule
13	\textbf{Condition} & \textbf{Model} & \textbf{Acc} & \textbf{Pass P} & \textbf{Pass R} & \textbf{Pass F1} & \textbf{Fail P} & \textbf{Fail R} & \textbf{Fail F1} \\
14	\midrule
15	No Trace          & Qwen-2.5-7B & 75.13 & 87.76 & 75.79 & 81.34 & 54.73 & 73.45 & 62.72 \\
16	Full Trace        & Qwen-2.5-7B & 81.76 & 87.74 & 86.60 & 87.17 & 67.43 & 69.62 & 68.51 \\
17	Full Trace (LO)   & Qwen-2.5-7B & 86.22 & 88.21 & 93.18 & 90.63 & 80.07 & 68.73 & 73.97 \\
18	VOTA              & Qwen-2.5-7B & 99.41 & 100.00 & 99.18 & 99.59 & 97.98 & 100.00 & 98.98 \\
19	Exception Only    & Qwen-2.5-7B & 99.83 & 100.00 & 99.76 & 99.88 & 99.41 & 100.00 & 99.71 \\
20	AE Only           & Qwen-2.5-7B & 99.92 & 100.00 & 99.88 & 99.94 & 99.71 & 100.00 & 99.85 \\
21	Loop Only         & Qwen-2.5-7B & 85.63 & 92.39 & 87.07 & 89.66 & 71.65 & 82.01 & 76.48 \\
22	VOTA\_no\_ae       & Qwen-2.5-7B & 99.41 & 99.88 & 99.29 & 99.59 & 98.26 & 99.71 & 98.98 \\
23	\midrule
24	No Trace          & DeepSeek-6.7B & 73.36 & 81.71 & 80.85 & 81.28 & 53.16 & 54.57 & 53.86 \\
25	Full Trace        & DeepSeek-6.7B & 79.16 & 85.70 & 85.10 & 85.40 & 63.20 & 64.30 & 63.70 \\
26	VOTA              & DeepSeek-6.7B & 84.45 & 82.14 & 100.00 & 90.20 & 100.00 & 45.40 & 62.50 \\
27	Exception Only    & DeepSeek-6.7B & 99.33 & 100.00 & 99.06 & 99.53 & 97.69 & 100.00 & 98.83 \\
28	\bottomrule
29	\end{tabular}
30	\end{table*}
31	
32	%% ============================================================
33	\section{Training Details}
34	\label{sec:training_details}
35	
36	Table~\ref{tab:hyperparams} summarizes the training hyperparameters shared across all conditions.
37	All experiments use the HuggingFace TRL \texttt{SFTTrainer} with LoRA \citep{hu2022lora} applied to all linear layers.
38	
39	\begin{table}[t]
40	\centering
41	\caption{Training hyperparameters (shared across all conditions).}
42	\label{tab:hyperparams}
43	\small
44	\resizebox{\columnwidth}{!}{%
45	\begin{tabular}{ll}
46	\toprule
47	\textbf{Hyperparameter} & \textbf{Value} \\
48	\midrule
49	LoRA rank ($r$)            & 16 \\
50	LoRA alpha ($\alpha$)      & 32 \\
51	LoRA dropout               & 0.05 \\
52	LoRA target modules        & all linear layers \\
53	\midrule
54	Epochs                     & 3 \\
55	Per-device batch size       & 4 \\
56	Gradient accumulation steps & 8 \\
57	Effective batch size        & 32 \\
58	\midrule
59	Learning rate               & $2 \times 10^{-4}$ \\
60	LR scheduler                & linear decay \\
61	Warmup ratio                & 0.1 \\
62	Weight decay                & 0.01 \\
63	\midrule
64	Max sequence length         & 2048 tokens \\
65	Primary seed                & 42 \\
66	Robustness seeds            & 123, 456 \\
67	\midrule
68	Hardware                    & 1$\times$ RTX PRO 6000 Blackwell (96\,GB VRAM) \\
69	Framework                   & HuggingFace TRL SFTTrainer \\
70	\bottomrule
71	\end{tabular}%
72	}
73	\end{table}
74	
75	Table~\ref{tab:train_time} reports per-condition training wall-clock times.
76	Conditions with longer trace inputs (e.g., \texttt{full\_trace}, VOTA) require proportionally more training time due to increased sequence lengths.
77	
78	\begin{table}[t]
79	\centering
80	\caption{Training wall-clock time per condition on a single RTX PRO 6000 Blackwell GPU. Where multiple seeds were run, individual times are listed.}
81	\label{tab:train_time}
82	\small
83	\begin{tabular}{llr}
84	\toprule
85	\textbf{Condition} & \textbf{Seed(s)} & \textbf{Time (h)} \\
86	\midrule
87	no\_trace       & 42         & ${\sim}$0.5 \\
88	full\_trace     & 42         & ${\sim}$2.2 \\
89	label\_only     & 42         & ${\sim}$2.2 \\
90	VOTA                     & 42         & ${\sim}$2.3 \\
91	exception\_only & 42         & ${\sim}$2.1 \\
92	exception\_only & 123        & ${\sim}$2.1 \\
93	exception\_only & 456        & ${\sim}$1.3 \\
94	ae\_only        & 42         & ${\sim}$1.8 \\
95	loop\_only      & 42         & ${\sim}$2.1 \\
96	VOTA\_no\_ae    & 42         & ${\sim}$1.8 \\
97	\bottomrule
98	\end{tabular}
99	\end{table}
100	
101	%% ============================================================
102	\section{VOTA Trace Examples}
103	\label{sec:vota_examples}
104	
105	We provide two representative VOTA trace examples illustrating the fail and pass cases.
106	In the fail case, the exception event provides an unambiguous fault signal.
107	In the pass case, the absence of an exception event combined with a matching assertion point confirms correct execution.
108	
109	\paragraph{Fail example.}
110	A \texttt{ZeroDivisionError} triggers an \texttt{[ERROR]} event, providing a direct fault signal that is sufficient for the model to predict \texttt{fail}.
111	
112	\begin{small}
113	\begin{verbatim}
114	## Function
115	def divide(a, b):
116	    return a / b
117	
118	## Test Input
119	divide(1, 0)
120	
121	## Expected Output
122	inf
123	
124	## VOTA Trace
125	[ERROR] ZeroDivisionError: division by zero
126	
127	## Verdict
128	fail
129	\end{verbatim}
130	\end{small}
131	
132	\paragraph{Pass example.}
133	No exception is raised, and the assertion point confirms that the actual output matches the expected value.
134	
135	\begin{small}
136	\begin{verbatim}
137	## Function
138	def add(a, b):
139	    return a + b
140	
141	## Test Input
142	add(2, 3)
143	
144	## Expected Output
145	5
146	
147	## VOTA Trace
148	[LOOP] No loops detected.
149	[ASSERT] actual=5, expected=5
150	
151	## Verdict
152	pass
153	\end{verbatim}
154	\end{small}
155	
156	These examples illustrate the core asymmetry exploited by the \texttt{exception\_only} condition: fail cases produce an explicit \texttt{[ERROR]} event, while pass cases are characterized by its absence.
157	This binary signal (presence vs.\ absence of an exception) is sufficient for near-perfect verdict prediction.
158	
159	%% ============================================================
160	\section{Full Experimental Results}
161	\label{sec:full_results}
162	
163	Tables~\ref{tab:full_qwen} and \ref{tab:full_deepseek} report the complete experimental results across all conditions, models, and seeds.
164	
165	\begin{table}[t]
166	\centering
167	\caption{Full results for Qwen-2.5-Coder-7B across all conditions and seeds. Conditions with a single seed report no variance. \texttt{exception\_only} achieves 99.83\% across all three seeds ($\sigma{=}$0). \texttt{ae\_only} achieves 99.64\% mean ($\pm$0.49; seed 123 at 99.08\% is the outlier).}
168	\label{tab:full_qwen}
169	\small
170	\resizebox{\columnwidth}{!}{%
171	\begin{tabular}{lcccc}
172	\toprule
173	\textbf{Condition} & \textbf{S42} & \textbf{S123} & \textbf{S456} & \textbf{Mean $\pm$ Std} \\
174	\midrule
175	exception\_only & 99.83 & 99.83 & 99.83 & 99.83 $\pm$ 0.00 \\
176	ae\_only        & 99.92 & 99.08 & 99.92 & 99.64 $\pm$ 0.49 \\
177	VOTA                     & 99.41 & ---   & ---   & --- \\
178	VOTA\_no\_ae    & 99.41 & ---   & ---   & --- \\
179	label\_only     & 86.22 & ---   & ---   & --- \\
180	loop\_only      & 85.63 & ---   & ---   & --- \\
181	full\_trace     & 81.76 & ---   & ---   & --- \\
182	no\_trace       & 75.13 & ---   & ---   & --- \\
183	\bottomrule
184	\end{tabular}%
185	}
186	\end{table}
187	
188	\begin{table}[t]
189	\centering
190	\caption{Full results for DeepSeek-Coder-6.7B across all conditions and seeds. \texttt{exception\_only} shows bimodal seed behavior: seeds 42 and 456 achieve 99.33\%, while seed 123 yields 91.09\% (LoRA initialization outlier, fail recall = 70.5\%).}
191	\label{tab:full_deepseek}
192	\small
193	\resizebox{\columnwidth}{!}{%
194	\begin{tabular}{llcc}
195	\toprule
196	\textbf{Condition} & \textbf{Seed} & \textbf{Accuracy} & \textbf{Notes} \\
197	\midrule
198	exception\_only & 42  & 99.33 & epoch 1: 99.83 \\
199	exception\_only & 456 & 99.33 & CI [98.82, 99.75] \\
200	exception\_only & 123 & 91.09 & fail recall = 70.5\%; CI [89.40, 92.60] \\
201	\midrule
202	VOTA                     & 42  & 84.45 & \\
203	no\_trace       & 42  & 73.36 & \\
204	full\_trace     & 42  & 79.16 & CI [76.80, 81.30] \\
205	\bottomrule
206	\end{tabular}%
207	}
208	\end{table}
209	
210	%% ============================================================
211	\section{Tokenizer and Truncation Analysis}
212	\label{sec:tokenizer_analysis}
213	
214	The VOTA cross-model gap (14.96pp, Table~\ref{tab:cross_model}; confounded by tokenizer-driven truncation; 91.7\% of DeepSeek training samples were affected) is driven by a training-time truncation asymmetry.
215	The DeepSeek tokenizer averages 2{,}626 tokens per VOTA sample versus 1{,}929 for Qwen, causing 91.7\% of DeepSeek VOTA training samples to exceed the 2{,}048-token context window.
216	The training framework preserves the verdict label but truncates trace content, so the model trains with incomplete diagnostic information for the majority of samples.
217	
218	A post-hoc group analysis provides directional evidence: partitioning DeepSeek VOTA test samples by whether their training-set counterparts exceeded the context window, intact samples ($N{=}99$) achieve 100\% accuracy while truncated samples ($N{=}1{,}091$) achieve 83.04\% (95\% CI [80.75\%, 85.24\%]; Fisher exact $p{<}0.001$), with all 185 errors concentrated in the fail class (fail recall = 31.23\%).
219	Per-class analysis (Table~\ref{tab:per_class}) confirms that DeepSeek VOTA achieves 100\% fail precision but only 45.43\% fail recall, systematically defaulting to \texttt{pass}---in contrast to Qwen VOTA, which achieves 100\% fail recall.
220	
221	Seed robustness diverges across models: Qwen \texttt{exception\_only} produces identical 99.83\% across all three seeds ($\sigma{=}0$), while DeepSeek shows bimodal behavior: seeds 42 and 456 achieve 99.33\% (fail recall = 100\%), seed 123 yields 91.09\% (fail recall = 70.5\%).
222	Because \texttt{exception\_only} test inputs contain 48.99\% duplicates (607 unique of 1,190; \S\ref{sec:dataset}), CIs assume $n{=}1{,}190$ independent trials; under deduplication ($n{=}607$), Qwen's accuracy is 99.67\% (Wilson CI [98.81, 99.91]).
223	
224	%% ============================================================
225	\section{Irreducible Sample Analysis}
226	\label{sec:irreducible}
227	
228	The \texttt{exception\_only} condition with Qwen-2.5-Coder-7B misclassifies exactly 2 out of 1,190 test samples across all three seeds (42, 123, 456), with 100\% overlap across seeds.
229	Both samples (IDs 901 and 905) share the following characteristics:
230	
231	\begin{itemize}
232	\item \textbf{Function:} \texttt{check\_dict\_case} (HumanEval/95)---a function that checks whether all dictionary keys are uniformly upper-case or lower-case strings.
233	\item \textbf{Ground-truth label:} \texttt{pass}.
234	\item \textbf{Predicted label:} \texttt{fail} (false negative).
235	\item \textbf{Cross-seed consistency:} Both samples are misclassified identically by all three seeds, indicating a systematic rather than stochastic error.
236	\end{itemize}
237	
238	Manual inspection reveals the root cause: \texttt{check\_dict\_case} uses \texttt{all()} over a generator expression, and Python's \texttt{all()} short-circuits on the first \texttt{True} value, raising \texttt{GeneratorExit} to terminate the generator.
239	Because \texttt{GeneratorExit} is a \texttt{BaseException} subclass, the tracer records it as seven \texttt{[ERROR] GeneratorExit} lines---even though the function executes correctly and the test passes.
240	The model observes these spurious error markers and reasonably but incorrectly predicts \texttt{fail}.
241	This is not a model failure but a representation ambiguity: the \texttt{exception\_only} format cannot distinguish genuine exceptions from benign \texttt{BaseException} subclasses triggered by Python's iterator protocol.
242	
243	Most configurations converge to these same 2 errors: Qwen-1.5B, Qwen-7B (3 seeds), CodeLlama-13B (seeds 42/456), and DeepSeek-6.7B (seeds 42/456) all produce error set $\{901, 905\}$.
244	However, CodeLlama-13B seed 123 achieves 100\% accuracy (0/1190 errors), correctly classifying both samples.
245	This demonstrates that 99.83\% is a near-perfect \emph{floor} (the convergence attractor for most LoRA initializations) rather than a hard data ceiling: the representation supports perfect accuracy, but most initializations converge to the same 2-error basin.
246	The practical implication is that these errors are high-probability convergence artifacts addressable through seed selection or ensemble methods, not fundamental limitations of the exception-based representation.
247	
248	%% ============================================================
249	\section{Exception Type Accuracy Breakdown}
250	\label{sec:exception_type}
251	
252	Table~\ref{tab:exception_type} reports \texttt{exception\_only} accuracy stratified by exception type on Qwen-2.5-7B (seed=42, $N{=}1{,}190$).
253	All standard exception types (\texttt{TypeError}, \texttt{ValueError}, \texttt{IndexError}, etc.) achieve 100\% accuracy.
254	The only misclassifications arise from \texttt{GeneratorExit}, a \texttt{BaseException} subclass that is not an \texttt{Exception}---it is raised by Python's iterator protocol during generator short-circuiting, not by actual program errors.
255	
256	\begin{table}[t]
257	\centering
258	\caption{Exception type accuracy breakdown for \texttt{exception\_only} (Qwen-7B, seed=42). All true error types achieve 100\%. The only failures come from \texttt{GeneratorExit} (a \texttt{BaseException} subclass, not an \texttt{Exception}), which appears in 2 passing samples.}
259	\label{tab:exception_type}
260	\small
261	\begin{tabular}{lcc}
262	\toprule
263	\textbf{Exception Type} & \textbf{Samples} & \textbf{Accuracy} \\
264	\midrule
265	TypeError & 96 & 100\% \\
266	ValueError & 62 & 100\% \\
267	IndexError & 41 & 100\% \\
268	KeyError & 28 & 100\% \\
269	AttributeError & 19 & 100\% \\
270	AssertionError & 15 & 100\% \\
271	RecursionError & 12 & 100\% \\
272	Other Exception & 66 & 100\% \\
273	\midrule
274	GeneratorExit (BaseException) & 2 & 0\% \\
275	No exception (pass class) & 849 & 100\% \\
276	\bottomrule
277	\end{tabular}
278	\end{table}
279	
280	This confirms that the model has learned a clean decision boundary: any true \texttt{Exception} subclass in the trace implies failure.
281	The \texttt{GeneratorExit} case represents a semantic ambiguity in the trace format rather than a model failure, as discussed in \S\ref{sec:irreducible}.
282	
283	%% ============================================================
284	\section{Trace Length Ablation}
285	\label{sec:trace_length_full}
286	
287	To test whether the \texttt{full\_trace} performance gap is caused by input truncation at training time, we vary the maximum trace token budget on Qwen-2.5-7B (seed=42) while keeping all other hyperparameters fixed.
288	
289	\begin{table}[t]
290	\centering
291	\caption{Trace length and truncation direction ablation on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). Head = standard left-truncation (retain first $k$ tokens); Tail = retain last $k$ tokens. Per-condition bootstrap 95\% CIs ($B{=}10{,}000$).}
292	\label{tab:trace_length}
293	\small
294	\begin{tabular}{llcc}
295	\toprule
296	\textbf{Direction} & \textbf{Max Tokens} & \textbf{Acc (\%)} & \textbf{95\% CI} \\
297	\midrule
298	Head & 256  & 78.82 & [76.4, 81.0] \\
299	Head & 512  & 80.42 & [78.2, 82.6] \\
300	Head & 1024 & 77.23 & [74.9, 79.6] \\
301	Head & no\_limit ($\infty$) & 81.76 & [79.7, 83.9] \\
302	\midrule
303	Tail & 256  & 77.48 & --- \\
304	Tail & 512  & 93.61 & --- \\
305	Tail & 1024 & 96.47 & --- \\
306	Tail & 2048 & 97.31 & --- \\
307	\bottomrule
308	\end{tabular}
309	\end{table}
310	
311	\begin{figure}[t]
312	\centering
313	\includegraphics[width=\columnwidth]{budget_curve}
314	\caption{Accuracy as a function of token budget and truncation direction (Qwen-2.5-7B, $N{=}1{,}190$). Tail-truncation (keeping last $k$ tokens) monotonically improves beyond 256 tokens and consistently outperforms head-truncation by 13--19pp at budgets ${\geq}$512. The flat head-truncation curve (77--82\%) contrasts with the steep tail-truncation rise, confirming that diagnostic signal is localized near trace end. Dashed lines show \texttt{exception\_only} (99.83\%) and \texttt{no\_trace} (75.13\%) as upper and lower bounds. Tail-256 (${\approx}$ \texttt{no\_trace}) indicates the signal window begins approximately 256 tokens from the trace terminus.}
315	\label{fig:trace_length}
316	\end{figure}
317	
318	As shown in Table~\ref{tab:trace_length} and Figure~\ref{fig:trace_length}, all four trace length conditions fall within a 5pp range (77.2\%--81.8\%).
319	To quantify the reliability of the observed differences, Table~\ref{tab:trace_length_pairwise} reports paired bootstrap comparisons ($B{=}10{,}000$, seed=42) across all condition pairs.
320	
321	\begin{table}[t]
322	\centering
323	\caption{Pairwise paired bootstrap comparisons for trace length ablation ($B{=}10{,}000$, seed=42). $\Delta$ = accuracy difference between the two conditions (first $-$ second in the budget group; condition $-$ baseline in the other groups). **$p{<}0.01$; ***$p{<}0.001$.}
324	\label{tab:trace_length_pairwise}
325	\small
326	\resizebox{\columnwidth}{!}{%
327	\begin{tabular}{llccc}
328	\toprule
329	& \textbf{Comparison} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} & \textbf{$p$-value} \\
330	\midrule
331	\multirow{4}{*}{\rotatebox{90}{\scriptsize Budget}}
332	& 512 vs.\ 256           & $+$1.60  & [$-$0.34, $+$3.53]   & 0.117 \\
333	& 1024 vs.\ 512          & $-$3.19  & [$-$5.29, $-$1.09]   & 0.002** \\
334	& no\_limit vs.\ 1024    & $+$4.54  & [$+$2.52, $+$6.55]   & ${<}$0.001*** \\
335	& no\_limit vs.\ 256     & $+$2.94  & [$+$0.84, $+$5.04]   & 0.006** \\
336	\midrule
337	\multirow{4}{*}{\rotatebox{90}{\scriptsize vs.\ no\_trace}}
338	& 256 $-$ no\_trace       & $+$3.70  & [$+$1.43, $+$6.05]   & 0.002** \\
339	& 512 $-$ no\_trace       & $+$5.29  & [$+$3.03, $+$7.56]   & ${<}$0.001*** \\
340	& 1024 $-$ no\_trace      & $+$2.10  & [$-$0.17, $+$4.37]   & 0.078 \\
341	& no\_limit $-$ no\_trace & $+$6.64  & [$+$4.37, $+$8.99]   & ${<}$0.001*** \\
342	\midrule
343	\multirow{4}{*}{\rotatebox{90}{\scriptsize vs.\ exc.}}
344	& 256 $-$ exc\_only       & $-$21.01 & [$-$23.45, $-$18.74] & ${<}$0.001*** \\
345	& 512 $-$ exc\_only       & $-$19.41 & [$-$21.76, $-$17.14] & ${<}$0.001*** \\
346	& 1024 $-$ exc\_only      & $-$22.61 & [$-$25.04, $-$20.25] & ${<}$0.001*** \\
347	& no\_limit $-$ exc\_only & $-$18.07 & [$-$20.34, $-$15.88] & ${<}$0.001*** \\
348	\bottomrule
349	\end{tabular}%
350	}
351	\end{table}
352	
353	\paragraph{Non-monotonic pattern (head-truncation).}
354	Under head-truncation (retaining trace prefixes), the trend is non-monotonic: 512 tokens (80.42\%) slightly outperforms 256 tokens (78.82\%), but doubling to 1024 tokens \emph{decreases} accuracy to 77.23\%, a statistically significant 3.19pp drop ($p{=}0.002$, 95\% CI [$-$5.29, $-$1.09]).
355	The no-limit condition (81.76\%) recovers and significantly exceeds 1024 tokens ($p{<}0.001$), but 1024 tokens is not significantly better than \texttt{no\_trace} (75.13\%; $\Delta{=}{+}2.10$pp, $p{=}0.078$, 95\% CI [$-$0.17, $+$4.37]).
356	This non-monotonicity is specific to head-truncation: the 1024-token prefix retains enough irrelevant content to mislead the model while discarding diagnostic events that appear near the trace terminus.
357	Under tail-truncation, accuracy increases monotonically for Qwen-7B and Qwen-1.5B (Table~\ref{tab:tail_cross_model}); only DeepSeek-6.7B shows a mild $-$1.5pp decrease at tail-1024$\to$tail-2048, attributable to architecture-specific long-context sensitivity rather than a systematic mid-length pathology.
358	
359	\paragraph{Comparison to baselines.}
360	All four trace budget conditions significantly exceed \texttt{no\_trace} except 1024 tokens ($p{=}0.078$), confirming that raw trace content provides some signal but unreliably so.
361	The gap to \texttt{exception\_only} (99.83\%) is massive for every budget condition (18--23pp, all $p{<}0.001$), underscoring that even unlimited raw traces cannot substitute for targeted signal extraction.
362	The best full-trace condition (no\_limit, 81.76\%) still lags \texttt{exception\_only} by 18.07pp (95\% CI [$-$20.34, $-$15.88]).
363	
364	\paragraph{Interpretation.}
365	These results rule out input truncation as the primary explanation for the full-trace performance gap: even with unlimited tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides.
366	The non-monotonic dip at 1024 tokens is consistent with a ``worst-of-both-worlds'' regime where the model receives enough noisy context to dilute the signal but not enough to compensate through broader coverage.
367	The result reinforces the information density interpretation (\S\ref{sec:density}): the gap between full traces and VOTA is driven by the \emph{content} of the trace (irrelevant lines diluting the diagnostic signal), not its \emph{length}.
368	In contrast, VOTA's compressed representation concentrates the diagnostic signal into fewer tokens, making it sensitive to truncation when those tokens are removed (\S\ref{sec:cross_model}).
369	
370	\paragraph{Truncation direction.}
371	Tail-truncation (retaining the last $k$ tokens) dramatically outperforms head-truncation: \texttt{tail\_2048} achieves 97.31\% vs.\ \texttt{head\_2048} (no\_limit) at 81.76\%, a 15.55pp improvement.
372	Even \texttt{tail\_512} (93.61\%) exceeds every head-truncation condition by over 11pp.
373	
374	However, \texttt{tail\_256} (77.48\%) performs at the \texttt{no\_trace} baseline level (75.13\%), indicating that the diagnostic signal does not reside in the very last trace lines.
375	The critical jump occurs between 256 and 512 tail tokens (+16.13pp), localizing the signal window to approximately 256--512 tokens from the trace terminus.
376	This is consistent with Python's execution model: exception tracebacks and assertion comparisons appear near the end of the trace but are preceded by the final function call frames, placing them typically 300--500 tokens from the terminus rather than at the absolute end.
377	
378	The 18.07pp gap from \texttt{full\_trace} to \texttt{exception\_only} decomposes as: 86\% positional concentration (recovered by tail-truncation at 2048 tokens) and 14\% residual content noise (the 2.52pp gap from \texttt{tail\_2048} to \texttt{exception\_only} that persists regardless of truncation direction).
379	The fact that \texttt{exception\_only} (99.83\%) still outperforms \texttt{tail\_2048} (97.31\%) confirms that semantic extraction (identifying the exception type and message) is superior to positional extraction (keeping a fixed window), because the model need not filter out non-diagnostic lines that happen to fall within the window.
380	
381	\paragraph{Cross-model budget curve.}
382	Table~\ref{tab:tail_cross_model} extends the tail-truncation analysis to a full budget sweep across three models spanning two architecture families and an 8.7$\times$ parameter range.
383	
384	\begin{table}[t]
385	\centering
386	\caption{Cross-model tail-truncation budget curve ($N{=}1{,}190$). A sharp phase transition occurs at 256$\to$512 tokens across all models (+14.7--23.0pp), after which accuracy converges into a narrow band regardless of scale or architecture. $\downarrow$: non-monotonic decrease at 1024$\to$2048 (DeepSeek only).}
387	\label{tab:tail_cross_model}
388	\small
389	\resizebox{\columnwidth}{!}{%
390	\begin{tabular}{lccccc}
391	\toprule
392	\textbf{Model} & \textbf{tail-256} & \textbf{tail-512} & \textbf{tail-1024} & \textbf{tail-2048} & \textbf{exc\_only} \\
393	\midrule
394	Qwen-7B (7B) & 78.9 & 93.6 & 96.5 & 97.3 & 99.83 \\
395	DeepSeek (6.7B) & 76.4 & 93.9 & 96.5 & 95.0$\downarrow$ & 99.33 \\
396	Qwen-1.5B (1.5B) & 72.6 & 95.6 & 96.6 & 97.9 & 99.83 \\
397	\bottomrule
398	\end{tabular}%
399	}
400	\end{table}
401	
402	\begin{table}[t]
403	\centering
404	\caption{Cross-model truncation direction comparison ($N{=}1{,}190$). Head-truncation retains the first 2,048 tokens; tail-truncation retains the last 2,048. The gap widens at smaller scale, consistent with smaller models' greater reliance on positional signal proximity.}
405	\label{tab:head_vs_tail}
406	\small
407	\begin{tabular}{lccc}
408	\toprule
409	\textbf{Model} & \textbf{head-2048 (\%)} & \textbf{tail-2048 (\%)} & \textbf{Gap (pp)} \\
410	\midrule
411	Qwen-7B & 81.8 & 97.3 & +15.5 \\
412	DeepSeek-6.7B & 78.7 & 95.0 & +16.3 \\
413	Qwen-1.5B & 75.3 & 97.9 & +22.6 \\
414	\bottomrule
415	\end{tabular}
416	\end{table}
417	
418	Three patterns emerge from the budget curve.
419	\emph{Phase transition at 256$\to$512 tokens}: all three models jump +14.7--23.0pp (Qwen-7B +14.7, DeepSeek +17.5, Qwen-1.5B +23.0), crossing from near-baseline to near-ceiling in a single budget doubling.
420	The threshold aligns with the typical exception traceback length (${\sim}$500 tokens): below this budget, the diagnostic event is truncated; above it, the event is captured regardless of model capacity or architecture.
421	
422	\emph{Convergence at tail-512+}: once the phase transition is crossed, all three models converge into a narrow 93.6--95.6\% band at tail-512 and an even tighter 96.5--96.6\% band at tail-1024.
423	Scale and architecture differences that dominate the signal-poor regime (tail-256 range: 72.6--78.9\%, 6.3pp) vanish in the signal-rich regime (tail-1024 range: 96.5--96.6\%, 0.1pp).
424	
425	\emph{Scale behavior inversion}: in the signal-poor regime (tail-256), smaller models perform worse (Qwen-1.5B 72.6\% vs.\ Qwen-7B 78.9\%, $-$6.3pp), mirroring the \texttt{no\_trace} scale pattern.
426	In the signal-rich regime (tail-512+), this reverses: Qwen-1.5B matches or exceeds Qwen-7B (95.6\% vs.\ 93.6\% at tail-512; 97.9\% vs.\ 97.3\% at tail-2048), confirming that sufficient trace signal eliminates the capacity advantage.
427	
428	\emph{Non-monotonicity}: DeepSeek-6.7B shows a $-$1.5pp decrease from tail-1024 (96.5\%) to tail-2048 (95.0\%), while the other two models increase monotonically.
429	This architecture-specific sensitivity is consistent with DeepSeek's known vulnerability to long-context formatting (Appendix~\ref{sec:training_dynamics}): additional tokens beyond the diagnostic window introduce noise that this model cannot filter as effectively.
430	
431	Table~\ref{tab:head_vs_tail} confirms the truncation direction effect across all models: tail-2048 outperforms head-2048 by 15.5--22.6pp.
432	The gap is largest for Qwen-1.5B (+22.6pp), indicating that smaller models benefit most from positional proximity to the diagnostic signal, as they lack the capacity to locate it within longer, noisier prefixes.
433	
434	%% ============================================================
435	\section{Calibration Analysis}
436	\label{sec:calibration_full}
437	
438	Beyond accuracy, we evaluate whether trace conditions affect prediction calibration, motivated by recent findings that code LLM confidence is often poorly calibrated \citep{spiess2025calibration}.
439	
440	\begin{table}[t]
441	\centering
442	\caption{Calibration metrics on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). ECE = expected calibration error; Brier = Brier score. Lower is better for both.}
443	\label{tab:calibration}
444	\small
445	\begin{tabular}{lcc}
446	\toprule
447	\textbf{Condition} & \textbf{ECE $\downarrow$} & \textbf{Brier $\downarrow$} \\
448	\midrule
449	ae\_only & \textbf{0.0004} & \textbf{0.0008} \\
450	exception\_only & 0.0027 & 0.0013 \\
451	VOTA & 0.0054 & 0.005 \\
452	full\_trace & 0.096 & 0.144 \\
453	no\_trace & 0.171 & 0.197 \\
454	\bottomrule
455	\end{tabular}
456	\end{table}
457	
458	Table~\ref{tab:calibration} shows that calibration quality mirrors the Tier~1/2 hierarchy.
459	Tier~1 conditions (\texttt{ae\_only}: ECE=0.0004; \texttt{exception\_only}: ECE=0.0027) produce near-perfectly calibrated predictions, while \texttt{full\_trace} (ECE=0.096) and \texttt{no\_trace} (ECE=0.171) exhibit substantial miscalibration.
460	VOTA (ECE=0.0054) is well-calibrated but slightly worse than either Tier~1 component alone, reinforcing the pattern that combining trace signals dilutes rather than improves the prediction signal.
461	
462	The Brier scores tell a consistent story: \texttt{ae\_only} (0.0008) and \texttt{exception\_only} (0.0013) achieve near-zero scores, while \texttt{no\_trace} (0.197) indicates substantial miscalibration.
463	
464	\begin{figure}[t]
465	\centering
466	\includegraphics[width=\columnwidth]{fig2_calibration}
467	\caption{Reliability diagrams for four trace conditions on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). \texttt{exception\_only} (ECE=0.0027) clusters near the diagonal, while \texttt{no\_trace} (ECE=0.171) exhibits systematic overconfidence, a 63$\times$ gap.}
468	\label{fig:calibration}
469	\end{figure}
470	
471	%% ============================================================
472	\section{Error Overlap Analysis}
473	\label{sec:error_overlap}
474	
475	We analyze the overlap between error sets of different conditions to determine whether they fail on the same samples (Figure~\ref{fig:error_overlap}).
476	
477	\texttt{exception\_only}'s 2 errors (samples 901 and 905) have zero intersection with the error sets of all other conditions (Jaccard = 0.000 in all pairwise comparisons).
478	This orthogonality arises because \texttt{exception\_only} errors are caused by \texttt{GeneratorExit} false positives (pass samples misclassified as fail due to benign \texttt{BaseException} events), while errors from other conditions are predominantly fail samples misclassified as pass due to insufficient signal.
479	
480	Among non-exception conditions, error sets exhibit hierarchical containment: \texttt{ae\_only} $\subset$ VOTA $\subset$ \texttt{loop\_only} $\subset$ \texttt{no\_trace}, with pairwise Jaccard indices increasing with signal overlap.
481	\texttt{loop\_only} and \texttt{full\_trace} share the highest overlap (Jaccard ${\sim}$0.65), reflecting their shared reliance on behavioral patterns rather than explicit fault indicators.
482	
483	This analysis confirms that \texttt{exception\_only} operates on an independent signal dimension: its errors are representation ambiguities (iterator protocol artifacts) rather than information deficits, explaining why combining it with other signals cannot eliminate these specific errors.
484	
485	\begin{figure}[t]
486	\centering
487	\includegraphics[width=\columnwidth]{error_overlap}
488	\caption{Jaccard similarity between error sets of different conditions (Qwen-7B, seed=42, $N{=}1{,}190$). \texttt{exception\_only} (exc\_only) has zero overlap with all other conditions, confirming it operates on an independent signal dimension.}
489	\label{fig:error_overlap}
490	\end{figure}
491	
492	%% ============================================================
493	\section{Cross-Dataset Generalization: DebugBench}
494	\label{sec:debugbench_full}
495	
496	To test whether exception-based verdict prediction generalizes beyond LLM-generated solutions, we evaluate on DebugBench \citep{tian2024debugbench}---a dataset of human-written programs with synthetically injected bugs (single-point mutations such as operator replacement, variable misuse, and missing statements).
497	After filtering for executable Python samples with valid traces, we retain 426 samples with a near-balanced class distribution (majority baseline: 51.4\%).
498	
499	\begin{table}[t]
500	\centering
501	\caption{Generalization to DebugBench ($N{=}426$, Qwen-2.5-7B, seed=42). Wilson 95\% CIs. The component ranking (exception\_only $\geq$ VOTA $>$ no\_trace) is preserved, and exception\_only achieves perfect accuracy.}
502	\label{tab:debugbench}
503	\small
504	\begin{tabular}{lcc}
505	\toprule
506	\textbf{Condition} & \textbf{Acc (\%)} & \textbf{95\% CI} \\
507	\midrule
508	exception\_only & \textbf{100.00} & [99.14, 100.00] \\
509	VOTA & 99.77 & [99.30, 100.00] \\
510	no\_trace & 96.71 & [94.80, 98.40] \\
511	\midrule
512	Majority baseline & 51.41 & --- \\
513	\bottomrule
514	\end{tabular}
515	\end{table}
516	
517	Table~\ref{tab:debugbench} shows that the component ranking from the main experiments is preserved: \texttt{exception\_only} (100.00\%) $\geq$ VOTA (99.77\%) $>$ \texttt{no\_trace} (96.71\%).
518	The \texttt{exception\_only} condition achieves perfect accuracy, confirming that the exception-based representation generalizes to a different fault distribution without degradation.
519	
520	The absolute margins are much narrower than on the main dataset: the \texttt{no\_trace} baseline already achieves 96.71\%---compared to 75.13\% on HumanEval+MBPP---leaving only 3.29pp of headroom for trace-based improvement.
521	This ceiling effect reflects a fundamental difference in fault characteristics: DebugBench bugs are synthetically injected single-point mutations, which produce code that is structurally dissimilar from the original correct solution; a model can often identify the fault from source code alone.
522	In contrast, the HumanEval+MBPP solutions are LLM-generated, producing natural errors (logic mistakes, edge-case failures) where the faulty and correct solutions may be structurally similar, making code-only verdict prediction substantially harder.
523	
524	These results support exception-based verdict prediction as a generalizable approach---the method does not degrade on an out-of-distribution dataset, and the exception dominance ranking (exception\_only $\geq$ VOTA $>$ no\_trace) is consistent across both datasets---but the narrow DebugBench margins are insufficient to independently validate trace importance.
525	The 24.70pp trace lift on the main dataset (no\_trace 75.13\% $\to$ exception\_only 99.83\%) remains the primary evidence for the value of exception-based trace signals.
526	
527	%% ============================================================
528	\section{Cross-Model Robustness Analysis}
529	\label{sec:robustness_analysis}
530	
531	The cross-model gap pattern (Table~\ref{tab:cross_model}) suggests a design principle: \emph{trace representations should match the model capability floor, not the ceiling.}
532	Exception events are consistently the most effective component on both models, and their structural simplicity---a fixed-format error message---ensures that the relative advantage over richer representations holds across all seeds.
533	Two of three DeepSeek seeds match Qwen-level accuracy (99.33\%); the outlier (seed 123, 91.09\%) we hypothesize reflects LoRA initialization sensitivity landing in a suboptimal basin (fail recall = 70.5\%, though direct evidence is lacking), not a failure of the exception signal itself---even this outlier outperforms VOTA (84.45\%) by 6.64pp.
534	The VOTA cross-model gap is confounded by two factors: (1)~tokenizer efficiency---the DeepSeek tokenizer averages 2{,}626 tokens per VOTA sample versus Qwen's 1{,}929, causing 91.7\% of training samples to exceed the 2{,}048-token context window; content-aware truncation preferentially removes the terminal structured prompt, preserving the verdict label but truncating trace content---and (2)~base model capability differences, consistent with findings that SFT generalization depends on pretrain quality \citep{yang2024generalization}.
535	The two factors cannot be disentangled in the current experimental design.
536	Our \texttt{exception\_only} design sidesteps the truncation confound entirely: inputs have a median of 150 tokens (mean 398), well below the 2{,}048-token context window, so no training samples are truncated on either model.
537	The resulting 0.56pp cross-model gap (Table~\ref{tab:cross_model}) is therefore a clean measure of model capability differences, making the ``capability floor'' principle directly testable.
538	The practical implication is that trace-based systems should default to the simplest sufficient signal; for smaller models, training stability (multi-seed selection, warmup schedules) is a secondary but addressable concern.
539	
540	%% ============================================================
541	\section{Training Dynamics and Loss Decoupling}
542	\label{sec:training_dynamics}
543	
544	The DeepSeek \texttt{exception\_only} results reveal two instructive training dynamics.
545	First, epoch-level analysis shows mild degradation in 2/3 seeds: seed 42 peaks at 99.83\% after epoch~1 but settles at 99.33\% by epoch~3 ($-$0.50pp), seed 123 degrades from 91.43\% to 91.09\% ($-$0.34pp), while seed 456 shows no epoch degradation (99.33\% at both epoch~1 and epoch~3).
546	Early stopping may yield marginal gains for some seeds, but the epoch effect is small (${\leq}$0.5pp) compared to the seed effect (8.24pp between seeds 42 and 123).
547	
548	Second, seeds 123 and 456 converge to nearly identical final training losses (0.122 and 0.123 respectively), yet their accuracies differ by 8.24pp (91.09\% vs.\ 99.33\%).
549	The critical difference lies in fail recall: seeds 42 and 456 achieve 100\%, while seed 123 achieves only 70.5\%---the LoRA initialization in seed 123 fails to learn the exception$\to$fail mapping for a substantial fraction of failing samples, even though the per-token loss appears converged.
550	This demonstrates that token-level training loss can mask fundamental differences in sample-level classification ability, suggesting a parallel to the eval-loss/accuracy decoupling observed in DeepSeek VOTA (where eval loss rose 65\% from epoch 1 to 3 while accuracy improved by 6.3pp) at the training phase.
551	The practical recommendation is twofold: (1)~use task-specific metrics (accuracy, fail recall) for checkpoint and seed selection rather than training or evaluation loss, and (2)~for deployment on smaller models, train multiple seeds and select the best, as a single run may not reliably converge to the correct classification boundary.
552	
553	\paragraph{Format collapse, not semantic failure.}
554	The 100 errors of seed 123 are not semantic failures but generation format collapse: on inputs exceeding 4,000 characters (those containing verbose locals dumps), the model echoes trace content instead of emitting a verdict token, while achieving zero errors on shorter inputs.
555	This indicates that the LoRA initialization of seed 123 specifically compromises long-context format compliance rather than exception signal comprehension, further supporting the robustness advantage of compact \texttt{exception\_only} inputs.
556	
557	The contrast with VOTA is instructive: DeepSeek VOTA accuracy monotonically increases from 78.15\% to 84.45\% across epochs, but is consistent with a performance limit associated with the high trace truncation rate (\S\ref{sec:cross_model})---the model progressively extracts signal from samples with intact trace content but cannot fully compensate for the information loss in the truncated majority.
558	The 84.45\% accuracy reflects a combination of trace information loss and model capability constraints.
559	
560	%% ============================================================
561	\section{Deduplication Statistics}
562	\label{sec:dedup_stats}
563	
564	Table~\ref{tab:dedup} reports the duplication rates across trace formats.
565	Because multiple passing solutions to the same problem produce identical (input, output) pairs in the \texttt{exception\_only} format---correct executions raise no exceptions, so the trace content is the same regardless of the solution's internal logic---the dataset contains duplicate rows.
566	Train--test input overlap is zero (split by problem ID), so no information leakage occurs.
567	The high duplication in \texttt{exception\_only} does not affect our experimental conclusions: after deduplication the training set still contains 2,858 unique samples and the test set 607, providing sufficient coverage for the 591-problem benchmark.
568	The \texttt{exception\_only} test set contains 48.99\% duplicate inputs due to representation compactness; all confidence intervals treat samples as independent Bernoulli trials.
569	
570	\begin{table}[t]
571	\centering
572	\caption{Deduplication statistics. The \texttt{exception\_only} format collapses multiple passing solutions into identical rows because correct executions produce no exception events. Train--test input overlap is 0 (no leakage).}
573	\label{tab:dedup}
574	\small
575	\begin{tabular}{lccc}
576	\toprule
577	\textbf{Split} & \textbf{Total} & \textbf{Unique} & \textbf{Dup.\ rate} \\
578	\midrule
579	exception\_only train & 4{,}720 & 2{,}858 & 39.45\% \\
580	exception\_only test  & 1{,}190 &   607 & 48.99\% \\
581	raw\_traces (full)    & 5{,}910 & 5{,}803 &  1.81\% \\
582	\bottomrule
583	\end{tabular}
584	\end{table}
585	
586	%% ============================================================
587	\section{Regex Baseline Analysis}
588	\label{sec:regex_baselines}
589	
590	To establish a non-learning upper bound, we evaluate six regex-based baselines on the \texttt{exception\_only} test set ($N{=}1{,}190$) and two format-specific baselines on VOTA and \texttt{full\_trace} inputs.
591	
592	\begin{table}[t]
593	\centering
594	\caption{Regex baseline accuracy ($N{=}1{,}190$). B4 is the strongest semantic baseline (6.22pp below SFT \texttt{exception\_only}, McNemar $p{<}0.001$). B6 uses an error count threshold. $^\ddag$B5 exploits a data formatting artifact: the \texttt{[No exception data in trace]} marker is deterministically present in all pass samples, making this a format-level shortcut rather than a genuine exception-based heuristic.}
595	\label{tab:regex}
596	\small
597	\begin{tabular}{llc}
598	\toprule
599	\textbf{Baseline} & \textbf{Method} & \textbf{Acc (\%)} \\
600	\midrule
601	B1: \texttt{[ERROR]} presence & string match & 93.45 \\
602	B2: Traceback presence & string match & 71.51 \\
603	B3: Any keyword & union of B1+B2+Exception & 93.45 \\
604	B4: Exception type regex & regex on exception class names & \textbf{93.61} \\
605	B5: Format marker & \texttt{[No exception data]} $\to$ pass & 99.33$^\ddag$ \\
606	B6: Error count $\geq$2 & count threshold & 92.02 \\
607	\midrule
608	VOTA format regex & best regex on VOTA traces & 75.55 \\
609	full\_trace format regex & best regex on full traces & 77.39 \\
610	\bottomrule
611	\end{tabular}
612	\end{table}
613	
614	The strongest legitimate baseline (B4, 93.61\%) applies regex pattern-matching on Python exception class names (e.g., \texttt{ValueError}, \texttt{TypeError}).
615	Its errors concentrate on 8 boundary samples where a \texttt{ValueError} is raised inside a \texttt{try/except} block and caught---the program passes despite an exception occurring in the trace.
616	SFT \texttt{exception\_only} correctly classifies 6 of these 8 samples, indicating that the model learns the semantic distinction between caught (benign) and uncaught (fault-indicating) exceptions.
617	B5 (99.33\%) achieves near-SFT accuracy but relies on the deterministic presence of a format marker in pass-class traces, which is an artifact of the trace preprocessing pipeline rather than a generalizable signal; McNemar test vs.\ SFT yields $p{=}0.041$, confirming a statistically significant difference.
618	
619	\paragraph{Cross-format comparison.}
620	Table~\ref{tab:regex_cross_format} compares SFT and the best applicable regex baseline for each trace format.
621	The SFT advantage increases with format complexity: \texttt{no\_trace} (+3.62pp over majority baseline) $<$ \texttt{full\_trace} (+4.37pp) $<$ \texttt{exception\_only} (+6.22pp) $\ll$ VOTA (+23.86pp).
622	The VOTA gap is largest because its structured multi-component format carries semantic content that regex cannot parse, while \texttt{exception\_only}'s simpler format allows regex to capture most of the signal.
623	
624	\begin{table}[t]
625	\centering
626	\caption{SFT vs.\ best regex baseline by trace format ($N{=}1{,}190$). Regex baselines: majority class for \texttt{no\_trace}, keyword matching for \texttt{full\_trace}, pattern matching for VOTA, exception type regex (B4) for \texttt{exception\_only}.}
627	\label{tab:regex_cross_format}
628	\small
629	\begin{tabular}{lccc}
630	\toprule
631	\textbf{Format} & \textbf{SFT (\%)} & \textbf{Regex (\%)} & \textbf{$\Delta$ (pp)} \\
632	\midrule
633	exception\_only & 99.83 & 93.61 & +6.22 \\
634	VOTA & 99.41 & 75.55 & +23.86 \\
635	full\_trace & 81.76 & 77.39 & +4.37 \\
636	no\_trace & 75.13 & 71.51 & +3.62 \\
637	\bottomrule
638	\end{tabular}
639	\end{table}
640	
641	%% ============================================================
642	\section{Cross-Model Zero-Shot Comparison}
643	\label{sec:zeroshot_cross_model}
644	
645	Table~\ref{tab:zeroshot_cross_model} compares zero-shot and SFT \texttt{exception\_only} accuracy across four models.
646	Zero-shot performance does not correlate with model size: the smallest model (Qwen-1.5B, 93.45\%) outperforms all larger models, while the largest (CodeLlama-13B) falls below majority baseline.
647	SFT compresses the 42.44pp zero-shot range to 0.56pp, eliminating architecture-dependent variance.
648	
649	\begin{table}[t]
650	\centering
651	\caption{Zero-shot vs.\ SFT \texttt{exception\_only} across four models ($N{=}1{,}190$). Zero-shot accuracy is uncorrelated with model size; SFT normalizes cross-architecture variance from 42.44pp to 0.56pp.}
652	\label{tab:zeroshot_cross_model}
653	\small
654	\begin{tabular}{llccc}
655	\toprule
656	\textbf{Model} & \textbf{Size} & \textbf{Zero-shot (\%)} & \textbf{SFT (\%)} & \textbf{$\Delta$ (pp)} \\
657	\midrule
658	Qwen-1.5B & 1.5B & 93.45 & 99.83 & +6.38 \\
659	DeepSeek-6.7B & 6.7B & 90.59 & 99.33 & +8.74 \\
660	Qwen-7B & 7B & 89.08 & 99.83 & +10.75 \\
661	CodeLlama-13B & 13B & 51.01 & 99.89 & +48.88 \\
662	\midrule
663	Range & --- & 42.44pp & 0.56pp & --- \\
664	\bottomrule
665	\end{tabular}
666	\end{table}
667	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "a664d2f4-c26c-4b0b-9fb2-b4462c9d73ec",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex",
      "content": "\\section{Per-Class Performance Breakdown}\n\\label{sec:per_class}\n\nTable~\\ref{tab:per_class} reports per-class precision, recall, and F1 for all experimental conditions.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Per-class precision, recall, and F1 for all experimental conditions (seed 42). DeepSeek VOTA achieves 100\\% fail precision but only 45.4\\% fail recall, indicating systematic bias toward predicting \\texttt{pass}. DeepSeek \\texttt{exception\\_only} seed 42 achieves 100\\% fail recall, but seed 123 drops to 70.5\\% (see Table~\\ref{tab:full_deepseek}).}\n\\label{tab:per_class}\n\\small\n\\begin{tabular}{llccccccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Model} & \\textbf{Acc} & \\textbf{Pass P} & \\textbf{Pass R} & \\textbf{Pass F1} & \\textbf{Fail P} & \\textbf{Fail R} & \\textbf{Fail F1} \\\\\n\\midrule\nNo Trace          & Qwen-2.5-7B & 75.13 & 87.76 & 75.79 & 81.34 & 54.73 & 73.45 & 62.72 \\\\\nFull Trace        & Qwen-2.5-7B & 81.76 & 87.74 & 86.60 & 87.17 & 67.43 & 69.62 & 68.51 \\\\\nFull Trace (LO)   & Qwen-2.5-7B & 86.22 & 88.21 & 93.18 & 90.63 & 80.07 & 68.73 & 73.97 \\\\\nVOTA              & Qwen-2.5-7B & 99.41 & 100.00 & 99.18 & 99.59 & 97.98 & 100.00 & 98.98 \\\\\nException Only    & Qwen-2.5-7B & 99.83 & 100.00 & 99.76 & 99.88 & 99.41 & 100.00 & 99.71 \\\\\nAE Only           & Qwen-2.5-7B & 99.92 & 100.00 & 99.88 & 99.94 & 99.71 & 100.00 & 99.85 \\\\\nLoop Only         & Qwen-2.5-7B & 85.63 & 92.39 & 87.07 & 89.66 & 71.65 & 82.01 & 76.48 \\\\\nVOTA\\_no\\_ae       & Qwen-2.5-7B & 99.41 & 99.88 & 99.29 & 99.59 & 98.26 & 99.71 & 98.98 \\\\\n\\midrule\nNo Trace          & DeepSeek-6.7B & 73.36 & 81.71 & 80.85 & 81.28 & 53.16 & 54.57 & 53.86 \\\\\nFull Trace        & DeepSeek-6.7B & 79.16 & 85.70 & 85.10 & 85.40 & 63.20 & 64.30 & 63.70 \\\\\nVOTA              & DeepSeek-6.7B & 84.45 & 82.14 & 100.00 & 90.20 & 100.00 & 45.40 & 62.50 \\\\\nException Only    & DeepSeek-6.7B & 99.33 & 100.00 & 99.06 & 99.53 & 97.69 & 100.00 & 98.83 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n%% ============================================================\n\\section{Training Details}\n\\label{sec:training_details}\n\nTable~\\ref{tab:hyperparams} summarizes the training hyperparameters shared across all conditions.\nAll experiments use the HuggingFace TRL \\texttt{SFTTrainer} with LoRA \\citep{hu2022lora} applied to all linear layers.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training hyperparameters (shared across all conditions).}\n\\label{tab:hyperparams}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll}\n\\toprule\n\\textbf{Hyperparameter} & \\textbf{Value} \\\\\n\\midrule\nLoRA rank ($r$)            & 16 \\\\\nLoRA alpha ($\\alpha$)      & 32 \\\\\nLoRA dropout               & 0.05 \\\\\nLoRA target modules        & all linear layers \\\\\n\\midrule\nEpochs                     & 3 \\\\\nPer-device batch size       & 4 \\\\\nGradient accumulation steps & 8 \\\\\nEffective batch size        & 32 \\\\\n\\midrule\nLearning rate               & $2 \\times 10^{-4}$ \\\\\nLR scheduler                & linear decay \\\\\nWarmup ratio                & 0.1 \\\\\nWeight decay                & 0.01 \\\\\n\\midrule\nMax sequence length         & 2048 tokens \\\\\nPrimary seed                & 42 \\\\\nRobustness seeds            & 123, 456 \\\\\n\\midrule\nHardware                    & 1$\\times$ RTX PRO 6000 Blackwell (96\\,GB VRAM) \\\\\nFramework                   & HuggingFace TRL SFTTrainer \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nTable~\\ref{tab:train_time} reports per-condition training wall-clock times.\nConditions with longer trace inputs (e.g., \\texttt{full\\_trace}, VOTA) require proportionally more training time due to increased sequence lengths.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training wall-clock time per condition on a single RTX PRO 6000 Blackwell GPU. Where multiple seeds were run, individual times are listed.}\n\\label{tab:train_time}\n\\small\n\\begin{tabular}{llr}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed(s)} & \\textbf{Time (h)} \\\\\n\\midrule\nno\\_trace       & 42         & ${\\sim}$0.5 \\\\\nfull\\_trace     & 42         & ${\\sim}$2.2 \\\\\nlabel\\_only     & 42         & ${\\sim}$2.2 \\\\\nVOTA                     & 42         & ${\\sim}$2.3 \\\\\nexception\\_only & 42         & ${\\sim}$2.1 \\\\\nexception\\_only & 123        & ${\\sim}$2.1 \\\\\nexception\\_only & 456        & ${\\sim}$1.3 \\\\\nae\\_only        & 42         & ${\\sim}$1.8 \\\\\nloop\\_only      & 42         & ${\\sim}$2.1 \\\\\nVOTA\\_no\\_ae    & 42         & ${\\sim}$1.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n\\section{VOTA Trace Examples}\n\\label{sec:vota_examples}\n\nWe provide two representative VOTA trace examples illustrating the fail and pass cases.\nIn the fail case, the exception event provides an unambiguous fault signal.\nIn the pass case, the absence of an exception event combined with a matching assertion point confirms correct execution.\n\n\\paragraph{Fail example.}\nA \\texttt{ZeroDivisionError} triggers an \\texttt{[ERROR]} event, providing a direct fault signal that is sufficient for the model to predict \\texttt{fail}.\n\n\\begin{small}\n\\begin{verbatim}\n## Function\ndef divide(a, b):\n    return a / b\n\n## Test Input\ndivide(1, 0)\n\n## Expected Output\ninf\n\n## VOTA Trace\n[ERROR] ZeroDivisionError: division by zero\n\n## Verdict\nfail\n\\end{verbatim}\n\\end{small}\n\n\\paragraph{Pass example.}\nNo exception is raised, and the assertion point confirms that the actual output matches the expected value.\n\n\\begin{small}\n\\begin{verbatim}\n## Function\ndef add(a, b):\n    return a + b\n\n## Test Input\nadd(2, 3)\n\n## Expected Output\n5\n\n## VOTA Trace\n[LOOP] No loops detected.\n[ASSERT] actual=5, expected=5\n\n## Verdict\npass\n\\end{verbatim}\n\\end{small}\n\nThese examples illustrate the core asymmetry exploited by the \\texttt{exception\\_only} condition: fail cases produce an explicit \\texttt{[ERROR]} event, while pass cases are characterized by its absence.\nThis binary signal (presence vs.\\ absence of an exception) is sufficient for near-perfect verdict prediction.\n\n%% ============================================================\n\\section{Full Experimental Results}\n\\label{sec:full_results}\n\nTables~\\ref{tab:full_qwen} and \\ref{tab:full_deepseek} report the complete experimental results across all conditions, models, and seeds.\n\n\\begin{table}[t]\n\\centering\n\\caption{Full results for Qwen-2.5-Coder-7B across all conditions and seeds. Conditions with a single seed report no variance. \\texttt{exception\\_only} achieves 99.83\\% across all three seeds ($\\sigma{=}$0). \\texttt{ae\\_only} achieves 99.64\\% mean ($\\pm$0.49; seed 123 at 99.08\\% is the outlier).}\n\\label{tab:full_qwen}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{S42} & \\textbf{S123} & \\textbf{S456} & \\textbf{Mean $\\pm$ Std} \\\\\n\\midrule\nexception\\_only & 99.83 & 99.83 & 99.83 & 99.83 $\\pm$ 0.00 \\\\\nae\\_only        & 99.92 & 99.08 & 99.92 & 99.64 $\\pm$ 0.49 \\\\\nVOTA                     & 99.41 & ---   & ---   & --- \\\\\nVOTA\\_no\\_ae    & 99.41 & ---   & ---   & --- \\\\\nlabel\\_only     & 86.22 & ---   & ---   & --- \\\\\nloop\\_only      & 85.63 & ---   & ---   & --- \\\\\nfull\\_trace     & 81.76 & ---   & ---   & --- \\\\\nno\\_trace       & 75.13 & ---   & ---   & --- \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Full results for DeepSeek-Coder-6.7B across all conditions and seeds. \\texttt{exception\\_only} shows bimodal seed behavior: seeds 42 and 456 achieve 99.33\\%, while seed 123 yields 91.09\\% (LoRA initialization outlier, fail recall = 70.5\\%).}\n\\label{tab:full_deepseek}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{Accuracy} & \\textbf{Notes} \\\\\n\\midrule\nexception\\_only & 42  & 99.33 & epoch 1: 99.83 \\\\\nexception\\_only & 456 & 99.33 & CI [98.82, 99.75] \\\\\nexception\\_only & 123 & 91.09 & fail recall = 70.5\\%; CI [89.40, 92.60] \\\\\n\\midrule\nVOTA                     & 42  & 84.45 & \\\\\nno\\_trace       & 42  & 73.36 & \\\\\nfull\\_trace     & 42  & 79.16 & CI [76.80, 81.30] \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n%% ============================================================\n\\section{Tokenizer and Truncation Analysis}\n\\label{sec:tokenizer_analysis}\n\nThe VOTA cross-model gap (14.96pp, Table~\\ref{tab:cross_model}; confounded by tokenizer-driven truncation; 91.7\\% of DeepSeek training samples were affected) is driven by a training-time truncation asymmetry.\nThe DeepSeek tokenizer averages 2{,}626 tokens per VOTA sample versus 1{,}929 for Qwen, causing 91.7\\% of DeepSeek VOTA training samples to exceed the 2{,}048-token context window.\nThe training framework preserves the verdict label but truncates trace content, so the model trains with incomplete diagnostic information for the majority of samples.\n\nA post-hoc group analysis provides directional evidence: partitioning DeepSeek VOTA test samples by whether their training-set counterparts exceeded the context window, intact samples ($N{=}99$) achieve 100\\% accuracy while truncated samples ($N{=}1{,}091$) achieve 83.04\\% (95\\% CI [80.75\\%, 85.24\\%]; Fisher exact $p{<}0.001$), with all 185 errors concentrated in the fail class (fail recall = 31.23\\%).\nPer-class analysis (Table~\\ref{tab:per_class}) confirms that DeepSeek VOTA achieves 100\\% fail precision but only 45.43\\% fail recall, systematically defaulting to \\texttt{pass}---in contrast to Qwen VOTA, which achieves 100\\% fail recall.\n\nSeed robustness diverges across models: Qwen \\texttt{exception\\_only} produces identical 99.83\\% across all three seeds ($\\sigma{=}0$), while DeepSeek shows bimodal behavior: seeds 42 and 456 achieve 99.33\\% (fail recall = 100\\%), seed 123 yields 91.09\\% (fail recall = 70.5\\%).\nBecause \\texttt{exception\\_only} test inputs contain 48.99\\% duplicates (607 unique of 1,190; \\S\\ref{sec:dataset}), CIs assume $n{=}1{,}190$ independent trials; under deduplication ($n{=}607$), Qwen's accuracy is 99.67\\% (Wilson CI [98.81, 99.91]).\n\n%% ============================================================\n\\section{Irreducible Sample Analysis}\n\\label{sec:irreducible}\n\nThe \\texttt{exception\\_only} condition with Qwen-2.5-Coder-7B misclassifies exactly 2 out of 1,190 test samples across all three seeds (42, 123, 456), with 100\\% overlap across seeds.\nBoth samples (IDs 901 and 905) share the following characteristics:\n\n\\begin{itemize}\n\\item \\textbf{Function:} \\texttt{check\\_dict\\_case} (HumanEval/95)---a function that checks whether all dictionary keys are uniformly upper-case or lower-case strings.\n\\item \\textbf{Ground-truth label:} \\texttt{pass}.\n\\item \\textbf{Predicted label:} \\texttt{fail} (false negative).\n\\item \\textbf{Cross-seed consistency:} Both samples are misclassified identically by all three seeds, indicating a systematic rather than stochastic error.\n\\end{itemize}\n\nManual inspection reveals the root cause: \\texttt{check\\_dict\\_case} uses \\texttt{all()} over a generator expression, and Python's \\texttt{all()} short-circuits on the first \\texttt{True} value, raising \\texttt{GeneratorExit} to terminate the generator.\nBecause \\texttt{GeneratorExit} is a \\texttt{BaseException} subclass, the tracer records it as seven \\texttt{[ERROR] GeneratorExit} lines---even though the function executes correctly and the test passes.\nThe model observes these spurious error markers and reasonably but incorrectly predicts \\texttt{fail}.\nThis is not a model failure but a representation ambiguity: the \\texttt{exception\\_only} format cannot distinguish genuine exceptions from benign \\texttt{BaseException} subclasses triggered by Python's iterator protocol.\n\nMost configurations converge to these same 2 errors: Qwen-1.5B, Qwen-7B (3 seeds), CodeLlama-13B (seeds 42/456), and DeepSeek-6.7B (seeds 42/456) all produce error set $\\{901, 905\\}$.\nHowever, CodeLlama-13B seed 123 achieves 100\\% accuracy (0/1190 errors), correctly classifying both samples.\nThis demonstrates that 99.83\\% is a near-perfect \\emph{floor} (the convergence attractor for most LoRA initializations) rather than a hard data ceiling: the representation supports perfect accuracy, but most initializations converge to the same 2-error basin.\nThe practical implication is that these errors are high-probability convergence artifacts addressable through seed selection or ensemble methods, not fundamental limitations of the exception-based representation.\n\n%% ============================================================\n\\section{Exception Type Accuracy Breakdown}\n\\label{sec:exception_type}\n\nTable~\\ref{tab:exception_type} reports \\texttt{exception\\_only} accuracy stratified by exception type on Qwen-2.5-7B (seed=42, $N{=}1{,}190$).\nAll standard exception types (\\texttt{TypeError}, \\texttt{ValueError}, \\texttt{IndexError}, etc.) achieve 100\\% accuracy.\nThe only misclassifications arise from \\texttt{GeneratorExit}, a \\texttt{BaseException} subclass that is not an \\texttt{Exception}---it is raised by Python's iterator protocol during generator short-circuiting, not by actual program errors.\n\n\\begin{table}[t]\n\\centering\n\\caption{Exception type accuracy breakdown for \\texttt{exception\\_only} (Qwen-7B, seed=42). All true error types achieve 100\\%. The only failures come from \\texttt{GeneratorExit} (a \\texttt{BaseException} subclass, not an \\texttt{Exception}), which appears in 2 passing samples.}\n\\label{tab:exception_type}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Exception Type} & \\textbf{Samples} & \\textbf{Accuracy} \\\\\n\\midrule\nTypeError & 96 & 100\\% \\\\\nValueError & 62 & 100\\% \\\\\nIndexError & 41 & 100\\% \\\\\nKeyError & 28 & 100\\% \\\\\nAttributeError & 19 & 100\\% \\\\\nAssertionError & 15 & 100\\% \\\\\nRecursionError & 12 & 100\\% \\\\\nOther Exception & 66 & 100\\% \\\\\n\\midrule\nGeneratorExit (BaseException) & 2 & 0\\% \\\\\nNo exception (pass class) & 849 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis confirms that the model has learned a clean decision boundary: any true \\texttt{Exception} subclass in the trace implies failure.\nThe \\texttt{GeneratorExit} case represents a semantic ambiguity in the trace format rather than a model failure, as discussed in \\S\\ref{sec:irreducible}.\n\n%% ============================================================\n\\section{Trace Length Ablation}\n\\label{sec:trace_length_full}\n\nTo test whether the \\texttt{full\\_trace} performance gap is caused by input truncation at training time, we vary the maximum trace token budget on Qwen-2.5-7B (seed=42) while keeping all other hyperparameters fixed.\n\n\\begin{table}[t]\n\\centering\n\\caption{Trace length and truncation direction ablation on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). Head = standard left-truncation (retain first $k$ tokens); Tail = retain last $k$ tokens. Per-condition bootstrap 95\\% CIs ($B{=}10{,}000$).}\n\\label{tab:trace_length}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Direction} & \\textbf{Max Tokens} & \\textbf{Acc (\\%)} & \\textbf{95\\% CI} \\\\\n\\midrule\nHead & 256  & 78.82 & [76.4, 81.0] \\\\\nHead & 512  & 80.42 & [78.2, 82.6] \\\\\nHead & 1024 & 77.23 & [74.9, 79.6] \\\\\nHead & no\\_limit ($\\infty$) & 81.76 & [79.7, 83.9] \\\\\n\\midrule\nTail & 256  & 77.48 & --- \\\\\nTail & 512  & 93.61 & --- \\\\\nTail & 1024 & 96.47 & --- \\\\\nTail & 2048 & 97.31 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{budget_curve}\n\\caption{Accuracy as a function of token budget and truncation direction (Qwen-2.5-7B, $N{=}1{,}190$). Tail-truncation (keeping last $k$ tokens) monotonically improves beyond 256 tokens and consistently outperforms head-truncation by 13--19pp at budgets ${\\geq}$512. The flat head-truncation curve (77--82\\%) contrasts with the steep tail-truncation rise, confirming that diagnostic signal is localized near trace end. Dashed lines show \\texttt{exception\\_only} (99.83\\%) and \\texttt{no\\_trace} (75.13\\%) as upper and lower bounds. Tail-256 (${\\approx}$ \\texttt{no\\_trace}) indicates the signal window begins approximately 256 tokens from the trace terminus.}\n\\label{fig:trace_length}\n\\end{figure}\n\nAs shown in Table~\\ref{tab:trace_length} and Figure~\\ref{fig:trace_length}, all four trace length conditions fall within a 5pp range (77.2\\%--81.8\\%).\nTo quantify the reliability of the observed differences, Table~\\ref{tab:trace_length_pairwise} reports paired bootstrap comparisons ($B{=}10{,}000$, seed=42) across all condition pairs.\n\n\\begin{table}[t]\n\\centering\n\\caption{Pairwise paired bootstrap comparisons for trace length ablation ($B{=}10{,}000$, seed=42). $\\Delta$ = accuracy difference between the two conditions (first $-$ second in the budget group; condition $-$ baseline in the other groups). **$p{<}0.01$; ***$p{<}0.001$.}\n\\label{tab:trace_length_pairwise}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n& \\textbf{Comparison} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} & \\textbf{$p$-value} \\\\\n\\midrule\n\\multirow{4}{*}{\\rotatebox{90}{\\scriptsize Budget}}\n& 512 vs.\\ 256           & $+$1.60  & [$-$0.34, $+$3.53]   & 0.117 \\\\\n& 1024 vs.\\ 512          & $-$3.19  & [$-$5.29, $-$1.09]   & 0.002** \\\\\n& no\\_limit vs.\\ 1024    & $+$4.54  & [$+$2.52, $+$6.55]   & ${<}$0.001*** \\\\\n& no\\_limit vs.\\ 256     & $+$2.94  & [$+$0.84, $+$5.04]   & 0.006** \\\\\n\\midrule\n\\multirow{4}{*}{\\rotatebox{90}{\\scriptsize vs.\\ no\\_trace}}\n& 256 $-$ no\\_trace       & $+$3.70  & [$+$1.43, $+$6.05]   & 0.002** \\\\\n& 512 $-$ no\\_trace       & $+$5.29  & [$+$3.03, $+$7.56]   & ${<}$0.001*** \\\\\n& 1024 $-$ no\\_trace      & $+$2.10  & [$-$0.17, $+$4.37]   & 0.078 \\\\\n& no\\_limit $-$ no\\_trace & $+$6.64  & [$+$4.37, $+$8.99]   & ${<}$0.001*** \\\\\n\\midrule\n\\multirow{4}{*}{\\rotatebox{90}{\\scriptsize vs.\\ exc.}}\n& 256 $-$ exc\\_only       & $-$21.01 & [$-$23.45, $-$18.74] & ${<}$0.001*** \\\\\n& 512 $-$ exc\\_only       & $-$19.41 & [$-$21.76, $-$17.14] & ${<}$0.001*** \\\\\n& 1024 $-$ exc\\_only      & $-$22.61 & [$-$25.04, $-$20.25] & ${<}$0.001*** \\\\\n& no\\_limit $-$ exc\\_only & $-$18.07 & [$-$20.34, $-$15.88] & ${<}$0.001*** \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\paragraph{Non-monotonic pattern (head-truncation).}\nUnder head-truncation (retaining trace prefixes), the trend is non-monotonic: 512 tokens (80.42\\%) slightly outperforms 256 tokens (78.82\\%), but doubling to 1024 tokens \\emph{decreases} accuracy to 77.23\\%, a statistically significant 3.19pp drop ($p{=}0.002$, 95\\% CI [$-$5.29, $-$1.09]).\nThe no-limit condition (81.76\\%) recovers and significantly exceeds 1024 tokens ($p{<}0.001$), but 1024 tokens is not significantly better than \\texttt{no\\_trace} (75.13\\%; $\\Delta{=}{+}2.10$pp, $p{=}0.078$, 95\\% CI [$-$0.17, $+$4.37]).\nThis non-monotonicity is specific to head-truncation: the 1024-token prefix retains enough irrelevant content to mislead the model while discarding diagnostic events that appear near the trace terminus.\nUnder tail-truncation, accuracy increases monotonically for Qwen-7B and Qwen-1.5B (Table~\\ref{tab:tail_cross_model}); only DeepSeek-6.7B shows a mild $-$1.5pp decrease at tail-1024$\\to$tail-2048, attributable to architecture-specific long-context sensitivity rather than a systematic mid-length pathology.\n\n\\paragraph{Comparison to baselines.}\nAll four trace budget conditions significantly exceed \\texttt{no\\_trace} except 1024 tokens ($p{=}0.078$), confirming that raw trace content provides some signal but unreliably so.\nThe gap to \\texttt{exception\\_only} (99.83\\%) is massive for every budget condition (18--23pp, all $p{<}0.001$), underscoring that even unlimited raw traces cannot substitute for targeted signal extraction.\nThe best full-trace condition (no\\_limit, 81.76\\%) still lags \\texttt{exception\\_only} by 18.07pp (95\\% CI [$-$20.34, $-$15.88]).\n\n\\paragraph{Interpretation.}\nThese results rule out input truncation as the primary explanation for the full-trace performance gap: even with unlimited tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides.\nThe non-monotonic dip at 1024 tokens is consistent with a ``worst-of-both-worlds'' regime where the model receives enough noisy context to dilute the signal but not enough to compensate through broader coverage.\nThe result reinforces the information density interpretation (\\S\\ref{sec:density}): the gap between full traces and VOTA is driven by the \\emph{content} of the trace (irrelevant lines diluting the diagnostic signal), not its \\emph{length}.\nIn contrast, VOTA's compressed representation concentrates the diagnostic signal into fewer tokens, making it sensitive to truncation when those tokens are removed (\\S\\ref{sec:cross_model}).\n\n\\paragraph{Truncation direction.}\nTail-truncation (retaining the last $k$ tokens) dramatically outperforms head-truncation: \\texttt{tail\\_2048} achieves 97.31\\% vs.\\ \\texttt{head\\_2048} (no\\_limit) at 81.76\\%, a 15.55pp improvement.\nEven \\texttt{tail\\_512} (93.61\\%) exceeds every head-truncation condition by over 11pp.\n\nHowever, \\texttt{tail\\_256} (77.48\\%) performs at the \\texttt{no\\_trace} baseline level (75.13\\%), indicating that the diagnostic signal does not reside in the very last trace lines.\nThe critical jump occurs between 256 and 512 tail tokens (+16.13pp), localizing the signal window to approximately 256--512 tokens from the trace terminus.\nThis is consistent with Python's execution model: exception tracebacks and assertion comparisons appear near the end of the trace but are preceded by the final function call frames, placing them typically 300--500 tokens from the terminus rather than at the absolute end.\n\nThe 18.07pp gap from \\texttt{full\\_trace} to \\texttt{exception\\_only} decomposes as: 86\\% positional concentration (recovered by tail-truncation at 2048 tokens) and 14\\% residual content noise (the 2.52pp gap from \\texttt{tail\\_2048} to \\texttt{exception\\_only} that persists regardless of truncation direction).\nThe fact that \\texttt{exception\\_only} (99.83\\%) still outperforms \\texttt{tail\\_2048} (97.31\\%) confirms that semantic extraction (identifying the exception type and message) is superior to positional extraction (keeping a fixed window), because the model need not filter out non-diagnostic lines that happen to fall within the window.\n\n\\paragraph{Cross-model budget curve.}\nTable~\\ref{tab:tail_cross_model} extends the tail-truncation analysis to a full budget sweep across three models spanning two architecture families and an 8.7$\\times$ parameter range.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model tail-truncation budget curve ($N{=}1{,}190$). A sharp phase transition occurs at 256$\\to$512 tokens across all models (+14.7--23.0pp), after which accuracy converges into a narrow band regardless of scale or architecture. $\\downarrow$: non-monotonic decrease at 1024$\\to$2048 (DeepSeek only).}\n\\label{tab:tail_cross_model}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{tail-256} & \\textbf{tail-512} & \\textbf{tail-1024} & \\textbf{tail-2048} & \\textbf{exc\\_only} \\\\\n\\midrule\nQwen-7B (7B) & 78.9 & 93.6 & 96.5 & 97.3 & 99.83 \\\\\nDeepSeek (6.7B) & 76.4 & 93.9 & 96.5 & 95.0$\\downarrow$ & 99.33 \\\\\nQwen-1.5B (1.5B) & 72.6 & 95.6 & 96.6 & 97.9 & 99.83 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model truncation direction comparison ($N{=}1{,}190$). Head-truncation retains the first 2,048 tokens; tail-truncation retains the last 2,048. The gap widens at smaller scale, consistent with smaller models' greater reliance on positional signal proximity.}\n\\label{tab:head_vs_tail}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{head-2048 (\\%)} & \\textbf{tail-2048 (\\%)} & \\textbf{Gap (pp)} \\\\\n\\midrule\nQwen-7B & 81.8 & 97.3 & +15.5 \\\\\nDeepSeek-6.7B & 78.7 & 95.0 & +16.3 \\\\\nQwen-1.5B & 75.3 & 97.9 & +22.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree patterns emerge from the budget curve.\n\\emph{Phase transition at 256$\\to$512 tokens}: all three models jump +14.7--23.0pp (Qwen-7B +14.7, DeepSeek +17.5, Qwen-1.5B +23.0), crossing from near-baseline to near-ceiling in a single budget doubling.\nThe threshold aligns with the typical exception traceback length (${\\sim}$500 tokens): below this budget, the diagnostic event is truncated; above it, the event is captured regardless of model capacity or architecture.\n\n\\emph{Convergence at tail-512+}: once the phase transition is crossed, all three models converge into a narrow 93.6--95.6\\% band at tail-512 and an even tighter 96.5--96.6\\% band at tail-1024.\nScale and architecture differences that dominate the signal-poor regime (tail-256 range: 72.6--78.9\\%, 6.3pp) vanish in the signal-rich regime (tail-1024 range: 96.5--96.6\\%, 0.1pp).\n\n\\emph{Scale behavior inversion}: in the signal-poor regime (tail-256), smaller models perform worse (Qwen-1.5B 72.6\\% vs.\\ Qwen-7B 78.9\\%, $-$6.3pp), mirroring the \\texttt{no\\_trace} scale pattern.\nIn the signal-rich regime (tail-512+), this reverses: Qwen-1.5B matches or exceeds Qwen-7B (95.6\\% vs.\\ 93.6\\% at tail-512; 97.9\\% vs.\\ 97.3\\% at tail-2048), confirming that sufficient trace signal eliminates the capacity advantage.\n\n\\emph{Non-monotonicity}: DeepSeek-6.7B shows a $-$1.5pp decrease from tail-1024 (96.5\\%) to tail-2048 (95.0\\%), while the other two models increase monotonically.\nThis architecture-specific sensitivity is consistent with DeepSeek's known vulnerability to long-context formatting (Appendix~\\ref{sec:training_dynamics}): additional tokens beyond the diagnostic window introduce noise that this model cannot filter as effectively.\n\nTable~\\ref{tab:head_vs_tail} confirms the truncation direction effect across all models: tail-2048 outperforms head-2048 by 15.5--22.6pp.\nThe gap is largest for Qwen-1.5B (+22.6pp), indicating that smaller models benefit most from positional proximity to the diagnostic signal, as they lack the capacity to locate it within longer, noisier prefixes.\n\n%% ============================================================\n\\section{Calibration Analysis}\n\\label{sec:calibration_full}\n\nBeyond accuracy, we evaluate whether trace conditions affect prediction calibration, motivated by recent findings that code LLM confidence is often poorly calibrated \\citep{spiess2025calibration}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Calibration metrics on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). ECE = expected calibration error; Brier = Brier score. Lower is better for both.}\n\\label{tab:calibration}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{ECE $\\downarrow$} & \\textbf{Brier $\\downarrow$} \\\\\n\\midrule\nae\\_only & \\textbf{0.0004} & \\textbf{0.0008} \\\\\nexception\\_only & 0.0027 & 0.0013 \\\\\nVOTA & 0.0054 & 0.005 \\\\\nfull\\_trace & 0.096 & 0.144 \\\\\nno\\_trace & 0.171 & 0.197 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:calibration} shows that calibration quality mirrors the Tier~1/2 hierarchy.\nTier~1 conditions (\\texttt{ae\\_only}: ECE=0.0004; \\texttt{exception\\_only}: ECE=0.0027) produce near-perfectly calibrated predictions, while \\texttt{full\\_trace} (ECE=0.096) and \\texttt{no\\_trace} (ECE=0.171) exhibit substantial miscalibration.\nVOTA (ECE=0.0054) is well-calibrated but slightly worse than either Tier~1 component alone, reinforcing the pattern that combining trace signals dilutes rather than improves the prediction signal.\n\nThe Brier scores tell a consistent story: \\texttt{ae\\_only} (0.0008) and \\texttt{exception\\_only} (0.0013) achieve near-zero scores, while \\texttt{no\\_trace} (0.197) indicates substantial miscalibration.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_calibration}\n\\caption{Reliability diagrams for four trace conditions on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). \\texttt{exception\\_only} (ECE=0.0027) clusters near the diagonal, while \\texttt{no\\_trace} (ECE=0.171) exhibits systematic overconfidence, a 63$\\times$ gap.}\n\\label{fig:calibration}\n\\end{figure}\n\n%% ============================================================\n\\section{Error Overlap Analysis}\n\\label{sec:error_overlap}\n\nWe analyze the overlap between error sets of different conditions to determine whether they fail on the same samples (Figure~\\ref{fig:error_overlap}).\n\n\\texttt{exception\\_only}'s 2 errors (samples 901 and 905) have zero intersection with the error sets of all other conditions (Jaccard = 0.000 in all pairwise comparisons).\nThis orthogonality arises because \\texttt{exception\\_only} errors are caused by \\texttt{GeneratorExit} false positives (pass samples misclassified as fail due to benign \\texttt{BaseException} events), while errors from other conditions are predominantly fail samples misclassified as pass due to insufficient signal.\n\nAmong non-exception conditions, error sets exhibit hierarchical containment: \\texttt{ae\\_only} $\\subset$ VOTA $\\subset$ \\texttt{loop\\_only} $\\subset$ \\texttt{no\\_trace}, with pairwise Jaccard indices increasing with signal overlap.\n\\texttt{loop\\_only} and \\texttt{full\\_trace} share the highest overlap (Jaccard ${\\sim}$0.65), reflecting their shared reliance on behavioral patterns rather than explicit fault indicators.\n\nThis analysis confirms that \\texttt{exception\\_only} operates on an independent signal dimension: its errors are representation ambiguities (iterator protocol artifacts) rather than information deficits, explaining why combining it with other signals cannot eliminate these specific errors.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{error_overlap}\n\\caption{Jaccard similarity between error sets of different conditions (Qwen-7B, seed=42, $N{=}1{,}190$). \\texttt{exception\\_only} (exc\\_only) has zero overlap with all other conditions, confirming it operates on an independent signal dimension.}\n\\label{fig:error_overlap}\n\\end{figure}\n\n%% ============================================================\n\\section{Cross-Dataset Generalization: DebugBench}\n\\label{sec:debugbench_full}\n\nTo test whether exception-based verdict prediction generalizes beyond LLM-generated solutions, we evaluate on DebugBench \\citep{tian2024debugbench}---a dataset of human-written programs with synthetically injected bugs (single-point mutations such as operator replacement, variable misuse, and missing statements).\nAfter filtering for executable Python samples with valid traces, we retain 426 samples with a near-balanced class distribution (majority baseline: 51.4\\%).\n\n\\begin{table}[t]\n\\centering\n\\caption{Generalization to DebugBench ($N{=}426$, Qwen-2.5-7B, seed=42). Wilson 95\\% CIs. The component ranking (exception\\_only $\\geq$ VOTA $>$ no\\_trace) is preserved, and exception\\_only achieves perfect accuracy.}\n\\label{tab:debugbench}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Acc (\\%)} & \\textbf{95\\% CI} \\\\\n\\midrule\nexception\\_only & \\textbf{100.00} & [99.14, 100.00] \\\\\nVOTA & 99.77 & [99.30, 100.00] \\\\\nno\\_trace & 96.71 & [94.80, 98.40] \\\\\n\\midrule\nMajority baseline & 51.41 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:debugbench} shows that the component ranking from the main experiments is preserved: \\texttt{exception\\_only} (100.00\\%) $\\geq$ VOTA (99.77\\%) $>$ \\texttt{no\\_trace} (96.71\\%).\nThe \\texttt{exception\\_only} condition achieves perfect accuracy, confirming that the exception-based representation generalizes to a different fault distribution without degradation.\n\nThe absolute margins are much narrower than on the main dataset: the \\texttt{no\\_trace} baseline already achieves 96.71\\%---compared to 75.13\\% on HumanEval+MBPP---leaving only 3.29pp of headroom for trace-based improvement.\nThis ceiling effect reflects a fundamental difference in fault characteristics: DebugBench bugs are synthetically injected single-point mutations, which produce code that is structurally dissimilar from the original correct solution; a model can often identify the fault from source code alone.\nIn contrast, the HumanEval+MBPP solutions are LLM-generated, producing natural errors (logic mistakes, edge-case failures) where the faulty and correct solutions may be structurally similar, making code-only verdict prediction substantially harder.\n\nThese results support exception-based verdict prediction as a generalizable approach---the method does not degrade on an out-of-distribution dataset, and the exception dominance ranking (exception\\_only $\\geq$ VOTA $>$ no\\_trace) is consistent across both datasets---but the narrow DebugBench margins are insufficient to independently validate trace importance.\nThe 24.70pp trace lift on the main dataset (no\\_trace 75.13\\% $\\to$ exception\\_only 99.83\\%) remains the primary evidence for the value of exception-based trace signals.\n\n%% ============================================================\n\\section{Cross-Model Robustness Analysis}\n\\label{sec:robustness_analysis}\n\nThe cross-model gap pattern (Table~\\ref{tab:cross_model}) suggests a design principle: \\emph{trace representations should match the model capability floor, not the ceiling.}\nException events are consistently the most effective component on both models, and their structural simplicity---a fixed-format error message---ensures that the relative advantage over richer representations holds across all seeds.\nTwo of three DeepSeek seeds match Qwen-level accuracy (99.33\\%); the outlier (seed 123, 91.09\\%) we hypothesize reflects LoRA initialization sensitivity landing in a suboptimal basin (fail recall = 70.5\\%, though direct evidence is lacking), not a failure of the exception signal itself---even this outlier outperforms VOTA (84.45\\%) by 6.64pp.\nThe VOTA cross-model gap is confounded by two factors: (1)~tokenizer efficiency---the DeepSeek tokenizer averages 2{,}626 tokens per VOTA sample versus Qwen's 1{,}929, causing 91.7\\% of training samples to exceed the 2{,}048-token context window; content-aware truncation preferentially removes the terminal structured prompt, preserving the verdict label but truncating trace content---and (2)~base model capability differences, consistent with findings that SFT generalization depends on pretrain quality \\citep{yang2024generalization}.\nThe two factors cannot be disentangled in the current experimental design.\nOur \\texttt{exception\\_only} design sidesteps the truncation confound entirely: inputs have a median of 150 tokens (mean 398), well below the 2{,}048-token context window, so no training samples are truncated on either model.\nThe resulting 0.56pp cross-model gap (Table~\\ref{tab:cross_model}) is therefore a clean measure of model capability differences, making the ``capability floor'' principle directly testable.\nThe practical implication is that trace-based systems should default to the simplest sufficient signal; for smaller models, training stability (multi-seed selection, warmup schedules) is a secondary but addressable concern.\n\n%% ============================================================\n\\section{Training Dynamics and Loss Decoupling}\n\\label{sec:training_dynamics}\n\nThe DeepSeek \\texttt{exception\\_only} results reveal two instructive training dynamics.\nFirst, epoch-level analysis shows mild degradation in 2/3 seeds: seed 42 peaks at 99.83\\% after epoch~1 but settles at 99.33\\% by epoch~3 ($-$0.50pp), seed 123 degrades from 91.43\\% to 91.09\\% ($-$0.34pp), while seed 456 shows no epoch degradation (99.33\\% at both epoch~1 and epoch~3).\nEarly stopping may yield marginal gains for some seeds, but the epoch effect is small (${\\leq}$0.5pp) compared to the seed effect (8.24pp between seeds 42 and 123).\n\nSecond, seeds 123 and 456 converge to nearly identical final training losses (0.122 and 0.123 respectively), yet their accuracies differ by 8.24pp (91.09\\% vs.\\ 99.33\\%).\nThe critical difference lies in fail recall: seeds 42 and 456 achieve 100\\%, while seed 123 achieves only 70.5\\%---the LoRA initialization in seed 123 fails to learn the exception$\\to$fail mapping for a substantial fraction of failing samples, even though the per-token loss appears converged.\nThis demonstrates that token-level training loss can mask fundamental differences in sample-level classification ability, suggesting a parallel to the eval-loss/accuracy decoupling observed in DeepSeek VOTA (where eval loss rose 65\\% from epoch 1 to 3 while accuracy improved by 6.3pp) at the training phase.\nThe practical recommendation is twofold: (1)~use task-specific metrics (accuracy, fail recall) for checkpoint and seed selection rather than training or evaluation loss, and (2)~for deployment on smaller models, train multiple seeds and select the best, as a single run may not reliably converge to the correct classification boundary.\n\n\\paragraph{Format collapse, not semantic failure.}\nThe 100 errors of seed 123 are not semantic failures but generation format collapse: on inputs exceeding 4,000 characters (those containing verbose locals dumps), the model echoes trace content instead of emitting a verdict token, while achieving zero errors on shorter inputs.\nThis indicates that the LoRA initialization of seed 123 specifically compromises long-context format compliance rather than exception signal comprehension, further supporting the robustness advantage of compact \\texttt{exception\\_only} inputs.\n\nThe contrast with VOTA is instructive: DeepSeek VOTA accuracy monotonically increases from 78.15\\% to 84.45\\% across epochs, but is consistent with a performance limit associated with the high trace truncation rate (\\S\\ref{sec:cross_model})---the model progressively extracts signal from samples with intact trace content but cannot fully compensate for the information loss in the truncated majority.\nThe 84.45\\% accuracy reflects a combination of trace information loss and model capability constraints.\n\n%% ============================================================\n\\section{Deduplication Statistics}\n\\label{sec:dedup_stats}\n\nTable~\\ref{tab:dedup} reports the duplication rates across trace formats.\nBecause multiple passing solutions to the same problem produce identical (input, output) pairs in the \\texttt{exception\\_only} format---correct executions raise no exceptions, so the trace content is the same regardless of the solution's internal logic---the dataset contains duplicate rows.\nTrain--test input overlap is zero (split by problem ID), so no information leakage occurs.\nThe high duplication in \\texttt{exception\\_only} does not affect our experimental conclusions: after deduplication the training set still contains 2,858 unique samples and the test set 607, providing sufficient coverage for the 591-problem benchmark.\nThe \\texttt{exception\\_only} test set contains 48.99\\% duplicate inputs due to representation compactness; all confidence intervals treat samples as independent Bernoulli trials.\n\n\\begin{table}[t]\n\\centering\n\\caption{Deduplication statistics. The \\texttt{exception\\_only} format collapses multiple passing solutions into identical rows because correct executions produce no exception events. Train--test input overlap is 0 (no leakage).}\n\\label{tab:dedup}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Split} & \\textbf{Total} & \\textbf{Unique} & \\textbf{Dup.\\ rate} \\\\\n\\midrule\nexception\\_only train & 4{,}720 & 2{,}858 & 39.45\\% \\\\\nexception\\_only test  & 1{,}190 &   607 & 48.99\\% \\\\\nraw\\_traces (full)    & 5{,}910 & 5{,}803 &  1.81\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n\\section{Regex Baseline Analysis}\n\\label{sec:regex_baselines}\n\nTo establish a non-learning upper bound, we evaluate six regex-based baselines on the \\texttt{exception\\_only} test set ($N{=}1{,}190$) and two format-specific baselines on VOTA and \\texttt{full\\_trace} inputs.\n\n\\begin{table}[t]\n\\centering\n\\caption{Regex baseline accuracy ($N{=}1{,}190$). B4 is the strongest semantic baseline (6.22pp below SFT \\texttt{exception\\_only}, McNemar $p{<}0.001$). B6 uses an error count threshold. $^\\ddag$B5 exploits a data formatting artifact: the \\texttt{[No exception data in trace]} marker is deterministically present in all pass samples, making this a format-level shortcut rather than a genuine exception-based heuristic.}\n\\label{tab:regex}\n\\small\n\\begin{tabular}{llc}\n\\toprule\n\\textbf{Baseline} & \\textbf{Method} & \\textbf{Acc (\\%)} \\\\\n\\midrule\nB1: \\texttt{[ERROR]} presence & string match & 93.45 \\\\\nB2: Traceback presence & string match & 71.51 \\\\\nB3: Any keyword & union of B1+B2+Exception & 93.45 \\\\\nB4: Exception type regex & regex on exception class names & \\textbf{93.61} \\\\\nB5: Format marker & \\texttt{[No exception data]} $\\to$ pass & 99.33$^\\ddag$ \\\\\nB6: Error count $\\geq$2 & count threshold & 92.02 \\\\\n\\midrule\nVOTA format regex & best regex on VOTA traces & 75.55 \\\\\nfull\\_trace format regex & best regex on full traces & 77.39 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe strongest legitimate baseline (B4, 93.61\\%) applies regex pattern-matching on Python exception class names (e.g., \\texttt{ValueError}, \\texttt{TypeError}).\nIts errors concentrate on 8 boundary samples where a \\texttt{ValueError} is raised inside a \\texttt{try/except} block and caught---the program passes despite an exception occurring in the trace.\nSFT \\texttt{exception\\_only} correctly classifies 6 of these 8 samples, indicating that the model learns the semantic distinction between caught (benign) and uncaught (fault-indicating) exceptions.\nB5 (99.33\\%) achieves near-SFT accuracy but relies on the deterministic presence of a format marker in pass-class traces, which is an artifact of the trace preprocessing pipeline rather than a generalizable signal; McNemar test vs.\\ SFT yields $p{=}0.041$, confirming a statistically significant difference.\n\n\\paragraph{Cross-format comparison.}\nTable~\\ref{tab:regex_cross_format} compares SFT and the best applicable regex baseline for each trace format.\nThe SFT advantage increases with format complexity: \\texttt{no\\_trace} (+3.62pp over majority baseline) $<$ \\texttt{full\\_trace} (+4.37pp) $<$ \\texttt{exception\\_only} (+6.22pp) $\\ll$ VOTA (+23.86pp).\nThe VOTA gap is largest because its structured multi-component format carries semantic content that regex cannot parse, while \\texttt{exception\\_only}'s simpler format allows regex to capture most of the signal.\n\n\\begin{table}[t]\n\\centering\n\\caption{SFT vs.\\ best regex baseline by trace format ($N{=}1{,}190$). Regex baselines: majority class for \\texttt{no\\_trace}, keyword matching for \\texttt{full\\_trace}, pattern matching for VOTA, exception type regex (B4) for \\texttt{exception\\_only}.}\n\\label{tab:regex_cross_format}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Format} & \\textbf{SFT (\\%)} & \\textbf{Regex (\\%)} & \\textbf{$\\Delta$ (pp)} \\\\\n\\midrule\nexception\\_only & 99.83 & 93.61 & +6.22 \\\\\nVOTA & 99.41 & 75.55 & +23.86 \\\\\nfull\\_trace & 81.76 & 77.39 & +4.37 \\\\\nno\\_trace & 75.13 & 71.51 & +3.62 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n\\section{Cross-Model Zero-Shot Comparison}\n\\label{sec:zeroshot_cross_model}\n\nTable~\\ref{tab:zeroshot_cross_model} compares zero-shot and SFT \\texttt{exception\\_only} accuracy across four models.\nZero-shot performance does not correlate with model size: the smallest model (Qwen-1.5B, 93.45\\%) outperforms all larger models, while the largest (CodeLlama-13B) falls below majority baseline.\nSFT compresses the 42.44pp zero-shot range to 0.56pp, eliminating architecture-dependent variance.\n\n\\begin{table}[t]\n\\centering\n\\caption{Zero-shot vs.\\ SFT \\texttt{exception\\_only} across four models ($N{=}1{,}190$). Zero-shot accuracy is uncorrelated with model size; SFT normalizes cross-architecture variance from 42.44pp to 0.56pp.}\n\\label{tab:zeroshot_cross_model}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Model} & \\textbf{Size} & \\textbf{Zero-shot (\\%)} & \\textbf{SFT (\\%)} & \\textbf{$\\Delta$ (pp)} \\\\\n\\midrule\nQwen-1.5B & 1.5B & 93.45 & 99.83 & +6.38 \\\\\nDeepSeek-6.7B & 6.7B & 90.59 & 99.33 & +8.74 \\\\\nQwen-7B & 7B & 89.08 & 99.83 & +10.75 \\\\\nCodeLlama-13B & 13B & 51.01 & 99.89 & +48.88 \\\\\n\\midrule\nRange & --- & 42.44pp & 0.56pp & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 667,
      "startLine": 1,
      "totalLines": 667
    }
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive view of the paper's current state. Let me also check if there's a CodeLlama-13B entry in the tail budget curve table, since the user mentioned CodeLlama-13B tail-512=97.5% data should be included.

Looking at Table `tab:tail_cross_model` (lines 386-400 of appendix.tex), it has:
- Qwen-7B: tail-256=78.9, tail-512=93.6, tail-1024=96.5, tail-2048=97.3


- DeepSeek (6.7B): tail-256=76.4, tail-512=93.9, tail-1024=96.5, tail-2048=95.0
- Qwen-1.5B: tail-256=72.6, tail-512=95.6, tail-1024=96.6, tail-2048=97.9

CodeLlama-13B is missing from the table, but the user expects it to be there with tail-512=97.5%. Currently only three models are present when the budget curve should include four models with all tail metrics.

For the head-tail gap analysis, I have three models documented in the table with gaps ranging from 15.5pp to 22.6pp, which matches what's mentioned in the text. The phase transition and convergence patterns are already written up, but I need to track down the missing CodeLlama-13B data points for tail-256 and tail-1024 since those are still running. I'm checking what CodeLlama-13B results are actually available—tail-512 is done at 97.5%, but tail-256 and tail-1024 are still running, so tail-2048 likely isn't ready either. This means the tables need to reflect only what's been completed, and the text references to "all three models" are accurate since CodeLlama isn't fully included yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "8f597472-51d6-4b34-af01-63ed3b0dc20d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167swEnjD8TSeXJkQtNxnX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16257,
      "cache_read_input_tokens": 34701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16257
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

_source line 19_

Now I have enough data to generate the audit. Let me also check if CodeLlama-13B is mentioned in the budget curve discussion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "3fe4d046-fa09-4015-8164-904833a55e5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167swEnjD8TSeXJkQtNxnX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16257,
      "cache_read_input_tokens": 34701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16257
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

_source line 20_

<details open><summary>🔧 Tool call — Grep · `toolu_01L59JWVdkz98MQzXbQaXoFn`</summary>

```json
{
  "pattern": "CodeLlama.*tail|codellama.*tail|CL-13B.*tail",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper",
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
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "246922c6-b68a-4a58-932e-8b0422a00a82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167swEnjD8TSeXJkQtNxnX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16257,
      "cache_read_input_tokens": 34701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16257
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

_source line 21 · 2026-05-18T01:47:59.107Z_

<details><summary>↩ Tool result · `toolu_01L59JWVdkz98MQzXbQaXoFn`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "b4d10191-52bc-4086-acdb-5fbeae5f5fd5",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01BYMS6BfC5jujneoG6LWkDx`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/paper_patch_audit/ 2>/dev/null || echo \"DIR_NOT_EXISTS\"",
  "description": "Check if output directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "74dfa695-89cf-4257-a158-a795cd5380ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167swEnjD8TSeXJkQtNxnX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16257,
      "cache_read_input_tokens": 34701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16257
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

_source line 23 · 2026-05-18T01:48:00.824Z_

<details><summary>↩ Tool result · `toolu_01BYMS6BfC5jujneoG6LWkDx`</summary>

```text
DIR_NOT_EXISTS
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "e1771115-ff40-498e-80d0-2eabd9f4becf",
  "tool_use_result": {
    "stdout": "DIR_NOT_EXISTS",
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

_source line 24_

<details open><summary>🔧 Tool call — Bash · `toolu_01QpSC7aopmubCMwVM3uDzky`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/paper_patch_audit",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "d027426e-59c7-49f4-9f6c-839c37449c86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G6PfHoLzu7S6bV6cDschfT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1401,
      "cache_read_input_tokens": 50958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1401
      },
      "output_tokens": 62,
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

_source line 25 · 2026-05-18T01:48:04.439Z_

<details><summary>↩ Tool result · `toolu_01QpSC7aopmubCMwVM3uDzky`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "9eff49e3-bf3d-4f47-98f2-a79467cc5f2b",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Write · `toolu_0187WkFd6dweNbgxMbEy8TmL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/paper_patch_audit/paper_patch_status.md",
  "content": "# Paper Patch Status: Budget Curve + Head-Tail Data\n\n**审计时间**: 2026-05-18  \n**论文路径**: `/root/trace-verdict-study/docs/paper/` (服务器) / `docs/paper/` (本地)\n\n---\n\n## 一、Budget Curve（tail-256/512/1024/2048）\n\n### 已写入 ✅\n\n| 数据点 | 位置 | 状态 |\n|--------|------|------|\n| Qwen-7B: 78.9/93.6/96.5/97.3 | appendix.tex Table 6 (`tab:tail_cross_model`) | ✅ 完整 |\n| DeepSeek-6.7B: 76.4/93.9/96.5/95.0↓ | appendix.tex Table 6 | ✅ 完整 |\n| Qwen-1.5B: 72.6/95.6/96.6/97.9 | appendix.tex Table 6 | ✅ 完整 |\n| Phase transition 256→512: +14.7~+23pp | experiments.tex L152 + appendix.tex L419-421 | ✅ |\n| tail-512 convergence (93.6-95.6% band) | appendix.tex L422-423 | ✅ |\n| tail-1024 convergence (96.5-96.6%) | appendix.tex L422-423 | ✅ |\n| Non-monotonicity: DeepSeek only, -1.5pp at 1024→2048 | experiments.tex L147, appendix.tex L428-429 | ✅ 正确描述为 architecture-specific |\n| Scale behavior inversion (signal-poor vs signal-rich) | appendix.tex L425-426 | ✅ |\n| Budget curve figure (`budget_curve`) | appendix.tex Fig 5 (`fig:trace_length`) | ✅ (仅 Qwen-7B) |\n\n### 缺失 ❌\n\n| 数据点 | 状态 | 说明 |\n|--------|------|------|\n| **CodeLlama-13B tail-512 = 97.5%** | ❌ 未写入 | 数据已有，表格和正文均无 |\n| **CodeLlama-13B tail-256** | ⏳ 实验运行中 | 等待结果 |\n| **CodeLlama-13B tail-1024** | ⏳ 实验运行中 | 等待结果 |\n| **CodeLlama-13B tail-2048** | ❓ 未确认 | 未见相关数据 |\n| 4-model budget curve figure 更新 | ❌ | 当前 figure 仅含 Qwen-7B 单模型 |\n\n### 正文描述需更新的地方\n\n- `experiments.tex` L152: \"all three models jump\" → 需改为 4 模型（待 CL-13B 数据齐全）\n- `appendix.tex` L382-383: \"three models spanning two architecture families\" → 需扩展为 four models, three families\n- `appendix.tex` Table 6 caption: 需加入 CodeLlama-13B 行\n- `appendix.tex` L419: \"all three models\" → \"all four models\"（待数据齐全）\n\n---\n\n## 二、Head-Tail Gap（跨模型对比）\n\n### 已写入 ✅\n\n| 数据点 | 位置 | 状态 |\n|--------|------|------|\n| Qwen-7B: head-2048=81.8%, tail-2048=97.3%, gap=+15.5pp | appendix.tex Table 7 (`tab:head_vs_tail`) | ✅ |\n| DeepSeek-6.7B: head-2048=78.7%, tail-2048=95.0%, gap=+16.3pp | appendix.tex Table 7 | ✅ |\n| Qwen-1.5B: head-2048=75.3%, tail-2048=97.9%, gap=+22.6pp | appendix.tex Table 7 | ✅ |\n| 15.5-22.6pp gap range | experiments.tex L150 | ✅ |\n| 小模型 gap 更大 (Qwen-1.5B +22.6pp vs Qwen-7B +15.5pp) | experiments.tex L150-151 + appendix.tex L431-432 | ✅ |\n\n### 缺失 ❌\n\n| 数据点 | 状态 | 说明 |\n|--------|------|------|\n| **CodeLlama-13B head-2048 vs tail-2048** | ❌ | 无 head-2048 实验数据 |\n\n---\n\n## 三、Non-Monotonicity Correction\n\n### 已写入 ✅\n\n正文和附录均已正确表述：仅 DeepSeek 在 tail-1024→2048 下降 1.5pp，非 universal pattern。\n\n- experiments.tex L147: \"only DeepSeek showing a mild architecture-specific reversal\"\n- appendix.tex L357: \"only DeepSeek-6.7B shows a mild −1.5pp decrease\"\n- appendix.tex L428-429: 明确说 \"while the other two models increase monotonically\"\n\n**状态**: ✅ 无需修改\n\n---\n\n## 四、总结\n\n### 已完成的 patch\n1. ✅ 3-model budget curve 表格和分析（Qwen-7B, DeepSeek, Qwen-1.5B）\n2. ✅ Phase transition / convergence / scale inversion 叙事\n3. ✅ 3-model head-tail gap 表格和分析\n4. ✅ Non-monotonicity 正确描述\n5. ✅ Budget curve figure (单模型版)\n\n### 待完成的 patch（按优先级）\n1. **P1**: CodeLlama-13B tail-512=97.5% 写入 Table 6（数据已有，立即可做）\n2. **P2**: 等待 CL-13B tail-256 和 tail-1024 实验完成后补全表格\n3. **P3**: 更新正文 \"three models\" → \"four models\"（待 P2 完成）\n4. **P4**: 更新 budget curve figure 为 4-model 版本\n5. **P5**: CodeLlama-13B head-tail gap 数据（需要 head-2048 实验）\n\n### 需要更新的章节列表\n| 文件 | 章节/位置 | 更新内容 |\n|------|-----------|----------|\n| `experiments.tex` | §4.5 Additional Analyses, L149-156 | 加入 CL-13B 数据，更新 \"three models\" |\n| `appendix.tex` | §Trace Length Full, Table 6 | 加 CL-13B 行 |\n| `appendix.tex` | §Trace Length Full, Table 7 | 加 CL-13B 行（待 head-2048 数据）|\n| `appendix.tex` | L382-383, L419 | \"three models\" → \"four models\" |\n| `appendix.tex` | budget_curve figure | 更新为多模型版本 |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "8b3e4c1e-bd64-4bf8-9f85-90f9641be041",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHtBEr6BhY6YAcSqtaRW6L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 126,
      "cache_read_input_tokens": 52359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 126
      },
      "output_tokens": 53,
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

_source line 27 · 2026-05-18T01:48:39.399Z_

<details><summary>↩ Tool result · `toolu_0187WkFd6dweNbgxMbEy8TmL`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/paper_patch_audit/paper_patch_status.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "5ac25c35-4ef8-48a0-aa38-642b47cf5247",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/paper_patch_audit/paper_patch_status.md",
    "content": "# Paper Patch Status: Budget Curve + Head-Tail Data\n\n**审计时间**: 2026-05-18  \n**论文路径**: `/root/trace-verdict-study/docs/paper/` (服务器) / `docs/paper/` (本地)\n\n---\n\n## 一、Budget Curve（tail-256/512/1024/2048）\n\n### 已写入 ✅\n\n| 数据点 | 位置 | 状态 |\n|--------|------|------|\n| Qwen-7B: 78.9/93.6/96.5/97.3 | appendix.tex Table 6 (`tab:tail_cross_model`) | ✅ 完整 |\n| DeepSeek-6.7B: 76.4/93.9/96.5/95.0↓ | appendix.tex Table 6 | ✅ 完整 |\n| Qwen-1.5B: 72.6/95.6/96.6/97.9 | appendix.tex Table 6 | ✅ 完整 |\n| Phase transition 256→512: +14.7~+23pp | experiments.tex L152 + appendix.tex L419-421 | ✅ |\n| tail-512 convergence (93.6-95.6% band) | appendix.tex L422-423 | ✅ |\n| tail-1024 convergence (96.5-96.6%) | appendix.tex L422-423 | ✅ |\n| Non-monotonicity: DeepSeek only, -1.5pp at 1024→2048 | experiments.tex L147, appendix.tex L428-429 | ✅ 正确描述为 architecture-specific |\n| Scale behavior inversion (signal-poor vs signal-rich) | appendix.tex L425-426 | ✅ |\n| Budget curve figure (`budget_curve`) | appendix.tex Fig 5 (`fig:trace_length`) | ✅ (仅 Qwen-7B) |\n\n### 缺失 ❌\n\n| 数据点 | 状态 | 说明 |\n|--------|------|------|\n| **CodeLlama-13B tail-512 = 97.5%** | ❌ 未写入 | 数据已有，表格和正文均无 |\n| **CodeLlama-13B tail-256** | ⏳ 实验运行中 | 等待结果 |\n| **CodeLlama-13B tail-1024** | ⏳ 实验运行中 | 等待结果 |\n| **CodeLlama-13B tail-2048** | ❓ 未确认 | 未见相关数据 |\n| 4-model budget curve figure 更新 | ❌ | 当前 figure 仅含 Qwen-7B 单模型 |\n\n### 正文描述需更新的地方\n\n- `experiments.tex` L152: \"all three models jump\" → 需改为 4 模型（待 CL-13B 数据齐全）\n- `appendix.tex` L382-383: \"three models spanning two architecture families\" → 需扩展为 four models, three families\n- `appendix.tex` Table 6 caption: 需加入 CodeLlama-13B 行\n- `appendix.tex` L419: \"all three models\" → \"all four models\"（待数据齐全）\n\n---\n\n## 二、Head-Tail Gap（跨模型对比）\n\n### 已写入 ✅\n\n| 数据点 | 位置 | 状态 |\n|--------|------|------|\n| Qwen-7B: head-2048=81.8%, tail-2048=97.3%, gap=+15.5pp | appendix.tex Table 7 (`tab:head_vs_tail`) | ✅ |\n| DeepSeek-6.7B: head-2048=78.7%, tail-2048=95.0%, gap=+16.3pp | appendix.tex Table 7 | ✅ |\n| Qwen-1.5B: head-2048=75.3%, tail-2048=97.9%, gap=+22.6pp | appendix.tex Table 7 | ✅ |\n| 15.5-22.6pp gap range | experiments.tex L150 | ✅ |\n| 小模型 gap 更大 (Qwen-1.5B +22.6pp vs Qwen-7B +15.5pp) | experiments.tex L150-151 + appendix.tex L431-432 | ✅ |\n\n### 缺失 ❌\n\n| 数据点 | 状态 | 说明 |\n|--------|------|------|\n| **CodeLlama-13B head-2048 vs tail-2048** | ❌ | 无 head-2048 实验数据 |\n\n---\n\n## 三、Non-Monotonicity Correction\n\n### 已写入 ✅\n\n正文和附录均已正确表述：仅 DeepSeek 在 tail-1024→2048 下降 1.5pp，非 universal pattern。\n\n- experiments.tex L147: \"only DeepSeek showing a mild architecture-specific reversal\"\n- appendix.tex L357: \"only DeepSeek-6.7B shows a mild −1.5pp decrease\"\n- appendix.tex L428-429: 明确说 \"while the other two models increase monotonically\"\n\n**状态**: ✅ 无需修改\n\n---\n\n## 四、总结\n\n### 已完成的 patch\n1. ✅ 3-model budget curve 表格和分析（Qwen-7B, DeepSeek, Qwen-1.5B）\n2. ✅ Phase transition / convergence / scale inversion 叙事\n3. ✅ 3-model head-tail gap 表格和分析\n4. ✅ Non-monotonicity 正确描述\n5. ✅ Budget curve figure (单模型版)\n\n### 待完成的 patch（按优先级）\n1. **P1**: CodeLlama-13B tail-512=97.5% 写入 Table 6（数据已有，立即可做）\n2. **P2**: 等待 CL-13B tail-256 和 tail-1024 实验完成后补全表格\n3. **P3**: 更新正文 \"three models\" → \"four models\"（待 P2 完成）\n4. **P4**: 更新 budget curve figure 为 4-model 版本\n5. **P5**: CodeLlama-13B head-tail gap 数据（需要 head-2048 实验）\n\n### 需要更新的章节列表\n| 文件 | 章节/位置 | 更新内容 |\n|------|-----------|----------|\n| `experiments.tex` | §4.5 Additional Analyses, L149-156 | 加入 CL-13B 数据，更新 \"three models\" |\n| `appendix.tex` | §Trace Length Full, Table 6 | 加 CL-13B 行 |\n| `appendix.tex` | §Trace Length Full, Table 7 | 加 CL-13B 行（待 head-2048 数据）|\n| `appendix.tex` | L382-383, L419 | \"three models\" → \"four models\" |\n| `appendix.tex` | budget_curve figure | 更新为多模型版本 |\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 28_

注册 artifact。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "252792c9-195f-4e60-aac7-873268786715",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XwemhGGJkzKRefzmCvN8jd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2138,
      "cache_read_input_tokens": 52485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2138
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

_source line 29_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018Li9xhJRxH4hyb35gksZef`</summary>

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
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "57597886-2825-48e6-b239-ded6269c054a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XwemhGGJkzKRefzmCvN8jd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2138,
      "cache_read_input_tokens": 52485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2138
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

_source line 30 · 2026-05-18T01:48:43.051Z_

<details><summary>↩ Tool result · `toolu_018Li9xhJRxH4hyb35gksZef`</summary>

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
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "6770a483-30a6-4a36-817a-8ddf9ac0176b",
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

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
The `save_project_file` tool only allows writing to memory.md, writing_plan.yaml, paper_framing.md. The artifact is already written to the local filesystem. Let me check if there's a `register_artifact` tool available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "78cecdc9-4b57-46d7-9e8b-3dd30736d5a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FFJ8889swBdV9caGu2BHVh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 369,
      "cache_read_input_tokens": 54623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 369
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

_source line 32_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FkZ8g86DBWmbvewYieE4F2`</summary>

```json
{
  "query": "register_artifact",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "4cbcab4c-b135-458c-b87f-03f7fb71bb0f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FFJ8889swBdV9caGu2BHVh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 369,
      "cache_read_input_tokens": 54623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 369
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

_source line 33 · 2026-05-18T01:48:47.016Z_

<details><summary>↩ Tool result · `toolu_01FkZ8g86DBWmbvewYieE4F2`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "5328b559-a851-4e00-badb-0fdc8a56cf46",
  "tool_use_result": {
    "matches": [],
    "query": "register_artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01USNcQSY1qqGWmVDwhQ1Z7z`</summary>

```json
{
  "query": "artifact",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "e99e406b-b610-4d1e-bcbb-fb10a5f6ff8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U8zt9FZUM72UEirEcrrDXM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 164,
      "cache_read_input_tokens": 54992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 164
      },
      "output_tokens": 58,
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

_source line 35 · 2026-05-18T01:48:49.824Z_

<details><summary>↩ Tool result · `toolu_01USNcQSY1qqGWmVDwhQ1Z7z`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "4f9bd833-fb71-4abf-a1f2-51d4724362ca",
  "tool_use_result": {
    "matches": [],
    "query": "artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 36_

没有 `register_artifact` 工具可用。报告已写入本地路径。

---

## 审计结果摘要

**已写入论文的数据（完整）：**
- 3 模型 budget curve 完整数据（Qwen-7B / DeepSeek / Qwen-1.5B × tail-256/512/1024/2048）
- Phase transition、convergence、scale inversion 叙事
- 3 模型 head-tail gap 表格（15.5–22.6pp）
- Non-monotonicity 已正确修正为 "仅 DeepSeek, -1.5pp"

**缺失：**
1. **P1（立即可做）**: CodeLlama-13B tail-512=97.5% 未写入 Table 6
2. **P2（等实验）**: CL-13B tail-256 和 tail-1024 还在跑
3. **P3**: 正文多处 "three models" 需改为 "four models"（待 P2）
4. **P4**: Budget curve figure 需更新为 4-model 版本
5. **P5**: CL-13B head-2048 数据缺失，无法填 head-tail gap 表

报告已写到 `artifacts/paper_patch_audit/paper_patch_status.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "uuid": "b941bf29-7354-4ed2-81c0-3621acd6356d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F1ZCRb9JsM6T7c8XAaeD6Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 90,
      "cache_read_input_tokens": 55156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 90
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

_source line 37_

没有 `register_artifact` 工具可用。报告已写入本地路径。

---

## 审计结果摘要

**已写入论文的数据（完整）：**
- 3 模型 budget curve 完整数据（Qwen-7B / DeepSeek / Qwen-1.5B × tail-256/512/1024/2048）
- Phase transition、convergence、scale inversion 叙事
- 3 模型 head-tail gap 表格（15.5–22.6pp）
- Non-monotonicity 已正确修正为 "仅 DeepSeek, -1.5pp"

**缺失：**
1. **P1（立即可做）**: CodeLlama-13B tail-512=97.5% 未写入 Table 6
2. **P2（等实验）**: CL-13B tail-256 和 tail-1024 还在跑
3. **P3**: 正文多处 "three models" 需改为 "four models"（待 P2）
4. **P4**: Budget curve figure 需更新为 4-model 版本
5. **P5**: CL-13B head-2048 数据缺失，无法填 head-tail gap 表

报告已写到 `artifacts/paper_patch_audit/paper_patch_status.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 105087,
  "duration_api_ms": 105315,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "cb515d2f-a856-41a3-b617-3d288c4d2a31",
  "total_cost_usd": 0.60131075,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 43405,
    "cache_read_input_tokens": 419407,
    "output_tokens": 4742,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 43405,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 361,
        "cache_read_input_tokens": 55156,
        "cache_creation_input_tokens": 90,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 90
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1611,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001706,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 14,
      "outputTokens": 4742,
      "cacheReadInputTokens": 419407,
      "cacheCreationInputTokens": 43405,
      "webSearchRequests": 0,
      "costUSD": 0.59960475,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ec133ca9-64b8-4502-b908-28cf4228a4c1"
}
```

</details>

---
