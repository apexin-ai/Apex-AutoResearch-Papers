# code cka stability script

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 85
- **Recorded user turns:** 1
- **Tool calls:** 28
- **Original source:** `logs/workers/worker_code_cka_stability_script_20260519T212201.log`
- **Structured JSON:** [`d01b6617fd6df5c53275.json`](../../sessions/d0/d01b6617fd6df5c53275.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
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
  "uuid": "311e39f8-e4e4-4c46-a311-dbf464fb8033",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/memory/"
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
    "resetsAt": 1779242400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "cf53f48b-232c-451e-bd74-0883ff00802f",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10"
}
```

---

### Assistant

_source line 4_

我先阅读项目现有的 CKA 计算代码，了解实现细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "61482d97-20ab-4b65-b9ae-a466cff395c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012VUf9kutmKD3jFSKFboM49",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12540,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12540
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

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Agent · `toolu_016Tg2EEvBPGKBxJ82QSY39c`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Explore CKA scoring code",
  "prompt": "I need to understand the CKA scoring implementation in this ML pruning project. The project is at /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/\n\nI need to find:\n1. How CKA scores are computed (which function/class)\n2. What calibration data is used (GSM8K train? something else?)\n3. Default calibration size\n4. What \"prunable structures\" are (attention heads, MLP groups, etc.)\n5. How the model is loaded and what model path is used\n\nSearch broadly in:\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/src/\n- Any other relevant directories\n\nLook for files like cka.py, prune.py, scoring.py, config files, etc. Read the key files thoroughly to understand the full CKA scoring pipeline."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "37bbaa7a-9584-4d70-a2fa-1adc63d06620",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012VUf9kutmKD3jFSKFboM49",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12540,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12540
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

### System

_source line 6_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a2b810fef875789a5",
  "tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "description": "Explore CKA scoring code",
  "task_type": "local_agent",
  "prompt": "I need to understand the CKA scoring implementation in this ML pruning project. The project is at /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/\n\nI need to find:\n1. How CKA scores are computed (which function/class)\n2. What calibration data is used (GSM8K train? something else?)\n3. Default calibration size\n4. What \"prunable structures\" are (attention heads, MLP groups, etc.)\n5. How the model is loaded and what model path is used\n\nSearch broadly in:\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/src/\n- Any other relevant directories\n\nLook for files like cka.py, prune.py, scoring.py, config files, etc. Read the key files thoroughly to understand the full CKA scoring pipeline.",
  "uuid": "625e4fa3-518e-4415-abc3-73a7fa2752be",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10"
}
```

---

## Round 1

79 recorded events

### User

_source line 7 · 2026-05-19T21:22:27.692Z_

I need to understand the CKA scoring implementation in this ML pruning project. The project is at /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/

I need to find:
1. How CKA scores are computed (which function/class)
2. What calibration data is used (GSM8K train? something else?)
3. Default calibration size
4. What "prunable structures" are (attention heads, MLP groups, etc.)
5. How the model is loaded and what model path is used

Search broadly in:
- /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/src/
- Any other relevant directories

Look for files like cka.py, prune.py, scoring.py, config files, etc. Read the key files thoroughly to understand the full CKA scoring pipeline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "243132c5-1eff-42e8-88b0-5be96f18673f"
}
```

</details>

---

### System

_source line 8_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2b810fef875789a5",
  "tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 16588,
    "tool_uses": 1,
    "duration_ms": 1328
  },
  "last_tool_name": "Bash",
  "uuid": "ee2b8977-7517-4739-b868-e7fb10bf7636",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10"
}
```

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ttd3KCXcQfVjWtPPx7cb6P`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune -type f -name \"*.py\" | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "3cd95c4d-180f-46ad-a7c6-daa7395512b9",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BtHXTwJeMVycwNc9kg5sxm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16569,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16569,
        "ephemeral_1h_input_tokens": 0
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

_source line 10 · 2026-05-19T21:22:29.342Z_

<details><summary>↩ Tool result · `toolu_01Ttd3KCXcQfVjWtPPx7cb6P`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig4_cka_heatmap.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig3_collapse_dynamics.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig1_framework.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig2_reward_trajectories.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig_appendix_kl.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig2_reward_accuracy.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig5_extended_training.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/correlation_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/importance_score.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/eval_gsm8k.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/rasp_scoring.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/run_cka_reliability.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_overlap.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/grasp_scoring.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/eval_mbpp.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/model_utils.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/prune.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/train_grpo.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/convert_graspune_to_hf.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/gradient_flow_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/correlation_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/_project/intermediate/plot_fig1_pipeline.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/figures/gen_fig3_collapse_dynamics.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/figures/gen_fig1_framework.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/figures/gen_fig2_reward_trajectories.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/prune_shortgpt.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/plot_cka_figures.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/bootstrap_ci_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/plot_fig1_pipeline.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "fcef28ba-f3d6-4b21-b0e5-6553351f98a8"
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
  "task_id": "a2b810fef875789a5",
  "tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0509_17/…",
  "usage": {
    "total_tokens": 18818,
    "tool_uses": 2,
    "duration_ms": 3124
  },
  "last_tool_name": "Glob",
  "uuid": "0a1773e0-07d3-434a-be8e-f007ea686746",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10"
}
```

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Glob · `toolu_01QvRu1vxgJqeyNUGT5S9XJ5`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/src/**/*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "bf9e79fd-c8c1-4342-b7e4-5ec3d52bd774",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ak1bM5fWjNPch7NXoMUD9a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2214,
      "cache_read_input_tokens": 16569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2214,
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

_source line 13 · 2026-05-19T21:22:30.844Z_

<details><summary>↩ Tool result · `toolu_01QvRu1vxgJqeyNUGT5S9XJ5`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "eafbeecd-d320-4af8-a2d1-f1571db6e24c"
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
  "task_id": "a2b810fef875789a5",
  "tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 18941,
    "tool_uses": 3,
    "duration_ms": 5557
  },
  "last_tool_name": "Bash",
  "uuid": "184a728e-4295-4dcc-a14f-d69c3324f426",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10"
}
```

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Bash · `toolu_01LuNnd2VKanjDffeY4EULM8`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/ | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "73a6dcfe-6f27-4980-9e64-93eef4cc3c9e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NJXfFNV3wBwamdFPUi5DZd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 121,
      "cache_read_input_tokens": 18783,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 121,
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

_source line 16 · 2026-05-19T21:22:33.374Z_

<details><summary>↩ Tool result · `toolu_01LuNnd2VKanjDffeY4EULM8`</summary>

```text
total 816
drwxr-xr-x 21 ubuntu ubuntu   4096 May 19 15:19 .
drwxr-xr-x 11 ubuntu ubuntu   4096 May 19 21:22 ..
drwxr-xr-x  7 ubuntu ubuntu   4096 May 17 03:43 _project
-rw-r--r--  1 ubuntu ubuntu   5897 May 15 09:03 alpha_ablation_diff_report.md
-rw-r--r--  1 ubuntu ubuntu   3313 May 16 15:45 analysis_grpo_standard_25_qwen_math.md
-rw-r--r--  1 ubuntu ubuntu   6088 May 17 23:22 analysis_recent_results_20260517.md
drwxr-xr-x  2 ubuntu ubuntu   4096 May 19 04:00 bootstrap_ci_accuracy
-rw-r--r--  1 ubuntu ubuntu   9623 May 18 10:19 bootstrap_ci_analysis.py
-rw-r--r--  1 ubuntu ubuntu 147700 May 19 03:12 bootstrap_ci_plot.png
-rw-r--r--  1 ubuntu ubuntu   1435 May 19 03:12 bootstrap_ci_results.json
-rw-r--r--  1 ubuntu ubuntu  27668 May 18 10:19 bootstrap_ci_reward_trajectories.json
-rw-r--r--  1 ubuntu ubuntu  20979 May 18 16:19 cka_heatmap_cka_only.json
-rw-r--r--  1 ubuntu ubuntu  20909 May 18 16:27 cka_heatmap_random.json
-rw-r--r--  1 ubuntu ubuntu  20899 May 18 16:31 cka_heatmap_rasp.json
-rw-r--r--  1 ubuntu ubuntu  20893 May 18 16:23 cka_heatmap_standard.json
-rw-r--r--  1 ubuntu ubuntu   5533 May 17 17:22 collapse_dynamics_comparison.md
-rw-r--r--  1 ubuntu ubuntu   3751 May 17 18:28 collapse_dynamics_step50_update.md
-rw-r--r--  1 ubuntu ubuntu  11846 May 17 03:43 collapse_onset_timing.json
-rw-r--r--  1 ubuntu ubuntu  19149 May 14 05:36 correlation_analysis.py
-rw-r--r--  1 ubuntu ubuntu   4810 May 17 14:43 diag_eval_math500_grpo_timeout.md
-rw-r--r--  1 ubuntu ubuntu    719 May 17 12:05 diag_eval_math500_unpruned.md
-rw-r--r--  1 ubuntu ubuntu   2568 May 16 21:35 diagnose_eval_grpo_standard_25.md
-rw-r--r--  1 ubuntu ubuntu   1855 May 16 23:24 diagnose_eval_pass_k8_v2.md
-rw-r--r--  1 ubuntu ubuntu   1981 May 16 22:26 diagnosis_inference_v2.md
drwxr-xr-x  6 ubuntu ubuntu   4096 May 16 15:46 dream_reports
-rw-r--r--  1 ubuntu ubuntu  39877 May 18 16:31 e3_cka_heatmap.pdf
drwxr-xr-x  3 ubuntu ubuntu   4096 May 19 03:48 eval_gsm8k_grpo_cka_only_20_extended_300
-rw-r--r--  1 ubuntu ubuntu   1037 May 19 02:42 eval_gsm8k_sft_rasp_20_1p5b_results.md
drwxr-xr-x  3 ubuntu ubuntu   4096 May 17 17:56 eval_humaneval_grpo_standard_20_2048
drwxr-xr-x  3 ubuntu ubuntu   4096 May 17 17:46 eval_humaneval_sft_standard_20_2048_v2
-rw-r--r--  1 ubuntu ubuntu    643 May 19 03:10 eval_math500_grpo_cka_only_20_2048_analysis.md
drwxr-xr-x  2 ubuntu ubuntu   4096 May 17 00:24 eval_pass_k8_rasp_20_grpo_deepseek
drwxr-xr-x  3 ubuntu ubuntu   4096 May 16 23:24 eval_pass_k8_standard_20_grpo_qwen_math_v2
drwxr-xr-x  3 ubuntu ubuntu   4096 May 16 18:20 eval_sft_rasp_rlvr_20
-rw-r--r--  1 ubuntu ubuntu  14768 May 16 05:26 evidence_table.md
-rw-r--r--  1 ubuntu ubuntu  10075 May 15 04:43 figure_plan.md
drwxr-xr-x  2 ubuntu ubuntu   4096 May 18 03:57 figures
drwxr-xr-x  3 ubuntu ubuntu   4096 May 19 14:45 gradient_flow_analysis
drwxr-xr-x  3 ubuntu ubuntu   4096 May 19 15:19 gradient_flow_v3
-rw-r--r--  1 ubuntu ubuntu   1290 May 18 01:37 grpo_cka_only_20_full_metrics.md
-rw-r--r--  1 ubuntu ubuntu  12330 May 16 01:59 grpo_collapse_dynamics_analysis.md
drwxr-xr-x  2 ubuntu ubuntu   4096 May 16 15:53 grpo_qwen_math_v3
-rw-r--r--  1 ubuntu ubuntu   5042 May 17 14:48 grpo_random_20_early_analysis.md
-rw-r--r--  1 ubuntu ubuntu   1266 May 18 01:37 grpo_random_20_full_metrics.md
-rw-r--r--  1 ubuntu ubuntu   1728 May 14 23:26 grpo_rasp_20_4096_status.md
drwxr-xr-x  3 ubuntu ubuntu   4096 May 16 17:05 grpo_rasp_25
-rw-r--r--  1 ubuntu ubuntu   2254 May 18 01:58 grpo_standard_20_fair_early_metrics.md
drwxr-xr-x  3 ubuntu ubuntu   4096 May 16 15:45 grpo_standard_25_qwen_math
drwxr-xr-x  3 ubuntu ubuntu   4096 May 17 19:08 humaneval_2048_matrix
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "d514c268-2f5b-451f-a923-6adc507c2c86"
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
  "task_id": "a2b810fef875789a5",
  "tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 20868,
    "tool_uses": 4,
    "duration_ms": 7606
  },
  "last_tool_name": "Bash",
  "uuid": "f81f55df-d4df-4c6b-8c74-99abd8c3dbcb",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10"
}
```

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01H7Gs8igDsmsJUxPKNFN8wP`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/ | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "cc71cbe1-b3b2-4b42-9aa2-9bbacda95cba",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Pnh3sirLCL6L5V9cgSJrLN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 18904,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 19 · 2026-05-19T21:22:35.368Z_

<details><summary>↩ Tool result · `toolu_01H7Gs8igDsmsJUxPKNFN8wP`</summary>

```text
total 176
drwxr-xr-x  2 ubuntu ubuntu  4096 May 19 14:25 .
drwxr-xr-x 11 ubuntu ubuntu  4096 May 19 21:22 ..
-rw-r--r--  1 ubuntu ubuntu 10296 May 14 03:56 cka_overlap.py
-rw-r--r--  1 ubuntu ubuntu  2921 May 15 04:00 convert_graspune_to_hf.py
-rw-r--r--  1 ubuntu ubuntu 12624 May 14 03:56 correlation_analysis.py
-rw-r--r--  1 ubuntu ubuntu  6278 May 14 02:52 eval_gsm8k.py
-rw-r--r--  1 ubuntu ubuntu  7086 May 19 13:32 eval_mbpp.py
-rw-r--r--  1 ubuntu ubuntu 10743 May 19 14:25 gradient_flow_analysis.py
-rw-r--r--  1 ubuntu ubuntu  9190 May 14 19:52 grasp_scoring.py
-rw-r--r--  1 ubuntu ubuntu  9276 May 14 02:50 importance_score.py
-rw-r--r--  1 ubuntu ubuntu  4267 May 15 03:59 model_utils.py
-rw-r--r--  1 ubuntu ubuntu 13838 May 14 02:52 prune.py
-rw-r--r--  1 ubuntu ubuntu  3987 May 14 02:51 rasp_scoring.py
-rw-r--r--  1 ubuntu ubuntu 22348 May 15 03:24 run_cka_reliability.py
-rw-r--r--  1 ubuntu ubuntu  1763 May 14 18:43 run_full_eval_d008.sh
-rw-r--r--  1 ubuntu ubuntu  2464 May 14 18:43 run_full_eval_d008_parallel.sh
-rw-r--r--  1 ubuntu ubuntu  2034 May 14 19:53 run_grasp_prune.sh
-rw-r--r--  1 ubuntu ubuntu  2971 May 15 04:00 run_graspune.sh
-rw-r--r--  1 ubuntu ubuntu  1811 May 14 19:52 run_grpo_multiseed.sh
-rwxr-xr-x  1 ubuntu ubuntu  3789 May 14 03:56 run_mvp.sh
-rw-r--r--  1 ubuntu ubuntu  7204 May 14 02:52 train_grpo.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "c0924877-53e0-4e4a-a5cf-a07939672bf5"
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
  "task_id": "a2b810fef875789a5",
  "tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "description": "Reading src/importance_score.py",
  "usage": {
    "total_tokens": 21674,
    "tool_uses": 5,
    "duration_ms": 9361
  },
  "last_tool_name": "Read",
  "uuid": "3aba2a5d-4e48-4e95-9a73-4ee697264a92",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10"
}
```

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_011WeMc3s6E3oiD4ULZBN9YD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/importance_score.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "a5bf8d44-7577-4c79-955a-c9b25b78f540",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012NJHCc7BLoUXMy8AgdYzbT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 804,
      "cache_read_input_tokens": 20819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 804,
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

_source line 22 · 2026-05-19T21:22:37.075Z_

<details><summary>↩ Tool result · `toolu_011WeMc3s6E3oiD4ULZBN9YD`</summary>

```text
1	"""
2	Gradient-based Importance Scoring for structured pruning.
3	
4	Computes Taylor-expansion importance I(h) = ||w_h * grad_h||_2 for each
5	attention head and MLP channel group on calibration data.
6	
7	Input:  model + calibration data (GSM8K train subset)
8	Output: per-structure I(h) scores saved as dict in .pt file
9	        Keys: 'attn_importance' (dict[layer_idx -> tensor[n_heads]]),
10	              'mlp_importance'  (dict[layer_idx -> tensor[n_groups]])
11	"""
12	
13	import argparse
14	import logging
15	import os
16	import random
17	
18	import numpy as np
19	import torch
20	from datasets import load_dataset
21	from transformers import AutoModelForCausalLM, AutoTokenizer
22	
23	logging.basicConfig(
24	    level=logging.INFO,
25	    format="%(asctime)s [%(levelname)s] %(message)s",
26	)
27	logger = logging.getLogger(__name__)
28	
29	
30	def set_seed(seed: int):
31	    random.seed(seed)
32	    np.random.seed(seed)
33	    torch.manual_seed(seed)
34	    torch.cuda.manual_seed_all(seed)
35	
36	
37	def load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):
38	    """Load GSM8K train questions as calibration prompts with labels for loss computation."""
39	    ds = load_dataset("openai/gsm8k", "main", split="train")
40	    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))
41	
42	    encodings = []
43	    for example in ds:
44	        text = f"Question: {example['question']}\nAnswer: {example['answer']}"
45	        ids = tokenizer(text, return_tensors="pt", truncation=True, max_length=max_length)
46	        encodings.append(ids)
47	    return encodings
48	
49	
50	def compute_importance(model, calibration_data, device):
51	    """Compute gradient-based importance for attention heads and MLP groups.
52	
53	    Uses Taylor expansion: I(h) = ||w_h * grad_h||_2
54	    Accumulates over calibration batches.
55	    """
56	    config = model.config
57	    n_layers = config.num_hidden_layers
58	    n_heads = config.num_attention_heads
59	    head_dim = config.hidden_size // n_heads
60	    intermediate_size = config.intermediate_size
61	    n_groups = n_heads  # match attention head count for MLP groups
62	    group_size = intermediate_size // n_groups
63	
64	    attn_importance = {i: torch.zeros(n_heads, device="cpu") for i in range(n_layers)}
65	    mlp_importance = {i: torch.zeros(n_groups, device="cpu") for i in range(n_layers)}
66	
67	    model.train()
68	
69	    for batch_idx, enc in enumerate(calibration_data):
70	        input_ids = enc["input_ids"].to(device)
71	        attention_mask = enc["attention_mask"].to(device)
72	        labels = input_ids.clone()
73	
74	        model.zero_grad()
75	        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
76	        loss = outputs.loss
77	        loss.backward()
78	
79	        with torch.no_grad():
80	            for layer_idx in range(n_layers):
81	                layer = model.model.layers[layer_idx]
82	
83	                # Attention head importance via q_proj weights
84	                q_weight = layer.self_attn.q_proj.weight  # [n_heads*head_dim, hidden]
85	                q_grad = layer.self_attn.q_proj.weight.grad
86	                if q_grad is not None:
87	                    # Reshape to [n_heads, head_dim, hidden]
88	                    w = q_weight.view(n_heads, head_dim, -1)
89	                    g = q_grad.view(n_heads, head_dim, -1)
90	                    taylor = (w * g).float()  # [n_heads, head_dim, hidden]
91	                    # L2 norm per head
92	                    head_scores = taylor.view(n_heads, -1).norm(dim=1)  # [n_heads]
93	                    attn_importance[layer_idx] += head_scores.cpu()
94	
95	                # Also incorporate k_proj and v_proj for attention importance
96	                for proj_name in ["k_proj", "v_proj", "o_proj"]:
97	                    proj = getattr(layer.self_attn, proj_name)
98	                    w = proj.weight
99	                    g = proj.weight.grad
100	                    if g is None:
101	                        continue
102	                    if proj_name == "o_proj":
103	                        # o_proj: [hidden, n_heads*head_dim] — split on dim=1
104	                        w_r = w.view(-1, n_heads, head_dim)
105	                        g_r = g.view(-1, n_heads, head_dim)
106	                        taylor = (w_r * g_r).float()
107	                        head_scores = taylor.permute(1, 0, 2).reshape(n_heads, -1).norm(dim=1)
108	                    elif proj_name == "k_proj":
109	                        # GQA: k_proj has n_kv_heads, broadcast to n_heads
110	                        n_kv = config.num_key_value_heads
111	                        kv_head_dim = config.hidden_size // n_heads
112	                        w_r = w.view(n_kv, kv_head_dim, -1)
113	                        g_r = g.view(n_kv, kv_head_dim, -1)
114	                        taylor = (w_r * g_r).float()
115	                        kv_scores = taylor.view(n_kv, -1).norm(dim=1)
116	                        # Broadcast KV heads to query heads
117	                        heads_per_kv = n_heads // n_kv
118	                        head_scores = kv_scores.repeat_interleave(heads_per_kv)
119	                    elif proj_name == "v_proj":
120	                        n_kv = config.num_key_value_heads
121	                        kv_head_dim = config.hidden_size // n_heads
122	                        w_r = w.view(n_kv, kv_head_dim, -1)
123	                        g_r = g.view(n_kv, kv_head_dim, -1)
124	                        taylor = (w_r * g_r).float()
125	                        kv_scores = taylor.view(n_kv, -1).norm(dim=1)
126	                        heads_per_kv = n_heads // n_kv
127	                        head_scores = kv_scores.repeat_interleave(heads_per_kv)
128	                    attn_importance[layer_idx] += head_scores.cpu()
129	
130	                # MLP importance via gate_proj
131	                gate_w = layer.mlp.gate_proj.weight  # [intermediate, hidden]
132	                gate_g = layer.mlp.gate_proj.weight.grad
133	                if gate_g is not None:
134	                    usable = n_groups * group_size
135	                    w_r = gate_w[:usable].view(n_groups, group_size, -1)
136	                    g_r = gate_g[:usable].view(n_groups, group_size, -1)
137	                    taylor = (w_r * g_r).float()
138	                    group_scores = taylor.view(n_groups, -1).norm(dim=1)
139	                    mlp_importance[layer_idx] += group_scores.cpu()
140	
141	                # Also use up_proj for MLP importance
142	                up_w = layer.mlp.up_proj.weight
143	                up_g = layer.mlp.up_proj.weight.grad
144	                if up_g is not None:
145	                    usable = n_groups * group_size
146	                    w_r = up_w[:usable].view(n_groups, group_size, -1)
147	                    g_r = up_g[:usable].view(n_groups, group_size, -1)
148	                    taylor = (w_r * g_r).float()
149	                    group_scores = taylor.view(n_groups, -1).norm(dim=1)
150	                    mlp_importance[layer_idx] += group_scores.cpu()
151	
152	        if (batch_idx + 1) % 50 == 0:
153	            logger.info(f"  Processed {batch_idx + 1}/{len(calibration_data)} samples")
154	
155	    # Average over samples
156	    n = len(calibration_data)
157	    for layer_idx in range(n_layers):
158	        attn_importance[layer_idx] /= n
159	        mlp_importance[layer_idx] /= n
160	
161	    return attn_importance, mlp_importance
162	
163	
164	def main():
165	    parser = argparse.ArgumentParser(description="Compute gradient-based importance scores for RASP")
166	    parser.add_argument("--model_path", type=str, required=True, help="Path to pretrained model")
167	    parser.add_argument("--output_path", type=str, required=True, help="Output .pt file for importance scores")
168	    parser.add_argument("--n_samples", type=int, default=512, help="Number of calibration samples")
169	    parser.add_argument("--max_length", type=int, default=512, help="Max token length for calibration inputs")
170	    parser.add_argument("--seed", type=int, default=42, help="Random seed")
171	    parser.add_argument("--dtype", type=str, default="bfloat16", choices=["float16", "bfloat16", "float32"])
172	    args = parser.parse_args()
173	
174	    set_seed(args.seed)
175	    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
176	    dtype_map = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}
177	    torch_dtype = dtype_map[args.dtype]
178	
179	    logger.info(f"Loading model from {args.model_path}")
180	    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
181	    model = AutoModelForCausalLM.from_pretrained(
182	        args.model_path,
183	        torch_dtype=torch_dtype,
184	        device_map=device,
185	        trust_remote_code=True,
186	    )
187	
188	    logger.info(f"Loading {args.n_samples} calibration samples")
189	    calibration_data = load_calibration_data(tokenizer, args.n_samples, args.max_length, args.seed)
190	
191	    logger.info("Computing gradient-based importance scores...")
192	    attn_importance, mlp_importance = compute_importance(model, calibration_data, device)
193	
194	    for layer_idx in range(model.config.num_hidden_layers):
195	        a = attn_importance[layer_idx]
196	        m = mlp_importance[layer_idx]
197	        logger.info(
198	            f"  Layer {layer_idx}: attn I(h) range [{a.min():.6f}, {a.max():.6f}], "
199	            f"mlp I(h) range [{m.min():.6f}, {m.max():.6f}]"
200	        )
201	
202	    os.makedirs(os.path.dirname(args.output_path) or ".", exist_ok=True)
203	    result = {"attn_importance": attn_importance, "mlp_importance": mlp_importance}
204	    torch.save(result, args.output_path)
205	    logger.info(f"Saved importance scores to {args.output_path}")
206	
207	
208	if __name__ == "__main__":
209	    main()
210	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "2b151958-a2a5-4f31-b69b-440995211039"
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
  "task_id": "a2b810fef875789a5",
  "tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "description": "Reading src/prune.py",
  "usage": {
    "total_tokens": 25190,
    "tool_uses": 6,
    "duration_ms": 11240
  },
  "last_tool_name": "Read",
  "uuid": "7c000c83-64ac-4fe6-a7f9-cc9a3f860153",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10"
}
```

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01BPevmRR8FHr3VxLWkUwXcB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/prune.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "d7ca8035-a096-4a4a-8a9e-ff6c6bf97123",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015VZsMLfmaDtRiv7jzi56df",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3510,
      "cache_read_input_tokens": 21623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3510,
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

_source line 25 · 2026-05-19T21:22:38.957Z_

<details><summary>↩ Tool result · `toolu_01BPevmRR8FHr3VxLWkUwXcB`</summary>

