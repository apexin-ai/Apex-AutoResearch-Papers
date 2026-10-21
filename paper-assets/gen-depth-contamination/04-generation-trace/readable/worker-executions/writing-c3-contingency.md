# writing c3 contingency

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/workers/worker_writing_c3-contingency_20260514T075812.log`
- **Structured JSON:** [`a889c7ef5f11158429ea.json`](../../sessions/a8/a889c7ef5f11158429ea.json)

## Before a recorded user message

9 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
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
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "555702c5-2e9b-4782-bb23-63dc0f47fd86",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/memory/"
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
    "resetsAt": 1778763000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "e0e01bff-0492-483c-bb4c-c16fa8421a5c",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94"
}
```

---

### Assistant

_source line 4_

Let me first read the existing paper files to match the writing style and understand the defined commands.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "7478fc0f-2f82-4a7b-8df9-3c7853238a08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014AdNmGHz2fvEUztvYichtV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11787,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11787
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JmKioRHKwSpUMz55nzbFCG`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
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
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "50bd70ab-f0f6-43ff-9739-3aa543735182",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014AdNmGHz2fvEUztvYichtV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11787,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11787
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

_source line 6 · 2026-05-14T07:58:23.741Z_

<details><summary>↩ Tool result · `toolu_01JmKioRHKwSpUMz55nzbFCG`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "19b7d09a-d14b-4962-b2e0-e6507c8a9e77",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me read the existing paper files to understand the style, commands, and context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "3a28a8a8-37c2-4377-b678-1e2db38643be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qv8SRSvUu8w4nwKqZGa4Yh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1332,
      "cache_read_input_tokens": 23628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1332
      },
      "output_tokens": 41,
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

_source line 8_

<details open><summary>🔧 Tool call — Agent · `toolu_01TsdVJ2QWqgfCbe9w5RBkDT`</summary>

```json
{
  "description": "Read paper files for style",
  "subagent_type": "Explore",
  "prompt": "I need to read several files in the project /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ to understand the writing style and LaTeX commands used.\n\n1. Find and read any .tex files related to experiments_c3, conclusion, discussion sections\n2. Find the file where LaTeX commands like \\Kempirical, \\auc are defined (likely a preamble or macros file)\n3. Read any existing artifacts to understand the tone\n\nSearch in these directories:\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/\n\nLook for .tex files, especially conclusion.tex, discussion.tex, experiments_c3.tex, macros.tex, preamble.tex, commands.tex, or similar."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "a5d1d7ad-8c0b-4832-987e-9a671b04021f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qv8SRSvUu8w4nwKqZGa4Yh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1332,
      "cache_read_input_tokens": 23628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1332
      },
      "output_tokens": 41,
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

_source line 9_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a9b17499a9915dbf4",
  "tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "description": "Read paper files for style",
  "task_type": "local_agent",
  "prompt": "I need to read several files in the project /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ to understand the writing style and LaTeX commands used.\n\n1. Find and read any .tex files related to experiments_c3, conclusion, discussion sections\n2. Find the file where LaTeX commands like \\Kempirical, \\auc are defined (likely a preamble or macros file)\n3. Read any existing artifacts to understand the tone\n\nSearch in these directories:\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/\n\nLook for .tex files, especially conclusion.tex, discussion.tex, experiments_c3.tex, macros.tex, preamble.tex, commands.tex, or similar.",
  "uuid": "1d83b6da-90e3-406e-91bd-d75bca161457",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94"
}
```

---

## Round 1

54 recorded events

### User

_source line 10 · 2026-05-14T07:58:31.040Z_

I need to read several files in the project /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ to understand the writing style and LaTeX commands used.

1. Find and read any .tex files related to experiments_c3, conclusion, discussion sections
2. Find the file where LaTeX commands like \Kempirical, \auc are defined (likely a preamble or macros file)
3. Read any existing artifacts to understand the tone

Search in these directories:
- /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/
- /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/

Look for .tex files, especially conclusion.tex, discussion.tex, experiments_c3.tex, macros.tex, preamble.tex, commands.tex, or similar.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "d61c2f3e-ed9f-4b19-8df9-660c5520e6bf"
}
```

</details>

---

### System

