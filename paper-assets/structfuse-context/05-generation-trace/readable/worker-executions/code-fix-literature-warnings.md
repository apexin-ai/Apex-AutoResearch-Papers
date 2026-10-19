# code fix literature warnings

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 105
- **Recorded user turns:** 1
- **Tool calls:** 36
- **Original source:** `logs/workers/worker_code_fix-literature-warnings_20260516T004234.log`
- **Structured JSON:** [`83571f67c645a59d3cb8.json`](../../sessions/83/83571f67c645a59d3cb8.json)

## Before a recorded user message

7 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
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
  "uuid": "04e2aa32-f949-4bb9-89de-71cb772da6c1",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/memory/"
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
    "resetsAt": 1778907000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "9a231f62-5995-41bd-899e-ab261ab45ac9",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by locating the relevant files and working on the warnings in the specified order. I'll parallelize the initial discovery work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "51129da3-a790-4954-a37e-4e38620d4a54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011G9trsyxCezVRrgkCWqMM2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11838,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11838
      },
      "output_tokens": 23,
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

先定位所有相关文件并搜索 GRACE 论文真实性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "bc6e78f8-06c2-4fab-a441-d3355818048b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011G9trsyxCezVRrgkCWqMM2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11838,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11838
      },
      "output_tokens": 23,
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

<details open><summary>🔧 Tool call — Agent · `toolu_01GhwiJiH4r6bvfttg5m316F`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find all relevant literature files",
  "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/, find:\n1. All .md files containing \"GRACE\" or \"grace\" (case insensitive)\n2. The file literature_map.yaml\n3. The file related_work_references.md\n4. The file related_work_supplement.md\n5. Any other files in artifacts/literature/ or artifacts/paper_drafts/\n\nUse Glob and Grep to locate these. Report exact file paths and brief content snippets around GRACE mentions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "ad4de823-3b7d-42c3-9826-b3a8d6f8a053",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011G9trsyxCezVRrgkCWqMM2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11838,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11838
      },
      "output_tokens": 23,
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

_source line 7_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a1772f50001039623",
  "tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "description": "Find all relevant literature files",
  "task_type": "local_agent",
  "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/, find:\n1. All .md files containing \"GRACE\" or \"grace\" (case insensitive)\n2. The file literature_map.yaml\n3. The file related_work_references.md\n4. The file related_work_supplement.md\n5. Any other files in artifacts/literature/ or artifacts/paper_drafts/\n\nUse Glob and Grep to locate these. Report exact file paths and brief content snippets around GRACE mentions.",
  "uuid": "1f8da134-a0c0-4146-aeaf-e2786eb18812",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8"
}
```

---

## Round 1

98 recorded events

### User

_source line 8 · 2026-05-16T00:42:49.846Z_

In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/, find:
1. All .md files containing "GRACE" or "grace" (case insensitive)
2. The file literature_map.yaml
3. The file related_work_references.md
4. The file related_work_supplement.md
5. Any other files in artifacts/literature/ or artifacts/paper_drafts/

Use Glob and Grep to locate these. Report exact file paths and brief content snippets around GRACE mentions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "6c726161-c821-4ddb-9554-e303644cc896"
}
```

</details>

---

### System

_source line 9_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1772f50001039623",
  "tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "description": "Finding **/*.md",
  "usage": {
    "total_tokens": 15530,
    "tool_uses": 1,
    "duration_ms": 4324
  },
  "last_tool_name": "Glob",
  "uuid": "053db683-d675-4d40-9f53-b78332cd55df",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8"
}
```

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Glob · `toolu_01An2Bb6Sa4jy3LNWtpU3oYH`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "9350459b-f84d-4a7c-b281-d57bcc5133e2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C2TSDsAMNQSzY8yta9NDH3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15521,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15521,
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

_source line 11 · 2026-05-16T00:42:54.239Z_

<details><summary>↩ Tool result · `toolu_01An2Bb6Sa4jy3LNWtpU3oYH`</summary>

```text
artifacts/mvp_p1_codeql_feasibility/report/mvp_phase1_report.md
artifacts/mvp_p2b_contrastive_training/report/failure_diagnosis.md
task_context/history/director/loop_1.md
task_context/history/agent/loop_1.md
task_context/history/agent/loop_1_1778635668.md
task_context/history/reviewer/loop_2.md
artifacts/_project/report/50repo_overlap_report.md
docs/IDEA_BRIEF.md
artifacts/dream_reports/dream_20260512T204322/best/review_report.md
artifacts/dream_reports/dream_20260512T204322/median/review_report.md
artifacts/dream_reports/dream_20260512T204322/worst/review_report.md
docs/handoff_20260513.md
task_context/history/reviewer/loop_3.md
task_context/history/agent/loop_2.md
task_context/history/agent/loop_2_1778708899.md
artifacts/disk_cleanup_report_20260513.md
artifacts/_project/report/scalability_summary.md
artifacts/plan_006/scalability_summary.md
artifacts/m1_progress_0513.md
artifacts/bjb1_status_check.md
artifacts/_project/report/pilot_results_summary.md
artifacts/_project/report/pilot_results_summary_64aa24.md
task_context/history/reviewer/loop_1.md
.claude/sessions/agent_cb55d4ab/CLAUDE.md
.claude/sessions/agent_cb55d4ab/AGENTS.md
task_context/history/director/loop_2.md
task_context/history/reviewer/loop_4.md
task_context/history/agent/loop_3.md
artifacts/rename_safety_report.md
artifacts/plan003_swebench_eval_plan.md
task_context/history/director/loop_3.md
task_context/history/reviewer/loop_5.md
artifacts/plan003_eval_readiness.md
task_context/history/director/loop_4.md
task_context/history/reviewer/loop_6.md
task_context/history/agent/loop_4.md
artifacts/training_status_snapshot.md
artifacts/swebench_eval_readiness.md
artifacts/dream_reports/dream_20260514T075732/best/paper_framing.md
artifacts/dream_reports/dream_20260514T075732/median/paper_framing.md
artifacts/dream_reports/dream_20260514T075732/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T075732/best/review_report.md
artifacts/dream_reports/dream_20260514T075732/median/review_report.md
artifacts/dream_reports/dream_20260514T075732/worst/review_report.md
artifacts/analysis/plan017_literature_comparison.md
artifacts/m2_full_qwen_analysis.md
artifacts/m2_full_qwen/report/m2_full_qwen_analysis.md
task_context/history/agent/loop_5.md
task_context/history/agent/loop_5_1778781850.md
task_context/history/reviewer/loop_7.md
artifacts/m2_qwen_status_check.md
artifacts/m2_full_starcoder/report/m2_starcoder_status_check.md
artifacts/m2_starcoder_status_check.md
artifacts/status_check_loop6.md
task_context/history/director/loop_5.md
artifacts/_project/report/plan_015_dynamic_mining_design.md
artifacts/dream_reports/dream_20260514T162530/best/paper_framing.md
artifacts/dream_reports/dream_20260514T162530/median/paper_framing.md
artifacts/dream_reports/dream_20260514T162530/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T162530/best/review_report.md
artifacts/dream_reports/dream_20260514T162530/median/review_report.md
artifacts/dream_reports/dream_20260514T162530/worst/review_report.md
artifacts/_project/paper/experimental_setup_k_checkpoint.md
task_context/history/agent/loop_6.md
artifacts/status_check_20260514.md
artifacts/paper_drafts/experimental_setup_k_checkpoint.md
artifacts/plan003_swebench_dryrun_report.md
task_context/history/reviewer/loop_8.md
task_context/history/director/loop_6.md
artifacts/plan005_stratified_analysis_report.md
artifacts/plan_005_stratified/report/v1_v2_changelog.md
artifacts/v1_v2_changelog.md
task_context/history/agent/loop_6_1778793131.md
artifacts/m1_reextract_v2_status.md
task_context/history/agent/loop_7.md
task_context/history/agent/loop_6_1778807209.md
artifacts/_project/report/related_work_expansion_report.md
artifacts/literature/related_work_expansion_report.md
artifacts/plan_003/report/swebench_dryrun_report.md
artifacts/plan_003/swebench_dryrun_report.md
artifacts/_project/paper/related_work_v1_dc54a3.md
artifacts/_project/paper/introduction_v1.md
artifacts/_project/paper/figure_design_v1.md
artifacts/paper_drafts/figure_design_v1.md
artifacts/_project/paper/experiments_v1_054f8d.md
artifacts/_project/paper/method_v1_3cf111.md
artifacts/_project/paper/method_v1_ce3556.md
artifacts/_project/paper/experiments_v1_eccca0.md
artifacts/_project/paper/experiments_v1_bcd130.md
artifacts/_project/paper/experiments_v1_d4b180.md
task_context/history/director/loop_7.md
task_context/history/agent/loop_8.md
task_context/history/agent/loop_7_1778818340.md
artifacts/_project/paper/method_v1_ae4280.md
artifacts/paper_drafts/claim2_wording_review.md
artifacts/paper_drafts/bm25_code_review.md
artifacts/_project/paper/discussion_v2.md
artifacts/_project/paper/related_work_v1.md
artifacts/_project/paper/method_v1.md
artifacts/_project/paper/introduction_v2.md
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "47b62bda-d1a9-4110-a514-f157a60b6bdb"
}
```

</details>

---

### System

_source line 12_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1772f50001039623",
  "tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "description": "Finding **/literature_map.yaml",
  "usage": {
    "total_tokens": 15533,
    "tool_uses": 2,
    "duration_ms": 4532
  },
  "last_tool_name": "Glob",
  "uuid": "f709d12e-07d8-4681-bd26-11cca1fba809",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8"
}
```

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Glob · `toolu_01YUdtY6mvdf3rU4jS5oDX6V`</summary>

```json
{
  "pattern": "**/literature_map.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "8b6e9800-0707-4491-9e93-cfd2e0885044",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C2TSDsAMNQSzY8yta9NDH3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15521,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15521,
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

_source line 14 · 2026-05-16T00:42:54.402Z_

<details><summary>↩ Tool result · `toolu_01YUdtY6mvdf3rU4jS5oDX6V`</summary>

```text
literature_map.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "9ef09dfb-7565-4751-8b05-909e7cf82ac4"
}
```

</details>

---

### System

_source line 15_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1772f50001039623",
  "tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "description": "Finding **/related_work*.md",
  "usage": {
    "total_tokens": 15536,
    "tool_uses": 3,
    "duration_ms": 4979
  },
  "last_tool_name": "Glob",
  "uuid": "5388e89e-322f-40ab-ad2c-6eb5ffaa140a",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8"
}
```

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Glob · `toolu_01AdGSwxC9zJhCMBYWM3nZpU`</summary>

```json
{
  "pattern": "**/related_work*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "711948ac-3cba-45bf-989d-05fdff2046a1",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C2TSDsAMNQSzY8yta9NDH3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15521,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15521,
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

_source line 17 · 2026-05-16T00:42:54.859Z_

<details><summary>↩ Tool result · `toolu_01AdGSwxC9zJhCMBYWM3nZpU`</summary>

```text
artifacts/_project/report/related_work_expansion_report.md
artifacts/literature/related_work_expansion_report.md
artifacts/_project/paper/related_work_v1_dc54a3.md
artifacts/_project/paper/related_work_v1.md
artifacts/paper_drafts/related_work_supplement.md
artifacts/_project/paper/related_work_v1_5cf1f6.md
artifacts/paper_drafts/related_work_v1.md
artifacts/_project/report/related_work_references.md
artifacts/literature/related_work_references.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "4ee262de-f7c9-4ede-9749-e531e3544a54"
}
```

</details>

---

### System

_source line 18_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1772f50001039623",
  "tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "description": "Finding artifacts/literature/**",
  "usage": {
    "total_tokens": 15539,
    "tool_uses": 4,
    "duration_ms": 5261
  },
  "last_tool_name": "Glob",
  "uuid": "26640b25-c9af-43f8-b8ab-2a60bca21694",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8"
}
```

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Glob · `toolu_01BU4399B9DZHxGKHhjBKwdR`</summary>

```json
{
  "pattern": "artifacts/literature/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "b6bbd37d-d0cf-4e4a-880f-1f0d6331cdc2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C2TSDsAMNQSzY8yta9NDH3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15521,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15521,
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

_source line 20 · 2026-05-16T00:42:55.152Z_

<details><summary>↩ Tool result · `toolu_01BU4399B9DZHxGKHhjBKwdR`</summary>

```text
artifacts/literature/related_work_expansion_report.md
artifacts/literature/related_work_references.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "dad31b23-2269-4a49-9ab6-cf1a8839bab5"
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
  "task_id": "a1772f50001039623",
  "tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "description": "Finding artifacts/paper_drafts/**",
  "usage": {
    "total_tokens": 15542,
    "tool_uses": 5,
    "duration_ms": 5370
  },
  "last_tool_name": "Glob",
  "uuid": "d5fa2af7-ff31-4349-8cd1-9405e276786b",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8"
}
```

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Glob · `toolu_01QKkQi7NDxAK4fMjkYX5iNM`</summary>

```json
{
  "pattern": "artifacts/paper_drafts/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "9cde3715-e342-4596-a4a3-6d9c38c4c571",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C2TSDsAMNQSzY8yta9NDH3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15521,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15521,
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

_source line 23 · 2026-05-16T00:42:55.256Z_

<details><summary>↩ Tool result · `toolu_01QKkQi7NDxAK4fMjkYX5iNM`</summary>

```text
artifacts/paper_drafts/experimental_setup_k_checkpoint.md
artifacts/paper_drafts/figure_design_v1.md
artifacts/paper_drafts/claim2_wording_review.md
artifacts/paper_drafts/bm25_code_review.md
artifacts/paper_drafts/introduction_v2.md
artifacts/paper_drafts/experiment_setup_v1.md
artifacts/paper_drafts/related_work_supplement.md
artifacts/paper_drafts/checkpoint_criterion_table.tex
artifacts/paper_drafts/fixed_checkpoint_table.tex
artifacts/paper_drafts/discussion_valloss_divergence.md
artifacts/paper_drafts/introduction_v1.md
artifacts/paper_drafts/abstract_v1.md
artifacts/paper_drafts/related_work_v1.md
artifacts/paper_drafts/references.bib
artifacts/paper_drafts/method_v1.md
artifacts/paper_drafts/conclusion_v1.md
artifacts/paper_drafts/abstract_v2.md
artifacts/paper_drafts/experiments_v1.md
artifacts/paper_drafts/discussion_v2.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "0d2d983b-d745-4617-ae85-e72c6703f039"
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
  "task_id": "a1772f50001039623",
  "tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "description": "Searching for grace",
  "usage": {
    "total_tokens": 19119,
    "tool_uses": 6,
    "duration_ms": 7937
  },
  "last_tool_name": "Grep",
  "uuid": "9919266c-62aa-4c3e-a652-b655945956b5",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8"
}
```

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Grep · `toolu_01ETqJ1Fr5L7PPoN6emTBgZq`</summary>

```json
{
  "pattern": "grace",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "type": "md",
  "output_mode": "files_with_matches",
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "e7193160-7062-4b02-99d0-5d0af5db1f31",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019aK1raap3AaF2SSuqkCWej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3571,
      "cache_read_input_tokens": 15521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3571,
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

_source line 26 · 2026-05-16T00:42:57.808Z_

<details><summary>↩ Tool result · `toolu_01ETqJ1Fr5L7PPoN6emTBgZq`</summary>

```text
Found 3 files
artifacts/paper_drafts/related_work_v1.md
artifacts/dream_reports/dream_20260514T162530/best/review_report.md
docs/IDEA_BRIEF.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "ce520a6a-dd55-4f2e-ac01-b97247b9fa1e"
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
  "task_id": "a1772f50001039623",
  "tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "description": "Reading literature_map.yaml",
  "usage": {
    "total_tokens": 19120,
    "tool_uses": 7,
    "duration_ms": 8148
  },
  "last_tool_name": "Read",
  "uuid": "91ff49dc-dabf-4e9f-8f8e-36b7a0b3efeb",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8"
}
```

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_01Yc4GMWKXifsQcDbsQ1xSqB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "cc51ce87-e8df-404b-9137-c0b056efa2a3",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019aK1raap3AaF2SSuqkCWej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3571,
      "cache_read_input_tokens": 15521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3571,
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

_source line 29 · 2026-05-16T00:42:58.004Z_

<details><summary>↩ Tool result · `toolu_01Yc4GMWKXifsQcDbsQ1xSqB`</summary>

```text
1	# StructFuse — Related Work Literature Map
2	# 最后更新: 2026-05-14
3	# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。
4	# 总计: 39 entries (含 2 个软件工具引用)
5	
6	categories:
7	
8	  # ==========================================================================
9	  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem
10	  # ==========================================================================
11	  code_retrieval_bug_fixing:
12	    description: "SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法"
13	    papers:
14	
15	      - title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
16	        authors: "Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan"
17	        venue: ICLR
18	        year: 2024
19	        relation: baseline
20	        summary: "从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。"
21	
22	      - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
23	        authors: "John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press"
24	        venue: NeurIPS
25	        year: 2024
26	        relation: competitor
27	        summary: "基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。"
28	
29	      - title: "AutoCodeRover: Autonomous Program Improvement"
30	        authors: "Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury"
31	        venue: ISSTA
32	        year: 2024
33	        relation: competitor
34	        summary: "结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。"
35	
36	      - title: "Agentless: Demystifying LLM-based Software Engineering Agents"
37	        authors: "Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang"
38	        venue: arXiv
39	        year: 2024
40	        relation: competitor
41	        summary: "无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。"
42	
43	      - title: "SWE-smith: Scaling Data for Software Engineering Agents"
44	        authors: "John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang"
45	        venue: "NeurIPS (Datasets & Benchmarks, Spotlight)"
46	        year: 2025
47	        relation: building-block
48	        summary: "自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。"
49	
50	      - title: "RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems"
51	        authors: "Tianyang Liu, Canwen Xu, Julian McAuley"
52	        venue: ICLR
53	        year: 2024
54	        relation: baseline
55	        summary: "Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。"
56	
57	      - title: "SweRank: Software Issue Localization with Code Ranking"
58	        authors: "Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty"
59	        venue: arXiv
60	        year: 2025
61	        relation: competitor
62	        summary: "Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。"
63	
64	      - title: "SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution"
65	        authors: "Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen"
66	        venue: "ACL (Findings)"
67	        year: 2025
68	        relation: competitor
69	        summary: "BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。"
70	
71	  # ==========================================================================
72	  # Category 2: Hard Negative Mining in Contrastive Learning
73	  # ==========================================================================
74	  hard_negative_mining:
75	    description: "对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择"
76	    papers:
77	
78	      - title: "Dense Passage Retrieval for Open-Domain Question Answering"
79	        authors: "Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih"
80	        venue: EMNLP
81	        year: 2020
82	        relation: background
83	        summary: "DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。"
84	
85	      - title: "Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval"
86	        authors: "Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk"
87	        venue: ICLR
88	        year: 2021
89	        relation: background
90	        summary: "ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。"
91	
92	      - title: "A Simple Framework for Contrastive Learning of Visual Representations"
93	        authors: "Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton"
94	        venue: ICML
95	        year: 2020
96	        relation: background
97	        summary: "SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。"
98	
99	      - title: "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks"
100	        authors: "Nils Reimers, Iryna Gurevych"
101	        venue: EMNLP
102	        year: 2019
103	        relation: background
104	        summary: "Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。"
105	
106	      - title: "Curriculum Learning for Dense Retrieval Distillation"
107	        authors: "Hansi Zeng, Hamed Zamani, Vishwa Vinay"
108	        venue: "SIGIR (Best Short Paper)"
109	        year: 2022
110	        relation: background
111	        summary: "CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。"
112	
113	      - title: "Effective Hard Negative Mining for Contrastive Learning-Based Code Search"
114	        authors: "Fan Y., Li C., Ge J., Huang L., Luo B."
115	        venue: "ACM TOSEM"
116	        year: 2025
117	        relation: contrast-target
118	        summary: "CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。"
119	        note: "关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。"
120	
121	  # ==========================================================================
122	  # Category 3: Contrastive Learning for Code
123	  # ==========================================================================
124	  contrastive_code_learning:
125	    description: "代码领域的对比学习方法，训练时利用代码特性构建正负样本"
126	    papers:
127	
128	      - title: "Contrastive Code Representation Learning"
129	        authors: "Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica"
130	        venue: EMNLP
131	        year: 2021
132	        relation: background
133	        summary: "ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。"
134	
135	      - title: "CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search"
136	        authors: "Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan"
137	        venue: EMNLP
138	        year: 2022
139	        relation: background
140	        summary: "结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。"
141	
142	      - title: "Towards Learning (Dis)-Similarity of Source Code from Program Contrasts"
143	        authors: "Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty"
144	        venue: "ACL (Long Papers)"
145	        year: 2022
146	        relation: background
147	        summary: "利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。"
148	
149	  # ==========================================================================
150	  # Category 4: Program Analysis for ML
151	  # ==========================================================================
152	  program_analysis_for_ml:
153	    description: "静态分析辅助 ML，结构信息在代码表示学习中的应用"
154	    papers:
155	
156	      - title: "CodeQL: Semantic Code Analysis Engine"
157	        authors: "GitHub / Semmle"
158	        venue: "Tool (open-source)"
159	        year: 2019
160	        relation: building-block
161	        summary: "基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。"
162	
163	      - title: "code2vec: Learning Distributed Representations of Code"
164	        authors: "Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav"
165	        venue: POPL
166	        year: 2019
167	        relation: background
168	        summary: "用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。"
169	
170	      - title: "code2seq: Generating Sequences from Structured Representations of Code"
171	        authors: "Uri Alon, Shaked Brody, Omer Levy, Eran Yahav"
172	        venue: ICLR
173	        year: 2019
174	        relation: background
175	        summary: "code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。"
176	
177	      - title: "Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree"
178	        authors: "Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin"
179	        venue: SANER
180	        year: 2020
181	        relation: background
182	        summary: "FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。"
183	
184	      - title: "GraphCodeBERT: Pre-training Code Representations with Data Flow"
185	        authors: "Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou"
186	        venue: ICLR
187	        year: 2021
188	        relation: background
189	        summary: "在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。"
190	
191	      - title: "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair"
192	        authors: "Shahd Seddik, Fatemeh Fard"
193	        venue: arXiv
194	        year: 2026
195	        relation: contrast
196	        summary: "用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。"
197	
198	  # ==========================================================================
199	  # Category 5: Code Embeddings / Code Search
200	  # ==========================================================================
201	  code_embeddings_search:
202	    description: "代码嵌入模型和代码搜索方法"
203	    papers:
204	
205	      - title: "CodeSearchNet Challenge: Evaluating the State of Semantic Code Search"
206	        authors: "Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt"
207	        venue: arXiv
208	        year: 2019
209	        relation: background
210	        summary: "代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。"
211	
212	      - title: "CodeBERT: A Pre-Trained Model for Programming and Natural Languages"
213	        authors: "Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou"
214	        venue: "EMNLP (Findings)"
215	        year: 2020
216	        relation: background
217	        summary: "首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。"
218	
219	      - title: "UniXcoder: Unified Cross-Modal Pre-training for Code Representation"
220	        authors: "Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin"
221	        venue: ACL
222	        year: 2022
223	        relation: background
224	        summary: "统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。"
225	
226	      - title: "StarCoder: May the Source Be with You!"
227	        authors: "Raymond Li, Loubna Ben Allal, et al. (BigCode)"
228	        venue: TMLR
229	        year: 2023
230	        relation: building-block
231	        summary: "大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。"
232	
233	      - title: "Code Llama: Open Foundation Models for Code"
234	        authors: "Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)"
235	        venue: arXiv
236	        year: 2023
237	        relation: background
238	        summary: "Meta 的代码大模型系列，基于 Llama 2 微调。"
239	
240	      - title: "Qwen2.5-Coder Technical Report"
241	        authors: "Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)"
242	        venue: arXiv
243	        year: 2024
244	        relation: building-block
245	        summary: "Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。"
246	
247	      - title: "DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence"
248	        authors: "Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang"
249	        venue: arXiv
250	        year: 2024
251	        relation: background
252	        summary: "开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。"
253	
254	      - title: "RepoFusion: Training Code Models to Understand Your Repository"
255	        authors: "Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak"
256	        venue: arXiv
257	        year: 2023
258	        relation: background
259	        summary: "训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。"
260	
261	      - title: "BM25"
262	        authors: "Stephen Robertson, Hugo Zaragoza"
263	        venue: "Foundations and Trends in Information Retrieval"
264	        year: 2009
265	        relation: baseline
266	        summary: "经典稀疏检索方法，StructFuse 的 baseline 之一。"
267	
268	  # ==========================================================================
269	  # Category 6: Graph-Guided Code Navigation (Inference-Time)
270	  # ==========================================================================
271	  graph_guided_inference:
272	    description: "推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）"
273	    papers:
274	
275	      - title: "LocAgent: Graph-Guided LLM Agents for Code Localization"
276	        authors: "Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang"
277	        venue: ACL
278	        year: 2025
279	        relation: contrast
280	        summary: "将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。"
281	
282	      - title: "CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases"
283	        authors: "Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou"
284	        venue: NAACL
285	        year: 2025
286	        relation: contrast
287	        summary: "将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。"
288	
289	      - title: "RANGER: Repository-Level Agent for Graph-Enhanced Retrieval"
290	        authors: "Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta"
291	        venue: arXiv
292	        year: 2025
293	        relation: contrast
294	        summary: "构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。"
295	
296	      - title: "RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph"
297	        authors: "Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu"
298	        venue: ICLR
299	        year: 2025
300	        relation: contrast
301	        summary: "以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。"
302	
303	      - title: "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph"
304	        authors: "Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang"
305	        venue: ASE
306	        year: 2024
307	        relation: contrast
308	        summary: "构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。"
309	
310	  # ==========================================================================
311	  # Category 7: Infrastructure / Tools
312	  # ==========================================================================
313	  infrastructure:
314	    description: "StructFuse 依赖的核心基础设施和工具"
315	    papers:
316	
317	      - title: "Billion-Scale Similarity Search with GPUs"
318	        authors: "Jeff Johnson, Matthijs Douze, Herve Jegou"
319	        venue: "IEEE Transactions on Big Data"
320	        year: 2021
321	        relation: building-block
322	        summary: "FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。"
323	
324	      - title: "Tree-sitter: An Incremental Parsing System for Programming Tools"
325	        authors: "Max Brunsfeld et al."
326	        venue: "Software (Zenodo DOI: 10.5281/zenodo.13375512)"
327	        year: 2018
328	        relation: building-block
329	        summary: "增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。"
330	        note: "软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。"
331	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "a6b0ed41-cc64-40f9-9089-d54eb0f0cc56"
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
  "task_id": "a1772f50001039623",
  "tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "description": "Reading artifacts/literature/related_work_references.md",
  "usage": {
    "total_tokens": 19121,
    "tool_uses": 8,
    "duration_ms": 8614
  },
  "last_tool_name": "Read",
  "uuid": "b20651df-7862-445f-847b-91b4b625c397",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8"
}
```

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01BYkW3fNJBxguYvhDyGUXS1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/literature/related_work_references.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "38ff137c-e4b6-49c4-af19-e49689a87c58",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019aK1raap3AaF2SSuqkCWej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3571,
      "cache_read_input_tokens": 15521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3571,
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

_source line 32 · 2026-05-16T00:42:58.473Z_

<details><summary>↩ Tool result · `toolu_01BYkW3fNJBxguYvhDyGUXS1`</summary>

````text
1	# StructFuse Related Work Literature Collection
2	
3	> Collected: 2026-05-16 | Total: 21 papers across 3 directions
4	
5	---
6	
7	## Direction 1: Code Retrieval 中的 Negative Mining 策略
8	
9	### 1.1 CoCoHaNeRe (direct-competitor)
10	
11	Code search framework with differentiable hard negative retrieval from a searchable memory bank. Average MRR exceeds CodeBERT/GraphCodeBERT/UniXcoder by 11.25%/8.13%/7.38%. **与 StructFuse 最直接的竞品——同样关注 code search 中 hard negative 的挖掘策略。**
12	
13	```bibtex
14	@article{fan2025cocohanere,
15	  title={Effective Hard Negative Mining for Contrastive Learning-Based Code Search},
16	  author={Fan, Ye and Li, Chao and Ge, Jing and Huang, Liang and Luo, Bin},
17	  journal={ACM Transactions on Software Engineering and Methodology},
18	  volume={34},
19	  number={3},
20	  pages={1--35},
21	  year={2025},
22	  doi={10.1145/3695994}
23	}
24	```
25	
26	### 1.2 CodeSearchNet (evaluation)
27	
28	Code search benchmark with 6M functions across 6 languages and expert relevance annotations. **StructFuse 使用的评估数据集的来源基准。**
29	
30	```bibtex
31	@article{husain2019codesearchnet,
32	  title={CodeSearchNet Challenge: Evaluating the State of Semantic Code Search},
33	  author={Husain, Hamel and Wu, Ho-Hsiang and Gazit, Tiferet and Allamanis, Miltiadis and Brockschmidt, Marc},
34	  journal={arXiv preprint arXiv:1909.09436},
35	  year={2019}
36	}
37	```
38	
39	### 1.3 CodeBERT (background)
40	
41	First bimodal pre-trained model for programming language and natural language, trained with replaced token detection. **Code retrieval 领域的基线模型。**
42	
43	```bibtex
44	@inproceedings{feng2020codebert,
45	  title={CodeBERT: A Pre-Trained Model for Programming and Natural Languages},
46	  author={Feng, Zhangyin and Guo, Daya and Tang, Duyu and Duan, Nan and Feng, Xiaocheng and Gong, Ming and Shou, Linjun and Qin, Bing and Liu, Ting and Jiang, Daxin and Zhou, Ming},
47	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020},
48	  pages={1536--1547},
49	  year={2020}
50	}
51	```
52	
53	### 1.4 GraphCodeBERT (method-component)
54	
55	First pre-trained model incorporating code structure (data flow) for code representations. Uses semantic-level structure rather than AST. **展示了结构化代码表示对检索的提升，StructFuse 的 structure-aware embedding 思路的先驱。**
56	
57	```bibtex
58	@inproceedings{guo2021graphcodebert,
59	  title={GraphCodeBERT: Pre-training Code Representations with Data Flow},
60	  author={Guo, Daya and Ren, Shuo and Lu, Shuai and Feng, Zhangyin and Tang, Duyu and Liu, Shujie and Zhou, Long and Duan, Nan and Svyatkovskiy, Alexey and Fu, Shengyu and Tufano, Michele and Deng, Shao Kun and Clement, Colin and Drain, Dawn and Sundaresan, Neel and Yin, Jian and Jiang, Daxin and Zhou, Ming},
61	  booktitle={International Conference on Learning Representations},
62	  year={2021}
63	}
64	```
65	
66	### 1.5 UniXcoder (background)
67	
68	Unified cross-modal pre-training leveraging AST and code comments via contrastive learning. **StructFuse 的 backbone encoder 之一，也展示了 AST 结构对代码表示的增益。**
69	
70	```bibtex
71	@inproceedings{guo2022unixcoder,
72	  title={UniXcoder: Unified Cross-Modal Pre-training for Code Representation},
73	  author={Guo, Daya and Lu, Shuai and Duan, Nan and Wang, Yanlin and Zhou, Ming and Yin, Jian},
74	  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
75	  pages={7212--7225},
76	  year={2022}
77	}
78	```
79	
80	### 1.6 CodeRetriever (direct-competitor)
81	
82	Large-scale contrastive pre-training with both unimodal (code-code) and bimodal (code-text) learning for code search. **与 StructFuse 类似的 contrastive learning 框架，但没有显式的 hard negative 策略。**
83	
84	```bibtex
85	@inproceedings{li2022coderetriever,
86	  title={CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search},
87	  author={Li, Xiaonan and Gong, Yeyun and Shen, Yelong and Qiu, Xipeng and Zhang, Hang and Yao, Bolun and Qi, Weizhen and Jiang, Daxin and Chen, Weizhu and Duan, Nan},
88	  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},
89	  pages={2898--2910},
90	  year={2022}
91	}
92	```
93	
94	### 1.7 CoCoSoDa (direct-competitor)
95	
96	Contrastive code search with soft data augmentation and momentum-based negative enrichment. Exceeds CodeBERT/GraphCodeBERT/UniXcoder by 13.3%/10.5%/5.9% MRR. **在 negative sample enrichment 方面与 StructFuse 互补——CoCoSoDa 用 momentum queue 增加 negative 数量，StructFuse 关注 negative difficulty。**
97	
98	```bibtex
99	@inproceedings{shi2023cocosoda,
100	  title={CoCoSoDa: Effective Contrastive Learning for Code Search},
101	  author={Shi, Ensheng and Wang, Yanlin and Gu, Wenchao and Du, Lun and Zhang, Hongyu and Han, Shi and Zhang, Dongmei and Sun, Hongbin},
102	  booktitle={2023 IEEE/ACM 45th International Conference on Software Engineering (ICSE)},
103	  pages={2198--2210},
104	  year={2023}
105	}
106	```
107	
108	---
109	
110	## Direction 2: Contrastive Learning 中 Hard Negative 的 Overfitting 问题
111	
112	### 2.1 CPC / InfoNCE (background)
113	
114	Introduces InfoNCE loss: contrastive predictive coding for unsupervised representation learning. **Contrastive learning 的基础损失函数，StructFuse 训练目标的理论根基。**
115	
116	```bibtex
117	@article{oord2018representation,
118	  title={Representation Learning with Contrastive Predictive Coding},
119	  author={van den Oord, Aaron and Li, Yazhe and Vinyals, Oriol},
120	  journal={arXiv preprint arXiv:1807.03748},
121	  year={2018}
122	}
123	```
124	
125	### 2.2 HCL (method-component)
126	
127	Develops controllable hard negative sampling for contrastive learning, showing harder negatives accelerate and improve learning. **理论上证明了 hard negative 的价值，但也暗示了过度 hard 会导致问题——StructFuse difficulty analysis 的理论起点。**
128	
129	```bibtex
130	@inproceedings{robinson2021contrastive,
131	  title={Contrastive Learning with Hard Negative Samples},
132	  author={Robinson, Joshua David and Chuang, Ching-Yao and Sra, Suvrit and Jegelka, Stefanie},
133	  booktitle={International Conference on Learning Representations},
134	  year={2021}
135	}
136	```
137	
138	### 2.3 DCL (method-component)
139	
140	Debiased contrastive objective correcting for false negatives (same-class samples treated as negatives). **False negative 是 hard negative 过拟合的重要来源之一，DCL 提供了理论框架。**
141	
142	```bibtex
143	@inproceedings{chuang2020debiased,
144	  title={Debiased Contrastive Learning},
145	  author={Chuang, Ching-Yao and Robinson, Joshua and Lin, Yen-Chen and Torralba, Antonio and Jegelka, Stefanie},
146	  booktitle={Advances in Neural Information Processing Systems},
147	  volume={33},
148	  pages={8765--8775},
149	  year={2020}
150	}
151	```
152	
153	### 2.4 MoCHi (method-component)
154	
155	Hard negative mixing at feature level with minimal overhead; shows harder negatives facilitate faster learning. **Feature-level hard negative 合成方法，与 StructFuse 的 structure-based negative mining 形成对比。**
156	
157	```bibtex
158	@inproceedings{kalantidis2020hard,
159	  title={Hard Negative Mixing for Contrastive Learning},
160	  author={Kalantidis, Yannis and Sariyildiz, Mert Bulent and Pion, No{\'e} and Weinzaepfel, Philippe and Larlus, Diane},
161	  booktitle={Advances in Neural Information Processing Systems},
162	  volume={33},
163	  pages={21798--21809},
164	  year={2020}
165	}
166	```
167	
168	### 2.5 Understanding Hard Negatives in NCE (background)
169	
170	Theoretical analysis: using model distribution as negative distribution reduces gradient bias. **为 hard negative 的作用提供了理论解释——StructFuse 的 difficulty-overfitting 分析可引用此理论框架。**
171	
172	```bibtex
173	@inproceedings{zhang2021understanding,
174	  title={Understanding Hard Negatives in Noise Contrastive Estimation},
175	  author={Zhang, Wenzheng and Stratos, Karl},
176	  booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
177	  pages={1090--1101},
178	  year={2021}
179	}
180	```
181	
182	### 2.6 ProGCL (method-component)
183	
184	Shows hard negatives in graph CL are often false negatives; proposes probability-based hardness that accounts for true/false negative distinction. **揭示了 hard negative = false negative 的陷阱，与 StructFuse 发现的 difficulty-overfitting 现象呼应。**
185	
186	```bibtex
187	@inproceedings{xia2022progcl,
188	  title={ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning},
189	  author={Xia, Jun and Wu, Lirong and Wang, Ge and Chen, Jintao and Li, Stan Z.},
190	  booktitle={Proceedings of the 39th International Conference on Machine Learning},
191	  pages={24332--24346},
192	  year={2022}
193	}
194	```
195	
196	### 2.7 WCL (method-component)
197	
198	Difficulty-based sampling exploiting a bias-amplifying encoder to find informative hard negatives while avoiding false negatives. **用 difficulty 分层采样来 debias，与 StructFuse 的 difficulty stratification 思路最接近。**
199	
200	```bibtex
201	@inproceedings{jang2023difficulty,
202	  title={Difficulty-Based Sampling for Debiased Contrastive Representation Learning},
203	  author={Jang, Taeuk and Wang, Xiaoqian},
204	  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
205	  pages={24039--24048},
206	  year={2023}
207	}
208	```
209	
210	---
211	
212	## Direction 3: Representation Geometry / Similarity Saturation
213	
214	### 3.1 SimCLR (background)
215	
216	Simple contrastive framework showing the importance of data augmentation, projection head, and batch size. **Contrastive learning 的经典方法论，StructFuse 实验设计的参考。**
217	
218	```bibtex
219	@inproceedings{chen2020simple,
220	  title={A Simple Framework for Contrastive Learning of Visual Representations},
221	  author={Chen, Ting and Kornblith, Simon and Norouzi, Mohammad and Hinton, Geoffrey},
222	  booktitle={Proceedings of the 37th International Conference on Machine Learning},
223	  pages={1597--1607},
224	  year={2020}
225	}
226	```
227	
228	### 3.2 Alignment & Uniformity (method-component)
229	
230	Identifies two key properties of contrastive loss: alignment of positive pairs and uniformity on hypersphere; proves contrastive loss optimizes both asymptotically. **StructFuse 分析 embedding space 质量的理论工具——可用 alignment/uniformity 指标量化 structure-aware embedding 的改进。**
231	
232	```bibtex
233	@inproceedings{wang2020understanding,
234	  title={Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere},
235	  author={Wang, Tongzhou and Isola, Phillip},
236	  booktitle={Proceedings of the 37th International Conference on Machine Learning},
237	  pages={9929--9939},
238	  year={2020}
239	}
240	```
241	
242	### 3.3 Representation Degeneration (background)
243	
244	Shows pre-trained LM embeddings degenerate into a narrow cone, limiting representation power; proposes regularization. **Embedding 退化的理论根源——StructFuse 观察到的 similarity saturation 可追溯到此现象。**
245	
246	```bibtex
247	@inproceedings{gao2019representation,
248	  title={Representation Degeneration Problem in Training Natural Language Generation Models},
249	  author={Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan},
250	  booktitle={International Conference on Learning Representations},
251	  year={2019}
252	}
253	```
254	
255	### 3.4 Anisotropy of Contextualized Representations (background)
256	
257	Discovers that BERT/ELMo/GPT-2 representations occupy a narrow cone (anisotropy) across all layers. **实证发现 pre-trained model 的各向异性问题，StructFuse 使用的 code encoder 继承了此问题。**
258	
259	```bibtex
260	@inproceedings{ethayarajh2019contextual,
261	  title={How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings},
262	  author={Ethayarajh, Kawin},
263	  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},
264	  pages={55--65},
265	  year={2019}
266	}
267	```
268	
269	### 3.5 BERT-flow (method-component)
270	
271	Shows BERT sentence embeddings are anisotropic; proposes normalizing flows to transform to isotropic Gaussian. **Anisotropy 矫正方法的代表，与 StructFuse 的 whitening/normalization 策略形成对比。**
272	
273	```bibtex
274	@inproceedings{li2020sentence,
275	  title={On the Sentence Embeddings from Pre-trained Language Models},
276	  author={Li, Bohan and Zhou, Hao and He, Junxian and Wang, Mingxuan and Yang, Yiming and Li, Lei},
277	  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},
278	  pages={9119--9130},
279	  year={2020}
280	}
281	```
282	
283	### 3.6 SimCSE (method-component)
284	
285	Contrastive learning regularizes anisotropic embedding space to be more uniform; uses dropout as minimal augmentation. Spectral analysis shows contrastive loss flattens singular spectrum. **直接证明 contrastive learning 改善 anisotropy——StructFuse 可引用其 uniformity 分析框架。**
286	
287	```bibtex
288	@inproceedings{gao2021simcse,
289	  title={SimCSE: Simple Contrastive Learning of Sentence Embeddings},
290	  author={Gao, Tianyu and Yao, Xingcheng and Chen, Danqi},
291	  booktitle={Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},
292	  pages={6894--6910},
293	  year={2021}
294	}
295	```
296	
297	### 3.7 Whitening for Sentence Representations (method-component)
298	
299	Whitening operation enhances isotropy and reduces dimensionality of sentence representations. **针对 anisotropy 的简洁解法，与 StructFuse 中 embedding post-processing 的讨论相关。**
300	
301	```bibtex
302	@article{su2021whitening,
303	  title={Whitening Sentence Representations for Better Semantics and Faster Retrieval},
304	  author={Su, Jianlin and Cao, Jiarun and Liu, Weijie and Ou, Yangyiwen},
305	  journal={arXiv preprint arXiv:2103.15316},
306	  year={2021}
307	}
308	```
309	
310	---
311	
312	## Summary
313	
314	| Direction | Papers | Key insight for StructFuse |
315	|-----------|--------|---------------------------|
316	| 1. Code retrieval negative mining | 7 | StructFuse fills the gap between structure-aware encoding (GraphCodeBERT) and hard negative mining (CoCoHaNeRe) by using structural similarity for difficulty-aware negative selection |
317	| 2. Hard negative overfitting | 7 | Existing work (HCL, DCL, ProGCL, WCL) shows hard negatives help but can cause overfitting/false-negative problems; StructFuse's difficulty stratification addresses this in code domain |
318	| 3. Representation geometry | 7 | Pre-trained code encoders inherit anisotropy (Ethayarajh, Gao 2019); contrastive learning improves uniformity (SimCSE, Wang & Isola) but similarity saturation in high-similarity regions remains; StructFuse's structure-aware negatives target this specific region |
319	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "cf3136db-61d4-4901-ad2c-97285c954394"
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
  "task_id": "a1772f50001039623",
  "tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "description": "Reading artifacts/paper_drafts/related_work_supplement.md",
  "usage": {
    "total_tokens": 19122,
    "tool_uses": 9,
    "duration_ms": 8814
  },
  "last_tool_name": "Read",
  "uuid": "84bad98a-7bab-477b-890d-e70e0388c4dc",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8"
}
```

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_013dNiKmg3x7DxvL3isNhHDE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_supplement.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "5135f103-066c-4a4d-8ef3-0eed39d51f36",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019aK1raap3AaF2SSuqkCWej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3571,
      "cache_read_input_tokens": 15521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3571,
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

_source line 35 · 2026-05-16T00:42:58.666Z_

<details><summary>↩ Tool result · `toolu_013dNiKmg3x7DxvL3isNhHDE`</summary>

```text
1	# Related Work Supplement: Contrastive Learning for Code & Adjacent Areas
2	
3	> **Purpose**: Supplementary paragraphs and citations to strengthen weak areas in Related Work v1.
4	> Six new papers added; RocketQA already cited in v1.
5	> Generated: 2026-05-15
6	
7	---
8	
9	## Supplement A: Contrastive Learning for Code (insert into Section 2.2, after the ContraCode/CodeRetriever paragraph)
10	
11	Beyond learning invariance to syntactic variation, contrastive pre-training has been applied to inject structural and robustness priors into code representations. SynCoBERT \cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pre-training that aligns code, natural language, and abstract syntax tree (AST) modalities through identifier prediction and AST edge prediction objectives, demonstrating that explicitly encoding syntactic structure during contrastive pre-training improves downstream code intelligence tasks. ContraBERT \cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing nine data augmentation operators that generate adversarial code and comment variants---including identifier renaming, dead code insertion, and operand swapping---and further trains existing code models with contrastive objectives on these augmented pairs. ContraBERT shows that contrastive pre-training with targeted perturbations substantially improves model robustness against adversarial attacks while maintaining strong performance on standard benchmarks. These methods enrich the positive pair construction space for code contrastive learning, yet they focus on augmenting the pre-training signal rather than improving the selection of negative examples during fine-tuning. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, it improves which negatives the model trains against by grounding negative selection in inter-procedural data-flow structure.
12	
13	## Supplement B: Hard Negative Mining in Dense Retrieval (insert into Section 2.3, after the CL-DRD sentence)
14	
15	The curriculum learning paradigm for negative sampling has been further developed by CAPSTONE \cite{he2023capstone}, which addresses the training-inference discrepancy in dual-encoder dense retrieval. CAPSTONE expands documents with pseudo-queries during training and employs a curriculum sampling strategy that progressively improves the relevance between generated and real queries, effectively controlling negative difficulty through the query generation quality. This approach achieves strong results on both in-domain and out-of-domain retrieval benchmarks, reinforcing the finding that curriculum-based difficulty scheduling benefits dense retrieval training. While CAPSTONE focuses on bridging the training-inference gap through document expansion, our structure-grounded negatives provide an orthogonal form of curriculum: negatives that are hard because they share data-flow context with the positive, not because of embedding proximity alone.
16	
17	## Supplement C: Cross-File Code Understanding and Evaluation (insert into Section 2.4, before the closing paragraph, or as a new subsection bridge)
18	
19	The importance of cross-file context for code understanding has been empirically validated by dedicated benchmarks. CrossCodeEval \cite{ding2023crosscodeeval} constructs a diverse, multilingual benchmark for cross-file code completion across Python, Java, TypeScript, and C\#, using static analysis to identify completion targets that strictly require cross-file dependencies. Experiments show that even state-of-the-art code LLMs struggle without cross-file context, and that retrieval-augmented approaches yield clear improvements---yet performance remains far below the ceiling, indicating substantial room for better cross-file retrieval. ProGraML \cite{cummins2021programl} provides a language-independent, graph-based program representation that captures control-flow, data-flow, and call relations across entire programs, achieving strong results on data-flow analysis tasks. ProGraML demonstrates that whole-program structural representations are learnable and informative, providing conceptual grounding for StructFuse's use of inter-procedural data-flow graphs as a training signal. CoSQA \cite{huang2021cosqa} contributes a large-scale dataset of 20,000+ real web queries paired with Python code, bridging the gap between synthetic code search benchmarks and real-world developer information needs; it also introduces a contrastive learning method (CoCLR) for data augmentation in code search training. Together, these resources underscore that cross-file structural dependencies and realistic query distributions are critical dimensions for advancing code retrieval---precisely the dimensions that StructFuse's structure-grounded training targets.
20	
21	---
22	
23	## Summary of New Citations
24	
25	| Paper | Venue | Year | Area | Relation to StructFuse |
26	|-------|-------|------|------|----------------------|
27	| SynCoBERT | arXiv | 2021 | Contrastive code pre-training | Syntax-guided contrastive pre-training; StructFuse uses structure for negatives, not positives |
28	| ContraBERT | ICSE | 2023 | Contrastive code pre-training | Robustness-oriented augmentation; complementary to StructFuse's negative mining |
29	| CAPSTONE | EMNLP | 2023 | Dense retrieval | Curriculum sampling for retrieval; StructFuse provides structure-based curriculum |
30	| CrossCodeEval | NeurIPS | 2023 | Benchmark | Validates importance of cross-file context for code tasks |
31	| ProGraML | ICML | 2021 | Program graphs for ML | Whole-program graph representation; conceptual grounding for StructFuse's data-flow use |
32	| CoSQA | ACL | 2021 | Code search dataset | Real-world query benchmark with contrastive learning augmentation |
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "d2606aaf-7610-4237-84e4-51233dfde48b"
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
  "task_id": "a1772f50001039623",
  "tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "description": "Reading artifacts/paper_drafts/related_work_v1.md",
  "usage": {
    "total_tokens": 33123,
    "tool_uses": 10,
    "duration_ms": 11353
  },
  "last_tool_name": "Read",
  "uuid": "1735263b-22f4-4895-98d4-7bfcf83ce89f",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8"
}
```

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01JZ3tjH5Bov8aWhCbpWrVW7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "0e818df9-a809-4cc1-9a87-9b8d7dfbd191",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EcuquJHgGKxXkzWxdBJxNq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 13987,
      "cache_read_input_tokens": 19092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13987,
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

_source line 38 · 2026-05-16T00:43:01.206Z_

<details><summary>↩ Tool result · `toolu_01JZ3tjH5Bov8aWhCbpWrVW7`</summary>

```text
1	# 2. Related Work
2	
3	## 2.1 Dense Retrieval for Code
4	
5	Code retrieval has evolved from sparse lexical methods such as BM25 \cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \cite{feng2020codebert}, UniXcoder \cite{guo2022unixcoder}, and InferCode \cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \cite{lozhkov2024starcoder2} and Qwen2.5-Coder \cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \cite{zhang2024codesage} and SCodeR \cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \cite{jimenez2024swebench}---has motivated specialized systems: SweRank \cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by systematically comparing negative mining strategies---random, embedding-distance, and structure-aware---for contrastive code retrieval, demonstrating that the choice of mining strategy meaningfully affects retrieval quality.
6	
7	## 2.2 Contrastive Learning for Code
8	
9	Sentence-BERT \cite{reimers2019sentencebert} established contrastive fine-tuning of pretrained encoders for dense text retrieval, a paradigm that has since become dominant for code representation learning. ContraCode \cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. Ding et al.\ \cite{ding2022programcontrasts} use structure-guided code transformations to synthesize contrastive pairs, demonstrating that program-structure-aware augmentation improves code clone detection and vulnerability identification. GraphCodeBERT \cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. While GraphCodeBERT uses structural edges as a pretraining objective, StructFuse addresses a complementary dimension: we systematically study how negative selection strategy---including structure-aware alternatives---affects contrastive code retrieval across encoders with distinct representation geometries.
10	
11	## 2.3 Hard Negative Mining
12	
13	The quality of negative examples critically affects contrastive learning \cite{chen2020simclr}. In dense text retrieval, DPR \cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \cite{zeng2022cldrd} and CAPSTONE \cite{he2023capstone}---schedule negative difficulty progressively during training.
14	
15	In the code domain, CoCoHaNeRe \cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search, evaluating both BM25-selected and embedding-based negatives and reporting limitations of each non-differentiable strategy. However, their claim that non-differentiable embedding negatives are ineffective has not been evaluated under controlled conditions in structural code retrieval settings, where repository-level file localization involves richer structural cues than the NL$\to$code search setting studied by CoCoHaNeRe. StructFuse addresses this gap with a systematic comparison of three mining strategies---random, embedding-distance, and dataflow-aware---across decoder-only encoders with distinct representation geometries. Our results show that static embedding-distance mining provides reliable improvement at zero additional cost, establishing it as a strong baseline that requires no gradient computation or dynamic index updates. We further incorporate data-flow structure as an additional signal dimension in the comparison, grounding hardness in inter-procedural program semantics rather than embedding proximity alone.
16	
17	## 2.4 Code Structure in Machine Learning
18	
19	Program dependence graphs \cite{ferrante1987pdg} and code property graphs \cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements. RepoFusion \cite{shrivastava2023repofusion} further demonstrates that training code models to incorporate cross-file repository context via Fusion-in-Decoder significantly improves completion quality, even outperforming much larger models that lack repository awareness.
20	
21	Recent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \cite{liu2025codexgraph} and RepoGraph \cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \cite{chen2025locagent} and RANGER \cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GRACE \cite{wang2025grace} constructs multi-level code graphs spanning repository, module, and function granularity---integrating AST, control-flow, and data-flow edges---for hierarchical retrieval-augmented code completion. GraphCoder \cite{liu2024graphcoder} and ARISE \cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, these methods primarily leverage structural graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse operates in a distinct regime: we leverage inter-procedural data-flow graphs at \emph{training time} to construct an additional strategy dimension for systematic comparison, enabling analysis of how structural signals interact with encoder representation geometry---all with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "fe4fe41c-6154-4106-aa3f-e0a1212a730b"
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
  "task_id": "a1772f50001039623",
  "tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "description": "Reading docs/IDEA_BRIEF.md",
  "usage": {
    "total_tokens": 33130,
    "tool_uses": 11,
    "duration_ms": 12048
  },
  "last_tool_name": "Read",
  "uuid": "92767cd1-e333-4b0d-92d1-f1e6eb5e6b11",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8"
}
```

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01UswEyyh7nciGGuz8omZawR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "345fe8be-bac9-4412-abd7-e3fdeb18e568",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EcuquJHgGKxXkzWxdBJxNq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 13987,
      "cache_read_input_tokens": 19092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13987,
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

_source line 41 · 2026-05-16T00:43:02.136Z_

<details><summary>↩ Tool result · `toolu_01UswEyyh7nciGGuz8omZawR`</summary>

```text
1	# Idea Brief: StructFuse: Data-Flow-Aware Contrastive Retrieval for Repository-Level Code Repair Context Selection
2	
3	
4	- **Idea ID**: `idea_006`
5	- **Created**: 2026-05-10
6	- **Approved**: 2026-05-12
7	- **Source**: web_research
8	- **Level**: top-tier
9	- **Target Venues**: EMNLP 2026 Main + Findings (ARR submission deadline: May 25, 2026; conference: Fall 2026; topic area: 'NLP and Code Models'; dual-targeting Main and Findings to de-risk rejection given empirical contribution type)
10	
11	## Seed Topic
12	
13	Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Code Models.
14	
15	Direction: Code understanding and generation — repo-level comprehension, program repair, code reasoning, debugging, test generation, code-to-documentation, cross-language code transfer. NOT just code completion — focus on higher-level code reasoning tasks.
16	
17	Contribution type: METHOD ONLY. Propose new training methods, retrieval-augmented code repair, or inference algorithms for code tasks. Not a new benchmark or leaderboard entry.
18	
19	HARD CONSTRAINTS:
20	1. Compute: ≤200 H100-hours total. Code models are often evaluated zero-shot or few-shot — budget goes to SFT/LoRA if fine-tuning.
21	2. Time: ≤16 days. Build on existing code models (DeepSeek-Coder-V2, StarCoder2, CodeLlama, Qwen2.5-Coder) and frameworks (aider, SWE-agent, Moatless).
22	3. Eval: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests.
23	
24	Look for: repo-level context compression for code understanding, retrieval-augmented repair with semantic code search, code reasoning via execution feedback, cross-repo transfer learning. Avoid: simple prompt templates for code completion.
25	
26	Tag: direction=code_models, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].
27	
28	## Generation Journey
29	
30	1. **Start** — 开始生成，seed: 'Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Code Models.\n\nDirection: Code understanding and generation — repo-level comprehension, program repair, code reasoning, debugging, test generation, code-to-documentation, cross-language code transfer. NOT just code completion — focus on higher-level code reasoning tasks.\n\nContribution type: METHOD ONLY. Propose new training methods, retrieval-augmented code repair, or inference algorithms for code tasks. Not a new benchmark or leaderboard entry.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Code models are often evaluated zero-shot or few-shot — budget goes to SFT/LoRA if fine-tuning.\n2. Time: ≤16 days. Build on existing code models (DeepSeek-Coder-V2, StarCoder2, CodeLlama, Qwen2.5-Coder) and frameworks (aider, SWE-agent, Moatless).\n3. Eval: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests.\n\nLook for: repo-level context compression for code understanding, retrieval-augmented repair with semantic code search, code reasoning via execution feedback, cross-repo transfer learning. Avoid: simple prompt templates for code completion.\n\nTag: direction=code_models, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].'
31	2. **Problem Discovery** (829s) — 发现 4 个研究方向
32	   - Execution Simulation as Cheap Verifier for Repair Scaling
33	   - Diagnostic Process Reward Model for Multi-Step Repair
34	   - Distilling Data-Flow Analysis into Neural Context Selection
35	   - RL-Trained Active Probing for Iterative Fault Localization
36	3. **Method Synthesis** (599s) — 完成: "Execution Simulation as Cheap Verifier for Repair Scaling" [solid] → ICSE 2027 (abstract Jun 23, paper Jun 30, 2026), EMNLP 2026 (ARR submission May 25, 2026), AAAI 2027 (expected ~Aug 2026)
37	3. **Method Synthesis** (320s) — 完成: "Diagnostic Process Reward Model for Multi-Step Repair" [solid] → AAAI 2027 (full paper deadline: August 1, 2026), ICLR 2027 (estimated deadline: October 2026), ICSE 2027 (abstract deadline: June 23, 2026)
38	3. **Method Synthesis** (371s) — 完成: "Distilling Data-Flow Analysis into Neural Context Selection" [solid] → EMNLP 2026 (ARR submission deadline: May 25, 2026; commitment deadline: Aug 2, 2026), AAAI 2027 (expected submission deadline: ~Aug 2026; conference: Feb 16-23, 2027 in Montréal), ICLR 2027 (expected submission deadline: ~Sep-Oct 2026; based on historical pattern)
39	3. **Method Synthesis** (713s) — 完成: "RL-Trained Active Probing for Iterative Fault Localization" [solid] → ICSE 2027 (full paper deadline June 30, 2026), AAAI 2027 (expected deadline ~August 1, 2026), ICLR 2027 (expected deadline ~September 2026)
40	
41	## Core Problem
42	
43	Repository-level bug repair requires selecting relevant context from large codebases. Existing context selectors fall into three paradigms, each with fundamental limitations: (1) Neural selectors like SWE-Pruner train on LLM-generated labels that are coupled to a specific teacher model's biases and selection patterns—labels are stochastic, non-reproducible, and encode the teacher's blind spots. (2) Retrieve-and-rerank methods like SweRank (ICLR 2026) achieve strong text-based localization but miss structural dependencies—lexically similar but structurally unrelated code becomes a false positive. (3) Graph-guided agents like LocAgent, RANGER, and CodexGraph capture structural edges (import/call/inheritance/USES) but omit fine-grained data-flow (def-use) edges, and operate purely at inference time without using structural signals to improve model training; ARISE uses intra-procedural def-use but only at runtime via tool calls, not as distilled knowledge, and explicitly does not cross call boundaries. On SWE-bench Pro (where top SEAL-standardized scores range from ~42-59%—GPT-5.4 at 59.1%, Claude Opus 4.6 at 51.9%—leaving 41-58pp improvement headroom, and context selection accounts for 4-10pp swings), context quality remains a key differentiator with substantial room for improvement. Can we build a context selector that leverages inter-procedural data-flow signals for structurally-grounded, interpretable, and model-independent selections—using deterministic program analysis rather than stochastic LLM judgments?
44	
45	## Opportunity / Why Now
46	
47	SWE-Pruner (arXiv:2601.16746) demonstrated a 0.6B neural skimmer can reduce tokens 23-54% with <1pp degradation, but its supervision comes from Qwen3-Coder-30B-A3B-Instruct (an MoE model with 3.3B active parameters)—while inference is cheap (~$10-35 to label 61K samples), the labels are coupled to that model's biases, non-reproducible across runs, and provide no interpretable rationale for selections. LocAgent (ACL 2025) showed graph-guided localization achieves 92.7% file-level accuracy using import/invocation/inheritance edges with fine-tuned Qwen2.5-32B, but omits data-flow edges. SweRank (ICLR 2026) achieves SOTA retrieve-and-rerank localization but is purely text-based. RANGER (arXiv:2509.25257) builds comprehensive repository knowledge graphs with MCTS-guided exploration and bi-encoder + cross-encoder cascade, achieving strong results on RepoBench (0.5471 Accuracy@5) and CrossCodeEval—but uses only structural/syntactic edges (CONTAINS, HAS_METHOD, INHERITS, USES) without data-flow, and is purely an inference-time system with no model training. CodexGraph (NAACL 2025) bridges LLMs and code repos via Neo4j code property graphs with Cypher queries (22.96% Pass@1 on SWE-bench Lite)—but again is purely inference-time with no data-flow edges, and the paper itself acknowledges room for 'schema completeness' improvements. ARISE (arXiv:2605.03117) confirmed data-flow slicing yields +17pp Function Recall@1, but (a) uses only Python's ast module for intra-procedural analysis (explicitly does not cross call boundaries), and (b) keeps analysis as runtime tool calls adding latency per agent step. SWE-Fixer (ACL Findings 2025) combines BM25 with a fine-tuned 7B retriever for coarse-to-fine file retrieval but uses no structural program analysis features. Sliceformer (arXiv:2604.26961) validated that data-flow knowledge transfers to neural models with 22% ExactMatch gains on slicing tasks. The opportunity: no existing work (a) uses inter-procedural def-use analysis for repair context selection, (b) distills data-flow signals into a fast retrieval model via contrastive training, or (c) exploits structural connectivity for contrastive hard negative mining. ARISE's intra-procedural limitation, RANGER/CodexGraph's inference-only graph use without data-flow edges, and SweRank's text-only approach leave a clear gap for inter-procedural data-flow-aware retrieval with structural training signal.
48	
49	## Landscape (SOTA & Limitations)
50	
51	**Neural context selectors**: SWE-Pruner trains a 0.6B skimmer on 61K samples labeled by Qwen3-Coder-30B-A3B-Instruct (an MoE model with 3.3B active parameters per forward pass, costing ~$10-35 for labeling at $0.07-0.19/1M input tokens), achieving <1pp degradation on SWE-bench Verified (70.6%->70.2%)—though SWE-bench Verified is known contaminated (OpenAI, Feb 2026). Squeez (arXiv:2604.04979) fine-tunes Qwen 3.5 2B for task-conditioned tool-output pruning (0.86 recall, 92% token removal) but targets tool outputs, not repository context. LongCodeZip (ASE 2025) achieves 5.6x compression via perplexity-based ranking, training-free but code-agnostic. **Retrieve-and-rerank approaches**: SweRank (ICLR 2026, arXiv:2505.07849) achieves SOTA issue localization via SweRankEmbed (bi-encoder retriever) + SweRankLLM (listwise LLM reranker), trained on the SweLoc dataset—purely text-based with no structural signals. SweRank+ (arXiv:2512.20482) extends to multilingual multi-turn ranking with 155K training instances. SWE-Fixer (ACL Findings 2025) combines BM25 with a fine-tuned 7B retriever (SWE-Fixer-Retriever-7B) for coarse-to-fine file retrieval, achieving 24.7%/32.8% on SWE-bench Lite/Verified with P2P filtering—architecturally the closest prior work to our retrieval fusion, but uses learned embeddings without structural program analysis features. **Graph-guided approaches**: LocAgent (ACL 2025, arXiv:2503.09089) parses codebases into directed heterogeneous graphs with import/invocation/inheritance edges, achieving 92.7% file-level accuracy with fine-tuned Qwen2.5-32B—but omits data-flow (def-use) edges and requires a 32B model at inference. RANGER (arXiv:2509.25257) constructs repository knowledge graphs with six node types (Module, Class, Function, Method, Field, GlobalVariable) and structural edges (CONTAINS, HAS_METHOD, HAS_FIELD, INHERITS, USES), employing MCTS-guided graph exploration with a bi-encoder (mxbai-embed-large-v1, 335M) + cross-encoder (bge-reranker-v2-m3, 568M) cascade—achieves 0.5471 Accuracy@5 on RepoBench with Qwen-3-8B embeddings, but uses no data-flow edges and is purely an inference-time system with no model training using structural signals. CodexGraph (NAACL 2025, arXiv:2408.03910) bridges LLMs and code repositories via Neo4j code property graphs with Cypher queries, using a similar structural schema (MODULE, CLASS, METHOD, FUNCTION, FIELD, GLOBAL_VARIABLE nodes; CONTAINS, HAS_METHOD, HAS_FIELD, INHERITS, USES edges)—achieves 22.96% Pass@1 on SWE-bench Lite with GPT-4o, but is purely inference-time with no model training, no data-flow edges, and the paper itself acknowledges room for improvement in 'schema completeness' including 'adding edges related to function calls.' KGCompass (arXiv:2503.21710) constructs repository knowledge graphs (58.3% repair) but with heavy construction overhead. GraphCoder (ASE 2024) uses code context graphs with control-flow and data-dependence for coarse-to-fine retrieval in code completion—related but targets completion, not repair context selection. SaraCoder (ICLR 2026) orchestrates semantic and structural cues for code completion with a graph-based structural similarity metric—demonstrates the value of structural signals in retrieval but does not address repair or use def-use data-flow. **Data-flow-specific approaches**: ARISE (arXiv:2605.03117) augments SWE-agent with statement-level def-use edges via Python's ast module, gaining +17pp Function Recall@1 and +4.7pp Pass@1 (22.0% on SWE-bench Lite with Qwen2.5-Coder-32B)—but is limited to intra-procedural analysis (explicitly does not cross call boundaries), keeps analysis as runtime tool calls, and requires a 32B model at inference. LLMxCPG (USENIX Security 2025) uses Code Property Graphs for vulnerability detection (67-91% code reduction, 15-40% F1 gain) but targets security, not repair context. Sliceformer (arXiv:2604.26961) distills DFG knowledge into CodeT5+ for slicing tasks via dataflow-aware pretraining objectives, validating structural knowledge transfer but not addressing repair. **Contrastive learning for code**: CoCoHaNeRe (TOSEM 2025) demonstrates that hard negative mining significantly improves contrastive code search (+7-11% MRR over baselines), but uses random or embedding-distance-based negatives without structural awareness. No existing work uses program-analysis-derived structural connectivity to mine hard negatives. **Compression paradigms**: An empirical study (arXiv:2604.13725) shows continuous latent vector compression surpasses full-context by up to 28.3% BLEU at 4x compression. **Benchmarks**: SWE-bench Pro (Scale AI, 1865 tasks total, 731 public) is the recommended hard benchmark—top SEAL-standardized scores: GPT-5.4 (xHigh) 59.1%, Claude Opus 4.6 (thinking) 51.9%, Gemini 3.1 Pro 46.1%; custom scaffolding goes higher (Claude Mythos Preview 77.8%). The 41-58pp gap between SEAL scores and perfect resolution means context selection has proportionally large impact—unlike near-saturated SWE-bench Verified where SWE-Pruner's <1pp degradation suggests diminishing returns. SWE-bench Lite (300 instances) remains widely used. RepoBench-R (ICLR 2024) directly evaluates cross-file context retrieval. **Gap**: No existing work combines inter-procedural data-flow analysis with contrastive hard negative mining for repair context retrieval. ARISE is intra-procedural only; SweRank and SWE-Fixer are text-only; LocAgent uses coarser structural edges without def-use; RANGER and CodexGraph use structural graphs at inference only, not for training; CoCoHaNeRe shows hard negatives work for code search but without structural awareness. The fusion of inter-procedural data-flow features with lexical retrieval via data-flow-aware contrastive learning is unexplored.
52	
53	## Proposed Approach
54	
55	We propose StructFuse, a two-stage context retrieval system that combines inter-procedural data-flow analysis with a novel data-flow-aware contrastive learning objective for repository-level code repair context selection.
56	
57	**Stage 1: Scope-Bounded Inter-Procedural Data-Flow Extraction (Days 1-3).** For ~5K SWE-smith training instances, we extract inter-procedural data-flow features using a two-phase CodeQL strategy designed to prevent query-evaluation blowups. **Phase 1a (call-graph pre-computation):** For each instance, we first run a lightweight CodeQL query to extract the call graph and identify all functions within 2 call-graph hops of the buggy function. This is fast (seconds per repo) because call-graph queries are relational joins, not data-flow tracking. **Phase 1b (scope-bounded data-flow query):** We then configure CodeQL's inter-procedural data-flow API with sources restricted to parameters and return values of only the functions identified in Phase 1a (within 2 call-graph hops), and sinks restricted to variable reads within those same functions. This bounds the analysis scope *before* query evaluation begins, preventing the Cartesian-product blowup that occurs with broad 'all parameters as sources' definitions—the reviewer correctly identified that post-hoc graph-distance filtering does not prevent evaluation-time blowups. We enforce strict resource limits: --timeout=300s and --ram=8192 per repo query. **Graceful degradation:** For repos where CodeQL times out (>300s) or produces insufficient coverage (<5 reachable files from bug location), we fall back to Beniget for intra-file def-use chains and record a binary label-source indicator (inter_procedural=True/False) for each instance. We budget Day 1 specifically for CodeQL query development and validation on 10 pilot repos—testing query precision, recall against gold patches, extraction throughput, and critically: timeout rates and memory consumption. We report three pilot statistics before scaling: (a) mean/max query time per repo, (b) fraction of repos that timeout, (c) average files reachable within 2 call-graph hops + data-flow from bug location. If >30% of repos timeout, we tighten to 1 call-graph hop before scaling. For each candidate file/function, we compute: (a) shortest data-flow path distance to the buggy location, (b) number of distinct data-flow paths, (c) dependency type (inter-procedural def-use, call-graph, import), (d) label-source indicator (CodeQL inter-procedural vs. Beniget intra-procedural). We also extract lexical features (BM25 scores, SweRankEmbed similarity) and structural metadata (git co-change frequency, import distance).
58	
59	**Stage 2: Data-Flow-Aware Contrastive Retrieval Training (Days 4-6).** This is the core methodological contribution. We train a Qwen2.5-Coder-3B bi-encoder retriever with a two-component objective:
60	
61	(a) *Data-flow-aware hard negative mining*: For each training instance, hard negatives are files that are lexically similar to the bug-relevant files (high BM25/embedding similarity) but structurally disconnected (no data-flow path within the scope-bounded analysis from the buggy location). This is inspired by CoCoHaNeRe's (TOSEM 2025) demonstration that hard negatives dramatically improve code search, but we replace their embedding-distance-based mining with program-analysis-derived structural connectivity—a fundamentally different and more principled signal. **Theoretical justification:** Embedding-distance-based hard negatives (as in CoCoHaNeRe) are partly redundant with the model's own learned similarity: the contrastive encoder already computes embedding similarity, so negatives selected by embedding distance provide gradient signal along dimensions the model has already partially learned to separate. In contrast, structurally disconnected negatives provide an *orthogonal* learning signal—the model cannot derive inter-procedural data-flow connectivity from lexical features alone, so these negatives force the model to internalize a structural relevance concept that is inaccessible through text-based training. In information-theoretic terms, this increases the effective diversity of the negative set in the InfoNCE objective, tightening the mutual information bound between queries and truly relevant code.
62	
63	(b) *Structure-conditioned contrastive loss*: We use an InfoNCE-style loss where positive pairs are (issue description, data-flow-connected code) and negatives include both random negatives and the structurally-mined hard negatives above. We weight the contrastive loss by data-flow path strength: code reachable via short, direct def-use chains receives higher positive weight than code connected only via long transitive paths. This encodes the inductive bias that direct data-flow connections are stronger relevance signals than transitive ones.
64	
65	(c) *Label-source-aware training*: To address heterogeneity from the Beniget fallback, we include the binary label-source indicator (inter-procedural vs. intra-procedural) as an explicit input feature to the fusion head. We weight instances with inter-procedural labels slightly higher (1.2x) in the contrastive loss, reflecting higher label quality. We include a dedicated ablation: training with vs. without Beniget-only instances, and with vs. without the label-source indicator.
66	
67	(d) *Multi-signal fusion head*: On top of the contrastive encoder, a lightweight MLP fusion head combines the learned embedding similarity with explicit features (data-flow distance, BM25 score, co-change frequency, label-source indicator) for final ranking. This allows the model to leverage both learned representations and interpretable structural features.
68	
69	Training takes ~3-5 hours per run on a single H100. We run 8 ablation configurations: (i) contrastive with data-flow hard negatives, (ii) contrastive with random negatives only, (iii) contrastive with embedding-distance hard negatives (CoCoHaNeRe-style, as direct comparison), (iv) standard cross-entropy SFT (as in SWE-Pruner's paradigm), (v) full fusion with MLP head, (vi) inter-procedural features only vs. intra-procedural only (testing whether crossing call boundaries matters), (vii) data-flow features only vs. lexical only, (viii) with vs. without Beniget-only instances + label-source indicator.
70	
71	**Stage 3: Evaluation (Days 7-11).** At inference, StructFuse operates as a two-stage cascade: (1) coarse file selection via BM25 + data-flow reachability (retain files within scope-bounded data-flow analysis OR top-30 BM25), then (2) fine-grained function ranking via the trained 3B contrastive model. This cascade adds architectural novelty over flat ranking approaches like SweRank while being directly comparable to SWE-Fixer's coarse-to-fine paradigm—with the key difference that our coarse stage uses structural reachability, not just BM25. Unlike RANGER and CodexGraph, which use graphs only at inference time, StructFuse uses structural signals during training to produce a model that has internalized data-flow relevance patterns.
72	
73	**Primary evaluation** (budget-safe): (a) SWE-bench Lite (300 instances, full)—the most widely compared benchmark with established baselines including ARISE (22.0% Pass@1). We estimate ~5-12min per instance with Qwen3.6-27B on H100 using vLLM serving under a 50-turn agent budget (consistent with SWE-agent's recommended cost-conservative configuration of $1/instance and 50-turn limit), yielding ~25-60h total. (b) RepoBench-R (cross-file retrieval evaluation, no LLM needed, ~15h).
74	
75	**Secondary evaluation** (if timeline permits): SWE-bench Pro (300-instance stratified sample of 731 public instances, ~25-60h). This provides signal on harder tasks where the 41-58pp SEAL gap means context selection has proportionally larger impact.
76	
77	Metrics: localization recall@k (file and function level), end-to-end Pass@1 repair rate, token efficiency, and a new metric: *structural precision*—what fraction of selected files are reachable via data-flow from the actual fix. End-to-end evaluation uses Qwen3.6-27B exclusively (open-weight, no API costs). We compare against: (i) SweRank/SweRankEmbed (ICLR 2026, SOTA text-based retrieval), (ii) SWE-Pruner (LLM-labeled selector), (iii) SWE-Fixer-Retriever (BM25 + neural, ACL Findings 2025), (iv) BM25 baseline, (v) ARISE's graph tools (intra-procedural def-use, 22.0% on SWE-bench Lite), (vi) no-pruning full-context.
78	
79	**Improvement ceiling analysis:** We explicitly address expected improvement magnitude. On SWE-bench Verified, SWE-Pruner's <1pp degradation suggests text-based context selection is near-sufficient for the remaining solvable instances—but this is a ceiling effect on a near-saturated benchmark. On SWE-bench Lite and Pro, where ARISE achieves only 22.0% and SEAL scores plateau at 42-59%, the headroom is 41-78pp. We hypothesize structural signals help precisely in cases where text-based retrieval fails: bugs caused by data-flow through indirect dependencies (e.g., a function modifies a shared data structure consumed 2 call-graph hops away, with no lexical overlap between the modifier and consumer). We include a qualitative failure analysis of 50 SWE-Pruner/SweRank failures on SWE-bench Lite, categorizing failures by whether data-flow analysis would have identified the correct context. We frame the primary contribution as the *training methodology* (data-flow-aware contrastive hard negatives)—generalizable to code search, vulnerability detection, and other code intelligence tasks—not just absolute improvement on one benchmark.
80	
81	**Stage 4: Writing (Days 11-15).** The paper presents four contributions: (1) *Methodological*: data-flow-aware contrastive hard negative mining—using program analysis to generate training negatives that are structurally disconnected from the bug despite lexical similarity, providing an orthogonal learning signal that embedding-distance negatives cannot offer. (2) *Technical*: scope-bounded inter-procedural data-flow extraction via two-phase CodeQL queries (call-graph pre-computation then bounded data-flow), with graceful degradation and label-source indicators for heterogeneous extraction quality. (3) *Empirical*: demonstration that inter-procedural def-use edges (crossing call boundaries) provide gains beyond ARISE's intra-procedural analysis, LocAgent's import/call/inheritance edges, and RANGER/CodexGraph's inference-only structural graphs, with the contrastive objective outperforming standard SFT on the same data. (4) *Practical*: a model-independent pipeline (CodeQL to contrastive training to 3B retriever) with deterministic, reproducible labels, interpretable selections with traceable data-flow paths, and zero marginal cost when scaling to new repositories (only CodeQL extraction needed, no LLM inference).
82	
83	## Resource Estimate
84	
85	- **auto_research**: {'claude_api_cost': '$200-400 (2000-4000 turns for iterative pipeline development, CodeQL query debugging, experiment scheduling)', 'estimated_gpu_cost': '$500-700 (200h H100 at spot ~$2.50/hr to on-demand ~$3.50/hr)', 'gpu_hours': '~200h H100 (full ablation suite including label-heterogeneity experiments, hyperparameter sweep over contrastive temperature and hard negative ratio, primary + secondary benchmark evaluation)', 'gpu_utilization': '~85-90% utilization; agent continuously launches experiments, parallelizes independent ablations', 'risk_note': 'Agent should validate scope-bounded CodeQL query on first 10 repos and report: (a) timeout rate with 300s limit, (b) avg reachable files within 2 call-graph hops, (c) fraction requiring Beniget fallback. If CodeQL timeout rate >30%, agent autonomously tightens to 1 call-graph hop. Label-source statistics automatically tracked and reported.', 'speed_bottleneck': 'SWE-bench Lite evaluation (~8min/instance x 300 instances on Qwen3.6-27B = ~40 H100-hours; parallelizable across GPUs). Optional SWE-bench Pro adds ~40h.', 'team': '0 (initial setup: CodeQL CLI installation, SWE-smith repo cloning, SWE-bench evaluation harness)', 'timeline': '10-12 days with 2-4 H100 GPUs available concurrently'}
86	- **human_in_loop**: {'claude_api_cost': '$80-150 (800-1500 turns for pipeline code generation and debugging)', 'estimated_gpu_cost': '$330-470 (140h H100 at spot ~$2.50/hr)', 'gpu_hours': '~140h H100 (same pipeline; agent manages CodeQL builds and queues training; human reviews CodeQL query quality at Day 1 pilot and ablation results at Day 6)', 'gpu_utilization': '~75-85% utilization; agent parallelizes independent experiments', 'risk_note': 'Tight timeline requires pre-validated CodeQL setup; human reviews scope-bounded query on 3 repos in first 4 hours before scaling. Label-source tracking automated from extraction phase.', 'team': '1 researcher, ~45min/day check-in for CodeQL query review and experiment approval', 'timeline': '12-14 days'}
87	- **manual**: {'claude_api_cost': '$0 for evaluation (Qwen3.6-27B only); ~$50-100 for writing assistance', 'estimated_gpu_cost': '$400-600 (170h H100 at spot ~$2.50/hr; no LLM API costs—all evaluation uses open-weight Qwen3.6-27B)', 'gpu_hours': '~170h H100 (CodeQL database creation + scope-bounded data-flow extraction for Python repos: ~10h CPU-parallel, no GPU; feature extraction: ~10h; contrastive training 8 ablation runs: ~40h; SWE-bench Lite evaluation 300 instances with Qwen3.6-27B at ~5-12min/instance: ~25-60h; RepoBench-R evaluation: ~15h; optional SWE-bench Pro 300 instances: ~25-60h if timeline permits)', 'gpu_utilization': '~70-80% utilization during evaluation phase (Qwen3.6-27B inference is GPU-bound via vLLM); ~50-60% during contrastive training', 'risk_note': "CodeQL scalability risk mitigated by scope-bounded query design: Phase 1a extracts call graph (fast, seconds/repo), Phase 1b restricts sources/sinks to functions within 2 call-graph hops. Explicit --timeout=300s and --ram=8192 per repo. Day 1 pilot on 10 repos reports: (a) mean/max query time, (b) timeout rate, (c) average reachable files. If >30% timeout, tighten to 1 call-graph hop. Beniget fallback with label-source indicator handles remaining failures. Evaluation time estimate based on SWE-agent's recommended 50-turn budget and $1/instance cost-conservative configuration; Qwen3.6-27B achieves ~85 TPS on RTX 3090, substantially faster on H100 with vLLM. Primary evaluation scoped to SWE-bench Lite (300) + RepoBench-R to ensure timeline safety.", 'team': '1-2 researchers (one with CodeQL/program analysis, one with contrastive learning; can be same person)', 'timeline': '15 days (Day 1: CodeQL query development + scope-bounded validation on 10 pilot repos, reporting timeout rates and reachability statistics; Days 2-3: full-scale data-flow extraction + feature computation with label-source tracking; Days 4-6: contrastive training + 8 ablations including label-heterogeneity ablation; Days 7-11: evaluation on SWE-bench Lite + RepoBench-R primary, SWE-bench Pro secondary; Days 11-15: writing including failure analysis and improvement ceiling discussion)'}
88	
89	## Key References
90	
91	- SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents (arXiv:2601.16746, Jan 2026) — 0.6B skimmer trained on labels from Qwen3-Coder-30B-A3B (MoE, 3.3B active params), <1pp degradation on SWE-bench Verified
92	- LocAgent: Graph-Guided LLM Agents for Code Localization (ACL 2025, arXiv:2503.09089) — 92.7% file-level accuracy on SWE-bench Lite using import/invocation/inheritance edges with fine-tuned Qwen2.5-32B; no def-use edges
93	- SweRank: Software Issue Localization with Code Ranking (ICLR 2026, arXiv:2505.07849) — SOTA retrieve-and-rerank via SweRankEmbed + SweRankLLM; text-only, no structural signals
94	- SweRank+: Multilingual, Multi-Turn Code Ranking (arXiv:2512.20482, Dec 2025) — extends SweRank to multilingual multi-turn with 155K training instances
95	- SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution (ACL Findings 2025) — BM25 + fine-tuned 7B retriever for coarse-to-fine file retrieval; 24.7%/32.8% on SWE-bench Lite/Verified; no structural program analysis features
96	- RANGER: Repository-Level Agent for Graph-Enhanced Retrieval (arXiv:2509.25257, Sep 2025) — repository knowledge graph with structural edges (CONTAINS, HAS_METHOD, INHERITS, USES), MCTS-guided exploration with bi-encoder (mxbai-embed-large-v1, 335M) + cross-encoder (bge-reranker-v2-m3, 568M) cascade; 0.5471 Accuracy@5 on RepoBench; no data-flow edges, no model training with structural signals, purely inference-time
97	- CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases (NAACL 2025, arXiv:2408.03910) — Neo4j code property graphs with Cypher queries; structural edges only (CONTAINS, HAS_METHOD, HAS_FIELD, INHERITS, USES), no data-flow edges; 22.96% Pass@1 on SWE-bench Lite with GPT-4o; purely inference-time, no model training
98	- ARISE: Repository-level Graph Representation for Agentic Fault Localization and Repair (arXiv:2605.03117, May 2026) — intra-procedural def-use edges via Python ast module (does NOT cross call boundaries), +17pp Function Recall@1, 22.0% Pass@1 on SWE-bench Lite with Qwen2.5-Coder-32B, runtime tool calls only
99	- Sliceformer: Static Program Slicing Using Language Models With Dataflow-Aware Pretraining (arXiv:2604.26961, Apr 2026) — validates data-flow knowledge transfer to neural models via DFG-aware pretraining objectives
100	- CoCoHaNeRe: Effective Hard Negative Mining for Contrastive Learning-Based Code Search (TOSEM 2025) — demonstrates hard negative mining improves code search MRR by 7-11% over baselines; uses embedding-distance negatives, not structural
101	- GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph (ASE 2024) — coarse-to-fine retrieval using control-flow and data-dependence graphs for code completion
102	- SaraCoder: Orchestrating Semantic and Structural Cues for Repository-Level Code Completion (ICLR 2026) — graph-based structural similarity for code completion retrieval
103	- LLMxCPG: Context-Aware Vulnerability Detection Through CPG-Guided LLMs (USENIX Security 2025) — CPG-guided context extraction, 67-91% code reduction
104	- Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents (arXiv:2604.04979, Apr 2026) — 0.86 recall, 92% token removal on tool outputs
105	- On the Effectiveness of Context Compression for Repository-Level Tasks (arXiv:2604.13725, Apr 2026) — continuous latent vectors surpass full-context by 28.3% at 4x compression
106	- LongCodeZip: Compress Long Context for Code Language Models (ASE 2025, arXiv:2510.00446) — 5.6x training-free compression
107	- RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems (ICLR 2024, arXiv:2306.03091) — cross-file retrieval evaluation benchmark
108	- SWE-ContextBench: A Benchmark for Context Learning in Coding (arXiv:2602.08316, Feb 2026) — 1100+376 context evaluation tasks
109	- On the Role of Fault Localization Context for LLM-Based Program Repair (arXiv:2604.05481, Apr 2026) — file-level is dominant factor
110	- Why SWE-bench Verified No Longer Measures Frontier Coding Capabilities (OpenAI, Feb 2026) — contamination analysis
111	- SWE-bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? (Scale AI, arXiv:2509.16941, 2025) — 1865 tasks, 731 public; SEAL top scores: GPT-5.4 59.1%, Claude Opus 4.6 51.9%
112	- Contrastive Learning with Hard Negative Samples (arXiv:2010.04592, Robinson et al., 2021) — theoretical analysis of hard negative sampling in contrastive learning; demonstrates debiased contrastive objectives
113	- LLMDFA: Analyzing Dataflow in Code with Large Language Models (NeurIPS 2024)
114	- SWE-smith: Scaling Data for Software Engineering Agents (NeurIPS 2025 D&B Spotlight) — 50K instances from 128 Python repos
115	- SWE-bench: Can Language Models Resolve Real-World GitHub Issues? (ICLR 2024)
116	
117	## Reviewer Evaluation
118	
119	**Scores**:
120	  - clarity: **{'rationale': 'Exceptional clarity across all dimensions. The four-stage approach is precisely specified with day-by-day timeline. The scope-bounded CodeQL strategy is explained mechanistically (Phase 1a call-graph, Phase 1b bounded data-flow). The ablation suite (8 configurations) directly tests each hypothesis. The theoretical justification for why structural negatives provide orthogonal gradient signal is well-articulated. The honest framing of SWE-Pruner (70.6%→70.2%, <1pp degradation) and improvement ceiling discussion are exemplary.', 'score': 5}**/5
121	  - feasibility: **{'rationale': 'The scope-bounded CodeQL strategy (call-graph pre-computation then restricted source/sink within 2 hops) is well-designed to prevent query-evaluation blowups — this directly addresses the critical scalability concern from Round 5. The Day 1 pilot with explicit go/no-go criteria (>30% timeout → tighten to 1 hop), Beniget fallback with label-source indicators, and 300s/8GB resource limits are realistic engineering. The 15-day timeline with ~5K training instances, 8 ablation runs at ~3-5h each, SWE-bench Lite (300 instances) + RepoBench-R primary evaluation, and SWE-bench Pro as secondary is tight but achievable. ~170h H100 fits the 200h budget with buffer. One concern: CodeQL database creation for ~5K SWE-smith repos is non-trivial (each requires a separate database), though this is CPU-bound and parallelizable.', 'score': 4}**/5
122	  - impact: **{'rationale': 'The training methodology (data-flow-aware contrastive hard negatives) is generalizable beyond repair to code search, vulnerability detection, and other code intelligence tasks — this broad applicability raises impact. The practical value is strong: deterministic labels, zero marginal cost, model-independent, interpretable selections. The improvement ceiling is honestly discussed, and the paper correctly argues structural signals matter most on unsaturated benchmarks (SWE-bench Pro 41-58pp gap). Impact is limited by being an incremental rather than paradigm-shifting contribution.', 'score': 4}**/5
123	  - novelty: **{'rationale': 'The combination of inter-procedural data-flow analysis for contrastive hard negative mining in code retrieval training is genuinely novel. No existing work uses program-analysis-derived structural connectivity for hard negative mining — CoCoHaNeRe uses embedding-distance negatives, ARISE is intra-procedural only and inference-time, RANGER/CodexGraph use structural graphs at inference only without data-flow edges. The theoretical argument about orthogonal gradient signal vs. embedding-distance negatives is sound. Deducted from 5 because the fusion of structural + lexical signals for retrieval is a well-trodden pattern (SWE-Fixer, SaraCoder), and the contrastive objective itself (InfoNCE with weighted positives) is standard — the novelty is specifically in what generates the negatives.', 'score': 4}**/5
124	
125	## Human Review Note
126	
127	## Agent 审核结果（完整三阶段 pipeline）
128	
129	**Verdict**: PASS
130	
131	**入口三重共识 (X)**: 29.0%
132	**终审自评 (Y)**: 34.0%
133	**出口三重共识 (Z)**: 34.0%
134	**Z 区间**: [28.0%, 38.0%]
135	**真实提升 (Z-X)**: +5.0 pp
136	**幻觉幅度 (Y-Z)**: +0.0 pp
137	**出口一致性**: 高
138	**出口三次评估**: [34.0, 34.0, 34.0]
139	
140	### 优化方案 / 拒绝详情
141	【优化方案】
142	
143	1. **[标题]** — 原标题 "StructFuse: Data-Flow-Aware Contrastive Retrieval for Repository-Level Code Repair Context Selection" 改为 "StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval"。将 "contrastive retrieval methodology" 置于前景，"code" 作为 instantiation domain 而非 pipeline 目标；去掉 "Repository-Level Code Repair Context Selection" 的 SE 色彩 — [命中 Significance / venue fit：降低 EMNLP reviewer 的 "this is a SE paper" 第一印象]
144	
145	2. **[Introduction — 动机重构，双支柱重新排序]** — 原稿以 "structural disconnection signal provides an orthogonal learning signal" 为单一动机，且 "orthogonal" 和 "tightening InfoNCE MI bound" 属 overclaim。改为双支柱结构：**Primary** = complementary signal dimension（structural connectivity encodes a relevance dimension entirely absent from textual signals，no amount of text-based training can recover inter-procedural data-flow relationships from token sequences alone）；**Secondary** = selection drift immunity（structural graph externally fixed，negative set does not drift with encoder updates）。显式提出 research question："Can structure-grounded contrastive training transfer non-differentiable program analysis knowledge into neural representations?" — [命中 Novelty + Clarity：从"又一个 code retrieval 系统"升级为"识别 embedding-distance negatives 根本性局限并提出 complementary paradigm"；且即使 reviewer 不买 selection drift severity，primary motivation 仍成立]
146	
147	3. **[Introduction — 跨域泛化原则]** — 原稿完全限于 code repair retrieval。新增显式抽象：*任何存在外部固定结构化知识图的领域（分子交互网络、电路拓扑、知识图谱 entity retrieval）都可用同一 paradigm 做 drift-immune structure-grounded hard negative mining*，code 是最佳 testbed（formal semantics 保证结构标注正确性）。Discussion 中勾勒 3-5 句跨域迁移路径 — [命中 Novelty / generalizability：直接回应 EMNLP reviewer 常见降分理由 "contribution 过于 domain-specific, applicability narrow"；让非 code 背景 reviewer 和 Area Chair 也能看到价值]
148	
149	4. **[Introduction — 形式化定义]** — 原稿无形式化。新增：给定检索域 D、结构图 G、相似度函数 s、查询 q，structure-grounded hard negative = argmax\_{x ∈ D : s(x,q) > τ ∧ ¬reachable\_G(x,q)} s(x,q)。强调结构图外部固定、不随 encoder 更新 — [命中 Novelty + Technical Soundness：提供 
150	
151	
152	
153	## MVP Validation Results
154	
155	- **Date**: 2026-05-12
156	- **Hypothesis Supported**: Yes
157	
158	### Key Metrics
159	
160	P1: timeout=0%, Fisher p=1.54e-7, instance_recall=75% | P2a: AUC=0.78, BM25_coeff=-1.80 | P2b(pool50): random R@1=0.525, emb_dist R@1=0.488 (-3.7pp) | Scale check: Z=40.8% instances have connected≠gold, timeout=4%
161	
162	### Summary
163	
164	MVP 三阶段验证完成。P1: CodeQL 2-hop dataflow 提取可行（timeout 0%, 8/10 repos 成功）；H2 sanity check 通过（Fisher p=1.54e-7, connected 文件 gold 覆盖率 1.44% vs disconnected 0%）。P2a: DataFlow+BM25 线性分类器 AUC=0.78 vs 纯 BM25 0.476，BM25 系数为负(-1.80)支持核心动机。P2b: random negatives (recall@1=0.525 at pool=50) 显著优于 embedding-distance negatives (recall@1=0.488)，确认 naive hard negatives 有害。Dataflow vs random 在 8-repo MVP 规模不可测（connected⊆gold 导致数据相同），但 50-repo 规模验证确认 40.8% 的 instances 有 connected-but-not-gold 文件（中型 repo 55.7%），方法在全量数据上可行。
165	
166	### Recommendation
167	
168	GO — 进入 research 阶段。立即启动 M1 全量 CodeQL 提取（CPU, ~10h），并行完成 paper_framing.md 和 experiment_plan.yaml。P2b dataflow 对比将在全量数据上完成。DDL May 25 距今 13 天，时间线紧但可控。
169	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "90e1d721-d595-4278-b5c0-26177cf9a996"
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
  "task_id": "a1772f50001039623",
  "tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "description": "Searching for grace",
  "usage": {
    "total_tokens": 33137,
    "tool_uses": 12,
    "duration_ms": 12359
  },
  "last_tool_name": "Grep",
  "uuid": "095314a5-c1f7-4350-8916-c185576a7f48",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8"
}
```

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Grep · `toolu_01BiA1MrWE6vVHrVcwQCVXpW`</summary>

```json
{
  "pattern": "grace",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "type": "md",
  "output_mode": "content",
  "context": 3,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "16a8cfcf-6d64-45a7-8c55-4d31afa6fa7c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EcuquJHgGKxXkzWxdBJxNq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 13987,
      "cache_read_input_tokens": 19092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13987,
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

_source line 44 · 2026-05-16T00:43:02.229Z_

<details><summary>↩ Tool result · `toolu_01BiA1MrWE6vVHrVcwQCVXpW`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/docs/IDEA_BRIEF.md-78-
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/docs/IDEA_BRIEF.md-79-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/docs/IDEA_BRIEF.md-80-
docs/IDEA_BRIEF.md:81:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/docs/IDEA_BRIEF.md-82-
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/docs/IDEA_BRIEF.md-83-## Resource Estimate
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/docs/IDEA_BRIEF.md-84-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md-39-
artifacts/dream_reports/dream_20260514T162530/best/review_report.md-40-- **S6: Multi-benchmark consistency.** Embedding mining improves both encoders on both SWE-smith and RepoBench-R. The encoder-strategy interaction (dataflow helps Qwen, neutral on StarCoder) replicates across benchmarks. This cross-benchmark stability rules out benchmark-specific artifacts.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md-41-
artifacts/dream_reports/dream_20260514T162530/best/review_report.md:42:- **S7: Pool size sensitivity analysis is thorough.** Testing at pool sizes 50, 100, 200, and 500 with 100% ranking stability and graceful delta degradation (-0.15pp per doubling) demonstrates the findings are not artifacts of unrealistically small pools. Embedding mining maintains +1.5pp at pool=500 for Qwen.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md-43-
artifacts/dream_reports/dream_20260514T162530/best/review_report.md-44-- **S8: SWE-bench Lite evaluation connects retrieval to downstream impact.** The +2.5pp embedding (p=0.018) and +3.2pp dataflow (p=0.008) resolve rate improvements, with bootstrap CIs excluding zero, add practical credibility beyond retrieval-only metrics.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md-45-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md-18-
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md-19-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md-20-
artifacts/paper_drafts/related_work_v1.md:21:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "72dfc487-bfbf-48af-840a-2f95fcbb230f"
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
  "task_id": "a1772f50001039623",
  "tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "description": "Reading artifacts/paper_drafts/related_work_v1.md",
  "usage": {
    "total_tokens": 48922,
    "tool_uses": 13,
    "duration_ms": 14263
  },
  "last_tool_name": "Read",
  "uuid": "653bf1e2-80ab-4161-8eea-7f437d361b8b",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8"
}
```

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_012QuTZqqwwwW9yxyMmAvZYh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
  "offset": 1,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "cee56b27-f8b2-47aa-8879-66ed77e5ff0c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MfctsAGNPW8bq9Bun1CSNU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 15783,
      "cache_read_input_tokens": 33079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15783,
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

_source line 47 · 2026-05-16T00:43:04.116Z_

<details><summary>↩ Tool result · `toolu_012QuTZqqwwwW9yxyMmAvZYh`</summary>

```text
1	# 2. Related Work
2	
3	## 2.1 Dense Retrieval for Code
4	
5	Code retrieval has evolved from sparse lexical methods such as BM25 \cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \cite{feng2020codebert}, UniXcoder \cite{guo2022unixcoder}, and InferCode \cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \cite{lozhkov2024starcoder2} and Qwen2.5-Coder \cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \cite{zhang2024codesage} and SCodeR \cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \cite{jimenez2024swebench}---has motivated specialized systems: SweRank \cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by systematically comparing negative mining strategies---random, embedding-distance, and structure-aware---for contrastive code retrieval, demonstrating that the choice of mining strategy meaningfully affects retrieval quality.
6	
7	## 2.2 Contrastive Learning for Code
8	
9	Sentence-BERT \cite{reimers2019sentencebert} established contrastive fine-tuning of pretrained encoders for dense text retrieval, a paradigm that has since become dominant for code representation learning. ContraCode \cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. Ding et al.\ \cite{ding2022programcontrasts} use structure-guided code transformations to synthesize contrastive pairs, demonstrating that program-structure-aware augmentation improves code clone detection and vulnerability identification. GraphCodeBERT \cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. While GraphCodeBERT uses structural edges as a pretraining objective, StructFuse addresses a complementary dimension: we systematically study how negative selection strategy---including structure-aware alternatives---affects contrastive code retrieval across encoders with distinct representation geometries.
10	
11	## 2.3 Hard Negative Mining
12	
13	The quality of negative examples critically affects contrastive learning \cite{chen2020simclr}. In dense text retrieval, DPR \cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \cite{zeng2022cldrd} and CAPSTONE \cite{he2023capstone}---schedule negative difficulty progressively during training.
14	
15	In the code domain, CoCoHaNeRe \cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search, evaluating both BM25-selected and embedding-based negatives and reporting limitations of each non-differentiable strategy. However, their claim that non-differentiable embedding negatives are ineffective has not been evaluated under controlled conditions in structural code retrieval settings, where repository-level file localization involves richer structural cues than the NL$\to$code search setting studied by CoCoHaNeRe. StructFuse addresses this gap with a systematic comparison of three mining strategies---random, embedding-distance, and dataflow-aware---across decoder-only encoders with distinct representation geometries. Our results show that static embedding-distance mining provides reliable improvement at zero additional cost, establishing it as a strong baseline that requires no gradient computation or dynamic index updates. We further incorporate data-flow structure as an additional signal dimension in the comparison, grounding hardness in inter-procedural program semantics rather than embedding proximity alone.
16	
17	## 2.4 Code Structure in Machine Learning
18	
19	Program dependence graphs \cite{ferrante1987pdg} and code property graphs \cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements. RepoFusion \cite{shrivastava2023repofusion} further demonstrates that training code models to incorporate cross-file repository context via Fusion-in-Decoder significantly improves completion quality, even outperforming much larger models that lack repository awareness.
20	
21	Recent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \cite{liu2025codexgraph} and RepoGraph \cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \cite{chen2025locagent} and RANGER \cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GRACE \cite{wang2025grace} constructs multi-level code graphs spanning repository, module, and function granularity---integrating AST, control-flow, and data-flow edges---for hierarchical retrieval-augmented code completion. GraphCoder \cite{liu2024graphcoder} and ARISE \cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, these methods primarily leverage structural graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse operates in a distinct regime: we leverage inter-procedural data-flow graphs at \emph{training time} to construct an additional strategy dimension for systematic comparison, enabling analysis of how structural signals interact with encoder representation geometry---all with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "153ae0c1-d31e-4cbe-ac17-8d9cc711ff72"
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
  "task_id": "a1772f50001039623",
  "tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 48923,
    "tool_uses": 14,
    "duration_ms": 14529
  },
  "last_tool_name": "Bash",
  "uuid": "7d9891f5-0538-46d5-a2e1-d32eeedc2af4",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8"
}
```

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_01LSFaMDvGdAJcCeXTWLNxP1`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/literature -type f 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "c0eb290d-7fbc-440f-971b-28edd984d5a2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MfctsAGNPW8bq9Bun1CSNU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 15783,
      "cache_read_input_tokens": 33079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15783,
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

_source line 50 · 2026-05-16T00:43:04.566Z_

<details><summary>↩ Tool result · `toolu_01LSFaMDvGdAJcCeXTWLNxP1`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/literature/related_work_expansion_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/literature/related_work_references.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "5dd439bf-4130-4b9b-8d77-db45948588c2"
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
  "task_id": "a1772f50001039623",
  "tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "description": "Reading artifacts/dream_reports/dream_20260514T162530/best/review_report.md",
  "usage": {
    "total_tokens": 51196,
    "tool_uses": 15,
    "duration_ms": 16661
  },
  "last_tool_name": "Read",
  "uuid": "8a15276c-f0c3-4152-b23a-84fc4db04023",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8"
}
```

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_0125PqNiBrdCu8HgDyAAqorH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "57131907-796f-4d81-800d-d6f75292c2f8",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012C7bvLEiLKfeJZJ9e9jM2Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2271,
      "cache_read_input_tokens": 48862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2271,
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

_source line 53 · 2026-05-16T00:43:06.515Z_

<details><summary>↩ Tool result · `toolu_0125PqNiBrdCu8HgDyAAqorH`</summary>

```text
1	---
2	dream_id: dream_20260514T162530
3	tier: best
4	overall_score: 4/6 Weak Accept
5	timestamp: 2026-05-14T17:10:52.369829+00:00
6	---
7	
8	---
9	dream_id: dream_20260514T162530
10	tier: best
11	reviewer: R1 (Methods and Experiments)
12	overall_score: 4/6 Weak Accept
13	timestamp: 2026-05-14
14	---
15	
16	# R1 Review: Methods and Experiments
17	
18	**Paper**: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
19	
20	---
21	
22	## 1. Summary
23	
24	This paper presents a systematic empirical comparison of four hard negative mining strategies (random, BM25, embedding-distance, dataflow-disconnected) for contrastive code retrieval, evaluated across two 3B-parameter decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with 9 random seeds each. The central findings are: (1) true embedding-distance mining consistently improves R@1 over random (+2.0pp Qwen, +1.5pp StarCoder), correcting a prior finding from CoCoHaNeRe that conflated BM25-proxy negatives with embedding-distance negatives; (2) BM25 negatives harm both encoders, empirically confirming the artifact; (3) dataflow-disconnected negatives provide conditional benefit on Qwen but not StarCoder, with a representation saturation hypothesis offered as explanation. The paper includes an extensive ablation suite (temperature, pool size, data scaling, hop depth, dynamic vs. static mining, fusion head, weighted vs. binary dataflow) and evaluates on SWE-smith validation, RepoBench-R, and SWE-bench Lite.
25	
26	---
27	
28	## 2. Strengths
29	
30	- **S1: Exemplary statistical discipline.** 54 training runs (2 encoders x 3 strategies x 9 seeds) with bootstrap 95% CIs and explicit p-values for all main comparisons is substantially above community standard. The paired bootstrap design for SWE-bench Lite (10K resamples) is appropriate for the binary outcome variable.
31	
32	- **S2: Comprehensive and purposeful ablation suite.** Each of the 8 ablations addresses a specific methodological concern or potential confound: temperature regime-specificity (Table 8), pool size artifact (Table 12), static vs. dynamic mining curriculum confound (Table 13), hop depth selection (Table 9), data scaling (Table 10), fusion head isolation (Table 11), weighted vs. binary dataflow (Table 14). This is not ablation padding -- each result answers a genuine question. The dynamic mining ablation is particularly valuable: ruling out the curriculum effect (+0.3pp, non-significant) justifies the practical recommendation to mine once from the pretrained checkpoint.
33	
34	- **S3: Clean experimental control.** The comparison holds all variables constant (data, encoder, LoRA configuration, training schedule, evaluation protocol) except the negative selection strategy. This is the correct experimental design for isolating a single factor's effect.
35	
36	- **S4: BM25 baseline closes the CoCoHaNeRe correction empirically.** Including BM25 negatives as a fourth strategy (Table 1) transforms the "correction" from an argumentative claim into an empirical demonstration. The 4-strategy ordering BM25 < random < dataflow <= embedding, with BM25 harming both encoders (-2.5pp Qwen, -2.7pp StarCoder), is the paper's most clean-cut contribution.
37	
38	- **S5: Honest conditional framing.** The paper does not overclaim dataflow benefit as universal. The conditional framing (helps Qwen, not StarCoder; helps when representations are saturated) and the stratified decomposition (true per-instance effect +2.8pp on the 34% with structural data, diluted to +1.0pp overall) demonstrate intellectual honesty. Many papers would suppress the StarCoder null or report only the pooled +1.0pp.
39	
40	- **S6: Multi-benchmark consistency.** Embedding mining improves both encoders on both SWE-smith and RepoBench-R. The encoder-strategy interaction (dataflow helps Qwen, neutral on StarCoder) replicates across benchmarks. This cross-benchmark stability rules out benchmark-specific artifacts.
41	
42	- **S7: Pool size sensitivity analysis is thorough.** Testing at pool sizes 50, 100, 200, and 500 with 100% ranking stability and graceful delta degradation (-0.15pp per doubling) demonstrates the findings are not artifacts of unrealistically small pools. Embedding mining maintains +1.5pp at pool=500 for Qwen.
43	
44	- **S8: SWE-bench Lite evaluation connects retrieval to downstream impact.** The +2.5pp embedding (p=0.018) and +3.2pp dataflow (p=0.008) resolve rate improvements, with bootstrap CIs excluding zero, add practical credibility beyond retrieval-only metrics.
45	
46	---
47	
48	## 3. Weaknesses
49	
50	### Major
51	
52	- **W1: N=2 encoders is fundamentally insufficient for the "representation saturation mediates strategy effectiveness" claim.** The mechanistic story -- that pos_sim saturation (0.986 Qwen vs. 0.799 StarCoder) determines whether dataflow negatives help -- rests on exactly two data points. These two encoders differ in pretraining data, pretraining objective (fill-in-the-middle vs. fill-in-the-middle with different ratios), tokenizer, and model family. Any of these confounds could explain the observed interaction. The paper correctly frames Claim 2 as conditional ("when encoder representations are saturated"), but the Discussion section (Section 6) presents the saturation mechanism as explanatory rather than merely correlational. With n=2, any post-hoc explanation fits. The neg_difficulty quartile analysis (Table 7b) is descriptive evidence for the saturation hypothesis but is computed on the same two encoders, not an independent validation. This is the paper's most fundamental limitation and limits the mechanistic claim to hypothesis-generating status.
53	
54	- **W2: The dataflow strategy is a mixture strategy, not a pure structural signal.** Dataflow negatives are available for only 34% of instances; the remaining 66% fall back to embedding-distance or random selection. The headline comparison in Table 1 (dataflow vs. random) therefore compares "34% structural + 66% fallback" against "100% random." The stratified analysis (Table 6) decomposes this correctly (+2.8pp on structural-available, +0.1pp on fallback), but this decomposition should be the primary presentation, not a secondary analysis. More critically, the fallback strategy for the 66% is not clearly specified -- is it embedding-distance mining or random? If the former, the "dataflow" condition actually contains a substantial embedding-distance component, making the dataflow-vs-embedding comparison in Table 1 confounded: they share 66% of the same negatives.
55	
56	- **W3: SWE-bench Lite's statistical power is marginal for the reported claims.** With 300 instances, the bootstrap CIs are ~3.6pp wide. The embedding-vs-random comparison (p=0.018) is significant but borderline; the dataflow-vs-embedding comparison (p=0.134) is not. The paper acknowledges this but then reports Table 3 (SWE-bench complexity breakdown) with sub-group analyses (N=189 single-file, N=111 multi-file) that have even less power. The multi-file dataflow advantage (+5.4pp) is presented as evidence for the dataflow mechanism, but with N=111 and no reported CI or p-value for this sub-group, this is anecdotal evidence dressed up as statistical analysis. The paper should either report CIs for each sub-group or refrain from drawing sub-group conclusions.
57	
58	- **W4: Effect sizes are small enough that uncontrolled implementation details could explain them.** The headline embedding-vs-random delta is +2.0pp (Qwen) and +1.5pp (StarCoder). These are within the range affected by hyperparameter choices not ablated: number of negatives per query (K, which is never specified in the paper), sequence length truncation, learning rate, weight decay, LoRA target modules. The data scaling ablation (Table 10) shows embedding delta growing from +1.2pp (1K) to +2.0pp (5K) -- the delta at 1K (+1.2pp) is comparable to the seed standard deviation (sigma=1.5), meaning individual seed outcomes at 1K would not be significant. The 5K result is more convincing, but the fact that the delta is still growing suggests we are observing the beginning of a trend, not its convergent value. This creates uncertainty about whether the finding is robust or still regime-dependent on data scale.
59	
60	- **W5: Checkpoint selection criterion is not specified.** The internal project history (D017) reveals that strategy rankings change depending on whether checkpoints are selected by best validation loss or best R@1. Specifically, for Qwen: by val_loss, embedding > dataflow > random; by peak R@1, dataflow > embedding > random. This is a material design choice that affects the headline claims, yet the paper does not state which criterion is used. If val_loss-selected checkpoints are reported (as seems likely from the main results ordering), the paper should acknowledge that R@1-selected checkpoints would produce different rankings and discuss why val_loss selection is preferred.
61	
62	### Minor
63	
64	- **W6: The paper claims "strategy rankings never reverse across any experimental condition tested" (Conclusion).** This is an overstatement. Table 12 shows StarCoder dataflow ranking changes from E>R>D (pool=50) to E>R~D (pool=200+). While this is not a reversal of the embedding-vs-random ordering, it represents instability in the dataflow ranking. The claim should be narrowed to "embedding > random never reverses."
65	
66	- **W7: Number of negatives per query (K) is not stated.** Section 3.1 defines the loss with K negatives but never specifies the value used. The review_context mentions pool_size=50 at training time, but it is unclear whether K=49 (all non-positive files in the pool) or some smaller K. This is a basic reproducibility gap.
67	
68	- **W8: BM25-embedding overlap of 87%.** The memory.md notes reveal that BM25 and embedding-distance negatives overlap by 87.1%. This high overlap means the BM25 harm (-2.5pp) cannot be cleanly attributed to "BM25 selects lexically similar files that destroy useful token-overlap signals" (as the paper argues). If 87% of negatives are identical, the 13% difference in negative composition is driving a 4.5pp R@1 difference, which implies those 13% of negatives have outsized influence. This deserves investigation and reporting: what characterizes the non-overlapping 13%? Are they high-lexical-overlap but low-embedding-similarity files?
69	
70	- **W9: Overfitting patterns are not reported.** Project logs show train_loss dropping to 0.04 while val_loss remains at 0.52, with best checkpoint at step 1000 out of ~4200 steps (epoch 1 midpoint). This severe overfitting (best at 25% of training) is never discussed. Strategy-specific overfitting dynamics could be informative: does dataflow overfit faster (fewer unique negatives due to 34% coverage)? Does embedding overfit slower (higher negative diversity)?
71	
72	- **W10: The paper name "StructFuse" implies a fusion architecture, but the best-performing approach uses no fusion.** Table 11 shows fusion slightly degrades performance (-0.4pp). The name is misleading for an analysis paper whose main recommendation is "use embedding-distance mining."
73	
74	- **W11: RepoBench-R pool sizes are imprecise.** "Pool ~18" and "pool ~6" are stated but the exact evaluation protocol is not described. Are these the natural candidate sets from RepoBench-R, or are they constructed to match the SWE-smith protocol?
75	
76	---
77	
78	## 4. Questions for Authors
79	
80	1. **Checkpoint criterion:** Which checkpoint selection criterion (best-val-loss vs. best-R@1) is used for all main results? Given that D017 shows these criteria produce different strategy rankings, please report results under both criteria or justify the chosen one.
81	
82	2. **Number of negatives K:** What value of K (negatives per query) is used in training? How does varying K interact with the mining strategy comparison?
83	
84	3. **Dataflow fallback strategy:** For the 66% of instances without structural data, does the dataflow condition fall back to embedding-distance mining or random sampling? If embedding-distance, then the dataflow-vs-embedding comparison in Table 1 is confounded by shared negatives on 66% of instances.
85	
86	4. **BM25-embedding overlap:** Given the 87.1% overlap between BM25 and embedding negatives reported in your analysis, how do you explain the 4.5pp performance gap? What characterizes the 13% of non-overlapping negatives that apparently drive this difference?
87	
88	5. **Learned temperature values:** The training configuration includes a learnable log_temperature parameter. Do the converged temperature values differ systematically across strategies? If so, the temperature ablation (Table 8, which fixes initial temperature) does not fully control for this confound.
89	
90	6. **Positive weighting confound:** Does the dataflow strategy use a different positive weighting scheme (e.g., pos_weight = exp(-alpha * dataflow_distance)) compared to random and embedding strategies? If so, Table 1 conflates two treatment differences (negative selection + positive weighting).
91	
92	7. **Overfitting dynamics:** Best checkpoints occur at step 1000 (~25% through training). Do different strategies exhibit different overfitting speeds? Is the strategy ranking stable across checkpoints (e.g., at step 500, 1000, 1500, 2000)?
93	
94	8. **CoCoHaNeRe evidence:** What specific textual or code-level evidence from CoCoHaNeRe supports the claim that they used BM25 as a proxy for embedding-distance? The strength of Claim 1 depends on the precision of this attribution.
95	
96	---
97	
98	## 5. Minor Issues
99	
100	- Table 10 (data scaling): Sigma is reported as a single number per data size, but it should be reported per strategy. If sigma is pooled across strategies, it obscures whether mining quality reduces seed variance (which would be informative).
101	- Table 9 (hop depth ablation): Single seed, Qwen only. The optimal hop depth could differ for StarCoder. At minimum, note this limitation.
102	- Table 11 (fusion head ablation): No CIs or p-values. Given the small deltas (-0.4pp, -6.7pp), statistical significance should be reported.
103	- The SWE-bench Lite evaluation uses only the Qwen retriever, not StarCoder. This asymmetry should be acknowledged in the Limitations section.
104	- The failure analysis (Table 15) is based on 50 instances from the random retriever only. A matched analysis comparing failure modes across strategies (which instances does dataflow rescue that embedding does not?) would be more informative.
105	- Section 3.3: "0% timeout rate" for CodeQL is stated for 5K instances / 131 repos. Clarify whether this refers to individual query timeout or total repo processing timeout.
106	- The abstract states "+2.0pp R@1 Qwen, +1.5pp StarCoder" for embedding mining, but Table 1 in the body shows these exact numbers. The abstract should reference CIs or state "statistically significant" to distinguish from noise.
107	
108	---
109	
110	## 6. Overall Assessment
111	
112	**Score: 4/6 (Weak Accept)**
113	
114	**Confidence: 4/5 (High)**
115	
116	This paper asks a genuinely important question -- what makes hard negatives work for code retrieval -- and answers it with above-average experimental rigor. The 54-run statistical design with bootstrap CIs, the 4-strategy comparison that empirically closes the CoCoHaNeRe BM25-proxy debate, the multi-benchmark consistency, and the extensive ablation suite represent careful, honest empirical work. The CoCoHaNeRe correction (Claim 1) is the paper's strongest and most useful contribution: the BM25 < random < embedding ordering, validated across two encoders and two benchmarks, is a service to the community.
117	
118	However, several issues prevent confident acceptance:
119	
120	(a) The mechanistic claim about representation saturation (Claim 2) is hypothesis-generating at best with n=2 encoders. The paper should explicitly reframe this as an observation with a testable prediction, not a validated mechanism.
121	
122	(b) The dataflow strategy's 34% coverage makes it a mixture condition whose headline effect (+1.0pp) is diluted. The stratified decomposition (+2.8pp on structural-available instances) is more honest but raises the question of practical utility: if 66% of instances receive no structural signal, the practical recommendation simplifies to "use embedding mining."
123	
124	(c) Effect sizes throughout are small (1.0-2.0pp R@1) and within the range sensitive to uncontrolled implementation details (number of negatives K, checkpoint selection criterion, learnable temperature).
125	
126	(d) Several reporting gaps -- unspecified K, unspecified checkpoint criterion, unreported overfitting dynamics, unreported learned temperatures -- create unnecessary uncertainty about the robustness of the headline numbers.
127	
128	The paper is above-average in execution quality and intellectual honesty, but the combination of small effect sizes, limited encoder diversity (n=2), and unresolved confounds places it at the accept/reject boundary. Addressing items (a) through (d) in revision -- particularly the checkpoint criterion transparency, the K specification, and explicit reframing of Claim 2 as hypothesis -- would likely push this to a 5/6.
129	
130	**What would change my score:**
131	- To 5/6: Specify checkpoint criterion and K; report results under both checkpoint criteria; explicitly reframe Claim 2 as hypothesis; add CIs to sub-group analyses.
132	- To 3/6: If the learned temperature values differ systematically across strategies (explaining the R@1 deltas as a temperature artifact rather than a mining quality effect) or if the positive weighting confound is confirmed.
133	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "52990149-e1cb-408c-978c-ffebd71f6cee"
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
  "task_id": "a1772f50001039623",
  "tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "description": "Reading artifacts/literature/related_work_expansion_report.md",
  "usage": {
    "total_tokens": 55962,
    "tool_uses": 16,
    "duration_ms": 18908
  },
  "last_tool_name": "Read",
  "uuid": "f7e79915-daa6-4ed4-8197-85568e55bc9c",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8"
}
```

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_01WAsjCumnkwMoVRbuzhxkCq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/literature/related_work_expansion_report.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "7834e793-a7fd-4e2d-bb6c-37daba1e39ee",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Cwe7eC7qb3r65A6zBNuMMG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4759,
      "cache_read_input_tokens": 51133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4759,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 56 · 2026-05-16T00:43:08.766Z_

<details><summary>↩ Tool result · `toolu_01WAsjCumnkwMoVRbuzhxkCq`</summary>

```text
1	# Related Work Expansion Report — StructFuse
2	**Date**: 2026-05-14
3	
4	## Summary
5	Literature map expanded from ~22 entries (6 needing verification) to **37 verified entries** across 7 categories. All "需验证" flags resolved. 15 new papers added, 2 existing entries corrected.
6	
7	---
8	
9	## New Papers Added (15)
10	
11	### Category 1: Code Retrieval / SWE-bench (+2)
12	
13	| Paper | Venue | Year | Relation to StructFuse |
14	|-------|-------|------|----------------------|
15	| **SweRank**: Software Issue Localization with Code Ranking | arXiv | 2025 | Text-based retrieve-and-rerank baseline for SWE-bench; direct comparison target |
16	| **SWE-Fixer**: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution | ACL Findings | 2025 | BM25 + LLM retriever pipeline; another text-based retrieval competitor |
17	
18	### Category 2: Hard Negative Mining (+1, +1 replacement)
19	
20	| Paper | Venue | Year | Relation to StructFuse |
21	|-------|-------|------|----------------------|
22	| **CoCoHaNeRe**: Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM TOSEM | 2025 | **CRITICAL**: Claim 1 correction target. See note below. |
23	| **CL-DRD**: Curriculum Learning for Dense Retrieval Distillation | SIGIR (Best Short Paper) | 2022 | Replaces the unverified "curriculum HN mining" entry |
24	
25	### Category 3: Contrastive Learning for Code (NEW category, +3)
26	
27	| Paper | Venue | Year | Relation to StructFuse |
28	|-------|-------|------|----------------------|
29	| **ContraCode**: Contrastive Code Representation Learning | EMNLP | 2021 | Self-supervised contrastive pre-training via compiler transformations |
30	| **CodeRetriever**: A Large Scale Contrastive Pre-Training Method for Code Search | EMNLP | 2022 | Unimodal + bimodal contrastive pre-training for code search |
31	| **Towards Learning (Dis)-Similarity of Source Code from Program Contrasts** | ACL Long Papers | 2022 | Moved from Cat 4; title and venue corrected |
32	
33	### Category 4: Program Analysis (+1)
34	
35	| Paper | Venue | Year | Relation to StructFuse |
36	|-------|-------|------|----------------------|
37	| **ARISE**: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv | 2025 | Intra-procedural def-use + runtime tool API; contrasts with StructFuse's inter-procedural static mining |
38	
39	### Category 5: Code Embeddings (+2)
40	
41	| Paper | Venue | Year | Relation to StructFuse |
42	|-------|-------|------|----------------------|
43	| **DeepSeek-Coder**: When the Large Language Model Meets Programming | arXiv | 2024 | Alternative code LLM backbone reference |
44	| **RepoFusion**: Training Code Models to Understand Your Repository | arXiv | 2023 | Cross-file repo context fusion for code completion |
45	
46	### Category 6: Graph-Guided Inference (NEW category, +3)
47	
48	| Paper | Venue | Year | Relation to StructFuse |
49	|-------|-------|------|----------------------|
50	| **LocAgent**: Graph-Guided LLM Agents for Code Localization | ACL | 2025 | Inference-time graph navigation; complementary to StructFuse's training-time structural signal |
51	| **CodexGraph**: Bridging LLMs and Code Repositories via Code Graph Databases | NAACL | 2025 | Graph DB interface for code retrieval at inference |
52	| **RANGER**: Repository-Level Agent for Graph-Enhanced Retrieval | arXiv | 2025 | Repo knowledge graph + MCTS exploration |
53	
54	### Category 7: Infrastructure (NEW category, +2)
55	
56	| Paper | Venue | Year | Relation to StructFuse |
57	|-------|-------|------|----------------------|
58	| **FAISS**: Billion-Scale Similarity Search with GPUs | IEEE Trans Big Data | 2021 | ANN library used for embedding-based hard negative mining |
59	| **Tree-sitter**: Incremental Parsing System | Software (Zenodo) | 2018 | Parsing tool; no formal paper, cite via Zenodo DOI |
60	
61	---
62	
63	## Verification Results
64	
65	### Previously "需验证" — Now Resolved
66	
67	| Entry | Status | Change |
68	|-------|--------|--------|
69	| SWE-smith venue | **Corrected** | arXiv → **NeurIPS 2025 D&B Spotlight** |
70	| SWE-smith authors | **Corrected** | Added Kilian Lieret, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ludwig Schmidt, Diyi Yang |
71	| RepoBench year/venue | **Confirmed** | ICLR 2024 ✓ |
72	| FA-AST authors/venue | **Confirmed** | Wenhan Wang et al., SANER 2020 ✓ |
73	| StarCoder venue | **Confirmed** | TMLR 2023 ✓ |
74	| Qwen2.5-Coder title/year | **Confirmed** | arXiv 2024 ✓ |
75	| Contrastive Learning paper | **Corrected** | Title: "Towards Learning (Dis)-Similarity of Source Code from Program Contrasts"; Venue: ACL 2022 Long Papers (not Findings) |
76	| Curriculum HN mining | **Replaced** | Was placeholder → Now: CL-DRD (Zeng et al., SIGIR 2022 Best Short Paper) |
77	
78	---
79	
80	## CoCoHaNeRe — Critical Finding
81	
82	**Full citation**: Fan Y., Li C., Ge J., Huang L., Luo B. "Effective Hard Negative Mining for Contrastive Learning-Based Code Search." ACM TOSEM, Vol 34, No 3, 2025. DOI: 10.1145/3695994.
83	
84	**Important nuance for Claim 1 framing**: CoCoHaNeRe does NOT explicitly claim that "embedding-distance hard negatives harm code search." Its argument is that using non-differentiable embedding negatives makes learning "slow and ineffective," and proposes differentiable gradient-based hard negatives as a solution. The paper's position is about the mechanism (differentiable vs. non-differentiable), not about whether embedding-distance negatives are inherently harmful.
85	
86	**Implication for StructFuse Claim 1**: The "correcting misconception" framing should be adjusted. Instead of "CoCoHaNeRe claims embedding negatives harm performance," the accurate framing is: "CoCoHaNeRe characterizes non-differentiable embedding negatives as ineffective and proposes gradient-based alternatives; we show that simple embedding-distance mining (without gradient coupling) consistently improves retrieval, challenging the premise that more complex mechanisms are necessary."
87	
88	---
89	
90	## What's NOT Included (and why)
91	
92	| Paper/Tool | Reason |
93	|------------|--------|
94	| **GRACE** (code-specific) | No well-known paper called "GRACE" for general code representation. Multiple GRACE papers exist (graph contrastive learning, vulnerability detection) but none match the intended scope. |
95	| **Aider** | Software tool, no formal paper. Can be mentioned in text as an SWE-bench method but not a citable reference. |
96	| **Moatless Tools** | Software tool by Albert Orwall. The associated paper is **SWE-Search** (Antoniades et al., ICLR 2025) — could be added if SWE-bench retrieval coverage needs strengthening. |
97	| **CoSQA** | Not searched; lower priority for this paper's scope. |
98	
99	---
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "b10f8d06-4730-4705-aadb-1be77498bc0d"
}
```

</details>

---

### System

_source line 57_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a1772f50001039623",
  "tool_use_id": "toolu_01GhwiJiH4r6bvfttg5m316F",
  "status": "completed",
  "output_file": "",
  "summary": "Find all relevant literature files",
  "usage": {
    "total_tokens": 58274,
    "tool_uses": 16,
    "duration_ms": 31773
  },
  "uuid": "b2146005-4abc-4ef6-b8cd-c3a8d4a8dd4d",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8"
}
```

---

### Tool result

_source line 58 · 2026-05-16T00:43:21.624Z_

<details><summary>↩ Tool result · `toolu_01GhwiJiH4r6bvfttg5m316F`</summary>

```text
Perfect! Now I have a comprehensive view of all the files. Let me create a summary report.

## Summary of Findings

I've completed a thorough search of the `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/` directory. Here are the results:

### **1. Files Containing "GRACE" (Case Insensitive)**

Found **3 files** with GRACE mentions:

1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md`** (Line 21)
   - Context: In section 2.4 "Code Structure in Machine Learning"
   - Snippet: "GRACE \cite{wang2025grace} constructs multi-level code graphs spanning repository, module, and function granularity---integrating AST, control-flow, and data-flow edges---for hierarchical retrieval-augmented code completion."
   - Role: Cited as an inference-time graph method that is complementary to StructFuse's training-time approach

2. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/docs/IDEA_BRIEF.md`** (Line 81)
   - Context: The mention is in an omitted long context line but references GRACE's multi-level code graphs

3. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md`** (Lines 39-44, 81 area)
   - Context: Discussion of empirical findings on pool sizes and strategy effectiveness

### **2. Literature and Related Work Files Found**

1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml`**
   - Complete literature map with 39 verified entries across 7 categories
   - Topics: Code retrieval, hard negative mining, contrastive learning, program analysis, code embeddings, graph-guided inference, infrastructure
   - Does NOT list GRACE (see rationale below)

2. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/literature/related_work_references.md`**
   - Comprehensive bibliography with 21 papers across 3 directions
   - Directions: Code retrieval negatives mining, hard negative overfitting, representation geometry/similarity saturation

3. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_supplement.md`**
   - Supplementary citations to strengthen weak areas in Related Work v1
   - Adds 6 new papers: SynCoBERT, ContraBERT, CAPSTONE, CrossCodeEval, ProGraML, CoSQA

### **3. Files in artifacts/literature/ and artifacts/paper_drafts/**

**In artifacts/literature/**:
- `related_work_expansion_report.md` - Documents expansion from ~22 to 37 verified entries, notes verification of papers, and explains GRACE exclusion
- `related_work_references.md` - Bibliography with bibtex citations

**In artifacts/paper_drafts/** (sample of 20+ files):
- `related_work_v1.md`, `related_work_supplement.md` - Main related work sections
- `abstract_v1.md`, `abstract_v2.md`
- `method_v1.md`, `introduction_v1.md`, `introduction_v2.md`
- `experiments_v1.md`, `discussion_v2.md`, `conclusion_v1.md`
- `figure_design_v1.md`, `claim2_wording_review.md`, `bm25_code_review.md`

### **4. Important Note on GRACE**

According to **`related_work_expansion_report.md` (lines 93-96)**:

> **GRACE** (code-specific) | No well-known paper called "GRACE" for general code representation. Multiple GRACE papers exist (graph contrastive learning, vulnerability detection) but none match the intended scope.

This indicates that while GRACE is cited in the paper (specifically `\cite{wang2025grace}`), it was considered but **not included in the formal literature_map.yaml** because the exact matching paper could not be verified during the literature expansion process.

### **Key Observation**

GRACE is referenced as a **2025 work by Wang** on hierarchical retrieval-augmented code completion using multi-level code graphs (AST, control-flow, data-flow edges), positioned as an **inference-time method complementary to StructFuse's training-time approach**. However, the literature expansion report suggests this paper could not be fully verified or matched to a well-known venue, indicating it may be a recent/emerging work or the citation details may need verification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "86b717e7-599b-40b3-a584-b9e9139eb806",
  "tool_use_result": {
    "status": "completed",
    "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/, find:\n1. All .md files containing \"GRACE\" or \"grace\" (case insensitive)\n2. The file literature_map.yaml\n3. The file related_work_references.md\n4. The file related_work_supplement.md\n5. Any other files in artifacts/literature/ or artifacts/paper_drafts/\n\nUse Glob and Grep to locate these. Report exact file paths and brief content snippets around GRACE mentions.",
    "agentId": "a1772f50001039623",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have a comprehensive view of all the files. Let me create a summary report.\n\n## Summary of Findings\n\nI've completed a thorough search of the `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/` directory. Here are the results:\n\n### **1. Files Containing \"GRACE\" (Case Insensitive)**\n\nFound **3 files** with GRACE mentions:\n\n1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md`** (Line 21)\n   - Context: In section 2.4 \"Code Structure in Machine Learning\"\n   - Snippet: \"GRACE \\cite{wang2025grace} constructs multi-level code graphs spanning repository, module, and function granularity---integrating AST, control-flow, and data-flow edges---for hierarchical retrieval-augmented code completion.\"\n   - Role: Cited as an inference-time graph method that is complementary to StructFuse's training-time approach\n\n2. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/docs/IDEA_BRIEF.md`** (Line 81)\n   - Context: The mention is in an omitted long context line but references GRACE's multi-level code graphs\n\n3. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md`** (Lines 39-44, 81 area)\n   - Context: Discussion of empirical findings on pool sizes and strategy effectiveness\n\n### **2. Literature and Related Work Files Found**\n\n1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml`**\n   - Complete literature map with 39 verified entries across 7 categories\n   - Topics: Code retrieval, hard negative mining, contrastive learning, program analysis, code embeddings, graph-guided inference, infrastructure\n   - Does NOT list GRACE (see rationale below)\n\n2. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/literature/related_work_references.md`**\n   - Comprehensive bibliography with 21 papers across 3 directions\n   - Directions: Code retrieval negatives mining, hard negative overfitting, representation geometry/similarity saturation\n\n3. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_supplement.md`**\n   - Supplementary citations to strengthen weak areas in Related Work v1\n   - Adds 6 new papers: SynCoBERT, ContraBERT, CAPSTONE, CrossCodeEval, ProGraML, CoSQA\n\n### **3. Files in artifacts/literature/ and artifacts/paper_drafts/**\n\n**In artifacts/literature/**:\n- `related_work_expansion_report.md` - Documents expansion from ~22 to 37 verified entries, notes verification of papers, and explains GRACE exclusion\n- `related_work_references.md` - Bibliography with bibtex citations\n\n**In artifacts/paper_drafts/** (sample of 20+ files):\n- `related_work_v1.md`, `related_work_supplement.md` - Main related work sections\n- `abstract_v1.md`, `abstract_v2.md`\n- `method_v1.md`, `introduction_v1.md`, `introduction_v2.md`\n- `experiments_v1.md`, `discussion_v2.md`, `conclusion_v1.md`\n- `figure_design_v1.md`, `claim2_wording_review.md`, `bm25_code_review.md`\n\n### **4. Important Note on GRACE**\n\nAccording to **`related_work_expansion_report.md` (lines 93-96)**:\n\n> **GRACE** (code-specific) | No well-known paper called \"GRACE\" for general code representation. Multiple GRACE papers exist (graph contrastive learning, vulnerability detection) but none match the intended scope.\n\nThis indicates that while GRACE is cited in the paper (specifically `\\cite{wang2025grace}`), it was considered but **not included in the formal literature_map.yaml** because the exact matching paper could not be verified during the literature expansion process.\n\n### **Key Observation**\n\nGRACE is referenced as a **2025 work by Wang** on hierarchical retrieval-augmented code completion using multi-level code graphs (AST, control-flow, data-flow edges), positioned as an **inference-time method complementary to StructFuse's training-time approach**. However, the literature expansion report suggests this paper could not be fully verified or matched to a well-known venue, indicating it may be a recent/emerging work or the citation details may need verification."
      }
    ],
    "totalDurationMs": 31775,
    "totalTokens": 59427,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2311,
      "cache_read_input_tokens": 55892,
      "output_tokens": 1218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2311
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 1218,
          "cache_read_input_tokens": 55892,
          "cache_creation_input_tokens": 2311,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2311,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 8,
      "searchCount": 7,
      "bashCount": 1,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015vhETFnHzrzBGEpvuUfTex`</summary>

```json
{
  "query": "select:WebSearch",
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
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "b7a8db54-5bd7-48a5-b3b9-84d5a4b3397f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DzknLLgJrL9CiASqsCYDHA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1520,
      "cache_read_input_tokens": 23679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1520
      },
      "output_tokens": 65,
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

_source line 60 · 2026-05-16T00:43:25.384Z_

<details><summary>↩ Tool result · `toolu_015vhETFnHzrzBGEpvuUfTex`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
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
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "ea1d312c-85bb-40b5-ac26-b6527fd1b2a6",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 61_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for the GRACE paper and read the relevant files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "d40a7c5d-11ff-4f86-a03b-4a06595f2292",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XWfjVaN8qiDnCMBTXZ1TG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 25199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 602
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

_source line 62_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AyKaTS7G1piJYkoDT1uU64`</summary>

```json
{
  "query": "GRACE wang2025grace code retrieval contrastive learning multi-level code graphs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "ee824d5b-29f3-4c83-a4d0-abcf70ab28be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XWfjVaN8qiDnCMBTXZ1TG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 25199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 602
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

_source line 63_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R2tnmaLyMxstbMBJW9H4dB`</summary>

```json
{
  "query": "\"GRACE\" hierarchical retrieval-augmented code completion AST control-flow data-flow 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "6a951458-c8ee-472f-b3cf-c52de4e80cb3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XWfjVaN8qiDnCMBTXZ1TG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 25199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 602
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

_source line 64_

<details open><summary>🔧 Tool call — Read · `toolu_01FkDVYFtmRa5Ak4tCMsoTcZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "1cc3f99b-122b-4397-834c-6276080f2813",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XWfjVaN8qiDnCMBTXZ1TG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 25199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 602
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

_source line 65 · 2026-05-16T00:43:30.089Z_

<details><summary>↩ Tool result · `toolu_01FkDVYFtmRa5Ak4tCMsoTcZ`</summary>

```text
1	# 2. Related Work
2	
3	## 2.1 Dense Retrieval for Code
4	
5	Code retrieval has evolved from sparse lexical methods such as BM25 \cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \cite{feng2020codebert}, UniXcoder \cite{guo2022unixcoder}, and InferCode \cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \cite{lozhkov2024starcoder2} and Qwen2.5-Coder \cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \cite{zhang2024codesage} and SCodeR \cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \cite{jimenez2024swebench}---has motivated specialized systems: SweRank \cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by systematically comparing negative mining strategies---random, embedding-distance, and structure-aware---for contrastive code retrieval, demonstrating that the choice of mining strategy meaningfully affects retrieval quality.
6	
7	## 2.2 Contrastive Learning for Code
8	
9	Sentence-BERT \cite{reimers2019sentencebert} established contrastive fine-tuning of pretrained encoders for dense text retrieval, a paradigm that has since become dominant for code representation learning. ContraCode \cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. Ding et al.\ \cite{ding2022programcontrasts} use structure-guided code transformations to synthesize contrastive pairs, demonstrating that program-structure-aware augmentation improves code clone detection and vulnerability identification. GraphCodeBERT \cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. While GraphCodeBERT uses structural edges as a pretraining objective, StructFuse addresses a complementary dimension: we systematically study how negative selection strategy---including structure-aware alternatives---affects contrastive code retrieval across encoders with distinct representation geometries.
10	
11	## 2.3 Hard Negative Mining
12	
13	The quality of negative examples critically affects contrastive learning \cite{chen2020simclr}. In dense text retrieval, DPR \cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \cite{zeng2022cldrd} and CAPSTONE \cite{he2023capstone}---schedule negative difficulty progressively during training.
14	
15	In the code domain, CoCoHaNeRe \cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search, evaluating both BM25-selected and embedding-based negatives and reporting limitations of each non-differentiable strategy. However, their claim that non-differentiable embedding negatives are ineffective has not been evaluated under controlled conditions in structural code retrieval settings, where repository-level file localization involves richer structural cues than the NL$\to$code search setting studied by CoCoHaNeRe. StructFuse addresses this gap with a systematic comparison of three mining strategies---random, embedding-distance, and dataflow-aware---across decoder-only encoders with distinct representation geometries. Our results show that static embedding-distance mining provides reliable improvement at zero additional cost, establishing it as a strong baseline that requires no gradient computation or dynamic index updates. We further incorporate data-flow structure as an additional signal dimension in the comparison, grounding hardness in inter-procedural program semantics rather than embedding proximity alone.
16	
17	## 2.4 Code Structure in Machine Learning
18	
19	Program dependence graphs \cite{ferrante1987pdg} and code property graphs \cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements. RepoFusion \cite{shrivastava2023repofusion} further demonstrates that training code models to incorporate cross-file repository context via Fusion-in-Decoder significantly improves completion quality, even outperforming much larger models that lack repository awareness.
20	
21	Recent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \cite{liu2025codexgraph} and RepoGraph \cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \cite{chen2025locagent} and RANGER \cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GRACE \cite{wang2025grace} constructs multi-level code graphs spanning repository, module, and function granularity---integrating AST, control-flow, and data-flow edges---for hierarchical retrieval-augmented code completion. GraphCoder \cite{liu2024graphcoder} and ARISE \cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, these methods primarily leverage structural graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse operates in a distinct regime: we leverage inter-procedural data-flow graphs at \emph{training time} to construct an additional strategy dimension for systematic comparison, enabling analysis of how structural signals interact with encoder representation geometry---all with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "50e12b1f-f064-41cf-a97b-aec87eb3cf60",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
      "content": "# 2. Related Work\n\n## 2.1 Dense Retrieval for Code\n\nCode retrieval has evolved from sparse lexical methods such as BM25 \\cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \\cite{feng2020codebert}, UniXcoder \\cite{guo2022unixcoder}, and InferCode \\cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \\cite{lozhkov2024starcoder2} and Qwen2.5-Coder \\cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \\cite{zhang2024codesage} and SCodeR \\cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \\cite{jimenez2024swebench}---has motivated specialized systems: SweRank \\cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \\cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by systematically comparing negative mining strategies---random, embedding-distance, and structure-aware---for contrastive code retrieval, demonstrating that the choice of mining strategy meaningfully affects retrieval quality.\n\n## 2.2 Contrastive Learning for Code\n\nSentence-BERT \\cite{reimers2019sentencebert} established contrastive fine-tuning of pretrained encoders for dense text retrieval, a paradigm that has since become dominant for code representation learning. ContraCode \\cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. Ding et al.\\ \\cite{ding2022programcontrasts} use structure-guided code transformations to synthesize contrastive pairs, demonstrating that program-structure-aware augmentation improves code clone detection and vulnerability identification. GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. While GraphCodeBERT uses structural edges as a pretraining objective, StructFuse addresses a complementary dimension: we systematically study how negative selection strategy---including structure-aware alternatives---affects contrastive code retrieval across encoders with distinct representation geometries.\n\n## 2.3 Hard Negative Mining\n\nThe quality of negative examples critically affects contrastive learning \\cite{chen2020simclr}. In dense text retrieval, DPR \\cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \\cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \\cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \\cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \\cite{zeng2022cldrd} and CAPSTONE \\cite{he2023capstone}---schedule negative difficulty progressively during training.\n\nIn the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search, evaluating both BM25-selected and embedding-based negatives and reporting limitations of each non-differentiable strategy. However, their claim that non-differentiable embedding negatives are ineffective has not been evaluated under controlled conditions in structural code retrieval settings, where repository-level file localization involves richer structural cues than the NL$\\to$code search setting studied by CoCoHaNeRe. StructFuse addresses this gap with a systematic comparison of three mining strategies---random, embedding-distance, and dataflow-aware---across decoder-only encoders with distinct representation geometries. Our results show that static embedding-distance mining provides reliable improvement at zero additional cost, establishing it as a strong baseline that requires no gradient computation or dynamic index updates. We further incorporate data-flow structure as an additional signal dimension in the comparison, grounding hardness in inter-procedural program semantics rather than embedding proximity alone.\n\n## 2.4 Code Structure in Machine Learning\n\nProgram dependence graphs \\cite{ferrante1987pdg} and code property graphs \\cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \\cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \\cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \\cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \\cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements. RepoFusion \\cite{shrivastava2023repofusion} further demonstrates that training code models to incorporate cross-file repository context via Fusion-in-Decoder significantly improves completion quality, even outperforming much larger models that lack repository awareness.\n\nRecent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GRACE \\cite{wang2025grace} constructs multi-level code graphs spanning repository, module, and function granularity---integrating AST, control-flow, and data-flow edges---for hierarchical retrieval-augmented code completion. GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, these methods primarily leverage structural graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse operates in a distinct regime: we leverage inter-procedural data-flow graphs at \\emph{training time} to construct an additional strategy dimension for systematic comparison, enabling analysis of how structural signals interact with encoder representation geometry---all with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.\n",
      "numLines": 22,
      "startLine": 1,
      "totalLines": 22
    }
  }
}
```

</details>

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Read · `toolu_011EvjTZPmrAJDKiNDEDDGCV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/literature/related_work_references.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "ab566b6b-41b9-4af8-8ce3-4b4821b27ad3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XWfjVaN8qiDnCMBTXZ1TG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 25199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 602
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

_source line 67 · 2026-05-16T00:43:30.765Z_

<details><summary>↩ Tool result · `toolu_011EvjTZPmrAJDKiNDEDDGCV`</summary>

````text
1	# StructFuse Related Work Literature Collection
2	
3	> Collected: 2026-05-16 | Total: 21 papers across 3 directions
4	
5	---
6	
7	## Direction 1: Code Retrieval 中的 Negative Mining 策略
8	
9	### 1.1 CoCoHaNeRe (direct-competitor)
10	
11	Code search framework with differentiable hard negative retrieval from a searchable memory bank. Average MRR exceeds CodeBERT/GraphCodeBERT/UniXcoder by 11.25%/8.13%/7.38%. **与 StructFuse 最直接的竞品——同样关注 code search 中 hard negative 的挖掘策略。**
12	
13	```bibtex
14	@article{fan2025cocohanere,
15	  title={Effective Hard Negative Mining for Contrastive Learning-Based Code Search},
16	  author={Fan, Ye and Li, Chao and Ge, Jing and Huang, Liang and Luo, Bin},
17	  journal={ACM Transactions on Software Engineering and Methodology},
18	  volume={34},
19	  number={3},
20	  pages={1--35},
21	  year={2025},
22	  doi={10.1145/3695994}
23	}
24	```
25	
26	### 1.2 CodeSearchNet (evaluation)
27	
28	Code search benchmark with 6M functions across 6 languages and expert relevance annotations. **StructFuse 使用的评估数据集的来源基准。**
29	
30	```bibtex
31	@article{husain2019codesearchnet,
32	  title={CodeSearchNet Challenge: Evaluating the State of Semantic Code Search},
33	  author={Husain, Hamel and Wu, Ho-Hsiang and Gazit, Tiferet and Allamanis, Miltiadis and Brockschmidt, Marc},
34	  journal={arXiv preprint arXiv:1909.09436},
35	  year={2019}
36	}
37	```
38	
39	### 1.3 CodeBERT (background)
40	
41	First bimodal pre-trained model for programming language and natural language, trained with replaced token detection. **Code retrieval 领域的基线模型。**
42	
43	```bibtex
44	@inproceedings{feng2020codebert,
45	  title={CodeBERT: A Pre-Trained Model for Programming and Natural Languages},
46	  author={Feng, Zhangyin and Guo, Daya and Tang, Duyu and Duan, Nan and Feng, Xiaocheng and Gong, Ming and Shou, Linjun and Qin, Bing and Liu, Ting and Jiang, Daxin and Zhou, Ming},
47	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020},
48	  pages={1536--1547},
49	  year={2020}
50	}
51	```
52	
53	### 1.4 GraphCodeBERT (method-component)
54	
55	First pre-trained model incorporating code structure (data flow) for code representations. Uses semantic-level structure rather than AST. **展示了结构化代码表示对检索的提升，StructFuse 的 structure-aware embedding 思路的先驱。**
56	
57	```bibtex
58	@inproceedings{guo2021graphcodebert,
59	  title={GraphCodeBERT: Pre-training Code Representations with Data Flow},
60	  author={Guo, Daya and Ren, Shuo and Lu, Shuai and Feng, Zhangyin and Tang, Duyu and Liu, Shujie and Zhou, Long and Duan, Nan and Svyatkovskiy, Alexey and Fu, Shengyu and Tufano, Michele and Deng, Shao Kun and Clement, Colin and Drain, Dawn and Sundaresan, Neel and Yin, Jian and Jiang, Daxin and Zhou, Ming},
61	  booktitle={International Conference on Learning Representations},
62	  year={2021}
63	}
64	```
65	
66	### 1.5 UniXcoder (background)
67	
68	Unified cross-modal pre-training leveraging AST and code comments via contrastive learning. **StructFuse 的 backbone encoder 之一，也展示了 AST 结构对代码表示的增益。**
69	
70	```bibtex
71	@inproceedings{guo2022unixcoder,
72	  title={UniXcoder: Unified Cross-Modal Pre-training for Code Representation},
73	  author={Guo, Daya and Lu, Shuai and Duan, Nan and Wang, Yanlin and Zhou, Ming and Yin, Jian},
74	  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
75	  pages={7212--7225},
76	  year={2022}
77	}
78	```
79	
80	### 1.6 CodeRetriever (direct-competitor)
81	
82	Large-scale contrastive pre-training with both unimodal (code-code) and bimodal (code-text) learning for code search. **与 StructFuse 类似的 contrastive learning 框架，但没有显式的 hard negative 策略。**
83	
84	```bibtex
85	@inproceedings{li2022coderetriever,
86	  title={CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search},
87	  author={Li, Xiaonan and Gong, Yeyun and Shen, Yelong and Qiu, Xipeng and Zhang, Hang and Yao, Bolun and Qi, Weizhen and Jiang, Daxin and Chen, Weizhu and Duan, Nan},
88	  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},
89	  pages={2898--2910},
90	  year={2022}
91	}
92	```
93	
94	### 1.7 CoCoSoDa (direct-competitor)
95	
96	Contrastive code search with soft data augmentation and momentum-based negative enrichment. Exceeds CodeBERT/GraphCodeBERT/UniXcoder by 13.3%/10.5%/5.9% MRR. **在 negative sample enrichment 方面与 StructFuse 互补——CoCoSoDa 用 momentum queue 增加 negative 数量，StructFuse 关注 negative difficulty。**
97	
98	```bibtex
99	@inproceedings{shi2023cocosoda,
100	  title={CoCoSoDa: Effective Contrastive Learning for Code Search},
101	  author={Shi, Ensheng and Wang, Yanlin and Gu, Wenchao and Du, Lun and Zhang, Hongyu and Han, Shi and Zhang, Dongmei and Sun, Hongbin},
102	  booktitle={2023 IEEE/ACM 45th International Conference on Software Engineering (ICSE)},
103	  pages={2198--2210},
104	  year={2023}
105	}
106	```
107	
108	---
109	
110	## Direction 2: Contrastive Learning 中 Hard Negative 的 Overfitting 问题
111	
112	### 2.1 CPC / InfoNCE (background)
113	
114	Introduces InfoNCE loss: contrastive predictive coding for unsupervised representation learning. **Contrastive learning 的基础损失函数，StructFuse 训练目标的理论根基。**
115	
116	```bibtex
117	@article{oord2018representation,
118	  title={Representation Learning with Contrastive Predictive Coding},
119	  author={van den Oord, Aaron and Li, Yazhe and Vinyals, Oriol},
120	  journal={arXiv preprint arXiv:1807.03748},
121	  year={2018}
122	}
123	```
124	
125	### 2.2 HCL (method-component)
126	
127	Develops controllable hard negative sampling for contrastive learning, showing harder negatives accelerate and improve learning. **理论上证明了 hard negative 的价值，但也暗示了过度 hard 会导致问题——StructFuse difficulty analysis 的理论起点。**
128	
129	```bibtex
130	@inproceedings{robinson2021contrastive,
131	  title={Contrastive Learning with Hard Negative Samples},
132	  author={Robinson, Joshua David and Chuang, Ching-Yao and Sra, Suvrit and Jegelka, Stefanie},
133	  booktitle={International Conference on Learning Representations},
134	  year={2021}
135	}
136	```
137	
138	### 2.3 DCL (method-component)
139	
140	Debiased contrastive objective correcting for false negatives (same-class samples treated as negatives). **False negative 是 hard negative 过拟合的重要来源之一，DCL 提供了理论框架。**
141	
142	```bibtex
143	@inproceedings{chuang2020debiased,
144	  title={Debiased Contrastive Learning},
145	  author={Chuang, Ching-Yao and Robinson, Joshua and Lin, Yen-Chen and Torralba, Antonio and Jegelka, Stefanie},
146	  booktitle={Advances in Neural Information Processing Systems},
147	  volume={33},
148	  pages={8765--8775},
149	  year={2020}
150	}
151	```
152	
153	### 2.4 MoCHi (method-component)
154	
155	Hard negative mixing at feature level with minimal overhead; shows harder negatives facilitate faster learning. **Feature-level hard negative 合成方法，与 StructFuse 的 structure-based negative mining 形成对比。**
156	
157	```bibtex
158	@inproceedings{kalantidis2020hard,
159	  title={Hard Negative Mixing for Contrastive Learning},
160	  author={Kalantidis, Yannis and Sariyildiz, Mert Bulent and Pion, No{\'e} and Weinzaepfel, Philippe and Larlus, Diane},
161	  booktitle={Advances in Neural Information Processing Systems},
162	  volume={33},
163	  pages={21798--21809},
164	  year={2020}
165	}
166	```
167	
168	### 2.5 Understanding Hard Negatives in NCE (background)
169	
170	Theoretical analysis: using model distribution as negative distribution reduces gradient bias. **为 hard negative 的作用提供了理论解释——StructFuse 的 difficulty-overfitting 分析可引用此理论框架。**
171	
172	```bibtex
173	@inproceedings{zhang2021understanding,
174	  title={Understanding Hard Negatives in Noise Contrastive Estimation},
175	  author={Zhang, Wenzheng and Stratos, Karl},
176	  booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
177	  pages={1090--1101},
178	  year={2021}
179	}
180	```
181	
182	### 2.6 ProGCL (method-component)
183	
184	Shows hard negatives in graph CL are often false negatives; proposes probability-based hardness that accounts for true/false negative distinction. **揭示了 hard negative = false negative 的陷阱，与 StructFuse 发现的 difficulty-overfitting 现象呼应。**
185	
186	```bibtex
187	@inproceedings{xia2022progcl,
188	  title={ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning},
189	  author={Xia, Jun and Wu, Lirong and Wang, Ge and Chen, Jintao and Li, Stan Z.},
190	  booktitle={Proceedings of the 39th International Conference on Machine Learning},
191	  pages={24332--24346},
192	  year={2022}
193	}
194	```
195	
196	### 2.7 WCL (method-component)
197	
198	Difficulty-based sampling exploiting a bias-amplifying encoder to find informative hard negatives while avoiding false negatives. **用 difficulty 分层采样来 debias，与 StructFuse 的 difficulty stratification 思路最接近。**
199	
200	```bibtex
201	@inproceedings{jang2023difficulty,
202	  title={Difficulty-Based Sampling for Debiased Contrastive Representation Learning},
203	  author={Jang, Taeuk and Wang, Xiaoqian},
204	  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
205	  pages={24039--24048},
206	  year={2023}
207	}
208	```
209	
210	---
211	
212	## Direction 3: Representation Geometry / Similarity Saturation
213	
214	### 3.1 SimCLR (background)
215	
216	Simple contrastive framework showing the importance of data augmentation, projection head, and batch size. **Contrastive learning 的经典方法论，StructFuse 实验设计的参考。**
217	
218	```bibtex
219	@inproceedings{chen2020simple,
220	  title={A Simple Framework for Contrastive Learning of Visual Representations},
221	  author={Chen, Ting and Kornblith, Simon and Norouzi, Mohammad and Hinton, Geoffrey},
222	  booktitle={Proceedings of the 37th International Conference on Machine Learning},
223	  pages={1597--1607},
224	  year={2020}
225	}
226	```
227	
228	### 3.2 Alignment & Uniformity (method-component)
229	
230	Identifies two key properties of contrastive loss: alignment of positive pairs and uniformity on hypersphere; proves contrastive loss optimizes both asymptotically. **StructFuse 分析 embedding space 质量的理论工具——可用 alignment/uniformity 指标量化 structure-aware embedding 的改进。**
231	
232	```bibtex
233	@inproceedings{wang2020understanding,
234	  title={Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere},
235	  author={Wang, Tongzhou and Isola, Phillip},
236	  booktitle={Proceedings of the 37th International Conference on Machine Learning},
237	  pages={9929--9939},
238	  year={2020}
239	}
240	```
241	
242	### 3.3 Representation Degeneration (background)
243	
244	Shows pre-trained LM embeddings degenerate into a narrow cone, limiting representation power; proposes regularization. **Embedding 退化的理论根源——StructFuse 观察到的 similarity saturation 可追溯到此现象。**
245	
246	```bibtex
247	@inproceedings{gao2019representation,
248	  title={Representation Degeneration Problem in Training Natural Language Generation Models},
249	  author={Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan},
250	  booktitle={International Conference on Learning Representations},
251	  year={2019}
252	}
253	```
254	
255	### 3.4 Anisotropy of Contextualized Representations (background)
256	
257	Discovers that BERT/ELMo/GPT-2 representations occupy a narrow cone (anisotropy) across all layers. **实证发现 pre-trained model 的各向异性问题，StructFuse 使用的 code encoder 继承了此问题。**
258	
259	```bibtex
260	@inproceedings{ethayarajh2019contextual,
261	  title={How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings},
262	  author={Ethayarajh, Kawin},
263	  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},
264	  pages={55--65},
265	  year={2019}
266	}
267	```
268	
269	### 3.5 BERT-flow (method-component)
270	
271	Shows BERT sentence embeddings are anisotropic; proposes normalizing flows to transform to isotropic Gaussian. **Anisotropy 矫正方法的代表，与 StructFuse 的 whitening/normalization 策略形成对比。**
272	
273	```bibtex
274	@inproceedings{li2020sentence,
275	  title={On the Sentence Embeddings from Pre-trained Language Models},
276	  author={Li, Bohan and Zhou, Hao and He, Junxian and Wang, Mingxuan and Yang, Yiming and Li, Lei},
277	  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},
278	  pages={9119--9130},
279	  year={2020}
280	}
281	```
282	
283	### 3.6 SimCSE (method-component)
284	
285	Contrastive learning regularizes anisotropic embedding space to be more uniform; uses dropout as minimal augmentation. Spectral analysis shows contrastive loss flattens singular spectrum. **直接证明 contrastive learning 改善 anisotropy——StructFuse 可引用其 uniformity 分析框架。**
286	
287	```bibtex
288	@inproceedings{gao2021simcse,
289	  title={SimCSE: Simple Contrastive Learning of Sentence Embeddings},
290	  author={Gao, Tianyu and Yao, Xingcheng and Chen, Danqi},
291	  booktitle={Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},
292	  pages={6894--6910},
293	  year={2021}
294	}
295	```
296	
297	### 3.7 Whitening for Sentence Representations (method-component)
298	
299	Whitening operation enhances isotropy and reduces dimensionality of sentence representations. **针对 anisotropy 的简洁解法，与 StructFuse 中 embedding post-processing 的讨论相关。**
300	
301	```bibtex
302	@article{su2021whitening,
303	  title={Whitening Sentence Representations for Better Semantics and Faster Retrieval},
304	  author={Su, Jianlin and Cao, Jiarun and Liu, Weijie and Ou, Yangyiwen},
305	  journal={arXiv preprint arXiv:2103.15316},
306	  year={2021}
307	}
308	```
309	
310	---
311	
312	## Summary
313	
314	| Direction | Papers | Key insight for StructFuse |
315	|-----------|--------|---------------------------|
316	| 1. Code retrieval negative mining | 7 | StructFuse fills the gap between structure-aware encoding (GraphCodeBERT) and hard negative mining (CoCoHaNeRe) by using structural similarity for difficulty-aware negative selection |
317	| 2. Hard negative overfitting | 7 | Existing work (HCL, DCL, ProGCL, WCL) shows hard negatives help but can cause overfitting/false-negative problems; StructFuse's difficulty stratification addresses this in code domain |
318	| 3. Representation geometry | 7 | Pre-trained code encoders inherit anisotropy (Ethayarajh, Gao 2019); contrastive learning improves uniformity (SimCSE, Wang & Isola) but similarity saturation in high-similarity regions remains; StructFuse's structure-aware negatives target this specific region |
319	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "b70df97c-5c5c-454e-9dc1-b3ac84864c7c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/literature/related_work_references.md",
      "content": "# StructFuse Related Work Literature Collection\n\n> Collected: 2026-05-16 | Total: 21 papers across 3 directions\n\n---\n\n## Direction 1: Code Retrieval 中的 Negative Mining 策略\n\n### 1.1 CoCoHaNeRe (direct-competitor)\n\nCode search framework with differentiable hard negative retrieval from a searchable memory bank. Average MRR exceeds CodeBERT/GraphCodeBERT/UniXcoder by 11.25%/8.13%/7.38%. **与 StructFuse 最直接的竞品——同样关注 code search 中 hard negative 的挖掘策略。**\n\n```bibtex\n@article{fan2025cocohanere,\n  title={Effective Hard Negative Mining for Contrastive Learning-Based Code Search},\n  author={Fan, Ye and Li, Chao and Ge, Jing and Huang, Liang and Luo, Bin},\n  journal={ACM Transactions on Software Engineering and Methodology},\n  volume={34},\n  number={3},\n  pages={1--35},\n  year={2025},\n  doi={10.1145/3695994}\n}\n```\n\n### 1.2 CodeSearchNet (evaluation)\n\nCode search benchmark with 6M functions across 6 languages and expert relevance annotations. **StructFuse 使用的评估数据集的来源基准。**\n\n```bibtex\n@article{husain2019codesearchnet,\n  title={CodeSearchNet Challenge: Evaluating the State of Semantic Code Search},\n  author={Husain, Hamel and Wu, Ho-Hsiang and Gazit, Tiferet and Allamanis, Miltiadis and Brockschmidt, Marc},\n  journal={arXiv preprint arXiv:1909.09436},\n  year={2019}\n}\n```\n\n### 1.3 CodeBERT (background)\n\nFirst bimodal pre-trained model for programming language and natural language, trained with replaced token detection. **Code retrieval 领域的基线模型。**\n\n```bibtex\n@inproceedings{feng2020codebert,\n  title={CodeBERT: A Pre-Trained Model for Programming and Natural Languages},\n  author={Feng, Zhangyin and Guo, Daya and Tang, Duyu and Duan, Nan and Feng, Xiaocheng and Gong, Ming and Shou, Linjun and Qin, Bing and Liu, Ting and Jiang, Daxin and Zhou, Ming},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020},\n  pages={1536--1547},\n  year={2020}\n}\n```\n\n### 1.4 GraphCodeBERT (method-component)\n\nFirst pre-trained model incorporating code structure (data flow) for code representations. Uses semantic-level structure rather than AST. **展示了结构化代码表示对检索的提升，StructFuse 的 structure-aware embedding 思路的先驱。**\n\n```bibtex\n@inproceedings{guo2021graphcodebert,\n  title={GraphCodeBERT: Pre-training Code Representations with Data Flow},\n  author={Guo, Daya and Ren, Shuo and Lu, Shuai and Feng, Zhangyin and Tang, Duyu and Liu, Shujie and Zhou, Long and Duan, Nan and Svyatkovskiy, Alexey and Fu, Shengyu and Tufano, Michele and Deng, Shao Kun and Clement, Colin and Drain, Dawn and Sundaresan, Neel and Yin, Jian and Jiang, Daxin and Zhou, Ming},\n  booktitle={International Conference on Learning Representations},\n  year={2021}\n}\n```\n\n### 1.5 UniXcoder (background)\n\nUnified cross-modal pre-training leveraging AST and code comments via contrastive learning. **StructFuse 的 backbone encoder 之一，也展示了 AST 结构对代码表示的增益。**\n\n```bibtex\n@inproceedings{guo2022unixcoder,\n  title={UniXcoder: Unified Cross-Modal Pre-training for Code Representation},\n  author={Guo, Daya and Lu, Shuai and Duan, Nan and Wang, Yanlin and Zhou, Ming and Yin, Jian},\n  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages={7212--7225},\n  year={2022}\n}\n```\n\n### 1.6 CodeRetriever (direct-competitor)\n\nLarge-scale contrastive pre-training with both unimodal (code-code) and bimodal (code-text) learning for code search. **与 StructFuse 类似的 contrastive learning 框架，但没有显式的 hard negative 策略。**\n\n```bibtex\n@inproceedings{li2022coderetriever,\n  title={CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search},\n  author={Li, Xiaonan and Gong, Yeyun and Shen, Yelong and Qiu, Xipeng and Zhang, Hang and Yao, Bolun and Qi, Weizhen and Jiang, Daxin and Chen, Weizhu and Duan, Nan},\n  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  pages={2898--2910},\n  year={2022}\n}\n```\n\n### 1.7 CoCoSoDa (direct-competitor)\n\nContrastive code search with soft data augmentation and momentum-based negative enrichment. Exceeds CodeBERT/GraphCodeBERT/UniXcoder by 13.3%/10.5%/5.9% MRR. **在 negative sample enrichment 方面与 StructFuse 互补——CoCoSoDa 用 momentum queue 增加 negative 数量，StructFuse 关注 negative difficulty。**\n\n```bibtex\n@inproceedings{shi2023cocosoda,\n  title={CoCoSoDa: Effective Contrastive Learning for Code Search},\n  author={Shi, Ensheng and Wang, Yanlin and Gu, Wenchao and Du, Lun and Zhang, Hongyu and Han, Shi and Zhang, Dongmei and Sun, Hongbin},\n  booktitle={2023 IEEE/ACM 45th International Conference on Software Engineering (ICSE)},\n  pages={2198--2210},\n  year={2023}\n}\n```\n\n---\n\n## Direction 2: Contrastive Learning 中 Hard Negative 的 Overfitting 问题\n\n### 2.1 CPC / InfoNCE (background)\n\nIntroduces InfoNCE loss: contrastive predictive coding for unsupervised representation learning. **Contrastive learning 的基础损失函数，StructFuse 训练目标的理论根基。**\n\n```bibtex\n@article{oord2018representation,\n  title={Representation Learning with Contrastive Predictive Coding},\n  author={van den Oord, Aaron and Li, Yazhe and Vinyals, Oriol},\n  journal={arXiv preprint arXiv:1807.03748},\n  year={2018}\n}\n```\n\n### 2.2 HCL (method-component)\n\nDevelops controllable hard negative sampling for contrastive learning, showing harder negatives accelerate and improve learning. **理论上证明了 hard negative 的价值，但也暗示了过度 hard 会导致问题——StructFuse difficulty analysis 的理论起点。**\n\n```bibtex\n@inproceedings{robinson2021contrastive,\n  title={Contrastive Learning with Hard Negative Samples},\n  author={Robinson, Joshua David and Chuang, Ching-Yao and Sra, Suvrit and Jegelka, Stefanie},\n  booktitle={International Conference on Learning Representations},\n  year={2021}\n}\n```\n\n### 2.3 DCL (method-component)\n\nDebiased contrastive objective correcting for false negatives (same-class samples treated as negatives). **False negative 是 hard negative 过拟合的重要来源之一，DCL 提供了理论框架。**\n\n```bibtex\n@inproceedings{chuang2020debiased,\n  title={Debiased Contrastive Learning},\n  author={Chuang, Ching-Yao and Robinson, Joshua and Lin, Yen-Chen and Torralba, Antonio and Jegelka, Stefanie},\n  booktitle={Advances in Neural Information Processing Systems},\n  volume={33},\n  pages={8765--8775},\n  year={2020}\n}\n```\n\n### 2.4 MoCHi (method-component)\n\nHard negative mixing at feature level with minimal overhead; shows harder negatives facilitate faster learning. **Feature-level hard negative 合成方法，与 StructFuse 的 structure-based negative mining 形成对比。**\n\n```bibtex\n@inproceedings{kalantidis2020hard,\n  title={Hard Negative Mixing for Contrastive Learning},\n  author={Kalantidis, Yannis and Sariyildiz, Mert Bulent and Pion, No{\\'e} and Weinzaepfel, Philippe and Larlus, Diane},\n  booktitle={Advances in Neural Information Processing Systems},\n  volume={33},\n  pages={21798--21809},\n  year={2020}\n}\n```\n\n### 2.5 Understanding Hard Negatives in NCE (background)\n\nTheoretical analysis: using model distribution as negative distribution reduces gradient bias. **为 hard negative 的作用提供了理论解释——StructFuse 的 difficulty-overfitting 分析可引用此理论框架。**\n\n```bibtex\n@inproceedings{zhang2021understanding,\n  title={Understanding Hard Negatives in Noise Contrastive Estimation},\n  author={Zhang, Wenzheng and Stratos, Karl},\n  booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},\n  pages={1090--1101},\n  year={2021}\n}\n```\n\n### 2.6 ProGCL (method-component)\n\nShows hard negatives in graph CL are often false negatives; proposes probability-based hardness that accounts for true/false negative distinction. **揭示了 hard negative = false negative 的陷阱，与 StructFuse 发现的 difficulty-overfitting 现象呼应。**\n\n```bibtex\n@inproceedings{xia2022progcl,\n  title={ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning},\n  author={Xia, Jun and Wu, Lirong and Wang, Ge and Chen, Jintao and Li, Stan Z.},\n  booktitle={Proceedings of the 39th International Conference on Machine Learning},\n  pages={24332--24346},\n  year={2022}\n}\n```\n\n### 2.7 WCL (method-component)\n\nDifficulty-based sampling exploiting a bias-amplifying encoder to find informative hard negatives while avoiding false negatives. **用 difficulty 分层采样来 debias，与 StructFuse 的 difficulty stratification 思路最接近。**\n\n```bibtex\n@inproceedings{jang2023difficulty,\n  title={Difficulty-Based Sampling for Debiased Contrastive Representation Learning},\n  author={Jang, Taeuk and Wang, Xiaoqian},\n  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},\n  pages={24039--24048},\n  year={2023}\n}\n```\n\n---\n\n## Direction 3: Representation Geometry / Similarity Saturation\n\n### 3.1 SimCLR (background)\n\nSimple contrastive framework showing the importance of data augmentation, projection head, and batch size. **Contrastive learning 的经典方法论，StructFuse 实验设计的参考。**\n\n```bibtex\n@inproceedings{chen2020simple,\n  title={A Simple Framework for Contrastive Learning of Visual Representations},\n  author={Chen, Ting and Kornblith, Simon and Norouzi, Mohammad and Hinton, Geoffrey},\n  booktitle={Proceedings of the 37th International Conference on Machine Learning},\n  pages={1597--1607},\n  year={2020}\n}\n```\n\n### 3.2 Alignment & Uniformity (method-component)\n\nIdentifies two key properties of contrastive loss: alignment of positive pairs and uniformity on hypersphere; proves contrastive loss optimizes both asymptotically. **StructFuse 分析 embedding space 质量的理论工具——可用 alignment/uniformity 指标量化 structure-aware embedding 的改进。**\n\n```bibtex\n@inproceedings{wang2020understanding,\n  title={Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere},\n  author={Wang, Tongzhou and Isola, Phillip},\n  booktitle={Proceedings of the 37th International Conference on Machine Learning},\n  pages={9929--9939},\n  year={2020}\n}\n```\n\n### 3.3 Representation Degeneration (background)\n\nShows pre-trained LM embeddings degenerate into a narrow cone, limiting representation power; proposes regularization. **Embedding 退化的理论根源——StructFuse 观察到的 similarity saturation 可追溯到此现象。**\n\n```bibtex\n@inproceedings{gao2019representation,\n  title={Representation Degeneration Problem in Training Natural Language Generation Models},\n  author={Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan},\n  booktitle={International Conference on Learning Representations},\n  year={2019}\n}\n```\n\n### 3.4 Anisotropy of Contextualized Representations (background)\n\nDiscovers that BERT/ELMo/GPT-2 representations occupy a narrow cone (anisotropy) across all layers. **实证发现 pre-trained model 的各向异性问题，StructFuse 使用的 code encoder 继承了此问题。**\n\n```bibtex\n@inproceedings{ethayarajh2019contextual,\n  title={How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings},\n  author={Ethayarajh, Kawin},\n  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n  pages={55--65},\n  year={2019}\n}\n```\n\n### 3.5 BERT-flow (method-component)\n\nShows BERT sentence embeddings are anisotropic; proposes normalizing flows to transform to isotropic Gaussian. **Anisotropy 矫正方法的代表，与 StructFuse 的 whitening/normalization 策略形成对比。**\n\n```bibtex\n@inproceedings{li2020sentence,\n  title={On the Sentence Embeddings from Pre-trained Language Models},\n  author={Li, Bohan and Zhou, Hao and He, Junxian and Wang, Mingxuan and Yang, Yiming and Li, Lei},\n  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n  pages={9119--9130},\n  year={2020}\n}\n```\n\n### 3.6 SimCSE (method-component)\n\nContrastive learning regularizes anisotropic embedding space to be more uniform; uses dropout as minimal augmentation. Spectral analysis shows contrastive loss flattens singular spectrum. **直接证明 contrastive learning 改善 anisotropy——StructFuse 可引用其 uniformity 分析框架。**\n\n```bibtex\n@inproceedings{gao2021simcse,\n  title={SimCSE: Simple Contrastive Learning of Sentence Embeddings},\n  author={Gao, Tianyu and Yao, Xingcheng and Chen, Danqi},\n  booktitle={Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},\n  pages={6894--6910},\n  year={2021}\n}\n```\n\n### 3.7 Whitening for Sentence Representations (method-component)\n\nWhitening operation enhances isotropy and reduces dimensionality of sentence representations. **针对 anisotropy 的简洁解法，与 StructFuse 中 embedding post-processing 的讨论相关。**\n\n```bibtex\n@article{su2021whitening,\n  title={Whitening Sentence Representations for Better Semantics and Faster Retrieval},\n  author={Su, Jianlin and Cao, Jiarun and Liu, Weijie and Ou, Yangyiwen},\n  journal={arXiv preprint arXiv:2103.15316},\n  year={2021}\n}\n```\n\n---\n\n## Summary\n\n| Direction | Papers | Key insight for StructFuse |\n|-----------|--------|---------------------------|\n| 1. Code retrieval negative mining | 7 | StructFuse fills the gap between structure-aware encoding (GraphCodeBERT) and hard negative mining (CoCoHaNeRe) by using structural similarity for difficulty-aware negative selection |\n| 2. Hard negative overfitting | 7 | Existing work (HCL, DCL, ProGCL, WCL) shows hard negatives help but can cause overfitting/false-negative problems; StructFuse's difficulty stratification addresses this in code domain |\n| 3. Representation geometry | 7 | Pre-trained code encoders inherit anisotropy (Ethayarajh, Gao 2019); contrastive learning improves uniformity (SimCSE, Wang & Isola) but similarity saturation in high-similarity regions remains; StructFuse's structure-aware negatives target this specific region |\n",
      "numLines": 319,
      "startLine": 1,
      "totalLines": 319
    }
  }
}
````

</details>

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Read · `toolu_01GVQFvvyiRLyc1TMdi57dp9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_supplement.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "5a922c2d-d477-4877-960c-d4febb31f10c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XWfjVaN8qiDnCMBTXZ1TG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 25199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 602
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

_source line 69 · 2026-05-16T00:43:31.527Z_

<details><summary>↩ Tool result · `toolu_01GVQFvvyiRLyc1TMdi57dp9`</summary>

```text
1	# Related Work Supplement: Contrastive Learning for Code & Adjacent Areas
2	
3	> **Purpose**: Supplementary paragraphs and citations to strengthen weak areas in Related Work v1.
4	> Six new papers added; RocketQA already cited in v1.
5	> Generated: 2026-05-15
6	
7	---
8	
9	## Supplement A: Contrastive Learning for Code (insert into Section 2.2, after the ContraCode/CodeRetriever paragraph)
10	
11	Beyond learning invariance to syntactic variation, contrastive pre-training has been applied to inject structural and robustness priors into code representations. SynCoBERT \cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pre-training that aligns code, natural language, and abstract syntax tree (AST) modalities through identifier prediction and AST edge prediction objectives, demonstrating that explicitly encoding syntactic structure during contrastive pre-training improves downstream code intelligence tasks. ContraBERT \cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing nine data augmentation operators that generate adversarial code and comment variants---including identifier renaming, dead code insertion, and operand swapping---and further trains existing code models with contrastive objectives on these augmented pairs. ContraBERT shows that contrastive pre-training with targeted perturbations substantially improves model robustness against adversarial attacks while maintaining strong performance on standard benchmarks. These methods enrich the positive pair construction space for code contrastive learning, yet they focus on augmenting the pre-training signal rather than improving the selection of negative examples during fine-tuning. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, it improves which negatives the model trains against by grounding negative selection in inter-procedural data-flow structure.
12	
13	## Supplement B: Hard Negative Mining in Dense Retrieval (insert into Section 2.3, after the CL-DRD sentence)
14	
15	The curriculum learning paradigm for negative sampling has been further developed by CAPSTONE \cite{he2023capstone}, which addresses the training-inference discrepancy in dual-encoder dense retrieval. CAPSTONE expands documents with pseudo-queries during training and employs a curriculum sampling strategy that progressively improves the relevance between generated and real queries, effectively controlling negative difficulty through the query generation quality. This approach achieves strong results on both in-domain and out-of-domain retrieval benchmarks, reinforcing the finding that curriculum-based difficulty scheduling benefits dense retrieval training. While CAPSTONE focuses on bridging the training-inference gap through document expansion, our structure-grounded negatives provide an orthogonal form of curriculum: negatives that are hard because they share data-flow context with the positive, not because of embedding proximity alone.
16	
17	## Supplement C: Cross-File Code Understanding and Evaluation (insert into Section 2.4, before the closing paragraph, or as a new subsection bridge)
18	
19	The importance of cross-file context for code understanding has been empirically validated by dedicated benchmarks. CrossCodeEval \cite{ding2023crosscodeeval} constructs a diverse, multilingual benchmark for cross-file code completion across Python, Java, TypeScript, and C\#, using static analysis to identify completion targets that strictly require cross-file dependencies. Experiments show that even state-of-the-art code LLMs struggle without cross-file context, and that retrieval-augmented approaches yield clear improvements---yet performance remains far below the ceiling, indicating substantial room for better cross-file retrieval. ProGraML \cite{cummins2021programl} provides a language-independent, graph-based program representation that captures control-flow, data-flow, and call relations across entire programs, achieving strong results on data-flow analysis tasks. ProGraML demonstrates that whole-program structural representations are learnable and informative, providing conceptual grounding for StructFuse's use of inter-procedural data-flow graphs as a training signal. CoSQA \cite{huang2021cosqa} contributes a large-scale dataset of 20,000+ real web queries paired with Python code, bridging the gap between synthetic code search benchmarks and real-world developer information needs; it also introduces a contrastive learning method (CoCLR) for data augmentation in code search training. Together, these resources underscore that cross-file structural dependencies and realistic query distributions are critical dimensions for advancing code retrieval---precisely the dimensions that StructFuse's structure-grounded training targets.
20	
21	---
22	
23	## Summary of New Citations
24	
25	| Paper | Venue | Year | Area | Relation to StructFuse |
26	|-------|-------|------|------|----------------------|
27	| SynCoBERT | arXiv | 2021 | Contrastive code pre-training | Syntax-guided contrastive pre-training; StructFuse uses structure for negatives, not positives |
28	| ContraBERT | ICSE | 2023 | Contrastive code pre-training | Robustness-oriented augmentation; complementary to StructFuse's negative mining |
29	| CAPSTONE | EMNLP | 2023 | Dense retrieval | Curriculum sampling for retrieval; StructFuse provides structure-based curriculum |
30	| CrossCodeEval | NeurIPS | 2023 | Benchmark | Validates importance of cross-file context for code tasks |
31	| ProGraML | ICML | 2021 | Program graphs for ML | Whole-program graph representation; conceptual grounding for StructFuse's data-flow use |
32	| CoSQA | ACL | 2021 | Code search dataset | Real-world query benchmark with contrastive learning augmentation |
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "aa79882e-8968-4885-bc64-174ea3483717",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_supplement.md",
      "content": "# Related Work Supplement: Contrastive Learning for Code & Adjacent Areas\n\n> **Purpose**: Supplementary paragraphs and citations to strengthen weak areas in Related Work v1.\n> Six new papers added; RocketQA already cited in v1.\n> Generated: 2026-05-15\n\n---\n\n## Supplement A: Contrastive Learning for Code (insert into Section 2.2, after the ContraCode/CodeRetriever paragraph)\n\nBeyond learning invariance to syntactic variation, contrastive pre-training has been applied to inject structural and robustness priors into code representations. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pre-training that aligns code, natural language, and abstract syntax tree (AST) modalities through identifier prediction and AST edge prediction objectives, demonstrating that explicitly encoding syntactic structure during contrastive pre-training improves downstream code intelligence tasks. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing nine data augmentation operators that generate adversarial code and comment variants---including identifier renaming, dead code insertion, and operand swapping---and further trains existing code models with contrastive objectives on these augmented pairs. ContraBERT shows that contrastive pre-training with targeted perturbations substantially improves model robustness against adversarial attacks while maintaining strong performance on standard benchmarks. These methods enrich the positive pair construction space for code contrastive learning, yet they focus on augmenting the pre-training signal rather than improving the selection of negative examples during fine-tuning. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, it improves which negatives the model trains against by grounding negative selection in inter-procedural data-flow structure.\n\n## Supplement B: Hard Negative Mining in Dense Retrieval (insert into Section 2.3, after the CL-DRD sentence)\n\nThe curriculum learning paradigm for negative sampling has been further developed by CAPSTONE \\cite{he2023capstone}, which addresses the training-inference discrepancy in dual-encoder dense retrieval. CAPSTONE expands documents with pseudo-queries during training and employs a curriculum sampling strategy that progressively improves the relevance between generated and real queries, effectively controlling negative difficulty through the query generation quality. This approach achieves strong results on both in-domain and out-of-domain retrieval benchmarks, reinforcing the finding that curriculum-based difficulty scheduling benefits dense retrieval training. While CAPSTONE focuses on bridging the training-inference gap through document expansion, our structure-grounded negatives provide an orthogonal form of curriculum: negatives that are hard because they share data-flow context with the positive, not because of embedding proximity alone.\n\n## Supplement C: Cross-File Code Understanding and Evaluation (insert into Section 2.4, before the closing paragraph, or as a new subsection bridge)\n\nThe importance of cross-file context for code understanding has been empirically validated by dedicated benchmarks. CrossCodeEval \\cite{ding2023crosscodeeval} constructs a diverse, multilingual benchmark for cross-file code completion across Python, Java, TypeScript, and C\\#, using static analysis to identify completion targets that strictly require cross-file dependencies. Experiments show that even state-of-the-art code LLMs struggle without cross-file context, and that retrieval-augmented approaches yield clear improvements---yet performance remains far below the ceiling, indicating substantial room for better cross-file retrieval. ProGraML \\cite{cummins2021programl} provides a language-independent, graph-based program representation that captures control-flow, data-flow, and call relations across entire programs, achieving strong results on data-flow analysis tasks. ProGraML demonstrates that whole-program structural representations are learnable and informative, providing conceptual grounding for StructFuse's use of inter-procedural data-flow graphs as a training signal. CoSQA \\cite{huang2021cosqa} contributes a large-scale dataset of 20,000+ real web queries paired with Python code, bridging the gap between synthetic code search benchmarks and real-world developer information needs; it also introduces a contrastive learning method (CoCLR) for data augmentation in code search training. Together, these resources underscore that cross-file structural dependencies and realistic query distributions are critical dimensions for advancing code retrieval---precisely the dimensions that StructFuse's structure-grounded training targets.\n\n---\n\n## Summary of New Citations\n\n| Paper | Venue | Year | Area | Relation to StructFuse |\n|-------|-------|------|------|----------------------|\n| SynCoBERT | arXiv | 2021 | Contrastive code pre-training | Syntax-guided contrastive pre-training; StructFuse uses structure for negatives, not positives |\n| ContraBERT | ICSE | 2023 | Contrastive code pre-training | Robustness-oriented augmentation; complementary to StructFuse's negative mining |\n| CAPSTONE | EMNLP | 2023 | Dense retrieval | Curriculum sampling for retrieval; StructFuse provides structure-based curriculum |\n| CrossCodeEval | NeurIPS | 2023 | Benchmark | Validates importance of cross-file context for code tasks |\n| ProGraML | ICML | 2021 | Program graphs for ML | Whole-program graph representation; conceptual grounding for StructFuse's data-flow use |\n| CoSQA | ACL | 2021 | Code search dataset | Real-world query benchmark with contrastive learning augmentation |\n",
      "numLines": 33,
      "startLine": 1,
      "totalLines": 33
    }
  }
}
```

</details>

---

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — Read · `toolu_01SAeZkhd3v3RQaVrxESxoa4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "49590ac9-22d0-414e-b541-e8237570a14f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XWfjVaN8qiDnCMBTXZ1TG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 25199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 602
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

_source line 71 · 2026-05-16T00:43:31.647Z_

<details><summary>↩ Tool result · `toolu_01SAeZkhd3v3RQaVrxESxoa4`</summary>

```text
1	# StructFuse — Related Work Literature Map
2	# 最后更新: 2026-05-14
3	# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。
4	# 总计: 39 entries (含 2 个软件工具引用)
5	
6	categories:
7	
8	  # ==========================================================================
9	  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem
10	  # ==========================================================================
11	  code_retrieval_bug_fixing:
12	    description: "SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法"
13	    papers:
14	
15	      - title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
16	        authors: "Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan"
17	        venue: ICLR
18	        year: 2024
19	        relation: baseline
20	        summary: "从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。"
21	
22	      - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
23	        authors: "John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press"
24	        venue: NeurIPS
25	        year: 2024
26	        relation: competitor
27	        summary: "基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。"
28	
29	      - title: "AutoCodeRover: Autonomous Program Improvement"
30	        authors: "Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury"
31	        venue: ISSTA
32	        year: 2024
33	        relation: competitor
34	        summary: "结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。"
35	
36	      - title: "Agentless: Demystifying LLM-based Software Engineering Agents"
37	        authors: "Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang"
38	        venue: arXiv
39	        year: 2024
40	        relation: competitor
41	        summary: "无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。"
42	
43	      - title: "SWE-smith: Scaling Data for Software Engineering Agents"
44	        authors: "John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang"
45	        venue: "NeurIPS (Datasets & Benchmarks, Spotlight)"
46	        year: 2025
47	        relation: building-block
48	        summary: "自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。"
49	
50	      - title: "RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems"
51	        authors: "Tianyang Liu, Canwen Xu, Julian McAuley"
52	        venue: ICLR
53	        year: 2024
54	        relation: baseline
55	        summary: "Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。"
56	
57	      - title: "SweRank: Software Issue Localization with Code Ranking"
58	        authors: "Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty"
59	        venue: arXiv
60	        year: 2025
61	        relation: competitor
62	        summary: "Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。"
63	
64	      - title: "SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution"
65	        authors: "Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen"
66	        venue: "ACL (Findings)"
67	        year: 2025
68	        relation: competitor
69	        summary: "BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。"
70	
71	  # ==========================================================================
72	  # Category 2: Hard Negative Mining in Contrastive Learning
73	  # ==========================================================================
74	  hard_negative_mining:
75	    description: "对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择"
76	    papers:
77	
78	      - title: "Dense Passage Retrieval for Open-Domain Question Answering"
79	        authors: "Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih"
80	        venue: EMNLP
81	        year: 2020
82	        relation: background
83	        summary: "DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。"
84	
85	      - title: "Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval"
86	        authors: "Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk"
87	        venue: ICLR
88	        year: 2021
89	        relation: background
90	        summary: "ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。"
91	
92	      - title: "A Simple Framework for Contrastive Learning of Visual Representations"
93	        authors: "Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton"
94	        venue: ICML
95	        year: 2020
96	        relation: background
97	        summary: "SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。"
98	
99	      - title: "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks"
100	        authors: "Nils Reimers, Iryna Gurevych"
101	        venue: EMNLP
102	        year: 2019
103	        relation: background
104	        summary: "Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。"
105	
106	      - title: "Curriculum Learning for Dense Retrieval Distillation"
107	        authors: "Hansi Zeng, Hamed Zamani, Vishwa Vinay"
108	        venue: "SIGIR (Best Short Paper)"
109	        year: 2022
110	        relation: background
111	        summary: "CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。"
112	
113	      - title: "Effective Hard Negative Mining for Contrastive Learning-Based Code Search"
114	        authors: "Fan Y., Li C., Ge J., Huang L., Luo B."
115	        venue: "ACM TOSEM"
116	        year: 2025
117	        relation: contrast-target
118	        summary: "CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。"
119	        note: "关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。"
120	
121	  # ==========================================================================
122	  # Category 3: Contrastive Learning for Code
123	  # ==========================================================================
124	  contrastive_code_learning:
125	    description: "代码领域的对比学习方法，训练时利用代码特性构建正负样本"
126	    papers:
127	
128	      - title: "Contrastive Code Representation Learning"
129	        authors: "Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica"
130	        venue: EMNLP
131	        year: 2021
132	        relation: background
133	        summary: "ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。"
134	
135	      - title: "CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search"
136	        authors: "Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan"
137	        venue: EMNLP
138	        year: 2022
139	        relation: background
140	        summary: "结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。"
141	
142	      - title: "Towards Learning (Dis)-Similarity of Source Code from Program Contrasts"
143	        authors: "Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty"
144	        venue: "ACL (Long Papers)"
145	        year: 2022
146	        relation: background
147	        summary: "利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。"
148	
149	  # ==========================================================================
150	  # Category 4: Program Analysis for ML
151	  # ==========================================================================
152	  program_analysis_for_ml:
153	    description: "静态分析辅助 ML，结构信息在代码表示学习中的应用"
154	    papers:
155	
156	      - title: "CodeQL: Semantic Code Analysis Engine"
157	        authors: "GitHub / Semmle"
158	        venue: "Tool (open-source)"
159	        year: 2019
160	        relation: building-block
161	        summary: "基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。"
162	
163	      - title: "code2vec: Learning Distributed Representations of Code"
164	        authors: "Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav"
165	        venue: POPL
166	        year: 2019
167	        relation: background
168	        summary: "用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。"
169	
170	      - title: "code2seq: Generating Sequences from Structured Representations of Code"
171	        authors: "Uri Alon, Shaked Brody, Omer Levy, Eran Yahav"
172	        venue: ICLR
173	        year: 2019
174	        relation: background
175	        summary: "code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。"
176	
177	      - title: "Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree"
178	        authors: "Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin"
179	        venue: SANER
180	        year: 2020
181	        relation: background
182	        summary: "FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。"
183	
184	      - title: "GraphCodeBERT: Pre-training Code Representations with Data Flow"
185	        authors: "Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou"
186	        venue: ICLR
187	        year: 2021
188	        relation: background
189	        summary: "在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。"
190	
191	      - title: "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair"
192	        authors: "Shahd Seddik, Fatemeh Fard"
193	        venue: arXiv
194	        year: 2026
195	        relation: contrast
196	        summary: "用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。"
197	
198	  # ==========================================================================
199	  # Category 5: Code Embeddings / Code Search
200	  # ==========================================================================
201	  code_embeddings_search:
202	    description: "代码嵌入模型和代码搜索方法"
203	    papers:
204	
205	      - title: "CodeSearchNet Challenge: Evaluating the State of Semantic Code Search"
206	        authors: "Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt"
207	        venue: arXiv
208	        year: 2019
209	        relation: background
210	        summary: "代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。"
211	
212	      - title: "CodeBERT: A Pre-Trained Model for Programming and Natural Languages"
213	        authors: "Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou"
214	        venue: "EMNLP (Findings)"
215	        year: 2020
216	        relation: background
217	        summary: "首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。"
218	
219	      - title: "UniXcoder: Unified Cross-Modal Pre-training for Code Representation"
220	        authors: "Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin"
221	        venue: ACL
222	        year: 2022
223	        relation: background
224	        summary: "统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。"
225	
226	      - title: "StarCoder: May the Source Be with You!"
227	        authors: "Raymond Li, Loubna Ben Allal, et al. (BigCode)"
228	        venue: TMLR
229	        year: 2023
230	        relation: building-block
231	        summary: "大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。"
232	
233	      - title: "Code Llama: Open Foundation Models for Code"
234	        authors: "Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)"
235	        venue: arXiv
236	        year: 2023
237	        relation: background
238	        summary: "Meta 的代码大模型系列，基于 Llama 2 微调。"
239	
240	      - title: "Qwen2.5-Coder Technical Report"
241	        authors: "Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)"
242	        venue: arXiv
243	        year: 2024
244	        relation: building-block
245	        summary: "Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。"
246	
247	      - title: "DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence"
248	        authors: "Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang"
249	        venue: arXiv
250	        year: 2024
251	        relation: background
252	        summary: "开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。"
253	
254	      - title: "RepoFusion: Training Code Models to Understand Your Repository"
255	        authors: "Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak"
256	        venue: arXiv
257	        year: 2023
258	        relation: background
259	        summary: "训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。"
260	
261	      - title: "BM25"
262	        authors: "Stephen Robertson, Hugo Zaragoza"
263	        venue: "Foundations and Trends in Information Retrieval"
264	        year: 2009
265	        relation: baseline
266	        summary: "经典稀疏检索方法，StructFuse 的 baseline 之一。"
267	
268	  # ==========================================================================
269	  # Category 6: Graph-Guided Code Navigation (Inference-Time)
270	  # ==========================================================================
271	  graph_guided_inference:
272	    description: "推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）"
273	    papers:
274	
275	      - title: "LocAgent: Graph-Guided LLM Agents for Code Localization"
276	        authors: "Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang"
277	        venue: ACL
278	        year: 2025
279	        relation: contrast
280	        summary: "将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。"
281	
282	      - title: "CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases"
283	        authors: "Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou"
284	        venue: NAACL
285	        year: 2025
286	        relation: contrast
287	        summary: "将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。"
288	
289	      - title: "RANGER: Repository-Level Agent for Graph-Enhanced Retrieval"
290	        authors: "Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta"
291	        venue: arXiv
292	        year: 2025
293	        relation: contrast
294	        summary: "构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。"
295	
296	      - title: "RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph"
297	        authors: "Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu"
298	        venue: ICLR
299	        year: 2025
300	        relation: contrast
301	        summary: "以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。"
302	
303	      - title: "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph"
304	        authors: "Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang"
305	        venue: ASE
306	        year: 2024
307	        relation: contrast
308	        summary: "构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。"
309	
310	  # ==========================================================================
311	  # Category 7: Infrastructure / Tools
312	  # ==========================================================================
313	  infrastructure:
314	    description: "StructFuse 依赖的核心基础设施和工具"
315	    papers:
316	
317	      - title: "Billion-Scale Similarity Search with GPUs"
318	        authors: "Jeff Johnson, Matthijs Douze, Herve Jegou"
319	        venue: "IEEE Transactions on Big Data"
320	        year: 2021
321	        relation: building-block
322	        summary: "FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。"
323	
324	      - title: "Tree-sitter: An Incremental Parsing System for Programming Tools"
325	        authors: "Max Brunsfeld et al."
326	        venue: "Software (Zenodo DOI: 10.5281/zenodo.13375512)"
327	        year: 2018
328	        relation: building-block
329	        summary: "增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。"
330	        note: "软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。"
331	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "d2484493-4808-4cef-965e-7326cf9f9661",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
      "content": "# StructFuse — Related Work Literature Map\n# 最后更新: 2026-05-14\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\n# 总计: 39 entries (含 2 个软件工具引用)\n\ncategories:\n\n  # ==========================================================================\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\n  # ==========================================================================\n  code_retrieval_bug_fixing:\n    description: \"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\"\n    papers:\n\n      - title: \"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\"\n        authors: \"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\"\n        venue: ICLR\n        year: 2024\n        relation: baseline\n        summary: \"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\"\n\n      - title: \"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\"\n        authors: \"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\"\n        venue: NeurIPS\n        year: 2024\n        relation: competitor\n        summary: \"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\"\n\n      - title: \"AutoCodeRover: Autonomous Program Improvement\"\n        authors: \"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\"\n        venue: ISSTA\n        year: 2024\n        relation: competitor\n        summary: \"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\"\n\n      - title: \"Agentless: Demystifying LLM-based Software Engineering Agents\"\n        authors: \"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\"\n        venue: arXiv\n        year: 2024\n        relation: competitor\n        summary: \"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\"\n\n      - title: \"SWE-smith: Scaling Data for Software Engineering Agents\"\n        authors: \"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\"\n        venue: \"NeurIPS (Datasets & Benchmarks, Spotlight)\"\n        year: 2025\n        relation: building-block\n        summary: \"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\"\n\n      - title: \"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\"\n        authors: \"Tianyang Liu, Canwen Xu, Julian McAuley\"\n        venue: ICLR\n        year: 2024\n        relation: baseline\n        summary: \"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\"\n\n      - title: \"SweRank: Software Issue Localization with Code Ranking\"\n        authors: \"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\"\n        venue: arXiv\n        year: 2025\n        relation: competitor\n        summary: \"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\"\n\n      - title: \"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\"\n        authors: \"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\"\n        venue: \"ACL (Findings)\"\n        year: 2025\n        relation: competitor\n        summary: \"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\"\n\n  # ==========================================================================\n  # Category 2: Hard Negative Mining in Contrastive Learning\n  # ==========================================================================\n  hard_negative_mining:\n    description: \"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\"\n    papers:\n\n      - title: \"Dense Passage Retrieval for Open-Domain Question Answering\"\n        authors: \"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\"\n        venue: EMNLP\n        year: 2020\n        relation: background\n        summary: \"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\"\n\n      - title: \"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\"\n        authors: \"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\"\n        venue: ICLR\n        year: 2021\n        relation: background\n        summary: \"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\"\n\n      - title: \"A Simple Framework for Contrastive Learning of Visual Representations\"\n        authors: \"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\"\n        venue: ICML\n        year: 2020\n        relation: background\n        summary: \"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\"\n\n      - title: \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\"\n        authors: \"Nils Reimers, Iryna Gurevych\"\n        venue: EMNLP\n        year: 2019\n        relation: background\n        summary: \"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\"\n\n      - title: \"Curriculum Learning for Dense Retrieval Distillation\"\n        authors: \"Hansi Zeng, Hamed Zamani, Vishwa Vinay\"\n        venue: \"SIGIR (Best Short Paper)\"\n        year: 2022\n        relation: background\n        summary: \"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\"\n\n      - title: \"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\"\n        authors: \"Fan Y., Li C., Ge J., Huang L., Luo B.\"\n        venue: \"ACM TOSEM\"\n        year: 2025\n        relation: contrast-target\n        summary: \"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\"\n        note: \"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\"\n\n  # ==========================================================================\n  # Category 3: Contrastive Learning for Code\n  # ==========================================================================\n  contrastive_code_learning:\n    description: \"代码领域的对比学习方法，训练时利用代码特性构建正负样本\"\n    papers:\n\n      - title: \"Contrastive Code Representation Learning\"\n        authors: \"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\"\n        venue: EMNLP\n        year: 2021\n        relation: background\n        summary: \"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\"\n\n      - title: \"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\"\n        authors: \"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\"\n        venue: EMNLP\n        year: 2022\n        relation: background\n        summary: \"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\"\n\n      - title: \"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\"\n        authors: \"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\"\n        venue: \"ACL (Long Papers)\"\n        year: 2022\n        relation: background\n        summary: \"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\"\n\n  # ==========================================================================\n  # Category 4: Program Analysis for ML\n  # ==========================================================================\n  program_analysis_for_ml:\n    description: \"静态分析辅助 ML，结构信息在代码表示学习中的应用\"\n    papers:\n\n      - title: \"CodeQL: Semantic Code Analysis Engine\"\n        authors: \"GitHub / Semmle\"\n        venue: \"Tool (open-source)\"\n        year: 2019\n        relation: building-block\n        summary: \"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\"\n\n      - title: \"code2vec: Learning Distributed Representations of Code\"\n        authors: \"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\"\n        venue: POPL\n        year: 2019\n        relation: background\n        summary: \"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\"\n\n      - title: \"code2seq: Generating Sequences from Structured Representations of Code\"\n        authors: \"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\"\n        venue: ICLR\n        year: 2019\n        relation: background\n        summary: \"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\"\n\n      - title: \"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\"\n        authors: \"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\"\n        venue: SANER\n        year: 2020\n        relation: background\n        summary: \"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\"\n\n      - title: \"GraphCodeBERT: Pre-training Code Representations with Data Flow\"\n        authors: \"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\"\n        venue: ICLR\n        year: 2021\n        relation: background\n        summary: \"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\"\n\n      - title: \"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\"\n        authors: \"Shahd Seddik, Fatemeh Fard\"\n        venue: arXiv\n        year: 2026\n        relation: contrast\n        summary: \"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\"\n\n  # ==========================================================================\n  # Category 5: Code Embeddings / Code Search\n  # ==========================================================================\n  code_embeddings_search:\n    description: \"代码嵌入模型和代码搜索方法\"\n    papers:\n\n      - title: \"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\"\n        authors: \"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\"\n        venue: arXiv\n        year: 2019\n        relation: background\n        summary: \"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\"\n\n      - title: \"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\"\n        authors: \"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\"\n        venue: \"EMNLP (Findings)\"\n        year: 2020\n        relation: background\n        summary: \"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\"\n\n      - title: \"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\"\n        authors: \"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\"\n        venue: ACL\n        year: 2022\n        relation: background\n        summary: \"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\"\n\n      - title: \"StarCoder: May the Source Be with You!\"\n        authors: \"Raymond Li, Loubna Ben Allal, et al. (BigCode)\"\n        venue: TMLR\n        year: 2023\n        relation: building-block\n        summary: \"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\"\n\n      - title: \"Code Llama: Open Foundation Models for Code\"\n        authors: \"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\"\n        venue: arXiv\n        year: 2023\n        relation: background\n        summary: \"Meta 的代码大模型系列，基于 Llama 2 微调。\"\n\n      - title: \"Qwen2.5-Coder Technical Report\"\n        authors: \"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\"\n        venue: arXiv\n        year: 2024\n        relation: building-block\n        summary: \"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\"\n\n      - title: \"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\"\n        authors: \"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\"\n        venue: arXiv\n        year: 2024\n        relation: background\n        summary: \"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\"\n\n      - title: \"RepoFusion: Training Code Models to Understand Your Repository\"\n        authors: \"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\"\n        venue: arXiv\n        year: 2023\n        relation: background\n        summary: \"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\"\n\n      - title: \"BM25\"\n        authors: \"Stephen Robertson, Hugo Zaragoza\"\n        venue: \"Foundations and Trends in Information Retrieval\"\n        year: 2009\n        relation: baseline\n        summary: \"经典稀疏检索方法，StructFuse 的 baseline 之一。\"\n\n  # ==========================================================================\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\n  # ==========================================================================\n  graph_guided_inference:\n    description: \"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\"\n    papers:\n\n      - title: \"LocAgent: Graph-Guided LLM Agents for Code Localization\"\n        authors: \"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\"\n        venue: ACL\n        year: 2025\n        relation: contrast\n        summary: \"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\"\n\n      - title: \"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\"\n        authors: \"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\"\n        venue: NAACL\n        year: 2025\n        relation: contrast\n        summary: \"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\"\n\n      - title: \"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\"\n        authors: \"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\"\n        venue: arXiv\n        year: 2025\n        relation: contrast\n        summary: \"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\"\n\n      - title: \"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\"\n        authors: \"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\"\n        venue: ICLR\n        year: 2025\n        relation: contrast\n        summary: \"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\"\n\n      - title: \"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\"\n        authors: \"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\"\n        venue: ASE\n        year: 2024\n        relation: contrast\n        summary: \"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\"\n\n  # ==========================================================================\n  # Category 7: Infrastructure / Tools\n  # ==========================================================================\n  infrastructure:\n    description: \"StructFuse 依赖的核心基础设施和工具\"\n    papers:\n\n      - title: \"Billion-Scale Similarity Search with GPUs\"\n        authors: \"Jeff Johnson, Matthijs Douze, Herve Jegou\"\n        venue: \"IEEE Transactions on Big Data\"\n        year: 2021\n        relation: building-block\n        summary: \"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\"\n\n      - title: \"Tree-sitter: An Incremental Parsing System for Programming Tools\"\n        authors: \"Max Brunsfeld et al.\"\n        venue: \"Software (Zenodo DOI: 10.5281/zenodo.13375512)\"\n        year: 2018\n        relation: building-block\n        summary: \"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\"\n        note: \"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\"\n",
      "numLines": 331,
      "startLine": 1,
      "totalLines": 331
    }
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-16T00:43:36.299Z_

<details><summary>↩ Tool result · `toolu_01AyKaTS7G1piJYkoDT1uU64`</summary>

```text
Web search results for query: "GRACE wang2025grace code retrieval contrastive learning multi-level code graphs"

Links: [{"title":"GRACE: Graph Convolutional Networks with Residual Connections and Contrastive Embedding Learning for Code Vulnerability Detection | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-1581-3_32"},{"title":"A Brief Introduction to Graph Contrastive Learning | GRACE","url":"https://wandb.ai/sauravmaheshkar/GRACE/reports/A-Brief-Introduction-to-Graph-Contrastive-Learning--Vmlldzo2MzYxODEy"},{"title":"GitHub - CRIPAC-DIG/GRACE: [GRL+ @ ICML 2020] PyTorch implementation for \"Deep Graph Contrastive Representation Learning\" (https://arxiv.org/abs/2006.04131v2) · GitHub","url":"https://github.com/CRIPAC-DIG/GRACE"},{"title":"Deep Graph Contrastive Learning - Homepage","url":"https://sxkdz.github.io/research/GraphCL/"},{"title":"GRACE: Graph Convolutional Networks with Residual Connections and Contrastive Embedding Learning for Code Vulnerability Detection | Request PDF","url":"https://www.researchgate.net/publication/396985821_GRACE_Graph_Convolutional_Networks_with_Residual_Connections_and_Contrastive_Embedding_Learning_for_Code_Vulnerability_Detection"},{"title":"Deep Graph Contrastive Representation Learning","url":"https://grlplus.github.io/papers/12.pdf"},{"title":"Deep Graph Contrastive Representation Learning Yanqiao Zhu1,2∗ Yichen Xu3∗,†","url":"https://arxiv.org/pdf/2006.04131"},{"title":"Local structure-aware graph contrastive representation learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S089360802300744X"},{"title":"Graph contrastive learning with node-level accurate difference","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11997587/"},{"title":"MDGCL: Graph Contrastive Learning Framework with Multiple Graph Diffusion Methods | Neural Processing Letters","url":"https://link.springer.com/article/10.1007/s11063-024-11672-3"}]

Based on the search results, I found information about GRACE, though the results primarily show two different research works with the GRACE acronym:

## GRACE for Code Vulnerability Detection (2025)

GRACE: Graph Convolutional Networks with Residual Connections and Contrastive Embedding Learning for Code Vulnerability Detection is a recent work published in 2025. This code vulnerability detection method integrates graph convolutional networks, residual connections, and contrastive learning, aiming to improve the detection performance of complex code vulnerabilities.

## Original GRACE Framework (2020)

There is also an earlier GRACE framework for graph representation learning. GRACE is a novel graph contrastive learning framework with its extension GCA featuring adaptive augmentation. The GRACE framework randomly applies removing edges and masking node features to produce different graph views for contrastive learning at both graph topology and node feature levels.

## Related Multi-Level Code Graph Approaches

The search also revealed related work on multi-level graph contrastive learning. Multi-level contrastive learning approaches propose a multi-level contrastive loss function to maximize the common information among similar instances at three levels. This is relevant to code retrieval tasks using multi-level code representations.

However, I did not find specific results for "wang2025grace code retrieval contrastive learning multi-level code graphs" as a single unified work. The search results suggest these may be related but distinct research directions in graph-based code analysis and representation learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "af064a94-f5e4-4eb6-8b6d-1bd658145554",
  "tool_use_result": {
    "query": "GRACE wang2025grace code retrieval contrastive learning multi-level code graphs",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ECuVcEJM3VuRUvKc9oLzsW",
        "content": [
          {
            "title": "GRACE: Graph Convolutional Networks with Residual Connections and Contrastive Embedding Learning for Code Vulnerability Detection | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-981-95-1581-3_32"
          },
          {
            "title": "A Brief Introduction to Graph Contrastive Learning | GRACE",
            "url": "https://wandb.ai/sauravmaheshkar/GRACE/reports/A-Brief-Introduction-to-Graph-Contrastive-Learning--Vmlldzo2MzYxODEy"
          },
          {
            "title": "GitHub - CRIPAC-DIG/GRACE: [GRL+ @ ICML 2020] PyTorch implementation for \"Deep Graph Contrastive Representation Learning\" (https://arxiv.org/abs/2006.04131v2) · GitHub",
            "url": "https://github.com/CRIPAC-DIG/GRACE"
          },
          {
            "title": "Deep Graph Contrastive Learning - Homepage",
            "url": "https://sxkdz.github.io/research/GraphCL/"
          },
          {
            "title": "GRACE: Graph Convolutional Networks with Residual Connections and Contrastive Embedding Learning for Code Vulnerability Detection | Request PDF",
            "url": "https://www.researchgate.net/publication/396985821_GRACE_Graph_Convolutional_Networks_with_Residual_Connections_and_Contrastive_Embedding_Learning_for_Code_Vulnerability_Detection"
          },
          {
            "title": "Deep Graph Contrastive Representation Learning",
            "url": "https://grlplus.github.io/papers/12.pdf"
          },
          {
            "title": "Deep Graph Contrastive Representation Learning Yanqiao Zhu1,2∗ Yichen Xu3∗,†",
            "url": "https://arxiv.org/pdf/2006.04131"
          },
          {
            "title": "Local structure-aware graph contrastive representation learning - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S089360802300744X"
          },
          {
            "title": "Graph contrastive learning with node-level accurate difference",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11997587/"
          },
          {
            "title": "MDGCL: Graph Contrastive Learning Framework with Multiple Graph Diffusion Methods | Neural Processing Letters",
            "url": "https://link.springer.com/article/10.1007/s11063-024-11672-3"
          }
        ]
      },
      "Based on the search results, I found information about GRACE, though the results primarily show two different research works with the GRACE acronym:\n\n## GRACE for Code Vulnerability Detection (2025)\n\nGRACE: Graph Convolutional Networks with Residual Connections and Contrastive Embedding Learning for Code Vulnerability Detection is a recent work published in 2025. This code vulnerability detection method integrates graph convolutional networks, residual connections, and contrastive learning, aiming to improve the detection performance of complex code vulnerabilities.\n\n## Original GRACE Framework (2020)\n\nThere is also an earlier GRACE framework for graph representation learning. GRACE is a novel graph contrastive learning framework with its extension GCA featuring adaptive augmentation. The GRACE framework randomly applies removing edges and masking node features to produce different graph views for contrastive learning at both graph topology and node feature levels.\n\n## Related Multi-Level Code Graph Approaches\n\nThe search also revealed related work on multi-level graph contrastive learning. Multi-level contrastive learning approaches propose a multi-level contrastive loss function to maximize the common information among similar instances at three levels. This is relevant to code retrieval tasks using multi-level code representations.\n\nHowever, I did not find specific results for \"wang2025grace code retrieval contrastive learning multi-level code graphs\" as a single unified work. The search results suggest these may be related but distinct research directions in graph-based code analysis and representation learning."
    ],
    "durationSeconds": 7.060837448000005
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-16T00:43:36.500Z_

<details><summary>↩ Tool result · `toolu_01R2tnmaLyMxstbMBJW9H4dB`</summary>

```text
Web search results for query: ""GRACE" hierarchical retrieval-augmented code completion AST control-flow data-flow 2025"

Links: [{"title":"GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion","url":"https://arxiv.org/html/2509.05980v1"},{"title":"[Literature Review] GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion","url":"https://www.themoonlight.io/en/review/grace-graph-guided-repository-aware-code-completion-through-hierarchical-code-fusion"},{"title":"[2509.05980] GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion","url":"https://arxiv.org/abs/2509.05980"},{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"[PDF] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GraphCoder:-Enhancing-Repository-Level-Code-via-and-Liu-Yu/793bbb3c70d4bac3908bd8f2ecc309f1bfdf5f52"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"CodeGRAG: Extracting Composed Syntax Graphs for Retrieval Augmented Cross-Lingual Code Generation","url":"https://arxiv.org/html/2405.02355v1"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/html/2406.07003v1"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering","url":"https://dl.acm.org/doi/abs/10.1145/3691620.3695054"},{"title":"[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/abs/2406.07003"}]

Based on the search results, here's what I found about GRACE:

## GRACE: Graph-Guided Repository-Aware Code Completion

GRACE is a novel framework that reimagines code repositories as hierarchical, semantically rich graph databases, fundamentally advancing repository-level code completion.

### Key Components

GRACE constructs a multi-level, multi-semantic code graph that unifies file structures, abstract syntax trees, function call graphs, class hierarchies, and data flow graphs to capture both static and dynamic code semantics.

The framework addresses significant limitations in existing retrieval-augmented generation (RAG) approaches. Current approaches overly rely on textual similarity for retrieval, neglecting structural relationships such as call chains and inheritance hierarchies, and lose critical structural information by naively concatenating retrieved snippets into text sequences for LLM input.

### Architecture

The graph structures are categorized into three levels: repo-level, module-level, and function-level. GRACE employs a Hybrid Graph Retriever that integrates graph neural network-based structural similarity with textual retrieval, refined by a graph attention network-based re-ranker to prioritize topologically relevant subgraphs.

### Performance

Using DeepSeek-V3 as the backbone LLM, GRACE surpasses the strongest graph-based RAG baselines by 8.19% EM and 7.51% ES points on every dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "f24cf052-941e-4c5c-ad4a-8979787ff5e3",
  "tool_use_result": {
    "query": "\"GRACE\" hierarchical retrieval-augmented code completion AST control-flow data-flow 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01W3iKbaUhLV291G8G2n1z5T",
        "content": [
          {
            "title": "GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion",
            "url": "https://arxiv.org/html/2509.05980v1"
          },
          {
            "title": "[Literature Review] GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion",
            "url": "https://www.themoonlight.io/en/review/grace-graph-guided-repository-aware-code-completion-through-hierarchical-code-fusion"
          },
          {
            "title": "[2509.05980] GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion",
            "url": "https://arxiv.org/abs/2509.05980"
          },
          {
            "title": "Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches",
            "url": "https://arxiv.org/html/2510.04905v1"
          },
          {
            "title": "[PDF] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/GraphCoder:-Enhancing-Repository-Level-Code-via-and-Liu-Yu/793bbb3c70d4bac3908bd8f2ecc309f1bfdf5f52"
          },
          {
            "title": "RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH",
            "url": "https://arxiv.org/pdf/2510.04905"
          },
          {
            "title": "CodeGRAG: Extracting Composed Syntax Graphs for Retrieval Augmented Cross-Lingual Code Generation",
            "url": "https://arxiv.org/html/2405.02355v1"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://arxiv.org/html/2406.07003v1"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering",
            "url": "https://dl.acm.org/doi/abs/10.1145/3691620.3695054"
          },
          {
            "title": "[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://arxiv.org/abs/2406.07003"
          }
        ]
      },
      "Based on the search results, here's what I found about GRACE:\n\n## GRACE: Graph-Guided Repository-Aware Code Completion\n\nGRACE is a novel framework that reimagines code repositories as hierarchical, semantically rich graph databases, fundamentally advancing repository-level code completion.\n\n### Key Components\n\nGRACE constructs a multi-level, multi-semantic code graph that unifies file structures, abstract syntax trees, function call graphs, class hierarchies, and data flow graphs to capture both static and dynamic code semantics.\n\nThe framework addresses significant limitations in existing retrieval-augmented generation (RAG) approaches. Current approaches overly rely on textual similarity for retrieval, neglecting structural relationships such as call chains and inheritance hierarchies, and lose critical structural information by naively concatenating retrieved snippets into text sequences for LLM input.\n\n### Architecture\n\nThe graph structures are categorized into three levels: repo-level, module-level, and function-level. GRACE employs a Hybrid Graph Retriever that integrates graph neural network-based structural similarity with textual retrieval, refined by a graph attention network-based re-ranker to prioritize topologically relevant subgraphs.\n\n### Performance\n\nUsing DeepSeek-V3 as the backbone LLM, GRACE surpasses the strongest graph-based RAG baselines by 8.19% EM and 7.51% ES points on every dataset."
    ],
    "durationSeconds": 6.876238537999998
  }
}
```

</details>

---

### Assistant

_source line 74_

<details><summary>Logged reasoning block</summary>

```text
Good, I now have all the information I need. Let me process the findings:

## Warning 1: GRACE

The second WebSearch found GRACE! It's real: "GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion" - arxiv.org/abs/2509.05980. However, the citation key is `wang2025grace` in the paper, but the arxiv ID is 2509.05980 which would be September 2025. Let me check if the authors match "Wang" - the search result doesn't explicitly say the authors. Let me look more carefully.


The arxiv paper is 2509.05980v1 with citation `wang2025grace`, and the paper definitely exists. The title and description match what's in the related_work_v1.md file—it constructs multi-level code graphs across repository, module, and function levels using AST, control-flow, and data-flow edges for hierarchical retrieval-augmented code completion, with DeepSeek-V3 as the backbone. So the paper is confirmed.

The expansion report said no well-known GRACE paper existed for code representation, but the WebSearch found it on arxiv, so either the report was outdated or the search didn't catch it at that time. Now I need to verify the authors match the citation `wang2025grace` by checking the arxiv page directly, since the search results don't show the author names. The arxiv ID and title match perfectly with what's documented, so GRACE is definitely real. The citation key suggests Wang as the first author, though I haven't explicitly confirmed that yet from the search results. The description in related_work_v1.md appears accurate based on the paper's actual title and focus on hierarchical code graphs for completion tasks.

Now I need to tackle the second warning about syncing literature_map.yaml with the two related work files—comparing the 39 entries there against the 21 papers in related_work_references.md and 6 in related_work_supplement.md to identify any discrepancies. I'm continuing through the references and finding more missing entries—MoCHi, several papers on hard negatives and contrastive learning approaches, plus work on representation issues like degeneration and anisotropy that should be documented. Continuing through the rest of the papers, I'm finding that CodeSage, SCodeR, RocketQA, STAR, PDG, and CPG aren't in the references, while SweRank, SWE-Fixer, SWE-bench, Sentence-BERT, ContraCode, the Ding et al. paper, DPR, ANCE, CL-DRD, and code2vec are all accounted for.

Looking at the second batch, CodeQL, CodexGraph, RepoGraph, LocAgent, RANGER, GraphCoder, ARISE, and RepoFusion are included, but GRACE, CrossCodeEval, and ProGraML are missing. Now I need to identify which papers from the references and supplements aren't yet in the literature map—there are quite a few gaps to fill, starting with papers like CoCoSoDa, the contrastive learning methods like CPC and HCL, and several others that appear in the related work but haven't been catalogued yet. I'm systematically checking which papers from the related work files are actually in the literature map. Looking at the first batch from related_work_references.md, the initial entries like CoCoHaNeRe, CodeSearchNet, CodeBERT, and GraphCodeBERT are already documented, but I need to continue verifying the rest against what's in the yaml file to identify the genuine gaps. I'm seeing that 20 papers are missing from the YAML file. I also need to fix a warning about UniXcoder—the related work section incorrectly states it's a backbone encoder for StructFuse, but actually StructFuse uses Qwen2.5-Coder-3B and StarCoder2-3B instead. Then I need to double-check the supplement for how dataflow negatives are described, particularly in the CAPSTONE section.

Looking at the supplement more carefully, there's a contradiction: it says negatives "share data-flow context with the positive," but the task definition says dataflow negatives should be files NOT reachable through data flow—the opposite meaning. I need to clarify which definition is correct and fix the documentation accordingly. I'm realizing there's a contradiction here—the supplement claims the negatives share data-flow context with the positive, but the task definition says they should be ¬reachable_G(x,q), meaning NOT connected through data-flow. I need to search the codebase more carefully to understand which definition is actually correct, because these two statements are saying opposite things. The supplement text has it backwards — it says negatives share data-flow context when they should actually be files that are NOT reachable through the data-flow graph, making them structurally disconnected hard negatives. I'm checking the related work sections to see if they clarify the direction, but they're vague enough that the supplement's explicit statement is the key reference point, even though it appears to be incorrect.

Now I'm planning the fixes: GRACE is a real paper and the description is accurate, so no changes needed there, though I should note that literature_map.yaml doesn't include it. For UniXcoder, I need to update the description in related_work_references.md to clarify its role as an important baseline in code retrieval rather than just a backbone encoder.

I also need to fix the dataflow negatives description in Supplement B to correctly specify that hard negatives don't share data-flow context with the positive. The big task is syncing literature_map.yaml with the 20 missing papers.

Let me start executing these fixes, beginning with the quick corrections and then tackling the literature map synchronization.

Now I'm searching for more information about GRACE's author to verify the details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "847a3a3a-2303-4ee7-be28-735aeb0bfe0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZXRgrzqzXN1ssFeQetUrG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 15433,
      "cache_creation_input_tokens": 2415,
      "cache_read_input_tokens": 25801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2415
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

_source line 75_

GRACE 论文找到了：**真实存在** — [GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion](https://arxiv.org/abs/2509.05980)。描述准确，无需删除。

现在并行执行 Warning 3 和 Warning 4 的快速修复，同时验证 GRACE 作者信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "3f03054c-4709-4ca5-82fe-7798ad5512c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZXRgrzqzXN1ssFeQetUrG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 15433,
      "cache_creation_input_tokens": 2415,
      "cache_read_input_tokens": 25801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2415
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

_source line 76_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01APKv2J8ddy9687UpfmeXCa`</summary>

```json
{
  "query": "arxiv 2509.05980 GRACE Graph-Guided Repository-Aware Code Completion authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "2450573f-95c6-4f2c-9fa2-95dccc3c3211",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZXRgrzqzXN1ssFeQetUrG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 15433,
      "cache_creation_input_tokens": 2415,
      "cache_read_input_tokens": 25801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2415
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

_source line 77 · 2026-05-16T00:45:14.417Z_

<details><summary>↩ Tool result · `toolu_01APKv2J8ddy9687UpfmeXCa`</summary>

```text
Web search results for query: "arxiv 2509.05980 GRACE Graph-Guided Repository-Aware Code Completion authors"

Links: [{"title":"[2509.05980] GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion","url":"https://arxiv.org/abs/2509.05980"},{"title":"Graph-Guided Repository-Aware Code Completion ...","url":"https://arxiv.org/pdf/2509.05980"},{"title":"GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion","url":"https://arxiv.org/html/2509.05980"},{"title":"[2509.25257] RANGER -- Repository-Level Agent for Graph-Enhanced Retrieval","url":"https://arxiv.org/abs/2509.25257"},{"title":"[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/abs/2406.07003"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/html/2406.07003v2"},{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"[2509.16112] CodeRAG: Finding Relevant and Necessary Knowledge for Retrieval-Augmented Repository-Level Code Completion","url":"https://arxiv.org/abs/2509.16112"},{"title":"RANGER -- Repository-Level Agent for Graph-Enhanced ...","url":"https://arxiv.org/pdf/2509.25257"},{"title":"RANGER: Repository‑level Agent for Graph‑Enhanced Retrieval","url":"https://arxiv.org/html/2509.25257v1"}]

Based on the search results, the authors of the paper "GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion" (arXiv:2509.05980) are Xingliang Wang, Baoyi Wang, Chen Zhi, Junxiao Han, Xinkui Zhao, Jianwei Yin, and Shuiguang Deng.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "e181ac62-fba5-4925-bc76-b83fe290cebb",
  "tool_use_result": {
    "query": "arxiv 2509.05980 GRACE Graph-Guided Repository-Aware Code Completion authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_019JA7bL94PrCx7wiSg8b5Ho",
        "content": [
          {
            "title": "[2509.05980] GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion",
            "url": "https://arxiv.org/abs/2509.05980"
          },
          {
            "title": "Graph-Guided Repository-Aware Code Completion ...",
            "url": "https://arxiv.org/pdf/2509.05980"
          },
          {
            "title": "GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion",
            "url": "https://arxiv.org/html/2509.05980"
          },
          {
            "title": "[2509.25257] RANGER -- Repository-Level Agent for Graph-Enhanced Retrieval",
            "url": "https://arxiv.org/abs/2509.25257"
          },
          {
            "title": "[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://arxiv.org/abs/2406.07003"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://arxiv.org/html/2406.07003v2"
          },
          {
            "title": "Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches",
            "url": "https://arxiv.org/html/2510.04905v1"
          },
          {
            "title": "[2509.16112] CodeRAG: Finding Relevant and Necessary Knowledge for Retrieval-Augmented Repository-Level Code Completion",
            "url": "https://arxiv.org/abs/2509.16112"
          },
          {
            "title": "RANGER -- Repository-Level Agent for Graph-Enhanced ...",
            "url": "https://arxiv.org/pdf/2509.25257"
          },
          {
            "title": "RANGER: Repository‑level Agent for Graph‑Enhanced Retrieval",
            "url": "https://arxiv.org/html/2509.25257v1"
          }
        ]
      },
      "Based on the search results, the authors of the paper \"GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion\" (arXiv:2509.05980) are Xingliang Wang, Baoyi Wang, Chen Zhi, Junxiao Han, Xinkui Zhao, Jianwei Yin, and Shuiguang Deng."
    ],
    "durationSeconds": 3.1355727180000104
  }
}
```

</details>

---

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Edit · `toolu_01QohqnMQamBxqBzYsFnrC16`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/literature/related_work_references.md",
  "old_string": "Unified cross-modal pre-training leveraging AST and code comments via contrastive learning. **StructFuse 的 backbone encoder 之一，也展示了 AST 结构对代码表示的增益。**",
  "new_string": "Unified cross-modal pre-training leveraging AST and code comments via contrastive learning. **代码检索领域的重要 baseline（AST-based pre-training），但不是 StructFuse 的 backbone。StructFuse 使用 Qwen2.5-Coder-3B 和 StarCoder2-3B 作为 backbone encoder。**"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "74864707-2cc6-41ab-b1a6-f11d99b37a5b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZXRgrzqzXN1ssFeQetUrG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 15433,
      "cache_creation_input_tokens": 2415,
      "cache_read_input_tokens": 25801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2415
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

_source line 79 · 2026-05-16T00:45:15.184Z_

<details><summary>↩ Tool result · `toolu_01QohqnMQamBxqBzYsFnrC16`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/literature/related_work_references.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "34c609c5-dee1-401b-ac4e-16139d711e06",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/literature/related_work_references.md",
    "oldString": "Unified cross-modal pre-training leveraging AST and code comments via contrastive learning. **StructFuse 的 backbone encoder 之一，也展示了 AST 结构对代码表示的增益。**",
    "newString": "Unified cross-modal pre-training leveraging AST and code comments via contrastive learning. **代码检索领域的重要 baseline（AST-based pre-training），但不是 StructFuse 的 backbone。StructFuse 使用 Qwen2.5-Coder-3B 和 StarCoder2-3B 作为 backbone encoder。**",
    "originalFile": "# StructFuse Related Work Literature Collection\n\n> Collected: 2026-05-16 | Total: 21 papers across 3 directions\n\n---\n\n## Direction 1: Code Retrieval 中的 Negative Mining 策略\n\n### 1.1 CoCoHaNeRe (direct-competitor)\n\nCode search framework with differentiable hard negative retrieval from a searchable memory bank. Average MRR exceeds CodeBERT/GraphCodeBERT/UniXcoder by 11.25%/8.13%/7.38%. **与 StructFuse 最直接的竞品——同样关注 code search 中 hard negative 的挖掘策略。**\n\n```bibtex\n@article{fan2025cocohanere,\n  title={Effective Hard Negative Mining for Contrastive Learning-Based Code Search},\n  author={Fan, Ye and Li, Chao and Ge, Jing and Huang, Liang and Luo, Bin},\n  journal={ACM Transactions on Software Engineering and Methodology},\n  volume={34},\n  number={3},\n  pages={1--35},\n  year={2025},\n  doi={10.1145/3695994}\n}\n```\n\n### 1.2 CodeSearchNet (evaluation)\n\nCode search benchmark with 6M functions across 6 languages and expert relevance annotations. **StructFuse 使用的评估数据集的来源基准。**\n\n```bibtex\n@article{husain2019codesearchnet,\n  title={CodeSearchNet Challenge: Evaluating the State of Semantic Code Search},\n  author={Husain, Hamel and Wu, Ho-Hsiang and Gazit, Tiferet and Allamanis, Miltiadis and Brockschmidt, Marc},\n  journal={arXiv preprint arXiv:1909.09436},\n  year={2019}\n}\n```\n\n### 1.3 CodeBERT (background)\n\nFirst bimodal pre-trained model for programming language and natural language, trained with replaced token detection. **Code retrieval 领域的基线模型。**\n\n```bibtex\n@inproceedings{feng2020codebert,\n  title={CodeBERT: A Pre-Trained Model for Programming and Natural Languages},\n  author={Feng, Zhangyin and Guo, Daya and Tang, Duyu and Duan, Nan and Feng, Xiaocheng and Gong, Ming and Shou, Linjun and Qin, Bing and Liu, Ting and Jiang, Daxin and Zhou, Ming},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020},\n  pages={1536--1547},\n  year={2020}\n}\n```\n\n### 1.4 GraphCodeBERT (method-component)\n\nFirst pre-trained model incorporating code structure (data flow) for code representations. Uses semantic-level structure rather than AST. **展示了结构化代码表示对检索的提升，StructFuse 的 structure-aware embedding 思路的先驱。**\n\n```bibtex\n@inproceedings{guo2021graphcodebert,\n  title={GraphCodeBERT: Pre-training Code Representations with Data Flow},\n  author={Guo, Daya and Ren, Shuo and Lu, Shuai and Feng, Zhangyin and Tang, Duyu and Liu, Shujie and Zhou, Long and Duan, Nan and Svyatkovskiy, Alexey and Fu, Shengyu and Tufano, Michele and Deng, Shao Kun and Clement, Colin and Drain, Dawn and Sundaresan, Neel and Yin, Jian and Jiang, Daxin and Zhou, Ming},\n  booktitle={International Conference on Learning Representations},\n  year={2021}\n}\n```\n\n### 1.5 UniXcoder (background)\n\nUnified cross-modal pre-training leveraging AST and code comments via contrastive learning. **StructFuse 的 backbone encoder 之一，也展示了 AST 结构对代码表示的增益。**\n\n```bibtex\n@inproceedings{guo2022unixcoder,\n  title={UniXcoder: Unified Cross-Modal Pre-training for Code Representation},\n  author={Guo, Daya and Lu, Shuai and Duan, Nan and Wang, Yanlin and Zhou, Ming and Yin, Jian},\n  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages={7212--7225},\n  year={2022}\n}\n```\n\n### 1.6 CodeRetriever (direct-competitor)\n\nLarge-scale contrastive pre-training with both unimodal (code-code) and bimodal (code-text) learning for code search. **与 StructFuse 类似的 contrastive learning 框架，但没有显式的 hard negative 策略。**\n\n```bibtex\n@inproceedings{li2022coderetriever,\n  title={CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search},\n  author={Li, Xiaonan and Gong, Yeyun and Shen, Yelong and Qiu, Xipeng and Zhang, Hang and Yao, Bolun and Qi, Weizhen and Jiang, Daxin and Chen, Weizhu and Duan, Nan},\n  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  pages={2898--2910},\n  year={2022}\n}\n```\n\n### 1.7 CoCoSoDa (direct-competitor)\n\nContrastive code search with soft data augmentation and momentum-based negative enrichment. Exceeds CodeBERT/GraphCodeBERT/UniXcoder by 13.3%/10.5%/5.9% MRR. **在 negative sample enrichment 方面与 StructFuse 互补——CoCoSoDa 用 momentum queue 增加 negative 数量，StructFuse 关注 negative difficulty。**\n\n```bibtex\n@inproceedings{shi2023cocosoda,\n  title={CoCoSoDa: Effective Contrastive Learning for Code Search},\n  author={Shi, Ensheng and Wang, Yanlin and Gu, Wenchao and Du, Lun and Zhang, Hongyu and Han, Shi and Zhang, Dongmei and Sun, Hongbin},\n  booktitle={2023 IEEE/ACM 45th International Conference on Software Engineering (ICSE)},\n  pages={2198--2210},\n  year={2023}\n}\n```\n\n---\n\n## Direction 2: Contrastive Learning 中 Hard Negative 的 Overfitting 问题\n\n### 2.1 CPC / InfoNCE (background)\n\nIntroduces InfoNCE loss: contrastive predictive coding for unsupervised representation learning. **Contrastive learning 的基础损失函数，StructFuse 训练目标的理论根基。**\n\n```bibtex\n@article{oord2018representation,\n  title={Representation Learning with Contrastive Predictive Coding},\n  author={van den Oord, Aaron and Li, Yazhe and Vinyals, Oriol},\n  journal={arXiv preprint arXiv:1807.03748},\n  year={2018}\n}\n```\n\n### 2.2 HCL (method-component)\n\nDevelops controllable hard negative sampling for contrastive learning, showing harder negatives accelerate and improve learning. **理论上证明了 hard negative 的价值，但也暗示了过度 hard 会导致问题——StructFuse difficulty analysis 的理论起点。**\n\n```bibtex\n@inproceedings{robinson2021contrastive,\n  title={Contrastive Learning with Hard Negative Samples},\n  author={Robinson, Joshua David and Chuang, Ching-Yao and Sra, Suvrit and Jegelka, Stefanie},\n  booktitle={International Conference on Learning Representations},\n  year={2021}\n}\n```\n\n### 2.3 DCL (method-component)\n\nDebiased contrastive objective correcting for false negatives (same-class samples treated as negatives). **False negative 是 hard negative 过拟合的重要来源之一，DCL 提供了理论框架。**\n\n```bibtex\n@inproceedings{chuang2020debiased,\n  title={Debiased Contrastive Learning},\n  author={Chuang, Ching-Yao and Robinson, Joshua and Lin, Yen-Chen and Torralba, Antonio and Jegelka, Stefanie},\n  booktitle={Advances in Neural Information Processing Systems},\n  volume={33},\n  pages={8765--8775},\n  year={2020}\n}\n```\n\n### 2.4 MoCHi (method-component)\n\nHard negative mixing at feature level with minimal overhead; shows harder negatives facilitate faster learning. **Feature-level hard negative 合成方法，与 StructFuse 的 structure-based negative mining 形成对比。**\n\n```bibtex\n@inproceedings{kalantidis2020hard,\n  title={Hard Negative Mixing for Contrastive Learning},\n  author={Kalantidis, Yannis and Sariyildiz, Mert Bulent and Pion, No{\\'e} and Weinzaepfel, Philippe and Larlus, Diane},\n  booktitle={Advances in Neural Information Processing Systems},\n  volume={33},\n  pages={21798--21809},\n  year={2020}\n}\n```\n\n### 2.5 Understanding Hard Negatives in NCE (background)\n\nTheoretical analysis: using model distribution as negative distribution reduces gradient bias. **为 hard negative 的作用提供了理论解释——StructFuse 的 difficulty-overfitting 分析可引用此理论框架。**\n\n```bibtex\n@inproceedings{zhang2021understanding,\n  title={Understanding Hard Negatives in Noise Contrastive Estimation},\n  author={Zhang, Wenzheng and Stratos, Karl},\n  booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},\n  pages={1090--1101},\n  year={2021}\n}\n```\n\n### 2.6 ProGCL (method-component)\n\nShows hard negatives in graph CL are often false negatives; proposes probability-based hardness that accounts for true/false negative distinction. **揭示了 hard negative = false negative 的陷阱，与 StructFuse 发现的 difficulty-overfitting 现象呼应。**\n\n```bibtex\n@inproceedings{xia2022progcl,\n  title={ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning},\n  author={Xia, Jun and Wu, Lirong and Wang, Ge and Chen, Jintao and Li, Stan Z.},\n  booktitle={Proceedings of the 39th International Conference on Machine Learning},\n  pages={24332--24346},\n  year={2022}\n}\n```\n\n### 2.7 WCL (method-component)\n\nDifficulty-based sampling exploiting a bias-amplifying encoder to find informative hard negatives while avoiding false negatives. **用 difficulty 分层采样来 debias，与 StructFuse 的 difficulty stratification 思路最接近。**\n\n```bibtex\n@inproceedings{jang2023difficulty,\n  title={Difficulty-Based Sampling for Debiased Contrastive Representation Learning},\n  author={Jang, Taeuk and Wang, Xiaoqian},\n  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},\n  pages={24039--24048},\n  year={2023}\n}\n```\n\n---\n\n## Direction 3: Representation Geometry / Similarity Saturation\n\n### 3.1 SimCLR (background)\n\nSimple contrastive framework showing the importance of data augmentation, projection head, and batch size. **Contrastive learning 的经典方法论，StructFuse 实验设计的参考。**\n\n```bibtex\n@inproceedings{chen2020simple,\n  title={A Simple Framework for Contrastive Learning of Visual Representations},\n  author={Chen, Ting and Kornblith, Simon and Norouzi, Mohammad and Hinton, Geoffrey},\n  booktitle={Proceedings of the 37th International Conference on Machine Learning},\n  pages={1597--1607},\n  year={2020}\n}\n```\n\n### 3.2 Alignment & Uniformity (method-component)\n\nIdentifies two key properties of contrastive loss: alignment of positive pairs and uniformity on hypersphere; proves contrastive loss optimizes both asymptotically. **StructFuse 分析 embedding space 质量的理论工具——可用 alignment/uniformity 指标量化 structure-aware embedding 的改进。**\n\n```bibtex\n@inproceedings{wang2020understanding,\n  title={Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere},\n  author={Wang, Tongzhou and Isola, Phillip},\n  booktitle={Proceedings of the 37th International Conference on Machine Learning},\n  pages={9929--9939},\n  year={2020}\n}\n```\n\n### 3.3 Representation Degeneration (background)\n\nShows pre-trained LM embeddings degenerate into a narrow cone, limiting representation power; proposes regularization. **Embedding 退化的理论根源——StructFuse 观察到的 similarity saturation 可追溯到此现象。**\n\n```bibtex\n@inproceedings{gao2019representation,\n  title={Representation Degeneration Problem in Training Natural Language Generation Models},\n  author={Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan},\n  booktitle={International Conference on Learning Representations},\n  year={2019}\n}\n```\n\n### 3.4 Anisotropy of Contextualized Representations (background)\n\nDiscovers that BERT/ELMo/GPT-2 representations occupy a narrow cone (anisotropy) across all layers. **实证发现 pre-trained model 的各向异性问题，StructFuse 使用的 code encoder 继承了此问题。**\n\n```bibtex\n@inproceedings{ethayarajh2019contextual,\n  title={How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings},\n  author={Ethayarajh, Kawin},\n  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n  pages={55--65},\n  year={2019}\n}\n```\n\n### 3.5 BERT-flow (method-component)\n\nShows BERT sentence embeddings are anisotropic; proposes normalizing flows to transform to isotropic Gaussian. **Anisotropy 矫正方法的代表，与 StructFuse 的 whitening/normalization 策略形成对比。**\n\n```bibtex\n@inproceedings{li2020sentence,\n  title={On the Sentence Embeddings from Pre-trained Language Models},\n  author={Li, Bohan and Zhou, Hao and He, Junxian and Wang, Mingxuan and Yang, Yiming and Li, Lei},\n  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n  pages={9119--9130},\n  year={2020}\n}\n```\n\n### 3.6 SimCSE (method-component)\n\nContrastive learning regularizes anisotropic embedding space to be more uniform; uses dropout as minimal augmentation. Spectral analysis shows contrastive loss flattens singular spectrum. **直接证明 contrastive learning 改善 anisotropy——StructFuse 可引用其 uniformity 分析框架。**\n\n```bibtex\n@inproceedings{gao2021simcse,\n  title={SimCSE: Simple Contrastive Learning of Sentence Embeddings},\n  author={Gao, Tianyu and Yao, Xingcheng and Chen, Danqi},\n  booktitle={Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},\n  pages={6894--6910},\n  year={2021}\n}\n```\n\n### 3.7 Whitening for Sentence Representations (method-component)\n\nWhitening operation enhances isotropy and reduces dimensionality of sentence representations. **针对 anisotropy 的简洁解法，与 StructFuse 中 embedding post-processing 的讨论相关。**\n\n```bibtex\n@article{su2021whitening,\n  title={Whitening Sentence Representations for Better Semantics and Faster Retrieval},\n  author={Su, Jianlin and Cao, Jiarun and Liu, Weijie and Ou, Yangyiwen},\n  journal={arXiv preprint arXiv:2103.15316},\n  year={2021}\n}\n```\n\n---\n\n## Summary\n\n| Direction | Papers | Key insight for StructFuse |\n|-----------|--------|---------------------------|\n| 1. Code retrieval negative mining | 7 | StructFuse fills the gap between structure-aware encoding (GraphCodeBERT) and hard negative mining (CoCoHaNeRe) by using structural similarity for difficulty-aware negative selection |\n| 2. Hard negative overfitting | 7 | Existing work (HCL, DCL, ProGCL, WCL) shows hard negatives help but can cause overfitting/false-negative problems; StructFuse's difficulty stratification addresses this in code domain |\n| 3. Representation geometry | 7 | Pre-trained code encoders inherit anisotropy (Ethayarajh, Gao 2019); contrastive learning improves uniformity (SimCSE, Wang & Isola) but similarity saturation in high-similarity regions remains; StructFuse's structure-aware negatives target this specific region |\n",
    "structuredPatch": [
      {
        "oldStart": 65,
        "oldLines": 7,
        "newStart": 65,
        "newLines": 7,
        "lines": [
          " ",
          " ### 1.5 UniXcoder (background)",
          " ",
          "-Unified cross-modal pre-training leveraging AST and code comments via contrastive learning. **StructFuse 的 backbone encoder 之一，也展示了 AST 结构对代码表示的增益。**",
          "+Unified cross-modal pre-training leveraging AST and code comments via contrastive learning. **代码检索领域的重要 baseline（AST-based pre-training），但不是 StructFuse 的 backbone。StructFuse 使用 Qwen2.5-Coder-3B 和 StarCoder2-3B 作为 backbone encoder。**",
          " ",
          " ```bibtex",
          " @inproceedings{guo2022unixcoder,"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---

### Tool call

_source line 80_

<details open><summary>🔧 Tool call — Edit · `toolu_019wV1Zet37Upw4AiPcJ92VL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_supplement.md",
  "old_string": "negatives that are hard because they share data-flow context with the positive, not because of embedding proximity alone.",
  "new_string": "negatives that are hard because they do *not* share data-flow context with the positive (¬reachable_G(x,q)), not because of embedding proximity alone."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "9ff9e02e-bd39-45eb-ba42-54b41804c183",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZXRgrzqzXN1ssFeQetUrG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 15433,
      "cache_creation_input_tokens": 2415,
      "cache_read_input_tokens": 25801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2415
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

_source line 81 · 2026-05-16T00:45:16.578Z_

<details><summary>↩ Tool result · `toolu_019wV1Zet37Upw4AiPcJ92VL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_supplement.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "3b9a4364-fc93-4252-9452-1301ad68dfc8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_supplement.md",
    "oldString": "negatives that are hard because they share data-flow context with the positive, not because of embedding proximity alone.",
    "newString": "negatives that are hard because they do *not* share data-flow context with the positive (¬reachable_G(x,q)), not because of embedding proximity alone.",
    "originalFile": "# Related Work Supplement: Contrastive Learning for Code & Adjacent Areas\n\n> **Purpose**: Supplementary paragraphs and citations to strengthen weak areas in Related Work v1.\n> Six new papers added; RocketQA already cited in v1.\n> Generated: 2026-05-15\n\n---\n\n## Supplement A: Contrastive Learning for Code (insert into Section 2.2, after the ContraCode/CodeRetriever paragraph)\n\nBeyond learning invariance to syntactic variation, contrastive pre-training has been applied to inject structural and robustness priors into code representations. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pre-training that aligns code, natural language, and abstract syntax tree (AST) modalities through identifier prediction and AST edge prediction objectives, demonstrating that explicitly encoding syntactic structure during contrastive pre-training improves downstream code intelligence tasks. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing nine data augmentation operators that generate adversarial code and comment variants---including identifier renaming, dead code insertion, and operand swapping---and further trains existing code models with contrastive objectives on these augmented pairs. ContraBERT shows that contrastive pre-training with targeted perturbations substantially improves model robustness against adversarial attacks while maintaining strong performance on standard benchmarks. These methods enrich the positive pair construction space for code contrastive learning, yet they focus on augmenting the pre-training signal rather than improving the selection of negative examples during fine-tuning. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, it improves which negatives the model trains against by grounding negative selection in inter-procedural data-flow structure.\n\n## Supplement B: Hard Negative Mining in Dense Retrieval (insert into Section 2.3, after the CL-DRD sentence)\n\nThe curriculum learning paradigm for negative sampling has been further developed by CAPSTONE \\cite{he2023capstone}, which addresses the training-inference discrepancy in dual-encoder dense retrieval. CAPSTONE expands documents with pseudo-queries during training and employs a curriculum sampling strategy that progressively improves the relevance between generated and real queries, effectively controlling negative difficulty through the query generation quality. This approach achieves strong results on both in-domain and out-of-domain retrieval benchmarks, reinforcing the finding that curriculum-based difficulty scheduling benefits dense retrieval training. While CAPSTONE focuses on bridging the training-inference gap through document expansion, our structure-grounded negatives provide an orthogonal form of curriculum: negatives that are hard because they share data-flow context with the positive, not because of embedding proximity alone.\n\n## Supplement C: Cross-File Code Understanding and Evaluation (insert into Section 2.4, before the closing paragraph, or as a new subsection bridge)\n\nThe importance of cross-file context for code understanding has been empirically validated by dedicated benchmarks. CrossCodeEval \\cite{ding2023crosscodeeval} constructs a diverse, multilingual benchmark for cross-file code completion across Python, Java, TypeScript, and C\\#, using static analysis to identify completion targets that strictly require cross-file dependencies. Experiments show that even state-of-the-art code LLMs struggle without cross-file context, and that retrieval-augmented approaches yield clear improvements---yet performance remains far below the ceiling, indicating substantial room for better cross-file retrieval. ProGraML \\cite{cummins2021programl} provides a language-independent, graph-based program representation that captures control-flow, data-flow, and call relations across entire programs, achieving strong results on data-flow analysis tasks. ProGraML demonstrates that whole-program structural representations are learnable and informative, providing conceptual grounding for StructFuse's use of inter-procedural data-flow graphs as a training signal. CoSQA \\cite{huang2021cosqa} contributes a large-scale dataset of 20,000+ real web queries paired with Python code, bridging the gap between synthetic code search benchmarks and real-world developer information needs; it also introduces a contrastive learning method (CoCLR) for data augmentation in code search training. Together, these resources underscore that cross-file structural dependencies and realistic query distributions are critical dimensions for advancing code retrieval---precisely the dimensions that StructFuse's structure-grounded training targets.\n\n---\n\n## Summary of New Citations\n\n| Paper | Venue | Year | Area | Relation to StructFuse |\n|-------|-------|------|------|----------------------|\n| SynCoBERT | arXiv | 2021 | Contrastive code pre-training | Syntax-guided contrastive pre-training; StructFuse uses structure for negatives, not positives |\n| ContraBERT | ICSE | 2023 | Contrastive code pre-training | Robustness-oriented augmentation; complementary to StructFuse's negative mining |\n| CAPSTONE | EMNLP | 2023 | Dense retrieval | Curriculum sampling for retrieval; StructFuse provides structure-based curriculum |\n| CrossCodeEval | NeurIPS | 2023 | Benchmark | Validates importance of cross-file context for code tasks |\n| ProGraML | ICML | 2021 | Program graphs for ML | Whole-program graph representation; conceptual grounding for StructFuse's data-flow use |\n| CoSQA | ACL | 2021 | Code search dataset | Real-world query benchmark with contrastive learning augmentation |\n",
    "structuredPatch": [
      {
        "oldStart": 12,
        "oldLines": 7,
        "newStart": 12,
        "newLines": 7,
        "lines": [
          " ",
          " ## Supplement B: Hard Negative Mining in Dense Retrieval (insert into Section 2.3, after the CL-DRD sentence)",
          " ",
          "-The curriculum learning paradigm for negative sampling has been further developed by CAPSTONE \\cite{he2023capstone}, which addresses the training-inference discrepancy in dual-encoder dense retrieval. CAPSTONE expands documents with pseudo-queries during training and employs a curriculum sampling strategy that progressively improves the relevance between generated and real queries, effectively controlling negative difficulty through the query generation quality. This approach achieves strong results on both in-domain and out-of-domain retrieval benchmarks, reinforcing the finding that curriculum-based difficulty scheduling benefits dense retrieval training. While CAPSTONE focuses on bridging the training-inference gap through document expansion, our structure-grounded negatives provide an orthogonal form of curriculum: negatives that are hard because they share data-flow context with the positive, not because of embedding proximity alone.",
          "+The curriculum learning paradigm for negative sampling has been further developed by CAPSTONE \\cite{he2023capstone}, which addresses the training-inference discrepancy in dual-encoder dense retrieval. CAPSTONE expands documents with pseudo-queries during training and employs a curriculum sampling strategy that progressively improves the relevance between generated and real queries, effectively controlling negative difficulty through the query generation quality. This approach achieves strong results on both in-domain and out-of-domain retrieval benchmarks, reinforcing the finding that curriculum-based difficulty scheduling benefits dense retrieval training. While CAPSTONE focuses on bridging the training-inference gap through document expansion, our structure-grounded negatives provide an orthogonal form of curriculum: negatives that are hard because they do *not* share data-flow context with the positive (¬reachable_G(x,q)), not because of embedding proximity alone.",
          " ",
          " ## Supplement C: Cross-File Code Understanding and Evaluation (insert into Section 2.4, before the closing paragraph, or as a new subsection bridge)",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 82_

<details><summary>Logged reasoning block</summary>

```text
Warning 3 and 4 are fixed. GRACE author confirmed: first author is Xingliang Wang → `wang2025grace` citation key is correct.

Now I need to tackle Warning 2: syncing literature_map.yaml with related_work_references.md and related_work_supplement.md.

Let me count the missing papers precisely:

From related_work_references.md (21 papers), missing from literature_map.yaml:
1. CoCoSoDa (shi2023cocosoda) - ICSE 2023


2. CPC/InfoNCE (oord2018representation) - arXiv 2018
3. HCL (robinson2021contrastive) - ICLR 2021
4. DCL (chuang2020debiased) - NeurIPS 2020
5. MoCHi (kalantidis2020hard) - NeurIPS 2020
6. Understanding Hard Negatives (zhang2021understanding) - NAACL 2021
7. ProGCL (xia2022progcl) - ICML 2022
8. WCL (jang2023difficulty) - incomplete entry
9. Alignment & Uniformity (wang2020understanding) - ICML 2020
10. Representation Degeneration (gao2019representation) - ICLR 2019
11. Anisotropy (ethayarajh2019contextual) - EMNLP 2019
12. BERT-flow (li2020sentence) - EMNLP 2020
13. SimCSE (gao2021simcse) - EMNLP 2021
14. Whitening (su2021whitening) - arXiv 2021
15. SynCoBERT (wang2021syncobert) - arXiv 2021
16. ContraBERT (liu2023contrabert) - incomplete entry

I'm continuing through the list of contrastive learning papers, completing the WCL entry from CVPR 2023 and adding the remaining papers on representation quality and degeneration issues. There are also a couple of papers from the supplementary materials that need to be included, though one entry appears to be cut off.

Now I'm looking at additional papers from the code-related research that should be added to the bibliography, including CAPSTONE, CrossCodeEval, ProGraML, and CoSQA, plus GRACE from the latest version. I also need to cross-reference the different versions of the related work documents to catch any papers that might be missing from the YAML file, like InferCode. I need to clarify the scope here—the task is specifically asking me to work with the 21 papers from related_work_references.md and 6 papers from related_work_supplement.md, so that's 27 papers total to check against literature_map.yaml. I should focus on finding which of those 27 are missing from the YAML file and add them in the correct format, organizing them into the appropriate categories.

Now I'm categorizing these papers into the existing structure. Hard negative mining papers like HCL, DCL, MoCHi, and ProGCL are method-components, while papers like Understanding Hard Negatives and CAPSTONE provide background on curriculum learning. For contrastive code learning, CoCoSoDa is a direct competitor in code search, and SynCoBERT and ContraBERT are background work on contrastive pretraining approaches.

I'm noticing that several papers on representation geometry—like Alignment & Uniformity, Representation Degeneration, Anisotropy, BERT-flow, SimCSE, and Whitening—don't fit cleanly into the existing categories, so I need to add a new representation_geometry category to the YAML structure.

Now I'm systematically building out the YAML entries for each category, starting with the papers that belong in hard_negative_mining, contrastive_code_learning, and the new representation_geometry section, making sure each entry has the required fields like title, authors, venue, year, relation, and summary. I've identified where each paper needs to go in the YAML structure. Now I'm drafting the edits to insert the new entries into their respective categories and create the representation_geometry section, then update the header count to reflect all 21 additional papers. I'm identifying the exact insertion points in the YAML file and planning strategic edits across multiple sections. Rather than making many small changes, I'll add content to the hard_negative_mining, contrastive_code_learning, program_analysis_for_ml, and code_embeddings_search sections, insert GRACE into graph_guided_inference, create a new representation_geometry category, and update the header count. Now I'm pinpointing the precise old_string values to match for each edit, starting with the CoCoHaNeRe note in the hard_negative_mining section. I'm working through a series of edits to organize research papers into categories. For the contrastive code learning section, I'm adding an entry about using program structure and functional properties to build contrastive sample pairs for learning code similarity representations. Then I'm inserting entries for program analysis methods that use multi-granularity program graphs with intra-procedural def-use edges to assist LLM agents in fault localization, followed by classical sparse retrieval baselines. I'm also adding a description of code context graphs with control-flow and data-dependence edges for coarse-to-fine retrieval in code completion tasks. Before the infrastructure section, I need to insert a new category for representation geometry, and finally update the header count to reflect all these additions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "43b0fe0d-3f32-4abc-b330-95b1670b67b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JwKruQFYeCUMkVFMVtkrfF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21742,
      "cache_read_input_tokens": 28216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21742
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

_source line 83_

Warning 3 和 4 已修复。GRACE 作者确认：Xingliang Wang 等，`wang2025grace` 引用键正确。

现在处理 Warning 2：同步 literature_map.yaml。需要添加 21 篇缺失论文。从文件末尾往前编辑避免行号偏移。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "763e7384-1929-409a-9156-16b78fb54749",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JwKruQFYeCUMkVFMVtkrfF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21742,
      "cache_read_input_tokens": 28216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21742
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

_source line 84_

<details open><summary>🔧 Tool call — Edit · `toolu_012zjQkGoFtw3NWSNJyyeXH2`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
  "old_string": "# 总计: 39 entries (含 2 个软件工具引用)",
  "new_string": "# 总计: 60 entries (含 2 个软件工具引用)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "e6120c23-de0b-41f0-9d1c-211bbb24aea1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JwKruQFYeCUMkVFMVtkrfF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21742,
      "cache_read_input_tokens": 28216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21742
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

_source line 85 · 2026-05-16T00:46:14.349Z_

<details><summary>↩ Tool result · `toolu_012zjQkGoFtw3NWSNJyyeXH2`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "8327d70e-347a-4d01-96a1-e7104360731e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
    "oldString": "# 总计: 39 entries (含 2 个软件工具引用)",
    "newString": "# 总计: 60 entries (含 2 个软件工具引用)",
    "originalFile": "# StructFuse — Related Work Literature Map\n# 最后更新: 2026-05-14\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\n# 总计: 39 entries (含 2 个软件工具引用)\n\ncategories:\n\n  # ==========================================================================\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\n  # ==========================================================================\n  code_retrieval_bug_fixing:\n    description: \"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\"\n    papers:\n\n      - title: \"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\"\n        authors: \"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\"\n        venue: ICLR\n        year: 2024\n        relation: baseline\n        summary: \"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\"\n\n      - title: \"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\"\n        authors: \"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\"\n        venue: NeurIPS\n        year: 2024\n        relation: competitor\n        summary: \"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\"\n\n      - title: \"AutoCodeRover: Autonomous Program Improvement\"\n        authors: \"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\"\n        venue: ISSTA\n        year: 2024\n        relation: competitor\n        summary: \"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\"\n\n      - title: \"Agentless: Demystifying LLM-based Software Engineering Agents\"\n        authors: \"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\"\n        venue: arXiv\n        year: 2024\n        relation: competitor\n        summary: \"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\"\n\n      - title: \"SWE-smith: Scaling Data for Software Engineering Agents\"\n        authors: \"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\"\n        venue: \"NeurIPS (Datasets & Benchmarks, Spotlight)\"\n        year: 2025\n        relation: building-block\n        summary: \"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\"\n\n      - title: \"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\"\n        authors: \"Tianyang Liu, Canwen Xu, Julian McAuley\"\n        venue: ICLR\n        year: 2024\n        relation: baseline\n        summary: \"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\"\n\n      - title: \"SweRank: Software Issue Localization with Code Ranking\"\n        authors: \"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\"\n        venue: arXiv\n        year: 2025\n        relation: competitor\n        summary: \"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\"\n\n      - title: \"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\"\n        authors: \"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\"\n        venue: \"ACL (Findings)\"\n        year: 2025\n        relation: competitor\n        summary: \"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\"\n\n  # ==========================================================================\n  # Category 2: Hard Negative Mining in Contrastive Learning\n  # ==========================================================================\n  hard_negative_mining:\n    description: \"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\"\n    papers:\n\n      - title: \"Dense Passage Retrieval for Open-Domain Question Answering\"\n        authors: \"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\"\n        venue: EMNLP\n        year: 2020\n        relation: background\n        summary: \"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\"\n\n      - title: \"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\"\n        authors: \"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\"\n        venue: ICLR\n        year: 2021\n        relation: background\n        summary: \"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\"\n\n      - title: \"A Simple Framework for Contrastive Learning of Visual Representations\"\n        authors: \"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\"\n        venue: ICML\n        year: 2020\n        relation: background\n        summary: \"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\"\n\n      - title: \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\"\n        authors: \"Nils Reimers, Iryna Gurevych\"\n        venue: EMNLP\n        year: 2019\n        relation: background\n        summary: \"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\"\n\n      - title: \"Curriculum Learning for Dense Retrieval Distillation\"\n        authors: \"Hansi Zeng, Hamed Zamani, Vishwa Vinay\"\n        venue: \"SIGIR (Best Short Paper)\"\n        year: 2022\n        relation: background\n        summary: \"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\"\n\n      - title: \"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\"\n        authors: \"Fan Y., Li C., Ge J., Huang L., Luo B.\"\n        venue: \"ACM TOSEM\"\n        year: 2025\n        relation: contrast-target\n        summary: \"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\"\n        note: \"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\"\n\n  # ==========================================================================\n  # Category 3: Contrastive Learning for Code\n  # ==========================================================================\n  contrastive_code_learning:\n    description: \"代码领域的对比学习方法，训练时利用代码特性构建正负样本\"\n    papers:\n\n      - title: \"Contrastive Code Representation Learning\"\n        authors: \"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\"\n        venue: EMNLP\n        year: 2021\n        relation: background\n        summary: \"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\"\n\n      - title: \"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\"\n        authors: \"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\"\n        venue: EMNLP\n        year: 2022\n        relation: background\n        summary: \"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\"\n\n      - title: \"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\"\n        authors: \"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\"\n        venue: \"ACL (Long Papers)\"\n        year: 2022\n        relation: background\n        summary: \"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\"\n\n  # ==========================================================================\n  # Category 4: Program Analysis for ML\n  # ==========================================================================\n  program_analysis_for_ml:\n    description: \"静态分析辅助 ML，结构信息在代码表示学习中的应用\"\n    papers:\n\n      - title: \"CodeQL: Semantic Code Analysis Engine\"\n        authors: \"GitHub / Semmle\"\n        venue: \"Tool (open-source)\"\n        year: 2019\n        relation: building-block\n        summary: \"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\"\n\n      - title: \"code2vec: Learning Distributed Representations of Code\"\n        authors: \"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\"\n        venue: POPL\n        year: 2019\n        relation: background\n        summary: \"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\"\n\n      - title: \"code2seq: Generating Sequences from Structured Representations of Code\"\n        authors: \"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\"\n        venue: ICLR\n        year: 2019\n        relation: background\n        summary: \"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\"\n\n      - title: \"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\"\n        authors: \"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\"\n        venue: SANER\n        year: 2020\n        relation: background\n        summary: \"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\"\n\n      - title: \"GraphCodeBERT: Pre-training Code Representations with Data Flow\"\n        authors: \"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\"\n        venue: ICLR\n        year: 2021\n        relation: background\n        summary: \"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\"\n\n      - title: \"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\"\n        authors: \"Shahd Seddik, Fatemeh Fard\"\n        venue: arXiv\n        year: 2026\n        relation: contrast\n        summary: \"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\"\n\n  # ==========================================================================\n  # Category 5: Code Embeddings / Code Search\n  # ==========================================================================\n  code_embeddings_search:\n    description: \"代码嵌入模型和代码搜索方法\"\n    papers:\n\n      - title: \"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\"\n        authors: \"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\"\n        venue: arXiv\n        year: 2019\n        relation: background\n        summary: \"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\"\n\n      - title: \"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\"\n        authors: \"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\"\n        venue: \"EMNLP (Findings)\"\n        year: 2020\n        relation: background\n        summary: \"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\"\n\n      - title: \"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\"\n        authors: \"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\"\n        venue: ACL\n        year: 2022\n        relation: background\n        summary: \"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\"\n\n      - title: \"StarCoder: May the Source Be with You!\"\n        authors: \"Raymond Li, Loubna Ben Allal, et al. (BigCode)\"\n        venue: TMLR\n        year: 2023\n        relation: building-block\n        summary: \"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\"\n\n      - title: \"Code Llama: Open Foundation Models for Code\"\n        authors: \"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\"\n        venue: arXiv\n        year: 2023\n        relation: background\n        summary: \"Meta 的代码大模型系列，基于 Llama 2 微调。\"\n\n      - title: \"Qwen2.5-Coder Technical Report\"\n        authors: \"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\"\n        venue: arXiv\n        year: 2024\n        relation: building-block\n        summary: \"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\"\n\n      - title: \"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\"\n        authors: \"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\"\n        venue: arXiv\n        year: 2024\n        relation: background\n        summary: \"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\"\n\n      - title: \"RepoFusion: Training Code Models to Understand Your Repository\"\n        authors: \"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\"\n        venue: arXiv\n        year: 2023\n        relation: background\n        summary: \"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\"\n\n      - title: \"BM25\"\n        authors: \"Stephen Robertson, Hugo Zaragoza\"\n        venue: \"Foundations and Trends in Information Retrieval\"\n        year: 2009\n        relation: baseline\n        summary: \"经典稀疏检索方法，StructFuse 的 baseline 之一。\"\n\n  # ==========================================================================\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\n  # ==========================================================================\n  graph_guided_inference:\n    description: \"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\"\n    papers:\n\n      - title: \"LocAgent: Graph-Guided LLM Agents for Code Localization\"\n        authors: \"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\"\n        venue: ACL\n        year: 2025\n        relation: contrast\n        summary: \"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\"\n\n      - title: \"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\"\n        authors: \"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\"\n        venue: NAACL\n        year: 2025\n        relation: contrast\n        summary: \"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\"\n\n      - title: \"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\"\n        authors: \"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\"\n        venue: arXiv\n        year: 2025\n        relation: contrast\n        summary: \"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\"\n\n      - title: \"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\"\n        authors: \"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\"\n        venue: ICLR\n        year: 2025\n        relation: contrast\n        summary: \"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\"\n\n      - title: \"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\"\n        authors: \"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\"\n        venue: ASE\n        year: 2024\n        relation: contrast\n        summary: \"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\"\n\n  # ==========================================================================\n  # Category 7: Infrastructure / Tools\n  # ==========================================================================\n  infrastructure:\n    description: \"StructFuse 依赖的核心基础设施和工具\"\n    papers:\n\n      - title: \"Billion-Scale Similarity Search with GPUs\"\n        authors: \"Jeff Johnson, Matthijs Douze, Herve Jegou\"\n        venue: \"IEEE Transactions on Big Data\"\n        year: 2021\n        relation: building-block\n        summary: \"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\"\n\n      - title: \"Tree-sitter: An Incremental Parsing System for Programming Tools\"\n        authors: \"Max Brunsfeld et al.\"\n        venue: \"Software (Zenodo DOI: 10.5281/zenodo.13375512)\"\n        year: 2018\n        relation: building-block\n        summary: \"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\"\n        note: \"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\"\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 7,
        "newStart": 1,
        "newLines": 7,
        "lines": [
          " # StructFuse — Related Work Literature Map",
          " # 最后更新: 2026-05-14",
          " # 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。",
          "-# 总计: 39 entries (含 2 个软件工具引用)",
          "+# 总计: 60 entries (含 2 个软件工具引用)",
          " ",
          " categories:",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 86_

<details open><summary>🔧 Tool call — Edit · `toolu_01KnznAyPRFmbmxVjQhUzoDW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
  "old_string": "        summary: \"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\"\n\n  # ==========================================================================\n  # Category 7: Infrastructure / Tools",
  "new_string": "        summary: \"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\"\n\n      - title: \"GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion\"\n        authors: \"Xingliang Wang, Baoyi Wang, Chen Zhi, Junxiao Han, Xinkui Zhao, Jianwei Yin, Shuiguang Deng\"\n        venue: arXiv\n        year: 2025\n        relation: contrast\n        summary: \"构建 repo/module/function 三层多语义代码图（AST + CFG + DFG + call graph + class hierarchy），用 GNN-based hybrid retriever 做层次化检索增强代码补全。推理时图方法，与 StructFuse 训练时结构信号互补。\"\n\n  # ==========================================================================\n  # Category 7: Representation Geometry / Similarity Saturation\n  # ==========================================================================\n  representation_geometry:\n    description: \"预训练模型表示空间几何分析及各向异性修正方法\"\n    papers:\n\n      - title: \"Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere\"\n        authors: \"Tongzhou Wang, Phillip Isola\"\n        venue: ICML\n        year: 2020\n        relation: method-component\n        summary: \"定义 alignment/uniformity 两个对比学习关键属性，证明对比损失渐近优化两者。StructFuse 分析 embedding space 质量的理论工具。\"\n\n      - title: \"Representation Degeneration Problem in Training Natural Language Generation Models\"\n        authors: \"Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang, Tie-Yan Liu\"\n        venue: ICLR\n        year: 2019\n        relation: background\n        summary: \"揭示预训练 LM embedding 退化为窄锥的现象，StructFuse 观察到的 similarity saturation 可追溯到此。\"\n\n      - title: \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\"\n        authors: \"Kawin Ethayarajh\"\n        venue: EMNLP\n        year: 2019\n        relation: background\n        summary: \"实证发现 BERT/ELMo/GPT-2 表示占据窄锥（各向异性），StructFuse 使用的 code encoder 继承此问题。\"\n\n      - title: \"On the Sentence Embeddings from Pre-trained Language Models\"\n        authors: \"Bohan Li, Hao Zhou, Junxian He, Mingxuan Wang, Yiming Yang, Lei Li\"\n        venue: EMNLP\n        year: 2020\n        relation: method-component\n        summary: \"BERT-flow: 用 normalizing flows 将各向异性句子嵌入变换为各向同性高斯分布。\"\n\n      - title: \"SimCSE: Simple Contrastive Learning of Sentence Embeddings\"\n        authors: \"Tianyu Gao, Xingcheng Yao, Danqi Chen\"\n        venue: EMNLP\n        year: 2021\n        relation: method-component\n        summary: \"用 dropout 作为最小增强的对比学习，直接证明 contrastive learning 改善 anisotropy。StructFuse 可引用其 uniformity 分析框架。\"\n\n      - title: \"Whitening Sentence Representations for Better Semantics and Faster Retrieval\"\n        authors: \"Jianlin Su, Jiarun Cao, Weijie Liu, Yangyiwen Ou\"\n        venue: arXiv\n        year: 2021\n        relation: method-component\n        summary: \"白化操作增强句子表示各向同性并降维，与 StructFuse embedding post-processing 讨论相关。\"\n\n  # ==========================================================================\n  # Category 8: Infrastructure / Tools"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "9a313e62-949d-4b0d-8852-f1524bf1afe5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YASMWrLFpGETJeCkrM1xhK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3613,
      "cache_read_input_tokens": 49958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3613
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

_source line 87 · 2026-05-16T00:46:38.322Z_

<details><summary>↩ Tool result · `toolu_01KnznAyPRFmbmxVjQhUzoDW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "f843910f-dbe0-471a-890f-cfb49f30a03a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
    "oldString": "        summary: \"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\"\n\n  # ==========================================================================\n  # Category 7: Infrastructure / Tools",
    "newString": "        summary: \"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\"\n\n      - title: \"GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion\"\n        authors: \"Xingliang Wang, Baoyi Wang, Chen Zhi, Junxiao Han, Xinkui Zhao, Jianwei Yin, Shuiguang Deng\"\n        venue: arXiv\n        year: 2025\n        relation: contrast\n        summary: \"构建 repo/module/function 三层多语义代码图（AST + CFG + DFG + call graph + class hierarchy），用 GNN-based hybrid retriever 做层次化检索增强代码补全。推理时图方法，与 StructFuse 训练时结构信号互补。\"\n\n  # ==========================================================================\n  # Category 7: Representation Geometry / Similarity Saturation\n  # ==========================================================================\n  representation_geometry:\n    description: \"预训练模型表示空间几何分析及各向异性修正方法\"\n    papers:\n\n      - title: \"Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere\"\n        authors: \"Tongzhou Wang, Phillip Isola\"\n        venue: ICML\n        year: 2020\n        relation: method-component\n        summary: \"定义 alignment/uniformity 两个对比学习关键属性，证明对比损失渐近优化两者。StructFuse 分析 embedding space 质量的理论工具。\"\n\n      - title: \"Representation Degeneration Problem in Training Natural Language Generation Models\"\n        authors: \"Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang, Tie-Yan Liu\"\n        venue: ICLR\n        year: 2019\n        relation: background\n        summary: \"揭示预训练 LM embedding 退化为窄锥的现象，StructFuse 观察到的 similarity saturation 可追溯到此。\"\n\n      - title: \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\"\n        authors: \"Kawin Ethayarajh\"\n        venue: EMNLP\n        year: 2019\n        relation: background\n        summary: \"实证发现 BERT/ELMo/GPT-2 表示占据窄锥（各向异性），StructFuse 使用的 code encoder 继承此问题。\"\n\n      - title: \"On the Sentence Embeddings from Pre-trained Language Models\"\n        authors: \"Bohan Li, Hao Zhou, Junxian He, Mingxuan Wang, Yiming Yang, Lei Li\"\n        venue: EMNLP\n        year: 2020\n        relation: method-component\n        summary: \"BERT-flow: 用 normalizing flows 将各向异性句子嵌入变换为各向同性高斯分布。\"\n\n      - title: \"SimCSE: Simple Contrastive Learning of Sentence Embeddings\"\n        authors: \"Tianyu Gao, Xingcheng Yao, Danqi Chen\"\n        venue: EMNLP\n        year: 2021\n        relation: method-component\n        summary: \"用 dropout 作为最小增强的对比学习，直接证明 contrastive learning 改善 anisotropy。StructFuse 可引用其 uniformity 分析框架。\"\n\n      - title: \"Whitening Sentence Representations for Better Semantics and Faster Retrieval\"\n        authors: \"Jianlin Su, Jiarun Cao, Weijie Liu, Yangyiwen Ou\"\n        venue: arXiv\n        year: 2021\n        relation: method-component\n        summary: \"白化操作增强句子表示各向同性并降维，与 StructFuse embedding post-processing 讨论相关。\"\n\n  # ==========================================================================\n  # Category 8: Infrastructure / Tools",
    "originalFile": "# StructFuse — Related Work Literature Map\n# 最后更新: 2026-05-14\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\n# 总计: 60 entries (含 2 个软件工具引用)\n\ncategories:\n\n  # ==========================================================================\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\n  # ==========================================================================\n  code_retrieval_bug_fixing:\n    description: \"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\"\n    papers:\n\n      - title: \"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\"\n        authors: \"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\"\n        venue: ICLR\n        year: 2024\n        relation: baseline\n        summary: \"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\"\n\n      - title: \"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\"\n        authors: \"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\"\n        venue: NeurIPS\n        year: 2024\n        relation: competitor\n        summary: \"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\"\n\n      - title: \"AutoCodeRover: Autonomous Program Improvement\"\n        authors: \"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\"\n        venue: ISSTA\n        year: 2024\n        relation: competitor\n        summary: \"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\"\n\n      - title: \"Agentless: Demystifying LLM-based Software Engineering Agents\"\n        authors: \"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\"\n        venue: arXiv\n        year: 2024\n        relation: competitor\n        summary: \"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\"\n\n      - title: \"SWE-smith: Scaling Data for Software Engineering Agents\"\n        authors: \"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\"\n        venue: \"NeurIPS (Datasets & Benchmarks, Spotlight)\"\n        year: 2025\n        relation: building-block\n        summary: \"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\"\n\n      - title: \"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\"\n        authors: \"Tianyang Liu, Canwen Xu, Julian McAuley\"\n        venue: ICLR\n        year: 2024\n        relation: baseline\n        summary: \"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\"\n\n      - title: \"SweRank: Software Issue Localization with Code Ranking\"\n        authors: \"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\"\n        venue: arXiv\n        year: 2025\n        relation: competitor\n        summary: \"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\"\n\n      - title: \"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\"\n        authors: \"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\"\n        venue: \"ACL (Findings)\"\n        year: 2025\n        relation: competitor\n        summary: \"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\"\n\n  # ==========================================================================\n  # Category 2: Hard Negative Mining in Contrastive Learning\n  # ==========================================================================\n  hard_negative_mining:\n    description: \"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\"\n    papers:\n\n      - title: \"Dense Passage Retrieval for Open-Domain Question Answering\"\n        authors: \"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\"\n        venue: EMNLP\n        year: 2020\n        relation: background\n        summary: \"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\"\n\n      - title: \"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\"\n        authors: \"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\"\n        venue: ICLR\n        year: 2021\n        relation: background\n        summary: \"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\"\n\n      - title: \"A Simple Framework for Contrastive Learning of Visual Representations\"\n        authors: \"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\"\n        venue: ICML\n        year: 2020\n        relation: background\n        summary: \"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\"\n\n      - title: \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\"\n        authors: \"Nils Reimers, Iryna Gurevych\"\n        venue: EMNLP\n        year: 2019\n        relation: background\n        summary: \"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\"\n\n      - title: \"Curriculum Learning for Dense Retrieval Distillation\"\n        authors: \"Hansi Zeng, Hamed Zamani, Vishwa Vinay\"\n        venue: \"SIGIR (Best Short Paper)\"\n        year: 2022\n        relation: background\n        summary: \"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\"\n\n      - title: \"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\"\n        authors: \"Fan Y., Li C., Ge J., Huang L., Luo B.\"\n        venue: \"ACM TOSEM\"\n        year: 2025\n        relation: contrast-target\n        summary: \"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\"\n        note: \"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\"\n\n  # ==========================================================================\n  # Category 3: Contrastive Learning for Code\n  # ==========================================================================\n  contrastive_code_learning:\n    description: \"代码领域的对比学习方法，训练时利用代码特性构建正负样本\"\n    papers:\n\n      - title: \"Contrastive Code Representation Learning\"\n        authors: \"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\"\n        venue: EMNLP\n        year: 2021\n        relation: background\n        summary: \"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\"\n\n      - title: \"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\"\n        authors: \"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\"\n        venue: EMNLP\n        year: 2022\n        relation: background\n        summary: \"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\"\n\n      - title: \"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\"\n        authors: \"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\"\n        venue: \"ACL (Long Papers)\"\n        year: 2022\n        relation: background\n        summary: \"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\"\n\n  # ==========================================================================\n  # Category 4: Program Analysis for ML\n  # ==========================================================================\n  program_analysis_for_ml:\n    description: \"静态分析辅助 ML，结构信息在代码表示学习中的应用\"\n    papers:\n\n      - title: \"CodeQL: Semantic Code Analysis Engine\"\n        authors: \"GitHub / Semmle\"\n        venue: \"Tool (open-source)\"\n        year: 2019\n        relation: building-block\n        summary: \"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\"\n\n      - title: \"code2vec: Learning Distributed Representations of Code\"\n        authors: \"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\"\n        venue: POPL\n        year: 2019\n        relation: background\n        summary: \"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\"\n\n      - title: \"code2seq: Generating Sequences from Structured Representations of Code\"\n        authors: \"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\"\n        venue: ICLR\n        year: 2019\n        relation: background\n        summary: \"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\"\n\n      - title: \"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\"\n        authors: \"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\"\n        venue: SANER\n        year: 2020\n        relation: background\n        summary: \"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\"\n\n      - title: \"GraphCodeBERT: Pre-training Code Representations with Data Flow\"\n        authors: \"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\"\n        venue: ICLR\n        year: 2021\n        relation: background\n        summary: \"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\"\n\n      - title: \"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\"\n        authors: \"Shahd Seddik, Fatemeh Fard\"\n        venue: arXiv\n        year: 2026\n        relation: contrast\n        summary: \"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\"\n\n  # ==========================================================================\n  # Category 5: Code Embeddings / Code Search\n  # ==========================================================================\n  code_embeddings_search:\n    description: \"代码嵌入模型和代码搜索方法\"\n    papers:\n\n      - title: \"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\"\n        authors: \"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\"\n        venue: arXiv\n        year: 2019\n        relation: background\n        summary: \"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\"\n\n      - title: \"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\"\n        authors: \"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\"\n        venue: \"EMNLP (Findings)\"\n        year: 2020\n        relation: background\n        summary: \"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\"\n\n      - title: \"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\"\n        authors: \"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\"\n        venue: ACL\n        year: 2022\n        relation: background\n        summary: \"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\"\n\n      - title: \"StarCoder: May the Source Be with You!\"\n        authors: \"Raymond Li, Loubna Ben Allal, et al. (BigCode)\"\n        venue: TMLR\n        year: 2023\n        relation: building-block\n        summary: \"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\"\n\n      - title: \"Code Llama: Open Foundation Models for Code\"\n        authors: \"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\"\n        venue: arXiv\n        year: 2023\n        relation: background\n        summary: \"Meta 的代码大模型系列，基于 Llama 2 微调。\"\n\n      - title: \"Qwen2.5-Coder Technical Report\"\n        authors: \"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\"\n        venue: arXiv\n        year: 2024\n        relation: building-block\n        summary: \"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\"\n\n      - title: \"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\"\n        authors: \"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\"\n        venue: arXiv\n        year: 2024\n        relation: background\n        summary: \"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\"\n\n      - title: \"RepoFusion: Training Code Models to Understand Your Repository\"\n        authors: \"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\"\n        venue: arXiv\n        year: 2023\n        relation: background\n        summary: \"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\"\n\n      - title: \"BM25\"\n        authors: \"Stephen Robertson, Hugo Zaragoza\"\n        venue: \"Foundations and Trends in Information Retrieval\"\n        year: 2009\n        relation: baseline\n        summary: \"经典稀疏检索方法，StructFuse 的 baseline 之一。\"\n\n  # ==========================================================================\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\n  # ==========================================================================\n  graph_guided_inference:\n    description: \"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\"\n    papers:\n\n      - title: \"LocAgent: Graph-Guided LLM Agents for Code Localization\"\n        authors: \"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\"\n        venue: ACL\n        year: 2025\n        relation: contrast\n        summary: \"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\"\n\n      - title: \"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\"\n        authors: \"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\"\n        venue: NAACL\n        year: 2025\n        relation: contrast\n        summary: \"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\"\n\n      - title: \"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\"\n        authors: \"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\"\n        venue: arXiv\n        year: 2025\n        relation: contrast\n        summary: \"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\"\n\n      - title: \"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\"\n        authors: \"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\"\n        venue: ICLR\n        year: 2025\n        relation: contrast\n        summary: \"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\"\n\n      - title: \"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\"\n        authors: \"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\"\n        venue: ASE\n        year: 2024\n        relation: contrast\n        summary: \"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\"\n\n  # ==========================================================================\n  # Category 7: Infrastructure / Tools\n  # ==========================================================================\n  infrastructure:\n    description: \"StructFuse 依赖的核心基础设施和工具\"\n    papers:\n\n      - title: \"Billion-Scale Similarity Search with GPUs\"\n        authors: \"Jeff Johnson, Matthijs Douze, Herve Jegou\"\n        venue: \"IEEE Transactions on Big Data\"\n        year: 2021\n        relation: building-block\n        summary: \"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\"\n\n      - title: \"Tree-sitter: An Incremental Parsing System for Programming Tools\"\n        authors: \"Max Brunsfeld et al.\"\n        venue: \"Software (Zenodo DOI: 10.5281/zenodo.13375512)\"\n        year: 2018\n        relation: building-block\n        summary: \"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\"\n        note: \"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\"\n",
    "structuredPatch": [
      {
        "oldStart": 307,
        "oldLines": 9,
        "newStart": 307,
        "newLines": 65,
        "lines": [
          "         relation: contrast",
          "         summary: \"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\"",
          " ",
          "+      - title: \"GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion\"",
          "+        authors: \"Xingliang Wang, Baoyi Wang, Chen Zhi, Junxiao Han, Xinkui Zhao, Jianwei Yin, Shuiguang Deng\"",
          "+        venue: arXiv",
          "+        year: 2025",
          "+        relation: contrast",
          "+        summary: \"构建 repo/module/function 三层多语义代码图（AST + CFG + DFG + call graph + class hierarchy），用 GNN-based hybrid retriever 做层次化检索增强代码补全。推理时图方法，与 StructFuse 训练时结构信号互补。\"",
          "+",
          "   # ==========================================================================",
          "-  # Category 7: Infrastructure / Tools",
          "+  # Category 7: Representation Geometry / Similarity Saturation",
          "   # ==========================================================================",
          "+  representation_geometry:",
          "+    description: \"预训练模型表示空间几何分析及各向异性修正方法\"",
          "+    papers:",
          "+",
          "+      - title: \"Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere\"",
          "+        authors: \"Tongzhou Wang, Phillip Isola\"",
          "+        venue: ICML",
          "+        year: 2020",
          "+        relation: method-component",
          "+        summary: \"定义 alignment/uniformity 两个对比学习关键属性，证明对比损失渐近优化两者。StructFuse 分析 embedding space 质量的理论工具。\"",
          "+",
          "+      - title: \"Representation Degeneration Problem in Training Natural Language Generation Models\"",
          "+        authors: \"Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang, Tie-Yan Liu\"",
          "+        venue: ICLR",
          "+        year: 2019",
          "+        relation: background",
          "+        summary: \"揭示预训练 LM embedding 退化为窄锥的现象，StructFuse 观察到的 similarity saturation 可追溯到此。\"",
          "+",
          "+      - title: \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\"",
          "+        authors: \"Kawin Ethayarajh\"",
          "+        venue: EMNLP",
          "+        year: 2019",
          "+        relation: background",
          "+        summary: \"实证发现 BERT/ELMo/GPT-2 表示占据窄锥（各向异性），StructFuse 使用的 code encoder 继承此问题。\"",
          "+",
          "+      - title: \"On the Sentence Embeddings from Pre-trained Language Models\"",
          "+        authors: \"Bohan Li, Hao Zhou, Junxian He, Mingxuan Wang, Yiming Yang, Lei Li\"",
          "+        venue: EMNLP",
          "+        year: 2020",
          "+        relation: method-component",
          "+        summary: \"BERT-flow: 用 normalizing flows 将各向异性句子嵌入变换为各向同性高斯分布。\"",
          "+",
          "+      - title: \"SimCSE: Simple Contrastive Learning of Sentence Embeddings\"",
          "+        authors: \"Tianyu Gao, Xingcheng Yao, Danqi Chen\"",
          "+        venue: EMNLP",
          "+        year: 2021",
          "+        relation: method-component",
          "+        summary: \"用 dropout 作为最小增强的对比学习，直接证明 contrastive learning 改善 anisotropy。StructFuse 可引用其 uniformity 分析框架。\"",
          "+",
          "+      - title: \"Whitening Sentence Representations for Better Semantics and Faster Retrieval\"",
          "+        authors: \"Jianlin Su, Jiarun Cao, Weijie Liu, Yangyiwen Ou\"",
          "+        venue: arXiv",
          "+        year: 2021",
          "+        relation: method-component",
          "+        summary: \"白化操作增强句子表示各向同性并降维，与 StructFuse embedding post-processing 讨论相关。\"",
          "+",
          "+  # ==========================================================================",
          "+  # Category 8: Infrastructure / Tools",
          "+  # ==========================================================================",
          "   infrastructure:",
          "     description: \"StructFuse 依赖的核心基础设施和工具\"",
          "     papers:"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 88_

<details open><summary>🔧 Tool call — Edit · `toolu_018tteNpFcMYMZ3PQr8YHUyh`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
  "old_string": "        summary: \"经典稀疏检索方法，StructFuse 的 baseline 之一。\"\n\n  # ==========================================================================\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)",
  "new_string": "        summary: \"经典稀疏检索方法，StructFuse 的 baseline 之一。\"\n\n      - title: \"CoSQA: 20,000+ Web Queries for Code Search and Question Answering\"\n        authors: \"Junjie Huang, Duyu Tang, Linjun Shou, Ming Gong, Ke Xu, Daxin Jiang, Ming Zhou, Nan Duan\"\n        venue: ACL\n        year: 2021\n        relation: background\n        summary: \"20,000+ 真实 web 查询与 Python 代码配对的大规模数据集，弥合合成 benchmark 与真实开发者需求的差距。\"\n\n  # ==========================================================================\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "438c756a-7cf2-48c7-98fc-6aca85412c13",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HvwQpHWrYzeEcQXFduuMwr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1385,
      "cache_read_input_tokens": 53571,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1385
      },
      "output_tokens": 72,
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

_source line 89 · 2026-05-16T00:46:45.138Z_

<details><summary>↩ Tool result · `toolu_018tteNpFcMYMZ3PQr8YHUyh`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "a59e451b-57f8-4f22-96af-55c53ce30344",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
    "oldString": "        summary: \"经典稀疏检索方法，StructFuse 的 baseline 之一。\"\n\n  # ==========================================================================\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)",
    "newString": "        summary: \"经典稀疏检索方法，StructFuse 的 baseline 之一。\"\n\n      - title: \"CoSQA: 20,000+ Web Queries for Code Search and Question Answering\"\n        authors: \"Junjie Huang, Duyu Tang, Linjun Shou, Ming Gong, Ke Xu, Daxin Jiang, Ming Zhou, Nan Duan\"\n        venue: ACL\n        year: 2021\n        relation: background\n        summary: \"20,000+ 真实 web 查询与 Python 代码配对的大规模数据集，弥合合成 benchmark 与真实开发者需求的差距。\"\n\n  # ==========================================================================\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)",
    "originalFile": "# StructFuse — Related Work Literature Map\n# 最后更新: 2026-05-14\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\n# 总计: 60 entries (含 2 个软件工具引用)\n\ncategories:\n\n  # ==========================================================================\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\n  # ==========================================================================\n  code_retrieval_bug_fixing:\n    description: \"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\"\n    papers:\n\n      - title: \"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\"\n        authors: \"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\"\n        venue: ICLR\n        year: 2024\n        relation: baseline\n        summary: \"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\"\n\n      - title: \"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\"\n        authors: \"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\"\n        venue: NeurIPS\n        year: 2024\n        relation: competitor\n        summary: \"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\"\n\n      - title: \"AutoCodeRover: Autonomous Program Improvement\"\n        authors: \"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\"\n        venue: ISSTA\n        year: 2024\n        relation: competitor\n        summary: \"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\"\n\n      - title: \"Agentless: Demystifying LLM-based Software Engineering Agents\"\n        authors: \"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\"\n        venue: arXiv\n        year: 2024\n        relation: competitor\n        summary: \"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\"\n\n      - title: \"SWE-smith: Scaling Data for Software Engineering Agents\"\n        authors: \"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\"\n        venue: \"NeurIPS (Datasets & Benchmarks, Spotlight)\"\n        year: 2025\n        relation: building-block\n        summary: \"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\"\n\n      - title: \"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\"\n        authors: \"Tianyang Liu, Canwen Xu, Julian McAuley\"\n        venue: ICLR\n        year: 2024\n        relation: baseline\n        summary: \"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\"\n\n      - title: \"SweRank: Software Issue Localization with Code Ranking\"\n        authors: \"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\"\n        venue: arXiv\n        year: 2025\n        relation: competitor\n        summary: \"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\"\n\n      - title: \"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\"\n        authors: \"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\"\n        venue: \"ACL (Findings)\"\n        year: 2025\n        relation: competitor\n        summary: \"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\"\n\n  # ==========================================================================\n  # Category 2: Hard Negative Mining in Contrastive Learning\n  # ==========================================================================\n  hard_negative_mining:\n    description: \"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\"\n    papers:\n\n      - title: \"Dense Passage Retrieval for Open-Domain Question Answering\"\n        authors: \"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\"\n        venue: EMNLP\n        year: 2020\n        relation: background\n        summary: \"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\"\n\n      - title: \"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\"\n        authors: \"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\"\n        venue: ICLR\n        year: 2021\n        relation: background\n        summary: \"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\"\n\n      - title: \"A Simple Framework for Contrastive Learning of Visual Representations\"\n        authors: \"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\"\n        venue: ICML\n        year: 2020\n        relation: background\n        summary: \"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\"\n\n      - title: \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\"\n        authors: \"Nils Reimers, Iryna Gurevych\"\n        venue: EMNLP\n        year: 2019\n        relation: background\n        summary: \"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\"\n\n      - title: \"Curriculum Learning for Dense Retrieval Distillation\"\n        authors: \"Hansi Zeng, Hamed Zamani, Vishwa Vinay\"\n        venue: \"SIGIR (Best Short Paper)\"\n        year: 2022\n        relation: background\n        summary: \"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\"\n\n      - title: \"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\"\n        authors: \"Fan Y., Li C., Ge J., Huang L., Luo B.\"\n        venue: \"ACM TOSEM\"\n        year: 2025\n        relation: contrast-target\n        summary: \"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\"\n        note: \"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\"\n\n  # ==========================================================================\n  # Category 3: Contrastive Learning for Code\n  # ==========================================================================\n  contrastive_code_learning:\n    description: \"代码领域的对比学习方法，训练时利用代码特性构建正负样本\"\n    papers:\n\n      - title: \"Contrastive Code Representation Learning\"\n        authors: \"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\"\n        venue: EMNLP\n        year: 2021\n        relation: background\n        summary: \"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\"\n\n      - title: \"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\"\n        authors: \"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\"\n        venue: EMNLP\n        year: 2022\n        relation: background\n        summary: \"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\"\n\n      - title: \"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\"\n        authors: \"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\"\n        venue: \"ACL (Long Papers)\"\n        year: 2022\n        relation: background\n        summary: \"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\"\n\n  # ==========================================================================\n  # Category 4: Program Analysis for ML\n  # ==========================================================================\n  program_analysis_for_ml:\n    description: \"静态分析辅助 ML，结构信息在代码表示学习中的应用\"\n    papers:\n\n      - title: \"CodeQL: Semantic Code Analysis Engine\"\n        authors: \"GitHub / Semmle\"\n        venue: \"Tool (open-source)\"\n        year: 2019\n        relation: building-block\n        summary: \"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\"\n\n      - title: \"code2vec: Learning Distributed Representations of Code\"\n        authors: \"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\"\n        venue: POPL\n        year: 2019\n        relation: background\n        summary: \"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\"\n\n      - title: \"code2seq: Generating Sequences from Structured Representations of Code\"\n        authors: \"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\"\n        venue: ICLR\n        year: 2019\n        relation: background\n        summary: \"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\"\n\n      - title: \"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\"\n        authors: \"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\"\n        venue: SANER\n        year: 2020\n        relation: background\n        summary: \"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\"\n\n      - title: \"GraphCodeBERT: Pre-training Code Representations with Data Flow\"\n        authors: \"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\"\n        venue: ICLR\n        year: 2021\n        relation: background\n        summary: \"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\"\n\n      - title: \"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\"\n        authors: \"Shahd Seddik, Fatemeh Fard\"\n        venue: arXiv\n        year: 2026\n        relation: contrast\n        summary: \"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\"\n\n  # ==========================================================================\n  # Category 5: Code Embeddings / Code Search\n  # ==========================================================================\n  code_embeddings_search:\n    description: \"代码嵌入模型和代码搜索方法\"\n    papers:\n\n      - title: \"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\"\n        authors: \"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\"\n        venue: arXiv\n        year: 2019\n        relation: background\n        summary: \"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\"\n\n      - title: \"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\"\n        authors: \"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\"\n        venue: \"EMNLP (Findings)\"\n        year: 2020\n        relation: background\n        summary: \"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\"\n\n      - title: \"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\"\n        authors: \"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\"\n        venue: ACL\n        year: 2022\n        relation: background\n        summary: \"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\"\n\n      - title: \"StarCoder: May the Source Be with You!\"\n        authors: \"Raymond Li, Loubna Ben Allal, et al. (BigCode)\"\n        venue: TMLR\n        year: 2023\n        relation: building-block\n        summary: \"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\"\n\n      - title: \"Code Llama: Open Foundation Models for Code\"\n        authors: \"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\"\n        venue: arXiv\n        year: 2023\n        relation: background\n        summary: \"Meta 的代码大模型系列，基于 Llama 2 微调。\"\n\n      - title: \"Qwen2.5-Coder Technical Report\"\n        authors: \"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\"\n        venue: arXiv\n        year: 2024\n        relation: building-block\n        summary: \"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\"\n\n      - title: \"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\"\n        authors: \"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\"\n        venue: arXiv\n        year: 2024\n        relation: background\n        summary: \"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\"\n\n      - title: \"RepoFusion: Training Code Models to Understand Your Repository\"\n        authors: \"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\"\n        venue: arXiv\n        year: 2023\n        relation: background\n        summary: \"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\"\n\n      - title: \"BM25\"\n        authors: \"Stephen Robertson, Hugo Zaragoza\"\n        venue: \"Foundations and Trends in Information Retrieval\"\n        year: 2009\n        relation: baseline\n        summary: \"经典稀疏检索方法，StructFuse 的 baseline 之一。\"\n\n  # ==========================================================================\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\n  # ==========================================================================\n  graph_guided_inference:\n    description: \"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\"\n    papers:\n\n      - title: \"LocAgent: Graph-Guided LLM Agents for Code Localization\"\n        authors: \"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\"\n        venue: ACL\n        year: 2025\n        relation: contrast\n        summary: \"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\"\n\n      - title: \"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\"\n        authors: \"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\"\n        venue: NAACL\n        year: 2025\n        relation: contrast\n        summary: \"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\"\n\n      - title: \"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\"\n        authors: \"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\"\n        venue: arXiv\n        year: 2025\n        relation: contrast\n        summary: \"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\"\n\n      - title: \"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\"\n        authors: \"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\"\n        venue: ICLR\n        year: 2025\n        relation: contrast\n        summary: \"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\"\n\n      - title: \"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\"\n        authors: \"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\"\n        venue: ASE\n        year: 2024\n        relation: contrast\n        summary: \"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\"\n\n      - title: \"GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion\"\n        authors: \"Xingliang Wang, Baoyi Wang, Chen Zhi, Junxiao Han, Xinkui Zhao, Jianwei Yin, Shuiguang Deng\"\n        venue: arXiv\n        year: 2025\n        relation: contrast\n        summary: \"构建 repo/module/function 三层多语义代码图（AST + CFG + DFG + call graph + class hierarchy），用 GNN-based hybrid retriever 做层次化检索增强代码补全。推理时图方法，与 StructFuse 训练时结构信号互补。\"\n\n  # ==========================================================================\n  # Category 7: Representation Geometry / Similarity Saturation\n  # ==========================================================================\n  representation_geometry:\n    description: \"预训练模型表示空间几何分析及各向异性修正方法\"\n    papers:\n\n      - title: \"Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere\"\n        authors: \"Tongzhou Wang, Phillip Isola\"\n        venue: ICML\n        year: 2020\n        relation: method-component\n        summary: \"定义 alignment/uniformity 两个对比学习关键属性，证明对比损失渐近优化两者。StructFuse 分析 embedding space 质量的理论工具。\"\n\n      - title: \"Representation Degeneration Problem in Training Natural Language Generation Models\"\n        authors: \"Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang, Tie-Yan Liu\"\n        venue: ICLR\n        year: 2019\n        relation: background\n        summary: \"揭示预训练 LM embedding 退化为窄锥的现象，StructFuse 观察到的 similarity saturation 可追溯到此。\"\n\n      - title: \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\"\n        authors: \"Kawin Ethayarajh\"\n        venue: EMNLP\n        year: 2019\n        relation: background\n        summary: \"实证发现 BERT/ELMo/GPT-2 表示占据窄锥（各向异性），StructFuse 使用的 code encoder 继承此问题。\"\n\n      - title: \"On the Sentence Embeddings from Pre-trained Language Models\"\n        authors: \"Bohan Li, Hao Zhou, Junxian He, Mingxuan Wang, Yiming Yang, Lei Li\"\n        venue: EMNLP\n        year: 2020\n        relation: method-component\n        summary: \"BERT-flow: 用 normalizing flows 将各向异性句子嵌入变换为各向同性高斯分布。\"\n\n      - title: \"SimCSE: Simple Contrastive Learning of Sentence Embeddings\"\n        authors: \"Tianyu Gao, Xingcheng Yao, Danqi Chen\"\n        venue: EMNLP\n        year: 2021\n        relation: method-component\n        summary: \"用 dropout 作为最小增强的对比学习，直接证明 contrastive learning 改善 anisotropy。StructFuse 可引用其 uniformity 分析框架。\"\n\n      - title: \"Whitening Sentence Representations for Better Semantics and Faster Retrieval\"\n        authors: \"Jianlin Su, Jiarun Cao, Weijie Liu, Yangyiwen Ou\"\n        venue: arXiv\n        year: 2021\n        relation: method-component\n        summary: \"白化操作增强句子表示各向同性并降维，与 StructFuse embedding post-processing 讨论相关。\"\n\n  # ==========================================================================\n  # Category 8: Infrastructure / Tools\n  # ==========================================================================\n  infrastructure:\n    description: \"StructFuse 依赖的核心基础设施和工具\"\n    papers:\n\n      - title: \"Billion-Scale Similarity Search with GPUs\"\n        authors: \"Jeff Johnson, Matthijs Douze, Herve Jegou\"\n        venue: \"IEEE Transactions on Big Data\"\n        year: 2021\n        relation: building-block\n        summary: \"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\"\n\n      - title: \"Tree-sitter: An Incremental Parsing System for Programming Tools\"\n        authors: \"Max Brunsfeld et al.\"\n        venue: \"Software (Zenodo DOI: 10.5281/zenodo.13375512)\"\n        year: 2018\n        relation: building-block\n        summary: \"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\"\n        note: \"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\"\n",
    "structuredPatch": [
      {
        "oldStart": 265,
        "oldLines": 6,
        "newStart": 265,
        "newLines": 13,
        "lines": [
          "         relation: baseline",
          "         summary: \"经典稀疏检索方法，StructFuse 的 baseline 之一。\"",
          " ",
          "+      - title: \"CoSQA: 20,000+ Web Queries for Code Search and Question Answering\"",
          "+        authors: \"Junjie Huang, Duyu Tang, Linjun Shou, Ming Gong, Ke Xu, Daxin Jiang, Ming Zhou, Nan Duan\"",
          "+        venue: ACL",
          "+        year: 2021",
          "+        relation: background",
          "+        summary: \"20,000+ 真实 web 查询与 Python 代码配对的大规模数据集，弥合合成 benchmark 与真实开发者需求的差距。\"",
          "+",
          "   # ==========================================================================",
          "   # Category 6: Graph-Guided Code Navigation (Inference-Time)",
          "   # =========================================================================="
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 90_

<details open><summary>🔧 Tool call — Edit · `toolu_015RRA2NmXyCPv5dW8yPtHNC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
  "old_string": "        summary: \"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\"\n\n  # ==========================================================================\n  # Category 5: Code Embeddings / Code Search",
  "new_string": "        summary: \"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\"\n\n      - title: \"ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimization\"\n        authors: \"Chris Cummins, Zacharias V. Fisches, Tal Ben-Nun, Torsten Hoefler, Michael FP O'Boyle, Hugh Leather\"\n        venue: ICML\n        year: 2021\n        relation: background\n        summary: \"语言无关的全程序图表示（control-flow + data-flow + call relations），证明整程序结构表示可学习且有效。StructFuse 使用 inter-procedural data-flow 的概念根基。\"\n\n      - title: \"CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion\"\n        authors: \"Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, Hantian Ding, Ming Tan, Nihal Jain, Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia, Dan Roth, Bing Xiang\"\n        venue: NeurIPS\n        year: 2023\n        relation: background\n        summary: \"多语言 cross-file 代码补全 benchmark，用静态分析确定需 cross-file 依赖的补全目标。验证了跨文件上下文对代码任务的关键性。\"\n\n  # ==========================================================================\n  # Category 5: Code Embeddings / Code Search"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "141b485b-112a-4d05-ae5b-a0bbd44d55fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C25AzD2gpqe7mZi2saZiDV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 447,
      "cache_read_input_tokens": 54956,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 447
      },
      "output_tokens": 72,
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

_source line 91 · 2026-05-16T00:46:57.168Z_

<details><summary>↩ Tool result · `toolu_015RRA2NmXyCPv5dW8yPtHNC`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "fa015b2c-2fbe-4b5c-aa01-0c754ed30f01",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
    "oldString": "        summary: \"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\"\n\n  # ==========================================================================\n  # Category 5: Code Embeddings / Code Search",
    "newString": "        summary: \"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\"\n\n      - title: \"ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimization\"\n        authors: \"Chris Cummins, Zacharias V. Fisches, Tal Ben-Nun, Torsten Hoefler, Michael FP O'Boyle, Hugh Leather\"\n        venue: ICML\n        year: 2021\n        relation: background\n        summary: \"语言无关的全程序图表示（control-flow + data-flow + call relations），证明整程序结构表示可学习且有效。StructFuse 使用 inter-procedural data-flow 的概念根基。\"\n\n      - title: \"CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion\"\n        authors: \"Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, Hantian Ding, Ming Tan, Nihal Jain, Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia, Dan Roth, Bing Xiang\"\n        venue: NeurIPS\n        year: 2023\n        relation: background\n        summary: \"多语言 cross-file 代码补全 benchmark，用静态分析确定需 cross-file 依赖的补全目标。验证了跨文件上下文对代码任务的关键性。\"\n\n  # ==========================================================================\n  # Category 5: Code Embeddings / Code Search",
    "originalFile": "# StructFuse — Related Work Literature Map\n# 最后更新: 2026-05-14\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\n# 总计: 60 entries (含 2 个软件工具引用)\n\ncategories:\n\n  # ==========================================================================\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\n  # ==========================================================================\n  code_retrieval_bug_fixing:\n    description: \"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\"\n    papers:\n\n      - title: \"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\"\n        authors: \"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\"\n        venue: ICLR\n        year: 2024\n        relation: baseline\n        summary: \"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\"\n\n      - title: \"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\"\n        authors: \"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\"\n        venue: NeurIPS\n        year: 2024\n        relation: competitor\n        summary: \"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\"\n\n      - title: \"AutoCodeRover: Autonomous Program Improvement\"\n        authors: \"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\"\n        venue: ISSTA\n        year: 2024\n        relation: competitor\n        summary: \"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\"\n\n      - title: \"Agentless: Demystifying LLM-based Software Engineering Agents\"\n        authors: \"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\"\n        venue: arXiv\n        year: 2024\n        relation: competitor\n        summary: \"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\"\n\n      - title: \"SWE-smith: Scaling Data for Software Engineering Agents\"\n        authors: \"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\"\n        venue: \"NeurIPS (Datasets & Benchmarks, Spotlight)\"\n        year: 2025\n        relation: building-block\n        summary: \"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\"\n\n      - title: \"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\"\n        authors: \"Tianyang Liu, Canwen Xu, Julian McAuley\"\n        venue: ICLR\n        year: 2024\n        relation: baseline\n        summary: \"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\"\n\n      - title: \"SweRank: Software Issue Localization with Code Ranking\"\n        authors: \"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\"\n        venue: arXiv\n        year: 2025\n        relation: competitor\n        summary: \"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\"\n\n      - title: \"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\"\n        authors: \"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\"\n        venue: \"ACL (Findings)\"\n        year: 2025\n        relation: competitor\n        summary: \"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\"\n\n  # ==========================================================================\n  # Category 2: Hard Negative Mining in Contrastive Learning\n  # ==========================================================================\n  hard_negative_mining:\n    description: \"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\"\n    papers:\n\n      - title: \"Dense Passage Retrieval for Open-Domain Question Answering\"\n        authors: \"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\"\n        venue: EMNLP\n        year: 2020\n        relation: background\n        summary: \"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\"\n\n      - title: \"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\"\n        authors: \"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\"\n        venue: ICLR\n        year: 2021\n        relation: background\n        summary: \"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\"\n\n      - title: \"A Simple Framework for Contrastive Learning of Visual Representations\"\n        authors: \"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\"\n        venue: ICML\n        year: 2020\n        relation: background\n        summary: \"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\"\n\n      - title: \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\"\n        authors: \"Nils Reimers, Iryna Gurevych\"\n        venue: EMNLP\n        year: 2019\n        relation: background\n        summary: \"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\"\n\n      - title: \"Curriculum Learning for Dense Retrieval Distillation\"\n        authors: \"Hansi Zeng, Hamed Zamani, Vishwa Vinay\"\n        venue: \"SIGIR (Best Short Paper)\"\n        year: 2022\n        relation: background\n        summary: \"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\"\n\n      - title: \"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\"\n        authors: \"Fan Y., Li C., Ge J., Huang L., Luo B.\"\n        venue: \"ACM TOSEM\"\n        year: 2025\n        relation: contrast-target\n        summary: \"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\"\n        note: \"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\"\n\n  # ==========================================================================\n  # Category 3: Contrastive Learning for Code\n  # ==========================================================================\n  contrastive_code_learning:\n    description: \"代码领域的对比学习方法，训练时利用代码特性构建正负样本\"\n    papers:\n\n      - title: \"Contrastive Code Representation Learning\"\n        authors: \"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\"\n        venue: EMNLP\n        year: 2021\n        relation: background\n        summary: \"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\"\n\n      - title: \"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\"\n        authors: \"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\"\n        venue: EMNLP\n        year: 2022\n        relation: background\n        summary: \"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\"\n\n      - title: \"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\"\n        authors: \"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\"\n        venue: \"ACL (Long Papers)\"\n        year: 2022\n        relation: background\n        summary: \"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\"\n\n  # ==========================================================================\n  # Category 4: Program Analysis for ML\n  # ==========================================================================\n  program_analysis_for_ml:\n    description: \"静态分析辅助 ML，结构信息在代码表示学习中的应用\"\n    papers:\n\n      - title: \"CodeQL: Semantic Code Analysis Engine\"\n        authors: \"GitHub / Semmle\"\n        venue: \"Tool (open-source)\"\n        year: 2019\n        relation: building-block\n        summary: \"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\"\n\n      - title: \"code2vec: Learning Distributed Representations of Code\"\n        authors: \"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\"\n        venue: POPL\n        year: 2019\n        relation: background\n        summary: \"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\"\n\n      - title: \"code2seq: Generating Sequences from Structured Representations of Code\"\n        authors: \"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\"\n        venue: ICLR\n        year: 2019\n        relation: background\n        summary: \"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\"\n\n      - title: \"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\"\n        authors: \"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\"\n        venue: SANER\n        year: 2020\n        relation: background\n        summary: \"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\"\n\n      - title: \"GraphCodeBERT: Pre-training Code Representations with Data Flow\"\n        authors: \"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\"\n        venue: ICLR\n        year: 2021\n        relation: background\n        summary: \"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\"\n\n      - title: \"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\"\n        authors: \"Shahd Seddik, Fatemeh Fard\"\n        venue: arXiv\n        year: 2026\n        relation: contrast\n        summary: \"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\"\n\n  # ==========================================================================\n  # Category 5: Code Embeddings / Code Search\n  # ==========================================================================\n  code_embeddings_search:\n    description: \"代码嵌入模型和代码搜索方法\"\n    papers:\n\n      - title: \"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\"\n        authors: \"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\"\n        venue: arXiv\n        year: 2019\n        relation: background\n        summary: \"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\"\n\n      - title: \"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\"\n        authors: \"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\"\n        venue: \"EMNLP (Findings)\"\n        year: 2020\n        relation: background\n        summary: \"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\"\n\n      - title: \"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\"\n        authors: \"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\"\n        venue: ACL\n        year: 2022\n        relation: background\n        summary: \"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\"\n\n      - title: \"StarCoder: May the Source Be with You!\"\n        authors: \"Raymond Li, Loubna Ben Allal, et al. (BigCode)\"\n        venue: TMLR\n        year: 2023\n        relation: building-block\n        summary: \"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\"\n\n      - title: \"Code Llama: Open Foundation Models for Code\"\n        authors: \"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\"\n        venue: arXiv\n        year: 2023\n        relation: background\n        summary: \"Meta 的代码大模型系列，基于 Llama 2 微调。\"\n\n      - title: \"Qwen2.5-Coder Technical Report\"\n        authors: \"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\"\n        venue: arXiv\n        year: 2024\n        relation: building-block\n        summary: \"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\"\n\n      - title: \"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\"\n        authors: \"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\"\n        venue: arXiv\n        year: 2024\n        relation: background\n        summary: \"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\"\n\n      - title: \"RepoFusion: Training Code Models to Understand Your Repository\"\n        authors: \"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\"\n        venue: arXiv\n        year: 2023\n        relation: background\n        summary: \"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\"\n\n      - title: \"BM25\"\n        authors: \"Stephen Robertson, Hugo Zaragoza\"\n        venue: \"Foundations and Trends in Information Retrieval\"\n        year: 2009\n        relation: baseline\n        summary: \"经典稀疏检索方法，StructFuse 的 baseline 之一。\"\n\n      - title: \"CoSQA: 20,000+ Web Queries for Code Search and Question Answering\"\n        authors: \"Junjie Huang, Duyu Tang, Linjun Shou, Ming Gong, Ke Xu, Daxin Jiang, Ming Zhou, Nan Duan\"\n        venue: ACL\n        year: 2021\n        relation: background\n        summary: \"20,000+ 真实 web 查询与 Python 代码配对的大规模数据集，弥合合成 benchmark 与真实开发者需求的差距。\"\n\n  # ==========================================================================\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\n  # ==========================================================================\n  graph_guided_inference:\n    description: \"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\"\n    papers:\n\n      - title: \"LocAgent: Graph-Guided LLM Agents for Code Localization\"\n        authors: \"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\"\n        venue: ACL\n        year: 2025\n        relation: contrast\n        summary: \"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\"\n\n      - title: \"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\"\n        authors: \"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\"\n        venue: NAACL\n        year: 2025\n        relation: contrast\n        summary: \"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\"\n\n      - title: \"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\"\n        authors: \"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\"\n        venue: arXiv\n        year: 2025\n        relation: contrast\n        summary: \"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\"\n\n      - title: \"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\"\n        authors: \"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\"\n        venue: ICLR\n        year: 2025\n        relation: contrast\n        summary: \"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\"\n\n      - title: \"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\"\n        authors: \"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\"\n        venue: ASE\n        year: 2024\n        relation: contrast\n        summary: \"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\"\n\n      - title: \"GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion\"\n        authors: \"Xingliang Wang, Baoyi Wang, Chen Zhi, Junxiao Han, Xinkui Zhao, Jianwei Yin, Shuiguang Deng\"\n        venue: arXiv\n        year: 2025\n        relation: contrast\n        summary: \"构建 repo/module/function 三层多语义代码图（AST + CFG + DFG + call graph + class hierarchy），用 GNN-based hybrid retriever 做层次化检索增强代码补全。推理时图方法，与 StructFuse 训练时结构信号互补。\"\n\n  # ==========================================================================\n  # Category 7: Representation Geometry / Similarity Saturation\n  # ==========================================================================\n  representation_geometry:\n    description: \"预训练模型表示空间几何分析及各向异性修正方法\"\n    papers:\n\n      - title: \"Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere\"\n        authors: \"Tongzhou Wang, Phillip Isola\"\n        venue: ICML\n        year: 2020\n        relation: method-component\n        summary: \"定义 alignment/uniformity 两个对比学习关键属性，证明对比损失渐近优化两者。StructFuse 分析 embedding space 质量的理论工具。\"\n\n      - title: \"Representation Degeneration Problem in Training Natural Language Generation Models\"\n        authors: \"Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang, Tie-Yan Liu\"\n        venue: ICLR\n        year: 2019\n        relation: background\n        summary: \"揭示预训练 LM embedding 退化为窄锥的现象，StructFuse 观察到的 similarity saturation 可追溯到此。\"\n\n      - title: \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\"\n        authors: \"Kawin Ethayarajh\"\n        venue: EMNLP\n        year: 2019\n        relation: background\n        summary: \"实证发现 BERT/ELMo/GPT-2 表示占据窄锥（各向异性），StructFuse 使用的 code encoder 继承此问题。\"\n\n      - title: \"On the Sentence Embeddings from Pre-trained Language Models\"\n        authors: \"Bohan Li, Hao Zhou, Junxian He, Mingxuan Wang, Yiming Yang, Lei Li\"\n        venue: EMNLP\n        year: 2020\n        relation: method-component\n        summary: \"BERT-flow: 用 normalizing flows 将各向异性句子嵌入变换为各向同性高斯分布。\"\n\n      - title: \"SimCSE: Simple Contrastive Learning of Sentence Embeddings\"\n        authors: \"Tianyu Gao, Xingcheng Yao, Danqi Chen\"\n        venue: EMNLP\n        year: 2021\n        relation: method-component\n        summary: \"用 dropout 作为最小增强的对比学习，直接证明 contrastive learning 改善 anisotropy。StructFuse 可引用其 uniformity 分析框架。\"\n\n      - title: \"Whitening Sentence Representations for Better Semantics and Faster Retrieval\"\n        authors: \"Jianlin Su, Jiarun Cao, Weijie Liu, Yangyiwen Ou\"\n        venue: arXiv\n        year: 2021\n        relation: method-component\n        summary: \"白化操作增强句子表示各向同性并降维，与 StructFuse embedding post-processing 讨论相关。\"\n\n  # ==========================================================================\n  # Category 8: Infrastructure / Tools\n  # ==========================================================================\n  infrastructure:\n    description: \"StructFuse 依赖的核心基础设施和工具\"\n    papers:\n\n      - title: \"Billion-Scale Similarity Search with GPUs\"\n        authors: \"Jeff Johnson, Matthijs Douze, Herve Jegou\"\n        venue: \"IEEE Transactions on Big Data\"\n        year: 2021\n        relation: building-block\n        summary: \"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\"\n\n      - title: \"Tree-sitter: An Incremental Parsing System for Programming Tools\"\n        authors: \"Max Brunsfeld et al.\"\n        venue: \"Software (Zenodo DOI: 10.5281/zenodo.13375512)\"\n        year: 2018\n        relation: building-block\n        summary: \"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\"\n        note: \"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\"\n",
    "structuredPatch": [
      {
        "oldStart": 195,
        "oldLines": 6,
        "newStart": 195,
        "newLines": 20,
        "lines": [
          "         relation: contrast",
          "         summary: \"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\"",
          " ",
          "+      - title: \"ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimization\"",
          "+        authors: \"Chris Cummins, Zacharias V. Fisches, Tal Ben-Nun, Torsten Hoefler, Michael FP O'Boyle, Hugh Leather\"",
          "+        venue: ICML",
          "+        year: 2021",
          "+        relation: background",
          "+        summary: \"语言无关的全程序图表示（control-flow + data-flow + call relations），证明整程序结构表示可学习且有效。StructFuse 使用 inter-procedural data-flow 的概念根基。\"",
          "+",
          "+      - title: \"CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion\"",
          "+        authors: \"Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, Hantian Ding, Ming Tan, Nihal Jain, Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia, Dan Roth, Bing Xiang\"",
          "+        venue: NeurIPS",
          "+        year: 2023",
          "+        relation: background",
          "+        summary: \"多语言 cross-file 代码补全 benchmark，用静态分析确定需 cross-file 依赖的补全目标。验证了跨文件上下文对代码任务的关键性。\"",
          "+",
          "   # ==========================================================================",
          "   # Category 5: Code Embeddings / Code Search",
          "   # =========================================================================="
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 92_

<details open><summary>🔧 Tool call — Edit · `toolu_012ZCDcNWanBv2SUNkhhQLKa`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
  "old_string": "        summary: \"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\"\n\n  # ==========================================================================\n  # Category 4: Program Analysis for ML",
  "new_string": "        summary: \"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\"\n\n      - title: \"CoCoSoDa: Effective Contrastive Learning for Code Search\"\n        authors: \"Ensheng Shi, Yanlin Wang, Wenchao Gu, Lun Du, Hongyu Zhang, Shi Han, Dongmei Zhang, Hongbin Sun\"\n        venue: ICSE\n        year: 2023\n        relation: direct-competitor\n        summary: \"对比代码搜索 + soft data augmentation + momentum-based negative enrichment。在 negative 数量维度与 StructFuse 互补（momentum queue vs. difficulty-aware selection）。\"\n\n      - title: \"SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation\"\n        authors: \"Xin Wang, Yasheng Wang, Fei Mi, Pingyi Zhou, Yao Wan, Xiao Liu, Li Li, Hao Wu, Jin Liu, Xin Jiang\"\n        venue: arXiv\n        year: 2021\n        relation: background\n        summary: \"语法引导的多模态对比预训练，对齐 code/NL/AST 三模态。通过 identifier prediction 和 AST edge prediction 显式编码句法结构。\"\n\n      - title: \"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning\"\n        authors: \"Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, Yang Liu\"\n        venue: ICSE\n        year: 2023\n        relation: background\n        summary: \"鲁棒性导向的对比预训练，设计 9 种对抗增强算子（identifier renaming, dead code insertion, operand swapping 等），提升模型对对抗攻击的鲁棒性。\"\n\n  # ==========================================================================\n  # Category 4: Program Analysis for ML"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "1a2cd7ec-ad10-47cc-8bb8-df9772560e9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JPpnzMYRZJmVBGZ9BFZyXk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 55403,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 736
      },
      "output_tokens": 72,
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

_source line 93 · 2026-05-16T00:47:11.695Z_

<details><summary>↩ Tool result · `toolu_012ZCDcNWanBv2SUNkhhQLKa`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "786920b7-f360-4fca-a3d4-c4899ee82673",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
    "oldString": "        summary: \"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\"\n\n  # ==========================================================================\n  # Category 4: Program Analysis for ML",
    "newString": "        summary: \"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\"\n\n      - title: \"CoCoSoDa: Effective Contrastive Learning for Code Search\"\n        authors: \"Ensheng Shi, Yanlin Wang, Wenchao Gu, Lun Du, Hongyu Zhang, Shi Han, Dongmei Zhang, Hongbin Sun\"\n        venue: ICSE\n        year: 2023\n        relation: direct-competitor\n        summary: \"对比代码搜索 + soft data augmentation + momentum-based negative enrichment。在 negative 数量维度与 StructFuse 互补（momentum queue vs. difficulty-aware selection）。\"\n\n      - title: \"SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation\"\n        authors: \"Xin Wang, Yasheng Wang, Fei Mi, Pingyi Zhou, Yao Wan, Xiao Liu, Li Li, Hao Wu, Jin Liu, Xin Jiang\"\n        venue: arXiv\n        year: 2021\n        relation: background\n        summary: \"语法引导的多模态对比预训练，对齐 code/NL/AST 三模态。通过 identifier prediction 和 AST edge prediction 显式编码句法结构。\"\n\n      - title: \"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning\"\n        authors: \"Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, Yang Liu\"\n        venue: ICSE\n        year: 2023\n        relation: background\n        summary: \"鲁棒性导向的对比预训练，设计 9 种对抗增强算子（identifier renaming, dead code insertion, operand swapping 等），提升模型对对抗攻击的鲁棒性。\"\n\n  # ==========================================================================\n  # Category 4: Program Analysis for ML",
    "originalFile": "# StructFuse — Related Work Literature Map\n# 最后更新: 2026-05-14\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\n# 总计: 60 entries (含 2 个软件工具引用)\n\ncategories:\n\n  # ==========================================================================\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\n  # ==========================================================================\n  code_retrieval_bug_fixing:\n    description: \"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\"\n    papers:\n\n      - title: \"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\"\n        authors: \"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\"\n        venue: ICLR\n        year: 2024\n        relation: baseline\n        summary: \"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\"\n\n      - title: \"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\"\n        authors: \"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\"\n        venue: NeurIPS\n        year: 2024\n        relation: competitor\n        summary: \"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\"\n\n      - title: \"AutoCodeRover: Autonomous Program Improvement\"\n        authors: \"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\"\n        venue: ISSTA\n        year: 2024\n        relation: competitor\n        summary: \"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\"\n\n      - title: \"Agentless: Demystifying LLM-based Software Engineering Agents\"\n        authors: \"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\"\n        venue: arXiv\n        year: 2024\n        relation: competitor\n        summary: \"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\"\n\n      - title: \"SWE-smith: Scaling Data for Software Engineering Agents\"\n        authors: \"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\"\n        venue: \"NeurIPS (Datasets & Benchmarks, Spotlight)\"\n        year: 2025\n        relation: building-block\n        summary: \"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\"\n\n      - title: \"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\"\n        authors: \"Tianyang Liu, Canwen Xu, Julian McAuley\"\n        venue: ICLR\n        year: 2024\n        relation: baseline\n        summary: \"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\"\n\n      - title: \"SweRank: Software Issue Localization with Code Ranking\"\n        authors: \"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\"\n        venue: arXiv\n        year: 2025\n        relation: competitor\n        summary: \"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\"\n\n      - title: \"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\"\n        authors: \"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\"\n        venue: \"ACL (Findings)\"\n        year: 2025\n        relation: competitor\n        summary: \"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\"\n\n  # ==========================================================================\n  # Category 2: Hard Negative Mining in Contrastive Learning\n  # ==========================================================================\n  hard_negative_mining:\n    description: \"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\"\n    papers:\n\n      - title: \"Dense Passage Retrieval for Open-Domain Question Answering\"\n        authors: \"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\"\n        venue: EMNLP\n        year: 2020\n        relation: background\n        summary: \"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\"\n\n      - title: \"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\"\n        authors: \"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\"\n        venue: ICLR\n        year: 2021\n        relation: background\n        summary: \"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\"\n\n      - title: \"A Simple Framework for Contrastive Learning of Visual Representations\"\n        authors: \"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\"\n        venue: ICML\n        year: 2020\n        relation: background\n        summary: \"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\"\n\n      - title: \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\"\n        authors: \"Nils Reimers, Iryna Gurevych\"\n        venue: EMNLP\n        year: 2019\n        relation: background\n        summary: \"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\"\n\n      - title: \"Curriculum Learning for Dense Retrieval Distillation\"\n        authors: \"Hansi Zeng, Hamed Zamani, Vishwa Vinay\"\n        venue: \"SIGIR (Best Short Paper)\"\n        year: 2022\n        relation: background\n        summary: \"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\"\n\n      - title: \"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\"\n        authors: \"Fan Y., Li C., Ge J., Huang L., Luo B.\"\n        venue: \"ACM TOSEM\"\n        year: 2025\n        relation: contrast-target\n        summary: \"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\"\n        note: \"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\"\n\n  # ==========================================================================\n  # Category 3: Contrastive Learning for Code\n  # ==========================================================================\n  contrastive_code_learning:\n    description: \"代码领域的对比学习方法，训练时利用代码特性构建正负样本\"\n    papers:\n\n      - title: \"Contrastive Code Representation Learning\"\n        authors: \"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\"\n        venue: EMNLP\n        year: 2021\n        relation: background\n        summary: \"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\"\n\n      - title: \"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\"\n        authors: \"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\"\n        venue: EMNLP\n        year: 2022\n        relation: background\n        summary: \"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\"\n\n      - title: \"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\"\n        authors: \"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\"\n        venue: \"ACL (Long Papers)\"\n        year: 2022\n        relation: background\n        summary: \"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\"\n\n  # ==========================================================================\n  # Category 4: Program Analysis for ML\n  # ==========================================================================\n  program_analysis_for_ml:\n    description: \"静态分析辅助 ML，结构信息在代码表示学习中的应用\"\n    papers:\n\n      - title: \"CodeQL: Semantic Code Analysis Engine\"\n        authors: \"GitHub / Semmle\"\n        venue: \"Tool (open-source)\"\n        year: 2019\n        relation: building-block\n        summary: \"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\"\n\n      - title: \"code2vec: Learning Distributed Representations of Code\"\n        authors: \"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\"\n        venue: POPL\n        year: 2019\n        relation: background\n        summary: \"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\"\n\n      - title: \"code2seq: Generating Sequences from Structured Representations of Code\"\n        authors: \"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\"\n        venue: ICLR\n        year: 2019\n        relation: background\n        summary: \"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\"\n\n      - title: \"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\"\n        authors: \"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\"\n        venue: SANER\n        year: 2020\n        relation: background\n        summary: \"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\"\n\n      - title: \"GraphCodeBERT: Pre-training Code Representations with Data Flow\"\n        authors: \"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\"\n        venue: ICLR\n        year: 2021\n        relation: background\n        summary: \"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\"\n\n      - title: \"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\"\n        authors: \"Shahd Seddik, Fatemeh Fard\"\n        venue: arXiv\n        year: 2026\n        relation: contrast\n        summary: \"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\"\n\n      - title: \"ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimization\"\n        authors: \"Chris Cummins, Zacharias V. Fisches, Tal Ben-Nun, Torsten Hoefler, Michael FP O'Boyle, Hugh Leather\"\n        venue: ICML\n        year: 2021\n        relation: background\n        summary: \"语言无关的全程序图表示（control-flow + data-flow + call relations），证明整程序结构表示可学习且有效。StructFuse 使用 inter-procedural data-flow 的概念根基。\"\n\n      - title: \"CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion\"\n        authors: \"Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, Hantian Ding, Ming Tan, Nihal Jain, Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia, Dan Roth, Bing Xiang\"\n        venue: NeurIPS\n        year: 2023\n        relation: background\n        summary: \"多语言 cross-file 代码补全 benchmark，用静态分析确定需 cross-file 依赖的补全目标。验证了跨文件上下文对代码任务的关键性。\"\n\n  # ==========================================================================\n  # Category 5: Code Embeddings / Code Search\n  # ==========================================================================\n  code_embeddings_search:\n    description: \"代码嵌入模型和代码搜索方法\"\n    papers:\n\n      - title: \"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\"\n        authors: \"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\"\n        venue: arXiv\n        year: 2019\n        relation: background\n        summary: \"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\"\n\n      - title: \"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\"\n        authors: \"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\"\n        venue: \"EMNLP (Findings)\"\n        year: 2020\n        relation: background\n        summary: \"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\"\n\n      - title: \"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\"\n        authors: \"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\"\n        venue: ACL\n        year: 2022\n        relation: background\n        summary: \"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\"\n\n      - title: \"StarCoder: May the Source Be with You!\"\n        authors: \"Raymond Li, Loubna Ben Allal, et al. (BigCode)\"\n        venue: TMLR\n        year: 2023\n        relation: building-block\n        summary: \"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\"\n\n      - title: \"Code Llama: Open Foundation Models for Code\"\n        authors: \"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\"\n        venue: arXiv\n        year: 2023\n        relation: background\n        summary: \"Meta 的代码大模型系列，基于 Llama 2 微调。\"\n\n      - title: \"Qwen2.5-Coder Technical Report\"\n        authors: \"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\"\n        venue: arXiv\n        year: 2024\n        relation: building-block\n        summary: \"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\"\n\n      - title: \"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\"\n        authors: \"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\"\n        venue: arXiv\n        year: 2024\n        relation: background\n        summary: \"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\"\n\n      - title: \"RepoFusion: Training Code Models to Understand Your Repository\"\n        authors: \"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\"\n        venue: arXiv\n        year: 2023\n        relation: background\n        summary: \"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\"\n\n      - title: \"BM25\"\n        authors: \"Stephen Robertson, Hugo Zaragoza\"\n        venue: \"Foundations and Trends in Information Retrieval\"\n        year: 2009\n        relation: baseline\n        summary: \"经典稀疏检索方法，StructFuse 的 baseline 之一。\"\n\n      - title: \"CoSQA: 20,000+ Web Queries for Code Search and Question Answering\"\n        authors: \"Junjie Huang, Duyu Tang, Linjun Shou, Ming Gong, Ke Xu, Daxin Jiang, Ming Zhou, Nan Duan\"\n        venue: ACL\n        year: 2021\n        relation: background\n        summary: \"20,000+ 真实 web 查询与 Python 代码配对的大规模数据集，弥合合成 benchmark 与真实开发者需求的差距。\"\n\n  # ==========================================================================\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\n  # ==========================================================================\n  graph_guided_inference:\n    description: \"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\"\n    papers:\n\n      - title: \"LocAgent: Graph-Guided LLM Agents for Code Localization\"\n        authors: \"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\"\n        venue: ACL\n        year: 2025\n        relation: contrast\n        summary: \"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\"\n\n      - title: \"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\"\n        authors: \"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\"\n        venue: NAACL\n        year: 2025\n        relation: contrast\n        summary: \"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\"\n\n      - title: \"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\"\n        authors: \"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\"\n        venue: arXiv\n        year: 2025\n        relation: contrast\n        summary: \"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\"\n\n      - title: \"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\"\n        authors: \"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\"\n        venue: ICLR\n        year: 2025\n        relation: contrast\n        summary: \"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\"\n\n      - title: \"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\"\n        authors: \"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\"\n        venue: ASE\n        year: 2024\n        relation: contrast\n        summary: \"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\"\n\n      - title: \"GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion\"\n        authors: \"Xingliang Wang, Baoyi Wang, Chen Zhi, Junxiao Han, Xinkui Zhao, Jianwei Yin, Shuiguang Deng\"\n        venue: arXiv\n        year: 2025\n        relation: contrast\n        summary: \"构建 repo/module/function 三层多语义代码图（AST + CFG + DFG + call graph + class hierarchy），用 GNN-based hybrid retriever 做层次化检索增强代码补全。推理时图方法，与 StructFuse 训练时结构信号互补。\"\n\n  # ==========================================================================\n  # Category 7: Representation Geometry / Similarity Saturation\n  # ==========================================================================\n  representation_geometry:\n    description: \"预训练模型表示空间几何分析及各向异性修正方法\"\n    papers:\n\n      - title: \"Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere\"\n        authors: \"Tongzhou Wang, Phillip Isola\"\n        venue: ICML\n        year: 2020\n        relation: method-component\n        summary: \"定义 alignment/uniformity 两个对比学习关键属性，证明对比损失渐近优化两者。StructFuse 分析 embedding space 质量的理论工具。\"\n\n      - title: \"Representation Degeneration Problem in Training Natural Language Generation Models\"\n        authors: \"Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang, Tie-Yan Liu\"\n        venue: ICLR\n        year: 2019\n        relation: background\n        summary: \"揭示预训练 LM embedding 退化为窄锥的现象，StructFuse 观察到的 similarity saturation 可追溯到此。\"\n\n      - title: \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\"\n        authors: \"Kawin Ethayarajh\"\n        venue: EMNLP\n        year: 2019\n        relation: background\n        summary: \"实证发现 BERT/ELMo/GPT-2 表示占据窄锥（各向异性），StructFuse 使用的 code encoder 继承此问题。\"\n\n      - title: \"On the Sentence Embeddings from Pre-trained Language Models\"\n        authors: \"Bohan Li, Hao Zhou, Junxian He, Mingxuan Wang, Yiming Yang, Lei Li\"\n        venue: EMNLP\n        year: 2020\n        relation: method-component\n        summary: \"BERT-flow: 用 normalizing flows 将各向异性句子嵌入变换为各向同性高斯分布。\"\n\n      - title: \"SimCSE: Simple Contrastive Learning of Sentence Embeddings\"\n        authors: \"Tianyu Gao, Xingcheng Yao, Danqi Chen\"\n        venue: EMNLP\n        year: 2021\n        relation: method-component\n        summary: \"用 dropout 作为最小增强的对比学习，直接证明 contrastive learning 改善 anisotropy。StructFuse 可引用其 uniformity 分析框架。\"\n\n      - title: \"Whitening Sentence Representations for Better Semantics and Faster Retrieval\"\n        authors: \"Jianlin Su, Jiarun Cao, Weijie Liu, Yangyiwen Ou\"\n        venue: arXiv\n        year: 2021\n        relation: method-component\n        summary: \"白化操作增强句子表示各向同性并降维，与 StructFuse embedding post-processing 讨论相关。\"\n\n  # ==========================================================================\n  # Category 8: Infrastructure / Tools\n  # ==========================================================================\n  infrastructure:\n    description: \"StructFuse 依赖的核心基础设施和工具\"\n    papers:\n\n      - title: \"Billion-Scale Similarity Search with GPUs\"\n        authors: \"Jeff Johnson, Matthijs Douze, Herve Jegou\"\n        venue: \"IEEE Transactions on Big Data\"\n        year: 2021\n        relation: building-block\n        summary: \"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\"\n\n      - title: \"Tree-sitter: An Incremental Parsing System for Programming Tools\"\n        authors: \"Max Brunsfeld et al.\"\n        venue: \"Software (Zenodo DOI: 10.5281/zenodo.13375512)\"\n        year: 2018\n        relation: building-block\n        summary: \"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\"\n        note: \"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\"\n",
    "structuredPatch": [
      {
        "oldStart": 146,
        "oldLines": 6,
        "newStart": 146,
        "newLines": 27,
        "lines": [
          "         relation: background",
          "         summary: \"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\"",
          " ",
          "+      - title: \"CoCoSoDa: Effective Contrastive Learning for Code Search\"",
          "+        authors: \"Ensheng Shi, Yanlin Wang, Wenchao Gu, Lun Du, Hongyu Zhang, Shi Han, Dongmei Zhang, Hongbin Sun\"",
          "+        venue: ICSE",
          "+        year: 2023",
          "+        relation: direct-competitor",
          "+        summary: \"对比代码搜索 + soft data augmentation + momentum-based negative enrichment。在 negative 数量维度与 StructFuse 互补（momentum queue vs. difficulty-aware selection）。\"",
          "+",
          "+      - title: \"SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation\"",
          "+        authors: \"Xin Wang, Yasheng Wang, Fei Mi, Pingyi Zhou, Yao Wan, Xiao Liu, Li Li, Hao Wu, Jin Liu, Xin Jiang\"",
          "+        venue: arXiv",
          "+        year: 2021",
          "+        relation: background",
          "+        summary: \"语法引导的多模态对比预训练，对齐 code/NL/AST 三模态。通过 identifier prediction 和 AST edge prediction 显式编码句法结构。\"",
          "+",
          "+      - title: \"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning\"",
          "+        authors: \"Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, Yang Liu\"",
          "+        venue: ICSE",
          "+        year: 2023",
          "+        relation: background",
          "+        summary: \"鲁棒性导向的对比预训练，设计 9 种对抗增强算子（identifier renaming, dead code insertion, operand swapping 等），提升模型对对抗攻击的鲁棒性。\"",
          "+",
          "   # ==========================================================================",
          "   # Category 4: Program Analysis for ML",
          "   # =========================================================================="
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 94_

<details open><summary>🔧 Tool call — Edit · `toolu_011uYckAQong2LYtDDoseiar`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
  "old_string": "        note: \"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\"\n\n  # ==========================================================================\n  # Category 3: Contrastive Learning for Code",
  "new_string": "        note: \"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\"\n\n      - title: \"Representation Learning with Contrastive Predictive Coding\"\n        authors: \"Aaron van den Oord, Yazhe Li, Oriol Vinyals\"\n        venue: arXiv\n        year: 2018\n        relation: background\n        summary: \"InfoNCE 损失函数：对比预测编码的无监督表示学习。StructFuse 训练目标的理论根基。\"\n\n      - title: \"Contrastive Learning with Hard Negative Samples\"\n        authors: \"Joshua David Robinson, Ching-Yao Chuang, Suvrit Sra, Stefanie Jegelka\"\n        venue: ICLR\n        year: 2021\n        relation: method-component\n        summary: \"HCL: 可控 hard negative 采样，证明更难的 negatives 加速和改善学习，但暗示过度 hard 会导致问题。StructFuse difficulty analysis 的理论起点。\"\n\n      - title: \"Debiased Contrastive Learning\"\n        authors: \"Ching-Yao Chuang, Joshua Robinson, Yen-Chen Lin, Antonio Torralba, Stefanie Jegelka\"\n        venue: NeurIPS\n        year: 2020\n        relation: method-component\n        summary: \"DCL: 去偏对比目标，修正 false negatives（同类样本被当作 negatives）问题。False negative 是 hard negative 过拟合的重要来源。\"\n\n      - title: \"Hard Negative Mixing for Contrastive Learning\"\n        authors: \"Yannis Kalantidis, Mert Bulent Sariyildiz, Noe Pion, Philippe Weinzaepfel, Diane Larlus\"\n        venue: NeurIPS\n        year: 2020\n        relation: method-component\n        summary: \"MoCHi: feature-level hard negative 混合合成，开销极小。与 StructFuse 的 structure-based negative mining 形成对比。\"\n\n      - title: \"Understanding Hard Negatives in Noise Contrastive Estimation\"\n        authors: \"Wenzheng Zhang, Karl Stratos\"\n        venue: NAACL\n        year: 2021\n        relation: background\n        summary: \"理论分析：用模型分布作为 negative 分布可减少梯度偏差。为 hard negative 作用提供理论解释。\"\n\n      - title: \"ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning\"\n        authors: \"Jun Xia, Lirong Wu, Ge Wang, Jintao Chen, Stan Z. Li\"\n        venue: ICML\n        year: 2022\n        relation: method-component\n        summary: \"揭示图对比学习中 hard negative = false negative 的陷阱，提出基于概率的 hardness 区分 true/false negatives。与 StructFuse difficulty-overfitting 发现呼应。\"\n\n      - title: \"Difficulty-Based Sampling for Debiased Contrastive Representation Learning\"\n        authors: \"Taeuk Jang, Xiaoqian Wang\"\n        venue: CVPR\n        year: 2023\n        relation: method-component\n        summary: \"WCL: 用 difficulty 分层采样 + bias-amplifying encoder 找信息性 hard negatives 同时避免 false negatives。与 StructFuse difficulty stratification 思路最接近。\"\n\n      - title: \"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion\"\n        authors: \"Xingwei He, Yeyun Gong, A-Long Jin, Hang Zhang, Anlei Dong, Jian Jiao, Siu Ming Yiu, Nan Duan\"\n        venue: EMNLP\n        year: 2023\n        relation: background\n        summary: \"课程采样策略 + pseudo-query 文档扩展，解决双塔检索训练-推理差异。StructFuse 的 structure-grounded negatives 提供正交的课程形式。\"\n\n  # ==========================================================================\n  # Category 3: Contrastive Learning for Code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "84adeffd-da2c-4310-99c3-c31b102f3b94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CyRJSQn3g99YFq8NDoYzQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 766,
      "cache_read_input_tokens": 56139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 766
      },
      "output_tokens": 72,
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

_source line 95 · 2026-05-16T00:47:40.893Z_

<details><summary>↩ Tool result · `toolu_011uYckAQong2LYtDDoseiar`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "86616d68-874d-4ac9-8514-97f21a1b9f15",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
    "oldString": "        note: \"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\"\n\n  # ==========================================================================\n  # Category 3: Contrastive Learning for Code",
    "newString": "        note: \"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\"\n\n      - title: \"Representation Learning with Contrastive Predictive Coding\"\n        authors: \"Aaron van den Oord, Yazhe Li, Oriol Vinyals\"\n        venue: arXiv\n        year: 2018\n        relation: background\n        summary: \"InfoNCE 损失函数：对比预测编码的无监督表示学习。StructFuse 训练目标的理论根基。\"\n\n      - title: \"Contrastive Learning with Hard Negative Samples\"\n        authors: \"Joshua David Robinson, Ching-Yao Chuang, Suvrit Sra, Stefanie Jegelka\"\n        venue: ICLR\n        year: 2021\n        relation: method-component\n        summary: \"HCL: 可控 hard negative 采样，证明更难的 negatives 加速和改善学习，但暗示过度 hard 会导致问题。StructFuse difficulty analysis 的理论起点。\"\n\n      - title: \"Debiased Contrastive Learning\"\n        authors: \"Ching-Yao Chuang, Joshua Robinson, Yen-Chen Lin, Antonio Torralba, Stefanie Jegelka\"\n        venue: NeurIPS\n        year: 2020\n        relation: method-component\n        summary: \"DCL: 去偏对比目标，修正 false negatives（同类样本被当作 negatives）问题。False negative 是 hard negative 过拟合的重要来源。\"\n\n      - title: \"Hard Negative Mixing for Contrastive Learning\"\n        authors: \"Yannis Kalantidis, Mert Bulent Sariyildiz, Noe Pion, Philippe Weinzaepfel, Diane Larlus\"\n        venue: NeurIPS\n        year: 2020\n        relation: method-component\n        summary: \"MoCHi: feature-level hard negative 混合合成，开销极小。与 StructFuse 的 structure-based negative mining 形成对比。\"\n\n      - title: \"Understanding Hard Negatives in Noise Contrastive Estimation\"\n        authors: \"Wenzheng Zhang, Karl Stratos\"\n        venue: NAACL\n        year: 2021\n        relation: background\n        summary: \"理论分析：用模型分布作为 negative 分布可减少梯度偏差。为 hard negative 作用提供理论解释。\"\n\n      - title: \"ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning\"\n        authors: \"Jun Xia, Lirong Wu, Ge Wang, Jintao Chen, Stan Z. Li\"\n        venue: ICML\n        year: 2022\n        relation: method-component\n        summary: \"揭示图对比学习中 hard negative = false negative 的陷阱，提出基于概率的 hardness 区分 true/false negatives。与 StructFuse difficulty-overfitting 发现呼应。\"\n\n      - title: \"Difficulty-Based Sampling for Debiased Contrastive Representation Learning\"\n        authors: \"Taeuk Jang, Xiaoqian Wang\"\n        venue: CVPR\n        year: 2023\n        relation: method-component\n        summary: \"WCL: 用 difficulty 分层采样 + bias-amplifying encoder 找信息性 hard negatives 同时避免 false negatives。与 StructFuse difficulty stratification 思路最接近。\"\n\n      - title: \"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion\"\n        authors: \"Xingwei He, Yeyun Gong, A-Long Jin, Hang Zhang, Anlei Dong, Jian Jiao, Siu Ming Yiu, Nan Duan\"\n        venue: EMNLP\n        year: 2023\n        relation: background\n        summary: \"课程采样策略 + pseudo-query 文档扩展，解决双塔检索训练-推理差异。StructFuse 的 structure-grounded negatives 提供正交的课程形式。\"\n\n  # ==========================================================================\n  # Category 3: Contrastive Learning for Code",
    "originalFile": "# StructFuse — Related Work Literature Map\n# 最后更新: 2026-05-14\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\n# 总计: 60 entries (含 2 个软件工具引用)\n\ncategories:\n\n  # ==========================================================================\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\n  # ==========================================================================\n  code_retrieval_bug_fixing:\n    description: \"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\"\n    papers:\n\n      - title: \"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\"\n        authors: \"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\"\n        venue: ICLR\n        year: 2024\n        relation: baseline\n        summary: \"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\"\n\n      - title: \"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\"\n        authors: \"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\"\n        venue: NeurIPS\n        year: 2024\n        relation: competitor\n        summary: \"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\"\n\n      - title: \"AutoCodeRover: Autonomous Program Improvement\"\n        authors: \"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\"\n        venue: ISSTA\n        year: 2024\n        relation: competitor\n        summary: \"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\"\n\n      - title: \"Agentless: Demystifying LLM-based Software Engineering Agents\"\n        authors: \"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\"\n        venue: arXiv\n        year: 2024\n        relation: competitor\n        summary: \"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\"\n\n      - title: \"SWE-smith: Scaling Data for Software Engineering Agents\"\n        authors: \"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\"\n        venue: \"NeurIPS (Datasets & Benchmarks, Spotlight)\"\n        year: 2025\n        relation: building-block\n        summary: \"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\"\n\n      - title: \"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\"\n        authors: \"Tianyang Liu, Canwen Xu, Julian McAuley\"\n        venue: ICLR\n        year: 2024\n        relation: baseline\n        summary: \"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\"\n\n      - title: \"SweRank: Software Issue Localization with Code Ranking\"\n        authors: \"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\"\n        venue: arXiv\n        year: 2025\n        relation: competitor\n        summary: \"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\"\n\n      - title: \"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\"\n        authors: \"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\"\n        venue: \"ACL (Findings)\"\n        year: 2025\n        relation: competitor\n        summary: \"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\"\n\n  # ==========================================================================\n  # Category 2: Hard Negative Mining in Contrastive Learning\n  # ==========================================================================\n  hard_negative_mining:\n    description: \"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\"\n    papers:\n\n      - title: \"Dense Passage Retrieval for Open-Domain Question Answering\"\n        authors: \"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\"\n        venue: EMNLP\n        year: 2020\n        relation: background\n        summary: \"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\"\n\n      - title: \"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\"\n        authors: \"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\"\n        venue: ICLR\n        year: 2021\n        relation: background\n        summary: \"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\"\n\n      - title: \"A Simple Framework for Contrastive Learning of Visual Representations\"\n        authors: \"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\"\n        venue: ICML\n        year: 2020\n        relation: background\n        summary: \"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\"\n\n      - title: \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\"\n        authors: \"Nils Reimers, Iryna Gurevych\"\n        venue: EMNLP\n        year: 2019\n        relation: background\n        summary: \"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\"\n\n      - title: \"Curriculum Learning for Dense Retrieval Distillation\"\n        authors: \"Hansi Zeng, Hamed Zamani, Vishwa Vinay\"\n        venue: \"SIGIR (Best Short Paper)\"\n        year: 2022\n        relation: background\n        summary: \"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\"\n\n      - title: \"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\"\n        authors: \"Fan Y., Li C., Ge J., Huang L., Luo B.\"\n        venue: \"ACM TOSEM\"\n        year: 2025\n        relation: contrast-target\n        summary: \"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\"\n        note: \"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\"\n\n  # ==========================================================================\n  # Category 3: Contrastive Learning for Code\n  # ==========================================================================\n  contrastive_code_learning:\n    description: \"代码领域的对比学习方法，训练时利用代码特性构建正负样本\"\n    papers:\n\n      - title: \"Contrastive Code Representation Learning\"\n        authors: \"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\"\n        venue: EMNLP\n        year: 2021\n        relation: background\n        summary: \"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\"\n\n      - title: \"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\"\n        authors: \"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\"\n        venue: EMNLP\n        year: 2022\n        relation: background\n        summary: \"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\"\n\n      - title: \"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\"\n        authors: \"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\"\n        venue: \"ACL (Long Papers)\"\n        year: 2022\n        relation: background\n        summary: \"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\"\n\n      - title: \"CoCoSoDa: Effective Contrastive Learning for Code Search\"\n        authors: \"Ensheng Shi, Yanlin Wang, Wenchao Gu, Lun Du, Hongyu Zhang, Shi Han, Dongmei Zhang, Hongbin Sun\"\n        venue: ICSE\n        year: 2023\n        relation: direct-competitor\n        summary: \"对比代码搜索 + soft data augmentation + momentum-based negative enrichment。在 negative 数量维度与 StructFuse 互补（momentum queue vs. difficulty-aware selection）。\"\n\n      - title: \"SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation\"\n        authors: \"Xin Wang, Yasheng Wang, Fei Mi, Pingyi Zhou, Yao Wan, Xiao Liu, Li Li, Hao Wu, Jin Liu, Xin Jiang\"\n        venue: arXiv\n        year: 2021\n        relation: background\n        summary: \"语法引导的多模态对比预训练，对齐 code/NL/AST 三模态。通过 identifier prediction 和 AST edge prediction 显式编码句法结构。\"\n\n      - title: \"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning\"\n        authors: \"Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, Yang Liu\"\n        venue: ICSE\n        year: 2023\n        relation: background\n        summary: \"鲁棒性导向的对比预训练，设计 9 种对抗增强算子（identifier renaming, dead code insertion, operand swapping 等），提升模型对对抗攻击的鲁棒性。\"\n\n  # ==========================================================================\n  # Category 4: Program Analysis for ML\n  # ==========================================================================\n  program_analysis_for_ml:\n    description: \"静态分析辅助 ML，结构信息在代码表示学习中的应用\"\n    papers:\n\n      - title: \"CodeQL: Semantic Code Analysis Engine\"\n        authors: \"GitHub / Semmle\"\n        venue: \"Tool (open-source)\"\n        year: 2019\n        relation: building-block\n        summary: \"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\"\n\n      - title: \"code2vec: Learning Distributed Representations of Code\"\n        authors: \"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\"\n        venue: POPL\n        year: 2019\n        relation: background\n        summary: \"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\"\n\n      - title: \"code2seq: Generating Sequences from Structured Representations of Code\"\n        authors: \"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\"\n        venue: ICLR\n        year: 2019\n        relation: background\n        summary: \"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\"\n\n      - title: \"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\"\n        authors: \"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\"\n        venue: SANER\n        year: 2020\n        relation: background\n        summary: \"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\"\n\n      - title: \"GraphCodeBERT: Pre-training Code Representations with Data Flow\"\n        authors: \"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\"\n        venue: ICLR\n        year: 2021\n        relation: background\n        summary: \"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\"\n\n      - title: \"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\"\n        authors: \"Shahd Seddik, Fatemeh Fard\"\n        venue: arXiv\n        year: 2026\n        relation: contrast\n        summary: \"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\"\n\n      - title: \"ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimization\"\n        authors: \"Chris Cummins, Zacharias V. Fisches, Tal Ben-Nun, Torsten Hoefler, Michael FP O'Boyle, Hugh Leather\"\n        venue: ICML\n        year: 2021\n        relation: background\n        summary: \"语言无关的全程序图表示（control-flow + data-flow + call relations），证明整程序结构表示可学习且有效。StructFuse 使用 inter-procedural data-flow 的概念根基。\"\n\n      - title: \"CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion\"\n        authors: \"Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, Hantian Ding, Ming Tan, Nihal Jain, Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia, Dan Roth, Bing Xiang\"\n        venue: NeurIPS\n        year: 2023\n        relation: background\n        summary: \"多语言 cross-file 代码补全 benchmark，用静态分析确定需 cross-file 依赖的补全目标。验证了跨文件上下文对代码任务的关键性。\"\n\n  # ==========================================================================\n  # Category 5: Code Embeddings / Code Search\n  # ==========================================================================\n  code_embeddings_search:\n    description: \"代码嵌入模型和代码搜索方法\"\n    papers:\n\n      - title: \"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\"\n        authors: \"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\"\n        venue: arXiv\n        year: 2019\n        relation: background\n        summary: \"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\"\n\n      - title: \"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\"\n        authors: \"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\"\n        venue: \"EMNLP (Findings)\"\n        year: 2020\n        relation: background\n        summary: \"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\"\n\n      - title: \"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\"\n        authors: \"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\"\n        venue: ACL\n        year: 2022\n        relation: background\n        summary: \"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\"\n\n      - title: \"StarCoder: May the Source Be with You!\"\n        authors: \"Raymond Li, Loubna Ben Allal, et al. (BigCode)\"\n        venue: TMLR\n        year: 2023\n        relation: building-block\n        summary: \"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\"\n\n      - title: \"Code Llama: Open Foundation Models for Code\"\n        authors: \"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\"\n        venue: arXiv\n        year: 2023\n        relation: background\n        summary: \"Meta 的代码大模型系列，基于 Llama 2 微调。\"\n\n      - title: \"Qwen2.5-Coder Technical Report\"\n        authors: \"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\"\n        venue: arXiv\n        year: 2024\n        relation: building-block\n        summary: \"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\"\n\n      - title: \"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\"\n        authors: \"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\"\n        venue: arXiv\n        year: 2024\n        relation: background\n        summary: \"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\"\n\n      - title: \"RepoFusion: Training Code Models to Understand Your Repository\"\n        authors: \"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\"\n        venue: arXiv\n        year: 2023\n        relation: background\n        summary: \"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\"\n\n      - title: \"BM25\"\n        authors: \"Stephen Robertson, Hugo Zaragoza\"\n        venue: \"Foundations and Trends in Information Retrieval\"\n        year: 2009\n        relation: baseline\n        summary: \"经典稀疏检索方法，StructFuse 的 baseline 之一。\"\n\n      - title: \"CoSQA: 20,000+ Web Queries for Code Search and Question Answering\"\n        authors: \"Junjie Huang, Duyu Tang, Linjun Shou, Ming Gong, Ke Xu, Daxin Jiang, Ming Zhou, Nan Duan\"\n        venue: ACL\n        year: 2021\n        relation: background\n        summary: \"20,000+ 真实 web 查询与 Python 代码配对的大规模数据集，弥合合成 benchmark 与真实开发者需求的差距。\"\n\n  # ==========================================================================\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\n  # ==========================================================================\n  graph_guided_inference:\n    description: \"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\"\n    papers:\n\n      - title: \"LocAgent: Graph-Guided LLM Agents for Code Localization\"\n        authors: \"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\"\n        venue: ACL\n        year: 2025\n        relation: contrast\n        summary: \"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\"\n\n      - title: \"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\"\n        authors: \"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\"\n        venue: NAACL\n        year: 2025\n        relation: contrast\n        summary: \"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\"\n\n      - title: \"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\"\n        authors: \"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\"\n        venue: arXiv\n        year: 2025\n        relation: contrast\n        summary: \"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\"\n\n      - title: \"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\"\n        authors: \"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\"\n        venue: ICLR\n        year: 2025\n        relation: contrast\n        summary: \"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\"\n\n      - title: \"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\"\n        authors: \"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\"\n        venue: ASE\n        year: 2024\n        relation: contrast\n        summary: \"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\"\n\n      - title: \"GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion\"\n        authors: \"Xingliang Wang, Baoyi Wang, Chen Zhi, Junxiao Han, Xinkui Zhao, Jianwei Yin, Shuiguang Deng\"\n        venue: arXiv\n        year: 2025\n        relation: contrast\n        summary: \"构建 repo/module/function 三层多语义代码图（AST + CFG + DFG + call graph + class hierarchy），用 GNN-based hybrid retriever 做层次化检索增强代码补全。推理时图方法，与 StructFuse 训练时结构信号互补。\"\n\n  # ==========================================================================\n  # Category 7: Representation Geometry / Similarity Saturation\n  # ==========================================================================\n  representation_geometry:\n    description: \"预训练模型表示空间几何分析及各向异性修正方法\"\n    papers:\n\n      - title: \"Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere\"\n        authors: \"Tongzhou Wang, Phillip Isola\"\n        venue: ICML\n        year: 2020\n        relation: method-component\n        summary: \"定义 alignment/uniformity 两个对比学习关键属性，证明对比损失渐近优化两者。StructFuse 分析 embedding space 质量的理论工具。\"\n\n      - title: \"Representation Degeneration Problem in Training Natural Language Generation Models\"\n        authors: \"Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang, Tie-Yan Liu\"\n        venue: ICLR\n        year: 2019\n        relation: background\n        summary: \"揭示预训练 LM embedding 退化为窄锥的现象，StructFuse 观察到的 similarity saturation 可追溯到此。\"\n\n      - title: \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\"\n        authors: \"Kawin Ethayarajh\"\n        venue: EMNLP\n        year: 2019\n        relation: background\n        summary: \"实证发现 BERT/ELMo/GPT-2 表示占据窄锥（各向异性），StructFuse 使用的 code encoder 继承此问题。\"\n\n      - title: \"On the Sentence Embeddings from Pre-trained Language Models\"\n        authors: \"Bohan Li, Hao Zhou, Junxian He, Mingxuan Wang, Yiming Yang, Lei Li\"\n        venue: EMNLP\n        year: 2020\n        relation: method-component\n        summary: \"BERT-flow: 用 normalizing flows 将各向异性句子嵌入变换为各向同性高斯分布。\"\n\n      - title: \"SimCSE: Simple Contrastive Learning of Sentence Embeddings\"\n        authors: \"Tianyu Gao, Xingcheng Yao, Danqi Chen\"\n        venue: EMNLP\n        year: 2021\n        relation: method-component\n        summary: \"用 dropout 作为最小增强的对比学习，直接证明 contrastive learning 改善 anisotropy。StructFuse 可引用其 uniformity 分析框架。\"\n\n      - title: \"Whitening Sentence Representations for Better Semantics and Faster Retrieval\"\n        authors: \"Jianlin Su, Jiarun Cao, Weijie Liu, Yangyiwen Ou\"\n        venue: arXiv\n        year: 2021\n        relation: method-component\n        summary: \"白化操作增强句子表示各向同性并降维，与 StructFuse embedding post-processing 讨论相关。\"\n\n  # ==========================================================================\n  # Category 8: Infrastructure / Tools\n  # ==========================================================================\n  infrastructure:\n    description: \"StructFuse 依赖的核心基础设施和工具\"\n    papers:\n\n      - title: \"Billion-Scale Similarity Search with GPUs\"\n        authors: \"Jeff Johnson, Matthijs Douze, Herve Jegou\"\n        venue: \"IEEE Transactions on Big Data\"\n        year: 2021\n        relation: building-block\n        summary: \"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\"\n\n      - title: \"Tree-sitter: An Incremental Parsing System for Programming Tools\"\n        authors: \"Max Brunsfeld et al.\"\n        venue: \"Software (Zenodo DOI: 10.5281/zenodo.13375512)\"\n        year: 2018\n        relation: building-block\n        summary: \"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\"\n        note: \"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\"\n",
    "structuredPatch": [
      {
        "oldStart": 118,
        "oldLines": 6,
        "newStart": 118,
        "newLines": 62,
        "lines": [
          "         summary: \"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\"",
          "         note: \"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\"",
          " ",
          "+      - title: \"Representation Learning with Contrastive Predictive Coding\"",
          "+        authors: \"Aaron van den Oord, Yazhe Li, Oriol Vinyals\"",
          "+        venue: arXiv",
          "+        year: 2018",
          "+        relation: background",
          "+        summary: \"InfoNCE 损失函数：对比预测编码的无监督表示学习。StructFuse 训练目标的理论根基。\"",
          "+",
          "+      - title: \"Contrastive Learning with Hard Negative Samples\"",
          "+        authors: \"Joshua David Robinson, Ching-Yao Chuang, Suvrit Sra, Stefanie Jegelka\"",
          "+        venue: ICLR",
          "+        year: 2021",
          "+        relation: method-component",
          "+        summary: \"HCL: 可控 hard negative 采样，证明更难的 negatives 加速和改善学习，但暗示过度 hard 会导致问题。StructFuse difficulty analysis 的理论起点。\"",
          "+",
          "+      - title: \"Debiased Contrastive Learning\"",
          "+        authors: \"Ching-Yao Chuang, Joshua Robinson, Yen-Chen Lin, Antonio Torralba, Stefanie Jegelka\"",
          "+        venue: NeurIPS",
          "+        year: 2020",
          "+        relation: method-component",
          "+        summary: \"DCL: 去偏对比目标，修正 false negatives（同类样本被当作 negatives）问题。False negative 是 hard negative 过拟合的重要来源。\"",
          "+",
          "+      - title: \"Hard Negative Mixing for Contrastive Learning\"",
          "+        authors: \"Yannis Kalantidis, Mert Bulent Sariyildiz, Noe Pion, Philippe Weinzaepfel, Diane Larlus\"",
          "+        venue: NeurIPS",
          "+        year: 2020",
          "+        relation: method-component",
          "+        summary: \"MoCHi: feature-level hard negative 混合合成，开销极小。与 StructFuse 的 structure-based negative mining 形成对比。\"",
          "+",
          "+      - title: \"Understanding Hard Negatives in Noise Contrastive Estimation\"",
          "+        authors: \"Wenzheng Zhang, Karl Stratos\"",
          "+        venue: NAACL",
          "+        year: 2021",
          "+        relation: background",
          "+        summary: \"理论分析：用模型分布作为 negative 分布可减少梯度偏差。为 hard negative 作用提供理论解释。\"",
          "+",
          "+      - title: \"ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning\"",
          "+        authors: \"Jun Xia, Lirong Wu, Ge Wang, Jintao Chen, Stan Z. Li\"",
          "+        venue: ICML",
          "+        year: 2022",
          "+        relation: method-component",
          "+        summary: \"揭示图对比学习中 hard negative = false negative 的陷阱，提出基于概率的 hardness 区分 true/false negatives。与 StructFuse difficulty-overfitting 发现呼应。\"",
          "+",
          "+      - title: \"Difficulty-Based Sampling for Debiased Contrastive Representation Learning\"",
          "+        authors: \"Taeuk Jang, Xiaoqian Wang\"",
          "+        venue: CVPR",
          "+        year: 2023",
          "+        relation: method-component",
          "+        summary: \"WCL: 用 difficulty 分层采样 + bias-amplifying encoder 找信息性 hard negatives 同时避免 false negatives。与 StructFuse difficulty stratification 思路最接近。\"",
          "+",
          "+      - title: \"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion\"",
          "+        authors: \"Xingwei He, Yeyun Gong, A-Long Jin, Hang Zhang, Anlei Dong, Jian Jiao, Siu Ming Yiu, Nan Duan\"",
          "+        venue: EMNLP",
          "+        year: 2023",
          "+        relation: background",
          "+        summary: \"课程采样策略 + pseudo-query 文档扩展，解决双塔检索训练-推理差异。StructFuse 的 structure-grounded negatives 提供正交的课程形式。\"",
          "+",
          "   # ==========================================================================",
          "   # Category 3: Contrastive Learning for Code",
          "   # =========================================================================="
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 96_

验证最终文件完整性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "93387da0-b903-48aa-a552-1d6164c113c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPEUz3yJsYC13jbT82Hayp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1436,
      "cache_read_input_tokens": 56905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1436
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

_source line 97_

<details open><summary>🔧 Tool call — Bash · `toolu_01J4Ngw8QqvrfjQr8ee3xK6n`</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\nwith open('literature_map.yaml') as f:\n    data = yaml.safe_load(f)\ntotal = 0\nfor cat_name, cat_data in data['categories'].items():\n    count = len(cat_data['papers'])\n    total += count\n    print(f'{cat_name}: {count} papers')\nprint(f'---\\nTotal: {total} papers')\n\"",
  "description": "Validate YAML structure and count papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "7bf6634b-01ab-43c9-b93e-67176720bba2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPEUz3yJsYC13jbT82Hayp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1436,
      "cache_read_input_tokens": 56905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1436
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

_source line 98 · 2026-05-16T00:47:45.151Z_

<details><summary>↩ Tool result · `toolu_01J4Ngw8QqvrfjQr8ee3xK6n`</summary>

```text
code_retrieval_bug_fixing: 8 papers
hard_negative_mining: 14 papers
contrastive_code_learning: 6 papers
program_analysis_for_ml: 8 papers
code_embeddings_search: 10 papers
graph_guided_inference: 6 papers
representation_geometry: 6 papers
infrastructure: 2 papers
---
Total: 60 papers
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "ccf09be2-9345-4e74-940b-d1c711a427ad",
  "tool_use_result": {
    "stdout": "code_retrieval_bug_fixing: 8 papers\nhard_negative_mining: 14 papers\ncontrastive_code_learning: 6 papers\nprogram_analysis_for_ml: 8 papers\ncode_embeddings_search: 10 papers\ngraph_guided_inference: 6 papers\nrepresentation_geometry: 6 papers\ninfrastructure: 2 papers\n---\nTotal: 60 papers",
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

_source line 99_

YAML 验证通过，60 篇，结构完整。验证所有修改文件的关键改动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "5af52e2b-1a82-4d6c-83d2-404cfe95e2f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xoBXJzyST2R6jPHYnhDQQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 300,
      "cache_read_input_tokens": 58341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 300
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

_source line 100_

<details open><summary>🔧 Tool call — Bash · `toolu_01HkXgK8MW7BBsoweGshED33`</summary>

```json
{
  "command": "grep -n \"backbone\" artifacts/literature/related_work_references.md | head -5",
  "description": "Verify UniXcoder fix in references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "4d5c643a-c6b3-4452-b29b-db87abfd00d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xoBXJzyST2R6jPHYnhDQQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 300,
      "cache_read_input_tokens": 58341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 300
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

_source line 101 · 2026-05-16T00:47:49.306Z_

<details><summary>↩ Tool result · `toolu_01HkXgK8MW7BBsoweGshED33`</summary>

```text
68:Unified cross-modal pre-training leveraging AST and code comments via contrastive learning. **代码检索领域的重要 baseline（AST-based pre-training），但不是 StructFuse 的 backbone。StructFuse 使用 Qwen2.5-Coder-3B 和 StarCoder2-3B 作为 backbone encoder。**
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "a9767c13-5ef6-4d61-8e41-8dcf6d14eb32",
  "tool_use_result": {
    "stdout": "68:Unified cross-modal pre-training leveraging AST and code comments via contrastive learning. **代码检索领域的重要 baseline（AST-based pre-training），但不是 StructFuse 的 backbone。StructFuse 使用 Qwen2.5-Coder-3B 和 StarCoder2-3B 作为 backbone encoder。**",
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

_source line 102_

<details open><summary>🔧 Tool call — Bash · `toolu_01FvVa8oMjSR2YNfGGMThzdq`</summary>

```json
{
  "command": "grep -n \"reachable\\|share data-flow\" artifacts/paper_drafts/related_work_supplement.md",
  "description": "Verify dataflow negatives fix in supplement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "f83dcc1d-2ff4-4a1b-a2f5-e24ea67fd2a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xoBXJzyST2R6jPHYnhDQQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 300,
      "cache_read_input_tokens": 58341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 300
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

_source line 103 · 2026-05-16T00:47:50.586Z_

<details><summary>↩ Tool result · `toolu_01FvVa8oMjSR2YNfGGMThzdq`</summary>

```text
15:The curriculum learning paradigm for negative sampling has been further developed by CAPSTONE \cite{he2023capstone}, which addresses the training-inference discrepancy in dual-encoder dense retrieval. CAPSTONE expands documents with pseudo-queries during training and employs a curriculum sampling strategy that progressively improves the relevance between generated and real queries, effectively controlling negative difficulty through the query generation quality. This approach achieves strong results on both in-domain and out-of-domain retrieval benchmarks, reinforcing the finding that curriculum-based difficulty scheduling benefits dense retrieval training. While CAPSTONE focuses on bridging the training-inference gap through document expansion, our structure-grounded negatives provide an orthogonal form of curriculum: negatives that are hard because they do *not* share data-flow context with the positive (¬reachable_G(x,q)), not because of embedding proximity alone.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "e7c612e1-cfa6-41dd-8b38-c4fe622b97f7",
  "tool_use_result": {
    "stdout": "15:The curriculum learning paradigm for negative sampling has been further developed by CAPSTONE \\cite{he2023capstone}, which addresses the training-inference discrepancy in dual-encoder dense retrieval. CAPSTONE expands documents with pseudo-queries during training and employs a curriculum sampling strategy that progressively improves the relevance between generated and real queries, effectively controlling negative difficulty through the query generation quality. This approach achieves strong results on both in-domain and out-of-domain retrieval benchmarks, reinforcing the finding that curriculum-based difficulty scheduling benefits dense retrieval training. While CAPSTONE focuses on bridging the training-inference gap through document expansion, our structure-grounded negatives provide an orthogonal form of curriculum: negatives that are hard because they do *not* share data-flow context with the positive (¬reachable_G(x,q)), not because of embedding proximity alone.",
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

_source line 104_

全部 4 个 warning 修复完成。

---

## 修复总结

### Warning 1: GRACE 幻觉引用 — **论文真实存在，无需删除**
- WebSearch 确认：[GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion](https://arxiv.org/abs/2509.05980)
- 作者：Xingliang Wang 等，2025，`wang2025grace` 引用键正确
- `related_work_v1.md` 中的描述（多层代码图 + 层次化检索增强补全）与论文内容吻合
- 此前 `related_work_expansion_report.md` 错误地排除了该论文

### Warning 2: literature_map.yaml 同步 — **新增 21 篇**
| 分类 | 新增 |
|------|------|
| hard_negative_mining | +8（InfoNCE, HCL, DCL, MoCHi, Understanding HN, ProGCL, WCL, CAPSTONE） |
| contrastive_code_learning | +3（CoCoSoDa, SynCoBERT, ContraBERT） |
| program_analysis_for_ml | +2（ProGraML, CrossCodeEval） |
| code_embeddings_search | +1（CoSQA） |
| graph_guided_inference | +1（GRACE） |
| representation_geometry（新建） | +6（Alignment&Uniformity, RepDegen, Anisotropy, BERT-flow, SimCSE, Whitening） |

总计：39 → 60 entries，8 个分类

### Warning 3: UniXcoder 事实错误 — **已修正**
- 文件：`artifacts/literature/related_work_references.md` 第 68 行
- 删除"StructFuse 的 backbone encoder 之一"，改为"代码检索领域的重要 baseline，不是 StructFuse 的 backbone。StructFuse 使用 Qwen2.5-Coder-3B 和 StarCoder2-3B"

### Warning 4: Dataflow negatives 方向错误 — **已修正**
- 文件：`artifacts/paper_drafts/related_work_supplement.md` Supplement B
- "share data-flow context" → "do *not* share data-flow context (¬reachable_G(x,q))"

### 修改文件列表
1. `artifacts/literature/related_work_references.md` — UniXcoder 描述修正
2. `artifacts/paper_drafts/related_work_supplement.md` — dataflow negatives 方向修正
3. `literature_map.yaml` — 新增 21 篇论文 + 新建 representation_geometry 分类

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "uuid": "bce92f43-c565-4d89-91bb-e5ebbf447a4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HismcMwUnYtnV3qRHVokfj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 674,
      "cache_read_input_tokens": 58641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 674
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

_source line 105_

全部 4 个 warning 修复完成。

---

## 修复总结

### Warning 1: GRACE 幻觉引用 — **论文真实存在，无需删除**
- WebSearch 确认：[GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion](https://arxiv.org/abs/2509.05980)
- 作者：Xingliang Wang 等，2025，`wang2025grace` 引用键正确
- `related_work_v1.md` 中的描述（多层代码图 + 层次化检索增强补全）与论文内容吻合
- 此前 `related_work_expansion_report.md` 错误地排除了该论文

### Warning 2: literature_map.yaml 同步 — **新增 21 篇**
| 分类 | 新增 |
|------|------|
| hard_negative_mining | +8（InfoNCE, HCL, DCL, MoCHi, Understanding HN, ProGCL, WCL, CAPSTONE） |
| contrastive_code_learning | +3（CoCoSoDa, SynCoBERT, ContraBERT） |
| program_analysis_for_ml | +2（ProGraML, CrossCodeEval） |
| code_embeddings_search | +1（CoSQA） |
| graph_guided_inference | +1（GRACE） |
| representation_geometry（新建） | +6（Alignment&Uniformity, RepDegen, Anisotropy, BERT-flow, SimCSE, Whitening） |

总计：39 → 60 entries，8 个分类

### Warning 3: UniXcoder 事实错误 — **已修正**
- 文件：`artifacts/literature/related_work_references.md` 第 68 行
- 删除"StructFuse 的 backbone encoder 之一"，改为"代码检索领域的重要 baseline，不是 StructFuse 的 backbone。StructFuse 使用 Qwen2.5-Coder-3B 和 StarCoder2-3B"

### Warning 4: Dataflow negatives 方向错误 — **已修正**
- 文件：`artifacts/paper_drafts/related_work_supplement.md` Supplement B
- "share data-flow context" → "do *not* share data-flow context (¬reachable_G(x,q))"

### 修改文件列表
1. `artifacts/literature/related_work_references.md` — UniXcoder 描述修正
2. `artifacts/paper_drafts/related_work_supplement.md` — dataflow negatives 方向修正
3. `literature_map.yaml` — 新增 21 篇论文 + 新建 representation_geometry 分类

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 322322,
  "duration_api_ms": 335004,
  "num_turns": 21,
  "stop_reason": "end_turn",
  "session_id": "dc2aaa0e-560b-4efb-a687-1448e278c4b8",
  "total_cost_usd": 1.2324391500000003,
  "usage": {
    "input_tokens": 15449,
    "cache_creation_input_tokens": 47474,
    "cache_read_input_tokens": 558650,
    "output_tokens": 15544,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 47474,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 746,
        "cache_read_input_tokens": 58641,
        "cache_creation_input_tokens": 674,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 674
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 45440,
      "outputTokens": 4001,
      "cacheReadInputTokens": 223579,
      "cacheCreationInputTokens": 58203,
      "webSearchRequests": 3,
      "costUSD": 0.19055665,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 15449,
      "outputTokens": 15544,
      "cacheReadInputTokens": 558650,
      "cacheCreationInputTokens": 47474,
      "webSearchRequests": 0,
      "costUSD": 1.0418824999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "36d2487d-004e-4978-a4e4-a323b4559c3e"
}
```

</details>

---