```text
1	"""
2	Structured Pruning for Qwen2.5 architecture.
3	
4	Removes attention heads and MLP channel groups based on RASP or standard importance scores.
5	Handles GQA (grouped query attention) correctly: when all query heads sharing a KV head
6	are pruned, the corresponding KV head is also removed.
7	
8	Input:  pretrained model + pruning scores
9	Output: pruned model saved to disk
10	"""
11	
12	import argparse
13	import copy
14	import logging
15	import os
16	import random
17	
18	import numpy as np
19	import torch
20	from transformers import AutoModelForCausalLM, AutoTokenizer
21	
22	logging.basicConfig(
23	    level=logging.INFO,
24	    format="%(asctime)s [%(levelname)s] %(message)s",
25	)
26	logger = logging.getLogger(__name__)
27	
28	
29	def set_seed(seed: int):
30	    random.seed(seed)
31	    np.random.seed(seed)
32	    torch.manual_seed(seed)
33	    torch.cuda.manual_seed_all(seed)
34	
35	
36	def compute_pruning_masks(scores: dict, n_to_prune: int) -> dict:
37	    """Determine which structures to prune globally.
38	
39	    Returns dict[layer_idx -> list of struct indices to KEEP].
40	    """
41	    ranking = []
42	    for layer_idx, layer_scores in scores.items():
43	        for struct_idx in range(layer_scores.shape[0]):
44	            ranking.append((layer_scores[struct_idx].item(), layer_idx, struct_idx))
45	    ranking.sort(key=lambda x: x[0])
46	
47	    prune_set = set()
48	    for i in range(min(n_to_prune, len(ranking))):
49	        _, layer_idx, struct_idx = ranking[i]
50	        prune_set.add((layer_idx, struct_idx))
51	
52	    keep_masks = {}
53	    for layer_idx, layer_scores in scores.items():
54	        n_structs = layer_scores.shape[0]
55	        keep = [i for i in range(n_structs) if (layer_idx, i) not in prune_set]
56	        keep_masks[layer_idx] = keep
57	    return keep_masks
58	
59	
60	def prune_attention_heads(model, attn_keep_masks: dict):
61	    """Prune attention heads from the model by slicing weight matrices in-place.
62	
63	    For GQA: KV heads are removed only when ALL query heads mapped to them are pruned.
64	    """
65	    config = model.config
66	    n_heads = config.num_attention_heads
67	    n_kv_heads = config.num_key_value_heads
68	    head_dim = config.hidden_size // n_heads
69	    heads_per_kv = n_heads // n_kv_heads
70	
71	    total_pruned_q = 0
72	    total_pruned_kv = 0
73	
74	    for layer_idx, keep_heads in attn_keep_masks.items():
75	        layer = model.model.layers[layer_idx]
76	        attn = layer.self_attn
77	        n_keep = len(keep_heads)
78	        pruned_q = n_heads - n_keep
79	
80	        # Q indices to keep
81	        q_indices = []
82	        for h in keep_heads:
83	            start = h * head_dim
84	            q_indices.extend(range(start, start + head_dim))
85	        q_indices = torch.tensor(q_indices, dtype=torch.long)
86	
87	        # Determine which KV heads to keep
88	        kv_keep = set()
89	        for h in keep_heads:
90	            kv_keep.add(h // heads_per_kv)
91	        kv_keep = sorted(kv_keep)
92	        n_kv_keep = len(kv_keep)
93	        pruned_kv = n_kv_heads - n_kv_keep
94	
95	        kv_indices = []
96	        for kv in kv_keep:
97	            start = kv * head_dim
98	            kv_indices.extend(range(start, start + head_dim))
99	        kv_indices = torch.tensor(kv_indices, dtype=torch.long)
100	
101	        # Slice q_proj: [n_heads*head_dim, hidden] -> [n_keep*head_dim, hidden]
102	        attn.q_proj.weight = torch.nn.Parameter(attn.q_proj.weight.data[q_indices])
103	        if attn.q_proj.bias is not None:
104	            attn.q_proj.bias = torch.nn.Parameter(attn.q_proj.bias.data[q_indices])
105	
106	        # Slice k_proj, v_proj: [n_kv*head_dim, hidden] -> [n_kv_keep*head_dim, hidden]
107	        attn.k_proj.weight = torch.nn.Parameter(attn.k_proj.weight.data[kv_indices])
108	        if attn.k_proj.bias is not None:
109	            attn.k_proj.bias = torch.nn.Parameter(attn.k_proj.bias.data[kv_indices])
110	
111	        attn.v_proj.weight = torch.nn.Parameter(attn.v_proj.weight.data[kv_indices])
112	        if attn.v_proj.bias is not None:
113	            attn.v_proj.bias = torch.nn.Parameter(attn.v_proj.bias.data[kv_indices])
114	
115	        # Slice o_proj: [hidden, n_heads*head_dim] -> [hidden, n_keep*head_dim]
116	        attn.o_proj.weight = torch.nn.Parameter(attn.o_proj.weight.data[:, q_indices])
117	
118	        # Update config attributes on the layer
119	        attn.num_heads = n_keep
120	        attn.num_key_value_heads = n_kv_keep
121	        attn.head_dim = head_dim
122	
123	        total_pruned_q += pruned_q
124	        total_pruned_kv += pruned_kv
125	
126	        if pruned_q > 0:
127	            logger.info(
128	                f"  Layer {layer_idx}: pruned {pruned_q}/{n_heads} Q heads, "
129	                f"{pruned_kv}/{n_kv_heads} KV heads"
130	            )
131	
132	    logger.info(f"Total attention pruning: {total_pruned_q} Q heads, {total_pruned_kv} KV heads removed")
133	
134	
135	def prune_mlp_channels(model, mlp_keep_masks: dict):
136	    """Prune MLP channel groups by slicing gate_proj, up_proj, and down_proj."""
137	    config = model.config
138	    intermediate_size = config.intermediate_size
139	    n_heads = config.num_attention_heads
140	    n_groups = n_heads
141	    group_size = intermediate_size // n_groups
142	
143	    total_pruned = 0
144	
145	    for layer_idx, keep_groups in mlp_keep_masks.items():
146	        layer = model.model.layers[layer_idx]
147	        mlp = layer.mlp
148	        n_keep = len(keep_groups)
149	        pruned = n_groups - n_keep
150	
151	        if pruned == 0:
152	            continue
153	
154	        # Channel indices to keep
155	        indices = []
156	        for g in keep_groups:
157	            start = g * group_size
158	            indices.extend(range(start, start + group_size))
159	        # Also keep any remainder channels beyond n_groups*group_size
160	        remainder_start = n_groups * group_size
161	        if remainder_start < intermediate_size:
162	            indices.extend(range(remainder_start, intermediate_size))
163	        indices = torch.tensor(indices, dtype=torch.long)
164	
165	        # gate_proj: [intermediate, hidden] -> [n_keep_channels, hidden]
166	        mlp.gate_proj.weight = torch.nn.Parameter(mlp.gate_proj.weight.data[indices])
167	        if mlp.gate_proj.bias is not None:
168	            mlp.gate_proj.bias = torch.nn.Parameter(mlp.gate_proj.bias.data[indices])
169	
170	        # up_proj: [intermediate, hidden] -> [n_keep_channels, hidden]
171	        mlp.up_proj.weight = torch.nn.Parameter(mlp.up_proj.weight.data[indices])
172	        if mlp.up_proj.bias is not None:
173	            mlp.up_proj.bias = torch.nn.Parameter(mlp.up_proj.bias.data[indices])
174	
175	        # down_proj: [hidden, intermediate] -> [hidden, n_keep_channels]
176	        mlp.down_proj.weight = torch.nn.Parameter(mlp.down_proj.weight.data[:, indices])
177	
178	        total_pruned += pruned
179	        logger.info(
180	            f"  Layer {layer_idx}: pruned {pruned}/{n_groups} MLP groups "
181	            f"({pruned * group_size} channels)"
182	        )
183	
184	    logger.info(f"Total MLP pruning: {total_pruned} groups removed")
185	
186	
187	def count_parameters(model) -> int:
188	    return sum(p.numel() for p in model.parameters())
189	
190	
191	def main():
192	    parser = argparse.ArgumentParser(description="Execute structured pruning on Qwen2.5 model")
193	    parser.add_argument("--model_path", type=str, required=True, help="Path to pretrained model")
194	    parser.add_argument("--importance_path", type=str, required=True, help="Path to importance scores .pt")
195	    parser.add_argument("--cka_path", type=str, default=None, help="Path to CKA overlap scores .pt")
196	    parser.add_argument("--mode", type=str, choices=["standard", "rasp"], required=True)
197	    parser.add_argument("--sparsity", type=float, default=0.35, help="Target sparsity ratio")
198	    parser.add_argument("--alpha", type=float, default=1.0, help="RASP alpha parameter")
199	    parser.add_argument("--output_path", type=str, required=True, help="Output path for pruned model")
200	    parser.add_argument("--seed", type=int, default=42)
201	    parser.add_argument("--dtype", type=str, default="bfloat16", choices=["float16", "bfloat16", "float32"])
202	    args = parser.parse_args()
203	
204	    set_seed(args.seed)
205	    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
206	    dtype_map = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}
207	    torch_dtype = dtype_map[args.dtype]
208	
209	    logger.info(f"Loading model from {args.model_path}")
210	    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
211	    model = AutoModelForCausalLM.from_pretrained(
212	        args.model_path,
213	        torch_dtype=torch_dtype,
214	        device_map="cpu",  # load on CPU for manipulation
215	        trust_remote_code=True,
216	    )
217	
218	    original_params = count_parameters(model)
219	    logger.info(f"Original model parameters: {original_params:,}")
220	
221	    # Load scores
222	    importance_data = torch.load(args.importance_path, map_location="cpu", weights_only=True)
223	    attn_importance = importance_data["attn_importance"]
224	    mlp_importance = importance_data["mlp_importance"]
225	
226	    if args.mode == "rasp":
227	        if args.cka_path is None:
228	            raise ValueError("--cka_path required for rasp mode")
229	        cka_data = torch.load(args.cka_path, map_location="cpu", weights_only=True)
230	        attn_overlap = cka_data["attn_overlap"]
231	        mlp_overlap = cka_data["mlp_overlap"]
232	        # S(h) = I(h) * (1 - F(h))^alpha
233	        attn_scores = {}
234	        for k in attn_importance:
235	            attn_scores[k] = attn_importance[k].float() * (1.0 - attn_overlap[k].float()).pow(args.alpha)
236	        mlp_scores = {}
237	        for k in mlp_importance:
238	            mlp_scores[k] = mlp_importance[k].float() * (1.0 - mlp_overlap[k].float()).pow(args.alpha)
239	        logger.info(f"Using RASP scoring with alpha={args.alpha}")
240	    else:
241	        attn_scores = {k: v.float() for k, v in attn_importance.items()}
242	        mlp_scores = {k: v.float() for k, v in mlp_importance.items()}
243	        logger.info("Using standard importance-only scoring")
244	
245	    # Compute how many structures to prune for target sparsity
246	    # Approximate: distribute sparsity proportionally between attn and MLP
247	    config = model.config
248	    n_layers = config.num_hidden_layers
249	    n_heads = config.num_attention_heads
250	    head_dim = config.hidden_size // n_heads
251	    intermediate_size = config.intermediate_size
252	    n_groups = n_heads
253	    group_size = intermediate_size // n_groups
254	
255	    total_attn_heads = n_layers * n_heads
256	    total_mlp_groups = n_layers * n_groups
257	
258	    # Estimate parameter counts
259	    # Per attention head: q_proj + share of k/v_proj + o_proj
260	    hidden = config.hidden_size
261	    attn_params_per_head = head_dim * hidden * 2  # q + o contribution
262	    mlp_params_per_group = group_size * hidden * 3  # gate + up + down contribution
263	
264	    total_prunable = total_attn_heads * attn_params_per_head + total_mlp_groups * mlp_params_per_group
265	    target_prune_params = original_params * args.sparsity
266	
267	    # Use a unified ranking approach: merge attn and MLP scores
268	    all_entries = []
269	    for layer_idx in range(n_layers):
270	        for h in range(n_heads):
271	            score = attn_scores[layer_idx][h].item()
272	            params = attn_params_per_head
273	            all_entries.append((score, "attn", layer_idx, h, params))
274	        for g in range(n_groups):
275	            score = mlp_scores[layer_idx][g].item()
276	            params = mlp_params_per_group
277	            all_entries.append((score, "mlp", layer_idx, g, params))
278	
279	    all_entries.sort(key=lambda x: x[0])
280	
281	    # Greedily select structures to prune until reaching target sparsity
282	    pruned_params = 0
283	    attn_prune_set = set()
284	    mlp_prune_set = set()
285	
286	    # Keep at least 4 heads per layer and 4 MLP groups per layer
287	    min_keep_per_layer = 4
288	    attn_prune_count = {i: 0 for i in range(n_layers)}
289	    mlp_prune_count = {i: 0 for i in range(n_layers)}
290	
291	    for score, stype, layer_idx, struct_idx, params in all_entries:
292	        if pruned_params >= target_prune_params:
293	            break
294	        if stype == "attn":
295	            if attn_prune_count[layer_idx] >= n_heads - min_keep_per_layer:
296	                continue
297	            attn_prune_set.add((layer_idx, struct_idx))
298	            attn_prune_count[layer_idx] += 1
299	        else:
300	            if mlp_prune_count[layer_idx] >= n_groups - min_keep_per_layer:
301	                continue
302	            mlp_prune_set.add((layer_idx, struct_idx))
303	            mlp_prune_count[layer_idx] += 1
304	        pruned_params += params
305	
306	    logger.info(f"Target sparsity: {args.sparsity:.0%}, pruning {len(attn_prune_set)} attn heads + "
307	                f"{len(mlp_prune_set)} MLP groups ({pruned_params:,} params)")
308	
309	    # Build keep masks
310	    attn_keep_masks = {}
311	    for layer_idx in range(n_layers):
312	        keep = [h for h in range(n_heads) if (layer_idx, h) not in attn_prune_set]
313	        attn_keep_masks[layer_idx] = keep
314	
315	    mlp_keep_masks = {}
316	    for layer_idx in range(n_layers):
317	        keep = [g for g in range(n_groups) if (layer_idx, g) not in mlp_prune_set]
318	        mlp_keep_masks[layer_idx] = keep
319	
320	    # Execute pruning
321	    logger.info("Pruning attention heads...")
322	    prune_attention_heads(model, attn_keep_masks)
323	
324	    logger.info("Pruning MLP channels...")
325	    prune_mlp_channels(model, mlp_keep_masks)
326	
327	    pruned_params_actual = count_parameters(model)
328	    actual_sparsity = 1.0 - pruned_params_actual / original_params
329	    logger.info(
330	        f"Pruned model parameters: {pruned_params_actual:,} "
331	        f"(actual sparsity: {actual_sparsity:.2%})"
332	    )
333	
334	    # Save
335	    logger.info(f"Saving pruned model to {args.output_path}")
336	    os.makedirs(args.output_path, exist_ok=True)
337	    model.save_pretrained(args.output_path)
338	    tokenizer.save_pretrained(args.output_path)
339	
340	    # Save pruning metadata
341	    metadata = {
342	        "mode": args.mode,
343	        "sparsity_target": args.sparsity,
344	        "sparsity_actual": actual_sparsity,
345	        "alpha": args.alpha if args.mode == "rasp" else None,
346	        "original_params": original_params,
347	        "pruned_params": pruned_params_actual,
348	        "attn_keep_masks": attn_keep_masks,
349	        "mlp_keep_masks": mlp_keep_masks,
350	    }
351	    torch.save(metadata, os.path.join(args.output_path, "pruning_metadata.pt"))
352	    logger.info("Done.")
353	
354	
355	if __name__ == "__main__":
356	    main()
357	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "fc480f36-4f58-46d5-a0d1-6ec60e7f67bd"
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
  "task_id": "a2b810fef875789a5",
  "tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "description": "Reading src/cka_overlap.py",
  "usage": {
    "total_tokens": 30675,
    "tool_uses": 7,
    "duration_ms": 13199
  },
  "last_tool_name": "Read",
  "uuid": "8fdc8e67-bae0-46e4-be13-297e7414800b",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10"
}
```

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01BHGDCC3SSMGguwkGM1PcGc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_overlap.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "3a2d2b28-5091-4a2a-8d7a-165d99487f45",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ts6gtzg5tCgmkovp6ozEpx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 5483,
      "cache_read_input_tokens": 25133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5483,
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

_source line 28 · 2026-05-19T21:22:40.898Z_

<details><summary>↩ Tool result · `toolu_01BHGDCC3SSMGguwkGM1PcGc`</summary>

```text
1	"""
2	CKA Overlap Computation for RASP.
3	
4	Computes intra-layer functional overlap F(h) for each attention head and MLP channel group
5	using linear CKA (Centered Kernel Alignment via HSIC).
6	
7	Input:  model + calibration data (GSM8K train subset)
8	Output: per-structure F(h) scores saved as dict in .pt file
9	        Keys: 'attn_overlap' (dict[layer_idx -> tensor[n_heads]]),
10	              'mlp_overlap'  (dict[layer_idx -> tensor[n_groups]])
11	"""
12	
13	import argparse
14	import logging
15	import math
16	import os
17	import random
18	
19	import numpy as np
20	import torch
21	from datasets import load_dataset
22	from transformers import AutoModelForCausalLM, AutoTokenizer
23	
24	logging.basicConfig(
25	    level=logging.INFO,
26	    format="%(asctime)s [%(levelname)s] %(message)s",
27	)
28	logger = logging.getLogger(__name__)
29	
30	
31	def set_seed(seed: int):
32	    random.seed(seed)
33	    np.random.seed(seed)
34	    torch.manual_seed(seed)
35	    torch.cuda.manual_seed_all(seed)
36	
37	
38	def linear_cka(X: torch.Tensor, Y: torch.Tensor) -> float:
39	    """Linear CKA between two activation matrices.
40	    X: [n, p], Y: [n, q]. Returns scalar similarity in [0, 1].
41	    """
42	    X = X - X.mean(0)
43	    Y = Y - Y.mean(0)
44	    hsic_xy = torch.norm(X.T @ Y, "fro") ** 2
45	    hsic_xx = torch.norm(X.T @ X, "fro") ** 2
46	    hsic_yy = torch.norm(Y.T @ Y, "fro") ** 2
47	    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()
48	
49	
50	def load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):
51	    """Load GSM8K train questions as calibration prompts."""
52	    ds = load_dataset("openai/gsm8k", "main", split="train")
53	    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))
54	
55	    encodings = []
56	    for example in ds:
57	        prompt = f"Question: {example['question']}\nAnswer: Let me think step by step.\n"
58	        ids = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
59	        encodings.append(ids)
60	    return encodings
61	
62	
63	def collect_head_activations(model, tokenizer, calibration_data, device):
64	    """Run calibration data through model and collect per-head activations for each layer.
65	
66	    Returns dict[layer_idx] -> tensor[n_samples, n_heads, pooled_dim]
67	    where pooled_dim collapses (seq_len, head_dim) via mean-pool over seq_len.
68	    """
69	    config = model.config
70	    n_layers = config.num_hidden_layers
71	    n_heads = config.num_attention_heads
72	    head_dim = config.hidden_size // n_heads
73	
74	    layer_activations = {i: [] for i in range(n_layers)}
75	    hooks = []
76	
77	    def make_hook(layer_idx):
78	        def hook_fn(module, input, output):
79	            # output of attention: (hidden_states, attn_weights, past_kv)
80	            # We hook into q_proj to get query states, then reshape per-head
81	            pass
82	        return hook_fn
83	
84	    # Hook into each attention layer's output (the hidden_states after o_proj)
85	    # We instead hook the q_proj to capture per-head representations
86	    q_proj_outputs = {i: [] for i in range(n_layers)}
87	
88	    def make_q_hook(layer_idx):
89	        def hook_fn(module, input, output):
90	            # output shape: [batch, seq_len, n_heads * head_dim]
91	            q_proj_outputs[layer_idx].append(output.detach())
92	        return hook_fn
93	
94	    for i in range(n_layers):
95	        layer = model.model.layers[i]
96	        h = layer.self_attn.q_proj.register_forward_hook(make_q_hook(i))
97	        hooks.append(h)
98	
99	    model.eval()
100	    with torch.no_grad():
101	        for batch_idx, enc in enumerate(calibration_data):
102	            input_ids = enc["input_ids"].to(device)
103	            attention_mask = enc["attention_mask"].to(device)
104	            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)
105	            if (batch_idx + 1) % 50 == 0:
106	                logger.info(f"  Processed {batch_idx + 1}/{len(calibration_data)} samples")
107	
108	    for h in hooks:
109	        h.remove()
110	
111	    # Reshape and mean-pool: [batch, seq, n_heads*head_dim] -> per-head [batch, head_dim]
112	    for layer_idx in range(n_layers):
113	        tensors = q_proj_outputs[layer_idx]  # list of [1, seq, n_heads*head_dim]
114	        per_head_list = []
115	        for t in tensors:
116	            t = t.squeeze(0)  # [seq, n_heads*head_dim]
117	            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]
118	            t = t.mean(dim=0)  # [n_heads, head_dim] — mean pool over seq
119	            per_head_list.append(t)
120	        layer_activations[layer_idx] = torch.stack(per_head_list, dim=0)  # [n_samples, n_heads, head_dim]
121	        q_proj_outputs[layer_idx] = None  # free memory
122	
123	    return layer_activations
124	
125	
126	def collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups: int = 28):
127	    """Collect MLP intermediate activations grouped into channel groups.
128	
129	    Returns dict[layer_idx] -> tensor[n_samples, n_groups, group_dim]
130	    """
131	    config = model.config
132	    n_layers = config.num_hidden_layers
133	    intermediate_size = config.intermediate_size
134	    group_size = intermediate_size // n_groups
135	
136	    gate_outputs = {i: [] for i in range(n_layers)}
137	    hooks = []
138	
139	    def make_gate_hook(layer_idx):
140	        def hook_fn(module, input, output):
141	            gate_outputs[layer_idx].append(output.detach())
142	        return hook_fn
143	
144	    for i in range(n_layers):
145	        layer = model.model.layers[i]
146	        h = layer.mlp.gate_proj.register_forward_hook(make_gate_hook(i))
147	        hooks.append(h)
148	
149	    model.eval()
150	    with torch.no_grad():
151	        for enc in calibration_data:
152	            input_ids = enc["input_ids"].to(device)
153	            attention_mask = enc["attention_mask"].to(device)
154	            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)
155	
156	    for h in hooks:
157	        h.remove()
158	
159	    layer_activations = {}
160	    for layer_idx in range(n_layers):
161	        tensors = gate_outputs[layer_idx]
162	        per_group_list = []
163	        for t in tensors:
164	            t = t.squeeze(0)  # [seq, intermediate_size]
165	            t = t.mean(dim=0)  # [intermediate_size] — mean pool over seq
166	            # Truncate to exact multiple of group_size
167	            usable = n_groups * group_size
168	            t = t[:usable].view(n_groups, group_size)  # [n_groups, group_size]
169	            per_group_list.append(t)
170	        layer_activations[layer_idx] = torch.stack(per_group_list, dim=0)  # [n_samples, n_groups, group_size]
171	        gate_outputs[layer_idx] = None
172	
173	    return layer_activations
174	
175	
176	def compute_overlap(activations_dict: dict, structure_name: str) -> tuple:
177	    """Compute F(h) = mean CKA similarity and pairwise CKA matrix per layer.
178	
179	    activations_dict: dict[layer_idx] -> tensor[n_samples, n_structures, dim]
180	    Returns: (overlap_scores, cka_matrices)
181	        overlap_scores: dict[layer_idx] -> tensor[n_structures] of overlap F(h) in [0, 1]
182	        cka_matrices: dict[layer_idx] -> tensor[n_structures, n_structures] pairwise CKA
183	    """
184	    overlap_scores = {}
185	    cka_matrices = {}
186	    for layer_idx, acts in activations_dict.items():
187	        n_samples, n_structs, dim = acts.shape
188	        matrix = torch.zeros(n_structs, n_structs)
189	        for i in range(n_structs):
190	            matrix[i, i] = 1.0
191	            for j in range(i + 1, n_structs):
192	                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())
193	                matrix[i, j] = val
194	                matrix[j, i] = val
195	        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)
196	        overlap_scores[layer_idx] = scores
197	        cka_matrices[layer_idx] = matrix
198	        logger.info(
199	            f"  Layer {layer_idx} {structure_name}: F(h) range [{scores.min():.4f}, {scores.max():.4f}], "
200	            f"mean={scores.mean():.4f}"
201	        )
202	    return overlap_scores, cka_matrices
203	
204	
205	def main():
206	    parser = argparse.ArgumentParser(description="Compute CKA-based functional overlap scores for RASP")
207	    parser.add_argument("--model_path", type=str, required=True, help="Path to pretrained model")
208	    parser.add_argument("--output_path", type=str, required=True, help="Output .pt file for overlap scores")
209	    parser.add_argument("--n_samples", type=int, default=512, help="Number of calibration samples")
210	    parser.add_argument("--max_length", type=int, default=512, help="Max token length for calibration inputs")
211	    parser.add_argument("--mlp_groups", type=int, default=28, help="Number of MLP channel groups per layer")
212	    parser.add_argument("--seed", type=int, default=42, help="Random seed")
213	    parser.add_argument("--dtype", type=str, default="bfloat16", choices=["float16", "bfloat16", "float32"])
214	    args = parser.parse_args()
215	
216	    set_seed(args.seed)
217	    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
218	    dtype_map = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}
219	    torch_dtype = dtype_map[args.dtype]
220	
221	    logger.info(f"Loading model from {args.model_path}")
222	    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
223	    model = AutoModelForCausalLM.from_pretrained(
224	        args.model_path,
225	        torch_dtype=torch_dtype,
226	        device_map=device,
227	        trust_remote_code=True,
228	    )
229	
230	    logger.info(f"Loading {args.n_samples} calibration samples from GSM8K train")
231	    calibration_data = load_calibration_data(tokenizer, args.n_samples, args.max_length, args.seed)
232	
233	    logger.info("Collecting attention head activations...")
234	    head_acts = collect_head_activations(model, tokenizer, calibration_data, device)
235	
236	    logger.info("Computing attention head overlap F(h)...")
237	    attn_overlap, attn_cka_matrix = compute_overlap(head_acts, "attn_heads")
238	    del head_acts
239	    torch.cuda.empty_cache()
240	
241	    logger.info("Collecting MLP activations...")
242	    mlp_acts = collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups=args.mlp_groups)
243	
244	    logger.info("Computing MLP group overlap F(h)...")
245	    mlp_overlap, mlp_cka_matrix = compute_overlap(mlp_acts, "mlp_groups")
246	    del mlp_acts
247	    torch.cuda.empty_cache()
248	
249	    os.makedirs(os.path.dirname(args.output_path) or ".", exist_ok=True)
250	    result = {
251	        "attn_overlap": attn_overlap,
252	        "mlp_overlap": mlp_overlap,
253	        "attn_cka_matrix": attn_cka_matrix,
254	        "mlp_cka_matrix": mlp_cka_matrix,
255	    }
256	    torch.save(result, args.output_path)
257	    logger.info(f"Saved CKA overlap scores to {args.output_path}")
258	
259	
260	if __name__ == "__main__":
261	    main()
262	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "498541a8-3e0b-49b1-ba0e-5b32138b5ae4"
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
  "task_id": "a2b810fef875789a5",
  "tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "description": "Reading src/run_cka_reliability.py",
  "usage": {
    "total_tokens": 34753,
    "tool_uses": 8,
    "duration_ms": 15231
  },
  "last_tool_name": "Read",
  "uuid": "459ca72a-1335-4be2-8ac4-26c90f17ad0f",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10"
}
```

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01S2dGdUyxiDbkcbRXi9rKVg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/run_cka_reliability.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "61c22c50-f22c-41b2-80df-1a2df948fb7e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TBsM2Wo89k7RRXonmjGeao",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 4074,
      "cache_read_input_tokens": 30616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4074,
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