_source line 11_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b17499a9915dbf4",
  "tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0509_7/p…",
  "usage": {
    "total_tokens": 18588,
    "tool_uses": 1,
    "duration_ms": 2077
  },
  "last_tool_name": "Glob",
  "uuid": "19ec32f7-5f50-400e-b138-c07fa8870f86",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94"
}
```

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Glob · `toolu_013iBcsdaoYsfV1W9Pu1d37H`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "cfdeec35-45b6-4e6a-990f-e2d0079d5861",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M84tQ1p6aThLtX1fVgTyBG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18579,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18579,
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

_source line 13 · 2026-05-14T07:58:33.155Z_

<details><summary>↩ Tool result · `toolu_013iBcsdaoYsfV1W9Pu1d37H`</summary>

```text
artifacts/dream_reports/dream_20260512T200328/best/paper.tex
artifacts/dream_reports/dream_20260512T200328/median/paper.tex
artifacts/dream_reports/dream_20260512T200328/worst/paper.tex
artifacts/dream_reports/dream_20260513T080728/best/paper.tex
artifacts/dream_reports/dream_20260513T080728/median/paper.tex
artifacts/dream_reports/dream_20260513T080728/worst/paper.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/experiments_c1.tex
artifacts/exp_015_neural_probe/paper/neural_probe_analysis.tex
docs/paper/related_work.tex
artifacts/drafts/neural_probe_analysis.tex
docs/paper/experiments_c3.tex
docs/paper/main.tex
docs/paper/appendix.tex
docs/paper/introduction.tex
docs/paper/experiments_c1.tex
docs/paper/method.tex
docs/paper/conclusion.tex
docs/paper/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "7ae1337a-c8c8-4ecb-8d3d-e7792665ac0a"
}
```

</details>

---

### System

_source line 14_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b17499a9915dbf4",
  "tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0509_7/p…",
  "usage": {
    "total_tokens": 18591,
    "tool_uses": 2,
    "duration_ms": 2384
  },
  "last_tool_name": "Glob",
  "uuid": "9f1c331b-52b0-445e-8fa2-4e2a6be6c796",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94"
}
```

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Glob · `toolu_01SVCanQJdHPYHjJtLD2hVuq`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/**"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "fafc5e93-f7d2-4220-88fd-d23c076571e2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M84tQ1p6aThLtX1fVgTyBG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18579,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18579,
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

_source line 16 · 2026-05-14T07:58:33.452Z_

<details><summary>↩ Tool result · `toolu_01SVCanQJdHPYHjJtLD2hVuq`</summary>

```text
artifacts/_project/report/related_work_structure.md
artifacts/_project/report/gpu_optimization_report.txt
artifacts/gpu_optimization_report.txt
artifacts/_project/report/claim_routes.md
artifacts/_project/report/theory_framework.md
artifacts/_project/report/full_study_plan.md
artifacts/_project/report/methodology_draft.md
artifacts/_project/report/figure_plan.md
artifacts/dream_reports/dream_20260512T200328/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260512T200328/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260512T200328/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260512T200328/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260512T200328/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T200328/best/experiment_data.json
artifacts/dream_reports/dream_20260512T200328/best/paper.tex
artifacts/dream_reports/dream_20260512T200328/best/paper.aux
artifacts/dream_reports/dream_20260512T200328/best/paper.out
artifacts/dream_reports/dream_20260512T200328/best/paper.pdf
artifacts/dream_reports/dream_20260512T200328/best/paper.log
artifacts/dream_reports/dream_20260512T200328/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260512T200328/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T200328/median/experiment_data.json
artifacts/dream_reports/dream_20260512T200328/median/paper.tex
artifacts/dream_reports/dream_20260512T200328/median/paper.aux
artifacts/dream_reports/dream_20260512T200328/median/paper.out
artifacts/dream_reports/dream_20260512T200328/median/paper.pdf
artifacts/dream_reports/dream_20260512T200328/median/paper.log
artifacts/dream_reports/dream_20260512T200328/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260512T200328/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T200328/worst/experiment_data.json
artifacts/dream_reports/dream_20260512T200328/worst/paper.tex
artifacts/dream_reports/dream_20260512T200328/worst/paper.aux
artifacts/dream_reports/dream_20260512T200328/worst/paper.out
artifacts/dream_reports/dream_20260512T200328/worst/paper.pdf
artifacts/dream_reports/dream_20260512T200328/worst/paper.log
artifacts/dream_reports/dream_20260512T200328/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260512T200328/logs/orchestrator.log
artifacts/dream_reports/dream_20260512T200328/best/review_report.md
artifacts/dream_reports/dream_20260512T200328/logs/review_best.log
artifacts/dream_reports/dream_20260512T200328/median/review_report.md
artifacts/dream_reports/dream_20260512T200328/logs/review_median.log
artifacts/dream_reports/dream_20260512T200328/worst/review_report.md
artifacts/dream_reports/dream_20260512T200328/logs/review_worst.log
artifacts/dream_reports/dream_20260512T200328/meta.yaml
artifacts/_project/report/literature_scan_2025_2026.md
artifacts/literature_scan_2025_2026.md
artifacts/_project/report/literature_positioning_notes.md
artifacts/_project/report/literature_positioning_notes_d23bf4.md
artifacts/literature_positioning_notes.md
artifacts/_project/chart/auc_heatmap.pdf
artifacts/figures/auc_heatmap.pdf
artifacts/_project/chart/feature_importance.pdf
artifacts/figures/feature_importance.pdf
artifacts/_project/chart/jsd_decay.pdf
artifacts/figures/jsd_decay.pdf
artifacts/exp005_4model_tau_matrix.json
artifacts/exp-005/data/exp005_4model_tau_matrix.json
artifacts/bootstrap_ci_4model.json
artifacts/exp-013/data/cross_transfer_matrix.csv
artifacts/exp-013/data/cross_transfer_matrix.json
artifacts/exp006_filtering_strategies.py
artifacts/exp006_continued_pretraining.py
artifacts/exp006_evaluate.py
artifacts/run_exp006.sh
artifacts/exp006_analyze.py
artifacts/dream_reports/dream_20260513T080728/logs/orchestrator.log
artifacts/dream_reports/dream_20260513T080728/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260513T080728/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260513T080728/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260513T080728/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260513T080728/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T080728/best/experiment_data.json
artifacts/dream_reports/dream_20260513T080728/best/paper_framing.md
artifacts/dream_reports/dream_20260513T080728/best/paper.tex
artifacts/dream_reports/dream_20260513T080728/best/paper.aux
artifacts/dream_reports/dream_20260513T080728/best/paper.out
artifacts/dream_reports/dream_20260513T080728/best/paper.pdf
artifacts/dream_reports/dream_20260513T080728/best/paper.log
artifacts/dream_reports/dream_20260513T080728/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260513T080728/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T080728/median/experiment_data.json
artifacts/dream_reports/dream_20260513T080728/median/paper_framing.md
artifacts/dream_reports/dream_20260513T080728/median/paper.tex
artifacts/dream_reports/dream_20260513T080728/median/paper.aux
artifacts/dream_reports/dream_20260513T080728/median/paper.out
artifacts/dream_reports/dream_20260513T080728/median/paper.pdf
artifacts/dream_reports/dream_20260513T080728/median/paper.log
artifacts/dream_reports/dream_20260513T080728/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260513T080728/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T080728/worst/experiment_data.json
artifacts/dream_reports/dream_20260513T080728/worst/paper_framing.md
artifacts/dream_reports/dream_20260513T080728/worst/paper.tex
artifacts/dream_reports/dream_20260513T080728/worst/paper.aux
artifacts/dream_reports/dream_20260513T080728/worst/paper.out
artifacts/dream_reports/dream_20260513T080728/worst/paper.pdf
artifacts/dream_reports/dream_20260513T080728/worst/paper.log
artifacts/dream_reports/dream_20260513T080728/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260513T080728/best/review_context.yaml
artifacts/dream_reports/dream_20260513T080728/best/review_report.md
artifacts/dream_reports/dream_20260513T080728/logs/review_best.log
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "0306e279-4a95-4bbd-9447-2e24258ac21e"
}
```

</details>

---

### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b17499a9915dbf4",
  "tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 18594,
    "tool_uses": 3,
    "duration_ms": 2641
  },
  "last_tool_name": "Bash",
  "uuid": "52967fc2-22b7-44c2-806c-1f3d1b25da4e",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94"
}
```

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01DDkrLCj621eYHLsTZKbs5o`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination -type f -name \"*macro*\" -o -name \"*preamble*\" -o -name \"*command*\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "eb875db7-aac9-4996-a126-a8a1e13837e3",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M84tQ1p6aThLtX1fVgTyBG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18579,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18579,
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

_source line 19 · 2026-05-14T07:58:33.886Z_

<details><summary>↩ Tool result · `toolu_01DDkrLCj621eYHLsTZKbs5o`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.venv/lib/python3.14/site-packages/pip/_internal/cli/req_command.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.venv/lib/python3.14/site-packages/pip/_internal/cli/__pycache__/req_command.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.venv/lib/python3.14/site-packages/pip/_internal/cli/__pycache__/index_command.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.venv/lib/python3.14/site-packages/pip/_internal/cli/__pycache__/command_context.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.venv/lib/python3.14/site-packages/pip/_internal/cli/__pycache__/base_command.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.venv/lib/python3.14/site-packages/pip/_internal/cli/base_command.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.venv/lib/python3.14/site-packages/pip/_internal/cli/command_context.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.venv/lib/python3.14/site-packages/pip/_internal/cli/index_command.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.venv/lib/python3.14/site-packages/pip/_internal/commands
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "8478b3c8-e2c3-46e3-8412-b58ded534725"
}
```

</details>

---

### System

_source line 20_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b17499a9915dbf4",
  "tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "description": "Reading docs/paper/main.tex",
  "usage": {
    "total_tokens": 22594,
    "tool_uses": 4,
    "duration_ms": 4538
  },
  "last_tool_name": "Read",
  "uuid": "ced998e3-e07f-402b-b606-c2a5f8256784",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94"
}
```

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_011ZMjDz4LXSYtxRxoYvrNze`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "ca9fc75a-ca85-42a1-8e79-fc9b87794d61",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CUmiN2D8TMSaUDjzeTF44m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3992,
      "cache_read_input_tokens": 18579,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3992,
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

_source line 22 · 2026-05-14T07:58:35.592Z_

<details><summary>↩ Tool result · `toolu_011ZMjDz4LXSYtxRxoYvrNze`</summary>

```text
1	% EMNLP 2026 Main — ARR May 2026
2	% Generational Depth Contamination
3	% Template: standard article class (swap to acl.sty for final submission)
4	\documentclass[11pt,a4paper]{article}
5	\usepackage[margin=1in]{geometry}
6	\usepackage{times}
7	\usepackage{graphicx}
8	\usepackage{amsmath}
9	\usepackage{amssymb}
10	\usepackage{amsthm}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{hyperref}
15	\usepackage[numbers]{natbib}
16	\usepackage{enumitem}
17	\usepackage{subcaption}
18	
19	\newcommand{\Kstar}{K^*}
20	\newcommand{\Kempirical}{K^*_{\text{empirical}}}
21	\newcommand{\Ktheory}{K^*_{\text{theory}}}
22	\newcommand{\auc}{\text{AUC}}
23	\newcommand{\jsd}{\text{JSD}}
24	
25	\title{Generational Depth Estimation of Recursive Synthetic Text:\\Measuring the Discrimination Boundary}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	% === Abstract ===
33	\begin{abstract}
34	Web-scale text corpora are increasingly contaminated by recursive synthetic content---text recursively generated across multiple generations. Information degrades monotonically per the Data Processing Inequality with each generation, yet no method estimates a document's generational depth. We introduce the first systematic framework for generational depth estimation. Our approach extracts 15 statistical features and classifies depth via Ordinal Binary Decomposition (OBD) with LightGBM, preserving ordinal structure. We empirically measure the discrimination boundary $\Kempirical$, the maximum depth at which adjacent generations remain statistically distinguishable. Across 4 model-mode configurations and 4 decoding strategies (8 conditions total) at the $\leq$1.5B parameter scale, we find $\Kempirical=2$ is consistent: bootstrap 95\% CI lower bounds for 1-vs-2 across the four model-mode configurations all exceed $\theta=0.60$ while all 2-vs-3 CI upper bounds fall below it; decoding strategies likewise yield $\auc$ above $\theta$ at 1-vs-2 and below at 2-vs-3. Cross-model transfer shows classifiers retain 80--92\% accuracy across continuation-mode generators, with binary (0-vs-1) $\auc$ exceeding 0.96, indicating depth features are largely text-intrinsic. Preliminary neural probing on one dataset yields $\Kempirical^{\text{neural}}=3$, suggesting our 15-feature $\Kempirical=2$ is a representation-dependent lower bound. Frontier LLMs achieve ${\sim}88\%$ binary detection but only ${\sim}33\%$ five-class depth accuracy---below our OBD classifier's 38.6\%---confirming depth estimation as a non-trivial task requiring specialized features. Our findings motivate a three-tier taxonomy (human / generation-1 / generation-2+) for depth-aware data curation; we investigate whether this coarse ordinal signal enables graduated filtering that outperforms binary approaches discarding all synthetic content indiscriminately.
35	\end{abstract}
36	
37	% === Section 1: Introduction ===
38	\input{introduction}
39	
40	% === Section 2: Related Work ===
41	\input{related_work}
42	
43	% === Section 3: Method ===
44	\input{method}
45	
46	% === Section 4: Experiments ===
47	\input{experiments_c1}
48	
49	% === Section 4.x: Graduated Filtering (DEFERRED) ===
50	% \input{experiments_c3}
51	
52	% === Section 5: Discussion ===
53	\input{discussion}
54	
55	% === Section 6: Conclusion ===
56	\input{conclusion}
57	
58	\bibliographystyle{plainnat}
59	\bibliography{references}
60	
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
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "e120a57c-65c5-4484-a692-53efaa2df23c"
}
```

</details>

---

### System

_source line 23_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b17499a9915dbf4",
  "tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "description": "Reading docs/paper/conclusion.tex",
  "usage": {
    "total_tokens": 22596,
    "tool_uses": 5,
    "duration_ms": 4718
  },
  "last_tool_name": "Read",
  "uuid": "dedad081-21ef-460c-ab5a-439a82275206",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94"
}
```

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01GbCkPYpVtMVVxDKZaTarDP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "af12896b-30e5-4a87-8b7b-ff22f2680194",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CUmiN2D8TMSaUDjzeTF44m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3992,
      "cache_read_input_tokens": 18579,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3992,
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

_source line 25 · 2026-05-14T07:58:35.771Z_

<details><summary>↩ Tool result · `toolu_01GbCkPYpVtMVVxDKZaTarDP`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	% === Contribution 1: K*=2 consistent boundary ===
5	% Sources: exp_007 (bootstrap CI + permutation), exp_001/exp_002/exp_017/mvp_pilot (model-mode), exp_003 (decoding ablation)
6	We presented the first systematic measurement of the generational depth
7	discrimination boundary $\Kempirical$ for recursive synthetic text.
8	Across three model architectures in four model-mode configurations
9	(Pythia-1.4B and OLMo-1B in continuation mode; Qwen2.5-1.5B-Instruct in both
10	continuation and rewrite modes) and 4 decoding strategies---totaling 8
11	conditions---we establish $\Kempirical = 2$ as a consistent boundary:
12	classifiers reliably distinguish adjacent generations up to depth~2, but all
13	deeper pairs fall below the operational threshold $\theta = 0.60$.
14	For the four model-mode configurations, bootstrap 95\% confidence intervals
15	and permutation tests confirm statistical significance at the 1v2 boundary
16	($p \leq 0.002$ for all four); the most marginal case, Qwen-continuation,
17	yields a CI lower bound of 0.6015, exceeding $\theta$ by only 0.15\,pp.
18	All four decoding configurations (greedy, nucleus, $T{=}0.70$, $T{=}1.2$)
19	likewise yield 1v2 point-estimate $\auc$ above $\theta$.
20	The 0v1 boundary is near-perfectly separable ($\auc > 0.99$), followed by a
21	sharp ${\sim}$30\,pp drop at 1v2 ($\auc$: 0.6112--0.7039 across all
22	conditions), while all 2v3 pairs fall below~$\theta$.
23	Recursive generation thus acts as a severely lossy channel whose discriminable
24	statistical fingerprint is exhausted within two steps.
25	
26	% === Contribution 2: Ordinal depth estimation framework ===
27	% Sources: exp_010 (OBD vs baselines), exp_013 (cross-model transfer), exp_005 (feature degradation), exp_011 (LLM zero-shot)
28	To operationalize depth estimation, we introduced an ordinal binary
29	decomposition (OBD) framework pairing 15 hand-crafted statistical features
30	with LightGBM classifiers.
31	Cross-model transfer experiments demonstrate 80--92\% accuracy retention
32	across continuation-mode model pairs, with
33	Pythia$\leftrightarrow$OLMo achieving 90--92\% and 0v1 transfer $\auc$
34	exceeding 0.96 across all tested model pairs---indicating that depth signals are largely
35	text-intrinsic rather than generator-specific.
36	Feature degradation orderings are consistent across architectures
37	(Spearman $\rho \geq 0.85$), with surprisal-variance features dominating
38	uniformly, suggesting that the two-step information loss is governed by the
39	autoregressive mechanism itself.
40	As a reference point, frontier LLMs (GPT-5.5, Claude Opus~4.6) achieve
41	${\sim}$88\% binary human-vs.-synthetic accuracy but only ${\sim}$33\% on
42	5-class depth estimation, below OBD-LightGBM's 38.6\%---confirming that
43	fine-grained depth discrimination requires specialized statistical features
44	rather than general language understanding.
45	A preliminary neural probing experiment suggests that this operational bound is not tight: a frozen Qwen2.5-1.5B encoder paired with an MLP classifier achieves $\Kempirical^{\text{neural}} = 3$ on the Qwen-continuation dataset (2v3 $\auc = 0.6195$ versus 0.5609 with hand-crafted features), indicating that learned representations recover depth signal beyond the 15-dimensional feature set.
46	This result, pending cross-model validation, provides initial evidence that $\Ktheory \geq 3$.
47	
48	% === Contribution 3: Graduated filtering (C3) ===
49	% Source: exp_006 (RUNNING — results pending)
50	The $\Kempirical = 2$ boundary implies a natural trichotomy---human (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\geq 2$)---that can be exploited for depth-aware data curation.
51	% TODO: exp-006 graduated filtering 具体结果填充。
52	% 预留内容：graduated filtering 利用三级分类法在 MMLU/HellaSwag 上的表现，
53	% 与 binary filtering 和 no-filter baseline 的对比。
54	
55	% === Limitations + Future Work ===
56	Our findings are bounded by the scale of models tested ($\leq$1.5B parameters), restriction to English C4 text, and the use of prompt-chain rather than retrain-chain protocols; $\Kempirical$ depends on the threshold $\theta$ and shifts with generation mode (continuation-mode configurations drop to $\Kempirical{=}1$ at $\theta{=}0.65$, while rewrite mode retains $\Kempirical{=}2$; Section~\ref{sec:limitations}); the 15-dimensional feature set yields $\Kempirical$ as an operational lower bound, and $\Ktheory$ may be strictly higher.
57	Several directions merit investigation: scaling to larger models (7B+) to test whether increased generation fidelity shifts the boundary; extending to multilingual and multi-domain corpora; establishing the relationship between prompt-chain and retrain-chain $\Kstar$ values, which would connect our measurements to the model collapse setting; incorporating few-shot or chain-of-thought prompting for LLM-based depth estimation; and extending the neural probe approach---which has yielded preliminary evidence of $\Kempirical^{\text{neural}} = 3$ on one dataset---through cross-model validation (Pythia, OLMo), bootstrap confidence intervals, multi-layer probing beyond the last hidden state, and comparison with fine-tuned (non-frozen) encoders to further narrow the gap between $\Kempirical$ and $\Ktheory$.
58	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "e172a302-e2e4-48a5-a10c-e99e0153a740"
}
```

</details>

---

### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b17499a9915dbf4",
  "tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "description": "Reading docs/paper/discussion.tex",
  "usage": {
    "total_tokens": 22598,
    "tool_uses": 6,
    "duration_ms": 4861
  },
  "last_tool_name": "Read",
  "uuid": "cb41f1c0-9175-4abd-8374-5571fcf3a770",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94"
}
```

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01MUnRWChC5kY2G3SovPTptd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "7e5610ef-944f-43c9-be6d-897ef037527d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CUmiN2D8TMSaUDjzeTF44m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3992,
      "cache_read_input_tokens": 18579,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3992,
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

_source line 28 · 2026-05-14T07:58:35.910Z_

<details><summary>↩ Tool result · `toolu_01MUnRWChC5kY2G3SovPTptd`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Theoretical Implications of $\Kempirical = 2$}
5	\label{sec:discuss_kstar}
6	
7	The Data Processing Inequality guarantees the existence of a finite $\Ktheory$ beyond which adjacent generations become indistinguishable (Section~\ref{sec:formulation}).
8	Our empirical result---$\Kempirical = 2$ consistently across all 8 tested configurations (4 model-mode combinations and 4 decoding strategies; Section~\ref{sec:kstar_boundary}, Figure~\ref{fig:auc_decay})---establishes that this boundary is not only finite but remarkably shallow at the $\leq$1.5B parameter scale.
9	
10	The shallowness of $\Kempirical$ is explained by the rate of information loss across generations.
11	The 0v1 boundary is near-trivially separable ($\auc > 0.99$ across all configurations; Table~\ref{tab:kstar_ci}), reflecting the large distributional gap between human text and first-generation synthetic text.
12	At the 1v2 boundary, $\auc$ drops by approximately 30 percentage points ($\auc$ range: 0.6112--0.7039 across all eight model$\times$decoding conditions; Table~\ref{tab:kstar_ci}, Figure~\ref{fig:auc_decay}; see also Figure~\ref{fig:s1_auc_decay_ci} in the Appendix), indicating that the majority of the discriminative signal is consumed in the first generation step.
13	By the 2v3 boundary, $\auc$ falls to 0.5496--0.5917 across all eight model$\times$decoding conditions (upper bound from nucleus $p{=}0.9$ decoding; Figure~\ref{fig:auc_decay})---below the operational threshold $\theta = 0.60$---and deeper pairs converge toward chance.
14	Recursive generation thus acts as a severely lossy channel whose information bottleneck is traversed within two steps.
15	
16	The feature degradation analysis (Section~\ref{sec:feature_degradation}) provides mechanistic evidence for this rapid collapse.
17	The most discriminative features---surprisal variance (\texttt{surp\_d1\_std}, \texttt{surp\_std}) and its derivatives---all capture the heterogeneity of token-level predictability.
18	Human text exhibits high surprisal variance reflecting diverse syntactic structures and unpredictable discourse patterns.
19	The first generation step smooths this variance substantially, replacing high-surprisal tokens and atypical constructions with more predictable alternatives; the second step reduces the remaining variance to near-floor levels, leaving insufficient statistical fingerprint for reliable adjacent-depth discrimination.
20	Crucially, this degradation ordering is consistent across model families (Spearman $\rho \geq 0.85$ for all continuation-mode pairs; Table~\ref{tab:top_features}), suggesting that the two-step information loss is governed by the autoregressive generation mechanism itself rather than by model-specific biases.
21	
22	This pattern aligns with findings from the model collapse literature.
23	Shumailov et al.~\cite{shumailov2024collapse} observed that tail-distribution degradation is most acute in the earliest generations, with minority modes vanishing before the output distribution stabilizes.
24	Dohmatob et al.~\cite{dohmatob2024model} derived scaling laws demonstrating that tail probability mass is lost at rates predictable from model and data scale.
25	Our $\Kempirical = 2$ provides a complementary, classifier-based measurement of this phenomenon: the information-theoretic discrimination boundary is reached after just two generation steps.
26	Alemohammad et al.~\cite{alemohammad2024selfconsuming} proved convergence to a fixed point for self-consuming generative models; $\Kempirical = 2$ indicates that, operationally, the approach to this fixed point is rapid enough that adjacent-generation distinctions collapse within two steps.
27	
28	Importantly, $\Kempirical = 2$ is an \emph{operational} lower bound conditioned on the 15-dimensional hand-crafted feature set; the \emph{theoretical} boundary $\Ktheory$ may be strictly higher.
29	Preliminary evidence from a neural probing experiment supports this distinction.
30	A frozen Qwen2.5-1.5B encoder (1536-dimensional last-layer representations) paired with a lightweight MLP classifier (Table~\ref{tab:s7_neural_probe}) achieves 2v3 $\auc = 0.6195$ ($\text{std} = 0.0094$) on the Qwen-continuation dataset, exceeding the $\theta = 0.60$ threshold that the same dataset's LightGBM classifier fails to cross ($\auc = 0.5609$; Section~\ref{sec:kstar_boundary}).
31	This yields $\Kempirical^{\text{neural}} = 3$: the learned representation recovers one additional discriminable boundary that the hand-crafted features miss.
32	The improvement is concentrated at the 2v3 pair ($+$5.86\,pp over LightGBM); at the already-separable 1v2 boundary the neural probe achieves 0.6983 versus 0.6112, a substantial gain but one that does not alter the boundary determination.
33	At 3v4, the neural probe reaches $\auc = 0.5930$---below $\theta$ but closer to the threshold than any hand-crafted configuration---suggesting that a still richer representation might push the boundary further.
34	The lossy-channel narrative remains intact: even with 1536-dimensional frozen representations, the discrimination boundary extends to only three steps, confirming that the information bottleneck of recursive generation is shallow even with substantially richer representations.
35	These results are preliminary: they cover a single model-dataset pair (Qwen-continuation) and lack bootstrap confidence intervals; cross-model validation on Pythia and OLMo is pending.
36	
37	The invariance of $\Kempirical = 2$ across decoding strategies merits emphasis.
38	Greedy decoding, nucleus sampling ($p{=}0.9$), $T{=}0.7$, and $T{=}1.2$ all yield $\Kempirical = 2$ (Figure~\ref{fig:auc_decay}; Table~\ref{tab:s2_decoding}), with 1v2 $\auc$ spanning a narrow range of [0.6866, 0.7039].
39	Higher decoding entropy modestly increases signal strength ($\auc_{1,2}$: 0.69 greedy $\to$ 0.70 at $T{=}1.2$) but does not shift the boundary.
40	This robustness suggests that $\Kempirical$ is governed by the fundamental information bottleneck of the generation process rather than by surface-level properties of the sampling algorithm.
41	
42	\subsection{Implications of Cross-Model Transfer}
43	\label{sec:discuss_transfer}
44	
45	The cross-model transfer results (Section~\ref{sec:transfer}) indicate that depth signals are largely encoded in text-level statistical properties rather than generator-specific artifacts.
46	Classifiers trained on Pythia-1.4B and evaluated on OLMo-1B retain 90--92\% of within-model accuracy, and the broader continuation-mode transfer matrix shows 80--92\% retention across all model pairs (Table~\ref{tab:transfer_matrix}; see Table~\ref{tab:s1_transfer} for the full matrix).
47	At the 0v1 boundary, cross-model $\auc$ exceeds 0.96 across all tested model pairs, confirming that binary contamination detection is fully transferable across the tested generators.
48	
49	The practical implication is direct: a single depth classifier trained on one model's outputs can be deployed to estimate generational depth for texts produced by other models, without model-specific retraining.
50	This transferability extends the utility of depth estimation to open-web settings where the generating model is unknown---precisely the scenario where depth-aware data curation is most needed.
51	
52	Two caveats bound this conclusion.
53	First, the text-intrinsic component dominates, as evidenced by high cross-model transfer retention (80--92\% across continuation-mode pairs), yet a nontrivial model-specific residual persists.
54	The Pythia$\leftrightarrow$OLMo pair, which spans different architectures and training corpora, achieves the highest cross-family retention (90--92\%), consistent with the depth signal being largely architecture-agnostic within continuation mode.
55	Second, Qwen-continuation$\leftrightarrow$OLMo retention (80--85\%) is lower than Pythia$\leftrightarrow$OLMo (90--92\%), indicating that model family similarity modulates transfer even among continuation-mode configurations.
56	
57	\subsection{Feature Importance Across Decoding Strategies}
58	\label{sec:discuss_features}
59	
60	While $\Kempirical = 2$ is invariant to decoding strategy (4/4 configurations), the feature importance ordering is not uniformly consistent.
61	Greedy decoding and $T{=}0.7$ share highly correlated feature rankings (Spearman $\rho = 0.914$), with top features dominated by vocabulary diversity measures: \texttt{self\_bleu}, \texttt{hapax\_ratio}, and \texttt{ttr}.
62	In contrast, greedy versus $T{=}1.2$ yields a lower correlation ($\rho = 0.53$, $p = 0.041$; suggestive but nonsignificant after Bonferroni correction for 6 pairwise comparisons), with $T{=}1.2$ promoting \texttt{hapax\_ratio}, \texttt{ttr}, and \texttt{surp\_skew} to the top ranks.
63	Notably, \texttt{freq\_entropy} rises from rank~10 under greedy ($\auc = 0.5139$) to rank~5 under $T{=}1.2$ ($\auc = 0.5905$), illustrating how high-entropy decoding amplifies frequency-distribution artifacts.
64	
65	This dissociation reveals an important distinction: the \emph{existence} of the depth boundary is robust, but the \emph{optimal feature subset} for detecting it depends on the sampling strategy.
66	High-entropy decoding amplifies frequency-distribution artifacts while attenuating vocabulary-diversity signals, shifting which text properties carry the most discriminative power without altering whether adjacent generations can be distinguished.
67	For practitioners, this implies that a general-purpose depth classifier should incorporate features from multiple groups---surprisal moments, vocabulary diversity, and frequency tail statistics---to maintain performance across unknown decoding conditions.
68	
69	The cross-model feature ordering (Section~\ref{sec:feature_degradation}) provides a complementary perspective: among continuation-mode models, single-feature $\auc$ rankings are highly consistent (Spearman $\rho \geq 0.85$), with surprisal-variance features---\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}---dominating uniformly.
70	A genuine limitation, however, is that depth-pair-level agreement weakens to $\tau \approx 0.37$ at the 1v2 boundary (Section~\ref{sec:feature_degradation}), indicating that the relative contribution of individual features at the discrimination boundary varies across models even when the aggregate ordering is shared.
71	
72	\subsection{Scale Considerations}
73	\label{sec:discuss_scale}
74	
75	Our experiments establish $\Kempirical = 2$ at the $\leq$1.5B parameter scale, providing the first empirical measurement of the generational depth boundary for language models.
76	This result constitutes a \emph{methodological lower bound}: the framework itself---15-dimensional token-level features, OBD-optimized classification, bootstrap confidence intervals, and permutation testing---is model-scale agnostic by construction.
77	All 15 features are computed from surface-level token statistics (surprisal moments, vocabulary diversity, frequency tail measures) without access to model internals, and the cross-model transfer results (80--92\% retention across architecturally distinct model families; Section~\ref{sec:transfer}) already demonstrate that the methodology generalizes across different architectures and training corpora at the tested scale.
78	
79	Scaling to larger models presents two possible outcomes, both of which reinforce rather than diminish the contribution.
80	If $\Kempirical > 2$ at 7B+ scales---as suggested by scaling laws showing that larger models exhibit slower tail-distribution degradation rates~\cite{dohmatob2024model, kaplan2020scaling}---then depth contamination becomes \emph{more} insidious: higher-fidelity generations would produce weaker depth signatures, making fine-grained detection more critical and the systematic framework we introduce more necessary.
81	Conversely, if $\Kempirical = 2$ persists at larger scales, our conclusions generalize directly.
82	In either case, the measurement methodology established here---the feature taxonomy, the $\Kstar$ estimation protocol, and the cross-model validation framework---provides the requisite infrastructure for characterizing depth boundaries at any scale.
83	The model collapse literature supports the expectation that depth-related phenomena are scale-persistent: Shumailov et al.~\cite{shumailov2024collapse} observed tail-mode collapse across model sizes, and Alemohammad et al.~\cite{alemohammad2024selfconsuming} proved fixed-point convergence for self-consuming generators without scale-dependent assumptions.
84	
85	We identify 7B-scale cross-scale validation as the immediate next step.
86	The experimental pipeline---data generation, feature extraction, and classifier evaluation---is fully implemented and directly applicable to larger models; only computational budget constrains this extension.
87	Critically, this limitation does not affect the validity of the $\Kempirical = 2$ result at $\leq$1.5B, which stands as the first empirical characterization of generational depth boundaries in language model outputs.
88	
89	\subsection{LLM Zero-Shot Baseline}
90	\label{sec:discuss_llm}
91	
92	Frontier LLMs provide a natural baseline for depth estimation.
93	On a 500-sample test set with 5 depth classes (depths 0--4), excluding depth~5 from the 6-class range used in the main feature-based experiments since depths $\geq 3$ are mutually indistinguishable ($\Kempirical = 2$), GPT-5.5 achieves 33.2\% accuracy (MAE = 1.10) and Claude Opus~4.6 achieves 33.1\% accuracy (MAE = 1.15)---both below the OBD-LightGBM baseline of 38.6\% (MAE = 1.11; see Table~\ref{tab:s3_llm_zeroshot} for per-depth confusion matrices).
94	Simultaneously, both models achieve approximately 88\% binary accuracy on the human-vs.-synthetic distinction (GPT-5.5: 87.8\%, Claude: 88.2\%).
95	
96	This gap between binary detection and depth estimation is informative.
97	Frontier LLMs can reliably determine \emph{whether} a text is machine-generated but cannot estimate \emph{how many generations of recursive processing} it has undergone.
98	Depth estimation requires sensitivity to subtle distributional shifts between adjacent generations---shifts orders of magnitude smaller than the human-vs.-machine gap.
99	The 15-dimensional statistical feature pipeline, despite its simplicity, captures these fine-grained shifts more effectively than frontier LLMs in a zero-shot setting.
100	This motivates the dedicated feature-engineering approach: the task demands specialized statistical sensitivity rather than general language understanding.
101	We evaluate only zero-shot prompting; few-shot or chain-of-thought strategies may narrow the gap and warrant future investigation.
102	
103	\subsection{Limitations}
104	\label{sec:limitations}
105	
106	We identify seven limitations that bound the generalizability of our findings.
107	
108	\emph{Model scale.}
109	All experiments use models at or below 1.5B parameters (Pythia-1.4B, OLMo-1B, Qwen2.5-1.5B-Instruct).
110	Larger models may produce higher-fidelity text with weaker depth signatures, potentially shifting $\Kempirical$ beyond~2.
111	
112	\emph{Prompt-chain versus retrain-chain.}
113	Our recursive generation protocol is a prompt-chain: the same fixed model repeatedly generates from the previous output.
114	Real-world model collapse involves retrain-chains, where models are retrained on data from earlier generations~\cite{shumailov2024collapse}.
115	Retrain-chains introduce additional degradation through training dynamics, potentially producing different $\Kstar$ values.
116	
117	\emph{Language and domain.}
118	All experiments use English text from the C4 corpus.
119	Depth dynamics may differ across languages, domains (e.g., code, scientific text), and source corpora with different distributional properties.
120	
121	\emph{Decoding coverage.}
122	We test four decoding strategies (greedy, nucleus $p{=}0.9$, $T{=}0.7$, $T{=}1.2$).
123	Other strategies---top-$k$ sampling, beam search, contrastive decoding---remain untested and may yield different feature importance patterns or boundary behavior.
124	
125	\emph{Threshold sensitivity.}
126	$\Kempirical$ depends on the operational threshold $\theta$.
127	$\Kempirical \geq 2$ across $\theta \in \{0.55, 0.60, 0.65\}$ for all four decoding strategies, rising to $\Kempirical = 3$ at $\theta = 0.55$ (all four 2v3 $\auc$ values exceed 0.55) and returning to $\Kempirical = 2$ at $\theta \in \{0.60, 0.65\}$.
128	At $\theta = 0.70$, three of four decoding configurations collapse to $\Kempirical = 1$; only the high-temperature setting ($T{=}1.2$) retains $\Kempirical = 2$, consistent with its elevated 1v2 $\auc$ (0.7039).
129	Beyond decoding parameters, the threshold sensitivity extends to generation mode: at $\theta{=}0.70$, $\Kempirical{=}1$ for all four model-mode configurations; at $\theta{=}0.65$, continuation-mode configurations already drop to $\Kempirical{=}1$, while rewrite mode retains $\Kempirical{=}2$.
130	Our current analysis primarily covers the decoding configuration axis.
131	The boundary is robust within a practical range but not invariant to threshold choice; our conclusions are conditioned on $\theta = 0.60$.
132	
133	\emph{Boundary marginality.}
134	The $\Kempirical = 2$ determination is statistically significant but numerically marginal at both ends.
135	On the lower side, Qwen-continuation's 1v2 CI lower bound (0.6015) exceeds $\theta = 0.60$ by only $+$0.15\,pp.
136	On the upper side, Qwen-rewrite's 2v3 CI upper bound (0.5991) falls below $\theta$ by only $-$0.09\,pp.
137	This narrow margin means that small changes in the feature set or classifier could shift the boundary---as the neural probe results confirm, where a richer representation pushes the 2v3 pair above $\theta$ on the Qwen-continuation dataset (Section~\ref{sec:discuss_kstar}).
138	Importantly, all eight boundary comparisons (four 1v2 and four 2v3) yield permutation $p < 0.01$, confirming that the statistical significance of the distinction is not in doubt---only its proximity to the operational threshold.
139	
140	\emph{Operational versus theoretical boundary.}
141	$\Kempirical$ is an operational lower bound that depends on the specific feature set and classifier.
142	$\Ktheory$ may be strictly greater; a more expressive classifier or richer feature representation could push $\Kempirical$ higher.
143	Preliminary neural probing results provide direct evidence for this gap: on the Qwen-continuation dataset, a frozen-encoder MLP achieves $\Kempirical^{\text{neural}} = 3$ (2v3 $\auc = 0.6195$) compared to $\Kempirical = 2$ with 15-dimensional hand-crafted features (2v3 $\auc = 0.5609$; Section~\ref{sec:kstar_boundary}).
144	This confirms that the 15D feature set does not saturate the available depth signal and that $\Ktheory \geq 3$.
145	However, the neural probe result rests on a single dataset and awaits cross-model validation and bootstrap confidence intervals before a firm revision of the headline $\Kempirical$ can be claimed.
146	
147	\emph{Feature representation.}
148	The 15-dimensional hand-crafted feature set, while interpretable and transferable, is not optimal.
149	A preliminary neural probing experiment demonstrates that frozen LLM embeddings (1536 dimensions) paired with a lightweight MLP push $\Kempirical$ from~2 to~3 on the Qwen-continuation dataset (Section~\ref{sec:discuss_kstar}), confirming that learned representations capture depth-discriminative patterns that statistical features miss.
150	The magnitude of the gain---2v3 $\auc$ rising from 0.5609 to 0.6195---indicates meaningful recoverable signal beyond what hand-crafted features extract.
151	Full characterization of this gap, including cross-model generalization and bootstrap uncertainty quantification, remains future work.
152	
153	\paragraph{Graduated Filtering.}
154	Results for graduated filtering will be added upon completion of ongoing experiments.
155	
156	\subsection{Broader Impact}
157	\label{sec:broader_impact}
158	
159	The $\Kempirical = 2$ boundary has implications beyond the immediate scope of depth classification.
160	
161	\paragraph{Synthetic data curation.}
162	The practical consequence of $\Kempirical = 2$ is a three-tier taxonomy of text quality: human-authored (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\geq 2$).
163	Texts at depth~$\geq 2$ are mutually indistinguishable and can be treated as a single category for curation purposes.
164	For practitioners filtering training data, this implies that a single round of synthetic rewriting suffices to make text statistically indistinguishable from text that has undergone multiple rounds of recycling---a form of one-wash laundering that limits the granularity of quality-based filtering.
165	This underscores the urgency of deploying depth-aware curation mechanisms before the first generation step, rather than relying on post-hoc detection.
166	Graduated filtering strategies that exploit this trichotomy may outperform binary human/synthetic filters, as the coarse ordinal signal (human / shallow / deep) captures the dominant axis of quality variation.
167	
168	\paragraph{Relation to model collapse.}
169	Shumailov et al.~\cite{shumailov2024collapse} and Alemohammad et al.~\cite{alemohammad2024selfconsuming} study model collapse under \emph{retrain-chains}, where models are iteratively trained on their own outputs.
170	Our prompt-chain protocol measures an adjacent but distinct phenomenon: the degradation of statistical distinguishability under recursive generation by a fixed model.
171	The rapid convergence we observe ($\Kempirical = 2$) is consistent with the theoretical prediction of convergence to a fixed point, but the precise relationship between prompt-chain $\Kempirical$ and retrain-chain convergence rates remains an open question.
172	If prompt-chain depth signals serve as an observable proxy for early-stage model collapse, depth estimation could provide a lightweight diagnostic for data curation pipelines without requiring expensive retraining experiments.
173	
174	\paragraph{AI text detection.}
175	Current AI text detection is predominantly binary: human versus machine.
176	Our results suggest that \emph{depth-aware} detection provides a strictly more informative signal.
177	The near-perfect 0v1 separability ($\auc > 0.99$) confirms that binary detection is reliable at this scale, but the 1v2 boundary ($\auc$: 0.61--0.70) reveals that first-generation text retains measurable statistical distance from deeper synthetic text.
178	This additional dimension---how many generations of processing a text has undergone---may prove valuable for provenance tracking and corpus quality assessment, where the binary human/AI label elides important distinctions between lightly and heavily recycled content.
179	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "d212469a-88f7-4531-9d93-f51adb367072"
}
```

</details>

---

### System

_source line 29_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b17499a9915dbf4",
  "tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "description": "Reading docs/paper/experiments_c3.tex",
  "usage": {
    "total_tokens": 31903,
    "tool_uses": 7,
    "duration_ms": 7691
  },
  "last_tool_name": "Read",
  "uuid": "4c6c6cdb-4495-415c-948c-2896ae4f6b93",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94"
}
```

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01FdYiraPh4jWfEjxdhLPnL9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "1197ed90-5b94-4501-aa88-ed37aea9b7d7",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019SKziTbZd5tyn5Q1znzmhb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9303,
      "cache_read_input_tokens": 22571,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9303,
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

_source line 31 · 2026-05-14T07:58:38.743Z_

<details><summary>↩ Tool result · `toolu_01FdYiraPh4jWfEjxdhLPnL9`</summary>

```text
1	\subsection{Graduated Filtering for Depth-Aware Data Curation}
2	\label{sec:graduated-filtering}
3	
4	The $\Kempirical = 2$ boundary establishes a three-tier taxonomy: human (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\geq 2$).
5	Binary filtering discards all synthetic content indiscriminately, sacrificing depth-1 text that retains most of the original signal.
6	We ask whether exploiting the coarse ordinal structure---weighting samples by predicted depth rather than applying a hard human/synthetic threshold---improves downstream language model quality.
7	
8	\paragraph{Filtering strategies.}
9	We compare six data curation strategies applied to a corpus of 30{,}000 documents (5{,}000 per depth level, depths 0--5) produced by the generational depth pipeline:
10	
11	\begin{enumerate}[label=(\roman*)]
12	  \item \textbf{No-filter}: all documents receive uniform weight (baseline).
13	
14	  \item \textbf{Binary-ours}: a LightGBM classifier trained on the 15-dimensional feature set distinguishes human (depth~0) from synthetic (depth~$\geq 1$).
15	  Each document receives weight $w = 1 - P(\text{synthetic})$.
16	  This represents the natural binary extension of our depth estimation framework.
17	
18	  \item \textbf{Binary-Drayson}: stratified importance resampling following Drayson et al.~\cite{drayson2025}, with $w_j = (1 - q(x_j))^b / Z$, $b = 1.5$, and oversampling factor $k = 1.5$.
19	  This is the strongest existing baseline for contamination-aware data curation.
20	
21	  \item \textbf{Graduated}: our proposed depth-aware strategy.
22	  The OBD-LightGBM classifier (Section~\ref{sec:classifier}) predicts a full depth distribution $P(d \mid \mathbf{x})$ for each document, from which we compute the expected depth $\hat{d} = \sum_d d \cdot P(d \mid \mathbf{x})$.
23	  Sample weights follow an exponential decay: $w = \exp(-\alpha \cdot \hat{d})$, where $\alpha$ controls the penalty for predicted depth.
24	  Low $\alpha$ values retain more synthetic content with gentle down-weighting; high $\alpha$ values approximate hard filtering.
25	  We sweep $\alpha \in \{0.1, 0.3, 0.5, 0.7, 0.9\}$.
26	
27	  \item \textbf{Surprisal}: a feature-based heuristic that retains documents whose mean surprisal exceeds the corpus median, exploiting the observation that deeper generations exhibit lower surprisal variance (Section~\ref{sec:feature_degradation}).
28	
29	  \item \textbf{DSIR}: Data Selection via Importance Resampling~\cite{xie2023dsir}, using bigram feature hashing with the depth-0 subcorpus as the reference distribution.
30	  This represents the state-of-the-art domain-matching baseline that is agnostic to generational depth.
31	\end{enumerate}
32	
33	\paragraph{Training setup.}
34	We fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\alpha_{\text{LoRA}} = 16$, target modules: \texttt{q\_proj}, \texttt{v\_proj}, dropout 0.05) on the filtered corpus for 3 epochs with learning rate $2 \times 10^{-5}$, batch size 4 with gradient accumulation 8, warmup ratio 0.1, and bfloat16 precision.
35	Documents are truncated to 512 tokens.
36	For strategies that produce continuous weights (graduated, binary-ours, binary-Drayson, DSIR), zero-weight samples are removed and the remaining samples are drawn via weighted random sampling; for binary strategies (surprisal), excluded samples are dropped outright.
37	Each strategy is evaluated across 5 random seeds (42, 123, 456, 789, 1024); the graduated strategy is further crossed with 5 $\alpha$ values, yielding 25 additional runs.
38	A base model baseline (no fine-tuning) is included for reference.
39	The total experimental budget is approximately 50 runs.
40	
41	\paragraph{Evaluation.}
42	We evaluate on two standard benchmarks via lm-eval-harness: MMLU (14{,}042 test examples, 0-shot) and HellaSwag (10{,}042 validation examples, 0-shot).
43	We report mean accuracy $\pm$ standard deviation across seeds.
44	
45	%% ====================================================================
46	\paragraph{Results.}
47	
48	\begin{table}[t]
49	\centering
50	\small
51	\caption{Downstream evaluation of filtering strategies.
52	MMLU and HellaSwag accuracy (0-shot) after LoRA continued pretraining on Qwen2.5-1.5B-Instruct with each strategy's filtered corpus.
53	Mean $\pm$ std over 5 seeds.
54	Best per-column result in bold; second-best underlined.
55	Graduated results use the best $\alpha$ from Table~\ref{tab:alpha_sweep}.}
56	\label{tab:filtering_main}
57	\begin{tabular}{lcc}
58	\toprule
59	\textbf{Strategy} & \textbf{MMLU} & \textbf{HellaSwag} \\
60	\midrule
61	Base model (no fine-tuning)
62	  & \textit{XX.X}
63	  & \textit{XX.X} \\
64	\midrule
65	No-filter
66	  & XX.X $\pm$ X.X
67	  & XX.X $\pm$ X.X \\
68	Binary-ours
69	  & XX.X $\pm$ X.X
70	  & XX.X $\pm$ X.X \\
71	Binary-Drayson
72	  & XX.X $\pm$ X.X
73	  & XX.X $\pm$ X.X \\
74	Graduated ($\alpha^*$)
75	  & \textbf{XX.X} $\pm$ X.X
76	  & \textbf{XX.X} $\pm$ X.X \\
77	Surprisal
78	  & XX.X $\pm$ X.X
79	  & XX.X $\pm$ X.X \\
80	DSIR
81	  & XX.X $\pm$ X.X
82	  & XX.X $\pm$ X.X \\
83	\bottomrule
84	\end{tabular}
85	\end{table}
86	
87	Table~\ref{tab:filtering_main} compares the six strategies on downstream benchmark accuracy.
88	% TODO: fill results and update narrative once exp-006 completes.
89	% Expected narrative structure:
90	% 1. No-filter baseline establishes the cost of training on contaminated data.
91	% 2. Binary strategies (ours + Drayson) improve over no-filter by removing synthetic content.
92	% 3. Graduated filtering outperforms binary by preserving depth-1 signal.
93	% 4. DSIR and surprisal provide reference points for non-depth-aware curation.
94	
95	%% ====================================================================
96	\paragraph{$\alpha$ sensitivity.}
97	
98	\begin{table}[t]
99	\centering
100	\small
101	\caption{Graduated filtering $\alpha$ sweep.
102	Mean accuracy $\pm$ std (5 seeds) for each decay parameter $\alpha$.
103	Lower $\alpha$ retains more synthetic content; higher $\alpha$ approximates hard filtering.}
104	\label{tab:alpha_sweep}
105	\begin{tabular}{ccc}
106	\toprule
107	$\alpha$ & \textbf{MMLU} & \textbf{HellaSwag} \\
108	\midrule
109	0.1 & XX.X $\pm$ X.X & XX.X $\pm$ X.X \\
110	0.3 & XX.X $\pm$ X.X & XX.X $\pm$ X.X \\
111	0.5 & XX.X $\pm$ X.X & XX.X $\pm$ X.X \\
112	0.7 & XX.X $\pm$ X.X & XX.X $\pm$ X.X \\
113	0.9 & XX.X $\pm$ X.X & XX.X $\pm$ X.X \\
114	\bottomrule
115	\end{tabular}
116	\end{table}
117	
118	Table~\ref{tab:alpha_sweep} shows the effect of the decay parameter $\alpha$ on downstream performance.
119	% TODO: fill results.
120	% Expected narrative:
121	% - Characterize the Pareto frontier: low alpha retains data volume but includes
122	%   more noise; high alpha is more selective but discards useful signal.
123	% - Identify optimal alpha and discuss whether the optimum is stable across seeds.
124	% - Connect to the K*=2 trichotomy: the graduated scheme effectively implements
125	%   a soft version of the human / gen-1 / gen-2+ partition, with alpha controlling
126	%   how aggressively deeper content is penalized.
127	
128	%% ====================================================================
129	\paragraph{Analysis.}
130	
131	% TODO: fill once results are available.
132	% Planned analysis points:
133	% (1) Does graduated filtering outperform binary? If so, this validates the
134	%     practical utility of the K*=2 trichotomy for data curation.
135	% (2) How does the optimal alpha relate to the discrimination boundary?
136	%     At alpha -> infinity, graduated degenerates to binary-ours (hard cutoff);
137	%     at alpha = 0, it degenerates to no-filter. The optimal alpha should
138	%     lie in between, reflecting the value of soft depth-aware weighting.
139	% (3) Which strategy benefits most from the seed averaging? If graduated
140	%     shows lower variance across seeds, it suggests the ordinal signal
141	%     provides a more stable curation criterion than binary classification.
142	% (4) Do the results differ between MMLU (knowledge-intensive) and
143	%     HellaSwag (commonsense reasoning)? Different tasks may exhibit
144	%     different sensitivity to data contamination depth.
145	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "a3891ab1-2ce6-4f16-9853-654947817286"
}
```

</details>

---

### System

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b17499a9915dbf4",
  "tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "description": "Reading docs/paper/method.tex",
  "usage": {
    "total_tokens": 31904,
    "tool_uses": 8,
    "duration_ms": 7827
  },
  "last_tool_name": "Read",
  "uuid": "082f6b1b-d6ba-4188-b3a8-380607059965",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94"
}
```

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01M98LHyCb3jLjcAuc6s4NrS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "e971f76d-79f0-4418-9ffc-64bc8ee1155f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019SKziTbZd5tyn5Q1znzmhb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9303,
      "cache_read_input_tokens": 22571,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9303,
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

_source line 34 · 2026-05-14T07:58:38.909Z_

<details><summary>↩ Tool result · `toolu_01M98LHyCb3jLjcAuc6s4NrS`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	% === Pipeline figure placeholder ===
5	% \begin{figure}[t]
6	% \centering
7	% \includegraphics[width=\columnwidth]{figures/pipeline.pdf}
8	% \caption{Overview of the generational depth estimation pipeline. Seed documents from C4 are recursively passed through a generation operator $G_\delta$ to produce a depth chain $X \to Y_1 \to \cdots \to Y_K$. Statistical features extracted by an external scorer model are fed to the OBD-LightGBM classifier for depth prediction.}
9	% \label{fig:pipeline}
10	% \end{figure}
11	
12	\subsection{Problem Formulation}
13	\label{sec:formulation}
14	
15	Recursive text generation naturally forms an iterated lossy channel.
16	Let $X$ denote an original human-written document drawn from a source distribution $\mathcal{D}$.
17	A generation operator $G_\delta = \text{LLM} + \delta$, parameterized by a decoding strategy $\delta$ (e.g., nucleus sampling with top-$p$ and temperature $T$), produces successive generations:
18	\begin{equation}
19	  X \to Y_1 \to Y_2 \to \cdots \to Y_K, \quad Y_k = G_\delta(Y_{k-1}),
20	  \label{eq:markov}
21	\end{equation}
22	where $Y_0 \triangleq X$.
23	The sequence $\{Y_k\}_{k=0}^K$ forms a Markov chain, since each generation depends only on its immediate predecessor.
24	
25	By the Data Processing Inequality (DPI), mutual information between the original document and successive generations is monotonically non-increasing:
26	\begin{equation}
27	  I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0.
28	  \label{eq:dpi}
29	\end{equation}
30	Since mutual information is bounded below by zero, this monotone sequence converges: the original signal degrades monotonically across generations.
31	Moreover, when the generation operator defines a finite-state Markov chain, the marginal distributions of adjacent generations converge to a shared stationary distribution, so that any classifier's ability to distinguish depth $k$ from depth $k{+}1$ must eventually degrade to chance.
32	Together, these arguments guarantee the existence of a finite $\Ktheory$ beyond which adjacent generations are indistinguishable---the \emph{information-theoretic discrimination boundary}.
33	
34	Motivated by this theoretical guarantee, we set out to \emph{empirically measure} the discrimination boundary.
35	We define an operational lower bound $\Kempirical$ via a classifier's ability to distinguish adjacent generations:
36	\begin{equation}
37	  \Kempirical = \max\{k : \text{CI}_{\text{lower}}^{95\%}(\auc_{k,k+1}) > \theta\},
38	  \label{eq:kstar}
39	\end{equation}
40	where $\auc_{k,k+1}$ is the pairwise area under the ROC curve for distinguishing depth $k$ from $k{+}1$, $\text{CI}_{\text{lower}}^{95\%}$ denotes the lower bound of a bootstrap 95\% confidence interval (1{,}000 resamples), and $\theta$ is an operational threshold justified in \S\ref{sec:kstar_operational}.
41	Since any specific classifier can only recover a subset of the information-theoretically available signal, $\Kempirical \leq \Ktheory$ by construction.
42	
43	\subsection{Feature Extraction}
44	\label{sec:features}
45	
46	We characterize each document with a 15-dimensional statistical feature vector, organized into four groups (Table~\ref{tab:features}).
47	All features are computed from token-level surprisal values and frequency statistics obtained via an external scorer model on the tokenized text.
48	
49	\begin{table}[t]
50	\centering
51	\small
52	\caption{The 15-dimensional feature set for generational depth estimation.}
53	\label{tab:features}
54	\begin{tabular}{lll}
55	\toprule
56	\textbf{Group} & \textbf{Feature} & \textbf{Description} \\
57	\midrule
58	\multirow{4}{*}{\parbox{2.2cm}{Surprisal\\moments}}
59	  & \texttt{surp\_mean}      & Mean token surprisal \\
60	  & \texttt{surp\_std}       & Std.\ dev.\ of token surprisal \\
61	  & \texttt{surp\_skew}      & Skewness of surprisal dist. \\
62	  & \texttt{surp\_kurt}      & Kurtosis of surprisal dist. \\
63	\midrule
64	\multirow{5}{*}{\parbox{2.2cm}{Surprisal\\derivatives}}
65	  & \texttt{surp\_d1\_mean}  & Mean 1st-order surprisal diff. \\
66	  & \texttt{surp\_d1\_std}   & Std.\ dev.\ of 1st-order diff. \\
67	  & \texttt{surp\_d1\_skew}  & Skewness of 1st-order diff. \\
68	  & \texttt{surp\_d2\_mean}  & Mean 2nd-order surprisal diff. \\
69	  & \texttt{surp\_d2\_std}   & Std.\ dev.\ of 2nd-order diff. \\
70	\midrule
71	\multirow{3}{*}{\parbox{2.2cm}{Vocabulary\\diversity}}
72	  & \texttt{ttr}             & Type-token ratio \\
73	  & \texttt{hapax\_ratio}    & Hapax legomena / unique tokens \\
74	  & \texttt{self\_bleu}      & 4-gram self-BLEU (within-document) \\
75	\midrule
76	\multirow{3}{*}{\parbox{2.2cm}{Frequency\\tail}}
77	  & \texttt{freq\_kurtosis}  & Kurtosis of token frequencies \\
78	  & \texttt{freq\_entropy}   & Token frequency entropy \\
79	  & \texttt{low\_freq\_ratio} & Fraction of rare tokens (freq $\leq 2$) \\
80	\bottomrule
81	\end{tabular}
82	\end{table}
83	
84	The first two groups capture the distribution and dynamics of token-level surprisal: moments summarize the shape of the surprisal distribution, while derivatives measure its local variability across token positions.
85	Vocabulary diversity features quantify lexical richness and repetitiveness: type-token ratio and hapax proportion reflect vocabulary breadth, while self-BLEU detects the increased intra-document $n$-gram overlap characteristic of deeper generations.
86	Frequency tail features characterize the token frequency distribution, capturing the well-documented phenomenon whereby recursive generation concentrates probability mass on high-frequency tokens and reduces the fraction of rare tokens \cite{shumailov2024collapse, dohmatob2024model}.
87	
88	We use hand-crafted statistical features rather than learned representations for three reasons: (1) they are directly interpretable, enabling degradation ordering analysis across model families; (2) they transfer across generators without retraining the feature extractor; and (3) they permit attribution of discriminative power to specific text properties, which is essential for understanding \emph{how} the depth signal degrades (full feature definitions in Table~\ref{tab:s5_features}).
89	
90	\subsection{Ordinal Binary Decomposition Classifier}
91	\label{sec:classifier}
92	
93	Generational depth is inherently ordinal: depth~1 is closer to depth~0 than depth~3 is.
94	We exploit this structure via \emph{Ordinal Binary Decomposition} (OBD), which decomposes a $(K{+}1)$-class ordinal classification problem into $K$ cumulative binary sub-classifiers.
95	The $k$-th sub-classifier estimates the exceedance probability:
96	\begin{equation}
97	  P(\text{depth} > k \mid \mathbf{x}), \quad k = 0, 1, \ldots, K{-}1,
98	\end{equation}
99	where $\mathbf{x} \in \mathbb{R}^{15}$ is the feature vector.
100	Each sub-classifier is an independent LightGBM model (hyperparameters in Table~\ref{tab:s6_lgbm_params}).
101	Class probabilities are recovered via the decomposition $P(Y{=}0) = 1 - P(Y{>}0)$ and $P(Y{=}k) = P(Y{>}k{-}1) - P(Y{>}k)$ for $k \geq 1$.
102	The predicted depth is:
103	\begin{equation}
104	  \hat{d}(\mathbf{x}) = \operatorname*{arg\,max}_{k} \; P(Y{=}k \mid \mathbf{x}).
105	\end{equation}
106	
107	We compared OBD-LightGBM against two alternatives: standard (unordered) multiclass LightGBM and ordinal logistic regression (LogisticAT).
108	OBD-LightGBM achieves lower mean absolute error (MAE) than multiclass LightGBM across all three model families (Qwen-rewrite: 0.984 vs.\ 1.016; Pythia: 1.107 vs.\ 1.140; OLMo: 1.147 vs.\ 1.181).
109	Ordinal logistic regression yields the lowest MAE overall (e.g., 0.911 on Qwen-rewrite) but at the cost of substantially degraded pairwise discrimination: mean pairwise $\auc$ of 0.4883 versus 0.6095 for OBD-LightGBM, averaged across the three families.
110	The low MAE of ordinal logistic regression stems from collapsing predictions toward central depths rather than improved discrimination---a pathology that renders it unsuitable when pairwise depth discriminability is the primary objective.
111	
112	\subsection{Operationalizing $\Kstar$}
113	\label{sec:kstar_operational}
114	
115	We set the operational threshold at $\theta = 0.60$.
116	This choice is grounded in the permutation test null distribution: across all model configurations, the 95th percentile of the null $\auc$ (obtained from 500 random label permutations) falls below 0.55.
117	A threshold of $\theta = 0.60$ therefore requires classification performance that is statistically significantly above chance at the $\alpha = 0.05$ level.
118	
119	Uncertainty is quantified via bootstrap resampling (1{,}000 resamples) of $\auc_{k,k+1}$ for each adjacent depth pair.
120	$\Kempirical$ is defined as the maximum depth $k$ for which $\text{CI}_{\text{lower}}^{95\%}(\auc_{k,k+1}) > \theta$ (Eq.~\ref{eq:kstar}).
121	
122	We examine threshold sensitivity at $\theta \in \{0.55, 0.60, 0.65, 0.70\}$.
123	At $\theta = 0.60$, $\Kempirical = 2$ holds across all four model configurations, with all permutation $p$-values for depth pair $1$ vs.\ $2$ at $p = 0.002$.
124	At the more lenient $\theta = 0.55$, $\Kempirical = 3$ uniformly across all four configurations.
125	At the stricter $\theta = 0.65$, only the rewrite configuration retains $\Kempirical = 2$; continuation-mode configurations yield $\Kempirical = 1$.
126	At $\theta = 0.70$, $\Kempirical = 1$ across all configurations.
127	This sensitivity profile confirms that $\Kempirical = 2$ is robust at our chosen threshold while remaining appropriately responsive to more stringent criteria.
128	
129	\subsection{Experimental Setup}
130	\label{sec:experimental_setup}
131	
132	We evaluate four model configurations spanning three model families and two generation modes (Table~\ref{tab:setup}).
133	
134	\begin{table}[t]
135	\centering
136	\small
137	\caption{Experimental configurations. All use the same seed corpus and evaluation protocol (5-fold group cross-validation grouped by seed document, $\auc$ as primary metric).}
138	\label{tab:setup}
139	\begin{tabular}{llcccc}
140	\toprule
141	\textbf{Config} & \textbf{Model} & \textbf{Mode} & \textbf{Decoding} & $N$ & \textbf{Depth} \\
142	\midrule
143	Qwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite      & $p{=}0.95$, $T{=}1.0$ & 5{,}000 & 0--5 \\
144	Qwen-cont & Qwen2.5-1.5B-Instruct & Continuation & $p{=}0.95$, $T{=}1.0$ & 5{,}000 & 0--5 \\
145	Pythia    & Pythia-1.4B            & Continuation & $p{=}0.95$, $T{=}1.0$ & 5{,}000 & 0--5 \\
146	OLMo      & OLMo-1B               & Continuation & $p{=}0.95$, $T{=}1.0$ & 5{,}000 & 0--5 \\
147	\bottomrule
148	\end{tabular}
149	\end{table}
150	
151	\paragraph{Seed corpus.}
152	We sample 5{,}000 documents from the C4 validation split, each truncated to 256 tokens, providing a controlled and reproducible starting point.
153	
154	\paragraph{Depth chain.}
155	Each seed document is recursively passed through the generation operator for $K = 5$ iterations, producing depths 0 (original) through 5.
156	This yields 30{,}000 documents per configuration (5{,}000 seeds $\times$ 6 depth levels).
157	
158	\paragraph{Decoding.}
159	All configurations use nucleus sampling with $p = 0.95$ and temperature $T = 1.0$, which we treat as the standard decoding condition.
160	The effect of alternative decoding strategies (greedy, lower temperature, different $p$) on $\Kempirical$ is examined in a separate ablation (\S\ref{sec:experiments}).
161	
162	\paragraph{Evaluation.}
163	We report pairwise $\auc$ for each adjacent depth pair $(k, k{+}1)$ under 5-fold group cross-validation (grouped by seed document to prevent cross-depth leakage), with bootstrap 95\% confidence intervals.
164	Ordinal MAE and Kendall's $\tau_b$ are reported as secondary metrics.
165	Dataset statistics are provided in Table~\ref{tab:s4_dataset_stats}; per-fold bootstrap results in Table~\ref{tab:s8_cv_folds}.
166	
167	\subsection{Generation Mode Control}
168	\label{sec:generation_mode_method}
169	
170	We investigate two generation modes that capture distinct recursive contamination scenarios:
171	
172	\paragraph{Continuation.}
173	The seed document is truncated to its first 128 tokens, and the LLM generates a continuation to 256 tokens.
174	This simulates scenarios where partial human text is extended by a model, a common pattern in collaborative writing and web content generation.
175	
176	\paragraph{Rewrite.}
177	The LLM receives the instruction ``Rewrite the following text while preserving its meaning'' and generates a full paraphrase.
178	This simulates content rewriting pipelines where existing text is rephrased at scale.
179	
180	We designate continuation as the \emph{canonical condition} for cross-model comparisons, based on three empirical findings from the cross-model transfer analysis.
181	First, classifiers trained on continuation-mode data retain 80--92\% accuracy when transferred across model families, versus only 61--63\% for rewrite-mode classifiers.
182	Second, the higher pairwise $\auc$ observed in rewrite mode ($\auc_{1,2} = 0.6955$ vs.\ $0.6112$ for continuation on Qwen) reflects instruction-following style artifacts rather than a stronger intrinsic depth signal, as evidenced by the poor cross-model transfer.
183	Third, the asymmetric transfer---continuation${\to}$rewrite retains 89\% performance versus rewrite${\to}$continuation at 82\%---indicates that continuation-mode features form a generalizable subset of what rewrite-mode classifiers exploit.
184	We therefore report continuation-mode results as primary and treat rewrite-mode results as an upper-bound ablation that quantifies the effect of mode-specific signal amplification.
185	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "9cc28921-992d-4eef-85f9-9d35022f731b"
}
```

</details>

---

### System

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b17499a9915dbf4",
  "tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "description": "Reading docs/paper/introduction.tex",
  "usage": {
    "total_tokens": 39504,
    "tool_uses": 9,
    "duration_ms": 10048
  },
  "last_tool_name": "Read",
  "uuid": "6aa9d3fb-3a0d-4e72-9813-0fefb3bd2a71",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94"
}
```

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01SsnSAGzEVDF9j6nQni411o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "1d82699c-8f02-4864-bb5c-589190011c08",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XwweC1Am9KXMVageRZWb3s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7598,
      "cache_read_input_tokens": 31874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7598,
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

_source line 37 · 2026-05-14T07:58:41.100Z_

<details><summary>↩ Tool result · `toolu_01SsnSAGzEVDF9j6nQni411o`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
5	Each pass through a language model constitutes a lossy channel: first-generation synthetic text retains much of the information structure of its human-written source, but within just two or three generations the output is qualitatively different---tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
6	This recursive degradation is not merely a theoretical concern; as synthetic text proliferates on the open web, training corpora inevitably ingest documents at varying generational depths, amplifying the risk of model collapse in downstream systems.
7	Yet the dominant paradigm in synthetic text detection treats all machine-generated text identically: a document is classified as human or synthetic, with no regard for how many rounds of recursive generation it has undergone.
8	This binary framing discards the generational depth dimension entirely.
9	
10	The gap cuts across three research communities.
11	Binary detection methods---including DivEye~\cite{basani2026diveye}, Min-K\%++~\cite{zhang2024minkpp}, and CoDeC~\cite{zawalski2026codec}---achieve strong human-versus-machine separation but produce no depth estimate.
12	The model collapse literature provides macro-level characterizations of recursive degradation: Shumailov et al.~\cite{shumailov2024collapse} demonstrated irreversible tail loss, Alemohammad et al.~\cite{alemohammad2024selfconsuming} proved convergence to a fixed point, and Schaeffer et al.~\cite{schaeffer2025position} organized the field into a taxonomy of eight definitions---yet none of these works provides a tool for estimating the generational depth of an individual text.
13	Data selection methods such as DSIR~\cite{xie2023dsir}, D4~\cite{tirumala2023d4}, and DoReMi~\cite{xie2023doremi} perform distribution matching to improve corpus quality but ignore recursive depth altogether.
14	The closest prior work is Drayson et al.~\cite{drayson2025}, who combined binary machine-generated text detection with stratified importance resampling to prevent model collapse---but their approach remains fundamentally binary.
15	No existing method estimates how many rounds of recursive generation a text has undergone, nor quantifies the boundary beyond which such estimation becomes infeasible.
16	
17	Recursive generation forms an iterated lossy channel; the Data Processing Inequality guarantees that the original signal degrades monotonically across generations, motivating the existence of a finite discrimination boundary $\Kstar$ beyond which adjacent generations become indistinguishable.
18	Markov chain convergence further implies that adjacent-generation distributions converge to a shared stationary distribution, so the classifier's task grows harder with each step.
19	Motivated by this theoretical structure, we set out to empirically measure $\Kempirical$---the maximum depth at which a classifier can reliably distinguish adjacent generations.
20	Our approach combines a 15-dimensional statistical feature pipeline---capturing surprisal moments, surprisal derivatives, vocabulary diversity, and frequency tail statistics---with an Ordinal Binary Decomposition (OBD) LightGBM classifier that respects the ordinal structure of depth.
21	We operationalize $\Kempirical$ as the deepest generation at which adjacent depths remain statistically distinguishable, with the bootstrap 95\% CI for pairwise $\auc$ exceeding an operational threshold $\theta = 0.60$ (formal definition in Section~\ref{sec:method}).
22	The choice of interpretable statistical features---rather than learned representations---is deliberate: it enables cross-generator transfer without retraining and permits attribution of discriminative power to specific text properties.
23	
24	Our contributions are organized into two groups.
25	The primary contribution is a systematic empirical characterization of $\Kempirical$ and its properties:
26	
27	\begin{enumerate}[label=(\alph*)]
28	  \item \textbf{$\Kempirical = 2$: a consistent boundary across all tested conditions.}
29	    Across 4 model-mode configurations and 4 decoding strategies (8 conditions total), all 1v2 bootstrap CI lower bounds exceed $\theta = 0.60$ and all 2v3 CI upper bounds fall below $\theta$, with permutation $p \leq 0.002$ for all boundary comparisons.
30	    The most marginal case is Qwen-continuation, where $\text{CI}_\text{lower} = 0.6015$.
31	    $\Kempirical = 2$ is thus established as a consistent discrimination boundary across all 8 tested conditions at the $\leq$1.5B scale.
32	    Higher decoding entropy increases signal strength ($\auc_{1,2}$: $0.69$ greedy $\to$ $0.70$ at $T{=}1.2$) but does not shift the boundary.
33	
34	  \item \textbf{Cross-model transfer.}
35	    Classifiers trained on one continuation-mode model and evaluated on another retain 80--92\% of within-model accuracy (Pythia$\leftrightarrow$OLMo: 90--92\%).
36	    At the 0v1 boundary, cross-model $\auc$ exceeds 0.96 across all tested model pairs.
37	    Transfer retention of 80--92\% suggests a large text-intrinsic component of the depth signal, rather than generator-specific artifacts.
38	
39	  \item \textbf{Degradation ordering consistency.}
40	    Single-feature $\auc$ rankings are highly correlated across continuation-mode models (Spearman $\rho \geq 0.85$), with the same top features---\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}---appearing across all three families.
41	    This shared ordering suggests a common degradation mechanism: each generation step smooths the token-level surprisal landscape.
42	    A limitation is that depth-pair-level agreement weakens ($\tau \approx 0.37$ at 1v2), indicating that individual feature contributions at the boundary vary across models.
43	
44	  \item \textbf{Generation mode analysis.}
45	    Within Qwen2.5-1.5B-Instruct, rewrite mode yields 1v2 $\auc = 0.6955$ versus continuation's $0.6112$ ($\Delta = +8.4$\,pp), but rewrite-trained classifiers transfer poorly across models (61--63\% retention versus 80--92\% for continuation).
46	    Cross-mode transfer is asymmetric: continuation$\to$rewrite retains 89\% while rewrite$\to$continuation retains 82\%.
47	    Continuation mode is therefore recommended as the canonical condition for cross-model comparisons.
48	\end{enumerate}
49	
50	\noindent As a secondary contribution, we investigate whether the coarse 3-class ordinal signal implied by $\Kempirical = 2$ enables \emph{graduated filtering}---depth-aware data curation that preserves mildly contaminated text (depth~1, retaining most original signal) while removing deeply corrupted text (depth~$\geq 3$)---and whether such filtering can improve upon binary approaches that discard all synthetic content indiscriminately (Section~\ref{sec:experiments}).
51	
52	The remainder of this paper is organized as follows.
53	Section~\ref{sec:related_work} reviews related work.
54	Section~\ref{sec:method} describes the method.
55	Section~\ref{sec:experiments} presents experimental results.
56	Section~\ref{sec:discussion} discusses implications and limitations.
57	Section~\ref{sec:conclusion} concludes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "48790365-d57b-47c6-ae2e-f4d3f43a84b5"
}
```

</details>

---

### System

_source line 38_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b17499a9915dbf4",
  "tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "description": "Running grep -r \"\\\\\\\\newcommand\\|\\\\\\\\def\" /home/ubuntu/.a…",
  "usage": {
    "total_tokens": 39505,
    "tool_uses": 10,
    "duration_ms": 10401
  },
  "last_tool_name": "Bash",
  "uuid": "4e741a5b-a09b-4b3d-be5e-06d60e776bba",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94"
}
```

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_016YSEFYs6eoffevD41ZcnQL`</summary>

```json
{
  "command": "grep -r \"\\\\\\\\newcommand\\|\\\\\\\\def\" /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/ 2>/dev/null | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "62cec4f2-ff4d-4c95-9ad8-d0025211da2d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XwweC1Am9KXMVageRZWb3s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7598,
      "cache_read_input_tokens": 31874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7598,
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

_source line 40 · 2026-05-14T07:58:41.521Z_

<details><summary>↩ Tool result · `toolu_016YSEFYs6eoffevD41ZcnQL`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.log:\defaultaddspace=\dimen177
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex:\newcommand{\Kstar}{K^*}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex:\newcommand{\Kempirical}{K^*_{\text{empirical}}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex:\newcommand{\Ktheory}{K^*_{\text{theory}}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex:\newcommand{\auc}{\text{AUC}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex:\newcommand{\jsd}{\text{JSD}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "818d27bf-c6fb-481a-b8b5-a7c213a2eff4"
}
```

</details>

---

### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b17499a9915dbf4",
  "tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "description": "Read paper files for style",
  "usage": {
    "total_tokens": 42035,
    "tool_uses": 11,
    "duration_ms": 12417
  },
  "last_tool_name": "mcp__agent-ml-research__read_project_file",
  "uuid": "82a5d405-84b5-45e0-b75f-d613d65a129c",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94"
}
```

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Fc2fHzHio9Acik5ZvabMcd`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "memory.md",
  "max_chars": 3000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "0e5f0978-6cbb-4ab4-bed9-c0609ba14cd4",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DP27sAohnNaKCJFXLMZ82Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2528,
      "cache_read_input_tokens": 39472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2528,
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

_source line 43 · 2026-05-14T07:58:43.476Z_

<details><summary>↩ Tool result · `toolu_01Fc2fHzHio9Acik5ZvabMcd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/memory.md\", \"content\": \"# Memory — gen-depth-contamination\\n\\n## 关键发现\\n\\n### K*(neural probe) 初步信号 = 3 [2026-05-14, 待验证]\\nexp-015 Qwen-cont 单数据集结果：K*=3（2v3 AUC=0.620 > θ=0.60）。但 Pythia/OLMo 因 OOM 丢失，**不可用于论文**。需重跑全 3 数据集 + bootstrap CI + permutation test 后才能写入论文。Director 明确指示：重跑前不更新论文。\\n\\n### exp-015 GPU OOM 教训 [2026-05-14]\\nexp-006 (15.5GB) + exp-015 (~9GB) 超出 4090D 24GB 显存。**硬规则**: 后续 GPU 并行必须用 `torch.cuda.max_memory_allocated()` 报告 peak VRAM，不用 nvidia-smi 静态快照（低估 peak usage）。GPU 共享实验必须独占，不并行。\\n\\n## 经验\\n\\n### AutoDL / westc-26893\\n- ModelScope CDN 下载 HuggingFace 模型比直连快（国内网络）\\n- source /etc/network_turbo 启用代理加速\\n- HF_HUB_DISABLE_XET=1 避免 xet_get 401 错误\\n- SSL 证书需设 REQUESTS_CA_BUNDLE + SSL_CERT_FILE\\n- conda 环境：source /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\n- 服务器别名从 autodl-4090d 改为 westc-26893（exp-003 cron 失败教训）\\n\\n### 实验管理\\n- submit_training_job 必须用于后台训练（不用 nohup）——自动 tmux + cron 监控\\n- Registry 状态必须顺序推进：PREPARING → PENDING → QUEUED → ALLOCATED → RUNNING → DONE\\n- GPU 编号始终从 0 开始（框架自动映射物理 GPU）\\n- **exp-006 实际速度 ~45.2min/run**（training 37.5min + eval 7.7min, range 44-49min）。99min 估计是错误的，monitor Worker 从实际 run 时间戳验证 45.2min 正确。\\n- exp-006 lm-eval 配置：batch_size=\\\"auto\\\", device=cuda:0, **MMLU 0-shot + HellaSwag 0-shot**（lm-eval 默认 0），eval 仅占 17% 总耗时 [2026-05-14]\\n- **exp-006 实际目录结构**：输出在 `outputs/exp006/`（非 `runs/exp006_graduated_filtering/`）。6 策略：`no-filter, binary-ours, binary-drayson, graduated, surprisal, dsir`。graduated 用 α∈{0.1,0.3,0.5,0.7,0.9} sweep。eval 结果格式：`scores.mmlu[\\\"acc,none\\\"]`, `scores.hellaswag[\\\"acc_norm,none\\\"]` [2026-05-14]\\n\\n### 论文写作\\n- Claude proxy model ID: 'claude-opus-4-6'（无 anthropic/ 前缀）\\n- 6 处 bib 条目有 hallucinated author first names，需验证所有 2025-2026 引用\\n- Qwen-cont/Qwen-rw 需一致使用 Qwen-continuation/Qwen-rewrite（running text）\\n- 90-92%（非 91-92%）for Pythia↔OLMo transfer retention\\n- discussion.tex 不应量化 \\\"70-85% text-intrinsic / 15-30% model-specific\\\" decomposition——数据不支持精确拆分\\n- Related Work 引用补充完成：probing classifiers (alain2017/conneau2018/belinkov2022/frank2001) + Strong Model Collapse (dohmatob2025) + Beyond Model Collapse (feng2025) + Fast-DetectGPT (bao2024) [2026-05-14]\\n- OBD 全称统一为 \\\"Ordinal Binary Decomposition\\\" [2026-05-14]\\n- $\\\\Kempirical^{\\\\text{neural}}$ 是 neural K* 的统一记号（非 $\\\\Kstar_{\\\\text{neural}}$）[2026-05-14]\\n\", \"total_chars\": 2238, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "8662b807-179e-4e1b-b887-0f7f7a846b93"
}
```

</details>

---

### System

_source line 44_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b17499a9915dbf4",
  "tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "description": "Running ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 42036,
    "tool_uses": 12,
    "duration_ms": 12804
  },
  "last_tool_name": "Bash",
  "uuid": "9252f911-c767-4814-b38b-e6619429dc99",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94"
}
```

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Bash · `toolu_01KkuRwJKdREk8p9qeCsc8pF`</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/report/ 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "4bce7a8c-e791-455a-822f-7ea3960866a8",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DP27sAohnNaKCJFXLMZ82Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2528,
      "cache_read_input_tokens": 39472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2528,
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

_source line 46 · 2026-05-14T07:58:43.915Z_

<details><summary>↩ Tool result · `toolu_01KkuRwJKdREk8p9qeCsc8pF`</summary>

```text
total 156K
-rw-r--r-- 1 ubuntu ubuntu 9.8K May 12 12:51 claim_routes.md
-rw-r--r-- 1 ubuntu ubuntu  17K May 12 16:50 figure_plan.md
-rw-r--r-- 1 ubuntu ubuntu  16K May 12 12:54 full_study_plan.md
-rw-r--r-- 1 ubuntu ubuntu 4.0K May 12 12:49 gpu_optimization_report.txt
-rw-r--r-- 1 ubuntu ubuntu  16K May 13 02:18 literature_positioning_notes.md
-rw-r--r-- 1 ubuntu ubuntu  16K May 13 02:18 literature_positioning_notes_d23bf4.md
-rw-r--r-- 1 ubuntu ubuntu  14K May 13 00:52 literature_scan_2025_2026.md
-rw-r--r-- 1 ubuntu ubuntu  20K May 12 16:28 methodology_draft.md
-rw-r--r-- 1 ubuntu ubuntu 9.3K May 12 12:49 related_work_structure.md
-rw-r--r-- 1 ubuntu ubuntu  11K May 14 06:55 reviewer_pass_round1.md
-rw-r--r-- 1 ubuntu ubuntu  11K May 12 12:52 theory_framework.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "8ee570ee-67a4-49e6-a78e-5e99bda42c21"
}
```

</details>

---

### System

_source line 47_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a9b17499a9915dbf4",
  "tool_use_id": "toolu_01TsdVJ2QWqgfCbe9w5RBkDT",
  "status": "completed",
  "output_file": "",
  "summary": "Read paper files for style",
  "usage": {
    "total_tokens": 44059,
    "tool_uses": 12,
    "duration_ms": 29148
  },
  "uuid": "8a462e2a-3192-4e7f-a658-0bd8f4b59fcc",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94"
}
```

---

### Tool result

_source line 48 · 2026-05-14T07:59:00.192Z_

<details><summary>↩ Tool result · `toolu_01TsdVJ2QWqgfCbe9w5RBkDT`</summary>

````text
Excellent! Now I have a comprehensive understanding of the project. Let me compile a final summary report:

## Summary: LaTeX Writing Style and Commands for gen-depth-contamination Project

### File Locations and Structure

**Primary LaTeX Files in `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/`:**
- `main.tex` - Document root with preamble and macro definitions
- `conclusion.tex` - Conclusion section
- `discussion.tex` - Discussion section (7 subsections with detailed analysis)
- `experiments_c3.tex` - Graduated filtering experiments (incomplete, with TODO placeholders)
- `method.tex` - Method section with formal problem formulation
- `introduction.tex` - Introduction with contribution enumeration
- `experiments_c1.tex` - Main experiments section
- `related_work.tex`, `appendix.tex` - Supporting sections

### Core LaTeX Command Definitions
Located in `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex` (lines 19-23):

```latex
\newcommand{\Kstar}{K^*}
\newcommand{\Kempirical}{K^*_{\text{empirical}}}
\newcommand{\Ktheory}{K^*_{\text{theory}}}
\newcommand{\auc}{\text{AUC}}
\newcommand{\jsd}{\text{JSD}}
```

Additionally, based on usage in discussion.tex and conclusions.tex:
- `\Kempirical^{\text{neural}}` for neural probe variant (K* neural)
- Subscript/superscript notation: `K^*_{\text{neural}}` is deprecated in favor of macro form

### Writing Style Characteristics

**Tone & Structure:**
1. **Formal academic prose** with extensive cross-references (e.g., `Section~\ref{sec:method}`, `Table~\ref{tab:kstar_ci}`)
2. **Numerical precision**: Report exact percentages, confidence intervals, and p-values (e.g., "0.60 by only +0.15\,pp")
3. **Methodological rigor**: Every finding includes bootstrap CI lower/upper bounds, permutation p-values, and operational thresholds
4. **Parenthetical citations**: Use `\cite{author2024}` format within text
5. **Parenthetical notation**: Use `($\theta = 0.60$)` for inline parameter definitions

**Pattern Examples from conclusion.tex:**
- "Across ... we establish $\Kempirical = 2$ as a consistent boundary"
- "For the four model-mode configurations, bootstrap 95\% confidence intervals and permutation tests confirm statistical significance at the 1v2 boundary ($p \leq 0.002$ for all four)"
- "All four decoding configurations (greedy, nucleus, $T{=}0.70$, $T{=}1.2$) likewise yield..."
- Uses em-dashes for elaboration: "The shallowness of $\Kempirical$ is explained by---"

**Feature & Metric Formatting:**
- Monospace feature names: `\texttt{surp\_d1\_std}`, `\texttt{hapax\_ratio}`, `\texttt{self\_bleu}`
- LaTeX-formatted metrics: `\text{MAE}`, `\auc` (not "AUC")
- Confidence intervals: `\text{CI}_{\text{lower}}^{95\%}`, `\text{CI}_{\text{upper}}^{95\%}`
- Model names with dashes: Qwen2.5-1.5B-Instruct, Pythia-1.4B, OLMo-1B

**Subsection Organization:**
From discussion.tex pattern:
- Subsections labeled: `\subsection{...}\label{sec:discuss_...}`
- Explicit subheadings with `\paragraph{}` for specific analysis points
- Limitations section uses `\emph{...}` for emphasis on constraint names

**Table & Figure References:**
- Tables: `Table~\ref{tab:filtering_main}` with boilerplate captions using `\toprule`, `\midrule`, `\bottomrule` from `booktabs` package
- Figures: `Figure~\ref{fig:auc_decay}` with inline reference to appendix versions (e.g., `Figure~\ref{fig:s1_auc_decay_ci}`)

### Incomplete/Template Sections

**In experiments_c3.tex** (lines 48-127):
- Table placeholders: `XX.X $\pm$ X.X` for results pending completion
- TODO comments indicating expected narrative structure
- Paragraph-level guidance for future analysis (lines 120-145)

### Document Context

**Project Scope:**
- EMNLP 2026 submission (ARR May 2026) on "Generational Depth Contamination" in language models
- Core finding: $\Kempirical = 2$ (two-generation discrimination boundary)
- Methods: OBD-LightGBM classifier on 15 hand-crafted statistical features
- Experiments: 8 conditions (4 model-mode configs × 4 decoding strategies)
- Secondary contribution: Graduated filtering for depth-aware data curation

**Memory Notes Highlight:**
- Neural probe preliminary results show $\Kempirical^{\text{neural}} = 3$ on single dataset (pending validation)
- Memory.md indicates references need verification (some hallucinated author names in 2025-2026 papers)
- Consistent notation: use "Qwen-continuation" not "Qwen-cont" in running text

### Package Dependencies (from main.tex)
```latex
\usepackage{times}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{booktabs}       % Professional tables
\usepackage{multirow}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage[numbers]{natbib}
\usepackage{enumitem}
\usepackage{subcaption}
```

This gives you a complete picture of the LaTeX conventions, macro system, writing tone, and structural patterns used throughout this research project.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "c38b33a2-4c9a-439c-b7b1-9f84cd04432a",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to read several files in the project /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ to understand the writing style and LaTeX commands used.\n\n1. Find and read any .tex files related to experiments_c3, conclusion, discussion sections\n2. Find the file where LaTeX commands like \\Kempirical, \\auc are defined (likely a preamble or macros file)\n3. Read any existing artifacts to understand the tone\n\nSearch in these directories:\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/\n\nLook for .tex files, especially conclusion.tex, discussion.tex, experiments_c3.tex, macros.tex, preamble.tex, commands.tex, or similar.",
    "agentId": "a9b17499a9915dbf4",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! Now I have a comprehensive understanding of the project. Let me compile a final summary report:\n\n## Summary: LaTeX Writing Style and Commands for gen-depth-contamination Project\n\n### File Locations and Structure\n\n**Primary LaTeX Files in `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/`:**\n- `main.tex` - Document root with preamble and macro definitions\n- `conclusion.tex` - Conclusion section\n- `discussion.tex` - Discussion section (7 subsections with detailed analysis)\n- `experiments_c3.tex` - Graduated filtering experiments (incomplete, with TODO placeholders)\n- `method.tex` - Method section with formal problem formulation\n- `introduction.tex` - Introduction with contribution enumeration\n- `experiments_c1.tex` - Main experiments section\n- `related_work.tex`, `appendix.tex` - Supporting sections\n\n### Core LaTeX Command Definitions\nLocated in `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex` (lines 19-23):\n\n```latex\n\\newcommand{\\Kstar}{K^*}\n\\newcommand{\\Kempirical}{K^*_{\\text{empirical}}}\n\\newcommand{\\Ktheory}{K^*_{\\text{theory}}}\n\\newcommand{\\auc}{\\text{AUC}}\n\\newcommand{\\jsd}{\\text{JSD}}\n```\n\nAdditionally, based on usage in discussion.tex and conclusions.tex:\n- `\\Kempirical^{\\text{neural}}` for neural probe variant (K* neural)\n- Subscript/superscript notation: `K^*_{\\text{neural}}` is deprecated in favor of macro form\n\n### Writing Style Characteristics\n\n**Tone & Structure:**\n1. **Formal academic prose** with extensive cross-references (e.g., `Section~\\ref{sec:method}`, `Table~\\ref{tab:kstar_ci}`)\n2. **Numerical precision**: Report exact percentages, confidence intervals, and p-values (e.g., \"0.60 by only +0.15\\,pp\")\n3. **Methodological rigor**: Every finding includes bootstrap CI lower/upper bounds, permutation p-values, and operational thresholds\n4. **Parenthetical citations**: Use `\\cite{author2024}` format within text\n5. **Parenthetical notation**: Use `($\\theta = 0.60$)` for inline parameter definitions\n\n**Pattern Examples from conclusion.tex:**\n- \"Across ... we establish $\\Kempirical = 2$ as a consistent boundary\"\n- \"For the four model-mode configurations, bootstrap 95\\% confidence intervals and permutation tests confirm statistical significance at the 1v2 boundary ($p \\leq 0.002$ for all four)\"\n- \"All four decoding configurations (greedy, nucleus, $T{=}0.70$, $T{=}1.2$) likewise yield...\"\n- Uses em-dashes for elaboration: \"The shallowness of $\\Kempirical$ is explained by---\"\n\n**Feature & Metric Formatting:**\n- Monospace feature names: `\\texttt{surp\\_d1\\_std}`, `\\texttt{hapax\\_ratio}`, `\\texttt{self\\_bleu}`\n- LaTeX-formatted metrics: `\\text{MAE}`, `\\auc` (not \"AUC\")\n- Confidence intervals: `\\text{CI}_{\\text{lower}}^{95\\%}`, `\\text{CI}_{\\text{upper}}^{95\\%}`\n- Model names with dashes: Qwen2.5-1.5B-Instruct, Pythia-1.4B, OLMo-1B\n\n**Subsection Organization:**\nFrom discussion.tex pattern:\n- Subsections labeled: `\\subsection{...}\\label{sec:discuss_...}`\n- Explicit subheadings with `\\paragraph{}` for specific analysis points\n- Limitations section uses `\\emph{...}` for emphasis on constraint names\n\n**Table & Figure References:**\n- Tables: `Table~\\ref{tab:filtering_main}` with boilerplate captions using `\\toprule`, `\\midrule`, `\\bottomrule` from `booktabs` package\n- Figures: `Figure~\\ref{fig:auc_decay}` with inline reference to appendix versions (e.g., `Figure~\\ref{fig:s1_auc_decay_ci}`)\n\n### Incomplete/Template Sections\n\n**In experiments_c3.tex** (lines 48-127):\n- Table placeholders: `XX.X $\\pm$ X.X` for results pending completion\n- TODO comments indicating expected narrative structure\n- Paragraph-level guidance for future analysis (lines 120-145)\n\n### Document Context\n\n**Project Scope:**\n- EMNLP 2026 submission (ARR May 2026) on \"Generational Depth Contamination\" in language models\n- Core finding: $\\Kempirical = 2$ (two-generation discrimination boundary)\n- Methods: OBD-LightGBM classifier on 15 hand-crafted statistical features\n- Experiments: 8 conditions (4 model-mode configs × 4 decoding strategies)\n- Secondary contribution: Graduated filtering for depth-aware data curation\n\n**Memory Notes Highlight:**\n- Neural probe preliminary results show $\\Kempirical^{\\text{neural}} = 3$ on single dataset (pending validation)\n- Memory.md indicates references need verification (some hallucinated author names in 2025-2026 papers)\n- Consistent notation: use \"Qwen-continuation\" not \"Qwen-cont\" in running text\n\n### Package Dependencies (from main.tex)\n```latex\n\\usepackage{times}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{amsthm}\n\\usepackage{booktabs}       % Professional tables\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[numbers]{natbib}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n```\n\nThis gives you a complete picture of the LaTeX conventions, macro system, writing tone, and structural patterns used throughout this research project."
      }
    ],
    "totalDurationMs": 29151,
    "totalTokens": 45580,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 42000,
      "output_tokens": 1554,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2019
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1554,
          "cache_read_input_tokens": 42000,
          "cache_creation_input_tokens": 2019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2019,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 6,
      "searchCount": 2,
      "bashCount": 3,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 1
    }
  }
}
````

</details>

---

### Assistant

_source line 49_

Now let me read the actual experiments_c3.tex and discussion.tex files to match the precise style.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "33f3912b-33d1-45ae-97d5-10fd55d1e611",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ErWamZPFbCojh1Cnu1w5R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 24960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1913
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

_source line 50_

<details open><summary>🔧 Tool call — Read · `toolu_01SHxpjSxdkAbc3NJyFS4ajk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "8a1a654b-c74b-48f3-ac36-ebacc40d92cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ErWamZPFbCojh1Cnu1w5R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 24960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1913
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

_source line 51 · 2026-05-14T07:59:03.743Z_

<details><summary>↩ Tool result · `toolu_01SHxpjSxdkAbc3NJyFS4ajk`</summary>

```text
1	\subsection{Graduated Filtering for Depth-Aware Data Curation}
2	\label{sec:graduated-filtering}
3	
4	The $\Kempirical = 2$ boundary establishes a three-tier taxonomy: human (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\geq 2$).
5	Binary filtering discards all synthetic content indiscriminately, sacrificing depth-1 text that retains most of the original signal.
6	We ask whether exploiting the coarse ordinal structure---weighting samples by predicted depth rather than applying a hard human/synthetic threshold---improves downstream language model quality.
7	
8	\paragraph{Filtering strategies.}
9	We compare six data curation strategies applied to a corpus of 30{,}000 documents (5{,}000 per depth level, depths 0--5) produced by the generational depth pipeline:
10	
11	\begin{enumerate}[label=(\roman*)]
12	  \item \textbf{No-filter}: all documents receive uniform weight (baseline).
13	
14	  \item \textbf{Binary-ours}: a LightGBM classifier trained on the 15-dimensional feature set distinguishes human (depth~0) from synthetic (depth~$\geq 1$).
15	  Each document receives weight $w = 1 - P(\text{synthetic})$.
16	  This represents the natural binary extension of our depth estimation framework.
17	
18	  \item \textbf{Binary-Drayson}: stratified importance resampling following Drayson et al.~\cite{drayson2025}, with $w_j = (1 - q(x_j))^b / Z$, $b = 1.5$, and oversampling factor $k = 1.5$.
19	  This is the strongest existing baseline for contamination-aware data curation.
20	
21	  \item \textbf{Graduated}: our proposed depth-aware strategy.
22	  The OBD-LightGBM classifier (Section~\ref{sec:classifier}) predicts a full depth distribution $P(d \mid \mathbf{x})$ for each document, from which we compute the expected depth $\hat{d} = \sum_d d \cdot P(d \mid \mathbf{x})$.
23	  Sample weights follow an exponential decay: $w = \exp(-\alpha \cdot \hat{d})$, where $\alpha$ controls the penalty for predicted depth.
24	  Low $\alpha$ values retain more synthetic content with gentle down-weighting; high $\alpha$ values approximate hard filtering.
25	  We sweep $\alpha \in \{0.1, 0.3, 0.5, 0.7, 0.9\}$.
26	
27	  \item \textbf{Surprisal}: a feature-based heuristic that retains documents whose mean surprisal exceeds the corpus median, exploiting the observation that deeper generations exhibit lower surprisal variance (Section~\ref{sec:feature_degradation}).
28	
29	  \item \textbf{DSIR}: Data Selection via Importance Resampling~\cite{xie2023dsir}, using bigram feature hashing with the depth-0 subcorpus as the reference distribution.
30	  This represents the state-of-the-art domain-matching baseline that is agnostic to generational depth.
31	\end{enumerate}
32	
33	\paragraph{Training setup.}
34	We fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\alpha_{\text{LoRA}} = 16$, target modules: \texttt{q\_proj}, \texttt{v\_proj}, dropout 0.05) on the filtered corpus for 3 epochs with learning rate $2 \times 10^{-5}$, batch size 4 with gradient accumulation 8, warmup ratio 0.1, and bfloat16 precision.
35	Documents are truncated to 512 tokens.
36	For strategies that produce continuous weights (graduated, binary-ours, binary-Drayson, DSIR), zero-weight samples are removed and the remaining samples are drawn via weighted random sampling; for binary strategies (surprisal), excluded samples are dropped outright.
37	Each strategy is evaluated across 5 random seeds (42, 123, 456, 789, 1024); the graduated strategy is further crossed with 5 $\alpha$ values, yielding 25 additional runs.
38	A base model baseline (no fine-tuning) is included for reference.
39	The total experimental budget is approximately 50 runs.
40	
41	\paragraph{Evaluation.}
42	We evaluate on two standard benchmarks via lm-eval-harness: MMLU (14{,}042 test examples, 0-shot) and HellaSwag (10{,}042 validation examples, 0-shot).
43	We report mean accuracy $\pm$ standard deviation across seeds.
44	
45	%% ====================================================================
46	\paragraph{Results.}
47	
48	\begin{table}[t]
49	\centering
50	\small
51	\caption{Downstream evaluation of filtering strategies.
52	MMLU and HellaSwag accuracy (0-shot) after LoRA continued pretraining on Qwen2.5-1.5B-Instruct with each strategy's filtered corpus.
53	Mean $\pm$ std over 5 seeds.
54	Best per-column result in bold; second-best underlined.
55	Graduated results use the best $\alpha$ from Table~\ref{tab:alpha_sweep}.}
56	\label{tab:filtering_main}
57	\begin{tabular}{lcc}
58	\toprule
59	\textbf{Strategy} & \textbf{MMLU} & \textbf{HellaSwag} \\
60	\midrule
61	Base model (no fine-tuning)
62	  & \textit{XX.X}
63	  & \textit{XX.X} \\
64	\midrule
65	No-filter
66	  & XX.X $\pm$ X.X
67	  & XX.X $\pm$ X.X \\
68	Binary-ours
69	  & XX.X $\pm$ X.X
70	  & XX.X $\pm$ X.X \\
71	Binary-Drayson
72	  & XX.X $\pm$ X.X
73	  & XX.X $\pm$ X.X \\
74	Graduated ($\alpha^*$)
75	  & \textbf{XX.X} $\pm$ X.X
76	  & \textbf{XX.X} $\pm$ X.X \\
77	Surprisal
78	  & XX.X $\pm$ X.X
79	  & XX.X $\pm$ X.X \\
80	DSIR
81	  & XX.X $\pm$ X.X
82	  & XX.X $\pm$ X.X \\
83	\bottomrule
84	\end{tabular}
85	\end{table}
86	
87	Table~\ref{tab:filtering_main} compares the six strategies on downstream benchmark accuracy.
88	% TODO: fill results and update narrative once exp-006 completes.
89	% Expected narrative structure:
90	% 1. No-filter baseline establishes the cost of training on contaminated data.
91	% 2. Binary strategies (ours + Drayson) improve over no-filter by removing synthetic content.
92	% 3. Graduated filtering outperforms binary by preserving depth-1 signal.
93	% 4. DSIR and surprisal provide reference points for non-depth-aware curation.
94	
95	%% ====================================================================
96	\paragraph{$\alpha$ sensitivity.}
97	
98	\begin{table}[t]
99	\centering
100	\small
101	\caption{Graduated filtering $\alpha$ sweep.
102	Mean accuracy $\pm$ std (5 seeds) for each decay parameter $\alpha$.
103	Lower $\alpha$ retains more synthetic content; higher $\alpha$ approximates hard filtering.}
104	\label{tab:alpha_sweep}
105	\begin{tabular}{ccc}
106	\toprule
107	$\alpha$ & \textbf{MMLU} & \textbf{HellaSwag} \\
108	\midrule
109	0.1 & XX.X $\pm$ X.X & XX.X $\pm$ X.X \\
110	0.3 & XX.X $\pm$ X.X & XX.X $\pm$ X.X \\
111	0.5 & XX.X $\pm$ X.X & XX.X $\pm$ X.X \\
112	0.7 & XX.X $\pm$ X.X & XX.X $\pm$ X.X \\
113	0.9 & XX.X $\pm$ X.X & XX.X $\pm$ X.X \\
114	\bottomrule
115	\end{tabular}
116	\end{table}
117	
118	Table~\ref{tab:alpha_sweep} shows the effect of the decay parameter $\alpha$ on downstream performance.
119	% TODO: fill results.
120	% Expected narrative:
121	% - Characterize the Pareto frontier: low alpha retains data volume but includes
122	%   more noise; high alpha is more selective but discards useful signal.
123	% - Identify optimal alpha and discuss whether the optimum is stable across seeds.
124	% - Connect to the K*=2 trichotomy: the graduated scheme effectively implements
125	%   a soft version of the human / gen-1 / gen-2+ partition, with alpha controlling
126	%   how aggressively deeper content is penalized.
127	
128	%% ====================================================================
129	\paragraph{Analysis.}
130	
131	% TODO: fill once results are available.
132	% Planned analysis points:
133	% (1) Does graduated filtering outperform binary? If so, this validates the
134	%     practical utility of the K*=2 trichotomy for data curation.
135	% (2) How does the optimal alpha relate to the discrimination boundary?
136	%     At alpha -> infinity, graduated degenerates to binary-ours (hard cutoff);
137	%     at alpha = 0, it degenerates to no-filter. The optimal alpha should
138	%     lie in between, reflecting the value of soft depth-aware weighting.
139	% (3) Which strategy benefits most from the seed averaging? If graduated
140	%     shows lower variance across seeds, it suggests the ordinal signal
141	%     provides a more stable curation criterion than binary classification.
142	% (4) Do the results differ between MMLU (knowledge-intensive) and
143	%     HellaSwag (commonsense reasoning)? Different tasks may exhibit
144	%     different sensitivity to data contamination depth.
145	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "a739c945-9e8d-4749-89f2-612bce86d251",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex",
      "content": "\\subsection{Graduated Filtering for Depth-Aware Data Curation}\n\\label{sec:graduated-filtering}\n\nThe $\\Kempirical = 2$ boundary establishes a three-tier taxonomy: human (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\\geq 2$).\nBinary filtering discards all synthetic content indiscriminately, sacrificing depth-1 text that retains most of the original signal.\nWe ask whether exploiting the coarse ordinal structure---weighting samples by predicted depth rather than applying a hard human/synthetic threshold---improves downstream language model quality.\n\n\\paragraph{Filtering strategies.}\nWe compare six data curation strategies applied to a corpus of 30{,}000 documents (5{,}000 per depth level, depths 0--5) produced by the generational depth pipeline:\n\n\\begin{enumerate}[label=(\\roman*)]\n  \\item \\textbf{No-filter}: all documents receive uniform weight (baseline).\n\n  \\item \\textbf{Binary-ours}: a LightGBM classifier trained on the 15-dimensional feature set distinguishes human (depth~0) from synthetic (depth~$\\geq 1$).\n  Each document receives weight $w = 1 - P(\\text{synthetic})$.\n  This represents the natural binary extension of our depth estimation framework.\n\n  \\item \\textbf{Binary-Drayson}: stratified importance resampling following Drayson et al.~\\cite{drayson2025}, with $w_j = (1 - q(x_j))^b / Z$, $b = 1.5$, and oversampling factor $k = 1.5$.\n  This is the strongest existing baseline for contamination-aware data curation.\n\n  \\item \\textbf{Graduated}: our proposed depth-aware strategy.\n  The OBD-LightGBM classifier (Section~\\ref{sec:classifier}) predicts a full depth distribution $P(d \\mid \\mathbf{x})$ for each document, from which we compute the expected depth $\\hat{d} = \\sum_d d \\cdot P(d \\mid \\mathbf{x})$.\n  Sample weights follow an exponential decay: $w = \\exp(-\\alpha \\cdot \\hat{d})$, where $\\alpha$ controls the penalty for predicted depth.\n  Low $\\alpha$ values retain more synthetic content with gentle down-weighting; high $\\alpha$ values approximate hard filtering.\n  We sweep $\\alpha \\in \\{0.1, 0.3, 0.5, 0.7, 0.9\\}$.\n\n  \\item \\textbf{Surprisal}: a feature-based heuristic that retains documents whose mean surprisal exceeds the corpus median, exploiting the observation that deeper generations exhibit lower surprisal variance (Section~\\ref{sec:feature_degradation}).\n\n  \\item \\textbf{DSIR}: Data Selection via Importance Resampling~\\cite{xie2023dsir}, using bigram feature hashing with the depth-0 subcorpus as the reference distribution.\n  This represents the state-of-the-art domain-matching baseline that is agnostic to generational depth.\n\\end{enumerate}\n\n\\paragraph{Training setup.}\nWe fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\\alpha_{\\text{LoRA}} = 16$, target modules: \\texttt{q\\_proj}, \\texttt{v\\_proj}, dropout 0.05) on the filtered corpus for 3 epochs with learning rate $2 \\times 10^{-5}$, batch size 4 with gradient accumulation 8, warmup ratio 0.1, and bfloat16 precision.\nDocuments are truncated to 512 tokens.\nFor strategies that produce continuous weights (graduated, binary-ours, binary-Drayson, DSIR), zero-weight samples are removed and the remaining samples are drawn via weighted random sampling; for binary strategies (surprisal), excluded samples are dropped outright.\nEach strategy is evaluated across 5 random seeds (42, 123, 456, 789, 1024); the graduated strategy is further crossed with 5 $\\alpha$ values, yielding 25 additional runs.\nA base model baseline (no fine-tuning) is included for reference.\nThe total experimental budget is approximately 50 runs.\n\n\\paragraph{Evaluation.}\nWe evaluate on two standard benchmarks via lm-eval-harness: MMLU (14{,}042 test examples, 0-shot) and HellaSwag (10{,}042 validation examples, 0-shot).\nWe report mean accuracy $\\pm$ standard deviation across seeds.\n\n%% ====================================================================\n\\paragraph{Results.}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Downstream evaluation of filtering strategies.\nMMLU and HellaSwag accuracy (0-shot) after LoRA continued pretraining on Qwen2.5-1.5B-Instruct with each strategy's filtered corpus.\nMean $\\pm$ std over 5 seeds.\nBest per-column result in bold; second-best underlined.\nGraduated results use the best $\\alpha$ from Table~\\ref{tab:alpha_sweep}.}\n\\label{tab:filtering_main}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Strategy} & \\textbf{MMLU} & \\textbf{HellaSwag} \\\\\n\\midrule\nBase model (no fine-tuning)\n  & \\textit{XX.X}\n  & \\textit{XX.X} \\\\\n\\midrule\nNo-filter\n  & XX.X $\\pm$ X.X\n  & XX.X $\\pm$ X.X \\\\\nBinary-ours\n  & XX.X $\\pm$ X.X\n  & XX.X $\\pm$ X.X \\\\\nBinary-Drayson\n  & XX.X $\\pm$ X.X\n  & XX.X $\\pm$ X.X \\\\\nGraduated ($\\alpha^*$)\n  & \\textbf{XX.X} $\\pm$ X.X\n  & \\textbf{XX.X} $\\pm$ X.X \\\\\nSurprisal\n  & XX.X $\\pm$ X.X\n  & XX.X $\\pm$ X.X \\\\\nDSIR\n  & XX.X $\\pm$ X.X\n  & XX.X $\\pm$ X.X \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:filtering_main} compares the six strategies on downstream benchmark accuracy.\n% TODO: fill results and update narrative once exp-006 completes.\n% Expected narrative structure:\n% 1. No-filter baseline establishes the cost of training on contaminated data.\n% 2. Binary strategies (ours + Drayson) improve over no-filter by removing synthetic content.\n% 3. Graduated filtering outperforms binary by preserving depth-1 signal.\n% 4. DSIR and surprisal provide reference points for non-depth-aware curation.\n\n%% ====================================================================\n\\paragraph{$\\alpha$ sensitivity.}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Graduated filtering $\\alpha$ sweep.\nMean accuracy $\\pm$ std (5 seeds) for each decay parameter $\\alpha$.\nLower $\\alpha$ retains more synthetic content; higher $\\alpha$ approximates hard filtering.}\n\\label{tab:alpha_sweep}\n\\begin{tabular}{ccc}\n\\toprule\n$\\alpha$ & \\textbf{MMLU} & \\textbf{HellaSwag} \\\\\n\\midrule\n0.1 & XX.X $\\pm$ X.X & XX.X $\\pm$ X.X \\\\\n0.3 & XX.X $\\pm$ X.X & XX.X $\\pm$ X.X \\\\\n0.5 & XX.X $\\pm$ X.X & XX.X $\\pm$ X.X \\\\\n0.7 & XX.X $\\pm$ X.X & XX.X $\\pm$ X.X \\\\\n0.9 & XX.X $\\pm$ X.X & XX.X $\\pm$ X.X \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:alpha_sweep} shows the effect of the decay parameter $\\alpha$ on downstream performance.\n% TODO: fill results.\n% Expected narrative:\n% - Characterize the Pareto frontier: low alpha retains data volume but includes\n%   more noise; high alpha is more selective but discards useful signal.\n% - Identify optimal alpha and discuss whether the optimum is stable across seeds.\n% - Connect to the K*=2 trichotomy: the graduated scheme effectively implements\n%   a soft version of the human / gen-1 / gen-2+ partition, with alpha controlling\n%   how aggressively deeper content is penalized.\n\n%% ====================================================================\n\\paragraph{Analysis.}\n\n% TODO: fill once results are available.\n% Planned analysis points:\n% (1) Does graduated filtering outperform binary? If so, this validates the\n%     practical utility of the K*=2 trichotomy for data curation.\n% (2) How does the optimal alpha relate to the discrimination boundary?\n%     At alpha -> infinity, graduated degenerates to binary-ours (hard cutoff);\n%     at alpha = 0, it degenerates to no-filter. The optimal alpha should\n%     lie in between, reflecting the value of soft depth-aware weighting.\n% (3) Which strategy benefits most from the seed averaging? If graduated\n%     shows lower variance across seeds, it suggests the ordinal signal\n%     provides a more stable curation criterion than binary classification.\n% (4) Do the results differ between MMLU (knowledge-intensive) and\n%     HellaSwag (commonsense reasoning)? Different tasks may exhibit\n%     different sensitivity to data contamination depth.\n",
      "numLines": 145,
      "startLine": 1,
      "totalLines": 145
    }
  }
}
```

</details>

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_01Ry7eBi6AfT1u79QVEvLEip`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "66e57fdf-f382-4069-8f66-811d51e29256",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ErWamZPFbCojh1Cnu1w5R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 24960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1913
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

_source line 53 · 2026-05-14T07:59:06.707Z_

<details><summary>↩ Tool result · `toolu_01Ry7eBi6AfT1u79QVEvLEip`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	% === Contribution 1: K*=2 consistent boundary ===
5	% Sources: exp_007 (bootstrap CI + permutation), exp_001/exp_002/exp_017/mvp_pilot (model-mode), exp_003 (decoding ablation)
6	We presented the first systematic measurement of the generational depth
7	discrimination boundary $\Kempirical$ for recursive synthetic text.
8	Across three model architectures in four model-mode configurations
9	(Pythia-1.4B and OLMo-1B in continuation mode; Qwen2.5-1.5B-Instruct in both
10	continuation and rewrite modes) and 4 decoding strategies---totaling 8
11	conditions---we establish $\Kempirical = 2$ as a consistent boundary:
12	classifiers reliably distinguish adjacent generations up to depth~2, but all
13	deeper pairs fall below the operational threshold $\theta = 0.60$.
14	For the four model-mode configurations, bootstrap 95\% confidence intervals
15	and permutation tests confirm statistical significance at the 1v2 boundary
16	($p \leq 0.002$ for all four); the most marginal case, Qwen-continuation,
17	yields a CI lower bound of 0.6015, exceeding $\theta$ by only 0.15\,pp.
18	All four decoding configurations (greedy, nucleus, $T{=}0.70$, $T{=}1.2$)
19	likewise yield 1v2 point-estimate $\auc$ above $\theta$.
20	The 0v1 boundary is near-perfectly separable ($\auc > 0.99$), followed by a
21	sharp ${\sim}$30\,pp drop at 1v2 ($\auc$: 0.6112--0.7039 across all
22	conditions), while all 2v3 pairs fall below~$\theta$.
23	Recursive generation thus acts as a severely lossy channel whose discriminable
24	statistical fingerprint is exhausted within two steps.
25	
26	% === Contribution 2: Ordinal depth estimation framework ===
27	% Sources: exp_010 (OBD vs baselines), exp_013 (cross-model transfer), exp_005 (feature degradation), exp_011 (LLM zero-shot)
28	To operationalize depth estimation, we introduced an ordinal binary
29	decomposition (OBD) framework pairing 15 hand-crafted statistical features
30	with LightGBM classifiers.
31	Cross-model transfer experiments demonstrate 80--92\% accuracy retention
32	across continuation-mode model pairs, with
33	Pythia$\leftrightarrow$OLMo achieving 90--92\% and 0v1 transfer $\auc$
34	exceeding 0.96 across all tested model pairs---indicating that depth signals are largely
35	text-intrinsic rather than generator-specific.
36	Feature degradation orderings are consistent across architectures
37	(Spearman $\rho \geq 0.85$), with surprisal-variance features dominating
38	uniformly, suggesting that the two-step information loss is governed by the
39	autoregressive mechanism itself.
40	As a reference point, frontier LLMs (GPT-5.5, Claude Opus~4.6) achieve
41	${\sim}$88\% binary human-vs.-synthetic accuracy but only ${\sim}$33\% on
42	5-class depth estimation, below OBD-LightGBM's 38.6\%---confirming that
43	fine-grained depth discrimination requires specialized statistical features
44	rather than general language understanding.
45	A preliminary neural probing experiment suggests that this operational bound is not tight: a frozen Qwen2.5-1.5B encoder paired with an MLP classifier achieves $\Kempirical^{\text{neural}} = 3$ on the Qwen-continuation dataset (2v3 $\auc = 0.6195$ versus 0.5609 with hand-crafted features), indicating that learned representations recover depth signal beyond the 15-dimensional feature set.
46	This result, pending cross-model validation, provides initial evidence that $\Ktheory \geq 3$.
47	
48	% === Contribution 3: Graduated filtering (C3) ===
49	% Source: exp_006 (RUNNING — results pending)
50	The $\Kempirical = 2$ boundary implies a natural trichotomy---human (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\geq 2$)---that can be exploited for depth-aware data curation.
51	% TODO: exp-006 graduated filtering 具体结果填充。
52	% 预留内容：graduated filtering 利用三级分类法在 MMLU/HellaSwag 上的表现，
53	% 与 binary filtering 和 no-filter baseline 的对比。
54	
55	% === Limitations + Future Work ===
56	Our findings are bounded by the scale of models tested ($\leq$1.5B parameters), restriction to English C4 text, and the use of prompt-chain rather than retrain-chain protocols; $\Kempirical$ depends on the threshold $\theta$ and shifts with generation mode (continuation-mode configurations drop to $\Kempirical{=}1$ at $\theta{=}0.65$, while rewrite mode retains $\Kempirical{=}2$; Section~\ref{sec:limitations}); the 15-dimensional feature set yields $\Kempirical$ as an operational lower bound, and $\Ktheory$ may be strictly higher.
57	Several directions merit investigation: scaling to larger models (7B+) to test whether increased generation fidelity shifts the boundary; extending to multilingual and multi-domain corpora; establishing the relationship between prompt-chain and retrain-chain $\Kstar$ values, which would connect our measurements to the model collapse setting; incorporating few-shot or chain-of-thought prompting for LLM-based depth estimation; and extending the neural probe approach---which has yielded preliminary evidence of $\Kempirical^{\text{neural}} = 3$ on one dataset---through cross-model validation (Pythia, OLMo), bootstrap confidence intervals, multi-layer probing beyond the last hidden state, and comparison with fine-tuned (non-frozen) encoders to further narrow the gap between $\Kempirical$ and $\Ktheory$.
58	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "31765ba1-f0bd-427e-a2b4-d7ca61beafb0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\n% === Contribution 1: K*=2 consistent boundary ===\n% Sources: exp_007 (bootstrap CI + permutation), exp_001/exp_002/exp_017/mvp_pilot (model-mode), exp_003 (decoding ablation)\nWe presented the first systematic measurement of the generational depth\ndiscrimination boundary $\\Kempirical$ for recursive synthetic text.\nAcross three model architectures in four model-mode configurations\n(Pythia-1.4B and OLMo-1B in continuation mode; Qwen2.5-1.5B-Instruct in both\ncontinuation and rewrite modes) and 4 decoding strategies---totaling 8\nconditions---we establish $\\Kempirical = 2$ as a consistent boundary:\nclassifiers reliably distinguish adjacent generations up to depth~2, but all\ndeeper pairs fall below the operational threshold $\\theta = 0.60$.\nFor the four model-mode configurations, bootstrap 95\\% confidence intervals\nand permutation tests confirm statistical significance at the 1v2 boundary\n($p \\leq 0.002$ for all four); the most marginal case, Qwen-continuation,\nyields a CI lower bound of 0.6015, exceeding $\\theta$ by only 0.15\\,pp.\nAll four decoding configurations (greedy, nucleus, $T{=}0.70$, $T{=}1.2$)\nlikewise yield 1v2 point-estimate $\\auc$ above $\\theta$.\nThe 0v1 boundary is near-perfectly separable ($\\auc > 0.99$), followed by a\nsharp ${\\sim}$30\\,pp drop at 1v2 ($\\auc$: 0.6112--0.7039 across all\nconditions), while all 2v3 pairs fall below~$\\theta$.\nRecursive generation thus acts as a severely lossy channel whose discriminable\nstatistical fingerprint is exhausted within two steps.\n\n% === Contribution 2: Ordinal depth estimation framework ===\n% Sources: exp_010 (OBD vs baselines), exp_013 (cross-model transfer), exp_005 (feature degradation), exp_011 (LLM zero-shot)\nTo operationalize depth estimation, we introduced an ordinal binary\ndecomposition (OBD) framework pairing 15 hand-crafted statistical features\nwith LightGBM classifiers.\nCross-model transfer experiments demonstrate 80--92\\% accuracy retention\nacross continuation-mode model pairs, with\nPythia$\\leftrightarrow$OLMo achieving 90--92\\% and 0v1 transfer $\\auc$\nexceeding 0.96 across all tested model pairs---indicating that depth signals are largely\ntext-intrinsic rather than generator-specific.\nFeature degradation orderings are consistent across architectures\n(Spearman $\\rho \\geq 0.85$), with surprisal-variance features dominating\nuniformly, suggesting that the two-step information loss is governed by the\nautoregressive mechanism itself.\nAs a reference point, frontier LLMs (GPT-5.5, Claude Opus~4.6) achieve\n${\\sim}$88\\% binary human-vs.-synthetic accuracy but only ${\\sim}$33\\% on\n5-class depth estimation, below OBD-LightGBM's 38.6\\%---confirming that\nfine-grained depth discrimination requires specialized statistical features\nrather than general language understanding.\nA preliminary neural probing experiment suggests that this operational bound is not tight: a frozen Qwen2.5-1.5B encoder paired with an MLP classifier achieves $\\Kempirical^{\\text{neural}} = 3$ on the Qwen-continuation dataset (2v3 $\\auc = 0.6195$ versus 0.5609 with hand-crafted features), indicating that learned representations recover depth signal beyond the 15-dimensional feature set.\nThis result, pending cross-model validation, provides initial evidence that $\\Ktheory \\geq 3$.\n\n% === Contribution 3: Graduated filtering (C3) ===\n% Source: exp_006 (RUNNING — results pending)\nThe $\\Kempirical = 2$ boundary implies a natural trichotomy---human (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\\geq 2$)---that can be exploited for depth-aware data curation.\n% TODO: exp-006 graduated filtering 具体结果填充。\n% 预留内容：graduated filtering 利用三级分类法在 MMLU/HellaSwag 上的表现，\n% 与 binary filtering 和 no-filter baseline 的对比。\n\n% === Limitations + Future Work ===\nOur findings are bounded by the scale of models tested ($\\leq$1.5B parameters), restriction to English C4 text, and the use of prompt-chain rather than retrain-chain protocols; $\\Kempirical$ depends on the threshold $\\theta$ and shifts with generation mode (continuation-mode configurations drop to $\\Kempirical{=}1$ at $\\theta{=}0.65$, while rewrite mode retains $\\Kempirical{=}2$; Section~\\ref{sec:limitations}); the 15-dimensional feature set yields $\\Kempirical$ as an operational lower bound, and $\\Ktheory$ may be strictly higher.\nSeveral directions merit investigation: scaling to larger models (7B+) to test whether increased generation fidelity shifts the boundary; extending to multilingual and multi-domain corpora; establishing the relationship between prompt-chain and retrain-chain $\\Kstar$ values, which would connect our measurements to the model collapse setting; incorporating few-shot or chain-of-thought prompting for LLM-based depth estimation; and extending the neural probe approach---which has yielded preliminary evidence of $\\Kempirical^{\\text{neural}} = 3$ on one dataset---through cross-model validation (Pythia, OLMo), bootstrap confidence intervals, multi-layer probing beyond the last hidden state, and comparison with fine-tuned (non-frozen) encoders to further narrow the gap between $\\Kempirical$ and $\\Ktheory$.\n",
      "numLines": 58,
      "startLine": 1,
      "totalLines": 58
    }
  }
}
```

</details>

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Read · `toolu_01BUpkE2Kh8bLsqD54dWssXM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "3039d3e2-7642-4db6-a41c-bf7eedac1764",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ErWamZPFbCojh1Cnu1w5R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 24960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1913
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

_source line 55 · 2026-05-14T07:59:06.843Z_

<details><summary>↩ Tool result · `toolu_01BUpkE2Kh8bLsqD54dWssXM`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Theoretical Implications of $\Kempirical = 2$}
5	\label{sec:discuss_kstar}
6	
7	The Data Processing Inequality guarantees the existence of a finite $\Ktheory$ beyond which adjacent generations become indistinguishable (Section~\ref{sec:formulation}).
8	Our empirical result---$\Kempirical = 2$ consistently across all 8 tested configurations (4 model-mode combinations and 4 decoding strategies; Section~\ref{sec:kstar_boundary}, Figure~\ref{fig:auc_decay})---establishes that this boundary is not only finite but remarkably shallow at the $\leq$1.5B parameter scale.
9	
10	The shallowness of $\Kempirical$ is explained by the rate of information loss across generations.
11	The 0v1 boundary is near-trivially separable ($\auc > 0.99$ across all configurations; Table~\ref{tab:kstar_ci}), reflecting the large distributional gap between human text and first-generation synthetic text.
12	At the 1v2 boundary, $\auc$ drops by approximately 30 percentage points ($\auc$ range: 0.6112--0.7039 across all eight model$\times$decoding conditions; Table~\ref{tab:kstar_ci}, Figure~\ref{fig:auc_decay}; see also Figure~\ref{fig:s1_auc_decay_ci} in the Appendix), indicating that the majority of the discriminative signal is consumed in the first generation step.
13	By the 2v3 boundary, $\auc$ falls to 0.5496--0.5917 across all eight model$\times$decoding conditions (upper bound from nucleus $p{=}0.9$ decoding; Figure~\ref{fig:auc_decay})---below the operational threshold $\theta = 0.60$---and deeper pairs converge toward chance.
14	Recursive generation thus acts as a severely lossy channel whose information bottleneck is traversed within two steps.
15	
16	The feature degradation analysis (Section~\ref{sec:feature_degradation}) provides mechanistic evidence for this rapid collapse.
17	The most discriminative features---surprisal variance (\texttt{surp\_d1\_std}, \texttt{surp\_std}) and its derivatives---all capture the heterogeneity of token-level predictability.
18	Human text exhibits high surprisal variance reflecting diverse syntactic structures and unpredictable discourse patterns.
19	The first generation step smooths this variance substantially, replacing high-surprisal tokens and atypical constructions with more predictable alternatives; the second step reduces the remaining variance to near-floor levels, leaving insufficient statistical fingerprint for reliable adjacent-depth discrimination.
20	Crucially, this degradation ordering is consistent across model families (Spearman $\rho \geq 0.85$ for all continuation-mode pairs; Table~\ref{tab:top_features}), suggesting that the two-step information loss is governed by the autoregressive generation mechanism itself rather than by model-specific biases.
21	
22	This pattern aligns with findings from the model collapse literature.
23	Shumailov et al.~\cite{shumailov2024collapse} observed that tail-distribution degradation is most acute in the earliest generations, with minority modes vanishing before the output distribution stabilizes.
24	Dohmatob et al.~\cite{dohmatob2024model} derived scaling laws demonstrating that tail probability mass is lost at rates predictable from model and data scale.
25	Our $\Kempirical = 2$ provides a complementary, classifier-based measurement of this phenomenon: the information-theoretic discrimination boundary is reached after just two generation steps.
26	Alemohammad et al.~\cite{alemohammad2024selfconsuming} proved convergence to a fixed point for self-consuming generative models; $\Kempirical = 2$ indicates that, operationally, the approach to this fixed point is rapid enough that adjacent-generation distinctions collapse within two steps.
27	
28	Importantly, $\Kempirical = 2$ is an \emph{operational} lower bound conditioned on the 15-dimensional hand-crafted feature set; the \emph{theoretical} boundary $\Ktheory$ may be strictly higher.
29	Preliminary evidence from a neural probing experiment supports this distinction.
30	A frozen Qwen2.5-1.5B encoder (1536-dimensional last-layer representations) paired with a lightweight MLP classifier (Table~\ref{tab:s7_neural_probe}) achieves 2v3 $\auc = 0.6195$ ($\text{std} = 0.0094$) on the Qwen-continuation dataset, exceeding the $\theta = 0.60$ threshold that the same dataset's LightGBM classifier fails to cross ($\auc = 0.5609$; Section~\ref{sec:kstar_boundary}).
31	This yields $\Kempirical^{\text{neural}} = 3$: the learned representation recovers one additional discriminable boundary that the hand-crafted features miss.
32	The improvement is concentrated at the 2v3 pair ($+$5.86\,pp over LightGBM); at the already-separable 1v2 boundary the neural probe achieves 0.6983 versus 0.6112, a substantial gain but one that does not alter the boundary determination.
33	At 3v4, the neural probe reaches $\auc = 0.5930$---below $\theta$ but closer to the threshold than any hand-crafted configuration---suggesting that a still richer representation might push the boundary further.
34	The lossy-channel narrative remains intact: even with 1536-dimensional frozen representations, the discrimination boundary extends to only three steps, confirming that the information bottleneck of recursive generation is shallow even with substantially richer representations.
35	These results are preliminary: they cover a single model-dataset pair (Qwen-continuation) and lack bootstrap confidence intervals; cross-model validation on Pythia and OLMo is pending.
36	
37	The invariance of $\Kempirical = 2$ across decoding strategies merits emphasis.
38	Greedy decoding, nucleus sampling ($p{=}0.9$), $T{=}0.7$, and $T{=}1.2$ all yield $\Kempirical = 2$ (Figure~\ref{fig:auc_decay}; Table~\ref{tab:s2_decoding}), with 1v2 $\auc$ spanning a narrow range of [0.6866, 0.7039].
39	Higher decoding entropy modestly increases signal strength ($\auc_{1,2}$: 0.69 greedy $\to$ 0.70 at $T{=}1.2$) but does not shift the boundary.
40	This robustness suggests that $\Kempirical$ is governed by the fundamental information bottleneck of the generation process rather than by surface-level properties of the sampling algorithm.
41	
42	\subsection{Implications of Cross-Model Transfer}
43	\label{sec:discuss_transfer}
44	
45	The cross-model transfer results (Section~\ref{sec:transfer}) indicate that depth signals are largely encoded in text-level statistical properties rather than generator-specific artifacts.
46	Classifiers trained on Pythia-1.4B and evaluated on OLMo-1B retain 90--92\% of within-model accuracy, and the broader continuation-mode transfer matrix shows 80--92\% retention across all model pairs (Table~\ref{tab:transfer_matrix}; see Table~\ref{tab:s1_transfer} for the full matrix).
47	At the 0v1 boundary, cross-model $\auc$ exceeds 0.96 across all tested model pairs, confirming that binary contamination detection is fully transferable across the tested generators.
48	
49	The practical implication is direct: a single depth classifier trained on one model's outputs can be deployed to estimate generational depth for texts produced by other models, without model-specific retraining.
50	This transferability extends the utility of depth estimation to open-web settings where the generating model is unknown---precisely the scenario where depth-aware data curation is most needed.
51	
52	Two caveats bound this conclusion.
53	First, the text-intrinsic component dominates, as evidenced by high cross-model transfer retention (80--92\% across continuation-mode pairs), yet a nontrivial model-specific residual persists.
54	The Pythia$\leftrightarrow$OLMo pair, which spans different architectures and training corpora, achieves the highest cross-family retention (90--92\%), consistent with the depth signal being largely architecture-agnostic within continuation mode.
55	Second, Qwen-continuation$\leftrightarrow$OLMo retention (80--85\%) is lower than Pythia$\leftrightarrow$OLMo (90--92\%), indicating that model family similarity modulates transfer even among continuation-mode configurations.
56	
57	\subsection{Feature Importance Across Decoding Strategies}
58	\label{sec:discuss_features}
59	
60	While $\Kempirical = 2$ is invariant to decoding strategy (4/4 configurations), the feature importance ordering is not uniformly consistent.
61	Greedy decoding and $T{=}0.7$ share highly correlated feature rankings (Spearman $\rho = 0.914$), with top features dominated by vocabulary diversity measures: \texttt{self\_bleu}, \texttt{hapax\_ratio}, and \texttt{ttr}.
62	In contrast, greedy versus $T{=}1.2$ yields a lower correlation ($\rho = 0.53$, $p = 0.041$; suggestive but nonsignificant after Bonferroni correction for 6 pairwise comparisons), with $T{=}1.2$ promoting \texttt{hapax\_ratio}, \texttt{ttr}, and \texttt{surp\_skew} to the top ranks.
63	Notably, \texttt{freq\_entropy} rises from rank~10 under greedy ($\auc = 0.5139$) to rank~5 under $T{=}1.2$ ($\auc = 0.5905$), illustrating how high-entropy decoding amplifies frequency-distribution artifacts.
64	
65	This dissociation reveals an important distinction: the \emph{existence} of the depth boundary is robust, but the \emph{optimal feature subset} for detecting it depends on the sampling strategy.
66	High-entropy decoding amplifies frequency-distribution artifacts while attenuating vocabulary-diversity signals, shifting which text properties carry the most discriminative power without altering whether adjacent generations can be distinguished.
67	For practitioners, this implies that a general-purpose depth classifier should incorporate features from multiple groups---surprisal moments, vocabulary diversity, and frequency tail statistics---to maintain performance across unknown decoding conditions.
68	
69	The cross-model feature ordering (Section~\ref{sec:feature_degradation}) provides a complementary perspective: among continuation-mode models, single-feature $\auc$ rankings are highly consistent (Spearman $\rho \geq 0.85$), with surprisal-variance features---\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}---dominating uniformly.
70	A genuine limitation, however, is that depth-pair-level agreement weakens to $\tau \approx 0.37$ at the 1v2 boundary (Section~\ref{sec:feature_degradation}), indicating that the relative contribution of individual features at the discrimination boundary varies across models even when the aggregate ordering is shared.
71	
72	\subsection{Scale Considerations}
73	\label{sec:discuss_scale}
74	
75	Our experiments establish $\Kempirical = 2$ at the $\leq$1.5B parameter scale, providing the first empirical measurement of the generational depth boundary for language models.
76	This result constitutes a \emph{methodological lower bound}: the framework itself---15-dimensional token-level features, OBD-optimized classification, bootstrap confidence intervals, and permutation testing---is model-scale agnostic by construction.
77	All 15 features are computed from surface-level token statistics (surprisal moments, vocabulary diversity, frequency tail measures) without access to model internals, and the cross-model transfer results (80--92\% retention across architecturally distinct model families; Section~\ref{sec:transfer}) already demonstrate that the methodology generalizes across different architectures and training corpora at the tested scale.
78	
79	Scaling to larger models presents two possible outcomes, both of which reinforce rather than diminish the contribution.
80	If $\Kempirical > 2$ at 7B+ scales---as suggested by scaling laws showing that larger models exhibit slower tail-distribution degradation rates~\cite{dohmatob2024model, kaplan2020scaling}---then depth contamination becomes \emph{more} insidious: higher-fidelity generations would produce weaker depth signatures, making fine-grained detection more critical and the systematic framework we introduce more necessary.
81	Conversely, if $\Kempirical = 2$ persists at larger scales, our conclusions generalize directly.
82	In either case, the measurement methodology established here---the feature taxonomy, the $\Kstar$ estimation protocol, and the cross-model validation framework---provides the requisite infrastructure for characterizing depth boundaries at any scale.
83	The model collapse literature supports the expectation that depth-related phenomena are scale-persistent: Shumailov et al.~\cite{shumailov2024collapse} observed tail-mode collapse across model sizes, and Alemohammad et al.~\cite{alemohammad2024selfconsuming} proved fixed-point convergence for self-consuming generators without scale-dependent assumptions.
84	
85	We identify 7B-scale cross-scale validation as the immediate next step.
86	The experimental pipeline---data generation, feature extraction, and classifier evaluation---is fully implemented and directly applicable to larger models; only computational budget constrains this extension.
87	Critically, this limitation does not affect the validity of the $\Kempirical = 2$ result at $\leq$1.5B, which stands as the first empirical characterization of generational depth boundaries in language model outputs.
88	
89	\subsection{LLM Zero-Shot Baseline}
90	\label{sec:discuss_llm}
91	
92	Frontier LLMs provide a natural baseline for depth estimation.
93	On a 500-sample test set with 5 depth classes (depths 0--4), excluding depth~5 from the 6-class range used in the main feature-based experiments since depths $\geq 3$ are mutually indistinguishable ($\Kempirical = 2$), GPT-5.5 achieves 33.2\% accuracy (MAE = 1.10) and Claude Opus~4.6 achieves 33.1\% accuracy (MAE = 1.15)---both below the OBD-LightGBM baseline of 38.6\% (MAE = 1.11; see Table~\ref{tab:s3_llm_zeroshot} for per-depth confusion matrices).
94	Simultaneously, both models achieve approximately 88\% binary accuracy on the human-vs.-synthetic distinction (GPT-5.5: 87.8\%, Claude: 88.2\%).
95	
96	This gap between binary detection and depth estimation is informative.
97	Frontier LLMs can reliably determine \emph{whether} a text is machine-generated but cannot estimate \emph{how many generations of recursive processing} it has undergone.
98	Depth estimation requires sensitivity to subtle distributional shifts between adjacent generations---shifts orders of magnitude smaller than the human-vs.-machine gap.
99	The 15-dimensional statistical feature pipeline, despite its simplicity, captures these fine-grained shifts more effectively than frontier LLMs in a zero-shot setting.
100	This motivates the dedicated feature-engineering approach: the task demands specialized statistical sensitivity rather than general language understanding.
101	We evaluate only zero-shot prompting; few-shot or chain-of-thought strategies may narrow the gap and warrant future investigation.
102	
103	\subsection{Limitations}
104	\label{sec:limitations}
105	
106	We identify seven limitations that bound the generalizability of our findings.
107	
108	\emph{Model scale.}
109	All experiments use models at or below 1.5B parameters (Pythia-1.4B, OLMo-1B, Qwen2.5-1.5B-Instruct).
110	Larger models may produce higher-fidelity text with weaker depth signatures, potentially shifting $\Kempirical$ beyond~2.
111	
112	\emph{Prompt-chain versus retrain-chain.}
113	Our recursive generation protocol is a prompt-chain: the same fixed model repeatedly generates from the previous output.
114	Real-world model collapse involves retrain-chains, where models are retrained on data from earlier generations~\cite{shumailov2024collapse}.
115	Retrain-chains introduce additional degradation through training dynamics, potentially producing different $\Kstar$ values.
116	
117	\emph{Language and domain.}
118	All experiments use English text from the C4 corpus.
119	Depth dynamics may differ across languages, domains (e.g., code, scientific text), and source corpora with different distributional properties.
120	
121	\emph{Decoding coverage.}
122	We test four decoding strategies (greedy, nucleus $p{=}0.9$, $T{=}0.7$, $T{=}1.2$).
123	Other strategies---top-$k$ sampling, beam search, contrastive decoding---remain untested and may yield different feature importance patterns or boundary behavior.
124	
125	\emph{Threshold sensitivity.}
126	$\Kempirical$ depends on the operational threshold $\theta$.
127	$\Kempirical \geq 2$ across $\theta \in \{0.55, 0.60, 0.65\}$ for all four decoding strategies, rising to $\Kempirical = 3$ at $\theta = 0.55$ (all four 2v3 $\auc$ values exceed 0.55) and returning to $\Kempirical = 2$ at $\theta \in \{0.60, 0.65\}$.
128	At $\theta = 0.70$, three of four decoding configurations collapse to $\Kempirical = 1$; only the high-temperature setting ($T{=}1.2$) retains $\Kempirical = 2$, consistent with its elevated 1v2 $\auc$ (0.7039).
129	Beyond decoding parameters, the threshold sensitivity extends to generation mode: at $\theta{=}0.70$, $\Kempirical{=}1$ for all four model-mode configurations; at $\theta{=}0.65$, continuation-mode configurations already drop to $\Kempirical{=}1$, while rewrite mode retains $\Kempirical{=}2$.
130	Our current analysis primarily covers the decoding configuration axis.
131	The boundary is robust within a practical range but not invariant to threshold choice; our conclusions are conditioned on $\theta = 0.60$.
132	
133	\emph{Boundary marginality.}
134	The $\Kempirical = 2$ determination is statistically significant but numerically marginal at both ends.
135	On the lower side, Qwen-continuation's 1v2 CI lower bound (0.6015) exceeds $\theta = 0.60$ by only $+$0.15\,pp.
136	On the upper side, Qwen-rewrite's 2v3 CI upper bound (0.5991) falls below $\theta$ by only $-$0.09\,pp.
137	This narrow margin means that small changes in the feature set or classifier could shift the boundary---as the neural probe results confirm, where a richer representation pushes the 2v3 pair above $\theta$ on the Qwen-continuation dataset (Section~\ref{sec:discuss_kstar}).
138	Importantly, all eight boundary comparisons (four 1v2 and four 2v3) yield permutation $p < 0.01$, confirming that the statistical significance of the distinction is not in doubt---only its proximity to the operational threshold.
139	
140	\emph{Operational versus theoretical boundary.}
141	$\Kempirical$ is an operational lower bound that depends on the specific feature set and classifier.
142	$\Ktheory$ may be strictly greater; a more expressive classifier or richer feature representation could push $\Kempirical$ higher.
143	Preliminary neural probing results provide direct evidence for this gap: on the Qwen-continuation dataset, a frozen-encoder MLP achieves $\Kempirical^{\text{neural}} = 3$ (2v3 $\auc = 0.6195$) compared to $\Kempirical = 2$ with 15-dimensional hand-crafted features (2v3 $\auc = 0.5609$; Section~\ref{sec:kstar_boundary}).
144	This confirms that the 15D feature set does not saturate the available depth signal and that $\Ktheory \geq 3$.
145	However, the neural probe result rests on a single dataset and awaits cross-model validation and bootstrap confidence intervals before a firm revision of the headline $\Kempirical$ can be claimed.
146	
147	\emph{Feature representation.}
148	The 15-dimensional hand-crafted feature set, while interpretable and transferable, is not optimal.
149	A preliminary neural probing experiment demonstrates that frozen LLM embeddings (1536 dimensions) paired with a lightweight MLP push $\Kempirical$ from~2 to~3 on the Qwen-continuation dataset (Section~\ref{sec:discuss_kstar}), confirming that learned representations capture depth-discriminative patterns that statistical features miss.
150	The magnitude of the gain---2v3 $\auc$ rising from 0.5609 to 0.6195---indicates meaningful recoverable signal beyond what hand-crafted features extract.
151	Full characterization of this gap, including cross-model generalization and bootstrap uncertainty quantification, remains future work.
152	
153	\paragraph{Graduated Filtering.}
154	Results for graduated filtering will be added upon completion of ongoing experiments.
155	
156	\subsection{Broader Impact}
157	\label{sec:broader_impact}
158	
159	The $\Kempirical = 2$ boundary has implications beyond the immediate scope of depth classification.
160	
161	\paragraph{Synthetic data curation.}
162	The practical consequence of $\Kempirical = 2$ is a three-tier taxonomy of text quality: human-authored (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\geq 2$).
163	Texts at depth~$\geq 2$ are mutually indistinguishable and can be treated as a single category for curation purposes.
164	For practitioners filtering training data, this implies that a single round of synthetic rewriting suffices to make text statistically indistinguishable from text that has undergone multiple rounds of recycling---a form of one-wash laundering that limits the granularity of quality-based filtering.
165	This underscores the urgency of deploying depth-aware curation mechanisms before the first generation step, rather than relying on post-hoc detection.
166	Graduated filtering strategies that exploit this trichotomy may outperform binary human/synthetic filters, as the coarse ordinal signal (human / shallow / deep) captures the dominant axis of quality variation.
167	
168	\paragraph{Relation to model collapse.}
169	Shumailov et al.~\cite{shumailov2024collapse} and Alemohammad et al.~\cite{alemohammad2024selfconsuming} study model collapse under \emph{retrain-chains}, where models are iteratively trained on their own outputs.
170	Our prompt-chain protocol measures an adjacent but distinct phenomenon: the degradation of statistical distinguishability under recursive generation by a fixed model.
171	The rapid convergence we observe ($\Kempirical = 2$) is consistent with the theoretical prediction of convergence to a fixed point, but the precise relationship between prompt-chain $\Kempirical$ and retrain-chain convergence rates remains an open question.
172	If prompt-chain depth signals serve as an observable proxy for early-stage model collapse, depth estimation could provide a lightweight diagnostic for data curation pipelines without requiring expensive retraining experiments.
173	
174	\paragraph{AI text detection.}
175	Current AI text detection is predominantly binary: human versus machine.
176	Our results suggest that \emph{depth-aware} detection provides a strictly more informative signal.
177	The near-perfect 0v1 separability ($\auc > 0.99$) confirms that binary detection is reliable at this scale, but the 1v2 boundary ($\auc$: 0.61--0.70) reveals that first-generation text retains measurable statistical distance from deeper synthetic text.
178	This additional dimension---how many generations of processing a text has undergone---may prove valuable for provenance tracking and corpus quality assessment, where the binary human/AI label elides important distinctions between lightly and heavily recycled content.
179	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "26232d9f-b7e4-4afa-8a3e-452312507fe8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\subsection{Theoretical Implications of $\\Kempirical = 2$}\n\\label{sec:discuss_kstar}\n\nThe Data Processing Inequality guarantees the existence of a finite $\\Ktheory$ beyond which adjacent generations become indistinguishable (Section~\\ref{sec:formulation}).\nOur empirical result---$\\Kempirical = 2$ consistently across all 8 tested configurations (4 model-mode combinations and 4 decoding strategies; Section~\\ref{sec:kstar_boundary}, Figure~\\ref{fig:auc_decay})---establishes that this boundary is not only finite but remarkably shallow at the $\\leq$1.5B parameter scale.\n\nThe shallowness of $\\Kempirical$ is explained by the rate of information loss across generations.\nThe 0v1 boundary is near-trivially separable ($\\auc > 0.99$ across all configurations; Table~\\ref{tab:kstar_ci}), reflecting the large distributional gap between human text and first-generation synthetic text.\nAt the 1v2 boundary, $\\auc$ drops by approximately 30 percentage points ($\\auc$ range: 0.6112--0.7039 across all eight model$\\times$decoding conditions; Table~\\ref{tab:kstar_ci}, Figure~\\ref{fig:auc_decay}; see also Figure~\\ref{fig:s1_auc_decay_ci} in the Appendix), indicating that the majority of the discriminative signal is consumed in the first generation step.\nBy the 2v3 boundary, $\\auc$ falls to 0.5496--0.5917 across all eight model$\\times$decoding conditions (upper bound from nucleus $p{=}0.9$ decoding; Figure~\\ref{fig:auc_decay})---below the operational threshold $\\theta = 0.60$---and deeper pairs converge toward chance.\nRecursive generation thus acts as a severely lossy channel whose information bottleneck is traversed within two steps.\n\nThe feature degradation analysis (Section~\\ref{sec:feature_degradation}) provides mechanistic evidence for this rapid collapse.\nThe most discriminative features---surprisal variance (\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_std}) and its derivatives---all capture the heterogeneity of token-level predictability.\nHuman text exhibits high surprisal variance reflecting diverse syntactic structures and unpredictable discourse patterns.\nThe first generation step smooths this variance substantially, replacing high-surprisal tokens and atypical constructions with more predictable alternatives; the second step reduces the remaining variance to near-floor levels, leaving insufficient statistical fingerprint for reliable adjacent-depth discrimination.\nCrucially, this degradation ordering is consistent across model families (Spearman $\\rho \\geq 0.85$ for all continuation-mode pairs; Table~\\ref{tab:top_features}), suggesting that the two-step information loss is governed by the autoregressive generation mechanism itself rather than by model-specific biases.\n\nThis pattern aligns with findings from the model collapse literature.\nShumailov et al.~\\cite{shumailov2024collapse} observed that tail-distribution degradation is most acute in the earliest generations, with minority modes vanishing before the output distribution stabilizes.\nDohmatob et al.~\\cite{dohmatob2024model} derived scaling laws demonstrating that tail probability mass is lost at rates predictable from model and data scale.\nOur $\\Kempirical = 2$ provides a complementary, classifier-based measurement of this phenomenon: the information-theoretic discrimination boundary is reached after just two generation steps.\nAlemohammad et al.~\\cite{alemohammad2024selfconsuming} proved convergence to a fixed point for self-consuming generative models; $\\Kempirical = 2$ indicates that, operationally, the approach to this fixed point is rapid enough that adjacent-generation distinctions collapse within two steps.\n\nImportantly, $\\Kempirical = 2$ is an \\emph{operational} lower bound conditioned on the 15-dimensional hand-crafted feature set; the \\emph{theoretical} boundary $\\Ktheory$ may be strictly higher.\nPreliminary evidence from a neural probing experiment supports this distinction.\nA frozen Qwen2.5-1.5B encoder (1536-dimensional last-layer representations) paired with a lightweight MLP classifier (Table~\\ref{tab:s7_neural_probe}) achieves 2v3 $\\auc = 0.6195$ ($\\text{std} = 0.0094$) on the Qwen-continuation dataset, exceeding the $\\theta = 0.60$ threshold that the same dataset's LightGBM classifier fails to cross ($\\auc = 0.5609$; Section~\\ref{sec:kstar_boundary}).\nThis yields $\\Kempirical^{\\text{neural}} = 3$: the learned representation recovers one additional discriminable boundary that the hand-crafted features miss.\nThe improvement is concentrated at the 2v3 pair ($+$5.86\\,pp over LightGBM); at the already-separable 1v2 boundary the neural probe achieves 0.6983 versus 0.6112, a substantial gain but one that does not alter the boundary determination.\nAt 3v4, the neural probe reaches $\\auc = 0.5930$---below $\\theta$ but closer to the threshold than any hand-crafted configuration---suggesting that a still richer representation might push the boundary further.\nThe lossy-channel narrative remains intact: even with 1536-dimensional frozen representations, the discrimination boundary extends to only three steps, confirming that the information bottleneck of recursive generation is shallow even with substantially richer representations.\nThese results are preliminary: they cover a single model-dataset pair (Qwen-continuation) and lack bootstrap confidence intervals; cross-model validation on Pythia and OLMo is pending.\n\nThe invariance of $\\Kempirical = 2$ across decoding strategies merits emphasis.\nGreedy decoding, nucleus sampling ($p{=}0.9$), $T{=}0.7$, and $T{=}1.2$ all yield $\\Kempirical = 2$ (Figure~\\ref{fig:auc_decay}; Table~\\ref{tab:s2_decoding}), with 1v2 $\\auc$ spanning a narrow range of [0.6866, 0.7039].\nHigher decoding entropy modestly increases signal strength ($\\auc_{1,2}$: 0.69 greedy $\\to$ 0.70 at $T{=}1.2$) but does not shift the boundary.\nThis robustness suggests that $\\Kempirical$ is governed by the fundamental information bottleneck of the generation process rather than by surface-level properties of the sampling algorithm.\n\n\\subsection{Implications of Cross-Model Transfer}\n\\label{sec:discuss_transfer}\n\nThe cross-model transfer results (Section~\\ref{sec:transfer}) indicate that depth signals are largely encoded in text-level statistical properties rather than generator-specific artifacts.\nClassifiers trained on Pythia-1.4B and evaluated on OLMo-1B retain 90--92\\% of within-model accuracy, and the broader continuation-mode transfer matrix shows 80--92\\% retention across all model pairs (Table~\\ref{tab:transfer_matrix}; see Table~\\ref{tab:s1_transfer} for the full matrix).\nAt the 0v1 boundary, cross-model $\\auc$ exceeds 0.96 across all tested model pairs, confirming that binary contamination detection is fully transferable across the tested generators.\n\nThe practical implication is direct: a single depth classifier trained on one model's outputs can be deployed to estimate generational depth for texts produced by other models, without model-specific retraining.\nThis transferability extends the utility of depth estimation to open-web settings where the generating model is unknown---precisely the scenario where depth-aware data curation is most needed.\n\nTwo caveats bound this conclusion.\nFirst, the text-intrinsic component dominates, as evidenced by high cross-model transfer retention (80--92\\% across continuation-mode pairs), yet a nontrivial model-specific residual persists.\nThe Pythia$\\leftrightarrow$OLMo pair, which spans different architectures and training corpora, achieves the highest cross-family retention (90--92\\%), consistent with the depth signal being largely architecture-agnostic within continuation mode.\nSecond, Qwen-continuation$\\leftrightarrow$OLMo retention (80--85\\%) is lower than Pythia$\\leftrightarrow$OLMo (90--92\\%), indicating that model family similarity modulates transfer even among continuation-mode configurations.\n\n\\subsection{Feature Importance Across Decoding Strategies}\n\\label{sec:discuss_features}\n\nWhile $\\Kempirical = 2$ is invariant to decoding strategy (4/4 configurations), the feature importance ordering is not uniformly consistent.\nGreedy decoding and $T{=}0.7$ share highly correlated feature rankings (Spearman $\\rho = 0.914$), with top features dominated by vocabulary diversity measures: \\texttt{self\\_bleu}, \\texttt{hapax\\_ratio}, and \\texttt{ttr}.\nIn contrast, greedy versus $T{=}1.2$ yields a lower correlation ($\\rho = 0.53$, $p = 0.041$; suggestive but nonsignificant after Bonferroni correction for 6 pairwise comparisons), with $T{=}1.2$ promoting \\texttt{hapax\\_ratio}, \\texttt{ttr}, and \\texttt{surp\\_skew} to the top ranks.\nNotably, \\texttt{freq\\_entropy} rises from rank~10 under greedy ($\\auc = 0.5139$) to rank~5 under $T{=}1.2$ ($\\auc = 0.5905$), illustrating how high-entropy decoding amplifies frequency-distribution artifacts.\n\nThis dissociation reveals an important distinction: the \\emph{existence} of the depth boundary is robust, but the \\emph{optimal feature subset} for detecting it depends on the sampling strategy.\nHigh-entropy decoding amplifies frequency-distribution artifacts while attenuating vocabulary-diversity signals, shifting which text properties carry the most discriminative power without altering whether adjacent generations can be distinguished.\nFor practitioners, this implies that a general-purpose depth classifier should incorporate features from multiple groups---surprisal moments, vocabulary diversity, and frequency tail statistics---to maintain performance across unknown decoding conditions.\n\nThe cross-model feature ordering (Section~\\ref{sec:feature_degradation}) provides a complementary perspective: among continuation-mode models, single-feature $\\auc$ rankings are highly consistent (Spearman $\\rho \\geq 0.85$), with surprisal-variance features---\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_std}, \\texttt{surp\\_d2\\_std}---dominating uniformly.\nA genuine limitation, however, is that depth-pair-level agreement weakens to $\\tau \\approx 0.37$ at the 1v2 boundary (Section~\\ref{sec:feature_degradation}), indicating that the relative contribution of individual features at the discrimination boundary varies across models even when the aggregate ordering is shared.\n\n\\subsection{Scale Considerations}\n\\label{sec:discuss_scale}\n\nOur experiments establish $\\Kempirical = 2$ at the $\\leq$1.5B parameter scale, providing the first empirical measurement of the generational depth boundary for language models.\nThis result constitutes a \\emph{methodological lower bound}: the framework itself---15-dimensional token-level features, OBD-optimized classification, bootstrap confidence intervals, and permutation testing---is model-scale agnostic by construction.\nAll 15 features are computed from surface-level token statistics (surprisal moments, vocabulary diversity, frequency tail measures) without access to model internals, and the cross-model transfer results (80--92\\% retention across architecturally distinct model families; Section~\\ref{sec:transfer}) already demonstrate that the methodology generalizes across different architectures and training corpora at the tested scale.\n\nScaling to larger models presents two possible outcomes, both of which reinforce rather than diminish the contribution.\nIf $\\Kempirical > 2$ at 7B+ scales---as suggested by scaling laws showing that larger models exhibit slower tail-distribution degradation rates~\\cite{dohmatob2024model, kaplan2020scaling}---then depth contamination becomes \\emph{more} insidious: higher-fidelity generations would produce weaker depth signatures, making fine-grained detection more critical and the systematic framework we introduce more necessary.\nConversely, if $\\Kempirical = 2$ persists at larger scales, our conclusions generalize directly.\nIn either case, the measurement methodology established here---the feature taxonomy, the $\\Kstar$ estimation protocol, and the cross-model validation framework---provides the requisite infrastructure for characterizing depth boundaries at any scale.\nThe model collapse literature supports the expectation that depth-related phenomena are scale-persistent: Shumailov et al.~\\cite{shumailov2024collapse} observed tail-mode collapse across model sizes, and Alemohammad et al.~\\cite{alemohammad2024selfconsuming} proved fixed-point convergence for self-consuming generators without scale-dependent assumptions.\n\nWe identify 7B-scale cross-scale validation as the immediate next step.\nThe experimental pipeline---data generation, feature extraction, and classifier evaluation---is fully implemented and directly applicable to larger models; only computational budget constrains this extension.\nCritically, this limitation does not affect the validity of the $\\Kempirical = 2$ result at $\\leq$1.5B, which stands as the first empirical characterization of generational depth boundaries in language model outputs.\n\n\\subsection{LLM Zero-Shot Baseline}\n\\label{sec:discuss_llm}\n\nFrontier LLMs provide a natural baseline for depth estimation.\nOn a 500-sample test set with 5 depth classes (depths 0--4), excluding depth~5 from the 6-class range used in the main feature-based experiments since depths $\\geq 3$ are mutually indistinguishable ($\\Kempirical = 2$), GPT-5.5 achieves 33.2\\% accuracy (MAE = 1.10) and Claude Opus~4.6 achieves 33.1\\% accuracy (MAE = 1.15)---both below the OBD-LightGBM baseline of 38.6\\% (MAE = 1.11; see Table~\\ref{tab:s3_llm_zeroshot} for per-depth confusion matrices).\nSimultaneously, both models achieve approximately 88\\% binary accuracy on the human-vs.-synthetic distinction (GPT-5.5: 87.8\\%, Claude: 88.2\\%).\n\nThis gap between binary detection and depth estimation is informative.\nFrontier LLMs can reliably determine \\emph{whether} a text is machine-generated but cannot estimate \\emph{how many generations of recursive processing} it has undergone.\nDepth estimation requires sensitivity to subtle distributional shifts between adjacent generations---shifts orders of magnitude smaller than the human-vs.-machine gap.\nThe 15-dimensional statistical feature pipeline, despite its simplicity, captures these fine-grained shifts more effectively than frontier LLMs in a zero-shot setting.\nThis motivates the dedicated feature-engineering approach: the task demands specialized statistical sensitivity rather than general language understanding.\nWe evaluate only zero-shot prompting; few-shot or chain-of-thought strategies may narrow the gap and warrant future investigation.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\nWe identify seven limitations that bound the generalizability of our findings.\n\n\\emph{Model scale.}\nAll experiments use models at or below 1.5B parameters (Pythia-1.4B, OLMo-1B, Qwen2.5-1.5B-Instruct).\nLarger models may produce higher-fidelity text with weaker depth signatures, potentially shifting $\\Kempirical$ beyond~2.\n\n\\emph{Prompt-chain versus retrain-chain.}\nOur recursive generation protocol is a prompt-chain: the same fixed model repeatedly generates from the previous output.\nReal-world model collapse involves retrain-chains, where models are retrained on data from earlier generations~\\cite{shumailov2024collapse}.\nRetrain-chains introduce additional degradation through training dynamics, potentially producing different $\\Kstar$ values.\n\n\\emph{Language and domain.}\nAll experiments use English text from the C4 corpus.\nDepth dynamics may differ across languages, domains (e.g., code, scientific text), and source corpora with different distributional properties.\n\n\\emph{Decoding coverage.}\nWe test four decoding strategies (greedy, nucleus $p{=}0.9$, $T{=}0.7$, $T{=}1.2$).\nOther strategies---top-$k$ sampling, beam search, contrastive decoding---remain untested and may yield different feature importance patterns or boundary behavior.\n\n\\emph{Threshold sensitivity.}\n$\\Kempirical$ depends on the operational threshold $\\theta$.\n$\\Kempirical \\geq 2$ across $\\theta \\in \\{0.55, 0.60, 0.65\\}$ for all four decoding strategies, rising to $\\Kempirical = 3$ at $\\theta = 0.55$ (all four 2v3 $\\auc$ values exceed 0.55) and returning to $\\Kempirical = 2$ at $\\theta \\in \\{0.60, 0.65\\}$.\nAt $\\theta = 0.70$, three of four decoding configurations collapse to $\\Kempirical = 1$; only the high-temperature setting ($T{=}1.2$) retains $\\Kempirical = 2$, consistent with its elevated 1v2 $\\auc$ (0.7039).\nBeyond decoding parameters, the threshold sensitivity extends to generation mode: at $\\theta{=}0.70$, $\\Kempirical{=}1$ for all four model-mode configurations; at $\\theta{=}0.65$, continuation-mode configurations already drop to $\\Kempirical{=}1$, while rewrite mode retains $\\Kempirical{=}2$.\nOur current analysis primarily covers the decoding configuration axis.\nThe boundary is robust within a practical range but not invariant to threshold choice; our conclusions are conditioned on $\\theta = 0.60$.\n\n\\emph{Boundary marginality.}\nThe $\\Kempirical = 2$ determination is statistically significant but numerically marginal at both ends.\nOn the lower side, Qwen-continuation's 1v2 CI lower bound (0.6015) exceeds $\\theta = 0.60$ by only $+$0.15\\,pp.\nOn the upper side, Qwen-rewrite's 2v3 CI upper bound (0.5991) falls below $\\theta$ by only $-$0.09\\,pp.\nThis narrow margin means that small changes in the feature set or classifier could shift the boundary---as the neural probe results confirm, where a richer representation pushes the 2v3 pair above $\\theta$ on the Qwen-continuation dataset (Section~\\ref{sec:discuss_kstar}).\nImportantly, all eight boundary comparisons (four 1v2 and four 2v3) yield permutation $p < 0.01$, confirming that the statistical significance of the distinction is not in doubt---only its proximity to the operational threshold.\n\n\\emph{Operational versus theoretical boundary.}\n$\\Kempirical$ is an operational lower bound that depends on the specific feature set and classifier.\n$\\Ktheory$ may be strictly greater; a more expressive classifier or richer feature representation could push $\\Kempirical$ higher.\nPreliminary neural probing results provide direct evidence for this gap: on the Qwen-continuation dataset, a frozen-encoder MLP achieves $\\Kempirical^{\\text{neural}} = 3$ (2v3 $\\auc = 0.6195$) compared to $\\Kempirical = 2$ with 15-dimensional hand-crafted features (2v3 $\\auc = 0.5609$; Section~\\ref{sec:kstar_boundary}).\nThis confirms that the 15D feature set does not saturate the available depth signal and that $\\Ktheory \\geq 3$.\nHowever, the neural probe result rests on a single dataset and awaits cross-model validation and bootstrap confidence intervals before a firm revision of the headline $\\Kempirical$ can be claimed.\n\n\\emph{Feature representation.}\nThe 15-dimensional hand-crafted feature set, while interpretable and transferable, is not optimal.\nA preliminary neural probing experiment demonstrates that frozen LLM embeddings (1536 dimensions) paired with a lightweight MLP push $\\Kempirical$ from~2 to~3 on the Qwen-continuation dataset (Section~\\ref{sec:discuss_kstar}), confirming that learned representations capture depth-discriminative patterns that statistical features miss.\nThe magnitude of the gain---2v3 $\\auc$ rising from 0.5609 to 0.6195---indicates meaningful recoverable signal beyond what hand-crafted features extract.\nFull characterization of this gap, including cross-model generalization and bootstrap uncertainty quantification, remains future work.\n\n\\paragraph{Graduated Filtering.}\nResults for graduated filtering will be added upon completion of ongoing experiments.\n\n\\subsection{Broader Impact}\n\\label{sec:broader_impact}\n\nThe $\\Kempirical = 2$ boundary has implications beyond the immediate scope of depth classification.\n\n\\paragraph{Synthetic data curation.}\nThe practical consequence of $\\Kempirical = 2$ is a three-tier taxonomy of text quality: human-authored (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\\geq 2$).\nTexts at depth~$\\geq 2$ are mutually indistinguishable and can be treated as a single category for curation purposes.\nFor practitioners filtering training data, this implies that a single round of synthetic rewriting suffices to make text statistically indistinguishable from text that has undergone multiple rounds of recycling---a form of one-wash laundering that limits the granularity of quality-based filtering.\nThis underscores the urgency of deploying depth-aware curation mechanisms before the first generation step, rather than relying on post-hoc detection.\nGraduated filtering strategies that exploit this trichotomy may outperform binary human/synthetic filters, as the coarse ordinal signal (human / shallow / deep) captures the dominant axis of quality variation.\n\n\\paragraph{Relation to model collapse.}\nShumailov et al.~\\cite{shumailov2024collapse} and Alemohammad et al.~\\cite{alemohammad2024selfconsuming} study model collapse under \\emph{retrain-chains}, where models are iteratively trained on their own outputs.\nOur prompt-chain protocol measures an adjacent but distinct phenomenon: the degradation of statistical distinguishability under recursive generation by a fixed model.\nThe rapid convergence we observe ($\\Kempirical = 2$) is consistent with the theoretical prediction of convergence to a fixed point, but the precise relationship between prompt-chain $\\Kempirical$ and retrain-chain convergence rates remains an open question.\nIf prompt-chain depth signals serve as an observable proxy for early-stage model collapse, depth estimation could provide a lightweight diagnostic for data curation pipelines without requiring expensive retraining experiments.\n\n\\paragraph{AI text detection.}\nCurrent AI text detection is predominantly binary: human versus machine.\nOur results suggest that \\emph{depth-aware} detection provides a strictly more informative signal.\nThe near-perfect 0v1 separability ($\\auc > 0.99$) confirms that binary detection is reliable at this scale, but the 1v2 boundary ($\\auc$: 0.61--0.70) reveals that first-generation text retains measurable statistical distance from deeper synthetic text.\nThis additional dimension---how many generations of processing a text has undergone---may prove valuable for provenance tracking and corpus quality assessment, where the binary human/AI label elides important distinctions between lightly and heavily recycled content.\n",
      "numLines": 179,
      "startLine": 1,
      "totalLines": 179
    }
  }
}
```

</details>

---

### Assistant

_source line 56_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the writing style, commands, and context. Let me write the two versions of the C3 conclusion text. I need to create the file at `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/c3_contingency_versions.tex`.

Key style observations:
- Measured, precise academic tone
- Uses \Kempirical, \auc, \Kstar, \Ktheory commands
- References sections/tables with Section~\ref{}, Table~\ref{}
- Numbers with \,pp for percentage points


- Em-dashes for elaboration
- \texttt{} for feature names
- Tilde for non-breaking spaces with references

Now I'll draft both versions with their conclusion and discussion paragraphs, maintaining the formal LaTeX structure and academic voice throughout.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "38dd2e60-c855-4068-a46a-bddab6227fd0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MF8MTuWeAX2PxqmUBQfA14",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10942,
      "cache_read_input_tokens": 26873,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10942
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

_source line 57_

Now I have the full style context. Let me write the contingency versions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "f1c32742-e03e-4dd9-b7b9-1e8b9a80ba05",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MF8MTuWeAX2PxqmUBQfA14",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10942,
      "cache_read_input_tokens": 26873,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10942
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

_source line 58_

<details open><summary>🔧 Tool call — Write · `toolu_01GRgEbqR9RhcBaTjRBPaSve`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/c3_contingency_versions.tex",
  "content": "%% ======================================================================\n%% C3 Graduated Filtering — Contingency Text Versions\n%% Pre-written for exp-006 results (ETA 2026-05-15).\n%% Replace XX.X ± X.X placeholders with actual numbers once available.\n%% ======================================================================\n\n\n%% ======================================================================\n%% VERSION A — Graduated filtering significantly outperforms binary\n%% ======================================================================\n\n%% --- For conclusion.tex (replace the C3 TODO block, lines 48–53) ---\n\n% === Contribution 3: Graduated filtering (C3) ===\n% Source: exp-006\nThe $\\Kempirical = 2$ boundary implies a natural trichotomy---human\n(depth~0), first-generation synthetic (depth~1), and deeper synthetic\n(depth~$\\geq 2$)---that can be exploited for depth-aware data curation.\nGraduated filtering, which assigns sample weights $w = \\exp(-\\alpha\n\\cdot \\hat{d})$ based on the OBD-predicted expected depth $\\hat{d}$,\noutperforms both binary filtering strategies on downstream benchmarks:\nat the optimal $\\alpha^* = $ XX.X, LoRA-tuned Qwen2.5-1.5B-Instruct\nachieves XX.X $\\pm$ X.X on MMLU and XX.X $\\pm$ X.X on HellaSwag,\ncompared to XX.X $\\pm$ X.X / XX.X $\\pm$ X.X for binary-ours and\nXX.X $\\pm$ X.X / XX.X $\\pm$ X.X for binary-Drayson\n(Table~\\ref{tab:filtering_main}).\nThe gain is attributable to the retention of depth-1 content, which\npreserves substantial original signal while only gently down-weighting\nfirst-generation text; binary strategies discard this stratum entirely,\nsacrificing data volume without commensurate quality improvement.\nThis validates the practical utility of the three-tier taxonomy derived\nfrom $\\Kempirical = 2$: depth-aware curation that distinguishes shallow\nfrom deep synthetic content yields measurably better training corpora\nthan the binary human-versus-synthetic partition.\n\n%% --- For discussion.tex (new subsection or append to §Broader Impact) ---\n\n\\paragraph{Graduated versus binary filtering.}\nThe graduated filtering results (Section~\\ref{sec:graduated-filtering})\nprovide direct evidence that the $\\Kempirical = 2$ trichotomy has\nactionable value for data curation.\nThe optimal decay parameter $\\alpha^* = $ XX.X falls in the moderate\nrange, neither so low as to approximate no-filter ($\\alpha \\to 0$) nor\nso high as to degenerate to hard binary filtering ($\\alpha \\to \\infty$).\nThis intermediate optimum reflects the core insight: depth-1 text, while\ndetectably synthetic, retains enough of the original distribution's\ndiversity---as evidenced by elevated surprisal variance and vocabulary\nrichness relative to depth~$\\geq 2$ (Section~\\ref{sec:feature_degradation})---to\nbenefit downstream training when appropriately down-weighted rather than\ndiscarded.\nThe MMLU improvement of $+$XX.X\\,pp over binary-ours and\n$+$XX.X\\,pp over binary-Drayson, together with consistent gains on\nHellaSwag ($+$XX.X\\,pp and $+$XX.X\\,pp, respectively), demonstrate\nthat the signal preserved in the depth-1 stratum translates to\nmeasurable downstream quality across both knowledge-intensive and\ncommonsense reasoning tasks.\nGraduated filtering also exhibits lower cross-seed variance than binary\nstrategies (XX.X versus XX.X on MMLU), suggesting that the ordinal\nweighting scheme provides a more stable curation signal than hard\nclassification boundaries.\n\n\n%% ======================================================================\n%% VERSION B — Graduated filtering NOT significantly better than binary\n%% ======================================================================\n\n%% --- For conclusion.tex (replace the C3 TODO block, lines 48–53) ---\n\n% === Contribution 3: Graduated filtering (C3) ===\n% Source: exp-006\nThe $\\Kempirical = 2$ boundary implies a natural trichotomy---human\n(depth~0), first-generation synthetic (depth~1), and deeper synthetic\n(depth~$\\geq 2$)---that provides a principled framework for depth-aware\ndata curation.\nWe evaluate graduated filtering, which assigns sample weights\n$w = \\exp(-\\alpha \\cdot \\hat{d})$ based on predicted expected depth, against\nbinary filtering baselines (Table~\\ref{tab:filtering_main}).\nAt the best $\\alpha$, graduated filtering achieves XX.X $\\pm$ X.X on\nMMLU and XX.X $\\pm$ X.X on HellaSwag, comparable to binary-ours\n(XX.X $\\pm$ X.X / XX.X $\\pm$ X.X) and binary-Drayson\n(XX.X $\\pm$ X.X / XX.X $\\pm$ X.X); the differences are not\nstatistically significant across 5 seeds ($p >$ XX.XX).\nThe three-tier taxonomy nonetheless provides a principled alternative to\nbinary filtering: graduated weighting achieves comparable downstream\nperformance while retaining a larger effective corpus through soft\ndown-weighting rather than hard exclusion, and the continuous $\\alpha$\nparameter offers practitioners an explicit knob for trading off data\nvolume against depth penalty---a degree of freedom absent from binary\nschemes.\n\n%% --- For discussion.tex (new subsection or append to §Broader Impact) ---\n\n\\paragraph{Graduated versus binary filtering.}\nThe comparable performance of graduated and binary filtering\n(Section~\\ref{sec:graduated-filtering}) admits several explanations.\nFirst, the LoRA fine-tuning protocol (rank~8, 3 epochs) applies\nsubstantial implicit regularization that may attenuate differences between\ncuration strategies: the low-rank bottleneck limits how much the model\ncan adapt to distributional differences in the training corpus, compressing\nthe effect of curation quality on downstream metrics.\nSecond, the corpus size (30{,}000 documents) is modest by pretraining\nstandards; depth-aware weighting may produce larger gains at scale, where\nthe volume of depth-1 content retained by graduated filtering represents\na proportionally larger share of useful training signal.\nThird, the evaluation benchmarks---MMLU and HellaSwag at 0-shot---measure\nbroad capabilities that may be less sensitive to fine-grained corpus\ncomposition than domain-specific or generation-intensive tasks.\nImportantly, the null result for graduated \\emph{superiority} does not\ndiminish the contribution of the $\\Kempirical = 2$ taxonomy itself, which\nstands as a characterization result independent of its downstream\napplication; the trichotomy identifies a real structural boundary in\nrecursive synthetic text regardless of whether current downstream\nevaluations resolve the marginal benefit of exploiting it.\nFuture work with full fine-tuning, larger corpora, and\ngeneration-intensive evaluation tasks (e.g., open-ended QA, summarization)\nmay better reveal the regime where graduated filtering's preservation of\ndepth-1 signal translates to measurable downstream gains.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "afdb1fd7-d2de-4c36-8659-39e29d610f68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MF8MTuWeAX2PxqmUBQfA14",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10942,
      "cache_read_input_tokens": 26873,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10942
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

_source line 59 · 2026-05-14T07:59:53.745Z_

<details><summary>↩ Tool result · `toolu_01GRgEbqR9RhcBaTjRBPaSve`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/c3_contingency_versions.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "b1a88f8b-579a-4950-ab00-15cc1085c5f5",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/c3_contingency_versions.tex",
    "content": "%% ======================================================================\n%% C3 Graduated Filtering — Contingency Text Versions\n%% Pre-written for exp-006 results (ETA 2026-05-15).\n%% Replace XX.X ± X.X placeholders with actual numbers once available.\n%% ======================================================================\n\n\n%% ======================================================================\n%% VERSION A — Graduated filtering significantly outperforms binary\n%% ======================================================================\n\n%% --- For conclusion.tex (replace the C3 TODO block, lines 48–53) ---\n\n% === Contribution 3: Graduated filtering (C3) ===\n% Source: exp-006\nThe $\\Kempirical = 2$ boundary implies a natural trichotomy---human\n(depth~0), first-generation synthetic (depth~1), and deeper synthetic\n(depth~$\\geq 2$)---that can be exploited for depth-aware data curation.\nGraduated filtering, which assigns sample weights $w = \\exp(-\\alpha\n\\cdot \\hat{d})$ based on the OBD-predicted expected depth $\\hat{d}$,\noutperforms both binary filtering strategies on downstream benchmarks:\nat the optimal $\\alpha^* = $ XX.X, LoRA-tuned Qwen2.5-1.5B-Instruct\nachieves XX.X $\\pm$ X.X on MMLU and XX.X $\\pm$ X.X on HellaSwag,\ncompared to XX.X $\\pm$ X.X / XX.X $\\pm$ X.X for binary-ours and\nXX.X $\\pm$ X.X / XX.X $\\pm$ X.X for binary-Drayson\n(Table~\\ref{tab:filtering_main}).\nThe gain is attributable to the retention of depth-1 content, which\npreserves substantial original signal while only gently down-weighting\nfirst-generation text; binary strategies discard this stratum entirely,\nsacrificing data volume without commensurate quality improvement.\nThis validates the practical utility of the three-tier taxonomy derived\nfrom $\\Kempirical = 2$: depth-aware curation that distinguishes shallow\nfrom deep synthetic content yields measurably better training corpora\nthan the binary human-versus-synthetic partition.\n\n%% --- For discussion.tex (new subsection or append to §Broader Impact) ---\n\n\\paragraph{Graduated versus binary filtering.}\nThe graduated filtering results (Section~\\ref{sec:graduated-filtering})\nprovide direct evidence that the $\\Kempirical = 2$ trichotomy has\nactionable value for data curation.\nThe optimal decay parameter $\\alpha^* = $ XX.X falls in the moderate\nrange, neither so low as to approximate no-filter ($\\alpha \\to 0$) nor\nso high as to degenerate to hard binary filtering ($\\alpha \\to \\infty$).\nThis intermediate optimum reflects the core insight: depth-1 text, while\ndetectably synthetic, retains enough of the original distribution's\ndiversity---as evidenced by elevated surprisal variance and vocabulary\nrichness relative to depth~$\\geq 2$ (Section~\\ref{sec:feature_degradation})---to\nbenefit downstream training when appropriately down-weighted rather than\ndiscarded.\nThe MMLU improvement of $+$XX.X\\,pp over binary-ours and\n$+$XX.X\\,pp over binary-Drayson, together with consistent gains on\nHellaSwag ($+$XX.X\\,pp and $+$XX.X\\,pp, respectively), demonstrate\nthat the signal preserved in the depth-1 stratum translates to\nmeasurable downstream quality across both knowledge-intensive and\ncommonsense reasoning tasks.\nGraduated filtering also exhibits lower cross-seed variance than binary\nstrategies (XX.X versus XX.X on MMLU), suggesting that the ordinal\nweighting scheme provides a more stable curation signal than hard\nclassification boundaries.\n\n\n%% ======================================================================\n%% VERSION B — Graduated filtering NOT significantly better than binary\n%% ======================================================================\n\n%% --- For conclusion.tex (replace the C3 TODO block, lines 48–53) ---\n\n% === Contribution 3: Graduated filtering (C3) ===\n% Source: exp-006\nThe $\\Kempirical = 2$ boundary implies a natural trichotomy---human\n(depth~0), first-generation synthetic (depth~1), and deeper synthetic\n(depth~$\\geq 2$)---that provides a principled framework for depth-aware\ndata curation.\nWe evaluate graduated filtering, which assigns sample weights\n$w = \\exp(-\\alpha \\cdot \\hat{d})$ based on predicted expected depth, against\nbinary filtering baselines (Table~\\ref{tab:filtering_main}).\nAt the best $\\alpha$, graduated filtering achieves XX.X $\\pm$ X.X on\nMMLU and XX.X $\\pm$ X.X on HellaSwag, comparable to binary-ours\n(XX.X $\\pm$ X.X / XX.X $\\pm$ X.X) and binary-Drayson\n(XX.X $\\pm$ X.X / XX.X $\\pm$ X.X); the differences are not\nstatistically significant across 5 seeds ($p >$ XX.XX).\nThe three-tier taxonomy nonetheless provides a principled alternative to\nbinary filtering: graduated weighting achieves comparable downstream\nperformance while retaining a larger effective corpus through soft\ndown-weighting rather than hard exclusion, and the continuous $\\alpha$\nparameter offers practitioners an explicit knob for trading off data\nvolume against depth penalty---a degree of freedom absent from binary\nschemes.\n\n%% --- For discussion.tex (new subsection or append to §Broader Impact) ---\n\n\\paragraph{Graduated versus binary filtering.}\nThe comparable performance of graduated and binary filtering\n(Section~\\ref{sec:graduated-filtering}) admits several explanations.\nFirst, the LoRA fine-tuning protocol (rank~8, 3 epochs) applies\nsubstantial implicit regularization that may attenuate differences between\ncuration strategies: the low-rank bottleneck limits how much the model\ncan adapt to distributional differences in the training corpus, compressing\nthe effect of curation quality on downstream metrics.\nSecond, the corpus size (30{,}000 documents) is modest by pretraining\nstandards; depth-aware weighting may produce larger gains at scale, where\nthe volume of depth-1 content retained by graduated filtering represents\na proportionally larger share of useful training signal.\nThird, the evaluation benchmarks---MMLU and HellaSwag at 0-shot---measure\nbroad capabilities that may be less sensitive to fine-grained corpus\ncomposition than domain-specific or generation-intensive tasks.\nImportantly, the null result for graduated \\emph{superiority} does not\ndiminish the contribution of the $\\Kempirical = 2$ taxonomy itself, which\nstands as a characterization result independent of its downstream\napplication; the trichotomy identifies a real structural boundary in\nrecursive synthetic text regardless of whether current downstream\nevaluations resolve the marginal benefit of exploiting it.\nFuture work with full fine-tuning, larger corpora, and\ngeneration-intensive evaluation tasks (e.g., open-ended QA, summarization)\nmay better reveal the regime where graduated filtering's preservation of\ndepth-1 signal translates to measurable downstream gains.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01LCp5qMLjfNyA2Sy5CHYyRa`</summary>

```json
{
  "name": "C3 Graduated Filtering Contingency Versions",
  "type": "paper",
  "description": "Two pre-written versions of C3 conclusion/discussion text for exp-006 results: Version A (graduated > binary, significant) and Version B (graduated ≈ binary, not significant). XX.X placeholders ready for number fill.",
  "project": "gen-depth-contamination",
  "exp_id": "exp-006",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/c3_contingency_versions.tex",
  "tags": [
    "paper",
    "c3",
    "contingency",
    "graduated-filtering"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "c14644e6-6c3e-42af-bdff-a67f0a4a8fb9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012odZgy4NFnAXRMTsVT3NuT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2107,
      "cache_read_input_tokens": 37815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2107
      },
      "output_tokens": 44,
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

_source line 61 · 2026-05-14T07:59:59.637Z_

<details><summary>↩ Tool result · `toolu_01LCp5qMLjfNyA2Sy5CHYyRa`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_32cfc1\", \"name\": \"C3 Graduated Filtering Contingency Versions\", \"type\": \"paper\", \"description\": \"Two pre-written versions of C3 conclusion/discussion text for exp-006 results: Version A (graduated > binary, significant) and Version B (graduated ≈ binary, not significant). XX.X placeholders ready for number fill.\", \"path\": \"projects/gen-depth-contamination/artifacts/exp-006/paper/c3_contingency_versions.tex\", \"url\": null, \"project\": \"gen-depth-contamination\", \"exp_id\": \"exp-006\", \"skill\": \"\", \"created_at\": \"2026-05-14T07:59:59.520362+00:00\", \"tags\": [\"paper\", \"c3\", \"contingency\", \"graduated-filtering\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "8f8bd983-90cf-46d3-b017-8c61b9d33456",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260514_32cfc1\\\", \\\"name\\\": \\\"C3 Graduated Filtering Contingency Versions\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Two pre-written versions of C3 conclusion/discussion text for exp-006 results: Version A (graduated > binary, significant) and Version B (graduated ≈ binary, not significant). XX.X placeholders ready for number fill.\\\", \\\"path\\\": \\\"projects/gen-depth-contamination/artifacts/exp-006/paper/c3_contingency_versions.tex\\\", \\\"url\\\": null, \\\"project\\\": \\\"gen-depth-contamination\\\", \\\"exp_id\\\": \\\"exp-006\\\", \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-14T07:59:59.520362+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"c3\\\", \\\"contingency\\\", \\\"graduated-filtering\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_32cfc1\", \"name\": \"C3 Graduated Filtering Contingency Versions\", \"type\": \"paper\", \"description\": \"Two pre-written versions of C3 conclusion/discussion text for exp-006 results: Version A (graduated > binary, significant) and Version B (graduated ≈ binary, not significant). XX.X placeholders ready for number fill.\", \"path\": \"projects/gen-depth-contamination/artifacts/exp-006/paper/c3_contingency_versions.tex\", \"url\": null, \"project\": \"gen-depth-contamination\", \"exp_id\": \"exp-006\", \"skill\": \"\", \"created_at\": \"2026-05-14T07:59:59.520362+00:00\", \"tags\": [\"paper\", \"c3\", \"contingency\", \"graduated-filtering\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 62_

已写入 `artifacts/c3_contingency_versions.tex` 并注册。结构：

- **Version A**（graduated 显著优于 binary）：conclusion 段强调 depth-1 保留机制和三级分类实用价值；discussion 段分析 optimal α 中间值的含义、跨 benchmark 一致性、cross-seed 方差优势。
- **Version B**（差异不显著）：conclusion 段重新定位为 "principled alternative with comparable performance"，强调连续 α 参数的灵活性；discussion 段给出三个解释（LoRA regularization、小数据集、benchmark 敏感度不足），明确 taxonomy 贡献独立于下游应用结果，指出 future work 方向。

两版均使用 `XX.X ± X.X` 占位符，exp-006 结果出来后直接填数字即可。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "uuid": "029ac676-6029-4fec-95ae-da633185df74",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016KYFrq68c2HWbwfETk2Wo3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 39922,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 708
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

_source line 63_

已写入 `artifacts/c3_contingency_versions.tex` 并注册。结构：

- **Version A**（graduated 显著优于 binary）：conclusion 段强调 depth-1 保留机制和三级分类实用价值；discussion 段分析 optimal α 中间值的含义、跨 benchmark 一致性、cross-seed 方差优势。
- **Version B**（差异不显著）：conclusion 段重新定位为 "principled alternative with comparable performance"，强调连续 α 参数的灵活性；discussion 段给出三个解释（LoRA regularization、小数据集、benchmark 敏感度不足），明确 taxonomy 贡献独立于下游应用结果，指出 future work 方向。

两版均使用 `XX.X ± X.X` 占位符，exp-006 结果出来后直接填数字即可。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 107730,
  "duration_api_ms": 108350,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "77a6dc16-e14b-41cc-9af2-e5a589b3ea94",
  "total_cost_usd": 0.4313951,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 28789,
    "cache_read_input_tokens": 165039,
    "output_tokens": 3330,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 28789,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 246,
        "cache_read_input_tokens": 39922,
        "cache_creation_input_tokens": 708,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 708
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1681,
      "outputTokens": 2698,
      "cacheReadInputTokens": 154496,
      "cacheCreationInputTokens": 44019,
      "webSearchRequests": 0,
      "costUSD": 0.08564435,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 3330,
      "cacheReadInputTokens": 165039,
      "cacheCreationInputTokens": 28789,
      "webSearchRequests": 0,
      "costUSD": 0.34575074999999994,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "bce6c96e-1810-4b81-bac1-b015870cd01a"
}
```

</details>

---
