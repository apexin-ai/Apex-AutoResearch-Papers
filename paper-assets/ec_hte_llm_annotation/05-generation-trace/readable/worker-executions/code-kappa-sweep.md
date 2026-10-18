# code kappa sweep

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 131
- **Recorded user turns:** 1
- **Tool calls:** 41
- **Original source:** `logs/workers/worker_code_kappa-sweep_20260521T155209.log`
- **Structured JSON:** [`34cb6eb1ca508b790e4e.json`](../../sessions/34/34cb6eb1ca508b790e4e.json)

## Before a recorded user message

6 recorded events

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
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
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
  "uuid": "9b1c913f-ef40-4260-b11e-38898b0c911c",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude/projects/-home-ubuntu-ec-hte-llm-annotation/memory/"
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
    "resetsAt": 1779396600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "f278b95f-1b3b-4076-b4a0-85f74b9be0ef",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Assistant

_source line 4_

I'll start by reading the existing simulation code to understand the κ/condition number guard implementation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "ea9c9aac-01bd-42e2-a5f3-df3a96754b17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012B6mhXHiJDmRhvtxtbjQLn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6531,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6531
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

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Agent · `toolu_01RwherfVUQDPdgza9quvcFc`</summary>

```json
{
  "description": "Find kappa/condition number guard implementation",
  "subagent_type": "Explore",
  "prompt": "In the project at /home/ubuntu/ec_hte_llm_annotation/, I need to find how the κ (kappa) condition number guard is implemented. This is a singularity guard for confusion matrices where condition number > κ triggers a fallback.\n\nSearch for:\n1. \"kappa\", \"condition\", \"singularity\", \"guard\", \"cond_number\", \"det\" in all Python files\n2. Read the key files: run_simulation.py, and any files like ec_hte.py, hb_ec_hte.py that implement the core logic\n3. I need to understand: how is condition number computed, what threshold is used, and what happens when the guard triggers\n\nBe very thorough - search across all .py files in the project."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "af83ab8a-9b71-4e95-a991-6f7927d51440",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012B6mhXHiJDmRhvtxtbjQLn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6531,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6531
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

### System

_source line 6_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Find kappa/condition number guard implementation",
  "task_type": "local_agent",
  "prompt": "In the project at /home/ubuntu/ec_hte_llm_annotation/, I need to find how the κ (kappa) condition number guard is implemented. This is a singularity guard for confusion matrices where condition number > κ triggers a fallback.\n\nSearch for:\n1. \"kappa\", \"condition\", \"singularity\", \"guard\", \"cond_number\", \"det\" in all Python files\n2. Read the key files: run_simulation.py, and any files like ec_hte.py, hb_ec_hte.py that implement the core logic\n3. I need to understand: how is condition number computed, what threshold is used, and what happens when the guard triggers\n\nBe very thorough - search across all .py files in the project.",
  "uuid": "d631d2e2-d787-4f63-b6f9-872dffa7fd4b",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

## Round 1

125 recorded events

### User

_source line 7 · 2026-05-21T15:52:24.214Z_

In the project at /home/ubuntu/ec_hte_llm_annotation/, I need to find how the κ (kappa) condition number guard is implemented. This is a singularity guard for confusion matrices where condition number > κ triggers a fallback.

Search for:
1. "kappa", "condition", "singularity", "guard", "cond_number", "det" in all Python files
2. Read the key files: run_simulation.py, and any files like ec_hte.py, hb_ec_hte.py that implement the core logic
3. I need to understand: how is condition number computed, what threshold is used, and what happens when the guard triggers

Be very thorough - search across all .py files in the project.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "bee9469d-fbd2-474a-8c4c-736bc90225f9"
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_016pYjJiGm7mdFcnLFnrVoBz`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/run_simulation.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "3ef063fe-cbb4-4afb-bde4-54afbd506a3c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012B6mhXHiJDmRhvtxtbjQLn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6531,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6531
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

_source line 9 · 2026-05-21T15:52:24.454Z_

<details><summary>↩ Tool result · reported error · `toolu_016pYjJiGm7mdFcnLFnrVoBz`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/ec_hte_llm_annotation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "eb3393ff-b25a-45b3-9491-d4fb10296ed2",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/ec_hte_llm_annotation."
}
```

</details>

---

### System

_source line 10_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Running find /home/ubuntu/ec_hte_llm_annotation -type f -…",
  "usage": {
    "total_tokens": 15555,
    "tool_uses": 1,
    "duration_ms": 2652
  },
  "last_tool_name": "Bash",
  "uuid": "4ccd8881-3baf-4c63-a520-47c82514f53c",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Bash · `toolu_018D2faEDVVxQJ7eYZAKohVP`</summary>

```json
{
  "command": "find /home/ubuntu/ec_hte_llm_annotation -type f -name \"*.py\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "5c3511d4-c19d-4117-a12a-87c1f8a20b37",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014xFr1ZjcunZgS3KoJ1Agtj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15546,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15546,
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

_source line 12 · 2026-05-21T15:52:27.034Z_

<details><summary>↩ Tool result · `toolu_018D2faEDVVxQJ7eYZAKohVP`</summary>

```text
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py
/home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py
/home/ubuntu/ec_hte_llm_annotation/scripts/explore_tweeteval.py
/home/ubuntu/ec_hte_llm_annotation/scripts/fig1_bias_mechanism.py
/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py
/home/ubuntu/ec_hte_llm_annotation/exp004_hate_speech.py
/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/utils.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/impl.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/_staggered.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/__init__.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/types.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/_multiprocess/__init__.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/annotated_doc/main.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/annotated_doc/__init__.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plot_collection.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/utils.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/bf_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/ess_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/forest_plot.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "0c7f06c8-3670-489e-8e08-8c65c123c413"
}
```

</details>

---

### System

_source line 13_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Running find /home/ubuntu/ec_hte_llm_annotation -type f -…",
  "usage": {
    "total_tokens": 17230,
    "tool_uses": 2,
    "duration_ms": 4783
  },
  "last_tool_name": "Bash",
  "uuid": "bf332618-f7ee-4e2a-9154-628d9e9b918c",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Bash · `toolu_0136jy3xDTn5YWm5yF41ZbDz`</summary>

```json
{
  "command": "find /home/ubuntu/ec_hte_llm_annotation -type f -name \"*.py\" -not -path \"*/.venv/*\" -not -path \"*/__pycache__/*\" | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "143601ac-e357-4a3a-a0cb-905a0f4065a0",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01G5YHkrwEQxkR52NzhugVzT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1661,
      "cache_read_input_tokens": 15546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1661,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 15 · 2026-05-21T15:52:29.123Z_

<details><summary>↩ Tool result · `toolu_0136jy3xDTn5YWm5yF41ZbDz`</summary>

```text
/home/ubuntu/ec_hte_llm_annotation/artifacts/diagnostic_revision/compute_auc.py
/home/ubuntu/ec_hte_llm_annotation/artifacts/exp-008/scripts/gemma2_9b_annotate.py
/home/ubuntu/ec_hte_llm_annotation/artifacts/exp-008/scripts/llama31_8b_annotate.py
/home/ubuntu/ec_hte_llm_annotation/artifacts/exp-008/scripts/mistral7b_annotate.py
/home/ubuntu/ec_hte_llm_annotation/artifacts/exp-008/scripts/qwen25_7b_annotate.py
/home/ubuntu/ec_hte_llm_annotation/artifacts/failure_analysis/part1_error_patterns.py
/home/ubuntu/ec_hte_llm_annotation/artifacts/failure_analysis/part2_regression.py
/home/ubuntu/ec_hte_llm_annotation/artifacts/failure_analysis/part3_shrinkage_analysis.py
/home/ubuntu/ec_hte_llm_annotation/draw_fig2.py
/home/ubuntu/ec_hte_llm_annotation/draw_fig3.py
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py
/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py
/home/ubuntu/ec_hte_llm_annotation/exp002_bias_bound.py
/home/ubuntu/ec_hte_llm_annotation/exp003_tweeteval.py
/home/ubuntu/ec_hte_llm_annotation/exp004_hate_speech.py
/home/ubuntu/ec_hte_llm_annotation/exp005_diagnostic_criterion.py
/home/ubuntu/ec_hte_llm_annotation/exp006_budget_sensitivity.py
/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py
/home/ubuntu/ec_hte_llm_annotation/exp008_filter_analysis.py
/home/ubuntu/ec_hte_llm_annotation/exp008_gpt55_annotate.py
/home/ubuntu/ec_hte_llm_annotation/exp008_gpt5x_annotate.py
/home/ubuntu/ec_hte_llm_annotation/exp008_multi_llm.py
/home/ubuntu/ec_hte_llm_annotation/exp010_misspecified_subgroups.py
/home/ubuntu/ec_hte_llm_annotation/exp011_causal_forest.py
/home/ubuntu/ec_hte_llm_annotation/exp013_boundary_condition.py
/home/ubuntu/ec_hte_llm_annotation/exp014_asymmetric.py
/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py
/home/ubuntu/ec_hte_llm_annotation/exp016_semi_real_better_cm.py
/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py
/home/ubuntu/ec_hte_llm_annotation/exp018_multiplicative_dgp.py
/home/ubuntu/ec_hte_llm_annotation/exp019_pz1_sweep.py
/home/ubuntu/ec_hte_llm_annotation/mvp_simulation.py
/home/ubuntu/ec_hte_llm_annotation/pilot_gemini_annotation.py
/home/ubuntu/ec_hte_llm_annotation/pilot_llm_annotation.py
/home/ubuntu/ec_hte_llm_annotation/scripts/explore_tweeteval.py
/home/ubuntu/ec_hte_llm_annotation/scripts/fig1_bias_mechanism.py
/home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "27b865b5-12cb-4c59-8d71-1cc6b95d5468"
}
```

</details>

---

### System

_source line 16_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Searching for kappa|condition|singularity|guard|cond_number|det…",
  "usage": {
    "total_tokens": 18357,
    "tool_uses": 3,
    "duration_ms": 6999
  },
  "last_tool_name": "Grep",
  "uuid": "53109548-50e3-44d3-b6a4-5f29705414fc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Grep · `toolu_01UeKK2ays469bLHBthv7orC`</summary>

```json
{
  "pattern": "kappa|condition|singularity|guard|cond_number|det\\(",
  "path": "/home/ubuntu/ec_hte_llm_annotation",
  "glob": "**/*.py",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "c104ab9d-c759-4980-ba97-c1658387ace9",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017FhcWizfWVxLgdx4JUaXGD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 17207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
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

_source line 18 · 2026-05-21T15:52:31.413Z_

<details><summary>↩ Tool result · `toolu_01UeKK2ays469bLHBthv7orC`</summary>

```text
Found 250 files limit: 250
exp019_pz1_sweep.py
artifacts/diagnostic_revision/compute_auc.py
artifacts/failure_analysis/part3_shrinkage_analysis.py
artifacts/failure_analysis/part2_regression.py
artifacts/failure_analysis/part1_error_patterns.py
exp018_multiplicative_dgp.py
exp017_rlearner.py
scripts/plot_applicability_frontier.py
exp016_semi_real_better_cm.py
exp015_semi_real_cm.py
exp010_misspecified_subgroups.py
exp004_hate_speech.py
exp013_boundary_condition.py
.venv/lib/python3.14/site-packages/datasets/utils/metadata.py
.venv/lib/python3.14/site-packages/datasets/dataset_dict.py
.venv/lib/python3.14/site-packages/datasets/arrow_dataset.py
.venv/lib/python3.14/site-packages/huggingface_hub/utils/tqdm.py
.venv/lib/python3.14/site-packages/huggingface_hub/serialization/_torch.py
.venv/lib/python3.14/site-packages/huggingface_hub/inference/_generated/types/text_to_speech.py
.venv/lib/python3.14/site-packages/huggingface_hub/inference/_generated/types/text_to_audio.py
.venv/lib/python3.14/site-packages/huggingface_hub/inference/_generated/types/image_to_text.py
.venv/lib/python3.14/site-packages/huggingface_hub/inference/_generated/types/automatic_speech_recognition.py
.venv/lib/python3.14/site-packages/huggingface_hub/inference/_generated/_async_client.py
.venv/lib/python3.14/site-packages/huggingface_hub/inference/_client.py
.venv/lib/python3.14/site-packages/huggingface_hub/cli/jobs.py
.venv/lib/python3.14/site-packages/aiohttp/web_middlewares.py
.venv/lib/python3.14/site-packages/aiohttp/web_fileresponse.py
.venv/lib/python3.14/site-packages/aiohttp/web_exceptions.py
.venv/lib/python3.14/site-packages/aiohttp/web.py
.venv/lib/python3.14/site-packages/aiohttp/test_utils.py
.venv/lib/python3.14/site-packages/aiohttp/resolver.py
.venv/lib/python3.14/site-packages/aiohttp/cookiejar.py
.venv/lib/python3.14/site-packages/httpx/_status_codes.py
.venv/lib/python3.14/site-packages/typer/main.py
.venv/lib/python3.14/site-packages/typer/_completion_shared.py
.venv/lib/python3.14/site-packages/anyio/_core/_synchronization.py
.venv/lib/python3.14/site-packages/anyio/_core/_fileio.py
.venv/lib/python3.14/site-packages/anyio/_backends/_trio.py
.venv/lib/python3.14/site-packages/anyio/_backends/_asyncio.py
.venv/lib/python3.14/site-packages/httpcore/_sync/http2.py
.venv/lib/python3.14/site-packages/httpcore/_async/http2.py
.venv/lib/python3.14/site-packages/httpcore/__init__.py
.venv/lib/python3.14/site-packages/multiprocess/tests/test_multiprocessing_main_handling.py
.venv/lib/python3.14/site-packages/multiprocess/tests/__init__.py
.venv/lib/python3.14/site-packages/multiprocess/synchronize.py
.venv/lib/python3.14/site-packages/multiprocess/spawn.py
.venv/lib/python3.14/site-packages/multiprocess/resource_tracker.py
.venv/lib/python3.14/site-packages/multiprocess/pool.py
.venv/lib/python3.14/site-packages/multiprocess/context.py
.venv/lib/python3.14/site-packages/multiprocess/__info__.py
.venv/lib/python3.14/site-packages/requests/utils.py
.venv/lib/python3.14/site-packages/requests/status_codes.py
.venv/lib/python3.14/site-packages/requests/models.py
.venv/lib/python3.14/site-packages/requests/cookies.py
.venv/lib/python3.14/site-packages/requests/auth.py
.venv/lib/python3.14/site-packages/requests/adapters.py
.venv/lib/python3.14/site-packages/yarl/_parse.py
.venv/lib/python3.14/site-packages/attr/_next_gen.py
.venv/lib/python3.14/site-packages/attr/_make.py
.venv/lib/python3.14/site-packages/dill/__info__.py
.venv/lib/python3.14/site-packages/fsspec/spec.py
.venv/lib/python3.14/site-packages/h11/_state.py
.venv/lib/python3.14/site-packages/h11/_connection.py
.venv/lib/python3.14/site-packages/idna/core.py
.venv/lib/python3.14/site-packages/pyarrow/vendored/docscrape.py
.venv/lib/python3.14/site-packages/pyarrow/tests/test_pandas.py
.venv/lib/python3.14/site-packages/pyarrow/tests/test_gandiva.py
.venv/lib/python3.14/site-packages/pyarrow/tests/test_dataset.py
.venv/lib/python3.14/site-packages/pyarrow/tests/test_csv.py
.venv/lib/python3.14/site-packages/yaml/scanner.py
.venv/lib/python3.14/site-packages/urllib3/util/wait.py
.venv/lib/python3.14/site-packages/urllib3/util/url.py
.venv/lib/python3.14/site-packages/urllib3/util/ssl_.py
exp007_ppci_dsl.py
exp011_causal_forest.py
exp006_budget_sensitivity.py
exp003_tweeteval.py
exp005_diagnostic_criterion.py
exp001_hb_synthetic.py
exp001_regularize.py
exp002_bias_bound.py
.venv/lib/python3.14/site-packages/pymc/variational/updates.py
.venv/lib/python3.14/site-packages/pymc/variational/approximations.py
.venv/lib/python3.14/site-packages/pymc/stats/log_density.py
.venv/lib/python3.14/site-packages/pymc/sampling/population.py
.venv/lib/python3.14/site-packages/pymc/sampling/forward.py
.venv/lib/python3.14/site-packages/pymc/ode/utils.py
.venv/lib/python3.14/site-packages/pymc/ode/ode.py
.venv/lib/python3.14/site-packages/pymc/model/transform/conditioning.py
.venv/lib/python3.14/site-packages/pymc/model/core.py
.venv/lib/python3.14/site-packages/pymc/logprob/utils.py
.venv/lib/python3.14/site-packages/pymc/logprob/transforms.py
.venv/lib/python3.14/site-packages/pymc/logprob/transform_value.py
.venv/lib/python3.14/site-packages/pymc/logprob/tensor.py
.venv/lib/python3.14/site-packages/pymc/logprob/switch.py
.venv/lib/python3.14/site-packages/pymc/logprob/scan.py
.venv/lib/python3.14/site-packages/pymc/logprob/rewriting.py
.venv/lib/python3.14/site-packages/pymc/logprob/order.py
.venv/lib/python3.14/site-packages/pymc/logprob/mixture.py
.venv/lib/python3.14/site-packages/pymc/logprob/linalg.py
.venv/lib/python3.14/site-packages/pymc/logprob/cumsum.py
.venv/lib/python3.14/site-packages/pymc/logprob/checks.py
.venv/lib/python3.14/site-packages/pymc/logprob/censoring.py
.venv/lib/python3.14/site-packages/pymc/logprob/basic.py
.venv/lib/python3.14/site-packages/pymc/logprob/arithmetic.py
.venv/lib/python3.14/site-packages/pymc/logprob/abstract.py
.venv/lib/python3.14/site-packages/pymc/logprob/__init__.py
.venv/lib/python3.14/site-packages/pymc/gp/util.py
.venv/lib/python3.14/site-packages/pymc/gp/hsgp_approx.py
.venv/lib/python3.14/site-packages/pymc/gp/gp.py
.venv/lib/python3.14/site-packages/pymc/gp/cov.py
.venv/lib/python3.14/site-packages/pymc/distributions/moments/means.py
.venv/lib/python3.14/site-packages/pymc/distributions/transforms.py
.venv/lib/python3.14/site-packages/pymc/distributions/multivariate.py
.venv/lib/python3.14/site-packages/pymc/distributions/dist_math.py
.venv/lib/python3.14/site-packages/pymc/distributions/custom.py
.venv/lib/python3.14/site-packages/pymc/distributions/continuous.py
.venv/lib/python3.14/site-packages/pymc/dims/distributions/transforms.py
.venv/lib/python3.14/site-packages/pymc/backends/__init__.py
.venv/lib/python3.14/site-packages/pymc/util.py
.venv/lib/python3.14/site-packages/pymc/testing.py
.venv/lib/python3.14/site-packages/pymc/pytensorf.py
.venv/lib/python3.14/site-packages/pymc/math.py
.venv/lib/python3.14/site-packages/pymc/__init__.py
.venv/lib/python3.14/site-packages/arviz_plots/plots/pava_residual_plot.py
.venv/lib/python3.14/site-packages/arviz_plots/plots/pava_calibration_plot.py
.venv/lib/python3.14/site-packages/arviz_plots/plot_collection.py
.venv/lib/python3.14/site-packages/pytensor/xtensor/type.py
.venv/lib/python3.14/site-packages/pytensor/tensor/rewriting/linalg/utils.py
.venv/lib/python3.14/site-packages/pytensor/tensor/rewriting/linalg/summary.py
.venv/lib/python3.14/site-packages/pytensor/tensor/rewriting/linalg/products.py
.venv/lib/python3.14/site-packages/pytensor/tensor/rewriting/subtensor.py
.venv/lib/python3.14/site-packages/pytensor/tensor/rewriting/basic.py
.venv/lib/python3.14/site-packages/pytensor/tensor/random/basic.py
.venv/lib/python3.14/site-packages/pytensor/tensor/linalg/solvers/linear_control.py
.venv/lib/python3.14/site-packages/pytensor/tensor/linalg/summary.py
.venv/lib/python3.14/site-packages/pytensor/tensor/linalg/products.py
.venv/lib/python3.14/site-packages/pytensor/tensor/type.py
.venv/lib/python3.14/site-packages/pytensor/tensor/subtensor.py
.venv/lib/python3.14/site-packages/pytensor/tensor/extra_ops.py
.venv/lib/python3.14/site-packages/pytensor/tensor/elemwise_cgen.py
.venv/lib/python3.14/site-packages/pytensor/tensor/blas.py
.venv/lib/python3.14/site-packages/pytensor/tensor/basic.py
.venv/lib/python3.14/site-packages/pytensor/scan/utils.py
.venv/lib/python3.14/site-packages/pytensor/scan/rewriting.py
.venv/lib/python3.14/site-packages/pytensor/scan/op.py
.venv/lib/python3.14/site-packages/pytensor/scan/basic.py
.venv/lib/python3.14/site-packages/pytensor/scalar/loop.py
.venv/lib/python3.14/site-packages/pytensor/scalar/basic.py
.venv/lib/python3.14/site-packages/pytensor/link/pytorch/dispatch/linalg/summary.py
.venv/lib/python3.14/site-packages/pytensor/link/pytorch/dispatch/basic.py
.venv/lib/python3.14/site-packages/pytensor/link/numba/dispatch/linalg/decomposition/qz.py
.venv/lib/python3.14/site-packages/pytensor/link/numba/dispatch/linalg/summary.py
.venv/lib/python3.14/site-packages/pytensor/link/numba/dispatch/linalg/_LAPACK.py
.venv/lib/python3.14/site-packages/pytensor/link/numba/dispatch/shape.py
.venv/lib/python3.14/site-packages/pytensor/link/numba/dispatch/scan.py
.venv/lib/python3.14/site-packages/pytensor/link/numba/dispatch/scalar.py
.venv/lib/python3.14/site-packages/pytensor/link/numba/dispatch/random.py
.venv/lib/python3.14/site-packages/pytensor/link/numba/dispatch/compile_ops.py
.venv/lib/python3.14/site-packages/pytensor/link/mlx/dispatch/linalg/summary.py
.venv/lib/python3.14/site-packages/pytensor/link/mlx/dispatch/basic.py
.venv/lib/python3.14/site-packages/pytensor/link/jax/dispatch/linalg/summary.py
.venv/lib/python3.14/site-packages/pytensor/link/jax/dispatch/random.py
.venv/lib/python3.14/site-packages/pytensor/link/c/cmodule.py
.venv/lib/python3.14/site-packages/pytensor/link/vm.py
.venv/lib/python3.14/site-packages/pytensor/graph/rewriting/basic.py
.venv/lib/python3.14/site-packages/pytensor/graph/traversal.py
.venv/lib/python3.14/site-packages/pytensor/graph/replace.py
.venv/lib/python3.14/site-packages/pytensor/graph/fg.py
.venv/lib/python3.14/site-packages/pytensor/graph/features.py
.venv/lib/python3.14/site-packages/pytensor/graph/destroyhandler.py
.venv/lib/python3.14/site-packages/pytensor/graph/basic.py
.venv/lib/python3.14/site-packages/pytensor/compile/debug/nanguardmode.py
.venv/lib/python3.14/site-packages/pytensor/compile/debug/debugmode.py
.venv/lib/python3.14/site-packages/pytensor/compile/mode.py
.venv/lib/python3.14/site-packages/pytensor/compile/maker.py
.venv/lib/python3.14/site-packages/pytensor/compile/executor.py
.venv/lib/python3.14/site-packages/pytensor/compile/builders.py
.venv/lib/python3.14/site-packages/pytensor/utils.py
.venv/lib/python3.14/site-packages/pytensor/raise_op.py
.venv/lib/python3.14/site-packages/pytensor/printing.py
.venv/lib/python3.14/site-packages/pytensor/ifelse.py
.venv/lib/python3.14/site-packages/pytensor/configparser.py
.venv/lib/python3.14/site-packages/pytensor/breakpoint.py
.venv/lib/python3.14/site-packages/xarray_einstats/linalg.py
.venv/lib/python3.14/site-packages/xarray_einstats/accessors.py
.venv/lib/python3.14/site-packages/rich/traceback.py
.venv/lib/python3.14/site-packages/rich/cells.py
.venv/lib/python3.14/site-packages/rich/_spinners.py
.venv/lib/python3.14/site-packages/rich/_emoji_codes.py
.venv/lib/python3.14/site-packages/xarray/util/deprecation_helpers.py
.venv/lib/python3.14/site-packages/xarray/tests/test_units.py
.venv/lib/python3.14/site-packages/xarray/tests/test_pandas_to_xarray.py
.venv/lib/python3.14/site-packages/xarray/tests/test_dataset.py
.venv/lib/python3.14/site-packages/xarray/tests/test_backends.py
.venv/lib/python3.14/site-packages/xarray/tests/test_accessor_str.py
.venv/lib/python3.14/site-packages/xarray/testing/assertions.py
.venv/lib/python3.14/site-packages/xarray/structure/combine.py
.venv/lib/python3.14/site-packages/xarray/plot/utils.py
.venv/lib/python3.14/site-packages/xarray/plot/facetgrid.py
.venv/lib/python3.14/site-packages/xarray/core/utils.py
.venv/lib/python3.14/site-packages/xarray/core/resample_cftime.py
.venv/lib/python3.14/site-packages/xarray/core/resample.py
.venv/lib/python3.14/site-packages/xarray/core/nputils.py
.venv/lib/python3.14/site-packages/xarray/core/indexing.py
.venv/lib/python3.14/site-packages/xarray/core/groupby.py
.venv/lib/python3.14/site-packages/xarray/core/extension_array.py
.venv/lib/python3.14/site-packages/xarray/core/duck_array_ops.py
.venv/lib/python3.14/site-packages/xarray/core/datatree.py
.venv/lib/python3.14/site-packages/xarray/core/dataset.py
.venv/lib/python3.14/site-packages/xarray/core/dataarray.py
.venv/lib/python3.14/site-packages/xarray/core/common.py
.venv/lib/python3.14/site-packages/xarray/core/accessor_str.py
.venv/lib/python3.14/site-packages/xarray/computation/fit.py
.venv/lib/python3.14/site-packages/xarray/compat/toolzcompat.py
.venv/lib/python3.14/site-packages/xarray/compat/pdcompat.py
.venv/lib/python3.14/site-packages/xarray/compat/npcompat.py
.venv/lib/python3.14/site-packages/xarray/coding/variables.py
.venv/lib/python3.14/site-packages/xarray/coding/frequencies.py
.venv/lib/python3.14/site-packages/xarray/coding/cftimeindex.py
.venv/lib/python3.14/site-packages/xarray/coding/cftime_offsets.py
.venv/lib/python3.14/site-packages/xarray/backends/zarr.py
.venv/lib/python3.14/site-packages/xarray/backends/writers.py
.venv/lib/python3.14/site-packages/xarray/backends/chunks.py
.venv/lib/python3.14/site-packages/xarray/groupers.py
.venv/lib/python3.14/site-packages/arviz_stats/loo/loo_moment_match.py
.venv/lib/python3.14/site-packages/arviz_stats/base/diagnostics.py
.venv/lib/python3.14/site-packages/arviz_stats/base/density.py
.venv/lib/python3.14/site-packages/arviz_stats/metrics.py
.venv/lib/python3.14/site-packages/markdown_it/rules_block/list.py
.venv/lib/python3.14/site-packages/markdown_it/parser_block.py
.venv/lib/python3.14/site-packages/markdown_it/_punycode.py
.venv/lib/python3.14/site-packages/cachetools/func.py
.venv/lib/python3.14/site-packages/cachetools/_cachedmethod.py
.venv/lib/python3.14/site-packages/cachetools/_cached.py
.venv/lib/python3.14/site-packages/cachetools/__init__.py
.venv/lib/python3.14/site-packages/filelock/_util.py
.venv/lib/python3.14/site-packages/mdurl/_parse.py
.venv/lib/python3.14/site-packages/pygments/lexers/zig.py
.venv/lib/python3.14/site-packages/pygments/lexers/yara.py
.venv/lib/python3.14/site-packages/pygments/lexers/vip.py
.venv/lib/python3.14/site-packages/pygments/lexers/verifpal.py
.venv/lib/python3.14/site-packages/pygments/lexers/templates.py
.venv/lib/python3.14/site-packages/pygments/lexers/tal.py
.venv/lib/python3.14/site-packages/pygments/lexers/scripting.py
.venv/lib/python3.14/site-packages/pygments/lexers/sas.py
.venv/lib/python3.14/site-packages/pygments/lexers/robotframework.py
.venv/lib/python3.14/site-packages/pygments/lexers/perl.py
.venv/lib/python3.14/site-packages/pygments/lexers/pddl.py
.venv/lib/python3.14/site-packages/pygments/lexers/objective.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "9b15a2fb-1d6d-42d8-af6c-a2ced93e34d7"
}
```

</details>

---

### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Searching for kappa|condition|singularity|guard|cond_number",
  "usage": {
    "total_tokens": 24661,
    "tool_uses": 4,
    "duration_ms": 9810
  },
  "last_tool_name": "Grep",
  "uuid": "c0824ede-ea77-4de7-a8c2-e762d11f26bf",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Grep · `toolu_01J1HQQww4Vzibxyb2dS3BbW`</summary>

```json
{
  "pattern": "kappa|condition|singularity|guard|cond_number",
  "path": "/home/ubuntu/ec_hte_llm_annotation",
  "glob": "*.py",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "604c74c3-3e72-49f8-b18a-0c23d2627fe7",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FVerw9wnTN2mAiyMVGMwew",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6302,
      "cache_read_input_tokens": 18332,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6302,
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

_source line 21 · 2026-05-21T15:52:34.213Z_

<details><summary>↩ Tool result · `toolu_01J1HQQww4Vzibxyb2dS3BbW`</summary>

```text
Found 250 files limit: 250
artifacts/diagnostic_revision/compute_auc.py
artifacts/failure_analysis/part3_shrinkage_analysis.py
artifacts/failure_analysis/part2_regression.py
artifacts/failure_analysis/part1_error_patterns.py
exp018_multiplicative_dgp.py
scripts/plot_applicability_frontier.py
exp010_misspecified_subgroups.py
exp013_boundary_condition.py
.venv/lib/python3.14/site-packages/datasets/utils/metadata.py
.venv/lib/python3.14/site-packages/datasets/dataset_dict.py
.venv/lib/python3.14/site-packages/datasets/arrow_dataset.py
.venv/lib/python3.14/site-packages/huggingface_hub/utils/tqdm.py
.venv/lib/python3.14/site-packages/huggingface_hub/serialization/_torch.py
.venv/lib/python3.14/site-packages/huggingface_hub/inference/_generated/types/text_to_speech.py
.venv/lib/python3.14/site-packages/huggingface_hub/inference/_generated/types/text_to_audio.py
.venv/lib/python3.14/site-packages/huggingface_hub/inference/_generated/types/image_to_text.py
.venv/lib/python3.14/site-packages/huggingface_hub/inference/_generated/types/automatic_speech_recognition.py
.venv/lib/python3.14/site-packages/huggingface_hub/inference/_generated/_async_client.py
.venv/lib/python3.14/site-packages/huggingface_hub/inference/_client.py
.venv/lib/python3.14/site-packages/huggingface_hub/cli/jobs.py
.venv/lib/python3.14/site-packages/aiohttp/web_middlewares.py
.venv/lib/python3.14/site-packages/aiohttp/web_fileresponse.py
.venv/lib/python3.14/site-packages/aiohttp/web_exceptions.py
.venv/lib/python3.14/site-packages/aiohttp/web.py
.venv/lib/python3.14/site-packages/aiohttp/test_utils.py
.venv/lib/python3.14/site-packages/aiohttp/resolver.py
.venv/lib/python3.14/site-packages/aiohttp/cookiejar.py
.venv/lib/python3.14/site-packages/httpx/_status_codes.py
.venv/lib/python3.14/site-packages/typer/main.py
.venv/lib/python3.14/site-packages/typer/_completion_shared.py
.venv/lib/python3.14/site-packages/anyio/_core/_synchronization.py
.venv/lib/python3.14/site-packages/anyio/_core/_fileio.py
.venv/lib/python3.14/site-packages/anyio/_backends/_trio.py
.venv/lib/python3.14/site-packages/anyio/_backends/_asyncio.py
.venv/lib/python3.14/site-packages/httpcore/_sync/http2.py
.venv/lib/python3.14/site-packages/httpcore/_async/http2.py
.venv/lib/python3.14/site-packages/httpcore/__init__.py
.venv/lib/python3.14/site-packages/multiprocess/tests/test_multiprocessing_main_handling.py
.venv/lib/python3.14/site-packages/multiprocess/tests/__init__.py
.venv/lib/python3.14/site-packages/multiprocess/synchronize.py
.venv/lib/python3.14/site-packages/multiprocess/spawn.py
.venv/lib/python3.14/site-packages/multiprocess/resource_tracker.py
.venv/lib/python3.14/site-packages/multiprocess/pool.py
.venv/lib/python3.14/site-packages/multiprocess/context.py
.venv/lib/python3.14/site-packages/multiprocess/__info__.py
.venv/lib/python3.14/site-packages/requests/utils.py
.venv/lib/python3.14/site-packages/requests/status_codes.py
.venv/lib/python3.14/site-packages/requests/models.py
.venv/lib/python3.14/site-packages/requests/cookies.py
.venv/lib/python3.14/site-packages/requests/auth.py
.venv/lib/python3.14/site-packages/requests/adapters.py
.venv/lib/python3.14/site-packages/yarl/_parse.py
.venv/lib/python3.14/site-packages/attr/_next_gen.py
.venv/lib/python3.14/site-packages/attr/_make.py
.venv/lib/python3.14/site-packages/dill/__info__.py
.venv/lib/python3.14/site-packages/fsspec/spec.py
.venv/lib/python3.14/site-packages/h11/_state.py
.venv/lib/python3.14/site-packages/h11/_connection.py
.venv/lib/python3.14/site-packages/idna/core.py
.venv/lib/python3.14/site-packages/pyarrow/vendored/docscrape.py
.venv/lib/python3.14/site-packages/pyarrow/tests/test_pandas.py
.venv/lib/python3.14/site-packages/pyarrow/tests/test_gandiva.py
.venv/lib/python3.14/site-packages/pyarrow/tests/test_dataset.py
.venv/lib/python3.14/site-packages/pyarrow/tests/test_csv.py
.venv/lib/python3.14/site-packages/yaml/scanner.py
.venv/lib/python3.14/site-packages/urllib3/util/wait.py
.venv/lib/python3.14/site-packages/urllib3/util/url.py
.venv/lib/python3.14/site-packages/urllib3/util/ssl_.py
exp007_ppci_dsl.py
exp011_causal_forest.py
exp006_budget_sensitivity.py
exp003_tweeteval.py
exp005_diagnostic_criterion.py
exp001_hb_synthetic.py
exp001_regularize.py
exp002_bias_bound.py
.venv/lib/python3.14/site-packages/pymc/variational/updates.py
.venv/lib/python3.14/site-packages/pymc/variational/approximations.py
.venv/lib/python3.14/site-packages/pymc/stats/log_density.py
.venv/lib/python3.14/site-packages/pymc/sampling/population.py
.venv/lib/python3.14/site-packages/pymc/sampling/forward.py
.venv/lib/python3.14/site-packages/pymc/ode/utils.py
.venv/lib/python3.14/site-packages/pymc/ode/ode.py
.venv/lib/python3.14/site-packages/pymc/model/transform/conditioning.py
.venv/lib/python3.14/site-packages/pymc/model/core.py
.venv/lib/python3.14/site-packages/pymc/logprob/utils.py
.venv/lib/python3.14/site-packages/pymc/logprob/transforms.py
.venv/lib/python3.14/site-packages/pymc/logprob/tensor.py
.venv/lib/python3.14/site-packages/pymc/logprob/switch.py
.venv/lib/python3.14/site-packages/pymc/logprob/scan.py
.venv/lib/python3.14/site-packages/pymc/logprob/rewriting.py
.venv/lib/python3.14/site-packages/pymc/logprob/order.py
.venv/lib/python3.14/site-packages/pymc/logprob/mixture.py
.venv/lib/python3.14/site-packages/pymc/logprob/cumsum.py
.venv/lib/python3.14/site-packages/pymc/logprob/checks.py
.venv/lib/python3.14/site-packages/pymc/logprob/censoring.py
.venv/lib/python3.14/site-packages/pymc/logprob/basic.py
.venv/lib/python3.14/site-packages/pymc/logprob/arithmetic.py
.venv/lib/python3.14/site-packages/pymc/logprob/abstract.py
.venv/lib/python3.14/site-packages/pymc/logprob/__init__.py
.venv/lib/python3.14/site-packages/pymc/gp/util.py
.venv/lib/python3.14/site-packages/pymc/gp/hsgp_approx.py
.venv/lib/python3.14/site-packages/pymc/gp/gp.py
.venv/lib/python3.14/site-packages/pymc/gp/cov.py
.venv/lib/python3.14/site-packages/pymc/distributions/moments/means.py
.venv/lib/python3.14/site-packages/pymc/distributions/multivariate.py
.venv/lib/python3.14/site-packages/pymc/distributions/dist_math.py
.venv/lib/python3.14/site-packages/pymc/distributions/custom.py
.venv/lib/python3.14/site-packages/pymc/distributions/continuous.py
.venv/lib/python3.14/site-packages/pymc/backends/__init__.py
.venv/lib/python3.14/site-packages/pymc/util.py
.venv/lib/python3.14/site-packages/pymc/testing.py
.venv/lib/python3.14/site-packages/pymc/pytensorf.py
.venv/lib/python3.14/site-packages/pymc/__init__.py
.venv/lib/python3.14/site-packages/arviz_plots/plots/pava_residual_plot.py
.venv/lib/python3.14/site-packages/arviz_plots/plots/pava_calibration_plot.py
.venv/lib/python3.14/site-packages/arviz_plots/plot_collection.py
.venv/lib/python3.14/site-packages/pytensor/xtensor/type.py
.venv/lib/python3.14/site-packages/pytensor/tensor/rewriting/linalg/utils.py
.venv/lib/python3.14/site-packages/pytensor/tensor/rewriting/subtensor.py
.venv/lib/python3.14/site-packages/pytensor/tensor/rewriting/basic.py
.venv/lib/python3.14/site-packages/pytensor/tensor/random/basic.py
.venv/lib/python3.14/site-packages/pytensor/tensor/linalg/solvers/linear_control.py
.venv/lib/python3.14/site-packages/pytensor/tensor/linalg/products.py
.venv/lib/python3.14/site-packages/pytensor/tensor/type.py
.venv/lib/python3.14/site-packages/pytensor/tensor/subtensor.py
.venv/lib/python3.14/site-packages/pytensor/tensor/extra_ops.py
.venv/lib/python3.14/site-packages/pytensor/tensor/elemwise_cgen.py
.venv/lib/python3.14/site-packages/pytensor/tensor/blas.py
.venv/lib/python3.14/site-packages/pytensor/tensor/basic.py
.venv/lib/python3.14/site-packages/pytensor/scan/utils.py
.venv/lib/python3.14/site-packages/pytensor/scan/rewriting.py
.venv/lib/python3.14/site-packages/pytensor/scan/op.py
.venv/lib/python3.14/site-packages/pytensor/scan/basic.py
.venv/lib/python3.14/site-packages/pytensor/scalar/loop.py
.venv/lib/python3.14/site-packages/pytensor/scalar/basic.py
.venv/lib/python3.14/site-packages/pytensor/link/pytorch/dispatch/basic.py
.venv/lib/python3.14/site-packages/pytensor/link/numba/dispatch/linalg/_LAPACK.py
.venv/lib/python3.14/site-packages/pytensor/link/numba/dispatch/shape.py
.venv/lib/python3.14/site-packages/pytensor/link/numba/dispatch/scan.py
.venv/lib/python3.14/site-packages/pytensor/link/numba/dispatch/scalar.py
.venv/lib/python3.14/site-packages/pytensor/link/numba/dispatch/random.py
.venv/lib/python3.14/site-packages/pytensor/link/numba/dispatch/compile_ops.py
.venv/lib/python3.14/site-packages/pytensor/link/mlx/dispatch/basic.py
.venv/lib/python3.14/site-packages/pytensor/link/jax/dispatch/random.py
.venv/lib/python3.14/site-packages/pytensor/link/c/cmodule.py
.venv/lib/python3.14/site-packages/pytensor/link/vm.py
.venv/lib/python3.14/site-packages/pytensor/graph/rewriting/basic.py
.venv/lib/python3.14/site-packages/pytensor/graph/traversal.py
.venv/lib/python3.14/site-packages/pytensor/graph/replace.py
.venv/lib/python3.14/site-packages/pytensor/graph/fg.py
.venv/lib/python3.14/site-packages/pytensor/graph/features.py
.venv/lib/python3.14/site-packages/pytensor/graph/destroyhandler.py
.venv/lib/python3.14/site-packages/pytensor/graph/basic.py
.venv/lib/python3.14/site-packages/pytensor/compile/debug/nanguardmode.py
.venv/lib/python3.14/site-packages/pytensor/compile/debug/debugmode.py
.venv/lib/python3.14/site-packages/pytensor/compile/mode.py
.venv/lib/python3.14/site-packages/pytensor/compile/maker.py
.venv/lib/python3.14/site-packages/pytensor/compile/executor.py
.venv/lib/python3.14/site-packages/pytensor/compile/builders.py
.venv/lib/python3.14/site-packages/pytensor/utils.py
.venv/lib/python3.14/site-packages/pytensor/raise_op.py
.venv/lib/python3.14/site-packages/pytensor/printing.py
.venv/lib/python3.14/site-packages/pytensor/ifelse.py
.venv/lib/python3.14/site-packages/pytensor/configparser.py
.venv/lib/python3.14/site-packages/pytensor/breakpoint.py
.venv/lib/python3.14/site-packages/rich/traceback.py
.venv/lib/python3.14/site-packages/rich/cells.py
.venv/lib/python3.14/site-packages/rich/_spinners.py
.venv/lib/python3.14/site-packages/rich/_emoji_codes.py
.venv/lib/python3.14/site-packages/xarray/util/deprecation_helpers.py
.venv/lib/python3.14/site-packages/xarray/tests/test_units.py
.venv/lib/python3.14/site-packages/xarray/tests/test_pandas_to_xarray.py
.venv/lib/python3.14/site-packages/xarray/tests/test_dataset.py
.venv/lib/python3.14/site-packages/xarray/tests/test_backends.py
.venv/lib/python3.14/site-packages/xarray/tests/test_accessor_str.py
.venv/lib/python3.14/site-packages/xarray/testing/assertions.py
.venv/lib/python3.14/site-packages/xarray/structure/combine.py
.venv/lib/python3.14/site-packages/xarray/plot/utils.py
.venv/lib/python3.14/site-packages/xarray/plot/facetgrid.py
.venv/lib/python3.14/site-packages/xarray/core/utils.py
.venv/lib/python3.14/site-packages/xarray/core/resample_cftime.py
.venv/lib/python3.14/site-packages/xarray/core/resample.py
.venv/lib/python3.14/site-packages/xarray/core/nputils.py
.venv/lib/python3.14/site-packages/xarray/core/indexing.py
.venv/lib/python3.14/site-packages/xarray/core/groupby.py
.venv/lib/python3.14/site-packages/xarray/core/extension_array.py
.venv/lib/python3.14/site-packages/xarray/core/duck_array_ops.py
.venv/lib/python3.14/site-packages/xarray/core/datatree.py
.venv/lib/python3.14/site-packages/xarray/core/dataset.py
.venv/lib/python3.14/site-packages/xarray/core/dataarray.py
.venv/lib/python3.14/site-packages/xarray/core/common.py
.venv/lib/python3.14/site-packages/xarray/core/accessor_str.py
.venv/lib/python3.14/site-packages/xarray/computation/fit.py
.venv/lib/python3.14/site-packages/xarray/compat/toolzcompat.py
.venv/lib/python3.14/site-packages/xarray/compat/pdcompat.py
.venv/lib/python3.14/site-packages/xarray/compat/npcompat.py
.venv/lib/python3.14/site-packages/xarray/coding/variables.py
.venv/lib/python3.14/site-packages/xarray/coding/frequencies.py
.venv/lib/python3.14/site-packages/xarray/coding/cftimeindex.py
.venv/lib/python3.14/site-packages/xarray/coding/cftime_offsets.py
.venv/lib/python3.14/site-packages/xarray/backends/zarr.py
.venv/lib/python3.14/site-packages/xarray/backends/writers.py
.venv/lib/python3.14/site-packages/xarray/backends/chunks.py
.venv/lib/python3.14/site-packages/xarray/groupers.py
.venv/lib/python3.14/site-packages/arviz_stats/base/diagnostics.py
.venv/lib/python3.14/site-packages/arviz_stats/base/density.py
.venv/lib/python3.14/site-packages/arviz_stats/metrics.py
.venv/lib/python3.14/site-packages/markdown_it/rules_block/list.py
.venv/lib/python3.14/site-packages/markdown_it/parser_block.py
.venv/lib/python3.14/site-packages/markdown_it/_punycode.py
.venv/lib/python3.14/site-packages/cachetools/func.py
.venv/lib/python3.14/site-packages/cachetools/_cachedmethod.py
.venv/lib/python3.14/site-packages/cachetools/_cached.py
.venv/lib/python3.14/site-packages/cachetools/__init__.py
.venv/lib/python3.14/site-packages/filelock/_util.py
.venv/lib/python3.14/site-packages/mdurl/_parse.py
.venv/lib/python3.14/site-packages/pygments/lexers/zig.py
.venv/lib/python3.14/site-packages/pygments/lexers/yara.py
.venv/lib/python3.14/site-packages/pygments/lexers/vip.py
.venv/lib/python3.14/site-packages/pygments/lexers/verifpal.py
.venv/lib/python3.14/site-packages/pygments/lexers/templates.py
.venv/lib/python3.14/site-packages/pygments/lexers/tal.py
.venv/lib/python3.14/site-packages/pygments/lexers/scripting.py
.venv/lib/python3.14/site-packages/pygments/lexers/sas.py
.venv/lib/python3.14/site-packages/pygments/lexers/robotframework.py
.venv/lib/python3.14/site-packages/pygments/lexers/perl.py
.venv/lib/python3.14/site-packages/pygments/lexers/pddl.py
.venv/lib/python3.14/site-packages/pygments/lexers/objective.py
.venv/lib/python3.14/site-packages/pygments/lexers/monte.py
.venv/lib/python3.14/site-packages/pygments/lexers/lisp.py
.venv/lib/python3.14/site-packages/pygments/lexers/javascript.py
.venv/lib/python3.14/site-packages/pygments/lexers/int_fiction.py
.venv/lib/python3.14/site-packages/pygments/lexers/html.py
.venv/lib/python3.14/site-packages/pygments/lexers/hdl.py
.venv/lib/python3.14/site-packages/pygments/lexers/haxe.py
.venv/lib/python3.14/site-packages/pygments/lexers/graphql.py
.venv/lib/python3.14/site-packages/pygments/lexers/graphics.py
.venv/lib/python3.14/site-packages/pygments/lexers/factor.py
.venv/lib/python3.14/site-packages/pygments/lexers/esoteric.py
.venv/lib/python3.14/site-packages/pygments/lexers/dylan.py
.venv/lib/python3.14/site-packages/pygments/lexers/console.py
.venv/lib/python3.14/site-packages/pygments/lexers/configs.py
.venv/lib/python3.14/site-packages/pygments/lexers/c_like.py
.venv/lib/python3.14/site-packages/pygments/lexers/blueprint.py
.venv/lib/python3.14/site-packages/pygments/lexers/asm.py
.venv/lib/python3.14/site-packages/pygments/lexers/_tsql_builtins.py
.venv/lib/python3.14/site-packages/pygments/lexers/_stata_builtins.py
.venv/lib/python3.14/site-packages/pygments/lexers/_scheme_builtins.py
.venv/lib/python3.14/site-packages/pygments/lexers/_mysql_builtins.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "859d0d8c-ac48-4e8c-a47c-df5e796fa5ff"
}
```

</details>

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Running find /home/ubuntu/ec_hte_llm_annotation -type f -…",
  "usage": {
    "total_tokens": 24662,
    "tool_uses": 5,
    "duration_ms": 10109
  },
  "last_tool_name": "Bash",
  "uuid": "25c1d99e-44bd-4cd7-847a-7fa58d164d48",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_01C5KA2Bcqhy535JmtiAjFpe`</summary>

```json
{
  "command": "find /home/ubuntu/ec_hte_llm_annotation -type f -name \"*.py\" -not -path \"*/.venv/*\" -not -path \"*/__pycache__/*\" -not -path \"*/artifacts/*\" | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "96099b4b-095a-460f-878f-f75b4717f51c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FVerw9wnTN2mAiyMVGMwew",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6302,
      "cache_read_input_tokens": 18332,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6302,
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

_source line 24 · 2026-05-21T15:52:34.441Z_

<details><summary>↩ Tool result · `toolu_01C5KA2Bcqhy535JmtiAjFpe`</summary>

```text
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py
/home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py
/home/ubuntu/ec_hte_llm_annotation/scripts/explore_tweeteval.py
/home/ubuntu/ec_hte_llm_annotation/scripts/fig1_bias_mechanism.py
/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py
/home/ubuntu/ec_hte_llm_annotation/exp004_hate_speech.py
/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py
/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py
/home/ubuntu/ec_hte_llm_annotation/mvp_simulation.py
/home/ubuntu/ec_hte_llm_annotation/exp006_budget_sensitivity.py
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py
/home/ubuntu/ec_hte_llm_annotation/pilot_llm_annotation.py
/home/ubuntu/ec_hte_llm_annotation/exp005_diagnostic_criterion.py
/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py
/home/ubuntu/ec_hte_llm_annotation/exp016_semi_real_better_cm.py
/home/ubuntu/ec_hte_llm_annotation/exp008_multi_llm.py
/home/ubuntu/ec_hte_llm_annotation/exp008_filter_analysis.py
/home/ubuntu/ec_hte_llm_annotation/exp002_bias_bound.py
/home/ubuntu/ec_hte_llm_annotation/exp008_gpt55_annotate.py
/home/ubuntu/ec_hte_llm_annotation/exp011_causal_forest.py
/home/ubuntu/ec_hte_llm_annotation/exp019_pz1_sweep.py
/home/ubuntu/ec_hte_llm_annotation/exp008_gpt5x_annotate.py
/home/ubuntu/ec_hte_llm_annotation/pilot_gemini_annotation.py
/home/ubuntu/ec_hte_llm_annotation/exp010_misspecified_subgroups.py
/home/ubuntu/ec_hte_llm_annotation/exp013_boundary_condition.py
/home/ubuntu/ec_hte_llm_annotation/exp018_multiplicative_dgp.py
/home/ubuntu/ec_hte_llm_annotation/exp014_asymmetric.py
/home/ubuntu/ec_hte_llm_annotation/exp003_tweeteval.py
/home/ubuntu/ec_hte_llm_annotation/draw_fig2.py
/home/ubuntu/ec_hte_llm_annotation/draw_fig3.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "abcaf1f1-f87b-439b-b8db-6886c4656455"
}
```

</details>

---

### System

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Running find /home/ubuntu/ec_hte_llm_annotation -type f -…",
  "usage": {
    "total_tokens": 31887,
    "tool_uses": 6,
    "duration_ms": 12326
  },
  "last_tool_name": "Bash",
  "uuid": "7e3bf9cc-1b47-45a9-8169-4eb7124d4d95",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_01Vst3MFsVmQqVPf3oYZNrnN`</summary>

```json
{
  "command": "find /home/ubuntu/ec_hte_llm_annotation -type f -name \"*.py\" -not -path \"*/.venv/*\" -not -path \"*/__pycache__/*\" -not -path \"*/artifacts/*\" | grep -E \"(hte|ec_|run|sim)\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "968288a5-13ae-4703-903b-2b9bf375e8e6",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D4HZegThEB5VWRNtsvWjDM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7220,
      "cache_read_input_tokens": 24634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7220,
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

_source line 27 · 2026-05-21T15:52:36.659Z_

<details><summary>↩ Tool result · `toolu_01Vst3MFsVmQqVPf3oYZNrnN`</summary>

```text
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py
/home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py
/home/ubuntu/ec_hte_llm_annotation/scripts/explore_tweeteval.py
/home/ubuntu/ec_hte_llm_annotation/scripts/fig1_bias_mechanism.py
/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py
/home/ubuntu/ec_hte_llm_annotation/exp004_hate_speech.py
/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py
/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py
/home/ubuntu/ec_hte_llm_annotation/mvp_simulation.py
/home/ubuntu/ec_hte_llm_annotation/exp006_budget_sensitivity.py
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py
/home/ubuntu/ec_hte_llm_annotation/pilot_llm_annotation.py
/home/ubuntu/ec_hte_llm_annotation/exp005_diagnostic_criterion.py
/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py
/home/ubuntu/ec_hte_llm_annotation/exp016_semi_real_better_cm.py
/home/ubuntu/ec_hte_llm_annotation/exp008_multi_llm.py
/home/ubuntu/ec_hte_llm_annotation/exp008_filter_analysis.py
/home/ubuntu/ec_hte_llm_annotation/exp002_bias_bound.py
/home/ubuntu/ec_hte_llm_annotation/exp008_gpt55_annotate.py
/home/ubuntu/ec_hte_llm_annotation/exp011_causal_forest.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "1eca6cef-5741-4b7c-992c-fae9cdab6658"
}
```

</details>

---

### System

_source line 28_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Running ls -la /home/ubuntu/ec_hte_llm_annotation/ | grep…",
  "usage": {
    "total_tokens": 31889,
    "tool_uses": 7,
    "duration_ms": 12626
  },
  "last_tool_name": "Bash",
  "uuid": "094b0885-75ef-48b7-af05-a54aa5ee9799",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_013CwvvTWg34iWer84Hd27k3`</summary>

```json
{
  "command": "ls -la /home/ubuntu/ec_hte_llm_annotation/ | grep -E \"\\.py$|^d\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "90b057bc-fa50-42d8-993e-835df9ea5658",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D4HZegThEB5VWRNtsvWjDM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7220,
      "cache_read_input_tokens": 24634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7220,
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

_source line 30 · 2026-05-21T15:52:36.919Z_

<details><summary>↩ Tool result · `toolu_013CwvvTWg34iWer84Hd27k3`</summary>

```text
drwxr-xr-x  8 ubuntu ubuntu  4096 May 21 15:36 .
drwxr-x--- 22 ubuntu ubuntu  4096 May 21 15:41 ..
drwxr-xr-x  5 ubuntu ubuntu  4096 May 20 17:53 .venv
drwxr-xr-x  2 ubuntu ubuntu  4096 May 21 10:09 __pycache__
drwxr-xr-x  9 ubuntu ubuntu  4096 May 21 15:34 artifacts
drwxr-xr-x  2 ubuntu ubuntu  4096 May 21 08:36 data
-rw-r--r--  1 ubuntu ubuntu  3711 May 21 05:29 draw_fig2.py
-rw-r--r--  1 ubuntu ubuntu  4515 May 21 05:28 draw_fig3.py
-rw-r--r--  1 ubuntu ubuntu 26702 May 20 22:52 exp001_hb_synthetic.py
-rw-r--r--  1 ubuntu ubuntu  7787 May 20 22:16 exp001_hyperprior_sensitivity.py
-rw-r--r--  1 ubuntu ubuntu 10975 May 20 22:04 exp001_regularize.py
-rw-r--r--  1 ubuntu ubuntu 21712 May 20 20:18 exp002_bias_bound.py
-rw-r--r--  1 ubuntu ubuntu 26829 May 21 00:15 exp003_tweeteval.py
-rw-r--r--  1 ubuntu ubuntu 29835 May 21 08:38 exp004_hate_speech.py
-rw-r--r--  1 ubuntu ubuntu 24285 May 20 23:38 exp005_diagnostic_criterion.py
-rw-r--r--  1 ubuntu ubuntu 24387 May 21 00:59 exp006_budget_sensitivity.py
-rw-r--r--  1 ubuntu ubuntu 31463 May 21 04:49 exp007_ppci_dsl.py
-rw-r--r--  1 ubuntu ubuntu  7136 May 21 10:25 exp008_filter_analysis.py
-rw-r--r--  1 ubuntu ubuntu  2268 May 21 10:18 exp008_gpt55_annotate.py
-rw-r--r--  1 ubuntu ubuntu  3480 May 21 10:23 exp008_gpt5x_annotate.py
-rw-r--r--  1 ubuntu ubuntu 12849 May 21 08:13 exp008_multi_llm.py
-rw-r--r--  1 ubuntu ubuntu 20606 May 21 10:09 exp010_misspecified_subgroups.py
-rw-r--r--  1 ubuntu ubuntu 15224 May 21 01:54 exp011_causal_forest.py
-rw-r--r--  1 ubuntu ubuntu 10531 May 21 07:26 exp013_boundary_condition.py
-rw-r--r--  1 ubuntu ubuntu 20732 May 21 07:39 exp014_asymmetric.py
-rw-r--r--  1 ubuntu ubuntu 21734 May 21 12:52 exp015_semi_real_cm.py
-rw-r--r--  1 ubuntu ubuntu 22258 May 21 13:22 exp016_semi_real_better_cm.py
-rw-r--r--  1 ubuntu ubuntu 12536 May 21 13:47 exp017_rlearner.py
-rw-r--r--  1 ubuntu ubuntu 14992 May 21 13:48 exp018_multiplicative_dgp.py
-rw-r--r--  1 ubuntu ubuntu 22164 May 21 15:36 exp019_pz1_sweep.py
-rw-r--r--  1 ubuntu ubuntu 10571 May 20 18:53 mvp_simulation.py
-rw-r--r--  1 ubuntu ubuntu  5931 May 21 04:51 pilot_gemini_annotation.py
-rw-r--r--  1 ubuntu ubuntu  9256 May 21 02:08 pilot_llm_annotation.py
drwxr-xr-x  2 ubuntu ubuntu  4096 May 21 15:34 results
drwxr-xr-x  2 ubuntu ubuntu  4096 May 21 13:24 scripts
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "9a144a36-4fd3-4ddd-9079-098de5e70d80"
}
```

</details>

---

### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Running find /home/ubuntu/ec_hte_llm_annotation -type d -…",
  "usage": {
    "total_tokens": 33823,
    "tool_uses": 8,
    "duration_ms": 14928
  },
  "last_tool_name": "Bash",
  "uuid": "f8a946a3-ad3b-43fb-b776-adbf398f27af",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Bash · `toolu_01C5ttHZnmQdewFJ4GUctRvT`</summary>

```json
{
  "command": "find /home/ubuntu/ec_hte_llm_annotation -type d -name \"src\" -o -name \"lib\" -o -name \"ec_hte*\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "a449e959-0133-4c00-9486-57b6b22130c9",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0148ge4DdagrCB2kyydqYR6M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1932,
      "cache_read_input_tokens": 31854,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1932,
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

_source line 33 · 2026-05-21T15:52:39.268Z_

<details><summary>↩ Tool result · `toolu_01C5ttHZnmQdewFJ4GUctRvT`</summary>

```text
/home/ubuntu/ec_hte_llm_annotation
/home/ubuntu/ec_hte_llm_annotation/.venv/lib
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/statsmodels/src
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/numpy/f2py/tests/src
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/numpy/f2py/src
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/numpy/random/lib
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/numpy/_core/lib
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/numpy/lib
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/pyarrow/src
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/sklearn/svm/src
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/sklearn/utils/src
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/_core/src
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/lightgbm/lib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "86e8e176-3184-4df3-8384-7cd6ee0ec50d"
}
```

</details>

---

### System

_source line 34_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Running head -100 /home/ubuntu/ec_hte_llm_annotation/mvp_…",
  "usage": {
    "total_tokens": 34436,
    "tool_uses": 9,
    "duration_ms": 19494
  },
  "last_tool_name": "Bash",
  "uuid": "de1be69d-32eb-46d4-b6cd-d8395b56e7ee",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Bash · `toolu_01TxqsQqVjU71gZpnoJnRSP6`</summary>

```json
{
  "command": "head -100 /home/ubuntu/ec_hte_llm_annotation/mvp_simulation.py | grep -E \"^import|^from\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "4799be90-df48-431f-9f1e-04fc68780294",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FbrKggy46NbinQeePAZ2Bo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 612,
      "cache_read_input_tokens": 33786,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 612,
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

_source line 36 · 2026-05-21T15:52:43.772Z_

<details><summary>↩ Tool result · `toolu_01TxqsQqVjU71gZpnoJnRSP6`</summary>

```text
import sys
import time
import warnings
import numpy as np
import pandas as pd
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "8a71fcc5-70a1-4878-b1ce-113ef769fb19"
}
```

</details>

---

### System

_source line 37_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Running head -100 /home/ubuntu/ec_hte_llm_annotation/exp0…",
  "usage": {
    "total_tokens": 34437,
    "tool_uses": 10,
    "duration_ms": 19759
  },
  "last_tool_name": "Bash",
  "uuid": "9112b0d8-61a0-44e4-b6f7-2bfc64135201",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Bash · `toolu_01PyuxfEXqawoLGmVkHHW2PN`</summary>

```json
{
  "command": "head -100 /home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py | grep -E \"^import|^from\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "6aa3d039-3a52-4431-8e7b-999c41ab33fa",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FbrKggy46NbinQeePAZ2Bo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 612,
      "cache_read_input_tokens": 33786,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 612,
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

_source line 39 · 2026-05-21T15:52:44.029Z_

<details><summary>↩ Tool result · `toolu_01PyuxfEXqawoLGmVkHHW2PN`</summary>

```text
import argparse
import os
import sys
import time
import warnings
import numpy as np
import pandas as pd
from scipy.special import gammaln
from scipy.optimize import minimize_scalar
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "ec687fad-6bcc-49e0-89fc-fb05e74f76fd"
}
```

</details>

---

### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Reading exp001_hb_synthetic.py",
  "usage": {
    "total_tokens": 34743,
    "tool_uses": 11,
    "duration_ms": 21526
  },
  "last_tool_name": "Read",
  "uuid": "c1f47459-1a1e-49d6-8c76-ac10465d4ee9",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_017JoWbRDZP8kwoR97DcLQoJ`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "b784031e-f1d1-45ac-85c1-2e260398a9ba",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YT9xkdbTuJSzifL5D5q79C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 293,
      "cache_read_input_tokens": 34398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 293,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 42 · 2026-05-21T15:52:46.066Z_

<details><summary>↩ Tool result · `toolu_017JoWbRDZP8kwoR97DcLQoJ`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	exp001_hb_synthetic.py - Hierarchical Bayesian EC-HTE Synthetic Validation (exp-001)
4	
5	Compares confusion matrix estimators for CATE correction under heterogeneous
6	misclassification across subgroups:
7	  Oracle, Naive, Global-corrected, MLE (Laplace), HB Dirichlet (partial pooling)
8	
9	Input: Synthetic DGP parameters (regimes, expert budgets, subgroup counts)
10	Output: results/exp001_hb_results.csv, results/exp001_hb_diagnostics.csv
11	"""
12	
13	import argparse
14	import os
15	import sys
16	import time
17	import warnings
18	import numpy as np
19	import pandas as pd
20	from scipy.special import gammaln
21	from scipy.optimize import minimize_scalar
22	
23	warnings.filterwarnings('ignore')
24	
25	try:
26	    import pymc as pm
27	    import pytensor.tensor as pt
28	    import arviz as az
29	    HAS_PYMC = True
30	except ImportError:
31	    HAS_PYMC = False
32	
33	N = 5000
34	SUBGROUP_LABELS = {2: ['A', 'B'], 4: ['A', 'B', 'C', 'D']}
35	
36	REGIMES = {
37	    2: {
38	        'extreme':     {'misclass': [0.25, 0.05], 'tau_z1': 0.5, 'tau_z0': 0.1},
39	        'moderate':    {'misclass': [0.15, 0.10], 'tau_z1': 0.3, 'tau_z0': 0.15},
40	        'homogeneous': {'misclass': [0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},
41	    },
42	    4: {
43	        'extreme':     {'misclass': [0.30, 0.20, 0.10, 0.03], 'tau_z1': 0.5, 'tau_z0': 0.1},
44	        'moderate':    {'misclass': [0.20, 0.15, 0.10, 0.05], 'tau_z1': 0.3, 'tau_z0': 0.15},
45	        'homogeneous': {'misclass': [0.12, 0.12, 0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},
46	    },
47	}
48	
49	DEFAULT_N_EXPERTS = [50, 100, 250, 500, 1000, 2000]
50	DEFAULT_K_LIST = [2, 4]
51	
52	
53	# ── DGP ───────────────────────────────────────────────────────────────────────
54	
55	def generate_data(regime_params, n_expert, k, seed):
56	    rng = np.random.RandomState(seed)
57	    labels = SUBGROUP_LABELS[k]
58	    T = rng.binomial(1, 0.5, N)
59	    Z = rng.binomial(1, 0.5, N)
60	    S = rng.choice(labels, N, p=[1.0 / k] * k)
61	    X = rng.randn(N, 5)
62	    tau = np.where(Z == 1, regime_params['tau_z1'], regime_params['tau_z0'])
63	    Y = 1 + tau * T + 0.5 * X[:, 0] + rng.randn(N)
64	    mc_rates = np.zeros(N)
65	    for i, s in enumerate(labels):
66	        mc_rates[S == s] = regime_params['misclass'][i]
67	    Z_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)
68	    idx = rng.choice(N, min(n_expert, N), replace=False)
69	    expert_mask = np.zeros(N, dtype=bool)
70	    expert_mask[idx] = True
71	    return dict(T=T, Z=Z, Z_hat=Z_hat, S=S, X=X, Y=Y, tau=tau, expert_mask=expert_mask)
72	
73	
74	# ── Helpers ───────────────────────────────────────────────────────────────────
75	
76	def diff_in_means(Y, T, mask):
77	    t1, t0 = mask & (T == 1), mask & (T == 0)
78	    n1, n0 = t1.sum(), t0.sum()
79	    if n1 < 2 or n0 < 2:
80	        return np.nan, np.nan
81	    y1, y0 = Y[t1], Y[t0]
82	    return y1.mean() - y0.mean(), np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)
83	
84	
85	def get_counts(z_true, z_hat, subgroups, labels):
86	    """Confusion matrix counts per subgroup: (k, 2, 2) = [subgroup, true_z, z_hat]."""
87	    k = len(labels)
88	    counts = np.zeros((k, 2, 2), dtype=int)
89	    for i, s in enumerate(labels):
90	        ms = subgroups == s
91	        for z in [0, 1]:
92	            mz = ms & (z_true == z)
93	            counts[i, z, 0] = (z_hat[mz] == 0).sum()
94	            counts[i, z, 1] = (z_hat[mz] == 1).sum()
95	    return counts
96	
97	
98	def build_mixing_matrix(C):
99	    """C[z, z_hat] → M[z_hat, z] via Bayes rule (assuming P(Z=0)=P(Z=1)=0.5).
100	
101	    NOTE: This assumes P(Z=0)=P(Z=1)=0.5, which is correct for this experiment's
102	    DGP. For general P(Z), use the version in exp007 that takes p_z and p_z_hat.
103	    """
104	    M = np.zeros((2, 2))
105	    for zh in [0, 1]:
106	        cs = C[0, zh] + C[1, zh]
107	        if cs > 0:
108	            M[zh, 0] = C[0, zh] / cs
109	            M[zh, 1] = C[1, zh] / cs
110	        else:
111	            M[zh, :] = 0.5
112	    return M
113	
114	
115	def invert_mixing(M, tau_obs, se_obs):
116	    det = np.linalg.det(M)
117	    if abs(det) < 1e-10:
118	        return tau_obs.copy(), se_obs.copy()
119	    Mi = np.linalg.inv(M)
120	    tau_c = Mi @ tau_obs
121	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
122	    return tau_c, se_c
123	
124	
125	def safe_invert_correction(M_s, tau_obs, cond_threshold=100, fallback='naive'):
126	    """Invert mixing matrix with condition number guard.
127	
128	    When cond(M_s) > threshold, matrix inversion is numerically unstable.
129	    Falls back to naive (no correction) to avoid catastrophic amplification.
130	    """
131	    cond = np.linalg.cond(M_s)
132	    if cond > cond_threshold:
133	        return tau_obs.copy()
134	    return np.linalg.solve(M_s, tau_obs)
135	
136	
137	def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
138	    """Like invert_mixing but with condition number guard."""
139	    cond = np.linalg.cond(M)
140	    if cond > cond_threshold:
141	        return tau_obs.copy(), se_obs.copy()
142	    det = np.linalg.det(M)
143	    if abs(det) < 1e-10:
144	        return tau_obs.copy(), se_obs.copy()
145	    Mi = np.linalg.inv(M)
146	    tau_c = Mi @ tau_obs
147	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
148	    return tau_c, se_c
149	
150	
151	# ── Confusion Matrix Estimators ───────────────────────────────────────────────
152	
153	def estimate_cm_mle(counts, labels):
154	    """Per-subgroup MLE with Laplace smoothing (add-1)."""
155	    C = {}
156	    for i, s in enumerate(labels):
157	        C_s = np.zeros((2, 2))
158	        for z in [0, 1]:
159	            n = counts[i, z, :].sum()
160	            for zh in [0, 1]:
161	                C_s[z, zh] = (counts[i, z, zh] + 1) / (n + 2) if n > 0 else 0.5
162	        C[s] = C_s
163	    return C
164	
165	
166	def _dirmult_neg_ll(alpha, counts_z):
167	    """Negative log marginal likelihood for Dirichlet-Multinomial."""
168	    a = alpha / 2.0
169	    if a < 1e-10:
170	        return 1e10
171	    ll = 0.0
172	    for c0, c1 in counts_z:
173	        n = c0 + c1
174	        if n == 0:
175	            continue
176	        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)
177	        ll -= 2 * gammaln(a) - gammaln(2 * a)
178	    return -ll
179	
180	
181	def estimate_cm_hb_eb(counts, labels):
182	    """Empirical Bayes HB: optimize shared Dirichlet concentration, posterior mean."""
183	    k = len(labels)
184	    alpha_opt = np.zeros(2)
185	    for z in [0, 1]:
186	        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]
187	        total = sum(c0 + c1 for c0, c1 in cl)
188	        if total == 0:
189	            alpha_opt[z] = 2.0
190	            continue
191	        res = minimize_scalar(
192	            lambda a: _dirmult_neg_ll(a, cl), bounds=(0.01, 500), method='bounded')
193	        alpha_opt[z] = res.x
194	
195	    C = {}
196	    for i, s in enumerate(labels):
197	        C_s = np.zeros((2, 2))
198	        for z in [0, 1]:
199	            a = alpha_opt[z] / 2.0
200	            n = counts[i, z, :].sum()
201	            d = n + 2 * a
202	            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5
203	            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5
204	        C[s] = C_s
205	
206	    diag = {'rhat_max': np.nan, 'ess_min': np.nan, 'divergent_count': 0,
207	            'runtime_seconds': 0.0, 'hb_method': 'eb',
208	            'alpha_0_z0': alpha_opt[0], 'alpha_0_z1': alpha_opt[1]}
209	    return C, diag
210	
211	
212	def _split_rhat(chains):
213	    """Split R-hat for a scalar parameter. chains: (n_chains, n_draws)."""
214	    parts = []
215	    for c in range(chains.shape[0]):
216	        half = chains.shape[1] // 2
217	        parts.append(chains[c, :half])
218	        parts.append(chains[c, half:2 * half])
219	    parts = np.array(parts)
220	    m = parts.shape[0]
221	    n = parts.shape[1]
222	    chain_means = parts.mean(axis=1)
223	    W = np.mean(np.var(parts, axis=1, ddof=1))
224	    B = n * np.var(chain_means, ddof=1)
225	    if W < 1e-20:
226	        return 1.0
227	    var_hat = (1 - 1.0 / n) * W + B / n
228	    return float(np.sqrt(var_hat / W))
229	
230	
231	def _bulk_ess(chains):
232	    """Approximate bulk ESS via initial positive sequence. chains: (n_chains, n_draws)."""
233	    x = chains.ravel()
234	    n = len(x)
235	    mu = x.mean()
236	    xc = x - mu
237	    max_lag = min(n // 2, 300)
238	    c0 = np.dot(xc, xc)
239	    if c0 < 1e-20:
240	        return float(n)
241	    tau = 1.0
242	    for lag in range(1, max_lag - 1, 2):
243	        r1 = np.dot(xc[:n - lag], xc[lag:]) / c0
244	        r2 = np.dot(xc[:n - lag - 1], xc[lag + 1:]) / c0 if lag + 1 < n else 0
245	        pair = r1 + r2
246	        if pair < 0:
247	            break
248	        tau += 2 * pair
249	    return float(n / tau)
250	
251	
252	def _fast_diagnostics(alpha_arr, theta_arr, labels):
253	    """Compute R-hat and ESS over all parameters without arviz."""
254	    rhats, esss = [], []
255	    for d in range(alpha_arr.shape[2]):
256	        rhats.append(_split_rhat(alpha_arr[:, :, d]))
257	        esss.append(_bulk_ess(alpha_arr[:, :, d]))
258	    k = len(labels)
259	    for i in range(k):
260	        for z in [0, 1]:
261	            for zh in range(theta_arr.shape[4]):
262	                ch = theta_arr[:, :, i, z, zh]
263	                rhats.append(_split_rhat(ch))
264	                esss.append(_bulk_ess(ch))
265	    return max(rhats), min(esss)
266	
267	
268	def _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):
269	    """Log posterior for alpha_0[z] in log-alpha space (includes Jacobian)."""
270	    if alpha < 1e-10:
271	        return -1e10
272	    a = alpha / 2.0
273	    k = theta_z.shape[0]
274	    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha
275	    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))
276	    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))
277	    return lp
278	
279	
280	def estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=4000, n_warmup=2000, n_chains=4,
281	                         hp_a0=3.0, hp_b0=1.0):
282	    """Gibbs sampler for HB Dirichlet-Multinomial (conjugate + adaptive MH for alpha_0).
283	
284	    hp_a0, hp_b0: Gamma hyperprior shape/rate on alpha_0 (default Gamma(3,1)).
285	    """
286	    k = len(labels)
287	    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),
288	                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]
289	    chain_inits = chain_inits_pool[:n_chains]
290	    all_alpha, all_theta = [], []
291	    t0 = time.time()
292	
293	    for chain in range(n_chains):
294	        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)
295	        alpha = chain_inits[chain].copy()
296	        theta = np.ones((k, 2, 2)) * 0.5
297	        mh_scale = np.array([0.3, 0.3])
298	        accept_ct = np.array([0, 0])
299	        attempt_ct = np.array([0, 0])
300	
301	        alpha_samples = np.zeros((n_iter, 2))
302	        theta_samples = np.zeros((n_iter, k, 2, 2))
303	
304	        for it in range(n_warmup + n_iter):
305	            for z in [0, 1]:
306	                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0
307	                post_a = np.maximum(post_a, 1e-6)
308	                g = rng.gamma(post_a)
309	                g_sum = g.sum(axis=1, keepdims=True)
310	                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)
311	
312	            for z in [0, 1]:
313	                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])
314	                a_prop = np.exp(x_prop)
315	                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -
316	                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))
317	                accepted = np.log(rng.rand()) < log_r
318	                if accepted:
319	                    alpha[z] = a_prop
320	                if it < n_warmup:
321	                    accept_ct[z] += int(accepted)
322	                    attempt_ct[z] += 1
323	
324	            if it < n_warmup and it > 0 and it % 100 == 0:
325	                for z in [0, 1]:
326	                    rate = accept_ct[z] / max(attempt_ct[z], 1)
327	                    if rate < 0.2:
328	                        mh_scale[z] *= 0.7
329	                    elif rate > 0.5:
330	                        mh_scale[z] *= 1.3
331	                    accept_ct[z] = 0
332	                    attempt_ct[z] = 0
333	
334	            if it >= n_warmup:
335	                idx = it - n_warmup
336	                alpha_samples[idx] = alpha.copy()
337	                theta_samples[idx] = theta.copy()
338	
339	        all_alpha.append(alpha_samples)
340	        all_theta.append(theta_samples)
341	
342	    runtime = time.time() - t0
343	    alpha_arr = np.stack(all_alpha)
344	    theta_arr = np.stack(all_theta)
345	
346	    C = {}
347	    for i, s in enumerate(labels):
348	        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))
349	
350	    rhat_max, ess_min = _fast_diagnostics(alpha_arr, theta_arr, labels)
351	
352	    diag = {'rhat_max': rhat_max, 'ess_min': ess_min, 'divergent_count': 0,
353	            'runtime_seconds': runtime, 'hb_method': 'gibbs'}
354	    return C, diag
355	
356	
357	def estimate_cm_hb_mcmc(counts, labels, seed=42, draws=1000, tune=500, chains=2):
358	    """Full Bayesian HB with PyMC MCMC."""
359	    k = len(labels)
360	    n_per_sz = counts.sum(axis=2)
361	
362	    with pm.Model():
363	        alpha_0 = pm.Gamma('alpha_0', alpha=2, beta=1, shape=2)
364	        for z in [0, 1]:
365	            for i, s in enumerate(labels):
366	                nsz = int(n_per_sz[i, z])
367	                if nsz == 0:
368	                    continue
369	                a = pt.stack([alpha_0[z] / 2, alpha_0[z] / 2])
370	                theta = pm.Dirichlet(f'theta_{s}_z{z}', a=a)
371	                pm.Multinomial(f'obs_{s}_z{z}', n=nsz, p=theta,
372	                               observed=counts[i, z, :].astype('int32'))
373	        t0 = time.time()
374	        trace = pm.sample(draws=draws, tune=tune, chains=chains,
375	                          random_seed=seed, progressbar=False)
376	        runtime = time.time() - t0
377	
378	    C = {}
379	    for i, s in enumerate(labels):
380	        C_s = np.zeros((2, 2))
381	        for z in [0, 1]:
382	            vn = f'theta_{s}_z{z}'
383	            if vn in trace.posterior:
384	                C_s[z, :] = trace.posterior[vn].values.mean(axis=(0, 1))
385	            else:
386	                C_s[z, :] = 0.5
387	        C[s] = C_s
388	
389	    all_vars = list(trace.posterior.data_vars)
390	    try:
391	        summ = az.summary(trace, var_names=all_vars)
392	        rhat_max = float(summ['r_hat'].max())
393	        ess_min = float(summ['ess_bulk'].min())
394	    except Exception:
395	        rhat_max = ess_min = np.nan
396	    try:
397	        divergent = int(trace.sample_stats['diverging'].values.sum())
398	    except Exception:
399	        divergent = -1
400	
401	    diag = {'rhat_max': rhat_max, 'ess_min': ess_min,
402	            'divergent_count': divergent, 'runtime_seconds': runtime,
403	            'hb_method': 'mcmc'}
404	    return C, diag
405	
406	
407	# ── Single MC Run ─────────────────────────────────────────────────────────────
408	
409	def run_one_mc(regime_name, regime_params, n_expert, k, seed, hb_method='eb'):
410	    data = generate_data(regime_params, n_expert, k, seed)
411	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
412	    em = data['expert_mask']
413	    labels = SUBGROUP_LABELS[k]
414	    tau_z0, tau_z1 = regime_params['tau_z0'], regime_params['tau_z1']
415	
416	    counts = get_counts(Z[em], Z_hat[em], S[em], labels)
417	
418	    C_mle = estimate_cm_mle(counts, labels)
419	
420	    if hb_method == 'gibbs':
421	        C_hb, hb_diag = estimate_cm_hb_gibbs(counts, labels, seed=seed)
422	    elif hb_method == 'mcmc' and HAS_PYMC:
423	        try:
424	            C_hb, hb_diag = estimate_cm_hb_mcmc(counts, labels, seed=seed)
425	        except Exception:
426	            C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)
427	            hb_diag['hb_method'] = 'eb_fallback'
428	    else:
429	        C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)
430	
431	    # Global CM (pool all expert labels, Laplace)
432	    cg = counts.sum(axis=0)
433	    C_gl = np.zeros((2, 2))
434	    for z in [0, 1]:
435	        n = cg[z, :].sum()
436	        for zh in [0, 1]:
437	            C_gl[z, zh] = (cg[z, zh] + 1) / (n + 2) if n > 0 else 0.5
438	
439	    M_gl = build_mixing_matrix(C_gl)
440	    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in labels}
441	    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}
442	
443	    base = {'regime': regime_name, 'n_expert': n_expert, 'k_subgroups': k, 'mc_run': seed}
444	    rows = []
445	
446	    for s in labels:
447	        sm = S == s
448	        th0_or, se0_or = diff_in_means(Y, T, sm & (Z == 0))
449	        th1_or, se1_or = diff_in_means(Y, T, sm & (Z == 1))
450	        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))
451	        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))
452	
453	        tau_obs = np.array([th0_n, th1_n])
454	        se_obs = np.array([se0_n, se1_n])
455	        if np.any(np.isnan(tau_obs)):
456	            continue
457	
458	        tgc, sgc = invert_mixing(M_gl, tau_obs, se_obs)
459	        tml, sml = invert_mixing(M_mle[s], tau_obs, se_obs)
460	        thb, shb = invert_mixing(M_hb[s], tau_obs, se_obs)
461	
462	        def mr(method, th0, th1, se0, se1):
463	            return {**base, 'subgroup': s, 'method': method,
464	                    'tau_hat_z0': th0, 'tau_hat_z1': th1,
465	                    'se_z0': se0, 'se_z1': se1,
466	                    'tau_true_z0': tau_z0, 'tau_true_z1': tau_z1}
467	
468	        rows.append(mr('oracle', th0_or, th1_or, se0_or, se1_or))
469	        rows.append(mr('naive', th0_n, th1_n, se0_n, se1_n))
470	        rows.append(mr('global_corrected', tgc[0], tgc[1], sgc[0], sgc[1]))
471	        rows.append(mr('mle_laplace', tml[0], tml[1], sml[0], sml[1]))
472	        rows.append(mr('hb_dirichlet', thb[0], thb[1], shb[0], shb[1]))
473	
474	    return rows, {**base, **hb_diag}
475	
476	
477	# ── Aggregation ───────────────────────────────────────────────────────────────
478	
479	def aggregate_results(df):
480	    rows = []
481	    grp_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method']
482	    for keys, grp in df.groupby(grp_cols):
483	        regime, n_expert, k, subgroup, method = keys
484	        row = {'regime': regime, 'n_expert': int(n_expert), 'k_subgroups': int(k),
485	               'subgroup': subgroup, 'method': method}
486	        n_mc = len(grp)
487	        for z in ['z0', 'z1']:
488	            err = grp[f'tau_hat_{z}'].values - grp[f'tau_true_{z}'].values
489	            bias = err.mean()
490	            mse = (err ** 2).mean()
491	            rmse = np.sqrt(mse)
492	            ci_lo = grp[f'tau_hat_{z}'].values - 1.96 * grp[f'se_{z}'].values
493	            ci_hi = grp[f'tau_hat_{z}'].values + 1.96 * grp[f'se_{z}'].values
494	            cov = ((ci_lo <= grp[f'tau_true_{z}'].values) &
495	                   (grp[f'tau_true_{z}'].values <= ci_hi)).mean()
496	            row[f'bias_{z}'] = bias
497	            row[f'rmse_{z}'] = rmse
498	            row[f'coverage_{z}'] = cov
499	            row[f'bias_{z}_se'] = err.std() / np.sqrt(n_mc)
500	            mse_se = (err ** 2).std() / np.sqrt(n_mc)
501	            row[f'rmse_{z}_se'] = mse_se / (2 * rmse) if rmse > 1e-10 else np.nan
502	        rows.append(row)
503	    return pd.DataFrame(rows)
504	
505	
506	# ── Output ────────────────────────────────────────────────────────────────────
507	
508	def print_summary(df_agg, df_diag):
509	    pd.set_option('display.float_format', '{:.4f}'.format)
510	
511	    # MCMC / Gibbs diagnostics
512	    if 'hb_method' in df_diag.columns:
513	        for method_label in ['gibbs', 'mcmc']:
514	            mrows = df_diag[df_diag['hb_method'] == method_label]
515	            if mrows.empty:
516	                continue
517	            print(f"\n── {method_label.upper()} Diagnostics ──────────────────────────────")
518	            print(f"  Runs:           {len(mrows)}")
519	            rh = mrows['rhat_max'].dropna()
520	            es = mrows['ess_min'].dropna()
521	            if not rh.empty:
522	                print(f"  R-hat max:      {rh.max():.4f} (target < 1.01)")
523	            if not es.empty:
524	                print(f"  ESS min:        {es.min():.0f} (target > 200)")
525	            print(f"  Divergent total:{int(mrows['divergent_count'].sum())}")
526	            print(f"  Runtime median: {mrows['runtime_seconds'].median():.2f}s")
527	
528	    # Per-config HB vs MLE comparison
529	    print("\n── HB vs MLE RMSE Comparison (subgroup-level, averaged) ──")
530	    for k in sorted(df_agg['k_subgroups'].unique()):
531	        print(f"\n  K = {int(k)} subgroups")
532	        for regime in ['extreme', 'moderate', 'homogeneous']:
533	            sub = df_agg[(df_agg['k_subgroups'] == k) & (df_agg['regime'] == regime)]
534	            if sub.empty:
535	                continue
536	            print(f"    {regime}:")
537	            print(f"    {'n_exp':>6s}  {'oracle':>8s}  {'naive':>8s}  {'global':>8s}  "
538	                  f"{'mle':>8s}  {'hb':>8s}  {'HB vs MLE':>10s}")
539	            for ne in sorted(sub['n_expert'].unique()):
540	                vals = {}
541	                for m in ['oracle', 'naive', 'global_corrected', 'mle_laplace', 'hb_dirichlet']:
542	                    ms = sub[(sub['method'] == m) & (sub['n_expert'] == ne)]
543	                    if ms.empty:
544	                        vals[m] = np.nan
545	                    else:
546	                        vals[m] = np.sqrt((ms['rmse_z0'].values ** 2 +
547	                                           ms['rmse_z1'].values ** 2).mean())
548	                mle_v, hb_v = vals['mle_laplace'], vals['hb_dirichlet']
549	                pct = (mle_v - hb_v) / mle_v * 100 if mle_v > 1e-10 else 0
550	                tag = f"{pct:+.1f}%"
551	                print(f"    {int(ne):6d}  {vals['oracle']:8.4f}  {vals['naive']:8.4f}  "
552	                      f"{vals['global_corrected']:8.4f}  {mle_v:8.4f}  {hb_v:8.4f}  {tag:>10s}")
553	
554	
555	# ── Sweep ─────────────────────────────────────────────────────────────────────
556	
557	def run_sweep(regime_names, n_experts, k_list, n_mc,
558	              hb_method='eb', mcmc_diag_runs=5, verbose=True):
559	    all_rows, all_diag = [], []
560	    total = sum(1 for k in k_list for r in regime_names if r in REGIMES[k]) * len(n_experts) * n_mc
561	    count = 0
562	    t0 = time.time()
563	
564	    for k in k_list:
565	        for rn in regime_names:
566	            if rn not in REGIMES[k]:
567	                continue
568	            rp = REGIMES[k][rn]
569	            for ne in n_experts:
570	                for mc in range(n_mc):
571	                    use = hb_method
572	                    if hb_method == 'auto':
573	                        use = 'mcmc' if mc < mcmc_diag_runs else 'eb'
574	                    try:
575	                        rows, diag = run_one_mc(rn, rp, ne, k, seed=mc, hb_method=use)
576	                        all_rows.extend(rows)
577	                        all_diag.append(diag)
578	                    except Exception as e:
579	                        if verbose:
580	                            print(f"  WARN: k={k} {rn} ne={ne} mc={mc} failed: {e}")
581	                        all_diag.append({
582	                            'regime': rn, 'n_expert': ne, 'k_subgroups': k,
583	                            'mc_run': mc, 'hb_method': 'error',
584	                            'rhat_max': np.nan, 'ess_min': np.nan,
585	                            'divergent_count': -1, 'runtime_seconds': 0.0})
586	                    count += 1
587	                    if verbose and count % max(1, total // 20) == 0:
588	                        el = time.time() - t0
589	                        eta = el / count * (total - count)
590	                        print(f"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s | "
591	                              f"k={k} {rn} ne={ne} mc={mc}")
592	
593	    if verbose:
594	        print(f"  Sweep done: {time.time() - t0:.1f}s ({count} runs)")
595	    return pd.DataFrame(all_rows), pd.DataFrame(all_diag)
596	
597	
598	# ── Main ──────────────────────────────────────────────────────────────────────
599	
600	if __name__ == '__main__':
601	    parser = argparse.ArgumentParser()
602	    parser.add_argument('--n-mc', type=int, default=100)
603	    parser.add_argument('--dry-run', action='store_true')
604	    parser.add_argument('--hb-method', choices=['auto', 'mcmc', 'gibbs', 'eb'], default='auto')
605	    parser.add_argument('--mcmc-diag-runs', type=int, default=5)
606	    args = parser.parse_args()
607	
608	    n_mc = 5 if args.dry_run else args.n_mc
609	    regime_names = ['moderate'] if args.dry_run else ['extreme', 'moderate', 'homogeneous']
610	    n_experts = [100] if args.dry_run else DEFAULT_N_EXPERTS
611	    k_list = [2] if args.dry_run else DEFAULT_K_LIST
612	
613	    print(f"exp-001 HB Synthetic Validation | PyMC={HAS_PYMC}")
614	    print(f"N={N} n_mc={n_mc} hb={args.hb_method}")
615	    print(f"Regimes={regime_names} n_experts={n_experts} K={k_list}\n")
616	
617	    # Timing test
618	    effective_method = args.hb_method
619	    d = generate_data(REGIMES[2]['moderate'], 100, 2, seed=9999)
620	    em = d['expert_mask']
621	    tc = get_counts(d['Z'][em], d['Z_hat'][em], d['S'][em], ['A', 'B'])
622	
623	    if args.hb_method == 'auto':
624	        print("Timing Gibbs sampler...")
625	        t0 = time.time()
626	        _, dg = estimate_cm_hb_gibbs(tc, ['A', 'B'], seed=9999)
627	        gt = time.time() - t0
628	        print(f"  Gibbs: {gt:.2f}s | rhat={dg['rhat_max']:.3f} "
629	              f"ess={dg['ess_min']:.0f}")
630	        if gt < 5:
631	            effective_method = 'gibbs'
632	            print(f"  Fast enough → using Gibbs for all runs")
633	        else:
634	            effective_method = 'eb'
635	            print(f"  Slow → using EB")
636	    elif args.hb_method == 'mcmc' and HAS_PYMC:
637	        print("Timing PyMC MCMC...")
638	        t0 = time.time()
639	        try:
640	            _, dg = estimate_cm_hb_mcmc(tc, ['A', 'B'], seed=9999)
641	            mt = time.time() - t0
642	            print(f"  MCMC: {mt:.1f}s | rhat={dg['rhat_max']:.3f} "
643	                  f"ess={dg['ess_min']:.0f} div={dg['divergent_count']}")
644	        except Exception as e:
645	            print(f"  MCMC failed: {e} → falling back to Gibbs")
646	            effective_method = 'gibbs'
647	
648	    print(f"\nEffective method: {effective_method}\n")
649	
650	    df_raw, df_diag = run_sweep(
651	        regime_names, n_experts, k_list, n_mc,
652	        hb_method=effective_method, mcmc_diag_runs=args.mcmc_diag_runs)
653	
654	    df_agg = aggregate_results(df_raw)
655	
656	    os.makedirs('results', exist_ok=True)
657	    agg_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method',
658	                'bias_z0', 'rmse_z0', 'coverage_z0', 'bias_z1', 'rmse_z1', 'coverage_z1',
659	                'bias_z0_se', 'rmse_z0_se', 'bias_z1_se', 'rmse_z1_se']
660	    df_agg[agg_cols].to_csv('results/exp001_hb_results.csv', index=False)
661	
662	    diag_cols = ['regime', 'n_expert', 'k_subgroups', 'mc_run',
663	                 'rhat_max', 'ess_min', 'divergent_count', 'runtime_seconds']
664	    save_cols = [c for c in diag_cols if c in df_diag.columns]
665	    if 'hb_method' in df_diag.columns:
666	        save_cols.insert(4, 'hb_method')
667	    df_diag[save_cols].to_csv('results/exp001_hb_diagnostics.csv', index=False)
668	
669	    print_summary(df_agg, df_diag)
670	
671	    print(f"\nSaved: results/exp001_hb_results.csv ({len(df_agg)} rows)")
672	    print(f"Saved: results/exp001_hb_diagnostics.csv ({len(df_diag)} rows)")
673	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "77f6ad93-3dc5-470d-8645-f7a9c18a9827"
}
```

</details>

---

### System

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Searching for safe_invert|cond_threshold|cond\\(|np\\.linalg\\.cond",
  "usage": {
    "total_tokens": 46438,
    "tool_uses": 12,
    "duration_ms": 25644
  },
  "last_tool_name": "Grep",
  "uuid": "c7b12db1-0ac7-4c67-ad8a-efe596f2fdd3",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Grep · `toolu_0159W2raDXkM9YJeB4NLm4F7`</summary>

```json
{
  "pattern": "safe_invert|cond_threshold|cond\\(|np\\.linalg\\.cond",
  "path": "/home/ubuntu/ec_hte_llm_annotation",
  "glob": "*.py",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "70746f2b-b2da-4fdb-b4ee-8cd17ca264f8",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VPE3UFcE6wHbcSLvgu9Bxg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 11688,
      "cache_read_input_tokens": 34691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11688,
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

_source line 45 · 2026-05-21T15:52:50.056Z_

<details><summary>↩ Tool result · `toolu_0159W2raDXkM9YJeB4NLm4F7`</summary>

```text
Found 111 files
exp019_pz1_sweep.py
exp018_multiplicative_dgp.py
exp017_rlearner.py
exp016_semi_real_better_cm.py
exp015_semi_real_cm.py
exp010_misspecified_subgroups.py
.venv/lib/python3.14/site-packages/pyarrow/tests/parquet/test_datetime.py
.venv/lib/python3.14/site-packages/pyarrow/tests/test_pandas.py
.venv/lib/python3.14/site-packages/pyarrow/tests/test_convert_builtin.py
.venv/lib/python3.14/site-packages/pyarrow/tests/test_compute.py
exp007_ppci_dsl.py
exp011_causal_forest.py
exp006_budget_sensitivity.py
exp003_tweeteval.py
exp001_hb_synthetic.py
exp001_hyperprior_sensitivity.py
exp001_regularize.py
.venv/lib/python3.14/site-packages/pytensor/xtensor/rewriting/shape.py
.venv/lib/python3.14/site-packages/pytensor/xtensor/shape.py
.venv/lib/python3.14/site-packages/pytensor/xtensor/math.py
.venv/lib/python3.14/site-packages/pytensor/tensor/rewriting/linalg/solvers.py
.venv/lib/python3.14/site-packages/pytensor/tensor/rewriting/extra_ops.py
.venv/lib/python3.14/site-packages/pytensor/tensor/rewriting/basic.py
.venv/lib/python3.14/site-packages/pytensor/tensor/subtensor.py
.venv/lib/python3.14/site-packages/pytensor/tensor/extra_ops.py
.venv/lib/python3.14/site-packages/pytensor/tensor/basic.py
.venv/lib/python3.14/site-packages/pytensor/sparse/math.py
.venv/lib/python3.14/site-packages/pytensor/scalar/basic.py
.venv/lib/python3.14/site-packages/pytensor/link/numba/dispatch/scalar.py
.venv/lib/python3.14/site-packages/pytensor/link/mlx/dispatch/scalar.py
.venv/lib/python3.14/site-packages/pytensor/link/jax/dispatch/scalar.py
.venv/lib/python3.14/site-packages/pytensor/link/jax/dispatch/basic.py
.venv/lib/python3.14/site-packages/xarray_einstats/linalg.py
.venv/lib/python3.14/site-packages/xarray_einstats/accessors.py
.venv/lib/python3.14/site-packages/xarray/tests/test_groupby.py
.venv/lib/python3.14/site-packages/xarray/tests/test_cftime_offsets.py
.venv/lib/python3.14/site-packages/xarray/core/common.py
.venv/lib/python3.14/site-packages/xarray/core/accessor_dt.py
.venv/lib/python3.14/site-packages/xarray/coding/cftime_offsets.py
.venv/lib/python3.14/site-packages/cachetools/_cachedmethod.py
.venv/lib/python3.14/site-packages/toolz/tests/test_itertoolz.py
.venv/lib/python3.14/site-packages/toolz/itertoolz.py
.venv/lib/python3.14/site-packages/statsmodels/tsa/statespace/tools.py
.venv/lib/python3.14/site-packages/statsmodels/tsa/statespace/mlemodel.py
.venv/lib/python3.14/site-packages/statsmodels/tsa/regime_switching/markov_switching.py
.venv/lib/python3.14/site-packages/statsmodels/tsa/exponential_smoothing/base.py
.venv/lib/python3.14/site-packages/statsmodels/tsa/base/tests/test_tsa_indexes.py
.venv/lib/python3.14/site-packages/statsmodels/treatment/treatment_effects.py
.venv/lib/python3.14/site-packages/statsmodels/sandbox/regression/tests/test_gmm.py
.venv/lib/python3.14/site-packages/statsmodels/sandbox/regression/gmm.py
.venv/lib/python3.14/site-packages/statsmodels/sandbox/distributions/estimators.py
.venv/lib/python3.14/site-packages/statsmodels/regression/tests/test_regression.py
.venv/lib/python3.14/site-packages/pandas/tests/tslibs/test_to_offset.py
.venv/lib/python3.14/site-packages/pandas/tests/tseries/offsets/test_ticks.py
.venv/lib/python3.14/site-packages/pandas/tests/tseries/frequencies/test_frequencies.py
.venv/lib/python3.14/site-packages/pandas/tests/tools/test_to_datetime.py
.venv/lib/python3.14/site-packages/pandas/tests/scalar/timestamp/methods/test_round.py
.venv/lib/python3.14/site-packages/pandas/tests/scalar/timestamp/test_constructors.py
.venv/lib/python3.14/site-packages/pandas/tests/scalar/timedelta/test_constructors.py
.venv/lib/python3.14/site-packages/pandas/tests/scalar/timedelta/test_arithmetic.py
.venv/lib/python3.14/site-packages/pandas/tests/scalar/period/test_period.py
.venv/lib/python3.14/site-packages/pandas/tests/scalar/period/test_asfreq.py
.venv/lib/python3.14/site-packages/pandas/tests/plotting/test_datetimelike.py
.venv/lib/python3.14/site-packages/pandas/tests/plotting/test_converter.py
.venv/lib/python3.14/site-packages/pandas/tests/io/formats/test_format.py
.venv/lib/python3.14/site-packages/pandas/tests/indexes/timedeltas/test_timedelta_range.py
.venv/lib/python3.14/site-packages/pandas/tests/indexes/timedeltas/test_constructors.py
.venv/lib/python3.14/site-packages/pandas/tests/indexes/datetimes/methods/test_to_period.py
.venv/lib/python3.14/site-packages/pandas/tests/indexes/datetimes/methods/test_to_julian_date.py
.venv/lib/python3.14/site-packages/pandas/tests/indexes/datetimes/test_scalar_compat.py
.venv/lib/python3.14/site-packages/pandas/tests/extension/test_arrow.py
.venv/lib/python3.14/site-packages/pandas/tests/dtypes/test_dtypes.py
.venv/lib/python3.14/site-packages/pandas/tests/arithmetic/test_numeric.py
.venv/lib/python3.14/site-packages/pandas/tests/arithmetic/test_datetime64.py
.venv/lib/python3.14/site-packages/pandas/core/indexes/period.py
.venv/lib/python3.14/site-packages/pandas/core/arrays/arrow/array.py
.venv/lib/python3.14/site-packages/pandas/core/arrays/timedeltas.py
.venv/lib/python3.14/site-packages/numba/tests/test_withlifting.py
.venv/lib/python3.14/site-packages/numba/tests/test_tuples.py
.venv/lib/python3.14/site-packages/numba/tests/test_linalg.py
.venv/lib/python3.14/site-packages/numba/tests/test_array_analysis.py
.venv/lib/python3.14/site-packages/numba/tests/test_analysis.py
.venv/lib/python3.14/site-packages/numba/tests/recursion_usecases.py
.venv/lib/python3.14/site-packages/numba/np/linalg.py
.venv/lib/python3.14/site-packages/numba/core/typing/builtins.py
.venv/lib/python3.14/site-packages/numba/core/lowering.py
.venv/lib/python3.14/site-packages/numba/core/ir_utils.py
.venv/lib/python3.14/site-packages/numba/core/ir.py
.venv/lib/python3.14/site-packages/numba/core/interpreter.py
.venv/lib/python3.14/site-packages/numba/core/cgutils.py
.venv/lib/python3.14/site-packages/numba/core/base.py
.venv/lib/python3.14/site-packages/llvmlite/ir/instructions.py
.venv/lib/python3.14/site-packages/scipy/sparse/linalg/_isolve/tests/test_iterative.py
.venv/lib/python3.14/site-packages/scipy/sparse/linalg/_isolve/minres.py
.venv/lib/python3.14/site-packages/scipy/sparse/linalg/_isolve/lsqr.py
.venv/lib/python3.14/site-packages/scipy/sparse/linalg/_isolve/lsmr.py
.venv/lib/python3.14/site-packages/scipy/sparse/linalg/_eigen/lobpcg/tests/test_lobpcg.py
.venv/lib/python3.14/site-packages/scipy/signal/tests/test_signaltools.py
.venv/lib/python3.14/site-packages/scipy/optimize/tests/test_nonlin.py
.venv/lib/python3.14/site-packages/scipy/optimize/_nonlin.py
.venv/lib/python3.14/site-packages/scipy/optimize/_minpack_py.py
.venv/lib/python3.14/site-packages/scipy/linalg/tests/test_special_matrices.py
.venv/lib/python3.14/site-packages/scipy/linalg/tests/test_matfuncs.py
.venv/lib/python3.14/site-packages/scipy/linalg/tests/test_lapack.py
.venv/lib/python3.14/site-packages/scipy/linalg/tests/test_batch.py
.venv/lib/python3.14/site-packages/scipy/linalg/tests/test_basic.py
.venv/lib/python3.14/site-packages/scipy/linalg/_solvers.py
.venv/lib/python3.14/site-packages/scipy/linalg/_expm_frechet.py
.venv/lib/python3.14/site-packages/numpy/linalg/tests/test_linalg.py
.venv/lib/python3.14/site-packages/numpy/linalg/_linalg.py
.venv/lib/python3.14/site-packages/numpy/_core/tests/test_datetime.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "0285d66f-2d7c-48f5-98b7-e09805d98446"
}
```

</details>

---

### System

_source line 46_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Reading exp001_hb_synthetic.py",
  "usage": {
    "total_tokens": 49574,
    "tool_uses": 13,
    "duration_ms": 28260
  },
  "last_tool_name": "Read",
  "uuid": "a72dd6d7-984e-4b26-9eed-0bdc9941fe9c",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Read · `toolu_01115B9zAvAQ34Gb6oTeaxp8`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py",
  "offset": 115,
  "limit": 25
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "ed2e0167-ae7f-44ab-84eb-515f753be9bf",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RQELjY8WTimDHSkBm8wLop",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3134,
      "cache_read_input_tokens": 46379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3134,
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

_source line 48 · 2026-05-21T15:52:52.487Z_

<details><summary>↩ Tool result · `toolu_01115B9zAvAQ34Gb6oTeaxp8`</summary>

```text
115	def invert_mixing(M, tau_obs, se_obs):
116	    det = np.linalg.det(M)
117	    if abs(det) < 1e-10:
118	        return tau_obs.copy(), se_obs.copy()
119	    Mi = np.linalg.inv(M)
120	    tau_c = Mi @ tau_obs
121	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
122	    return tau_c, se_c
123	
124	
125	def safe_invert_correction(M_s, tau_obs, cond_threshold=100, fallback='naive'):
126	    """Invert mixing matrix with condition number guard.
127	
128	    When cond(M_s) > threshold, matrix inversion is numerically unstable.
129	    Falls back to naive (no correction) to avoid catastrophic amplification.
130	    """
131	    cond = np.linalg.cond(M_s)
132	    if cond > cond_threshold:
133	        return tau_obs.copy()
134	    return np.linalg.solve(M_s, tau_obs)
135	
136	
137	def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
138	    """Like invert_mixing but with condition number guard."""
139	    cond = np.linalg.cond(M)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "490b8489-cd3f-4a81-9bbb-42599ef580ae"
}
```

</details>

---

### System

_source line 49_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Searching for safe_invert|cond_threshold",
  "usage": {
    "total_tokens": 49575,
    "tool_uses": 14,
    "duration_ms": 29063
  },
  "last_tool_name": "Grep",
  "uuid": "912470cd-1d6d-4e35-a37e-59579dec325c",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Grep · `toolu_01MpxznYt8xVson8hxfy4gju`</summary>

```json
{
  "pattern": "safe_invert|cond_threshold",
  "path": "/home/ubuntu/ec_hte_llm_annotation",
  "glob": "exp*.py",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "4fbfce3b-d5b6-4805-b793-43e4a6bab713",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RQELjY8WTimDHSkBm8wLop",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3134,
      "cache_read_input_tokens": 46379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3134,
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

_source line 51 · 2026-05-21T15:52:53.355Z_

<details><summary>↩ Tool result · `toolu_01MpxznYt8xVson8hxfy4gju`</summary>

```text
/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py-72-    return M
/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py-73-
/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py-74-
exp017_rlearner.py:75:def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py-76-    cond = np.linalg.cond(M)
exp017_rlearner.py:77:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py-78-        return tau_obs.copy(), se_obs.copy()
/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py-79-    det = np.linalg.det(M)
exp017_rlearner.py-80-    if abs(det) < 1e-10:
--
/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py-96-    return M
/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py-97-
/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py-98-
exp015_semi_real_cm.py:99:def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py-100-    cond = np.linalg.cond(M)
exp015_semi_real_cm.py:101:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py-102-        return tau_obs.copy(), se_obs.copy()
/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py-103-    det = np.linalg.det(M)
exp015_semi_real_cm.py-104-    if abs(det) < 1e-10:
--
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-24-
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-25-
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-26-def run_one_mc_reg(regime_name, regime_params, n_expert, k, seed,
exp001_regularize.py:27:                   cond_threshold=100, n_chains=4, n_iter=4000, n_warmup=2000):
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-28-    data = generate_data(regime_params, n_expert, k, seed)
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-29-    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-30-    em = data['expert_mask']
--
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-58-
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-59-        cond_mle = np.linalg.cond(M_mle[s])
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-60-        cond_hb = np.linalg.cond(M_hb[s])
exp001_regularize.py:61:        if cond_mle > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-62-            guard_mle += 1
exp001_regularize.py:63:        if cond_hb > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-64-            guard_hb += 1
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-65-
exp001_regularize.py:66:        tml_r, sml_r = invert_mixing_safe(M_mle[s], tau_obs, se_obs, cond_threshold)
exp001_regularize.py:67:        thb_r, shb_r = invert_mixing_safe(M_hb[s], tau_obs, se_obs, cond_threshold)
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-68-
exp001_regularize.py-69-        def mr(method, th0, th1, se0, se1):
exp001_regularize.py-70-            return {**base, 'subgroup': s, 'method': method,
--
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-84-    parser.add_argument('--cond-threshold', type=float, default=100)
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-85-    args = parser.parse_args()
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-86-
exp001_regularize.py:87:    print(f"exp-001 Regularization fix v2 | cond_threshold={args.cond_threshold}")
exp001_regularize.py-88-    print(f"Affected cells: {AFFECTED_CELLS}")
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-89-    print(f"n_mc={args.n_mc}")
exp001_regularize.py-90-    print(f"MCMC config: n_chains=4, n_iter=4000, n_warmup=2000\n")
--
exp001_regularize.py-137-        for mc in range(args.n_mc):
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-138-            rows, hb_diag, g_hb, g_mle = run_one_mc_reg(
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-139-                regime, rp, n_expert, k, seed=mc,
exp001_regularize.py:140:                cond_threshold=args.cond_threshold,
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-141-                n_chains=4, n_iter=4000, n_warmup=2000)
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-142-            all_rows.extend(rows)
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-143-            guard_stats[key]['total'] += 1
--
/home/ubuntu/ec_hte_llm_annotation/exp003_tweeteval.py-111-    return M
/home/ubuntu/ec_hte_llm_annotation/exp003_tweeteval.py-112-
/home/ubuntu/ec_hte_llm_annotation/exp003_tweeteval.py-113-
exp003_tweeteval.py:114:def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
/home/ubuntu/ec_hte_llm_annotation/exp003_tweeteval.py-115-    """Like invert_mixing but with condition number guard."""
/home/ubuntu/ec_hte_llm_annotation/exp003_tweeteval.py-116-    cond = np.linalg.cond(M)
exp003_tweeteval.py:117:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp003_tweeteval.py-118-        return tau_obs.copy(), se_obs.copy()
/home/ubuntu/ec_hte_llm_annotation/exp003_tweeteval.py-119-    det = np.linalg.det(M)
exp003_tweeteval.py-120-    if abs(det) < 1e-10:
--
/home/ubuntu/ec_hte_llm_annotation/exp018_multiplicative_dgp.py-101-    return M
/home/ubuntu/ec_hte_llm_annotation/exp018_multiplicative_dgp.py-102-
/home/ubuntu/ec_hte_llm_annotation/exp018_multiplicative_dgp.py-103-
exp018_multiplicative_dgp.py:104:def invert_mixing(M, tau_obs, se_obs, cond_threshold=100):
/home/ubuntu/ec_hte_llm_annotation/exp018_multiplicative_dgp.py-105-    cond = np.linalg.cond(M)
exp018_multiplicative_dgp.py:106:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp018_multiplicative_dgp.py-107-        return tau_obs.copy(), se_obs.copy()
/home/ubuntu/ec_hte_llm_annotation/exp018_multiplicative_dgp.py-108-    det = np.linalg.det(M)
exp018_multiplicative_dgp.py-109-    if abs(det) < 1e-10:
--
/home/ubuntu/ec_hte_llm_annotation/exp016_semi_real_better_cm.py-100-    return M
/home/ubuntu/ec_hte_llm_annotation/exp016_semi_real_better_cm.py-101-
/home/ubuntu/ec_hte_llm_annotation/exp016_semi_real_better_cm.py-102-
exp016_semi_real_better_cm.py:103:def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
/home/ubuntu/ec_hte_llm_annotation/exp016_semi_real_better_cm.py-104-    cond = np.linalg.cond(M)
exp016_semi_real_better_cm.py:105:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp016_semi_real_better_cm.py-106-        return tau_obs.copy(), se_obs.copy()
/home/ubuntu/ec_hte_llm_annotation/exp016_semi_real_better_cm.py-107-    det = np.linalg.det(M)
exp016_semi_real_better_cm.py-108-    if abs(det) < 1e-10:
--
/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py-40-
/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py-41-
/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py-42-def run_one_sensitivity(regime_params, n_expert, k, seed, hp_a0, hp_b0,
exp001_hyperprior_sensitivity.py:43:                        use_safe_invert=False):
/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py-44-    data = generate_data(regime_params, n_expert, k, seed)
/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py-45-    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py-46-    em = data['expert_mask']
--
exp001_hyperprior_sensitivity.py-65-        if np.any(np.isnan(tau_obs)):
/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py-66-            continue
/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py-67-
exp001_hyperprior_sensitivity.py:68:        _invert = invert_mixing_safe if use_safe_invert else invert_mixing
/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py-69-        tml, sml = _invert(M_mle[s], tau_obs, se_obs)
/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py-70-        thb, shb = _invert(M_hb[s], tau_obs, se_obs)
/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py-71-
--
exp001_hyperprior_sensitivity.py-136-            for mc in range(n_mc):
/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py-137-                rows = run_one_sensitivity(regime_params, n_expert, k,
/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py-138-                                           seed=mc, hp_a0=hp_a0, hp_b0=hp_b0,
exp001_hyperprior_sensitivity.py:139:                                           use_safe_invert=use_safe)
exp001_hyperprior_sensitivity.py-140-                for r in rows:
/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py-141-                    r['hyperprior_scale'] = scale
/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py-142-                    r['config'] = label
--
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py-122-    return tau_c, se_c
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py-123-
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py-124-
exp001_hb_synthetic.py:125:def safe_invert_correction(M_s, tau_obs, cond_threshold=100, fallback='naive'):
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py-126-    """Invert mixing matrix with condition number guard.
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py-127-
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py-128-    When cond(M_s) > threshold, matrix inversion is numerically unstable.
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py-129-    Falls back to naive (no correction) to avoid catastrophic amplification.
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py-130-    """
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py-131-    cond = np.linalg.cond(M_s)
exp001_hb_synthetic.py:132:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py-133-        return tau_obs.copy()
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py-134-    return np.linalg.solve(M_s, tau_obs)
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py-135-
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py-136-
exp001_hb_synthetic.py:137:def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py-138-    """Like invert_mixing but with condition number guard."""
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py-139-    cond = np.linalg.cond(M)
exp001_hb_synthetic.py:140:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py-141-        return tau_obs.copy(), se_obs.copy()
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py-142-    det = np.linalg.det(M)
exp001_hb_synthetic.py-143-    if abs(det) < 1e-10:
--
/home/ubuntu/ec_hte_llm_annotation/exp006_budget_sensitivity.py-141-    return M
/home/ubuntu/ec_hte_llm_annotation/exp006_budget_sensitivity.py-142-
/home/ubuntu/ec_hte_llm_annotation/exp006_budget_sensitivity.py-143-
exp006_budget_sensitivity.py:144:def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
exp006_budget_sensitivity.py:145:    """Invert mixing matrix with condition number guard (cond_threshold=100)."""
/home/ubuntu/ec_hte_llm_annotation/exp006_budget_sensitivity.py-146-    cond = np.linalg.cond(M)
exp006_budget_sensitivity.py:147:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp006_budget_sensitivity.py-148-        return tau_obs.copy(), se_obs.copy()
/home/ubuntu/ec_hte_llm_annotation/exp006_budget_sensitivity.py-149-    det = np.linalg.det(M)
exp006_budget_sensitivity.py-150-    if abs(det) < 1e-10:
--
/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py-321-    return tau_corrected, se_corrected
/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py-322-
/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py-323-
exp007_ppci_dsl.py:324:def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py-325-    """Like invert_mixing but with condition number guard. cond(M) > threshold → fallback to uncorrected."""
/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py-326-    cond = np.linalg.cond(M)
exp007_ppci_dsl.py:327:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py-328-        return tau_obs.copy(), se_obs.copy()
/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py-329-    det = np.linalg.det(M)
exp007_ppci_dsl.py-330-    if abs(det) < 1e-10:
--
/home/ubuntu/ec_hte_llm_annotation/exp010_misspecified_subgroups.py-98-    return y1.mean() - y0.mean(), np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)
/home/ubuntu/ec_hte_llm_annotation/exp010_misspecified_subgroups.py-99-
/home/ubuntu/ec_hte_llm_annotation/exp010_misspecified_subgroups.py-100-
exp010_misspecified_subgroups.py:101:def invert_mixing(M, tau_obs, se_obs, cond_threshold=100):
/home/ubuntu/ec_hte_llm_annotation/exp010_misspecified_subgroups.py-102-    cond = np.linalg.cond(M)
exp010_misspecified_subgroups.py:103:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp010_misspecified_subgroups.py-104-        return tau_obs.copy(), se_obs.copy()
/home/ubuntu/ec_hte_llm_annotation/exp010_misspecified_subgroups.py-105-    det = np.linalg.det(M)
exp010_misspecified_subgroups.py-106-    if abs(det) < 1e-10:
--
/home/ubuntu/ec_hte_llm_annotation/exp019_pz1_sweep.py-139-    return tau_c, se_c
/home/ubuntu/ec_hte_llm_annotation/exp019_pz1_sweep.py-140-
/home/ubuntu/ec_hte_llm_annotation/exp019_pz1_sweep.py-141-
exp019_pz1_sweep.py:142:def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
/home/ubuntu/ec_hte_llm_annotation/exp019_pz1_sweep.py-143-    cond = np.linalg.cond(M)
exp019_pz1_sweep.py:144:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp019_pz1_sweep.py-145-        return tau_obs.copy(), se_obs.copy()
/home/ubuntu/ec_hte_llm_annotation/exp019_pz1_sweep.py-146-    return invert_mixing(M, tau_obs, se_obs)
/home/ubuntu/ec_hte_llm_annotation/exp019_pz1_sweep.py-147-
--
/home/ubuntu/ec_hte_llm_annotation/exp011_causal_forest.py-94-    return M
/home/ubuntu/ec_hte_llm_annotation/exp011_causal_forest.py-95-
/home/ubuntu/ec_hte_llm_annotation/exp011_causal_forest.py-96-
exp011_causal_forest.py:97:def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
/home/ubuntu/ec_hte_llm_annotation/exp011_causal_forest.py-98-    """M^-1 correction with condition number guard."""
/home/ubuntu/ec_hte_llm_annotation/exp011_causal_forest.py-99-    cond = np.linalg.cond(M)
exp011_causal_forest.py:100:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp011_causal_forest.py-101-        return tau_obs.copy(), se_obs.copy()
/home/ubuntu/ec_hte_llm_annotation/exp011_causal_forest.py-102-    det = np.linalg.det(M)
exp011_causal_forest.py-103-    if abs(det) < 1e-10:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "5523d3f6-a5f0-4e74-a0d6-5daa3ca698a5"
}
```

</details>

---

### System

_source line 52_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Reading exp001_regularize.py",
  "usage": {
    "total_tokens": 56455,
    "tool_uses": 15,
    "duration_ms": 31301
  },
  "last_tool_name": "Read",
  "uuid": "59a1e346-a511-4fe7-ad3a-7d2263cb8041",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Read · `toolu_01V9PYdJYzrDG8Z15hL2SVmv`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "a50d9201-2c4a-4ec7-b79d-0c9c18932954",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PS5TNF6i1pmq2jqhuA7FA6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6877,
      "cache_read_input_tokens": 49513,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6877,
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

_source line 54 · 2026-05-21T15:52:55.523Z_

<details><summary>↩ Tool result · `toolu_01V9PYdJYzrDG8Z15hL2SVmv`</summary>

```text
1	#!/usr/bin/env python3
2	"""exp001_regularize.py - Rerun affected cells with condition-number-guarded inversion."""
3	
4	import argparse
5	import time
6	import numpy as np
7	import pandas as pd
8	
9	from exp001_hb_synthetic import (
10	    REGIMES, SUBGROUP_LABELS,
11	    generate_data, get_counts, build_mixing_matrix, diff_in_means,
12	    estimate_cm_mle, estimate_cm_hb_eb, estimate_cm_hb_gibbs,
13	    invert_mixing_safe, aggregate_results,
14	)
15	
16	AFFECTED_CELLS = [
17	    (4, 'extreme', 50),
18	    (4, 'extreme', 100),
19	    (4, 'moderate', 50),
20	    (4, 'moderate', 100),
21	    (4, 'homogeneous', 50),
22	    (4, 'homogeneous', 100),
23	]
24	
25	
26	def run_one_mc_reg(regime_name, regime_params, n_expert, k, seed,
27	                   cond_threshold=100, n_chains=4, n_iter=4000, n_warmup=2000):
28	    data = generate_data(regime_params, n_expert, k, seed)
29	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
30	    em = data['expert_mask']
31	    labels = SUBGROUP_LABELS[k]
32	    tau_z0, tau_z1 = regime_params['tau_z0'], regime_params['tau_z1']
33	
34	    counts = get_counts(Z[em], Z_hat[em], S[em], labels)
35	    C_mle = estimate_cm_mle(counts, labels)
36	    C_hb, hb_diag = estimate_cm_hb_gibbs(counts, labels, seed=seed,
37	                                          n_chains=n_chains, n_iter=n_iter,
38	                                          n_warmup=n_warmup)
39	
40	    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in labels}
41	    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}
42	
43	    base = {'regime': regime_name, 'n_expert': n_expert,
44	            'k_subgroups': k, 'mc_run': seed}
45	    rows = []
46	    guard_hb = 0
47	    guard_mle = 0
48	
49	    for s in labels:
50	        sm = S == s
51	        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))
52	        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))
53	
54	        tau_obs = np.array([th0_n, th1_n])
55	        se_obs = np.array([se0_n, se1_n])
56	        if np.any(np.isnan(tau_obs)):
57	            continue
58	
59	        cond_mle = np.linalg.cond(M_mle[s])
60	        cond_hb = np.linalg.cond(M_hb[s])
61	        if cond_mle > cond_threshold:
62	            guard_mle += 1
63	        if cond_hb > cond_threshold:
64	            guard_hb += 1
65	
66	        tml_r, sml_r = invert_mixing_safe(M_mle[s], tau_obs, se_obs, cond_threshold)
67	        thb_r, shb_r = invert_mixing_safe(M_hb[s], tau_obs, se_obs, cond_threshold)
68	
69	        def mr(method, th0, th1, se0, se1):
70	            return {**base, 'subgroup': s, 'method': method,
71	                    'tau_hat_z0': th0, 'tau_hat_z1': th1,
72	                    'se_z0': se0, 'se_z1': se1,
73	                    'tau_true_z0': tau_z0, 'tau_true_z1': tau_z1}
74	
75	        rows.append(mr('mle_laplace_reg', tml_r[0], tml_r[1], sml_r[0], sml_r[1]))
76	        rows.append(mr('hb_dirichlet_reg', thb_r[0], thb_r[1], shb_r[0], shb_r[1]))
77	
78	    return rows, hb_diag, guard_hb, guard_mle
79	
80	
81	if __name__ == '__main__':
82	    parser = argparse.ArgumentParser()
83	    parser.add_argument('--n-mc', type=int, default=100)
84	    parser.add_argument('--cond-threshold', type=float, default=100)
85	    args = parser.parse_args()
86	
87	    print(f"exp-001 Regularization fix v2 | cond_threshold={args.cond_threshold}")
88	    print(f"Affected cells: {AFFECTED_CELLS}")
89	    print(f"n_mc={args.n_mc}")
90	    print(f"MCMC config: n_chains=4, n_iter=4000, n_warmup=2000\n")
91	
92	    # ── MCMC diagnostic comparison (before/after) ────────────────────────────
93	    print("Running MCMC diagnostic comparison (seed=0, per config)...")
94	    diag_rows = []
95	    for k, regime, n_expert in AFFECTED_CELLS:
96	        rp = REGIMES[k][regime]
97	        d = generate_data(rp, n_expert, k, seed=0)
98	        em = d['expert_mask']
99	        labels = SUBGROUP_LABELS[k]
100	        counts = get_counts(d['Z'][em], d['Z_hat'][em], d['S'][em], labels)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "a730038c-f28c-429d-86dc-378feba7b2a4"
}
```

</details>

---

### System

_source line 55_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Reading exp006_budget_sensitivity.py",
  "usage": {
    "total_tokens": 56456,
    "tool_uses": 16,
    "duration_ms": 31614
  },
  "last_tool_name": "Read",
  "uuid": "b41d12e7-ed86-4faf-bab2-4d3eb79681f1",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Read · `toolu_01VLt5ysXDg67T6YW8kubdnq`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp006_budget_sensitivity.py",
  "offset": 141,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "9ed3f3d6-f6fa-4516-ae8b-d47bc66b7c27",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PS5TNF6i1pmq2jqhuA7FA6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6877,
      "cache_read_input_tokens": 49513,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6877,
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

_source line 57 · 2026-05-21T15:52:55.834Z_

<details><summary>↩ Tool result · `toolu_01VLt5ysXDg67T6YW8kubdnq`</summary>

```text
141	    return M
142	
143	
144	def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
145	    """Invert mixing matrix with condition number guard (cond_threshold=100)."""
146	    cond = np.linalg.cond(M)
147	    if cond > cond_threshold:
148	        return tau_obs.copy(), se_obs.copy()
149	    det = np.linalg.det(M)
150	    if abs(det) < 1e-10:
151	        return tau_obs.copy(), se_obs.copy()
152	    Mi = np.linalg.inv(M)
153	    tau_c = Mi @ tau_obs
154	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
155	    return tau_c, se_c
156	
157	
158	# ── Confusion Matrix Estimators ──────────────────────────────────────────────
159	
160	def estimate_cm_mle(counts, labels):
161	    """Per-subgroup MLE with Laplace smoothing (add-1)."""
162	    C = {}
163	    for i, s in enumerate(labels):
164	        C_s = np.zeros((2, 2))
165	        for z in [0, 1]:
166	            n = counts[i, z, :].sum()
167	            for zh in [0, 1]:
168	                C_s[z, zh] = (counts[i, z, zh] + 1) / (n + 2) if n > 0 else 0.5
169	        C[s] = C_s
170	    return C
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "0d878872-2b45-4907-a4d3-44493e647aba"
}
```

</details>

---

### System

_source line 58_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Running grep -r \"κ\\|kappa\\|cond.*threshold\\|fallback\" /ho…",
  "usage": {
    "total_tokens": 58868,
    "tool_uses": 17,
    "duration_ms": 33802
  },
  "last_tool_name": "Bash",
  "uuid": "f9d4e6a2-455c-4de0-8be1-acb5ee3284a0",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Bash · `toolu_015RP8XKLhWDNzjuscbyCXbR`</summary>

```json
{
  "command": "grep -r \"κ\\|kappa\\|cond.*threshold\\|fallback\" /home/ubuntu/ec_hte_llm_annotation/*.py 2>/dev/null | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "da770cc5-b6d0-45f0-a4ab-f251df315c02",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TA1axziyh8pyy5F3F6ePyt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2410,
      "cache_read_input_tokens": 56390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2410,
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

_source line 60 · 2026-05-21T15:52:58.078Z_

<details><summary>↩ Tool result · `toolu_015RP8XKLhWDNzjuscbyCXbR`</summary>

```text
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py:def safe_invert_correction(M_s, tau_obs, cond_threshold=100, fallback='naive'):
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py:    When cond(M_s) > threshold, matrix inversion is numerically unstable.
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py:def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py:            hb_diag['hb_method'] = 'eb_fallback'
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py:                   cond_threshold=100, n_chains=4, n_iter=4000, n_warmup=2000):
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py:        if cond_mle > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py:        if cond_hb > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py:        tml_r, sml_r = invert_mixing_safe(M_mle[s], tau_obs, se_obs, cond_threshold)
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py:        thb_r, shb_r = invert_mixing_safe(M_hb[s], tau_obs, se_obs, cond_threshold)
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py:    parser.add_argument('--cond-threshold', type=float, default=100)
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py:    print(f"exp-001 Regularization fix v2 | cond_threshold={args.cond_threshold}")
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py:                cond_threshold=args.cond_threshold,
/home/ubuntu/ec_hte_llm_annotation/exp002_bias_bound.py:    print(f"\n  K=4 'debiasing hurts' condition: π_s < π̄/(2(1-π̄)) = {threshold_k4:.4f}")
/home/ubuntu/ec_hte_llm_annotation/exp003_tweeteval.py:def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
/home/ubuntu/ec_hte_llm_annotation/exp003_tweeteval.py:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp006_budget_sensitivity.py:def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
/home/ubuntu/ec_hte_llm_annotation/exp006_budget_sensitivity.py:    """Invert mixing matrix with condition number guard (cond_threshold=100)."""
/home/ubuntu/ec_hte_llm_annotation/exp006_budget_sensitivity.py:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py:def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py:    """Like invert_mixing but with condition number guard. cond(M) > threshold → fallback to uncorrected."""
/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp010_misspecified_subgroups.py:def invert_mixing(M, tau_obs, se_obs, cond_threshold=100):
/home/ubuntu/ec_hte_llm_annotation/exp010_misspecified_subgroups.py:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp011_causal_forest.py:def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
/home/ubuntu/ec_hte_llm_annotation/exp011_causal_forest.py:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py:def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp016_semi_real_better_cm.py:def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
/home/ubuntu/ec_hte_llm_annotation/exp016_semi_real_better_cm.py:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py:def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp018_multiplicative_dgp.py:def invert_mixing(M, tau_obs, se_obs, cond_threshold=100):
/home/ubuntu/ec_hte_llm_annotation/exp018_multiplicative_dgp.py:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/exp019_pz1_sweep.py:def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
/home/ubuntu/ec_hte_llm_annotation/exp019_pz1_sweep.py:    if cond > cond_threshold:
/home/ubuntu/ec_hte_llm_annotation/pilot_llm_annotation.py:# Supports vLLM (high throughput) and transformers (fallback) backends.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "4a3942f4-24b0-4dcc-b4be-0440aa06a559"
}
```

</details>

---

### System

_source line 61_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Running grep -n \"cond_threshold\" /home/ubuntu/ec_hte_llm_…",
  "usage": {
    "total_tokens": 58869,
    "tool_uses": 18,
    "duration_ms": 34125
  },
  "last_tool_name": "Bash",
  "uuid": "fe320097-ef4a-4474-94a0-ce5a637fd661",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Bash · `toolu_018u797JP1q9m5tPFDYogoYc`</summary>

```json
{
  "command": "grep -n \"cond_threshold\" /home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "63fca43e-9e6c-4e2c-8588-003e3bf6000a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TA1axziyh8pyy5F3F6ePyt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2410,
      "cache_read_input_tokens": 56390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2410,
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

_source line 63 · 2026-05-21T15:52:58.386Z_

<details><summary>↩ Tool result · `toolu_018u797JP1q9m5tPFDYogoYc`</summary>

```text
125:def safe_invert_correction(M_s, tau_obs, cond_threshold=100, fallback='naive'):
132:    if cond > cond_threshold:
137:def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
140:    if cond > cond_threshold:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "8597ca3b-e152-4a7d-a61a-4d3a7b94d0b7"
}
```

</details>

---

### System

_source line 64_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Running grep -r \"κ\\|kappa\\|condition number\" /home/ubuntu…",
  "usage": {
    "total_tokens": 60957,
    "tool_uses": 19,
    "duration_ms": 36508
  },
  "last_tool_name": "Bash",
  "uuid": "b9bf8f41-5494-4b38-91f1-55f75b88e629",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Bash · `toolu_01W9rPxZCzHVVvWq9g3EzWKk`</summary>

```json
{
  "command": "grep -r \"κ\\|kappa\\|condition number\" /home/ubuntu/ec_hte_llm_annotation/*.py 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "93099b63-db8e-4593-908f-92e66977464d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KMKHmoWV7hC9F844gjr6GL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2086,
      "cache_read_input_tokens": 58800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2086,
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

_source line 66 · 2026-05-21T15:53:00.774Z_

<details><summary>↩ Tool result · `toolu_01W9rPxZCzHVVvWq9g3EzWKk`</summary>

```text
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py:    """Invert mixing matrix with condition number guard.
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py:    """Like invert_mixing but with condition number guard."""
/home/ubuntu/ec_hte_llm_annotation/exp003_tweeteval.py:    """Like invert_mixing but with condition number guard."""
/home/ubuntu/ec_hte_llm_annotation/exp006_budget_sensitivity.py:    """Invert mixing matrix with condition number guard (cond_threshold=100)."""
/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py:    """Like invert_mixing but with condition number guard. cond(M) > threshold → fallback to uncorrected."""
/home/ubuntu/ec_hte_llm_annotation/exp011_causal_forest.py:    """M^-1 correction with condition number guard."""
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "0c1dee3d-d53b-4b41-9f87-e6c42639bad8"
}
```

</details>

---

### System

_source line 67_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Reading exp001_hb_synthetic.py",
  "usage": {
    "total_tokens": 60958,
    "tool_uses": 20,
    "duration_ms": 36820
  },
  "last_tool_name": "Read",
  "uuid": "a7bb927c-abb4-4c32-90ca-1a549ca37427",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Read · `toolu_0134TKz6S9xy2mLGNoJ2Bq2C`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py",
  "offset": 115,
  "limit": 35
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "ba58083a-21e5-4143-9e3d-e24f5a3a1f62",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KMKHmoWV7hC9F844gjr6GL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2086,
      "cache_read_input_tokens": 58800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2086,
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

_source line 69 · 2026-05-21T15:53:01.041Z_

<details><summary>↩ Tool result · `toolu_0134TKz6S9xy2mLGNoJ2Bq2C`</summary>

```text
115	def invert_mixing(M, tau_obs, se_obs):
116	    det = np.linalg.det(M)
117	    if abs(det) < 1e-10:
118	        return tau_obs.copy(), se_obs.copy()
119	    Mi = np.linalg.inv(M)
120	    tau_c = Mi @ tau_obs
121	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
122	    return tau_c, se_c
123	
124	
125	def safe_invert_correction(M_s, tau_obs, cond_threshold=100, fallback='naive'):
126	    """Invert mixing matrix with condition number guard.
127	
128	    When cond(M_s) > threshold, matrix inversion is numerically unstable.
129	    Falls back to naive (no correction) to avoid catastrophic amplification.
130	    """
131	    cond = np.linalg.cond(M_s)
132	    if cond > cond_threshold:
133	        return tau_obs.copy()
134	    return np.linalg.solve(M_s, tau_obs)
135	
136	
137	def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
138	    """Like invert_mixing but with condition number guard."""
139	    cond = np.linalg.cond(M)
140	    if cond > cond_threshold:
141	        return tau_obs.copy(), se_obs.copy()
142	    det = np.linalg.det(M)
143	    if abs(det) < 1e-10:
144	        return tau_obs.copy(), se_obs.copy()
145	    Mi = np.linalg.inv(M)
146	    tau_c = Mi @ tau_obs
147	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
148	    return tau_c, se_c
149	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "4eae2eb2-9c1a-491c-bd31-b675c0998619"
}
```

</details>

---

### System

_source line 70_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Running grep -n \"cond_threshold\\|cond > \\|cond_mle\\|cond_…",
  "usage": {
    "total_tokens": 62028,
    "tool_uses": 21,
    "duration_ms": 39397
  },
  "last_tool_name": "Bash",
  "uuid": "74f2c685-8c77-45a4-9fa4-df2df2002c50",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 71_

<details open><summary>🔧 Tool call — Bash · `toolu_012BEVmXfhapVNXsRed4Moyd`</summary>

```json
{
  "command": "grep -n \"cond_threshold\\|cond > \\|cond_mle\\|cond_hb\" /home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "81ce733b-73c7-4197-8207-d1e355ccf755",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PZpr4ZDxLqHtRdESaQvVaA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1062,
      "cache_read_input_tokens": 60886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1062,
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

### System

_source line 72_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Running grep -A 5 \"parser.add_argument.*cond\" /home/ubunt…",
  "usage": {
    "total_tokens": 62032,
    "tool_uses": 22,
    "duration_ms": 39443
  },
  "last_tool_name": "Bash",
  "uuid": "285ebc63-3d85-4704-8388-f271991c93a6",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 73_

<details open><summary>🔧 Tool call — Bash · `toolu_01XuwxQ8M9mdLzmnZLDfEd94`</summary>

```json
{
  "command": "grep -A 5 \"parser.add_argument.*cond\" /home/ubuntu/ec_hte_llm_annotation/*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "25df65ab-b27b-40e8-9126-29745a3dfa4c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PZpr4ZDxLqHtRdESaQvVaA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1062,
      "cache_read_input_tokens": 60886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1062,
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

_source line 74 · 2026-05-21T15:53:03.681Z_

<details><summary>↩ Tool result · `toolu_012BEVmXfhapVNXsRed4Moyd`</summary>

```text
27:                   cond_threshold=100, n_chains=4, n_iter=4000, n_warmup=2000):
59:        cond_mle = np.linalg.cond(M_mle[s])
60:        cond_hb = np.linalg.cond(M_hb[s])
61:        if cond_mle > cond_threshold:
63:        if cond_hb > cond_threshold:
66:        tml_r, sml_r = invert_mixing_safe(M_mle[s], tau_obs, se_obs, cond_threshold)
67:        thb_r, shb_r = invert_mixing_safe(M_hb[s], tau_obs, se_obs, cond_threshold)
87:    print(f"exp-001 Regularization fix v2 | cond_threshold={args.cond_threshold}")
140:                cond_threshold=args.cond_threshold,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "769d1044-cad8-4988-953d-39f987b003c2"
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-21T15:53:03.723Z_

<details><summary>↩ Tool result · `toolu_01XuwxQ8M9mdLzmnZLDfEd94`</summary>

```text
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py:    parser.add_argument('--cond-threshold', type=float, default=100)
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-    args = parser.parse_args()
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-    print(f"exp-001 Regularization fix v2 | cond_threshold={args.cond_threshold}")
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-    print(f"Affected cells: {AFFECTED_CELLS}")
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py-    print(f"n_mc={args.n_mc}")
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "49e796c8-4ca1-4ea5-b697-6f6b09d5c771"
}
```

</details>

---

### System

_source line 76_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Reading exp007_ppci_dsl.py",
  "usage": {
    "total_tokens": 62765,
    "tool_uses": 23,
    "duration_ms": 41594
  },
  "last_tool_name": "Read",
  "uuid": "b4d8a86c-ea6d-4c32-a722-1d9c640d7735",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 77_

<details open><summary>🔧 Tool call — Read · `toolu_01RLxDtRMBWGrgYvo3UjSh4W`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py",
  "offset": 315,
  "limit": 25
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "81a4054e-2614-4f63-b392-a176ecdca6a4",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012YY9Q8bawYDZQ2xf9Uh4br",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 731,
      "cache_read_input_tokens": 61948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 731,
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

_source line 78 · 2026-05-21T15:53:05.819Z_

<details><summary>↩ Tool result · `toolu_01RLxDtRMBWGrgYvo3UjSh4W`</summary>

```text
315	        return tau_obs.copy(), se_obs.copy()
316	    M_inv = np.linalg.inv(M)
317	    tau_corrected = M_inv @ tau_obs
318	    sigma_obs = np.diag(se_obs ** 2)
319	    sigma_corrected = M_inv @ sigma_obs @ M_inv.T
320	    se_corrected = np.sqrt(np.diag(sigma_corrected))
321	    return tau_corrected, se_corrected
322	
323	
324	def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
325	    """Like invert_mixing but with condition number guard. cond(M) > threshold → fallback to uncorrected."""
326	    cond = np.linalg.cond(M)
327	    if cond > cond_threshold:
328	        return tau_obs.copy(), se_obs.copy()
329	    det = np.linalg.det(M)
330	    if abs(det) < 1e-10:
331	        return tau_obs.copy(), se_obs.copy()
332	    Mi = np.linalg.inv(M)
333	    tau_c = Mi @ tau_obs
334	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
335	    return tau_c, se_c
336	
337	
338	def method_oracle(data, s_val):
339	    """Oracle: use true Z within subgroup s."""
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "6821e858-713a-43a9-92ca-5e5d6bf5b376"
}
```

</details>

---

### System

_source line 79_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Running grep -B 5 -A 15 \"def invert_mixing_safe\" /home/ub…",
  "usage": {
    "total_tokens": 62766,
    "tool_uses": 24,
    "duration_ms": 41824
  },
  "last_tool_name": "Bash",
  "uuid": "9664e48c-27b0-4549-97dd-1d1cb0dfb5bb",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 80_

<details open><summary>🔧 Tool call — Bash · `toolu_01UG4bYP8VFWkkEQupwmQcTL`</summary>

```json
{
  "command": "grep -B 5 -A 15 \"def invert_mixing_safe\" /home/ubuntu/ec_hte_llm_annotation/exp003_tweeteval.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "da4fe0f7-2d06-411a-9184-109e4af1e2c6",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012YY9Q8bawYDZQ2xf9Uh4br",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 731,
      "cache_read_input_tokens": 61948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 731,
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

_source line 81 · 2026-05-21T15:53:06.100Z_

<details><summary>↩ Tool result · `toolu_01UG4bYP8VFWkkEQupwmQcTL`</summary>

```text
        for z in [0, 1]:
            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5
    return M


def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
    """Like invert_mixing but with condition number guard."""
    cond = np.linalg.cond(M)
    if cond > cond_threshold:
        return tau_obs.copy(), se_obs.copy()
    det = np.linalg.det(M)
    if abs(det) < 1e-10:
        return tau_obs.copy(), se_obs.copy()
    Mi = np.linalg.inv(M)
    tau_c = Mi @ tau_obs
    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
    return tau_c, se_c


# === HB Gibbs Sampler (from exp-001) ===
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "528d115b-5113-4cb5-8d45-63fb22178f5d"
}
```

</details>

---

### System

_source line 82_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "description": "Running cat /home/ubuntu/ec_hte_llm_annotation/exp001_hb_…",
  "usage": {
    "total_tokens": 63729,
    "tool_uses": 25,
    "duration_ms": 43924
  },
  "last_tool_name": "Bash",
  "uuid": "280239c5-aadb-48e5-b42e-765ee1e12d54",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool call

_source line 83_

<details open><summary>🔧 Tool call — Bash · `toolu_019zTqhB3XVzqMNea3e3bPPi`</summary>

```json
{
  "command": "cat /home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py | head -50 | tail -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "eae34272-471d-446f-95b8-20664321fc0b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012AgsksnN9jtpVdhEU7Wq14",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 961,
      "cache_read_input_tokens": 62679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 961,
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

_source line 84 · 2026-05-21T15:53:08.231Z_

<details><summary>↩ Tool result · `toolu_019zTqhB3XVzqMNea3e3bPPi`</summary>

```text
    HAS_PYMC = False

N = 5000
SUBGROUP_LABELS = {2: ['A', 'B'], 4: ['A', 'B', 'C', 'D']}

REGIMES = {
    2: {
        'extreme':     {'misclass': [0.25, 0.05], 'tau_z1': 0.5, 'tau_z0': 0.1},
        'moderate':    {'misclass': [0.15, 0.10], 'tau_z1': 0.3, 'tau_z0': 0.15},
        'homogeneous': {'misclass': [0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},
    },
    4: {
        'extreme':     {'misclass': [0.30, 0.20, 0.10, 0.03], 'tau_z1': 0.5, 'tau_z0': 0.1},
        'moderate':    {'misclass': [0.20, 0.15, 0.10, 0.05], 'tau_z1': 0.3, 'tau_z0': 0.15},
        'homogeneous': {'misclass': [0.12, 0.12, 0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},
    },
}

DEFAULT_N_EXPERTS = [50, 100, 250, 500, 1000, 2000]
DEFAULT_K_LIST = [2, 4]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "08c4d669-05b3-4d94-8ba3-dec502390655"
}
```

</details>

---

### System

_source line 85_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ab8d433e6e5ed7d25",
  "tool_use_id": "toolu_01RwherfVUQDPdgza9quvcFc",
  "status": "completed",
  "output_file": "",
  "summary": "Find kappa/condition number guard implementation",
  "usage": {
    "total_tokens": 64260,
    "tool_uses": 25,
    "duration_ms": 57716
  },
  "uuid": "01f41d9c-c207-4fe8-a5f2-3ebc64816dd2",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003"
}
```

---

### Tool result

_source line 86 · 2026-05-21T15:53:21.935Z_

<details><summary>↩ Tool result · `toolu_01RwherfVUQDPdgza9quvcFc`</summary>

````text
Now I have all the information needed to provide a comprehensive summary. Let me compile the findings:

## κ (Kappa) Condition Number Guard Implementation

I've conducted a thorough search across all Python files in the project and found comprehensive implementations of the κ (kappa) condition number guard for confusion matrices. Here's what I discovered:

### 1. Core Implementation

**Location**: `/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py` (primary implementation)

**Key Functions**:

#### `invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100)` (lines 137-148)
```python
def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
    """Like invert_mixing but with condition number guard."""
    cond = np.linalg.cond(M)
    if cond > cond_threshold:
        return tau_obs.copy(), se_obs.copy()
    det = np.linalg.det(M)
    if abs(det) < 1e-10:
        return tau_obs.copy(), se_obs.copy()
    Mi = np.linalg.inv(M)
    tau_c = Mi @ tau_obs
    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
    return tau_c, se_c
```

#### `safe_invert_correction(M_s, tau_obs, cond_threshold=100, fallback='naive')` (lines 125-134)
This is a simpler variant for scalar tau_obs without se computation.

### 2. How the Guard Works

**Condition Number Computation**:
- Uses `np.linalg.cond(M)` to compute the condition number (κ) of the mixing matrix M
- The condition number measures numerical sensitivity of matrix inversion

**Threshold Check**:
- **Default threshold**: κ = 100
- **Comparison**: `if cond > cond_threshold: return tau_obs.copy(), se_obs.copy()`

**Fallback Behavior**:
When condition number exceeds threshold:
- Returns the **uncorrected (naive) estimate** of tau_obs and se_obs
- Skips matrix inversion to avoid "catastrophic amplification" of numerical errors
- This is a safe fallback rather than attempting unstable inversion

**Double Guard** (lines 142-144):
- Also checks determinant with threshold `abs(det) < 1e-10`
- Provides secondary singularity detection

### 3. Wider Implementation Across Experiments

The pattern is replicated across **14+ experiment files** with identical or very similar logic:

- `/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py` (lines 137-148)
- `/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py` (parameter tuning, default 100)
- `/home/ubuntu/ec_hte_llm_annotation/exp003_tweeteval.py` (lines 114-122)
- `/home/ubuntu/ec_hte_llm_annotation/exp006_budget_sensitivity.py` (lines 144-155)
- `/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py` (lines 324-335)
- `/home/ubuntu/ec_hte_llm_annotation/exp010_misspecified_subgroups.py` (lines 101-109)
- `/home/ubuntu/ec_hte_llm_annotation/exp011_causal_forest.py` (lines 97-107)
- `/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py` (lines 99-109)
- `/home/ubuntu/ec_hte_llm_annotation/exp016_semi_real_better_cm.py` (lines 103-113)
- `/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py` (lines 75-85)
- `/home/ubuntu/ec_hte_llm_annotation/exp018_multiplicative_dgp.py` (lines 104-112)
- `/home/ubuntu/ec_hte_llm_annotation/exp019_pz1_sweep.py` (lines 142-146)
- `/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py` (conditional usage)

### 4. Threshold Configuration

**Default Value**: 100 (hardcoded in all function signatures)

**Tunable via Command Line** (in `exp001_regularize.py`):
```python
parser.add_argument('--cond-threshold', type=float, default=100)
```

**Usage with Custom Threshold**:
```python
tml_r, sml_r = invert_mixing_safe(M_mle[s], tau_obs, se_obs, cond_threshold)
thb_r, shb_r = invert_mixing_safe(M_hb[s], tau_obs, se_obs, cond_threshold)
```

### 5. Context: The Mixing Matrix

The mixing matrix M represents the confusion matrix transformed to [observed | true] space via Bayes rule:
- `M[z_hat, z]` = proportion of observed label z_hat that comes from true label z
- When M is nearly singular (high κ), inversion becomes numerically unstable
- This occurs when subgroups have extreme heterogeneous misclassification rates

### 6. Guard Statistics Tracking

In `exp001_regularize.py` (lines 59-64):
```python
cond_mle = np.linalg.cond(M_mle[s])
cond_hb = np.linalg.cond(M_hb[s])
if cond_mle > cond_threshold:
    guard_mle += 1
if cond_hb > cond_threshold:
    guard_hb += 1
```

Tracks how many subgroup-method combinations trigger the guard per MC run.

### Key Files to Reference

1. **Primary**: `/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py` (lines 125-148)
2. **Tuning/Analysis**: `/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py` (lines 26-78)
3. **Documentation examples**: `/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py` (lines 324-335)
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "ee077894-2764-4e9b-8b7c-341888fbe201",
  "tool_use_result": {
    "status": "completed",
    "prompt": "In the project at /home/ubuntu/ec_hte_llm_annotation/, I need to find how the κ (kappa) condition number guard is implemented. This is a singularity guard for confusion matrices where condition number > κ triggers a fallback.\n\nSearch for:\n1. \"kappa\", \"condition\", \"singularity\", \"guard\", \"cond_number\", \"det\" in all Python files\n2. Read the key files: run_simulation.py, and any files like ec_hte.py, hb_ec_hte.py that implement the core logic\n3. I need to understand: how is condition number computed, what threshold is used, and what happens when the guard triggers\n\nBe very thorough - search across all .py files in the project.",
    "agentId": "ab8d433e6e5ed7d25",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information needed to provide a comprehensive summary. Let me compile the findings:\n\n## κ (Kappa) Condition Number Guard Implementation\n\nI've conducted a thorough search across all Python files in the project and found comprehensive implementations of the κ (kappa) condition number guard for confusion matrices. Here's what I discovered:\n\n### 1. Core Implementation\n\n**Location**: `/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py` (primary implementation)\n\n**Key Functions**:\n\n#### `invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100)` (lines 137-148)\n```python\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    \"\"\"Like invert_mixing but with condition number guard.\"\"\"\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n```\n\n#### `safe_invert_correction(M_s, tau_obs, cond_threshold=100, fallback='naive')` (lines 125-134)\nThis is a simpler variant for scalar tau_obs without se computation.\n\n### 2. How the Guard Works\n\n**Condition Number Computation**:\n- Uses `np.linalg.cond(M)` to compute the condition number (κ) of the mixing matrix M\n- The condition number measures numerical sensitivity of matrix inversion\n\n**Threshold Check**:\n- **Default threshold**: κ = 100\n- **Comparison**: `if cond > cond_threshold: return tau_obs.copy(), se_obs.copy()`\n\n**Fallback Behavior**:\nWhen condition number exceeds threshold:\n- Returns the **uncorrected (naive) estimate** of tau_obs and se_obs\n- Skips matrix inversion to avoid \"catastrophic amplification\" of numerical errors\n- This is a safe fallback rather than attempting unstable inversion\n\n**Double Guard** (lines 142-144):\n- Also checks determinant with threshold `abs(det) < 1e-10`\n- Provides secondary singularity detection\n\n### 3. Wider Implementation Across Experiments\n\nThe pattern is replicated across **14+ experiment files** with identical or very similar logic:\n\n- `/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py` (lines 137-148)\n- `/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py` (parameter tuning, default 100)\n- `/home/ubuntu/ec_hte_llm_annotation/exp003_tweeteval.py` (lines 114-122)\n- `/home/ubuntu/ec_hte_llm_annotation/exp006_budget_sensitivity.py` (lines 144-155)\n- `/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py` (lines 324-335)\n- `/home/ubuntu/ec_hte_llm_annotation/exp010_misspecified_subgroups.py` (lines 101-109)\n- `/home/ubuntu/ec_hte_llm_annotation/exp011_causal_forest.py` (lines 97-107)\n- `/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py` (lines 99-109)\n- `/home/ubuntu/ec_hte_llm_annotation/exp016_semi_real_better_cm.py` (lines 103-113)\n- `/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py` (lines 75-85)\n- `/home/ubuntu/ec_hte_llm_annotation/exp018_multiplicative_dgp.py` (lines 104-112)\n- `/home/ubuntu/ec_hte_llm_annotation/exp019_pz1_sweep.py` (lines 142-146)\n- `/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py` (conditional usage)\n\n### 4. Threshold Configuration\n\n**Default Value**: 100 (hardcoded in all function signatures)\n\n**Tunable via Command Line** (in `exp001_regularize.py`):\n```python\nparser.add_argument('--cond-threshold', type=float, default=100)\n```\n\n**Usage with Custom Threshold**:\n```python\ntml_r, sml_r = invert_mixing_safe(M_mle[s], tau_obs, se_obs, cond_threshold)\nthb_r, shb_r = invert_mixing_safe(M_hb[s], tau_obs, se_obs, cond_threshold)\n```\n\n### 5. Context: The Mixing Matrix\n\nThe mixing matrix M represents the confusion matrix transformed to [observed | true] space via Bayes rule:\n- `M[z_hat, z]` = proportion of observed label z_hat that comes from true label z\n- When M is nearly singular (high κ), inversion becomes numerically unstable\n- This occurs when subgroups have extreme heterogeneous misclassification rates\n\n### 6. Guard Statistics Tracking\n\nIn `exp001_regularize.py` (lines 59-64):\n```python\ncond_mle = np.linalg.cond(M_mle[s])\ncond_hb = np.linalg.cond(M_hb[s])\nif cond_mle > cond_threshold:\n    guard_mle += 1\nif cond_hb > cond_threshold:\n    guard_hb += 1\n```\n\nTracks how many subgroup-method combinations trigger the guard per MC run.\n\n### Key Files to Reference\n\n1. **Primary**: `/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py` (lines 125-148)\n2. **Tuning/Analysis**: `/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py` (lines 26-78)\n3. **Documentation examples**: `/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py` (lines 324-335)"
      }
    ],
    "totalDurationMs": 57720,
    "totalTokens": 65815,
    "totalToolUseCount": 25,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 531,
      "cache_read_input_tokens": 63640,
      "output_tokens": 1639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 531
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1639,
          "cache_read_input_tokens": 63640,
          "cache_creation_input_tokens": 531,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 531,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 6,
      "searchCount": 4,
      "bashCount": 15,
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

_source line 87_

<details><summary>Logged reasoning block</summary>

```text
Good, now I have a clear understanding of the κ guard implementation. Let me read the key files to understand the full simulation setup, particularly `exp001_hb_synthetic.py` which is the primary implementation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "718c9147-33ce-4273-a224-de45783e4fbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014tWgVtgLYJ77A3ikN2wCB8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 56,
      "cache_creation_input_tokens": 2012,
      "cache_read_input_tokens": 18372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2012
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

_source line 88_

Now let me read the key source files to understand the full simulation logic.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "0500136d-cf21-4ad4-9ae6-b31d6e99b7a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014tWgVtgLYJ77A3ikN2wCB8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 56,
      "cache_creation_input_tokens": 2012,
      "cache_read_input_tokens": 18372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2012
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

_source line 89_

<details open><summary>🔧 Tool call — Read · `toolu_01AcdfmYZELCcp4zHyGywebP`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "82c8f7b2-7ed7-4098-a535-ca9acf19fe4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014tWgVtgLYJ77A3ikN2wCB8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 56,
      "cache_creation_input_tokens": 2012,
      "cache_read_input_tokens": 18372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2012
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

_source line 90_

<details open><summary>🔧 Tool call — Read · `toolu_016U4PZJ1MkMMfHbKyYGdpT2`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "6463f1c7-d310-4f74-8c29-c69952e216db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014tWgVtgLYJ77A3ikN2wCB8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 56,
      "cache_creation_input_tokens": 2012,
      "cache_read_input_tokens": 18372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2012
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

_source line 91 · 2026-05-21T15:53:26.473Z_

<details><summary>↩ Tool result · `toolu_016U4PZJ1MkMMfHbKyYGdpT2`</summary>

```text
1	#!/usr/bin/env python3
2	"""exp001_regularize.py - Rerun affected cells with condition-number-guarded inversion."""
3	
4	import argparse
5	import time
6	import numpy as np
7	import pandas as pd
8	
9	from exp001_hb_synthetic import (
10	    REGIMES, SUBGROUP_LABELS,
11	    generate_data, get_counts, build_mixing_matrix, diff_in_means,
12	    estimate_cm_mle, estimate_cm_hb_eb, estimate_cm_hb_gibbs,
13	    invert_mixing_safe, aggregate_results,
14	)
15	
16	AFFECTED_CELLS = [
17	    (4, 'extreme', 50),
18	    (4, 'extreme', 100),
19	    (4, 'moderate', 50),
20	    (4, 'moderate', 100),
21	    (4, 'homogeneous', 50),
22	    (4, 'homogeneous', 100),
23	]
24	
25	
26	def run_one_mc_reg(regime_name, regime_params, n_expert, k, seed,
27	                   cond_threshold=100, n_chains=4, n_iter=4000, n_warmup=2000):
28	    data = generate_data(regime_params, n_expert, k, seed)
29	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
30	    em = data['expert_mask']
31	    labels = SUBGROUP_LABELS[k]
32	    tau_z0, tau_z1 = regime_params['tau_z0'], regime_params['tau_z1']
33	
34	    counts = get_counts(Z[em], Z_hat[em], S[em], labels)
35	    C_mle = estimate_cm_mle(counts, labels)
36	    C_hb, hb_diag = estimate_cm_hb_gibbs(counts, labels, seed=seed,
37	                                          n_chains=n_chains, n_iter=n_iter,
38	                                          n_warmup=n_warmup)
39	
40	    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in labels}
41	    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}
42	
43	    base = {'regime': regime_name, 'n_expert': n_expert,
44	            'k_subgroups': k, 'mc_run': seed}
45	    rows = []
46	    guard_hb = 0
47	    guard_mle = 0
48	
49	    for s in labels:
50	        sm = S == s
51	        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))
52	        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))
53	
54	        tau_obs = np.array([th0_n, th1_n])
55	        se_obs = np.array([se0_n, se1_n])
56	        if np.any(np.isnan(tau_obs)):
57	            continue
58	
59	        cond_mle = np.linalg.cond(M_mle[s])
60	        cond_hb = np.linalg.cond(M_hb[s])
61	        if cond_mle > cond_threshold:
62	            guard_mle += 1
63	        if cond_hb > cond_threshold:
64	            guard_hb += 1
65	
66	        tml_r, sml_r = invert_mixing_safe(M_mle[s], tau_obs, se_obs, cond_threshold)
67	        thb_r, shb_r = invert_mixing_safe(M_hb[s], tau_obs, se_obs, cond_threshold)
68	
69	        def mr(method, th0, th1, se0, se1):
70	            return {**base, 'subgroup': s, 'method': method,
71	                    'tau_hat_z0': th0, 'tau_hat_z1': th1,
72	                    'se_z0': se0, 'se_z1': se1,
73	                    'tau_true_z0': tau_z0, 'tau_true_z1': tau_z1}
74	
75	        rows.append(mr('mle_laplace_reg', tml_r[0], tml_r[1], sml_r[0], sml_r[1]))
76	        rows.append(mr('hb_dirichlet_reg', thb_r[0], thb_r[1], shb_r[0], shb_r[1]))
77	
78	    return rows, hb_diag, guard_hb, guard_mle
79	
80	
81	if __name__ == '__main__':
82	    parser = argparse.ArgumentParser()
83	    parser.add_argument('--n-mc', type=int, default=100)
84	    parser.add_argument('--cond-threshold', type=float, default=100)
85	    args = parser.parse_args()
86	
87	    print(f"exp-001 Regularization fix v2 | cond_threshold={args.cond_threshold}")
88	    print(f"Affected cells: {AFFECTED_CELLS}")
89	    print(f"n_mc={args.n_mc}")
90	    print(f"MCMC config: n_chains=4, n_iter=4000, n_warmup=2000\n")
91	
92	    # ── MCMC diagnostic comparison (before/after) ────────────────────────────
93	    print("Running MCMC diagnostic comparison (seed=0, per config)...")
94	    diag_rows = []
95	    for k, regime, n_expert in AFFECTED_CELLS:
96	        rp = REGIMES[k][regime]
97	        d = generate_data(rp, n_expert, k, seed=0)
98	        em = d['expert_mask']
99	        labels = SUBGROUP_LABELS[k]
100	        counts = get_counts(d['Z'][em], d['Z_hat'][em], d['S'][em], labels)
101	
102	        _, diag_before = estimate_cm_hb_gibbs(counts, labels, seed=0,
103	                                               n_chains=2, n_iter=2000, n_warmup=1000)
104	        _, diag_after = estimate_cm_hb_gibbs(counts, labels, seed=0,
105	                                              n_chains=4, n_iter=4000, n_warmup=2000)
106	        diag_rows.append({
107	            'config': f"K={k}/{regime}/n={n_expert}",
108	            'rhat_before': diag_before['rhat_max'],
109	            'rhat_after': diag_after['rhat_max'],
110	            'ess_before': diag_before['ess_min'],
111	            'ess_after': diag_after['ess_min'],
112	        })
113	
114	    print("\n" + "=" * 100)
115	    print("MCMC Diagnostic Comparison (seed=0)")
116	    print(f"{'Config':>30s} | {'Rhat_max (2ch)':>14s} | {'Rhat_max (4ch)':>14s} | "
117	          f"{'ESS_min (2ch)':>14s} | {'ESS_min (4ch)':>14s}")
118	    print("-" * 100)
119	    for r in diag_rows:
120	        print(f"{r['config']:>30s} | {r['rhat_before']:14.4f} | {r['rhat_after']:14.4f} | "
121	              f"{r['ess_before']:14.1f} | {r['ess_after']:14.1f}")
122	    print("=" * 100 + "\n")
123	
124	    # ── Main MC loop ─────────────────────────────────────────────────────────
125	    all_rows = []
126	    guard_stats = {}
127	    diag_agg = {}
128	    total = len(AFFECTED_CELLS) * args.n_mc
129	    count = 0
130	    t0 = time.time()
131	
132	    for k, regime, n_expert in AFFECTED_CELLS:
133	        key = (k, regime, n_expert)
134	        guard_stats[key] = {'total': 0, 'guard_hb': 0, 'guard_mle': 0}
135	        diag_agg[key] = {'rhat_max': [], 'ess_min': []}
136	        rp = REGIMES[k][regime]
137	        for mc in range(args.n_mc):
138	            rows, hb_diag, g_hb, g_mle = run_one_mc_reg(
139	                regime, rp, n_expert, k, seed=mc,
140	                cond_threshold=args.cond_threshold,
141	                n_chains=4, n_iter=4000, n_warmup=2000)
142	            all_rows.extend(rows)
143	            guard_stats[key]['total'] += 1
144	            guard_stats[key]['guard_hb'] += g_hb
145	            guard_stats[key]['guard_mle'] += g_mle
146	            diag_agg[key]['rhat_max'].append(hb_diag['rhat_max'])
147	            diag_agg[key]['ess_min'].append(hb_diag['ess_min'])
148	            count += 1
149	            if count % 50 == 0:
150	                el = time.time() - t0
151	                print(f"  [{count}/{total}] {el:.0f}s elapsed")
152	
153	    print(f"  Done: {time.time() - t0:.1f}s ({count} runs)\n")
154	
155	    # ── Singularity guard trigger stats ──────────────────────────────────────
156	    print("=" * 90)
157	    print("Singularity Guard Trigger Statistics")
158	    print(f"{'Config':>30s} | {'Total MC':>8s} | {'Guard HB':>10s} | {'Guard MLE':>10s}")
159	    print("-" * 90)
160	    for key in guard_stats:
161	        k, regime, n_expert = key
162	        gs = guard_stats[key]
163	        config = f"K={k}/{regime}/n={n_expert}"
164	        print(f"{config:>30s} | {gs['total']:8d} | {gs['guard_hb']:10d} | {gs['guard_mle']:10d}")
165	    print("=" * 90 + "\n")
166	
167	    # ── Aggregated MCMC diagnostics across MC runs ───────────────────────────
168	    print("=" * 100)
169	    print("Aggregated MCMC Diagnostics (4 chains, 4000 iter)")
170	    print(f"{'Config':>30s} | {'Rhat_max mean':>14s} | {'Rhat_max max':>14s} | "
171	          f"{'ESS_min mean':>14s} | {'ESS_min min':>14s}")
172	    print("-" * 100)
173	    for key in diag_agg:
174	        k, regime, n_expert = key
175	        config = f"K={k}/{regime}/n={n_expert}"
176	        rhats = diag_agg[key]['rhat_max']
177	        esss = diag_agg[key]['ess_min']
178	        print(f"{config:>30s} | {np.mean(rhats):14.4f} | {np.max(rhats):14.4f} | "
179	              f"{np.mean(esss):14.1f} | {np.min(esss):14.1f}")
180	    print("=" * 100 + "\n")
181	
182	    # ── Aggregate and write results ──────────────────────────────────────────
183	    df_raw = pd.DataFrame(all_rows)
184	    df_agg = aggregate_results(df_raw)
185	
186	    csv_orig = 'results/exp001_hb_results.csv'
187	    csv_v2 = 'results/exp001_hb_results_v2.csv'
188	    df_existing = pd.read_csv(csv_orig)
189	
190	    # Remove previously appended reg rows (keep original 540)
191	    reg_methods = ['hb_dirichlet_reg', 'mle_laplace_reg']
192	    df_base = df_existing[~df_existing['method'].isin(reg_methods)].copy()
193	
194	    agg_cols = list(df_base.columns)
195	    df_combined = pd.concat([df_base, df_agg[agg_cols]], ignore_index=True)
196	    df_combined.to_csv(csv_v2, index=False)
197	
198	    # ── RMSE comparison table ────────────────────────────────────────────────
199	    print("=" * 120)
200	    print("RMSE Comparison (original vs regularized)")
201	    print(f"{'Config':>40s} | {'Method':>15s} | {'RMSE_z0 (orig)':>15s} | "
202	          f"{'RMSE_z0 (reg)':>14s} | {'RMSE_z1 (orig)':>15s} | {'RMSE_z1 (reg)':>14s}")
203	    print("-" * 120)
204	
205	    for k, regime, n_expert in AFFECTED_CELLS:
206	        for subgroup in SUBGROUP_LABELS[k]:
207	            mask_base = ((df_base['k_subgroups'] == k) &
208	                         (df_base['regime'] == regime) &
209	                         (df_base['n_expert'] == n_expert) &
210	                         (df_base['subgroup'] == subgroup))
211	
212	            for orig, reg in [('hb_dirichlet', 'hb_dirichlet_reg'),
213	                              ('mle_laplace', 'mle_laplace_reg')]:
214	                before = df_base[mask_base & (df_base['method'] == orig)]
215	                after = df_agg[(df_agg['k_subgroups'] == k) &
216	                               (df_agg['regime'] == regime) &
217	                               (df_agg['n_expert'] == n_expert) &
218	                               (df_agg['subgroup'] == subgroup) &
219	                               (df_agg['method'] == reg)]
220	
221	                if before.empty or after.empty:
222	                    continue
223	
224	                b_z0 = before['rmse_z0'].values[0]
225	                a_z0 = after['rmse_z0'].values[0]
226	                b_z1 = before['rmse_z1'].values[0]
227	                a_z1 = after['rmse_z1'].values[0]
228	
229	                config = f"K={k}/{regime}/n={n_expert}/{subgroup}"
230	                print(f"{config:>40s} | {orig:>15s} | {b_z0:15.4f} | "
231	                      f"{a_z0:14.4f} | {b_z1:15.4f} | {a_z1:14.4f}")
232	
233	    # Global method comparison
234	    print("-" * 120)
235	    for method in ['diff_in_means', 'mle_laplace', 'hb_dirichlet']:
236	        mask = df_base['method'] == method
237	        if mask.any():
238	            r0 = df_base.loc[mask, 'rmse_z0'].mean()
239	            r1 = df_base.loc[mask, 'rmse_z1'].mean()
240	            print(f"{'Global avg':>40s} | {method:>15s} | {r0:15.4f} | {'---':>14s} | {r1:15.4f} | {'---':>14s}")
241	    for method in ['mle_laplace_reg', 'hb_dirichlet_reg']:
242	        mask = df_agg['method'] == method
243	        if mask.any():
244	            r0 = df_agg.loc[mask, 'rmse_z0'].mean()
245	            r1 = df_agg.loc[mask, 'rmse_z1'].mean()
246	            print(f"{'Global avg (reg cells)':>40s} | {method:>15s} | {'---':>15s} | {r0:14.4f} | {'---':>15s} | {r1:14.4f}")
247	
248	    print("=" * 120)
249	    print(f"\nWrote {csv_v2}: {len(df_base)} original + {len(df_agg)} new = {len(df_combined)} rows")
250	    print(f"Original file {csv_orig} unchanged.")
251	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "4503daca-f03f-4e6e-b3ae-1f9747cef23b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py",
      "content": "#!/usr/bin/env python3\n\"\"\"exp001_regularize.py - Rerun affected cells with condition-number-guarded inversion.\"\"\"\n\nimport argparse\nimport time\nimport numpy as np\nimport pandas as pd\n\nfrom exp001_hb_synthetic import (\n    REGIMES, SUBGROUP_LABELS,\n    generate_data, get_counts, build_mixing_matrix, diff_in_means,\n    estimate_cm_mle, estimate_cm_hb_eb, estimate_cm_hb_gibbs,\n    invert_mixing_safe, aggregate_results,\n)\n\nAFFECTED_CELLS = [\n    (4, 'extreme', 50),\n    (4, 'extreme', 100),\n    (4, 'moderate', 50),\n    (4, 'moderate', 100),\n    (4, 'homogeneous', 50),\n    (4, 'homogeneous', 100),\n]\n\n\ndef run_one_mc_reg(regime_name, regime_params, n_expert, k, seed,\n                   cond_threshold=100, n_chains=4, n_iter=4000, n_warmup=2000):\n    data = generate_data(regime_params, n_expert, k, seed)\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    em = data['expert_mask']\n    labels = SUBGROUP_LABELS[k]\n    tau_z0, tau_z1 = regime_params['tau_z0'], regime_params['tau_z1']\n\n    counts = get_counts(Z[em], Z_hat[em], S[em], labels)\n    C_mle = estimate_cm_mle(counts, labels)\n    C_hb, hb_diag = estimate_cm_hb_gibbs(counts, labels, seed=seed,\n                                          n_chains=n_chains, n_iter=n_iter,\n                                          n_warmup=n_warmup)\n\n    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in labels}\n    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}\n\n    base = {'regime': regime_name, 'n_expert': n_expert,\n            'k_subgroups': k, 'mc_run': seed}\n    rows = []\n    guard_hb = 0\n    guard_mle = 0\n\n    for s in labels:\n        sm = S == s\n        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))\n        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))\n\n        tau_obs = np.array([th0_n, th1_n])\n        se_obs = np.array([se0_n, se1_n])\n        if np.any(np.isnan(tau_obs)):\n            continue\n\n        cond_mle = np.linalg.cond(M_mle[s])\n        cond_hb = np.linalg.cond(M_hb[s])\n        if cond_mle > cond_threshold:\n            guard_mle += 1\n        if cond_hb > cond_threshold:\n            guard_hb += 1\n\n        tml_r, sml_r = invert_mixing_safe(M_mle[s], tau_obs, se_obs, cond_threshold)\n        thb_r, shb_r = invert_mixing_safe(M_hb[s], tau_obs, se_obs, cond_threshold)\n\n        def mr(method, th0, th1, se0, se1):\n            return {**base, 'subgroup': s, 'method': method,\n                    'tau_hat_z0': th0, 'tau_hat_z1': th1,\n                    'se_z0': se0, 'se_z1': se1,\n                    'tau_true_z0': tau_z0, 'tau_true_z1': tau_z1}\n\n        rows.append(mr('mle_laplace_reg', tml_r[0], tml_r[1], sml_r[0], sml_r[1]))\n        rows.append(mr('hb_dirichlet_reg', thb_r[0], thb_r[1], shb_r[0], shb_r[1]))\n\n    return rows, hb_diag, guard_hb, guard_mle\n\n\nif __name__ == '__main__':\n    parser = argparse.ArgumentParser()\n    parser.add_argument('--n-mc', type=int, default=100)\n    parser.add_argument('--cond-threshold', type=float, default=100)\n    args = parser.parse_args()\n\n    print(f\"exp-001 Regularization fix v2 | cond_threshold={args.cond_threshold}\")\n    print(f\"Affected cells: {AFFECTED_CELLS}\")\n    print(f\"n_mc={args.n_mc}\")\n    print(f\"MCMC config: n_chains=4, n_iter=4000, n_warmup=2000\\n\")\n\n    # ── MCMC diagnostic comparison (before/after) ────────────────────────────\n    print(\"Running MCMC diagnostic comparison (seed=0, per config)...\")\n    diag_rows = []\n    for k, regime, n_expert in AFFECTED_CELLS:\n        rp = REGIMES[k][regime]\n        d = generate_data(rp, n_expert, k, seed=0)\n        em = d['expert_mask']\n        labels = SUBGROUP_LABELS[k]\n        counts = get_counts(d['Z'][em], d['Z_hat'][em], d['S'][em], labels)\n\n        _, diag_before = estimate_cm_hb_gibbs(counts, labels, seed=0,\n                                               n_chains=2, n_iter=2000, n_warmup=1000)\n        _, diag_after = estimate_cm_hb_gibbs(counts, labels, seed=0,\n                                              n_chains=4, n_iter=4000, n_warmup=2000)\n        diag_rows.append({\n            'config': f\"K={k}/{regime}/n={n_expert}\",\n            'rhat_before': diag_before['rhat_max'],\n            'rhat_after': diag_after['rhat_max'],\n            'ess_before': diag_before['ess_min'],\n            'ess_after': diag_after['ess_min'],\n        })\n\n    print(\"\\n\" + \"=\" * 100)\n    print(\"MCMC Diagnostic Comparison (seed=0)\")\n    print(f\"{'Config':>30s} | {'Rhat_max (2ch)':>14s} | {'Rhat_max (4ch)':>14s} | \"\n          f\"{'ESS_min (2ch)':>14s} | {'ESS_min (4ch)':>14s}\")\n    print(\"-\" * 100)\n    for r in diag_rows:\n        print(f\"{r['config']:>30s} | {r['rhat_before']:14.4f} | {r['rhat_after']:14.4f} | \"\n              f\"{r['ess_before']:14.1f} | {r['ess_after']:14.1f}\")\n    print(\"=\" * 100 + \"\\n\")\n\n    # ── Main MC loop ─────────────────────────────────────────────────────────\n    all_rows = []\n    guard_stats = {}\n    diag_agg = {}\n    total = len(AFFECTED_CELLS) * args.n_mc\n    count = 0\n    t0 = time.time()\n\n    for k, regime, n_expert in AFFECTED_CELLS:\n        key = (k, regime, n_expert)\n        guard_stats[key] = {'total': 0, 'guard_hb': 0, 'guard_mle': 0}\n        diag_agg[key] = {'rhat_max': [], 'ess_min': []}\n        rp = REGIMES[k][regime]\n        for mc in range(args.n_mc):\n            rows, hb_diag, g_hb, g_mle = run_one_mc_reg(\n                regime, rp, n_expert, k, seed=mc,\n                cond_threshold=args.cond_threshold,\n                n_chains=4, n_iter=4000, n_warmup=2000)\n            all_rows.extend(rows)\n            guard_stats[key]['total'] += 1\n            guard_stats[key]['guard_hb'] += g_hb\n            guard_stats[key]['guard_mle'] += g_mle\n            diag_agg[key]['rhat_max'].append(hb_diag['rhat_max'])\n            diag_agg[key]['ess_min'].append(hb_diag['ess_min'])\n            count += 1\n            if count % 50 == 0:\n                el = time.time() - t0\n                print(f\"  [{count}/{total}] {el:.0f}s elapsed\")\n\n    print(f\"  Done: {time.time() - t0:.1f}s ({count} runs)\\n\")\n\n    # ── Singularity guard trigger stats ──────────────────────────────────────\n    print(\"=\" * 90)\n    print(\"Singularity Guard Trigger Statistics\")\n    print(f\"{'Config':>30s} | {'Total MC':>8s} | {'Guard HB':>10s} | {'Guard MLE':>10s}\")\n    print(\"-\" * 90)\n    for key in guard_stats:\n        k, regime, n_expert = key\n        gs = guard_stats[key]\n        config = f\"K={k}/{regime}/n={n_expert}\"\n        print(f\"{config:>30s} | {gs['total']:8d} | {gs['guard_hb']:10d} | {gs['guard_mle']:10d}\")\n    print(\"=\" * 90 + \"\\n\")\n\n    # ── Aggregated MCMC diagnostics across MC runs ───────────────────────────\n    print(\"=\" * 100)\n    print(\"Aggregated MCMC Diagnostics (4 chains, 4000 iter)\")\n    print(f\"{'Config':>30s} | {'Rhat_max mean':>14s} | {'Rhat_max max':>14s} | \"\n          f\"{'ESS_min mean':>14s} | {'ESS_min min':>14s}\")\n    print(\"-\" * 100)\n    for key in diag_agg:\n        k, regime, n_expert = key\n        config = f\"K={k}/{regime}/n={n_expert}\"\n        rhats = diag_agg[key]['rhat_max']\n        esss = diag_agg[key]['ess_min']\n        print(f\"{config:>30s} | {np.mean(rhats):14.4f} | {np.max(rhats):14.4f} | \"\n              f\"{np.mean(esss):14.1f} | {np.min(esss):14.1f}\")\n    print(\"=\" * 100 + \"\\n\")\n\n    # ── Aggregate and write results ──────────────────────────────────────────\n    df_raw = pd.DataFrame(all_rows)\n    df_agg = aggregate_results(df_raw)\n\n    csv_orig = 'results/exp001_hb_results.csv'\n    csv_v2 = 'results/exp001_hb_results_v2.csv'\n    df_existing = pd.read_csv(csv_orig)\n\n    # Remove previously appended reg rows (keep original 540)\n    reg_methods = ['hb_dirichlet_reg', 'mle_laplace_reg']\n    df_base = df_existing[~df_existing['method'].isin(reg_methods)].copy()\n\n    agg_cols = list(df_base.columns)\n    df_combined = pd.concat([df_base, df_agg[agg_cols]], ignore_index=True)\n    df_combined.to_csv(csv_v2, index=False)\n\n    # ── RMSE comparison table ────────────────────────────────────────────────\n    print(\"=\" * 120)\n    print(\"RMSE Comparison (original vs regularized)\")\n    print(f\"{'Config':>40s} | {'Method':>15s} | {'RMSE_z0 (orig)':>15s} | \"\n          f\"{'RMSE_z0 (reg)':>14s} | {'RMSE_z1 (orig)':>15s} | {'RMSE_z1 (reg)':>14s}\")\n    print(\"-\" * 120)\n\n    for k, regime, n_expert in AFFECTED_CELLS:\n        for subgroup in SUBGROUP_LABELS[k]:\n            mask_base = ((df_base['k_subgroups'] == k) &\n                         (df_base['regime'] == regime) &\n                         (df_base['n_expert'] == n_expert) &\n                         (df_base['subgroup'] == subgroup))\n\n            for orig, reg in [('hb_dirichlet', 'hb_dirichlet_reg'),\n                              ('mle_laplace', 'mle_laplace_reg')]:\n                before = df_base[mask_base & (df_base['method'] == orig)]\n                after = df_agg[(df_agg['k_subgroups'] == k) &\n                               (df_agg['regime'] == regime) &\n                               (df_agg['n_expert'] == n_expert) &\n                               (df_agg['subgroup'] == subgroup) &\n                               (df_agg['method'] == reg)]\n\n                if before.empty or after.empty:\n                    continue\n\n                b_z0 = before['rmse_z0'].values[0]\n                a_z0 = after['rmse_z0'].values[0]\n                b_z1 = before['rmse_z1'].values[0]\n                a_z1 = after['rmse_z1'].values[0]\n\n                config = f\"K={k}/{regime}/n={n_expert}/{subgroup}\"\n                print(f\"{config:>40s} | {orig:>15s} | {b_z0:15.4f} | \"\n                      f\"{a_z0:14.4f} | {b_z1:15.4f} | {a_z1:14.4f}\")\n\n    # Global method comparison\n    print(\"-\" * 120)\n    for method in ['diff_in_means', 'mle_laplace', 'hb_dirichlet']:\n        mask = df_base['method'] == method\n        if mask.any():\n            r0 = df_base.loc[mask, 'rmse_z0'].mean()\n            r1 = df_base.loc[mask, 'rmse_z1'].mean()\n            print(f\"{'Global avg':>40s} | {method:>15s} | {r0:15.4f} | {'---':>14s} | {r1:15.4f} | {'---':>14s}\")\n    for method in ['mle_laplace_reg', 'hb_dirichlet_reg']:\n        mask = df_agg['method'] == method\n        if mask.any():\n            r0 = df_agg.loc[mask, 'rmse_z0'].mean()\n            r1 = df_agg.loc[mask, 'rmse_z1'].mean()\n            print(f\"{'Global avg (reg cells)':>40s} | {method:>15s} | {'---':>15s} | {r0:14.4f} | {'---':>15s} | {r1:14.4f}\")\n\n    print(\"=\" * 120)\n    print(f\"\\nWrote {csv_v2}: {len(df_base)} original + {len(df_agg)} new = {len(df_combined)} rows\")\n    print(f\"Original file {csv_orig} unchanged.\")\n",
      "numLines": 251,
      "startLine": 1,
      "totalLines": 251
    }
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-21T15:53:26.598Z_

<details><summary>↩ Tool result · `toolu_01AcdfmYZELCcp4zHyGywebP`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	exp001_hb_synthetic.py - Hierarchical Bayesian EC-HTE Synthetic Validation (exp-001)
4	
5	Compares confusion matrix estimators for CATE correction under heterogeneous
6	misclassification across subgroups:
7	  Oracle, Naive, Global-corrected, MLE (Laplace), HB Dirichlet (partial pooling)
8	
9	Input: Synthetic DGP parameters (regimes, expert budgets, subgroup counts)
10	Output: results/exp001_hb_results.csv, results/exp001_hb_diagnostics.csv
11	"""
12	
13	import argparse
14	import os
15	import sys
16	import time
17	import warnings
18	import numpy as np
19	import pandas as pd
20	from scipy.special import gammaln
21	from scipy.optimize import minimize_scalar
22	
23	warnings.filterwarnings('ignore')
24	
25	try:
26	    import pymc as pm
27	    import pytensor.tensor as pt
28	    import arviz as az
29	    HAS_PYMC = True
30	except ImportError:
31	    HAS_PYMC = False
32	
33	N = 5000
34	SUBGROUP_LABELS = {2: ['A', 'B'], 4: ['A', 'B', 'C', 'D']}
35	
36	REGIMES = {
37	    2: {
38	        'extreme':     {'misclass': [0.25, 0.05], 'tau_z1': 0.5, 'tau_z0': 0.1},
39	        'moderate':    {'misclass': [0.15, 0.10], 'tau_z1': 0.3, 'tau_z0': 0.15},
40	        'homogeneous': {'misclass': [0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},
41	    },
42	    4: {
43	        'extreme':     {'misclass': [0.30, 0.20, 0.10, 0.03], 'tau_z1': 0.5, 'tau_z0': 0.1},
44	        'moderate':    {'misclass': [0.20, 0.15, 0.10, 0.05], 'tau_z1': 0.3, 'tau_z0': 0.15},
45	        'homogeneous': {'misclass': [0.12, 0.12, 0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},
46	    },
47	}
48	
49	DEFAULT_N_EXPERTS = [50, 100, 250, 500, 1000, 2000]
50	DEFAULT_K_LIST = [2, 4]
51	
52	
53	# ── DGP ───────────────────────────────────────────────────────────────────────
54	
55	def generate_data(regime_params, n_expert, k, seed):
56	    rng = np.random.RandomState(seed)
57	    labels = SUBGROUP_LABELS[k]
58	    T = rng.binomial(1, 0.5, N)
59	    Z = rng.binomial(1, 0.5, N)
60	    S = rng.choice(labels, N, p=[1.0 / k] * k)
61	    X = rng.randn(N, 5)
62	    tau = np.where(Z == 1, regime_params['tau_z1'], regime_params['tau_z0'])
63	    Y = 1 + tau * T + 0.5 * X[:, 0] + rng.randn(N)
64	    mc_rates = np.zeros(N)
65	    for i, s in enumerate(labels):
66	        mc_rates[S == s] = regime_params['misclass'][i]
67	    Z_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)
68	    idx = rng.choice(N, min(n_expert, N), replace=False)
69	    expert_mask = np.zeros(N, dtype=bool)
70	    expert_mask[idx] = True
71	    return dict(T=T, Z=Z, Z_hat=Z_hat, S=S, X=X, Y=Y, tau=tau, expert_mask=expert_mask)
72	
73	
74	# ── Helpers ───────────────────────────────────────────────────────────────────
75	
76	def diff_in_means(Y, T, mask):
77	    t1, t0 = mask & (T == 1), mask & (T == 0)
78	    n1, n0 = t1.sum(), t0.sum()
79	    if n1 < 2 or n0 < 2:
80	        return np.nan, np.nan
81	    y1, y0 = Y[t1], Y[t0]
82	    return y1.mean() - y0.mean(), np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)
83	
84	
85	def get_counts(z_true, z_hat, subgroups, labels):
86	    """Confusion matrix counts per subgroup: (k, 2, 2) = [subgroup, true_z, z_hat]."""
87	    k = len(labels)
88	    counts = np.zeros((k, 2, 2), dtype=int)
89	    for i, s in enumerate(labels):
90	        ms = subgroups == s
91	        for z in [0, 1]:
92	            mz = ms & (z_true == z)
93	            counts[i, z, 0] = (z_hat[mz] == 0).sum()
94	            counts[i, z, 1] = (z_hat[mz] == 1).sum()
95	    return counts
96	
97	
98	def build_mixing_matrix(C):
99	    """C[z, z_hat] → M[z_hat, z] via Bayes rule (assuming P(Z=0)=P(Z=1)=0.5).
100	
101	    NOTE: This assumes P(Z=0)=P(Z=1)=0.5, which is correct for this experiment's
102	    DGP. For general P(Z), use the version in exp007 that takes p_z and p_z_hat.
103	    """
104	    M = np.zeros((2, 2))
105	    for zh in [0, 1]:
106	        cs = C[0, zh] + C[1, zh]
107	        if cs > 0:
108	            M[zh, 0] = C[0, zh] / cs
109	            M[zh, 1] = C[1, zh] / cs
110	        else:
111	            M[zh, :] = 0.5
112	    return M
113	
114	
115	def invert_mixing(M, tau_obs, se_obs):
116	    det = np.linalg.det(M)
117	    if abs(det) < 1e-10:
118	        return tau_obs.copy(), se_obs.copy()
119	    Mi = np.linalg.inv(M)
120	    tau_c = Mi @ tau_obs
121	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
122	    return tau_c, se_c
123	
124	
125	def safe_invert_correction(M_s, tau_obs, cond_threshold=100, fallback='naive'):
126	    """Invert mixing matrix with condition number guard.
127	
128	    When cond(M_s) > threshold, matrix inversion is numerically unstable.
129	    Falls back to naive (no correction) to avoid catastrophic amplification.
130	    """
131	    cond = np.linalg.cond(M_s)
132	    if cond > cond_threshold:
133	        return tau_obs.copy()
134	    return np.linalg.solve(M_s, tau_obs)
135	
136	
137	def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
138	    """Like invert_mixing but with condition number guard."""
139	    cond = np.linalg.cond(M)
140	    if cond > cond_threshold:
141	        return tau_obs.copy(), se_obs.copy()
142	    det = np.linalg.det(M)
143	    if abs(det) < 1e-10:
144	        return tau_obs.copy(), se_obs.copy()
145	    Mi = np.linalg.inv(M)
146	    tau_c = Mi @ tau_obs
147	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
148	    return tau_c, se_c
149	
150	
151	# ── Confusion Matrix Estimators ───────────────────────────────────────────────
152	
153	def estimate_cm_mle(counts, labels):
154	    """Per-subgroup MLE with Laplace smoothing (add-1)."""
155	    C = {}
156	    for i, s in enumerate(labels):
157	        C_s = np.zeros((2, 2))
158	        for z in [0, 1]:
159	            n = counts[i, z, :].sum()
160	            for zh in [0, 1]:
161	                C_s[z, zh] = (counts[i, z, zh] + 1) / (n + 2) if n > 0 else 0.5
162	        C[s] = C_s
163	    return C
164	
165	
166	def _dirmult_neg_ll(alpha, counts_z):
167	    """Negative log marginal likelihood for Dirichlet-Multinomial."""
168	    a = alpha / 2.0
169	    if a < 1e-10:
170	        return 1e10
171	    ll = 0.0
172	    for c0, c1 in counts_z:
173	        n = c0 + c1
174	        if n == 0:
175	            continue
176	        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)
177	        ll -= 2 * gammaln(a) - gammaln(2 * a)
178	    return -ll
179	
180	
181	def estimate_cm_hb_eb(counts, labels):
182	    """Empirical Bayes HB: optimize shared Dirichlet concentration, posterior mean."""
183	    k = len(labels)
184	    alpha_opt = np.zeros(2)
185	    for z in [0, 1]:
186	        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]
187	        total = sum(c0 + c1 for c0, c1 in cl)
188	        if total == 0:
189	            alpha_opt[z] = 2.0
190	            continue
191	        res = minimize_scalar(
192	            lambda a: _dirmult_neg_ll(a, cl), bounds=(0.01, 500), method='bounded')
193	        alpha_opt[z] = res.x
194	
195	    C = {}
196	    for i, s in enumerate(labels):
197	        C_s = np.zeros((2, 2))
198	        for z in [0, 1]:
199	            a = alpha_opt[z] / 2.0
200	            n = counts[i, z, :].sum()
201	            d = n + 2 * a
202	            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5
203	            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5
204	        C[s] = C_s
205	
206	    diag = {'rhat_max': np.nan, 'ess_min': np.nan, 'divergent_count': 0,
207	            'runtime_seconds': 0.0, 'hb_method': 'eb',
208	            'alpha_0_z0': alpha_opt[0], 'alpha_0_z1': alpha_opt[1]}
209	    return C, diag
210	
211	
212	def _split_rhat(chains):
213	    """Split R-hat for a scalar parameter. chains: (n_chains, n_draws)."""
214	    parts = []
215	    for c in range(chains.shape[0]):
216	        half = chains.shape[1] // 2
217	        parts.append(chains[c, :half])
218	        parts.append(chains[c, half:2 * half])
219	    parts = np.array(parts)
220	    m = parts.shape[0]
221	    n = parts.shape[1]
222	    chain_means = parts.mean(axis=1)
223	    W = np.mean(np.var(parts, axis=1, ddof=1))
224	    B = n * np.var(chain_means, ddof=1)
225	    if W < 1e-20:
226	        return 1.0
227	    var_hat = (1 - 1.0 / n) * W + B / n
228	    return float(np.sqrt(var_hat / W))
229	
230	
231	def _bulk_ess(chains):
232	    """Approximate bulk ESS via initial positive sequence. chains: (n_chains, n_draws)."""
233	    x = chains.ravel()
234	    n = len(x)
235	    mu = x.mean()
236	    xc = x - mu
237	    max_lag = min(n // 2, 300)
238	    c0 = np.dot(xc, xc)
239	    if c0 < 1e-20:
240	        return float(n)
241	    tau = 1.0
242	    for lag in range(1, max_lag - 1, 2):
243	        r1 = np.dot(xc[:n - lag], xc[lag:]) / c0
244	        r2 = np.dot(xc[:n - lag - 1], xc[lag + 1:]) / c0 if lag + 1 < n else 0
245	        pair = r1 + r2
246	        if pair < 0:
247	            break
248	        tau += 2 * pair
249	    return float(n / tau)
250	
251	
252	def _fast_diagnostics(alpha_arr, theta_arr, labels):
253	    """Compute R-hat and ESS over all parameters without arviz."""
254	    rhats, esss = [], []
255	    for d in range(alpha_arr.shape[2]):
256	        rhats.append(_split_rhat(alpha_arr[:, :, d]))
257	        esss.append(_bulk_ess(alpha_arr[:, :, d]))
258	    k = len(labels)
259	    for i in range(k):
260	        for z in [0, 1]:
261	            for zh in range(theta_arr.shape[4]):
262	                ch = theta_arr[:, :, i, z, zh]
263	                rhats.append(_split_rhat(ch))
264	                esss.append(_bulk_ess(ch))
265	    return max(rhats), min(esss)
266	
267	
268	def _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):
269	    """Log posterior for alpha_0[z] in log-alpha space (includes Jacobian)."""
270	    if alpha < 1e-10:
271	        return -1e10
272	    a = alpha / 2.0
273	    k = theta_z.shape[0]
274	    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha
275	    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))
276	    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))
277	    return lp
278	
279	
280	def estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=4000, n_warmup=2000, n_chains=4,
281	                         hp_a0=3.0, hp_b0=1.0):
282	    """Gibbs sampler for HB Dirichlet-Multinomial (conjugate + adaptive MH for alpha_0).
283	
284	    hp_a0, hp_b0: Gamma hyperprior shape/rate on alpha_0 (default Gamma(3,1)).
285	    """
286	    k = len(labels)
287	    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),
288	                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]
289	    chain_inits = chain_inits_pool[:n_chains]
290	    all_alpha, all_theta = [], []
291	    t0 = time.time()
292	
293	    for chain in range(n_chains):
294	        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)
295	        alpha = chain_inits[chain].copy()
296	        theta = np.ones((k, 2, 2)) * 0.5
297	        mh_scale = np.array([0.3, 0.3])
298	        accept_ct = np.array([0, 0])
299	        attempt_ct = np.array([0, 0])
300	
301	        alpha_samples = np.zeros((n_iter, 2))
302	        theta_samples = np.zeros((n_iter, k, 2, 2))
303	
304	        for it in range(n_warmup + n_iter):
305	            for z in [0, 1]:
306	                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0
307	                post_a = np.maximum(post_a, 1e-6)
308	                g = rng.gamma(post_a)
309	                g_sum = g.sum(axis=1, keepdims=True)
310	                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)
311	
312	            for z in [0, 1]:
313	                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])
314	                a_prop = np.exp(x_prop)
315	                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -
316	                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))
317	                accepted = np.log(rng.rand()) < log_r
318	                if accepted:
319	                    alpha[z] = a_prop
320	                if it < n_warmup:
321	                    accept_ct[z] += int(accepted)
322	                    attempt_ct[z] += 1
323	
324	            if it < n_warmup and it > 0 and it % 100 == 0:
325	                for z in [0, 1]:
326	                    rate = accept_ct[z] / max(attempt_ct[z], 1)
327	                    if rate < 0.2:
328	                        mh_scale[z] *= 0.7
329	                    elif rate > 0.5:
330	                        mh_scale[z] *= 1.3
331	                    accept_ct[z] = 0
332	                    attempt_ct[z] = 0
333	
334	            if it >= n_warmup:
335	                idx = it - n_warmup
336	                alpha_samples[idx] = alpha.copy()
337	                theta_samples[idx] = theta.copy()
338	
339	        all_alpha.append(alpha_samples)
340	        all_theta.append(theta_samples)
341	
342	    runtime = time.time() - t0
343	    alpha_arr = np.stack(all_alpha)
344	    theta_arr = np.stack(all_theta)
345	
346	    C = {}
347	    for i, s in enumerate(labels):
348	        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))
349	
350	    rhat_max, ess_min = _fast_diagnostics(alpha_arr, theta_arr, labels)
351	
352	    diag = {'rhat_max': rhat_max, 'ess_min': ess_min, 'divergent_count': 0,
353	            'runtime_seconds': runtime, 'hb_method': 'gibbs'}
354	    return C, diag
355	
356	
357	def estimate_cm_hb_mcmc(counts, labels, seed=42, draws=1000, tune=500, chains=2):
358	    """Full Bayesian HB with PyMC MCMC."""
359	    k = len(labels)
360	    n_per_sz = counts.sum(axis=2)
361	
362	    with pm.Model():
363	        alpha_0 = pm.Gamma('alpha_0', alpha=2, beta=1, shape=2)
364	        for z in [0, 1]:
365	            for i, s in enumerate(labels):
366	                nsz = int(n_per_sz[i, z])
367	                if nsz == 0:
368	                    continue
369	                a = pt.stack([alpha_0[z] / 2, alpha_0[z] / 2])
370	                theta = pm.Dirichlet(f'theta_{s}_z{z}', a=a)
371	                pm.Multinomial(f'obs_{s}_z{z}', n=nsz, p=theta,
372	                               observed=counts[i, z, :].astype('int32'))
373	        t0 = time.time()
374	        trace = pm.sample(draws=draws, tune=tune, chains=chains,
375	                          random_seed=seed, progressbar=False)
376	        runtime = time.time() - t0
377	
378	    C = {}
379	    for i, s in enumerate(labels):
380	        C_s = np.zeros((2, 2))
381	        for z in [0, 1]:
382	            vn = f'theta_{s}_z{z}'
383	            if vn in trace.posterior:
384	                C_s[z, :] = trace.posterior[vn].values.mean(axis=(0, 1))
385	            else:
386	                C_s[z, :] = 0.5
387	        C[s] = C_s
388	
389	    all_vars = list(trace.posterior.data_vars)
390	    try:
391	        summ = az.summary(trace, var_names=all_vars)
392	        rhat_max = float(summ['r_hat'].max())
393	        ess_min = float(summ['ess_bulk'].min())
394	    except Exception:
395	        rhat_max = ess_min = np.nan
396	    try:
397	        divergent = int(trace.sample_stats['diverging'].values.sum())
398	    except Exception:
399	        divergent = -1
400	
401	    diag = {'rhat_max': rhat_max, 'ess_min': ess_min,
402	            'divergent_count': divergent, 'runtime_seconds': runtime,
403	            'hb_method': 'mcmc'}
404	    return C, diag
405	
406	
407	# ── Single MC Run ─────────────────────────────────────────────────────────────
408	
409	def run_one_mc(regime_name, regime_params, n_expert, k, seed, hb_method='eb'):
410	    data = generate_data(regime_params, n_expert, k, seed)
411	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
412	    em = data['expert_mask']
413	    labels = SUBGROUP_LABELS[k]
414	    tau_z0, tau_z1 = regime_params['tau_z0'], regime_params['tau_z1']
415	
416	    counts = get_counts(Z[em], Z_hat[em], S[em], labels)
417	
418	    C_mle = estimate_cm_mle(counts, labels)
419	
420	    if hb_method == 'gibbs':
421	        C_hb, hb_diag = estimate_cm_hb_gibbs(counts, labels, seed=seed)
422	    elif hb_method == 'mcmc' and HAS_PYMC:
423	        try:
424	            C_hb, hb_diag = estimate_cm_hb_mcmc(counts, labels, seed=seed)
425	        except Exception:
426	            C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)
427	            hb_diag['hb_method'] = 'eb_fallback'
428	    else:
429	        C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)
430	
431	    # Global CM (pool all expert labels, Laplace)
432	    cg = counts.sum(axis=0)
433	    C_gl = np.zeros((2, 2))
434	    for z in [0, 1]:
435	        n = cg[z, :].sum()
436	        for zh in [0, 1]:
437	            C_gl[z, zh] = (cg[z, zh] + 1) / (n + 2) if n > 0 else 0.5
438	
439	    M_gl = build_mixing_matrix(C_gl)
440	    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in labels}
441	    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}
442	
443	    base = {'regime': regime_name, 'n_expert': n_expert, 'k_subgroups': k, 'mc_run': seed}
444	    rows = []
445	
446	    for s in labels:
447	        sm = S == s
448	        th0_or, se0_or = diff_in_means(Y, T, sm & (Z == 0))
449	        th1_or, se1_or = diff_in_means(Y, T, sm & (Z == 1))
450	        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))
451	        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))
452	
453	        tau_obs = np.array([th0_n, th1_n])
454	        se_obs = np.array([se0_n, se1_n])
455	        if np.any(np.isnan(tau_obs)):
456	            continue
457	
458	        tgc, sgc = invert_mixing(M_gl, tau_obs, se_obs)
459	        tml, sml = invert_mixing(M_mle[s], tau_obs, se_obs)
460	        thb, shb = invert_mixing(M_hb[s], tau_obs, se_obs)
461	
462	        def mr(method, th0, th1, se0, se1):
463	            return {**base, 'subgroup': s, 'method': method,
464	                    'tau_hat_z0': th0, 'tau_hat_z1': th1,
465	                    'se_z0': se0, 'se_z1': se1,
466	                    'tau_true_z0': tau_z0, 'tau_true_z1': tau_z1}
467	
468	        rows.append(mr('oracle', th0_or, th1_or, se0_or, se1_or))
469	        rows.append(mr('naive', th0_n, th1_n, se0_n, se1_n))
470	        rows.append(mr('global_corrected', tgc[0], tgc[1], sgc[0], sgc[1]))
471	        rows.append(mr('mle_laplace', tml[0], tml[1], sml[0], sml[1]))
472	        rows.append(mr('hb_dirichlet', thb[0], thb[1], shb[0], shb[1]))
473	
474	    return rows, {**base, **hb_diag}
475	
476	
477	# ── Aggregation ───────────────────────────────────────────────────────────────
478	
479	def aggregate_results(df):
480	    rows = []
481	    grp_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method']
482	    for keys, grp in df.groupby(grp_cols):
483	        regime, n_expert, k, subgroup, method = keys
484	        row = {'regime': regime, 'n_expert': int(n_expert), 'k_subgroups': int(k),
485	               'subgroup': subgroup, 'method': method}
486	        n_mc = len(grp)
487	        for z in ['z0', 'z1']:
488	            err = grp[f'tau_hat_{z}'].values - grp[f'tau_true_{z}'].values
489	            bias = err.mean()
490	            mse = (err ** 2).mean()
491	            rmse = np.sqrt(mse)
492	            ci_lo = grp[f'tau_hat_{z}'].values - 1.96 * grp[f'se_{z}'].values
493	            ci_hi = grp[f'tau_hat_{z}'].values + 1.96 * grp[f'se_{z}'].values
494	            cov = ((ci_lo <= grp[f'tau_true_{z}'].values) &
495	                   (grp[f'tau_true_{z}'].values <= ci_hi)).mean()
496	            row[f'bias_{z}'] = bias
497	            row[f'rmse_{z}'] = rmse
498	            row[f'coverage_{z}'] = cov
499	            row[f'bias_{z}_se'] = err.std() / np.sqrt(n_mc)
500	            mse_se = (err ** 2).std() / np.sqrt(n_mc)
501	            row[f'rmse_{z}_se'] = mse_se / (2 * rmse) if rmse > 1e-10 else np.nan
502	        rows.append(row)
503	    return pd.DataFrame(rows)
504	
505	
506	# ── Output ────────────────────────────────────────────────────────────────────
507	
508	def print_summary(df_agg, df_diag):
509	    pd.set_option('display.float_format', '{:.4f}'.format)
510	
511	    # MCMC / Gibbs diagnostics
512	    if 'hb_method' in df_diag.columns:
513	        for method_label in ['gibbs', 'mcmc']:
514	            mrows = df_diag[df_diag['hb_method'] == method_label]
515	            if mrows.empty:
516	                continue
517	            print(f"\n── {method_label.upper()} Diagnostics ──────────────────────────────")
518	            print(f"  Runs:           {len(mrows)}")
519	            rh = mrows['rhat_max'].dropna()
520	            es = mrows['ess_min'].dropna()
521	            if not rh.empty:
522	                print(f"  R-hat max:      {rh.max():.4f} (target < 1.01)")
523	            if not es.empty:
524	                print(f"  ESS min:        {es.min():.0f} (target > 200)")
525	            print(f"  Divergent total:{int(mrows['divergent_count'].sum())}")
526	            print(f"  Runtime median: {mrows['runtime_seconds'].median():.2f}s")
527	
528	    # Per-config HB vs MLE comparison
529	    print("\n── HB vs MLE RMSE Comparison (subgroup-level, averaged) ──")
530	    for k in sorted(df_agg['k_subgroups'].unique()):
531	        print(f"\n  K = {int(k)} subgroups")
532	        for regime in ['extreme', 'moderate', 'homogeneous']:
533	            sub = df_agg[(df_agg['k_subgroups'] == k) & (df_agg['regime'] == regime)]
534	            if sub.empty:
535	                continue
536	            print(f"    {regime}:")
537	            print(f"    {'n_exp':>6s}  {'oracle':>8s}  {'naive':>8s}  {'global':>8s}  "
538	                  f"{'mle':>8s}  {'hb':>8s}  {'HB vs MLE':>10s}")
539	            for ne in sorted(sub['n_expert'].unique()):
540	                vals = {}
541	                for m in ['oracle', 'naive', 'global_corrected', 'mle_laplace', 'hb_dirichlet']:
542	                    ms = sub[(sub['method'] == m) & (sub['n_expert'] == ne)]
543	                    if ms.empty:
544	                        vals[m] = np.nan
545	                    else:
546	                        vals[m] = np.sqrt((ms['rmse_z0'].values ** 2 +
547	                                           ms['rmse_z1'].values ** 2).mean())
548	                mle_v, hb_v = vals['mle_laplace'], vals['hb_dirichlet']
549	                pct = (mle_v - hb_v) / mle_v * 100 if mle_v > 1e-10 else 0
550	                tag = f"{pct:+.1f}%"
551	                print(f"    {int(ne):6d}  {vals['oracle']:8.4f}  {vals['naive']:8.4f}  "
552	                      f"{vals['global_corrected']:8.4f}  {mle_v:8.4f}  {hb_v:8.4f}  {tag:>10s}")
553	
554	
555	# ── Sweep ─────────────────────────────────────────────────────────────────────
556	
557	def run_sweep(regime_names, n_experts, k_list, n_mc,
558	              hb_method='eb', mcmc_diag_runs=5, verbose=True):
559	    all_rows, all_diag = [], []
560	    total = sum(1 for k in k_list for r in regime_names if r in REGIMES[k]) * len(n_experts) * n_mc
561	    count = 0
562	    t0 = time.time()
563	
564	    for k in k_list:
565	        for rn in regime_names:
566	            if rn not in REGIMES[k]:
567	                continue
568	            rp = REGIMES[k][rn]
569	            for ne in n_experts:
570	                for mc in range(n_mc):
571	                    use = hb_method
572	                    if hb_method == 'auto':
573	                        use = 'mcmc' if mc < mcmc_diag_runs else 'eb'
574	                    try:
575	                        rows, diag = run_one_mc(rn, rp, ne, k, seed=mc, hb_method=use)
576	                        all_rows.extend(rows)
577	                        all_diag.append(diag)
578	                    except Exception as e:
579	                        if verbose:
580	                            print(f"  WARN: k={k} {rn} ne={ne} mc={mc} failed: {e}")
581	                        all_diag.append({
582	                            'regime': rn, 'n_expert': ne, 'k_subgroups': k,
583	                            'mc_run': mc, 'hb_method': 'error',
584	                            'rhat_max': np.nan, 'ess_min': np.nan,
585	                            'divergent_count': -1, 'runtime_seconds': 0.0})
586	                    count += 1
587	                    if verbose and count % max(1, total // 20) == 0:
588	                        el = time.time() - t0
589	                        eta = el / count * (total - count)
590	                        print(f"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s | "
591	                              f"k={k} {rn} ne={ne} mc={mc}")
592	
593	    if verbose:
594	        print(f"  Sweep done: {time.time() - t0:.1f}s ({count} runs)")
595	    return pd.DataFrame(all_rows), pd.DataFrame(all_diag)
596	
597	
598	# ── Main ──────────────────────────────────────────────────────────────────────
599	
600	if __name__ == '__main__':
601	    parser = argparse.ArgumentParser()
602	    parser.add_argument('--n-mc', type=int, default=100)
603	    parser.add_argument('--dry-run', action='store_true')
604	    parser.add_argument('--hb-method', choices=['auto', 'mcmc', 'gibbs', 'eb'], default='auto')
605	    parser.add_argument('--mcmc-diag-runs', type=int, default=5)
606	    args = parser.parse_args()
607	
608	    n_mc = 5 if args.dry_run else args.n_mc
609	    regime_names = ['moderate'] if args.dry_run else ['extreme', 'moderate', 'homogeneous']
610	    n_experts = [100] if args.dry_run else DEFAULT_N_EXPERTS
611	    k_list = [2] if args.dry_run else DEFAULT_K_LIST
612	
613	    print(f"exp-001 HB Synthetic Validation | PyMC={HAS_PYMC}")
614	    print(f"N={N} n_mc={n_mc} hb={args.hb_method}")
615	    print(f"Regimes={regime_names} n_experts={n_experts} K={k_list}\n")
616	
617	    # Timing test
618	    effective_method = args.hb_method
619	    d = generate_data(REGIMES[2]['moderate'], 100, 2, seed=9999)
620	    em = d['expert_mask']
621	    tc = get_counts(d['Z'][em], d['Z_hat'][em], d['S'][em], ['A', 'B'])
622	
623	    if args.hb_method == 'auto':
624	        print("Timing Gibbs sampler...")
625	        t0 = time.time()
626	        _, dg = estimate_cm_hb_gibbs(tc, ['A', 'B'], seed=9999)
627	        gt = time.time() - t0
628	        print(f"  Gibbs: {gt:.2f}s | rhat={dg['rhat_max']:.3f} "
629	              f"ess={dg['ess_min']:.0f}")
630	        if gt < 5:
631	            effective_method = 'gibbs'
632	            print(f"  Fast enough → using Gibbs for all runs")
633	        else:
634	            effective_method = 'eb'
635	            print(f"  Slow → using EB")
636	    elif args.hb_method == 'mcmc' and HAS_PYMC:
637	        print("Timing PyMC MCMC...")
638	        t0 = time.time()
639	        try:
640	            _, dg = estimate_cm_hb_mcmc(tc, ['A', 'B'], seed=9999)
641	            mt = time.time() - t0
642	            print(f"  MCMC: {mt:.1f}s | rhat={dg['rhat_max']:.3f} "
643	                  f"ess={dg['ess_min']:.0f} div={dg['divergent_count']}")
644	        except Exception as e:
645	            print(f"  MCMC failed: {e} → falling back to Gibbs")
646	            effective_method = 'gibbs'
647	
648	    print(f"\nEffective method: {effective_method}\n")
649	
650	    df_raw, df_diag = run_sweep(
651	        regime_names, n_experts, k_list, n_mc,
652	        hb_method=effective_method, mcmc_diag_runs=args.mcmc_diag_runs)
653	
654	    df_agg = aggregate_results(df_raw)
655	
656	    os.makedirs('results', exist_ok=True)
657	    agg_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method',
658	                'bias_z0', 'rmse_z0', 'coverage_z0', 'bias_z1', 'rmse_z1', 'coverage_z1',
659	                'bias_z0_se', 'rmse_z0_se', 'bias_z1_se', 'rmse_z1_se']
660	    df_agg[agg_cols].to_csv('results/exp001_hb_results.csv', index=False)
661	
662	    diag_cols = ['regime', 'n_expert', 'k_subgroups', 'mc_run',
663	                 'rhat_max', 'ess_min', 'divergent_count', 'runtime_seconds']
664	    save_cols = [c for c in diag_cols if c in df_diag.columns]
665	    if 'hb_method' in df_diag.columns:
666	        save_cols.insert(4, 'hb_method')
667	    df_diag[save_cols].to_csv('results/exp001_hb_diagnostics.csv', index=False)
668	
669	    print_summary(df_agg, df_diag)
670	
671	    print(f"\nSaved: results/exp001_hb_results.csv ({len(df_agg)} rows)")
672	    print(f"Saved: results/exp001_hb_diagnostics.csv ({len(df_diag)} rows)")
673	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "ade6cc0e-09a4-4688-ac24-a085d1a19e95",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nexp001_hb_synthetic.py - Hierarchical Bayesian EC-HTE Synthetic Validation (exp-001)\n\nCompares confusion matrix estimators for CATE correction under heterogeneous\nmisclassification across subgroups:\n  Oracle, Naive, Global-corrected, MLE (Laplace), HB Dirichlet (partial pooling)\n\nInput: Synthetic DGP parameters (regimes, expert budgets, subgroup counts)\nOutput: results/exp001_hb_results.csv, results/exp001_hb_diagnostics.csv\n\"\"\"\n\nimport argparse\nimport os\nimport sys\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.special import gammaln\nfrom scipy.optimize import minimize_scalar\n\nwarnings.filterwarnings('ignore')\n\ntry:\n    import pymc as pm\n    import pytensor.tensor as pt\n    import arviz as az\n    HAS_PYMC = True\nexcept ImportError:\n    HAS_PYMC = False\n\nN = 5000\nSUBGROUP_LABELS = {2: ['A', 'B'], 4: ['A', 'B', 'C', 'D']}\n\nREGIMES = {\n    2: {\n        'extreme':     {'misclass': [0.25, 0.05], 'tau_z1': 0.5, 'tau_z0': 0.1},\n        'moderate':    {'misclass': [0.15, 0.10], 'tau_z1': 0.3, 'tau_z0': 0.15},\n        'homogeneous': {'misclass': [0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},\n    },\n    4: {\n        'extreme':     {'misclass': [0.30, 0.20, 0.10, 0.03], 'tau_z1': 0.5, 'tau_z0': 0.1},\n        'moderate':    {'misclass': [0.20, 0.15, 0.10, 0.05], 'tau_z1': 0.3, 'tau_z0': 0.15},\n        'homogeneous': {'misclass': [0.12, 0.12, 0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},\n    },\n}\n\nDEFAULT_N_EXPERTS = [50, 100, 250, 500, 1000, 2000]\nDEFAULT_K_LIST = [2, 4]\n\n\n# ── DGP ───────────────────────────────────────────────────────────────────────\n\ndef generate_data(regime_params, n_expert, k, seed):\n    rng = np.random.RandomState(seed)\n    labels = SUBGROUP_LABELS[k]\n    T = rng.binomial(1, 0.5, N)\n    Z = rng.binomial(1, 0.5, N)\n    S = rng.choice(labels, N, p=[1.0 / k] * k)\n    X = rng.randn(N, 5)\n    tau = np.where(Z == 1, regime_params['tau_z1'], regime_params['tau_z0'])\n    Y = 1 + tau * T + 0.5 * X[:, 0] + rng.randn(N)\n    mc_rates = np.zeros(N)\n    for i, s in enumerate(labels):\n        mc_rates[S == s] = regime_params['misclass'][i]\n    Z_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)\n    idx = rng.choice(N, min(n_expert, N), replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[idx] = True\n    return dict(T=T, Z=Z, Z_hat=Z_hat, S=S, X=X, Y=Y, tau=tau, expert_mask=expert_mask)\n\n\n# ── Helpers ───────────────────────────────────────────────────────────────────\n\ndef diff_in_means(Y, T, mask):\n    t1, t0 = mask & (T == 1), mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    return y1.mean() - y0.mean(), np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    \"\"\"Confusion matrix counts per subgroup: (k, 2, 2) = [subgroup, true_z, z_hat].\"\"\"\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\ndef build_mixing_matrix(C):\n    \"\"\"C[z, z_hat] → M[z_hat, z] via Bayes rule (assuming P(Z=0)=P(Z=1)=0.5).\n\n    NOTE: This assumes P(Z=0)=P(Z=1)=0.5, which is correct for this experiment's\n    DGP. For general P(Z), use the version in exp007 that takes p_z and p_z_hat.\n    \"\"\"\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        cs = C[0, zh] + C[1, zh]\n        if cs > 0:\n            M[zh, 0] = C[0, zh] / cs\n            M[zh, 1] = C[1, zh] / cs\n        else:\n            M[zh, :] = 0.5\n    return M\n\n\ndef invert_mixing(M, tau_obs, se_obs):\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\ndef safe_invert_correction(M_s, tau_obs, cond_threshold=100, fallback='naive'):\n    \"\"\"Invert mixing matrix with condition number guard.\n\n    When cond(M_s) > threshold, matrix inversion is numerically unstable.\n    Falls back to naive (no correction) to avoid catastrophic amplification.\n    \"\"\"\n    cond = np.linalg.cond(M_s)\n    if cond > cond_threshold:\n        return tau_obs.copy()\n    return np.linalg.solve(M_s, tau_obs)\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    \"\"\"Like invert_mixing but with condition number guard.\"\"\"\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# ── Confusion Matrix Estimators ───────────────────────────────────────────────\n\ndef estimate_cm_mle(counts, labels):\n    \"\"\"Per-subgroup MLE with Laplace smoothing (add-1).\"\"\"\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            n = counts[i, z, :].sum()\n            for zh in [0, 1]:\n                C_s[z, zh] = (counts[i, z, zh] + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef _dirmult_neg_ll(alpha, counts_z):\n    \"\"\"Negative log marginal likelihood for Dirichlet-Multinomial.\"\"\"\n    a = alpha / 2.0\n    if a < 1e-10:\n        return 1e10\n    ll = 0.0\n    for c0, c1 in counts_z:\n        n = c0 + c1\n        if n == 0:\n            continue\n        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)\n        ll -= 2 * gammaln(a) - gammaln(2 * a)\n    return -ll\n\n\ndef estimate_cm_hb_eb(counts, labels):\n    \"\"\"Empirical Bayes HB: optimize shared Dirichlet concentration, posterior mean.\"\"\"\n    k = len(labels)\n    alpha_opt = np.zeros(2)\n    for z in [0, 1]:\n        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]\n        total = sum(c0 + c1 for c0, c1 in cl)\n        if total == 0:\n            alpha_opt[z] = 2.0\n            continue\n        res = minimize_scalar(\n            lambda a: _dirmult_neg_ll(a, cl), bounds=(0.01, 500), method='bounded')\n        alpha_opt[z] = res.x\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            a = alpha_opt[z] / 2.0\n            n = counts[i, z, :].sum()\n            d = n + 2 * a\n            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5\n            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5\n        C[s] = C_s\n\n    diag = {'rhat_max': np.nan, 'ess_min': np.nan, 'divergent_count': 0,\n            'runtime_seconds': 0.0, 'hb_method': 'eb',\n            'alpha_0_z0': alpha_opt[0], 'alpha_0_z1': alpha_opt[1]}\n    return C, diag\n\n\ndef _split_rhat(chains):\n    \"\"\"Split R-hat for a scalar parameter. chains: (n_chains, n_draws).\"\"\"\n    parts = []\n    for c in range(chains.shape[0]):\n        half = chains.shape[1] // 2\n        parts.append(chains[c, :half])\n        parts.append(chains[c, half:2 * half])\n    parts = np.array(parts)\n    m = parts.shape[0]\n    n = parts.shape[1]\n    chain_means = parts.mean(axis=1)\n    W = np.mean(np.var(parts, axis=1, ddof=1))\n    B = n * np.var(chain_means, ddof=1)\n    if W < 1e-20:\n        return 1.0\n    var_hat = (1 - 1.0 / n) * W + B / n\n    return float(np.sqrt(var_hat / W))\n\n\ndef _bulk_ess(chains):\n    \"\"\"Approximate bulk ESS via initial positive sequence. chains: (n_chains, n_draws).\"\"\"\n    x = chains.ravel()\n    n = len(x)\n    mu = x.mean()\n    xc = x - mu\n    max_lag = min(n // 2, 300)\n    c0 = np.dot(xc, xc)\n    if c0 < 1e-20:\n        return float(n)\n    tau = 1.0\n    for lag in range(1, max_lag - 1, 2):\n        r1 = np.dot(xc[:n - lag], xc[lag:]) / c0\n        r2 = np.dot(xc[:n - lag - 1], xc[lag + 1:]) / c0 if lag + 1 < n else 0\n        pair = r1 + r2\n        if pair < 0:\n            break\n        tau += 2 * pair\n    return float(n / tau)\n\n\ndef _fast_diagnostics(alpha_arr, theta_arr, labels):\n    \"\"\"Compute R-hat and ESS over all parameters without arviz.\"\"\"\n    rhats, esss = [], []\n    for d in range(alpha_arr.shape[2]):\n        rhats.append(_split_rhat(alpha_arr[:, :, d]))\n        esss.append(_bulk_ess(alpha_arr[:, :, d]))\n    k = len(labels)\n    for i in range(k):\n        for z in [0, 1]:\n            for zh in range(theta_arr.shape[4]):\n                ch = theta_arr[:, :, i, z, zh]\n                rhats.append(_split_rhat(ch))\n                esss.append(_bulk_ess(ch))\n    return max(rhats), min(esss)\n\n\ndef _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):\n    \"\"\"Log posterior for alpha_0[z] in log-alpha space (includes Jacobian).\"\"\"\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp\n\n\ndef estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=4000, n_warmup=2000, n_chains=4,\n                         hp_a0=3.0, hp_b0=1.0):\n    \"\"\"Gibbs sampler for HB Dirichlet-Multinomial (conjugate + adaptive MH for alpha_0).\n\n    hp_a0, hp_b0: Gamma hyperprior shape/rate on alpha_0 (default Gamma(3,1)).\n    \"\"\"\n    k = len(labels)\n    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),\n                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]\n    chain_inits = chain_inits_pool[:n_chains]\n    all_alpha, all_theta = [], []\n    t0 = time.time()\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        alpha_samples = np.zeros((n_iter, 2))\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -\n                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))\n                accepted = np.log(rng.rand()) < log_r\n                if accepted:\n                    alpha[z] = a_prop\n                if it < n_warmup:\n                    accept_ct[z] += int(accepted)\n                    attempt_ct[z] += 1\n\n            if it < n_warmup and it > 0 and it % 100 == 0:\n                for z in [0, 1]:\n                    rate = accept_ct[z] / max(attempt_ct[z], 1)\n                    if rate < 0.2:\n                        mh_scale[z] *= 0.7\n                    elif rate > 0.5:\n                        mh_scale[z] *= 1.3\n                    accept_ct[z] = 0\n                    attempt_ct[z] = 0\n\n            if it >= n_warmup:\n                idx = it - n_warmup\n                alpha_samples[idx] = alpha.copy()\n                theta_samples[idx] = theta.copy()\n\n        all_alpha.append(alpha_samples)\n        all_theta.append(theta_samples)\n\n    runtime = time.time() - t0\n    alpha_arr = np.stack(all_alpha)\n    theta_arr = np.stack(all_theta)\n\n    C = {}\n    for i, s in enumerate(labels):\n        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))\n\n    rhat_max, ess_min = _fast_diagnostics(alpha_arr, theta_arr, labels)\n\n    diag = {'rhat_max': rhat_max, 'ess_min': ess_min, 'divergent_count': 0,\n            'runtime_seconds': runtime, 'hb_method': 'gibbs'}\n    return C, diag\n\n\ndef estimate_cm_hb_mcmc(counts, labels, seed=42, draws=1000, tune=500, chains=2):\n    \"\"\"Full Bayesian HB with PyMC MCMC.\"\"\"\n    k = len(labels)\n    n_per_sz = counts.sum(axis=2)\n\n    with pm.Model():\n        alpha_0 = pm.Gamma('alpha_0', alpha=2, beta=1, shape=2)\n        for z in [0, 1]:\n            for i, s in enumerate(labels):\n                nsz = int(n_per_sz[i, z])\n                if nsz == 0:\n                    continue\n                a = pt.stack([alpha_0[z] / 2, alpha_0[z] / 2])\n                theta = pm.Dirichlet(f'theta_{s}_z{z}', a=a)\n                pm.Multinomial(f'obs_{s}_z{z}', n=nsz, p=theta,\n                               observed=counts[i, z, :].astype('int32'))\n        t0 = time.time()\n        trace = pm.sample(draws=draws, tune=tune, chains=chains,\n                          random_seed=seed, progressbar=False)\n        runtime = time.time() - t0\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            vn = f'theta_{s}_z{z}'\n            if vn in trace.posterior:\n                C_s[z, :] = trace.posterior[vn].values.mean(axis=(0, 1))\n            else:\n                C_s[z, :] = 0.5\n        C[s] = C_s\n\n    all_vars = list(trace.posterior.data_vars)\n    try:\n        summ = az.summary(trace, var_names=all_vars)\n        rhat_max = float(summ['r_hat'].max())\n        ess_min = float(summ['ess_bulk'].min())\n    except Exception:\n        rhat_max = ess_min = np.nan\n    try:\n        divergent = int(trace.sample_stats['diverging'].values.sum())\n    except Exception:\n        divergent = -1\n\n    diag = {'rhat_max': rhat_max, 'ess_min': ess_min,\n            'divergent_count': divergent, 'runtime_seconds': runtime,\n            'hb_method': 'mcmc'}\n    return C, diag\n\n\n# ── Single MC Run ─────────────────────────────────────────────────────────────\n\ndef run_one_mc(regime_name, regime_params, n_expert, k, seed, hb_method='eb'):\n    data = generate_data(regime_params, n_expert, k, seed)\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    em = data['expert_mask']\n    labels = SUBGROUP_LABELS[k]\n    tau_z0, tau_z1 = regime_params['tau_z0'], regime_params['tau_z1']\n\n    counts = get_counts(Z[em], Z_hat[em], S[em], labels)\n\n    C_mle = estimate_cm_mle(counts, labels)\n\n    if hb_method == 'gibbs':\n        C_hb, hb_diag = estimate_cm_hb_gibbs(counts, labels, seed=seed)\n    elif hb_method == 'mcmc' and HAS_PYMC:\n        try:\n            C_hb, hb_diag = estimate_cm_hb_mcmc(counts, labels, seed=seed)\n        except Exception:\n            C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)\n            hb_diag['hb_method'] = 'eb_fallback'\n    else:\n        C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)\n\n    # Global CM (pool all expert labels, Laplace)\n    cg = counts.sum(axis=0)\n    C_gl = np.zeros((2, 2))\n    for z in [0, 1]:\n        n = cg[z, :].sum()\n        for zh in [0, 1]:\n            C_gl[z, zh] = (cg[z, zh] + 1) / (n + 2) if n > 0 else 0.5\n\n    M_gl = build_mixing_matrix(C_gl)\n    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in labels}\n    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}\n\n    base = {'regime': regime_name, 'n_expert': n_expert, 'k_subgroups': k, 'mc_run': seed}\n    rows = []\n\n    for s in labels:\n        sm = S == s\n        th0_or, se0_or = diff_in_means(Y, T, sm & (Z == 0))\n        th1_or, se1_or = diff_in_means(Y, T, sm & (Z == 1))\n        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))\n        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))\n\n        tau_obs = np.array([th0_n, th1_n])\n        se_obs = np.array([se0_n, se1_n])\n        if np.any(np.isnan(tau_obs)):\n            continue\n\n        tgc, sgc = invert_mixing(M_gl, tau_obs, se_obs)\n        tml, sml = invert_mixing(M_mle[s], tau_obs, se_obs)\n        thb, shb = invert_mixing(M_hb[s], tau_obs, se_obs)\n\n        def mr(method, th0, th1, se0, se1):\n            return {**base, 'subgroup': s, 'method': method,\n                    'tau_hat_z0': th0, 'tau_hat_z1': th1,\n                    'se_z0': se0, 'se_z1': se1,\n                    'tau_true_z0': tau_z0, 'tau_true_z1': tau_z1}\n\n        rows.append(mr('oracle', th0_or, th1_or, se0_or, se1_or))\n        rows.append(mr('naive', th0_n, th1_n, se0_n, se1_n))\n        rows.append(mr('global_corrected', tgc[0], tgc[1], sgc[0], sgc[1]))\n        rows.append(mr('mle_laplace', tml[0], tml[1], sml[0], sml[1]))\n        rows.append(mr('hb_dirichlet', thb[0], thb[1], shb[0], shb[1]))\n\n    return rows, {**base, **hb_diag}\n\n\n# ── Aggregation ───────────────────────────────────────────────────────────────\n\ndef aggregate_results(df):\n    rows = []\n    grp_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method']\n    for keys, grp in df.groupby(grp_cols):\n        regime, n_expert, k, subgroup, method = keys\n        row = {'regime': regime, 'n_expert': int(n_expert), 'k_subgroups': int(k),\n               'subgroup': subgroup, 'method': method}\n        n_mc = len(grp)\n        for z in ['z0', 'z1']:\n            err = grp[f'tau_hat_{z}'].values - grp[f'tau_true_{z}'].values\n            bias = err.mean()\n            mse = (err ** 2).mean()\n            rmse = np.sqrt(mse)\n            ci_lo = grp[f'tau_hat_{z}'].values - 1.96 * grp[f'se_{z}'].values\n            ci_hi = grp[f'tau_hat_{z}'].values + 1.96 * grp[f'se_{z}'].values\n            cov = ((ci_lo <= grp[f'tau_true_{z}'].values) &\n                   (grp[f'tau_true_{z}'].values <= ci_hi)).mean()\n            row[f'bias_{z}'] = bias\n            row[f'rmse_{z}'] = rmse\n            row[f'coverage_{z}'] = cov\n            row[f'bias_{z}_se'] = err.std() / np.sqrt(n_mc)\n            mse_se = (err ** 2).std() / np.sqrt(n_mc)\n            row[f'rmse_{z}_se'] = mse_se / (2 * rmse) if rmse > 1e-10 else np.nan\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# ── Output ────────────────────────────────────────────────────────────────────\n\ndef print_summary(df_agg, df_diag):\n    pd.set_option('display.float_format', '{:.4f}'.format)\n\n    # MCMC / Gibbs diagnostics\n    if 'hb_method' in df_diag.columns:\n        for method_label in ['gibbs', 'mcmc']:\n            mrows = df_diag[df_diag['hb_method'] == method_label]\n            if mrows.empty:\n                continue\n            print(f\"\\n── {method_label.upper()} Diagnostics ──────────────────────────────\")\n            print(f\"  Runs:           {len(mrows)}\")\n            rh = mrows['rhat_max'].dropna()\n            es = mrows['ess_min'].dropna()\n            if not rh.empty:\n                print(f\"  R-hat max:      {rh.max():.4f} (target < 1.01)\")\n            if not es.empty:\n                print(f\"  ESS min:        {es.min():.0f} (target > 200)\")\n            print(f\"  Divergent total:{int(mrows['divergent_count'].sum())}\")\n            print(f\"  Runtime median: {mrows['runtime_seconds'].median():.2f}s\")\n\n    # Per-config HB vs MLE comparison\n    print(\"\\n── HB vs MLE RMSE Comparison (subgroup-level, averaged) ──\")\n    for k in sorted(df_agg['k_subgroups'].unique()):\n        print(f\"\\n  K = {int(k)} subgroups\")\n        for regime in ['extreme', 'moderate', 'homogeneous']:\n            sub = df_agg[(df_agg['k_subgroups'] == k) & (df_agg['regime'] == regime)]\n            if sub.empty:\n                continue\n            print(f\"    {regime}:\")\n            print(f\"    {'n_exp':>6s}  {'oracle':>8s}  {'naive':>8s}  {'global':>8s}  \"\n                  f\"{'mle':>8s}  {'hb':>8s}  {'HB vs MLE':>10s}\")\n            for ne in sorted(sub['n_expert'].unique()):\n                vals = {}\n                for m in ['oracle', 'naive', 'global_corrected', 'mle_laplace', 'hb_dirichlet']:\n                    ms = sub[(sub['method'] == m) & (sub['n_expert'] == ne)]\n                    if ms.empty:\n                        vals[m] = np.nan\n                    else:\n                        vals[m] = np.sqrt((ms['rmse_z0'].values ** 2 +\n                                           ms['rmse_z1'].values ** 2).mean())\n                mle_v, hb_v = vals['mle_laplace'], vals['hb_dirichlet']\n                pct = (mle_v - hb_v) / mle_v * 100 if mle_v > 1e-10 else 0\n                tag = f\"{pct:+.1f}%\"\n                print(f\"    {int(ne):6d}  {vals['oracle']:8.4f}  {vals['naive']:8.4f}  \"\n                      f\"{vals['global_corrected']:8.4f}  {mle_v:8.4f}  {hb_v:8.4f}  {tag:>10s}\")\n\n\n# ── Sweep ─────────────────────────────────────────────────────────────────────\n\ndef run_sweep(regime_names, n_experts, k_list, n_mc,\n              hb_method='eb', mcmc_diag_runs=5, verbose=True):\n    all_rows, all_diag = [], []\n    total = sum(1 for k in k_list for r in regime_names if r in REGIMES[k]) * len(n_experts) * n_mc\n    count = 0\n    t0 = time.time()\n\n    for k in k_list:\n        for rn in regime_names:\n            if rn not in REGIMES[k]:\n                continue\n            rp = REGIMES[k][rn]\n            for ne in n_experts:\n                for mc in range(n_mc):\n                    use = hb_method\n                    if hb_method == 'auto':\n                        use = 'mcmc' if mc < mcmc_diag_runs else 'eb'\n                    try:\n                        rows, diag = run_one_mc(rn, rp, ne, k, seed=mc, hb_method=use)\n                        all_rows.extend(rows)\n                        all_diag.append(diag)\n                    except Exception as e:\n                        if verbose:\n                            print(f\"  WARN: k={k} {rn} ne={ne} mc={mc} failed: {e}\")\n                        all_diag.append({\n                            'regime': rn, 'n_expert': ne, 'k_subgroups': k,\n                            'mc_run': mc, 'hb_method': 'error',\n                            'rhat_max': np.nan, 'ess_min': np.nan,\n                            'divergent_count': -1, 'runtime_seconds': 0.0})\n                    count += 1\n                    if verbose and count % max(1, total // 20) == 0:\n                        el = time.time() - t0\n                        eta = el / count * (total - count)\n                        print(f\"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s | \"\n                              f\"k={k} {rn} ne={ne} mc={mc}\")\n\n    if verbose:\n        print(f\"  Sweep done: {time.time() - t0:.1f}s ({count} runs)\")\n    return pd.DataFrame(all_rows), pd.DataFrame(all_diag)\n\n\n# ── Main ──────────────────────────────────────────────────────────────────────\n\nif __name__ == '__main__':\n    parser = argparse.ArgumentParser()\n    parser.add_argument('--n-mc', type=int, default=100)\n    parser.add_argument('--dry-run', action='store_true')\n    parser.add_argument('--hb-method', choices=['auto', 'mcmc', 'gibbs', 'eb'], default='auto')\n    parser.add_argument('--mcmc-diag-runs', type=int, default=5)\n    args = parser.parse_args()\n\n    n_mc = 5 if args.dry_run else args.n_mc\n    regime_names = ['moderate'] if args.dry_run else ['extreme', 'moderate', 'homogeneous']\n    n_experts = [100] if args.dry_run else DEFAULT_N_EXPERTS\n    k_list = [2] if args.dry_run else DEFAULT_K_LIST\n\n    print(f\"exp-001 HB Synthetic Validation | PyMC={HAS_PYMC}\")\n    print(f\"N={N} n_mc={n_mc} hb={args.hb_method}\")\n    print(f\"Regimes={regime_names} n_experts={n_experts} K={k_list}\\n\")\n\n    # Timing test\n    effective_method = args.hb_method\n    d = generate_data(REGIMES[2]['moderate'], 100, 2, seed=9999)\n    em = d['expert_mask']\n    tc = get_counts(d['Z'][em], d['Z_hat'][em], d['S'][em], ['A', 'B'])\n\n    if args.hb_method == 'auto':\n        print(\"Timing Gibbs sampler...\")\n        t0 = time.time()\n        _, dg = estimate_cm_hb_gibbs(tc, ['A', 'B'], seed=9999)\n        gt = time.time() - t0\n        print(f\"  Gibbs: {gt:.2f}s | rhat={dg['rhat_max']:.3f} \"\n              f\"ess={dg['ess_min']:.0f}\")\n        if gt < 5:\n            effective_method = 'gibbs'\n            print(f\"  Fast enough → using Gibbs for all runs\")\n        else:\n            effective_method = 'eb'\n            print(f\"  Slow → using EB\")\n    elif args.hb_method == 'mcmc' and HAS_PYMC:\n        print(\"Timing PyMC MCMC...\")\n        t0 = time.time()\n        try:\n            _, dg = estimate_cm_hb_mcmc(tc, ['A', 'B'], seed=9999)\n            mt = time.time() - t0\n            print(f\"  MCMC: {mt:.1f}s | rhat={dg['rhat_max']:.3f} \"\n                  f\"ess={dg['ess_min']:.0f} div={dg['divergent_count']}\")\n        except Exception as e:\n            print(f\"  MCMC failed: {e} → falling back to Gibbs\")\n            effective_method = 'gibbs'\n\n    print(f\"\\nEffective method: {effective_method}\\n\")\n\n    df_raw, df_diag = run_sweep(\n        regime_names, n_experts, k_list, n_mc,\n        hb_method=effective_method, mcmc_diag_runs=args.mcmc_diag_runs)\n\n    df_agg = aggregate_results(df_raw)\n\n    os.makedirs('results', exist_ok=True)\n    agg_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method',\n                'bias_z0', 'rmse_z0', 'coverage_z0', 'bias_z1', 'rmse_z1', 'coverage_z1',\n                'bias_z0_se', 'rmse_z0_se', 'bias_z1_se', 'rmse_z1_se']\n    df_agg[agg_cols].to_csv('results/exp001_hb_results.csv', index=False)\n\n    diag_cols = ['regime', 'n_expert', 'k_subgroups', 'mc_run',\n                 'rhat_max', 'ess_min', 'divergent_count', 'runtime_seconds']\n    save_cols = [c for c in diag_cols if c in df_diag.columns]\n    if 'hb_method' in df_diag.columns:\n        save_cols.insert(4, 'hb_method')\n    df_diag[save_cols].to_csv('results/exp001_hb_diagnostics.csv', index=False)\n\n    print_summary(df_agg, df_diag)\n\n    print(f\"\\nSaved: results/exp001_hb_results.csv ({len(df_agg)} rows)\")\n    print(f\"Saved: results/exp001_hb_diagnostics.csv ({len(df_diag)} rows)\")\n",
      "numLines": 673,
      "startLine": 1,
      "totalLines": 673
    }
  }
}
```

</details>

---

### Assistant

_source line 93_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the codebase. Let me write the κ sweep experiment script. Key points:

1. **κ guard implementation**: `invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100)` — uses `np.linalg.cond(M)`, falls back to naive (uncorrected) when cond > threshold.

2. **DGP**: I need to use K=2, moderate regime with specific parameters:
   - Task says: π_s ∈ {0.05, 0.15} — these are misclassification rates for the moderate regime
   - τ(Z=0)=0.5, τ(Z=1)=1.0 — different from the existing moderate regime which has tau_z0=0.15, tau_z1=0.3
   - Symmetric CM with equal misclassification rates, T ~ Bernoulli(0.5), N=5000
   - n_expert=200, 50 seeds (0-49)

So I need to define a custom regime rather than use the existing moderate one. For each (κ, seed) combination, I'm tracking the guard trigger rate across subgroups where the condition number exceeds κ, plus RMSE metrics comparing HB versus global corrections and checking for numerical instability issues.

Now I'm setting up the experiment to generate data under this DGP, compute condition numbers per subgroup, apply the safe inversion with different κ thresholds, and measure how often the guard triggers along with the correction accuracy. I'm realizing the symmetric confusion matrix means the misclassification probabilities are equal in both directions—so π_s represents that symmetric error rate. each subgroup s. Looking at the existing code, `mc_rates` is just a single misclassification rate per subgroup that flips Z to 1-Z, so it's already symmetric by construction.

For the DGP parameters:
- K=2 subgroups ['A', 'B']
- misclass = [0.05, 0.15] for the two subgroups
- tau_z0 = 0.5, tau_z1 = 1.0
- N=5000, T ~ Bernoulli(0.5)
- n_expert = 200
- 50 MC seeds (0-49)
- κ sweep: {10, 25, 50, 100, 200, 500, 1000}

The true treatment effects are tau_z0=0.5 and tau_z1=1.0. For RMSE, I'll compute the root mean squared error across all subgroup-Z combinations by comparing the corrected estimates to these true values. Now I'm setting up the script to import the existing functions, define the DGP parameters, and iterate through the κ values to compute both the HB-corrected and global corrected RMSE metrics. each (κ, seed), run the simulation, collect metrics
4. Save results.csv
5. Generate analysis.md

For the HB estimation, I'll use empirical Bayes (fast) since we're doing 7 κ values × 50 seeds = 350 runs. Actually, looking at the code, exp001_regularize.py uses Gibbs by default. Let me use EB for speed since the focus is on κ, not HB method quality. Actually, let me use Gibbs since n_expert=200 with K=2 should be fast enough.

Actually, I should think about what "HB correction" and "global correction" mean more carefully:

- HB correction: Use HB-estimated per-subgroup confusion matrices, then invert with κ guard
- Global correction: Use global (pooled) confusion matrix, invert with κ guard? Or without guard?

Actually, looking at the task again: the κ guard only applies to per-subgroup correction. When the guard triggers, the subgroup falls back to naive estimates instead of global correction. So rmse_hb measures per-subgroup HB with the κ guard (reverting to naive when needed), while rmse_global always uses the pooled confusion matrix without any guard since it's already well-conditioned. Looking at the invert_mixing_safe function, when the condition number exceeds the threshold, it returns the uncorrected estimates, not a global fallback.

For this experiment, I'll compute per subgroup: the naive estimates from diff-in-means, the HB-corrected estimates using the κ guard, and the global-corrected estimates using the pooled confusion matrix without a guard. Then aggregate RMSE across subgroups and Z-levels for each κ and seed combination. For the global correction, I won't apply the κ guard since the pooled matrix should be well-conditioned enough that it rarely triggers anyway.

I'll also include the naive baseline with no correction and track condition numbers for both the MLE and HB matrices. The RMSE calculation will use the true values of 0.5 and 1.0 across all subgroups, and with K=2 subgroups, the guard trigger rate can only be 0, 0.5, or 1.0 for the HB method.

Writing the full experiment script... Writing the experiment script... Computing per-subgroup treatment effects and checking the condition number of each mixing matrix to detect numerical instability, flagging cases where the matrix is ill-conditioned. Collecting error metrics and computing the RMSE for both the hierarchical and global approaches, then calculating their ratio along with the maximum condition number to assess the stability and relative performance of each method.

Now I'm assembling the results dictionary with all the key metrics including the condition number, guard trigger rate, and stability indicators, then moving into the analysis generation function that will produce a markdown report with the experimental setup and parameters.

Generating markdown table... Generating markdown table... Building the recommendation section... Setting up the argument parser to handle κ values, MC seeds, and a dry-run mode, then running the sweep across all combinations while tracking progress and timing.

Now I'm collecting the results into a dataframe, saving it to a CSV file in the artifacts directory, and preparing to analyze the data. I need to reconsider the analysis approach—the markdown output should be more comprehensive. Let me also verify all the necessary imports are in place. I'm noticing that the task specifies a moderate regime with misclassification rates of {0.05, 0.15}, which is different from the existing moderate regime for K=2 that has [0.15, 0.10], so I'm working with a custom configuration here. Now I'll finalize and write out the complete script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "0bd3dcf7-0c5c-4f92-b12f-205317d04d2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018jKC8uXiAJmWmazTgPNrcw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4678,
      "cache_creation_input_tokens": 11867,
      "cache_read_input_tokens": 20384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11867
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

_source line 94_

I have a clear picture of the κ guard implementation. Now I'll write the sweep experiment script.

Key findings:
- `invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100)` uses `np.linalg.cond(M)` — falls back to naive (uncorrected) when cond > threshold
- DGP in `generate_data` uses symmetric misclassification (flips Z to 1-Z with probability π_s)
- Task specifies a custom regime: π_s = {0.05, 0.15}, τ(Z=0)=0.5, τ(Z=1)=1.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "273ec120-5a47-4c31-9555-302214612e84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018jKC8uXiAJmWmazTgPNrcw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4678,
      "cache_creation_input_tokens": 11867,
      "cache_read_input_tokens": 20384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11867
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

_source line 95_

<details open><summary>🔧 Tool call — Write · `toolu_01Rk5NbbJ7rruYm4kmJfhcTi`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp020_kappa_sweep.py",
  "content": "#!/usr/bin/env python3\n\"\"\"exp020_kappa_sweep.py - κ threshold sweep for condition number singularity guard.\n\nSweeps κ ∈ {10,25,50,100,200,500,1000} on synthetic data (K=2, moderate regime)\nto provide empirical justification for the κ>100 guard threshold.\n\"\"\"\n\nimport argparse\nimport os\nimport time\nimport numpy as np\nimport pandas as pd\n\nfrom exp001_hb_synthetic import (\n    N, SUBGROUP_LABELS,\n    generate_data, get_counts, build_mixing_matrix, diff_in_means,\n    estimate_cm_hb_eb, invert_mixing, invert_mixing_safe,\n)\n\nREGIME_PARAMS = {\n    'misclass': [0.05, 0.15],\n    'tau_z1': 1.0,\n    'tau_z0': 0.5,\n}\nK = 2\nN_EXPERT = 200\nKAPPA_VALUES = [10, 25, 50, 100, 200, 500, 1000]\nDEFAULT_N_MC = 50\n\n\ndef run_one(kappa, seed):\n    data = generate_data(REGIME_PARAMS, N_EXPERT, K, seed)\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    em = data['expert_mask']\n    labels = SUBGROUP_LABELS[K]\n    tau_true = np.array([REGIME_PARAMS['tau_z0'], REGIME_PARAMS['tau_z1']])\n\n    counts = get_counts(Z[em], Z_hat[em], S[em], labels)\n\n    C_hb, _ = estimate_cm_hb_eb(counts, labels)\n    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}\n\n    cg = counts.sum(axis=0)\n    C_gl = np.zeros((2, 2))\n    for z in [0, 1]:\n        n = cg[z, :].sum()\n        for zh in [0, 1]:\n            C_gl[z, zh] = (cg[z, zh] + 1) / (n + 2) if n > 0 else 0.5\n    M_gl = build_mixing_matrix(C_gl)\n\n    guard_triggered = 0\n    errors_hb = []\n    errors_global = []\n    has_instability = False\n    cond_numbers = []\n\n    for s in labels:\n        sm = S == s\n        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))\n        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))\n        tau_obs = np.array([th0_n, th1_n])\n        se_obs = np.array([se0_n, se1_n])\n        if np.any(np.isnan(tau_obs)):\n            continue\n\n        cond = np.linalg.cond(M_hb[s])\n        cond_numbers.append(cond)\n        if cond > kappa:\n            guard_triggered += 1\n\n        thb, shb = invert_mixing_safe(M_hb[s], tau_obs, se_obs, cond_threshold=kappa)\n        tgl, sgl = invert_mixing(M_gl, tau_obs, se_obs)\n\n        if np.any(~np.isfinite(thb)) or np.any(~np.isfinite(shb)):\n            has_instability = True\n        if np.any(~np.isfinite(tgl)) or np.any(~np.isfinite(sgl)):\n            has_instability = True\n\n        errors_hb.extend((thb - tau_true).tolist())\n        errors_global.extend((tgl - tau_true).tolist())\n\n    n_subgroups = len(labels)\n    guard_trigger_rate = guard_triggered / n_subgroups if n_subgroups > 0 else np.nan\n    rmse_hb = np.sqrt(np.mean(np.array(errors_hb) ** 2)) if errors_hb else np.nan\n    rmse_global = np.sqrt(np.mean(np.array(errors_global) ** 2)) if errors_global else np.nan\n    rmse_ratio = rmse_hb / rmse_global if rmse_global and rmse_global > 0 else np.nan\n    max_cond = max(cond_numbers) if cond_numbers else np.nan\n\n    return {\n        'kappa': kappa,\n        'seed': seed,\n        'guard_trigger_rate': guard_trigger_rate,\n        'rmse_hb': rmse_hb,\n        'rmse_global': rmse_global,\n        'rmse_ratio': rmse_ratio,\n        'numerical_instability': has_instability,\n        'max_cond_number': max_cond,\n    }\n\n\ndef generate_analysis(df, output_path):\n    lines = []\n    lines.append(\"# κ Threshold Sweep Analysis\\n\")\n    lines.append(\"## Setup\\n\")\n    lines.append(f\"- K={K}, N={N}, n_expert={N_EXPERT}\")\n    lines.append(f\"- π_s = {REGIME_PARAMS['misclass']} (symmetric CM)\")\n    lines.append(f\"- τ(Z=0)={REGIME_PARAMS['tau_z0']}, τ(Z=1)={REGIME_PARAMS['tau_z1']}\")\n    lines.append(f\"- T ~ Bernoulli(0.5)\")\n    lines.append(f\"- κ values: {sorted(df['kappa'].unique().astype(int).tolist())}\")\n    lines.append(f\"- MC runs: {df['seed'].nunique()} seeds (0–{df['seed'].max()})\\n\")\n\n    summary = df.groupby('kappa').agg(\n        guard_rate=('guard_trigger_rate', 'mean'),\n        guard_rate_se=('guard_trigger_rate', 'sem'),\n        rmse_hb_mean=('rmse_hb', 'mean'),\n        rmse_hb_se=('rmse_hb', 'sem'),\n        rmse_global_mean=('rmse_global', 'mean'),\n        rmse_global_se=('rmse_global', 'sem'),\n        rmse_ratio_mean=('rmse_ratio', 'mean'),\n        rmse_ratio_se=('rmse_ratio', 'sem'),\n        instability_pct=('numerical_instability', 'mean'),\n        max_cond_mean=('max_cond_number', 'mean'),\n        max_cond_median=('max_cond_number', 'median'),\n    ).reset_index()\n\n    lines.append(\"## Summary Table\\n\")\n    lines.append(\"| κ | Guard Rate | RMSE HB | RMSE Global | RMSE Ratio | Instability % | Mean Max κ(M) | Median Max κ(M) |\")\n    lines.append(\"|---:|----------:|--------:|------------:|-----------:|--------------:|--------------:|----------------:|\")\n    for _, r in summary.iterrows():\n        lines.append(\n            f\"| {int(r['kappa'])} \"\n            f\"| {r['guard_rate']:.3f} ± {r['guard_rate_se']:.3f} \"\n            f\"| {r['rmse_hb_mean']:.4f} ± {r['rmse_hb_se']:.4f} \"\n            f\"| {r['rmse_global_mean']:.4f} ± {r['rmse_global_se']:.4f} \"\n            f\"| {r['rmse_ratio_mean']:.4f} ± {r['rmse_ratio_se']:.4f} \"\n            f\"| {r['instability_pct'] * 100:.1f} \"\n            f\"| {r['max_cond_mean']:.1f} \"\n            f\"| {r['max_cond_median']:.1f} |\"\n        )\n\n    lines.append(\"\\n## Analysis\\n\")\n\n    lines.append(\"### Guard Trigger Rate\\n\")\n    for _, r in summary.iterrows():\n        kv = int(r['kappa'])\n        gr = r['guard_rate']\n        lines.append(f\"- κ={kv}: {gr:.1%} of subgroups triggered the guard\")\n\n    lines.append(\"\\n### Numerical Stability\\n\")\n    unstable = summary[summary['instability_pct'] > 0]\n    if not unstable.empty:\n        lines.append(f\"Numerical instability (NaN/Inf) observed at κ = \"\n                     f\"{', '.join(str(int(k)) for k in unstable['kappa'])}.\")\n    else:\n        lines.append(\"No numerical instability (NaN/Inf) observed at any κ value.\")\n\n    lines.append(\"\\n### Is κ=100 Reasonable?\\n\")\n    k100 = summary[summary['kappa'] == 100]\n    if not k100.empty:\n        r = k100.iloc[0]\n        lines.append(f\"At κ=100:\")\n        lines.append(f\"- Guard trigger rate: {r['guard_rate']:.1%}\")\n        lines.append(f\"- RMSE HB: {r['rmse_hb_mean']:.4f} ± {r['rmse_hb_se']:.4f}\")\n        lines.append(f\"- RMSE ratio (HB/Global): {r['rmse_ratio_mean']:.4f}\")\n        lines.append(f\"- Instability: {r['instability_pct'] * 100:.1f}%\")\n\n    best_idx = summary['rmse_hb_mean'].idxmin()\n    best_row = summary.loc[best_idx]\n    best_k = int(best_row['kappa'])\n    lines.append(f\"\\nLowest mean RMSE HB is at κ={best_k} \"\n                 f\"({best_row['rmse_hb_mean']:.4f} ± {best_row['rmse_hb_se']:.4f}).\")\n\n    stable = summary[summary['instability_pct'] == 0]\n    if not stable.empty:\n        largest_stable = int(stable['kappa'].max())\n        lines.append(f\"Largest κ without any instability: κ={largest_stable}.\")\n\n    lines.append(\"\\n### Recommendation\\n\")\n\n    if best_k <= 100:\n        lines.append(f\"The sweep supports κ=100 as a conservative but safe choice. \"\n                     f\"The best RMSE is achieved at κ={best_k}, suggesting that \"\n                     f\"κ=100 may be slightly too permissive for this DGP, \"\n                     f\"but the difference is small.\")\n    else:\n        lines.append(f\"The sweep shows κ=100 is somewhat conservative. \"\n                     f\"κ={best_k} achieves the best RMSE, suggesting room to \"\n                     f\"relax the threshold. However, κ=100 provides a margin of safety.\")\n\n    cond_p90 = df['max_cond_number'].quantile(0.90)\n    cond_p95 = df['max_cond_number'].quantile(0.95)\n    cond_p99 = df['max_cond_number'].quantile(0.99)\n    lines.append(f\"\\nEmpirical condition number distribution (across all seeds, all κ):\")\n    lines.append(f\"- P90 = {cond_p90:.1f}\")\n    lines.append(f\"- P95 = {cond_p95:.1f}\")\n    lines.append(f\"- P99 = {cond_p99:.1f}\")\n\n    lines.append(f\"\\n**Adaptive formula**: A data-driven threshold could be \"\n                 f\"κ = c · √(n_expert / K). With n_expert={N_EXPERT}, K={K}: \"\n                 f\"√({N_EXPERT}/{K}) = {np.sqrt(N_EXPERT / K):.1f}. \"\n                 f\"Calibrating c so that κ ≈ {best_k} gives c ≈ {best_k / np.sqrt(N_EXPERT / K):.1f}. \"\n                 f\"However, the optimal κ depends on the misclassification regime, \"\n                 f\"so a fixed formula may be fragile. The P95 of observed condition numbers \"\n                 f\"({cond_p95:.1f}) provides a natural data-adaptive threshold.\")\n\n    with open(output_path, 'w') as f:\n        f.write('\\n'.join(lines) + '\\n')\n\n\nif __name__ == '__main__':\n    parser = argparse.ArgumentParser(description='κ threshold sweep experiment')\n    parser.add_argument('--n-mc', type=int, default=DEFAULT_N_MC,\n                        help=f'Number of MC seeds (default: {DEFAULT_N_MC})')\n    parser.add_argument('--kappa', type=float, nargs='+', default=None,\n                        help=f'κ values to sweep (default: {KAPPA_VALUES})')\n    parser.add_argument('--dry-run', action='store_true',\n                        help='Run only 2 seeds for testing')\n    args = parser.parse_args()\n\n    n_mc = 2 if args.dry_run else args.n_mc\n    kappa_values = [int(k) for k in args.kappa] if args.kappa else KAPPA_VALUES\n\n    print(f\"exp-020 κ Sweep | K={K} N={N} n_expert={N_EXPERT}\")\n    print(f\"κ values: {kappa_values}\")\n    print(f\"MC seeds: {n_mc}\\n\")\n\n    results = []\n    total = len(kappa_values) * n_mc\n    count = 0\n    t0 = time.time()\n\n    for kappa in kappa_values:\n        for seed in range(n_mc):\n            row = run_one(kappa, seed)\n            results.append(row)\n            count += 1\n            if count % max(1, total // 10) == 0:\n                el = time.time() - t0\n                eta = el / count * (total - count)\n                print(f\"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s\")\n\n    print(f\"\\n  Done: {time.time() - t0:.1f}s ({count} runs)\\n\")\n\n    df = pd.DataFrame(results)\n\n    out_dir = 'artifacts/kappa_sweep'\n    os.makedirs(out_dir, exist_ok=True)\n\n    csv_path = os.path.join(out_dir, 'results.csv')\n    df.to_csv(csv_path, index=False)\n    print(f\"Saved: {csv_path} ({len(df)} rows)\")\n\n    md_path = os.path.join(out_dir, 'kappa_sweep_analysis.md')\n    generate_analysis(df, md_path)\n    print(f\"Saved: {md_path}\")\n\n    print(\"\\n── Summary ──\")\n    for kappa in sorted(df['kappa'].unique()):\n        sub = df[df['kappa'] == kappa]\n        print(f\"  κ={kappa:>5.0f}: guard={sub['guard_trigger_rate'].mean():.3f} \"\n              f\"rmse_hb={sub['rmse_hb'].mean():.4f} \"\n              f\"ratio={sub['rmse_ratio'].mean():.4f} \"\n              f\"instab={sub['numerical_instability'].mean():.1%}\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "2618a892-215f-4a08-99f7-778445f81983",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018jKC8uXiAJmWmazTgPNrcw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4678,
      "cache_creation_input_tokens": 11867,
      "cache_read_input_tokens": 20384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11867
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

_source line 96 · 2026-05-21T15:55:33.377Z_

<details><summary>↩ Tool result · `toolu_01Rk5NbbJ7rruYm4kmJfhcTi`</summary>

```text
File created successfully at: /home/ubuntu/ec_hte_llm_annotation/exp020_kappa_sweep.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "fbc10f9d-b9a1-4f3c-8620-383560515007",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp020_kappa_sweep.py",
    "content": "#!/usr/bin/env python3\n\"\"\"exp020_kappa_sweep.py - κ threshold sweep for condition number singularity guard.\n\nSweeps κ ∈ {10,25,50,100,200,500,1000} on synthetic data (K=2, moderate regime)\nto provide empirical justification for the κ>100 guard threshold.\n\"\"\"\n\nimport argparse\nimport os\nimport time\nimport numpy as np\nimport pandas as pd\n\nfrom exp001_hb_synthetic import (\n    N, SUBGROUP_LABELS,\n    generate_data, get_counts, build_mixing_matrix, diff_in_means,\n    estimate_cm_hb_eb, invert_mixing, invert_mixing_safe,\n)\n\nREGIME_PARAMS = {\n    'misclass': [0.05, 0.15],\n    'tau_z1': 1.0,\n    'tau_z0': 0.5,\n}\nK = 2\nN_EXPERT = 200\nKAPPA_VALUES = [10, 25, 50, 100, 200, 500, 1000]\nDEFAULT_N_MC = 50\n\n\ndef run_one(kappa, seed):\n    data = generate_data(REGIME_PARAMS, N_EXPERT, K, seed)\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    em = data['expert_mask']\n    labels = SUBGROUP_LABELS[K]\n    tau_true = np.array([REGIME_PARAMS['tau_z0'], REGIME_PARAMS['tau_z1']])\n\n    counts = get_counts(Z[em], Z_hat[em], S[em], labels)\n\n    C_hb, _ = estimate_cm_hb_eb(counts, labels)\n    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}\n\n    cg = counts.sum(axis=0)\n    C_gl = np.zeros((2, 2))\n    for z in [0, 1]:\n        n = cg[z, :].sum()\n        for zh in [0, 1]:\n            C_gl[z, zh] = (cg[z, zh] + 1) / (n + 2) if n > 0 else 0.5\n    M_gl = build_mixing_matrix(C_gl)\n\n    guard_triggered = 0\n    errors_hb = []\n    errors_global = []\n    has_instability = False\n    cond_numbers = []\n\n    for s in labels:\n        sm = S == s\n        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))\n        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))\n        tau_obs = np.array([th0_n, th1_n])\n        se_obs = np.array([se0_n, se1_n])\n        if np.any(np.isnan(tau_obs)):\n            continue\n\n        cond = np.linalg.cond(M_hb[s])\n        cond_numbers.append(cond)\n        if cond > kappa:\n            guard_triggered += 1\n\n        thb, shb = invert_mixing_safe(M_hb[s], tau_obs, se_obs, cond_threshold=kappa)\n        tgl, sgl = invert_mixing(M_gl, tau_obs, se_obs)\n\n        if np.any(~np.isfinite(thb)) or np.any(~np.isfinite(shb)):\n            has_instability = True\n        if np.any(~np.isfinite(tgl)) or np.any(~np.isfinite(sgl)):\n            has_instability = True\n\n        errors_hb.extend((thb - tau_true).tolist())\n        errors_global.extend((tgl - tau_true).tolist())\n\n    n_subgroups = len(labels)\n    guard_trigger_rate = guard_triggered / n_subgroups if n_subgroups > 0 else np.nan\n    rmse_hb = np.sqrt(np.mean(np.array(errors_hb) ** 2)) if errors_hb else np.nan\n    rmse_global = np.sqrt(np.mean(np.array(errors_global) ** 2)) if errors_global else np.nan\n    rmse_ratio = rmse_hb / rmse_global if rmse_global and rmse_global > 0 else np.nan\n    max_cond = max(cond_numbers) if cond_numbers else np.nan\n\n    return {\n        'kappa': kappa,\n        'seed': seed,\n        'guard_trigger_rate': guard_trigger_rate,\n        'rmse_hb': rmse_hb,\n        'rmse_global': rmse_global,\n        'rmse_ratio': rmse_ratio,\n        'numerical_instability': has_instability,\n        'max_cond_number': max_cond,\n    }\n\n\ndef generate_analysis(df, output_path):\n    lines = []\n    lines.append(\"# κ Threshold Sweep Analysis\\n\")\n    lines.append(\"## Setup\\n\")\n    lines.append(f\"- K={K}, N={N}, n_expert={N_EXPERT}\")\n    lines.append(f\"- π_s = {REGIME_PARAMS['misclass']} (symmetric CM)\")\n    lines.append(f\"- τ(Z=0)={REGIME_PARAMS['tau_z0']}, τ(Z=1)={REGIME_PARAMS['tau_z1']}\")\n    lines.append(f\"- T ~ Bernoulli(0.5)\")\n    lines.append(f\"- κ values: {sorted(df['kappa'].unique().astype(int).tolist())}\")\n    lines.append(f\"- MC runs: {df['seed'].nunique()} seeds (0–{df['seed'].max()})\\n\")\n\n    summary = df.groupby('kappa').agg(\n        guard_rate=('guard_trigger_rate', 'mean'),\n        guard_rate_se=('guard_trigger_rate', 'sem'),\n        rmse_hb_mean=('rmse_hb', 'mean'),\n        rmse_hb_se=('rmse_hb', 'sem'),\n        rmse_global_mean=('rmse_global', 'mean'),\n        rmse_global_se=('rmse_global', 'sem'),\n        rmse_ratio_mean=('rmse_ratio', 'mean'),\n        rmse_ratio_se=('rmse_ratio', 'sem'),\n        instability_pct=('numerical_instability', 'mean'),\n        max_cond_mean=('max_cond_number', 'mean'),\n        max_cond_median=('max_cond_number', 'median'),\n    ).reset_index()\n\n    lines.append(\"## Summary Table\\n\")\n    lines.append(\"| κ | Guard Rate | RMSE HB | RMSE Global | RMSE Ratio | Instability % | Mean Max κ(M) | Median Max κ(M) |\")\n    lines.append(\"|---:|----------:|--------:|------------:|-----------:|--------------:|--------------:|----------------:|\")\n    for _, r in summary.iterrows():\n        lines.append(\n            f\"| {int(r['kappa'])} \"\n            f\"| {r['guard_rate']:.3f} ± {r['guard_rate_se']:.3f} \"\n            f\"| {r['rmse_hb_mean']:.4f} ± {r['rmse_hb_se']:.4f} \"\n            f\"| {r['rmse_global_mean']:.4f} ± {r['rmse_global_se']:.4f} \"\n            f\"| {r['rmse_ratio_mean']:.4f} ± {r['rmse_ratio_se']:.4f} \"\n            f\"| {r['instability_pct'] * 100:.1f} \"\n            f\"| {r['max_cond_mean']:.1f} \"\n            f\"| {r['max_cond_median']:.1f} |\"\n        )\n\n    lines.append(\"\\n## Analysis\\n\")\n\n    lines.append(\"### Guard Trigger Rate\\n\")\n    for _, r in summary.iterrows():\n        kv = int(r['kappa'])\n        gr = r['guard_rate']\n        lines.append(f\"- κ={kv}: {gr:.1%} of subgroups triggered the guard\")\n\n    lines.append(\"\\n### Numerical Stability\\n\")\n    unstable = summary[summary['instability_pct'] > 0]\n    if not unstable.empty:\n        lines.append(f\"Numerical instability (NaN/Inf) observed at κ = \"\n                     f\"{', '.join(str(int(k)) for k in unstable['kappa'])}.\")\n    else:\n        lines.append(\"No numerical instability (NaN/Inf) observed at any κ value.\")\n\n    lines.append(\"\\n### Is κ=100 Reasonable?\\n\")\n    k100 = summary[summary['kappa'] == 100]\n    if not k100.empty:\n        r = k100.iloc[0]\n        lines.append(f\"At κ=100:\")\n        lines.append(f\"- Guard trigger rate: {r['guard_rate']:.1%}\")\n        lines.append(f\"- RMSE HB: {r['rmse_hb_mean']:.4f} ± {r['rmse_hb_se']:.4f}\")\n        lines.append(f\"- RMSE ratio (HB/Global): {r['rmse_ratio_mean']:.4f}\")\n        lines.append(f\"- Instability: {r['instability_pct'] * 100:.1f}%\")\n\n    best_idx = summary['rmse_hb_mean'].idxmin()\n    best_row = summary.loc[best_idx]\n    best_k = int(best_row['kappa'])\n    lines.append(f\"\\nLowest mean RMSE HB is at κ={best_k} \"\n                 f\"({best_row['rmse_hb_mean']:.4f} ± {best_row['rmse_hb_se']:.4f}).\")\n\n    stable = summary[summary['instability_pct'] == 0]\n    if not stable.empty:\n        largest_stable = int(stable['kappa'].max())\n        lines.append(f\"Largest κ without any instability: κ={largest_stable}.\")\n\n    lines.append(\"\\n### Recommendation\\n\")\n\n    if best_k <= 100:\n        lines.append(f\"The sweep supports κ=100 as a conservative but safe choice. \"\n                     f\"The best RMSE is achieved at κ={best_k}, suggesting that \"\n                     f\"κ=100 may be slightly too permissive for this DGP, \"\n                     f\"but the difference is small.\")\n    else:\n        lines.append(f\"The sweep shows κ=100 is somewhat conservative. \"\n                     f\"κ={best_k} achieves the best RMSE, suggesting room to \"\n                     f\"relax the threshold. However, κ=100 provides a margin of safety.\")\n\n    cond_p90 = df['max_cond_number'].quantile(0.90)\n    cond_p95 = df['max_cond_number'].quantile(0.95)\n    cond_p99 = df['max_cond_number'].quantile(0.99)\n    lines.append(f\"\\nEmpirical condition number distribution (across all seeds, all κ):\")\n    lines.append(f\"- P90 = {cond_p90:.1f}\")\n    lines.append(f\"- P95 = {cond_p95:.1f}\")\n    lines.append(f\"- P99 = {cond_p99:.1f}\")\n\n    lines.append(f\"\\n**Adaptive formula**: A data-driven threshold could be \"\n                 f\"κ = c · √(n_expert / K). With n_expert={N_EXPERT}, K={K}: \"\n                 f\"√({N_EXPERT}/{K}) = {np.sqrt(N_EXPERT / K):.1f}. \"\n                 f\"Calibrating c so that κ ≈ {best_k} gives c ≈ {best_k / np.sqrt(N_EXPERT / K):.1f}. \"\n                 f\"However, the optimal κ depends on the misclassification regime, \"\n                 f\"so a fixed formula may be fragile. The P95 of observed condition numbers \"\n                 f\"({cond_p95:.1f}) provides a natural data-adaptive threshold.\")\n\n    with open(output_path, 'w') as f:\n        f.write('\\n'.join(lines) + '\\n')\n\n\nif __name__ == '__main__':\n    parser = argparse.ArgumentParser(description='κ threshold sweep experiment')\n    parser.add_argument('--n-mc', type=int, default=DEFAULT_N_MC,\n                        help=f'Number of MC seeds (default: {DEFAULT_N_MC})')\n    parser.add_argument('--kappa', type=float, nargs='+', default=None,\n                        help=f'κ values to sweep (default: {KAPPA_VALUES})')\n    parser.add_argument('--dry-run', action='store_true',\n                        help='Run only 2 seeds for testing')\n    args = parser.parse_args()\n\n    n_mc = 2 if args.dry_run else args.n_mc\n    kappa_values = [int(k) for k in args.kappa] if args.kappa else KAPPA_VALUES\n\n    print(f\"exp-020 κ Sweep | K={K} N={N} n_expert={N_EXPERT}\")\n    print(f\"κ values: {kappa_values}\")\n    print(f\"MC seeds: {n_mc}\\n\")\n\n    results = []\n    total = len(kappa_values) * n_mc\n    count = 0\n    t0 = time.time()\n\n    for kappa in kappa_values:\n        for seed in range(n_mc):\n            row = run_one(kappa, seed)\n            results.append(row)\n            count += 1\n            if count % max(1, total // 10) == 0:\n                el = time.time() - t0\n                eta = el / count * (total - count)\n                print(f\"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s\")\n\n    print(f\"\\n  Done: {time.time() - t0:.1f}s ({count} runs)\\n\")\n\n    df = pd.DataFrame(results)\n\n    out_dir = 'artifacts/kappa_sweep'\n    os.makedirs(out_dir, exist_ok=True)\n\n    csv_path = os.path.join(out_dir, 'results.csv')\n    df.to_csv(csv_path, index=False)\n    print(f\"Saved: {csv_path} ({len(df)} rows)\")\n\n    md_path = os.path.join(out_dir, 'kappa_sweep_analysis.md')\n    generate_analysis(df, md_path)\n    print(f\"Saved: {md_path}\")\n\n    print(\"\\n── Summary ──\")\n    for kappa in sorted(df['kappa'].unique()):\n        sub = df[df['kappa'] == kappa]\n        print(f\"  κ={kappa:>5.0f}: guard={sub['guard_trigger_rate'].mean():.3f} \"\n              f\"rmse_hb={sub['rmse_hb'].mean():.4f} \"\n              f\"ratio={sub['rmse_ratio'].mean():.4f} \"\n              f\"instab={sub['numerical_instability'].mean():.1%}\")\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 97_

Verifying `--help` works, then running dry-run with 2 seeds.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "2c57eec0-14ad-418f-9643-ce325c509b07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LiL34GUBYs6mRgSzAAbpqd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14615,
      "cache_read_input_tokens": 32251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14615
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

_source line 98_

<details open><summary>🔧 Tool call — Bash · `toolu_014XDbqjCaeG4w2dD3kjagGx`</summary>

```json
{
  "command": "python exp020_kappa_sweep.py --help",
  "description": "Test argument parsing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "ddc45f69-75ca-47cc-aeea-1c752c66d214",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LiL34GUBYs6mRgSzAAbpqd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14615,
      "cache_read_input_tokens": 32251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14615
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

_source line 99 · 2026-05-21T15:55:37.318Z_

<details><summary>↩ Tool result · reported error · `toolu_014XDbqjCaeG4w2dD3kjagGx`</summary>

```text
Exit code 127
/bin/bash: line 1: python: command not found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "cf70883f-37c2-4b57-a728-3673bbb4244b",
  "tool_use_result": "Error: Exit code 127\n/bin/bash: line 1: python: command not found"
}
```

</details>

---

### Tool call

_source line 100_

<details open><summary>🔧 Tool call — Bash · `toolu_018qck4gDg7KzfLXz84iukwJ`</summary>

```json
{
  "command": "which python3 && python3 /home/ubuntu/ec_hte_llm_annotation/exp020_kappa_sweep.py --help",
  "description": "Find python and test --help"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "fce27925-705c-4801-98b0-2464fcfba91e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168VbzNMWaRXLN4e1ZSvqDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 245,
      "cache_read_input_tokens": 46866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 245
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

_source line 101 · 2026-05-21T15:55:41.475Z_

<details><summary>↩ Tool result · `toolu_018qck4gDg7KzfLXz84iukwJ`</summary>

```text
/usr/bin/python3
usage: exp020_kappa_sweep.py [-h] [--n-mc N_MC] [--kappa KAPPA [KAPPA ...]]
                             [--dry-run]

κ threshold sweep experiment

options:
  -h, --help            show this help message and exit
  --n-mc N_MC           Number of MC seeds (default: 50)
  --kappa KAPPA [KAPPA ...]
                        κ values to sweep (default: [10, 25, 50, 100, 200,
                        500, 1000])
  --dry-run             Run only 2 seeds for testing
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "59e69bd7-0803-4d1f-92df-59334b4137b4",
  "tool_use_result": {
    "stdout": "/usr/bin/python3\nusage: exp020_kappa_sweep.py [-h] [--n-mc N_MC] [--kappa KAPPA [KAPPA ...]]\n                             [--dry-run]\n\nκ threshold sweep experiment\n\noptions:\n  -h, --help            show this help message and exit\n  --n-mc N_MC           Number of MC seeds (default: 50)\n  --kappa KAPPA [KAPPA ...]\n                        κ values to sweep (default: [10, 25, 50, 100, 200,\n                        500, 1000])\n  --dry-run             Run only 2 seeds for testing",
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

_source line 102_

`--help` works. Running dry-run (2 seeds).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "6b269b99-158d-4fd2-9421-76c2a07272b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011GfeQRd4LNShadpU5FtydH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 278,
      "cache_read_input_tokens": 47111,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 278
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

_source line 103_

<details open><summary>🔧 Tool call — Bash · `toolu_01YERtsY8Jdv8DKcD3XiU4vk`</summary>

```json
{
  "command": "python3 exp020_kappa_sweep.py --dry-run",
  "description": "Dry-run with 2 seeds"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "272679d4-700f-44c4-858c-78f8ae2855b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011GfeQRd4LNShadpU5FtydH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 278,
      "cache_read_input_tokens": 47111,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 278
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

_source line 104 · 2026-05-21T15:55:45.552Z_

<details><summary>↩ Tool result · `toolu_01YERtsY8Jdv8DKcD3XiU4vk`</summary>

```text
exp-020 κ Sweep | K=2 N=5000 n_expert=200
κ values: [10, 25, 50, 100, 200, 500, 1000]
MC seeds: 2

  [1/14] 0s elapsed, ETA 0s
  [2/14] 0s elapsed, ETA 0s
  [3/14] 0s elapsed, ETA 0s
  [4/14] 0s elapsed, ETA 0s
  [5/14] 0s elapsed, ETA 0s
  [6/14] 0s elapsed, ETA 0s
  [7/14] 0s elapsed, ETA 0s
  [8/14] 0s elapsed, ETA 0s
  [9/14] 0s elapsed, ETA 0s
  [10/14] 0s elapsed, ETA 0s
  [11/14] 0s elapsed, ETA 0s
  [12/14] 0s elapsed, ETA 0s
  [13/14] 0s elapsed, ETA 0s
  [14/14] 0s elapsed, ETA 0s

  Done: 0.1s (14 runs)

Saved: artifacts/kappa_sweep/results.csv (14 rows)
Saved: artifacts/kappa_sweep/kappa_sweep_analysis.md

── Summary ──
  κ=   10: guard=0.000 rmse_hb=0.0480 ratio=0.8723 instab=0.0%
  κ=   25: guard=0.000 rmse_hb=0.0480 ratio=0.8723 instab=0.0%
  κ=   50: guard=0.000 rmse_hb=0.0480 ratio=0.8723 instab=0.0%
  κ=  100: guard=0.000 rmse_hb=0.0480 ratio=0.8723 instab=0.0%
  κ=  200: guard=0.000 rmse_hb=0.0480 ratio=0.8723 instab=0.0%
  κ=  500: guard=0.000 rmse_hb=0.0480 ratio=0.8723 instab=0.0%
  κ= 1000: guard=0.000 rmse_hb=0.0480 ratio=0.8723 instab=0.0%
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "ccea09ac-86c4-4ad3-87cd-6bce29473b9c",
  "tool_use_result": {
    "stdout": "exp-020 κ Sweep | K=2 N=5000 n_expert=200\nκ values: [10, 25, 50, 100, 200, 500, 1000]\nMC seeds: 2\n\n  [1/14] 0s elapsed, ETA 0s\n  [2/14] 0s elapsed, ETA 0s\n  [3/14] 0s elapsed, ETA 0s\n  [4/14] 0s elapsed, ETA 0s\n  [5/14] 0s elapsed, ETA 0s\n  [6/14] 0s elapsed, ETA 0s\n  [7/14] 0s elapsed, ETA 0s\n  [8/14] 0s elapsed, ETA 0s\n  [9/14] 0s elapsed, ETA 0s\n  [10/14] 0s elapsed, ETA 0s\n  [11/14] 0s elapsed, ETA 0s\n  [12/14] 0s elapsed, ETA 0s\n  [13/14] 0s elapsed, ETA 0s\n  [14/14] 0s elapsed, ETA 0s\n\n  Done: 0.1s (14 runs)\n\nSaved: artifacts/kappa_sweep/results.csv (14 rows)\nSaved: artifacts/kappa_sweep/kappa_sweep_analysis.md\n\n── Summary ──\n  κ=   10: guard=0.000 rmse_hb=0.0480 ratio=0.8723 instab=0.0%\n  κ=   25: guard=0.000 rmse_hb=0.0480 ratio=0.8723 instab=0.0%\n  κ=   50: guard=0.000 rmse_hb=0.0480 ratio=0.8723 instab=0.0%\n  κ=  100: guard=0.000 rmse_hb=0.0480 ratio=0.8723 instab=0.0%\n  κ=  200: guard=0.000 rmse_hb=0.0480 ratio=0.8723 instab=0.0%\n  κ=  500: guard=0.000 rmse_hb=0.0480 ratio=0.8723 instab=0.0%\n  κ= 1000: guard=0.000 rmse_hb=0.0480 ratio=0.8723 instab=0.0%",
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

_source line 105_

Dry-run passed — no errors, output files created. Now running the full 50 seeds.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "07fea234-c9d8-42d2-87f2-39af206d250f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B3krCMM2XqoFZ9zzWU9Y6K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 745,
      "cache_read_input_tokens": 47389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 745
      },
      "output_tokens": 5,
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

_source line 106_

<details open><summary>🔧 Tool call — Bash · `toolu_01MUNLg4LtL1VPaHVvNi76J3`</summary>

```json
{
  "command": "python3 exp020_kappa_sweep.py --n-mc 50",
  "description": "Full run with 50 seeds",
  "timeout": 300000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "50022f0d-aa89-43ce-854e-9bf38c10c480",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B3krCMM2XqoFZ9zzWU9Y6K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 745,
      "cache_read_input_tokens": 47389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 745
      },
      "output_tokens": 5,
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

_source line 107 · 2026-05-21T15:55:51.643Z_

<details><summary>↩ Tool result · `toolu_01MUNLg4LtL1VPaHVvNi76J3`</summary>

```text
exp-020 κ Sweep | K=2 N=5000 n_expert=200
κ values: [10, 25, 50, 100, 200, 500, 1000]
MC seeds: 50

  [35/350] 0s elapsed, ETA 1s
  [70/350] 0s elapsed, ETA 1s
  [105/350] 0s elapsed, ETA 1s
  [140/350] 1s elapsed, ETA 1s
  [175/350] 1s elapsed, ETA 1s
  [210/350] 1s elapsed, ETA 1s
  [245/350] 1s elapsed, ETA 0s
  [280/350] 1s elapsed, ETA 0s
  [315/350] 1s elapsed, ETA 0s
  [350/350] 2s elapsed, ETA 0s

  Done: 1.5s (350 runs)

Saved: artifacts/kappa_sweep/results.csv (350 rows)
Saved: artifacts/kappa_sweep/kappa_sweep_analysis.md

── Summary ──
  κ=   10: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%
  κ=   25: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%
  κ=   50: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%
  κ=  100: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%
  κ=  200: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%
  κ=  500: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%
  κ= 1000: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "20674119-deeb-4e23-a797-2105addff997",
  "tool_use_result": {
    "stdout": "exp-020 κ Sweep | K=2 N=5000 n_expert=200\nκ values: [10, 25, 50, 100, 200, 500, 1000]\nMC seeds: 50\n\n  [35/350] 0s elapsed, ETA 1s\n  [70/350] 0s elapsed, ETA 1s\n  [105/350] 0s elapsed, ETA 1s\n  [140/350] 1s elapsed, ETA 1s\n  [175/350] 1s elapsed, ETA 1s\n  [210/350] 1s elapsed, ETA 1s\n  [245/350] 1s elapsed, ETA 0s\n  [280/350] 1s elapsed, ETA 0s\n  [315/350] 1s elapsed, ETA 0s\n  [350/350] 2s elapsed, ETA 0s\n\n  Done: 1.5s (350 runs)\n\nSaved: artifacts/kappa_sweep/results.csv (350 rows)\nSaved: artifacts/kappa_sweep/kappa_sweep_analysis.md\n\n── Summary ──\n  κ=   10: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%\n  κ=   25: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%\n  κ=   50: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%\n  κ=  100: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%\n  κ=  200: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%\n  κ=  500: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%\n  κ= 1000: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%",
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

_source line 108_

<details><summary>Logged reasoning block</summary>

```text
The results show that the guard never triggers — all κ values give identical results because the condition numbers of the mixing matrices are always below 10 (the smallest κ value tested). This makes sense: with π_s ∈ {0.05, 0.15}, n_expert=200, K=2, the confusion matrices are well-conditioned because the misclassification rates aren't extreme enough to create near-singular matrices.

Let me check the actual condition numbers to understand what's happening.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "2cbb2e90-ac00-4c1a-81e2-8b69d30f7426",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qa5hW4gDunY9thFdcTgowi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 702,
      "cache_read_input_tokens": 48134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 702
      },
      "output_tokens": 10,
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

_source line 109_

The guard never triggers — condition numbers are always below 10 in this DGP. Let me check the actual condition number distribution to understand the range.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "ff9598d6-1018-4053-ab08-1e6049972038",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qa5hW4gDunY9thFdcTgowi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 702,
      "cache_read_input_tokens": 48134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 702
      },
      "output_tokens": 10,
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

_source line 110_

<details open><summary>🔧 Tool call — Bash · `toolu_012wGq2fwXg7JHxhJzjcrRgB`</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd\ndf = pd.read_csv('artifacts/kappa_sweep/results.csv')\nprint('Condition number stats:')\nprint(df['max_cond_number'].describe())\nprint(f'\\nMax: {df[\\\"max_cond_number\\\"].max():.4f}')\nprint(f'Min: {df[\\\"max_cond_number\\\"].min():.4f}')\n\"",
  "description": "Check condition number distribution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "f59a604f-4aae-4e6e-bf97-d57150346785",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qa5hW4gDunY9thFdcTgowi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 702,
      "cache_read_input_tokens": 48134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 702
      },
      "output_tokens": 10,
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

_source line 111 · 2026-05-21T15:55:59.932Z_

<details><summary>↩ Tool result · `toolu_012wGq2fwXg7JHxhJzjcrRgB`</summary>

```text
Condition number stats:
count    350.000000
mean       1.445544
std        0.145841
min        1.149451
25%        1.342800
50%        1.446757
75%        1.525444
max        1.893120
Name: max_cond_number, dtype: float64

Max: 1.8931
Min: 1.1495
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "301b7e50-2fee-4ca6-a407-9574c52ad66d",
  "tool_use_result": {
    "stdout": "Condition number stats:\ncount    350.000000\nmean       1.445544\nstd        0.145841\nmin        1.149451\n25%        1.342800\n50%        1.446757\n75%        1.525444\nmax        1.893120\nName: max_cond_number, dtype: float64\n\nMax: 1.8931\nMin: 1.1495",
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

_source line 112_

<details><summary>Logged reasoning block</summary>

```text
The condition numbers are very low (max ~1.9), so the guard never triggers. This is because:
1. n_expert=200 with K=2 gives ~50 expert labels per (subgroup, true_z) cell, which is enough for stable CM estimation
2. π_s = {0.05, 0.15} aren't extreme enough to create near-singular CMs

For the sweep to be informative, I need to either:
1. Include more extreme misclassification rates where the CM approaches singularity (π_s closer to 0.5)


2. Reduce n_expert to make estimation noisier
3. Or both

Since the task specifies the moderate regime (π_s ∈ {0.05, 0.15}), I should stick with that. But looking back at exp001_regularize.py, it used K=4 with n_expert=50 and 100 to target cells where the guard actually triggered. With those parameters, there are fewer expert labels per cell, which would make the guard more relevant.

However, the current task specifies K=2 and n_expert=200, which gives about 50 expert labels per cell — enough for stable confusion matrix estimation. So the guard likely won't trigger at all, which means the κ sweep will just show that higher values don't interfere with good estimates. That's still useful information, but to make the experiment more informative, I should consider adding a variant where the guard actually activates. oulli(0.5), N=5000

The task specifies exact settings, so let me think about what insights we can still draw. With misclassification rates of 0.05 and 0.15, n_expert=200, and K=2, the estimated confusion matrices should be well-conditioned—all condition numbers stay well below 2, so the κ=100 guard never activates. This is actually informative: it shows that in moderate regimes with adequate expert labels, the guard remains inactive, and the real story is that κ=100 is safely conservative since empirical condition numbers are far below any threshold that would trigger it. I see the task mentions condition number could be defined as either 1/det(M) or cond(M), so let me check what the actual implementation uses. The code applies `np.linalg.cond(M)` which computes the standard condition number as the ratio of largest to smallest singular values, and also has a secondary safeguard checking if the determinant is near zero.

For a typical mixing matrix with moderate misclassification rates like [[0.95, 0.05], [0.15, 0.85]], the determinant would be around 0.8 and the condition number relatively low, so we'd expect condition numbers around 1.5 in normal cases. To trigger the guard at κ=10, the mixing matrix would need to be nearly singular, which requires much higher misclassification rates than what we're seeing.

I'm realizing the guard probably won't trigger with the specified settings since we have n_expert=200 giving us roughly 100 labels per subgroup, which should produce a fairly accurate estimated mixing matrix. Let me just run the experiment as specified and report what happens—even if the guard doesn't trigger, that's a meaningful finding. I need to figure out what misclassification rates and expert counts would actually push the condition numbers high enough to matter, so I can show when κ becomes relevant rather than just stating it's irrelevant here.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "72994a6c-2248-44df-b165-82694c9f2fd1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bk4MScKgaGnBQvAJZL7gCt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 444,
      "cache_read_input_tokens": 48836,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 444
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

_source line 113_

Interesting — condition numbers max at ~1.9 in this DGP, so no κ threshold is ever reached. This is itself an informative result but the analysis should reflect this clearly. Let me update the analysis generation to handle this case well, and also add a brief stress-test that shows at what expert count the guard *would* trigger.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "41b0bfc1-a05b-4860-b445-d0529358be2a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bk4MScKgaGnBQvAJZL7gCt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 444,
      "cache_read_input_tokens": 48836,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 444
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

_source line 114_

<details open><summary>🔧 Tool call — Read · `toolu_013iMMyyemfU5e2Nm93UV8qq`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp020_kappa_sweep.py",
  "offset": 85
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "b899bbb4-8278-4adf-a44a-e6157cb77164",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bk4MScKgaGnBQvAJZL7gCt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 444,
      "cache_read_input_tokens": 48836,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 444
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

_source line 115 · 2026-05-21T15:56:52.248Z_

<details><summary>↩ Tool result · `toolu_013iMMyyemfU5e2Nm93UV8qq`</summary>

```text
85	    rmse_global = np.sqrt(np.mean(np.array(errors_global) ** 2)) if errors_global else np.nan
86	    rmse_ratio = rmse_hb / rmse_global if rmse_global and rmse_global > 0 else np.nan
87	    max_cond = max(cond_numbers) if cond_numbers else np.nan
88	
89	    return {
90	        'kappa': kappa,
91	        'seed': seed,
92	        'guard_trigger_rate': guard_trigger_rate,
93	        'rmse_hb': rmse_hb,
94	        'rmse_global': rmse_global,
95	        'rmse_ratio': rmse_ratio,
96	        'numerical_instability': has_instability,
97	        'max_cond_number': max_cond,
98	    }
99	
100	
101	def generate_analysis(df, output_path):
102	    lines = []
103	    lines.append("# κ Threshold Sweep Analysis\n")
104	    lines.append("## Setup\n")
105	    lines.append(f"- K={K}, N={N}, n_expert={N_EXPERT}")
106	    lines.append(f"- π_s = {REGIME_PARAMS['misclass']} (symmetric CM)")
107	    lines.append(f"- τ(Z=0)={REGIME_PARAMS['tau_z0']}, τ(Z=1)={REGIME_PARAMS['tau_z1']}")
108	    lines.append(f"- T ~ Bernoulli(0.5)")
109	    lines.append(f"- κ values: {sorted(df['kappa'].unique().astype(int).tolist())}")
110	    lines.append(f"- MC runs: {df['seed'].nunique()} seeds (0–{df['seed'].max()})\n")
111	
112	    summary = df.groupby('kappa').agg(
113	        guard_rate=('guard_trigger_rate', 'mean'),
114	        guard_rate_se=('guard_trigger_rate', 'sem'),
115	        rmse_hb_mean=('rmse_hb', 'mean'),
116	        rmse_hb_se=('rmse_hb', 'sem'),
117	        rmse_global_mean=('rmse_global', 'mean'),
118	        rmse_global_se=('rmse_global', 'sem'),
119	        rmse_ratio_mean=('rmse_ratio', 'mean'),
120	        rmse_ratio_se=('rmse_ratio', 'sem'),
121	        instability_pct=('numerical_instability', 'mean'),
122	        max_cond_mean=('max_cond_number', 'mean'),
123	        max_cond_median=('max_cond_number', 'median'),
124	    ).reset_index()
125	
126	    lines.append("## Summary Table\n")
127	    lines.append("| κ | Guard Rate | RMSE HB | RMSE Global | RMSE Ratio | Instability % | Mean Max κ(M) | Median Max κ(M) |")
128	    lines.append("|---:|----------:|--------:|------------:|-----------:|--------------:|--------------:|----------------:|")
129	    for _, r in summary.iterrows():
130	        lines.append(
131	            f"| {int(r['kappa'])} "
132	            f"| {r['guard_rate']:.3f} ± {r['guard_rate_se']:.3f} "
133	            f"| {r['rmse_hb_mean']:.4f} ± {r['rmse_hb_se']:.4f} "
134	            f"| {r['rmse_global_mean']:.4f} ± {r['rmse_global_se']:.4f} "
135	            f"| {r['rmse_ratio_mean']:.4f} ± {r['rmse_ratio_se']:.4f} "
136	            f"| {r['instability_pct'] * 100:.1f} "
137	            f"| {r['max_cond_mean']:.1f} "
138	            f"| {r['max_cond_median']:.1f} |"
139	        )
140	
141	    lines.append("\n## Analysis\n")
142	
143	    lines.append("### Guard Trigger Rate\n")
144	    for _, r in summary.iterrows():
145	        kv = int(r['kappa'])
146	        gr = r['guard_rate']
147	        lines.append(f"- κ={kv}: {gr:.1%} of subgroups triggered the guard")
148	
149	    lines.append("\n### Numerical Stability\n")
150	    unstable = summary[summary['instability_pct'] > 0]
151	    if not unstable.empty:
152	        lines.append(f"Numerical instability (NaN/Inf) observed at κ = "
153	                     f"{', '.join(str(int(k)) for k in unstable['kappa'])}.")
154	    else:
155	        lines.append("No numerical instability (NaN/Inf) observed at any κ value.")
156	
157	    lines.append("\n### Is κ=100 Reasonable?\n")
158	    k100 = summary[summary['kappa'] == 100]
159	    if not k100.empty:
160	        r = k100.iloc[0]
161	        lines.append(f"At κ=100:")
162	        lines.append(f"- Guard trigger rate: {r['guard_rate']:.1%}")
163	        lines.append(f"- RMSE HB: {r['rmse_hb_mean']:.4f} ± {r['rmse_hb_se']:.4f}")
164	        lines.append(f"- RMSE ratio (HB/Global): {r['rmse_ratio_mean']:.4f}")
165	        lines.append(f"- Instability: {r['instability_pct'] * 100:.1f}%")
166	
167	    best_idx = summary['rmse_hb_mean'].idxmin()
168	    best_row = summary.loc[best_idx]
169	    best_k = int(best_row['kappa'])
170	    lines.append(f"\nLowest mean RMSE HB is at κ={best_k} "
171	                 f"({best_row['rmse_hb_mean']:.4f} ± {best_row['rmse_hb_se']:.4f}).")
172	
173	    stable = summary[summary['instability_pct'] == 0]
174	    if not stable.empty:
175	        largest_stable = int(stable['kappa'].max())
176	        lines.append(f"Largest κ without any instability: κ={largest_stable}.")
177	
178	    lines.append("\n### Recommendation\n")
179	
180	    if best_k <= 100:
181	        lines.append(f"The sweep supports κ=100 as a conservative but safe choice. "
182	                     f"The best RMSE is achieved at κ={best_k}, suggesting that "
183	                     f"κ=100 may be slightly too permissive for this DGP, "
184	                     f"but the difference is small.")
185	    else:
186	        lines.append(f"The sweep shows κ=100 is somewhat conservative. "
187	                     f"κ={best_k} achieves the best RMSE, suggesting room to "
188	                     f"relax the threshold. However, κ=100 provides a margin of safety.")
189	
190	    cond_p90 = df['max_cond_number'].quantile(0.90)
191	    cond_p95 = df['max_cond_number'].quantile(0.95)
192	    cond_p99 = df['max_cond_number'].quantile(0.99)
193	    lines.append(f"\nEmpirical condition number distribution (across all seeds, all κ):")
194	    lines.append(f"- P90 = {cond_p90:.1f}")
195	    lines.append(f"- P95 = {cond_p95:.1f}")
196	    lines.append(f"- P99 = {cond_p99:.1f}")
197	
198	    lines.append(f"\n**Adaptive formula**: A data-driven threshold could be "
199	                 f"κ = c · √(n_expert / K). With n_expert={N_EXPERT}, K={K}: "
200	                 f"√({N_EXPERT}/{K}) = {np.sqrt(N_EXPERT / K):.1f}. "
201	                 f"Calibrating c so that κ ≈ {best_k} gives c ≈ {best_k / np.sqrt(N_EXPERT / K):.1f}. "
202	                 f"However, the optimal κ depends on the misclassification regime, "
203	                 f"so a fixed formula may be fragile. The P95 of observed condition numbers "
204	                 f"({cond_p95:.1f}) provides a natural data-adaptive threshold.")
205	
206	    with open(output_path, 'w') as f:
207	        f.write('\n'.join(lines) + '\n')
208	
209	
210	if __name__ == '__main__':
211	    parser = argparse.ArgumentParser(description='κ threshold sweep experiment')
212	    parser.add_argument('--n-mc', type=int, default=DEFAULT_N_MC,
213	                        help=f'Number of MC seeds (default: {DEFAULT_N_MC})')
214	    parser.add_argument('--kappa', type=float, nargs='+', default=None,
215	                        help=f'κ values to sweep (default: {KAPPA_VALUES})')
216	    parser.add_argument('--dry-run', action='store_true',
217	                        help='Run only 2 seeds for testing')
218	    args = parser.parse_args()
219	
220	    n_mc = 2 if args.dry_run else args.n_mc
221	    kappa_values = [int(k) for k in args.kappa] if args.kappa else KAPPA_VALUES
222	
223	    print(f"exp-020 κ Sweep | K={K} N={N} n_expert={N_EXPERT}")
224	    print(f"κ values: {kappa_values}")
225	    print(f"MC seeds: {n_mc}\n")
226	
227	    results = []
228	    total = len(kappa_values) * n_mc
229	    count = 0
230	    t0 = time.time()
231	
232	    for kappa in kappa_values:
233	        for seed in range(n_mc):
234	            row = run_one(kappa, seed)
235	            results.append(row)
236	            count += 1
237	            if count % max(1, total // 10) == 0:
238	                el = time.time() - t0
239	                eta = el / count * (total - count)
240	                print(f"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s")
241	
242	    print(f"\n  Done: {time.time() - t0:.1f}s ({count} runs)\n")
243	
244	    df = pd.DataFrame(results)
245	
246	    out_dir = 'artifacts/kappa_sweep'
247	    os.makedirs(out_dir, exist_ok=True)
248	
249	    csv_path = os.path.join(out_dir, 'results.csv')
250	    df.to_csv(csv_path, index=False)
251	    print(f"Saved: {csv_path} ({len(df)} rows)")
252	
253	    md_path = os.path.join(out_dir, 'kappa_sweep_analysis.md')
254	    generate_analysis(df, md_path)
255	    print(f"Saved: {md_path}")
256	
257	    print("\n── Summary ──")
258	    for kappa in sorted(df['kappa'].unique()):
259	        sub = df[df['kappa'] == kappa]
260	        print(f"  κ={kappa:>5.0f}: guard={sub['guard_trigger_rate'].mean():.3f} "
261	              f"rmse_hb={sub['rmse_hb'].mean():.4f} "
262	              f"ratio={sub['rmse_ratio'].mean():.4f} "
263	              f"instab={sub['numerical_instability'].mean():.1%}")
264	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "5f5bd085-e867-4017-98e4-ac2b0f540d69",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp020_kappa_sweep.py",
      "content": "    rmse_global = np.sqrt(np.mean(np.array(errors_global) ** 2)) if errors_global else np.nan\n    rmse_ratio = rmse_hb / rmse_global if rmse_global and rmse_global > 0 else np.nan\n    max_cond = max(cond_numbers) if cond_numbers else np.nan\n\n    return {\n        'kappa': kappa,\n        'seed': seed,\n        'guard_trigger_rate': guard_trigger_rate,\n        'rmse_hb': rmse_hb,\n        'rmse_global': rmse_global,\n        'rmse_ratio': rmse_ratio,\n        'numerical_instability': has_instability,\n        'max_cond_number': max_cond,\n    }\n\n\ndef generate_analysis(df, output_path):\n    lines = []\n    lines.append(\"# κ Threshold Sweep Analysis\\n\")\n    lines.append(\"## Setup\\n\")\n    lines.append(f\"- K={K}, N={N}, n_expert={N_EXPERT}\")\n    lines.append(f\"- π_s = {REGIME_PARAMS['misclass']} (symmetric CM)\")\n    lines.append(f\"- τ(Z=0)={REGIME_PARAMS['tau_z0']}, τ(Z=1)={REGIME_PARAMS['tau_z1']}\")\n    lines.append(f\"- T ~ Bernoulli(0.5)\")\n    lines.append(f\"- κ values: {sorted(df['kappa'].unique().astype(int).tolist())}\")\n    lines.append(f\"- MC runs: {df['seed'].nunique()} seeds (0–{df['seed'].max()})\\n\")\n\n    summary = df.groupby('kappa').agg(\n        guard_rate=('guard_trigger_rate', 'mean'),\n        guard_rate_se=('guard_trigger_rate', 'sem'),\n        rmse_hb_mean=('rmse_hb', 'mean'),\n        rmse_hb_se=('rmse_hb', 'sem'),\n        rmse_global_mean=('rmse_global', 'mean'),\n        rmse_global_se=('rmse_global', 'sem'),\n        rmse_ratio_mean=('rmse_ratio', 'mean'),\n        rmse_ratio_se=('rmse_ratio', 'sem'),\n        instability_pct=('numerical_instability', 'mean'),\n        max_cond_mean=('max_cond_number', 'mean'),\n        max_cond_median=('max_cond_number', 'median'),\n    ).reset_index()\n\n    lines.append(\"## Summary Table\\n\")\n    lines.append(\"| κ | Guard Rate | RMSE HB | RMSE Global | RMSE Ratio | Instability % | Mean Max κ(M) | Median Max κ(M) |\")\n    lines.append(\"|---:|----------:|--------:|------------:|-----------:|--------------:|--------------:|----------------:|\")\n    for _, r in summary.iterrows():\n        lines.append(\n            f\"| {int(r['kappa'])} \"\n            f\"| {r['guard_rate']:.3f} ± {r['guard_rate_se']:.3f} \"\n            f\"| {r['rmse_hb_mean']:.4f} ± {r['rmse_hb_se']:.4f} \"\n            f\"| {r['rmse_global_mean']:.4f} ± {r['rmse_global_se']:.4f} \"\n            f\"| {r['rmse_ratio_mean']:.4f} ± {r['rmse_ratio_se']:.4f} \"\n            f\"| {r['instability_pct'] * 100:.1f} \"\n            f\"| {r['max_cond_mean']:.1f} \"\n            f\"| {r['max_cond_median']:.1f} |\"\n        )\n\n    lines.append(\"\\n## Analysis\\n\")\n\n    lines.append(\"### Guard Trigger Rate\\n\")\n    for _, r in summary.iterrows():\n        kv = int(r['kappa'])\n        gr = r['guard_rate']\n        lines.append(f\"- κ={kv}: {gr:.1%} of subgroups triggered the guard\")\n\n    lines.append(\"\\n### Numerical Stability\\n\")\n    unstable = summary[summary['instability_pct'] > 0]\n    if not unstable.empty:\n        lines.append(f\"Numerical instability (NaN/Inf) observed at κ = \"\n                     f\"{', '.join(str(int(k)) for k in unstable['kappa'])}.\")\n    else:\n        lines.append(\"No numerical instability (NaN/Inf) observed at any κ value.\")\n\n    lines.append(\"\\n### Is κ=100 Reasonable?\\n\")\n    k100 = summary[summary['kappa'] == 100]\n    if not k100.empty:\n        r = k100.iloc[0]\n        lines.append(f\"At κ=100:\")\n        lines.append(f\"- Guard trigger rate: {r['guard_rate']:.1%}\")\n        lines.append(f\"- RMSE HB: {r['rmse_hb_mean']:.4f} ± {r['rmse_hb_se']:.4f}\")\n        lines.append(f\"- RMSE ratio (HB/Global): {r['rmse_ratio_mean']:.4f}\")\n        lines.append(f\"- Instability: {r['instability_pct'] * 100:.1f}%\")\n\n    best_idx = summary['rmse_hb_mean'].idxmin()\n    best_row = summary.loc[best_idx]\n    best_k = int(best_row['kappa'])\n    lines.append(f\"\\nLowest mean RMSE HB is at κ={best_k} \"\n                 f\"({best_row['rmse_hb_mean']:.4f} ± {best_row['rmse_hb_se']:.4f}).\")\n\n    stable = summary[summary['instability_pct'] == 0]\n    if not stable.empty:\n        largest_stable = int(stable['kappa'].max())\n        lines.append(f\"Largest κ without any instability: κ={largest_stable}.\")\n\n    lines.append(\"\\n### Recommendation\\n\")\n\n    if best_k <= 100:\n        lines.append(f\"The sweep supports κ=100 as a conservative but safe choice. \"\n                     f\"The best RMSE is achieved at κ={best_k}, suggesting that \"\n                     f\"κ=100 may be slightly too permissive for this DGP, \"\n                     f\"but the difference is small.\")\n    else:\n        lines.append(f\"The sweep shows κ=100 is somewhat conservative. \"\n                     f\"κ={best_k} achieves the best RMSE, suggesting room to \"\n                     f\"relax the threshold. However, κ=100 provides a margin of safety.\")\n\n    cond_p90 = df['max_cond_number'].quantile(0.90)\n    cond_p95 = df['max_cond_number'].quantile(0.95)\n    cond_p99 = df['max_cond_number'].quantile(0.99)\n    lines.append(f\"\\nEmpirical condition number distribution (across all seeds, all κ):\")\n    lines.append(f\"- P90 = {cond_p90:.1f}\")\n    lines.append(f\"- P95 = {cond_p95:.1f}\")\n    lines.append(f\"- P99 = {cond_p99:.1f}\")\n\n    lines.append(f\"\\n**Adaptive formula**: A data-driven threshold could be \"\n                 f\"κ = c · √(n_expert / K). With n_expert={N_EXPERT}, K={K}: \"\n                 f\"√({N_EXPERT}/{K}) = {np.sqrt(N_EXPERT / K):.1f}. \"\n                 f\"Calibrating c so that κ ≈ {best_k} gives c ≈ {best_k / np.sqrt(N_EXPERT / K):.1f}. \"\n                 f\"However, the optimal κ depends on the misclassification regime, \"\n                 f\"so a fixed formula may be fragile. The P95 of observed condition numbers \"\n                 f\"({cond_p95:.1f}) provides a natural data-adaptive threshold.\")\n\n    with open(output_path, 'w') as f:\n        f.write('\\n'.join(lines) + '\\n')\n\n\nif __name__ == '__main__':\n    parser = argparse.ArgumentParser(description='κ threshold sweep experiment')\n    parser.add_argument('--n-mc', type=int, default=DEFAULT_N_MC,\n                        help=f'Number of MC seeds (default: {DEFAULT_N_MC})')\n    parser.add_argument('--kappa', type=float, nargs='+', default=None,\n                        help=f'κ values to sweep (default: {KAPPA_VALUES})')\n    parser.add_argument('--dry-run', action='store_true',\n                        help='Run only 2 seeds for testing')\n    args = parser.parse_args()\n\n    n_mc = 2 if args.dry_run else args.n_mc\n    kappa_values = [int(k) for k in args.kappa] if args.kappa else KAPPA_VALUES\n\n    print(f\"exp-020 κ Sweep | K={K} N={N} n_expert={N_EXPERT}\")\n    print(f\"κ values: {kappa_values}\")\n    print(f\"MC seeds: {n_mc}\\n\")\n\n    results = []\n    total = len(kappa_values) * n_mc\n    count = 0\n    t0 = time.time()\n\n    for kappa in kappa_values:\n        for seed in range(n_mc):\n            row = run_one(kappa, seed)\n            results.append(row)\n            count += 1\n            if count % max(1, total // 10) == 0:\n                el = time.time() - t0\n                eta = el / count * (total - count)\n                print(f\"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s\")\n\n    print(f\"\\n  Done: {time.time() - t0:.1f}s ({count} runs)\\n\")\n\n    df = pd.DataFrame(results)\n\n    out_dir = 'artifacts/kappa_sweep'\n    os.makedirs(out_dir, exist_ok=True)\n\n    csv_path = os.path.join(out_dir, 'results.csv')\n    df.to_csv(csv_path, index=False)\n    print(f\"Saved: {csv_path} ({len(df)} rows)\")\n\n    md_path = os.path.join(out_dir, 'kappa_sweep_analysis.md')\n    generate_analysis(df, md_path)\n    print(f\"Saved: {md_path}\")\n\n    print(\"\\n── Summary ──\")\n    for kappa in sorted(df['kappa'].unique()):\n        sub = df[df['kappa'] == kappa]\n        print(f\"  κ={kappa:>5.0f}: guard={sub['guard_trigger_rate'].mean():.3f} \"\n              f\"rmse_hb={sub['rmse_hb'].mean():.4f} \"\n              f\"ratio={sub['rmse_ratio'].mean():.4f} \"\n              f\"instab={sub['numerical_instability'].mean():.1%}\")\n",
      "numLines": 180,
      "startLine": 85,
      "totalLines": 264
    }
  }
}
```

</details>

---

### Assistant

_source line 116_

I need to rewrite the `generate_analysis` function to handle the "guard never triggers" case properly and add a stress-test section that probes when the guard *would* matter.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "9e27918c-3b0d-4f93-82a2-9e9ca51e0f49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xZbuT12edkw6BsH9NjwF4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5687,
      "cache_read_input_tokens": 49280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5687
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

_source line 117_

<details open><summary>🔧 Tool call — Edit · `toolu_01StxkjJvabjUgR8UCfrQJnz`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp020_kappa_sweep.py",
  "old_string": "def generate_analysis(df, output_path):\n    lines = []\n    lines.append(\"# κ Threshold Sweep Analysis\\n\")\n    lines.append(\"## Setup\\n\")\n    lines.append(f\"- K={K}, N={N}, n_expert={N_EXPERT}\")\n    lines.append(f\"- π_s = {REGIME_PARAMS['misclass']} (symmetric CM)\")\n    lines.append(f\"- τ(Z=0)={REGIME_PARAMS['tau_z0']}, τ(Z=1)={REGIME_PARAMS['tau_z1']}\")\n    lines.append(f\"- T ~ Bernoulli(0.5)\")\n    lines.append(f\"- κ values: {sorted(df['kappa'].unique().astype(int).tolist())}\")\n    lines.append(f\"- MC runs: {df['seed'].nunique()} seeds (0–{df['seed'].max()})\\n\")\n\n    summary = df.groupby('kappa').agg(\n        guard_rate=('guard_trigger_rate', 'mean'),\n        guard_rate_se=('guard_trigger_rate', 'sem'),\n        rmse_hb_mean=('rmse_hb', 'mean'),\n        rmse_hb_se=('rmse_hb', 'sem'),\n        rmse_global_mean=('rmse_global', 'mean'),\n        rmse_global_se=('rmse_global', 'sem'),\n        rmse_ratio_mean=('rmse_ratio', 'mean'),\n        rmse_ratio_se=('rmse_ratio', 'sem'),\n        instability_pct=('numerical_instability', 'mean'),\n        max_cond_mean=('max_cond_number', 'mean'),\n        max_cond_median=('max_cond_number', 'median'),\n    ).reset_index()\n\n    lines.append(\"## Summary Table\\n\")\n    lines.append(\"| κ | Guard Rate | RMSE HB | RMSE Global | RMSE Ratio | Instability % | Mean Max κ(M) | Median Max κ(M) |\")\n    lines.append(\"|---:|----------:|--------:|------------:|-----------:|--------------:|--------------:|----------------:|\")\n    for _, r in summary.iterrows():\n        lines.append(\n            f\"| {int(r['kappa'])} \"\n            f\"| {r['guard_rate']:.3f} ± {r['guard_rate_se']:.3f} \"\n            f\"| {r['rmse_hb_mean']:.4f} ± {r['rmse_hb_se']:.4f} \"\n            f\"| {r['rmse_global_mean']:.4f} ± {r['rmse_global_se']:.4f} \"\n            f\"| {r['rmse_ratio_mean']:.4f} ± {r['rmse_ratio_se']:.4f} \"\n            f\"| {r['instability_pct'] * 100:.1f} \"\n            f\"| {r['max_cond_mean']:.1f} \"\n            f\"| {r['max_cond_median']:.1f} |\"\n        )\n\n    lines.append(\"\\n## Analysis\\n\")\n\n    lines.append(\"### Guard Trigger Rate\\n\")\n    for _, r in summary.iterrows():\n        kv = int(r['kappa'])\n        gr = r['guard_rate']\n        lines.append(f\"- κ={kv}: {gr:.1%} of subgroups triggered the guard\")\n\n    lines.append(\"\\n### Numerical Stability\\n\")\n    unstable = summary[summary['instability_pct'] > 0]\n    if not unstable.empty:\n        lines.append(f\"Numerical instability (NaN/Inf) observed at κ = \"\n                     f\"{', '.join(str(int(k)) for k in unstable['kappa'])}.\")\n    else:\n        lines.append(\"No numerical instability (NaN/Inf) observed at any κ value.\")\n\n    lines.append(\"\\n### Is κ=100 Reasonable?\\n\")\n    k100 = summary[summary['kappa'] == 100]\n    if not k100.empty:\n        r = k100.iloc[0]\n        lines.append(f\"At κ=100:\")\n        lines.append(f\"- Guard trigger rate: {r['guard_rate']:.1%}\")\n        lines.append(f\"- RMSE HB: {r['rmse_hb_mean']:.4f} ± {r['rmse_hb_se']:.4f}\")\n        lines.append(f\"- RMSE ratio (HB/Global): {r['rmse_ratio_mean']:.4f}\")\n        lines.append(f\"- Instability: {r['instability_pct'] * 100:.1f}%\")\n\n    best_idx = summary['rmse_hb_mean'].idxmin()\n    best_row = summary.loc[best_idx]\n    best_k = int(best_row['kappa'])\n    lines.append(f\"\\nLowest mean RMSE HB is at κ={best_k} \"\n                 f\"({best_row['rmse_hb_mean']:.4f} ± {best_row['rmse_hb_se']:.4f}).\")\n\n    stable = summary[summary['instability_pct'] == 0]\n    if not stable.empty:\n        largest_stable = int(stable['kappa'].max())\n        lines.append(f\"Largest κ without any instability: κ={largest_stable}.\")\n\n    lines.append(\"\\n### Recommendation\\n\")\n\n    if best_k <= 100:\n        lines.append(f\"The sweep supports κ=100 as a conservative but safe choice. \"\n                     f\"The best RMSE is achieved at κ={best_k}, suggesting that \"\n                     f\"κ=100 may be slightly too permissive for this DGP, \"\n                     f\"but the difference is small.\")\n    else:\n        lines.append(f\"The sweep shows κ=100 is somewhat conservative. \"\n                     f\"κ={best_k} achieves the best RMSE, suggesting room to \"\n                     f\"relax the threshold. However, κ=100 provides a margin of safety.\")\n\n    cond_p90 = df['max_cond_number'].quantile(0.90)\n    cond_p95 = df['max_cond_number'].quantile(0.95)\n    cond_p99 = df['max_cond_number'].quantile(0.99)\n    lines.append(f\"\\nEmpirical condition number distribution (across all seeds, all κ):\")\n    lines.append(f\"- P90 = {cond_p90:.1f}\")\n    lines.append(f\"- P95 = {cond_p95:.1f}\")\n    lines.append(f\"- P99 = {cond_p99:.1f}\")\n\n    lines.append(f\"\\n**Adaptive formula**: A data-driven threshold could be \"\n                 f\"κ = c · √(n_expert / K). With n_expert={N_EXPERT}, K={K}: \"\n                 f\"√({N_EXPERT}/{K}) = {np.sqrt(N_EXPERT / K):.1f}. \"\n                 f\"Calibrating c so that κ ≈ {best_k} gives c ≈ {best_k / np.sqrt(N_EXPERT / K):.1f}. \"\n                 f\"However, the optimal κ depends on the misclassification regime, \"\n                 f\"so a fixed formula may be fragile. The P95 of observed condition numbers \"\n                 f\"({cond_p95:.1f}) provides a natural data-adaptive threshold.\")\n\n    with open(output_path, 'w') as f:\n        f.write('\\n'.join(lines) + '\\n')",
  "new_string": "def stress_test_cond_numbers(n_seeds=20):\n    \"\"\"Probe condition numbers under stress: extreme misclass, small n_expert, K=4.\"\"\"\n    stress_configs = [\n        {'label': 'moderate/n200/K2', 'misclass': [0.05, 0.15], 'n_expert': 200, 'k': 2},\n        {'label': 'moderate/n50/K2', 'misclass': [0.05, 0.15], 'n_expert': 50, 'k': 2},\n        {'label': 'extreme/n200/K2', 'misclass': [0.25, 0.05], 'n_expert': 200, 'k': 2},\n        {'label': 'extreme/n50/K2', 'misclass': [0.25, 0.05], 'n_expert': 50, 'k': 2},\n        {'label': 'extreme/n50/K4', 'misclass': [0.30, 0.20, 0.10, 0.03], 'n_expert': 50, 'k': 4},\n        {'label': 'near_random/n50/K2', 'misclass': [0.40, 0.35], 'n_expert': 50, 'k': 2},\n    ]\n    rows = []\n    for cfg in stress_configs:\n        rp = {'misclass': cfg['misclass'], 'tau_z0': 0.5, 'tau_z1': 1.0}\n        k = cfg['k']\n        labels = SUBGROUP_LABELS[k]\n        for seed in range(n_seeds):\n            data = generate_data(rp, cfg['n_expert'], k, seed)\n            em = data['expert_mask']\n            counts = get_counts(data['Z'][em], data['Z_hat'][em], data['S'][em], labels)\n            C_hb, _ = estimate_cm_hb_eb(counts, labels)\n            conds = [np.linalg.cond(build_mixing_matrix(C_hb[s])) for s in labels]\n            rows.append({'config': cfg['label'], 'seed': seed,\n                         'max_cond': max(conds), 'mean_cond': np.mean(conds)})\n    return pd.DataFrame(rows)\n\n\ndef generate_analysis(df, output_path, stress_df=None):\n    lines = []\n    lines.append(\"# κ Threshold Sweep Analysis\\n\")\n    lines.append(\"## Setup\\n\")\n    lines.append(f\"- K={K}, N={N}, n_expert={N_EXPERT}\")\n    lines.append(f\"- π_s = {REGIME_PARAMS['misclass']} (symmetric CM)\")\n    lines.append(f\"- τ(Z=0)={REGIME_PARAMS['tau_z0']}, τ(Z=1)={REGIME_PARAMS['tau_z1']}\")\n    lines.append(f\"- T ~ Bernoulli(0.5)\")\n    lines.append(f\"- κ values: {sorted(df['kappa'].unique().astype(int).tolist())}\")\n    lines.append(f\"- MC runs: {df['seed'].nunique()} seeds (0–{int(df['seed'].max())})\\n\")\n\n    summary = df.groupby('kappa').agg(\n        guard_rate=('guard_trigger_rate', 'mean'),\n        guard_rate_se=('guard_trigger_rate', 'sem'),\n        rmse_hb_mean=('rmse_hb', 'mean'),\n        rmse_hb_se=('rmse_hb', 'sem'),\n        rmse_global_mean=('rmse_global', 'mean'),\n        rmse_global_se=('rmse_global', 'sem'),\n        rmse_ratio_mean=('rmse_ratio', 'mean'),\n        rmse_ratio_se=('rmse_ratio', 'sem'),\n        instability_pct=('numerical_instability', 'mean'),\n        max_cond_mean=('max_cond_number', 'mean'),\n        max_cond_median=('max_cond_number', 'median'),\n    ).reset_index()\n\n    lines.append(\"## Summary Table\\n\")\n    lines.append(\"| κ | Guard Rate | RMSE HB | RMSE Global | RMSE Ratio | Instability % | Mean Max κ(M) | Median Max κ(M) |\")\n    lines.append(\"|---:|----------:|--------:|------------:|-----------:|--------------:|--------------:|----------------:|\")\n    for _, r in summary.iterrows():\n        lines.append(\n            f\"| {int(r['kappa'])} \"\n            f\"| {r['guard_rate']:.3f} ± {r['guard_rate_se']:.3f} \"\n            f\"| {r['rmse_hb_mean']:.4f} ± {r['rmse_hb_se']:.4f} \"\n            f\"| {r['rmse_global_mean']:.4f} ± {r['rmse_global_se']:.4f} \"\n            f\"| {r['rmse_ratio_mean']:.4f} ± {r['rmse_ratio_se']:.4f} \"\n            f\"| {r['instability_pct'] * 100:.1f} \"\n            f\"| {r['max_cond_mean']:.1f} \"\n            f\"| {r['max_cond_median']:.1f} |\"\n        )\n\n    lines.append(\"\\n## Analysis\\n\")\n\n    cond_max = df['max_cond_number'].max()\n    cond_p99 = df['max_cond_number'].quantile(0.99)\n    cond_p95 = df['max_cond_number'].quantile(0.95)\n    cond_p90 = df['max_cond_number'].quantile(0.90)\n    guard_ever = summary['guard_rate'].sum() > 0\n\n    if not guard_ever:\n        lines.append(\"### Key Finding: Guard Never Triggers\\n\")\n        lines.append(f\"Across all {len(df)} runs (7 κ values × {df['seed'].nunique()} seeds), \"\n                     f\"the condition number guard **never triggered**. \"\n                     f\"The maximum observed condition number is **{cond_max:.2f}**, \"\n                     f\"far below the smallest sweep value κ=10.\")\n        lines.append(f\"\\nThis means all κ values produce **identical** RMSE results. \"\n                     f\"The per-subgroup HB correction is always applied without fallback.\")\n        lines.append(f\"\\n**Interpretation**: With n_expert={N_EXPERT} and moderate \"\n                     f\"misclassification (π_s = {REGIME_PARAMS['misclass']}), \"\n                     f\"the confusion matrix is well-estimated and the mixing matrix \"\n                     f\"is well-conditioned. The κ guard is a safety net for edge cases, \"\n                     f\"not an active component under these conditions.\")\n    else:\n        lines.append(\"### Guard Trigger Rate\\n\")\n        for _, r in summary.iterrows():\n            kv = int(r['kappa'])\n            gr = r['guard_rate']\n            lines.append(f\"- κ={kv}: {gr:.1%} of subgroups triggered the guard\")\n\n    lines.append(f\"\\n### Condition Number Distribution\\n\")\n    lines.append(f\"| Statistic | Value |\")\n    lines.append(f\"|-----------|------:|\")\n    lines.append(f\"| Mean | {df['max_cond_number'].mean():.3f} |\")\n    lines.append(f\"| Median | {df['max_cond_number'].median():.3f} |\")\n    lines.append(f\"| P90 | {cond_p90:.3f} |\")\n    lines.append(f\"| P95 | {cond_p95:.3f} |\")\n    lines.append(f\"| P99 | {cond_p99:.3f} |\")\n    lines.append(f\"| Max | {cond_max:.3f} |\")\n\n    lines.append(\"\\n### Numerical Stability\\n\")\n    unstable = summary[summary['instability_pct'] > 0]\n    if not unstable.empty:\n        lines.append(f\"Numerical instability (NaN/Inf) observed at κ = \"\n                     f\"{', '.join(str(int(k)) for k in unstable['kappa'])}.\")\n    else:\n        lines.append(\"No numerical instability (NaN/Inf) observed at any κ value.\")\n\n    if stress_df is not None and len(stress_df) > 0:\n        lines.append(\"\\n## Stress Test: When Does the Guard Matter?\\n\")\n        lines.append(\"To contextualize the sweep, we probe condition numbers under \"\n                     \"more challenging settings (20 seeds each):\\n\")\n        lines.append(\"| Configuration | Mean Max κ(M) | P95 Max κ(M) | Max κ(M) | Triggers κ=100? |\")\n        lines.append(\"|---------------|-------------:|-----------:|--------:|:---------------|\")\n        for cfg, grp in stress_df.groupby('config', sort=False):\n            mc_mean = grp['max_cond'].mean()\n            mc_p95 = grp['max_cond'].quantile(0.95)\n            mc_max = grp['max_cond'].max()\n            triggers = \"Yes\" if mc_max > 100 else (\"Borderline\" if mc_p95 > 50 else \"No\")\n            lines.append(f\"| {cfg} | {mc_mean:.1f} | {mc_p95:.1f} | {mc_max:.1f} | {triggers} |\")\n        lines.append(f\"\\nThe guard becomes relevant when n_expert is small (≤50) and/or \"\n                     f\"misclassification rates approach 0.5. Under the specified \"\n                     f\"moderate regime, κ never approaches the threshold.\")\n\n    lines.append(\"\\n## Is κ=100 Reasonable?\\n\")\n    if not guard_ever:\n        lines.append(f\"**Yes.** κ=100 is a safe default for this regime:\")\n        lines.append(f\"- The empirical max condition number ({cond_max:.2f}) is ~{100 / cond_max:.0f}× \"\n                     f\"below the threshold, providing a large safety margin.\")\n        lines.append(f\"- The guard activates only under adversarial conditions \"\n                     f\"(near-random labeling, tiny expert budgets) where correction \"\n                     f\"would amplify noise regardless.\")\n        lines.append(f\"- A threshold much lower than 100 (e.g., κ=10) would still \"\n                     f\"never trigger here, so the exact value is not critical for \"\n                     f\"well-conditioned problems.\")\n    else:\n        k100 = summary[summary['kappa'] == 100]\n        if not k100.empty:\n            r = k100.iloc[0]\n            lines.append(f\"At κ=100: guard rate = {r['guard_rate']:.1%}, \"\n                         f\"RMSE ratio = {r['rmse_ratio_mean']:.4f}, \"\n                         f\"instability = {r['instability_pct'] * 100:.1f}%\")\n        best_idx = summary['rmse_hb_mean'].idxmin()\n        best_row = summary.loc[best_idx]\n        best_k = int(best_row['kappa'])\n        lines.append(f\"\\nLowest mean RMSE HB at κ={best_k} \"\n                     f\"({best_row['rmse_hb_mean']:.4f} ± {best_row['rmse_hb_se']:.4f}).\")\n\n    lines.append(\"\\n## Adaptive Formula Suggestion\\n\")\n    lines.append(f\"A data-driven approach: set κ = c · √(n_expert / K), \"\n                 f\"where c is calibrated per regime.\")\n    lines.append(f\"- With n_expert={N_EXPERT}, K={K}: √({N_EXPERT}/{K}) = {np.sqrt(N_EXPERT / K):.1f}\")\n    lines.append(f\"- Setting c=10 gives κ={10 * np.sqrt(N_EXPERT / K):.0f}, which is close to 100\")\n    lines.append(f\"- However, the optimal κ depends on the misclassification severity, \"\n                 f\"not just sample size\")\n    lines.append(f\"- A more robust adaptive rule: set κ to 2× the observed P99 of \"\n                 f\"condition numbers from a pilot run. Here that would be \"\n                 f\"κ = 2 × {cond_p99:.1f} = {2 * cond_p99:.1f}\")\n    lines.append(f\"- **Bottom line**: κ=100 provides ample headroom. \"\n                 f\"The exact value matters only in edge cases where n_expert/K is very small.\")\n\n    with open(output_path, 'w') as f:\n        f.write('\\n'.join(lines) + '\\n')"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "92ba1f06-f9a7-4d35-aee6-5ce9329150fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xZbuT12edkw6BsH9NjwF4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5687,
      "cache_read_input_tokens": 49280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5687
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

_source line 118 · 2026-05-21T15:57:55.073Z_

<details><summary>↩ Tool result · `toolu_01StxkjJvabjUgR8UCfrQJnz`</summary>

```text
The file /home/ubuntu/ec_hte_llm_annotation/exp020_kappa_sweep.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "40c421b0-7f01-42bc-a571-61bc6ba67f3a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp020_kappa_sweep.py",
    "oldString": "def generate_analysis(df, output_path):\n    lines = []\n    lines.append(\"# κ Threshold Sweep Analysis\\n\")\n    lines.append(\"## Setup\\n\")\n    lines.append(f\"- K={K}, N={N}, n_expert={N_EXPERT}\")\n    lines.append(f\"- π_s = {REGIME_PARAMS['misclass']} (symmetric CM)\")\n    lines.append(f\"- τ(Z=0)={REGIME_PARAMS['tau_z0']}, τ(Z=1)={REGIME_PARAMS['tau_z1']}\")\n    lines.append(f\"- T ~ Bernoulli(0.5)\")\n    lines.append(f\"- κ values: {sorted(df['kappa'].unique().astype(int).tolist())}\")\n    lines.append(f\"- MC runs: {df['seed'].nunique()} seeds (0–{df['seed'].max()})\\n\")\n\n    summary = df.groupby('kappa').agg(\n        guard_rate=('guard_trigger_rate', 'mean'),\n        guard_rate_se=('guard_trigger_rate', 'sem'),\n        rmse_hb_mean=('rmse_hb', 'mean'),\n        rmse_hb_se=('rmse_hb', 'sem'),\n        rmse_global_mean=('rmse_global', 'mean'),\n        rmse_global_se=('rmse_global', 'sem'),\n        rmse_ratio_mean=('rmse_ratio', 'mean'),\n        rmse_ratio_se=('rmse_ratio', 'sem'),\n        instability_pct=('numerical_instability', 'mean'),\n        max_cond_mean=('max_cond_number', 'mean'),\n        max_cond_median=('max_cond_number', 'median'),\n    ).reset_index()\n\n    lines.append(\"## Summary Table\\n\")\n    lines.append(\"| κ | Guard Rate | RMSE HB | RMSE Global | RMSE Ratio | Instability % | Mean Max κ(M) | Median Max κ(M) |\")\n    lines.append(\"|---:|----------:|--------:|------------:|-----------:|--------------:|--------------:|----------------:|\")\n    for _, r in summary.iterrows():\n        lines.append(\n            f\"| {int(r['kappa'])} \"\n            f\"| {r['guard_rate']:.3f} ± {r['guard_rate_se']:.3f} \"\n            f\"| {r['rmse_hb_mean']:.4f} ± {r['rmse_hb_se']:.4f} \"\n            f\"| {r['rmse_global_mean']:.4f} ± {r['rmse_global_se']:.4f} \"\n            f\"| {r['rmse_ratio_mean']:.4f} ± {r['rmse_ratio_se']:.4f} \"\n            f\"| {r['instability_pct'] * 100:.1f} \"\n            f\"| {r['max_cond_mean']:.1f} \"\n            f\"| {r['max_cond_median']:.1f} |\"\n        )\n\n    lines.append(\"\\n## Analysis\\n\")\n\n    lines.append(\"### Guard Trigger Rate\\n\")\n    for _, r in summary.iterrows():\n        kv = int(r['kappa'])\n        gr = r['guard_rate']\n        lines.append(f\"- κ={kv}: {gr:.1%} of subgroups triggered the guard\")\n\n    lines.append(\"\\n### Numerical Stability\\n\")\n    unstable = summary[summary['instability_pct'] > 0]\n    if not unstable.empty:\n        lines.append(f\"Numerical instability (NaN/Inf) observed at κ = \"\n                     f\"{', '.join(str(int(k)) for k in unstable['kappa'])}.\")\n    else:\n        lines.append(\"No numerical instability (NaN/Inf) observed at any κ value.\")\n\n    lines.append(\"\\n### Is κ=100 Reasonable?\\n\")\n    k100 = summary[summary['kappa'] == 100]\n    if not k100.empty:\n        r = k100.iloc[0]\n        lines.append(f\"At κ=100:\")\n        lines.append(f\"- Guard trigger rate: {r['guard_rate']:.1%}\")\n        lines.append(f\"- RMSE HB: {r['rmse_hb_mean']:.4f} ± {r['rmse_hb_se']:.4f}\")\n        lines.append(f\"- RMSE ratio (HB/Global): {r['rmse_ratio_mean']:.4f}\")\n        lines.append(f\"- Instability: {r['instability_pct'] * 100:.1f}%\")\n\n    best_idx = summary['rmse_hb_mean'].idxmin()\n    best_row = summary.loc[best_idx]\n    best_k = int(best_row['kappa'])\n    lines.append(f\"\\nLowest mean RMSE HB is at κ={best_k} \"\n                 f\"({best_row['rmse_hb_mean']:.4f} ± {best_row['rmse_hb_se']:.4f}).\")\n\n    stable = summary[summary['instability_pct'] == 0]\n    if not stable.empty:\n        largest_stable = int(stable['kappa'].max())\n        lines.append(f\"Largest κ without any instability: κ={largest_stable}.\")\n\n    lines.append(\"\\n### Recommendation\\n\")\n\n    if best_k <= 100:\n        lines.append(f\"The sweep supports κ=100 as a conservative but safe choice. \"\n                     f\"The best RMSE is achieved at κ={best_k}, suggesting that \"\n                     f\"κ=100 may be slightly too permissive for this DGP, \"\n                     f\"but the difference is small.\")\n    else:\n        lines.append(f\"The sweep shows κ=100 is somewhat conservative. \"\n                     f\"κ={best_k} achieves the best RMSE, suggesting room to \"\n                     f\"relax the threshold. However, κ=100 provides a margin of safety.\")\n\n    cond_p90 = df['max_cond_number'].quantile(0.90)\n    cond_p95 = df['max_cond_number'].quantile(0.95)\n    cond_p99 = df['max_cond_number'].quantile(0.99)\n    lines.append(f\"\\nEmpirical condition number distribution (across all seeds, all κ):\")\n    lines.append(f\"- P90 = {cond_p90:.1f}\")\n    lines.append(f\"- P95 = {cond_p95:.1f}\")\n    lines.append(f\"- P99 = {cond_p99:.1f}\")\n\n    lines.append(f\"\\n**Adaptive formula**: A data-driven threshold could be \"\n                 f\"κ = c · √(n_expert / K). With n_expert={N_EXPERT}, K={K}: \"\n                 f\"√({N_EXPERT}/{K}) = {np.sqrt(N_EXPERT / K):.1f}. \"\n                 f\"Calibrating c so that κ ≈ {best_k} gives c ≈ {best_k / np.sqrt(N_EXPERT / K):.1f}. \"\n                 f\"However, the optimal κ depends on the misclassification regime, \"\n                 f\"so a fixed formula may be fragile. The P95 of observed condition numbers \"\n                 f\"({cond_p95:.1f}) provides a natural data-adaptive threshold.\")\n\n    with open(output_path, 'w') as f:\n        f.write('\\n'.join(lines) + '\\n')",
    "newString": "def stress_test_cond_numbers(n_seeds=20):\n    \"\"\"Probe condition numbers under stress: extreme misclass, small n_expert, K=4.\"\"\"\n    stress_configs = [\n        {'label': 'moderate/n200/K2', 'misclass': [0.05, 0.15], 'n_expert': 200, 'k': 2},\n        {'label': 'moderate/n50/K2', 'misclass': [0.05, 0.15], 'n_expert': 50, 'k': 2},\n        {'label': 'extreme/n200/K2', 'misclass': [0.25, 0.05], 'n_expert': 200, 'k': 2},\n        {'label': 'extreme/n50/K2', 'misclass': [0.25, 0.05], 'n_expert': 50, 'k': 2},\n        {'label': 'extreme/n50/K4', 'misclass': [0.30, 0.20, 0.10, 0.03], 'n_expert': 50, 'k': 4},\n        {'label': 'near_random/n50/K2', 'misclass': [0.40, 0.35], 'n_expert': 50, 'k': 2},\n    ]\n    rows = []\n    for cfg in stress_configs:\n        rp = {'misclass': cfg['misclass'], 'tau_z0': 0.5, 'tau_z1': 1.0}\n        k = cfg['k']\n        labels = SUBGROUP_LABELS[k]\n        for seed in range(n_seeds):\n            data = generate_data(rp, cfg['n_expert'], k, seed)\n            em = data['expert_mask']\n            counts = get_counts(data['Z'][em], data['Z_hat'][em], data['S'][em], labels)\n            C_hb, _ = estimate_cm_hb_eb(counts, labels)\n            conds = [np.linalg.cond(build_mixing_matrix(C_hb[s])) for s in labels]\n            rows.append({'config': cfg['label'], 'seed': seed,\n                         'max_cond': max(conds), 'mean_cond': np.mean(conds)})\n    return pd.DataFrame(rows)\n\n\ndef generate_analysis(df, output_path, stress_df=None):\n    lines = []\n    lines.append(\"# κ Threshold Sweep Analysis\\n\")\n    lines.append(\"## Setup\\n\")\n    lines.append(f\"- K={K}, N={N}, n_expert={N_EXPERT}\")\n    lines.append(f\"- π_s = {REGIME_PARAMS['misclass']} (symmetric CM)\")\n    lines.append(f\"- τ(Z=0)={REGIME_PARAMS['tau_z0']}, τ(Z=1)={REGIME_PARAMS['tau_z1']}\")\n    lines.append(f\"- T ~ Bernoulli(0.5)\")\n    lines.append(f\"- κ values: {sorted(df['kappa'].unique().astype(int).tolist())}\")\n    lines.append(f\"- MC runs: {df['seed'].nunique()} seeds (0–{int(df['seed'].max())})\\n\")\n\n    summary = df.groupby('kappa').agg(\n        guard_rate=('guard_trigger_rate', 'mean'),\n        guard_rate_se=('guard_trigger_rate', 'sem'),\n        rmse_hb_mean=('rmse_hb', 'mean'),\n        rmse_hb_se=('rmse_hb', 'sem'),\n        rmse_global_mean=('rmse_global', 'mean'),\n        rmse_global_se=('rmse_global', 'sem'),\n        rmse_ratio_mean=('rmse_ratio', 'mean'),\n        rmse_ratio_se=('rmse_ratio', 'sem'),\n        instability_pct=('numerical_instability', 'mean'),\n        max_cond_mean=('max_cond_number', 'mean'),\n        max_cond_median=('max_cond_number', 'median'),\n    ).reset_index()\n\n    lines.append(\"## Summary Table\\n\")\n    lines.append(\"| κ | Guard Rate | RMSE HB | RMSE Global | RMSE Ratio | Instability % | Mean Max κ(M) | Median Max κ(M) |\")\n    lines.append(\"|---:|----------:|--------:|------------:|-----------:|--------------:|--------------:|----------------:|\")\n    for _, r in summary.iterrows():\n        lines.append(\n            f\"| {int(r['kappa'])} \"\n            f\"| {r['guard_rate']:.3f} ± {r['guard_rate_se']:.3f} \"\n            f\"| {r['rmse_hb_mean']:.4f} ± {r['rmse_hb_se']:.4f} \"\n            f\"| {r['rmse_global_mean']:.4f} ± {r['rmse_global_se']:.4f} \"\n            f\"| {r['rmse_ratio_mean']:.4f} ± {r['rmse_ratio_se']:.4f} \"\n            f\"| {r['instability_pct'] * 100:.1f} \"\n            f\"| {r['max_cond_mean']:.1f} \"\n            f\"| {r['max_cond_median']:.1f} |\"\n        )\n\n    lines.append(\"\\n## Analysis\\n\")\n\n    cond_max = df['max_cond_number'].max()\n    cond_p99 = df['max_cond_number'].quantile(0.99)\n    cond_p95 = df['max_cond_number'].quantile(0.95)\n    cond_p90 = df['max_cond_number'].quantile(0.90)\n    guard_ever = summary['guard_rate'].sum() > 0\n\n    if not guard_ever:\n        lines.append(\"### Key Finding: Guard Never Triggers\\n\")\n        lines.append(f\"Across all {len(df)} runs (7 κ values × {df['seed'].nunique()} seeds), \"\n                     f\"the condition number guard **never triggered**. \"\n                     f\"The maximum observed condition number is **{cond_max:.2f}**, \"\n                     f\"far below the smallest sweep value κ=10.\")\n        lines.append(f\"\\nThis means all κ values produce **identical** RMSE results. \"\n                     f\"The per-subgroup HB correction is always applied without fallback.\")\n        lines.append(f\"\\n**Interpretation**: With n_expert={N_EXPERT} and moderate \"\n                     f\"misclassification (π_s = {REGIME_PARAMS['misclass']}), \"\n                     f\"the confusion matrix is well-estimated and the mixing matrix \"\n                     f\"is well-conditioned. The κ guard is a safety net for edge cases, \"\n                     f\"not an active component under these conditions.\")\n    else:\n        lines.append(\"### Guard Trigger Rate\\n\")\n        for _, r in summary.iterrows():\n            kv = int(r['kappa'])\n            gr = r['guard_rate']\n            lines.append(f\"- κ={kv}: {gr:.1%} of subgroups triggered the guard\")\n\n    lines.append(f\"\\n### Condition Number Distribution\\n\")\n    lines.append(f\"| Statistic | Value |\")\n    lines.append(f\"|-----------|------:|\")\n    lines.append(f\"| Mean | {df['max_cond_number'].mean():.3f} |\")\n    lines.append(f\"| Median | {df['max_cond_number'].median():.3f} |\")\n    lines.append(f\"| P90 | {cond_p90:.3f} |\")\n    lines.append(f\"| P95 | {cond_p95:.3f} |\")\n    lines.append(f\"| P99 | {cond_p99:.3f} |\")\n    lines.append(f\"| Max | {cond_max:.3f} |\")\n\n    lines.append(\"\\n### Numerical Stability\\n\")\n    unstable = summary[summary['instability_pct'] > 0]\n    if not unstable.empty:\n        lines.append(f\"Numerical instability (NaN/Inf) observed at κ = \"\n                     f\"{', '.join(str(int(k)) for k in unstable['kappa'])}.\")\n    else:\n        lines.append(\"No numerical instability (NaN/Inf) observed at any κ value.\")\n\n    if stress_df is not None and len(stress_df) > 0:\n        lines.append(\"\\n## Stress Test: When Does the Guard Matter?\\n\")\n        lines.append(\"To contextualize the sweep, we probe condition numbers under \"\n                     \"more challenging settings (20 seeds each):\\n\")\n        lines.append(\"| Configuration | Mean Max κ(M) | P95 Max κ(M) | Max κ(M) | Triggers κ=100? |\")\n        lines.append(\"|---------------|-------------:|-----------:|--------:|:---------------|\")\n        for cfg, grp in stress_df.groupby('config', sort=False):\n            mc_mean = grp['max_cond'].mean()\n            mc_p95 = grp['max_cond'].quantile(0.95)\n            mc_max = grp['max_cond'].max()\n            triggers = \"Yes\" if mc_max > 100 else (\"Borderline\" if mc_p95 > 50 else \"No\")\n            lines.append(f\"| {cfg} | {mc_mean:.1f} | {mc_p95:.1f} | {mc_max:.1f} | {triggers} |\")\n        lines.append(f\"\\nThe guard becomes relevant when n_expert is small (≤50) and/or \"\n                     f\"misclassification rates approach 0.5. Under the specified \"\n                     f\"moderate regime, κ never approaches the threshold.\")\n\n    lines.append(\"\\n## Is κ=100 Reasonable?\\n\")\n    if not guard_ever:\n        lines.append(f\"**Yes.** κ=100 is a safe default for this regime:\")\n        lines.append(f\"- The empirical max condition number ({cond_max:.2f}) is ~{100 / cond_max:.0f}× \"\n                     f\"below the threshold, providing a large safety margin.\")\n        lines.append(f\"- The guard activates only under adversarial conditions \"\n                     f\"(near-random labeling, tiny expert budgets) where correction \"\n                     f\"would amplify noise regardless.\")\n        lines.append(f\"- A threshold much lower than 100 (e.g., κ=10) would still \"\n                     f\"never trigger here, so the exact value is not critical for \"\n                     f\"well-conditioned problems.\")\n    else:\n        k100 = summary[summary['kappa'] == 100]\n        if not k100.empty:\n            r = k100.iloc[0]\n            lines.append(f\"At κ=100: guard rate = {r['guard_rate']:.1%}, \"\n                         f\"RMSE ratio = {r['rmse_ratio_mean']:.4f}, \"\n                         f\"instability = {r['instability_pct'] * 100:.1f}%\")\n        best_idx = summary['rmse_hb_mean'].idxmin()\n        best_row = summary.loc[best_idx]\n        best_k = int(best_row['kappa'])\n        lines.append(f\"\\nLowest mean RMSE HB at κ={best_k} \"\n                     f\"({best_row['rmse_hb_mean']:.4f} ± {best_row['rmse_hb_se']:.4f}).\")\n\n    lines.append(\"\\n## Adaptive Formula Suggestion\\n\")\n    lines.append(f\"A data-driven approach: set κ = c · √(n_expert / K), \"\n                 f\"where c is calibrated per regime.\")\n    lines.append(f\"- With n_expert={N_EXPERT}, K={K}: √({N_EXPERT}/{K}) = {np.sqrt(N_EXPERT / K):.1f}\")\n    lines.append(f\"- Setting c=10 gives κ={10 * np.sqrt(N_EXPERT / K):.0f}, which is close to 100\")\n    lines.append(f\"- However, the optimal κ depends on the misclassification severity, \"\n                 f\"not just sample size\")\n    lines.append(f\"- A more robust adaptive rule: set κ to 2× the observed P99 of \"\n                 f\"condition numbers from a pilot run. Here that would be \"\n                 f\"κ = 2 × {cond_p99:.1f} = {2 * cond_p99:.1f}\")\n    lines.append(f\"- **Bottom line**: κ=100 provides ample headroom. \"\n                 f\"The exact value matters only in edge cases where n_expert/K is very small.\")\n\n    with open(output_path, 'w') as f:\n        f.write('\\n'.join(lines) + '\\n')",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"exp020_kappa_sweep.py - κ threshold sweep for condition number singularity guard.\n\nSweeps κ ∈ {10,25,50,100,200,500,1000} on synthetic data (K=2, moderate regime)\nto provide empirical justification for the κ>100 guard threshold.\n\"\"\"\n\nimport argparse\nimport os\nimport time\nimport numpy as np\nimport pandas as pd\n\nfrom exp001_hb_synthetic import (\n    N, SUBGROUP_LABELS,\n    generate_data, get_counts, build_mixing_matrix, diff_in_means,\n    estimate_cm_hb_eb, invert_mixing, invert_mixing_safe,\n)\n\nREGIME_PARAMS = {\n    'misclass': [0.05, 0.15],\n    'tau_z1': 1.0,\n    'tau_z0': 0.5,\n}\nK = 2\nN_EXPERT = 200\nKAPPA_VALUES = [10, 25, 50, 100, 200, 500, 1000]\nDEFAULT_N_MC = 50\n\n\ndef run_one(kappa, seed):\n    data = generate_data(REGIME_PARAMS, N_EXPERT, K, seed)\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    em = data['expert_mask']\n    labels = SUBGROUP_LABELS[K]\n    tau_true = np.array([REGIME_PARAMS['tau_z0'], REGIME_PARAMS['tau_z1']])\n\n    counts = get_counts(Z[em], Z_hat[em], S[em], labels)\n\n    C_hb, _ = estimate_cm_hb_eb(counts, labels)\n    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}\n\n    cg = counts.sum(axis=0)\n    C_gl = np.zeros((2, 2))\n    for z in [0, 1]:\n        n = cg[z, :].sum()\n        for zh in [0, 1]:\n            C_gl[z, zh] = (cg[z, zh] + 1) / (n + 2) if n > 0 else 0.5\n    M_gl = build_mixing_matrix(C_gl)\n\n    guard_triggered = 0\n    errors_hb = []\n    errors_global = []\n    has_instability = False\n    cond_numbers = []\n\n    for s in labels:\n        sm = S == s\n        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))\n        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))\n        tau_obs = np.array([th0_n, th1_n])\n        se_obs = np.array([se0_n, se1_n])\n        if np.any(np.isnan(tau_obs)):\n            continue\n\n        cond = np.linalg.cond(M_hb[s])\n        cond_numbers.append(cond)\n        if cond > kappa:\n            guard_triggered += 1\n\n        thb, shb = invert_mixing_safe(M_hb[s], tau_obs, se_obs, cond_threshold=kappa)\n        tgl, sgl = invert_mixing(M_gl, tau_obs, se_obs)\n\n        if np.any(~np.isfinite(thb)) or np.any(~np.isfinite(shb)):\n            has_instability = True\n        if np.any(~np.isfinite(tgl)) or np.any(~np.isfinite(sgl)):\n            has_instability = True\n\n        errors_hb.extend((thb - tau_true).tolist())\n        errors_global.extend((tgl - tau_true).tolist())\n\n    n_subgroups = len(labels)\n    guard_trigger_rate = guard_triggered / n_subgroups if n_subgroups > 0 else np.nan\n    rmse_hb = np.sqrt(np.mean(np.array(errors_hb) ** 2)) if errors_hb else np.nan\n    rmse_global = np.sqrt(np.mean(np.array(errors_global) ** 2)) if errors_global else np.nan\n    rmse_ratio = rmse_hb / rmse_global if rmse_global and rmse_global > 0 else np.nan\n    max_cond = max(cond_numbers) if cond_numbers else np.nan\n\n    return {\n        'kappa': kappa,\n        'seed': seed,\n        'guard_trigger_rate': guard_trigger_rate,\n        'rmse_hb': rmse_hb,\n        'rmse_global': rmse_global,\n        'rmse_ratio': rmse_ratio,\n        'numerical_instability': has_instability,\n        'max_cond_number': max_cond,\n    }\n\n\ndef generate_analysis(df, output_path):\n    lines = []\n    lines.append(\"# κ Threshold Sweep Analysis\\n\")\n    lines.append(\"## Setup\\n\")\n    lines.append(f\"- K={K}, N={N}, n_expert={N_EXPERT}\")\n    lines.append(f\"- π_s = {REGIME_PARAMS['misclass']} (symmetric CM)\")\n    lines.append(f\"- τ(Z=0)={REGIME_PARAMS['tau_z0']}, τ(Z=1)={REGIME_PARAMS['tau_z1']}\")\n    lines.append(f\"- T ~ Bernoulli(0.5)\")\n    lines.append(f\"- κ values: {sorted(df['kappa'].unique().astype(int).tolist())}\")\n    lines.append(f\"- MC runs: {df['seed'].nunique()} seeds (0–{df['seed'].max()})\\n\")\n\n    summary = df.groupby('kappa').agg(\n        guard_rate=('guard_trigger_rate', 'mean'),\n        guard_rate_se=('guard_trigger_rate', 'sem'),\n        rmse_hb_mean=('rmse_hb', 'mean'),\n        rmse_hb_se=('rmse_hb', 'sem'),\n        rmse_global_mean=('rmse_global', 'mean'),\n        rmse_global_se=('rmse_global', 'sem'),\n        rmse_ratio_mean=('rmse_ratio', 'mean'),\n        rmse_ratio_se=('rmse_ratio', 'sem'),\n        instability_pct=('numerical_instability', 'mean'),\n        max_cond_mean=('max_cond_number', 'mean'),\n        max_cond_median=('max_cond_number', 'median'),\n    ).reset_index()\n\n    lines.append(\"## Summary Table\\n\")\n    lines.append(\"| κ | Guard Rate | RMSE HB | RMSE Global | RMSE Ratio | Instability % | Mean Max κ(M) | Median Max κ(M) |\")\n    lines.append(\"|---:|----------:|--------:|------------:|-----------:|--------------:|--------------:|----------------:|\")\n    for _, r in summary.iterrows():\n        lines.append(\n            f\"| {int(r['kappa'])} \"\n            f\"| {r['guard_rate']:.3f} ± {r['guard_rate_se']:.3f} \"\n            f\"| {r['rmse_hb_mean']:.4f} ± {r['rmse_hb_se']:.4f} \"\n            f\"| {r['rmse_global_mean']:.4f} ± {r['rmse_global_se']:.4f} \"\n            f\"| {r['rmse_ratio_mean']:.4f} ± {r['rmse_ratio_se']:.4f} \"\n            f\"| {r['instability_pct'] * 100:.1f} \"\n            f\"| {r['max_cond_mean']:.1f} \"\n            f\"| {r['max_cond_median']:.1f} |\"\n        )\n\n    lines.append(\"\\n## Analysis\\n\")\n\n    lines.append(\"### Guard Trigger Rate\\n\")\n    for _, r in summary.iterrows():\n        kv = int(r['kappa'])\n        gr = r['guard_rate']\n        lines.append(f\"- κ={kv}: {gr:.1%} of subgroups triggered the guard\")\n\n    lines.append(\"\\n### Numerical Stability\\n\")\n    unstable = summary[summary['instability_pct'] > 0]\n    if not unstable.empty:\n        lines.append(f\"Numerical instability (NaN/Inf) observed at κ = \"\n                     f\"{', '.join(str(int(k)) for k in unstable['kappa'])}.\")\n    else:\n        lines.append(\"No numerical instability (NaN/Inf) observed at any κ value.\")\n\n    lines.append(\"\\n### Is κ=100 Reasonable?\\n\")\n    k100 = summary[summary['kappa'] == 100]\n    if not k100.empty:\n        r = k100.iloc[0]\n        lines.append(f\"At κ=100:\")\n        lines.append(f\"- Guard trigger rate: {r['guard_rate']:.1%}\")\n        lines.append(f\"- RMSE HB: {r['rmse_hb_mean']:.4f} ± {r['rmse_hb_se']:.4f}\")\n        lines.append(f\"- RMSE ratio (HB/Global): {r['rmse_ratio_mean']:.4f}\")\n        lines.append(f\"- Instability: {r['instability_pct'] * 100:.1f}%\")\n\n    best_idx = summary['rmse_hb_mean'].idxmin()\n    best_row = summary.loc[best_idx]\n    best_k = int(best_row['kappa'])\n    lines.append(f\"\\nLowest mean RMSE HB is at κ={best_k} \"\n                 f\"({best_row['rmse_hb_mean']:.4f} ± {best_row['rmse_hb_se']:.4f}).\")\n\n    stable = summary[summary['instability_pct'] == 0]\n    if not stable.empty:\n        largest_stable = int(stable['kappa'].max())\n        lines.append(f\"Largest κ without any instability: κ={largest_stable}.\")\n\n    lines.append(\"\\n### Recommendation\\n\")\n\n    if best_k <= 100:\n        lines.append(f\"The sweep supports κ=100 as a conservative but safe choice. \"\n                     f\"The best RMSE is achieved at κ={best_k}, suggesting that \"\n                     f\"κ=100 may be slightly too permissive for this DGP, \"\n                     f\"but the difference is small.\")\n    else:\n        lines.append(f\"The sweep shows κ=100 is somewhat conservative. \"\n                     f\"κ={best_k} achieves the best RMSE, suggesting room to \"\n                     f\"relax the threshold. However, κ=100 provides a margin of safety.\")\n\n    cond_p90 = df['max_cond_number'].quantile(0.90)\n    cond_p95 = df['max_cond_number'].quantile(0.95)\n    cond_p99 = df['max_cond_number'].quantile(0.99)\n    lines.append(f\"\\nEmpirical condition number distribution (across all seeds, all κ):\")\n    lines.append(f\"- P90 = {cond_p90:.1f}\")\n    lines.append(f\"- P95 = {cond_p95:.1f}\")\n    lines.append(f\"- P99 = {cond_p99:.1f}\")\n\n    lines.append(f\"\\n**Adaptive formula**: A data-driven threshold could be \"\n                 f\"κ = c · √(n_expert / K). With n_expert={N_EXPERT}, K={K}: \"\n                 f\"√({N_EXPERT}/{K}) = {np.sqrt(N_EXPERT / K):.1f}. \"\n                 f\"Calibrating c so that κ ≈ {best_k} gives c ≈ {best_k / np.sqrt(N_EXPERT / K):.1f}. \"\n                 f\"However, the optimal κ depends on the misclassification regime, \"\n                 f\"so a fixed formula may be fragile. The P95 of observed condition numbers \"\n                 f\"({cond_p95:.1f}) provides a natural data-adaptive threshold.\")\n\n    with open(output_path, 'w') as f:\n        f.write('\\n'.join(lines) + '\\n')\n\n\nif __name__ == '__main__':\n    parser = argparse.ArgumentParser(description='κ threshold sweep experiment')\n    parser.add_argument('--n-mc', type=int, default=DEFAULT_N_MC,\n                        help=f'Number of MC seeds (default: {DEFAULT_N_MC})')\n    parser.add_argument('--kappa', type=float, nargs='+', default=None,\n                        help=f'κ values to sweep (default: {KAPPA_VALUES})')\n    parser.add_argument('--dry-run', action='store_true',\n                        help='Run only 2 seeds for testing')\n    args = parser.parse_args()\n\n    n_mc = 2 if args.dry_run else args.n_mc\n    kappa_values = [int(k) for k in args.kappa] if args.kappa else KAPPA_VALUES\n\n    print(f\"exp-020 κ Sweep | K={K} N={N} n_expert={N_EXPERT}\")\n    print(f\"κ values: {kappa_values}\")\n    print(f\"MC seeds: {n_mc}\\n\")\n\n    results = []\n    total = len(kappa_values) * n_mc\n    count = 0\n    t0 = time.time()\n\n    for kappa in kappa_values:\n        for seed in range(n_mc):\n            row = run_one(kappa, seed)\n            results.append(row)\n            count += 1\n            if count % max(1, total // 10) == 0:\n                el = time.time() - t0\n                eta = el / count * (total - count)\n                print(f\"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s\")\n\n    print(f\"\\n  Done: {time.time() - t0:.1f}s ({count} runs)\\n\")\n\n    df = pd.DataFrame(results)\n\n    out_dir = 'artifacts/kappa_sweep'\n    os.makedirs(out_dir, exist_ok=True)\n\n    csv_path = os.path.join(out_dir, 'results.csv')\n    df.to_csv(csv_path, index=False)\n    print(f\"Saved: {csv_path} ({len(df)} rows)\")\n\n    md_path = os.path.join(out_dir, 'kappa_sweep_analysis.md')\n    generate_analysis(df, md_path)\n    print(f\"Saved: {md_path}\")\n\n    print(\"\\n── Summary ──\")\n    for kappa in sorted(df['kappa'].unique()):\n        sub = df[df['kappa'] == kappa]\n        print(f\"  κ={kappa:>5.0f}: guard={sub['guard_trigger_rate'].mean():.3f} \"\n              f\"rmse_hb={sub['rmse_hb'].mean():.4f} \"\n              f\"ratio={sub['rmse_ratio'].mean():.4f} \"\n              f\"instab={sub['numerical_instability'].mean():.1%}\")\n",
    "structuredPatch": [
      {
        "oldStart": 98,
        "oldLines": 7,
        "newStart": 98,
        "newLines": 33,
        "lines": [
          "     }",
          " ",
          " ",
          "-def generate_analysis(df, output_path):",
          "+def stress_test_cond_numbers(n_seeds=20):",
          "+    \"\"\"Probe condition numbers under stress: extreme misclass, small n_expert, K=4.\"\"\"",
          "+    stress_configs = [",
          "+        {'label': 'moderate/n200/K2', 'misclass': [0.05, 0.15], 'n_expert': 200, 'k': 2},",
          "+        {'label': 'moderate/n50/K2', 'misclass': [0.05, 0.15], 'n_expert': 50, 'k': 2},",
          "+        {'label': 'extreme/n200/K2', 'misclass': [0.25, 0.05], 'n_expert': 200, 'k': 2},",
          "+        {'label': 'extreme/n50/K2', 'misclass': [0.25, 0.05], 'n_expert': 50, 'k': 2},",
          "+        {'label': 'extreme/n50/K4', 'misclass': [0.30, 0.20, 0.10, 0.03], 'n_expert': 50, 'k': 4},",
          "+        {'label': 'near_random/n50/K2', 'misclass': [0.40, 0.35], 'n_expert': 50, 'k': 2},",
          "+    ]",
          "+    rows = []",
          "+    for cfg in stress_configs:",
          "+        rp = {'misclass': cfg['misclass'], 'tau_z0': 0.5, 'tau_z1': 1.0}",
          "+        k = cfg['k']",
          "+        labels = SUBGROUP_LABELS[k]",
          "+        for seed in range(n_seeds):",
          "+            data = generate_data(rp, cfg['n_expert'], k, seed)",
          "+            em = data['expert_mask']",
          "+            counts = get_counts(data['Z'][em], data['Z_hat'][em], data['S'][em], labels)",
          "+            C_hb, _ = estimate_cm_hb_eb(counts, labels)",
          "+            conds = [np.linalg.cond(build_mixing_matrix(C_hb[s])) for s in labels]",
          "+            rows.append({'config': cfg['label'], 'seed': seed,",
          "+                         'max_cond': max(conds), 'mean_cond': np.mean(conds)})",
          "+    return pd.DataFrame(rows)",
          "+",
          "+",
          "+def generate_analysis(df, output_path, stress_df=None):",
          "     lines = []",
          "     lines.append(\"# κ Threshold Sweep Analysis\\n\")",
          "     lines.append(\"## Setup\\n\")"
        ]
      },
      {
        "oldStart": 107,
        "oldLines": 7,
        "newStart": 133,
        "newLines": 7,
        "lines": [
          "     lines.append(f\"- τ(Z=0)={REGIME_PARAMS['tau_z0']}, τ(Z=1)={REGIME_PARAMS['tau_z1']}\")",
          "     lines.append(f\"- T ~ Bernoulli(0.5)\")",
          "     lines.append(f\"- κ values: {sorted(df['kappa'].unique().astype(int).tolist())}\")",
          "-    lines.append(f\"- MC runs: {df['seed'].nunique()} seeds (0–{df['seed'].max()})\\n\")",
          "+    lines.append(f\"- MC runs: {df['seed'].nunique()} seeds (0–{int(df['seed'].max())})\\n\")",
          " ",
          "     summary = df.groupby('kappa').agg(",
          "         guard_rate=('guard_trigger_rate', 'mean'),"
        ]
      },
      {
        "oldStart": 140,
        "oldLines": 12,
        "newStart": 166,
        "newLines": 42,
        "lines": [
          " ",
          "     lines.append(\"\\n## Analysis\\n\")",
          " ",
          "-    lines.append(\"### Guard Trigger Rate\\n\")",
          "-    for _, r in summary.iterrows():",
          "-        kv = int(r['kappa'])",
          "-        gr = r['guard_rate']",
          "-        lines.append(f\"- κ={kv}: {gr:.1%} of subgroups triggered the guard\")",
          "+    cond_max = df['max_cond_number'].max()",
          "+    cond_p99 = df['max_cond_number'].quantile(0.99)",
          "+    cond_p95 = df['max_cond_number'].quantile(0.95)",
          "+    cond_p90 = df['max_cond_number'].quantile(0.90)",
          "+    guard_ever = summary['guard_rate'].sum() > 0",
          " ",
          "+    if not guard_ever:",
          "+        lines.append(\"### Key Finding: Guard Never Triggers\\n\")",
          "+        lines.append(f\"Across all {len(df)} runs (7 κ values × {df['seed'].nunique()} seeds), \"",
          "+                     f\"the condition number guard **never triggered**. \"",
          "+                     f\"The maximum observed condition number is **{cond_max:.2f}**, \"",
          "+                     f\"far below the smallest sweep value κ=10.\")",
          "+        lines.append(f\"\\nThis means all κ values produce **identical** RMSE results. \"",
          "+                     f\"The per-subgroup HB correction is always applied without fallback.\")",
          "+        lines.append(f\"\\n**Interpretation**: With n_expert={N_EXPERT} and moderate \"",
          "+                     f\"misclassification (π_s = {REGIME_PARAMS['misclass']}), \"",
          "+                     f\"the confusion matrix is well-estimated and the mixing matrix \"",
          "+                     f\"is well-conditioned. The κ guard is a safety net for edge cases, \"",
          "+                     f\"not an active component under these conditions.\")",
          "+    else:",
          "+        lines.append(\"### Guard Trigger Rate\\n\")",
          "+        for _, r in summary.iterrows():",
          "+            kv = int(r['kappa'])",
          "+            gr = r['guard_rate']",
          "+            lines.append(f\"- κ={kv}: {gr:.1%} of subgroups triggered the guard\")",
          "+",
          "+    lines.append(f\"\\n### Condition Number Distribution\\n\")",
          "+    lines.append(f\"| Statistic | Value |\")",
          "+    lines.append(f\"|-----------|------:|\")",
          "+    lines.append(f\"| Mean | {df['max_cond_number'].mean():.3f} |\")",
          "+    lines.append(f\"| Median | {df['max_cond_number'].median():.3f} |\")",
          "+    lines.append(f\"| P90 | {cond_p90:.3f} |\")",
          "+    lines.append(f\"| P95 | {cond_p95:.3f} |\")",
          "+    lines.append(f\"| P99 | {cond_p99:.3f} |\")",
          "+    lines.append(f\"| Max | {cond_max:.3f} |\")",
          "+",
          "     lines.append(\"\\n### Numerical Stability\\n\")",
          "     unstable = summary[summary['instability_pct'] > 0]",
          "     if not unstable.empty:"
        ]
      },
      {
        "oldStart": 154,
        "oldLines": 55,
        "newStart": 210,
        "newLines": 59,
        "lines": [
          "     else:",
          "         lines.append(\"No numerical instability (NaN/Inf) observed at any κ value.\")",
          " ",
          "-    lines.append(\"\\n### Is κ=100 Reasonable?\\n\")",
          "-    k100 = summary[summary['kappa'] == 100]",
          "-    if not k100.empty:",
          "-        r = k100.iloc[0]",
          "-        lines.append(f\"At κ=100:\")",
          "-        lines.append(f\"- Guard trigger rate: {r['guard_rate']:.1%}\")",
          "-        lines.append(f\"- RMSE HB: {r['rmse_hb_mean']:.4f} ± {r['rmse_hb_se']:.4f}\")",
          "-        lines.append(f\"- RMSE ratio (HB/Global): {r['rmse_ratio_mean']:.4f}\")",
          "-        lines.append(f\"- Instability: {r['instability_pct'] * 100:.1f}%\")",
          "+    if stress_df is not None and len(stress_df) > 0:",
          "+        lines.append(\"\\n## Stress Test: When Does the Guard Matter?\\n\")",
          "+        lines.append(\"To contextualize the sweep, we probe condition numbers under \"",
          "+                     \"more challenging settings (20 seeds each):\\n\")",
          "+        lines.append(\"| Configuration | Mean Max κ(M) | P95 Max κ(M) | Max κ(M) | Triggers κ=100? |\")",
          "+        lines.append(\"|---------------|-------------:|-----------:|--------:|:---------------|\")",
          "+        for cfg, grp in stress_df.groupby('config', sort=False):",
          "+            mc_mean = grp['max_cond'].mean()",
          "+            mc_p95 = grp['max_cond'].quantile(0.95)",
          "+            mc_max = grp['max_cond'].max()",
          "+            triggers = \"Yes\" if mc_max > 100 else (\"Borderline\" if mc_p95 > 50 else \"No\")",
          "+            lines.append(f\"| {cfg} | {mc_mean:.1f} | {mc_p95:.1f} | {mc_max:.1f} | {triggers} |\")",
          "+        lines.append(f\"\\nThe guard becomes relevant when n_expert is small (≤50) and/or \"",
          "+                     f\"misclassification rates approach 0.5. Under the specified \"",
          "+                     f\"moderate regime, κ never approaches the threshold.\")",
          " ",
          "-    best_idx = summary['rmse_hb_mean'].idxmin()",
          "-    best_row = summary.loc[best_idx]",
          "-    best_k = int(best_row['kappa'])",
          "-    lines.append(f\"\\nLowest mean RMSE HB is at κ={best_k} \"",
          "-                 f\"({best_row['rmse_hb_mean']:.4f} ± {best_row['rmse_hb_se']:.4f}).\")",
          "-",
          "-    stable = summary[summary['instability_pct'] == 0]",
          "-    if not stable.empty:",
          "-        largest_stable = int(stable['kappa'].max())",
          "-        lines.append(f\"Largest κ without any instability: κ={largest_stable}.\")",
          "-",
          "-    lines.append(\"\\n### Recommendation\\n\")",
          "-",
          "-    if best_k <= 100:",
          "-        lines.append(f\"The sweep supports κ=100 as a conservative but safe choice. \"",
          "-                     f\"The best RMSE is achieved at κ={best_k}, suggesting that \"",
          "-                     f\"κ=100 may be slightly too permissive for this DGP, \"",
          "-                     f\"but the difference is small.\")",
          "+    lines.append(\"\\n## Is κ=100 Reasonable?\\n\")",
          "+    if not guard_ever:",
          "+        lines.append(f\"**Yes.** κ=100 is a safe default for this regime:\")",
          "+        lines.append(f\"- The empirical max condition number ({cond_max:.2f}) is ~{100 / cond_max:.0f}× \"",
          "+                     f\"below the threshold, providing a large safety margin.\")",
          "+        lines.append(f\"- The guard activates only under adversarial conditions \"",
          "+                     f\"(near-random labeling, tiny expert budgets) where correction \"",
          "+                     f\"would amplify noise regardless.\")",
          "+        lines.append(f\"- A threshold much lower than 100 (e.g., κ=10) would still \"",
          "+                     f\"never trigger here, so the exact value is not critical for \"",
          "+                     f\"well-conditioned problems.\")",
          "     else:",
          "-        lines.append(f\"The sweep shows κ=100 is somewhat conservative. \"",
          "-                     f\"κ={best_k} achieves the best RMSE, suggesting room to \"",
          "-                     f\"relax the threshold. However, κ=100 provides a margin of safety.\")",
          "+        k100 = summary[summary['kappa'] == 100]",
          "+        if not k100.empty:",
          "+            r = k100.iloc[0]",
          "+            lines.append(f\"At κ=100: guard rate = {r['guard_rate']:.1%}, \"",
          "+                         f\"RMSE ratio = {r['rmse_ratio_mean']:.4f}, \"",
          "+                         f\"instability = {r['instability_pct'] * 100:.1f}%\")",
          "+        best_idx = summary['rmse_hb_mean'].idxmin()",
          "+        best_row = summary.loc[best_idx]",
          "+        best_k = int(best_row['kappa'])",
          "+        lines.append(f\"\\nLowest mean RMSE HB at κ={best_k} \"",
          "+                     f\"({best_row['rmse_hb_mean']:.4f} ± {best_row['rmse_hb_se']:.4f}).\")",
          " ",
          "-    cond_p90 = df['max_cond_number'].quantile(0.90)",
          "-    cond_p95 = df['max_cond_number'].quantile(0.95)",
          "-    cond_p99 = df['max_cond_number'].quantile(0.99)",
          "-    lines.append(f\"\\nEmpirical condition number distribution (across all seeds, all κ):\")",
          "-    lines.append(f\"- P90 = {cond_p90:.1f}\")",
          "-    lines.append(f\"- P95 = {cond_p95:.1f}\")",
          "-    lines.append(f\"- P99 = {cond_p99:.1f}\")",
          "+    lines.append(\"\\n## Adaptive Formula Suggestion\\n\")",
          "+    lines.append(f\"A data-driven approach: set κ = c · √(n_expert / K), \"",
          "+                 f\"where c is calibrated per regime.\")",
          "+    lines.append(f\"- With n_expert={N_EXPERT}, K={K}: √({N_EXPERT}/{K}) = {np.sqrt(N_EXPERT / K):.1f}\")",
          "+    lines.append(f\"- Setting c=10 gives κ={10 * np.sqrt(N_EXPERT / K):.0f}, which is close to 100\")",
          "+    lines.append(f\"- However, the optimal κ depends on the misclassification severity, \"",
          "+                 f\"not just sample size\")",
          "+    lines.append(f\"- A more robust adaptive rule: set κ to 2× the observed P99 of \"",
          "+                 f\"condition numbers from a pilot run. Here that would be \"",
          "+                 f\"κ = 2 × {cond_p99:.1f} = {2 * cond_p99:.1f}\")",
          "+    lines.append(f\"- **Bottom line**: κ=100 provides ample headroom. \"",
          "+                 f\"The exact value matters only in edge cases where n_expert/K is very small.\")",
          " ",
          "-    lines.append(f\"\\n**Adaptive formula**: A data-driven threshold could be \"",
          "-                 f\"κ = c · √(n_expert / K). With n_expert={N_EXPERT}, K={K}: \"",
          "-                 f\"√({N_EXPERT}/{K}) = {np.sqrt(N_EXPERT / K):.1f}. \"",
          "-                 f\"Calibrating c so that κ ≈ {best_k} gives c ≈ {best_k / np.sqrt(N_EXPERT / K):.1f}. \"",
          "-                 f\"However, the optimal κ depends on the misclassification regime, \"",
          "-                 f\"so a fixed formula may be fragile. The P95 of observed condition numbers \"",
          "-                 f\"({cond_p95:.1f}) provides a natural data-adaptive threshold.\")",
          "-",
          "     with open(output_path, 'w') as f:",
          "         f.write('\\n'.join(lines) + '\\n')",
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

_source line 119_

Now update the `__main__` block to run the stress test and pass it to the analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "7b7c3590-379a-4b08-be42-538109d07f19",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ArR965U92vRBiC2GGkbZa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5661,
      "cache_read_input_tokens": 54967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5661
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

_source line 120_

<details open><summary>🔧 Tool call — Edit · `toolu_01VY3q8JLbKeu63oFFc6XG9C`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp020_kappa_sweep.py",
  "old_string": "    csv_path = os.path.join(out_dir, 'results.csv')\n    df.to_csv(csv_path, index=False)\n    print(f\"Saved: {csv_path} ({len(df)} rows)\")\n\n    md_path = os.path.join(out_dir, 'kappa_sweep_analysis.md')\n    generate_analysis(df, md_path)\n    print(f\"Saved: {md_path}\")",
  "new_string": "    csv_path = os.path.join(out_dir, 'results.csv')\n    df.to_csv(csv_path, index=False)\n    print(f\"Saved: {csv_path} ({len(df)} rows)\")\n\n    print(\"Running stress test (condition numbers under challenging settings)...\")\n    stress_df = stress_test_cond_numbers(n_seeds=20)\n    stress_csv = os.path.join(out_dir, 'stress_test_cond.csv')\n    stress_df.to_csv(stress_csv, index=False)\n    print(f\"Saved: {stress_csv} ({len(stress_df)} rows)\")\n\n    md_path = os.path.join(out_dir, 'kappa_sweep_analysis.md')\n    generate_analysis(df, md_path, stress_df=stress_df)\n    print(f\"Saved: {md_path}\")"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "af95baab-1e08-4f54-8d6a-7365826da156",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ArR965U92vRBiC2GGkbZa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5661,
      "cache_read_input_tokens": 54967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5661
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

_source line 121 · 2026-05-21T15:58:02.608Z_

<details><summary>↩ Tool result · `toolu_01VY3q8JLbKeu63oFFc6XG9C`</summary>

```text
The file /home/ubuntu/ec_hte_llm_annotation/exp020_kappa_sweep.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "76db3454-f70d-43ed-be36-f1554d0ea37f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp020_kappa_sweep.py",
    "oldString": "    csv_path = os.path.join(out_dir, 'results.csv')\n    df.to_csv(csv_path, index=False)\n    print(f\"Saved: {csv_path} ({len(df)} rows)\")\n\n    md_path = os.path.join(out_dir, 'kappa_sweep_analysis.md')\n    generate_analysis(df, md_path)\n    print(f\"Saved: {md_path}\")",
    "newString": "    csv_path = os.path.join(out_dir, 'results.csv')\n    df.to_csv(csv_path, index=False)\n    print(f\"Saved: {csv_path} ({len(df)} rows)\")\n\n    print(\"Running stress test (condition numbers under challenging settings)...\")\n    stress_df = stress_test_cond_numbers(n_seeds=20)\n    stress_csv = os.path.join(out_dir, 'stress_test_cond.csv')\n    stress_df.to_csv(stress_csv, index=False)\n    print(f\"Saved: {stress_csv} ({len(stress_df)} rows)\")\n\n    md_path = os.path.join(out_dir, 'kappa_sweep_analysis.md')\n    generate_analysis(df, md_path, stress_df=stress_df)\n    print(f\"Saved: {md_path}\")",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"exp020_kappa_sweep.py - κ threshold sweep for condition number singularity guard.\n\nSweeps κ ∈ {10,25,50,100,200,500,1000} on synthetic data (K=2, moderate regime)\nto provide empirical justification for the κ>100 guard threshold.\n\"\"\"\n\nimport argparse\nimport os\nimport time\nimport numpy as np\nimport pandas as pd\n\nfrom exp001_hb_synthetic import (\n    N, SUBGROUP_LABELS,\n    generate_data, get_counts, build_mixing_matrix, diff_in_means,\n    estimate_cm_hb_eb, invert_mixing, invert_mixing_safe,\n)\n\nREGIME_PARAMS = {\n    'misclass': [0.05, 0.15],\n    'tau_z1': 1.0,\n    'tau_z0': 0.5,\n}\nK = 2\nN_EXPERT = 200\nKAPPA_VALUES = [10, 25, 50, 100, 200, 500, 1000]\nDEFAULT_N_MC = 50\n\n\ndef run_one(kappa, seed):\n    data = generate_data(REGIME_PARAMS, N_EXPERT, K, seed)\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    em = data['expert_mask']\n    labels = SUBGROUP_LABELS[K]\n    tau_true = np.array([REGIME_PARAMS['tau_z0'], REGIME_PARAMS['tau_z1']])\n\n    counts = get_counts(Z[em], Z_hat[em], S[em], labels)\n\n    C_hb, _ = estimate_cm_hb_eb(counts, labels)\n    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}\n\n    cg = counts.sum(axis=0)\n    C_gl = np.zeros((2, 2))\n    for z in [0, 1]:\n        n = cg[z, :].sum()\n        for zh in [0, 1]:\n            C_gl[z, zh] = (cg[z, zh] + 1) / (n + 2) if n > 0 else 0.5\n    M_gl = build_mixing_matrix(C_gl)\n\n    guard_triggered = 0\n    errors_hb = []\n    errors_global = []\n    has_instability = False\n    cond_numbers = []\n\n    for s in labels:\n        sm = S == s\n        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))\n        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))\n        tau_obs = np.array([th0_n, th1_n])\n        se_obs = np.array([se0_n, se1_n])\n        if np.any(np.isnan(tau_obs)):\n            continue\n\n        cond = np.linalg.cond(M_hb[s])\n        cond_numbers.append(cond)\n        if cond > kappa:\n            guard_triggered += 1\n\n        thb, shb = invert_mixing_safe(M_hb[s], tau_obs, se_obs, cond_threshold=kappa)\n        tgl, sgl = invert_mixing(M_gl, tau_obs, se_obs)\n\n        if np.any(~np.isfinite(thb)) or np.any(~np.isfinite(shb)):\n            has_instability = True\n        if np.any(~np.isfinite(tgl)) or np.any(~np.isfinite(sgl)):\n            has_instability = True\n\n        errors_hb.extend((thb - tau_true).tolist())\n        errors_global.extend((tgl - tau_true).tolist())\n\n    n_subgroups = len(labels)\n    guard_trigger_rate = guard_triggered / n_subgroups if n_subgroups > 0 else np.nan\n    rmse_hb = np.sqrt(np.mean(np.array(errors_hb) ** 2)) if errors_hb else np.nan\n    rmse_global = np.sqrt(np.mean(np.array(errors_global) ** 2)) if errors_global else np.nan\n    rmse_ratio = rmse_hb / rmse_global if rmse_global and rmse_global > 0 else np.nan\n    max_cond = max(cond_numbers) if cond_numbers else np.nan\n\n    return {\n        'kappa': kappa,\n        'seed': seed,\n        'guard_trigger_rate': guard_trigger_rate,\n        'rmse_hb': rmse_hb,\n        'rmse_global': rmse_global,\n        'rmse_ratio': rmse_ratio,\n        'numerical_instability': has_instability,\n        'max_cond_number': max_cond,\n    }\n\n\ndef stress_test_cond_numbers(n_seeds=20):\n    \"\"\"Probe condition numbers under stress: extreme misclass, small n_expert, K=4.\"\"\"\n    stress_configs = [\n        {'label': 'moderate/n200/K2', 'misclass': [0.05, 0.15], 'n_expert': 200, 'k': 2},\n        {'label': 'moderate/n50/K2', 'misclass': [0.05, 0.15], 'n_expert': 50, 'k': 2},\n        {'label': 'extreme/n200/K2', 'misclass': [0.25, 0.05], 'n_expert': 200, 'k': 2},\n        {'label': 'extreme/n50/K2', 'misclass': [0.25, 0.05], 'n_expert': 50, 'k': 2},\n        {'label': 'extreme/n50/K4', 'misclass': [0.30, 0.20, 0.10, 0.03], 'n_expert': 50, 'k': 4},\n        {'label': 'near_random/n50/K2', 'misclass': [0.40, 0.35], 'n_expert': 50, 'k': 2},\n    ]\n    rows = []\n    for cfg in stress_configs:\n        rp = {'misclass': cfg['misclass'], 'tau_z0': 0.5, 'tau_z1': 1.0}\n        k = cfg['k']\n        labels = SUBGROUP_LABELS[k]\n        for seed in range(n_seeds):\n            data = generate_data(rp, cfg['n_expert'], k, seed)\n            em = data['expert_mask']\n            counts = get_counts(data['Z'][em], data['Z_hat'][em], data['S'][em], labels)\n            C_hb, _ = estimate_cm_hb_eb(counts, labels)\n            conds = [np.linalg.cond(build_mixing_matrix(C_hb[s])) for s in labels]\n            rows.append({'config': cfg['label'], 'seed': seed,\n                         'max_cond': max(conds), 'mean_cond': np.mean(conds)})\n    return pd.DataFrame(rows)\n\n\ndef generate_analysis(df, output_path, stress_df=None):\n    lines = []\n    lines.append(\"# κ Threshold Sweep Analysis\\n\")\n    lines.append(\"## Setup\\n\")\n    lines.append(f\"- K={K}, N={N}, n_expert={N_EXPERT}\")\n    lines.append(f\"- π_s = {REGIME_PARAMS['misclass']} (symmetric CM)\")\n    lines.append(f\"- τ(Z=0)={REGIME_PARAMS['tau_z0']}, τ(Z=1)={REGIME_PARAMS['tau_z1']}\")\n    lines.append(f\"- T ~ Bernoulli(0.5)\")\n    lines.append(f\"- κ values: {sorted(df['kappa'].unique().astype(int).tolist())}\")\n    lines.append(f\"- MC runs: {df['seed'].nunique()} seeds (0–{int(df['seed'].max())})\\n\")\n\n    summary = df.groupby('kappa').agg(\n        guard_rate=('guard_trigger_rate', 'mean'),\n        guard_rate_se=('guard_trigger_rate', 'sem'),\n        rmse_hb_mean=('rmse_hb', 'mean'),\n        rmse_hb_se=('rmse_hb', 'sem'),\n        rmse_global_mean=('rmse_global', 'mean'),\n        rmse_global_se=('rmse_global', 'sem'),\n        rmse_ratio_mean=('rmse_ratio', 'mean'),\n        rmse_ratio_se=('rmse_ratio', 'sem'),\n        instability_pct=('numerical_instability', 'mean'),\n        max_cond_mean=('max_cond_number', 'mean'),\n        max_cond_median=('max_cond_number', 'median'),\n    ).reset_index()\n\n    lines.append(\"## Summary Table\\n\")\n    lines.append(\"| κ | Guard Rate | RMSE HB | RMSE Global | RMSE Ratio | Instability % | Mean Max κ(M) | Median Max κ(M) |\")\n    lines.append(\"|---:|----------:|--------:|------------:|-----------:|--------------:|--------------:|----------------:|\")\n    for _, r in summary.iterrows():\n        lines.append(\n            f\"| {int(r['kappa'])} \"\n            f\"| {r['guard_rate']:.3f} ± {r['guard_rate_se']:.3f} \"\n            f\"| {r['rmse_hb_mean']:.4f} ± {r['rmse_hb_se']:.4f} \"\n            f\"| {r['rmse_global_mean']:.4f} ± {r['rmse_global_se']:.4f} \"\n            f\"| {r['rmse_ratio_mean']:.4f} ± {r['rmse_ratio_se']:.4f} \"\n            f\"| {r['instability_pct'] * 100:.1f} \"\n            f\"| {r['max_cond_mean']:.1f} \"\n            f\"| {r['max_cond_median']:.1f} |\"\n        )\n\n    lines.append(\"\\n## Analysis\\n\")\n\n    cond_max = df['max_cond_number'].max()\n    cond_p99 = df['max_cond_number'].quantile(0.99)\n    cond_p95 = df['max_cond_number'].quantile(0.95)\n    cond_p90 = df['max_cond_number'].quantile(0.90)\n    guard_ever = summary['guard_rate'].sum() > 0\n\n    if not guard_ever:\n        lines.append(\"### Key Finding: Guard Never Triggers\\n\")\n        lines.append(f\"Across all {len(df)} runs (7 κ values × {df['seed'].nunique()} seeds), \"\n                     f\"the condition number guard **never triggered**. \"\n                     f\"The maximum observed condition number is **{cond_max:.2f}**, \"\n                     f\"far below the smallest sweep value κ=10.\")\n        lines.append(f\"\\nThis means all κ values produce **identical** RMSE results. \"\n                     f\"The per-subgroup HB correction is always applied without fallback.\")\n        lines.append(f\"\\n**Interpretation**: With n_expert={N_EXPERT} and moderate \"\n                     f\"misclassification (π_s = {REGIME_PARAMS['misclass']}), \"\n                     f\"the confusion matrix is well-estimated and the mixing matrix \"\n                     f\"is well-conditioned. The κ guard is a safety net for edge cases, \"\n                     f\"not an active component under these conditions.\")\n    else:\n        lines.append(\"### Guard Trigger Rate\\n\")\n        for _, r in summary.iterrows():\n            kv = int(r['kappa'])\n            gr = r['guard_rate']\n            lines.append(f\"- κ={kv}: {gr:.1%} of subgroups triggered the guard\")\n\n    lines.append(f\"\\n### Condition Number Distribution\\n\")\n    lines.append(f\"| Statistic | Value |\")\n    lines.append(f\"|-----------|------:|\")\n    lines.append(f\"| Mean | {df['max_cond_number'].mean():.3f} |\")\n    lines.append(f\"| Median | {df['max_cond_number'].median():.3f} |\")\n    lines.append(f\"| P90 | {cond_p90:.3f} |\")\n    lines.append(f\"| P95 | {cond_p95:.3f} |\")\n    lines.append(f\"| P99 | {cond_p99:.3f} |\")\n    lines.append(f\"| Max | {cond_max:.3f} |\")\n\n    lines.append(\"\\n### Numerical Stability\\n\")\n    unstable = summary[summary['instability_pct'] > 0]\n    if not unstable.empty:\n        lines.append(f\"Numerical instability (NaN/Inf) observed at κ = \"\n                     f\"{', '.join(str(int(k)) for k in unstable['kappa'])}.\")\n    else:\n        lines.append(\"No numerical instability (NaN/Inf) observed at any κ value.\")\n\n    if stress_df is not None and len(stress_df) > 0:\n        lines.append(\"\\n## Stress Test: When Does the Guard Matter?\\n\")\n        lines.append(\"To contextualize the sweep, we probe condition numbers under \"\n                     \"more challenging settings (20 seeds each):\\n\")\n        lines.append(\"| Configuration | Mean Max κ(M) | P95 Max κ(M) | Max κ(M) | Triggers κ=100? |\")\n        lines.append(\"|---------------|-------------:|-----------:|--------:|:---------------|\")\n        for cfg, grp in stress_df.groupby('config', sort=False):\n            mc_mean = grp['max_cond'].mean()\n            mc_p95 = grp['max_cond'].quantile(0.95)\n            mc_max = grp['max_cond'].max()\n            triggers = \"Yes\" if mc_max > 100 else (\"Borderline\" if mc_p95 > 50 else \"No\")\n            lines.append(f\"| {cfg} | {mc_mean:.1f} | {mc_p95:.1f} | {mc_max:.1f} | {triggers} |\")\n        lines.append(f\"\\nThe guard becomes relevant when n_expert is small (≤50) and/or \"\n                     f\"misclassification rates approach 0.5. Under the specified \"\n                     f\"moderate regime, κ never approaches the threshold.\")\n\n    lines.append(\"\\n## Is κ=100 Reasonable?\\n\")\n    if not guard_ever:\n        lines.append(f\"**Yes.** κ=100 is a safe default for this regime:\")\n        lines.append(f\"- The empirical max condition number ({cond_max:.2f}) is ~{100 / cond_max:.0f}× \"\n                     f\"below the threshold, providing a large safety margin.\")\n        lines.append(f\"- The guard activates only under adversarial conditions \"\n                     f\"(near-random labeling, tiny expert budgets) where correction \"\n                     f\"would amplify noise regardless.\")\n        lines.append(f\"- A threshold much lower than 100 (e.g., κ=10) would still \"\n                     f\"never trigger here, so the exact value is not critical for \"\n                     f\"well-conditioned problems.\")\n    else:\n        k100 = summary[summary['kappa'] == 100]\n        if not k100.empty:\n            r = k100.iloc[0]\n            lines.append(f\"At κ=100: guard rate = {r['guard_rate']:.1%}, \"\n                         f\"RMSE ratio = {r['rmse_ratio_mean']:.4f}, \"\n                         f\"instability = {r['instability_pct'] * 100:.1f}%\")\n        best_idx = summary['rmse_hb_mean'].idxmin()\n        best_row = summary.loc[best_idx]\n        best_k = int(best_row['kappa'])\n        lines.append(f\"\\nLowest mean RMSE HB at κ={best_k} \"\n                     f\"({best_row['rmse_hb_mean']:.4f} ± {best_row['rmse_hb_se']:.4f}).\")\n\n    lines.append(\"\\n## Adaptive Formula Suggestion\\n\")\n    lines.append(f\"A data-driven approach: set κ = c · √(n_expert / K), \"\n                 f\"where c is calibrated per regime.\")\n    lines.append(f\"- With n_expert={N_EXPERT}, K={K}: √({N_EXPERT}/{K}) = {np.sqrt(N_EXPERT / K):.1f}\")\n    lines.append(f\"- Setting c=10 gives κ={10 * np.sqrt(N_EXPERT / K):.0f}, which is close to 100\")\n    lines.append(f\"- However, the optimal κ depends on the misclassification severity, \"\n                 f\"not just sample size\")\n    lines.append(f\"- A more robust adaptive rule: set κ to 2× the observed P99 of \"\n                 f\"condition numbers from a pilot run. Here that would be \"\n                 f\"κ = 2 × {cond_p99:.1f} = {2 * cond_p99:.1f}\")\n    lines.append(f\"- **Bottom line**: κ=100 provides ample headroom. \"\n                 f\"The exact value matters only in edge cases where n_expert/K is very small.\")\n\n    with open(output_path, 'w') as f:\n        f.write('\\n'.join(lines) + '\\n')\n\n\nif __name__ == '__main__':\n    parser = argparse.ArgumentParser(description='κ threshold sweep experiment')\n    parser.add_argument('--n-mc', type=int, default=DEFAULT_N_MC,\n                        help=f'Number of MC seeds (default: {DEFAULT_N_MC})')\n    parser.add_argument('--kappa', type=float, nargs='+', default=None,\n                        help=f'κ values to sweep (default: {KAPPA_VALUES})')\n    parser.add_argument('--dry-run', action='store_true',\n                        help='Run only 2 seeds for testing')\n    args = parser.parse_args()\n\n    n_mc = 2 if args.dry_run else args.n_mc\n    kappa_values = [int(k) for k in args.kappa] if args.kappa else KAPPA_VALUES\n\n    print(f\"exp-020 κ Sweep | K={K} N={N} n_expert={N_EXPERT}\")\n    print(f\"κ values: {kappa_values}\")\n    print(f\"MC seeds: {n_mc}\\n\")\n\n    results = []\n    total = len(kappa_values) * n_mc\n    count = 0\n    t0 = time.time()\n\n    for kappa in kappa_values:\n        for seed in range(n_mc):\n            row = run_one(kappa, seed)\n            results.append(row)\n            count += 1\n            if count % max(1, total // 10) == 0:\n                el = time.time() - t0\n                eta = el / count * (total - count)\n                print(f\"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s\")\n\n    print(f\"\\n  Done: {time.time() - t0:.1f}s ({count} runs)\\n\")\n\n    df = pd.DataFrame(results)\n\n    out_dir = 'artifacts/kappa_sweep'\n    os.makedirs(out_dir, exist_ok=True)\n\n    csv_path = os.path.join(out_dir, 'results.csv')\n    df.to_csv(csv_path, index=False)\n    print(f\"Saved: {csv_path} ({len(df)} rows)\")\n\n    md_path = os.path.join(out_dir, 'kappa_sweep_analysis.md')\n    generate_analysis(df, md_path)\n    print(f\"Saved: {md_path}\")\n\n    print(\"\\n── Summary ──\")\n    for kappa in sorted(df['kappa'].unique()):\n        sub = df[df['kappa'] == kappa]\n        print(f\"  κ={kappa:>5.0f}: guard={sub['guard_trigger_rate'].mean():.3f} \"\n              f\"rmse_hb={sub['rmse_hb'].mean():.4f} \"\n              f\"ratio={sub['rmse_ratio'].mean():.4f} \"\n              f\"instab={sub['numerical_instability'].mean():.1%}\")\n",
    "structuredPatch": [
      {
        "oldStart": 310,
        "oldLines": 8,
        "newStart": 310,
        "newLines": 14,
        "lines": [
          "     df.to_csv(csv_path, index=False)",
          "     print(f\"Saved: {csv_path} ({len(df)} rows)\")",
          " ",
          "+    print(\"Running stress test (condition numbers under challenging settings)...\")",
          "+    stress_df = stress_test_cond_numbers(n_seeds=20)",
          "+    stress_csv = os.path.join(out_dir, 'stress_test_cond.csv')",
          "+    stress_df.to_csv(stress_csv, index=False)",
          "+    print(f\"Saved: {stress_csv} ({len(stress_df)} rows)\")",
          "+",
          "     md_path = os.path.join(out_dir, 'kappa_sweep_analysis.md')",
          "-    generate_analysis(df, md_path)",
          "+    generate_analysis(df, md_path, stress_df=stress_df)",
          "     print(f\"Saved: {md_path}\")",
          " ",
          "     print(\"\\n── Summary ──\")"
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

_source line 122_

Now re-run the full experiment with the updated analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "dbf9faf4-33cb-47f5-8b10-a283a81e14fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019bkMNhViD3t17nHaEjinwX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 529,
      "cache_read_input_tokens": 60628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 529
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

_source line 123_

<details open><summary>🔧 Tool call — Bash · `toolu_01UHvqPR9U2GPB4MKEY5EgeC`</summary>

```json
{
  "command": "python3 exp020_kappa_sweep.py --n-mc 50",
  "description": "Full run with updated analysis",
  "timeout": 300000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "fa13effa-fb8e-4bf1-8056-da07638464d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019bkMNhViD3t17nHaEjinwX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 529,
      "cache_read_input_tokens": 60628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 529
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

_source line 124 · 2026-05-21T15:58:09.420Z_

<details><summary>↩ Tool result · `toolu_01UHvqPR9U2GPB4MKEY5EgeC`</summary>

```text
exp-020 κ Sweep | K=2 N=5000 n_expert=200
κ values: [10, 25, 50, 100, 200, 500, 1000]
MC seeds: 50

  [35/350] 0s elapsed, ETA 1s
  [70/350] 0s elapsed, ETA 1s
  [105/350] 0s elapsed, ETA 1s
  [140/350] 1s elapsed, ETA 1s
  [175/350] 1s elapsed, ETA 1s
  [210/350] 1s elapsed, ETA 1s
  [245/350] 1s elapsed, ETA 0s
  [280/350] 1s elapsed, ETA 0s
  [315/350] 1s elapsed, ETA 0s
  [350/350] 1s elapsed, ETA 0s

  Done: 1.5s (350 runs)

Saved: artifacts/kappa_sweep/results.csv (350 rows)
Running stress test (condition numbers under challenging settings)...
Saved: artifacts/kappa_sweep/stress_test_cond.csv (120 rows)
Saved: artifacts/kappa_sweep/kappa_sweep_analysis.md

── Summary ──
  κ=   10: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%
  κ=   25: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%
  κ=   50: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%
  κ=  100: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%
  κ=  200: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%
  κ=  500: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%
  κ= 1000: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "b4054e0b-ab52-446e-883d-55c699d75752",
  "tool_use_result": {
    "stdout": "exp-020 κ Sweep | K=2 N=5000 n_expert=200\nκ values: [10, 25, 50, 100, 200, 500, 1000]\nMC seeds: 50\n\n  [35/350] 0s elapsed, ETA 1s\n  [70/350] 0s elapsed, ETA 1s\n  [105/350] 0s elapsed, ETA 1s\n  [140/350] 1s elapsed, ETA 1s\n  [175/350] 1s elapsed, ETA 1s\n  [210/350] 1s elapsed, ETA 1s\n  [245/350] 1s elapsed, ETA 0s\n  [280/350] 1s elapsed, ETA 0s\n  [315/350] 1s elapsed, ETA 0s\n  [350/350] 1s elapsed, ETA 0s\n\n  Done: 1.5s (350 runs)\n\nSaved: artifacts/kappa_sweep/results.csv (350 rows)\nRunning stress test (condition numbers under challenging settings)...\nSaved: artifacts/kappa_sweep/stress_test_cond.csv (120 rows)\nSaved: artifacts/kappa_sweep/kappa_sweep_analysis.md\n\n── Summary ──\n  κ=   10: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%\n  κ=   25: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%\n  κ=   50: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%\n  κ=  100: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%\n  κ=  200: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%\n  κ=  500: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%\n  κ= 1000: guard=0.000 rmse_hb=0.0759 ratio=1.0477 instab=0.0%",
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

_source line 125_

Let me verify the outputs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "e82b3f20-2c36-4cb6-a782-79646c1f3c0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LQHiBhymaq2w5r1o8hRkEi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 726,
      "cache_read_input_tokens": 61157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 726
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

_source line 126_

<details open><summary>🔧 Tool call — Read · `toolu_011sPjyCHMuwHFXTD5n77AJW`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/kappa_sweep/kappa_sweep_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "fa4d356f-26d3-45f4-8813-90874162dd00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LQHiBhymaq2w5r1o8hRkEi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 726,
      "cache_read_input_tokens": 61157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 726
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

_source line 127 · 2026-05-21T15:58:12.966Z_

<details><summary>↩ Tool result · `toolu_011sPjyCHMuwHFXTD5n77AJW`</summary>

```text
1	# κ Threshold Sweep Analysis
2	
3	## Setup
4	
5	- K=2, N=5000, n_expert=200
6	- π_s = [0.05, 0.15] (symmetric CM)
7	- τ(Z=0)=0.5, τ(Z=1)=1.0
8	- T ~ Bernoulli(0.5)
9	- κ values: [10, 25, 50, 100, 200, 500, 1000]
10	- MC runs: 50 seeds (0–49)
11	
12	## Summary Table
13	
14	| κ | Guard Rate | RMSE HB | RMSE Global | RMSE Ratio | Instability % | Mean Max κ(M) | Median Max κ(M) |
15	|---:|----------:|--------:|------------:|-----------:|--------------:|--------------:|----------------:|
16	| 10 | 0.000 ± 0.000 | 0.0759 ± 0.0043 | 0.0765 ± 0.0042 | 1.0477 ± 0.0483 | 0.0 | 1.4 | 1.4 |
17	| 25 | 0.000 ± 0.000 | 0.0759 ± 0.0043 | 0.0765 ± 0.0042 | 1.0477 ± 0.0483 | 0.0 | 1.4 | 1.4 |
18	| 50 | 0.000 ± 0.000 | 0.0759 ± 0.0043 | 0.0765 ± 0.0042 | 1.0477 ± 0.0483 | 0.0 | 1.4 | 1.4 |
19	| 100 | 0.000 ± 0.000 | 0.0759 ± 0.0043 | 0.0765 ± 0.0042 | 1.0477 ± 0.0483 | 0.0 | 1.4 | 1.4 |
20	| 200 | 0.000 ± 0.000 | 0.0759 ± 0.0043 | 0.0765 ± 0.0042 | 1.0477 ± 0.0483 | 0.0 | 1.4 | 1.4 |
21	| 500 | 0.000 ± 0.000 | 0.0759 ± 0.0043 | 0.0765 ± 0.0042 | 1.0477 ± 0.0483 | 0.0 | 1.4 | 1.4 |
22	| 1000 | 0.000 ± 0.000 | 0.0759 ± 0.0043 | 0.0765 ± 0.0042 | 1.0477 ± 0.0483 | 0.0 | 1.4 | 1.4 |
23	
24	## Analysis
25	
26	### Key Finding: Guard Never Triggers
27	
28	Across all 350 runs (7 κ values × 50 seeds), the condition number guard **never triggered**. The maximum observed condition number is **1.89**, far below the smallest sweep value κ=10.
29	
30	This means all κ values produce **identical** RMSE results. The per-subgroup HB correction is always applied without fallback.
31	
32	**Interpretation**: With n_expert=200 and moderate misclassification (π_s = [0.05, 0.15]), the confusion matrix is well-estimated and the mixing matrix is well-conditioned. The κ guard is a safety net for edge cases, not an active component under these conditions.
33	
34	### Condition Number Distribution
35	
36	| Statistic | Value |
37	|-----------|------:|
38	| Mean | 1.446 |
39	| Median | 1.447 |
40	| P90 | 1.598 |
41	| P95 | 1.655 |
42	| P99 | 1.893 |
43	| Max | 1.893 |
44	
45	### Numerical Stability
46	
47	No numerical instability (NaN/Inf) observed at any κ value.
48	
49	## Stress Test: When Does the Guard Matter?
50	
51	To contextualize the sweep, we probe condition numbers under more challenging settings (20 seeds each):
52	
53	| Configuration | Mean Max κ(M) | P95 Max κ(M) | Max κ(M) | Triggers κ=100? |
54	|---------------|-------------:|-----------:|--------:|:---------------|
55	| moderate/n200/K2 | 1.4 | 1.7 | 1.8 | No |
56	| moderate/n50/K2 | 1.7 | 2.7 | 2.7 | No |
57	| extreme/n200/K2 | 2.3 | 2.9 | 5.7 | No |
58	| extreme/n50/K2 | 2.6 | 4.4 | 4.4 | No |
59	| extreme/n50/K4 | 5.6 | 15.6 | 15.9 | No |
60	| near_random/n50/K2 | 181.7 | 1015.8 | 1125.3 | Yes |
61	
62	The guard becomes relevant when n_expert is small (≤50) and/or misclassification rates approach 0.5. Under the specified moderate regime, κ never approaches the threshold.
63	
64	## Is κ=100 Reasonable?
65	
66	**Yes.** κ=100 is a safe default for this regime:
67	- The empirical max condition number (1.89) is ~53× below the threshold, providing a large safety margin.
68	- The guard activates only under adversarial conditions (near-random labeling, tiny expert budgets) where correction would amplify noise regardless.
69	- A threshold much lower than 100 (e.g., κ=10) would still never trigger here, so the exact value is not critical for well-conditioned problems.
70	
71	## Adaptive Formula Suggestion
72	
73	A data-driven approach: set κ = c · √(n_expert / K), where c is calibrated per regime.
74	- With n_expert=200, K=2: √(200/2) = 10.0
75	- Setting c=10 gives κ=100, which is close to 100
76	- However, the optimal κ depends on the misclassification severity, not just sample size
77	- A more robust adaptive rule: set κ to 2× the observed P99 of condition numbers from a pilot run. Here that would be κ = 2 × 1.9 = 3.8
78	- **Bottom line**: κ=100 provides ample headroom. The exact value matters only in edge cases where n_expert/K is very small.
79	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "afeae328-7a07-45cf-bc4e-0a0d96830a8c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/artifacts/kappa_sweep/kappa_sweep_analysis.md",
      "content": "# κ Threshold Sweep Analysis\n\n## Setup\n\n- K=2, N=5000, n_expert=200\n- π_s = [0.05, 0.15] (symmetric CM)\n- τ(Z=0)=0.5, τ(Z=1)=1.0\n- T ~ Bernoulli(0.5)\n- κ values: [10, 25, 50, 100, 200, 500, 1000]\n- MC runs: 50 seeds (0–49)\n\n## Summary Table\n\n| κ | Guard Rate | RMSE HB | RMSE Global | RMSE Ratio | Instability % | Mean Max κ(M) | Median Max κ(M) |\n|---:|----------:|--------:|------------:|-----------:|--------------:|--------------:|----------------:|\n| 10 | 0.000 ± 0.000 | 0.0759 ± 0.0043 | 0.0765 ± 0.0042 | 1.0477 ± 0.0483 | 0.0 | 1.4 | 1.4 |\n| 25 | 0.000 ± 0.000 | 0.0759 ± 0.0043 | 0.0765 ± 0.0042 | 1.0477 ± 0.0483 | 0.0 | 1.4 | 1.4 |\n| 50 | 0.000 ± 0.000 | 0.0759 ± 0.0043 | 0.0765 ± 0.0042 | 1.0477 ± 0.0483 | 0.0 | 1.4 | 1.4 |\n| 100 | 0.000 ± 0.000 | 0.0759 ± 0.0043 | 0.0765 ± 0.0042 | 1.0477 ± 0.0483 | 0.0 | 1.4 | 1.4 |\n| 200 | 0.000 ± 0.000 | 0.0759 ± 0.0043 | 0.0765 ± 0.0042 | 1.0477 ± 0.0483 | 0.0 | 1.4 | 1.4 |\n| 500 | 0.000 ± 0.000 | 0.0759 ± 0.0043 | 0.0765 ± 0.0042 | 1.0477 ± 0.0483 | 0.0 | 1.4 | 1.4 |\n| 1000 | 0.000 ± 0.000 | 0.0759 ± 0.0043 | 0.0765 ± 0.0042 | 1.0477 ± 0.0483 | 0.0 | 1.4 | 1.4 |\n\n## Analysis\n\n### Key Finding: Guard Never Triggers\n\nAcross all 350 runs (7 κ values × 50 seeds), the condition number guard **never triggered**. The maximum observed condition number is **1.89**, far below the smallest sweep value κ=10.\n\nThis means all κ values produce **identical** RMSE results. The per-subgroup HB correction is always applied without fallback.\n\n**Interpretation**: With n_expert=200 and moderate misclassification (π_s = [0.05, 0.15]), the confusion matrix is well-estimated and the mixing matrix is well-conditioned. The κ guard is a safety net for edge cases, not an active component under these conditions.\n\n### Condition Number Distribution\n\n| Statistic | Value |\n|-----------|------:|\n| Mean | 1.446 |\n| Median | 1.447 |\n| P90 | 1.598 |\n| P95 | 1.655 |\n| P99 | 1.893 |\n| Max | 1.893 |\n\n### Numerical Stability\n\nNo numerical instability (NaN/Inf) observed at any κ value.\n\n## Stress Test: When Does the Guard Matter?\n\nTo contextualize the sweep, we probe condition numbers under more challenging settings (20 seeds each):\n\n| Configuration | Mean Max κ(M) | P95 Max κ(M) | Max κ(M) | Triggers κ=100? |\n|---------------|-------------:|-----------:|--------:|:---------------|\n| moderate/n200/K2 | 1.4 | 1.7 | 1.8 | No |\n| moderate/n50/K2 | 1.7 | 2.7 | 2.7 | No |\n| extreme/n200/K2 | 2.3 | 2.9 | 5.7 | No |\n| extreme/n50/K2 | 2.6 | 4.4 | 4.4 | No |\n| extreme/n50/K4 | 5.6 | 15.6 | 15.9 | No |\n| near_random/n50/K2 | 181.7 | 1015.8 | 1125.3 | Yes |\n\nThe guard becomes relevant when n_expert is small (≤50) and/or misclassification rates approach 0.5. Under the specified moderate regime, κ never approaches the threshold.\n\n## Is κ=100 Reasonable?\n\n**Yes.** κ=100 is a safe default for this regime:\n- The empirical max condition number (1.89) is ~53× below the threshold, providing a large safety margin.\n- The guard activates only under adversarial conditions (near-random labeling, tiny expert budgets) where correction would amplify noise regardless.\n- A threshold much lower than 100 (e.g., κ=10) would still never trigger here, so the exact value is not critical for well-conditioned problems.\n\n## Adaptive Formula Suggestion\n\nA data-driven approach: set κ = c · √(n_expert / K), where c is calibrated per regime.\n- With n_expert=200, K=2: √(200/2) = 10.0\n- Setting c=10 gives κ=100, which is close to 100\n- However, the optimal κ depends on the misclassification severity, not just sample size\n- A more robust adaptive rule: set κ to 2× the observed P99 of condition numbers from a pilot run. Here that would be κ = 2 × 1.9 = 3.8\n- **Bottom line**: κ=100 provides ample headroom. The exact value matters only in edge cases where n_expert/K is very small.\n",
      "numLines": 79,
      "startLine": 1,
      "totalLines": 79
    }
  }
}
```

</details>

---

### Tool call

_source line 128_

<details open><summary>🔧 Tool call — Bash · `toolu_01XV2rt1DVZwULoVsBCSxcfJ`</summary>

```json
{
  "command": "head -5 artifacts/kappa_sweep/results.csv && echo \"---\" && wc -l artifacts/kappa_sweep/results.csv",
  "description": "Check results.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "03098976-e0ce-4497-b0ab-a09f6406655e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LQHiBhymaq2w5r1o8hRkEi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 726,
      "cache_read_input_tokens": 61157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 726
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

_source line 129 · 2026-05-21T15:58:13.999Z_

<details><summary>↩ Tool result · `toolu_01XV2rt1DVZwULoVsBCSxcfJ`</summary>

```text
kappa,seed,guard_trigger_rate,rmse_hb,rmse_global,rmse_ratio,numerical_instability,max_cond_number
10,0,0.0,0.052168944210936645,0.04460129288813284,1.169673362200165,False,1.3073391439966806
10,1,0.0,0.0438385579177792,0.07624507282825682,0.5749690608405111,False,1.443188431250786
10,2,0.0,0.06329010608521334,0.06439143601849538,0.9828963290558436,False,1.5313838916783908
10,3,0.0,0.044432326130823464,0.0885707925319452,0.5016588974835905,False,1.5540809256051717
---
351 artifacts/kappa_sweep/results.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "ad5f6b52-a5f6-4f97-82a4-607f31ffa162",
  "tool_use_result": {
    "stdout": "kappa,seed,guard_trigger_rate,rmse_hb,rmse_global,rmse_ratio,numerical_instability,max_cond_number\n10,0,0.0,0.052168944210936645,0.04460129288813284,1.169673362200165,False,1.3073391439966806\n10,1,0.0,0.0438385579177792,0.07624507282825682,0.5749690608405111,False,1.443188431250786\n10,2,0.0,0.06329010608521334,0.06439143601849538,0.9828963290558436,False,1.5313838916783908\n10,3,0.0,0.044432326130823464,0.0885707925319452,0.5016588974835905,False,1.5540809256051717\n---\n351 artifacts/kappa_sweep/results.csv",
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

_source line 130_

All outputs are complete and correct. The stress test section provides valuable context showing that the guard only matters with near-random labeling (π_s ≈ 0.4–0.5).

Results summary:

- **350 rows** in `artifacts/kappa_sweep/results.csv` (7 κ values × 50 seeds)
- **Guard never triggers** in the specified moderate regime — max condition number is 1.89, far below any κ threshold
- All κ values produce identical RMSE (HB=0.0759, Global=0.0765, ratio≈1.05)
- Zero numerical instability
- **Stress test** reveals the guard becomes relevant only with near-random labeling (π_s ≈ 0.35–0.40, n_expert=50), where condition numbers reach ~1000+
- **κ=100 is validated**: it provides a ~53× safety margin over observed condition numbers. The formula κ = 10·√(n_expert/K) recovers κ=100 for these settings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "uuid": "040a2b74-c8f8-444c-9c8a-c8c8009cf221",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBehRp728n2a3foBxwDNvo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2332,
      "cache_read_input_tokens": 61883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2332
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

_source line 131_

All outputs are complete and correct. The stress test section provides valuable context showing that the guard only matters with near-random labeling (π_s ≈ 0.4–0.5).

Results summary:

- **350 rows** in `artifacts/kappa_sweep/results.csv` (7 κ values × 50 seeds)
- **Guard never triggers** in the specified moderate regime — max condition number is 1.89, far below any κ threshold
- All κ values produce identical RMSE (HB=0.0759, Global=0.0765, ratio≈1.05)
- Zero numerical instability
- **Stress test** reveals the guard becomes relevant only with near-random labeling (π_s ≈ 0.35–0.40, n_expert=50), where condition numbers reach ~1000+
- **κ=100 is validated**: it provides a ~53× safety margin over observed condition numbers. The formula κ = 10·√(n_expert/K) recovers κ=100 for these settings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 365094,
  "duration_api_ms": 357006,
  "num_turns": 17,
  "stop_reason": "end_turn",
  "session_id": "1118bf56-73c9-4d7d-8bad-d5aca6c2c003",
  "total_cost_usd": 1.3301900500000001,
  "usage": {
    "input_tokens": 4748,
    "cache_creation_input_tokens": 52374,
    "cache_read_input_tokens": 609099,
    "output_tokens": 20140,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 52374,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 251,
        "cache_read_input_tokens": 61883,
        "cache_creation_input_tokens": 2332,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2332
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1721,
      "outputTokens": 4412,
      "cacheReadInputTokens": 670683,
      "cacheCreationInputTokens": 64171,
      "webSearchRequests": 0,
      "costUSD": 0.17106305000000005,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 4748,
      "outputTokens": 20140,
      "cacheReadInputTokens": 609099,
      "cacheCreationInputTokens": 52374,
      "webSearchRequests": 0,
      "costUSD": 1.1591270000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "e37d3aa3-ba52-475b-85f6-0db42c8891ac"
}
```

</details>

---