_source line 31 · 2026-05-19T21:22:42.928Z_

<details><summary>↩ Tool result · `toolu_01S2dGdUyxiDbkcbRXi9rKVg`</summary>

```text
1	"""
2	CKA Reliability Analysis for RASP.
3	
4	Validates the stability of structural scoring by:
5	1-3. Cross-model CKA split-half reliability (original vs pruned, per GQA group)
6	4.   F(h) split-half reliability for attention heads (intra-layer overlap)
7	5.   F(h) split-half reliability for MLP groups (intra-layer overlap)
8	
9	Phases 1-3 address cross-model CKA stability.
10	Phases 4-5 address intra-layer F(h) stability (Claim 2 core metric).
11	"""
12	
13	import argparse
14	import json
15	import logging
16	import os
17	import random
18	import sys
19	
20	import numpy as np
21	import scipy.stats as stats
22	import torch
23	from datasets import load_dataset
24	from transformers import AutoModelForCausalLM, AutoTokenizer
25	
26	logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
27	logger = logging.getLogger(__name__)
28	
29	
30	def set_seed(seed):
31	    random.seed(seed)
32	    np.random.seed(seed)
33	    torch.manual_seed(seed)
34	    torch.cuda.manual_seed_all(seed)
35	
36	
37	def linear_cka(X, Y):
38	    """Linear CKA between two activation matrices. X: [n, p], Y: [n, q]."""
39	    X = X - X.mean(0)
40	    Y = Y - Y.mean(0)
41	    hsic_xy = torch.norm(X.T @ Y, "fro") ** 2
42	    hsic_xx = torch.norm(X.T @ X, "fro") ** 2
43	    hsic_yy = torch.norm(Y.T @ Y, "fro") ** 2
44	    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()
45	
46	
47	def load_calibration_data(tokenizer, n_samples, max_length=512, seed=42):
48	    ds = load_dataset("openai/gsm8k", "main", split="train")
49	    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))
50	    encodings = []
51	    for example in ds:
52	        prompt = f"Question: {example['question']}\nAnswer: Let me think step by step.\n"
53	        ids = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
54	        encodings.append(ids)
55	    return encodings
56	
57	
58	def collect_qproj_activations(model, calibration_data, device):
59	    """Collect per-head q_proj activations, mean-pooled over seq length.
60	    Returns dict[layer_idx] -> tensor[n_samples, n_heads_in_layer, head_dim] on CPU float32.
61	    """
62	    n_layers = model.config.num_hidden_layers
63	    head_dim = model.config.hidden_size // model.config.num_attention_heads
64	
65	    q_outputs = {i: [] for i in range(n_layers)}
66	    hooks = []
67	
68	    def make_hook(layer_idx):
69	        def fn(module, inp, out):
70	            q_outputs[layer_idx].append(out.detach().cpu())
71	        return fn
72	
73	    for i in range(n_layers):
74	        h = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_hook(i))
75	        hooks.append(h)
76	
77	    model.eval()
78	    with torch.no_grad():
79	        for idx, enc in enumerate(calibration_data):
80	            input_ids = enc["input_ids"].to(device)
81	            attention_mask = enc["attention_mask"].to(device)
82	            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)
83	            if (idx + 1) % 200 == 0:
84	                logger.info(f"  Forward pass {idx + 1}/{len(calibration_data)}")
85	
86	    for h in hooks:
87	        h.remove()
88	
89	    activations = {}
90	    for layer_idx in range(n_layers):
91	        out_dim = q_outputs[layer_idx][0].squeeze(0).shape[-1]
92	        n_heads = out_dim // head_dim
93	        per_head = []
94	        for t in q_outputs[layer_idx]:
95	            t = t.squeeze(0)  # [seq, n_heads * head_dim]
96	            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]
97	            t = t.mean(dim=0)  # [n_heads, head_dim]
98	            per_head.append(t)
99	        activations[layer_idx] = torch.stack(per_head, dim=0).float()
100	        q_outputs[layer_idx] = None
101	
102	    return activations
103	
104	
105	def collect_mlp_activations(model, calibration_data, device, n_groups=28):
106	    """Collect MLP gate_proj activations grouped into channel groups.
107	    Returns dict[layer_idx] -> tensor[n_samples, n_groups, group_dim] on CPU float32.
108	    """
109	    n_layers = model.config.num_hidden_layers
110	    intermediate_size = model.config.intermediate_size
111	    group_size = intermediate_size // n_groups
112	
113	    gate_outputs = {i: [] for i in range(n_layers)}
114	    hooks = []
115	
116	    def make_hook(layer_idx):
117	        def fn(module, inp, out):
118	            gate_outputs[layer_idx].append(out.detach().cpu())
119	        return fn
120	
121	    for i in range(n_layers):
122	        h = model.model.layers[i].mlp.gate_proj.register_forward_hook(make_hook(i))
123	        hooks.append(h)
124	
125	    model.eval()
126	    with torch.no_grad():
127	        for idx, enc in enumerate(calibration_data):
128	            input_ids = enc["input_ids"].to(device)
129	            attention_mask = enc["attention_mask"].to(device)
130	            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)
131	            if (idx + 1) % 200 == 0:
132	                logger.info(f"  Forward pass {idx + 1}/{len(calibration_data)}")
133	
134	    for h in hooks:
135	        h.remove()
136	
137	    activations = {}
138	    for layer_idx in range(n_layers):
139	        per_group = []
140	        for t in gate_outputs[layer_idx]:
141	            t = t.squeeze(0)  # [seq, intermediate_size]
142	            t = t.mean(dim=0)  # [intermediate_size]
143	            usable = n_groups * group_size
144	            t = t[:usable].view(n_groups, group_size)
145	            per_group.append(t)
146	        activations[layer_idx] = torch.stack(per_group, dim=0).float()
147	        gate_outputs[layer_idx] = None
148	
149	    return activations
150	
151	
152	def load_pruned_model_with_meta(base_model_path, pruned_model_path, torch_dtype, device):
153	    """Load structurally pruned model via base model reconstruction + saved weights."""
154	    meta_path = os.path.join(pruned_model_path, "pruning_metadata.pt")
155	    pruning_meta = torch.load(meta_path, map_location="cpu", weights_only=True)
156	
157	    src_dir = os.path.dirname(os.path.abspath(__file__))
158	    if src_dir not in sys.path:
159	        sys.path.insert(0, src_dir)
160	    from prune import prune_attention_heads, prune_mlp_channels
161	
162	    logging.getLogger("prune").setLevel(logging.WARNING)
163	    model = AutoModelForCausalLM.from_pretrained(
164	        base_model_path, torch_dtype=torch_dtype, device_map="cpu", trust_remote_code=True
165	    )
166	    prune_attention_heads(model, pruning_meta["attn_keep_masks"])
167	    prune_mlp_channels(model, pruning_meta["mlp_keep_masks"])
168	
169	    safetensor_files = sorted(
170	        [f for f in os.listdir(pruned_model_path) if f.endswith(".safetensors")]
171	    )
172	    if safetensor_files:
173	        from safetensors.torch import load_file
174	        state_dict = {}
175	        for f in safetensor_files:
176	            state_dict.update(load_file(os.path.join(pruned_model_path, f)))
177	    else:
178	        state_dict = torch.load(
179	            os.path.join(pruned_model_path, "pytorch_model.bin"),
180	            map_location="cpu", weights_only=True,
181	        )
182	    model.load_state_dict(state_dict)
183	    model.to(device)
184	    return model, pruning_meta
185	
186	
187	def compute_group_cka(orig_acts, pruned_acts, keep_masks, n_heads_orig, n_kv_heads,
188	                      sample_indices=None):
189	    """Compute per-GQA-group CKA between original and pruned representations.
190	
191	    For each KV group, concatenates retained Q head activations from both models
192	    and computes linear CKA. Original uses all Q heads in the group, pruned uses
193	    only retained Q heads (CKA handles different feature dimensions).
194	
195	    Returns dict[(layer, group)] -> float (or NaN if group fully pruned).
196	    """
197	    heads_per_kv = n_heads_orig // n_kv_heads
198	    n_layers = len(orig_acts)
199	    scores = {}
200	
201	    for layer_idx in range(n_layers):
202	        orig_layer = orig_acts[layer_idx]   # [N, n_heads_orig, head_dim]
203	        pruned_layer = pruned_acts[layer_idx]  # [N, n_retained, head_dim]
204	        retained = keep_masks[layer_idx]
205	
206	        if sample_indices is not None:
207	            orig_layer = orig_layer[sample_indices]
208	            pruned_layer = pruned_layer[sample_indices]
209	
210	        for g in range(n_kv_heads):
211	            orig_head_range = list(range(g * heads_per_kv, (g + 1) * heads_per_kv))
212	            pruned_positions = [i for i, h in enumerate(retained) if h in orig_head_range]
213	
214	            if not pruned_positions:
215	                scores[(layer_idx, g)] = float("nan")
216	                continue
217	
218	            n = orig_layer.shape[0]
219	            orig_flat = orig_layer[:, orig_head_range, :].reshape(n, -1)
220	            pruned_flat = pruned_layer[:, pruned_positions, :].reshape(n, -1)
221	            scores[(layer_idx, g)] = linear_cka(orig_flat, pruned_flat)
222	
223	    return scores
224	
225	
226	def scores_to_aligned_arrays(scores_a, scores_b):
227	    """Extract aligned non-NaN value arrays from two score dicts."""
228	    common = sorted(set(scores_a.keys()) & set(scores_b.keys()))
229	    a_vals, b_vals = [], []
230	    for k in common:
231	        va, vb = scores_a[k], scores_b[k]
232	        if (isinstance(va, float) and va != va) or (isinstance(vb, float) and vb != vb):
233	            continue
234	        a_vals.append(va)
235	        b_vals.append(vb)
236	    return np.array(a_vals), np.array(b_vals)
237	
238	
239	def compute_fh_scores(acts_dict, sample_indices=None):
240	    """Compute intra-layer F(h) for each structure.
241	    acts_dict: dict[layer_idx] -> tensor[n_samples, n_structs, dim]
242	    Returns dict[layer_idx] -> tensor[n_structs] of F(h) values.
243	    """
244	    fh = {}
245	    for layer_idx, acts in acts_dict.items():
246	        if sample_indices is not None:
247	            acts = acts[sample_indices]
248	        n_samples, n_structs, dim = acts.shape
249	        matrix = torch.zeros(n_structs, n_structs)
250	        for i in range(n_structs):
251	            matrix[i, i] = 1.0
252	            for j in range(i + 1, n_structs):
253	                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())
254	                matrix[i, j] = val
255	                matrix[j, i] = val
256	        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)
257	        fh[layer_idx] = scores
258	    return fh
259	
260	
261	def compute_fh_reliability(acts_dict, n_splits, seed, structure_name):
262	    """Split-half reliability of F(h) rankings across all layers.
263	    Returns list of per-split result dicts with Spearman rho.
264	    """
265	    n_total = next(iter(acts_dict.values())).shape[0]
266	    split_results = []
267	    for i in range(n_splits):
268	        rng = np.random.RandomState(seed + i)
269	        perm = rng.permutation(n_total)
270	        half = n_total // 2
271	        idx_a = sorted(perm[:half].tolist())
272	        idx_b = sorted(perm[half:2 * half].tolist())
273	
274	        logger.info(f"  Split {i}: computing F(h) on half A ({len(idx_a)} samples)...")
275	        fh_a = compute_fh_scores(acts_dict, idx_a)
276	        logger.info(f"  Split {i}: computing F(h) on half B ({len(idx_b)} samples)...")
277	        fh_b = compute_fh_scores(acts_dict, idx_b)
278	
279	        vals_a, vals_b = [], []
280	        for layer_idx in sorted(fh_a.keys()):
281	            vals_a.extend(fh_a[layer_idx].tolist())
282	            vals_b.extend(fh_b[layer_idx].tolist())
283	
284	        rho, p = stats.spearmanr(vals_a, vals_b)
285	        split_results.append({"split": i, "rho": float(rho), "p_value": float(p),
286	                              "n_structures": len(vals_a)})
287	        logger.info(f"  Split {i} {structure_name}: rho={rho:.4f}, p={p:.2e}, n={len(vals_a)}")
288	    return split_results
289	
290	
291	def main():
292	    parser = argparse.ArgumentParser(description="CKA Reliability Analysis for RASP scoring")
293	    parser.add_argument("--original_model", type=str, required=True)
294	    parser.add_argument("--pruned_model", type=str, default=None)
295	    parser.add_argument("--gpu_id", type=int, default=0)
296	    parser.add_argument("--num_samples", type=int, default=1024)
297	    parser.add_argument("--max_length", type=int, default=512)
298	    parser.add_argument("--n_splits", type=int, default=5)
299	    parser.add_argument("--output", type=str, required=True)
300	    parser.add_argument("--seed", type=int, default=42)
301	    parser.add_argument("--dtype", type=str, default="bfloat16",
302	                        choices=["float16", "bfloat16", "float32"])
303	    parser.add_argument("--mlp_groups", type=int, default=28,
304	                        help="Number of MLP channel groups per layer")
305	    parser.add_argument("--skip_cross_model", action="store_true",
306	                        help="Skip Phase 1-3 (cross-model CKA); only run F(h) reliability")
307	    args = parser.parse_args()
308	
309	    if not args.skip_cross_model and not args.pruned_model:
310	        parser.error("--pruned_model is required unless --skip_cross_model is set")
311	
312	    set_seed(args.seed)
313	    device = torch.device(f"cuda:{args.gpu_id}" if torch.cuda.is_available() else "cpu")
314	    torch_dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16,
315	                   "float32": torch.float32}[args.dtype]
316	
317	    logger.info("Loading tokenizer and calibration data...")
318	    tokenizer = AutoTokenizer.from_pretrained(args.original_model, trust_remote_code=True)
319	    calibration_data = load_calibration_data(tokenizer, args.num_samples, args.max_length,
320	                                             args.seed)
321	    n_total = len(calibration_data)
322	    logger.info(f"Loaded {n_total} calibration samples")
323	
324	    # --- Load original model and collect all activations ---
325	    logger.info("Loading original model...")
326	    orig_model = AutoModelForCausalLM.from_pretrained(
327	        args.original_model, torch_dtype=torch_dtype, device_map=device, trust_remote_code=True
328	    )
329	    config = orig_model.config
330	    n_heads_orig = config.num_attention_heads
331	    n_kv_heads = config.num_key_value_heads
332	    n_layers = config.num_hidden_layers
333	    heads_per_kv = n_heads_orig // n_kv_heads
334	    logger.info(f"Architecture: {n_layers}L x {n_heads_orig}Q x {n_kv_heads}KV "
335	                f"({heads_per_kv} Q/KV group, {n_layers * n_kv_heads} total groups)")
336	
337	    logger.info("Collecting original model q_proj activations...")
338	    orig_acts = collect_qproj_activations(orig_model, calibration_data, device)
339	
340	    logger.info("Collecting original model MLP gate_proj activations...")
341	    orig_mlp_acts = collect_mlp_activations(orig_model, calibration_data, device, args.mlp_groups)
342	
343	    del orig_model
344	    torch.cuda.empty_cache()
345	    logger.info("Original model freed. All activations cached on CPU.")
346	
347	    output = {
348	        "config": {
349	            "original_model": args.original_model,
350	            "num_samples": n_total,
351	            "n_layers": n_layers,
352	            "n_heads_original": n_heads_orig,
353	            "n_kv_heads": n_kv_heads,
354	            "heads_per_kv": heads_per_kv,
355	            "total_gqa_groups": n_layers * n_kv_heads,
356	            "mlp_groups": args.mlp_groups,
357	            "seed": args.seed,
358	        },
359	    }
360	
361	    # --- Phase 1-3: Cross-model CKA (optional) ---
362	    if not args.skip_cross_model:
363	        logger.info("Loading pruned model...")
364	        pruned_model, pruning_meta = load_pruned_model_with_meta(
365	            args.original_model, args.pruned_model, torch_dtype, device
366	        )
367	        keep_masks = pruning_meta["attn_keep_masks"]
368	        logger.info("Collecting pruned model activations...")
369	        pruned_acts = collect_qproj_activations(pruned_model, calibration_data, device)
370	        del pruned_model
371	        torch.cuda.empty_cache()
372	        logger.info("Pruned model freed.")
373	
374	        # Phase 1: Full CKA scores
375	        logger.info("=" * 50)
376	        logger.info("Phase 1: Full CKA scores (N=%d)...", n_total)
377	        full_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,
378	                                        n_heads_orig, n_kv_heads)
379	        valid_scores = {k: v for k, v in full_scores.items()
380	                        if not (isinstance(v, float) and v != v)}
381	        vals = np.array(list(valid_scores.values()))
382	        logger.info(f"Valid groups: {len(valid_scores)}/{n_layers * n_kv_heads}")
383	        logger.info(f"CKA: mean={vals.mean():.4f}, std={vals.std():.4f}, "
384	                    f"range=[{vals.min():.4f}, {vals.max():.4f}]")
385	
386	        # Phase 2: Split-half reliability (cross-model)
387	        logger.info("=" * 50)
388	        logger.info("Phase 2: Split-half reliability (%d splits)...", args.n_splits)
389	        cross_split_results = []
390	        for i in range(args.n_splits):
391	            rng = np.random.RandomState(args.seed + i)
392	            perm = rng.permutation(n_total)
393	            half = n_total // 2
394	            idx_a = sorted(perm[:half].tolist())
395	            idx_b = sorted(perm[half:2 * half].tolist())
396	
397	            scores_a = compute_group_cka(orig_acts, pruned_acts, keep_masks,
398	                                         n_heads_orig, n_kv_heads, idx_a)
399	            scores_b = compute_group_cka(orig_acts, pruned_acts, keep_masks,
400	                                         n_heads_orig, n_kv_heads, idx_b)
401	            arr_a, arr_b = scores_to_aligned_arrays(scores_a, scores_b)
402	            rho, p = stats.spearmanr(arr_a, arr_b)
403	            cross_split_results.append({"split": i, "rho": float(rho), "p_value": float(p),
404	                                        "n_groups": len(arr_a)})
405	            logger.info(f"  Split {i}: rho={rho:.4f}, p={p:.2e}")
406	
407	        cross_mean_rho = float(np.mean([r["rho"] for r in cross_split_results]))
408	        cross_std_rho = float(np.std([r["rho"] for r in cross_split_results]))
409	
410	        # Phase 3: Calibration size sensitivity
411	        logger.info("=" * 50)
412	        logger.info("Phase 3: Calibration size sensitivity...")
413	        size_results = []
414	        for n_sub in [128, 256, 512]:
415	            if n_sub >= n_total:
416	                continue
417	            rng = np.random.RandomState(args.seed)
418	            sub_idx = sorted(rng.permutation(n_total)[:n_sub].tolist())
419	
420	            sub_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,
421	                                           n_heads_orig, n_kv_heads, sub_idx)
422	            ref_vals, sub_vals = scores_to_aligned_arrays(full_scores, sub_scores)
423	            rho, p = stats.spearmanr(ref_vals, sub_vals)
424	            size_results.append({"n_samples": n_sub, "rho_vs_full": float(rho),
425	                                 "p_value": float(p)})
426	            logger.info(f"  N={n_sub}: rho={rho:.4f} vs N={n_total}")
427	
428	        del pruned_acts
429	        torch.cuda.empty_cache()
430	
431	        per_group = {}
432	        for (l, g), v in full_scores.items():
433	            key = f"layer{l}_group{g}"
434	            per_group[key] = None if (isinstance(v, float) and v != v) else float(v)
435	
436	        output["config"]["pruned_model"] = args.pruned_model
437	        output["config"]["valid_gqa_groups"] = len(valid_scores)
438	        output["per_group_cka_scores"] = per_group
439	        output["cka_summary"] = {
440	            "mean": float(vals.mean()),
441	            "std": float(vals.std()),
442	            "min": float(vals.min()),
443	            "max": float(vals.max()),
444	            "median": float(np.median(vals)),
445	        }
446	        output["split_half_reliability"] = {
447	            "per_split": cross_split_results,
448	            "mean_rho": cross_mean_rho,
449	            "std_rho": cross_std_rho,
450	            "pass": cross_mean_rho > 0.9,
451	        }
452	        output["size_sensitivity"] = {
453	            "reference_n": n_total,
454	            "per_size": size_results,
455	            "all_pass_0.9": all(s["rho_vs_full"] > 0.9 for s in size_results),
456	        }
457	
458	    # --- Phase 4: F(h) attention head split-half reliability ---
459	    logger.info("=" * 50)
460	    logger.info("Phase 4: F(h) attention head split-half reliability (%d splits)...",
461	                args.n_splits)
462	    attn_fh_results = compute_fh_reliability(orig_acts, args.n_splits, args.seed, "attn_heads")
463	    attn_mean_rho = float(np.mean([r["rho"] for r in attn_fh_results]))
464	    attn_std_rho = float(np.std([r["rho"] for r in attn_fh_results]))
465	    attn_pass = attn_mean_rho > 0.9
466	    logger.info(f"Attn F(h) reliability: mean_rho={attn_mean_rho:.4f} +/- {attn_std_rho:.4f} "
467	                f"{'PASS' if attn_pass else 'FAIL'}")
468	
469	    output["fh_attn_reliability"] = {
470	        "per_split": attn_fh_results,
471	        "mean_rho": attn_mean_rho,
472	        "std_rho": attn_std_rho,
473	        "pass": attn_pass,
474	    }
475	
476	    del orig_acts
477	    torch.cuda.empty_cache()
478	
479	    # --- Phase 5: F(h) MLP group split-half reliability ---
480	    logger.info("=" * 50)
481	    logger.info("Phase 5: F(h) MLP group split-half reliability (%d splits)...", args.n_splits)
482	    mlp_fh_results = compute_fh_reliability(orig_mlp_acts, args.n_splits, args.seed, "mlp_groups")
483	    mlp_mean_rho = float(np.mean([r["rho"] for r in mlp_fh_results]))
484	    mlp_std_rho = float(np.std([r["rho"] for r in mlp_fh_results]))
485	    mlp_pass = mlp_mean_rho > 0.9
486	    logger.info(f"MLP F(h) reliability: mean_rho={mlp_mean_rho:.4f} +/- {mlp_std_rho:.4f} "
487	                f"{'PASS' if mlp_pass else 'FAIL'}")
488	
489	    output["fh_mlp_reliability"] = {
490	        "per_split": mlp_fh_results,
491	        "mean_rho": mlp_mean_rho,
492	        "std_rho": mlp_std_rho,
493	        "pass": mlp_pass,
494	    }
495	
496	    del orig_mlp_acts
497	    torch.cuda.empty_cache()
498	
499	    # --- Save results ---
500	    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
501	    with open(args.output, "w") as f:
502	        json.dump(output, f, indent=2)
503	    logger.info(f"Results saved to {args.output}")
504	
505	    # --- Print summary ---
506	    print(f"\n{'=' * 60}")
507	    print("CKA Reliability Analysis")
508	    print(f"{'=' * 60}")
509	
510	    if not args.skip_cross_model:
511	        print(f"\nCross-model CKA (Phase 1-3):")
512	        print(f"  GQA groups: {len(valid_scores)}/{n_layers * n_kv_heads} valid")
513	        print(f"  CKA scores: {vals.mean():.4f} +/- {vals.std():.4f} "
514	              f"[{vals.min():.4f}, {vals.max():.4f}]")
515	        sh_pass = "PASS" if cross_mean_rho > 0.9 else "FAIL"
516	        print(f"  Split-half reliability ({args.n_splits} splits):")
517	        print(f"    rho = {cross_mean_rho:.4f} +/- {cross_std_rho:.4f}  {sh_pass} "
518	              f"(threshold: 0.9)")
519	        for r in cross_split_results:
520	            print(f"      Split {r['split']}: rho={r['rho']:.4f}")
521	        print(f"  Size sensitivity (vs N={n_total}):")
522	        for s in size_results:
523	            sv = "PASS" if s["rho_vs_full"] > 0.9 else "FAIL"
524	            print(f"    N={s['n_samples']:4d}: rho={s['rho_vs_full']:.4f}  {sv}")
525	
526	    print(f"\nF(h) Attention head reliability (Phase 4):")
527	    ah_label = "PASS" if attn_pass else "FAIL"
528	    print(f"  rho = {attn_mean_rho:.4f} +/- {attn_std_rho:.4f}  {ah_label} (threshold: 0.9)")
529	    for r in attn_fh_results:
530	        print(f"    Split {r['split']}: rho={r['rho']:.4f}")
531	
532	    print(f"\nF(h) MLP group reliability (Phase 5):")
533	    mh_label = "PASS" if mlp_pass else "FAIL"
534	    print(f"  rho = {mlp_mean_rho:.4f} +/- {mlp_std_rho:.4f}  {mh_label} (threshold: 0.9)")
535	    for r in mlp_fh_results:
536	        print(f"    Split {r['split']}: rho={r['rho']:.4f}")
537	
538	    print(f"{'=' * 60}")
539	
540	
541	if __name__ == "__main__":
542	    main()
543	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "613c1474-8464-48ac-85e9-7ed2257b8677"
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
  "task_id": "a2b810fef875789a5",
  "tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "description": "Reading src/model_utils.py",
  "usage": {
    "total_tokens": 43755,
    "tool_uses": 9,
    "duration_ms": 17216
  },
  "last_tool_name": "Read",
  "uuid": "b80edbe0-0acc-4ae3-8148-b1ce79f8e891",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10"
}
```

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01McSgmhbLSd9dyq7DM37KKn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/model_utils.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "f5d64c87-31e9-4e3e-958d-87eb9bd584b9",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AGbQCjeHZArwYBF6vcgfHS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 8994,
      "cache_read_input_tokens": 34690,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8994,
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

_source line 34 · 2026-05-19T21:22:44.914Z_

<details><summary>↩ Tool result · `toolu_01McSgmhbLSd9dyq7DM37KKn`</summary>

```text
1	import logging
2	import os
3	
4	import torch
5	import torch.nn as nn
6	from transformers import AutoConfig, AutoModelForCausalLM
7	
8	logger = logging.getLogger(__name__)
9	
10	
11	def _load_state_dict(model_path):
12	    safetensor_files = sorted(
13	        f for f in os.listdir(model_path) if f.endswith(".safetensors")
14	    )
15	    if safetensor_files:
16	        from safetensors.torch import load_file
17	        state_dict = {}
18	        for f in safetensor_files:
19	            state_dict.update(load_file(os.path.join(model_path, f)))
20	        return state_dict
21	    return torch.load(
22	        os.path.join(model_path, "pytorch_model.bin"),
23	        map_location="cpu", weights_only=True,
24	    )
25	
26	
27	def load_pruned_model(model_path, device_map="auto", torch_dtype=torch.bfloat16):
28	    """Load a pruned model that may have non-uniform MLP/attention dimensions per layer."""
29	    config = AutoConfig.from_pretrained(model_path, trust_remote_code=True)
30	    per_layer_sizes = getattr(config, "per_layer_intermediate_size", None)
31	    per_layer_heads = getattr(config, "per_layer_num_heads", None)
32	    per_layer_kv_heads = getattr(config, "per_layer_num_kv_heads", None)
33	
34	    if per_layer_sizes is None and per_layer_heads is None:
35	        return AutoModelForCausalLM.from_pretrained(
36	            model_path, torch_dtype=torch_dtype, device_map=device_map,
37	            trust_remote_code=True,
38	        )
39	
40	    hidden_size = config.hidden_size
41	    head_dim = getattr(config, "head_dim", hidden_size // config.num_attention_heads)
42	
43	    if per_layer_sizes is not None:
44	        max_size = max(per_layer_sizes)
45	        config.intermediate_size = max_size
46	        logger.info(
47	            "Non-uniform MLP detected: intermediate_size range [%d, %d]",
48	            min(per_layer_sizes), max_size,
49	        )
50	
51	    if per_layer_heads is not None:
52	        config.num_attention_heads = max(per_layer_heads)
53	        config.num_key_value_heads = max(per_layer_kv_heads)
54	        logger.info(
55	            "Non-uniform attention detected: heads range [%d, %d], kv_heads range [%d, %d]",
56	            min(per_layer_heads), max(per_layer_heads),
57	            min(per_layer_kv_heads), max(per_layer_kv_heads),
58	        )
59	
60	    prev_dtype = torch.get_default_dtype()
61	    torch.set_default_dtype(torch_dtype)
62	    try:
63	        model = AutoModelForCausalLM.from_config(config)
64	        num_layers = len(model.model.layers)
65	
66	        for layer_idx in range(num_layers):
67	            layer = model.model.layers[layer_idx]
68	
69	            if per_layer_sizes is not None:
70	                size = per_layer_sizes[layer_idx]
71	                if size != config.intermediate_size:
72	                    mlp = layer.mlp
73	                    mlp.gate_proj = nn.Linear(hidden_size, size, bias=False)
74	                    mlp.up_proj = nn.Linear(hidden_size, size, bias=False)
75	                    mlp.down_proj = nn.Linear(size, hidden_size, bias=False)
76	
77	            if per_layer_heads is not None:
78	                nh = per_layer_heads[layer_idx]
79	                nkv = per_layer_kv_heads[layer_idx]
80	                if nh != config.num_attention_heads or nkv != config.num_key_value_heads:
81	                    attn = layer.self_attn
82	                    q_out = nh * head_dim
83	                    kv_out = nkv * head_dim
84	                    attn.q_proj = nn.Linear(hidden_size, q_out, bias=getattr(attn.q_proj, 'bias', None) is not None)
85	                    attn.k_proj = nn.Linear(hidden_size, kv_out, bias=getattr(attn.k_proj, 'bias', None) is not None)
86	                    attn.v_proj = nn.Linear(hidden_size, kv_out, bias=getattr(attn.v_proj, 'bias', None) is not None)
87	                    attn.o_proj = nn.Linear(q_out, hidden_size, bias=getattr(attn.o_proj, 'bias', None) is not None)
88	                    attn.num_heads = nh
89	                    attn.num_key_value_heads = nkv
90	                    attn.num_key_value_groups = max(1, nh // max(1, nkv))
91	                    attn.head_dim = head_dim
92	    finally:
93	        torch.set_default_dtype(prev_dtype)
94	
95	    state_dict = _load_state_dict(model_path)
96	    model.load_state_dict(state_dict, strict=True)
97	    del state_dict
98	
99	    if device_map == "auto":
100	        model = model.cuda()
101	    elif device_map is not None and str(device_map) != "cpu":
102	        model = model.to(device_map)
103	
104	    model.eval()
105	    return model
106	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "b913f4d0-bcc7-4209-a116-5c7c01e464ce"
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
  "task_id": "a2b810fef875789a5",
  "tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "description": "Reading src/rasp_scoring.py",
  "usage": {
    "total_tokens": 45491,
    "tool_uses": 10,
    "duration_ms": 19318
  },
  "last_tool_name": "Read",
  "uuid": "f2a42e6a-fdd6-4081-9497-f5ddedb76dcf",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10"
}
```

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01YNspqRtGJmriqiy5uSHL7x`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/rasp_scoring.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "a238dfb6-1c75-4952-94dc-708f0e814623",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SyrTXc5G4gLFsiymF9csYg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1730,
      "cache_read_input_tokens": 43684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1730,
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

_source line 37 · 2026-05-19T21:22:47.029Z_

<details><summary>↩ Tool result · `toolu_01YNspqRtGJmriqiy5uSHL7x`</summary>

```text
1	"""
2	RASP Scoring: combine importance I(h) and functional overlap F(h).
3	
4	S(h) = I(h) * (1 - F(h))^alpha
5	
6	Structures with lower S(h) are pruned first.
7	Standard baseline uses only I(h) for ranking.
8	"""
9	
10	import argparse
11	import logging
12	import os
13	
14	import torch
15	
16	logging.basicConfig(
17	    level=logging.INFO,
18	    format="%(asctime)s [%(levelname)s] %(message)s",
19	)
20	logger = logging.getLogger(__name__)
21	
22	
23	def compute_rasp_scores(importance: dict, overlap: dict, alpha: float = 1.0) -> dict:
24	    """Compute S(h) = I(h) * (1 - F(h))^alpha for each structure.
25	
26	    Args:
27	        importance: dict[layer_idx -> tensor of I(h)]
28	        overlap: dict[layer_idx -> tensor of F(h)]
29	        alpha: recoverability penalty exponent
30	
31	    Returns:
32	        dict[layer_idx -> tensor of S(h)]
33	    """
34	    scores = {}
35	    for layer_idx in importance:
36	        ih = importance[layer_idx].float()
37	        fh = overlap[layer_idx].float()
38	        sh = ih * (1.0 - fh).pow(alpha)
39	        scores[layer_idx] = sh
40	    return scores
41	
42	
43	def rank_structures(scores: dict) -> list:
44	    """Flatten and rank all structures globally by score (ascending = prune first).
45	
46	    Returns list of (score, layer_idx, struct_idx) sorted ascending.
47	    """
48	    entries = []
49	    for layer_idx, layer_scores in scores.items():
50	        for struct_idx in range(layer_scores.shape[0]):
51	            entries.append((layer_scores[struct_idx].item(), layer_idx, struct_idx))
52	    entries.sort(key=lambda x: x[0])
53	    return entries
54	
55	
56	def main():
57	    parser = argparse.ArgumentParser(description="Compute RASP pruning scores")
58	    parser.add_argument("--importance_path", type=str, required=True, help="Path to importance scores .pt")
59	    parser.add_argument("--cka_path", type=str, default=None, help="Path to CKA overlap scores .pt (None for standard mode)")
60	    parser.add_argument("--mode", type=str, choices=["standard", "rasp"], default="rasp")
61	    parser.add_argument("--alpha", type=float, default=1.0, help="Recoverability penalty exponent")
62	    parser.add_argument("--output_path", type=str, required=True, help="Output .pt file for pruning scores")
63	    args = parser.parse_args()
64	
65	    importance_data = torch.load(args.importance_path, map_location="cpu", weights_only=True)
66	    attn_importance = importance_data["attn_importance"]
67	    mlp_importance = importance_data["mlp_importance"]
68	
69	    if args.mode == "rasp":
70	        if args.cka_path is None:
71	            raise ValueError("--cka_path required for rasp mode")
72	        cka_data = torch.load(args.cka_path, map_location="cpu", weights_only=True)
73	        attn_overlap = cka_data["attn_overlap"]
74	        mlp_overlap = cka_data["mlp_overlap"]
75	
76	        attn_scores = compute_rasp_scores(attn_importance, attn_overlap, args.alpha)
77	        mlp_scores = compute_rasp_scores(mlp_importance, mlp_overlap, args.alpha)
78	        logger.info(f"Computed RASP scores with alpha={args.alpha}")
79	    else:
80	        # Standard: score = importance only
81	        attn_scores = {k: v.float() for k, v in attn_importance.items()}
82	        mlp_scores = {k: v.float() for k, v in mlp_importance.items()}
83	        logger.info("Computed standard importance-only scores")
84	
85	    attn_ranking = rank_structures(attn_scores)
86	    mlp_ranking = rank_structures(mlp_scores)
87	
88	    logger.info(f"Attention heads total: {len(attn_ranking)}, lowest 5 scores: "
89	                f"{[f'L{e[1]}H{e[2]}={e[0]:.6f}' for e in attn_ranking[:5]]}")
90	    logger.info(f"MLP groups total: {len(mlp_ranking)}, lowest 5 scores: "
91	                f"{[f'L{e[1]}G{e[2]}={e[0]:.6f}' for e in mlp_ranking[:5]]}")
92	
93	    os.makedirs(os.path.dirname(args.output_path) or ".", exist_ok=True)
94	    result = {
95	        "attn_scores": attn_scores,
96	        "mlp_scores": mlp_scores,
97	        "attn_ranking": attn_ranking,
98	        "mlp_ranking": mlp_ranking,
99	        "mode": args.mode,
100	        "alpha": args.alpha,
101	    }
102	    torch.save(result, args.output_path)
103	    logger.info(f"Saved pruning scores to {args.output_path}")
104	
105	
106	if __name__ == "__main__":
107	    main()
108	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "a33d0b20-2205-471e-98c4-e8b860337732"
}
```

</details>

---

### System

_source line 38_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a2b810fef875789a5",
  "tool_use_id": "toolu_016Tg2EEvBPGKBxJ82QSY39c",
  "status": "completed",
  "output_file": "",
  "summary": "Explore CKA scoring code",
  "usage": {
    "total_tokens": 47154,
    "tool_uses": 10,
    "duration_ms": 35222
  },
  "uuid": "ed52bd94-69ac-4858-b50d-9e05736b4cc7",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10"
}
```

---

### Tool result

_source line 39 · 2026-05-19T21:23:02.918Z_

<details><summary>↩ Tool result · `toolu_016Tg2EEvBPGKBxJ82QSY39c`</summary>

````text
Perfect! Now let me create a comprehensive summary document based on my findings:

## Summary: CKA Scoring Implementation in Recovery-Aware Structural Pruning

Based on my thorough analysis of the codebase, here's the complete breakdown of the CKA scoring implementation:

### 1. **CKA Scoring Function & Implementation**

The CKA (Centered Kernel Alignment) scoring is computed in `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_overlap.py`:

- **Function**: `linear_cka()` (lines 38-47) - Computes linear CKA similarity between two activation matrices X and Y
- **Formula**: `CKA(X,Y) = HSIC(X,Y) / (√HSIC(X,X) × √HSIC(Y,Y))`
  - X, Y are [n, p] and [n, q] shaped activation matrices
  - HSIC = Frobenius norm of X^T @ Y (Hilbert-Schmidt Independence Criterion)
  - Returns scalar similarity in [0, 1]

- **Per-structure F(h) computation** (lines 176-202):
  - Computes pairwise CKA matrix between all structures in a layer
  - F(h) = mean CKA of structure h with all other structures
  - Formula: `F(h) = (sum of CKA similarities for h) - 1 / (n_structures - 1)`
  - Returns dict[layer_idx] -> tensor[n_structures] of overlap scores F(h) in [0, 1]

### 2. **Calibration Data**

**Source**: GSM8K train split (OpenAI's Grade School Math 8K dataset)

From `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_overlap.py` (lines 50-60):
```python
def load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):
    ds = load_dataset("openai/gsm8k", "main", split="train")
    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))
    # Prompt format: "Question: {question}\nAnswer: Let me think step by step.\n"
```

### 3. **Default Calibration Size**

- **Default**: 512 samples (line 209 in cka_overlap.py: `default=512`)
- Configurable via `--n_samples` argument
- Max sequence length: 512 tokens (default, configurable via `--max_length`)
- Seed: 42 (default for reproducibility)

### 4. **Prunable Structures**

Two types of structures are pruned:

**A. Attention Heads**
- Per layer: structures are individual attention heads
- Total structures per layer: `n_heads` (default: 28 for the model)
- GQA (Grouped Query Attention) handling:
  - Model has 28 query heads but uses key-value heads (KV) for efficiency
  - When Q heads mapping to same KV head are pruned, the KV head is also removed
  - Activations: q_proj output, mean-pooled over sequence length
  - Dimension: [n_samples, n_heads, head_dim]

**B. MLP Channel Groups**
- Per layer: intermediate activations are grouped into channel groups
- Default groups: 28 groups per layer (configurable via `--mlp_groups`)
- Group size: `intermediate_size / n_groups` (typically 256 channels per group)
- Activations: gate_proj output, mean-pooled over sequence length
- Dimension: [n_samples, n_groups, group_size]

From `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_overlap.py` (lines 63-123 for attention, 126-173 for MLP):
- Attention uses `q_proj` hook output
- MLP uses `gate_proj` hook output
- Both mean-pooled over sequence dimension before CKA computation

### 5. **Model Loading**

**Default model path**: Qwen2.5 family models (from HuggingFace)

From `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_overlap.py` (lines 221-228):
```python
tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    args.model_path,
    torch_dtype=torch_dtype,
    device_map=device,
    trust_remote_code=True,
)
```

- Architecture: Qwen2.5 (supports GQA)
- Loaded via `transformers.AutoModelForCausalLM`
- Data types supported: float16, bfloat16 (default), float32
- Device: CUDA if available, otherwise CPU

### 6. **Complete RASP Scoring Pipeline**

From `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/rasp_scoring.py`:

**Combined RASP Score**:
```
S(h) = I(h) × (1 - F(h))^α
```

Where:
- `I(h)` = gradient-based importance (Taylor expansion: ||w_h × grad_h||_2)
- `F(h)` = functional overlap (mean CKA with other structures)
- `α` = recoverability penalty exponent (default: 1.0, configurable)

**Pruning Strategy** (from prune.py):
- Ranks all structures globally by S(h)
- Greedily selects lowest-scoring structures to prune
- Enforces minimum of 4 structures per layer (safety constraint)
- Uses parameter-weighted selection (attn_params_per_head vs mlp_params_per_group)

### 7. **Key File Locations**

- **CKA computation**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_overlap.py`
- **Importance scoring**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/importance_score.py`
- **RASP scoring**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/rasp_scoring.py`
- **Pruning execution**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/prune.py`
- **Reliability validation**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/run_cka_reliability.py`

### 8. **Reliability Validation**

The `run_cka_reliability.py` script (22KB) validates CKA stability across:
- **Phase 1-3**: Cross-model CKA (original vs pruned), split-half reliability, calibration size sensitivity
- **Phase 4**: F(h) attention head split-half reliability (Spearman rho > 0.9)
- **Phase 5**: F(h) MLP group split-half reliability (Spearman rho > 0.9)
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "e4a89771-b5b8-423b-b9c3-8fdecda9b519",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to understand the CKA scoring implementation in this ML pruning project. The project is at /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/\n\nI need to find:\n1. How CKA scores are computed (which function/class)\n2. What calibration data is used (GSM8K train? something else?)\n3. Default calibration size\n4. What \"prunable structures\" are (attention heads, MLP groups, etc.)\n5. How the model is loaded and what model path is used\n\nSearch broadly in:\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/src/\n- Any other relevant directories\n\nLook for files like cka.py, prune.py, scoring.py, config files, etc. Read the key files thoroughly to understand the full CKA scoring pipeline.",
    "agentId": "a2b810fef875789a5",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now let me create a comprehensive summary document based on my findings:\n\n## Summary: CKA Scoring Implementation in Recovery-Aware Structural Pruning\n\nBased on my thorough analysis of the codebase, here's the complete breakdown of the CKA scoring implementation:\n\n### 1. **CKA Scoring Function & Implementation**\n\nThe CKA (Centered Kernel Alignment) scoring is computed in `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_overlap.py`:\n\n- **Function**: `linear_cka()` (lines 38-47) - Computes linear CKA similarity between two activation matrices X and Y\n- **Formula**: `CKA(X,Y) = HSIC(X,Y) / (√HSIC(X,X) × √HSIC(Y,Y))`\n  - X, Y are [n, p] and [n, q] shaped activation matrices\n  - HSIC = Frobenius norm of X^T @ Y (Hilbert-Schmidt Independence Criterion)\n  - Returns scalar similarity in [0, 1]\n\n- **Per-structure F(h) computation** (lines 176-202):\n  - Computes pairwise CKA matrix between all structures in a layer\n  - F(h) = mean CKA of structure h with all other structures\n  - Formula: `F(h) = (sum of CKA similarities for h) - 1 / (n_structures - 1)`\n  - Returns dict[layer_idx] -> tensor[n_structures] of overlap scores F(h) in [0, 1]\n\n### 2. **Calibration Data**\n\n**Source**: GSM8K train split (OpenAI's Grade School Math 8K dataset)\n\nFrom `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_overlap.py` (lines 50-60):\n```python\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\n    ds = load_dataset(\"openai/gsm8k\", \"main\", split=\"train\")\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\n    # Prompt format: \"Question: {question}\\nAnswer: Let me think step by step.\\n\"\n```\n\n### 3. **Default Calibration Size**\n\n- **Default**: 512 samples (line 209 in cka_overlap.py: `default=512`)\n- Configurable via `--n_samples` argument\n- Max sequence length: 512 tokens (default, configurable via `--max_length`)\n- Seed: 42 (default for reproducibility)\n\n### 4. **Prunable Structures**\n\nTwo types of structures are pruned:\n\n**A. Attention Heads**\n- Per layer: structures are individual attention heads\n- Total structures per layer: `n_heads` (default: 28 for the model)\n- GQA (Grouped Query Attention) handling:\n  - Model has 28 query heads but uses key-value heads (KV) for efficiency\n  - When Q heads mapping to same KV head are pruned, the KV head is also removed\n  - Activations: q_proj output, mean-pooled over sequence length\n  - Dimension: [n_samples, n_heads, head_dim]\n\n**B. MLP Channel Groups**\n- Per layer: intermediate activations are grouped into channel groups\n- Default groups: 28 groups per layer (configurable via `--mlp_groups`)\n- Group size: `intermediate_size / n_groups` (typically 256 channels per group)\n- Activations: gate_proj output, mean-pooled over sequence length\n- Dimension: [n_samples, n_groups, group_size]\n\nFrom `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_overlap.py` (lines 63-123 for attention, 126-173 for MLP):\n- Attention uses `q_proj` hook output\n- MLP uses `gate_proj` hook output\n- Both mean-pooled over sequence dimension before CKA computation\n\n### 5. **Model Loading**\n\n**Default model path**: Qwen2.5 family models (from HuggingFace)\n\nFrom `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_overlap.py` (lines 221-228):\n```python\ntokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\nmodel = AutoModelForCausalLM.from_pretrained(\n    args.model_path,\n    torch_dtype=torch_dtype,\n    device_map=device,\n    trust_remote_code=True,\n)\n```\n\n- Architecture: Qwen2.5 (supports GQA)\n- Loaded via `transformers.AutoModelForCausalLM`\n- Data types supported: float16, bfloat16 (default), float32\n- Device: CUDA if available, otherwise CPU\n\n### 6. **Complete RASP Scoring Pipeline**\n\nFrom `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/rasp_scoring.py`:\n\n**Combined RASP Score**:\n```\nS(h) = I(h) × (1 - F(h))^α\n```\n\nWhere:\n- `I(h)` = gradient-based importance (Taylor expansion: ||w_h × grad_h||_2)\n- `F(h)` = functional overlap (mean CKA with other structures)\n- `α` = recoverability penalty exponent (default: 1.0, configurable)\n\n**Pruning Strategy** (from prune.py):\n- Ranks all structures globally by S(h)\n- Greedily selects lowest-scoring structures to prune\n- Enforces minimum of 4 structures per layer (safety constraint)\n- Uses parameter-weighted selection (attn_params_per_head vs mlp_params_per_group)\n\n### 7. **Key File Locations**\n\n- **CKA computation**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_overlap.py`\n- **Importance scoring**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/importance_score.py`\n- **RASP scoring**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/rasp_scoring.py`\n- **Pruning execution**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/prune.py`\n- **Reliability validation**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/run_cka_reliability.py`\n\n### 8. **Reliability Validation**\n\nThe `run_cka_reliability.py` script (22KB) validates CKA stability across:\n- **Phase 1-3**: Cross-model CKA (original vs pruned), split-half reliability, calibration size sensitivity\n- **Phase 4**: F(h) attention head split-half reliability (Spearman rho > 0.9)\n- **Phase 5**: F(h) MLP group split-half reliability (Spearman rho > 0.9)"
      }
    ],
    "totalDurationMs": 35224,
    "totalTokens": 48985,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1662,
      "cache_read_input_tokens": 45414,
      "output_tokens": 1904,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1662
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1904,
          "cache_read_input_tokens": 45414,
          "cache_creation_input_tokens": 1662,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1662,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 6,
      "searchCount": 1,
      "bashCount": 3,
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

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01BZU6BJKpM8YGfbyPoci4wx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/src/cka_overlap.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "043f6211-1df1-44e2-9404-b1fc40610f4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UAs9c5TeDNhMNMuVWtgVrW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2260,
      "cache_read_input_tokens": 24381,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2260
      },
      "output_tokens": 61,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_01TXP8kpHkw4bY2AGr7GSbNj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/src/run_cka_reliability.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "f55d8818-2d42-4164-ada3-29a2de9c779a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UAs9c5TeDNhMNMuVWtgVrW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2260,
      "cache_read_input_tokens": 24381,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2260
      },
      "output_tokens": 61,
      "service_tier": "standard",
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

_source line 42 · 2026-05-19T21:23:05.621Z_

<details><summary>↩ Tool result · reported error · `toolu_01BZU6BJKpM8YGfbyPoci4wx`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "0b9c92e6-0cc4-458d-a577-37f19650f060",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune."
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-19T21:23:05.622Z_

<details><summary>↩ Tool result · reported error · `toolu_01TXP8kpHkw4bY2AGr7GSbNj`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "1bd25648-4357-444d-a283-a934ef390b0b",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune."
}
```

</details>

---

### Assistant

_source line 44_

<details><summary>Logged reasoning block</summary>

```text
The files are on the remote server, not locally. Let me check the local artifacts directory and also read from the remote server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "711374e3-7abf-44b8-bacf-4e70fde1909c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Jnkg3Qk7LncRCcbpAy6EV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 314,
      "cache_read_input_tokens": 26641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 314
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

_source line 45_

<details open><summary>🔧 Tool call — Glob · `toolu_011WPuMXjBSdVbkYvJLEuYpE`</summary>

```json
{
  "pattern": "artifacts/**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "86864640-65c7-48c3-a771-205082f30f90",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Jnkg3Qk7LncRCcbpAy6EV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 314,
      "cache_read_input_tokens": 26641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 314
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

_source line 46 · 2026-05-19T21:23:09.139Z_

<details><summary>↩ Tool result · `toolu_011WPuMXjBSdVbkYvJLEuYpE`</summary>

```text
artifacts/correlation_analysis.py
artifacts/plot_cka_figures.py
artifacts/_project/intermediate/plot_fig1_pipeline.py
artifacts/plot_fig1_pipeline.py
artifacts/figures/gen_fig2_reward_trajectories.py
artifacts/figures/gen_fig3_collapse_dynamics.py
artifacts/figures/gen_fig1_framework.py
artifacts/bootstrap_ci_analysis.py
artifacts/prune_shortgpt.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "c8d726d1-af45-418c-a1ca-5faeffaf5651",
  "tool_use_result": {
    "filenames": [
      "artifacts/correlation_analysis.py",
      "artifacts/plot_cka_figures.py",
      "artifacts/_project/intermediate/plot_fig1_pipeline.py",
      "artifacts/plot_fig1_pipeline.py",
      "artifacts/figures/gen_fig2_reward_trajectories.py",
      "artifacts/figures/gen_fig3_collapse_dynamics.py",
      "artifacts/figures/gen_fig1_framework.py",
      "artifacts/bootstrap_ci_analysis.py",
      "artifacts/prune_shortgpt.py"
    ],
    "durationMs": 28,
    "numFiles": 9,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Glob · `toolu_012kfjUwma9nz79CF8JWSi9V`</summary>

```json
{
  "pattern": "src/**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "22b22a47-7c9c-4e8d-a867-c289d6b5fdf6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Jnkg3Qk7LncRCcbpAy6EV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 314,
      "cache_read_input_tokens": 26641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 314
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

_source line 48 · 2026-05-19T21:23:09.797Z_

<details><summary>↩ Tool result · `toolu_012kfjUwma9nz79CF8JWSi9V`</summary>

```text
src/importance_score.py
src/rasp_scoring.py
src/prune.py
src/train_grpo.py
src/eval_gsm8k.py
src/correlation_analysis.py
src/cka_overlap.py
src/grasp_scoring.py
src/run_cka_reliability.py
src/model_utils.py
src/convert_graspune_to_hf.py
src/eval_mbpp.py
src/gradient_flow_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "227ccd33-9155-49d7-80e5-7ba966c9721f",
  "tool_use_result": {
    "filenames": [
      "src/importance_score.py",
      "src/rasp_scoring.py",
      "src/prune.py",
      "src/train_grpo.py",
      "src/eval_gsm8k.py",
      "src/correlation_analysis.py",
      "src/cka_overlap.py",
      "src/grasp_scoring.py",
      "src/run_cka_reliability.py",
      "src/model_utils.py",
      "src/convert_graspune_to_hf.py",
      "src/eval_mbpp.py",
      "src/gradient_flow_analysis.py"
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

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_017CPzrDXJiJRUBSqo7AfJdj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_overlap.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "2cbbdba6-57a7-4a7f-9726-2f4bebf77d0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UgVZMUayi37Azsncyt2JA1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 518,
      "cache_read_input_tokens": 26955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 518
      },
      "output_tokens": 64,
      "service_tier": "standard",
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

_source line 50 · 2026-05-19T21:23:18.210Z_

<details><summary>↩ Tool result · `toolu_017CPzrDXJiJRUBSqo7AfJdj`</summary>

```text
1	"""
2	CKA Overlap Computation for RASP.
3	
4	Computes intra-layer functional overlap F(h) for each attention head and MLP channel group
5	using linear CKA (Centered Kernel Alignment via HSIC).
6	
7	Input:  model + calibration data (GSM8K train subset)
8	Output: per-structure F(h) scores saved as dict in .pt file
9	        Keys: 'attn_overlap' (dict[layer_idx -> tensor[n_heads]]),
10	              'mlp_overlap'  (dict[layer_idx -> tensor[n_groups]])
11	"""
12	
13	import argparse
14	import logging
15	import math
16	import os
17	import random
18	
19	import numpy as np
20	import torch
21	from datasets import load_dataset
22	from transformers import AutoModelForCausalLM, AutoTokenizer
23	
24	logging.basicConfig(
25	    level=logging.INFO,
26	    format="%(asctime)s [%(levelname)s] %(message)s",
27	)
28	logger = logging.getLogger(__name__)
29	
30	
31	def set_seed(seed: int):
32	    random.seed(seed)
33	    np.random.seed(seed)
34	    torch.manual_seed(seed)
35	    torch.cuda.manual_seed_all(seed)
36	
37	
38	def linear_cka(X: torch.Tensor, Y: torch.Tensor) -> float:
39	    """Linear CKA between two activation matrices.
40	    X: [n, p], Y: [n, q]. Returns scalar similarity in [0, 1].
41	    """
42	    X = X - X.mean(0)
43	    Y = Y - Y.mean(0)
44	    hsic_xy = torch.norm(X.T @ Y, "fro") ** 2
45	    hsic_xx = torch.norm(X.T @ X, "fro") ** 2
46	    hsic_yy = torch.norm(Y.T @ Y, "fro") ** 2
47	    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()
48	
49	
50	def load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):
51	    """Load GSM8K train questions as calibration prompts."""
52	    ds = load_dataset("openai/gsm8k", "main", split="train")
53	    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))
54	
55	    encodings = []
56	    for example in ds:
57	        prompt = f"Question: {example['question']}\nAnswer: Let me think step by step.\n"
58	        ids = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
59	        encodings.append(ids)
60	    return encodings
61	
62	
63	def collect_head_activations(model, tokenizer, calibration_data, device):
64	    """Run calibration data through model and collect per-head activations for each layer.
65	
66	    Returns dict[layer_idx] -> tensor[n_samples, n_heads, pooled_dim]
67	    where pooled_dim collapses (seq_len, head_dim) via mean-pool over seq_len.
68	    """
69	    config = model.config
70	    n_layers = config.num_hidden_layers
71	    n_heads = config.num_attention_heads
72	    head_dim = config.hidden_size // n_heads
73	
74	    layer_activations = {i: [] for i in range(n_layers)}
75	    hooks = []
76	
77	    def make_hook(layer_idx):
78	        def hook_fn(module, input, output):
79	            # output of attention: (hidden_states, attn_weights, past_kv)
80	            # We hook into q_proj to get query states, then reshape per-head
81	            pass
82	        return hook_fn
83	
84	    # Hook into each attention layer's output (the hidden_states after o_proj)
85	    # We instead hook the q_proj to capture per-head representations
86	    q_proj_outputs = {i: [] for i in range(n_layers)}
87	
88	    def make_q_hook(layer_idx):
89	        def hook_fn(module, input, output):
90	            # output shape: [batch, seq_len, n_heads * head_dim]
91	            q_proj_outputs[layer_idx].append(output.detach())
92	        return hook_fn
93	
94	    for i in range(n_layers):
95	        layer = model.model.layers[i]
96	        h = layer.self_attn.q_proj.register_forward_hook(make_q_hook(i))
97	        hooks.append(h)
98	
99	    model.eval()
100	    with torch.no_grad():
101	        for batch_idx, enc in enumerate(calibration_data):
102	            input_ids = enc["input_ids"].to(device)
103	            attention_mask = enc["attention_mask"].to(device)
104	            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)
105	            if (batch_idx + 1) % 50 == 0:
106	                logger.info(f"  Processed {batch_idx + 1}/{len(calibration_data)} samples")
107	
108	    for h in hooks:
109	        h.remove()
110	
111	    # Reshape and mean-pool: [batch, seq, n_heads*head_dim] -> per-head [batch, head_dim]
112	    for layer_idx in range(n_layers):
113	        tensors = q_proj_outputs[layer_idx]  # list of [1, seq, n_heads*head_dim]
114	        per_head_list = []
115	        for t in tensors:
116	            t = t.squeeze(0)  # [seq, n_heads*head_dim]
117	            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]
118	            t = t.mean(dim=0)  # [n_heads, head_dim] — mean pool over seq
119	            per_head_list.append(t)
120	        layer_activations[layer_idx] = torch.stack(per_head_list, dim=0)  # [n_samples, n_heads, head_dim]
121	        q_proj_outputs[layer_idx] = None  # free memory
122	
123	    return layer_activations
124	
125	
126	def collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups: int = 28):
127	    """Collect MLP intermediate activations grouped into channel groups.
128	
129	    Returns dict[layer_idx] -> tensor[n_samples, n_groups, group_dim]
130	    """
131	    config = model.config
132	    n_layers = config.num_hidden_layers
133	    intermediate_size = config.intermediate_size
134	    group_size = intermediate_size // n_groups
135	
136	    gate_outputs = {i: [] for i in range(n_layers)}
137	    hooks = []
138	
139	    def make_gate_hook(layer_idx):
140	        def hook_fn(module, input, output):
141	            gate_outputs[layer_idx].append(output.detach())
142	        return hook_fn
143	
144	    for i in range(n_layers):
145	        layer = model.model.layers[i]
146	        h = layer.mlp.gate_proj.register_forward_hook(make_gate_hook(i))
147	        hooks.append(h)
148	
149	    model.eval()
150	    with torch.no_grad():
151	        for enc in calibration_data:
152	            input_ids = enc["input_ids"].to(device)
153	            attention_mask = enc["attention_mask"].to(device)
154	            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)
155	
156	    for h in hooks:
157	        h.remove()
158	
159	    layer_activations = {}
160	    for layer_idx in range(n_layers):
161	        tensors = gate_outputs[layer_idx]
162	        per_group_list = []
163	        for t in tensors:
164	            t = t.squeeze(0)  # [seq, intermediate_size]
165	            t = t.mean(dim=0)  # [intermediate_size] — mean pool over seq
166	            # Truncate to exact multiple of group_size
167	            usable = n_groups * group_size
168	            t = t[:usable].view(n_groups, group_size)  # [n_groups, group_size]
169	            per_group_list.append(t)
170	        layer_activations[layer_idx] = torch.stack(per_group_list, dim=0)  # [n_samples, n_groups, group_size]
171	        gate_outputs[layer_idx] = None
172	
173	    return layer_activations
174	
175	
176	def compute_overlap(activations_dict: dict, structure_name: str) -> tuple:
177	    """Compute F(h) = mean CKA similarity and pairwise CKA matrix per layer.
178	
179	    activations_dict: dict[layer_idx] -> tensor[n_samples, n_structures, dim]
180	    Returns: (overlap_scores, cka_matrices)
181	        overlap_scores: dict[layer_idx] -> tensor[n_structures] of overlap F(h) in [0, 1]
182	        cka_matrices: dict[layer_idx] -> tensor[n_structures, n_structures] pairwise CKA
183	    """
184	    overlap_scores = {}
185	    cka_matrices = {}
186	    for layer_idx, acts in activations_dict.items():
187	        n_samples, n_structs, dim = acts.shape
188	        matrix = torch.zeros(n_structs, n_structs)
189	        for i in range(n_structs):
190	            matrix[i, i] = 1.0
191	            for j in range(i + 1, n_structs):
192	                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())
193	                matrix[i, j] = val
194	                matrix[j, i] = val
195	        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)
196	        overlap_scores[layer_idx] = scores
197	        cka_matrices[layer_idx] = matrix
198	        logger.info(
199	            f"  Layer {layer_idx} {structure_name}: F(h) range [{scores.min():.4f}, {scores.max():.4f}], "
200	            f"mean={scores.mean():.4f}"
201	        )
202	    return overlap_scores, cka_matrices
203	
204	
205	def main():
206	    parser = argparse.ArgumentParser(description="Compute CKA-based functional overlap scores for RASP")
207	    parser.add_argument("--model_path", type=str, required=True, help="Path to pretrained model")
208	    parser.add_argument("--output_path", type=str, required=True, help="Output .pt file for overlap scores")
209	    parser.add_argument("--n_samples", type=int, default=512, help="Number of calibration samples")
210	    parser.add_argument("--max_length", type=int, default=512, help="Max token length for calibration inputs")
211	    parser.add_argument("--mlp_groups", type=int, default=28, help="Number of MLP channel groups per layer")
212	    parser.add_argument("--seed", type=int, default=42, help="Random seed")
213	    parser.add_argument("--dtype", type=str, default="bfloat16", choices=["float16", "bfloat16", "float32"])
214	    args = parser.parse_args()
215	
216	    set_seed(args.seed)
217	    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
218	    dtype_map = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}
219	    torch_dtype = dtype_map[args.dtype]
220	
221	    logger.info(f"Loading model from {args.model_path}")
222	    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
223	    model = AutoModelForCausalLM.from_pretrained(
224	        args.model_path,
225	        torch_dtype=torch_dtype,
226	        device_map=device,
227	        trust_remote_code=True,
228	    )
229	
230	    logger.info(f"Loading {args.n_samples} calibration samples from GSM8K train")
231	    calibration_data = load_calibration_data(tokenizer, args.n_samples, args.max_length, args.seed)
232	
233	    logger.info("Collecting attention head activations...")
234	    head_acts = collect_head_activations(model, tokenizer, calibration_data, device)
235	
236	    logger.info("Computing attention head overlap F(h)...")
237	    attn_overlap, attn_cka_matrix = compute_overlap(head_acts, "attn_heads")
238	    del head_acts
239	    torch.cuda.empty_cache()
240	
241	    logger.info("Collecting MLP activations...")
242	    mlp_acts = collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups=args.mlp_groups)
243	
244	    logger.info("Computing MLP group overlap F(h)...")
245	    mlp_overlap, mlp_cka_matrix = compute_overlap(mlp_acts, "mlp_groups")
246	    del mlp_acts
247	    torch.cuda.empty_cache()
248	
249	    os.makedirs(os.path.dirname(args.output_path) or ".", exist_ok=True)
250	    result = {
251	        "attn_overlap": attn_overlap,
252	        "mlp_overlap": mlp_overlap,
253	        "attn_cka_matrix": attn_cka_matrix,
254	        "mlp_cka_matrix": mlp_cka_matrix,
255	    }
256	    torch.save(result, args.output_path)
257	    logger.info(f"Saved CKA overlap scores to {args.output_path}")
258	
259	
260	if __name__ == "__main__":
261	    main()
262	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "88175135-2a72-46a4-8fcb-507bb849e5f9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_overlap.py",
      "content": "\"\"\"\nCKA Overlap Computation for RASP.\n\nComputes intra-layer functional overlap F(h) for each attention head and MLP channel group\nusing linear CKA (Centered Kernel Alignment via HSIC).\n\nInput:  model + calibration data (GSM8K train subset)\nOutput: per-structure F(h) scores saved as dict in .pt file\n        Keys: 'attn_overlap' (dict[layer_idx -> tensor[n_heads]]),\n              'mlp_overlap'  (dict[layer_idx -> tensor[n_groups]])\n\"\"\"\n\nimport argparse\nimport logging\nimport math\nimport os\nimport random\n\nimport numpy as np\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n)\nlogger = logging.getLogger(__name__)\n\n\ndef set_seed(seed: int):\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n\n\ndef linear_cka(X: torch.Tensor, Y: torch.Tensor) -> float:\n    \"\"\"Linear CKA between two activation matrices.\n    X: [n, p], Y: [n, q]. Returns scalar similarity in [0, 1].\n    \"\"\"\n    X = X - X.mean(0)\n    Y = Y - Y.mean(0)\n    hsic_xy = torch.norm(X.T @ Y, \"fro\") ** 2\n    hsic_xx = torch.norm(X.T @ X, \"fro\") ** 2\n    hsic_yy = torch.norm(Y.T @ Y, \"fro\") ** 2\n    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()\n\n\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\n    \"\"\"Load GSM8K train questions as calibration prompts.\"\"\"\n    ds = load_dataset(\"openai/gsm8k\", \"main\", split=\"train\")\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\n\n    encodings = []\n    for example in ds:\n        prompt = f\"Question: {example['question']}\\nAnswer: Let me think step by step.\\n\"\n        ids = tokenizer(prompt, return_tensors=\"pt\", truncation=True, max_length=max_length)\n        encodings.append(ids)\n    return encodings\n\n\ndef collect_head_activations(model, tokenizer, calibration_data, device):\n    \"\"\"Run calibration data through model and collect per-head activations for each layer.\n\n    Returns dict[layer_idx] -> tensor[n_samples, n_heads, pooled_dim]\n    where pooled_dim collapses (seq_len, head_dim) via mean-pool over seq_len.\n    \"\"\"\n    config = model.config\n    n_layers = config.num_hidden_layers\n    n_heads = config.num_attention_heads\n    head_dim = config.hidden_size // n_heads\n\n    layer_activations = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_hook(layer_idx):\n        def hook_fn(module, input, output):\n            # output of attention: (hidden_states, attn_weights, past_kv)\n            # We hook into q_proj to get query states, then reshape per-head\n            pass\n        return hook_fn\n\n    # Hook into each attention layer's output (the hidden_states after o_proj)\n    # We instead hook the q_proj to capture per-head representations\n    q_proj_outputs = {i: [] for i in range(n_layers)}\n\n    def make_q_hook(layer_idx):\n        def hook_fn(module, input, output):\n            # output shape: [batch, seq_len, n_heads * head_dim]\n            q_proj_outputs[layer_idx].append(output.detach())\n        return hook_fn\n\n    for i in range(n_layers):\n        layer = model.model.layers[i]\n        h = layer.self_attn.q_proj.register_forward_hook(make_q_hook(i))\n        hooks.append(h)\n\n    model.eval()\n    with torch.no_grad():\n        for batch_idx, enc in enumerate(calibration_data):\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n            if (batch_idx + 1) % 50 == 0:\n                logger.info(f\"  Processed {batch_idx + 1}/{len(calibration_data)} samples\")\n\n    for h in hooks:\n        h.remove()\n\n    # Reshape and mean-pool: [batch, seq, n_heads*head_dim] -> per-head [batch, head_dim]\n    for layer_idx in range(n_layers):\n        tensors = q_proj_outputs[layer_idx]  # list of [1, seq, n_heads*head_dim]\n        per_head_list = []\n        for t in tensors:\n            t = t.squeeze(0)  # [seq, n_heads*head_dim]\n            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]\n            t = t.mean(dim=0)  # [n_heads, head_dim] — mean pool over seq\n            per_head_list.append(t)\n        layer_activations[layer_idx] = torch.stack(per_head_list, dim=0)  # [n_samples, n_heads, head_dim]\n        q_proj_outputs[layer_idx] = None  # free memory\n\n    return layer_activations\n\n\ndef collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups: int = 28):\n    \"\"\"Collect MLP intermediate activations grouped into channel groups.\n\n    Returns dict[layer_idx] -> tensor[n_samples, n_groups, group_dim]\n    \"\"\"\n    config = model.config\n    n_layers = config.num_hidden_layers\n    intermediate_size = config.intermediate_size\n    group_size = intermediate_size // n_groups\n\n    gate_outputs = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_gate_hook(layer_idx):\n        def hook_fn(module, input, output):\n            gate_outputs[layer_idx].append(output.detach())\n        return hook_fn\n\n    for i in range(n_layers):\n        layer = model.model.layers[i]\n        h = layer.mlp.gate_proj.register_forward_hook(make_gate_hook(i))\n        hooks.append(h)\n\n    model.eval()\n    with torch.no_grad():\n        for enc in calibration_data:\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n\n    for h in hooks:\n        h.remove()\n\n    layer_activations = {}\n    for layer_idx in range(n_layers):\n        tensors = gate_outputs[layer_idx]\n        per_group_list = []\n        for t in tensors:\n            t = t.squeeze(0)  # [seq, intermediate_size]\n            t = t.mean(dim=0)  # [intermediate_size] — mean pool over seq\n            # Truncate to exact multiple of group_size\n            usable = n_groups * group_size\n            t = t[:usable].view(n_groups, group_size)  # [n_groups, group_size]\n            per_group_list.append(t)\n        layer_activations[layer_idx] = torch.stack(per_group_list, dim=0)  # [n_samples, n_groups, group_size]\n        gate_outputs[layer_idx] = None\n\n    return layer_activations\n\n\ndef compute_overlap(activations_dict: dict, structure_name: str) -> tuple:\n    \"\"\"Compute F(h) = mean CKA similarity and pairwise CKA matrix per layer.\n\n    activations_dict: dict[layer_idx] -> tensor[n_samples, n_structures, dim]\n    Returns: (overlap_scores, cka_matrices)\n        overlap_scores: dict[layer_idx] -> tensor[n_structures] of overlap F(h) in [0, 1]\n        cka_matrices: dict[layer_idx] -> tensor[n_structures, n_structures] pairwise CKA\n    \"\"\"\n    overlap_scores = {}\n    cka_matrices = {}\n    for layer_idx, acts in activations_dict.items():\n        n_samples, n_structs, dim = acts.shape\n        matrix = torch.zeros(n_structs, n_structs)\n        for i in range(n_structs):\n            matrix[i, i] = 1.0\n            for j in range(i + 1, n_structs):\n                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())\n                matrix[i, j] = val\n                matrix[j, i] = val\n        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)\n        overlap_scores[layer_idx] = scores\n        cka_matrices[layer_idx] = matrix\n        logger.info(\n            f\"  Layer {layer_idx} {structure_name}: F(h) range [{scores.min():.4f}, {scores.max():.4f}], \"\n            f\"mean={scores.mean():.4f}\"\n        )\n    return overlap_scores, cka_matrices\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Compute CKA-based functional overlap scores for RASP\")\n    parser.add_argument(\"--model_path\", type=str, required=True, help=\"Path to pretrained model\")\n    parser.add_argument(\"--output_path\", type=str, required=True, help=\"Output .pt file for overlap scores\")\n    parser.add_argument(\"--n_samples\", type=int, default=512, help=\"Number of calibration samples\")\n    parser.add_argument(\"--max_length\", type=int, default=512, help=\"Max token length for calibration inputs\")\n    parser.add_argument(\"--mlp_groups\", type=int, default=28, help=\"Number of MLP channel groups per layer\")\n    parser.add_argument(\"--seed\", type=int, default=42, help=\"Random seed\")\n    parser.add_argument(\"--dtype\", type=str, default=\"bfloat16\", choices=[\"float16\", \"bfloat16\", \"float32\"])\n    args = parser.parse_args()\n\n    set_seed(args.seed)\n    device = torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n    dtype_map = {\"float16\": torch.float16, \"bfloat16\": torch.bfloat16, \"float32\": torch.float32}\n    torch_dtype = dtype_map[args.dtype]\n\n    logger.info(f\"Loading model from {args.model_path}\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\n    model = AutoModelForCausalLM.from_pretrained(\n        args.model_path,\n        torch_dtype=torch_dtype,\n        device_map=device,\n        trust_remote_code=True,\n    )\n\n    logger.info(f\"Loading {args.n_samples} calibration samples from GSM8K train\")\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, args.max_length, args.seed)\n\n    logger.info(\"Collecting attention head activations...\")\n    head_acts = collect_head_activations(model, tokenizer, calibration_data, device)\n\n    logger.info(\"Computing attention head overlap F(h)...\")\n    attn_overlap, attn_cka_matrix = compute_overlap(head_acts, \"attn_heads\")\n    del head_acts\n    torch.cuda.empty_cache()\n\n    logger.info(\"Collecting MLP activations...\")\n    mlp_acts = collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups=args.mlp_groups)\n\n    logger.info(\"Computing MLP group overlap F(h)...\")\n    mlp_overlap, mlp_cka_matrix = compute_overlap(mlp_acts, \"mlp_groups\")\n    del mlp_acts\n    torch.cuda.empty_cache()\n\n    os.makedirs(os.path.dirname(args.output_path) or \".\", exist_ok=True)\n    result = {\n        \"attn_overlap\": attn_overlap,\n        \"mlp_overlap\": mlp_overlap,\n        \"attn_cka_matrix\": attn_cka_matrix,\n        \"mlp_cka_matrix\": mlp_cka_matrix,\n    }\n    torch.save(result, args.output_path)\n    logger.info(f\"Saved CKA overlap scores to {args.output_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 262,
      "startLine": 1,
      "totalLines": 262
    }
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_014QS9UrcH5icEH7UtfTQyXn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/run_cka_reliability.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "5e74ee2c-db6d-4bc7-bec1-f478318208b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UgVZMUayi37Azsncyt2JA1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 518,
      "cache_read_input_tokens": 26955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 518
      },
      "output_tokens": 64,
      "service_tier": "standard",
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

_source line 52 · 2026-05-19T21:23:18.462Z_

<details><summary>↩ Tool result · `toolu_014QS9UrcH5icEH7UtfTQyXn`</summary>

```text
1	"""
2	CKA Reliability Analysis for RASP.
3	
4	Validates the stability of structural scoring by:
5	1-3. Cross-model CKA split-half reliability (original vs pruned, per GQA group)
6	4.   F(h) split-half reliability for attention heads (intra-layer overlap)
7	5.   F(h) split-half reliability for MLP groups (intra-layer overlap)
8	
9	Phases 1-3 address cross-model CKA stability.
10	Phases 4-5 address intra-layer F(h) stability (Claim 2 core metric).
11	"""
12	
13	import argparse
14	import json
15	import logging
16	import os
17	import random
18	import sys
19	
20	import numpy as np
21	import scipy.stats as stats
22	import torch
23	from datasets import load_dataset
24	from transformers import AutoModelForCausalLM, AutoTokenizer
25	
26	logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
27	logger = logging.getLogger(__name__)
28	
29	
30	def set_seed(seed):
31	    random.seed(seed)
32	    np.random.seed(seed)
33	    torch.manual_seed(seed)
34	    torch.cuda.manual_seed_all(seed)
35	
36	
37	def linear_cka(X, Y):
38	    """Linear CKA between two activation matrices. X: [n, p], Y: [n, q]."""
39	    X = X - X.mean(0)
40	    Y = Y - Y.mean(0)
41	    hsic_xy = torch.norm(X.T @ Y, "fro") ** 2
42	    hsic_xx = torch.norm(X.T @ X, "fro") ** 2
43	    hsic_yy = torch.norm(Y.T @ Y, "fro") ** 2
44	    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()
45	
46	
47	def load_calibration_data(tokenizer, n_samples, max_length=512, seed=42):
48	    ds = load_dataset("openai/gsm8k", "main", split="train")
49	    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))
50	    encodings = []
51	    for example in ds:
52	        prompt = f"Question: {example['question']}\nAnswer: Let me think step by step.\n"
53	        ids = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
54	        encodings.append(ids)
55	    return encodings
56	
57	
58	def collect_qproj_activations(model, calibration_data, device):
59	    """Collect per-head q_proj activations, mean-pooled over seq length.
60	    Returns dict[layer_idx] -> tensor[n_samples, n_heads_in_layer, head_dim] on CPU float32.
61	    """
62	    n_layers = model.config.num_hidden_layers
63	    head_dim = model.config.hidden_size // model.config.num_attention_heads
64	
65	    q_outputs = {i: [] for i in range(n_layers)}
66	    hooks = []
67	
68	    def make_hook(layer_idx):
69	        def fn(module, inp, out):
70	            q_outputs[layer_idx].append(out.detach().cpu())
71	        return fn
72	
73	    for i in range(n_layers):
74	        h = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_hook(i))
75	        hooks.append(h)
76	
77	    model.eval()
78	    with torch.no_grad():
79	        for idx, enc in enumerate(calibration_data):
80	            input_ids = enc["input_ids"].to(device)
81	            attention_mask = enc["attention_mask"].to(device)
82	            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)
83	            if (idx + 1) % 200 == 0:
84	                logger.info(f"  Forward pass {idx + 1}/{len(calibration_data)}")
85	
86	    for h in hooks:
87	        h.remove()
88	
89	    activations = {}
90	    for layer_idx in range(n_layers):
91	        out_dim = q_outputs[layer_idx][0].squeeze(0).shape[-1]
92	        n_heads = out_dim // head_dim
93	        per_head = []
94	        for t in q_outputs[layer_idx]:
95	            t = t.squeeze(0)  # [seq, n_heads * head_dim]
96	            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]
97	            t = t.mean(dim=0)  # [n_heads, head_dim]
98	            per_head.append(t)
99	        activations[layer_idx] = torch.stack(per_head, dim=0).float()
100	        q_outputs[layer_idx] = None
101	
102	    return activations
103	
104	
105	def collect_mlp_activations(model, calibration_data, device, n_groups=28):
106	    """Collect MLP gate_proj activations grouped into channel groups.
107	    Returns dict[layer_idx] -> tensor[n_samples, n_groups, group_dim] on CPU float32.
108	    """
109	    n_layers = model.config.num_hidden_layers
110	    intermediate_size = model.config.intermediate_size
111	    group_size = intermediate_size // n_groups
112	
113	    gate_outputs = {i: [] for i in range(n_layers)}
114	    hooks = []
115	
116	    def make_hook(layer_idx):
117	        def fn(module, inp, out):
118	            gate_outputs[layer_idx].append(out.detach().cpu())
119	        return fn
120	
121	    for i in range(n_layers):
122	        h = model.model.layers[i].mlp.gate_proj.register_forward_hook(make_hook(i))
123	        hooks.append(h)
124	
125	    model.eval()
126	    with torch.no_grad():
127	        for idx, enc in enumerate(calibration_data):
128	            input_ids = enc["input_ids"].to(device)
129	            attention_mask = enc["attention_mask"].to(device)
130	            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)
131	            if (idx + 1) % 200 == 0:
132	                logger.info(f"  Forward pass {idx + 1}/{len(calibration_data)}")
133	
134	    for h in hooks:
135	        h.remove()
136	
137	    activations = {}
138	    for layer_idx in range(n_layers):
139	        per_group = []
140	        for t in gate_outputs[layer_idx]:
141	            t = t.squeeze(0)  # [seq, intermediate_size]
142	            t = t.mean(dim=0)  # [intermediate_size]
143	            usable = n_groups * group_size
144	            t = t[:usable].view(n_groups, group_size)
145	            per_group.append(t)
146	        activations[layer_idx] = torch.stack(per_group, dim=0).float()
147	        gate_outputs[layer_idx] = None
148	
149	    return activations
150	
151	
152	def load_pruned_model_with_meta(base_model_path, pruned_model_path, torch_dtype, device):
153	    """Load structurally pruned model via base model reconstruction + saved weights."""
154	    meta_path = os.path.join(pruned_model_path, "pruning_metadata.pt")
155	    pruning_meta = torch.load(meta_path, map_location="cpu", weights_only=True)
156	
157	    src_dir = os.path.dirname(os.path.abspath(__file__))
158	    if src_dir not in sys.path:
159	        sys.path.insert(0, src_dir)
160	    from prune import prune_attention_heads, prune_mlp_channels
161	
162	    logging.getLogger("prune").setLevel(logging.WARNING)
163	    model = AutoModelForCausalLM.from_pretrained(
164	        base_model_path, torch_dtype=torch_dtype, device_map="cpu", trust_remote_code=True
165	    )
166	    prune_attention_heads(model, pruning_meta["attn_keep_masks"])
167	    prune_mlp_channels(model, pruning_meta["mlp_keep_masks"])
168	
169	    safetensor_files = sorted(
170	        [f for f in os.listdir(pruned_model_path) if f.endswith(".safetensors")]
171	    )
172	    if safetensor_files:
173	        from safetensors.torch import load_file
174	        state_dict = {}
175	        for f in safetensor_files:
176	            state_dict.update(load_file(os.path.join(pruned_model_path, f)))
177	    else:
178	        state_dict = torch.load(
179	            os.path.join(pruned_model_path, "pytorch_model.bin"),
180	            map_location="cpu", weights_only=True,
181	        )
182	    model.load_state_dict(state_dict)
183	    model.to(device)
184	    return model, pruning_meta
185	
186	
187	def compute_group_cka(orig_acts, pruned_acts, keep_masks, n_heads_orig, n_kv_heads,
188	                      sample_indices=None):
189	    """Compute per-GQA-group CKA between original and pruned representations.
190	
191	    For each KV group, concatenates retained Q head activations from both models
192	    and computes linear CKA. Original uses all Q heads in the group, pruned uses
193	    only retained Q heads (CKA handles different feature dimensions).
194	
195	    Returns dict[(layer, group)] -> float (or NaN if group fully pruned).
196	    """
197	    heads_per_kv = n_heads_orig // n_kv_heads
198	    n_layers = len(orig_acts)
199	    scores = {}
200	
201	    for layer_idx in range(n_layers):
202	        orig_layer = orig_acts[layer_idx]   # [N, n_heads_orig, head_dim]
203	        pruned_layer = pruned_acts[layer_idx]  # [N, n_retained, head_dim]
204	        retained = keep_masks[layer_idx]
205	
206	        if sample_indices is not None:
207	            orig_layer = orig_layer[sample_indices]
208	            pruned_layer = pruned_layer[sample_indices]
209	
210	        for g in range(n_kv_heads):
211	            orig_head_range = list(range(g * heads_per_kv, (g + 1) * heads_per_kv))
212	            pruned_positions = [i for i, h in enumerate(retained) if h in orig_head_range]
213	
214	            if not pruned_positions:
215	                scores[(layer_idx, g)] = float("nan")
216	                continue
217	
218	            n = orig_layer.shape[0]
219	            orig_flat = orig_layer[:, orig_head_range, :].reshape(n, -1)
220	            pruned_flat = pruned_layer[:, pruned_positions, :].reshape(n, -1)
221	            scores[(layer_idx, g)] = linear_cka(orig_flat, pruned_flat)
222	
223	    return scores
224	
225	
226	def scores_to_aligned_arrays(scores_a, scores_b):
227	    """Extract aligned non-NaN value arrays from two score dicts."""
228	    common = sorted(set(scores_a.keys()) & set(scores_b.keys()))
229	    a_vals, b_vals = [], []
230	    for k in common:
231	        va, vb = scores_a[k], scores_b[k]
232	        if (isinstance(va, float) and va != va) or (isinstance(vb, float) and vb != vb):
233	            continue
234	        a_vals.append(va)
235	        b_vals.append(vb)
236	    return np.array(a_vals), np.array(b_vals)
237	
238	
239	def compute_fh_scores(acts_dict, sample_indices=None):
240	    """Compute intra-layer F(h) for each structure.
241	    acts_dict: dict[layer_idx] -> tensor[n_samples, n_structs, dim]
242	    Returns dict[layer_idx] -> tensor[n_structs] of F(h) values.
243	    """
244	    fh = {}
245	    for layer_idx, acts in acts_dict.items():
246	        if sample_indices is not None:
247	            acts = acts[sample_indices]
248	        n_samples, n_structs, dim = acts.shape
249	        matrix = torch.zeros(n_structs, n_structs)
250	        for i in range(n_structs):
251	            matrix[i, i] = 1.0
252	            for j in range(i + 1, n_structs):
253	                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())
254	                matrix[i, j] = val
255	                matrix[j, i] = val
256	        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)
257	        fh[layer_idx] = scores
258	    return fh
259	
260	
261	def compute_fh_reliability(acts_dict, n_splits, seed, structure_name):
262	    """Split-half reliability of F(h) rankings across all layers.
263	    Returns list of per-split result dicts with Spearman rho.
264	    """
265	    n_total = next(iter(acts_dict.values())).shape[0]
266	    split_results = []
267	    for i in range(n_splits):
268	        rng = np.random.RandomState(seed + i)
269	        perm = rng.permutation(n_total)
270	        half = n_total // 2
271	        idx_a = sorted(perm[:half].tolist())
272	        idx_b = sorted(perm[half:2 * half].tolist())
273	
274	        logger.info(f"  Split {i}: computing F(h) on half A ({len(idx_a)} samples)...")
275	        fh_a = compute_fh_scores(acts_dict, idx_a)
276	        logger.info(f"  Split {i}: computing F(h) on half B ({len(idx_b)} samples)...")
277	        fh_b = compute_fh_scores(acts_dict, idx_b)
278	
279	        vals_a, vals_b = [], []
280	        for layer_idx in sorted(fh_a.keys()):
281	            vals_a.extend(fh_a[layer_idx].tolist())
282	            vals_b.extend(fh_b[layer_idx].tolist())
283	
284	        rho, p = stats.spearmanr(vals_a, vals_b)
285	        split_results.append({"split": i, "rho": float(rho), "p_value": float(p),
286	                              "n_structures": len(vals_a)})
287	        logger.info(f"  Split {i} {structure_name}: rho={rho:.4f}, p={p:.2e}, n={len(vals_a)}")
288	    return split_results
289	
290	
291	def main():
292	    parser = argparse.ArgumentParser(description="CKA Reliability Analysis for RASP scoring")
293	    parser.add_argument("--original_model", type=str, required=True)
294	    parser.add_argument("--pruned_model", type=str, default=None)
295	    parser.add_argument("--gpu_id", type=int, default=0)
296	    parser.add_argument("--num_samples", type=int, default=1024)
297	    parser.add_argument("--max_length", type=int, default=512)
298	    parser.add_argument("--n_splits", type=int, default=5)
299	    parser.add_argument("--output", type=str, required=True)
300	    parser.add_argument("--seed", type=int, default=42)
301	    parser.add_argument("--dtype", type=str, default="bfloat16",
302	                        choices=["float16", "bfloat16", "float32"])
303	    parser.add_argument("--mlp_groups", type=int, default=28,
304	                        help="Number of MLP channel groups per layer")
305	    parser.add_argument("--skip_cross_model", action="store_true",
306	                        help="Skip Phase 1-3 (cross-model CKA); only run F(h) reliability")
307	    args = parser.parse_args()
308	
309	    if not args.skip_cross_model and not args.pruned_model:
310	        parser.error("--pruned_model is required unless --skip_cross_model is set")
311	
312	    set_seed(args.seed)
313	    device = torch.device(f"cuda:{args.gpu_id}" if torch.cuda.is_available() else "cpu")
314	    torch_dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16,
315	                   "float32": torch.float32}[args.dtype]
316	
317	    logger.info("Loading tokenizer and calibration data...")
318	    tokenizer = AutoTokenizer.from_pretrained(args.original_model, trust_remote_code=True)
319	    calibration_data = load_calibration_data(tokenizer, args.num_samples, args.max_length,
320	                                             args.seed)
321	    n_total = len(calibration_data)
322	    logger.info(f"Loaded {n_total} calibration samples")
323	
324	    # --- Load original model and collect all activations ---
325	    logger.info("Loading original model...")
326	    orig_model = AutoModelForCausalLM.from_pretrained(
327	        args.original_model, torch_dtype=torch_dtype, device_map=device, trust_remote_code=True
328	    )
329	    config = orig_model.config
330	    n_heads_orig = config.num_attention_heads
331	    n_kv_heads = config.num_key_value_heads
332	    n_layers = config.num_hidden_layers
333	    heads_per_kv = n_heads_orig // n_kv_heads
334	    logger.info(f"Architecture: {n_layers}L x {n_heads_orig}Q x {n_kv_heads}KV "
335	                f"({heads_per_kv} Q/KV group, {n_layers * n_kv_heads} total groups)")
336	
337	    logger.info("Collecting original model q_proj activations...")
338	    orig_acts = collect_qproj_activations(orig_model, calibration_data, device)
339	
340	    logger.info("Collecting original model MLP gate_proj activations...")
341	    orig_mlp_acts = collect_mlp_activations(orig_model, calibration_data, device, args.mlp_groups)
342	
343	    del orig_model
344	    torch.cuda.empty_cache()
345	    logger.info("Original model freed. All activations cached on CPU.")
346	
347	    output = {
348	        "config": {
349	            "original_model": args.original_model,
350	            "num_samples": n_total,
351	            "n_layers": n_layers,
352	            "n_heads_original": n_heads_orig,
353	            "n_kv_heads": n_kv_heads,
354	            "heads_per_kv": heads_per_kv,
355	            "total_gqa_groups": n_layers * n_kv_heads,
356	            "mlp_groups": args.mlp_groups,
357	            "seed": args.seed,
358	        },
359	    }
360	
361	    # --- Phase 1-3: Cross-model CKA (optional) ---
362	    if not args.skip_cross_model:
363	        logger.info("Loading pruned model...")
364	        pruned_model, pruning_meta = load_pruned_model_with_meta(
365	            args.original_model, args.pruned_model, torch_dtype, device
366	        )
367	        keep_masks = pruning_meta["attn_keep_masks"]
368	        logger.info("Collecting pruned model activations...")
369	        pruned_acts = collect_qproj_activations(pruned_model, calibration_data, device)
370	        del pruned_model
371	        torch.cuda.empty_cache()
372	        logger.info("Pruned model freed.")
373	
374	        # Phase 1: Full CKA scores
375	        logger.info("=" * 50)
376	        logger.info("Phase 1: Full CKA scores (N=%d)...", n_total)
377	        full_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,
378	                                        n_heads_orig, n_kv_heads)
379	        valid_scores = {k: v for k, v in full_scores.items()
380	                        if not (isinstance(v, float) and v != v)}
381	        vals = np.array(list(valid_scores.values()))
382	        logger.info(f"Valid groups: {len(valid_scores)}/{n_layers * n_kv_heads}")
383	        logger.info(f"CKA: mean={vals.mean():.4f}, std={vals.std():.4f}, "
384	                    f"range=[{vals.min():.4f}, {vals.max():.4f}]")
385	
386	        # Phase 2: Split-half reliability (cross-model)
387	        logger.info("=" * 50)
388	        logger.info("Phase 2: Split-half reliability (%d splits)...", args.n_splits)
389	        cross_split_results = []
390	        for i in range(args.n_splits):
391	            rng = np.random.RandomState(args.seed + i)
392	            perm = rng.permutation(n_total)
393	            half = n_total // 2
394	            idx_a = sorted(perm[:half].tolist())
395	            idx_b = sorted(perm[half:2 * half].tolist())
396	
397	            scores_a = compute_group_cka(orig_acts, pruned_acts, keep_masks,
398	                                         n_heads_orig, n_kv_heads, idx_a)
399	            scores_b = compute_group_cka(orig_acts, pruned_acts, keep_masks,
400	                                         n_heads_orig, n_kv_heads, idx_b)
401	            arr_a, arr_b = scores_to_aligned_arrays(scores_a, scores_b)
402	            rho, p = stats.spearmanr(arr_a, arr_b)
403	            cross_split_results.append({"split": i, "rho": float(rho), "p_value": float(p),
404	                                        "n_groups": len(arr_a)})
405	            logger.info(f"  Split {i}: rho={rho:.4f}, p={p:.2e}")
406	
407	        cross_mean_rho = float(np.mean([r["rho"] for r in cross_split_results]))
408	        cross_std_rho = float(np.std([r["rho"] for r in cross_split_results]))
409	
410	        # Phase 3: Calibration size sensitivity
411	        logger.info("=" * 50)
412	        logger.info("Phase 3: Calibration size sensitivity...")
413	        size_results = []
414	        for n_sub in [128, 256, 512]:
415	            if n_sub >= n_total:
416	                continue
417	            rng = np.random.RandomState(args.seed)
418	            sub_idx = sorted(rng.permutation(n_total)[:n_sub].tolist())
419	
420	            sub_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,
421	                                           n_heads_orig, n_kv_heads, sub_idx)
422	            ref_vals, sub_vals = scores_to_aligned_arrays(full_scores, sub_scores)
423	            rho, p = stats.spearmanr(ref_vals, sub_vals)
424	            size_results.append({"n_samples": n_sub, "rho_vs_full": float(rho),
425	                                 "p_value": float(p)})
426	            logger.info(f"  N={n_sub}: rho={rho:.4f} vs N={n_total}")
427	
428	        del pruned_acts
429	        torch.cuda.empty_cache()
430	
431	        per_group = {}
432	        for (l, g), v in full_scores.items():
433	            key = f"layer{l}_group{g}"
434	            per_group[key] = None if (isinstance(v, float) and v != v) else float(v)
435	
436	        output["config"]["pruned_model"] = args.pruned_model
437	        output["config"]["valid_gqa_groups"] = len(valid_scores)
438	        output["per_group_cka_scores"] = per_group
439	        output["cka_summary"] = {
440	            "mean": float(vals.mean()),
441	            "std": float(vals.std()),
442	            "min": float(vals.min()),
443	            "max": float(vals.max()),
444	            "median": float(np.median(vals)),
445	        }
446	        output["split_half_reliability"] = {
447	            "per_split": cross_split_results,
448	            "mean_rho": cross_mean_rho,
449	            "std_rho": cross_std_rho,
450	            "pass": cross_mean_rho > 0.9,
451	        }
452	        output["size_sensitivity"] = {
453	            "reference_n": n_total,
454	            "per_size": size_results,
455	            "all_pass_0.9": all(s["rho_vs_full"] > 0.9 for s in size_results),
456	        }
457	
458	    # --- Phase 4: F(h) attention head split-half reliability ---
459	    logger.info("=" * 50)
460	    logger.info("Phase 4: F(h) attention head split-half reliability (%d splits)...",
461	                args.n_splits)
462	    attn_fh_results = compute_fh_reliability(orig_acts, args.n_splits, args.seed, "attn_heads")
463	    attn_mean_rho = float(np.mean([r["rho"] for r in attn_fh_results]))
464	    attn_std_rho = float(np.std([r["rho"] for r in attn_fh_results]))
465	    attn_pass = attn_mean_rho > 0.9
466	    logger.info(f"Attn F(h) reliability: mean_rho={attn_mean_rho:.4f} +/- {attn_std_rho:.4f} "
467	                f"{'PASS' if attn_pass else 'FAIL'}")
468	
469	    output["fh_attn_reliability"] = {
470	        "per_split": attn_fh_results,
471	        "mean_rho": attn_mean_rho,
472	        "std_rho": attn_std_rho,
473	        "pass": attn_pass,
474	    }
475	
476	    del orig_acts
477	    torch.cuda.empty_cache()
478	
479	    # --- Phase 5: F(h) MLP group split-half reliability ---
480	    logger.info("=" * 50)
481	    logger.info("Phase 5: F(h) MLP group split-half reliability (%d splits)...", args.n_splits)
482	    mlp_fh_results = compute_fh_reliability(orig_mlp_acts, args.n_splits, args.seed, "mlp_groups")
483	    mlp_mean_rho = float(np.mean([r["rho"] for r in mlp_fh_results]))
484	    mlp_std_rho = float(np.std([r["rho"] for r in mlp_fh_results]))
485	    mlp_pass = mlp_mean_rho > 0.9
486	    logger.info(f"MLP F(h) reliability: mean_rho={mlp_mean_rho:.4f} +/- {mlp_std_rho:.4f} "
487	                f"{'PASS' if mlp_pass else 'FAIL'}")
488	
489	    output["fh_mlp_reliability"] = {
490	        "per_split": mlp_fh_results,
491	        "mean_rho": mlp_mean_rho,
492	        "std_rho": mlp_std_rho,
493	        "pass": mlp_pass,
494	    }
495	
496	    del orig_mlp_acts
497	    torch.cuda.empty_cache()
498	
499	    # --- Save results ---
500	    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
501	    with open(args.output, "w") as f:
502	        json.dump(output, f, indent=2)
503	    logger.info(f"Results saved to {args.output}")
504	
505	    # --- Print summary ---
506	    print(f"\n{'=' * 60}")
507	    print("CKA Reliability Analysis")
508	    print(f"{'=' * 60}")
509	
510	    if not args.skip_cross_model:
511	        print(f"\nCross-model CKA (Phase 1-3):")
512	        print(f"  GQA groups: {len(valid_scores)}/{n_layers * n_kv_heads} valid")
513	        print(f"  CKA scores: {vals.mean():.4f} +/- {vals.std():.4f} "
514	              f"[{vals.min():.4f}, {vals.max():.4f}]")
515	        sh_pass = "PASS" if cross_mean_rho > 0.9 else "FAIL"
516	        print(f"  Split-half reliability ({args.n_splits} splits):")
517	        print(f"    rho = {cross_mean_rho:.4f} +/- {cross_std_rho:.4f}  {sh_pass} "
518	              f"(threshold: 0.9)")
519	        for r in cross_split_results:
520	            print(f"      Split {r['split']}: rho={r['rho']:.4f}")
521	        print(f"  Size sensitivity (vs N={n_total}):")
522	        for s in size_results:
523	            sv = "PASS" if s["rho_vs_full"] > 0.9 else "FAIL"
524	            print(f"    N={s['n_samples']:4d}: rho={s['rho_vs_full']:.4f}  {sv}")
525	
526	    print(f"\nF(h) Attention head reliability (Phase 4):")
527	    ah_label = "PASS" if attn_pass else "FAIL"
528	    print(f"  rho = {attn_mean_rho:.4f} +/- {attn_std_rho:.4f}  {ah_label} (threshold: 0.9)")
529	    for r in attn_fh_results:
530	        print(f"    Split {r['split']}: rho={r['rho']:.4f}")
531	
532	    print(f"\nF(h) MLP group reliability (Phase 5):")
533	    mh_label = "PASS" if mlp_pass else "FAIL"
534	    print(f"  rho = {mlp_mean_rho:.4f} +/- {mlp_std_rho:.4f}  {mh_label} (threshold: 0.9)")
535	    for r in mlp_fh_results:
536	        print(f"    Split {r['split']}: rho={r['rho']:.4f}")
537	
538	    print(f"{'=' * 60}")
539	
540	
541	if __name__ == "__main__":
542	    main()
543	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "f02a42a4-ed19-427e-b57e-d9997a13ab9a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/run_cka_reliability.py",
      "content": "\"\"\"\nCKA Reliability Analysis for RASP.\n\nValidates the stability of structural scoring by:\n1-3. Cross-model CKA split-half reliability (original vs pruned, per GQA group)\n4.   F(h) split-half reliability for attention heads (intra-layer overlap)\n5.   F(h) split-half reliability for MLP groups (intra-layer overlap)\n\nPhases 1-3 address cross-model CKA stability.\nPhases 4-5 address intra-layer F(h) stability (Claim 2 core metric).\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\nimport sys\n\nimport numpy as np\nimport scipy.stats as stats\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s [%(levelname)s] %(message)s\")\nlogger = logging.getLogger(__name__)\n\n\ndef set_seed(seed):\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n\n\ndef linear_cka(X, Y):\n    \"\"\"Linear CKA between two activation matrices. X: [n, p], Y: [n, q].\"\"\"\n    X = X - X.mean(0)\n    Y = Y - Y.mean(0)\n    hsic_xy = torch.norm(X.T @ Y, \"fro\") ** 2\n    hsic_xx = torch.norm(X.T @ X, \"fro\") ** 2\n    hsic_yy = torch.norm(Y.T @ Y, \"fro\") ** 2\n    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()\n\n\ndef load_calibration_data(tokenizer, n_samples, max_length=512, seed=42):\n    ds = load_dataset(\"openai/gsm8k\", \"main\", split=\"train\")\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\n    encodings = []\n    for example in ds:\n        prompt = f\"Question: {example['question']}\\nAnswer: Let me think step by step.\\n\"\n        ids = tokenizer(prompt, return_tensors=\"pt\", truncation=True, max_length=max_length)\n        encodings.append(ids)\n    return encodings\n\n\ndef collect_qproj_activations(model, calibration_data, device):\n    \"\"\"Collect per-head q_proj activations, mean-pooled over seq length.\n    Returns dict[layer_idx] -> tensor[n_samples, n_heads_in_layer, head_dim] on CPU float32.\n    \"\"\"\n    n_layers = model.config.num_hidden_layers\n    head_dim = model.config.hidden_size // model.config.num_attention_heads\n\n    q_outputs = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_hook(layer_idx):\n        def fn(module, inp, out):\n            q_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    for i in range(n_layers):\n        h = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_hook(i))\n        hooks.append(h)\n\n    model.eval()\n    with torch.no_grad():\n        for idx, enc in enumerate(calibration_data):\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n            if (idx + 1) % 200 == 0:\n                logger.info(f\"  Forward pass {idx + 1}/{len(calibration_data)}\")\n\n    for h in hooks:\n        h.remove()\n\n    activations = {}\n    for layer_idx in range(n_layers):\n        out_dim = q_outputs[layer_idx][0].squeeze(0).shape[-1]\n        n_heads = out_dim // head_dim\n        per_head = []\n        for t in q_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, n_heads * head_dim]\n            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]\n            t = t.mean(dim=0)  # [n_heads, head_dim]\n            per_head.append(t)\n        activations[layer_idx] = torch.stack(per_head, dim=0).float()\n        q_outputs[layer_idx] = None\n\n    return activations\n\n\ndef collect_mlp_activations(model, calibration_data, device, n_groups=28):\n    \"\"\"Collect MLP gate_proj activations grouped into channel groups.\n    Returns dict[layer_idx] -> tensor[n_samples, n_groups, group_dim] on CPU float32.\n    \"\"\"\n    n_layers = model.config.num_hidden_layers\n    intermediate_size = model.config.intermediate_size\n    group_size = intermediate_size // n_groups\n\n    gate_outputs = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_hook(layer_idx):\n        def fn(module, inp, out):\n            gate_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    for i in range(n_layers):\n        h = model.model.layers[i].mlp.gate_proj.register_forward_hook(make_hook(i))\n        hooks.append(h)\n\n    model.eval()\n    with torch.no_grad():\n        for idx, enc in enumerate(calibration_data):\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n            if (idx + 1) % 200 == 0:\n                logger.info(f\"  Forward pass {idx + 1}/{len(calibration_data)}\")\n\n    for h in hooks:\n        h.remove()\n\n    activations = {}\n    for layer_idx in range(n_layers):\n        per_group = []\n        for t in gate_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, intermediate_size]\n            t = t.mean(dim=0)  # [intermediate_size]\n            usable = n_groups * group_size\n            t = t[:usable].view(n_groups, group_size)\n            per_group.append(t)\n        activations[layer_idx] = torch.stack(per_group, dim=0).float()\n        gate_outputs[layer_idx] = None\n\n    return activations\n\n\ndef load_pruned_model_with_meta(base_model_path, pruned_model_path, torch_dtype, device):\n    \"\"\"Load structurally pruned model via base model reconstruction + saved weights.\"\"\"\n    meta_path = os.path.join(pruned_model_path, \"pruning_metadata.pt\")\n    pruning_meta = torch.load(meta_path, map_location=\"cpu\", weights_only=True)\n\n    src_dir = os.path.dirname(os.path.abspath(__file__))\n    if src_dir not in sys.path:\n        sys.path.insert(0, src_dir)\n    from prune import prune_attention_heads, prune_mlp_channels\n\n    logging.getLogger(\"prune\").setLevel(logging.WARNING)\n    model = AutoModelForCausalLM.from_pretrained(\n        base_model_path, torch_dtype=torch_dtype, device_map=\"cpu\", trust_remote_code=True\n    )\n    prune_attention_heads(model, pruning_meta[\"attn_keep_masks\"])\n    prune_mlp_channels(model, pruning_meta[\"mlp_keep_masks\"])\n\n    safetensor_files = sorted(\n        [f for f in os.listdir(pruned_model_path) if f.endswith(\".safetensors\")]\n    )\n    if safetensor_files:\n        from safetensors.torch import load_file\n        state_dict = {}\n        for f in safetensor_files:\n            state_dict.update(load_file(os.path.join(pruned_model_path, f)))\n    else:\n        state_dict = torch.load(\n            os.path.join(pruned_model_path, \"pytorch_model.bin\"),\n            map_location=\"cpu\", weights_only=True,\n        )\n    model.load_state_dict(state_dict)\n    model.to(device)\n    return model, pruning_meta\n\n\ndef compute_group_cka(orig_acts, pruned_acts, keep_masks, n_heads_orig, n_kv_heads,\n                      sample_indices=None):\n    \"\"\"Compute per-GQA-group CKA between original and pruned representations.\n\n    For each KV group, concatenates retained Q head activations from both models\n    and computes linear CKA. Original uses all Q heads in the group, pruned uses\n    only retained Q heads (CKA handles different feature dimensions).\n\n    Returns dict[(layer, group)] -> float (or NaN if group fully pruned).\n    \"\"\"\n    heads_per_kv = n_heads_orig // n_kv_heads\n    n_layers = len(orig_acts)\n    scores = {}\n\n    for layer_idx in range(n_layers):\n        orig_layer = orig_acts[layer_idx]   # [N, n_heads_orig, head_dim]\n        pruned_layer = pruned_acts[layer_idx]  # [N, n_retained, head_dim]\n        retained = keep_masks[layer_idx]\n\n        if sample_indices is not None:\n            orig_layer = orig_layer[sample_indices]\n            pruned_layer = pruned_layer[sample_indices]\n\n        for g in range(n_kv_heads):\n            orig_head_range = list(range(g * heads_per_kv, (g + 1) * heads_per_kv))\n            pruned_positions = [i for i, h in enumerate(retained) if h in orig_head_range]\n\n            if not pruned_positions:\n                scores[(layer_idx, g)] = float(\"nan\")\n                continue\n\n            n = orig_layer.shape[0]\n            orig_flat = orig_layer[:, orig_head_range, :].reshape(n, -1)\n            pruned_flat = pruned_layer[:, pruned_positions, :].reshape(n, -1)\n            scores[(layer_idx, g)] = linear_cka(orig_flat, pruned_flat)\n\n    return scores\n\n\ndef scores_to_aligned_arrays(scores_a, scores_b):\n    \"\"\"Extract aligned non-NaN value arrays from two score dicts.\"\"\"\n    common = sorted(set(scores_a.keys()) & set(scores_b.keys()))\n    a_vals, b_vals = [], []\n    for k in common:\n        va, vb = scores_a[k], scores_b[k]\n        if (isinstance(va, float) and va != va) or (isinstance(vb, float) and vb != vb):\n            continue\n        a_vals.append(va)\n        b_vals.append(vb)\n    return np.array(a_vals), np.array(b_vals)\n\n\ndef compute_fh_scores(acts_dict, sample_indices=None):\n    \"\"\"Compute intra-layer F(h) for each structure.\n    acts_dict: dict[layer_idx] -> tensor[n_samples, n_structs, dim]\n    Returns dict[layer_idx] -> tensor[n_structs] of F(h) values.\n    \"\"\"\n    fh = {}\n    for layer_idx, acts in acts_dict.items():\n        if sample_indices is not None:\n            acts = acts[sample_indices]\n        n_samples, n_structs, dim = acts.shape\n        matrix = torch.zeros(n_structs, n_structs)\n        for i in range(n_structs):\n            matrix[i, i] = 1.0\n            for j in range(i + 1, n_structs):\n                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())\n                matrix[i, j] = val\n                matrix[j, i] = val\n        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)\n        fh[layer_idx] = scores\n    return fh\n\n\ndef compute_fh_reliability(acts_dict, n_splits, seed, structure_name):\n    \"\"\"Split-half reliability of F(h) rankings across all layers.\n    Returns list of per-split result dicts with Spearman rho.\n    \"\"\"\n    n_total = next(iter(acts_dict.values())).shape[0]\n    split_results = []\n    for i in range(n_splits):\n        rng = np.random.RandomState(seed + i)\n        perm = rng.permutation(n_total)\n        half = n_total // 2\n        idx_a = sorted(perm[:half].tolist())\n        idx_b = sorted(perm[half:2 * half].tolist())\n\n        logger.info(f\"  Split {i}: computing F(h) on half A ({len(idx_a)} samples)...\")\n        fh_a = compute_fh_scores(acts_dict, idx_a)\n        logger.info(f\"  Split {i}: computing F(h) on half B ({len(idx_b)} samples)...\")\n        fh_b = compute_fh_scores(acts_dict, idx_b)\n\n        vals_a, vals_b = [], []\n        for layer_idx in sorted(fh_a.keys()):\n            vals_a.extend(fh_a[layer_idx].tolist())\n            vals_b.extend(fh_b[layer_idx].tolist())\n\n        rho, p = stats.spearmanr(vals_a, vals_b)\n        split_results.append({\"split\": i, \"rho\": float(rho), \"p_value\": float(p),\n                              \"n_structures\": len(vals_a)})\n        logger.info(f\"  Split {i} {structure_name}: rho={rho:.4f}, p={p:.2e}, n={len(vals_a)}\")\n    return split_results\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"CKA Reliability Analysis for RASP scoring\")\n    parser.add_argument(\"--original_model\", type=str, required=True)\n    parser.add_argument(\"--pruned_model\", type=str, default=None)\n    parser.add_argument(\"--gpu_id\", type=int, default=0)\n    parser.add_argument(\"--num_samples\", type=int, default=1024)\n    parser.add_argument(\"--max_length\", type=int, default=512)\n    parser.add_argument(\"--n_splits\", type=int, default=5)\n    parser.add_argument(\"--output\", type=str, required=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--dtype\", type=str, default=\"bfloat16\",\n                        choices=[\"float16\", \"bfloat16\", \"float32\"])\n    parser.add_argument(\"--mlp_groups\", type=int, default=28,\n                        help=\"Number of MLP channel groups per layer\")\n    parser.add_argument(\"--skip_cross_model\", action=\"store_true\",\n                        help=\"Skip Phase 1-3 (cross-model CKA); only run F(h) reliability\")\n    args = parser.parse_args()\n\n    if not args.skip_cross_model and not args.pruned_model:\n        parser.error(\"--pruned_model is required unless --skip_cross_model is set\")\n\n    set_seed(args.seed)\n    device = torch.device(f\"cuda:{args.gpu_id}\" if torch.cuda.is_available() else \"cpu\")\n    torch_dtype = {\"float16\": torch.float16, \"bfloat16\": torch.bfloat16,\n                   \"float32\": torch.float32}[args.dtype]\n\n    logger.info(\"Loading tokenizer and calibration data...\")\n    tokenizer = AutoTokenizer.from_pretrained(args.original_model, trust_remote_code=True)\n    calibration_data = load_calibration_data(tokenizer, args.num_samples, args.max_length,\n                                             args.seed)\n    n_total = len(calibration_data)\n    logger.info(f\"Loaded {n_total} calibration samples\")\n\n    # --- Load original model and collect all activations ---\n    logger.info(\"Loading original model...\")\n    orig_model = AutoModelForCausalLM.from_pretrained(\n        args.original_model, torch_dtype=torch_dtype, device_map=device, trust_remote_code=True\n    )\n    config = orig_model.config\n    n_heads_orig = config.num_attention_heads\n    n_kv_heads = config.num_key_value_heads\n    n_layers = config.num_hidden_layers\n    heads_per_kv = n_heads_orig // n_kv_heads\n    logger.info(f\"Architecture: {n_layers}L x {n_heads_orig}Q x {n_kv_heads}KV \"\n                f\"({heads_per_kv} Q/KV group, {n_layers * n_kv_heads} total groups)\")\n\n    logger.info(\"Collecting original model q_proj activations...\")\n    orig_acts = collect_qproj_activations(orig_model, calibration_data, device)\n\n    logger.info(\"Collecting original model MLP gate_proj activations...\")\n    orig_mlp_acts = collect_mlp_activations(orig_model, calibration_data, device, args.mlp_groups)\n\n    del orig_model\n    torch.cuda.empty_cache()\n    logger.info(\"Original model freed. All activations cached on CPU.\")\n\n    output = {\n        \"config\": {\n            \"original_model\": args.original_model,\n            \"num_samples\": n_total,\n            \"n_layers\": n_layers,\n            \"n_heads_original\": n_heads_orig,\n            \"n_kv_heads\": n_kv_heads,\n            \"heads_per_kv\": heads_per_kv,\n            \"total_gqa_groups\": n_layers * n_kv_heads,\n            \"mlp_groups\": args.mlp_groups,\n            \"seed\": args.seed,\n        },\n    }\n\n    # --- Phase 1-3: Cross-model CKA (optional) ---\n    if not args.skip_cross_model:\n        logger.info(\"Loading pruned model...\")\n        pruned_model, pruning_meta = load_pruned_model_with_meta(\n            args.original_model, args.pruned_model, torch_dtype, device\n        )\n        keep_masks = pruning_meta[\"attn_keep_masks\"]\n        logger.info(\"Collecting pruned model activations...\")\n        pruned_acts = collect_qproj_activations(pruned_model, calibration_data, device)\n        del pruned_model\n        torch.cuda.empty_cache()\n        logger.info(\"Pruned model freed.\")\n\n        # Phase 1: Full CKA scores\n        logger.info(\"=\" * 50)\n        logger.info(\"Phase 1: Full CKA scores (N=%d)...\", n_total)\n        full_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                        n_heads_orig, n_kv_heads)\n        valid_scores = {k: v for k, v in full_scores.items()\n                        if not (isinstance(v, float) and v != v)}\n        vals = np.array(list(valid_scores.values()))\n        logger.info(f\"Valid groups: {len(valid_scores)}/{n_layers * n_kv_heads}\")\n        logger.info(f\"CKA: mean={vals.mean():.4f}, std={vals.std():.4f}, \"\n                    f\"range=[{vals.min():.4f}, {vals.max():.4f}]\")\n\n        # Phase 2: Split-half reliability (cross-model)\n        logger.info(\"=\" * 50)\n        logger.info(\"Phase 2: Split-half reliability (%d splits)...\", args.n_splits)\n        cross_split_results = []\n        for i in range(args.n_splits):\n            rng = np.random.RandomState(args.seed + i)\n            perm = rng.permutation(n_total)\n            half = n_total // 2\n            idx_a = sorted(perm[:half].tolist())\n            idx_b = sorted(perm[half:2 * half].tolist())\n\n            scores_a = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                         n_heads_orig, n_kv_heads, idx_a)\n            scores_b = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                         n_heads_orig, n_kv_heads, idx_b)\n            arr_a, arr_b = scores_to_aligned_arrays(scores_a, scores_b)\n            rho, p = stats.spearmanr(arr_a, arr_b)\n            cross_split_results.append({\"split\": i, \"rho\": float(rho), \"p_value\": float(p),\n                                        \"n_groups\": len(arr_a)})\n            logger.info(f\"  Split {i}: rho={rho:.4f}, p={p:.2e}\")\n\n        cross_mean_rho = float(np.mean([r[\"rho\"] for r in cross_split_results]))\n        cross_std_rho = float(np.std([r[\"rho\"] for r in cross_split_results]))\n\n        # Phase 3: Calibration size sensitivity\n        logger.info(\"=\" * 50)\n        logger.info(\"Phase 3: Calibration size sensitivity...\")\n        size_results = []\n        for n_sub in [128, 256, 512]:\n            if n_sub >= n_total:\n                continue\n            rng = np.random.RandomState(args.seed)\n            sub_idx = sorted(rng.permutation(n_total)[:n_sub].tolist())\n\n            sub_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                           n_heads_orig, n_kv_heads, sub_idx)\n            ref_vals, sub_vals = scores_to_aligned_arrays(full_scores, sub_scores)\n            rho, p = stats.spearmanr(ref_vals, sub_vals)\n            size_results.append({\"n_samples\": n_sub, \"rho_vs_full\": float(rho),\n                                 \"p_value\": float(p)})\n            logger.info(f\"  N={n_sub}: rho={rho:.4f} vs N={n_total}\")\n\n        del pruned_acts\n        torch.cuda.empty_cache()\n\n        per_group = {}\n        for (l, g), v in full_scores.items():\n            key = f\"layer{l}_group{g}\"\n            per_group[key] = None if (isinstance(v, float) and v != v) else float(v)\n\n        output[\"config\"][\"pruned_model\"] = args.pruned_model\n        output[\"config\"][\"valid_gqa_groups\"] = len(valid_scores)\n        output[\"per_group_cka_scores\"] = per_group\n        output[\"cka_summary\"] = {\n            \"mean\": float(vals.mean()),\n            \"std\": float(vals.std()),\n            \"min\": float(vals.min()),\n            \"max\": float(vals.max()),\n            \"median\": float(np.median(vals)),\n        }\n        output[\"split_half_reliability\"] = {\n            \"per_split\": cross_split_results,\n            \"mean_rho\": cross_mean_rho,\n            \"std_rho\": cross_std_rho,\n            \"pass\": cross_mean_rho > 0.9,\n        }\n        output[\"size_sensitivity\"] = {\n            \"reference_n\": n_total,\n            \"per_size\": size_results,\n            \"all_pass_0.9\": all(s[\"rho_vs_full\"] > 0.9 for s in size_results),\n        }\n\n    # --- Phase 4: F(h) attention head split-half reliability ---\n    logger.info(\"=\" * 50)\n    logger.info(\"Phase 4: F(h) attention head split-half reliability (%d splits)...\",\n                args.n_splits)\n    attn_fh_results = compute_fh_reliability(orig_acts, args.n_splits, args.seed, \"attn_heads\")\n    attn_mean_rho = float(np.mean([r[\"rho\"] for r in attn_fh_results]))\n    attn_std_rho = float(np.std([r[\"rho\"] for r in attn_fh_results]))\n    attn_pass = attn_mean_rho > 0.9\n    logger.info(f\"Attn F(h) reliability: mean_rho={attn_mean_rho:.4f} +/- {attn_std_rho:.4f} \"\n                f\"{'PASS' if attn_pass else 'FAIL'}\")\n\n    output[\"fh_attn_reliability\"] = {\n        \"per_split\": attn_fh_results,\n        \"mean_rho\": attn_mean_rho,\n        \"std_rho\": attn_std_rho,\n        \"pass\": attn_pass,\n    }\n\n    del orig_acts\n    torch.cuda.empty_cache()\n\n    # --- Phase 5: F(h) MLP group split-half reliability ---\n    logger.info(\"=\" * 50)\n    logger.info(\"Phase 5: F(h) MLP group split-half reliability (%d splits)...\", args.n_splits)\n    mlp_fh_results = compute_fh_reliability(orig_mlp_acts, args.n_splits, args.seed, \"mlp_groups\")\n    mlp_mean_rho = float(np.mean([r[\"rho\"] for r in mlp_fh_results]))\n    mlp_std_rho = float(np.std([r[\"rho\"] for r in mlp_fh_results]))\n    mlp_pass = mlp_mean_rho > 0.9\n    logger.info(f\"MLP F(h) reliability: mean_rho={mlp_mean_rho:.4f} +/- {mlp_std_rho:.4f} \"\n                f\"{'PASS' if mlp_pass else 'FAIL'}\")\n\n    output[\"fh_mlp_reliability\"] = {\n        \"per_split\": mlp_fh_results,\n        \"mean_rho\": mlp_mean_rho,\n        \"std_rho\": mlp_std_rho,\n        \"pass\": mlp_pass,\n    }\n\n    del orig_mlp_acts\n    torch.cuda.empty_cache()\n\n    # --- Save results ---\n    os.makedirs(os.path.dirname(args.output) or \".\", exist_ok=True)\n    with open(args.output, \"w\") as f:\n        json.dump(output, f, indent=2)\n    logger.info(f\"Results saved to {args.output}\")\n\n    # --- Print summary ---\n    print(f\"\\n{'=' * 60}\")\n    print(\"CKA Reliability Analysis\")\n    print(f\"{'=' * 60}\")\n\n    if not args.skip_cross_model:\n        print(f\"\\nCross-model CKA (Phase 1-3):\")\n        print(f\"  GQA groups: {len(valid_scores)}/{n_layers * n_kv_heads} valid\")\n        print(f\"  CKA scores: {vals.mean():.4f} +/- {vals.std():.4f} \"\n              f\"[{vals.min():.4f}, {vals.max():.4f}]\")\n        sh_pass = \"PASS\" if cross_mean_rho > 0.9 else \"FAIL\"\n        print(f\"  Split-half reliability ({args.n_splits} splits):\")\n        print(f\"    rho = {cross_mean_rho:.4f} +/- {cross_std_rho:.4f}  {sh_pass} \"\n              f\"(threshold: 0.9)\")\n        for r in cross_split_results:\n            print(f\"      Split {r['split']}: rho={r['rho']:.4f}\")\n        print(f\"  Size sensitivity (vs N={n_total}):\")\n        for s in size_results:\n            sv = \"PASS\" if s[\"rho_vs_full\"] > 0.9 else \"FAIL\"\n            print(f\"    N={s['n_samples']:4d}: rho={s['rho_vs_full']:.4f}  {sv}\")\n\n    print(f\"\\nF(h) Attention head reliability (Phase 4):\")\n    ah_label = \"PASS\" if attn_pass else \"FAIL\"\n    print(f\"  rho = {attn_mean_rho:.4f} +/- {attn_std_rho:.4f}  {ah_label} (threshold: 0.9)\")\n    for r in attn_fh_results:\n        print(f\"    Split {r['split']}: rho={r['rho']:.4f}\")\n\n    print(f\"\\nF(h) MLP group reliability (Phase 5):\")\n    mh_label = \"PASS\" if mlp_pass else \"FAIL\"\n    print(f\"  rho = {mlp_mean_rho:.4f} +/- {mlp_std_rho:.4f}  {mh_label} (threshold: 0.9)\")\n    for r in mlp_fh_results:\n        print(f\"    Split {r['split']}: rho={r['rho']:.4f}\")\n\n    print(f\"{'=' * 60}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 543,
      "startLine": 1,
      "totalLines": 543
    }
  }
}
```

</details>

---

### Assistant

_source line 53_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the codebase. Let me also check the model path on the server to confirm.

Key findings:
1. `cka_overlap.py` has the core CKA computation: `linear_cka()`, `load_calibration_data()`, `collect_head_activations()`, `collect_mlp_activations()`, `compute_overlap()`
2. `run_cka_reliability.py` already has a similar structure with `compute_fh_scores()` that computes F(h) scores and `compute_fh_reliability()` for split-half reliability


3. The calibration setup uses GSM8K training data with 512 samples by default (seed 42), and the model is DeepSeek-R1-Distill-Qwen-7B with 28 layers, each containing 28 attention heads and 28 MLP groups.

I need to write a script that loads the dense model and GSM8K calibration data at 1024 samples, then subsamples from that single collection to evaluate across the 256, 512, and 1024 sample sizes.

For the analysis, I'll compute F(h) scores at each calibration size, calculate Spearman rank correlations between the size pairs, and report the top and bottom 10 structures for each, saving everything to JSON. I can reuse the existing helper functions like `linear_cka()`, `load_calibration_data()`, the activation collection functions from run_cka_reliability.py, and `compute_fh_scores()`.

The efficient approach is to load all 1024 calibration samples upfront, collect activations in a single forward pass, then subsample those activations for each calibration size to compute the F(h) scores and correlations.

I'll structure the script to import the existing `compute_fh_scores` function which already supports the `sample_indices` parameter, making it straightforward to evaluate different calibration sizes without redundant model passes.

Writing the analysis script... I need to decide between using the first N samples versus random subsampling. The existing code already handles this by shuffling with a fixed seed and taking the first N samples, which means the 256-sample set is a subset of 512, which is a subset of 1024—this naturally mirrors how calibration would work at different sizes. Since I'm collecting all 1024 activations upfront, I can just use indices to subsample for each size without redundant computation.

Now I'm thinking through the model path structure. The scripts expect models to live in `/root/autodl-tmp/recovery_aware_struct_prune/models/`, so I'll default to something like `/root/autodl-tmp/recovery_aware_struct_prune/models/DeepSeek-R1-Distill-Qwen-7B`.

Writing the script...

For the Spearman correlation analysis, I need to flatten the F(h) scores across all layers into a single vector for each calibration size and then compute pairwise correlations between them. For the top-10 and bottom-10 analysis, I need to extract structure labels like "layer_X_attn_head_Y" or "layer_X_mlp_group_Y" from the results.

The script also needs to be self-contained, so I'm adding the src directory to sys.path to import the existing modules, similar to how `run_cka_reliability.py` handles it.

Writing the script now... Setting up logging and defining helper functions... Setting up the argument parser with options for MLP groups, random seed, and data type, then loading the model and tokenizer from the specified path with the chosen precision settings.

Now I'm loading the calibration data and collecting activation patterns from both the attention heads and MLP layers across all 1024 samples, then cleaning up the model from memory.

Computing F(h) scores for each calibration subset size...

Now I'm flattening the attention and MLP scores into vectors and extracting the top and bottom structures for each calibration size. Computing pairwise correlations between model sizes using Spearman's rank correlation for attention weights, MLP values, and combined structures, then storing the correlation coefficients and p-values in the results dictionary.

Now I'm calculating summary statistics across all pairs—finding the minimum and mean correlation values, checking if all correlations exceed the 0.95 stability threshold, and preparing to save the complete results to a JSON file. Finishing the output formatting and then wrapping up the main function. I'm also thinking through the runtime—loading the model takes about 30 seconds, processing 1024 calibration samples another 10 seconds, and the forward pass roughly 5 seconds, so the whole analysis should complete in a reasonable timeframe. I should verify the imports are correct and make sure the per-size output displays the top and bottom 10 structures for each calibration size. I'm realizing there's a potential inefficiency with running two separate forward passes through the model—one for collecting q_proj activations and another for MLP activations. I should check if I can consolidate these into a single pass to cut the runtime roughly in half.

Looking back at the existing codebase structure, both `cka_overlap.py` and `run_cka_reliability.py` follow the same pattern of separate passes, so while it's not optimal, it's consistent with what's already there. For 1024 samples, the total time should still be manageable at around 10 minutes.

I need to verify the model path exists on the server—I'll use the default location from the constraints: `/root/autodl-tmp/recovery_aware_struct_prune/models/DeepSeek-R1-Distill-Qwen-7B`.

Writing the final script... I need to understand what `compute_fh_scores` does - it looks like it's building a matrix structure for computing some kind of similarity or correlation metric across the activations, iterating through pairs of structures to populate the matrix values. I'm satisfied with the function setup, so now I'll put together the final script. I should add some progress logging around the F(h) computations since we're running six of them across 28 layers each, even though I'm reusing the existing functions without modifying them.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "7468a452-666a-452a-95ff-fe8330be833a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKovrACnckDtYCRVWw31a8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13049,
      "cache_read_input_tokens": 27473,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13049
      },
      "output_tokens": 12,
      "service_tier": "standard",
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

_source line 54_

Now I have full understanding of the codebase. Key findings:
- `cka_overlap.py`: `linear_cka()`, `load_calibration_data()` (GSM8K train, default 512), `compute_overlap()`
- `run_cka_reliability.py`: `collect_qproj_activations()`, `collect_mlp_activations()`, `compute_fh_scores()` — all reusable
- 28 layers × (28 attn heads + 28 MLP groups) = 1568 prunable structures
- Calibration data shuffled with seed=42, first N selected — so 256 ⊂ 512 ⊂ 1024

Writing the stability analysis script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "a45eac97-c98f-4952-be72-83f316e15ccd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKovrACnckDtYCRVWw31a8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13049,
      "cache_read_input_tokens": 27473,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13049
      },
      "output_tokens": 12,
      "service_tier": "standard",
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

_source line 55_

<details open><summary>🔧 Tool call — Write · `toolu_0156VzHbf8kCvV73xWwNh6pq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_stability_analysis.py",
  "content": "\"\"\"\nCKA Scoring Stability Analysis.\n\nValidates that CKA-based pruning scores (F(h) overlap) are robust to calibration\nset size. Computes F(h) for all prunable structures using 256/512/1024 calibration\nsamples from GSM8K train, then measures pairwise Spearman rank correlation.\nrho > 0.95 indicates stable scoring.\n\nInput:  --model_path  Dense base model (DeepSeek-R1-Distill-Qwen-7B)\n        --device      GPU device (e.g. cuda:3)\nOutput: --output_path JSON with Spearman correlations, top/bottom-10 structures\nDeps:   cka_overlap.py (load_calibration_data, set_seed)\n        run_cka_reliability.py (collect_qproj_activations, collect_mlp_activations,\n                                compute_fh_scores)\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\n\nimport numpy as np\nimport scipy.stats as stats\nimport torch\n\nsrc_dir = os.path.dirname(os.path.abspath(__file__))\nif src_dir not in sys.path:\n    sys.path.insert(0, src_dir)\n\nfrom cka_overlap import load_calibration_data, set_seed\nfrom run_cka_reliability import (\n    collect_mlp_activations,\n    collect_qproj_activations,\n    compute_fh_scores,\n)\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s [%(levelname)s] %(message)s\")\nlogger = logging.getLogger(__name__)\n\nCALIB_SIZES = [256, 512, 1024]\n\n\ndef fh_to_flat_vector(fh_dict):\n    \"\"\"Flatten per-layer F(h) into a single vector, ordered by (layer_idx, struct_idx).\"\"\"\n    vals = []\n    labels = []\n    for layer_idx in sorted(fh_dict.keys()):\n        for i, s in enumerate(fh_dict[layer_idx].tolist()):\n            vals.append(s)\n            labels.append((layer_idx, i))\n    return np.array(vals), labels\n\n\ndef get_top_bottom(vals, labels, structure_type, k=10):\n    \"\"\"Return top-k highest and bottom-k lowest F(h) structures.\"\"\"\n    indices = np.argsort(vals)\n    bottom = []\n    for idx in indices[:k]:\n        layer, struct = labels[idx]\n        bottom.append({\"name\": f\"layer{layer}_{structure_type}{struct}\",\n                        \"score\": round(float(vals[idx]), 6)})\n    top = []\n    for idx in indices[-k:][::-1]:\n        layer, struct = labels[idx]\n        top.append({\"name\": f\"layer{layer}_{structure_type}{struct}\",\n                     \"score\": round(float(vals[idx]), 6)})\n    return top, bottom\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"CKA scoring stability across calibration sizes\")\n    parser.add_argument(\"--model_path\", type=str, required=True)\n    parser.add_argument(\"--output_path\", type=str, required=True)\n    parser.add_argument(\"--device\", type=str, default=\"cuda:0\")\n    parser.add_argument(\"--mlp_groups\", type=int, default=28)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--dtype\", type=str, default=\"bfloat16\",\n                        choices=[\"float16\", \"bfloat16\", \"float32\"])\n    args = parser.parse_args()\n\n    set_seed(args.seed)\n    device = torch.device(args.device)\n    torch_dtype = {\"float16\": torch.float16, \"bfloat16\": torch.bfloat16,\n                   \"float32\": torch.float32}[args.dtype]\n\n    logger.info(f\"Loading model from {args.model_path}\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\n    model = AutoModelForCausalLM.from_pretrained(\n        args.model_path, torch_dtype=torch_dtype, device_map=device, trust_remote_code=True,\n    )\n\n    max_size = max(CALIB_SIZES)\n    logger.info(f\"Loading {max_size} calibration samples from GSM8K train\")\n    calibration_data = load_calibration_data(tokenizer, max_size, seed=args.seed)\n    logger.info(f\"Loaded {len(calibration_data)} samples\")\n\n    # Collect activations once with max calibration size\n    logger.info(\"Collecting attention head activations...\")\n    attn_acts = collect_qproj_activations(model, calibration_data, device)\n\n    logger.info(\"Collecting MLP group activations...\")\n    mlp_acts = collect_mlp_activations(model, calibration_data, device, args.mlp_groups)\n\n    del model\n    torch.cuda.empty_cache()\n    logger.info(\"Model freed\")\n\n    # Compute F(h) for each calibration size by subsampling activations.\n    # load_calibration_data shuffles with fixed seed then takes first N,\n    # so first-256 subset matches what n_samples=256 would produce.\n    attn_fh_by_size = {}\n    mlp_fh_by_size = {}\n    for size in CALIB_SIZES:\n        indices = list(range(size)) if size < max_size else None\n        logger.info(f\"Computing F(h) with N={size} ...\")\n        attn_fh_by_size[size] = compute_fh_scores(attn_acts, indices)\n        mlp_fh_by_size[size] = compute_fh_scores(mlp_acts, indices)\n        logger.info(f\"  N={size} done\")\n\n    del attn_acts, mlp_acts\n    torch.cuda.empty_cache()\n\n    # Flatten scores per size, compute top/bottom structures\n    results = {\"calibration_sizes\": CALIB_SIZES, \"correlations\": {}, \"per_size\": {}}\n    attn_flat = {}\n    mlp_flat = {}\n\n    for size in CALIB_SIZES:\n        attn_vals, attn_labels = fh_to_flat_vector(attn_fh_by_size[size])\n        mlp_vals, mlp_labels = fh_to_flat_vector(mlp_fh_by_size[size])\n        attn_flat[size] = (attn_vals, attn_labels)\n        mlp_flat[size] = (mlp_vals, mlp_labels)\n\n        attn_top, attn_bot = get_top_bottom(attn_vals, attn_labels, \"attn_head\")\n        mlp_top, mlp_bot = get_top_bottom(mlp_vals, mlp_labels, \"mlp_group\")\n        results[\"per_size\"][str(size)] = {\n            \"n_attn_structures\": len(attn_vals),\n            \"n_mlp_structures\": len(mlp_vals),\n            \"attn\": {\"top10\": attn_top, \"bottom10\": attn_bot},\n            \"mlp\": {\"top10\": mlp_top, \"bottom10\": mlp_bot},\n        }\n\n    # Pairwise Spearman rank correlations\n    pairs = [(256, 512), (256, 1024), (512, 1024)]\n    for sa, sb in pairs:\n        pair_key = f\"{sa}_vs_{sb}\"\n        rho_attn, p_attn = stats.spearmanr(attn_flat[sa][0], attn_flat[sb][0])\n        rho_mlp, p_mlp = stats.spearmanr(mlp_flat[sa][0], mlp_flat[sb][0])\n\n        combined_a = np.concatenate([attn_flat[sa][0], mlp_flat[sa][0]])\n        combined_b = np.concatenate([attn_flat[sb][0], mlp_flat[sb][0]])\n        rho_all, p_all = stats.spearmanr(combined_a, combined_b)\n\n        results[\"correlations\"][pair_key] = {\n            \"attn\": {\"rho\": round(float(rho_attn), 6), \"p_value\": float(p_attn)},\n            \"mlp\": {\"rho\": round(float(rho_mlp), 6), \"p_value\": float(p_mlp)},\n            \"combined\": {\"rho\": round(float(rho_all), 6), \"p_value\": float(p_all)},\n        }\n        logger.info(f\"{pair_key}: attn rho={rho_attn:.4f}, mlp rho={rho_mlp:.4f}, \"\n                     f\"combined rho={rho_all:.4f}\")\n\n    all_combined_rhos = [results[\"correlations\"][f\"{a}_vs_{b}\"][\"combined\"][\"rho\"]\n                         for a, b in pairs]\n    results[\"summary\"] = {\n        \"min_combined_rho\": float(min(all_combined_rhos)),\n        \"mean_combined_rho\": float(np.mean(all_combined_rhos)),\n        \"stable\": all(r > 0.95 for r in all_combined_rhos),\n        \"threshold\": 0.95,\n    }\n\n    os.makedirs(os.path.dirname(args.output_path) or \".\", exist_ok=True)\n    with open(args.output_path, \"w\") as f:\n        json.dump(results, f, indent=2)\n    logger.info(f\"Saved to {args.output_path}\")\n\n    # Print summary\n    print(f\"\\n{'=' * 60}\")\n    print(\"CKA Scoring Stability Analysis\")\n    print(f\"{'=' * 60}\")\n    for pair_key, corr in results[\"correlations\"].items():\n        print(f\"\\n{pair_key}:\")\n        print(f\"  Attention heads:  rho={corr['attn']['rho']:.4f}  \"\n              f\"(p={corr['attn']['p_value']:.2e})\")\n        print(f\"  MLP groups:       rho={corr['mlp']['rho']:.4f}  \"\n              f\"(p={corr['mlp']['p_value']:.2e})\")\n        print(f\"  Combined:         rho={corr['combined']['rho']:.4f}  \"\n              f\"(p={corr['combined']['p_value']:.2e})\")\n\n    status = \"PASS\" if results[\"summary\"][\"stable\"] else \"FAIL\"\n    print(f\"\\nOverall: {status} (threshold rho>0.95, \"\n          f\"min rho={results['summary']['min_combined_rho']:.4f})\")\n    print(f\"{'=' * 60}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "72313d2b-a05e-4632-af91-e9d2b7529af7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKovrACnckDtYCRVWw31a8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13049,
      "cache_read_input_tokens": 27473,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13049
      },
      "output_tokens": 12,
      "service_tier": "standard",
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

_source line 56 · 2026-05-19T21:25:37.189Z_

<details><summary>↩ Tool result · `toolu_0156VzHbf8kCvV73xWwNh6pq`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_stability_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "54cfd65e-62a3-4760-ae6f-28f8416c25b8",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_stability_analysis.py",
    "content": "\"\"\"\nCKA Scoring Stability Analysis.\n\nValidates that CKA-based pruning scores (F(h) overlap) are robust to calibration\nset size. Computes F(h) for all prunable structures using 256/512/1024 calibration\nsamples from GSM8K train, then measures pairwise Spearman rank correlation.\nrho > 0.95 indicates stable scoring.\n\nInput:  --model_path  Dense base model (DeepSeek-R1-Distill-Qwen-7B)\n        --device      GPU device (e.g. cuda:3)\nOutput: --output_path JSON with Spearman correlations, top/bottom-10 structures\nDeps:   cka_overlap.py (load_calibration_data, set_seed)\n        run_cka_reliability.py (collect_qproj_activations, collect_mlp_activations,\n                                compute_fh_scores)\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\n\nimport numpy as np\nimport scipy.stats as stats\nimport torch\n\nsrc_dir = os.path.dirname(os.path.abspath(__file__))\nif src_dir not in sys.path:\n    sys.path.insert(0, src_dir)\n\nfrom cka_overlap import load_calibration_data, set_seed\nfrom run_cka_reliability import (\n    collect_mlp_activations,\n    collect_qproj_activations,\n    compute_fh_scores,\n)\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s [%(levelname)s] %(message)s\")\nlogger = logging.getLogger(__name__)\n\nCALIB_SIZES = [256, 512, 1024]\n\n\ndef fh_to_flat_vector(fh_dict):\n    \"\"\"Flatten per-layer F(h) into a single vector, ordered by (layer_idx, struct_idx).\"\"\"\n    vals = []\n    labels = []\n    for layer_idx in sorted(fh_dict.keys()):\n        for i, s in enumerate(fh_dict[layer_idx].tolist()):\n            vals.append(s)\n            labels.append((layer_idx, i))\n    return np.array(vals), labels\n\n\ndef get_top_bottom(vals, labels, structure_type, k=10):\n    \"\"\"Return top-k highest and bottom-k lowest F(h) structures.\"\"\"\n    indices = np.argsort(vals)\n    bottom = []\n    for idx in indices[:k]:\n        layer, struct = labels[idx]\n        bottom.append({\"name\": f\"layer{layer}_{structure_type}{struct}\",\n                        \"score\": round(float(vals[idx]), 6)})\n    top = []\n    for idx in indices[-k:][::-1]:\n        layer, struct = labels[idx]\n        top.append({\"name\": f\"layer{layer}_{structure_type}{struct}\",\n                     \"score\": round(float(vals[idx]), 6)})\n    return top, bottom\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"CKA scoring stability across calibration sizes\")\n    parser.add_argument(\"--model_path\", type=str, required=True)\n    parser.add_argument(\"--output_path\", type=str, required=True)\n    parser.add_argument(\"--device\", type=str, default=\"cuda:0\")\n    parser.add_argument(\"--mlp_groups\", type=int, default=28)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--dtype\", type=str, default=\"bfloat16\",\n                        choices=[\"float16\", \"bfloat16\", \"float32\"])\n    args = parser.parse_args()\n\n    set_seed(args.seed)\n    device = torch.device(args.device)\n    torch_dtype = {\"float16\": torch.float16, \"bfloat16\": torch.bfloat16,\n                   \"float32\": torch.float32}[args.dtype]\n\n    logger.info(f\"Loading model from {args.model_path}\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\n    model = AutoModelForCausalLM.from_pretrained(\n        args.model_path, torch_dtype=torch_dtype, device_map=device, trust_remote_code=True,\n    )\n\n    max_size = max(CALIB_SIZES)\n    logger.info(f\"Loading {max_size} calibration samples from GSM8K train\")\n    calibration_data = load_calibration_data(tokenizer, max_size, seed=args.seed)\n    logger.info(f\"Loaded {len(calibration_data)} samples\")\n\n    # Collect activations once with max calibration size\n    logger.info(\"Collecting attention head activations...\")\n    attn_acts = collect_qproj_activations(model, calibration_data, device)\n\n    logger.info(\"Collecting MLP group activations...\")\n    mlp_acts = collect_mlp_activations(model, calibration_data, device, args.mlp_groups)\n\n    del model\n    torch.cuda.empty_cache()\n    logger.info(\"Model freed\")\n\n    # Compute F(h) for each calibration size by subsampling activations.\n    # load_calibration_data shuffles with fixed seed then takes first N,\n    # so first-256 subset matches what n_samples=256 would produce.\n    attn_fh_by_size = {}\n    mlp_fh_by_size = {}\n    for size in CALIB_SIZES:\n        indices = list(range(size)) if size < max_size else None\n        logger.info(f\"Computing F(h) with N={size} ...\")\n        attn_fh_by_size[size] = compute_fh_scores(attn_acts, indices)\n        mlp_fh_by_size[size] = compute_fh_scores(mlp_acts, indices)\n        logger.info(f\"  N={size} done\")\n\n    del attn_acts, mlp_acts\n    torch.cuda.empty_cache()\n\n    # Flatten scores per size, compute top/bottom structures\n    results = {\"calibration_sizes\": CALIB_SIZES, \"correlations\": {}, \"per_size\": {}}\n    attn_flat = {}\n    mlp_flat = {}\n\n    for size in CALIB_SIZES:\n        attn_vals, attn_labels = fh_to_flat_vector(attn_fh_by_size[size])\n        mlp_vals, mlp_labels = fh_to_flat_vector(mlp_fh_by_size[size])\n        attn_flat[size] = (attn_vals, attn_labels)\n        mlp_flat[size] = (mlp_vals, mlp_labels)\n\n        attn_top, attn_bot = get_top_bottom(attn_vals, attn_labels, \"attn_head\")\n        mlp_top, mlp_bot = get_top_bottom(mlp_vals, mlp_labels, \"mlp_group\")\n        results[\"per_size\"][str(size)] = {\n            \"n_attn_structures\": len(attn_vals),\n            \"n_mlp_structures\": len(mlp_vals),\n            \"attn\": {\"top10\": attn_top, \"bottom10\": attn_bot},\n            \"mlp\": {\"top10\": mlp_top, \"bottom10\": mlp_bot},\n        }\n\n    # Pairwise Spearman rank correlations\n    pairs = [(256, 512), (256, 1024), (512, 1024)]\n    for sa, sb in pairs:\n        pair_key = f\"{sa}_vs_{sb}\"\n        rho_attn, p_attn = stats.spearmanr(attn_flat[sa][0], attn_flat[sb][0])\n        rho_mlp, p_mlp = stats.spearmanr(mlp_flat[sa][0], mlp_flat[sb][0])\n\n        combined_a = np.concatenate([attn_flat[sa][0], mlp_flat[sa][0]])\n        combined_b = np.concatenate([attn_flat[sb][0], mlp_flat[sb][0]])\n        rho_all, p_all = stats.spearmanr(combined_a, combined_b)\n\n        results[\"correlations\"][pair_key] = {\n            \"attn\": {\"rho\": round(float(rho_attn), 6), \"p_value\": float(p_attn)},\n            \"mlp\": {\"rho\": round(float(rho_mlp), 6), \"p_value\": float(p_mlp)},\n            \"combined\": {\"rho\": round(float(rho_all), 6), \"p_value\": float(p_all)},\n        }\n        logger.info(f\"{pair_key}: attn rho={rho_attn:.4f}, mlp rho={rho_mlp:.4f}, \"\n                     f\"combined rho={rho_all:.4f}\")\n\n    all_combined_rhos = [results[\"correlations\"][f\"{a}_vs_{b}\"][\"combined\"][\"rho\"]\n                         for a, b in pairs]\n    results[\"summary\"] = {\n        \"min_combined_rho\": float(min(all_combined_rhos)),\n        \"mean_combined_rho\": float(np.mean(all_combined_rhos)),\n        \"stable\": all(r > 0.95 for r in all_combined_rhos),\n        \"threshold\": 0.95,\n    }\n\n    os.makedirs(os.path.dirname(args.output_path) or \".\", exist_ok=True)\n    with open(args.output_path, \"w\") as f:\n        json.dump(results, f, indent=2)\n    logger.info(f\"Saved to {args.output_path}\")\n\n    # Print summary\n    print(f\"\\n{'=' * 60}\")\n    print(\"CKA Scoring Stability Analysis\")\n    print(f\"{'=' * 60}\")\n    for pair_key, corr in results[\"correlations\"].items():\n        print(f\"\\n{pair_key}:\")\n        print(f\"  Attention heads:  rho={corr['attn']['rho']:.4f}  \"\n              f\"(p={corr['attn']['p_value']:.2e})\")\n        print(f\"  MLP groups:       rho={corr['mlp']['rho']:.4f}  \"\n              f\"(p={corr['mlp']['p_value']:.2e})\")\n        print(f\"  Combined:         rho={corr['combined']['rho']:.4f}  \"\n              f\"(p={corr['combined']['p_value']:.2e})\")\n\n    status = \"PASS\" if results[\"summary\"][\"stable\"] else \"FAIL\"\n    print(f\"\\nOverall: {status} (threshold rho>0.95, \"\n          f\"min rho={results['summary']['min_combined_rho']:.4f})\")\n    print(f\"{'=' * 60}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 57_

<details><summary>Logged reasoning block</summary>

```text
Now let me verify the model path on the server to confirm. Let me also check the server setup.

Let me look for the model path in existing scripts or configs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "d0dcbb9b-5630-4919-8c09-79f6cdf4d115",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rJXymskjS5T3hoNcsgmka",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9433,
      "cache_read_input_tokens": 40522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9433
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

_source line 58_

脚本已写好。确认一下服务器上的模型路径。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "c4db6011-db3d-47cf-a2ac-8b3b6bb656b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rJXymskjS5T3hoNcsgmka",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9433,
      "cache_read_input_tokens": 40522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9433
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

_source line 59_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QU2d81sFGgBRpbAujeavqb`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
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
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "10860cad-64bb-48d2-bcbf-feaf61323e5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rJXymskjS5T3hoNcsgmka",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9433,
      "cache_read_input_tokens": 40522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9433
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

_source line 60 · 2026-05-19T21:25:42.343Z_

<details><summary>↩ Tool result · `toolu_01QU2d81sFGgBRpbAujeavqb`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
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
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "06e9d526-2ddb-415a-bc66-5f497985e7c1",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016NLDN277rw3hJK4XnRW6yB`</summary>

```json
{
  "server": "westb-23072",
  "command": "ls /root/autodl-tmp/recovery_aware_struct_prune/models/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "529ba238-ce89-407c-8147-273cff1fe221",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014msLAJEWJFR6bYAp5N9YCX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 496,
      "cache_read_input_tokens": 49955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 496
      },
      "output_tokens": 46,
      "service_tier": "standard",
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

_source line 62 · 2026-05-19T21:25:47.719Z_

<details><summary>↩ Tool result · `toolu_016NLDN277rw3hJK4XnRW6yB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"DeepSeek-R1-Distill-Qwen-1.5B\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.02}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "60c70ff6-2c9d-42b8-9658-f9d006e2b74e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"DeepSeek-R1-Distill-Qwen-1.5B\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.02}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"DeepSeek-R1-Distill-Qwen-1.5B\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.02}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 63_

<details><summary>Logged reasoning block</summary>

```text
The model on westb-23072 is DeepSeek-R1-Distill-Qwen-1.5B, not 7B. Let me check if the 7B model is elsewhere, or if it's on westd-29022.

Wait, the task says the model is DeepSeek-R1-Distill-Qwen-7B. Let me check the other server and also look for 7B on westb.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "3dce84d6-9b55-4f0c-b45b-53fca7039b58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ri5CRUe1igJE3ZrobYD1GU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 219,
      "cache_read_input_tokens": 50451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 219
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

_source line 64_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01ESNAug9TUS7Ch7swrLf14t`</summary>

```json
{
  "server": "westb-23072",
  "command": "find /root/autodl-tmp/recovery_aware_struct_prune/ -maxdepth 3 -name \"config.json\" -path \"*/models/*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "2c9e0290-3a23-4918-b428-4d778e0e72b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ri5CRUe1igJE3ZrobYD1GU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 219,
      "cache_read_input_tokens": 50451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 219
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

_source line 65_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WPNviJXtVbmdtHxsY8Fexn`</summary>

```json
{
  "server": "westd-29022",
  "command": "ls /root/autodl-tmp/recovery_aware_struct_prune/models/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "b2918fde-ad2a-4ed1-8867-6d8cc924ffbb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ri5CRUe1igJE3ZrobYD1GU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 219,
      "cache_read_input_tokens": 50451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 219
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

_source line 66 · 2026-05-19T21:25:53.547Z_

<details><summary>↩ Tool result · `toolu_01ESNAug9TUS7Ch7swrLf14t`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/recovery_aware_struct_prune/models/DeepSeek-R1-Distill-Qwen-1.5B/config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.79}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "a84dbc93-2649-410a-9531-01535691e22e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/models/DeepSeek-R1-Distill-Qwen-1.5B/config.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.79}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/recovery_aware_struct_prune/models/DeepSeek-R1-Distill-Qwen-1.5B/config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.79}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-19T21:25:54.601Z_

<details><summary>↩ Tool result · `toolu_01WPNviJXtVbmdtHxsY8Fexn`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/recovery_aware_struct_prune/models/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.04}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "93772306-dcdd-4a47-9264-0b68abf30b65",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"ls: cannot access '/root/autodl-tmp/recovery_aware_struct_prune/models/': No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.04}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/recovery_aware_struct_prune/models/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.04}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01F1ZstXbjTZxE56zMSX23sr`</summary>

```json
{
  "server": "westd-29022",
  "command": "find /root/autodl-tmp/ -maxdepth 3 -name \"config.json\" -path \"*Qwen*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "15fc40e1-fbec-4be9-9ff4-cb6b90054881",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014G3AAsdKPEsUqMLfdJwsWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 50670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 652
      },
      "output_tokens": 63,
      "service_tier": "standard",
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

_source line 69 · 2026-05-19T21:25:57.665Z_

<details><summary>↩ Tool result · `toolu_01F1ZstXbjTZxE56zMSX23sr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B/config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "386928ad-9fbf-4e20-8fd3-f9d694e02bcb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B/config.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B/config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 70_

<details><summary>Logged reasoning block</summary>

```text
OK so:
- westb-23072: has 1.5B model at `/root/autodl-tmp/recovery_aware_struct_prune/models/DeepSeek-R1-Distill-Qwen-1.5B/`
- westd-29022: has 7B model at `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B/`

The task says to run on "westd:3" which means westd-29022 cuda:3. And the 7B model is on westd-29022.


I should verify that the project code is also available on westd-29022.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "df996b3a-9bf4-44e8-9054-c881479c8062",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013cfATueXH5krTfsSujPPek",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 238,
      "cache_read_input_tokens": 51322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 238
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

_source line 71_

7B 模型在 westd-29022 的 `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B/`。确认 westd 上的项目代码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "0c87d08d-d7a8-4fc9-be16-aaa63da9a679",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013cfATueXH5krTfsSujPPek",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 238,
      "cache_read_input_tokens": 51322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 238
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

_source line 72_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MS5pUhrRMsynfsALjaN2xf`</summary>

```json
{
  "server": "westd-29022",
  "command": "ls /root/recovery_aware_struct_prune/src/cka_overlap.py /root/recovery_aware_struct_prune/src/run_cka_reliability.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "bee744f2-a1c6-44f7-8c08-f6826aae84f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013cfATueXH5krTfsSujPPek",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 238,
      "cache_read_input_tokens": 51322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 238
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

_source line 73 · 2026-05-19T21:26:04.293Z_

<details><summary>↩ Tool result · `toolu_01MS5pUhrRMsynfsALjaN2xf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/recovery_aware_struct_prune/src/cka_overlap.py\\n/root/recovery_aware_struct_prune/src/run_cka_reliability.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "27ce5db0-7857-430f-a01a-88440ce469b7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/recovery_aware_struct_prune/src/cka_overlap.py\\\\n/root/recovery_aware_struct_prune/src/run_cka_reliability.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/recovery_aware_struct_prune/src/cka_overlap.py\\n/root/recovery_aware_struct_prune/src/run_cka_reliability.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 74_

代码就位。需要先把新脚本同步到 westd-29022 再运行。确认 GPU 3 可用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "cb208922-e2cf-4cc1-a78c-6c64efef0fff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F6HsZvQwSzpNpXZ54dx6Sf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 495,
      "cache_read_input_tokens": 51560,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 495
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

_source line 75_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01AsC4Dnz4qxF5hwVz7Eq1S5`</summary>

```json
{
  "server": "westd-29022",
  "command": "python3 -c \"import torch; print(torch.cuda.get_device_name(3), torch.cuda.mem_get_info(3)[0]//1024**3, 'GB free')\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "7f43f6b5-d871-44b3-9358-83e67c1f2790",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F6HsZvQwSzpNpXZ54dx6Sf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 495,
      "cache_read_input_tokens": 51560,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 495
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

_source line 76 · 2026-05-19T21:26:19.929Z_

<details><summary>↩ Tool result · `toolu_01AsC4Dnz4qxF5hwVz7Eq1S5`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "33b3f9b2-f384-4abc-bdc8-ff0677818ec9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 77_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WaPsUtRQ9A1i8u2qJfPoAr`</summary>

```json
{
  "server": "westd-29022",
  "command": "python3 -c \"import torch; print(torch.cuda.get_device_name(3), torch.cuda.mem_get_info(3)[0]//1024**3, 'GB free')\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "2f1013d5-936b-49af-854a-e12b49e72fac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3wy15g923YxCVUmC5hj4q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 385,
      "cache_read_input_tokens": 52055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 385
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

_source line 78 · 2026-05-19T21:26:22.962Z_

<details><summary>↩ Tool result · `toolu_01WaPsUtRQ9A1i8u2qJfPoAr`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "b5a0ce90-1e81-4ae2-9f71-21835c4d860f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 79_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013D6x2JswPs9yZaX4cu5G4q`</summary>

```json
{
  "server": "westd-29022",
  "command": "python3 -c \"import torch; print(torch.cuda.get_device_name(3))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "066487f9-9251-43bc-8029-70d95c2fa230",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vp6Kr6YsF113Y1ZzEXkdS9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 243,
      "cache_read_input_tokens": 52440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 243
      },
      "output_tokens": 73,
      "service_tier": "standard",
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

_source line 80 · 2026-05-19T21:26:26.573Z_

<details><summary>↩ Tool result · `toolu_013D6x2JswPs9yZaX4cu5G4q`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "e3f7716a-932f-4dcc-ade2-2e2bb7250689",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 81_

<details><summary>Logged reasoning block</summary>

```text
The semicolons inside the Python string are being caught by the read-only filter. Let me use nvidia-smi instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "fa3756b1-2bf7-40a7-b4cd-c3977f0fb99d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013j3F7WEhNixiyFoMUTzhCW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 218,
      "cache_read_input_tokens": 52683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 218
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

_source line 82_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HkMk7rEXuR9nM8DRJ5bm2g`</summary>

```json
{
  "server": "westd-29022",
  "command": "nvidia-smi --query-gpu=index,name,memory.total,memory.free --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "99326a6e-dda3-4eee-b468-e86fdf8f9fba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013j3F7WEhNixiyFoMUTzhCW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 218,
      "cache_read_input_tokens": 52683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 218
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

_source line 83 · 2026-05-19T21:26:31.496Z_

<details><summary>↩ Tool result · `toolu_01HkMk7rEXuR9nM8DRJ5bm2g`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, NVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB, 84392 MiB\\n1, NVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB, 79974 MiB\\n2, NVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB, 80484 MiB\\n3, NVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB, 97250 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "8932e239-f79e-42de-b7d6-5ee58fc68ea9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"0, NVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB, 84392 MiB\\\\n1, NVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB, 79974 MiB\\\\n2, NVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB, 80484 MiB\\\\n3, NVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB, 97250 MiB\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"0, NVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB, 84392 MiB\\n1, NVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB, 79974 MiB\\n2, NVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB, 80484 MiB\\n3, NVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB, 97250 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 84_

GPU 3 有 97GB 可用，完全够用。以下是脚本和运行方案总结：

---

**脚本路径**: `src/cka_stability_analysis.py`

**运行命令** (westd-29022, cuda:3):
```bash
cd /root/recovery_aware_struct_prune && python src/cka_stability_analysis.py \
  --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B \
  --output_path /root/autodl-tmp/recovery_aware_struct_prune/cka_stability_results.json \
  --device cuda:3
```

**脚本逻辑**:
1. 加载 7B dense 模型到 cuda:3
2. 加载 1024 个 GSM8K train 校准样本（seed=42，与 pruning 一致）
3. 收集全部 1024 样本的 q_proj（attn heads）和 gate_proj（MLP groups）激活
4. 释放模型，对 256/512/1024 三种 size 分别计算 F(h)（通过 subsample indices，256 ⊂ 512 ⊂ 1024）
5. 计算 3 对 Spearman rank correlation（attn / mlp / combined）
6. 输出 top-10 / bottom-10 结构 + 完整 JSON

**复用函数**: `load_calibration_data`, `set_seed` from `cka_overlap.py`; `collect_qproj_activations`, `collect_mlp_activations`, `compute_fh_scores` from `run_cka_reliability.py`

**预估运行时间**: ~25-35 分钟
- 模型加载: ~1 min
- 前向收集激活 (2×1024 samples): ~10 min
- F(h) 计算 (3 sizes × 2 types × 28 layers × 378 pairs): ~15-20 min

需要先把脚本 sync 到 westd-29022，是否批准运行？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "uuid": "a4820c7d-b968-4576-8b3a-ec4e7a3b5a50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5XxT6gfvN8sb8kQYtbnAE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 384,
      "cache_read_input_tokens": 52901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 384
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

_source line 85_

GPU 3 有 97GB 可用，完全够用。以下是脚本和运行方案总结：

---

**脚本路径**: `src/cka_stability_analysis.py`

**运行命令** (westd-29022, cuda:3):
```bash
cd /root/recovery_aware_struct_prune && python src/cka_stability_analysis.py \
  --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B \
  --output_path /root/autodl-tmp/recovery_aware_struct_prune/cka_stability_results.json \
  --device cuda:3
```

**脚本逻辑**:
1. 加载 7B dense 模型到 cuda:3
2. 加载 1024 个 GSM8K train 校准样本（seed=42，与 pruning 一致）
3. 收集全部 1024 样本的 q_proj（attn heads）和 gate_proj（MLP groups）激活
4. 释放模型，对 256/512/1024 三种 size 分别计算 F(h)（通过 subsample indices，256 ⊂ 512 ⊂ 1024）
5. 计算 3 对 Spearman rank correlation（attn / mlp / combined）
6. 输出 top-10 / bottom-10 结构 + 完整 JSON

**复用函数**: `load_calibration_data`, `set_seed` from `cka_overlap.py`; `collect_qproj_activations`, `collect_mlp_activations`, `compute_fh_scores` from `run_cka_reliability.py`

**预估运行时间**: ~25-35 分钟
- 模型加载: ~1 min
- 前向收集激活 (2×1024 samples): ~10 min
- F(h) 计算 (3 sizes × 2 types × 28 layers × 378 pairs): ~15-20 min

需要先把脚本 sync 到 westd-29022，是否批准运行？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 282801,
  "duration_api_ms": 280318,
  "num_turns": 19,
  "stop_reason": "end_turn",
  "session_id": "eed79268-9e39-47a1-a855-8f15cce15e10",
  "total_cost_usd": 0.9875314999999999,
  "usage": {
    "input_tokens": 19,
    "cache_creation_input_tokens": 41444,
    "cache_read_input_tokens": 621850,
    "output_tokens": 12557,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 41444,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 568,
        "cache_read_input_tokens": 52901,
        "cache_creation_input_tokens": 384,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 384
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1928,
      "outputTokens": 3033,
      "cacheReadInputTokens": 276235,
      "cacheCreationInputTokens": 47076,
      "webSearchRequests": 0,
      "costUSD": 0.10356150000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 19,
      "outputTokens": 12557,
      "cacheReadInputTokens": 621850,
      "cacheCreationInputTokens": 41444,
      "webSearchRequests": 0,
      "costUSD": 0.88397,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3106d78e-5de2-4546-8e70-1c52f1f35831"
}
```

</details>

---
