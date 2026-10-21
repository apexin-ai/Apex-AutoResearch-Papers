# code baseline battery 009 — Part 1 of 2

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Worker execution logs

[Transcript overview](../code-baseline-battery-009.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/d3/d3feb99d1f8fb95d1b89.json)

## Before a recorded user message

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
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
  "uuid": "99fc505b-432d-448f-9d03-9a87ece0df1d",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est/memory/"
  },
  "fast_mode_state": "off"
}
```

---


### Assistant

_source line 3_

Looking at the project structure and existing code first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "bf31997e-9826-4202-a809-1ab9099845e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZ8MSHzXqYFe99NFqNnMAo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11759,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11759
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


### Runtime record

_source line 4_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778803200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "5019333b-3801-46f2-8235-53f10402b8aa",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Agent · `toolu_018LqyWVrFGYJWUDKTkV7xwf`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Explore project structure and existing code",
  "prompt": "Explore the project at /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est to understand:\n1. Overall directory structure\n2. The existing classify.py at src/classify.py - read the full file\n3. Any existing baselines code\n4. Data format - check if data/features_all.jsonl exists locally or only on remote server\n5. Any requirements.txt or setup files\n\nSearch breadth: medium"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "a672a818-9578-4ecf-bf95-7e9b16a2ab5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZ8MSHzXqYFe99NFqNnMAo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11759,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11759
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


### System

_source line 6_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Explore project structure and existing code",
  "task_type": "local_agent",
  "prompt": "Explore the project at /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est to understand:\n1. Overall directory structure\n2. The existing classify.py at src/classify.py - read the full file\n3. Any existing baselines code\n4. Data format - check if data/features_all.jsonl exists locally or only on remote server\n5. Any requirements.txt or setup files\n\nSearch breadth: medium",
  "uuid": "e1886cfb-2ab0-42b0-a0c2-34033e728dd7",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


## Round 1

## Round 1

181 recorded events


### User

_source line 7 · 2026-05-14T23:00:56.133Z_

Explore the project at /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est to understand:
1. Overall directory structure
2. The existing classify.py at src/classify.py - read the full file
3. Any existing baselines code
4. Data format - check if data/features_all.jsonl exists locally or only on remote server
5. Any requirements.txt or setup files

Search breadth: medium

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "4118f27f-8bb2-4c3d-916d-ae90cb689c61"
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
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 16460,
    "tool_uses": 1,
    "duration_ms": 1710
  },
  "last_tool_name": "Bash",
  "uuid": "db1928f3-8f35-4227-a06d-1f1488f8915e",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Bash · `toolu_01YHoTW6bhh7Se1kmzzFQ5KR`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est -type f -name \"*.py\" -o -name \"*.txt\" -o -name \"*.md\" -o -name \"*.jsonl\" -o -name \"*.yaml\" -o -name \"*.yml\" | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "98cf42ea-6d3c-477c-8b9d-49ec12e42308",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Mvma1rAYhcLskYj6gMWiUX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16451,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16451,
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

_source line 10 · 2026-05-14T23:00:58.114Z_

<details><summary>↩ Tool result · `toolu_01YHoTW6bhh7Se1kmzzFQ5KR`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_ppl_regression.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/generate_next_depth.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/atlas_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_diveye_ordinal.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_utils.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/add_seed_id.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_zeroshot_llm.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_ce_classification.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/dcol_train_standalone_deprecated.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/lora_finetune.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_coral.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/IDEA_BRIEF.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/ralph_loop_timeline.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/worker_research_diveye_citation_verify_20260514T195449.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/cron_hook_gpt2xl_temp09_001.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/worker_code_baseline_rf_lr_unified_20260514T164446.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/worker_code_remaining_3x3_scripts_20260514T193717.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/worker_analysis_cross_model_gpt2xl_001_20260514T182022.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/worker_ssh_dcol_cleanup_and_verify_20260514T193350.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/cron_hook_mvp_pipeline_pythia_002.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/worker_code_prep_remaining_scripts_20260514T174849.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/worker_monitor_training_progress_check_20260514T165444.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/worker_check_training_progress_20240514_20260514T201533.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/worker_infra_restart-qwen-base-pipeline_20260514T114711.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/worker_ssh_olmo_rescue_20260514T170614.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/cron_hook_pythia_temp09_001.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/cron_hook_cross_model_olmo_002.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/worker_code_submit_pythia_topk50_20260514T182132.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/worker_code_dcol_feature_based_20260514T161727.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/archive/cron_hook_cross_model_gpt2xl_001_20260514T224322_468770.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer_20260514T135853_757198.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/archive/cron_hook_cross_model_olmo_001_20260514T174649_607019.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer_20260514T182340_195492.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/archive/cron_hook_pythia_temp09_001_20260514T193428_924631.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/archive/feishu_group_oc_5d269fdb74af3f4ab8d78b82a993f5cf_director_20260514T182347_469604.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/archive/feishu_group_oc_5d269fdb74af3f4ab8d78b82a993f5cf_director_20260514T224243_176612.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/archive/cron_hook_mvp_pipeline_pythia_002_20260514T201353_465852.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/archive/feishu_group_oc_5d269fdb74af3f4ab8d78b82a993f5cf_director_20260514T155927_121865.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_20260514T224251_277821.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer_20260514T224248_233307.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/archive/cron_hook_mvp_pipeline_pythia_002_20260514T165224_990958.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/archive/cron_hook_pythia_temp09_001_20260514T225710_497159.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_20260514T155930_361689.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/worker_code_feature-extraction-v2_20260514T114749.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/cron_hook_cross_model_gpt2xl_001.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/cron_hook_pythia_topk50_001.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/worker_ssh_three_class_eval_persist_20260514T183740.jsonl
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "f096e5a2-2f9c-42d0-ba4c-a036c0ced47c"
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
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 20309,
    "tool_uses": 2,
    "duration_ms": 3436
  },
  "last_tool_name": "Bash",
  "uuid": "01f80f6e-e5ab-4010-9ed3-cd1fb537bfd1",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Bash · `toolu_01GTs1pb178LZFXRFqmSsPmC`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "9980ad3c-5ac8-48da-bf6a-efc91e3a081e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LQwQ3iYDYqG9Y2qE8faXL4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3845,
      "cache_read_input_tokens": 16451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3845,
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

_source line 13 · 2026-05-14T23:00:59.646Z_

<details><summary>↩ Tool result · `toolu_01GTs1pb178LZFXRFqmSsPmC`</summary>

```text
total 156
drwxr-xr-x 9 ubuntu ubuntu  4096 May 14 23:00 .
drwxrwxr-x 7 ubuntu ubuntu  4096 May 14 09:51 ..
drwxr-xr-x 3 ubuntu ubuntu  4096 May 14 09:51 .claude
-rw-r--r-- 1 ubuntu ubuntu 12798 May 14 23:00 AGENTS.md
-rw-r--r-- 1 ubuntu ubuntu     0 May 14 09:53 ROADMAP.lock
-rw------- 1 ubuntu ubuntu  5038 May 14 23:00 ROADMAP.md
drwxr-xr-x 7 ubuntu ubuntu  4096 May 14 22:44 artifacts
drwxr-xr-x 2 ubuntu ubuntu 12288 May 14 23:00 checkpoints
-rw-r--r-- 1 ubuntu ubuntu     0 May 14 14:03 decisions.lock
-rw------- 1 ubuntu ubuntu  5684 May 14 22:47 decisions.yaml
drwxr-xr-x 2 ubuntu ubuntu  4096 May 14 09:51 docs
-rwxr-xr-x 1 ubuntu ubuntu     0 May 14 14:06 dream_registry.lock
-rw------- 1 ubuntu ubuntu   963 May 14 15:06 dream_registry.yaml
-rw-r--r-- 1 ubuntu ubuntu   968 May 14 15:06 dream_registry.yaml.bak
-rw-r--r-- 1 ubuntu ubuntu  6005 May 14 23:00 experiment_plan.yaml
drwxr-xr-x 4 ubuntu ubuntu  4096 May 14 09:55 logs
-rw-r--r-- 1 ubuntu ubuntu  5839 May 14 22:50 memory.md
-rw-r--r-- 1 ubuntu ubuntu  8067 May 14 22:47 paper_framing.md
-rw-r--r-- 1 ubuntu ubuntu     0 May 14 10:14 registry.lock
-rw------- 1 ubuntu ubuntu 44072 May 14 23:00 registry.yaml
-rw-r--r-- 1 ubuntu ubuntu  2075 May 14 23:00 report.md
drwxr-xr-x 2 ubuntu ubuntu  4096 May 14 19:56 scripts
-rwxr-xr-x 1 ubuntu ubuntu     0 May 14 09:51 study_status.lock
drwxr-xr-x 3 ubuntu ubuntu  4096 May 14 22:57 task_context
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "b49450dd-a393-4e45-a54c-1cd28c2d1c92"
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
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 21127,
    "tool_uses": 3,
    "duration_ms": 4947
  },
  "last_tool_name": "Bash",
  "uuid": "7a2a73e7-5be9-467d-a072-02c7a71c9e21",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Bash · `toolu_01E3ksak9aE5tCNLuJ6bjXk2`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est -type d -name \"src\" -o -name \"data\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "7456e4c7-386a-43a2-a889-d6672d9fbd3e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GT6utLfWXgJFvPSJvDrPt5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 812,
      "cache_read_input_tokens": 20296,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 812,
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

_source line 16 · 2026-05-14T23:01:01.138Z_

<details><summary>↩ Tool result · `toolu_01E3ksak9aE5tCNLuJ6bjXk2`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/data
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "bb087759-6051-4afb-86a9-3b109f742f2d"
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
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 21289,
    "tool_uses": 4,
    "duration_ms": 6222
  },
  "last_tool_name": "Bash",
  "uuid": "7bf9dbf0-4ed4-4819-ac8f-f65ebd2c07d5",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_014HiZ6epXApCaFbXEBmcMHG`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est -name \"classify.py\" -o -name \"requirements.txt\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "27e5c34c-ba5a-4a70-ab27-710fd2ac1111",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KYP2n8QcacZLXbUW8ory2X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 160,
      "cache_read_input_tokens": 21108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 160,
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

_source line 19 · 2026-05-14T23:01:02.419Z_

<details><summary>↩ Tool result · `toolu_014HiZ6epXApCaFbXEBmcMHG`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "ea818562-9cdd-42b6-b84f-7180d2403ec6"
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
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 21422,
    "tool_uses": 5,
    "duration_ms": 7504
  },
  "last_tool_name": "Bash",
  "uuid": "c1d360e4-e62f-4c1b-bc11-3fa6cc0aae68",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Bash · `toolu_01MhMnts2ZXbGQFAnpPgXMP2`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "d9f2e96a-2575-4a5b-9f0b-1e7bcf6a5ceb",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GY4CnesJnaA8byBzTxYCiU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 126,
      "cache_read_input_tokens": 21268,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 126,
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

_source line 22 · 2026-05-14T23:01:03.696Z_

<details><summary>↩ Tool result · `toolu_01MhMnts2ZXbGQFAnpPgXMP2`</summary>

```text
total 160
drwxr-xr-x 7 ubuntu ubuntu  4096 May 14 22:44 .
drwxr-xr-x 9 ubuntu ubuntu  4096 May 14 23:00 ..
drwxr-xr-x 5 ubuntu ubuntu  4096 May 14 17:18 _project
-rw-r--r-- 1 ubuntu ubuntu 11517 May 14 20:15 baseline_diveye.py
-rw-r--r-- 1 ubuntu ubuntu 10919 May 14 20:14 baseline_perplexity_regression.py
-rw-r--r-- 1 ubuntu ubuntu 13388 May 14 20:16 baseline_zero_shot_llm.py
-rw-r--r-- 1 ubuntu ubuntu 26894 May 14 17:21 baselines.py
-rw-r--r-- 1 ubuntu ubuntu  1681 May 14 22:44 dcol_002_oom_diagnosis.md
drwxr-xr-x 2 ubuntu ubuntu  4096 May 14 16:56 dcol_code
drwxr-xr-x 3 ubuntu ubuntu  4096 May 14 22:44 dcol_deberta_002
-rw-r--r-- 1 ubuntu ubuntu 29131 May 14 19:55 dcol_feature_mlp.py
-rw-r--r-- 1 ubuntu ubuntu  2010 May 14 17:18 diveye_citation_audit.md
drwxr-xr-x 3 ubuntu ubuntu  4096 May 14 15:06 dream_reports
-rw-r--r-- 1 ubuntu ubuntu  5444 May 14 16:11 eval_d1d3.py
-rw-r--r-- 1 ubuntu ubuntu  7755 May 14 22:39 feature_importance_consistency_analysis.md
-rw-r--r-- 1 ubuntu ubuntu  6926 May 14 22:44 manifest.yaml
drwxr-xr-x 3 ubuntu ubuntu  4096 May 14 20:31 pythia_topk50_001
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "9258ddee-17dd-46d8-b7e5-de7901b45500"
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
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 22092,
    "tool_uses": 6,
    "duration_ms": 8775
  },
  "last_tool_name": "Bash",
  "uuid": "4bec26bc-cc4e-43b6-a0bd-6990c61223f6",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Bash · `toolu_01XoFYwEUuX82pKTVtkYy6rx`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "15153ba6-f87a-4767-b7e1-f5953eef5f00",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EiEDCv4JjsygkczAfyVdpP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 668,
      "cache_read_input_tokens": 21394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 668,
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

_source line 25 · 2026-05-14T23:01:04.987Z_

<details><summary>↩ Tool result · `toolu_01XoFYwEUuX82pKTVtkYy6rx`</summary>

```text
total 20
drwxr-xr-x 5 ubuntu ubuntu 4096 May 14 17:18 .
drwxr-xr-x 7 ubuntu ubuntu 4096 May 14 22:44 ..
drwxr-xr-x 2 ubuntu ubuntu 4096 May 14 18:38 data
drwxr-xr-x 2 ubuntu ubuntu 4096 May 14 16:57 intermediate
drwxr-xr-x 2 ubuntu ubuntu 4096 May 14 17:18 report
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "2cd0ad00-8810-4b99-ad44-fc7875cde651"
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
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Running ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 22416,
    "tool_uses": 7,
    "duration_ms": 9959
  },
  "last_tool_name": "Bash",
  "uuid": "8fde6b65-c3b1-4e46-9d96-815c1bf86af5",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Bash · `toolu_01L5yN7PcR8YYSgNBPzHDhvk`</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/data/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "1c36c45a-3693-4614-b4a6-1b6c30585fec",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MYM3M5N8VMPrN4ab4BdYg5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 259,
      "cache_read_input_tokens": 22062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 259,
        "ephemeral_1h_input_tokens": 0
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

_source line 28 · 2026-05-14T23:01:06.204Z_

<details><summary>↩ Tool result · `toolu_01L5yN7PcR8YYSgNBPzHDhvk`</summary>

```text
total 20K
-rw-r--r-- 1 ubuntu ubuntu 753 May 14 16:49 baseline_unified_comparison.md
-rw-r--r-- 1 ubuntu ubuntu 260 May 14 18:38 edd_matrix.json
-rw-r--r-- 1 ubuntu ubuntu 326 May 14 18:38 feature_consistency.json
-rw-r--r-- 1 ubuntu ubuntu 172 May 14 18:38 heatmap_data.json
-rw-r--r-- 1 ubuntu ubuntu 440 May 14 18:38 monotonicity_scores.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "77f00ccc-d3f1-4928-906d-af88516d2fc4"
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
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 22682,
    "tool_uses": 8,
    "duration_ms": 11908
  },
  "last_tool_name": "Bash",
  "uuid": "29bf7e59-c463-4251-afbe-461115c05f89",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Bash · `toolu_01EWD7S8ERNgSJbtZ2oU6ARs`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "dec18871-4489-42d2-854a-5f33f25f32bc",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019Bs6RrWKnnp3Rx72TfRk1W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 264,
      "cache_read_input_tokens": 22321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 264,
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

_source line 31 · 2026-05-14T23:01:08.106Z_

<details><summary>↩ Tool result · `toolu_01EWD7S8ERNgSJbtZ2oU6ARs`</summary>

```text
total 156
drwxr-xr-x 2 ubuntu ubuntu  4096 May 14 19:56 .
drwxr-xr-x 9 ubuntu ubuntu  4096 May 14 23:00 ..
-rw-r--r-- 1 ubuntu ubuntu   804 May 14 09:59 add_seed_id.py
-rw-r--r-- 1 ubuntu ubuntu 10517 May 14 18:36 atlas_analysis.py
-rw-r--r-- 1 ubuntu ubuntu  9106 May 14 19:56 baseline_ce_classification.py
-rw-r--r-- 1 ubuntu ubuntu 11152 May 14 19:56 baseline_coral.py
-rw-r--r-- 1 ubuntu ubuntu  4571 May 14 18:59 baseline_diveye_ordinal.py
-rw-r--r-- 1 ubuntu ubuntu  4648 May 14 18:59 baseline_ppl_regression.py
-rw-r--r-- 1 ubuntu ubuntu  6400 May 14 18:58 baseline_utils.py
-rw-r--r-- 1 ubuntu ubuntu  6967 May 14 19:01 baseline_zeroshot_llm.py
-rw-r--r-- 1 ubuntu ubuntu 16840 May 14 19:21 dcol_train_standalone_deprecated.py
-rw-r--r-- 1 ubuntu ubuntu  5212 May 14 14:09 generate_next_depth.py
-rw-r--r-- 1 ubuntu ubuntu  4190 May 14 14:41 lora_finetune.py
-rw-r--r-- 1 ubuntu ubuntu  2288 May 14 18:51 run_eval_pythia_topk50.sh
-rw-r--r-- 1 ubuntu ubuntu  2400 May 14 18:33 run_pipeline.sh
-rw-r--r-- 1 ubuntu ubuntu  3219 May 14 18:33 run_pipeline_gpt2xl.sh
-rwxr-xr-x 1 ubuntu ubuntu  3321 May 14 18:33 run_pipeline_gpt2xl_temp09.sh
-rwxr-xr-x 1 ubuntu ubuntu  3251 May 14 18:33 run_pipeline_gpt2xl_topk50.sh
-rw-r--r-- 1 ubuntu ubuntu  3203 May 14 18:33 run_pipeline_olmo.sh
-rwxr-xr-x 1 ubuntu ubuntu  3315 May 14 18:33 run_pipeline_olmo_temp09.sh
-rwxr-xr-x 1 ubuntu ubuntu  3245 May 14 18:33 run_pipeline_olmo_topk50.sh
-rwxr-xr-x 1 ubuntu ubuntu  3142 May 14 18:33 run_pipeline_pythia_temp09.sh
-rwxr-xr-x 1 ubuntu ubuntu  3077 May 14 18:33 run_pipeline_pythia_topk50.sh
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "10bf75dc-02fb-4ab9-b446-0ea37afdb92a"
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
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Reading scripts/baseline_utils.py",
  "usage": {
    "total_tokens": 23595,
    "tool_uses": 9,
    "duration_ms": 14411
  },
  "last_tool_name": "Read",
  "uuid": "865be2c4-5ce5-48eb-86f7-3db50c684d50",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01XMqKNqrppcm2QYejM77N9H`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_utils.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "816ff3e3-b895-4a15-99e7-de189bb413b1",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KF4XVE8M3k24mZtZq67Sbd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 911,
      "cache_read_input_tokens": 22585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 911,
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

_source line 34 · 2026-05-14T23:01:10.559Z_

<details><summary>↩ Tool result · `toolu_01XMqKNqrppcm2QYejM77N9H`</summary>

```text
1	"""
2	Shared utilities for baseline battery experiments.
3	
4	Provides: data loading (raw JSONL + pre-extracted features), stratified splitting,
5	evaluation metrics (accuracy, MAE, pairwise AUC, classification report), and
6	standardized output saving.
7	"""
8	
9	import json
10	import os
11	import glob as glob_mod
12	import numpy as np
13	from collections import Counter
14	from sklearn.model_selection import train_test_split
15	from sklearn.metrics import (
16	    accuracy_score, classification_report, confusion_matrix, roc_auc_score,
17	)
18	
19	NUM_DEPTHS = 4
20	DEPTH_LABELS = list(range(NUM_DEPTHS))
21	
22	FEATURE_NAMES = [
23	    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
24	    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
25	    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
26	    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
27	    "rep_2gram", "rep_3gram", "rep_4gram",
28	]
29	NUM_FEATURES = len(FEATURE_NAMES)
30	
31	
32	# ── Data loading ──
33	
34	def load_jsonl_data(data_dirs, max_samples=0, seed=42):
35	    """Load raw text + depth labels from depth_*.jsonl files across directories."""
36	    texts, labels = [], []
37	    for data_dir in data_dirs:
38	        for d in range(NUM_DEPTHS):
39	            fpath = os.path.join(data_dir, f"depth_{d}.jsonl")
40	            if not os.path.exists(fpath):
41	                matches = glob_mod.glob(os.path.join(data_dir, f"*depth_{d}*.jsonl"))
42	                fpath = matches[0] if matches else None
43	            if fpath is None or not os.path.exists(fpath):
44	                continue
45	            with open(fpath) as f:
46	                for line in f:
47	                    line = line.strip()
48	                    if not line:
49	                        continue
50	                    rec = json.loads(line)
51	                    texts.append(rec["text"])
52	                    labels.append(rec.get("depth", d))
53	    labels = np.array(labels, dtype=np.int64)
54	    if max_samples > 0 and len(texts) > max_samples:
55	        rng = np.random.RandomState(seed)
56	        idx = sorted(rng.choice(len(texts), max_samples, replace=False))
57	        texts = [texts[i] for i in idx]
58	        labels = labels[idx]
59	    print(f"Loaded {len(texts)} samples. Depth distribution: {dict(Counter(labels))}")
60	    return texts, labels
61	
62	
63	def load_features(features_path):
64	    """Load pre-extracted 19-dim features from JSONL → (X [n, 19], y [n])."""
65	    records = []
66	    with open(features_path) as f:
67	        for line in f:
68	            line = line.strip()
69	            if line:
70	                records.append(json.loads(line))
71	    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)
72	    y = np.array([r["depth"] for r in records], dtype=np.int64)
73	    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
74	    print(f"Loaded features: {X.shape[0]} samples, {X.shape[1]} dims. "
75	          f"Depth distribution: {dict(Counter(y))}")
76	    return X, y
77	
78	
79	# ── Splitting ──
80	
81	def stratified_split(labels, eval_split=0.1, seed=42):
82	    """Return (train_idx, eval_idx) arrays with stratification."""
83	    train_idx, eval_idx = train_test_split(
84	        np.arange(len(labels)), test_size=eval_split,
85	        stratify=labels, random_state=seed,
86	    )
87	    return train_idx, eval_idx
88	
89	
90	# ── Evaluation ──
91	
92	def _pairwise_auc(y_true, y_prob, d1, d2):
93	    mask = np.isin(y_true, [d1, d2])
94	    if mask.sum() < 2:
95	        return None
96	    yt = (y_true[mask] == d2).astype(int)
97	    if len(np.unique(yt)) < 2:
98	        return None
99	    yp = y_prob[mask, d2]
100	    return float(roc_auc_score(yt, yp))
101	
102	
103	def compute_all_pairwise_auc(y_true, y_prob):
104	    result = {}
105	    for i, d1 in enumerate(DEPTH_LABELS):
106	        for d2 in DEPTH_LABELS[i + 1:]:
107	            auc = _pairwise_auc(y_true, y_prob, d1, d2)
108	            result[f"d{d1}_vs_d{d2}"] = round(auc, 4) if auc is not None else None
109	    return result
110	
111	
112	def evaluate_and_save(method_name, y_true, y_pred, y_prob, output_dir):
113	    """Compute all metrics, print summary, save three output files."""
114	    os.makedirs(output_dir, exist_ok=True)
115	    y_true = np.asarray(y_true)
116	    y_pred = np.asarray(y_pred)
117	
118	    acc = accuracy_score(y_true, y_pred)
119	    mae = float(np.mean(np.abs(y_true - y_pred)))
120	    cr_dict = classification_report(
121	        y_true, y_pred,
122	        target_names=[f"d{d}" for d in DEPTH_LABELS],
123	        output_dict=True, zero_division=0,
124	    )
125	    pair_aucs = compute_all_pairwise_auc(y_true, y_prob) if y_prob is not None else {}
126	
127	    print(f"\n{'=' * 50}")
128	    print(f"  {method_name}")
129	    print(f"{'=' * 50}")
130	    print(f"  Accuracy: {acc:.4f}   MAE: {mae:.4f}")
131	    if pair_aucs:
132	        print(f"  Pairwise AUC: {pair_aucs}")
133	    print(classification_report(
134	        y_true, y_pred,
135	        target_names=[f"d{d}" for d in DEPTH_LABELS], zero_division=0,
136	    ))
137	
138	    # 1) classification report
139	    report = {"accuracy": round(acc, 4), "mae": round(mae, 4), "per_class": cr_dict}
140	    _save_json(os.path.join(output_dir, f"{method_name}_classification_report.json"), report)
141	
142	    # 2) pairwise AUC
143	    _save_json(os.path.join(output_dir, f"{method_name}_pairwise_auc.json"), pair_aucs)
144	
145	    # 3) predictions
146	    preds = []
147	    for i in range(len(y_true)):
148	        entry = {"y_true": int(y_true[i]), "y_pred": int(y_pred[i])}
149	        if y_prob is not None:
150	            entry["y_prob"] = [round(float(p), 6) for p in y_prob[i]]
151	        preds.append(entry)
152	    _save_json(os.path.join(output_dir, f"{method_name}_predictions.json"), preds)
153	
154	    print(f"  Saved to {output_dir}/")
155	    return {"accuracy": acc, "mae": mae, "pairwise_auc": pair_aucs}
156	
157	
158	def _save_json(path, obj):
159	    with open(path, "w") as f:
160	        json.dump(obj, f, indent=2)
161	
162	
163	def add_common_args(parser):
164	    """Add the unified CLI arguments shared across all baselines."""
165	    parser.add_argument("--data_dirs", nargs="+", default=["data/"],
166	                        help="Directories containing depth_*.jsonl files")
167	    parser.add_argument("--features_path", default=None,
168	                        help="Path to pre-extracted features JSONL (for feature-based methods)")
169	    parser.add_argument("--output_dir", default="results/baselines/")
170	    parser.add_argument("--seed", type=int, default=42)
171	    parser.add_argument("--eval_split", type=float, default=0.1)
172	    parser.add_argument("--max_seq_len", type=int, default=512)
173	    parser.add_argument("--max_samples", type=int, default=0,
174	                        help="Max total samples to use (0 = all)")
175	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "0d24878e-808f-4b13-b14e-6e7a0eb4afde"
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
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Reading scripts/baseline_ce_classification.py",
  "usage": {
    "total_tokens": 26347,
    "tool_uses": 10,
    "duration_ms": 16434
  },
  "last_tool_name": "Read",
  "uuid": "44aea64b-817e-4a30-abcc-776817f70e9e",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01J7GRJt76WLWSrcksCQcSw2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_ce_classification.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "75c36556-0718-4e74-bdb7-b12f8a68a3ca",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HFpYCdEyNw3nid1HF8vRiB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 2748,
      "cache_read_input_tokens": 23496,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2748,
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

_source line 37 · 2026-05-14T23:01:12.591Z_

<details><summary>↩ Tool result · `toolu_01J7GRJt76WLWSrcksCQcSw2`</summary>

```text
1	"""
2	Baseline 4: Standard Cross-Entropy Classification for recursive generation depth estimation.
3	
4	Standard 4-class classification with DeBERTa backbone and CE loss.
5	No ordinal awareness — serves as ablation for DCOL and CORAL to demonstrate
6	that ordinal-aware losses add value.
7	
8	Architecture: DeBERTa → [CLS] pooling → Linear(hidden, 4) → CrossEntropyLoss
9	Default: DeBERTa-v3-large (435M) to match DCOL backbone for fair comparison.
10	
11	Input:  Raw depth_*.jsonl files (--data_dirs)
12	Output: {method}_classification_report.json, {method}_pairwise_auc.json, {method}_predictions.json
13	
14	Usage:
15	  python baseline_ce_classification.py --data_dirs data/  # default: deberta-v3-large
16	  python baseline_ce_classification.py --data_dirs data/ --model_name microsoft/deberta-v3-base --model_path /root/autodl-tmp/models/deberta-v3-base
17	  python baseline_ce_classification.py --data_dirs data/ --dry_run  # CPU, 2 steps
18	"""
19	
20	import argparse
21	import random
22	import numpy as np
23	import torch
24	import torch.nn as nn
25	from torch.utils.data import DataLoader, Dataset
26	from transformers import AutoModel, AutoTokenizer
27	
28	from baseline_utils import (
29	    load_jsonl_data, stratified_split, evaluate_and_save,
30	    add_common_args, NUM_DEPTHS,
31	)
32	
33	
34	def set_seed(seed):
35	    random.seed(seed)
36	    np.random.seed(seed)
37	    torch.manual_seed(seed)
38	    torch.cuda.manual_seed_all(seed)
39	
40	
41	class DepthTextDataset(Dataset):
42	    def __init__(self, texts, labels, tokenizer, max_seq_len):
43	        self.texts = texts
44	        self.labels = labels
45	        self.tokenizer = tokenizer
46	        self.max_seq_len = max_seq_len
47	
48	    def __len__(self):
49	        return len(self.texts)
50	
51	    def __getitem__(self, idx):
52	        enc = self.tokenizer(
53	            self.texts[idx],
54	            max_length=self.max_seq_len,
55	            padding="max_length",
56	            truncation=True,
57	            return_tensors="pt",
58	        )
59	        return {
60	            "input_ids": enc["input_ids"].squeeze(0),
61	            "attention_mask": enc["attention_mask"].squeeze(0),
62	            "label": torch.tensor(self.labels[idx], dtype=torch.long),
63	        }
64	
65	
66	class CEClassifier(nn.Module):
67	    """DeBERTa + linear head with standard cross-entropy loss."""
68	
69	    def __init__(self, model_name_or_path, num_classes=NUM_DEPTHS, dropout=0.1):
70	        super().__init__()
71	        self.encoder = AutoModel.from_pretrained(model_name_or_path)
72	        hidden_size = self.encoder.config.hidden_size
73	        self.dropout = nn.Dropout(dropout)
74	        self.classifier = nn.Linear(hidden_size, num_classes)
75	
76	    def forward(self, input_ids, attention_mask):
77	        outputs = self.encoder(input_ids=input_ids, attention_mask=attention_mask)
78	        cls_repr = outputs.last_hidden_state[:, 0, :]
79	        cls_repr = self.dropout(cls_repr)
80	        logits = self.classifier(cls_repr)
81	        return logits
82	
83	
84	def train_epoch(model, loader, optimizer, criterion, device, scaler, max_steps=None):
85	    model.train()
86	    total_loss, total_correct, total_samples = 0.0, 0, 0
87	    for step, batch in enumerate(loader):
88	        if max_steps and step >= max_steps:
89	            break
90	        input_ids = batch["input_ids"].to(device)
91	        attention_mask = batch["attention_mask"].to(device)
92	        labels = batch["label"].to(device)
93	
94	        optimizer.zero_grad()
95	        with torch.amp.autocast("cuda", enabled=scaler is not None):
96	            logits = model(input_ids, attention_mask)
97	            loss = criterion(logits, labels)
98	
99	        if scaler is not None:
100	            scaler.scale(loss).backward()
101	            scaler.unscale_(optimizer)
102	            nn.utils.clip_grad_norm_(model.parameters(), 1.0)
103	            scaler.step(optimizer)
104	            scaler.update()
105	        else:
106	            loss.backward()
107	            nn.utils.clip_grad_norm_(model.parameters(), 1.0)
108	            optimizer.step()
109	
110	        total_loss += loss.item() * len(labels)
111	        total_correct += (logits.argmax(dim=-1) == labels).sum().item()
112	        total_samples += len(labels)
113	
114	    return total_loss / max(total_samples, 1), total_correct / max(total_samples, 1)
115	
116	
117	@torch.no_grad()
118	def evaluate_model(model, loader, criterion, device, max_steps=None):
119	    model.eval()
120	    total_loss, all_preds, all_labels, all_probs = 0.0, [], [], []
121	    total_samples = 0
122	    for step, batch in enumerate(loader):
123	        if max_steps and step >= max_steps:
124	            break
125	        input_ids = batch["input_ids"].to(device)
126	        attention_mask = batch["attention_mask"].to(device)
127	        labels = batch["label"].to(device)
128	
129	        logits = model(input_ids, attention_mask)
130	        loss = criterion(logits, labels)
131	
132	        total_loss += loss.item() * len(labels)
133	        total_samples += len(labels)
134	        probs = torch.softmax(logits, dim=-1)
135	        all_preds.append(logits.argmax(dim=-1).cpu().numpy())
136	        all_labels.append(labels.cpu().numpy())
137	        all_probs.append(probs.cpu().numpy())
138	
139	    return (
140	        total_loss / max(total_samples, 1),
141	        np.concatenate(all_preds),
142	        np.concatenate(all_labels),
143	        np.concatenate(all_probs),
144	    )
145	
146	
147	def main():
148	    parser = argparse.ArgumentParser(description="Standard CE Classification baseline (DeBERTa)")
149	    add_common_args(parser)
150	    parser.add_argument("--model_name", default="microsoft/deberta-v3-large")
151	    parser.add_argument("--model_path", default="/root/autodl-tmp/models/deberta-v3-large")
152	    parser.add_argument("--epochs", type=int, default=5)
153	    parser.add_argument("--batch_size", type=int, default=16)
154	    parser.add_argument("--lr", type=float, default=2e-5)
155	    parser.add_argument("--warmup_ratio", type=float, default=0.1)
156	    parser.add_argument("--patience", type=int, default=3)
157	    parser.add_argument("--dropout", type=float, default=0.1)
158	    parser.add_argument("--fp16", action="store_true")
159	    parser.add_argument("--dry_run", action="store_true", help="CPU dry-run, 2 steps only")
160	    args = parser.parse_args()
161	
162	    set_seed(args.seed)
163	    device = torch.device("cpu") if args.dry_run else torch.device("cuda" if torch.cuda.is_available() else "cpu")
164	    print(f"Device: {device}")
165	
166	    texts, labels = load_jsonl_data(args.data_dirs, max_samples=args.max_samples, seed=args.seed)
167	    if args.dry_run and len(texts) > 64:
168	        texts, labels = texts[:64], labels[:64]
169	
170	    train_idx, eval_idx = stratified_split(labels, eval_split=args.eval_split, seed=args.seed)
171	    train_texts = [texts[i] for i in train_idx]
172	    eval_texts = [texts[i] for i in eval_idx]
173	    train_labels, eval_labels = labels[train_idx], labels[eval_idx]
174	    print(f"Train: {len(train_labels)}, Eval: {len(eval_labels)}")
175	
176	    tokenizer = AutoTokenizer.from_pretrained(args.model_path)
177	    train_ds = DepthTextDataset(train_texts, train_labels, tokenizer, args.max_seq_len)
178	    eval_ds = DepthTextDataset(eval_texts, eval_labels, tokenizer, args.max_seq_len)
179	    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True, num_workers=2, pin_memory=True)
180	    eval_loader = DataLoader(eval_ds, batch_size=args.batch_size * 2, shuffle=False, num_workers=2, pin_memory=True)
181	
182	    model = CEClassifier(args.model_path, dropout=args.dropout).to(device).float()
183	    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=0.01)
184	    criterion = nn.CrossEntropyLoss()
185	    scaler = torch.amp.GradScaler("cuda") if (args.fp16 and device.type == "cuda") else None
186	
187	    total_steps = len(train_loader) * args.epochs
188	    warmup_steps = int(total_steps * args.warmup_ratio)
189	    scheduler = torch.optim.lr_scheduler.LinearLR(
190	        optimizer, start_factor=0.1, total_iters=warmup_steps,
191	    )
192	
193	    max_steps_per_epoch = 2 if args.dry_run else None
194	    best_eval_loss = float("inf")
195	    patience_counter = 0
196	
197	    for epoch in range(args.epochs):
198	        train_loss, train_acc = train_epoch(
199	            model, train_loader, optimizer, criterion, device, scaler, max_steps=max_steps_per_epoch,
200	        )
201	        scheduler.step()
202	
203	        eval_loss, y_pred, y_true, y_prob = evaluate_model(
204	            model, eval_loader, criterion, device, max_steps=max_steps_per_epoch,
205	        )
206	        print(f"Epoch {epoch+1}/{args.epochs}  train_loss={train_loss:.4f}  "
207	              f"train_acc={train_acc:.4f}  eval_loss={eval_loss:.4f}")
208	
209	        if eval_loss < best_eval_loss - 1e-4:
210	            best_eval_loss = eval_loss
211	            patience_counter = 0
212	            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
213	            best_preds = (y_true.copy(), y_pred.copy(), y_prob.copy())
214	        else:
215	            patience_counter += 1
216	            if patience_counter >= args.patience:
217	                print(f"Early stopping at epoch {epoch+1}")
218	                break
219	
220	        if args.dry_run:
221	            print("Dry run complete (2 steps). Pipeline OK.")
222	            return
223	
224	    model.load_state_dict({k: v.to(device) for k, v in best_state.items()})
225	    y_true, y_pred, y_prob = best_preds
226	    model_tag = "large" if "large" in args.model_name else "base"
227	    evaluate_and_save(f"ce_deberta_{model_tag}", y_true, y_pred, y_prob, args.output_dir)
228	
229	
230	if __name__ == "__main__":
231	    main()
232	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "005d31d7-e225-4514-a1cd-bd4e2a563bc4"
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
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Reading artifacts/baselines.py",
  "usage": {
    "total_tokens": 29875,
    "tool_uses": 11,
    "duration_ms": 18498
  },
  "last_tool_name": "Read",
  "uuid": "062c1282-d98c-47ce-ab20-3cf1e15c15ca",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01CCKxJVqWpRnuVKBgZHLsbK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/baselines.py",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "f2cb3367-9807-444b-aabf-8242d02c7be4",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012SHNDd17nibtr95S4pT4F7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 3526,
      "cache_read_input_tokens": 26244,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3526,
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

_source line 40 · 2026-05-14T23:01:14.639Z_

<details><summary>↩ Tool result · `toolu_01CCKxJVqWpRnuVKBgZHLsbK`</summary>

```text
1	"""
2	Baseline battery for recursive generation depth estimation.
3	
4	Baselines:
5	  1. PPLRegressionBaseline  — OLS regression on mean_ppl (single) or all 19 features (multi)
6	  2. CEClassificationBaseline — MLP with cross-entropy loss (DCOL ablation, no contrastive loss)
7	  3. CORALBaseline — Ordinal regression with K-1 binary classifiers (Cao et al., 2020)
8	  4. DivEyeBaseline — Surprisal diversity features + XGBoost (Basani & Chen, TMLR 2026)
9	
10	Usage:
11	  python src/baselines.py --method ppl_reg --features_path data/features_all.jsonl
12	  python src/baselines.py --method ce_mlp  --features_path data/features_all.jsonl --epochs 50
13	  python src/baselines.py --method coral   --features_path data/features_all.jsonl --epochs 50
14	  python src/baselines.py --method diveye  --features_path data/features_all.jsonl
15	  python src/baselines.py --method all     --features_path data/features_all.jsonl --epochs 50
16	"""
17	
18	import argparse
19	import json
20	import os
21	import sys
22	import numpy as np
23	from collections import Counter
24	
25	import torch
26	import torch.nn as nn
27	import torch.optim as optim
28	from torch.utils.data import DataLoader, TensorDataset
29	
30	from sklearn.linear_model import LinearRegression
31	from sklearn.preprocessing import StandardScaler
32	from sklearn.model_selection import train_test_split
33	from sklearn.metrics import (
34	    accuracy_score, confusion_matrix, classification_report, roc_auc_score,
35	)
36	
37	# ── Feature schema (must match extract_features.py / dcol_dataset.py) ──
38	
39	FEATURE_NAMES = [
40	    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
41	    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
42	    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
43	    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
44	    "rep_2gram", "rep_3gram", "rep_4gram",
45	]
46	NUM_FEATURES = len(FEATURE_NAMES)
47	NUM_DEPTHS = 4
48	DEPTH_LABELS = list(range(NUM_DEPTHS))
49	
50	# ── Data loading ──
51	
52	def load_features(path):
53	    """Load JSONL features file → (X [n, 19], y [n])."""
54	    records = []
55	    with open(path) as f:
56	        for line in f:
57	            line = line.strip()
58	            if line:
59	                records.append(json.loads(line))
60	    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)
61	    y = np.array([r["depth"] for r in records], dtype=np.int64)
62	    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
63	    return X, y
64	
65	
66	def prepare_splits(X, y, test_size=0.15, val_size=0.15, seed=42):
67	    idx = np.arange(len(y))
68	    train_val_idx, test_idx = train_test_split(
69	        idx, test_size=test_size, stratify=y, random_state=seed
70	    )
71	    rel_val = val_size / (1 - test_size)
72	    train_idx, val_idx = train_test_split(
73	        train_val_idx, test_size=rel_val,
74	        stratify=y[train_val_idx], random_state=seed
75	    )
76	    return (
77	        X[train_idx], y[train_idx],
78	        X[val_idx], y[val_idx],
79	        X[test_idx], y[test_idx],
80	    )
81	
82	# ── Evaluation metrics ──
83	
84	def pairwise_auc(y_true, y_prob, d1, d2):
85	    mask = np.isin(y_true, [d1, d2])
86	    if mask.sum() < 2:
87	        return None
88	    yt = (y_true[mask] == d2).astype(int)
89	    if len(np.unique(yt)) < 2:
90	        return None
91	    yp = y_prob[mask, d2]
92	    return float(roc_auc_score(yt, yp))
93	
94	
95	def compute_all_pairwise_auc(y_true, y_prob):
96	    result = {}
97	    for i, d1 in enumerate(DEPTH_LABELS):
98	        for d2 in DEPTH_LABELS[i + 1:]:
99	            auc = pairwise_auc(y_true, y_prob, d1, d2)
100	            result[f"d{d1}_vs_d{d2}"] = round(auc, 4) if auc is not None else None
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "15a42dc2-4f24-439a-b186-943c76ab5428"
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
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Reading artifacts/dcol_feature_mlp.py",
  "usage": {
    "total_tokens": 31517,
    "tool_uses": 12,
    "duration_ms": 20795
  },
  "last_tool_name": "Read",
  "uuid": "f30c0d6c-f0ce-4ba4-b2e8-7086fe391b0c",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_01EHo4tiEZ9jTm3yC5vmtxjh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dcol_feature_mlp.py",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "9ac871de-bfee-4e8e-8d99-8ae495996f87",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013FPY7rJA5hyHqby4ZaBNnn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1634,
      "cache_read_input_tokens": 29770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1634,
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

_source line 43 · 2026-05-14T23:01:16.961Z_

<details><summary>↩ Tool result · `toolu_01EHo4tiEZ9jTm3yC5vmtxjh`</summary>

```text
1	"""
2	Feature-based DCOL (Depth Contrastive Ordinal Learning) training framework.
3	
4	Input:  JSONL/CSV files with 19-dim statistical features + depth label (0-3)
5	Output: Trained MLP checkpoint, evaluation metrics, embedding visualizations
6	
7	Architecture:
8	  Encoder:     MLP  19 -> hidden_dim(128) -> 64,  ReLU + BatchNorm + Dropout
9	  Proj head:   64 -> proj_dim(32),  L2-normalized (contrastive space)
10	  Class head:  64 -> 4  (depth classification)
11	
12	Loss (Eq.1 — Dream D002 hard constraint):
13	  L_DCOL = L_attractive + L_repulsive + lambda * L_CE
14	
15	Dependencies: torch, sklearn, numpy, pandas, matplotlib
16	"""
17	
18	import argparse
19	import json
20	import logging
21	import os
22	import sys
23	import time
24	from collections import defaultdict
25	from pathlib import Path
26	
27	import numpy as np
28	import pandas as pd
29	import torch
30	import torch.nn as nn
31	import torch.nn.functional as F
32	from torch.utils.data import Dataset, DataLoader, Sampler
33	from sklearn.model_selection import train_test_split
34	from sklearn.metrics import (
35	    accuracy_score, confusion_matrix, classification_report, roc_auc_score,
36	)
37	from sklearn.preprocessing import StandardScaler
38	
39	logger = logging.getLogger(__name__)
40	
41	# ── Feature schema (matches features_all.jsonl from MVP extraction) ──────────
42	FEATURE_NAMES = [
43	    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
44	    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
45	    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
46	    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
47	    "rep_2gram", "rep_3gram", "rep_4gram",
48	]
49	NUM_FEATURES = len(FEATURE_NAMES)  # 19
50	
51	
52	# ═══════════════════════════════════════════════════════════════════════════════
53	# Data loading
54	# ═══════════════════════════════════════════════════════════════════════════════
55	
56	def load_features_file(path: str) -> pd.DataFrame:
57	    """Load a single features file (JSONL or CSV). Returns DataFrame with feature columns + 'depth'."""
58	    path = str(path)
59	    if path.endswith(".csv"):
60	        df = pd.read_csv(path)
61	    else:
62	        records = []
63	        with open(path) as f:
64	            for line in f:
65	                line = line.strip()
66	                if line:
67	                    records.append(json.loads(line))
68	        df = pd.DataFrame(records)
69	
70	    required = set(FEATURE_NAMES) | {"depth"}
71	    missing = required - set(df.columns)
72	    if missing:
73	        raise ValueError(f"Missing columns in {path}: {missing}")
74	    return df[FEATURE_NAMES + ["depth"]]
75	
76	
77	def load_data(data_dirs: list[str]) -> pd.DataFrame:
78	    """Load and concatenate feature files from multiple paths."""
79	    frames = []
80	    for p in data_dirs:
81	        df = load_features_file(p)
82	        logger.info(f"  Loaded {len(df)} samples from {p}")
83	        frames.append(df)
84	    combined = pd.concat(frames, ignore_index=True)
85	    logger.info(f"Total: {len(combined)} samples, depth distribution: "
86	                f"{dict(combined['depth'].value_counts().sort_index())}")
87	    return combined
88	
89	
90	# ═══════════════════════════════════════════════════════════════════════════════
91	# Dataset & Sampler
92	# ═══════════════════════════════════════════════════════════════════════════════
93	
94	class FeatureDataset(Dataset):
95	    def __init__(self, features: np.ndarray, labels: np.ndarray):
96	        self.features = torch.tensor(features, dtype=torch.float32)
97	        self.labels = torch.tensor(labels, dtype=torch.long)
98	        self.depth_to_indices = defaultdict(list)
99	        for i, y in enumerate(labels):
100	            self.depth_to_indices[int(y)].append(i)
101	
102	    def __len__(self):
103	        return len(self.labels)
104	
105	    def __getitem__(self, idx):
106	        return self.features[idx], self.labels[idx]
107	
108	
109	class BalancedDepthSampler(Sampler):
110	    """Each batch has equal samples per depth for valid contrastive pairs."""
111	
112	    def __init__(self, dataset: FeatureDataset, batch_size: int):
113	        self.dataset = dataset
114	        self.num_depths = len(dataset.depth_to_indices)
115	        self.per_depth = max(1, batch_size // self.num_depths)
116	        self.batch_size = self.per_depth * self.num_depths
117	
118	    def __iter__(self):
119	        depth_indices = {
120	            d: np.random.permutation(idx).tolist()
121	            for d, idx in self.dataset.depth_to_indices.items()
122	        }
123	        n_batches = min(len(v) // self.per_depth for v in depth_indices.values())
124	        for b in range(n_batches):
125	            batch = []
126	            for d in sorted(depth_indices):
127	                batch.extend(depth_indices[d][b * self.per_depth:(b + 1) * self.per_depth])
128	            yield batch
129	
130	    def __len__(self):
131	        return min(len(v) // self.per_depth for v in self.dataset.depth_to_indices.values())
132	
133	
134	# ═══════════════════════════════════════════════════════════════════════════════
135	# Model
136	# ═══════════════════════════════════════════════════════════════════════════════
137	
138	class DCOLFeatureModel(nn.Module):
139	    """
140	    Feature-based DCOL model.
141	
142	    Forward pass:
143	      x (B, 19) -> encoder -> h (B, 64) -> proj_head -> z (B, proj_dim)  [contrastive]
144	                                          -> cls_head  -> logits (B, 4)   [classification]
145	
146	    Training uses both z (contrastive loss) and logits (CE loss).
147	    Inference uses only logits.
148	    """
149	
150	    def __init__(self, input_dim=19, hidden_dim=128, embed_dim=64, proj_dim=32, num_classes=4, dropout=0.3):
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "07947df9-0124-4b0b-a760-b88809ca8551"
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
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Reading memory.md",
  "usage": {
    "total_tokens": 33655,
    "tool_uses": 13,
    "duration_ms": 22795
  },
  "last_tool_name": "Read",
  "uuid": "4489b17a-28a4-44ee-8c73-72fd21bb45fb",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Read · `toolu_01F17aDm3QaVvy9ws3yrMPxC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "44c72df5-dece-44d3-88a6-ca5f98d78f78",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ae7gNZRYFRznqm9evsUaED",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 2130,
      "cache_read_input_tokens": 31404,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2130,
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

_source line 46 · 2026-05-14T23:01:18.934Z_

<details><summary>↩ Tool result · `toolu_01F17aDm3QaVvy9ws3yrMPxC`</summary>

```text
1	# Memory — recursive_gen_depth_est
2	
3	## 经验教训
4	
5	### [2026-05-14] Cron false failure 根因
6	Worker 绕过 `submit_training_job`（ToolSearch 找不到该工具），用 raw ssh_execute 创建 tmux session，导致无 sentinel 文件。Cron handler 连续检测 "process dead, no sentinel, no W&B" → 误标 failed。
7	**修复**：所有 pipeline 脚本已添加 EXIT trap（通过 `AML_EXP_ID` 环境变量写 sentinel 到 `/tmp/agent-ml-exit/{exp_id}.exit`）。spawn_worker 时确保 tool_groups 包含 submit_training_job 所需工具，或在 tools 中显式传入。
8	
9	### [2026-05-14] GPT-2 XL 表现最强的可能原因
10	GPT-2 XL nucleus 83.3% >> Pythia 78.2% / OLMo 78.8%。Worker 分析：跨模型 surprisal（Pythia 参考模型评估 GPT-2 XL 文本）放大了递归退化信号 + GPT-2 XL 代码污染极低（<1.5%）。这对 paper framing 有影响——需要讨论 cross-model evaluation 是否引入了 bias。
11	
12	### [2026-05-14] DivEye 引用验证 (Reviewer 引用审计)
13	- **结论: 真实论文 ✓**
14	- 论文: "Diversity Boosts AI-Generated Text Detection", Advik Raj Basani & Pin-Yu Chen
15	- 发表: TMLR 2026 (confirmed via OpenReview + GitHub tag)
16	- arXiv: https://arxiv.org/abs/2509.18880
17	- OpenReview: https://openreview.net/forum?id=DNgsOhGZBI
18	- GitHub: https://github.com/IBM/diveye (存在，CC BY-NC-SA 4.0，Python 实现)
19	- HuggingFace Space: https://huggingface.co/spaces/pinyuchen/Diveye_AI_text_detector
20	- 官网: https://diveye.vercel.app/
21	- 也在 ICML 2025 DIG-BUG workshop 发表 (CEUR-WS Vol-4038)
22	- **注意**: baselines.py 中曾误写为 "ICLR 2026"，已修正为 "TMLR 2026"
23	- **行动: 保留引用，无需替换**
24	
25	### [2026-05-14] 3×3 矩阵排队优化
26	同模型不同 decoding strategy 的 pipeline 可复用 depth-0 LoRA adapter（Step 1 与 decoding 无关）。通过 symlink nucleus adapter 跳过重复训练，节省 ~4.5min/run。
27	
28	### [2026-05-14] DCOL 训练踩坑
29	- v1 (dcol_deberta_001): margin_lr=1e-3 太高（与 base lr 2e-5 差 50x），导致 embedding collapse。CL loss 从 0.46 塌缩到 0.03，但 4-class acc 仅 31.5%。
30	- v2 (dcol_deberta_002): 修复参数（margin_lr→1e-4, L2 norm, cl_weight→1.0），但因僵尸进程（PID 193689 占 57GB）导致 OOM。
31	- **教训**: kill_job 只杀父进程，必须手动确认所有子进程也死了。
32	
33	## 解码策略对深度信号强度的影响 (2026-05-14, updated)
34	
35	### 信号强度不是单调排序——是模型依赖的
36	
37	早期 Pythia-only 数据暗示 nucleus > temp > top-k，但 GPT-2 XL 数据推翻了这一简单排序：
38	
39	**Pythia-1.4B**: nucleus (78.2%) > temp (76.3%, -1.9pp) > top-k (69.6%, -8.6pp)
40	**GPT-2 XL**: temp (85.4%) > nucleus (83.3%) > top-k (待验证)
41	**OLMo-1B**: nucleus (78.8%), temp (运行中), top-k (待排)
42	
43	**关键发现**: 温度采样对深度信号的影响方向是**模型依赖的**——Pythia 降 1.9pp，GPT-2 XL 反升 2.1pp。可能原因：GPT-2 XL 在 τ=0.9 下递归训练产生的分布偏移恰好放大了 Pythia 参考模型能捕捉到的 surprisal 信号。
44	
45	**论文 framing 启示**:
46	- 不能说 "strategy-agnostic"，需要用 "strategy-dependent magnitude with consistent signal presence"
47	- Top-k 一致性地削弱信号（Pythia -8.6pp），硬截断可能是主要机制
48	- Temp/nucleus 之间的差异是模型特异的，这本身是一个有趣的发现，值得在 Discussion 中展开
49	
50	## 跨实验 Feature Importance 一致性分析 (2026-05-14, updated)
51	
52	6 实验（3 模型 × 2-3 策略）的 19 特征 importance 全量对比。详细报告：`artifacts/feature_importance_consistency_analysis.md`
53	
54	### Universal Core 4 特征（6/6 实验 top-5）
55	1. **var_surprisal** — rank 1-4, importance 0.121-0.208, CV=0.17
56	2. **p90_ppl** — rank 1-2, importance 0.135-0.263, CV=0.25
57	3. **mean_surprisal** — rank 2-4, importance 0.070-0.148, CV=0.29
58	4. **p75_ppl** — rank 3-5, importance 0.061-0.146, CV=0.36
59	
60	Core 4 累积占总 importance 的 44-68%。
61	
62	### Spearman Rank Correlation
63	- 同模型跨策略平均 ρ = 0.859（Pythia t09 与 k50 完全一致 ρ=1.000）
64	- 同策略跨模型（nucleus）平均 ρ = 0.801
65	- 全部 15 对平均 ρ = 0.79
66	- **跨策略一致性 > 跨模型一致性**，但两者均显著
67	
68	### 特征层级
69	- Tier 1 (Core): var_surprisal, p90_ppl — 始终 top-2
70	- Tier 2 (Strong): mean_surprisal, p75_ppl — 始终 top-5
71	- Tier 3 (Moderate): mean_ppl, type_token_ratio, p50_ppl 等 — 有模型依赖
72	- Tier 4 (Weak): skewness/kurtosis_ppl, n-gram entropy, repetition — 低且不稳定
73	- Tier 5 (Null): var_ppl — 所有实验 rank 19
74	
75	### 关键异常
76	- mean_ppl 在 GPT2XL_t09 中 importance ≈ 0（rank 18），但在 Pythia 三实验中稳定 rank 3。共线性导致 tree 模型的 importance 重分配。
77	- 所有 surprise/perplexity 特征 >> 所有 lexical diversity 特征（top-4 全是 surprise-based）
78	
79	### [2026-05-14] Reviewer 指出: Feature Importance Ranking 不稳定
80	**发现**: GPT-2 XL 跨策略 feature importance **ranking** 不稳定——var_surprisal 从 nucleus 的 rank 1 降到 temp09 的 rank 4。但 top feature **SET** (var_surprisal, p90_ppl, mean_surprisal, p75_ppl) 在所有实验中保持一致。
81	**论文 claim 修正**: 必须用 "top feature **set** stable across models and strategies" 而非 "ranking stable"。Ranking 波动是 RF importance 的已知问题（共线性特征间 importance 重分配），不影响 set-level 结论。
82	**行动**: 写论文时避免引用 Spearman rank correlation 作为 stability 的唯一证据，补充 set overlap / Jaccard similarity 指标。
83	
84	### 论文论据
85	这一致性是论文的强论据：递归生成深度在文本中留下的统计指纹是 **model-general** 和 **strategy-robust** 的，核心信号（surprise variance + extreme perplexity）不依赖于特定模型架构或解码配置。
86	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "7a6b770a-a021-46d3-a7b6-4deab5c804ad"
}
```

</details>

---


### System

_source line 47_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 36395,
    "tool_uses": 14,
    "duration_ms": 25253
  },
  "last_tool_name": "Bash",
  "uuid": "a4c23e52-125e-434d-9120-88426a207091",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Bash · `toolu_011EsGjqKZaLFZoAezeyHaYp`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est -name \"features*.jsonl\" -o -name \"depth_*.jsonl\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "fc5d28ad-5ca0-4327-80c6-5d11b498e789",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WDo3wTscPFzdia1PFUGMM5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 2738,
      "cache_read_input_tokens": 33534,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2738,
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

_source line 49 · 2026-05-14T23:01:21.493Z_

<details><summary>↩ Tool result · `toolu_011EsGjqKZaLFZoAezeyHaYp`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "19492131-f78f-45d7-ac8a-651353df4530"
}
```

</details>

---


### System

_source line 50_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Reading docs/IDEA_BRIEF.md",
  "usage": {
    "total_tokens": 36541,
    "tool_uses": 15,
    "duration_ms": 26851
  },
  "last_tool_name": "Read",
  "uuid": "a8c79c8c-f22d-4cd3-b4b4-827546aca2d4",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01GPFs9AxSVp54N6TtMxNkBa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "019fff80-8702-472d-9211-b3a17349f1ab",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013qGLg6QV6XATh68QtYkpuf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 145,
      "cache_read_input_tokens": 36272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 145,
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

_source line 52 · 2026-05-14T23:01:22.999Z_

<details><summary>↩ Tool result · `toolu_01GPFs9AxSVp54N6TtMxNkBa`</summary>

```text
1	# Idea Brief: How Deep Is Your Data? Estimating Recursive Generation Depth for Synthetic Text Quality Scoring
2	
3	
4	- **Idea ID**: `idea_008`
5	- **Created**: 2026-05-14
6	- **Approved**: 2026-05-14
7	- **Source**: foreign:be-idea-gen-0509-10
8	- **Level**: top-tier
9	- **Target Venues**: EMNLP 2026 (ARR submission deadline: May 25, 2026 — directly aligned with special theme on data contamination and feedback loops), AACL-IJCNLP 2026 (ARR submission deadline: May 25, 2026 — same ARR cycle, binding venue choice at submission), AAAI 2027 (abstract: July 25, full paper: August 1, 2026), CIKM 2026 (abstract: May 16, full paper: May 23, 2026)
10	
11	## Seed Topic
12	
13	Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Machine Learning for NLP / Resources and Evaluation. Aligns with EMNLP 2026 special theme "New Missions for NLP Research" which explicitly calls for work on data contamination, synthetic data feedback loops, and data governance.
14	
15	Direction: Synthetic data quality, model collapse prevention, contamination detection. In-scope: synthetic data verification/filtering methods, detecting training data contamination in benchmarks, methods to break recursive data feedback loops, data mixing strategies that prevent quality degradation, principled synthetic data generation with quality guarantees.
16	
17	Contribution type: METHOD ONLY. Must propose a concrete detection algorithm, filtering pipeline, or training recipe — not just an observation about model collapse. Method + analysis OK.
18	
19	HARD CONSTRAINTS:
20	1. Compute: ≤200 H100-hours total. Model collapse experiments need multiple training iterations — budget for small models (1B-3B) across 3-5 generations.
21	2. Time: ≤16 days. Use small open models (Pythia, OLMo-1B, Qwen-0.5B/1.8B) for iterative collapse experiments.
22	3. Eval: perplexity degradation curves, downstream task quality (MMLU, HellaSwag), diversity metrics (self-BLEU, n-gram entropy), contamination detection accuracy.
23	
24	This is a hot EMNLP 2026 special theme area with relatively few established methods — high novelty potential.
25	
26	Tag: direction=data_governance, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].
27	
28	## Core Problem
29	
30	Current synthetic text detection is binary (real vs. synthetic), but the practical value of synthetic training data depends critically on its recursive generation depth — how many model-to-model training cycles it has undergone. First-generation synthetic data can improve training, while deeply recursive content drives distribution collapse. No existing method estimates this ordinal depth from text alone, leaving a critical gap for data curation pipelines operating on web-scraped corpora of unknown provenance.
31	
32	## Opportunity / Why Now
33	
34	By early 2026, over 60% of data used in AI projects is synthetically generated (Gartner), creating uncontrolled recursive feedback loops in web-scraped training data. Existing detectors answer 'is this synthetic?' (LOKI, RADAR, Binoculars, DivEye) or 'how much was AI-edited?' (EditLens, ICLR 2026), but not 'how many recursive training cycles has this text undergone?' — a critical distinction since 1st-gen rephrased data improves training while 3rd+ gen text drives collapse (Nature 2024). Meanwhile, the 'Model Collapse Does Not Mean What You Think' position paper (NeurIPS 2025) argues that catastrophic collapse requires unrealistic assumptions, but acknowledges that diversity collapse and quality degradation are real concerns under practical conditions. This reframing strengthens rather than weakens our motivation: even without catastrophic collapse, knowing generation depth enables principled synthetic data quality scoring for curation pipelines — retaining high-quality shallow-generation content while filtering deeply recursive text. This directly addresses EMNLP 2026's special theme on data contamination and feedback loops.
35	
36	## Landscape (SOTA & Limitations)
37	
38	Synthetic text detection is a mature binary classification task: LOKI (ICLR 2025 Spotlight) benchmarks detection across modalities; DivEye (TMLR 2026) achieves SOTA zero-shot detection via surprisal variability features; five methods are considered reliable as of 2026 (Min-K%, ConStat, time-based partition, canary GUID, guided completion). EditLens (ICLR 2026) is the first detector to estimate the continuous extent of AI editing rather than binary classification, but addresses single-pass editing, not recursive generation. For model collapse, Drayson et al. (EMNLP 2025) analyzed text characteristics across 100 generations of GPT-2 and SmolLM2 under six decoding strategies, finding non-monotonic degradation patterns — notably that pure sampling increases perplexity variance rather than converging, while temperature sampling shows 70% diversity collapse. They used binary detection with importance resampling to prevent collapse but did not attempt depth classification. The 'Recursive Training Loops' paper (EMNLP 2025 Oral) showed lexical diversity amplifies distribution shift while semantic diversity mitigates it, but assumed depth is known a priori. For ordinal classification methods, CLOC (CVPR 2025) introduced multi-margin N-pair contrastive learning with learnable margins for ordinal tasks, and GoR (ICLR 2026) reformulated ordinal regression as sequential token generation. Neither has been applied to text depth estimation. The key gap: no existing work treats recursive generation depth as an estimable quantity from text alone — all analysis assumes depth is known from controlled experiments.
39	
40	## Proposed Approach
41	
42	We formalize the task of ordinal generation depth estimation: given a text sample, predict its recursive generation depth d ∈ {0, 1, 2, 3, 4, 5} where 0 = human-authored and 1–5 = successive model-to-model training cycles. Our method has three components:
43	
44	**1. Multi-Generational Benchmark Construction.** We construct depth-labeled corpora by iteratively fine-tuning three 1–2B parameter open-source LLMs — Pythia-1.4B, OLMo-1B, and Qwen2.5-1.8B — on their own outputs for 5 generations using LoRA, across three decoding strategies (nucleus p=0.95, temperature τ=0.9, top-k k=50). Each generation fine-tunes a fresh base model on the previous generation's output, producing 9 independent recursive chains (3 models × 3 strategies) with ~30K samples per generation per chain. This yields ~540K depth-labeled samples total.
45	
46	**2. Depth-Contrastive Ordinal Learning (DCOL).** We adapt CLOC's multi-margin N-pair contrastive loss (CVPR 2025) to text, using a DeBERTa-v3-large encoder to learn depth-aware representations. The key insight: distances between adjacent generation depths are non-uniform (the gap between human and gen-1 text is far larger than between gen-3 and gen-4), so fixed-margin approaches like CORAL underperform. DCOL uses learnable margins between each pair of adjacent depths, preserving ordinal structure while allowing the embedding space to capture the actual geometry of degradation. We augment learned representations with interpretable statistical features — DivEye-style surprisal variability (variance/entropy of token-level surprisal under a frozen reference model), Min-K%-style log-probability percentiles, and lexical diversity metrics (type-token ratio, hapax ratio, n-gram entropy) — fused via a lightweight MLP head for final ordinal prediction.
47	
48	**3. Cross-Strategy Feature Analysis.** We systematically study which features degrade monotonically with depth across all decoding strategies vs. which are strategy-dependent, directly addressing Drayson et al.'s finding of non-monotonic patterns. Rather than assuming monotonicity, we empirically identify robust depth indicators and show DCOL's contrastive representations learn strategy-invariant depth signals.
49	
50	Evaluation: (a) leave-one-model-family-out generalization (train on 2 families, test on 3rd); (b) leave-one-strategy-out robustness; (c) mixed-provenance evaluation on synthetic documents constructed from paragraphs sampled from different generation depths, inspired by PAN 2025/2026 mixed authorship tasks; (d) baselines including repurposed binary detectors (Binoculars, DivEye), perplexity regression, CORAL ordinal regression, EditLens (continuous scoring), and zero-shot LLM prompting.
51	
52	## Resource Estimate
53	
54	- **auto_research**: {'claude_api_cost': '$200-400 (~2000-4000 turns)', 'estimated_gpu_cost': '$360-400 at ~$2/h H100 spot pricing', 'gpu_hours': '~180-200h H100 (explores exhaustive feature combinations, additional decoding strategies, hyperparameter sweeps for contrastive loss margins)', 'gpu_utilization': '80-90% — agent pipelines fine-tuning immediately after generation, runs feature extraction on CPU in parallel', 'risk_note': 'May over-explore contrastive loss hyperparameters while under-investing in qualitative analysis of cross-model generalization failures', 'speed_bottleneck': 'Serial data generation pipeline — each generation depends on the previous, creating ~5h critical path per chain; additional GPUs only parallelize across the 9 chains', 'team': '0 (initial setup ~1.5h)', 'timeline': '7-10 days with 4 H100s (serial floor: ~25h wall time for deepest 5-gen chain)'}
55	- **human_in_loop**: {'claude_api_cost': '$100-200 (~1000-2000 turns)', 'estimated_gpu_cost': '$260-320 at ~$2/h H100 spot pricing', 'gpu_hours': '~130-160h H100 (agent explores additional feature combinations and cross-strategy ablations)', 'gpu_utilization': '50-65% — agent pipelines generation steps and queues classifier training with reduced inter-step idle time', 'risk_note': 'Serial dependency in 5-generation chains limits parallelization — each gen requires previous gen to complete and model to be fine-tuned on it', 'team': '1 researcher, ~30min/day reviewing agent proposals', 'timeline': '10-12 days'}
56	- **manual**: {'estimated_gpu_cost': '$200-300 at ~$2/h H100 spot pricing', 'gpu_hours': '~100-130h H100 (data pipeline: 3 models × 3 strategies × 5 gens, ~45h LoRA fine-tuning + generation; DCOL training + ablations ~40h; feature extraction + baselines ~20h)', 'gpu_utilization': '20-30% — serial dependency within each generation chain creates ~1h idle gaps between steps for analysis and debugging', 'team': '1-2 researchers', 'timeline': '14 days (Days 1-4: data pipeline; Days 5-8: DCOL training + feature analysis; Days 9-14: evaluation, ablations, writing)'}
57	
58	## Key References
59	
60	- LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models (ICLR 2025 Spotlight)
61	- AI models collapse when trained on recursively generated data (Nature 2024)
62	- Machine-generated text detection prevents language model collapse (Drayson et al., EMNLP 2025) — analyzes text characteristics across 100 generations under 6 decoding strategies; non-monotonic degradation patterns; binary detection + importance resampling
63	- Recursive Training Loops in LLMs: How training data properties modulate distribution shift in generated data? (EMNLP 2025 Oral)
64	- Position: Model Collapse Does Not Mean What You Think (NeurIPS 2025 Position Track, arXiv 2503.03150) — argues collapse narrative is oversimplified; real risks are diversity loss under practical conditions
65	- Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data (ICLR 2025)
66	- EditLens: Quantifying the Extent of AI Editing in Text (ICLR 2026) — first continuous AI editing extent score; addresses single-pass editing, not recursive depth
67	- Diversity Boosts AI-Generated Text Detection (DivEye, TMLR 2026) — surprisal variability features for zero-shot detection
68	- CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss (CVPR 2025) — learnable margins for ordinal representation learning
69	- Generative Ordinal Regression (GoR, ICLR 2026) — reformulates ordinal regression as sequential token generation
70	- ConStat: Performance-Based Contamination Detection in Large Language Models (NeurIPS 2024)
71	- Detecting Pretraining Data from Large Language Models (Min-K%, ICLR 2024)
72	- PAN 2025/2026 Shared Tasks on Generative AI Detection in mixed and obfuscated authorship scenarios
73	
74	## Reviewer Evaluation
75	
76	**Scores**:
77	  - clarity: **{'rationale': 'The proposal is well-structured with clear three-component architecture (benchmark construction, DCOL method, cross-strategy analysis). The evaluation plan is comprehensive with leave-one-out generalization, cross-strategy robustness, mixed-provenance documents, and multiple baselines (Binoculars, DivEye, CORAL, EditLens, zero-shot LLM). The motivation chain — from binary detection to ordinal depth estimation for data curation — is logically sound. The connection to EMNLP 2026 special theme is explicit and genuine.', 'score': 4}**/5
78	  - feasibility: **{'rationale': 'The revised proposal correctly uses user-specified small models (Pythia-1.4B, OLMo-1B, Qwen2.5-1.8B) with LoRA, which fits comfortably on a single H100 with <2GB overhead per 1B params. Manual estimate of ~100-130h H100 is within the ≤200h cap. 3 models × 3 strategies × 5 generations = 45 LoRA fine-tuning runs is realistic for ~45h. DeBERTa-v3-large training on 540K samples should take ~5-10h. The 14-day manual timeline is tight but achievable — serial dependency in generation chains (each gen requires the previous) is the real bottleneck, but parallelizing across the 9 chains (3 models × 3 strategies) mitigates this. All models and datasets are open-source and available on HuggingFace.', 'score': 4}**/5
79	  - impact: **{'rationale': "Ordinal depth estimation fills a real practical need: web-scraped training corpora increasingly contain multi-generational synthetic content, and knowing generation depth enables principled data curation (retain shallow-gen, filter deep-gen). This directly addresses the synthetic data feedback loop problem highlighted by EMNLP 2026's special theme. The benchmark itself (540K depth-labeled samples across 3 model families × 3 strategies × 5 generations) would be a valuable community resource. The practical framing — data curation rather than collapse prevention — correctly positions the work given the NeurIPS 2025 position paper arguing collapse is overstated.", 'score': 4}**/5
80	  - novelty: **{'rationale': "The core idea — ordinal generation depth estimation from text alone — is genuinely novel. Extensive searching confirms no existing work treats recursive generation depth as an estimable ordinal quantity. Drayson et al. (EMNLP 2025) characterizes degradation across 100 generations but never attempts depth classification. The 'Characterizing Model Collapse' paper (arXiv 2410.12341) measures collapse from next-token distributions but explicitly does NOT classify depth. EditLens (ICLR 2026) estimates single-pass AI editing extent but not recursive depth. DCOL — adapting CLOC's multi-margin contrastive loss to text — is a reasonable but not groundbreaking methodological contribution; the novelty lies primarily in the problem formalization and benchmark construction.", 'score': 4}**/5
81	
82	## Human Review Note
83	
84	## Agent 审核结果（完整三阶段 pipeline）
85	
86	**Verdict**: PASS
87	
88	**入口三重共识 (X)**: 26.0%
89	**终审自评 (Y)**: 32.0%
90	**出口三重共识 (Z)**: 35.0%
91	**Z 区间**: [29.0%, 39.0%]
92	**真实提升 (Z-X)**: +9.0 pp
93	**幻觉幅度 (Y-Z)**: -3.0 pp
94	**出口一致性**: 高（std=2.1% < 3%）
95	**出口三次评估**: [35.0, 33.0, 38.0]
96	
97	### 优化方案 / 拒绝详情
98	【优化方案】
99	
100	1. **[Introduction / 整体 Framing] — 从 "AI text detection" 赛道重新定位为 "understanding and mitigating feedback loops" 赛道** — 命中 Significance + Relevance to Venue
101	   原始 proposal 末尾仅一句"directly addressing EMNLP 2026's special theme on data contamination and feedback loops"，属于贴标签式提法。优化后将 depth=k 显式等价于 k 次 model→data→model 反馈循环，整篇论文的叙事锚定为对 special theme 的直接回应。同时增加 empirical evidence 段落：引用 Common Crawl 中 AI 内容比例趋势数据 + 主流训练 pipeline（GPT/Llama/Qwen）均取用 CC 的产业事实 → 下一代模型训练数据已包含 depth-1 内容 → 1-2 个 cycle 后 depth ≥ 2 不可忽略的 temporal projection 论证，将框架定位为"前瞻性早期预警"。
102	
103	2. **[Contribution 结构] — 从单一"方法+实验"结构重组为三线并行贡献，且明确主次层级** — 命中 Contribution Clarity + Novelty
104	   原始 proposal 是一段式叙述，贡献模糊。优化后拆分为：
105	   - **Contribution 1 (Primary)**: Depth estimation 任务形式化 + DCOL 方法
106	   - **Contribution 2 (Primary)**: Depth Degradation Atlas + Effective Discriminable Depth (EDD) 系统测量
107	   - **Contribution 3 (Proof-of-Concept)**: Depth-graduated curation 下游验证
108	   关键变化：Contribution 3 明确降级为 proof-of-concept（~1-1.5 页），避免 scope inflation；Atlas 和 EDD 测量不附属于方法，而是独立科学贡献。
109	
110	3. **[Contribution 2 / Atlas] — 新增 Effective Discriminable Depth (EDD) 作为独立科学指标** — 命中 Novelty + Significance
111	   原始 proposal 未提及 saturation boundary。优化后正式定义 EDD（相邻深度间特征差异低于噪声校准阈值的最小深度 k*），报告 per model × strategy × feature 的 EDD 矩阵。即使 EDD 较低（2-3），确定该边界本身即为核心发现——与 Shumailov et al. 的理论衰退曲线形成经验对偶。预判性声明：(a) 确定边界 = 科学贡献，(b) DCOL 的 learnable margins 自适应发现哪些 depth pairs 不可区分（margin→0），(c) 即使最终实用粒度为 3-class，ordinal 框架仍优于 unordered classification。
112	
113	4. **[Contribution 2 / Atlas] — 新增 monotonicity score 和 margin-feature alignment 分析** — 命中 Analysis Depth + Novelty
114	   原始 proposal 仅说"systematically analyzing which features degrade monotonically"。优化后：(a) 对每个 feature 提出正式的 monotonicity score 度量；(b) 直接回应 Drayson et al.——精确刻画非单调性出现/消失的条件；(c) 新增"margin-feature alignment"分析——量化 DCOL 学到的 margin 分布与 feature-level 退化几何的对应关系（scatter plot + rank correlation），作为独立 interpretability result 回应"contrastive learning 到底学到了什么"。
115	
116	5. **[Method / DCOL] — 显式处理 ordinal 假设与 non-monotonicity 的张力** — 命中 Technical Soundness
117	   原始 proposal 同时引用 Drayson et al. 的非单调性发现和使用 ordinal contrastive loss，但未解释这一内在矛盾。优化后在方法论中正面承认张力，论证 learnable non-uniform margins 作为 soft inductive bias 的合理性——即使局部非单调，全局趋势仍为 degradation，margins 可自适应压缩至接近 0 来适应非单调区域。通过消融实验（DCOL vs. CE loss vs. 固定等距 ordinal）实证验证。
118	
119	6. **[Method / DCOL] — 明确 text-specific 设计差异化，解决"CLOC adaptation"novelty 质疑** — 命中 Novelty
120	   原始 proposal 仅说"adapting multi-margin contrastive learning (CLOC) to text"，未说明文本域的独特挑战。优化后明确三个 text-specific modifications 及其各自动机：
121	   - **Strategy-aware margin conditioning**: decoding strategy 是一阶混淆因子（同一 depth 不同 strategy 的分布差异可能大于相邻 depth 的差异）
122	   - **Surprisal-augmented contrastive anchors**: 修改 contrastive loss 的相似度计算几何（非简单特征拼接），将 token-level 分布统计 grounding 到锚点表征
123	   - **Non-uniform learnable margins**: 适应文本生成退化的非等距语义几何（depth 0→1 跳变远大于 3→4 增量退化）
124	   同时将 novelty 重心从"DCOL 方法本身"转向"depth estimation framework（问题定义 + Atlas + curation paradigm）"，DCOL 是框架内的 strong method。
125	
126	7. **[Method / Inference] — 解决 strategy-unknown 推理问题** — 命中 Technical Soundness
127	   原始 proposal 未讨论推理时 decoding strategy 未知的情况。优化后明确：推理阶段对所有 strategy 预测做加权平均（marginalize over strategies）。增加 strategy-agnostic baseline 消融，证明 conditioning 即使在 strategy 未知时仍有益（因训练阶段帮助了表征学习）。
128	
129	8. **[Benchmark] — 增加生态效度探针，缩小 controlled→wild transfer gap** — 命中 Technical Soundness + Significance
130	   原始 proposal 仅有同模型递归链 + inference-time 混合段落评估。优化后增加：
131	   - **跨架构递归链**: Pythia→OLMo→Qwen 跨家族递归，模拟现实跨厂商污染
132	   - **混合比例梯度**: 80/20, 50/50, 20/80 的 depth-0 + depth-k 混合训练
133	   - **Wild-data calibration analysis**: 在 RedPajama/Dolma 上验证 DCOL depth score 与 feature-orthogonal quality proxies（AlignScore, perplexity）的相关性，确认 score 在 wild 数据上的语义有效性
134	   - **诚实定位**: 受控条件为 primary scientific setting，wild transfer 为 probed but future work
135	
136	9. **[Benchmark] — 增加 7B+ cross-scale probe 和 API-based 大模型验证** — 命中 Technical Soundness
137	   原始 proposal 仅用 1-2B 模型。优化后增加 Llama-3.1-8B 或 Qwen2.5-7B 的 3 代 depth 链作为 held-out test，补充 API-based 大模型 iterative rewriting 验证 + WildChat/LMSYS-Chat 定性特征趋势分析。将小模型 focus 定位为有意的实验控制设计。
138	
139	10. **[Feature Extraction] — 新增原创特征设计** — 命中 Novelty
140	    原始 proposal 的特征全部来自已有工作（DivEye, Drayson et al., Shumailov et al.）。优化后增加两组新特征：
141	    - Token-level perplexity 分布形状特征（skewness, kurtosis, entropy）——超越均值，捕获分布变化
142	    - Cross-depth n-gram overlap 衰减率——度量代际文本与原始人类文本的渐进偏离速度
143	
144	11. **[Baselines] — 从"相关工作列举"改为"task-appropriate baseline 矩阵"** — 命中 Experimental Rigor
145	    原始 proposal 仅将 LOKI/DivEye/EditLens 列为相关工作，未设计 depth estimation 的对照组。优化后构建 7 类 baselines：
146	    (1) Naïve depth proxies（现有 detector confidence 作 depth 相关性测试，含 meta-level 双面叙事价值）
147	    (2) Standard CE classification（消融 ordinal 结构）
148	    (3) Standard CORAL 固定等距 margins（消融 contrastive + learnable margins）
149	    (4) Feature-only ordinal regression（消融 learned representations）
150	    (5) 粒度消融: binary / 3-class / 6-class（验证 ordinal framing 的边际收益）
151	    (6) Strategy-agnostic DCOL（验证 strategy conditioning 价值）
152	    (7) Component ablation（逐一去除 surprisal anchors / learnable margins / strategy conditioning）
153	
154	12. **[Downstream Curation] — 严格化实验设计** — 命中 Technical Soundness
155	    原始 proposal 声称 graduated filtering 优于 binary filtering 但未给出实验细节。优化后：binary baseline 阈值在 held-out validation set 上扫描确保公平对比；graduated curation 使用预注册 1/k 线性衰减权重 + sensitivity analysis；所有比较含 bootstrap CI 和 paired significance test；实验逻辑链显式自洽（小模型训练 → 小模型数据过滤 → 小模型下游评估）。
156	
157	13. **[Downstream Curation] — 新增 depth vs. quality 直接验证** — 命中 Technical Soundness
158	    原始 proposal 隐含假设 depth 与 quality 单调递减但未验证。优化后增加 depth-quality 曲线分析（多维 quality proxy: perplexity, AlignScore, diversity, coherence），明确在哪些条件下单调性成立/破裂。若非单调，graduated filtering 适配为 depth-features→predicted quality→weight。
159	
160	14. **[Related Work] — 从零散提及扩展为全面结构化覆盖** — 命中 Related Work
161	    原始 proposal 仅提及 LOKI, DivEye, EditLens, Drayson et al. 和 Shumailov et al.。优化后增加：
162	    - Model collapse 核心文献（Shumailov Nature 2024, Alemohammad 2024, Dohmatob 2024）
163	    - Watermarking/provenance（Kirchenbauer 2023, SynthID, Christ 2024）——supply-side vs. demand-side 互补定位
164	    - Membership inference（Min-K%++）——membership ≠ ordinal depth
165	    - Data contamination detection（Shi et al. 2024）
166	    - Binary detection 最新工作（RAID, Binoculars）
167	    - Fine-grained provenance/attribution（Turingbench, data lineage tracking）——depth ≠ source identity
168	    - Data curation 文献（Surplexity, D4, DSIR）
169	    - Ordinal regression in NLP（sentiment scale, age estimation）——DCOL 的技术背景
170	
171	15. **[Scope / 写作策略] — 增加 appendix 策略和诚实定位** — 命中 Presentation + Soundness
172	    原始 proposal 无篇幅管理意识。优化后明确：Atlas 的大量 heatmaps 和 sensitivity analysis 进 appendix，正文放 key findings + representative visualizations；downstream curation 的完整 sensitivity 进 appendix；Scope section 诚实界定 controlled vs. wild 的边界。Benchmark 构建成本估算（~200-300 GPU-hours）和公开发布承诺消除 reviewer 对可复现性的疑虑。
173	
174	【主要风险】:
175	
176	1. **Novelty ceiling — "新问题 + adapted 方法"的天花板**: DCOL 的核心技术仍是 CLOC 的 domain adaptation，即使增加了 text-specific modifications 和 novelty 重心转移（框架 > 方法），novelty 敏感的审稿人仍可能评 "interesting empirical study with limited methodological contribution"。这是概率上界的主要限制因素。
177	
178	2. **实验结果不确定性**: EDD 位置、cross-scale 泛化效果、graduated filtering 收益幅度、margin-feature alignment 的实际对齐程度——任一 negative 结果都可能改变论文面貌。特别是如果 EDD=2 且 graduated filtering 收益统计不显著，reviewer 可能判定"binary detection 实际上已经够用"。
179	
180	【实施评估】:
181	- **计算资源**: Benchmark 构建约 200-300 GPU-hours（A100），含 3 models × 3 strategies × 5 depths 的 iterative fine-tuning + 跨架构链 + 混合训练变体。DCOL 训练（DeBERTa-v3-large）约 20-30 GPU-hours 含全部 ablation 变体。7B cross-scale probe 额外约 50-80 GPU-hours。Downstream curation 的 1B 模型微调约 30-50 GPU-hours。**总计约 300-460 GPU-hours**，单卡 A100 约 2-3 周，或 4 卡并行约 5-7 天。
182	- **数据需求**: C4 和 Wikipedia 子集（公开可得）各 50K 文档作为种子；RedPajama 或 Dolma 子集用于 wild validation（公开可得）；WildChat / LMSYS-Chat 用于大模型特征趋势分析（公开可得）。Common Crawl 子集用于 naturalistic validation。**所有数据集均公开可得，无数据获取障碍**。
183	- **人工介入**: 无需人工标注（depth labels 由受控生成过程自动产生）。论文写作和 Atlas 可视化需要研究者投入。**无额外人工标注成本**。
184	- **训练需求**: 需要模型训练。(1) Benchmark 构建需对 1-2B 模型做 ~45 次 fine-tuning（3×3×5）+ 跨架构链和混合训练变体 ~15-20 次。(2) DCOL 及其 ablation 变体约 10-15 次 DeBERTa-v3-large 训练。(3) 7B 模型 3 代 fine-tuning 约 3-6 次。(4) Downstream 1B 模型微调 4-5 次。**总训练 runs ~75-85 次，但单次 run 较短（1-2B 模型 fine-tuning 单卡 A100 约 2-4 小时/次）**。
185	- **新 Benchmark**: 是，需构建 multi-generational depth benchmark（540K+ depth-labeled samples）。这是论文的核心贡献之一。Benchmark 将公开发布供社区复用。
186	- **预估周期**: 从启动到可投稿约 **8-12 周**。Benchmark 构建约 2-3 周（含跨架构/混合训练变体），DCOL 开发和 ablation 约 2-3 周，Atlas 分析和可视化约 1-2 周，downstream curation 实验约 1 周，论文撰写约 2-3 周。关键路径在 benchmark 构建（最耗时且为后续实验前提）。
187	
188	
189	
190	## MVP Validation Results
191	
192	- **Date**: 2026-05-14
193	- **Hypothesis Supported**: Yes
194	
195	### Key Metrics
196	
197	4-class accuracy: 78.2% [76.9%, 79.4%] (threshold >40%) | Adjacent AUC: d0v1=0.998, d1v2=0.861, d2v3=0.801 (threshold >0.6) | MAE: 0.237 | Content-type control: 81.6% acc after filtering code (signal is perplexity-based, not domain confusion) | Training loss trend: 2.241→1.389→1.025 | GPU cost: 1.78 GPU·h
198	
199	### Summary
200	
201	MVP 验证递归生成深度可从文本统计特征区分。用 Pythia-1.4B + nucleus sampling 生成 4 个深度（0-3）各 5000 条文本，提取 19 维 perplexity/surprisal/词汇多样性特征，Random Forest 分类器 4-class accuracy 78.2%，远超 25% chance 和 40% 阈值。控制实验过滤代码样本后 accuracy 提升至 81.6%，排除域混淆。训练 loss 单调递减（2.24→1.39→1.03）直接反映分布窄化。Top 特征为 surprisal 方差和 perplexity 高百分位数。
202	
203	### Recommendation
204	
205	强烈建议进入 research phase。结果不仅通过 MVP gate，还已达到 research-phase gate 的 2/3 标准（acc≥55%: 78.2%✅, AUC≥0.70: ✅）。剩余验证项为跨模型泛化。建议立即启动：(1) 跨模型验证（GPT-2/OPT）(2) DeBERTa 端到端分类器 (3) 论文 framing。
206	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "9cfd18b9-f531-4658-95bf-f0f23d720411"
}
```

</details>

---


### System

_source line 53_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 46287,
    "tool_uses": 16,
    "duration_ms": 29372
  },
  "last_tool_name": "Bash",
  "uuid": "185e685c-80d2-4e4b-88d7-10a657173139",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Bash · `toolu_01EFLYe8Jb3KmGzyutbgASE4`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/ | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "b3984c76-2b4d-4e16-8039-d2933a527a8f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TnnKBa7GB9W7ySKnu9QPYc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9740,
      "cache_read_input_tokens": 36417,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9740,
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

_source line 55 · 2026-05-14T23:01:25.593Z_

<details><summary>↩ Tool result · `toolu_01EFLYe8Jb3KmGzyutbgASE4`</summary>

```text
total 608
drwxr-xr-x 2 ubuntu ubuntu 12288 May 14 23:01 .
drwxr-xr-x 9 ubuntu ubuntu  4096 May 14 23:01 ..
-rw------- 1 ubuntu ubuntu   380 May 14 22:56 atlas_v1_analysis_ALLOCATED_20260514T225639.json
-rw------- 1 ubuntu ubuntu  1317 May 14 22:56 atlas_v1_analysis_ANALYZING_20260514T225659.json
-rw------- 1 ubuntu ubuntu  1357 May 14 22:57 atlas_v1_analysis_DONE_20260514T225702.json
-rw------- 1 ubuntu ubuntu   379 May 14 22:56 atlas_v1_analysis_PENDING_20260514T225633.json
-rw------- 1 ubuntu ubuntu   375 May 14 22:56 atlas_v1_analysis_QUEUED_20260514T225636.json
-rw------- 1 ubuntu ubuntu   757 May 14 22:56 atlas_v1_analysis_RUNNING_20260514T225645.json
-rw------- 1 ubuntu ubuntu   926 May 14 22:56 atlas_v1_analysis_RUNNING_20260514T225650.json
-rw------- 1 ubuntu ubuntu  1181 May 14 14:44 cross_model_gpt2xl_001_ALLOCATED_20260514T144409.json
-rw------- 1 ubuntu ubuntu  1719 May 14 18:19 cross_model_gpt2xl_001_ANALYZING_20260514T181923.json
-rw------- 1 ubuntu ubuntu  4733 May 14 18:27 cross_model_gpt2xl_001_ANALYZING_20260514T182728.json
-rw------- 1 ubuntu ubuntu  4840 May 14 18:27 cross_model_gpt2xl_001_DONE_20260514T182747.json
-rw------- 1 ubuntu ubuntu  3241 May 14 18:28 cross_model_gpt2xl_001_DONE_20260514T182804.json
-rw------- 1 ubuntu ubuntu   773 May 14 14:10 cross_model_gpt2xl_001_PREPARING_20260514T141051.json
-rw------- 1 ubuntu ubuntu  1178 May 14 14:44 cross_model_gpt2xl_001_QUEUED_20260514T144405.json
-rw------- 1 ubuntu ubuntu  1643 May 14 14:44 cross_model_gpt2xl_001_RUNNING_20260514T144421.json
-rw------- 1 ubuntu ubuntu  1173 May 14 14:38 cross_model_olmo_001_ALLOCATED_20260514T143841.json
-rw------- 1 ubuntu ubuntu  1724 May 14 14:43 cross_model_olmo_001_ANALYZING_20260514T144328.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "530faec6-0caa-4b3d-9455-6a7a36de93ee"
}
```

</details>

---


### System

_source line 56_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 47205,
    "tool_uses": 17,
    "duration_ms": 30859
  },
  "last_tool_name": "Bash",
  "uuid": "bbfaa09d-0e77-4298-ba49-e8ed39aaf1b8",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Bash · `toolu_01StUVLSbYrhRra5cFrEooeF`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est -maxdepth 2 -name \"README*\" -o -name \"CLAUDE.md\" -o -name \"requirements.txt\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "96963d5d-3935-49b3-9a94-8b4e2ef5db12",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ERzxkqqR7ZU75mP4PNr8g3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 908,
      "cache_read_input_tokens": 46157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 908,
        "ephemeral_1h_input_tokens": 0
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

_source line 58 · 2026-05-14T23:01:27.078Z_

<details><summary>↩ Tool result · `toolu_01StUVLSbYrhRra5cFrEooeF`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/CLAUDE.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "180c18eb-5991-497d-868a-1338bbe0e255"
}
```

</details>

---


### System

_source line 59_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Reading .claude/CLAUDE.md",
  "usage": {
    "total_tokens": 47388,
    "tool_uses": 18,
    "duration_ms": 32216
  },
  "last_tool_name": "Read",
  "uuid": "3729a5ae-7a60-4522-8a18-f71d44c1cb52",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Read · `toolu_01PfbkZPFx6kD4S69PDmXh2C`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/CLAUDE.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "5fa1f33a-3e24-4027-9d61-5df8aecd9ca3",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q985uq4bMmviPkw5RYG3s6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 177,
      "cache_read_input_tokens": 47065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 177,
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

_source line 61 · 2026-05-14T23:01:28.356Z_

<details><summary>↩ Tool result · `toolu_01PfbkZPFx6kD4S69PDmXh2C`</summary>

````text
1	## 当前项目
2	当前绑定项目：**recursive_gen_depth_est**
3	
4	## 按需查阅
5	- 项目配置：`load_project_config("recursive_gen_depth_est")` 或 `load_project_config("recursive_gen_depth_est", section="execution")`
6	- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）
7	- 路线图：`read_roadmap()` 读取研究方向和短期任务
8	- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/`（写文件后用 `register_artifact` 注册）
9	
10	## Worker 操作规范
11	
12	### ssh-env-setup
13	
14	# 远程服务器环境搭建规范
15	
16	## 核心原则
17	
18	**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。
19	
20	**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。
21	
22	**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**
23	
24	## Phase 1: 环境探测（用 ssh_read_only）
25	
26	连接到服务器后，第一步永远是收集信息，不要直接装东西：
27	
28	```bash
29	# 1. Python 环境
30	which python3 && python3 --version
31	pip3 --version 2>/dev/null || echo "NO_PIP"
32	
33	# 2. CUDA 环境
34	nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo "NO_GPU"
35	nvcc --version 2>/dev/null | grep "release" || echo "NO_NVCC"
36	
37	# 3. 包管理器
38	ls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo "NO_CONDA"
39	ls -d .venv venv env 2>/dev/null || echo "NO_VENV"
40	pip3 list --format=freeze 2>/dev/null | grep -iE "torch|transformers|flash" || echo "NO_ML_PKGS"
41	
42	# 4. PEP 668 检查
43	python3 -c "import sysconfig; print(sysconfig.get_path('stdlib'))" 2>/dev/null
44	ls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo "PEP668_MANAGED" || echo "PEP668_OK"
45	```
46	
47	根据探测结果决定安装策略，不要猜。
48	
49	## Phase 2: 环境策略选择
50	
51	根据 Phase 1 结果选择**一个**策略，不要混用：
52	
53	| 探测结果 | 策略 | 说明 |
54	|----------|------|------|
55	| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |
56	| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |
57	| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |
58	| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |
59	
60	**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。
61	
62	## Phase 3: PyTorch 安装
63	
64	### CUDA 版本映射（2025-2026 常用）
65	
66	先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：
67	
68	| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |
69	|-----------|----------------------|-----------------|
70	| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |
71	| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |
72	| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |
73	| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |
74	
75	**不要猜版本号。** 如果不确定可用版本：
76	```bash
77	pip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3
78	```
79	
80	安装命令：
81	```bash
82	pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}
83	```
84	
85	### 大包超时处理
86	
87	PyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：
88	
89	```bash
90	# 方法 1: nohup + 轮询（推荐）
91	nohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &
92	echo $!  # 记录 PID
93	
94	# 后续用 ssh_read_only 轮询
95	cat /tmp/pip_install.log | tail -5
96	ps -p &lt;PID> -o pid= 2>/dev/null && echo "STILL_RUNNING" || echo "DONE"
97	```
98	
99	```bash
100	# 方法 2: 加大 pip 超时
101	pip install --timeout 300 torch ...
102	```
103	
104	## Phase 4: 验证（必须执行）
105	
106	安装后必须验证，不要假设成功：
107	
108	```bash
109	python3 -c "
110	import torch
111	print(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')
112	if torch.cuda.is_available():
113	    for i in range(torch.cuda.device_count()):
114	        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')
115	"
116	```
117	
118	验证失败的常见原因：
119	- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本
120	- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`
121	- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量
122	
123	## Phase 5: 项目依赖
124	
125	基础环境就绪后，安装项目依赖：
126	
127	```bash
128	# 优先用 requirements.txt / pyproject.toml
129	pip install -r requirements.txt  # 或 pip install -e .
130	
131	# 常用 ML 依赖补装
132	pip install transformers datasets einops accelerate wandb
133	```
134	
135	flash-attention 特殊处理（编译型包）：
136	```bash
137	# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟
138	pip install flash-attn --no-build-isolation
139	# 如果编译失败，试预编译版本
140	pip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels
141	```
142	
143	## ssh_read_only vs ssh_execute 使用规则
144	
145	| 操作 | 用哪个工具 |
146	|------|-----------|
147	| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |
148	| 读文件内容、查日志 | `ssh_read_only` |
149	| 安装包（pip install, conda install） | `ssh_execute` |
150	| 创建/修改文件、启动进程 | `ssh_execute` |
151	| 运行实验脚本 | `ssh_execute` |
152	
153	**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**
154	
155	## AutoDL 专项注意事项
156	
157	AutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：
158	
159	### 磁盘
160	- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`
161	- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满
162	- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径
163	
164	### 网络
165	- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连
166	- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401
167	- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误
168	- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c "from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')"`
169	
170	### SSH
171	- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`
172	
173	## 经验沉淀
174	
175	- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数
176	- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python
177	- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断
178	- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip
179	- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码
180	- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确
181	
182	## 更多 Skills（按需加载）
183	
184	执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。
185	
186	- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`
187	- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`
188	- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`
189	- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`
190	- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`
191	- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——reliability diagrams、ECE heatmap、T* scatter plot、模型对比图，直接在 A6000 服务器上执行，输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`
192	- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`
193	- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`
194	- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`
195	- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`
196	- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`
197	- **paper-banana** — 用 PaperBanana 生成发表级学术统计图——LLM 写 matplotlib 代码 + Critic 迭代 3 轮，输入 CSV/JSON 数据 + 意图描述即可。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`
198	- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说"提取图"/"抽图"/"extract figures"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`
199	- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`
200	- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说"有什么新论文"/"最近进展"/"research news"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`
201	- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`
202	- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`
203	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "6f725d49-8a3f-4e97-a813-1ad9e1bc821c"
}
```

</details>

---


### System

_source line 62_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 52887,
    "tool_uses": 19,
    "duration_ms": 34660
  },
  "last_tool_name": "Bash",
  "uuid": "0559e142-704e-4f8b-8925-65c98cc0b072",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Bash · `toolu_01KLbGt9AEy3h1AX9zwcR1LG`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est -type f -name \"*.py\" | grep -v logs | grep -v checkpoints | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "5e5d1650-467b-42e9-9520-7b31df04e2de",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018iSVsoz3xJroD6NRsdehKi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5491,
      "cache_read_input_tokens": 47242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5491,
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

_source line 64 · 2026-05-14T23:01:30.862Z_

<details><summary>↩ Tool result · `toolu_01KLbGt9AEy3h1AX9zwcR1LG`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/baseline_diveye.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/baseline_perplexity_regression.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/baseline_zero_shot_llm.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/baselines.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dcol_code/dcol_dataset.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dcol_code/dcol_loss.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dcol_code/dcol_model.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dcol_code/eval_dcol.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dcol_code/train_dcol.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dcol_feature_mlp.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/eval_d1d3.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/add_seed_id.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/atlas_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_ce_classification.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_coral.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_diveye_ordinal.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_ppl_regression.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_utils.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_zeroshot_llm.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/dcol_train_standalone_deprecated.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/generate_next_depth.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/lora_finetune.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "bf9595ce-5315-4c5c-9e8e-0b4a0972564c"
}
```

</details>

---


### System

_source line 65_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Reading scripts/baseline_coral.py",
  "usage": {
    "total_tokens": 53938,
    "tool_uses": 20,
    "duration_ms": 36368
  },
  "last_tool_name": "Read",
  "uuid": "b383a9b4-c8f9-4724-af7b-92489ec0be08",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Read · `toolu_018bCCvWapi3XyN83frJ6Asu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_coral.py",
  "limit": 120
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "94302691-d476-4b7e-b5b4-70445d44704f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LuP6cRgsDrCBZrnZirmbV1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1049,
      "cache_read_input_tokens": 52733,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1049,
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

_source line 67 · 2026-05-14T23:01:32.508Z_

<details><summary>↩ Tool result · `toolu_018bCCvWapi3XyN83frJ6Asu`</summary>

```text
1	"""
2	Baseline 3: CORAL (Consistent Rank Logits) for recursive generation depth estimation.
3	
4	Classic ordinal classification method (Cao, Mirjalili & Raschka, 2020).
5	Converts K-class ordinal problem into K-1 binary decisions sharing a backbone.
6	
7	Architecture: DeBERTa → [CLS] → shared Linear(hidden, 1) + K-1 bias terms
8	Each head k outputs logit for P(depth > k), k = 0..K-2.
9	Default: DeBERTa-v3-large (435M) to match DCOL backbone for fair comparison.
10	
11	CORAL loss (rank-consistent):
12	  L = Σ_{k=0}^{K-2} BCE(σ(w^T h + b_k), 𝟙[y > k])
13	where w is shared across thresholds and b_k is per-threshold bias.
14	
15	Prediction: depth = Σ_k 𝟙[σ(w^T h + b_k) > 0.5]
16	
17	Ref: Cao, W., Mirjalili, V. & Raschka, S. (2020). "Rank consistent ordinal
18	     regression for neural networks with consistent confidence sets."
19	     Pattern Recognition, 108, 107736.
20	
21	Input:  Raw depth_*.jsonl files (--data_dirs)
22	Output: {method}_classification_report.json, {method}_pairwise_auc.json, {method}_predictions.json
23	
24	Usage:
25	  python baseline_coral.py --data_dirs data/  # default: deberta-v3-large
26	  python baseline_coral.py --data_dirs data/ --model_name microsoft/deberta-v3-base --model_path /root/autodl-tmp/models/deberta-v3-base
27	  python baseline_coral.py --data_dirs data/ --dry_run
28	"""
29	
30	import argparse
31	import random
32	import numpy as np
33	import torch
34	import torch.nn as nn
35	from torch.utils.data import DataLoader, Dataset
36	from transformers import AutoModel, AutoTokenizer
37	
38	from baseline_utils import (
39	    load_jsonl_data, stratified_split, evaluate_and_save,
40	    add_common_args, NUM_DEPTHS,
41	)
42	
43	
44	def set_seed(seed):
45	    random.seed(seed)
46	    np.random.seed(seed)
47	    torch.manual_seed(seed)
48	    torch.cuda.manual_seed_all(seed)
49	
50	
51	class DepthTextDataset(Dataset):
52	    def __init__(self, texts, labels, tokenizer, max_seq_len):
53	        self.texts = texts
54	        self.labels = labels
55	        self.tokenizer = tokenizer
56	        self.max_seq_len = max_seq_len
57	
58	    def __len__(self):
59	        return len(self.texts)
60	
61	    def __getitem__(self, idx):
62	        enc = self.tokenizer(
63	            self.texts[idx],
64	            max_length=self.max_seq_len,
65	            padding="max_length",
66	            truncation=True,
67	            return_tensors="pt",
68	        )
69	        return {
70	            "input_ids": enc["input_ids"].squeeze(0),
71	            "attention_mask": enc["attention_mask"].squeeze(0),
72	            "label": torch.tensor(self.labels[idx], dtype=torch.long),
73	        }
74	
75	
76	class CORALModel(nn.Module):
77	    """
78	    DeBERTa + CORAL ordinal head.
79	
80	    The CORAL head has:
81	      - One shared weight vector w (Linear(hidden, 1, bias=False))
82	      - K-1 independent bias terms b_k
83	    Output: K-1 logits, logit_k = w^T h + b_k
84	    """
85	
86	    def __init__(self, model_name_or_path, num_classes=NUM_DEPTHS, dropout=0.1):
87	        super().__init__()
88	        self.num_thresholds = num_classes - 1
89	        self.encoder = AutoModel.from_pretrained(model_name_or_path)
90	        hidden_size = self.encoder.config.hidden_size
91	        self.dropout = nn.Dropout(dropout)
92	        self.fc = nn.Linear(hidden_size, 1, bias=False)
93	        self.biases = nn.Parameter(torch.zeros(self.num_thresholds))
94	
95	    def forward(self, input_ids, attention_mask):
96	        outputs = self.encoder(input_ids=input_ids, attention_mask=attention_mask)
97	        cls_repr = outputs.last_hidden_state[:, 0, :]
98	        cls_repr = self.dropout(cls_repr)
99	        logit_base = self.fc(cls_repr)  # [B, 1]
100	        logits = logit_base + self.biases  # [B, K-1] broadcast
101	        return logits
102	
103	
104	def coral_loss(logits, labels, num_classes=NUM_DEPTHS):
105	    """
106	    CORAL rank-consistent loss.
107	
108	    For each threshold k (0..K-2), construct binary target 𝟙[y > k]
109	    and compute BCE with logits.
110	    """
111	    num_thresholds = num_classes - 1
112	    ordinal_targets = torch.zeros(len(labels), num_thresholds,
113	                                  device=labels.device, dtype=logits.dtype)
114	    for k in range(num_thresholds):
115	        ordinal_targets[:, k] = (labels > k).float()
116	    return nn.functional.binary_cross_entropy_with_logits(logits, ordinal_targets)
117	
118	
119	def coral_predict(logits):
120	    """depth = number of thresholds where σ(logit) > 0.5"""
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "d97b8e6b-0465-41d0-9b9a-71f89aacb075"
}
```

</details>

---


### System

_source line 68_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Reading artifacts/dcol_code/dcol_model.py",
  "usage": {
    "total_tokens": 55735,
    "tool_uses": 21,
    "duration_ms": 38306
  },
  "last_tool_name": "Read",
  "uuid": "afb478fd-7efa-4658-a12a-fdad7c46a5c0",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Read · `toolu_01FK6tqNpADRS9vEGTU9eGRq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dcol_code/dcol_model.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "abcbaf89-b20b-4279-8f96-586f364421d0",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YJq1MHKysfQQD5gnwoAzCC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1789,
      "cache_read_input_tokens": 53782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1789,
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

_source line 70 · 2026-05-14T23:01:34.457Z_

<details><summary>↩ Tool result · `toolu_01FK6tqNpADRS9vEGTU9eGRq`</summary>

```text
1	"""DeBERTa-v3-large encoder with MLP projection head for DCOL.
2	
3	Input:  tokenized text (input_ids, attention_mask)
4	Output: L2-normalized 128-dim embeddings
5	
6	Dependencies: transformers, torch
7	"""
8	
9	import torch
10	import torch.nn as nn
11	from transformers import AutoModel
12	
13	
14	class DColModel(nn.Module):
15	    def __init__(self, model_name: str = "microsoft/deberta-v3-large", embed_dim: int = 128):
16	        super().__init__()
17	        self.encoder = AutoModel.from_pretrained(model_name)
18	        hidden = self.encoder.config.hidden_size  # 1024 for deberta-v3-large
19	        self.proj = nn.Sequential(
20	            nn.Linear(hidden, hidden),
21	            nn.GELU(),
22	            nn.Linear(hidden, embed_dim),
23	        )
24	
25	    def forward(self, input_ids: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
26	        out = self.encoder(input_ids=input_ids, attention_mask=attention_mask)
27	        cls = out.last_hidden_state[:, 0]  # CLS pooling
28	        emb = self.proj(cls)
29	        return nn.functional.normalize(emb, dim=-1)
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "63d1f399-434f-4456-b4cd-6c82894b5766"
}
```

</details>

---


### System

_source line 71_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Reading ~/.agent-ml-research-idea_gen_0513_2/scripts/baseline_diveye_ordinal.py",
  "usage": {
    "total_tokens": 56248,
    "tool_uses": 22,
    "duration_ms": 40217
  },
  "last_tool_name": "Read",
  "uuid": "ca18192e-073b-4ff6-bbb1-61336ccf17d5",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Read · `toolu_01Y8bu34tzib41iv5XhwcnyU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/scripts/baseline_diveye_ordinal.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "64c85ad2-fc66-4638-8500-1031da43bebc",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GsBR2G7Tp8vvoRqMUsboAK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 507,
      "cache_read_input_tokens": 55571,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 507,
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

_source line 73 · 2026-05-14T23:01:36.361Z_

<details><summary>↩ Tool result · reported error · `toolu_01Y8bu34tzib41iv5XhwcnyU`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "ca0d94b8-0bac-46f5-9229-e85250af4f00",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est."
}
```

</details>

---


### System

_source line 74_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Reading scripts/baseline_diveye_ordinal.py",
  "usage": {
    "total_tokens": 56481,
    "tool_uses": 23,
    "duration_ms": 41464
  },
  "last_tool_name": "Read",
  "uuid": "944b9cb3-1f05-45b1-a1fa-3105a460bcdf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 75_

<details open><summary>🔧 Tool call — Read · `toolu_01Ju5gXgZQKsfsmwfri2QSKz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_diveye_ordinal.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "1e9c5582-73ec-4362-a8b3-c42513b15166",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XN78C9c2mKPYr4dwCxr4e5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 160,
      "cache_read_input_tokens": 56078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 160,
        "ephemeral_1h_input_tokens": 0
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

_source line 76 · 2026-05-14T23:01:37.610Z_

<details><summary>↩ Tool result · `toolu_01Ju5gXgZQKsfsmwfri2QSKz`</summary>

```text
1	"""
2	Baseline 1: DivEye Binary → Ordinal for recursive generation depth estimation.
3	
4	Adapts DivEye (Basani & Chen, TMLR 2026) from binary human-vs-AI detection to
5	ordinal depth classification. DivEye's core insight: AI-generated text has lower
6	surprisal diversity than human text; deeper recursion should further reduce diversity.
7	
8	Method:
9	  - Extract DivEye-style diversity features (surprisal variance, entropy, lexical
10	    diversity, repetition) from pre-computed 19-dim feature vectors
11	  - Train One-vs-Rest (OVR) classifiers: one binary classifier per depth
12	  - Predict depth = argmax(OVR decision scores)
13	
14	Ref: Basani, A. R. & Chen, P.-Y. (2026). "Diversity Boosts AI-Generated Text
15	     Detection." TMLR. GitHub: https://github.com/IBM/diveye
16	
17	Input:  Pre-extracted features JSONL (--features_path)
18	Output: {method}_classification_report.json, {method}_pairwise_auc.json, {method}_predictions.json
19	
20	Usage:
21	  python baseline_diveye_ordinal.py --features_path data/features_all.jsonl
22	  python baseline_diveye_ordinal.py --features_path data/features_all.jsonl --base_clf svm
23	"""
24	
25	import argparse
26	import numpy as np
27	from sklearn.preprocessing import StandardScaler
28	from sklearn.multiclass import OneVsRestClassifier
29	from sklearn.linear_model import LogisticRegression
30	from sklearn.svm import SVC
31	from sklearn.calibration import CalibratedClassifierCV
32	
33	from baseline_utils import (
34	    load_features, stratified_split, evaluate_and_save,
35	    add_common_args, NUM_DEPTHS, FEATURE_NAMES,
36	)
37	
38	# DivEye feature subset: surprisal distributional + lexical diversity + repetition
39	DIVEYE_FEATURES = [
40	    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
41	    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
42	    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
43	    "rep_2gram", "rep_3gram", "rep_4gram",
44	]
45	DIVEYE_INDICES = [FEATURE_NAMES.index(f) for f in DIVEYE_FEATURES]
46	
47	
48	class DivEyeOrdinal:
49	    """OVR classifier on DivEye diversity features for ordinal depth prediction."""
50	
51	    def __init__(self, base_clf="logistic", C=1.0, seed=42):
52	        self.scaler = StandardScaler()
53	        self.seed = seed
54	        if base_clf == "logistic":
55	            estimator = LogisticRegression(
56	                C=C, max_iter=1000, random_state=seed,
57	            )
58	        elif base_clf == "svm":
59	            estimator = CalibratedClassifierCV(
60	                SVC(C=C, kernel="rbf", random_state=seed),
61	                cv=3,
62	            )
63	        else:
64	            raise ValueError(f"Unknown base_clf: {base_clf}")
65	        self.ovr = OneVsRestClassifier(estimator)
66	
67	    def fit(self, X, y):
68	        Xd = self.scaler.fit_transform(X[:, DIVEYE_INDICES])
69	        self.ovr.fit(Xd, y)
70	
71	    def predict(self, X):
72	        Xd = self.scaler.transform(X[:, DIVEYE_INDICES])
73	        return self.ovr.predict(Xd)
74	
75	    def predict_proba(self, X):
76	        Xd = self.scaler.transform(X[:, DIVEYE_INDICES])
77	        if hasattr(self.ovr, "predict_proba"):
78	            probs = self.ovr.predict_proba(Xd)
79	        else:
80	            scores = self.ovr.decision_function(Xd)
81	            from scipy.special import softmax
82	            probs = softmax(scores, axis=1)
83	        if probs.shape[1] < NUM_DEPTHS:
84	            full = np.zeros((probs.shape[0], NUM_DEPTHS))
85	            for i, c in enumerate(self.ovr.classes_):
86	                full[:, c] = probs[:, i]
87	            return full
88	        return probs
89	
90	
91	def main():
92	    parser = argparse.ArgumentParser(description="DivEye Binary→Ordinal baseline")
93	    add_common_args(parser)
94	    parser.add_argument("--base_clf", choices=["logistic", "svm"], default="logistic")
95	    parser.add_argument("--C", type=float, default=1.0, help="Regularization strength")
96	    args = parser.parse_args()
97	
98	    if args.features_path is None:
99	        print("ERROR: --features_path is required for DivEye baseline.")
100	        print("Run extract_features.py first to generate features JSONL.")
101	        return
102	
103	    X, y = load_features(args.features_path)
104	    train_idx, eval_idx = stratified_split(y, eval_split=args.eval_split, seed=args.seed)
105	    X_train, y_train = X[train_idx], y[train_idx]
106	    X_eval, y_eval = X[eval_idx], y[eval_idx]
107	    print(f"Train: {len(y_train)}, Eval: {len(y_eval)}")
108	
109	    method_name = f"diveye_ovr_{args.base_clf}"
110	    model = DivEyeOrdinal(base_clf=args.base_clf, C=args.C, seed=args.seed)
111	    model.fit(X_train, y_train)
112	    y_pred = model.predict(X_eval)
113	    y_prob = model.predict_proba(X_eval)
114	    evaluate_and_save(method_name, y_eval, y_pred, y_prob, args.output_dir)
115	
116	
117	if __name__ == "__main__":
118	    main()
119	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "3da4f061-08f7-4a33-a1ab-737f4d93527c"
}
```

</details>

---


### System

_source line 77_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Reading scripts/baseline_ppl_regression.py",
  "usage": {
    "total_tokens": 58380,
    "tool_uses": 24,
    "duration_ms": 43550
  },
  "last_tool_name": "Read",
  "uuid": "9048c94d-5942-4f35-a449-4ef99f61bcaa",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Read · `toolu_019nNnatmqMrkumUUyy7r5g5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_ppl_regression.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "e8998229-e425-462c-abf3-d423fe39af5e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UMMTkvbB3XBD6TVirgpbZc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1898,
      "cache_read_input_tokens": 56238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1898,
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

_source line 79 · 2026-05-14T23:01:39.695Z_

<details><summary>↩ Tool result · `toolu_019nNnatmqMrkumUUyy7r5g5`</summary>

```text
1	"""
2	Baseline 2: Perplexity-only Regression for recursive generation depth estimation.
3	
4	Simplest baseline — uses only perplexity statistics (mean_ppl, p75_ppl, p90_ppl)
5	to predict recursion depth via:
6	  (a) Ridge Regression → round to nearest integer depth
7	  (b) Ordinal Logistic Regression (cumulative link model)
8	
9	If PPL alone separates depths well, more complex methods add no value.
10	
11	Input:  Pre-extracted features JSONL (--features_path) or raw depth_*.jsonl (--data_dirs)
12	Output: {method}_classification_report.json, {method}_pairwise_auc.json, {method}_predictions.json
13	
14	Usage:
15	  python baseline_ppl_regression.py --features_path data/features_all.jsonl
16	  python baseline_ppl_regression.py --features_path data/features_all.jsonl --mode ordinal
17	"""
18	
19	import argparse
20	import numpy as np
21	from sklearn.linear_model import Ridge
22	from sklearn.preprocessing import StandardScaler
23	
24	from baseline_utils import (
25	    load_features, stratified_split, evaluate_and_save,
26	    add_common_args, NUM_DEPTHS, FEATURE_NAMES,
27	)
28	
29	PPL_FEATURES = ["mean_ppl", "p75_ppl", "p90_ppl"]
30	PPL_INDICES = [FEATURE_NAMES.index(f) for f in PPL_FEATURES]
31	
32	
33	class RidgePPLRegressor:
34	    """Ridge regression on 3 PPL features → round to nearest depth."""
35	
36	    def __init__(self, alpha=1.0):
37	        self.scaler = StandardScaler()
38	        self.model = Ridge(alpha=alpha)
39	
40	    def fit(self, X, y):
41	        Xs = self.scaler.fit_transform(X[:, PPL_INDICES])
42	        self.model.fit(Xs, y.astype(np.float64))
43	
44	    def predict(self, X):
45	        Xs = self.scaler.transform(X[:, PPL_INDICES])
46	        raw = self.model.predict(Xs)
47	        return np.clip(np.round(raw).astype(int), 0, NUM_DEPTHS - 1)
48	
49	    def predict_proba(self, X):
50	        preds = self.predict(X)
51	        prob = np.zeros((len(preds), NUM_DEPTHS))
52	        for i, p in enumerate(preds):
53	            prob[i, p] = 1.0
54	        return prob
55	
56	
57	class OrdinalLogisticPPL:
58	    """
59	    Ordinal Logistic Regression (cumulative model) on 3 PPL features.
60	
61	    Uses K-1 binary logistic regressions: P(depth >= k) for k=1..K-1.
62	    Falls back to sklearn LogisticRegression if mord is unavailable.
63	    """
64	
65	    def __init__(self):
66	        self.scaler = StandardScaler()
67	        self.models = []
68	
69	    def fit(self, X, y):
70	        Xs = self.scaler.fit_transform(X[:, PPL_INDICES])
71	        from sklearn.linear_model import LogisticRegression
72	        self.models = []
73	        for k in range(1, NUM_DEPTHS):
74	            binary_y = (y >= k).astype(int)
75	            clf = LogisticRegression(max_iter=1000, C=1.0)
76	            clf.fit(Xs, binary_y)
77	            self.models.append(clf)
78	
79	    def predict_proba(self, X):
80	        Xs = self.scaler.transform(X[:, PPL_INDICES])
81	        cum_probs = np.column_stack([
82	            m.predict_proba(Xs)[:, 1] for m in self.models
83	        ])
84	        probs = np.zeros((len(X), NUM_DEPTHS))
85	        probs[:, 0] = 1.0 - cum_probs[:, 0]
86	        for k in range(1, NUM_DEPTHS - 1):
87	            probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]
88	        probs[:, NUM_DEPTHS - 1] = cum_probs[:, NUM_DEPTHS - 2]
89	        probs = np.clip(probs, 0, 1)
90	        row_sums = probs.sum(axis=1, keepdims=True)
91	        probs = probs / np.where(row_sums > 0, row_sums, 1.0)
92	        return probs
93	
94	    def predict(self, X):
95	        return self.predict_proba(X).argmax(axis=1)
96	
97	
98	def main():
99	    parser = argparse.ArgumentParser(description="Perplexity-only Regression baseline")
100	    add_common_args(parser)
101	    parser.add_argument("--mode", choices=["ridge", "ordinal", "both"], default="both")
102	    parser.add_argument("--alpha", type=float, default=1.0, help="Ridge regularization")
103	    args = parser.parse_args()
104	
105	    if args.features_path is None:
106	        print("ERROR: --features_path is required for PPL regression baseline.")
107	        print("Run extract_features.py first to generate features JSONL.")
108	        return
109	
110	    X, y = load_features(args.features_path)
111	    train_idx, eval_idx = stratified_split(y, eval_split=args.eval_split, seed=args.seed)
112	    X_train, y_train = X[train_idx], y[train_idx]
113	    X_eval, y_eval = X[eval_idx], y[eval_idx]
114	    print(f"Train: {len(y_train)}, Eval: {len(y_eval)}")
115	
116	    modes = ["ridge", "ordinal"] if args.mode == "both" else [args.mode]
117	
118	    for mode in modes:
119	        method_name = f"ppl_{mode}"
120	        if mode == "ridge":
121	            model = RidgePPLRegressor(alpha=args.alpha)
122	        else:
123	            model = OrdinalLogisticPPL()
124	
125	        model.fit(X_train, y_train)
126	        y_pred = model.predict(X_eval)
127	        y_prob = model.predict_proba(X_eval)
128	        evaluate_and_save(method_name, y_eval, y_pred, y_prob, args.output_dir)
129	
130	
131	if __name__ == "__main__":
132	    main()
133	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "6077fef1-73c0-48de-8676-3c18b07155ba"
}
```

</details>

---


### System

_source line 80_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "description": "Reading experiment_plan.yaml",
  "usage": {
    "total_tokens": 60402,
    "tool_uses": 25,
    "duration_ms": 45636
  },
  "last_tool_name": "Read",
  "uuid": "83c5e6c5-ec78-4662-b1ef-b4e2fe186c23",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool call

_source line 81_

<details open><summary>🔧 Tool call — Read · `toolu_01ENnrKH22W2TZu2to8aQvVv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/experiment_plan.yaml",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "31b5141a-7edf-49f8-9c0d-2f9165f3bcdd",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TWgZsabF2A81TZ6hzqyZRw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2018,
      "cache_read_input_tokens": 58136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2018,
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

_source line 82 · 2026-05-14T23:01:41.776Z_

<details><summary>↩ Tool result · `toolu_01ENnrKH22W2TZu2to8aQvVv`</summary>

```text
1	experiments:
2	  # === P0: Must-run (headline results) ===
3	
4	  - id: plan_001a
5	    claim: 1
6	    description: "Pythia-1.4B recursive chain — nucleus p=0.95 (MVP)"
7	    priority: P0
8	    gpu_budget_hours: 2
9	    deps: []
10	    status: done
11	    notes: "4 depths × 1 strategy. 78.2% 4-class acc, d1v2 AUC 0.861. Content-type control: 81.6%."
12	    registry_id: mvp_pipeline_pythia_002
13	
14	  - id: plan_001b
15	    claim: 1
16	    description: "Pythia-1.4B — temperature τ=0.9 chain (4 depths)"
17	    priority: P0
18	    gpu_budget_hours: 2
19	    deps: []
20	    registry_id: pythia_temp09_001
21	    notes: "τ=0.9 temp-only decoding. Data→data/pythia_temp09/. Launched on cuda:0 after OLMo."
22	
23	  - id: plan_001c
24	    claim: 1
25	    description: "Pythia-1.4B — top-k k=50 chain (4 depths)"
26	    priority: P0
27	    gpu_budget_hours: 2
28	    deps: []
29	    registry_id: pythia_topk50_001
30	    notes: "top-k k=50 decoding. Data→data/pythia_topk50/. Queued for cuda:1 after GPT-2 XL."
31	
32	  - id: plan_002
33	    claim: 1
34	    description: "OLMo-1B recursive chain (4 depths × 3 strategies)"
35	    priority: P0
36	    gpu_budget_hours: 8
37	    deps: []
38	    registry_id: cross_model_olmo_002
39	    notes: "OLMo-1B on Dolma. q_proj/k_proj/v_proj LoRA. olmo_001 failed (script bug), olmo_002 重跑。等 cuda:0 释放。"
40	
41	  - id: plan_003
42	    claim: 1
43	    description: "GPT-2 XL 1.5B recursive chain (4 depths × 3 strategies)"
44	    priority: P0
45	    gpu_budget_hours: 8
46	    deps: []
47	    registry_id: cross_model_gpt2xl_001
48	    notes: "GPT-2 most studied in collapse literature. WebText training data. c_attn/c_proj LoRA."
49	
50	  - id: plan_002b
51	    claim: 1
52	    description: "OLMo-1B — temperature τ=0.9 chain (4 depths)"
53	    priority: P0
54	    gpu_budget_hours: 2
55	    deps: []
56	    registry_id: olmo_temp09_002
57	    notes: "3×3 matrix cell. OLMo temp09. olmo_temp09_001 failed (kill at Step 3 67%), olmo_temp09_002 从断点恢复。"
58	
59	  - id: plan_002c
60	    claim: 1
61	    description: "OLMo-1B — top-k k=50 chain (4 depths)"
62	    priority: P0
63	    gpu_budget_hours: 2
64	    deps: []
65	    notes: "3×3 matrix cell. OLMo topk50."
66	
67	  - id: plan_003b
68	    claim: 1
69	    description: "GPT-2 XL — temperature τ=0.9 chain (4 depths)"
70	    priority: P0
71	    gpu_budget_hours: 2
72	    deps: []
73	    registry_id: gpt2xl_temp09_001
74	    notes: "3×3 matrix cell. Running on cuda:1."
75	
76	  - id: plan_003c
77	    claim: 1
78	    description: "GPT-2 XL — top-k k=50 chain (4 depths)"
79	    priority: P0
80	    gpu_budget_hours: 2
81	    deps: []
82	    registry_id: gpt2xl_topk50_001
83	    notes: "3×3 matrix cell. GPT-2 XL topk50."
84	
85	  - id: plan_004
86	    claim: 1
87	    description: "DCOL training: DeBERTa-v3-large with learnable margins contrastive loss"
88	    priority: P0
89	    gpu_budget_hours: 15
90	    deps: [plan_001b, plan_002, plan_003]
91	    notes: "Adapt CLOC multi-margin N-pair loss. If DCOL improvement over RF is < 5pp, pivot: Atlas (Claim 2) becomes primary contribution, DCOL becomes one method within the framework."
92	
93	  - id: plan_005
94	    claim: 1
95	    description: "Leave-one-model-out generalization: train on 2 families, test on 3rd"
96	    priority: P0
97	    gpu_budget_hours: 5
98	    deps: [plan_004]
99	    notes: "3 rotations. Research-phase gate: cross-model acc ≥ 45%."
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "cdd949c8-e2e5-4701-8c5b-2dc6cf6b7b20"
}
```

</details>

---


### System

_source line 83_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ae103953f0d698396",
  "tool_use_id": "toolu_018LqyWVrFGYJWUDKTkV7xwf",
  "status": "completed",
  "output_file": "",
  "summary": "Explore project structure and existing code",
  "usage": {
    "total_tokens": 62019,
    "tool_uses": 25,
    "duration_ms": 71849
  },
  "uuid": "7b4a96c4-7ba3-4659-a7e7-d1f77e817b38",
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec"
}
```

---


### Tool result

_source line 84 · 2026-05-14T23:02:07.985Z_

<details><summary>↩ Tool result · `toolu_018LqyWVrFGYJWUDKTkV7xwf`</summary>

````text
Perfect! Now I have a comprehensive understanding of the project. Let me create a summary report for the user.

## Project Exploration Summary: recursive_gen_depth_est

I've thoroughly explored the project structure, codebase, and supporting documentation. Here's my comprehensive findings:

### 1. **Overall Directory Structure**

```
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/
├── artifacts/                    # Core implementations & analyses
│   ├── baseline_*.py            # Individual baseline implementations
│   ├── baselines.py             # Unified baseline battery framework
│   ├── dcol_feature_mlp.py       # Feature-based DCOL training (MLP)
│   ├── dcol_code/               # Text-based DCOL implementation
│   │   ├── dcol_dataset.py
│   │   ├── dcol_loss.py
│   │   ├── dcol_model.py        # DeBERTa encoder with projection head
│   │   ├── train_dcol.py
│   │   └── eval_dcol.py
│   ├── eval_d1d3.py             # Depth-specific evaluation
│   ├── _project/data/           # Local project data (minimal)
│   └── dream_reports/           # Analysis reports
├── scripts/                      # Standalone baseline scripts
│   ├── baseline_utils.py         # Shared utilities (CRITICAL FILE)
│   ├── baseline_ce_classification.py     # Standard CE baseline
│   ├── baseline_coral.py         # Ordinal CORAL baseline
│   ├── baseline_diveye_ordinal.py        # DivEye diversity features
│   ├── baseline_ppl_regression.py        # Perplexity-only regression
│   ├── baseline_zeroshot_llm.py  # Zero-shot LLM prompting
│   ├── generate_next_depth.py    # Data generation pipeline
│   ├── lora_finetune.py          # LoRA fine-tuning on recursive chains
│   ├── atlas_analysis.py         # Feature importance analysis
│   ├── run_pipeline_*.sh         # Pipeline execution scripts
│   └── add_seed_id.py            # Utility for reproducibility
├── docs/
│   └── IDEA_BRIEF.md             # Full research proposal (~200 lines)
├── checkpoints/                  # Experiment status files
├── memory.md                      # Key findings & lessons learned
├── paper_framing.md              # Paper structure & framing
├── experiment_plan.yaml          # Research plan with status
├── ROADMAP.md                    # Short-term task roadmap
├── .claude/CLAUDE.md             # Worker guidelines & best practices
└── registry.yaml                 # Experiment tracking

Data note: No local features_all.jsonl found—data is generated on remote servers
and stored in task_context/ or remote data directories.
```

### 2. **Critical File: baseline_utils.py**

**Location**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_utils.py` (175 lines)

**Key Constants**:
- `NUM_DEPTHS = 4` (depths 0-3, representing 0 = human, 1-3 = recursive generations)
- `FEATURE_NAMES` (19 features):
  - **Perplexity-based** (9): mean_ppl, var_ppl, skewness_ppl, kurtosis_ppl, p10_ppl, p25_ppl, p50_ppl, p75_ppl, p90_ppl
  - **Surprisal-based** (3): mean_surprisal, var_surprisal, entropy_of_surprisal
  - **Lexical diversity** (7): type_token_ratio, hapax_ratio, bigram_entropy, trigram_entropy, rep_2gram, rep_3gram, rep_4gram

**Key Functions**:
- `load_jsonl_data()` — Load raw text + labels from depth_*.jsonl files
- `load_features()` — Load pre-extracted 19-dim feature vectors from JSONL
- `stratified_split()` — Train/eval split with stratification
- `evaluate_and_save()` — Compute accuracy, MAE, pairwise AUC, save predictions
- `add_common_args()` — Unified CLI argument parser for all baselines

### 3. **Existing Baselines Code**

**4 Main Baseline Methods** (all in `scripts/`):

| Baseline | File | Architecture | Loss | Input |
|----------|------|--------------|------|-------|
| **PPL Regression** | `baseline_ppl_regression.py` | Ridge regression on 3 PPL features (mean_ppl, p75_ppl, p90_ppl) | L2 (regression) | Features (JSONL) |
| **DivEye OVR** | `baseline_diveye_ordinal.py` | One-vs-Rest on 14 diversity features | Binary CE | Features (JSONL) |
| **CE Classification** | `baseline_ce_classification.py` | DeBERTa-v3-large → CLS → Linear(hidden, 4) | Standard CE loss | Raw text (depth_*.jsonl) |
| **CORAL (Ordinal)** | `baseline_coral.py` | DeBERTa-v3-large → K-1 shared threshold logits | Rank-consistent BCE | Raw text (depth_*.jsonl) |

**Additional Baselines** (in `artifacts/`):
- `baselines.py` — Unified framework supporting all methods above
- `baseline_zero_shot_llm.py` — Prompt-based LLM classification
- `baseline_perplexity_regression.py` — Single-feature PPL regression

### 4. **Data Format**

**No local features_all.jsonl exists locally.** The data is:
- **Generated on remote servers** via LoRA fine-tuning pipelines (3 models × 3 decoding strategies × 4 depths)
- **Format**: JSONL with 19 feature dimensions + depth label:
  ```json
  {"mean_ppl": 45.2, "var_ppl": 8.5, ..., "rep_4gram": 0.12, "depth": 1}
  ```
- **Raw text format**: `depth_0.jsonl`, `depth_1.jsonl`, etc. with `{"text": "...", "depth": k}`

**Key data sources** (from memory.md & IDEA_BRIEF):
- **Pythia-1.4B**: nucleus (78.2% acc), temp09 (76.3%), topk50 (69.6%)
- **GPT-2 XL**: temp (85.4%), nucleus (83.3%)
- **OLMo-1B**: nucleus (78.8%)

### 5. **Existing DCOL Implementation**

**Feature-based DCOL** (`artifacts/dcol_feature_mlp.py`, 400+ lines):
- **Input**: 19-dim features (JSONL)
- **Architecture**: MLP(19→128→64) + projection head (64→32, L2-norm) + classifier (64→4)
- **Loss**: L_DCOL = L_attractive + L_repulsive + λ·L_CE
- **Features**: BalancedDepthSampler for valid contrastive pairs

**Text-based DCOL** (`artifacts/dcol_code/`):
- `dcol_model.py`: DeBERTa-v3-large → CLS → Linear(1024→embed_dim) projection
- Designed for raw text (not pre-extracted features)

### 6. **Requirements & Dependencies**

**No requirements.txt exists locally.** Based on imports across all scripts:

```
Core ML:
  torch ≥ 2.0
  transformers
  scikit-learn
  numpy, pandas
  
Distributed/Optimization:
  accelerate
  peft (for LoRA)
  
Monitoring:
  wandb (weights & biases)
  
Optional:
  flash-attn (for training speedup)
```

### 7. **Key Findings from Memory & Experiments**

**MVP Results** (Pythia-1.4B nucleus):
- **4-class accuracy**: 78.2% (95% CI: [76.9%, 79.4%])
- **Adjacent AUC**: d0v1=0.998, d1v2=0.861, d2v3=0.801
- **MAE**: 0.237
- **Top features**: var_surprisal (rank 1-4), p90_ppl (rank 1-2)

**Cross-Model Findings**:
- **Signal strength is model-dependent**: Pythia nucleus > temp > topk; GPT-2 XL temp > nucleus > topk
- **Feature consistency**: 6/6 experiments show same "core 4" features dominate (var_surprisal, p90_ppl, mean_surprisal, p75_ppl)
- **Spearman rank correlation**: 0.79 average across models/strategies (highest within-model: 0.859)

**Known Issues** (documented in memory.md):
- DCOL v1 had margin collapse (margin_lr=1e-3 too high)
- DCOL v2 suffered OOM from zombie processes
- DivEye citation corrected: TMLR 2026 (not ICLR 2026)

### 8. **Relevant File Paths**

**Core Scripts**:
- Utilities: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_utils.py`
- Baselines: All in `scripts/baseline_*.py`
- DCOL: `artifacts/dcol_feature_mlp.py` and `artifacts/dcol_code/`

**Documentation**:
- Project brief: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/IDEA_BRIEF.md`
- Memory: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/memory.md`
- Worker guide: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/CLAUDE.md`

**Note**: There is **NO `src/classify.py`** file. The classification logic is distributed across multiple baseline scripts in `scripts/` and `artifacts/`.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "0b093a8c-4d84-4782-965b-085dafa9ab06",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Explore the project at /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est to understand:\n1. Overall directory structure\n2. The existing classify.py at src/classify.py - read the full file\n3. Any existing baselines code\n4. Data format - check if data/features_all.jsonl exists locally or only on remote server\n5. Any requirements.txt or setup files\n\nSearch breadth: medium",
    "agentId": "ae103953f0d698396",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have a comprehensive understanding of the project. Let me create a summary report for the user.\n\n## Project Exploration Summary: recursive_gen_depth_est\n\nI've thoroughly explored the project structure, codebase, and supporting documentation. Here's my comprehensive findings:\n\n### 1. **Overall Directory Structure**\n\n```\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/\n├── artifacts/                    # Core implementations & analyses\n│   ├── baseline_*.py            # Individual baseline implementations\n│   ├── baselines.py             # Unified baseline battery framework\n│   ├── dcol_feature_mlp.py       # Feature-based DCOL training (MLP)\n│   ├── dcol_code/               # Text-based DCOL implementation\n│   │   ├── dcol_dataset.py\n│   │   ├── dcol_loss.py\n│   │   ├── dcol_model.py        # DeBERTa encoder with projection head\n│   │   ├── train_dcol.py\n│   │   └── eval_dcol.py\n│   ├── eval_d1d3.py             # Depth-specific evaluation\n│   ├── _project/data/           # Local project data (minimal)\n│   └── dream_reports/           # Analysis reports\n├── scripts/                      # Standalone baseline scripts\n│   ├── baseline_utils.py         # Shared utilities (CRITICAL FILE)\n│   ├── baseline_ce_classification.py     # Standard CE baseline\n│   ├── baseline_coral.py         # Ordinal CORAL baseline\n│   ├── baseline_diveye_ordinal.py        # DivEye diversity features\n│   ├── baseline_ppl_regression.py        # Perplexity-only regression\n│   ├── baseline_zeroshot_llm.py  # Zero-shot LLM prompting\n│   ├── generate_next_depth.py    # Data generation pipeline\n│   ├── lora_finetune.py          # LoRA fine-tuning on recursive chains\n│   ├── atlas_analysis.py         # Feature importance analysis\n│   ├── run_pipeline_*.sh         # Pipeline execution scripts\n│   └── add_seed_id.py            # Utility for reproducibility\n├── docs/\n│   └── IDEA_BRIEF.md             # Full research proposal (~200 lines)\n├── checkpoints/                  # Experiment status files\n├── memory.md                      # Key findings & lessons learned\n├── paper_framing.md              # Paper structure & framing\n├── experiment_plan.yaml          # Research plan with status\n├── ROADMAP.md                    # Short-term task roadmap\n├── .claude/CLAUDE.md             # Worker guidelines & best practices\n└── registry.yaml                 # Experiment tracking\n\nData note: No local features_all.jsonl found—data is generated on remote servers\nand stored in task_context/ or remote data directories.\n```\n\n### 2. **Critical File: baseline_utils.py**\n\n**Location**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_utils.py` (175 lines)\n\n**Key Constants**:\n- `NUM_DEPTHS = 4` (depths 0-3, representing 0 = human, 1-3 = recursive generations)\n- `FEATURE_NAMES` (19 features):\n  - **Perplexity-based** (9): mean_ppl, var_ppl, skewness_ppl, kurtosis_ppl, p10_ppl, p25_ppl, p50_ppl, p75_ppl, p90_ppl\n  - **Surprisal-based** (3): mean_surprisal, var_surprisal, entropy_of_surprisal\n  - **Lexical diversity** (7): type_token_ratio, hapax_ratio, bigram_entropy, trigram_entropy, rep_2gram, rep_3gram, rep_4gram\n\n**Key Functions**:\n- `load_jsonl_data()` — Load raw text + labels from depth_*.jsonl files\n- `load_features()` — Load pre-extracted 19-dim feature vectors from JSONL\n- `stratified_split()` — Train/eval split with stratification\n- `evaluate_and_save()` — Compute accuracy, MAE, pairwise AUC, save predictions\n- `add_common_args()` — Unified CLI argument parser for all baselines\n\n### 3. **Existing Baselines Code**\n\n**4 Main Baseline Methods** (all in `scripts/`):\n\n| Baseline | File | Architecture | Loss | Input |\n|----------|------|--------------|------|-------|\n| **PPL Regression** | `baseline_ppl_regression.py` | Ridge regression on 3 PPL features (mean_ppl, p75_ppl, p90_ppl) | L2 (regression) | Features (JSONL) |\n| **DivEye OVR** | `baseline_diveye_ordinal.py` | One-vs-Rest on 14 diversity features | Binary CE | Features (JSONL) |\n| **CE Classification** | `baseline_ce_classification.py` | DeBERTa-v3-large → CLS → Linear(hidden, 4) | Standard CE loss | Raw text (depth_*.jsonl) |\n| **CORAL (Ordinal)** | `baseline_coral.py` | DeBERTa-v3-large → K-1 shared threshold logits | Rank-consistent BCE | Raw text (depth_*.jsonl) |\n\n**Additional Baselines** (in `artifacts/`):\n- `baselines.py` — Unified framework supporting all methods above\n- `baseline_zero_shot_llm.py` — Prompt-based LLM classification\n- `baseline_perplexity_regression.py` — Single-feature PPL regression\n\n### 4. **Data Format**\n\n**No local features_all.jsonl exists locally.** The data is:\n- **Generated on remote servers** via LoRA fine-tuning pipelines (3 models × 3 decoding strategies × 4 depths)\n- **Format**: JSONL with 19 feature dimensions + depth label:\n  ```json\n  {\"mean_ppl\": 45.2, \"var_ppl\": 8.5, ..., \"rep_4gram\": 0.12, \"depth\": 1}\n  ```\n- **Raw text format**: `depth_0.jsonl`, `depth_1.jsonl`, etc. with `{\"text\": \"...\", \"depth\": k}`\n\n**Key data sources** (from memory.md & IDEA_BRIEF):\n- **Pythia-1.4B**: nucleus (78.2% acc), temp09 (76.3%), topk50 (69.6%)\n- **GPT-2 XL**: temp (85.4%), nucleus (83.3%)\n- **OLMo-1B**: nucleus (78.8%)\n\n### 5. **Existing DCOL Implementation**\n\n**Feature-based DCOL** (`artifacts/dcol_feature_mlp.py`, 400+ lines):\n- **Input**: 19-dim features (JSONL)\n- **Architecture**: MLP(19→128→64) + projection head (64→32, L2-norm) + classifier (64→4)\n- **Loss**: L_DCOL = L_attractive + L_repulsive + λ·L_CE\n- **Features**: BalancedDepthSampler for valid contrastive pairs\n\n**Text-based DCOL** (`artifacts/dcol_code/`):\n- `dcol_model.py`: DeBERTa-v3-large → CLS → Linear(1024→embed_dim) projection\n- Designed for raw text (not pre-extracted features)\n\n### 6. **Requirements & Dependencies**\n\n**No requirements.txt exists locally.** Based on imports across all scripts:\n\n```\nCore ML:\n  torch ≥ 2.0\n  transformers\n  scikit-learn\n  numpy, pandas\n  \nDistributed/Optimization:\n  accelerate\n  peft (for LoRA)\n  \nMonitoring:\n  wandb (weights & biases)\n  \nOptional:\n  flash-attn (for training speedup)\n```\n\n### 7. **Key Findings from Memory & Experiments**\n\n**MVP Results** (Pythia-1.4B nucleus):\n- **4-class accuracy**: 78.2% (95% CI: [76.9%, 79.4%])\n- **Adjacent AUC**: d0v1=0.998, d1v2=0.861, d2v3=0.801\n- **MAE**: 0.237\n- **Top features**: var_surprisal (rank 1-4), p90_ppl (rank 1-2)\n\n**Cross-Model Findings**:\n- **Signal strength is model-dependent**: Pythia nucleus > temp > topk; GPT-2 XL temp > nucleus > topk\n- **Feature consistency**: 6/6 experiments show same \"core 4\" features dominate (var_surprisal, p90_ppl, mean_surprisal, p75_ppl)\n- **Spearman rank correlation**: 0.79 average across models/strategies (highest within-model: 0.859)\n\n**Known Issues** (documented in memory.md):\n- DCOL v1 had margin collapse (margin_lr=1e-3 too high)\n- DCOL v2 suffered OOM from zombie processes\n- DivEye citation corrected: TMLR 2026 (not ICLR 2026)\n\n### 8. **Relevant File Paths**\n\n**Core Scripts**:\n- Utilities: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_utils.py`\n- Baselines: All in `scripts/baseline_*.py`\n- DCOL: `artifacts/dcol_feature_mlp.py` and `artifacts/dcol_code/`\n\n**Documentation**:\n- Project brief: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/IDEA_BRIEF.md`\n- Memory: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/memory.md`\n- Worker guide: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/CLAUDE.md`\n\n**Note**: There is **NO `src/classify.py`** file. The classification logic is distributed across multiple baseline scripts in `scripts/` and `artifacts/`."
      }
    ],
    "totalDurationMs": 71851,
    "totalTokens": 64424,
    "totalToolUseCount": 25,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 60154,
      "output_tokens": 2651,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1616
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2651,
          "cache_read_input_tokens": 60154,
          "cache_creation_input_tokens": 1616,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1616,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 13,
      "searchCount": 0,
      "bashCount": 12,
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

_source line 85_

<details><summary>Logged reasoning block</summary>

```text
The exploration reveals that there are already existing baseline implementations in `scripts/` directory. The task asks me to create `src/baselines.py` but the existing code is in `scripts/` and `artifacts/`. Let me read the key existing files to understand the current state and decide what needs to be done.

Key findings:
1. No `src/classify.py` exists - the task description is slightly outdated
2. Existing baselines already exist in `scripts/baseline_*.py`
3. `scripts/baseline_utils.py` has shared utilities
4. There's also `artifacts/baselines.py` which seems to be a unified framework


5. I need to examine the actual implementations to understand what's already been done and what consolidation or refactoring is needed
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "8f1c261c-d553-45a0-9def-8173f57bec04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0156TyoVouLj4Woqu89sRSJo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2877,
      "cache_read_input_tokens": 23600,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2877
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

_source line 86_

Existing baseline code already exists in `scripts/` and `artifacts/`. Let me read the key files to understand what's done vs. what needs updating.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "baa34e4f-8a14-4a54-9df2-bcbea8b822b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0156TyoVouLj4Woqu89sRSJo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2877,
      "cache_read_input_tokens": 23600,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2877
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

_source line 87_

<details open><summary>🔧 Tool call — Read · `toolu_01MVmpkx78hV2VeMpp7xceXd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_utils.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "faffdd7d-8375-442d-b907-5fe0a8d357ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0156TyoVouLj4Woqu89sRSJo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2877,
      "cache_read_input_tokens": 23600,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2877
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

_source line 88 · 2026-05-14T23:02:17.066Z_

<details><summary>↩ Tool result · `toolu_01MVmpkx78hV2VeMpp7xceXd`</summary>

```text
1	"""
2	Shared utilities for baseline battery experiments.
3	
4	Provides: data loading (raw JSONL + pre-extracted features), stratified splitting,
5	evaluation metrics (accuracy, MAE, pairwise AUC, classification report), and
6	standardized output saving.
7	"""
8	
9	import json
10	import os
11	import glob as glob_mod
12	import numpy as np
13	from collections import Counter
14	from sklearn.model_selection import train_test_split
15	from sklearn.metrics import (
16	    accuracy_score, classification_report, confusion_matrix, roc_auc_score,
17	)
18	
19	NUM_DEPTHS = 4
20	DEPTH_LABELS = list(range(NUM_DEPTHS))
21	
22	FEATURE_NAMES = [
23	    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
24	    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
25	    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
26	    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
27	    "rep_2gram", "rep_3gram", "rep_4gram",
28	]
29	NUM_FEATURES = len(FEATURE_NAMES)
30	
31	
32	# ── Data loading ──
33	
34	def load_jsonl_data(data_dirs, max_samples=0, seed=42):
35	    """Load raw text + depth labels from depth_*.jsonl files across directories."""
36	    texts, labels = [], []
37	    for data_dir in data_dirs:
38	        for d in range(NUM_DEPTHS):
39	            fpath = os.path.join(data_dir, f"depth_{d}.jsonl")
40	            if not os.path.exists(fpath):
41	                matches = glob_mod.glob(os.path.join(data_dir, f"*depth_{d}*.jsonl"))
42	                fpath = matches[0] if matches else None
43	            if fpath is None or not os.path.exists(fpath):
44	                continue
45	            with open(fpath) as f:
46	                for line in f:
47	                    line = line.strip()
48	                    if not line:
49	                        continue
50	                    rec = json.loads(line)
51	                    texts.append(rec["text"])
52	                    labels.append(rec.get("depth", d))
53	    labels = np.array(labels, dtype=np.int64)
54	    if max_samples > 0 and len(texts) > max_samples:
55	        rng = np.random.RandomState(seed)
56	        idx = sorted(rng.choice(len(texts), max_samples, replace=False))
57	        texts = [texts[i] for i in idx]
58	        labels = labels[idx]
59	    print(f"Loaded {len(texts)} samples. Depth distribution: {dict(Counter(labels))}")
60	    return texts, labels
61	
62	
63	def load_features(features_path):
64	    """Load pre-extracted 19-dim features from JSONL → (X [n, 19], y [n])."""
65	    records = []
66	    with open(features_path) as f:
67	        for line in f:
68	            line = line.strip()
69	            if line:
70	                records.append(json.loads(line))
71	    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)
72	    y = np.array([r["depth"] for r in records], dtype=np.int64)
73	    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
74	    print(f"Loaded features: {X.shape[0]} samples, {X.shape[1]} dims. "
75	          f"Depth distribution: {dict(Counter(y))}")
76	    return X, y
77	
78	
79	# ── Splitting ──
80	
81	def stratified_split(labels, eval_split=0.1, seed=42):
82	    """Return (train_idx, eval_idx) arrays with stratification."""
83	    train_idx, eval_idx = train_test_split(
84	        np.arange(len(labels)), test_size=eval_split,
85	        stratify=labels, random_state=seed,
86	    )
87	    return train_idx, eval_idx
88	
89	
90	# ── Evaluation ──
91	
92	def _pairwise_auc(y_true, y_prob, d1, d2):
93	    mask = np.isin(y_true, [d1, d2])
94	    if mask.sum() < 2:
95	        return None
96	    yt = (y_true[mask] == d2).astype(int)
97	    if len(np.unique(yt)) < 2:
98	        return None
99	    yp = y_prob[mask, d2]
100	    return float(roc_auc_score(yt, yp))
101	
102	
103	def compute_all_pairwise_auc(y_true, y_prob):
104	    result = {}
105	    for i, d1 in enumerate(DEPTH_LABELS):
106	        for d2 in DEPTH_LABELS[i + 1:]:
107	            auc = _pairwise_auc(y_true, y_prob, d1, d2)
108	            result[f"d{d1}_vs_d{d2}"] = round(auc, 4) if auc is not None else None
109	    return result
110	
111	
112	def evaluate_and_save(method_name, y_true, y_pred, y_prob, output_dir):
113	    """Compute all metrics, print summary, save three output files."""
114	    os.makedirs(output_dir, exist_ok=True)
115	    y_true = np.asarray(y_true)
116	    y_pred = np.asarray(y_pred)
117	
118	    acc = accuracy_score(y_true, y_pred)
119	    mae = float(np.mean(np.abs(y_true - y_pred)))
120	    cr_dict = classification_report(
121	        y_true, y_pred,
122	        target_names=[f"d{d}" for d in DEPTH_LABELS],
123	        output_dict=True, zero_division=0,
124	    )
125	    pair_aucs = compute_all_pairwise_auc(y_true, y_prob) if y_prob is not None else {}
126	
127	    print(f"\n{'=' * 50}")
128	    print(f"  {method_name}")
129	    print(f"{'=' * 50}")
130	    print(f"  Accuracy: {acc:.4f}   MAE: {mae:.4f}")
131	    if pair_aucs:
132	        print(f"  Pairwise AUC: {pair_aucs}")
133	    print(classification_report(
134	        y_true, y_pred,
135	        target_names=[f"d{d}" for d in DEPTH_LABELS], zero_division=0,
136	    ))
137	
138	    # 1) classification report
139	    report = {"accuracy": round(acc, 4), "mae": round(mae, 4), "per_class": cr_dict}
140	    _save_json(os.path.join(output_dir, f"{method_name}_classification_report.json"), report)
141	
142	    # 2) pairwise AUC
143	    _save_json(os.path.join(output_dir, f"{method_name}_pairwise_auc.json"), pair_aucs)
144	
145	    # 3) predictions
146	    preds = []
147	    for i in range(len(y_true)):
148	        entry = {"y_true": int(y_true[i]), "y_pred": int(y_pred[i])}
149	        if y_prob is not None:
150	            entry["y_prob"] = [round(float(p), 6) for p in y_prob[i]]
151	        preds.append(entry)
152	    _save_json(os.path.join(output_dir, f"{method_name}_predictions.json"), preds)
153	
154	    print(f"  Saved to {output_dir}/")
155	    return {"accuracy": acc, "mae": mae, "pairwise_auc": pair_aucs}
156	
157	
158	def _save_json(path, obj):
159	    with open(path, "w") as f:
160	        json.dump(obj, f, indent=2)
161	
162	
163	def add_common_args(parser):
164	    """Add the unified CLI arguments shared across all baselines."""
165	    parser.add_argument("--data_dirs", nargs="+", default=["data/"],
166	                        help="Directories containing depth_*.jsonl files")
167	    parser.add_argument("--features_path", default=None,
168	                        help="Path to pre-extracted features JSONL (for feature-based methods)")
169	    parser.add_argument("--output_dir", default="results/baselines/")
170	    parser.add_argument("--seed", type=int, default=42)
171	    parser.add_argument("--eval_split", type=float, default=0.1)
172	    parser.add_argument("--max_seq_len", type=int, default=512)
173	    parser.add_argument("--max_samples", type=int, default=0,
174	                        help="Max total samples to use (0 = all)")
175	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "39120e25-777b-471a-81e1-8832393bcc84",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_utils.py",
      "content": "\"\"\"\nShared utilities for baseline battery experiments.\n\nProvides: data loading (raw JSONL + pre-extracted features), stratified splitting,\nevaluation metrics (accuracy, MAE, pairwise AUC, classification report), and\nstandardized output saving.\n\"\"\"\n\nimport json\nimport os\nimport glob as glob_mod\nimport numpy as np\nfrom collections import Counter\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.metrics import (\n    accuracy_score, classification_report, confusion_matrix, roc_auc_score,\n)\n\nNUM_DEPTHS = 4\nDEPTH_LABELS = list(range(NUM_DEPTHS))\n\nFEATURE_NAMES = [\n    \"mean_ppl\", \"var_ppl\", \"skewness_ppl\", \"kurtosis_ppl\",\n    \"p10_ppl\", \"p25_ppl\", \"p50_ppl\", \"p75_ppl\", \"p90_ppl\",\n    \"mean_surprisal\", \"var_surprisal\", \"entropy_of_surprisal\",\n    \"type_token_ratio\", \"hapax_ratio\", \"bigram_entropy\", \"trigram_entropy\",\n    \"rep_2gram\", \"rep_3gram\", \"rep_4gram\",\n]\nNUM_FEATURES = len(FEATURE_NAMES)\n\n\n# ── Data loading ──\n\ndef load_jsonl_data(data_dirs, max_samples=0, seed=42):\n    \"\"\"Load raw text + depth labels from depth_*.jsonl files across directories.\"\"\"\n    texts, labels = [], []\n    for data_dir in data_dirs:\n        for d in range(NUM_DEPTHS):\n            fpath = os.path.join(data_dir, f\"depth_{d}.jsonl\")\n            if not os.path.exists(fpath):\n                matches = glob_mod.glob(os.path.join(data_dir, f\"*depth_{d}*.jsonl\"))\n                fpath = matches[0] if matches else None\n            if fpath is None or not os.path.exists(fpath):\n                continue\n            with open(fpath) as f:\n                for line in f:\n                    line = line.strip()\n                    if not line:\n                        continue\n                    rec = json.loads(line)\n                    texts.append(rec[\"text\"])\n                    labels.append(rec.get(\"depth\", d))\n    labels = np.array(labels, dtype=np.int64)\n    if max_samples > 0 and len(texts) > max_samples:\n        rng = np.random.RandomState(seed)\n        idx = sorted(rng.choice(len(texts), max_samples, replace=False))\n        texts = [texts[i] for i in idx]\n        labels = labels[idx]\n    print(f\"Loaded {len(texts)} samples. Depth distribution: {dict(Counter(labels))}\")\n    return texts, labels\n\n\ndef load_features(features_path):\n    \"\"\"Load pre-extracted 19-dim features from JSONL → (X [n, 19], y [n]).\"\"\"\n    records = []\n    with open(features_path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                records.append(json.loads(line))\n    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)\n    y = np.array([r[\"depth\"] for r in records], dtype=np.int64)\n    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)\n    print(f\"Loaded features: {X.shape[0]} samples, {X.shape[1]} dims. \"\n          f\"Depth distribution: {dict(Counter(y))}\")\n    return X, y\n\n\n# ── Splitting ──\n\ndef stratified_split(labels, eval_split=0.1, seed=42):\n    \"\"\"Return (train_idx, eval_idx) arrays with stratification.\"\"\"\n    train_idx, eval_idx = train_test_split(\n        np.arange(len(labels)), test_size=eval_split,\n        stratify=labels, random_state=seed,\n    )\n    return train_idx, eval_idx\n\n\n# ── Evaluation ──\n\ndef _pairwise_auc(y_true, y_prob, d1, d2):\n    mask = np.isin(y_true, [d1, d2])\n    if mask.sum() < 2:\n        return None\n    yt = (y_true[mask] == d2).astype(int)\n    if len(np.unique(yt)) < 2:\n        return None\n    yp = y_prob[mask, d2]\n    return float(roc_auc_score(yt, yp))\n\n\ndef compute_all_pairwise_auc(y_true, y_prob):\n    result = {}\n    for i, d1 in enumerate(DEPTH_LABELS):\n        for d2 in DEPTH_LABELS[i + 1:]:\n            auc = _pairwise_auc(y_true, y_prob, d1, d2)\n            result[f\"d{d1}_vs_d{d2}\"] = round(auc, 4) if auc is not None else None\n    return result\n\n\ndef evaluate_and_save(method_name, y_true, y_pred, y_prob, output_dir):\n    \"\"\"Compute all metrics, print summary, save three output files.\"\"\"\n    os.makedirs(output_dir, exist_ok=True)\n    y_true = np.asarray(y_true)\n    y_pred = np.asarray(y_pred)\n\n    acc = accuracy_score(y_true, y_pred)\n    mae = float(np.mean(np.abs(y_true - y_pred)))\n    cr_dict = classification_report(\n        y_true, y_pred,\n        target_names=[f\"d{d}\" for d in DEPTH_LABELS],\n        output_dict=True, zero_division=0,\n    )\n    pair_aucs = compute_all_pairwise_auc(y_true, y_prob) if y_prob is not None else {}\n\n    print(f\"\\n{'=' * 50}\")\n    print(f\"  {method_name}\")\n    print(f\"{'=' * 50}\")\n    print(f\"  Accuracy: {acc:.4f}   MAE: {mae:.4f}\")\n    if pair_aucs:\n        print(f\"  Pairwise AUC: {pair_aucs}\")\n    print(classification_report(\n        y_true, y_pred,\n        target_names=[f\"d{d}\" for d in DEPTH_LABELS], zero_division=0,\n    ))\n\n    # 1) classification report\n    report = {\"accuracy\": round(acc, 4), \"mae\": round(mae, 4), \"per_class\": cr_dict}\n    _save_json(os.path.join(output_dir, f\"{method_name}_classification_report.json\"), report)\n\n    # 2) pairwise AUC\n    _save_json(os.path.join(output_dir, f\"{method_name}_pairwise_auc.json\"), pair_aucs)\n\n    # 3) predictions\n    preds = []\n    for i in range(len(y_true)):\n        entry = {\"y_true\": int(y_true[i]), \"y_pred\": int(y_pred[i])}\n        if y_prob is not None:\n            entry[\"y_prob\"] = [round(float(p), 6) for p in y_prob[i]]\n        preds.append(entry)\n    _save_json(os.path.join(output_dir, f\"{method_name}_predictions.json\"), preds)\n\n    print(f\"  Saved to {output_dir}/\")\n    return {\"accuracy\": acc, \"mae\": mae, \"pairwise_auc\": pair_aucs}\n\n\ndef _save_json(path, obj):\n    with open(path, \"w\") as f:\n        json.dump(obj, f, indent=2)\n\n\ndef add_common_args(parser):\n    \"\"\"Add the unified CLI arguments shared across all baselines.\"\"\"\n    parser.add_argument(\"--data_dirs\", nargs=\"+\", default=[\"data/\"],\n                        help=\"Directories containing depth_*.jsonl files\")\n    parser.add_argument(\"--features_path\", default=None,\n                        help=\"Path to pre-extracted features JSONL (for feature-based methods)\")\n    parser.add_argument(\"--output_dir\", default=\"results/baselines/\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--eval_split\", type=float, default=0.1)\n    parser.add_argument(\"--max_seq_len\", type=int, default=512)\n    parser.add_argument(\"--max_samples\", type=int, default=0,\n                        help=\"Max total samples to use (0 = all)\")\n",
      "numLines": 175,
      "startLine": 1,
      "totalLines": 175
    }
  }
}
```

</details>

---


### Tool call

_source line 89_

<details open><summary>🔧 Tool call — Read · `toolu_018br6mRsgFF6q2Yw8VUMGAF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/baselines.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "0f735671-1f46-46f7-9025-3ae7b92541d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0156TyoVouLj4Woqu89sRSJo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2877,
      "cache_read_input_tokens": 23600,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2877
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

_source line 90 · 2026-05-14T23:02:17.785Z_

<details><summary>↩ Tool result · `toolu_018br6mRsgFF6q2Yw8VUMGAF`</summary>

```text
1	"""
2	Baseline battery for recursive generation depth estimation.
3	
4	Baselines:
5	  1. PPLRegressionBaseline  — OLS regression on mean_ppl (single) or all 19 features (multi)
6	  2. CEClassificationBaseline — MLP with cross-entropy loss (DCOL ablation, no contrastive loss)
7	  3. CORALBaseline — Ordinal regression with K-1 binary classifiers (Cao et al., 2020)
8	  4. DivEyeBaseline — Surprisal diversity features + XGBoost (Basani & Chen, TMLR 2026)
9	
10	Usage:
11	  python src/baselines.py --method ppl_reg --features_path data/features_all.jsonl
12	  python src/baselines.py --method ce_mlp  --features_path data/features_all.jsonl --epochs 50
13	  python src/baselines.py --method coral   --features_path data/features_all.jsonl --epochs 50
14	  python src/baselines.py --method diveye  --features_path data/features_all.jsonl
15	  python src/baselines.py --method all     --features_path data/features_all.jsonl --epochs 50
16	"""
17	
18	import argparse
19	import json
20	import os
21	import sys
22	import numpy as np
23	from collections import Counter
24	
25	import torch
26	import torch.nn as nn
27	import torch.optim as optim
28	from torch.utils.data import DataLoader, TensorDataset
29	
30	from sklearn.linear_model import LinearRegression
31	from sklearn.preprocessing import StandardScaler
32	from sklearn.model_selection import train_test_split
33	from sklearn.metrics import (
34	    accuracy_score, confusion_matrix, classification_report, roc_auc_score,
35	)
36	
37	# ── Feature schema (must match extract_features.py / dcol_dataset.py) ──
38	
39	FEATURE_NAMES = [
40	    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
41	    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
42	    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
43	    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
44	    "rep_2gram", "rep_3gram", "rep_4gram",
45	]
46	NUM_FEATURES = len(FEATURE_NAMES)
47	NUM_DEPTHS = 4
48	DEPTH_LABELS = list(range(NUM_DEPTHS))
49	
50	# ── Data loading ──
51	
52	def load_features(path):
53	    """Load JSONL features file → (X [n, 19], y [n])."""
54	    records = []
55	    with open(path) as f:
56	        for line in f:
57	            line = line.strip()
58	            if line:
59	                records.append(json.loads(line))
60	    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)
61	    y = np.array([r["depth"] for r in records], dtype=np.int64)
62	    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
63	    return X, y
64	
65	
66	def prepare_splits(X, y, test_size=0.15, val_size=0.15, seed=42):
67	    idx = np.arange(len(y))
68	    train_val_idx, test_idx = train_test_split(
69	        idx, test_size=test_size, stratify=y, random_state=seed
70	    )
71	    rel_val = val_size / (1 - test_size)
72	    train_idx, val_idx = train_test_split(
73	        train_val_idx, test_size=rel_val,
74	        stratify=y[train_val_idx], random_state=seed
75	    )
76	    return (
77	        X[train_idx], y[train_idx],
78	        X[val_idx], y[val_idx],
79	        X[test_idx], y[test_idx],
80	    )
81	
82	# ── Evaluation metrics ──
83	
84	def pairwise_auc(y_true, y_prob, d1, d2):
85	    mask = np.isin(y_true, [d1, d2])
86	    if mask.sum() < 2:
87	        return None
88	    yt = (y_true[mask] == d2).astype(int)
89	    if len(np.unique(yt)) < 2:
90	        return None
91	    yp = y_prob[mask, d2]
92	    return float(roc_auc_score(yt, yp))
93	
94	
95	def compute_all_pairwise_auc(y_true, y_prob):
96	    result = {}
97	    for i, d1 in enumerate(DEPTH_LABELS):
98	        for d2 in DEPTH_LABELS[i + 1:]:
99	            auc = pairwise_auc(y_true, y_prob, d1, d2)
100	            result[f"d{d1}_vs_d{d2}"] = round(auc, 4) if auc is not None else None
101	    return result
102	
103	
104	def bootstrap_ci(y_true, y_pred, metric_fn=accuracy_score, n_boot=1000, seed=42):
105	    rng = np.random.RandomState(seed)
106	    scores = []
107	    n = len(y_true)
108	    for _ in range(n_boot):
109	        idx = rng.choice(n, n, replace=True)
110	        scores.append(metric_fn(y_true[idx], y_pred[idx]))
111	    lo = float(np.percentile(scores, 2.5))
112	    hi = float(np.percentile(scores, 97.5))
113	    return lo, hi
114	
115	
116	def evaluate(name, y_true, y_pred, y_prob=None):
117	    """Print and return evaluation metrics."""
118	    acc4 = accuracy_score(y_true, y_pred)
119	    ci_lo, ci_hi = bootstrap_ci(y_true, y_pred)
120	
121	    # 3-class accuracy (depth 1-3 only)
122	    mask_13 = y_true >= 1
123	    acc3 = accuracy_score(y_true[mask_13], y_pred[mask_13]) if mask_13.sum() > 0 else 0.0
124	
125	    mae = float(np.mean(np.abs(y_true - y_pred)))
126	
127	    cm = confusion_matrix(y_true, y_pred, labels=DEPTH_LABELS)
128	    per_class_recall = cm.diagonal() / cm.sum(axis=1).clip(min=1)
129	
130	    pair_aucs = {}
131	    if y_prob is not None:
132	        pair_aucs = compute_all_pairwise_auc(y_true, y_prob)
133	
134	    print(f"\n{'='*60}")
135	    print(f"  {name}")
136	    print(f"{'='*60}")
137	    print(f"  4-class accuracy : {acc4:.4f}  (95% CI: [{ci_lo:.4f}, {ci_hi:.4f}])")
138	    print(f"  3-class accuracy : {acc3:.4f}  (d1-d3 only)")
139	    print(f"  MAE              : {mae:.4f}")
140	    print(f"  Per-class recall : {dict(zip([f'd{d}' for d in DEPTH_LABELS], [round(r,4) for r in per_class_recall]))}")
141	    if pair_aucs:
142	        print(f"  Pairwise AUC     : {pair_aucs}")
143	    print(f"\n  Confusion matrix:")
144	    print(f"  {'':>8s}", " ".join(f"pred-{d}" for d in DEPTH_LABELS))
145	    for i, d in enumerate(DEPTH_LABELS):
146	        print(f"  true-{d}  ", " ".join(f"{cm[i,j]:6d}" for j in range(NUM_DEPTHS)))
147	
148	    cr = classification_report(
149	        y_true, y_pred,
150	        target_names=[f"depth-{d}" for d in DEPTH_LABELS],
151	        zero_division=0,
152	    )
153	    print(f"\n{cr}")
154	
155	    return {
156	        "method": name,
157	        "acc_4class": round(acc4, 4),
158	        "acc_4class_ci": [round(ci_lo, 4), round(ci_hi, 4)],
159	        "acc_3class": round(acc3, 4),
160	        "mae": round(mae, 4),
161	        "per_class_recall": {f"d{d}": round(r, 4) for d, r in zip(DEPTH_LABELS, per_class_recall)},
162	        "pairwise_auc": pair_aucs,
163	    }
164	
165	
166	# ═══════════════════════════════════════════════════════════════════════
167	#  Baseline 1: PPL Regression
168	# ═══════════════════════════════════════════════════════════════════════
169	
170	class PPLRegressionBaseline:
171	    """
172	    Linear regression → round to nearest depth.
173	
174	    Single-feature mode: depth = a * mean_ppl + b
175	    Multi-feature mode:  depth = X @ w + b  (19-dim OLS)
176	
177	    Simplest possible baseline. If mean_ppl alone suffices, complex models are
178	    unnecessary.
179	    """
180	
181	    def __init__(self, mode="multi"):
182	        self.mode = mode  # "single" or "multi"
183	        self.scaler = StandardScaler()
184	        self.model = LinearRegression()
185	
186	    def _select(self, X):
187	        if self.mode == "single":
188	            idx = FEATURE_NAMES.index("mean_ppl")
189	            return X[:, idx:idx+1]
190	        return X
191	
192	    def fit(self, X_train, y_train):
193	        Xs = self._select(X_train)
194	        Xs = self.scaler.fit_transform(Xs)
195	        self.model.fit(Xs, y_train.astype(np.float64))
196	
197	    def predict(self, X_test):
198	        Xs = self._select(X_test)
199	        Xs = self.scaler.transform(Xs)
200	        raw = self.model.predict(Xs)
201	        return np.clip(np.round(raw).astype(int), 0, NUM_DEPTHS - 1)
202	
203	    def predict_proba(self, X_test):
204	        preds = self.predict(X_test)
205	        prob = np.zeros((len(preds), NUM_DEPTHS))
206	        for i, p in enumerate(preds):
207	            prob[i, p] = 1.0
208	        return prob
209	
210	
211	# ═══════════════════════════════════════════════════════════════════════
212	#  Baseline 2: Cross-Entropy MLP (DCOL ablation)
213	# ═══════════════════════════════════════════════════════════════════════
214	
215	class _CEMLP(nn.Module):
216	    """19 → 128 → 64 → 4  with ReLU + dropout. Same architecture as DCOL's
217	    feature head, but trained with CE loss only (no contrastive loss)."""
218	
219	    def __init__(self, input_dim=NUM_FEATURES, hidden1=128, hidden2=64,
220	                 num_classes=NUM_DEPTHS, dropout=0.3):
221	        super().__init__()
222	        self.net = nn.Sequential(
223	            nn.Linear(input_dim, hidden1),
224	            nn.ReLU(),
225	            nn.Dropout(dropout),
226	            nn.Linear(hidden1, hidden2),
227	            nn.ReLU(),
228	            nn.Dropout(dropout),
229	            nn.Linear(hidden2, num_classes),
230	        )
231	
232	    def forward(self, x):
233	        return self.net(x)
234	
235	
236	class CEClassificationBaseline:
237	    """
238	    Standard multi-class MLP with cross-entropy loss.
239	
240	    Architecture identical to DCOL's feature classifier head (19→128→64→4)
241	    but uses only CE loss — no contrastive learning.
242	    This is the key ablation: if CE-MLP matches DCOL, the contrastive loss
243	    adds no value.
244	    """
245	
246	    def __init__(self, lr=1e-3, epochs=100, batch_size=256, patience=10,
247	                 device=None, seed=42):
248	        self.lr = lr
249	        self.epochs = epochs
250	        self.batch_size = batch_size
251	        self.patience = patience
252	        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
253	        self.seed = seed
254	        self.scaler = StandardScaler()
255	        self.model = None
256	
257	    def fit(self, X_train, y_train, X_val=None, y_val=None):
258	        torch.manual_seed(self.seed)
259	        np.random.seed(self.seed)
260	
261	        X_s = self.scaler.fit_transform(X_train).astype(np.float32)
262	        Xt = torch.tensor(X_s, device=self.device)
263	        yt = torch.tensor(y_train, dtype=torch.long, device=self.device)
264	        ds = TensorDataset(Xt, yt)
265	        loader = DataLoader(ds, batch_size=self.batch_size, shuffle=True)
266	
267	        self.model = _CEMLP().to(self.device)
268	        optimizer = optim.Adam(self.model.parameters(), lr=self.lr, weight_decay=1e-4)
269	        criterion = nn.CrossEntropyLoss()
270	
271	        best_loss = float("inf")
272	        wait = 0
273	        best_state = None
274	
275	        has_val = X_val is not None and y_val is not None
276	        if has_val:
277	            Xv = torch.tensor(self.scaler.transform(X_val).astype(np.float32),
278	                              device=self.device)
279	            yv = torch.tensor(y_val, dtype=torch.long, device=self.device)
280	
281	        for epoch in range(self.epochs):
282	            self.model.train()
283	            epoch_loss = 0.0
284	            for xb, yb in loader:
285	                optimizer.zero_grad()
286	                logits = self.model(xb)
287	                loss = criterion(logits, yb)
288	                loss.backward()
289	                optimizer.step()
290	                epoch_loss += loss.item() * len(xb)
291	            epoch_loss /= len(ds)
292	
293	            if has_val:
294	                self.model.eval()
295	                with torch.no_grad():
296	                    val_logits = self.model(Xv)
297	                    val_loss = criterion(val_logits, yv).item()
298	            else:
299	                val_loss = epoch_loss
300	
301	            if val_loss < best_loss - 1e-4:
302	                best_loss = val_loss
303	                best_state = {k: v.clone() for k, v in self.model.state_dict().items()}
304	                wait = 0
305	            else:
306	                wait += 1
307	                if wait >= self.patience:
308	                    break
309	
310	        if best_state is not None:
311	            self.model.load_state_dict(best_state)
312	
313	    def predict(self, X_test):
314	        self.model.eval()
315	        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),
316	                           device=self.device)
317	        with torch.no_grad():
318	            logits = self.model(X_s)
319	        return logits.argmax(dim=-1).cpu().numpy()
320	
321	    def predict_proba(self, X_test):
322	        self.model.eval()
323	        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),
324	                           device=self.device)
325	        with torch.no_grad():
326	            logits = self.model(X_s)
327	            probs = torch.softmax(logits, dim=-1)
328	        return probs.cpu().numpy()
329	
330	
331	# ═══════════════════════════════════════════════════════════════════════
332	#  Baseline 3: CORAL Ordinal Regression
333	# ═══════════════════════════════════════════════════════════════════════
334	
335	class _CORALNet(nn.Module):
336	    """
337	    CORAL ordinal regression (Cao et al., 2020, "Rank consistent ordinal
338	    regression for neural networks with consistent confidence sets").
339	
340	    Architecture: 19 → 128 → 64 → shared representation, then K-1 = 3
341	    independent sigmoid heads.
342	
343	    Each head k answers: P(depth > k).
344	    Prediction: depth = sum_k I[P(depth > k) > 0.5].
345	
346	    Loss (rank-consistent):
347	        L = sum_{k=0}^{K-2} BCE(sigmoid(w_k^T h + b_k), I[y > k])
348	
349	    Weight sharing across heads ensures rank consistency: predictions are
350	    monotonically decreasing in threshold order.
351	    """
352	
353	    def __init__(self, input_dim=NUM_FEATURES, hidden1=128, hidden2=64,
354	                 num_classes=NUM_DEPTHS, dropout=0.3):
355	        super().__init__()
356	        self.num_classes = num_classes
357	        self.backbone = nn.Sequential(
358	            nn.Linear(input_dim, hidden1),
359	            nn.ReLU(),
360	            nn.Dropout(dropout),
361	            nn.Linear(hidden1, hidden2),
362	            nn.ReLU(),
363	            nn.Dropout(dropout),
364	        )
365	        # K-1 independent binary heads (shared backbone, separate bias)
366	        self.fc = nn.Linear(hidden2, 1, bias=False)
367	        self.biases = nn.Parameter(torch.zeros(num_classes - 1))
368	
369	    def forward(self, x):
370	        h = self.backbone(x)             # [B, 64]
371	        logit_base = self.fc(h)          # [B, 1]
372	        # broadcast: [B, K-1]
373	        logits = logit_base + self.biases # each head shares weight, different bias
374	        return logits
375	
376	
377	class CORALBaseline:
378	    """
379	    CORAL ordinal regression for depth estimation.
380	
381	    Ref: Cao, Mirjalili & Raschka (2020). "Rank consistent ordinal regression
382	    for neural networks with consistent confidence sets." Pattern Recognition.
383	
384	    Exploits ordinal structure: depth 0 < 1 < 2 < 3.
385	    Alternative to DCOL's contrastive approach for leveraging label ordering.
386	    """
387	
388	    def __init__(self, lr=1e-3, epochs=100, batch_size=256, patience=10,
389	                 device=None, seed=42):
390	        self.lr = lr
391	        self.epochs = epochs
392	        self.batch_size = batch_size
393	        self.patience = patience
394	        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
395	        self.seed = seed
396	        self.scaler = StandardScaler()
397	        self.model = None
398	
399	    @staticmethod
400	    def _encode_ordinal(y, num_classes):
401	        """Convert class labels to K-1 binary ordinal targets.
402	        y=2, K=4 → [1, 1, 0]  (depth > 0? yes, depth > 1? yes, depth > 2? no)
403	        """
404	        n = len(y)
405	        targets = np.zeros((n, num_classes - 1), dtype=np.float32)
406	        for k in range(num_classes - 1):
407	            targets[:, k] = (y > k).astype(np.float32)
408	        return targets
409	
410	    def fit(self, X_train, y_train, X_val=None, y_val=None):
411	        torch.manual_seed(self.seed)
412	        np.random.seed(self.seed)
413	
414	        X_s = self.scaler.fit_transform(X_train).astype(np.float32)
415	        ord_targets = self._encode_ordinal(y_train, NUM_DEPTHS)
416	
417	        Xt = torch.tensor(X_s, device=self.device)
418	        ot = torch.tensor(ord_targets, device=self.device)
419	        ds = TensorDataset(Xt, ot)
420	        loader = DataLoader(ds, batch_size=self.batch_size, shuffle=True)
421	
422	        self.model = _CORALNet().to(self.device)
423	        optimizer = optim.Adam(self.model.parameters(), lr=self.lr, weight_decay=1e-4)
424	        criterion = nn.BCEWithLogitsLoss()
425	
426	        best_loss = float("inf")
427	        wait = 0
428	        best_state = None
429	
430	        has_val = X_val is not None and y_val is not None
431	        if has_val:
432	            Xv = torch.tensor(self.scaler.transform(X_val).astype(np.float32),
433	                              device=self.device)
434	            ov = torch.tensor(self._encode_ordinal(y_val, NUM_DEPTHS),
435	                              device=self.device)
436	
437	        for epoch in range(self.epochs):
438	            self.model.train()
439	            epoch_loss = 0.0
440	            for xb, ob in loader:
441	                optimizer.zero_grad()
442	                logits = self.model(xb)
443	                loss = criterion(logits, ob)
444	                loss.backward()
445	                optimizer.step()
446	                epoch_loss += loss.item() * len(xb)
447	            epoch_loss /= len(ds)
448	
449	            if has_val:
450	                self.model.eval()
451	                with torch.no_grad():
452	                    val_logits = self.model(Xv)
453	                    val_loss = criterion(val_logits, ov).item()
454	            else:
455	                val_loss = epoch_loss
456	
457	            if val_loss < best_loss - 1e-4:
458	                best_loss = val_loss
459	                best_state = {k: v.clone() for k, v in self.model.state_dict().items()}
460	                wait = 0
461	            else:
462	                wait += 1
463	                if wait >= self.patience:
464	                    break
465	
466	        if best_state is not None:
467	            self.model.load_state_dict(best_state)
468	
469	    def predict(self, X_test):
470	        self.model.eval()
471	        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),
472	                           device=self.device)
473	        with torch.no_grad():
474	            logits = self.model(X_s)
475	            probs = torch.sigmoid(logits)  # [B, K-1], P(depth > k)
476	        # depth = number of thresholds exceeded
477	        preds = (probs > 0.5).sum(dim=-1).cpu().numpy().astype(int)
478	        return preds
479	
480	    def predict_proba(self, X_test):
481	        """Convert cumulative probabilities to per-class probabilities.
482	        P(depth=k) = P(depth>k-1) - P(depth>k), with boundary conditions.
483	        """
484	        self.model.eval()
485	        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),
486	                           device=self.device)
487	        with torch.no_grad():
488	            logits = self.model(X_s)
489	            cum_probs = torch.sigmoid(logits).cpu().numpy()  # [B, K-1]
490	
491	        n = len(X_test)
492	        probs = np.zeros((n, NUM_DEPTHS))
493	        # P(depth=0) = 1 - P(depth>0)
494	        probs[:, 0] = 1.0 - cum_probs[:, 0]
495	        # P(depth=k) = P(depth>k-1) - P(depth>k) for k=1..K-2
496	        for k in range(1, NUM_DEPTHS - 1):
497	            probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]
498	        # P(depth=K-1) = P(depth>K-2)
499	        probs[:, NUM_DEPTHS - 1] = cum_probs[:, NUM_DEPTHS - 2]
500	        probs = np.clip(probs, 0, 1)
501	        row_sums = probs.sum(axis=1, keepdims=True)
502	        probs = probs / np.where(row_sums > 0, row_sums, 1.0)
503	        return probs
504	
505	
506	# ═══════════════════════════════════════════════════════════════════════
507	#  Baseline 4: DivEye (Surprisal Diversity + XGBoost)
508	# ═══════════════════════════════════════════════════════════════════════
509	
510	# DivEye feature groups mapped to our 19 features:
511	#   Distributional: mean_ppl, var_ppl, skewness_ppl, kurtosis_ppl → matches
512	#                   DivEye's mean/var/skewness/kurtosis of surprisal
513	#   Surprisal:      mean_surprisal, var_surprisal, entropy_of_surprisal
514	#   Lexical diversity: type_token_ratio, hapax_ratio, bigram_entropy, trigram_entropy
515	#   Repetition:     rep_2gram, rep_3gram, rep_4gram
516	#
517	# TODO: DivEye's temporal features (first-order ∆S and second-order ∆²S,
518	#       computed from per-token surprisal sequences) are not available in our
519	#       pre-computed features. Full DivEye reproduction requires raw token-level
520	#       surprisal; these summary statistics are a proxy.
521	
522	DIVEYE_FEATURE_INDICES = [
523	    FEATURE_NAMES.index(f) for f in [
524	        "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
525	        "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
526	        "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
527	        "rep_2gram", "rep_3gram", "rep_4gram",
528	    ]
529	]
530	
531	
532	class DivEyeBaseline:
533	    """
534	    DivEye-style detection adapted for depth estimation.
535	
536	    Ref: Basani, A. R. & Chen, P.-Y. (2026). Diversity Boosts AI-Generated Text Detection. Transactions on Machine Learning Research (TMLR).
537	    GitHub: https://github.com/IBM/diveye
538	
539	    DivEye's insight: human text has higher surprisal diversity (distributional,
540	    first-order temporal ∆S, second-order ∆²S). We adapt this to depth estimation:
541	    deeper recursive generations should have *lower* diversity.
542	
543	    Implementation: XGBoost on surprisal-related feature subset (14 of 19 features).
544	    Full DivEye also uses first/second-order temporal surprisal features from raw
545	    token sequences — those are not available in our pre-extracted features.
546	    """
547	
548	    def __init__(self, seed=42):
549	        self.seed = seed
550	        self.model = None
551	
552	    def fit(self, X_train, y_train, **kwargs):
553	        try:
554	            from xgboost import XGBClassifier
555	        except ImportError:
556	            print("[ERROR] xgboost not installed. Run: pip install xgboost")
557	            sys.exit(1)
558	
559	        Xd = X_train[:, DIVEYE_FEATURE_INDICES]
560	        self.model = XGBClassifier(
561	            n_estimators=200,
562	            max_depth=6,
563	            learning_rate=0.1,
564	            subsample=0.8,
565	            colsample_bytree=0.8,
566	            random_state=self.seed,
567	            use_label_encoder=False,
568	            eval_metric="mlogloss",
569	            verbosity=0,
570	        )
571	        self.model.fit(Xd, y_train)
572	
573	    def predict(self, X_test):
574	        Xd = X_test[:, DIVEYE_FEATURE_INDICES]
575	        return self.model.predict(Xd)
576	
577	    def predict_proba(self, X_test):
578	        Xd = X_test[:, DIVEYE_FEATURE_INDICES]
579	        probs = self.model.predict_proba(Xd)
580	        # Ensure output is [n, NUM_DEPTHS] even if some classes are missing
581	        if probs.shape[1] < NUM_DEPTHS:
582	            full = np.zeros((probs.shape[0], NUM_DEPTHS))
583	            for i, c in enumerate(self.model.classes_):
584	                full[:, c] = probs[:, i]
585	            return full
586	        return probs
587	
588	
589	# ═══════════════════════════════════════════════════════════════════════
590	#  Unified Runner
591	# ═══════════════════════════════════════════════════════════════════════
592	
593	BASELINE_REGISTRY = {
594	    "ppl_reg_single": ("PPL Regression (single: mean_ppl)", lambda: PPLRegressionBaseline(mode="single")),
595	    "ppl_reg":        ("PPL Regression (multi: 19-dim OLS)", lambda: PPLRegressionBaseline(mode="multi")),
596	    "ce_mlp":         ("CE-MLP (DCOL ablation)", None),  # needs args
597	    "coral":          ("CORAL Ordinal Regression", None),
598	    "diveye":         ("DivEye (XGBoost)", lambda: DivEyeBaseline()),
599	}
600	
601	
602	def run_baseline(method, X_train, y_train, X_val, y_val, X_test, y_test, args):
603	    if method == "ppl_reg_single":
604	        bl = PPLRegressionBaseline(mode="single")
605	        bl.fit(X_train, y_train)
606	    elif method == "ppl_reg":
607	        bl = PPLRegressionBaseline(mode="multi")
608	        bl.fit(X_train, y_train)
609	    elif method == "ce_mlp":
610	        bl = CEClassificationBaseline(
611	            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,
612	            patience=args.patience, seed=args.seed,
613	        )
614	        bl.fit(X_train, y_train, X_val, y_val)
615	    elif method == "coral":
616	        bl = CORALBaseline(
617	            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,
618	            patience=args.patience, seed=args.seed,
619	        )
620	        bl.fit(X_train, y_train, X_val, y_val)
621	    elif method == "diveye":
622	        bl = DivEyeBaseline(seed=args.seed)
623	        bl.fit(X_train, y_train)
624	    else:
625	        print(f"Unknown method: {method}")
626	        return None
627	
628	    y_pred = bl.predict(X_test)
629	    y_prob = bl.predict_proba(X_test)
630	    name = BASELINE_REGISTRY.get(method, (method, None))[0]
631	    return evaluate(name, y_test, y_pred, y_prob)
632	
633	
634	def parse_args():
635	    p = argparse.ArgumentParser(description="Baseline battery for depth estimation.")
636	    p.add_argument("--method", default="all",
637	                   choices=["ppl_reg_single", "ppl_reg", "ce_mlp", "coral", "diveye", "all"])
638	    p.add_argument("--features_path", default="data/features_all.jsonl")
639	    p.add_argument("--output_dir", default="results/baselines/")
640	    p.add_argument("--seed", type=int, default=42)
641	    p.add_argument("--test_size", type=float, default=0.15)
642	    p.add_argument("--val_size", type=float, default=0.15)
643	    p.add_argument("--epochs", type=int, default=100)
644	    p.add_argument("--batch_size", type=int, default=256)
645	    p.add_argument("--lr", type=float, default=1e-3)
646	    p.add_argument("--patience", type=int, default=10)
647	    return p.parse_args()
648	
649	
650	def main():
651	    args = parse_args()
652	    print(f"Loading features from {args.features_path} ...")
653	    X, y = load_features(args.features_path)
654	    print(f"  {X.shape[0]} samples, {X.shape[1]} features")
655	    print(f"  Depth distribution: {dict(Counter(y))}")
656	
657	    X_train, y_train, X_val, y_val, X_test, y_test = prepare_splits(
658	        X, y, test_size=args.test_size, val_size=args.val_size, seed=args.seed
659	    )
660	    print(f"  Train: {len(y_train)}, Val: {len(y_val)}, Test: {len(y_test)}")
661	
662	    methods = list(BASELINE_REGISTRY.keys()) if args.method == "all" else [args.method]
663	    all_results = {}
664	
665	    for m in methods:
666	        result = run_baseline(m, X_train, y_train, X_val, y_val, X_test, y_test, args)
667	        if result is not None:
668	            all_results[m] = result
669	
670	    # Summary table
671	    if len(all_results) > 1:
672	        print(f"\n{'='*60}")
673	        print(f"  SUMMARY")
674	        print(f"{'='*60}")
675	        print(f"  {'Method':<35s} {'4-cls':>6s} {'3-cls':>6s} {'MAE':>6s}")
676	        print(f"  {'-'*35} {'-'*6} {'-'*6} {'-'*6}")
677	        for m, r in all_results.items():
678	            print(f"  {r['method']:<35s} {r['acc_4class']:6.4f} {r['acc_3class']:6.4f} {r['mae']:6.4f}")
679	        # Reference: RF MVP
680	        print(f"  {'(ref) RF MVP':<35s} {'0.7815':>6s} {'—':>6s} {'—':>6s}")
681	
682	    os.makedirs(args.output_dir, exist_ok=True)
683	    out_path = os.path.join(args.output_dir, "baseline_results.json")
684	    with open(out_path, "w") as f:
685	        json.dump(all_results, f, indent=2, default=str)
686	    print(f"\nResults saved to {out_path}")
687	
688	
689	if __name__ == "__main__":
690	    main()
691	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "4477082f-e8b1-40e1-b830-0205e0e6bb23",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/baselines.py",
      "content": "\"\"\"\nBaseline battery for recursive generation depth estimation.\n\nBaselines:\n  1. PPLRegressionBaseline  — OLS regression on mean_ppl (single) or all 19 features (multi)\n  2. CEClassificationBaseline — MLP with cross-entropy loss (DCOL ablation, no contrastive loss)\n  3. CORALBaseline — Ordinal regression with K-1 binary classifiers (Cao et al., 2020)\n  4. DivEyeBaseline — Surprisal diversity features + XGBoost (Basani & Chen, TMLR 2026)\n\nUsage:\n  python src/baselines.py --method ppl_reg --features_path data/features_all.jsonl\n  python src/baselines.py --method ce_mlp  --features_path data/features_all.jsonl --epochs 50\n  python src/baselines.py --method coral   --features_path data/features_all.jsonl --epochs 50\n  python src/baselines.py --method diveye  --features_path data/features_all.jsonl\n  python src/baselines.py --method all     --features_path data/features_all.jsonl --epochs 50\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport sys\nimport numpy as np\nfrom collections import Counter\n\nimport torch\nimport torch.nn as nn\nimport torch.optim as optim\nfrom torch.utils.data import DataLoader, TensorDataset\n\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.metrics import (\n    accuracy_score, confusion_matrix, classification_report, roc_auc_score,\n)\n\n# ── Feature schema (must match extract_features.py / dcol_dataset.py) ──\n\nFEATURE_NAMES = [\n    \"mean_ppl\", \"var_ppl\", \"skewness_ppl\", \"kurtosis_ppl\",\n    \"p10_ppl\", \"p25_ppl\", \"p50_ppl\", \"p75_ppl\", \"p90_ppl\",\n    \"mean_surprisal\", \"var_surprisal\", \"entropy_of_surprisal\",\n    \"type_token_ratio\", \"hapax_ratio\", \"bigram_entropy\", \"trigram_entropy\",\n    \"rep_2gram\", \"rep_3gram\", \"rep_4gram\",\n]\nNUM_FEATURES = len(FEATURE_NAMES)\nNUM_DEPTHS = 4\nDEPTH_LABELS = list(range(NUM_DEPTHS))\n\n# ── Data loading ──\n\ndef load_features(path):\n    \"\"\"Load JSONL features file → (X [n, 19], y [n]).\"\"\"\n    records = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                records.append(json.loads(line))\n    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)\n    y = np.array([r[\"depth\"] for r in records], dtype=np.int64)\n    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)\n    return X, y\n\n\ndef prepare_splits(X, y, test_size=0.15, val_size=0.15, seed=42):\n    idx = np.arange(len(y))\n    train_val_idx, test_idx = train_test_split(\n        idx, test_size=test_size, stratify=y, random_state=seed\n    )\n    rel_val = val_size / (1 - test_size)\n    train_idx, val_idx = train_test_split(\n        train_val_idx, test_size=rel_val,\n        stratify=y[train_val_idx], random_state=seed\n    )\n    return (\n        X[train_idx], y[train_idx],\n        X[val_idx], y[val_idx],\n        X[test_idx], y[test_idx],\n    )\n\n# ── Evaluation metrics ──\n\ndef pairwise_auc(y_true, y_prob, d1, d2):\n    mask = np.isin(y_true, [d1, d2])\n    if mask.sum() < 2:\n        return None\n    yt = (y_true[mask] == d2).astype(int)\n    if len(np.unique(yt)) < 2:\n        return None\n    yp = y_prob[mask, d2]\n    return float(roc_auc_score(yt, yp))\n\n\ndef compute_all_pairwise_auc(y_true, y_prob):\n    result = {}\n    for i, d1 in enumerate(DEPTH_LABELS):\n        for d2 in DEPTH_LABELS[i + 1:]:\n            auc = pairwise_auc(y_true, y_prob, d1, d2)\n            result[f\"d{d1}_vs_d{d2}\"] = round(auc, 4) if auc is not None else None\n    return result\n\n\ndef bootstrap_ci(y_true, y_pred, metric_fn=accuracy_score, n_boot=1000, seed=42):\n    rng = np.random.RandomState(seed)\n    scores = []\n    n = len(y_true)\n    for _ in range(n_boot):\n        idx = rng.choice(n, n, replace=True)\n        scores.append(metric_fn(y_true[idx], y_pred[idx]))\n    lo = float(np.percentile(scores, 2.5))\n    hi = float(np.percentile(scores, 97.5))\n    return lo, hi\n\n\ndef evaluate(name, y_true, y_pred, y_prob=None):\n    \"\"\"Print and return evaluation metrics.\"\"\"\n    acc4 = accuracy_score(y_true, y_pred)\n    ci_lo, ci_hi = bootstrap_ci(y_true, y_pred)\n\n    # 3-class accuracy (depth 1-3 only)\n    mask_13 = y_true >= 1\n    acc3 = accuracy_score(y_true[mask_13], y_pred[mask_13]) if mask_13.sum() > 0 else 0.0\n\n    mae = float(np.mean(np.abs(y_true - y_pred)))\n\n    cm = confusion_matrix(y_true, y_pred, labels=DEPTH_LABELS)\n    per_class_recall = cm.diagonal() / cm.sum(axis=1).clip(min=1)\n\n    pair_aucs = {}\n    if y_prob is not None:\n        pair_aucs = compute_all_pairwise_auc(y_true, y_prob)\n\n    print(f\"\\n{'='*60}\")\n    print(f\"  {name}\")\n    print(f\"{'='*60}\")\n    print(f\"  4-class accuracy : {acc4:.4f}  (95% CI: [{ci_lo:.4f}, {ci_hi:.4f}])\")\n    print(f\"  3-class accuracy : {acc3:.4f}  (d1-d3 only)\")\n    print(f\"  MAE              : {mae:.4f}\")\n    print(f\"  Per-class recall : {dict(zip([f'd{d}' for d in DEPTH_LABELS], [round(r,4) for r in per_class_recall]))}\")\n    if pair_aucs:\n        print(f\"  Pairwise AUC     : {pair_aucs}\")\n    print(f\"\\n  Confusion matrix:\")\n    print(f\"  {'':>8s}\", \" \".join(f\"pred-{d}\" for d in DEPTH_LABELS))\n    for i, d in enumerate(DEPTH_LABELS):\n        print(f\"  true-{d}  \", \" \".join(f\"{cm[i,j]:6d}\" for j in range(NUM_DEPTHS)))\n\n    cr = classification_report(\n        y_true, y_pred,\n        target_names=[f\"depth-{d}\" for d in DEPTH_LABELS],\n        zero_division=0,\n    )\n    print(f\"\\n{cr}\")\n\n    return {\n        \"method\": name,\n        \"acc_4class\": round(acc4, 4),\n        \"acc_4class_ci\": [round(ci_lo, 4), round(ci_hi, 4)],\n        \"acc_3class\": round(acc3, 4),\n        \"mae\": round(mae, 4),\n        \"per_class_recall\": {f\"d{d}\": round(r, 4) for d, r in zip(DEPTH_LABELS, per_class_recall)},\n        \"pairwise_auc\": pair_aucs,\n    }\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  Baseline 1: PPL Regression\n# ═══════════════════════════════════════════════════════════════════════\n\nclass PPLRegressionBaseline:\n    \"\"\"\n    Linear regression → round to nearest depth.\n\n    Single-feature mode: depth = a * mean_ppl + b\n    Multi-feature mode:  depth = X @ w + b  (19-dim OLS)\n\n    Simplest possible baseline. If mean_ppl alone suffices, complex models are\n    unnecessary.\n    \"\"\"\n\n    def __init__(self, mode=\"multi\"):\n        self.mode = mode  # \"single\" or \"multi\"\n        self.scaler = StandardScaler()\n        self.model = LinearRegression()\n\n    def _select(self, X):\n        if self.mode == \"single\":\n            idx = FEATURE_NAMES.index(\"mean_ppl\")\n            return X[:, idx:idx+1]\n        return X\n\n    def fit(self, X_train, y_train):\n        Xs = self._select(X_train)\n        Xs = self.scaler.fit_transform(Xs)\n        self.model.fit(Xs, y_train.astype(np.float64))\n\n    def predict(self, X_test):\n        Xs = self._select(X_test)\n        Xs = self.scaler.transform(Xs)\n        raw = self.model.predict(Xs)\n        return np.clip(np.round(raw).astype(int), 0, NUM_DEPTHS - 1)\n\n    def predict_proba(self, X_test):\n        preds = self.predict(X_test)\n        prob = np.zeros((len(preds), NUM_DEPTHS))\n        for i, p in enumerate(preds):\n            prob[i, p] = 1.0\n        return prob\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  Baseline 2: Cross-Entropy MLP (DCOL ablation)\n# ═══════════════════════════════════════════════════════════════════════\n\nclass _CEMLP(nn.Module):\n    \"\"\"19 → 128 → 64 → 4  with ReLU + dropout. Same architecture as DCOL's\n    feature head, but trained with CE loss only (no contrastive loss).\"\"\"\n\n    def __init__(self, input_dim=NUM_FEATURES, hidden1=128, hidden2=64,\n                 num_classes=NUM_DEPTHS, dropout=0.3):\n        super().__init__()\n        self.net = nn.Sequential(\n            nn.Linear(input_dim, hidden1),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n            nn.Linear(hidden1, hidden2),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n            nn.Linear(hidden2, num_classes),\n        )\n\n    def forward(self, x):\n        return self.net(x)\n\n\nclass CEClassificationBaseline:\n    \"\"\"\n    Standard multi-class MLP with cross-entropy loss.\n\n    Architecture identical to DCOL's feature classifier head (19→128→64→4)\n    but uses only CE loss — no contrastive learning.\n    This is the key ablation: if CE-MLP matches DCOL, the contrastive loss\n    adds no value.\n    \"\"\"\n\n    def __init__(self, lr=1e-3, epochs=100, batch_size=256, patience=10,\n                 device=None, seed=42):\n        self.lr = lr\n        self.epochs = epochs\n        self.batch_size = batch_size\n        self.patience = patience\n        self.device = device or (\"cuda\" if torch.cuda.is_available() else \"cpu\")\n        self.seed = seed\n        self.scaler = StandardScaler()\n        self.model = None\n\n    def fit(self, X_train, y_train, X_val=None, y_val=None):\n        torch.manual_seed(self.seed)\n        np.random.seed(self.seed)\n\n        X_s = self.scaler.fit_transform(X_train).astype(np.float32)\n        Xt = torch.tensor(X_s, device=self.device)\n        yt = torch.tensor(y_train, dtype=torch.long, device=self.device)\n        ds = TensorDataset(Xt, yt)\n        loader = DataLoader(ds, batch_size=self.batch_size, shuffle=True)\n\n        self.model = _CEMLP().to(self.device)\n        optimizer = optim.Adam(self.model.parameters(), lr=self.lr, weight_decay=1e-4)\n        criterion = nn.CrossEntropyLoss()\n\n        best_loss = float(\"inf\")\n        wait = 0\n        best_state = None\n\n        has_val = X_val is not None and y_val is not None\n        if has_val:\n            Xv = torch.tensor(self.scaler.transform(X_val).astype(np.float32),\n                              device=self.device)\n            yv = torch.tensor(y_val, dtype=torch.long, device=self.device)\n\n        for epoch in range(self.epochs):\n            self.model.train()\n            epoch_loss = 0.0\n            for xb, yb in loader:\n                optimizer.zero_grad()\n                logits = self.model(xb)\n                loss = criterion(logits, yb)\n                loss.backward()\n                optimizer.step()\n                epoch_loss += loss.item() * len(xb)\n            epoch_loss /= len(ds)\n\n            if has_val:\n                self.model.eval()\n                with torch.no_grad():\n                    val_logits = self.model(Xv)\n                    val_loss = criterion(val_logits, yv).item()\n            else:\n                val_loss = epoch_loss\n\n            if val_loss < best_loss - 1e-4:\n                best_loss = val_loss\n                best_state = {k: v.clone() for k, v in self.model.state_dict().items()}\n                wait = 0\n            else:\n                wait += 1\n                if wait >= self.patience:\n                    break\n\n        if best_state is not None:\n            self.model.load_state_dict(best_state)\n\n    def predict(self, X_test):\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n        return logits.argmax(dim=-1).cpu().numpy()\n\n    def predict_proba(self, X_test):\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n            probs = torch.softmax(logits, dim=-1)\n        return probs.cpu().numpy()\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  Baseline 3: CORAL Ordinal Regression\n# ═══════════════════════════════════════════════════════════════════════\n\nclass _CORALNet(nn.Module):\n    \"\"\"\n    CORAL ordinal regression (Cao et al., 2020, \"Rank consistent ordinal\n    regression for neural networks with consistent confidence sets\").\n\n    Architecture: 19 → 128 → 64 → shared representation, then K-1 = 3\n    independent sigmoid heads.\n\n    Each head k answers: P(depth > k).\n    Prediction: depth = sum_k I[P(depth > k) > 0.5].\n\n    Loss (rank-consistent):\n        L = sum_{k=0}^{K-2} BCE(sigmoid(w_k^T h + b_k), I[y > k])\n\n    Weight sharing across heads ensures rank consistency: predictions are\n    monotonically decreasing in threshold order.\n    \"\"\"\n\n    def __init__(self, input_dim=NUM_FEATURES, hidden1=128, hidden2=64,\n                 num_classes=NUM_DEPTHS, dropout=0.3):\n        super().__init__()\n        self.num_classes = num_classes\n        self.backbone = nn.Sequential(\n            nn.Linear(input_dim, hidden1),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n            nn.Linear(hidden1, hidden2),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n        )\n        # K-1 independent binary heads (shared backbone, separate bias)\n        self.fc = nn.Linear(hidden2, 1, bias=False)\n        self.biases = nn.Parameter(torch.zeros(num_classes - 1))\n\n    def forward(self, x):\n        h = self.backbone(x)             # [B, 64]\n        logit_base = self.fc(h)          # [B, 1]\n        # broadcast: [B, K-1]\n        logits = logit_base + self.biases # each head shares weight, different bias\n        return logits\n\n\nclass CORALBaseline:\n    \"\"\"\n    CORAL ordinal regression for depth estimation.\n\n    Ref: Cao, Mirjalili & Raschka (2020). \"Rank consistent ordinal regression\n    for neural networks with consistent confidence sets.\" Pattern Recognition.\n\n    Exploits ordinal structure: depth 0 < 1 < 2 < 3.\n    Alternative to DCOL's contrastive approach for leveraging label ordering.\n    \"\"\"\n\n    def __init__(self, lr=1e-3, epochs=100, batch_size=256, patience=10,\n                 device=None, seed=42):\n        self.lr = lr\n        self.epochs = epochs\n        self.batch_size = batch_size\n        self.patience = patience\n        self.device = device or (\"cuda\" if torch.cuda.is_available() else \"cpu\")\n        self.seed = seed\n        self.scaler = StandardScaler()\n        self.model = None\n\n    @staticmethod\n    def _encode_ordinal(y, num_classes):\n        \"\"\"Convert class labels to K-1 binary ordinal targets.\n        y=2, K=4 → [1, 1, 0]  (depth > 0? yes, depth > 1? yes, depth > 2? no)\n        \"\"\"\n        n = len(y)\n        targets = np.zeros((n, num_classes - 1), dtype=np.float32)\n        for k in range(num_classes - 1):\n            targets[:, k] = (y > k).astype(np.float32)\n        return targets\n\n    def fit(self, X_train, y_train, X_val=None, y_val=None):\n        torch.manual_seed(self.seed)\n        np.random.seed(self.seed)\n\n        X_s = self.scaler.fit_transform(X_train).astype(np.float32)\n        ord_targets = self._encode_ordinal(y_train, NUM_DEPTHS)\n\n        Xt = torch.tensor(X_s, device=self.device)\n        ot = torch.tensor(ord_targets, device=self.device)\n        ds = TensorDataset(Xt, ot)\n        loader = DataLoader(ds, batch_size=self.batch_size, shuffle=True)\n\n        self.model = _CORALNet().to(self.device)\n        optimizer = optim.Adam(self.model.parameters(), lr=self.lr, weight_decay=1e-4)\n        criterion = nn.BCEWithLogitsLoss()\n\n        best_loss = float(\"inf\")\n        wait = 0\n        best_state = None\n\n        has_val = X_val is not None and y_val is not None\n        if has_val:\n            Xv = torch.tensor(self.scaler.transform(X_val).astype(np.float32),\n                              device=self.device)\n            ov = torch.tensor(self._encode_ordinal(y_val, NUM_DEPTHS),\n                              device=self.device)\n\n        for epoch in range(self.epochs):\n            self.model.train()\n            epoch_loss = 0.0\n            for xb, ob in loader:\n                optimizer.zero_grad()\n                logits = self.model(xb)\n                loss = criterion(logits, ob)\n                loss.backward()\n                optimizer.step()\n                epoch_loss += loss.item() * len(xb)\n            epoch_loss /= len(ds)\n\n            if has_val:\n                self.model.eval()\n                with torch.no_grad():\n                    val_logits = self.model(Xv)\n                    val_loss = criterion(val_logits, ov).item()\n            else:\n                val_loss = epoch_loss\n\n            if val_loss < best_loss - 1e-4:\n                best_loss = val_loss\n                best_state = {k: v.clone() for k, v in self.model.state_dict().items()}\n                wait = 0\n            else:\n                wait += 1\n                if wait >= self.patience:\n                    break\n\n        if best_state is not None:\n            self.model.load_state_dict(best_state)\n\n    def predict(self, X_test):\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n            probs = torch.sigmoid(logits)  # [B, K-1], P(depth > k)\n        # depth = number of thresholds exceeded\n        preds = (probs > 0.5).sum(dim=-1).cpu().numpy().astype(int)\n        return preds\n\n    def predict_proba(self, X_test):\n        \"\"\"Convert cumulative probabilities to per-class probabilities.\n        P(depth=k) = P(depth>k-1) - P(depth>k), with boundary conditions.\n        \"\"\"\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n            cum_probs = torch.sigmoid(logits).cpu().numpy()  # [B, K-1]\n\n        n = len(X_test)\n        probs = np.zeros((n, NUM_DEPTHS))\n        # P(depth=0) = 1 - P(depth>0)\n        probs[:, 0] = 1.0 - cum_probs[:, 0]\n        # P(depth=k) = P(depth>k-1) - P(depth>k) for k=1..K-2\n        for k in range(1, NUM_DEPTHS - 1):\n            probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]\n        # P(depth=K-1) = P(depth>K-2)\n        probs[:, NUM_DEPTHS - 1] = cum_probs[:, NUM_DEPTHS - 2]\n        probs = np.clip(probs, 0, 1)\n        row_sums = probs.sum(axis=1, keepdims=True)\n        probs = probs / np.where(row_sums > 0, row_sums, 1.0)\n        return probs\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  Baseline 4: DivEye (Surprisal Diversity + XGBoost)\n# ═══════════════════════════════════════════════════════════════════════\n\n# DivEye feature groups mapped to our 19 features:\n#   Distributional: mean_ppl, var_ppl, skewness_ppl, kurtosis_ppl → matches\n#                   DivEye's mean/var/skewness/kurtosis of surprisal\n#   Surprisal:      mean_surprisal, var_surprisal, entropy_of_surprisal\n#   Lexical diversity: type_token_ratio, hapax_ratio, bigram_entropy, trigram_entropy\n#   Repetition:     rep_2gram, rep_3gram, rep_4gram\n#\n# TODO: DivEye's temporal features (first-order ∆S and second-order ∆²S,\n#       computed from per-token surprisal sequences) are not available in our\n#       pre-computed features. Full DivEye reproduction requires raw token-level\n#       surprisal; these summary statistics are a proxy.\n\nDIVEYE_FEATURE_INDICES = [\n    FEATURE_NAMES.index(f) for f in [\n        \"mean_ppl\", \"var_ppl\", \"skewness_ppl\", \"kurtosis_ppl\",\n        \"mean_surprisal\", \"var_surprisal\", \"entropy_of_surprisal\",\n        \"type_token_ratio\", \"hapax_ratio\", \"bigram_entropy\", \"trigram_entropy\",\n        \"rep_2gram\", \"rep_3gram\", \"rep_4gram\",\n    ]\n]\n\n\nclass DivEyeBaseline:\n    \"\"\"\n    DivEye-style detection adapted for depth estimation.\n\n    Ref: Basani, A. R. & Chen, P.-Y. (2026). Diversity Boosts AI-Generated Text Detection. Transactions on Machine Learning Research (TMLR).\n    GitHub: https://github.com/IBM/diveye\n\n    DivEye's insight: human text has higher surprisal diversity (distributional,\n    first-order temporal ∆S, second-order ∆²S). We adapt this to depth estimation:\n    deeper recursive generations should have *lower* diversity.\n\n    Implementation: XGBoost on surprisal-related feature subset (14 of 19 features).\n    Full DivEye also uses first/second-order temporal surprisal features from raw\n    token sequences — those are not available in our pre-extracted features.\n    \"\"\"\n\n    def __init__(self, seed=42):\n        self.seed = seed\n        self.model = None\n\n    def fit(self, X_train, y_train, **kwargs):\n        try:\n            from xgboost import XGBClassifier\n        except ImportError:\n            print(\"[ERROR] xgboost not installed. Run: pip install xgboost\")\n            sys.exit(1)\n\n        Xd = X_train[:, DIVEYE_FEATURE_INDICES]\n        self.model = XGBClassifier(\n            n_estimators=200,\n            max_depth=6,\n            learning_rate=0.1,\n            subsample=0.8,\n            colsample_bytree=0.8,\n            random_state=self.seed,\n            use_label_encoder=False,\n            eval_metric=\"mlogloss\",\n            verbosity=0,\n        )\n        self.model.fit(Xd, y_train)\n\n    def predict(self, X_test):\n        Xd = X_test[:, DIVEYE_FEATURE_INDICES]\n        return self.model.predict(Xd)\n\n    def predict_proba(self, X_test):\n        Xd = X_test[:, DIVEYE_FEATURE_INDICES]\n        probs = self.model.predict_proba(Xd)\n        # Ensure output is [n, NUM_DEPTHS] even if some classes are missing\n        if probs.shape[1] < NUM_DEPTHS:\n            full = np.zeros((probs.shape[0], NUM_DEPTHS))\n            for i, c in enumerate(self.model.classes_):\n                full[:, c] = probs[:, i]\n            return full\n        return probs\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  Unified Runner\n# ═══════════════════════════════════════════════════════════════════════\n\nBASELINE_REGISTRY = {\n    \"ppl_reg_single\": (\"PPL Regression (single: mean_ppl)\", lambda: PPLRegressionBaseline(mode=\"single\")),\n    \"ppl_reg\":        (\"PPL Regression (multi: 19-dim OLS)\", lambda: PPLRegressionBaseline(mode=\"multi\")),\n    \"ce_mlp\":         (\"CE-MLP (DCOL ablation)\", None),  # needs args\n    \"coral\":          (\"CORAL Ordinal Regression\", None),\n    \"diveye\":         (\"DivEye (XGBoost)\", lambda: DivEyeBaseline()),\n}\n\n\ndef run_baseline(method, X_train, y_train, X_val, y_val, X_test, y_test, args):\n    if method == \"ppl_reg_single\":\n        bl = PPLRegressionBaseline(mode=\"single\")\n        bl.fit(X_train, y_train)\n    elif method == \"ppl_reg\":\n        bl = PPLRegressionBaseline(mode=\"multi\")\n        bl.fit(X_train, y_train)\n    elif method == \"ce_mlp\":\n        bl = CEClassificationBaseline(\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\n            patience=args.patience, seed=args.seed,\n        )\n        bl.fit(X_train, y_train, X_val, y_val)\n    elif method == \"coral\":\n        bl = CORALBaseline(\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\n            patience=args.patience, seed=args.seed,\n        )\n        bl.fit(X_train, y_train, X_val, y_val)\n    elif method == \"diveye\":\n        bl = DivEyeBaseline(seed=args.seed)\n        bl.fit(X_train, y_train)\n    else:\n        print(f\"Unknown method: {method}\")\n        return None\n\n    y_pred = bl.predict(X_test)\n    y_prob = bl.predict_proba(X_test)\n    name = BASELINE_REGISTRY.get(method, (method, None))[0]\n    return evaluate(name, y_test, y_pred, y_prob)\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"Baseline battery for depth estimation.\")\n    p.add_argument(\"--method\", default=\"all\",\n                   choices=[\"ppl_reg_single\", \"ppl_reg\", \"ce_mlp\", \"coral\", \"diveye\", \"all\"])\n    p.add_argument(\"--features_path\", default=\"data/features_all.jsonl\")\n    p.add_argument(\"--output_dir\", default=\"results/baselines/\")\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--test_size\", type=float, default=0.15)\n    p.add_argument(\"--val_size\", type=float, default=0.15)\n    p.add_argument(\"--epochs\", type=int, default=100)\n    p.add_argument(\"--batch_size\", type=int, default=256)\n    p.add_argument(\"--lr\", type=float, default=1e-3)\n    p.add_argument(\"--patience\", type=int, default=10)\n    return p.parse_args()\n\n\ndef main():\n    args = parse_args()\n    print(f\"Loading features from {args.features_path} ...\")\n    X, y = load_features(args.features_path)\n    print(f\"  {X.shape[0]} samples, {X.shape[1]} features\")\n    print(f\"  Depth distribution: {dict(Counter(y))}\")\n\n    X_train, y_train, X_val, y_val, X_test, y_test = prepare_splits(\n        X, y, test_size=args.test_size, val_size=args.val_size, seed=args.seed\n    )\n    print(f\"  Train: {len(y_train)}, Val: {len(y_val)}, Test: {len(y_test)}\")\n\n    methods = list(BASELINE_REGISTRY.keys()) if args.method == \"all\" else [args.method]\n    all_results = {}\n\n    for m in methods:\n        result = run_baseline(m, X_train, y_train, X_val, y_val, X_test, y_test, args)\n        if result is not None:\n            all_results[m] = result\n\n    # Summary table\n    if len(all_results) > 1:\n        print(f\"\\n{'='*60}\")\n        print(f\"  SUMMARY\")\n        print(f\"{'='*60}\")\n        print(f\"  {'Method':<35s} {'4-cls':>6s} {'3-cls':>6s} {'MAE':>6s}\")\n        print(f\"  {'-'*35} {'-'*6} {'-'*6} {'-'*6}\")\n        for m, r in all_results.items():\n            print(f\"  {r['method']:<35s} {r['acc_4class']:6.4f} {r['acc_3class']:6.4f} {r['mae']:6.4f}\")\n        # Reference: RF MVP\n        print(f\"  {'(ref) RF MVP':<35s} {'0.7815':>6s} {'—':>6s} {'—':>6s}\")\n\n    os.makedirs(args.output_dir, exist_ok=True)\n    out_path = os.path.join(args.output_dir, \"baseline_results.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(all_results, f, indent=2, default=str)\n    print(f\"\\nResults saved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 691,
      "startLine": 1,
      "totalLines": 691
    }
  }
}
```

</details>

---


### Tool call

_source line 91_

<details open><summary>🔧 Tool call — Read · `toolu_01VfCHgc5o5tibPV3sHJ4J7v`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_ppl_regression.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "6587b959-f2a6-4d9e-bd7e-770d3dca4ff2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0156TyoVouLj4Woqu89sRSJo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2877,
      "cache_read_input_tokens": 23600,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2877
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

_source line 92 · 2026-05-14T23:02:17.915Z_

<details><summary>↩ Tool result · `toolu_01VfCHgc5o5tibPV3sHJ4J7v`</summary>

```text
1	"""
2	Baseline 2: Perplexity-only Regression for recursive generation depth estimation.
3	
4	Simplest baseline — uses only perplexity statistics (mean_ppl, p75_ppl, p90_ppl)
5	to predict recursion depth via:
6	  (a) Ridge Regression → round to nearest integer depth
7	  (b) Ordinal Logistic Regression (cumulative link model)
8	
9	If PPL alone separates depths well, more complex methods add no value.
10	
11	Input:  Pre-extracted features JSONL (--features_path) or raw depth_*.jsonl (--data_dirs)
12	Output: {method}_classification_report.json, {method}_pairwise_auc.json, {method}_predictions.json
13	
14	Usage:
15	  python baseline_ppl_regression.py --features_path data/features_all.jsonl
16	  python baseline_ppl_regression.py --features_path data/features_all.jsonl --mode ordinal
17	"""
18	
19	import argparse
20	import numpy as np
21	from sklearn.linear_model import Ridge
22	from sklearn.preprocessing import StandardScaler
23	
24	from baseline_utils import (
25	    load_features, stratified_split, evaluate_and_save,
26	    add_common_args, NUM_DEPTHS, FEATURE_NAMES,
27	)
28	
29	PPL_FEATURES = ["mean_ppl", "p75_ppl", "p90_ppl"]
30	PPL_INDICES = [FEATURE_NAMES.index(f) for f in PPL_FEATURES]
31	
32	
33	class RidgePPLRegressor:
34	    """Ridge regression on 3 PPL features → round to nearest depth."""
35	
36	    def __init__(self, alpha=1.0):
37	        self.scaler = StandardScaler()
38	        self.model = Ridge(alpha=alpha)
39	
40	    def fit(self, X, y):
41	        Xs = self.scaler.fit_transform(X[:, PPL_INDICES])
42	        self.model.fit(Xs, y.astype(np.float64))
43	
44	    def predict(self, X):
45	        Xs = self.scaler.transform(X[:, PPL_INDICES])
46	        raw = self.model.predict(Xs)
47	        return np.clip(np.round(raw).astype(int), 0, NUM_DEPTHS - 1)
48	
49	    def predict_proba(self, X):
50	        preds = self.predict(X)
51	        prob = np.zeros((len(preds), NUM_DEPTHS))
52	        for i, p in enumerate(preds):
53	            prob[i, p] = 1.0
54	        return prob
55	
56	
57	class OrdinalLogisticPPL:
58	    """
59	    Ordinal Logistic Regression (cumulative model) on 3 PPL features.
60	
61	    Uses K-1 binary logistic regressions: P(depth >= k) for k=1..K-1.
62	    Falls back to sklearn LogisticRegression if mord is unavailable.
63	    """
64	
65	    def __init__(self):
66	        self.scaler = StandardScaler()
67	        self.models = []
68	
69	    def fit(self, X, y):
70	        Xs = self.scaler.fit_transform(X[:, PPL_INDICES])
71	        from sklearn.linear_model import LogisticRegression
72	        self.models = []
73	        for k in range(1, NUM_DEPTHS):
74	            binary_y = (y >= k).astype(int)
75	            clf = LogisticRegression(max_iter=1000, C=1.0)
76	            clf.fit(Xs, binary_y)
77	            self.models.append(clf)
78	
79	    def predict_proba(self, X):
80	        Xs = self.scaler.transform(X[:, PPL_INDICES])
81	        cum_probs = np.column_stack([
82	            m.predict_proba(Xs)[:, 1] for m in self.models
83	        ])
84	        probs = np.zeros((len(X), NUM_DEPTHS))
85	        probs[:, 0] = 1.0 - cum_probs[:, 0]
86	        for k in range(1, NUM_DEPTHS - 1):
87	            probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]
88	        probs[:, NUM_DEPTHS - 1] = cum_probs[:, NUM_DEPTHS - 2]
89	        probs = np.clip(probs, 0, 1)
90	        row_sums = probs.sum(axis=1, keepdims=True)
91	        probs = probs / np.where(row_sums > 0, row_sums, 1.0)
92	        return probs
93	
94	    def predict(self, X):
95	        return self.predict_proba(X).argmax(axis=1)
96	
97	
98	def main():
99	    parser = argparse.ArgumentParser(description="Perplexity-only Regression baseline")
100	    add_common_args(parser)
101	    parser.add_argument("--mode", choices=["ridge", "ordinal", "both"], default="both")
102	    parser.add_argument("--alpha", type=float, default=1.0, help="Ridge regularization")
103	    args = parser.parse_args()
104	
105	    if args.features_path is None:
106	        print("ERROR: --features_path is required for PPL regression baseline.")
107	        print("Run extract_features.py first to generate features JSONL.")
108	        return
109	
110	    X, y = load_features(args.features_path)
111	    train_idx, eval_idx = stratified_split(y, eval_split=args.eval_split, seed=args.seed)
112	    X_train, y_train = X[train_idx], y[train_idx]
113	    X_eval, y_eval = X[eval_idx], y[eval_idx]
114	    print(f"Train: {len(y_train)}, Eval: {len(y_eval)}")
115	
116	    modes = ["ridge", "ordinal"] if args.mode == "both" else [args.mode]
117	
118	    for mode in modes:
119	        method_name = f"ppl_{mode}"
120	        if mode == "ridge":
121	            model = RidgePPLRegressor(alpha=args.alpha)
122	        else:
123	            model = OrdinalLogisticPPL()
124	
125	        model.fit(X_train, y_train)
126	        y_pred = model.predict(X_eval)
127	        y_prob = model.predict_proba(X_eval)
128	        evaluate_and_save(method_name, y_eval, y_pred, y_prob, args.output_dir)
129	
130	
131	if __name__ == "__main__":
132	    main()
133	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "a362be6c-3593-4df4-bef5-4a2bb9270cc9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_ppl_regression.py",
      "content": "\"\"\"\nBaseline 2: Perplexity-only Regression for recursive generation depth estimation.\n\nSimplest baseline — uses only perplexity statistics (mean_ppl, p75_ppl, p90_ppl)\nto predict recursion depth via:\n  (a) Ridge Regression → round to nearest integer depth\n  (b) Ordinal Logistic Regression (cumulative link model)\n\nIf PPL alone separates depths well, more complex methods add no value.\n\nInput:  Pre-extracted features JSONL (--features_path) or raw depth_*.jsonl (--data_dirs)\nOutput: {method}_classification_report.json, {method}_pairwise_auc.json, {method}_predictions.json\n\nUsage:\n  python baseline_ppl_regression.py --features_path data/features_all.jsonl\n  python baseline_ppl_regression.py --features_path data/features_all.jsonl --mode ordinal\n\"\"\"\n\nimport argparse\nimport numpy as np\nfrom sklearn.linear_model import Ridge\nfrom sklearn.preprocessing import StandardScaler\n\nfrom baseline_utils import (\n    load_features, stratified_split, evaluate_and_save,\n    add_common_args, NUM_DEPTHS, FEATURE_NAMES,\n)\n\nPPL_FEATURES = [\"mean_ppl\", \"p75_ppl\", \"p90_ppl\"]\nPPL_INDICES = [FEATURE_NAMES.index(f) for f in PPL_FEATURES]\n\n\nclass RidgePPLRegressor:\n    \"\"\"Ridge regression on 3 PPL features → round to nearest depth.\"\"\"\n\n    def __init__(self, alpha=1.0):\n        self.scaler = StandardScaler()\n        self.model = Ridge(alpha=alpha)\n\n    def fit(self, X, y):\n        Xs = self.scaler.fit_transform(X[:, PPL_INDICES])\n        self.model.fit(Xs, y.astype(np.float64))\n\n    def predict(self, X):\n        Xs = self.scaler.transform(X[:, PPL_INDICES])\n        raw = self.model.predict(Xs)\n        return np.clip(np.round(raw).astype(int), 0, NUM_DEPTHS - 1)\n\n    def predict_proba(self, X):\n        preds = self.predict(X)\n        prob = np.zeros((len(preds), NUM_DEPTHS))\n        for i, p in enumerate(preds):\n            prob[i, p] = 1.0\n        return prob\n\n\nclass OrdinalLogisticPPL:\n    \"\"\"\n    Ordinal Logistic Regression (cumulative model) on 3 PPL features.\n\n    Uses K-1 binary logistic regressions: P(depth >= k) for k=1..K-1.\n    Falls back to sklearn LogisticRegression if mord is unavailable.\n    \"\"\"\n\n    def __init__(self):\n        self.scaler = StandardScaler()\n        self.models = []\n\n    def fit(self, X, y):\n        Xs = self.scaler.fit_transform(X[:, PPL_INDICES])\n        from sklearn.linear_model import LogisticRegression\n        self.models = []\n        for k in range(1, NUM_DEPTHS):\n            binary_y = (y >= k).astype(int)\n            clf = LogisticRegression(max_iter=1000, C=1.0)\n            clf.fit(Xs, binary_y)\n            self.models.append(clf)\n\n    def predict_proba(self, X):\n        Xs = self.scaler.transform(X[:, PPL_INDICES])\n        cum_probs = np.column_stack([\n            m.predict_proba(Xs)[:, 1] for m in self.models\n        ])\n        probs = np.zeros((len(X), NUM_DEPTHS))\n        probs[:, 0] = 1.0 - cum_probs[:, 0]\n        for k in range(1, NUM_DEPTHS - 1):\n            probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]\n        probs[:, NUM_DEPTHS - 1] = cum_probs[:, NUM_DEPTHS - 2]\n        probs = np.clip(probs, 0, 1)\n        row_sums = probs.sum(axis=1, keepdims=True)\n        probs = probs / np.where(row_sums > 0, row_sums, 1.0)\n        return probs\n\n    def predict(self, X):\n        return self.predict_proba(X).argmax(axis=1)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Perplexity-only Regression baseline\")\n    add_common_args(parser)\n    parser.add_argument(\"--mode\", choices=[\"ridge\", \"ordinal\", \"both\"], default=\"both\")\n    parser.add_argument(\"--alpha\", type=float, default=1.0, help=\"Ridge regularization\")\n    args = parser.parse_args()\n\n    if args.features_path is None:\n        print(\"ERROR: --features_path is required for PPL regression baseline.\")\n        print(\"Run extract_features.py first to generate features JSONL.\")\n        return\n\n    X, y = load_features(args.features_path)\n    train_idx, eval_idx = stratified_split(y, eval_split=args.eval_split, seed=args.seed)\n    X_train, y_train = X[train_idx], y[train_idx]\n    X_eval, y_eval = X[eval_idx], y[eval_idx]\n    print(f\"Train: {len(y_train)}, Eval: {len(y_eval)}\")\n\n    modes = [\"ridge\", \"ordinal\"] if args.mode == \"both\" else [args.mode]\n\n    for mode in modes:\n        method_name = f\"ppl_{mode}\"\n        if mode == \"ridge\":\n            model = RidgePPLRegressor(alpha=args.alpha)\n        else:\n            model = OrdinalLogisticPPL()\n\n        model.fit(X_train, y_train)\n        y_pred = model.predict(X_eval)\n        y_prob = model.predict_proba(X_eval)\n        evaluate_and_save(method_name, y_eval, y_pred, y_prob, args.output_dir)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 133,
      "startLine": 1,
      "totalLines": 133
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
Now let me read the remaining baseline scripts and the zero-shot LLM baseline.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "b069c1c3-6f32-4007-91a6-c2f7a4c6916f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Ai8DvYTokR9U6g6n5HQqM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15361,
      "cache_read_input_tokens": 26477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15361
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

Let me read the remaining baseline scripts and check the remote server state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "7a7790e7-04b9-4644-8674-6f35fb24620f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Ai8DvYTokR9U6g6n5HQqM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15361,
      "cache_read_input_tokens": 26477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15361
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

<details open><summary>🔧 Tool call — Read · `toolu_01XxPpfNzcT7w6d21q1tsUXZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_coral.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "89c8d76f-9c0d-4250-9bfd-3fcde38b09f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Ai8DvYTokR9U6g6n5HQqM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15361,
      "cache_read_input_tokens": 26477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15361
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

_source line 96 · 2026-05-14T23:02:23.318Z_

<details><summary>↩ Tool result · `toolu_01XxPpfNzcT7w6d21q1tsUXZ`</summary>

```text
1	"""
2	Baseline 3: CORAL (Consistent Rank Logits) for recursive generation depth estimation.
3	
4	Classic ordinal classification method (Cao, Mirjalili & Raschka, 2020).
5	Converts K-class ordinal problem into K-1 binary decisions sharing a backbone.
6	
7	Architecture: DeBERTa → [CLS] → shared Linear(hidden, 1) + K-1 bias terms
8	Each head k outputs logit for P(depth > k), k = 0..K-2.
9	Default: DeBERTa-v3-large (435M) to match DCOL backbone for fair comparison.
10	
11	CORAL loss (rank-consistent):
12	  L = Σ_{k=0}^{K-2} BCE(σ(w^T h + b_k), 𝟙[y > k])
13	where w is shared across thresholds and b_k is per-threshold bias.
14	
15	Prediction: depth = Σ_k 𝟙[σ(w^T h + b_k) > 0.5]
16	
17	Ref: Cao, W., Mirjalili, V. & Raschka, S. (2020). "Rank consistent ordinal
18	     regression for neural networks with consistent confidence sets."
19	     Pattern Recognition, 108, 107736.
20	
21	Input:  Raw depth_*.jsonl files (--data_dirs)
22	Output: {method}_classification_report.json, {method}_pairwise_auc.json, {method}_predictions.json
23	
24	Usage:
25	  python baseline_coral.py --data_dirs data/  # default: deberta-v3-large
26	  python baseline_coral.py --data_dirs data/ --model_name microsoft/deberta-v3-base --model_path /root/autodl-tmp/models/deberta-v3-base
27	  python baseline_coral.py --data_dirs data/ --dry_run
28	"""
29	
30	import argparse
31	import random
32	import numpy as np
33	import torch
34	import torch.nn as nn
35	from torch.utils.data import DataLoader, Dataset
36	from transformers import AutoModel, AutoTokenizer
37	
38	from baseline_utils import (
39	    load_jsonl_data, stratified_split, evaluate_and_save,
40	    add_common_args, NUM_DEPTHS,
41	)
42	
43	
44	def set_seed(seed):
45	    random.seed(seed)
46	    np.random.seed(seed)
47	    torch.manual_seed(seed)
48	    torch.cuda.manual_seed_all(seed)
49	
50	
51	class DepthTextDataset(Dataset):
52	    def __init__(self, texts, labels, tokenizer, max_seq_len):
53	        self.texts = texts
54	        self.labels = labels
55	        self.tokenizer = tokenizer
56	        self.max_seq_len = max_seq_len
57	
58	    def __len__(self):
59	        return len(self.texts)
60	
61	    def __getitem__(self, idx):
62	        enc = self.tokenizer(
63	            self.texts[idx],
64	            max_length=self.max_seq_len,
65	            padding="max_length",
66	            truncation=True,
67	            return_tensors="pt",
68	        )
69	        return {
70	            "input_ids": enc["input_ids"].squeeze(0),
71	            "attention_mask": enc["attention_mask"].squeeze(0),
72	            "label": torch.tensor(self.labels[idx], dtype=torch.long),
73	        }
74	
75	
76	class CORALModel(nn.Module):
77	    """
78	    DeBERTa + CORAL ordinal head.
79	
80	    The CORAL head has:
81	      - One shared weight vector w (Linear(hidden, 1, bias=False))
82	      - K-1 independent bias terms b_k
83	    Output: K-1 logits, logit_k = w^T h + b_k
84	    """
85	
86	    def __init__(self, model_name_or_path, num_classes=NUM_DEPTHS, dropout=0.1):
87	        super().__init__()
88	        self.num_thresholds = num_classes - 1
89	        self.encoder = AutoModel.from_pretrained(model_name_or_path)
90	        hidden_size = self.encoder.config.hidden_size
91	        self.dropout = nn.Dropout(dropout)
92	        self.fc = nn.Linear(hidden_size, 1, bias=False)
93	        self.biases = nn.Parameter(torch.zeros(self.num_thresholds))
94	
95	    def forward(self, input_ids, attention_mask):
96	        outputs = self.encoder(input_ids=input_ids, attention_mask=attention_mask)
97	        cls_repr = outputs.last_hidden_state[:, 0, :]
98	        cls_repr = self.dropout(cls_repr)
99	        logit_base = self.fc(cls_repr)  # [B, 1]
100	        logits = logit_base + self.biases  # [B, K-1] broadcast
101	        return logits
102	
103	
104	def coral_loss(logits, labels, num_classes=NUM_DEPTHS):
105	    """
106	    CORAL rank-consistent loss.
107	
108	    For each threshold k (0..K-2), construct binary target 𝟙[y > k]
109	    and compute BCE with logits.
110	    """
111	    num_thresholds = num_classes - 1
112	    ordinal_targets = torch.zeros(len(labels), num_thresholds,
113	                                  device=labels.device, dtype=logits.dtype)
114	    for k in range(num_thresholds):
115	        ordinal_targets[:, k] = (labels > k).float()
116	    return nn.functional.binary_cross_entropy_with_logits(logits, ordinal_targets)
117	
118	
119	def coral_predict(logits):
120	    """depth = number of thresholds where σ(logit) > 0.5"""
121	    probs = torch.sigmoid(logits)
122	    return (probs > 0.5).sum(dim=-1).long()
123	
124	
125	def coral_predict_proba(logits, num_classes=NUM_DEPTHS):
126	    """
127	    Convert cumulative probabilities to per-class probabilities.
128	    P(d=0) = 1 - P(d>0)
129	    P(d=k) = P(d>k-1) - P(d>k)  for k=1..K-2
130	    P(d=K-1) = P(d>K-2)
131	    """
132	    cum_probs = torch.sigmoid(logits).cpu().numpy()  # [B, K-1]
133	    n = cum_probs.shape[0]
134	    probs = np.zeros((n, num_classes))
135	    probs[:, 0] = 1.0 - cum_probs[:, 0]
136	    for k in range(1, num_classes - 1):
137	        probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]
138	    probs[:, num_classes - 1] = cum_probs[:, num_classes - 2]
139	    probs = np.clip(probs, 0, 1)
140	    row_sums = probs.sum(axis=1, keepdims=True)
141	    probs = probs / np.where(row_sums > 0, row_sums, 1.0)
142	    return probs
143	
144	
145	def train_epoch(model, loader, optimizer, device, scaler, max_steps=None):
146	    model.train()
147	    total_loss, total_correct, total_samples = 0.0, 0, 0
148	    for step, batch in enumerate(loader):
149	        if max_steps and step >= max_steps:
150	            break
151	        input_ids = batch["input_ids"].to(device)
152	        attention_mask = batch["attention_mask"].to(device)
153	        labels = batch["label"].to(device)
154	
155	        optimizer.zero_grad()
156	        with torch.amp.autocast("cuda", enabled=scaler is not None):
157	            logits = model(input_ids, attention_mask)
158	            loss = coral_loss(logits, labels)
159	
160	        if scaler is not None:
161	            scaler.scale(loss).backward()
162	            scaler.unscale_(optimizer)
163	            nn.utils.clip_grad_norm_(model.parameters(), 1.0)
164	            scaler.step(optimizer)
165	            scaler.update()
166	        else:
167	            loss.backward()
168	            nn.utils.clip_grad_norm_(model.parameters(), 1.0)
169	            optimizer.step()
170	
171	        preds = coral_predict(logits)
172	        total_loss += loss.item() * len(labels)
173	        total_correct += (preds == labels).sum().item()
174	        total_samples += len(labels)
175	
176	    return total_loss / max(total_samples, 1), total_correct / max(total_samples, 1)
177	
178	
179	@torch.no_grad()
180	def evaluate_model(model, loader, device, max_steps=None):
181	    model.eval()
182	    total_loss, all_preds, all_labels, all_probs = 0.0, [], [], []
183	    total_samples = 0
184	    for step, batch in enumerate(loader):
185	        if max_steps and step >= max_steps:
186	            break
187	        input_ids = batch["input_ids"].to(device)
188	        attention_mask = batch["attention_mask"].to(device)
189	        labels = batch["label"].to(device)
190	
191	        logits = model(input_ids, attention_mask)
192	        loss = coral_loss(logits, labels)
193	
194	        total_loss += loss.item() * len(labels)
195	        total_samples += len(labels)
196	        all_preds.append(coral_predict(logits).cpu().numpy())
197	        all_labels.append(labels.cpu().numpy())
198	        all_probs.append(coral_predict_proba(logits))
199	
200	    return (
201	        total_loss / max(total_samples, 1),
202	        np.concatenate(all_preds),
203	        np.concatenate(all_labels),
204	        np.concatenate(all_probs),
205	    )
206	
207	
208	def main():
209	    parser = argparse.ArgumentParser(description="CORAL ordinal classification baseline (DeBERTa)")
210	    add_common_args(parser)
211	    parser.add_argument("--model_name", default="microsoft/deberta-v3-large")
212	    parser.add_argument("--model_path", default="/root/autodl-tmp/models/deberta-v3-large")
213	    parser.add_argument("--epochs", type=int, default=5)
214	    parser.add_argument("--batch_size", type=int, default=16)
215	    parser.add_argument("--lr", type=float, default=2e-5)
216	    parser.add_argument("--warmup_ratio", type=float, default=0.1)
217	    parser.add_argument("--patience", type=int, default=3)
218	    parser.add_argument("--dropout", type=float, default=0.1)
219	    parser.add_argument("--fp16", action="store_true")
220	    parser.add_argument("--dry_run", action="store_true", help="CPU dry-run, 2 steps only")
221	    args = parser.parse_args()
222	
223	    set_seed(args.seed)
224	    device = torch.device("cpu") if args.dry_run else torch.device("cuda" if torch.cuda.is_available() else "cpu")
225	    print(f"Device: {device}")
226	
227	    texts, labels = load_jsonl_data(args.data_dirs, max_samples=args.max_samples, seed=args.seed)
228	    if args.dry_run and len(texts) > 64:
229	        texts, labels = texts[:64], labels[:64]
230	
231	    train_idx, eval_idx = stratified_split(labels, eval_split=args.eval_split, seed=args.seed)
232	    train_texts = [texts[i] for i in train_idx]
233	    eval_texts = [texts[i] for i in eval_idx]
234	    train_labels, eval_labels = labels[train_idx], labels[eval_idx]
235	    print(f"Train: {len(train_labels)}, Eval: {len(eval_labels)}")
236	
237	    tokenizer = AutoTokenizer.from_pretrained(args.model_path)
238	    train_ds = DepthTextDataset(train_texts, train_labels, tokenizer, args.max_seq_len)
239	    eval_ds = DepthTextDataset(eval_texts, eval_labels, tokenizer, args.max_seq_len)
240	    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True, num_workers=2, pin_memory=True)
241	    eval_loader = DataLoader(eval_ds, batch_size=args.batch_size * 2, shuffle=False, num_workers=2, pin_memory=True)
242	
243	    model = CORALModel(args.model_path, dropout=args.dropout).to(device).float()
244	    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=0.01)
245	    scaler = torch.amp.GradScaler("cuda") if (args.fp16 and device.type == "cuda") else None
246	
247	    total_steps = len(train_loader) * args.epochs
248	    warmup_steps = int(total_steps * args.warmup_ratio)
249	    scheduler = torch.optim.lr_scheduler.LinearLR(
250	        optimizer, start_factor=0.1, total_iters=warmup_steps,
251	    )
252	
253	    max_steps_per_epoch = 2 if args.dry_run else None
254	    best_eval_loss = float("inf")
255	    patience_counter = 0
256	
257	    for epoch in range(args.epochs):
258	        train_loss, train_acc = train_epoch(
259	            model, train_loader, optimizer, device, scaler, max_steps=max_steps_per_epoch,
260	        )
261	        scheduler.step()
262	
263	        eval_loss, y_pred, y_true, y_prob = evaluate_model(
264	            model, eval_loader, device, max_steps=max_steps_per_epoch,
265	        )
266	        print(f"Epoch {epoch+1}/{args.epochs}  train_loss={train_loss:.4f}  "
267	              f"train_acc={train_acc:.4f}  eval_loss={eval_loss:.4f}")
268	
269	        if eval_loss < best_eval_loss - 1e-4:
270	            best_eval_loss = eval_loss
271	            patience_counter = 0
272	            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
273	            best_preds = (y_true.copy(), y_pred.copy(), y_prob.copy())
274	        else:
275	            patience_counter += 1
276	            if patience_counter >= args.patience:
277	                print(f"Early stopping at epoch {epoch+1}")
278	                break
279	
280	        if args.dry_run:
281	            print("Dry run complete (2 steps). Pipeline OK.")
282	            return
283	
284	    model.load_state_dict({k: v.to(device) for k, v in best_state.items()})
285	    y_true, y_pred, y_prob = best_preds
286	    model_tag = "large" if "large" in args.model_name else "base"
287	    evaluate_and_save(f"coral_deberta_{model_tag}", y_true, y_pred, y_prob, args.output_dir)
288	
289	
290	if __name__ == "__main__":
291	    main()
292	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "4cceeba6-8910-4b48-b160-53cb800015fa",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_coral.py",
      "content": "\"\"\"\nBaseline 3: CORAL (Consistent Rank Logits) for recursive generation depth estimation.\n\nClassic ordinal classification method (Cao, Mirjalili & Raschka, 2020).\nConverts K-class ordinal problem into K-1 binary decisions sharing a backbone.\n\nArchitecture: DeBERTa → [CLS] → shared Linear(hidden, 1) + K-1 bias terms\nEach head k outputs logit for P(depth > k), k = 0..K-2.\nDefault: DeBERTa-v3-large (435M) to match DCOL backbone for fair comparison.\n\nCORAL loss (rank-consistent):\n  L = Σ_{k=0}^{K-2} BCE(σ(w^T h + b_k), 𝟙[y > k])\nwhere w is shared across thresholds and b_k is per-threshold bias.\n\nPrediction: depth = Σ_k 𝟙[σ(w^T h + b_k) > 0.5]\n\nRef: Cao, W., Mirjalili, V. & Raschka, S. (2020). \"Rank consistent ordinal\n     regression for neural networks with consistent confidence sets.\"\n     Pattern Recognition, 108, 107736.\n\nInput:  Raw depth_*.jsonl files (--data_dirs)\nOutput: {method}_classification_report.json, {method}_pairwise_auc.json, {method}_predictions.json\n\nUsage:\n  python baseline_coral.py --data_dirs data/  # default: deberta-v3-large\n  python baseline_coral.py --data_dirs data/ --model_name microsoft/deberta-v3-base --model_path /root/autodl-tmp/models/deberta-v3-base\n  python baseline_coral.py --data_dirs data/ --dry_run\n\"\"\"\n\nimport argparse\nimport random\nimport numpy as np\nimport torch\nimport torch.nn as nn\nfrom torch.utils.data import DataLoader, Dataset\nfrom transformers import AutoModel, AutoTokenizer\n\nfrom baseline_utils import (\n    load_jsonl_data, stratified_split, evaluate_and_save,\n    add_common_args, NUM_DEPTHS,\n)\n\n\ndef set_seed(seed):\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n\n\nclass DepthTextDataset(Dataset):\n    def __init__(self, texts, labels, tokenizer, max_seq_len):\n        self.texts = texts\n        self.labels = labels\n        self.tokenizer = tokenizer\n        self.max_seq_len = max_seq_len\n\n    def __len__(self):\n        return len(self.texts)\n\n    def __getitem__(self, idx):\n        enc = self.tokenizer(\n            self.texts[idx],\n            max_length=self.max_seq_len,\n            padding=\"max_length\",\n            truncation=True,\n            return_tensors=\"pt\",\n        )\n        return {\n            \"input_ids\": enc[\"input_ids\"].squeeze(0),\n            \"attention_mask\": enc[\"attention_mask\"].squeeze(0),\n            \"label\": torch.tensor(self.labels[idx], dtype=torch.long),\n        }\n\n\nclass CORALModel(nn.Module):\n    \"\"\"\n    DeBERTa + CORAL ordinal head.\n\n    The CORAL head has:\n      - One shared weight vector w (Linear(hidden, 1, bias=False))\n      - K-1 independent bias terms b_k\n    Output: K-1 logits, logit_k = w^T h + b_k\n    \"\"\"\n\n    def __init__(self, model_name_or_path, num_classes=NUM_DEPTHS, dropout=0.1):\n        super().__init__()\n        self.num_thresholds = num_classes - 1\n        self.encoder = AutoModel.from_pretrained(model_name_or_path)\n        hidden_size = self.encoder.config.hidden_size\n        self.dropout = nn.Dropout(dropout)\n        self.fc = nn.Linear(hidden_size, 1, bias=False)\n        self.biases = nn.Parameter(torch.zeros(self.num_thresholds))\n\n    def forward(self, input_ids, attention_mask):\n        outputs = self.encoder(input_ids=input_ids, attention_mask=attention_mask)\n        cls_repr = outputs.last_hidden_state[:, 0, :]\n        cls_repr = self.dropout(cls_repr)\n        logit_base = self.fc(cls_repr)  # [B, 1]\n        logits = logit_base + self.biases  # [B, K-1] broadcast\n        return logits\n\n\ndef coral_loss(logits, labels, num_classes=NUM_DEPTHS):\n    \"\"\"\n    CORAL rank-consistent loss.\n\n    For each threshold k (0..K-2), construct binary target 𝟙[y > k]\n    and compute BCE with logits.\n    \"\"\"\n    num_thresholds = num_classes - 1\n    ordinal_targets = torch.zeros(len(labels), num_thresholds,\n                                  device=labels.device, dtype=logits.dtype)\n    for k in range(num_thresholds):\n        ordinal_targets[:, k] = (labels > k).float()\n    return nn.functional.binary_cross_entropy_with_logits(logits, ordinal_targets)\n\n\ndef coral_predict(logits):\n    \"\"\"depth = number of thresholds where σ(logit) > 0.5\"\"\"\n    probs = torch.sigmoid(logits)\n    return (probs > 0.5).sum(dim=-1).long()\n\n\ndef coral_predict_proba(logits, num_classes=NUM_DEPTHS):\n    \"\"\"\n    Convert cumulative probabilities to per-class probabilities.\n    P(d=0) = 1 - P(d>0)\n    P(d=k) = P(d>k-1) - P(d>k)  for k=1..K-2\n    P(d=K-1) = P(d>K-2)\n    \"\"\"\n    cum_probs = torch.sigmoid(logits).cpu().numpy()  # [B, K-1]\n    n = cum_probs.shape[0]\n    probs = np.zeros((n, num_classes))\n    probs[:, 0] = 1.0 - cum_probs[:, 0]\n    for k in range(1, num_classes - 1):\n        probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]\n    probs[:, num_classes - 1] = cum_probs[:, num_classes - 2]\n    probs = np.clip(probs, 0, 1)\n    row_sums = probs.sum(axis=1, keepdims=True)\n    probs = probs / np.where(row_sums > 0, row_sums, 1.0)\n    return probs\n\n\ndef train_epoch(model, loader, optimizer, device, scaler, max_steps=None):\n    model.train()\n    total_loss, total_correct, total_samples = 0.0, 0, 0\n    for step, batch in enumerate(loader):\n        if max_steps and step >= max_steps:\n            break\n        input_ids = batch[\"input_ids\"].to(device)\n        attention_mask = batch[\"attention_mask\"].to(device)\n        labels = batch[\"label\"].to(device)\n\n        optimizer.zero_grad()\n        with torch.amp.autocast(\"cuda\", enabled=scaler is not None):\n            logits = model(input_ids, attention_mask)\n            loss = coral_loss(logits, labels)\n\n        if scaler is not None:\n            scaler.scale(loss).backward()\n            scaler.unscale_(optimizer)\n            nn.utils.clip_grad_norm_(model.parameters(), 1.0)\n            scaler.step(optimizer)\n            scaler.update()\n        else:\n            loss.backward()\n            nn.utils.clip_grad_norm_(model.parameters(), 1.0)\n            optimizer.step()\n\n        preds = coral_predict(logits)\n        total_loss += loss.item() * len(labels)\n        total_correct += (preds == labels).sum().item()\n        total_samples += len(labels)\n\n    return total_loss / max(total_samples, 1), total_correct / max(total_samples, 1)\n\n\n@torch.no_grad()\ndef evaluate_model(model, loader, device, max_steps=None):\n    model.eval()\n    total_loss, all_preds, all_labels, all_probs = 0.0, [], [], []\n    total_samples = 0\n    for step, batch in enumerate(loader):\n        if max_steps and step >= max_steps:\n            break\n        input_ids = batch[\"input_ids\"].to(device)\n        attention_mask = batch[\"attention_mask\"].to(device)\n        labels = batch[\"label\"].to(device)\n\n        logits = model(input_ids, attention_mask)\n        loss = coral_loss(logits, labels)\n\n        total_loss += loss.item() * len(labels)\n        total_samples += len(labels)\n        all_preds.append(coral_predict(logits).cpu().numpy())\n        all_labels.append(labels.cpu().numpy())\n        all_probs.append(coral_predict_proba(logits))\n\n    return (\n        total_loss / max(total_samples, 1),\n        np.concatenate(all_preds),\n        np.concatenate(all_labels),\n        np.concatenate(all_probs),\n    )\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"CORAL ordinal classification baseline (DeBERTa)\")\n    add_common_args(parser)\n    parser.add_argument(\"--model_name\", default=\"microsoft/deberta-v3-large\")\n    parser.add_argument(\"--model_path\", default=\"/root/autodl-tmp/models/deberta-v3-large\")\n    parser.add_argument(\"--epochs\", type=int, default=5)\n    parser.add_argument(\"--batch_size\", type=int, default=16)\n    parser.add_argument(\"--lr\", type=float, default=2e-5)\n    parser.add_argument(\"--warmup_ratio\", type=float, default=0.1)\n    parser.add_argument(\"--patience\", type=int, default=3)\n    parser.add_argument(\"--dropout\", type=float, default=0.1)\n    parser.add_argument(\"--fp16\", action=\"store_true\")\n    parser.add_argument(\"--dry_run\", action=\"store_true\", help=\"CPU dry-run, 2 steps only\")\n    args = parser.parse_args()\n\n    set_seed(args.seed)\n    device = torch.device(\"cpu\") if args.dry_run else torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n    print(f\"Device: {device}\")\n\n    texts, labels = load_jsonl_data(args.data_dirs, max_samples=args.max_samples, seed=args.seed)\n    if args.dry_run and len(texts) > 64:\n        texts, labels = texts[:64], labels[:64]\n\n    train_idx, eval_idx = stratified_split(labels, eval_split=args.eval_split, seed=args.seed)\n    train_texts = [texts[i] for i in train_idx]\n    eval_texts = [texts[i] for i in eval_idx]\n    train_labels, eval_labels = labels[train_idx], labels[eval_idx]\n    print(f\"Train: {len(train_labels)}, Eval: {len(eval_labels)}\")\n\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path)\n    train_ds = DepthTextDataset(train_texts, train_labels, tokenizer, args.max_seq_len)\n    eval_ds = DepthTextDataset(eval_texts, eval_labels, tokenizer, args.max_seq_len)\n    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True, num_workers=2, pin_memory=True)\n    eval_loader = DataLoader(eval_ds, batch_size=args.batch_size * 2, shuffle=False, num_workers=2, pin_memory=True)\n\n    model = CORALModel(args.model_path, dropout=args.dropout).to(device).float()\n    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=0.01)\n    scaler = torch.amp.GradScaler(\"cuda\") if (args.fp16 and device.type == \"cuda\") else None\n\n    total_steps = len(train_loader) * args.epochs\n    warmup_steps = int(total_steps * args.warmup_ratio)\n    scheduler = torch.optim.lr_scheduler.LinearLR(\n        optimizer, start_factor=0.1, total_iters=warmup_steps,\n    )\n\n    max_steps_per_epoch = 2 if args.dry_run else None\n    best_eval_loss = float(\"inf\")\n    patience_counter = 0\n\n    for epoch in range(args.epochs):\n        train_loss, train_acc = train_epoch(\n            model, train_loader, optimizer, device, scaler, max_steps=max_steps_per_epoch,\n        )\n        scheduler.step()\n\n        eval_loss, y_pred, y_true, y_prob = evaluate_model(\n            model, eval_loader, device, max_steps=max_steps_per_epoch,\n        )\n        print(f\"Epoch {epoch+1}/{args.epochs}  train_loss={train_loss:.4f}  \"\n              f\"train_acc={train_acc:.4f}  eval_loss={eval_loss:.4f}\")\n\n        if eval_loss < best_eval_loss - 1e-4:\n            best_eval_loss = eval_loss\n            patience_counter = 0\n            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}\n            best_preds = (y_true.copy(), y_pred.copy(), y_prob.copy())\n        else:\n            patience_counter += 1\n            if patience_counter >= args.patience:\n                print(f\"Early stopping at epoch {epoch+1}\")\n                break\n\n        if args.dry_run:\n            print(\"Dry run complete (2 steps). Pipeline OK.\")\n            return\n\n    model.load_state_dict({k: v.to(device) for k, v in best_state.items()})\n    y_true, y_pred, y_prob = best_preds\n    model_tag = \"large\" if \"large\" in args.model_name else \"base\"\n    evaluate_and_save(f\"coral_deberta_{model_tag}\", y_true, y_pred, y_prob, args.output_dir)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 292,
      "startLine": 1,
      "totalLines": 292
    }
  }
}
```

</details>

---


### Tool call

_source line 97_

<details open><summary>🔧 Tool call — Read · `toolu_01EKETaBFZmBZEf8DAs296mh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_ce_classification.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "4db97f1e-87b7-4077-9a1c-fc61ae01489b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Ai8DvYTokR9U6g6n5HQqM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15361,
      "cache_read_input_tokens": 26477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15361
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

_source line 98 · 2026-05-14T23:02:24.277Z_

<details><summary>↩ Tool result · `toolu_01EKETaBFZmBZEf8DAs296mh`</summary>

```text
1	"""
2	Baseline 4: Standard Cross-Entropy Classification for recursive generation depth estimation.
3	
4	Standard 4-class classification with DeBERTa backbone and CE loss.
5	No ordinal awareness — serves as ablation for DCOL and CORAL to demonstrate
6	that ordinal-aware losses add value.
7	
8	Architecture: DeBERTa → [CLS] pooling → Linear(hidden, 4) → CrossEntropyLoss
9	Default: DeBERTa-v3-large (435M) to match DCOL backbone for fair comparison.
10	
11	Input:  Raw depth_*.jsonl files (--data_dirs)
12	Output: {method}_classification_report.json, {method}_pairwise_auc.json, {method}_predictions.json
13	
14	Usage:
15	  python baseline_ce_classification.py --data_dirs data/  # default: deberta-v3-large
16	  python baseline_ce_classification.py --data_dirs data/ --model_name microsoft/deberta-v3-base --model_path /root/autodl-tmp/models/deberta-v3-base
17	  python baseline_ce_classification.py --data_dirs data/ --dry_run  # CPU, 2 steps
18	"""
19	
20	import argparse
21	import random
22	import numpy as np
23	import torch
24	import torch.nn as nn
25	from torch.utils.data import DataLoader, Dataset
26	from transformers import AutoModel, AutoTokenizer
27	
28	from baseline_utils import (
29	    load_jsonl_data, stratified_split, evaluate_and_save,
30	    add_common_args, NUM_DEPTHS,
31	)
32	
33	
34	def set_seed(seed):
35	    random.seed(seed)
36	    np.random.seed(seed)
37	    torch.manual_seed(seed)
38	    torch.cuda.manual_seed_all(seed)
39	
40	
41	class DepthTextDataset(Dataset):
42	    def __init__(self, texts, labels, tokenizer, max_seq_len):
43	        self.texts = texts
44	        self.labels = labels
45	        self.tokenizer = tokenizer
46	        self.max_seq_len = max_seq_len
47	
48	    def __len__(self):
49	        return len(self.texts)
50	
51	    def __getitem__(self, idx):
52	        enc = self.tokenizer(
53	            self.texts[idx],
54	            max_length=self.max_seq_len,
55	            padding="max_length",
56	            truncation=True,
57	            return_tensors="pt",
58	        )
59	        return {
60	            "input_ids": enc["input_ids"].squeeze(0),
61	            "attention_mask": enc["attention_mask"].squeeze(0),
62	            "label": torch.tensor(self.labels[idx], dtype=torch.long),
63	        }
64	
65	
66	class CEClassifier(nn.Module):
67	    """DeBERTa + linear head with standard cross-entropy loss."""
68	
69	    def __init__(self, model_name_or_path, num_classes=NUM_DEPTHS, dropout=0.1):
70	        super().__init__()
71	        self.encoder = AutoModel.from_pretrained(model_name_or_path)
72	        hidden_size = self.encoder.config.hidden_size
73	        self.dropout = nn.Dropout(dropout)
74	        self.classifier = nn.Linear(hidden_size, num_classes)
75	
76	    def forward(self, input_ids, attention_mask):
77	        outputs = self.encoder(input_ids=input_ids, attention_mask=attention_mask)
78	        cls_repr = outputs.last_hidden_state[:, 0, :]
79	        cls_repr = self.dropout(cls_repr)
80	        logits = self.classifier(cls_repr)
81	        return logits
82	
83	
84	def train_epoch(model, loader, optimizer, criterion, device, scaler, max_steps=None):
85	    model.train()
86	    total_loss, total_correct, total_samples = 0.0, 0, 0
87	    for step, batch in enumerate(loader):
88	        if max_steps and step >= max_steps:
89	            break
90	        input_ids = batch["input_ids"].to(device)
91	        attention_mask = batch["attention_mask"].to(device)
92	        labels = batch["label"].to(device)
93	
94	        optimizer.zero_grad()
95	        with torch.amp.autocast("cuda", enabled=scaler is not None):
96	            logits = model(input_ids, attention_mask)
97	            loss = criterion(logits, labels)
98	
99	        if scaler is not None:
100	            scaler.scale(loss).backward()
101	            scaler.unscale_(optimizer)
102	            nn.utils.clip_grad_norm_(model.parameters(), 1.0)
103	            scaler.step(optimizer)
104	            scaler.update()
105	        else:
106	            loss.backward()
107	            nn.utils.clip_grad_norm_(model.parameters(), 1.0)
108	            optimizer.step()
109	
110	        total_loss += loss.item() * len(labels)
111	        total_correct += (logits.argmax(dim=-1) == labels).sum().item()
112	        total_samples += len(labels)
113	
114	    return total_loss / max(total_samples, 1), total_correct / max(total_samples, 1)
115	
116	
117	@torch.no_grad()
118	def evaluate_model(model, loader, criterion, device, max_steps=None):
119	    model.eval()
120	    total_loss, all_preds, all_labels, all_probs = 0.0, [], [], []
121	    total_samples = 0
122	    for step, batch in enumerate(loader):
123	        if max_steps and step >= max_steps:
124	            break
125	        input_ids = batch["input_ids"].to(device)
126	        attention_mask = batch["attention_mask"].to(device)
127	        labels = batch["label"].to(device)
128	
129	        logits = model(input_ids, attention_mask)
130	        loss = criterion(logits, labels)
131	
132	        total_loss += loss.item() * len(labels)
133	        total_samples += len(labels)
134	        probs = torch.softmax(logits, dim=-1)
135	        all_preds.append(logits.argmax(dim=-1).cpu().numpy())
136	        all_labels.append(labels.cpu().numpy())
137	        all_probs.append(probs.cpu().numpy())
138	
139	    return (
140	        total_loss / max(total_samples, 1),
141	        np.concatenate(all_preds),
142	        np.concatenate(all_labels),
143	        np.concatenate(all_probs),
144	    )
145	
146	
147	def main():
148	    parser = argparse.ArgumentParser(description="Standard CE Classification baseline (DeBERTa)")
149	    add_common_args(parser)
150	    parser.add_argument("--model_name", default="microsoft/deberta-v3-large")
151	    parser.add_argument("--model_path", default="/root/autodl-tmp/models/deberta-v3-large")
152	    parser.add_argument("--epochs", type=int, default=5)
153	    parser.add_argument("--batch_size", type=int, default=16)
154	    parser.add_argument("--lr", type=float, default=2e-5)
155	    parser.add_argument("--warmup_ratio", type=float, default=0.1)
156	    parser.add_argument("--patience", type=int, default=3)
157	    parser.add_argument("--dropout", type=float, default=0.1)
158	    parser.add_argument("--fp16", action="store_true")
159	    parser.add_argument("--dry_run", action="store_true", help="CPU dry-run, 2 steps only")
160	    args = parser.parse_args()
161	
162	    set_seed(args.seed)
163	    device = torch.device("cpu") if args.dry_run else torch.device("cuda" if torch.cuda.is_available() else "cpu")
164	    print(f"Device: {device}")
165	
166	    texts, labels = load_jsonl_data(args.data_dirs, max_samples=args.max_samples, seed=args.seed)
167	    if args.dry_run and len(texts) > 64:
168	        texts, labels = texts[:64], labels[:64]
169	
170	    train_idx, eval_idx = stratified_split(labels, eval_split=args.eval_split, seed=args.seed)
171	    train_texts = [texts[i] for i in train_idx]
172	    eval_texts = [texts[i] for i in eval_idx]
173	    train_labels, eval_labels = labels[train_idx], labels[eval_idx]
174	    print(f"Train: {len(train_labels)}, Eval: {len(eval_labels)}")
175	
176	    tokenizer = AutoTokenizer.from_pretrained(args.model_path)
177	    train_ds = DepthTextDataset(train_texts, train_labels, tokenizer, args.max_seq_len)
178	    eval_ds = DepthTextDataset(eval_texts, eval_labels, tokenizer, args.max_seq_len)
179	    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True, num_workers=2, pin_memory=True)
180	    eval_loader = DataLoader(eval_ds, batch_size=args.batch_size * 2, shuffle=False, num_workers=2, pin_memory=True)
181	
182	    model = CEClassifier(args.model_path, dropout=args.dropout).to(device).float()
183	    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=0.01)
184	    criterion = nn.CrossEntropyLoss()
185	    scaler = torch.amp.GradScaler("cuda") if (args.fp16 and device.type == "cuda") else None
186	
187	    total_steps = len(train_loader) * args.epochs
188	    warmup_steps = int(total_steps * args.warmup_ratio)
189	    scheduler = torch.optim.lr_scheduler.LinearLR(
190	        optimizer, start_factor=0.1, total_iters=warmup_steps,
191	    )
192	
193	    max_steps_per_epoch = 2 if args.dry_run else None
194	    best_eval_loss = float("inf")
195	    patience_counter = 0
196	
197	    for epoch in range(args.epochs):
198	        train_loss, train_acc = train_epoch(
199	            model, train_loader, optimizer, criterion, device, scaler, max_steps=max_steps_per_epoch,
200	        )
201	        scheduler.step()
202	
203	        eval_loss, y_pred, y_true, y_prob = evaluate_model(
204	            model, eval_loader, criterion, device, max_steps=max_steps_per_epoch,
205	        )
206	        print(f"Epoch {epoch+1}/{args.epochs}  train_loss={train_loss:.4f}  "
207	              f"train_acc={train_acc:.4f}  eval_loss={eval_loss:.4f}")
208	
209	        if eval_loss < best_eval_loss - 1e-4:
210	            best_eval_loss = eval_loss
211	            patience_counter = 0
212	            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
213	            best_preds = (y_true.copy(), y_pred.copy(), y_prob.copy())
214	        else:
215	            patience_counter += 1
216	            if patience_counter >= args.patience:
217	                print(f"Early stopping at epoch {epoch+1}")
218	                break
219	
220	        if args.dry_run:
221	            print("Dry run complete (2 steps). Pipeline OK.")
222	            return
223	
224	    model.load_state_dict({k: v.to(device) for k, v in best_state.items()})
225	    y_true, y_pred, y_prob = best_preds
226	    model_tag = "large" if "large" in args.model_name else "base"
227	    evaluate_and_save(f"ce_deberta_{model_tag}", y_true, y_pred, y_prob, args.output_dir)
228	
229	
230	if __name__ == "__main__":
231	    main()
232	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "ab092545-0ddc-4888-834f-2fd924784c3b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_ce_classification.py",
      "content": "\"\"\"\nBaseline 4: Standard Cross-Entropy Classification for recursive generation depth estimation.\n\nStandard 4-class classification with DeBERTa backbone and CE loss.\nNo ordinal awareness — serves as ablation for DCOL and CORAL to demonstrate\nthat ordinal-aware losses add value.\n\nArchitecture: DeBERTa → [CLS] pooling → Linear(hidden, 4) → CrossEntropyLoss\nDefault: DeBERTa-v3-large (435M) to match DCOL backbone for fair comparison.\n\nInput:  Raw depth_*.jsonl files (--data_dirs)\nOutput: {method}_classification_report.json, {method}_pairwise_auc.json, {method}_predictions.json\n\nUsage:\n  python baseline_ce_classification.py --data_dirs data/  # default: deberta-v3-large\n  python baseline_ce_classification.py --data_dirs data/ --model_name microsoft/deberta-v3-base --model_path /root/autodl-tmp/models/deberta-v3-base\n  python baseline_ce_classification.py --data_dirs data/ --dry_run  # CPU, 2 steps\n\"\"\"\n\nimport argparse\nimport random\nimport numpy as np\nimport torch\nimport torch.nn as nn\nfrom torch.utils.data import DataLoader, Dataset\nfrom transformers import AutoModel, AutoTokenizer\n\nfrom baseline_utils import (\n    load_jsonl_data, stratified_split, evaluate_and_save,\n    add_common_args, NUM_DEPTHS,\n)\n\n\ndef set_seed(seed):\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n\n\nclass DepthTextDataset(Dataset):\n    def __init__(self, texts, labels, tokenizer, max_seq_len):\n        self.texts = texts\n        self.labels = labels\n        self.tokenizer = tokenizer\n        self.max_seq_len = max_seq_len\n\n    def __len__(self):\n        return len(self.texts)\n\n    def __getitem__(self, idx):\n        enc = self.tokenizer(\n            self.texts[idx],\n            max_length=self.max_seq_len,\n            padding=\"max_length\",\n            truncation=True,\n            return_tensors=\"pt\",\n        )\n        return {\n            \"input_ids\": enc[\"input_ids\"].squeeze(0),\n            \"attention_mask\": enc[\"attention_mask\"].squeeze(0),\n            \"label\": torch.tensor(self.labels[idx], dtype=torch.long),\n        }\n\n\nclass CEClassifier(nn.Module):\n    \"\"\"DeBERTa + linear head with standard cross-entropy loss.\"\"\"\n\n    def __init__(self, model_name_or_path, num_classes=NUM_DEPTHS, dropout=0.1):\n        super().__init__()\n        self.encoder = AutoModel.from_pretrained(model_name_or_path)\n        hidden_size = self.encoder.config.hidden_size\n        self.dropout = nn.Dropout(dropout)\n        self.classifier = nn.Linear(hidden_size, num_classes)\n\n    def forward(self, input_ids, attention_mask):\n        outputs = self.encoder(input_ids=input_ids, attention_mask=attention_mask)\n        cls_repr = outputs.last_hidden_state[:, 0, :]\n        cls_repr = self.dropout(cls_repr)\n        logits = self.classifier(cls_repr)\n        return logits\n\n\ndef train_epoch(model, loader, optimizer, criterion, device, scaler, max_steps=None):\n    model.train()\n    total_loss, total_correct, total_samples = 0.0, 0, 0\n    for step, batch in enumerate(loader):\n        if max_steps and step >= max_steps:\n            break\n        input_ids = batch[\"input_ids\"].to(device)\n        attention_mask = batch[\"attention_mask\"].to(device)\n        labels = batch[\"label\"].to(device)\n\n        optimizer.zero_grad()\n        with torch.amp.autocast(\"cuda\", enabled=scaler is not None):\n            logits = model(input_ids, attention_mask)\n            loss = criterion(logits, labels)\n\n        if scaler is not None:\n            scaler.scale(loss).backward()\n            scaler.unscale_(optimizer)\n            nn.utils.clip_grad_norm_(model.parameters(), 1.0)\n            scaler.step(optimizer)\n            scaler.update()\n        else:\n            loss.backward()\n            nn.utils.clip_grad_norm_(model.parameters(), 1.0)\n            optimizer.step()\n\n        total_loss += loss.item() * len(labels)\n        total_correct += (logits.argmax(dim=-1) == labels).sum().item()\n        total_samples += len(labels)\n\n    return total_loss / max(total_samples, 1), total_correct / max(total_samples, 1)\n\n\n@torch.no_grad()\ndef evaluate_model(model, loader, criterion, device, max_steps=None):\n    model.eval()\n    total_loss, all_preds, all_labels, all_probs = 0.0, [], [], []\n    total_samples = 0\n    for step, batch in enumerate(loader):\n        if max_steps and step >= max_steps:\n            break\n        input_ids = batch[\"input_ids\"].to(device)\n        attention_mask = batch[\"attention_mask\"].to(device)\n        labels = batch[\"label\"].to(device)\n\n        logits = model(input_ids, attention_mask)\n        loss = criterion(logits, labels)\n\n        total_loss += loss.item() * len(labels)\n        total_samples += len(labels)\n        probs = torch.softmax(logits, dim=-1)\n        all_preds.append(logits.argmax(dim=-1).cpu().numpy())\n        all_labels.append(labels.cpu().numpy())\n        all_probs.append(probs.cpu().numpy())\n\n    return (\n        total_loss / max(total_samples, 1),\n        np.concatenate(all_preds),\n        np.concatenate(all_labels),\n        np.concatenate(all_probs),\n    )\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Standard CE Classification baseline (DeBERTa)\")\n    add_common_args(parser)\n    parser.add_argument(\"--model_name\", default=\"microsoft/deberta-v3-large\")\n    parser.add_argument(\"--model_path\", default=\"/root/autodl-tmp/models/deberta-v3-large\")\n    parser.add_argument(\"--epochs\", type=int, default=5)\n    parser.add_argument(\"--batch_size\", type=int, default=16)\n    parser.add_argument(\"--lr\", type=float, default=2e-5)\n    parser.add_argument(\"--warmup_ratio\", type=float, default=0.1)\n    parser.add_argument(\"--patience\", type=int, default=3)\n    parser.add_argument(\"--dropout\", type=float, default=0.1)\n    parser.add_argument(\"--fp16\", action=\"store_true\")\n    parser.add_argument(\"--dry_run\", action=\"store_true\", help=\"CPU dry-run, 2 steps only\")\n    args = parser.parse_args()\n\n    set_seed(args.seed)\n    device = torch.device(\"cpu\") if args.dry_run else torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n    print(f\"Device: {device}\")\n\n    texts, labels = load_jsonl_data(args.data_dirs, max_samples=args.max_samples, seed=args.seed)\n    if args.dry_run and len(texts) > 64:\n        texts, labels = texts[:64], labels[:64]\n\n    train_idx, eval_idx = stratified_split(labels, eval_split=args.eval_split, seed=args.seed)\n    train_texts = [texts[i] for i in train_idx]\n    eval_texts = [texts[i] for i in eval_idx]\n    train_labels, eval_labels = labels[train_idx], labels[eval_idx]\n    print(f\"Train: {len(train_labels)}, Eval: {len(eval_labels)}\")\n\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path)\n    train_ds = DepthTextDataset(train_texts, train_labels, tokenizer, args.max_seq_len)\n    eval_ds = DepthTextDataset(eval_texts, eval_labels, tokenizer, args.max_seq_len)\n    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True, num_workers=2, pin_memory=True)\n    eval_loader = DataLoader(eval_ds, batch_size=args.batch_size * 2, shuffle=False, num_workers=2, pin_memory=True)\n\n    model = CEClassifier(args.model_path, dropout=args.dropout).to(device).float()\n    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=0.01)\n    criterion = nn.CrossEntropyLoss()\n    scaler = torch.amp.GradScaler(\"cuda\") if (args.fp16 and device.type == \"cuda\") else None\n\n    total_steps = len(train_loader) * args.epochs\n    warmup_steps = int(total_steps * args.warmup_ratio)\n    scheduler = torch.optim.lr_scheduler.LinearLR(\n        optimizer, start_factor=0.1, total_iters=warmup_steps,\n    )\n\n    max_steps_per_epoch = 2 if args.dry_run else None\n    best_eval_loss = float(\"inf\")\n    patience_counter = 0\n\n    for epoch in range(args.epochs):\n        train_loss, train_acc = train_epoch(\n            model, train_loader, optimizer, criterion, device, scaler, max_steps=max_steps_per_epoch,\n        )\n        scheduler.step()\n\n        eval_loss, y_pred, y_true, y_prob = evaluate_model(\n            model, eval_loader, criterion, device, max_steps=max_steps_per_epoch,\n        )\n        print(f\"Epoch {epoch+1}/{args.epochs}  train_loss={train_loss:.4f}  \"\n              f\"train_acc={train_acc:.4f}  eval_loss={eval_loss:.4f}\")\n\n        if eval_loss < best_eval_loss - 1e-4:\n            best_eval_loss = eval_loss\n            patience_counter = 0\n            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}\n            best_preds = (y_true.copy(), y_pred.copy(), y_prob.copy())\n        else:\n            patience_counter += 1\n            if patience_counter >= args.patience:\n                print(f\"Early stopping at epoch {epoch+1}\")\n                break\n\n        if args.dry_run:\n            print(\"Dry run complete (2 steps). Pipeline OK.\")\n            return\n\n    model.load_state_dict({k: v.to(device) for k, v in best_state.items()})\n    y_true, y_pred, y_prob = best_preds\n    model_tag = \"large\" if \"large\" in args.model_name else \"base\"\n    evaluate_and_save(f\"ce_deberta_{model_tag}\", y_true, y_pred, y_prob, args.output_dir)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 232,
      "startLine": 1,
      "totalLines": 232
    }
  }
}
```

</details>

---


### Tool call

_source line 99_

<details open><summary>🔧 Tool call — Read · `toolu_01PC15JV3q1VGq4WiELZdBFP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_diveye_ordinal.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "287e3a46-b36c-429d-a8c8-f3dd72910e80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Ai8DvYTokR9U6g6n5HQqM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15361,
      "cache_read_input_tokens": 26477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15361
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

_source line 100 · 2026-05-14T23:02:24.618Z_

<details><summary>↩ Tool result · `toolu_01PC15JV3q1VGq4WiELZdBFP`</summary>

```text
1	"""
2	Baseline 1: DivEye Binary → Ordinal for recursive generation depth estimation.
3	
4	Adapts DivEye (Basani & Chen, TMLR 2026) from binary human-vs-AI detection to
5	ordinal depth classification. DivEye's core insight: AI-generated text has lower
6	surprisal diversity than human text; deeper recursion should further reduce diversity.
7	
8	Method:
9	  - Extract DivEye-style diversity features (surprisal variance, entropy, lexical
10	    diversity, repetition) from pre-computed 19-dim feature vectors
11	  - Train One-vs-Rest (OVR) classifiers: one binary classifier per depth
12	  - Predict depth = argmax(OVR decision scores)
13	
14	Ref: Basani, A. R. & Chen, P.-Y. (2026). "Diversity Boosts AI-Generated Text
15	     Detection." TMLR. GitHub: https://github.com/IBM/diveye
16	
17	Input:  Pre-extracted features JSONL (--features_path)
18	Output: {method}_classification_report.json, {method}_pairwise_auc.json, {method}_predictions.json
19	
20	Usage:
21	  python baseline_diveye_ordinal.py --features_path data/features_all.jsonl
22	  python baseline_diveye_ordinal.py --features_path data/features_all.jsonl --base_clf svm
23	"""
24	
25	import argparse
26	import numpy as np
27	from sklearn.preprocessing import StandardScaler
28	from sklearn.multiclass import OneVsRestClassifier
29	from sklearn.linear_model import LogisticRegression
30	from sklearn.svm import SVC
31	from sklearn.calibration import CalibratedClassifierCV
32	
33	from baseline_utils import (
34	    load_features, stratified_split, evaluate_and_save,
35	    add_common_args, NUM_DEPTHS, FEATURE_NAMES,
36	)
37	
38	# DivEye feature subset: surprisal distributional + lexical diversity + repetition
39	DIVEYE_FEATURES = [
40	    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
41	    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
42	    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
43	    "rep_2gram", "rep_3gram", "rep_4gram",
44	]
45	DIVEYE_INDICES = [FEATURE_NAMES.index(f) for f in DIVEYE_FEATURES]
46	
47	
48	class DivEyeOrdinal:
49	    """OVR classifier on DivEye diversity features for ordinal depth prediction."""
50	
51	    def __init__(self, base_clf="logistic", C=1.0, seed=42):
52	        self.scaler = StandardScaler()
53	        self.seed = seed
54	        if base_clf == "logistic":
55	            estimator = LogisticRegression(
56	                C=C, max_iter=1000, random_state=seed,
57	            )
58	        elif base_clf == "svm":
59	            estimator = CalibratedClassifierCV(
60	                SVC(C=C, kernel="rbf", random_state=seed),
61	                cv=3,
62	            )
63	        else:
64	            raise ValueError(f"Unknown base_clf: {base_clf}")
65	        self.ovr = OneVsRestClassifier(estimator)
66	
67	    def fit(self, X, y):
68	        Xd = self.scaler.fit_transform(X[:, DIVEYE_INDICES])
69	        self.ovr.fit(Xd, y)
70	
71	    def predict(self, X):
72	        Xd = self.scaler.transform(X[:, DIVEYE_INDICES])
73	        return self.ovr.predict(Xd)
74	
75	    def predict_proba(self, X):
76	        Xd = self.scaler.transform(X[:, DIVEYE_INDICES])
77	        if hasattr(self.ovr, "predict_proba"):
78	            probs = self.ovr.predict_proba(Xd)
79	        else:
80	            scores = self.ovr.decision_function(Xd)
81	            from scipy.special import softmax
82	            probs = softmax(scores, axis=1)
83	        if probs.shape[1] < NUM_DEPTHS:
84	            full = np.zeros((probs.shape[0], NUM_DEPTHS))
85	            for i, c in enumerate(self.ovr.classes_):
86	                full[:, c] = probs[:, i]
87	            return full
88	        return probs
89	
90	
91	def main():
92	    parser = argparse.ArgumentParser(description="DivEye Binary→Ordinal baseline")
93	    add_common_args(parser)
94	    parser.add_argument("--base_clf", choices=["logistic", "svm"], default="logistic")
95	    parser.add_argument("--C", type=float, default=1.0, help="Regularization strength")
96	    args = parser.parse_args()
97	
98	    if args.features_path is None:
99	        print("ERROR: --features_path is required for DivEye baseline.")
100	        print("Run extract_features.py first to generate features JSONL.")
101	        return
102	
103	    X, y = load_features(args.features_path)
104	    train_idx, eval_idx = stratified_split(y, eval_split=args.eval_split, seed=args.seed)
105	    X_train, y_train = X[train_idx], y[train_idx]
106	    X_eval, y_eval = X[eval_idx], y[eval_idx]
107	    print(f"Train: {len(y_train)}, Eval: {len(y_eval)}")
108	
109	    method_name = f"diveye_ovr_{args.base_clf}"
110	    model = DivEyeOrdinal(base_clf=args.base_clf, C=args.C, seed=args.seed)
111	    model.fit(X_train, y_train)
112	    y_pred = model.predict(X_eval)
113	    y_prob = model.predict_proba(X_eval)
114	    evaluate_and_save(method_name, y_eval, y_pred, y_prob, args.output_dir)
115	
116	
117	if __name__ == "__main__":
118	    main()
119	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "1d8b9a4e-b409-4b27-b422-f7147bc8d2b3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_diveye_ordinal.py",
      "content": "\"\"\"\nBaseline 1: DivEye Binary → Ordinal for recursive generation depth estimation.\n\nAdapts DivEye (Basani & Chen, TMLR 2026) from binary human-vs-AI detection to\nordinal depth classification. DivEye's core insight: AI-generated text has lower\nsurprisal diversity than human text; deeper recursion should further reduce diversity.\n\nMethod:\n  - Extract DivEye-style diversity features (surprisal variance, entropy, lexical\n    diversity, repetition) from pre-computed 19-dim feature vectors\n  - Train One-vs-Rest (OVR) classifiers: one binary classifier per depth\n  - Predict depth = argmax(OVR decision scores)\n\nRef: Basani, A. R. & Chen, P.-Y. (2026). \"Diversity Boosts AI-Generated Text\n     Detection.\" TMLR. GitHub: https://github.com/IBM/diveye\n\nInput:  Pre-extracted features JSONL (--features_path)\nOutput: {method}_classification_report.json, {method}_pairwise_auc.json, {method}_predictions.json\n\nUsage:\n  python baseline_diveye_ordinal.py --features_path data/features_all.jsonl\n  python baseline_diveye_ordinal.py --features_path data/features_all.jsonl --base_clf svm\n\"\"\"\n\nimport argparse\nimport numpy as np\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.multiclass import OneVsRestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.svm import SVC\nfrom sklearn.calibration import CalibratedClassifierCV\n\nfrom baseline_utils import (\n    load_features, stratified_split, evaluate_and_save,\n    add_common_args, NUM_DEPTHS, FEATURE_NAMES,\n)\n\n# DivEye feature subset: surprisal distributional + lexical diversity + repetition\nDIVEYE_FEATURES = [\n    \"mean_ppl\", \"var_ppl\", \"skewness_ppl\", \"kurtosis_ppl\",\n    \"mean_surprisal\", \"var_surprisal\", \"entropy_of_surprisal\",\n    \"type_token_ratio\", \"hapax_ratio\", \"bigram_entropy\", \"trigram_entropy\",\n    \"rep_2gram\", \"rep_3gram\", \"rep_4gram\",\n]\nDIVEYE_INDICES = [FEATURE_NAMES.index(f) for f in DIVEYE_FEATURES]\n\n\nclass DivEyeOrdinal:\n    \"\"\"OVR classifier on DivEye diversity features for ordinal depth prediction.\"\"\"\n\n    def __init__(self, base_clf=\"logistic\", C=1.0, seed=42):\n        self.scaler = StandardScaler()\n        self.seed = seed\n        if base_clf == \"logistic\":\n            estimator = LogisticRegression(\n                C=C, max_iter=1000, random_state=seed,\n            )\n        elif base_clf == \"svm\":\n            estimator = CalibratedClassifierCV(\n                SVC(C=C, kernel=\"rbf\", random_state=seed),\n                cv=3,\n            )\n        else:\n            raise ValueError(f\"Unknown base_clf: {base_clf}\")\n        self.ovr = OneVsRestClassifier(estimator)\n\n    def fit(self, X, y):\n        Xd = self.scaler.fit_transform(X[:, DIVEYE_INDICES])\n        self.ovr.fit(Xd, y)\n\n    def predict(self, X):\n        Xd = self.scaler.transform(X[:, DIVEYE_INDICES])\n        return self.ovr.predict(Xd)\n\n    def predict_proba(self, X):\n        Xd = self.scaler.transform(X[:, DIVEYE_INDICES])\n        if hasattr(self.ovr, \"predict_proba\"):\n            probs = self.ovr.predict_proba(Xd)\n        else:\n            scores = self.ovr.decision_function(Xd)\n            from scipy.special import softmax\n            probs = softmax(scores, axis=1)\n        if probs.shape[1] < NUM_DEPTHS:\n            full = np.zeros((probs.shape[0], NUM_DEPTHS))\n            for i, c in enumerate(self.ovr.classes_):\n                full[:, c] = probs[:, i]\n            return full\n        return probs\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"DivEye Binary→Ordinal baseline\")\n    add_common_args(parser)\n    parser.add_argument(\"--base_clf\", choices=[\"logistic\", \"svm\"], default=\"logistic\")\n    parser.add_argument(\"--C\", type=float, default=1.0, help=\"Regularization strength\")\n    args = parser.parse_args()\n\n    if args.features_path is None:\n        print(\"ERROR: --features_path is required for DivEye baseline.\")\n        print(\"Run extract_features.py first to generate features JSONL.\")\n        return\n\n    X, y = load_features(args.features_path)\n    train_idx, eval_idx = stratified_split(y, eval_split=args.eval_split, seed=args.seed)\n    X_train, y_train = X[train_idx], y[train_idx]\n    X_eval, y_eval = X[eval_idx], y[eval_idx]\n    print(f\"Train: {len(y_train)}, Eval: {len(y_eval)}\")\n\n    method_name = f\"diveye_ovr_{args.base_clf}\"\n    model = DivEyeOrdinal(base_clf=args.base_clf, C=args.C, seed=args.seed)\n    model.fit(X_train, y_train)\n    y_pred = model.predict(X_eval)\n    y_prob = model.predict_proba(X_eval)\n    evaluate_and_save(method_name, y_eval, y_pred, y_prob, args.output_dir)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 119,
      "startLine": 1,
      "totalLines": 119
    }
  }
}
```

</details>

---


### Assistant

_source line 101_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the zero-shot LLM baseline and check what exists on the remote server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "ac50a007-c5ca-4bf1-a720-787177366dba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ToZEZvHumAKaeYQow84muo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10089,
      "cache_read_input_tokens": 41838,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10089
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

_source line 102_

Now let me check the zero-shot LLM baseline and the remote server state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "e81ce3c1-90a3-4be4-a046-fd5630af15ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ToZEZvHumAKaeYQow84muo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10089,
      "cache_read_input_tokens": 41838,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10089
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

_source line 103_

<details open><summary>🔧 Tool call — Read · `toolu_01EhkMbcdkBhcEQoTNU7BYgw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_zeroshot_llm.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "7e7f8bba-6f54-47eb-a5b8-ab7cbba82873",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ToZEZvHumAKaeYQow84muo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10089,
      "cache_read_input_tokens": 41838,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10089
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

_source line 104 · 2026-05-14T23:02:30.333Z_

<details><summary>↩ Tool result · `toolu_01EhkMbcdkBhcEQoTNU7BYgw`</summary>

```text
1	"""
2	Baseline 5: Zero-shot LLM Prompting for recursive generation depth estimation.
3	
4	Uses an LLM (Claude or OpenAI GPT) to directly judge the recursion depth of a
5	text passage. No training required — pure in-context prompting.
6	
7	The prompt explains the concept of recursive text generation and asks the LLM to
8	classify the text into depth 0 (human-written), 1, 2, or 3 (each successive depth
9	is generated by an LLM conditioned on the previous depth's output).
10	
11	Supports: --provider claude (Anthropic API) or --provider openai (OpenAI API)
12	
13	Input:  Raw depth_*.jsonl files (--data_dirs)
14	Output: {method}_classification_report.json, {method}_pairwise_auc.json, {method}_predictions.json
15	
16	Usage:
17	  python baseline_zeroshot_llm.py --data_dirs data/ --provider claude --max_samples 200
18	  python baseline_zeroshot_llm.py --data_dirs data/ --provider openai --model gpt-4o
19	"""
20	
21	import argparse
22	import json
23	import os
24	import re
25	import time
26	import numpy as np
27	from collections import Counter
28	
29	from baseline_utils import (
30	    load_jsonl_data, stratified_split, evaluate_and_save,
31	    add_common_args, NUM_DEPTHS,
32	)
33	
34	SYSTEM_PROMPT = """You are an expert at detecting AI-generated text and estimating its generation depth.
35	
36	"Recursive generation depth" refers to how many times a text has been through an LLM generation cycle:
37	- Depth 0: Original human-written text (e.g., Wikipedia, StackExchange, academic papers)
38	- Depth 1: Text generated by an LLM given human-written text as a prompt/seed
39	- Depth 2: Text generated by an LLM given depth-1 text as input
40	- Depth 3: Text generated by an LLM given depth-2 text as input
41	
42	Key patterns by depth:
43	- Depth 0 (human): Rich vocabulary, domain-specific terminology, natural topic shifts, occasional typos/informal phrasing
44	- Depth 1 (first-gen): Fluent but slightly generic, may have formulaic transitions, maintains topic coherence
45	- Depth 2 (second-gen): More repetitive phrasing, narrower vocabulary, increasingly generic content, possible topic drift
46	- Depth 3 (third-gen): Noticeable repetition, formulaic structure, may contain subtle incoherence or circular reasoning, very generic language"""
47	
48	USER_PROMPT_TEMPLATE = """Analyze the following text and estimate its recursive generation depth (0, 1, 2, or 3).
49	
50	TEXT:
51	{text}
52	
53	Respond with ONLY a JSON object in this exact format:
54	{{"depth": &lt;integer 0-3>, "confidence": &lt;float 0-1>, "reasoning": "&lt;brief one-sentence explanation>"}}"""
55	
56	
57	def truncate_text(text, max_tokens=512):
58	    words = text.split()
59	    approx_tokens = int(max_tokens * 0.75)
60	    if len(words) > approx_tokens:
61	        words = words[:approx_tokens]
62	    return " ".join(words)
63	
64	
65	def parse_llm_response(response_text):
66	    """Extract depth prediction from LLM response."""
67	    json_match = re.search(r'\{[^{}]*"depth"\s*:\s*(\d)[^{}]*\}', response_text)
68	    if json_match:
69	        try:
70	            obj = json.loads(json_match.group(0))
71	            depth = int(obj.get("depth", -1))
72	            confidence = float(obj.get("confidence", 0.5))
73	            if 0 <= depth <= 3:
74	                return depth, confidence
75	        except (json.JSONDecodeError, ValueError):
76	            pass
77	
78	    digit_match = re.search(r'\b([0-3])\b', response_text)
79	    if digit_match:
80	        return int(digit_match.group(1)), 0.5
81	
82	    return 0, 0.0
83	
84	
85	def call_claude(text, model, max_tokens=256):
86	    import anthropic
87	    client = anthropic.Anthropic()
88	    message = client.messages.create(
89	        model=model,
90	        max_tokens=max_tokens,
91	        system=SYSTEM_PROMPT,
92	        messages=[{"role": "user", "content": USER_PROMPT_TEMPLATE.format(text=text)}],
93	    )
94	    return message.content[0].text
95	
96	
97	def call_openai(text, model, max_tokens=256):
98	    import openai
99	    client = openai.OpenAI()
100	    response = client.chat.completions.create(
101	        model=model,
102	        max_tokens=max_tokens,
103	        messages=[
104	            {"role": "system", "content": SYSTEM_PROMPT},
105	            {"role": "user", "content": USER_PROMPT_TEMPLATE.format(text=text)},
106	        ],
107	    )
108	    return response.choices[0].message.content
109	
110	
111	def main():
112	    parser = argparse.ArgumentParser(description="Zero-shot LLM Prompting baseline")
113	    add_common_args(parser)
114	    parser.add_argument("--provider", choices=["claude", "openai"], default="claude")
115	    parser.add_argument("--model", default=None,
116	                        help="Model name (default: claude-sonnet-4-20250514 / gpt-4o)")
117	    parser.add_argument("--max_eval_samples", type=int, default=200,
118	                        help="Max samples to evaluate (API cost control)")
119	    parser.add_argument("--rate_limit_delay", type=float, default=0.5,
120	                        help="Seconds between API calls")
121	    args = parser.parse_args()
122	
123	    if args.model is None:
124	        args.model = "claude-sonnet-4-20250514" if args.provider == "claude" else "gpt-4o"
125	
126	    texts, labels = load_jsonl_data(args.data_dirs, max_samples=args.max_samples, seed=args.seed)
127	
128	    _, eval_idx = stratified_split(labels, eval_split=args.eval_split, seed=args.seed)
129	    eval_texts = [texts[i] for i in eval_idx]
130	    eval_labels = labels[eval_idx]
131	
132	    if len(eval_texts) > args.max_eval_samples:
133	        rng = np.random.RandomState(args.seed)
134	        sample_idx = sorted(rng.choice(len(eval_texts), args.max_eval_samples, replace=False))
135	        eval_texts = [eval_texts[i] for i in sample_idx]
136	        eval_labels = eval_labels[sample_idx]
137	
138	    print(f"Evaluating {len(eval_texts)} samples with {args.provider}/{args.model}")
139	    print(f"Label distribution: {dict(Counter(eval_labels))}")
140	
141	    call_fn = call_claude if args.provider == "claude" else call_openai
142	    y_preds, y_probs = [], []
143	    errors = 0
144	
145	    for i, (text, label) in enumerate(zip(eval_texts, eval_labels)):
146	        truncated = truncate_text(text, max_tokens=args.max_seq_len)
147	        try:
148	            response = call_fn(truncated, args.model)
149	            depth, confidence = parse_llm_response(response)
150	            y_preds.append(depth)
151	            prob = np.zeros(NUM_DEPTHS)
152	            prob[depth] = confidence
153	            remaining = (1.0 - confidence) / max(NUM_DEPTHS - 1, 1)
154	            for d in range(NUM_DEPTHS):
155	                if d != depth:
156	                    prob[d] = remaining
157	            y_probs.append(prob)
158	        except Exception as e:
159	            print(f"  [{i}] API error: {e}")
160	            y_preds.append(0)
161	            y_probs.append(np.ones(NUM_DEPTHS) / NUM_DEPTHS)
162	            errors += 1
163	
164	        if (i + 1) % 20 == 0:
165	            print(f"  Progress: {i+1}/{len(eval_texts)}")
166	
167	        if args.rate_limit_delay > 0:
168	            time.sleep(args.rate_limit_delay)
169	
170	    y_preds = np.array(y_preds)
171	    y_probs = np.array(y_probs)
172	
173	    if errors > 0:
174	        print(f"\n{errors}/{len(eval_texts)} API errors encountered.")
175	
176	    method_name = f"zeroshot_{args.provider}_{args.model.replace('/', '_')}"
177	    evaluate_and_save(method_name, eval_labels, y_preds, y_probs, args.output_dir)
178	
179	
180	if __name__ == "__main__":
181	    main()
182	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "f04ffd09-bc11-4e6b-8f0b-51d30359c933",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/baseline_zeroshot_llm.py",
      "content": "\"\"\"\nBaseline 5: Zero-shot LLM Prompting for recursive generation depth estimation.\n\nUses an LLM (Claude or OpenAI GPT) to directly judge the recursion depth of a\ntext passage. No training required — pure in-context prompting.\n\nThe prompt explains the concept of recursive text generation and asks the LLM to\nclassify the text into depth 0 (human-written), 1, 2, or 3 (each successive depth\nis generated by an LLM conditioned on the previous depth's output).\n\nSupports: --provider claude (Anthropic API) or --provider openai (OpenAI API)\n\nInput:  Raw depth_*.jsonl files (--data_dirs)\nOutput: {method}_classification_report.json, {method}_pairwise_auc.json, {method}_predictions.json\n\nUsage:\n  python baseline_zeroshot_llm.py --data_dirs data/ --provider claude --max_samples 200\n  python baseline_zeroshot_llm.py --data_dirs data/ --provider openai --model gpt-4o\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport re\nimport time\nimport numpy as np\nfrom collections import Counter\n\nfrom baseline_utils import (\n    load_jsonl_data, stratified_split, evaluate_and_save,\n    add_common_args, NUM_DEPTHS,\n)\n\nSYSTEM_PROMPT = \"\"\"You are an expert at detecting AI-generated text and estimating its generation depth.\n\n\"Recursive generation depth\" refers to how many times a text has been through an LLM generation cycle:\n- Depth 0: Original human-written text (e.g., Wikipedia, StackExchange, academic papers)\n- Depth 1: Text generated by an LLM given human-written text as a prompt/seed\n- Depth 2: Text generated by an LLM given depth-1 text as input\n- Depth 3: Text generated by an LLM given depth-2 text as input\n\nKey patterns by depth:\n- Depth 0 (human): Rich vocabulary, domain-specific terminology, natural topic shifts, occasional typos/informal phrasing\n- Depth 1 (first-gen): Fluent but slightly generic, may have formulaic transitions, maintains topic coherence\n- Depth 2 (second-gen): More repetitive phrasing, narrower vocabulary, increasingly generic content, possible topic drift\n- Depth 3 (third-gen): Noticeable repetition, formulaic structure, may contain subtle incoherence or circular reasoning, very generic language\"\"\"\n\nUSER_PROMPT_TEMPLATE = \"\"\"Analyze the following text and estimate its recursive generation depth (0, 1, 2, or 3).\n\nTEXT:\n{text}\n\nRespond with ONLY a JSON object in this exact format:\n{{\"depth\": &lt;integer 0-3>, \"confidence\": &lt;float 0-1>, \"reasoning\": \"&lt;brief one-sentence explanation>\"}}\"\"\"\n\n\ndef truncate_text(text, max_tokens=512):\n    words = text.split()\n    approx_tokens = int(max_tokens * 0.75)\n    if len(words) > approx_tokens:\n        words = words[:approx_tokens]\n    return \" \".join(words)\n\n\ndef parse_llm_response(response_text):\n    \"\"\"Extract depth prediction from LLM response.\"\"\"\n    json_match = re.search(r'\\{[^{}]*\"depth\"\\s*:\\s*(\\d)[^{}]*\\}', response_text)\n    if json_match:\n        try:\n            obj = json.loads(json_match.group(0))\n            depth = int(obj.get(\"depth\", -1))\n            confidence = float(obj.get(\"confidence\", 0.5))\n            if 0 <= depth <= 3:\n                return depth, confidence\n        except (json.JSONDecodeError, ValueError):\n            pass\n\n    digit_match = re.search(r'\\b([0-3])\\b', response_text)\n    if digit_match:\n        return int(digit_match.group(1)), 0.5\n\n    return 0, 0.0\n\n\ndef call_claude(text, model, max_tokens=256):\n    import anthropic\n    client = anthropic.Anthropic()\n    message = client.messages.create(\n        model=model,\n        max_tokens=max_tokens,\n        system=SYSTEM_PROMPT,\n        messages=[{\"role\": \"user\", \"content\": USER_PROMPT_TEMPLATE.format(text=text)}],\n    )\n    return message.content[0].text\n\n\ndef call_openai(text, model, max_tokens=256):\n    import openai\n    client = openai.OpenAI()\n    response = client.chat.completions.create(\n        model=model,\n        max_tokens=max_tokens,\n        messages=[\n            {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n            {\"role\": \"user\", \"content\": USER_PROMPT_TEMPLATE.format(text=text)},\n        ],\n    )\n    return response.choices[0].message.content\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Zero-shot LLM Prompting baseline\")\n    add_common_args(parser)\n    parser.add_argument(\"--provider\", choices=[\"claude\", \"openai\"], default=\"claude\")\n    parser.add_argument(\"--model\", default=None,\n                        help=\"Model name (default: claude-sonnet-4-20250514 / gpt-4o)\")\n    parser.add_argument(\"--max_eval_samples\", type=int, default=200,\n                        help=\"Max samples to evaluate (API cost control)\")\n    parser.add_argument(\"--rate_limit_delay\", type=float, default=0.5,\n                        help=\"Seconds between API calls\")\n    args = parser.parse_args()\n\n    if args.model is None:\n        args.model = \"claude-sonnet-4-20250514\" if args.provider == \"claude\" else \"gpt-4o\"\n\n    texts, labels = load_jsonl_data(args.data_dirs, max_samples=args.max_samples, seed=args.seed)\n\n    _, eval_idx = stratified_split(labels, eval_split=args.eval_split, seed=args.seed)\n    eval_texts = [texts[i] for i in eval_idx]\n    eval_labels = labels[eval_idx]\n\n    if len(eval_texts) > args.max_eval_samples:\n        rng = np.random.RandomState(args.seed)\n        sample_idx = sorted(rng.choice(len(eval_texts), args.max_eval_samples, replace=False))\n        eval_texts = [eval_texts[i] for i in sample_idx]\n        eval_labels = eval_labels[sample_idx]\n\n    print(f\"Evaluating {len(eval_texts)} samples with {args.provider}/{args.model}\")\n    print(f\"Label distribution: {dict(Counter(eval_labels))}\")\n\n    call_fn = call_claude if args.provider == \"claude\" else call_openai\n    y_preds, y_probs = [], []\n    errors = 0\n\n    for i, (text, label) in enumerate(zip(eval_texts, eval_labels)):\n        truncated = truncate_text(text, max_tokens=args.max_seq_len)\n        try:\n            response = call_fn(truncated, args.model)\n            depth, confidence = parse_llm_response(response)\n            y_preds.append(depth)\n            prob = np.zeros(NUM_DEPTHS)\n            prob[depth] = confidence\n            remaining = (1.0 - confidence) / max(NUM_DEPTHS - 1, 1)\n            for d in range(NUM_DEPTHS):\n                if d != depth:\n                    prob[d] = remaining\n            y_probs.append(prob)\n        except Exception as e:\n            print(f\"  [{i}] API error: {e}\")\n            y_preds.append(0)\n            y_probs.append(np.ones(NUM_DEPTHS) / NUM_DEPTHS)\n            errors += 1\n\n        if (i + 1) % 20 == 0:\n            print(f\"  Progress: {i+1}/{len(eval_texts)}\")\n\n        if args.rate_limit_delay > 0:\n            time.sleep(args.rate_limit_delay)\n\n    y_preds = np.array(y_preds)\n    y_probs = np.array(y_probs)\n\n    if errors > 0:\n        print(f\"\\n{errors}/{len(eval_texts)} API errors encountered.\")\n\n    method_name = f\"zeroshot_{args.provider}_{args.model.replace('/', '_')}\"\n    evaluate_and_save(method_name, eval_labels, y_preds, y_probs, args.output_dir)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 182,
      "startLine": 1,
      "totalLines": 182
    }
  }
}
```

</details>

---


### Tool call

_source line 105_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01ABY8Sik25LoQDuBiC6vFo3`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__save_project_file",
  "max_results": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "c217d553-2ba9-4534-ad3a-b0b1dd78d131",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ToZEZvHumAKaeYQow84muo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10089,
      "cache_read_input_tokens": 41838,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10089
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

_source line 106 · 2026-05-14T23:02:32.054Z_

<details><summary>↩ Tool result · `toolu_01ABY8Sik25LoQDuBiC6vFo3`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__detect_image"
}
```

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
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "f0a61dd7-0cdf-4fd5-bf53-2704bdcf2bb6",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 26
  }
}
```

</details>

---


### Assistant

_source line 107_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture of the existing code. Let me summarize what exists:

1. **`artifacts/baselines.py`** - A unified baseline battery with 4 methods (PPL Regression, CE MLP, CORAL, DivEye) all using 19-dim features. This is feature-based only.
2. **`scripts/baseline_ppl_regression.py`** - Standalone PPL regression (Ridge + Ordinal Logistic)
3. **`scripts/baseline_coral.py`** - Standalone CORAL with DeBERTa backbone (text-based)


4. **`scripts/baseline_ce_classification.py`** - Standalone CE with DeBERTa backbone (text-based)
5. **`scripts/baseline_diveye_ordinal.py`** - Standalone DivEye with OVR classifier (feature-based)
6. **`scripts/baseline_zeroshot_llm.py`** - Zero-shot LLM prompting (text-based)
7. **`scripts/baseline_utils.py`** - Shared utilities

So the unified baseline in `artifacts/baselines.py` is already fairly complete, though it looks like the task is asking me to write or refactor `src/baselines.py` instead.

Looking at what's actually implemented, I can see that most of the required baselines are covered across both locations—perplexity regression, CORAL, CE, and DivEye all exist in some form, with feature-based versions in artifacts and text-based DeBERTa versions in scripts. The zero-shot LLM approach is only in the scripts directory so far, so I'd need to check if that needs to be integrated into the main baseline module.

The task specifies using `src/baselines.py` with a `--data_path` argument, but the current setup splits things between `artifacts/` and `scripts/` directories with different parameter naming conventions. I should verify what's actually on the remote server and whether the `src/` directory structure exists there, since the task description references a specific command format that doesn't match the current codebase organization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "537e17bd-27e3-450f-8f1f-a0c93c3f4c6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YVbQ3odot1cU9BPUicccf2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3881,
      "cache_read_input_tokens": 51927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3881
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

_source line 108_

The baseline code is largely complete across `artifacts/baselines.py` and `scripts/baseline_*.py`. The unified `artifacts/baselines.py` is missing the Zero-shot LLM method. Let me check the remote server state and then sync everything into `src/baselines.py`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "b336a050-2355-4577-98ed-0428c1983be4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YVbQ3odot1cU9BPUicccf2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3881,
      "cache_read_input_tokens": 51927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3881
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

_source line 109_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__detect_image · `toolu_01Qv7eZha1Wgd3gKQQ4uaEvE`</summary>

```json
{
  "server": "gpu-6000pro-2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "87e6e346-61c5-47c9-9c9b-eddbface86fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YVbQ3odot1cU9BPUicccf2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3881,
      "cache_read_input_tokens": 51927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3881
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

_source line 110 · 2026-05-14T23:02:56.759Z_

<details><summary>↩ Tool result · `toolu_01Qv7eZha1Wgd3gKQQ4uaEvE`</summary>

```text
{"result":"{\n  \"detected\": false,\n  \"status\": \"unknown\",\n  \"skip_base_setup\": false,\n  \"message\": \"No image marker file found. Use traditional env-setup flow.\"\n}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "16bfdb2c-4ac7-45e5-b6a5-0311694559ff",
  "tool_use_result": {
    "content": "{\"result\":\"{\\n  \\\"detected\\\": false,\\n  \\\"status\\\": \\\"unknown\\\",\\n  \\\"skip_base_setup\\\": false,\\n  \\\"message\\\": \\\"No image marker file found. Use traditional env-setup flow.\\\"\\n}\"}",
    "structuredContent": {
      "result": "{\n  \"detected\": false,\n  \"status\": \"unknown\",\n  \"skip_base_setup\": false,\n  \"message\": \"No image marker file found. Use traditional env-setup flow.\"\n}"
    }
  }
}
```

</details>

---


### Tool call

_source line 111_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01QN8Gar7oidXxcxmL1fyAfG`</summary>

```json
{
  "server": "gpu-6000pro-2",
  "command": "ls -la /root/autodl-tmp/recursive_gen_depth_est/src/ 2>/dev/null; echo \"---\"; ls -la /root/autodl-tmp/recursive_gen_depth_est/data/features_all.jsonl 2>/dev/null; echo \"---\"; ls /root/autodl-tmp/recursive_gen_depth_est/scripts/ 2>/dev/null; echo \"---\"; head -2 /root/autodl-tmp/recursive_gen_depth_est/data/features_all.jsonl 2>/dev/null; echo \"---\"; wc -l /root/autodl-tmp/recursive_gen_depth_est/data/features_all.jsonl 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "2c60dc05-9714-40fd-938e-a0ae54d44925",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JPj8zBKVQjHhVghU5HHqQJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1031,
      "cache_read_input_tokens": 55808,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1031
      },
      "output_tokens": 54,
      "service_tier": "standard",
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

_source line 112 · 2026-05-14T23:03:00.738Z_

<details><summary>↩ Tool result · `toolu_01QN8Gar7oidXxcxmL1fyAfG`</summary>

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
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "5052c411-a645-41f0-a3e9-f2b9b912b0be",
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

_source line 113_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BTkvjN6Sa2vKsX752K9E4W`</summary>

```json
{
  "server": "gpu-6000pro-2",
  "command": "ls -la /root/autodl-tmp/recursive_gen_depth_est/src/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "0e6fb5b0-bf69-4109-bdf0-0a097a329356",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014h2aFWzSuujbK3eS6ffC3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 352,
      "cache_read_input_tokens": 56839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 352
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

_source line 114 · 2026-05-14T23:03:04.057Z_

<details><summary>↩ Tool result · `toolu_01BTkvjN6Sa2vKsX752K9E4W`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 148\\ndrwxr-xr-x  3 root root  4096 May 15 03:57 .\\ndrwxr-xr-x 11 root root   188 May 15 06:26 ..\\n-rw-r--r--  1 root root     0 May 15 00:10 __init__.py\\ndrwxr-xr-x  2 root root  4096 May 15 00:29 __pycache__\\n-rw-r--r--  1 root root 19548 May 15 00:12 atlas_analysis.py\\n-rw-r--r--  1 root root  9696 May 15 00:09 atlas_plots.py\\n-rw-r--r--  1 root root 30204 May 15 01:22 baselines.py\\n-rw-r--r--  1 root root  8455 May 15 00:24 dcol_dataset.py\\n-rw-r--r--  1 root root 10165 May 15 00:18 dcol_eval.py\\n-rw-r--r--  1 root root 25918 May 15 00:32 dcol_feature_mlp.py\\n-rw-r--r--  1 root root 20847 May 15 06:38 dcol_trainer.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.75}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "d7d3f6ca-25eb-424a-9e16-34e708dafc50",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 148\\\\ndrwxr-xr-x  3 root root  4096 May 15 03:57 .\\\\ndrwxr-xr-x 11 root root   188 May 15 06:26 ..\\\\n-rw-r--r--  1 root root     0 May 15 00:10 __init__.py\\\\ndrwxr-xr-x  2 root root  4096 May 15 00:29 __pycache__\\\\n-rw-r--r--  1 root root 19548 May 15 00:12 atlas_analysis.py\\\\n-rw-r--r--  1 root root  9696 May 15 00:09 atlas_plots.py\\\\n-rw-r--r--  1 root root 30204 May 15 01:22 baselines.py\\\\n-rw-r--r--  1 root root  8455 May 15 00:24 dcol_dataset.py\\\\n-rw-r--r--  1 root root 10165 May 15 00:18 dcol_eval.py\\\\n-rw-r--r--  1 root root 25918 May 15 00:32 dcol_feature_mlp.py\\\\n-rw-r--r--  1 root root 20847 May 15 06:38 dcol_trainer.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.75}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 148\\ndrwxr-xr-x  3 root root  4096 May 15 03:57 .\\ndrwxr-xr-x 11 root root   188 May 15 06:26 ..\\n-rw-r--r--  1 root root     0 May 15 00:10 __init__.py\\ndrwxr-xr-x  2 root root  4096 May 15 00:29 __pycache__\\n-rw-r--r--  1 root root 19548 May 15 00:12 atlas_analysis.py\\n-rw-r--r--  1 root root  9696 May 15 00:09 atlas_plots.py\\n-rw-r--r--  1 root root 30204 May 15 01:22 baselines.py\\n-rw-r--r--  1 root root  8455 May 15 00:24 dcol_dataset.py\\n-rw-r--r--  1 root root 10165 May 15 00:18 dcol_eval.py\\n-rw-r--r--  1 root root 25918 May 15 00:32 dcol_feature_mlp.py\\n-rw-r--r--  1 root root 20847 May 15 06:38 dcol_trainer.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.75}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 115_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PVENbwcfrQE7Q9RjzCo5yb`</summary>

```json
{
  "server": "gpu-6000pro-2",
  "command": "ls -la /root/autodl-tmp/recursive_gen_depth_est/data/features_all.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "29ee5c79-c515-4ca9-9b8f-dde2d00eff72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014h2aFWzSuujbK3eS6ffC3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 352,
      "cache_read_input_tokens": 56839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 352
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


### Tool call

_source line 116_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MZQxmaywXNxHfr671sbUjQ`</summary>

```json
{
  "server": "gpu-6000pro-2",
  "command": "ls /root/autodl-tmp/recursive_gen_depth_est/scripts/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "9187f4f4-ccc7-4dfe-982e-1b90c58477c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014h2aFWzSuujbK3eS6ffC3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 352,
      "cache_read_input_tokens": 56839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 352
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

_source line 117 · 2026-05-14T23:03:04.964Z_

<details><summary>↩ Tool result · `toolu_01PVENbwcfrQE7Q9RjzCo5yb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 13702118 May 14 21:58 /root/autodl-tmp/recursive_gen_depth_est/data/features_all.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.79}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "ab0eacbf-48b1-4341-99f7-7a2b7dc6133b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"-rw-r--r-- 1 root root 13702118 May 14 21:58 /root/autodl-tmp/recursive_gen_depth_est/data/features_all.jsonl\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.79}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 13702118 May 14 21:58 /root/autodl-tmp/recursive_gen_depth_est/data/features_all.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.79}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 118 · 2026-05-14T23:03:05.892Z_

<details><summary>↩ Tool result · `toolu_01MZQxmaywXNxHfr671sbUjQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\nadd_seed_id.py\\natlas_analysis.py\\nbaseline_ce_classification.py\\nbaseline_coral.py\\nbaseline_diveye_ordinal.py\\nbaseline_ppl_regression.py\\nbaseline_utils.py\\nbaseline_zeroshot_llm.py\\ndcol_train_standalone_deprecated.py\\neval_d1d3.py\\nextract_features.py\\nfilter_code.py\\nfilter_features_d1d3.py\\ngenerate_next_depth.py\\nlora_finetune.py\\nprepare_seed_data.py\\nrun_atlas_analysis.sh\\nrun_dcol_training.sh\\nrun_eval_gpt2xl_temp09.sh\\nrun_eval_pythia_topk50.sh\\nrun_evaluation.sh\\nrun_pipeline.sh\\nrun_pipeline_base.sh\\nrun_pipeline_gpt2xl.sh\\nrun_pipeline_gpt2xl_temp09.sh\\nrun_pipeline_gpt2xl_topk50.sh\\nrun_pipeline_olmo.sh\\nrun_pipeline_olmo_temp09.sh\\nrun_pipeline_olmo_temp09_resume.sh\\nrun_pipeline_olmo_topk50.sh\\nrun_pipeline_pythia_temp09.sh\\nrun_pipeline_pythia_topk50.sh\\nrun_three_class_eval.py\\ntrain_classifier.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "e96bab8d-673a-47d6-9edc-7601c36a424b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"__pycache__\\\\nadd_seed_id.py\\\\natlas_analysis.py\\\\nbaseline_ce_classification.py\\\\nbaseline_coral.py\\\\nbaseline_diveye_ordinal.py\\\\nbaseline_ppl_regression.py\\\\nbaseline_utils.py\\\\nbaseline_zeroshot_llm.py\\\\ndcol_train_standalone_deprecated.py\\\\neval_d1d3.py\\\\nextract_features.py\\\\nfilter_code.py\\\\nfilter_features_d1d3.py\\\\ngenerate_next_depth.py\\\\nlora_finetune.py\\\\nprepare_seed_data.py\\\\nrun_atlas_analysis.sh\\\\nrun_dcol_training.sh\\\\nrun_eval_gpt2xl_temp09.sh\\\\nrun_eval_pythia_topk50.sh\\\\nrun_evaluation.sh\\\\nrun_pipeline.sh\\\\nrun_pipeline_base.sh\\\\nrun_pipeline_gpt2xl.sh\\\\nrun_pipeline_gpt2xl_temp09.sh\\\\nrun_pipeline_gpt2xl_topk50.sh\\\\nrun_pipeline_olmo.sh\\\\nrun_pipeline_olmo_temp09.sh\\\\nrun_pipeline_olmo_temp09_resume.sh\\\\nrun_pipeline_olmo_topk50.sh\\\\nrun_pipeline_pythia_temp09.sh\\\\nrun_pipeline_pythia_topk50.sh\\\\nrun_three_class_eval.py\\\\ntrain_classifier.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.91}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\nadd_seed_id.py\\natlas_analysis.py\\nbaseline_ce_classification.py\\nbaseline_coral.py\\nbaseline_diveye_ordinal.py\\nbaseline_ppl_regression.py\\nbaseline_utils.py\\nbaseline_zeroshot_llm.py\\ndcol_train_standalone_deprecated.py\\neval_d1d3.py\\nextract_features.py\\nfilter_code.py\\nfilter_features_d1d3.py\\ngenerate_next_depth.py\\nlora_finetune.py\\nprepare_seed_data.py\\nrun_atlas_analysis.sh\\nrun_dcol_training.sh\\nrun_eval_gpt2xl_temp09.sh\\nrun_eval_pythia_topk50.sh\\nrun_evaluation.sh\\nrun_pipeline.sh\\nrun_pipeline_base.sh\\nrun_pipeline_gpt2xl.sh\\nrun_pipeline_gpt2xl_temp09.sh\\nrun_pipeline_gpt2xl_topk50.sh\\nrun_pipeline_olmo.sh\\nrun_pipeline_olmo_temp09.sh\\nrun_pipeline_olmo_temp09_resume.sh\\nrun_pipeline_olmo_topk50.sh\\nrun_pipeline_pythia_temp09.sh\\nrun_pipeline_pythia_topk50.sh\\nrun_three_class_eval.py\\ntrain_classifier.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 119_

<details><summary>Logged reasoning block</summary>

```text
So the remote server already has `src/baselines.py` (30KB) and all the `scripts/baseline_*.py` files. Let me check what the current `src/baselines.py` on the server looks like.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "533c4e1f-ba08-4ca0-96cf-91e20eb0db38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PPFrSxg2N3uK1iTXkryqWD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1378,
      "cache_read_input_tokens": 57191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1378
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

_source line 120_

The server already has `src/baselines.py` (30KB) and `data/features_all.jsonl` (13MB). Let me check the current server version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "2b5922e7-1487-4839-8e5f-5828808165ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PPFrSxg2N3uK1iTXkryqWD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1378,
      "cache_read_input_tokens": 57191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1378
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

_source line 121_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LBQW6hCv25fQB1xk74JpwU`</summary>

```json
{
  "server": "gpu-6000pro-2",
  "command": "head -50 /root/autodl-tmp/recursive_gen_depth_est/src/baselines.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "89057fa5-1aa7-49a2-8da0-0ddb936a82d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PPFrSxg2N3uK1iTXkryqWD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1378,
      "cache_read_input_tokens": 57191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1378
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

_source line 122_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01JNuoBat56akkN7KxkKQfth`</summary>

```json
{
  "server": "gpu-6000pro-2",
  "command": "wc -l /root/autodl-tmp/recursive_gen_depth_est/src/baselines.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "7374694a-af0c-4db9-9dbb-5efb2f2c0aeb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PPFrSxg2N3uK1iTXkryqWD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1378,
      "cache_read_input_tokens": 57191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1378
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

_source line 123 · 2026-05-14T23:03:11.755Z_

<details><summary>↩ Tool result · `toolu_01LBQW6hCv25fQB1xk74JpwU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nBaseline battery for recursive generation depth estimation.\\n\\nBaselines:\\n  1. PPLRegressionBaseline  — OLS regression on mean_ppl (single) or all 19 features (multi)\\n  2. CEClassificationBaseline — MLP with cross-entropy loss (DCOL ablation, no contrastive loss)\\n  3. CORALBaseline — Ordinal regression with K-1 binary classifiers (Cao et al., 2020)\\n  4. DivEyeBaseline — Surprisal diversity features + XGBoost (Basani & Chen, TMLR 2026)\\n\\nUsage:\\n  python src/baselines.py --method ppl_reg --features_path data/features_all.jsonl\\n  python src/baselines.py --method ce_mlp  --features_path data/features_all.jsonl --epochs 50\\n  python src/baselines.py --method coral   --features_path data/features_all.jsonl --epochs 50\\n  python src/baselines.py --method diveye  --features_path data/features_all.jsonl\\n  python src/baselines.py --method all     --features_path data/features_all.jsonl --epochs 50\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nimport numpy as np\\nfrom collections import Counter\\n\\nimport torch\\nimport torch.nn as nn\\nimport torch.optim as optim\\nfrom torch.utils.data import DataLoader, TensorDataset\\n\\nfrom sklearn.linear_model import LinearRegression\\nfrom sklearn.preprocessing import StandardScaler\\nfrom sklearn.model_selection import train_test_split\\nfrom sklearn.metrics import (\\n    accuracy_score, confusion_matrix, classification_report, roc_auc_score,\\n)\\n\\n# ── Feature schema (must match extract_features.py / dcol_dataset.py) ──\\n\\nFEATURE_NAMES = [\\n    \\\"mean_ppl\\\", \\\"var_ppl\\\", \\\"skewness_ppl\\\", \\\"kurtosis_ppl\\\",\\n    \\\"p10_ppl\\\", \\\"p25_ppl\\\", \\\"p50_ppl\\\", \\\"p75_ppl\\\", \\\"p90_ppl\\\",\\n    \\\"mean_surprisal\\\", \\\"var_surprisal\\\", \\\"entropy_of_surprisal\\\",\\n    \\\"type_token_ratio\\\", \\\"hapax_ratio\\\", \\\"bigram_entropy\\\", \\\"trigram_entropy\\\",\\n    \\\"rep_2gram\\\", \\\"rep_3gram\\\", \\\"rep_4gram\\\",\\n]\\nNUM_FEATURES = len(FEATURE_NAMES)\\nNUM_DEPTHS = 4\\nDEPTH_LABELS = list(range(NUM_DEPTHS))\\n\\n# ── Data loading ──\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.75}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "6ae6485c-62f4-450e-bb19-8beea303ed0b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nBaseline battery for recursive generation depth estimation.\\\\n\\\\nBaselines:\\\\n  1. PPLRegressionBaseline  — OLS regression on mean_ppl (single) or all 19 features (multi)\\\\n  2. CEClassificationBaseline — MLP with cross-entropy loss (DCOL ablation, no contrastive loss)\\\\n  3. CORALBaseline — Ordinal regression with K-1 binary classifiers (Cao et al., 2020)\\\\n  4. DivEyeBaseline — Surprisal diversity features + XGBoost (Basani & Chen, TMLR 2026)\\\\n\\\\nUsage:\\\\n  python src/baselines.py --method ppl_reg --features_path data/features_all.jsonl\\\\n  python src/baselines.py --method ce_mlp  --features_path data/features_all.jsonl --epochs 50\\\\n  python src/baselines.py --method coral   --features_path data/features_all.jsonl --epochs 50\\\\n  python src/baselines.py --method diveye  --features_path data/features_all.jsonl\\\\n  python src/baselines.py --method all     --features_path data/features_all.jsonl --epochs 50\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport os\\\\nimport sys\\\\nimport numpy as np\\\\nfrom collections import Counter\\\\n\\\\nimport torch\\\\nimport torch.nn as nn\\\\nimport torch.optim as optim\\\\nfrom torch.utils.data import DataLoader, TensorDataset\\\\n\\\\nfrom sklearn.linear_model import LinearRegression\\\\nfrom sklearn.preprocessing import StandardScaler\\\\nfrom sklearn.model_selection import train_test_split\\\\nfrom sklearn.metrics import (\\\\n    accuracy_score, confusion_matrix, classification_report, roc_auc_score,\\\\n)\\\\n\\\\n# ── Feature schema (must match extract_features.py / dcol_dataset.py) ──\\\\n\\\\nFEATURE_NAMES = [\\\\n    \\\\\\\"mean_ppl\\\\\\\", \\\\\\\"var_ppl\\\\\\\", \\\\\\\"skewness_ppl\\\\\\\", \\\\\\\"kurtosis_ppl\\\\\\\",\\\\n    \\\\\\\"p10_ppl\\\\\\\", \\\\\\\"p25_ppl\\\\\\\", \\\\\\\"p50_ppl\\\\\\\", \\\\\\\"p75_ppl\\\\\\\", \\\\\\\"p90_ppl\\\\\\\",\\\\n    \\\\\\\"mean_surprisal\\\\\\\", \\\\\\\"var_surprisal\\\\\\\", \\\\\\\"entropy_of_surprisal\\\\\\\",\\\\n    \\\\\\\"type_token_ratio\\\\\\\", \\\\\\\"hapax_ratio\\\\\\\", \\\\\\\"bigram_entropy\\\\\\\", \\\\\\\"trigram_entropy\\\\\\\",\\\\n    \\\\\\\"rep_2gram\\\\\\\", \\\\\\\"rep_3gram\\\\\\\", \\\\\\\"rep_4gram\\\\\\\",\\\\n]\\\\nNUM_FEATURES = len(FEATURE_NAMES)\\\\nNUM_DEPTHS = 4\\\\nDEPTH_LABELS = list(range(NUM_DEPTHS))\\\\n\\\\n# ── Data loading ──\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.75}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nBaseline battery for recursive generation depth estimation.\\n\\nBaselines:\\n  1. PPLRegressionBaseline  — OLS regression on mean_ppl (single) or all 19 features (multi)\\n  2. CEClassificationBaseline — MLP with cross-entropy loss (DCOL ablation, no contrastive loss)\\n  3. CORALBaseline — Ordinal regression with K-1 binary classifiers (Cao et al., 2020)\\n  4. DivEyeBaseline — Surprisal diversity features + XGBoost (Basani & Chen, TMLR 2026)\\n\\nUsage:\\n  python src/baselines.py --method ppl_reg --features_path data/features_all.jsonl\\n  python src/baselines.py --method ce_mlp  --features_path data/features_all.jsonl --epochs 50\\n  python src/baselines.py --method coral   --features_path data/features_all.jsonl --epochs 50\\n  python src/baselines.py --method diveye  --features_path data/features_all.jsonl\\n  python src/baselines.py --method all     --features_path data/features_all.jsonl --epochs 50\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nimport numpy as np\\nfrom collections import Counter\\n\\nimport torch\\nimport torch.nn as nn\\nimport torch.optim as optim\\nfrom torch.utils.data import DataLoader, TensorDataset\\n\\nfrom sklearn.linear_model import LinearRegression\\nfrom sklearn.preprocessing import StandardScaler\\nfrom sklearn.model_selection import train_test_split\\nfrom sklearn.metrics import (\\n    accuracy_score, confusion_matrix, classification_report, roc_auc_score,\\n)\\n\\n# ── Feature schema (must match extract_features.py / dcol_dataset.py) ──\\n\\nFEATURE_NAMES = [\\n    \\\"mean_ppl\\\", \\\"var_ppl\\\", \\\"skewness_ppl\\\", \\\"kurtosis_ppl\\\",\\n    \\\"p10_ppl\\\", \\\"p25_ppl\\\", \\\"p50_ppl\\\", \\\"p75_ppl\\\", \\\"p90_ppl\\\",\\n    \\\"mean_surprisal\\\", \\\"var_surprisal\\\", \\\"entropy_of_surprisal\\\",\\n    \\\"type_token_ratio\\\", \\\"hapax_ratio\\\", \\\"bigram_entropy\\\", \\\"trigram_entropy\\\",\\n    \\\"rep_2gram\\\", \\\"rep_3gram\\\", \\\"rep_4gram\\\",\\n]\\nNUM_FEATURES = len(FEATURE_NAMES)\\nNUM_DEPTHS = 4\\nDEPTH_LABELS = list(range(NUM_DEPTHS))\\n\\n# ── Data loading ──\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.75}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 124_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01FSzaotBCzJoC1gKdyLraFF`</summary>

```json
{
  "server": "gpu-6000pro-2",
  "command": "wc -l /root/autodl-tmp/recursive_gen_depth_est/data/features_all.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "6a4ff467-a555-4920-a545-2ecc904af885",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PPFrSxg2N3uK1iTXkryqWD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1378,
      "cache_read_input_tokens": 57191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1378
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

_source line 125 · 2026-05-14T23:03:12.672Z_

<details><summary>↩ Tool result · `toolu_01JNuoBat56akkN7KxkKQfth`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"772 /root/autodl-tmp/recursive_gen_depth_est/src/baselines.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "ecb35d65-b4fe-4cba-b95c-097b253a67c6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"772 /root/autodl-tmp/recursive_gen_depth_est/src/baselines.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.91}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"772 /root/autodl-tmp/recursive_gen_depth_est/src/baselines.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 126 · 2026-05-14T23:03:13.588Z_

<details><summary>↩ Tool result · `toolu_01FSzaotBCzJoC1gKdyLraFF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"20000 /root/autodl-tmp/recursive_gen_depth_est/data/features_all.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "be0e7305-423b-4be4-a2c9-e7d2ec67a9b3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"20000 /root/autodl-tmp/recursive_gen_depth_est/data/features_all.jsonl\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.91}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"20000 /root/autodl-tmp/recursive_gen_depth_est/data/features_all.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 127_

<details><summary>Logged reasoning block</summary>

```text
The server has:
- `src/baselines.py` — 772 lines, same content as `artifacts/baselines.py` (691 lines locally — the server version might have some additions)
- `data/features_all.jsonl` — 20000 lines
- All the `scripts/baseline_*.py` files

Let me read the full server version to see if it differs from the local one.

Actually, looking at the local `artifacts/baselines.py` which is 691 lines, and the server one which is 772 lines, the server version has ~80 more lines. Let me check what's different — maybe Zero-shot LLM was already added.


I'll scan the server version starting around line 600 to see what those extra lines contain.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "89386eef-d20d-455b-b4c7-9a7d4a680ca5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012PFq6dcH3BuxUCgdWAKKDr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1667,
      "cache_read_input_tokens": 58569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1667
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

_source line 128_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01QXNXeXz6phR4pvwtJUsSY3`</summary>

```json
{
  "server": "gpu-6000pro-2",
  "command": "tail -150 /root/autodl-tmp/recursive_gen_depth_est/src/baselines.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "81f1f42f-1c50-4ddc-92c1-44a80d96ca5d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012PFq6dcH3BuxUCgdWAKKDr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1667,
      "cache_read_input_tokens": 58569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1667
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

_source line 129 · 2026-05-14T23:03:21.350Z_

<details><summary>↩ Tool result · `toolu_01QXNXeXz6phR4pvwtJUsSY3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"            return full\\n        return probs\\n\\n\\n# ═══════════════════════════════════════════════════════════════════════\\n#  Baseline 6: Logistic Regression\\n# ═══════════════════════════════════════════════════════════════════════\\n\\nclass LogisticRegressionBaseline:\\n\\n    def __init__(self, max_iter=1000, seed=42):\\n        self.seed = seed\\n        self.max_iter = max_iter\\n        self.scaler = StandardScaler()\\n        self.model = None\\n\\n    def fit(self, X_train, y_train, **kwargs):\\n        from sklearn.linear_model import LogisticRegression as _LR\\n        X_s = self.scaler.fit_transform(X_train)\\n        self.model = _LR(\\n            max_iter=self.max_iter,\\n            random_state=self.seed,\\n            solver=\\\"lbfgs\\\",\\n        )\\n        self.model.fit(X_s, y_train)\\n\\n    def predict(self, X_test):\\n        X_s = self.scaler.transform(X_test)\\n        return self.model.predict(X_s)\\n\\n    def predict_proba(self, X_test):\\n        X_s = self.scaler.transform(X_test)\\n        probs = self.model.predict_proba(X_s)\\n        if probs.shape[1] < NUM_DEPTHS:\\n            full = np.zeros((probs.shape[0], NUM_DEPTHS))\\n            for i, c in enumerate(self.model.classes_):\\n                full[:, c] = probs[:, i]\\n            return full\\n        return probs\\n\\n\\n# ═══════════════════════════════════════════════════════════════════════\\n#  Unified Runner\\n# ═══════════════════════════════════════════════════════════════════════\\n\\nBASELINE_REGISTRY = {\\n    \\\"ppl_reg_single\\\": (\\\"PPL Regression (single: mean_ppl)\\\", lambda: PPLRegressionBaseline(mode=\\\"single\\\")),\\n    \\\"ppl_reg\\\":        (\\\"PPL Regression (multi: 19-dim OLS)\\\", lambda: PPLRegressionBaseline(mode=\\\"multi\\\")),\\n    \\\"ce_mlp\\\":         (\\\"CE-MLP (DCOL ablation)\\\", None),\\n    \\\"coral\\\":          (\\\"CORAL Ordinal Regression\\\", None),\\n    \\\"diveye\\\":         (\\\"DivEye (XGBoost)\\\", lambda: DivEyeBaseline()),\\n    \\\"rf\\\":             (\\\"Random Forest\\\", lambda: RandomForestBaseline()),\\n    \\\"lr\\\":             (\\\"Logistic Regression\\\", lambda: LogisticRegressionBaseline()),\\n}\\n\\n\\ndef run_baseline(method, X_train, y_train, X_val, y_val, X_test, y_test, args):\\n    if method == \\\"ppl_reg_single\\\":\\n        bl = PPLRegressionBaseline(mode=\\\"single\\\")\\n        bl.fit(X_train, y_train)\\n    elif method == \\\"ppl_reg\\\":\\n        bl = PPLRegressionBaseline(mode=\\\"multi\\\")\\n        bl.fit(X_train, y_train)\\n    elif method == \\\"ce_mlp\\\":\\n        bl = CEClassificationBaseline(\\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\\n            patience=args.patience, seed=args.seed,\\n        )\\n        bl.fit(X_train, y_train, X_val, y_val)\\n    elif method == \\\"coral\\\":\\n        bl = CORALBaseline(\\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\\n            patience=args.patience, seed=args.seed,\\n        )\\n        bl.fit(X_train, y_train, X_val, y_val)\\n    elif method == \\\"diveye\\\":\\n        bl = DivEyeBaseline(seed=args.seed)\\n        bl.fit(X_train, y_train)\\n    elif method == \\\"rf\\\":\\n        bl = RandomForestBaseline(n_estimators=100, seed=args.seed)\\n        bl.fit(X_train, y_train)\\n    elif method == \\\"lr\\\":\\n        bl = LogisticRegressionBaseline(max_iter=1000, seed=args.seed)\\n        bl.fit(X_train, y_train)\\n    else:\\n        print(f\\\"Unknown method: {method}\\\")\\n        return None\\n\\n    y_pred = bl.predict(X_test)\\n    y_prob = bl.predict_proba(X_test)\\n    name = BASELINE_REGISTRY.get(method, (method, None))[0]\\n    return evaluate(name, y_test, y_pred, y_prob)\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"Baseline battery for depth estimation.\\\")\\n    p.add_argument(\\\"--method\\\", default=\\\"all\\\",\\n                   choices=[\\\"ppl_reg_single\\\", \\\"ppl_reg\\\", \\\"ce_mlp\\\", \\\"coral\\\", \\\"diveye\\\", \\\"rf\\\", \\\"lr\\\", \\\"all\\\"])\\n    p.add_argument(\\\"--features_path\\\", default=\\\"data/features_all.jsonl\\\")\\n    p.add_argument(\\\"--output_dir\\\", default=\\\"results/baselines/\\\")\\n    p.add_argument(\\\"--seed\\\", type=int, default=42)\\n    p.add_argument(\\\"--test_size\\\", type=float, default=0.15)\\n    p.add_argument(\\\"--val_size\\\", type=float, default=0.15)\\n    p.add_argument(\\\"--epochs\\\", type=int, default=100)\\n    p.add_argument(\\\"--batch_size\\\", type=int, default=256)\\n    p.add_argument(\\\"--lr\\\", type=float, default=1e-3)\\n    p.add_argument(\\\"--patience\\\", type=int, default=10)\\n    return p.parse_args()\\n\\n\\ndef main():\\n    args = parse_args()\\n    print(f\\\"Loading features from {args.features_path} ...\\\")\\n    X, y = load_features(args.features_path)\\n    print(f\\\"  {X.shape[0]} samples, {X.shape[1]} features\\\")\\n    print(f\\\"  Depth distribution: {dict(Counter(y))}\\\")\\n\\n    X_train, y_train, X_val, y_val, X_test, y_test = prepare_splits(\\n        X, y, test_size=args.test_size, val_size=args.val_size, seed=args.seed\\n    )\\n    print(f\\\"  Train: {len(y_train)}, Val: {len(y_val)}, Test: {len(y_test)}\\\")\\n\\n    methods = list(BASELINE_REGISTRY.keys()) if args.method == \\\"all\\\" else [args.method]\\n    all_results = {}\\n\\n    for m in methods:\\n        result = run_baseline(m, X_train, y_train, X_val, y_val, X_test, y_test, args)\\n        if result is not None:\\n            all_results[m] = result\\n\\n    # Summary table\\n    if len(all_results) > 1:\\n        print(f\\\"\\\\n{'='*60}\\\")\\n        print(f\\\"  SUMMARY\\\")\\n        print(f\\\"{'='*60}\\\")\\n        print(f\\\"  {'Method':<35s} {'4-cls':>6s} {'3-cls':>6s} {'MAE':>6s}\\\")\\n        print(f\\\"  {'-'*35} {'-'*6} {'-'*6} {'-'*6}\\\")\\n        for m, r in all_results.items():\\n            print(f\\\"  {r['method']:<35s} {r['acc_4class']:6.4f} {r['acc_3class']:6.4f} {r['mae']:6.4f}\\\")\\n\\n\\n    os.makedirs(args.output_dir, exist_ok=True)\\n    out_path = os.path.join(args.output_dir, \\\"baseline_results.json\\\")\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(all_results, f, indent=2, default=str)\\n    print(f\\\"\\\\nResults saved to {out_path}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.75}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "1586f1d2-993b-4e9c-b7c9-694dc30379ad",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"            return full\\\\n        return probs\\\\n\\\\n\\\\n# ═══════════════════════════════════════════════════════════════════════\\\\n#  Baseline 6: Logistic Regression\\\\n# ═══════════════════════════════════════════════════════════════════════\\\\n\\\\nclass LogisticRegressionBaseline:\\\\n\\\\n    def __init__(self, max_iter=1000, seed=42):\\\\n        self.seed = seed\\\\n        self.max_iter = max_iter\\\\n        self.scaler = StandardScaler()\\\\n        self.model = None\\\\n\\\\n    def fit(self, X_train, y_train, **kwargs):\\\\n        from sklearn.linear_model import LogisticRegression as _LR\\\\n        X_s = self.scaler.fit_transform(X_train)\\\\n        self.model = _LR(\\\\n            max_iter=self.max_iter,\\\\n            random_state=self.seed,\\\\n            solver=\\\\\\\"lbfgs\\\\\\\",\\\\n        )\\\\n        self.model.fit(X_s, y_train)\\\\n\\\\n    def predict(self, X_test):\\\\n        X_s = self.scaler.transform(X_test)\\\\n        return self.model.predict(X_s)\\\\n\\\\n    def predict_proba(self, X_test):\\\\n        X_s = self.scaler.transform(X_test)\\\\n        probs = self.model.predict_proba(X_s)\\\\n        if probs.shape[1] < NUM_DEPTHS:\\\\n            full = np.zeros((probs.shape[0], NUM_DEPTHS))\\\\n            for i, c in enumerate(self.model.classes_):\\\\n                full[:, c] = probs[:, i]\\\\n            return full\\\\n        return probs\\\\n\\\\n\\\\n# ═══════════════════════════════════════════════════════════════════════\\\\n#  Unified Runner\\\\n# ═══════════════════════════════════════════════════════════════════════\\\\n\\\\nBASELINE_REGISTRY = {\\\\n    \\\\\\\"ppl_reg_single\\\\\\\": (\\\\\\\"PPL Regression (single: mean_ppl)\\\\\\\", lambda: PPLRegressionBaseline(mode=\\\\\\\"single\\\\\\\")),\\\\n    \\\\\\\"ppl_reg\\\\\\\":        (\\\\\\\"PPL Regression (multi: 19-dim OLS)\\\\\\\", lambda: PPLRegressionBaseline(mode=\\\\\\\"multi\\\\\\\")),\\\\n    \\\\\\\"ce_mlp\\\\\\\":         (\\\\\\\"CE-MLP (DCOL ablation)\\\\\\\", None),\\\\n    \\\\\\\"coral\\\\\\\":          (\\\\\\\"CORAL Ordinal Regression\\\\\\\", None),\\\\n    \\\\\\\"diveye\\\\\\\":         (\\\\\\\"DivEye (XGBoost)\\\\\\\", lambda: DivEyeBaseline()),\\\\n    \\\\\\\"rf\\\\\\\":             (\\\\\\\"Random Forest\\\\\\\", lambda: RandomForestBaseline()),\\\\n    \\\\\\\"lr\\\\\\\":             (\\\\\\\"Logistic Regression\\\\\\\", lambda: LogisticRegressionBaseline()),\\\\n}\\\\n\\\\n\\\\ndef run_baseline(method, X_train, y_train, X_val, y_val, X_test, y_test, args):\\\\n    if method == \\\\\\\"ppl_reg_single\\\\\\\":\\\\n        bl = PPLRegressionBaseline(mode=\\\\\\\"single\\\\\\\")\\\\n        bl.fit(X_train, y_train)\\\\n    elif method == \\\\\\\"ppl_reg\\\\\\\":\\\\n        bl = PPLRegressionBaseline(mode=\\\\\\\"multi\\\\\\\")\\\\n        bl.fit(X_train, y_train)\\\\n    elif method == \\\\\\\"ce_mlp\\\\\\\":\\\\n        bl = CEClassificationBaseline(\\\\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\\\\n            patience=args.patience, seed=args.seed,\\\\n        )\\\\n        bl.fit(X_train, y_train, X_val, y_val)\\\\n    elif method == \\\\\\\"coral\\\\\\\":\\\\n        bl = CORALBaseline(\\\\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\\\\n            patience=args.patience, seed=args.seed,\\\\n        )\\\\n        bl.fit(X_train, y_train, X_val, y_val)\\\\n    elif method == \\\\\\\"diveye\\\\\\\":\\\\n        bl = DivEyeBaseline(seed=args.seed)\\\\n        bl.fit(X_train, y_train)\\\\n    elif method == \\\\\\\"rf\\\\\\\":\\\\n        bl = RandomForestBaseline(n_estimators=100, seed=args.seed)\\\\n        bl.fit(X_train, y_train)\\\\n    elif method == \\\\\\\"lr\\\\\\\":\\\\n        bl = LogisticRegressionBaseline(max_iter=1000, seed=args.seed)\\\\n        bl.fit(X_train, y_train)\\\\n    else:\\\\n        print(f\\\\\\\"Unknown method: {method}\\\\\\\")\\\\n        return None\\\\n\\\\n    y_pred = bl.predict(X_test)\\\\n    y_prob = bl.predict_proba(X_test)\\\\n    name = BASELINE_REGISTRY.get(method, (method, None))[0]\\\\n    return evaluate(name, y_test, y_pred, y_prob)\\\\n\\\\n\\\\ndef parse_args():\\\\n    p = argparse.ArgumentParser(description=\\\\\\\"Baseline battery for depth estimation.\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--method\\\\\\\", default=\\\\\\\"all\\\\\\\",\\\\n                   choices=[\\\\\\\"ppl_reg_single\\\\\\\", \\\\\\\"ppl_reg\\\\\\\", \\\\\\\"ce_mlp\\\\\\\", \\\\\\\"coral\\\\\\\", \\\\\\\"diveye\\\\\\\", \\\\\\\"rf\\\\\\\", \\\\\\\"lr\\\\\\\", \\\\\\\"all\\\\\\\"])\\\\n    p.add_argument(\\\\\\\"--features_path\\\\\\\", default=\\\\\\\"data/features_all.jsonl\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--output_dir\\\\\\\", default=\\\\\\\"results/baselines/\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--seed\\\\\\\", type=int, default=42)\\\\n    p.add_argument(\\\\\\\"--test_size\\\\\\\", type=float, default=0.15)\\\\n    p.add_argument(\\\\\\\"--val_size\\\\\\\", type=float, default=0.15)\\\\n    p.add_argument(\\\\\\\"--epochs\\\\\\\", type=int, default=100)\\\\n    p.add_argument(\\\\\\\"--batch_size\\\\\\\", type=int, default=256)\\\\n    p.add_argument(\\\\\\\"--lr\\\\\\\", type=float, default=1e-3)\\\\n    p.add_argument(\\\\\\\"--patience\\\\\\\", type=int, default=10)\\\\n    return p.parse_args()\\\\n\\\\n\\\\ndef main():\\\\n    args = parse_args()\\\\n    print(f\\\\\\\"Loading features from {args.features_path} ...\\\\\\\")\\\\n    X, y = load_features(args.features_path)\\\\n    print(f\\\\\\\"  {X.shape[0]} samples, {X.shape[1]} features\\\\\\\")\\\\n    print(f\\\\\\\"  Depth distribution: {dict(Counter(y))}\\\\\\\")\\\\n\\\\n    X_train, y_train, X_val, y_val, X_test, y_test = prepare_splits(\\\\n        X, y, test_size=args.test_size, val_size=args.val_size, seed=args.seed\\\\n    )\\\\n    print(f\\\\\\\"  Train: {len(y_train)}, Val: {len(y_val)}, Test: {len(y_test)}\\\\\\\")\\\\n\\\\n    methods = list(BASELINE_REGISTRY.keys()) if args.method == \\\\\\\"all\\\\\\\" else [args.method]\\\\n    all_results = {}\\\\n\\\\n    for m in methods:\\\\n        result = run_baseline(m, X_train, y_train, X_val, y_val, X_test, y_test, args)\\\\n        if result is not None:\\\\n            all_results[m] = result\\\\n\\\\n    # Summary table\\\\n    if len(all_results) > 1:\\\\n        print(f\\\\\\\"\\\\\\\\n{'='*60}\\\\\\\")\\\\n        print(f\\\\\\\"  SUMMARY\\\\\\\")\\\\n        print(f\\\\\\\"{'='*60}\\\\\\\")\\\\n        print(f\\\\\\\"  {'Method':<35s} {'4-cls':>6s} {'3-cls':>6s} {'MAE':>6s}\\\\\\\")\\\\n        print(f\\\\\\\"  {'-'*35} {'-'*6} {'-'*6} {'-'*6}\\\\\\\")\\\\n        for m, r in all_results.items():\\\\n            print(f\\\\\\\"  {r['method']:<35s} {r['acc_4class']:6.4f} {r['acc_3class']:6.4f} {r['mae']:6.4f}\\\\\\\")\\\\n\\\\n\\\\n    os.makedirs(args.output_dir, exist_ok=True)\\\\n    out_path = os.path.join(args.output_dir, \\\\\\\"baseline_results.json\\\\\\\")\\\\n    with open(out_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(all_results, f, indent=2, default=str)\\\\n    print(f\\\\\\\"\\\\\\\\nResults saved to {out_path}\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.75}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"            return full\\n        return probs\\n\\n\\n# ═══════════════════════════════════════════════════════════════════════\\n#  Baseline 6: Logistic Regression\\n# ═══════════════════════════════════════════════════════════════════════\\n\\nclass LogisticRegressionBaseline:\\n\\n    def __init__(self, max_iter=1000, seed=42):\\n        self.seed = seed\\n        self.max_iter = max_iter\\n        self.scaler = StandardScaler()\\n        self.model = None\\n\\n    def fit(self, X_train, y_train, **kwargs):\\n        from sklearn.linear_model import LogisticRegression as _LR\\n        X_s = self.scaler.fit_transform(X_train)\\n        self.model = _LR(\\n            max_iter=self.max_iter,\\n            random_state=self.seed,\\n            solver=\\\"lbfgs\\\",\\n        )\\n        self.model.fit(X_s, y_train)\\n\\n    def predict(self, X_test):\\n        X_s = self.scaler.transform(X_test)\\n        return self.model.predict(X_s)\\n\\n    def predict_proba(self, X_test):\\n        X_s = self.scaler.transform(X_test)\\n        probs = self.model.predict_proba(X_s)\\n        if probs.shape[1] < NUM_DEPTHS:\\n            full = np.zeros((probs.shape[0], NUM_DEPTHS))\\n            for i, c in enumerate(self.model.classes_):\\n                full[:, c] = probs[:, i]\\n            return full\\n        return probs\\n\\n\\n# ═══════════════════════════════════════════════════════════════════════\\n#  Unified Runner\\n# ═══════════════════════════════════════════════════════════════════════\\n\\nBASELINE_REGISTRY = {\\n    \\\"ppl_reg_single\\\": (\\\"PPL Regression (single: mean_ppl)\\\", lambda: PPLRegressionBaseline(mode=\\\"single\\\")),\\n    \\\"ppl_reg\\\":        (\\\"PPL Regression (multi: 19-dim OLS)\\\", lambda: PPLRegressionBaseline(mode=\\\"multi\\\")),\\n    \\\"ce_mlp\\\":         (\\\"CE-MLP (DCOL ablation)\\\", None),\\n    \\\"coral\\\":          (\\\"CORAL Ordinal Regression\\\", None),\\n    \\\"diveye\\\":         (\\\"DivEye (XGBoost)\\\", lambda: DivEyeBaseline()),\\n    \\\"rf\\\":             (\\\"Random Forest\\\", lambda: RandomForestBaseline()),\\n    \\\"lr\\\":             (\\\"Logistic Regression\\\", lambda: LogisticRegressionBaseline()),\\n}\\n\\n\\ndef run_baseline(method, X_train, y_train, X_val, y_val, X_test, y_test, args):\\n    if method == \\\"ppl_reg_single\\\":\\n        bl = PPLRegressionBaseline(mode=\\\"single\\\")\\n        bl.fit(X_train, y_train)\\n    elif method == \\\"ppl_reg\\\":\\n        bl = PPLRegressionBaseline(mode=\\\"multi\\\")\\n        bl.fit(X_train, y_train)\\n    elif method == \\\"ce_mlp\\\":\\n        bl = CEClassificationBaseline(\\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\\n            patience=args.patience, seed=args.seed,\\n        )\\n        bl.fit(X_train, y_train, X_val, y_val)\\n    elif method == \\\"coral\\\":\\n        bl = CORALBaseline(\\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\\n            patience=args.patience, seed=args.seed,\\n        )\\n        bl.fit(X_train, y_train, X_val, y_val)\\n    elif method == \\\"diveye\\\":\\n        bl = DivEyeBaseline(seed=args.seed)\\n        bl.fit(X_train, y_train)\\n    elif method == \\\"rf\\\":\\n        bl = RandomForestBaseline(n_estimators=100, seed=args.seed)\\n        bl.fit(X_train, y_train)\\n    elif method == \\\"lr\\\":\\n        bl = LogisticRegressionBaseline(max_iter=1000, seed=args.seed)\\n        bl.fit(X_train, y_train)\\n    else:\\n        print(f\\\"Unknown method: {method}\\\")\\n        return None\\n\\n    y_pred = bl.predict(X_test)\\n    y_prob = bl.predict_proba(X_test)\\n    name = BASELINE_REGISTRY.get(method, (method, None))[0]\\n    return evaluate(name, y_test, y_pred, y_prob)\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"Baseline battery for depth estimation.\\\")\\n    p.add_argument(\\\"--method\\\", default=\\\"all\\\",\\n                   choices=[\\\"ppl_reg_single\\\", \\\"ppl_reg\\\", \\\"ce_mlp\\\", \\\"coral\\\", \\\"diveye\\\", \\\"rf\\\", \\\"lr\\\", \\\"all\\\"])\\n    p.add_argument(\\\"--features_path\\\", default=\\\"data/features_all.jsonl\\\")\\n    p.add_argument(\\\"--output_dir\\\", default=\\\"results/baselines/\\\")\\n    p.add_argument(\\\"--seed\\\", type=int, default=42)\\n    p.add_argument(\\\"--test_size\\\", type=float, default=0.15)\\n    p.add_argument(\\\"--val_size\\\", type=float, default=0.15)\\n    p.add_argument(\\\"--epochs\\\", type=int, default=100)\\n    p.add_argument(\\\"--batch_size\\\", type=int, default=256)\\n    p.add_argument(\\\"--lr\\\", type=float, default=1e-3)\\n    p.add_argument(\\\"--patience\\\", type=int, default=10)\\n    return p.parse_args()\\n\\n\\ndef main():\\n    args = parse_args()\\n    print(f\\\"Loading features from {args.features_path} ...\\\")\\n    X, y = load_features(args.features_path)\\n    print(f\\\"  {X.shape[0]} samples, {X.shape[1]} features\\\")\\n    print(f\\\"  Depth distribution: {dict(Counter(y))}\\\")\\n\\n    X_train, y_train, X_val, y_val, X_test, y_test = prepare_splits(\\n        X, y, test_size=args.test_size, val_size=args.val_size, seed=args.seed\\n    )\\n    print(f\\\"  Train: {len(y_train)}, Val: {len(y_val)}, Test: {len(y_test)}\\\")\\n\\n    methods = list(BASELINE_REGISTRY.keys()) if args.method == \\\"all\\\" else [args.method]\\n    all_results = {}\\n\\n    for m in methods:\\n        result = run_baseline(m, X_train, y_train, X_val, y_val, X_test, y_test, args)\\n        if result is not None:\\n            all_results[m] = result\\n\\n    # Summary table\\n    if len(all_results) > 1:\\n        print(f\\\"\\\\n{'='*60}\\\")\\n        print(f\\\"  SUMMARY\\\")\\n        print(f\\\"{'='*60}\\\")\\n        print(f\\\"  {'Method':<35s} {'4-cls':>6s} {'3-cls':>6s} {'MAE':>6s}\\\")\\n        print(f\\\"  {'-'*35} {'-'*6} {'-'*6} {'-'*6}\\\")\\n        for m, r in all_results.items():\\n            print(f\\\"  {r['method']:<35s} {r['acc_4class']:6.4f} {r['acc_3class']:6.4f} {r['mae']:6.4f}\\\")\\n\\n\\n    os.makedirs(args.output_dir, exist_ok=True)\\n    out_path = os.path.join(args.output_dir, \\\"baseline_results.json\\\")\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(all_results, f, indent=2, default=str)\\n    print(f\\\"\\\\nResults saved to {out_path}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.75}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 130_

<details><summary>Logged reasoning block</summary>

```text
The server version has two additional baselines compared to the local version:
- `RandomForestBaseline` — baseline 5
- `LogisticRegressionBaseline` — baseline 6

Let me also check what baselines 5 and 6 look like on the server (around lines 590-660 which would be the RF baseline).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "39ab5504-b2f2-4082-a625-edab7d41518a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KUzdp21yTGE9PUNXHMLh4s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2805,
      "cache_read_input_tokens": 60236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2805
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

_source line 131_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01NtRg3n3VZAGEpwtQNnV5Hu`</summary>

```json
{
  "server": "gpu-6000pro-2",
  "command": "grep -n \"class Random\\|class Logistic\\|Baseline 5\\|Baseline 6\" /root/autodl-tmp/recursive_gen_depth_est/src/baselines.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "2562df7a-0c47-48bf-a986-0ee1002bec06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KUzdp21yTGE9PUNXHMLh4s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2805,
      "cache_read_input_tokens": 60236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2805
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

_source line 132 · 2026-05-14T23:03:27.598Z_

<details><summary>↩ Tool result · `toolu_01NtRg3n3VZAGEpwtQNnV5Hu`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "03d56627-b126-44ff-b974-9a80c97234d1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 133_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01D2J5iohtpfHpabexPXjbHL`</summary>

```json
{
  "server": "gpu-6000pro-2",
  "command": "grep -n \"class Random\" /root/autodl-tmp/recursive_gen_depth_est/src/baselines.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "df7a7cee-7f9a-4c48-b982-8011418b9e98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqTAbn52BeKvKkxQfUsVRM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 317,
      "cache_read_input_tokens": 63041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 317
      },
      "output_tokens": 71,
      "service_tier": "standard",
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

_source line 134 · 2026-05-14T23:03:30.390Z_

<details><summary>↩ Tool result · `toolu_01D2J5iohtpfHpabexPXjbHL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"594:class RandomForestBaseline:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.75}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "040da75a-781f-4f7a-a391-d5241101c4f2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"594:class RandomForestBaseline:\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.75}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"594:class RandomForestBaseline:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.75}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 135_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PwnaeC2LnjGQzwsMupRsX1`</summary>

```json
{
  "server": "gpu-6000pro-2",
  "command": "cat /root/autodl-tmp/recursive_gen_depth_est/src/baselines.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "04d4b88a-9a57-48f2-9a8f-269abf038b90",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015p3iivuT6odazDeBYznzjR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 198,
      "cache_read_input_tokens": 63358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 198
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

_source line 136 · 2026-05-14T23:03:33.740Z_

<details><summary>↩ Tool result · `toolu_01PwnaeC2LnjGQzwsMupRsX1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nBaseline battery for recursive generation depth estimation.\\n\\nBaselines:\\n  1. PPLRegressionBaseline  — OLS regression on mean_ppl (single) or all 19 features (multi)\\n  2. CEClassificationBaseline — MLP with cross-entropy loss (DCOL ablation, no contrastive loss)\\n  3. CORALBaseline — Ordinal regression with K-1 binary classifiers (Cao et al., 2020)\\n  4. DivEyeBaseline — Surprisal diversity features + XGBoost (Basani & Chen, TMLR 2026)\\n\\nUsage:\\n  python src/baselines.py --method ppl_reg --features_path data/features_all.jsonl\\n  python src/baselines.py --method ce_mlp  --features_path data/features_all.jsonl --epochs 50\\n  python src/baselines.py --method coral   --features_path data/features_all.jsonl --epochs 50\\n  python src/baselines.py --method diveye  --features_path data/features_all.jsonl\\n  python src/baselines.py --method all     --features_path data/features_all.jsonl --epochs 50\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nimport numpy as np\\nfrom collections import Counter\\n\\nimport torch\\nimport torch.nn as nn\\nimport torch.optim as optim\\nfrom torch.utils.data import DataLoader, TensorDataset\\n\\nfrom sklearn.linear_model import LinearRegression\\nfrom sklearn.preprocessing import StandardScaler\\nfrom sklearn.model_selection import train_test_split\\nfrom sklearn.metrics import (\\n    accuracy_score, confusion_matrix, classification_report, roc_auc_score,\\n)\\n\\n# ── Feature schema (must match extract_features.py / dcol_dataset.py) ──\\n\\nFEATURE_NAMES = [\\n    \\\"mean_ppl\\\", \\\"var_ppl\\\", \\\"skewness_ppl\\\", \\\"kurtosis_ppl\\\",\\n    \\\"p10_ppl\\\", \\\"p25_ppl\\\", \\\"p50_ppl\\\", \\\"p75_ppl\\\", \\\"p90_ppl\\\",\\n    \\\"mean_surprisal\\\", \\\"var_surprisal\\\", \\\"entropy_of_surprisal\\\",\\n    \\\"type_token_ratio\\\", \\\"hapax_ratio\\\", \\\"bigram_entropy\\\", \\\"trigram_entropy\\\",\\n    \\\"rep_2gram\\\", \\\"rep_3gram\\\", \\\"rep_4gram\\\",\\n]\\nNUM_FEATURES = len(FEATURE_NAMES)\\nNUM_DEPTHS = 4\\nDEPTH_LABELS = list(range(NUM_DEPTHS))\\n\\n# ── Data loading ──\\n\\ndef load_features(path):\\n    \\\"\\\"\\\"Load JSONL features file → (X [n, 19], y [n]).\\\"\\\"\\\"\\n    records = []\\n    with open(path) as f:\\n        for line in f:\\n            line = line.strip()\\n            if line:\\n                records.append(json.loads(line))\\n    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)\\n    y = np.array([r[\\\"depth\\\"] for r in records], dtype=np.int64)\\n    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)\\n    return X, y\\n\\n\\ndef prepare_splits(X, y, test_size=0.15, val_size=0.15, seed=42):\\n    idx = np.arange(len(y))\\n    train_val_idx, test_idx = train_test_split(\\n        idx, test_size=test_size, stratify=y, random_state=seed\\n    )\\n    rel_val = val_size / (1 - test_size)\\n    train_idx, val_idx = train_test_split(\\n        train_val_idx, test_size=rel_val,\\n        stratify=y[train_val_idx], random_state=seed\\n    )\\n    return (\\n        X[train_idx], y[train_idx],\\n        X[val_idx], y[val_idx],\\n        X[test_idx], y[test_idx],\\n    )\\n\\n# ── Evaluation metrics ──\\n\\ndef pairwise_auc(y_true, y_prob, d1, d2):\\n    mask = np.isin(y_true, [d1, d2])\\n    if mask.sum() < 2:\\n        return None\\n    yt = (y_true[mask] == d2).astype(int)\\n    if len(np.unique(yt)) < 2:\\n        return None\\n    yp = y_prob[mask, d2]\\n    return float(roc_auc_score(yt, yp))\\n\\n\\ndef compute_all_pairwise_auc(y_true, y_prob):\\n    result = {}\\n    for i, d1 in enumerate(DEPTH_LABELS):\\n        for d2 in DEPTH_LABELS[i + 1:]:\\n            auc = pairwise_auc(y_true, y_prob, d1, d2)\\n            result[f\\\"d{d1}_vs_d{d2}\\\"] = round(auc, 4) if auc is not None else None\\n    return result\\n\\n\\ndef bootstrap_ci(y_true, y_pred, metric_fn=accuracy_score, n_boot=1000, seed=42):\\n    rng = np.random.RandomState(seed)\\n    scores = []\\n    n = len(y_true)\\n    for _ in range(n_boot):\\n        idx = rng.choice(n, n, replace=True)\\n        scores.append(metric_fn(y_true[idx], y_pred[idx]))\\n    lo = float(np.percentile(scores, 2.5))\\n    hi = float(np.percentile(scores, 97.5))\\n    return lo, hi\\n\\n\\ndef evaluate(name, y_true, y_pred, y_prob=None):\\n    \\\"\\\"\\\"Print and return evaluation metrics.\\\"\\\"\\\"\\n    acc4 =\\n\\n... [截断: 输出过长，省略 20144 字符] ...\\n\\n),\\n    \\\"coral\\\":          (\\\"CORAL Ordinal Regression\\\", None),\\n    \\\"diveye\\\":         (\\\"DivEye (XGBoost)\\\", lambda: DivEyeBaseline()),\\n    \\\"rf\\\":             (\\\"Random Forest\\\", lambda: RandomForestBaseline()),\\n    \\\"lr\\\":             (\\\"Logistic Regression\\\", lambda: LogisticRegressionBaseline()),\\n}\\n\\n\\ndef run_baseline(method, X_train, y_train, X_val, y_val, X_test, y_test, args):\\n    if method == \\\"ppl_reg_single\\\":\\n        bl = PPLRegressionBaseline(mode=\\\"single\\\")\\n        bl.fit(X_train, y_train)\\n    elif method == \\\"ppl_reg\\\":\\n        bl = PPLRegressionBaseline(mode=\\\"multi\\\")\\n        bl.fit(X_train, y_train)\\n    elif method == \\\"ce_mlp\\\":\\n        bl = CEClassificationBaseline(\\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\\n            patience=args.patience, seed=args.seed,\\n        )\\n        bl.fit(X_train, y_train, X_val, y_val)\\n    elif method == \\\"coral\\\":\\n        bl = CORALBaseline(\\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\\n            patience=args.patience, seed=args.seed,\\n        )\\n        bl.fit(X_train, y_train, X_val, y_val)\\n    elif method == \\\"diveye\\\":\\n        bl = DivEyeBaseline(seed=args.seed)\\n        bl.fit(X_train, y_train)\\n    elif method == \\\"rf\\\":\\n        bl = RandomForestBaseline(n_estimators=100, seed=args.seed)\\n        bl.fit(X_train, y_train)\\n    elif method == \\\"lr\\\":\\n        bl = LogisticRegressionBaseline(max_iter=1000, seed=args.seed)\\n        bl.fit(X_train, y_train)\\n    else:\\n        print(f\\\"Unknown method: {method}\\\")\\n        return None\\n\\n    y_pred = bl.predict(X_test)\\n    y_prob = bl.predict_proba(X_test)\\n    name = BASELINE_REGISTRY.get(method, (method, None))[0]\\n    return evaluate(name, y_test, y_pred, y_prob)\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"Baseline battery for depth estimation.\\\")\\n    p.add_argument(\\\"--method\\\", default=\\\"all\\\",\\n                   choices=[\\\"ppl_reg_single\\\", \\\"ppl_reg\\\", \\\"ce_mlp\\\", \\\"coral\\\", \\\"diveye\\\", \\\"rf\\\", \\\"lr\\\", \\\"all\\\"])\\n    p.add_argument(\\\"--features_path\\\", default=\\\"data/features_all.jsonl\\\")\\n    p.add_argument(\\\"--output_dir\\\", default=\\\"results/baselines/\\\")\\n    p.add_argument(\\\"--seed\\\", type=int, default=42)\\n    p.add_argument(\\\"--test_size\\\", type=float, default=0.15)\\n    p.add_argument(\\\"--val_size\\\", type=float, default=0.15)\\n    p.add_argument(\\\"--epochs\\\", type=int, default=100)\\n    p.add_argument(\\\"--batch_size\\\", type=int, default=256)\\n    p.add_argument(\\\"--lr\\\", type=float, default=1e-3)\\n    p.add_argument(\\\"--patience\\\", type=int, default=10)\\n    return p.parse_args()\\n\\n\\ndef main():\\n    args = parse_args()\\n    print(f\\\"Loading features from {args.features_path} ...\\\")\\n    X, y = load_features(args.features_path)\\n    print(f\\\"  {X.shape[0]} samples, {X.shape[1]} features\\\")\\n    print(f\\\"  Depth distribution: {dict(Counter(y))}\\\")\\n\\n    X_train, y_train, X_val, y_val, X_test, y_test = prepare_splits(\\n        X, y, test_size=args.test_size, val_size=args.val_size, seed=args.seed\\n    )\\n    print(f\\\"  Train: {len(y_train)}, Val: {len(y_val)}, Test: {len(y_test)}\\\")\\n\\n    methods = list(BASELINE_REGISTRY.keys()) if args.method == \\\"all\\\" else [args.method]\\n    all_results = {}\\n\\n    for m in methods:\\n        result = run_baseline(m, X_train, y_train, X_val, y_val, X_test, y_test, args)\\n        if result is not None:\\n            all_results[m] = result\\n\\n    # Summary table\\n    if len(all_results) > 1:\\n        print(f\\\"\\\\n{'='*60}\\\")\\n        print(f\\\"  SUMMARY\\\")\\n        print(f\\\"{'='*60}\\\")\\n        print(f\\\"  {'Method':<35s} {'4-cls':>6s} {'3-cls':>6s} {'MAE':>6s}\\\")\\n        print(f\\\"  {'-'*35} {'-'*6} {'-'*6} {'-'*6}\\\")\\n        for m, r in all_results.items():\\n            print(f\\\"  {r['method']:<35s} {r['acc_4class']:6.4f} {r['acc_3class']:6.4f} {r['mae']:6.4f}\\\")\\n\\n\\n    os.makedirs(args.output_dir, exist_ok=True)\\n    out_path = os.path.join(args.output_dir, \\\"baseline_results.json\\\")\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(all_results, f, indent=2, default=str)\\n    print(f\\\"\\\\nResults saved to {out_path}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.05}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "140c0af4-519b-4f2d-9f57-ca4cf9bb5ecd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nBaseline battery for recursive generation depth estimation.\\\\n\\\\nBaselines:\\\\n  1. PPLRegressionBaseline  — OLS regression on mean_ppl (single) or all 19 features (multi)\\\\n  2. CEClassificationBaseline — MLP with cross-entropy loss (DCOL ablation, no contrastive loss)\\\\n  3. CORALBaseline — Ordinal regression with K-1 binary classifiers (Cao et al., 2020)\\\\n  4. DivEyeBaseline — Surprisal diversity features + XGBoost (Basani & Chen, TMLR 2026)\\\\n\\\\nUsage:\\\\n  python src/baselines.py --method ppl_reg --features_path data/features_all.jsonl\\\\n  python src/baselines.py --method ce_mlp  --features_path data/features_all.jsonl --epochs 50\\\\n  python src/baselines.py --method coral   --features_path data/features_all.jsonl --epochs 50\\\\n  python src/baselines.py --method diveye  --features_path data/features_all.jsonl\\\\n  python src/baselines.py --method all     --features_path data/features_all.jsonl --epochs 50\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport os\\\\nimport sys\\\\nimport numpy as np\\\\nfrom collections import Counter\\\\n\\\\nimport torch\\\\nimport torch.nn as nn\\\\nimport torch.optim as optim\\\\nfrom torch.utils.data import DataLoader, TensorDataset\\\\n\\\\nfrom sklearn.linear_model import LinearRegression\\\\nfrom sklearn.preprocessing import StandardScaler\\\\nfrom sklearn.model_selection import train_test_split\\\\nfrom sklearn.metrics import (\\\\n    accuracy_score, confusion_matrix, classification_report, roc_auc_score,\\\\n)\\\\n\\\\n# ── Feature schema (must match extract_features.py / dcol_dataset.py) ──\\\\n\\\\nFEATURE_NAMES = [\\\\n    \\\\\\\"mean_ppl\\\\\\\", \\\\\\\"var_ppl\\\\\\\", \\\\\\\"skewness_ppl\\\\\\\", \\\\\\\"kurtosis_ppl\\\\\\\",\\\\n    \\\\\\\"p10_ppl\\\\\\\", \\\\\\\"p25_ppl\\\\\\\", \\\\\\\"p50_ppl\\\\\\\", \\\\\\\"p75_ppl\\\\\\\", \\\\\\\"p90_ppl\\\\\\\",\\\\n    \\\\\\\"mean_surprisal\\\\\\\", \\\\\\\"var_surprisal\\\\\\\", \\\\\\\"entropy_of_surprisal\\\\\\\",\\\\n    \\\\\\\"type_token_ratio\\\\\\\", \\\\\\\"hapax_ratio\\\\\\\", \\\\\\\"bigram_entropy\\\\\\\", \\\\\\\"trigram_entropy\\\\\\\",\\\\n    \\\\\\\"rep_2gram\\\\\\\", \\\\\\\"rep_3gram\\\\\\\", \\\\\\\"rep_4gram\\\\\\\",\\\\n]\\\\nNUM_FEATURES = len(FEATURE_NAMES)\\\\nNUM_DEPTHS = 4\\\\nDEPTH_LABELS = list(range(NUM_DEPTHS))\\\\n\\\\n# ── Data loading ──\\\\n\\\\ndef load_features(path):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load JSONL features file → (X [n, 19], y [n]).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    records = []\\\\n    with open(path) as f:\\\\n        for line in f:\\\\n            line = line.strip()\\\\n            if line:\\\\n                records.append(json.loads(line))\\\\n    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)\\\\n    y = np.array([r[\\\\\\\"depth\\\\\\\"] for r in records], dtype=np.int64)\\\\n    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)\\\\n    return X, y\\\\n\\\\n\\\\ndef prepare_splits(X, y, test_size=0.15, val_size=0.15, seed=42):\\\\n    idx = np.arange(len(y))\\\\n    train_val_idx, test_idx = train_test_split(\\\\n        idx, test_size=test_size, stratify=y, random_state=seed\\\\n    )\\\\n    rel_val = val_size / (1 - test_size)\\\\n    train_idx, val_idx = train_test_split(\\\\n        train_val_idx, test_size=rel_val,\\\\n        stratify=y[train_val_idx], random_state=seed\\\\n    )\\\\n    return (\\\\n        X[train_idx], y[train_idx],\\\\n        X[val_idx], y[val_idx],\\\\n        X[test_idx], y[test_idx],\\\\n    )\\\\n\\\\n# ── Evaluation metrics ──\\\\n\\\\ndef pairwise_auc(y_true, y_prob, d1, d2):\\\\n    mask = np.isin(y_true, [d1, d2])\\\\n    if mask.sum() < 2:\\\\n        return None\\\\n    yt = (y_true[mask] == d2).astype(int)\\\\n    if len(np.unique(yt)) < 2:\\\\n        return None\\\\n    yp = y_prob[mask, d2]\\\\n    return float(roc_auc_score(yt, yp))\\\\n\\\\n\\\\ndef compute_all_pairwise_auc(y_true, y_prob):\\\\n    result = {}\\\\n    for i, d1 in enumerate(DEPTH_LABELS):\\\\n        for d2 in DEPTH_LABELS[i + 1:]:\\\\n            auc = pairwise_auc(y_true, y_prob, d1, d2)\\\\n            result[f\\\\\\\"d{d1}_vs_d{d2}\\\\\\\"] = round(auc, 4) if auc is not None else None\\\\n    return result\\\\n\\\\n\\\\ndef bootstrap_ci(y_true, y_pred, metric_fn=accuracy_score, n_boot=1000, seed=42):\\\\n    rng = np.random.RandomState(seed)\\\\n    scores = []\\\\n    n = len(y_true)\\\\n    for _ in range(n_boot):\\\\n        idx = rng.choice(n, n, replace=True)\\\\n        scores.append(metric_fn(y_true[idx], y_pred[idx]))\\\\n    lo = float(np.percentile(scores, 2.5))\\\\n    hi = float(np.percentile(scores, 97.5))\\\\n    return lo, hi\\\\n\\\\n\\\\ndef evaluate(name, y_true, y_pred, y_prob=None):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Print and return evaluation metrics.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    acc4 =\\\\n\\\\n... [截断: 输出过长，省略 20144 字符] ...\\\\n\\\\n),\\\\n    \\\\\\\"coral\\\\\\\":          (\\\\\\\"CORAL Ordinal Regression\\\\\\\", None),\\\\n    \\\\\\\"diveye\\\\\\\":         (\\\\\\\"DivEye (XGBoost)\\\\\\\", lambda: DivEyeBaseline()),\\\\n    \\\\\\\"rf\\\\\\\":             (\\\\\\\"Random Forest\\\\\\\", lambda: RandomForestBaseline()),\\\\n    \\\\\\\"lr\\\\\\\":             (\\\\\\\"Logistic Regression\\\\\\\", lambda: LogisticRegressionBaseline()),\\\\n}\\\\n\\\\n\\\\ndef run_baseline(method, X_train, y_train, X_val, y_val, X_test, y_test, args):\\\\n    if method == \\\\\\\"ppl_reg_single\\\\\\\":\\\\n        bl = PPLRegressionBaseline(mode=\\\\\\\"single\\\\\\\")\\\\n        bl.fit(X_train, y_train)\\\\n    elif method == \\\\\\\"ppl_reg\\\\\\\":\\\\n        bl = PPLRegressionBaseline(mode=\\\\\\\"multi\\\\\\\")\\\\n        bl.fit(X_train, y_train)\\\\n    elif method == \\\\\\\"ce_mlp\\\\\\\":\\\\n        bl = CEClassificationBaseline(\\\\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\\\\n            patience=args.patience, seed=args.seed,\\\\n        )\\\\n        bl.fit(X_train, y_train, X_val, y_val)\\\\n    elif method == \\\\\\\"coral\\\\\\\":\\\\n        bl = CORALBaseline(\\\\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\\\\n            patience=args.patience, seed=args.seed,\\\\n        )\\\\n        bl.fit(X_train, y_train, X_val, y_val)\\\\n    elif method == \\\\\\\"diveye\\\\\\\":\\\\n        bl = DivEyeBaseline(seed=args.seed)\\\\n        bl.fit(X_train, y_train)\\\\n    elif method == \\\\\\\"rf\\\\\\\":\\\\n        bl = RandomForestBaseline(n_estimators=100, seed=args.seed)\\\\n        bl.fit(X_train, y_train)\\\\n    elif method == \\\\\\\"lr\\\\\\\":\\\\n        bl = LogisticRegressionBaseline(max_iter=1000, seed=args.seed)\\\\n        bl.fit(X_train, y_train)\\\\n    else:\\\\n        print(f\\\\\\\"Unknown method: {method}\\\\\\\")\\\\n        return None\\\\n\\\\n    y_pred = bl.predict(X_test)\\\\n    y_prob = bl.predict_proba(X_test)\\\\n    name = BASELINE_REGISTRY.get(method, (method, None))[0]\\\\n    return evaluate(name, y_test, y_pred, y_prob)\\\\n\\\\n\\\\ndef parse_args():\\\\n    p = argparse.ArgumentParser(description=\\\\\\\"Baseline battery for depth estimation.\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--method\\\\\\\", default=\\\\\\\"all\\\\\\\",\\\\n                   choices=[\\\\\\\"ppl_reg_single\\\\\\\", \\\\\\\"ppl_reg\\\\\\\", \\\\\\\"ce_mlp\\\\\\\", \\\\\\\"coral\\\\\\\", \\\\\\\"diveye\\\\\\\", \\\\\\\"rf\\\\\\\", \\\\\\\"lr\\\\\\\", \\\\\\\"all\\\\\\\"])\\\\n    p.add_argument(\\\\\\\"--features_path\\\\\\\", default=\\\\\\\"data/features_all.jsonl\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--output_dir\\\\\\\", default=\\\\\\\"results/baselines/\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--seed\\\\\\\", type=int, default=42)\\\\n    p.add_argument(\\\\\\\"--test_size\\\\\\\", type=float, default=0.15)\\\\n    p.add_argument(\\\\\\\"--val_size\\\\\\\", type=float, default=0.15)\\\\n    p.add_argument(\\\\\\\"--epochs\\\\\\\", type=int, default=100)\\\\n    p.add_argument(\\\\\\\"--batch_size\\\\\\\", type=int, default=256)\\\\n    p.add_argument(\\\\\\\"--lr\\\\\\\", type=float, default=1e-3)\\\\n    p.add_argument(\\\\\\\"--patience\\\\\\\", type=int, default=10)\\\\n    return p.parse_args()\\\\n\\\\n\\\\ndef main():\\\\n    args = parse_args()\\\\n    print(f\\\\\\\"Loading features from {args.features_path} ...\\\\\\\")\\\\n    X, y = load_features(args.features_path)\\\\n    print(f\\\\\\\"  {X.shape[0]} samples, {X.shape[1]} features\\\\\\\")\\\\n    print(f\\\\\\\"  Depth distribution: {dict(Counter(y))}\\\\\\\")\\\\n\\\\n    X_train, y_train, X_val, y_val, X_test, y_test = prepare_splits(\\\\n        X, y, test_size=args.test_size, val_size=args.val_size, seed=args.seed\\\\n    )\\\\n    print(f\\\\\\\"  Train: {len(y_train)}, Val: {len(y_val)}, Test: {len(y_test)}\\\\\\\")\\\\n\\\\n    methods = list(BASELINE_REGISTRY.keys()) if args.method == \\\\\\\"all\\\\\\\" else [args.method]\\\\n    all_results = {}\\\\n\\\\n    for m in methods:\\\\n        result = run_baseline(m, X_train, y_train, X_val, y_val, X_test, y_test, args)\\\\n        if result is not None:\\\\n            all_results[m] = result\\\\n\\\\n    # Summary table\\\\n    if len(all_results) > 1:\\\\n        print(f\\\\\\\"\\\\\\\\n{'='*60}\\\\\\\")\\\\n        print(f\\\\\\\"  SUMMARY\\\\\\\")\\\\n        print(f\\\\\\\"{'='*60}\\\\\\\")\\\\n        print(f\\\\\\\"  {'Method':<35s} {'4-cls':>6s} {'3-cls':>6s} {'MAE':>6s}\\\\\\\")\\\\n        print(f\\\\\\\"  {'-'*35} {'-'*6} {'-'*6} {'-'*6}\\\\\\\")\\\\n        for m, r in all_results.items():\\\\n            print(f\\\\\\\"  {r['method']:<35s} {r['acc_4class']:6.4f} {r['acc_3class']:6.4f} {r['mae']:6.4f}\\\\\\\")\\\\n\\\\n\\\\n    os.makedirs(args.output_dir, exist_ok=True)\\\\n    out_path = os.path.join(args.output_dir, \\\\\\\"baseline_results.json\\\\\\\")\\\\n    with open(out_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(all_results, f, indent=2, default=str)\\\\n    print(f\\\\\\\"\\\\\\\\nResults saved to {out_path}\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.05}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nBaseline battery for recursive generation depth estimation.\\n\\nBaselines:\\n  1. PPLRegressionBaseline  — OLS regression on mean_ppl (single) or all 19 features (multi)\\n  2. CEClassificationBaseline — MLP with cross-entropy loss (DCOL ablation, no contrastive loss)\\n  3. CORALBaseline — Ordinal regression with K-1 binary classifiers (Cao et al., 2020)\\n  4. DivEyeBaseline — Surprisal diversity features + XGBoost (Basani & Chen, TMLR 2026)\\n\\nUsage:\\n  python src/baselines.py --method ppl_reg --features_path data/features_all.jsonl\\n  python src/baselines.py --method ce_mlp  --features_path data/features_all.jsonl --epochs 50\\n  python src/baselines.py --method coral   --features_path data/features_all.jsonl --epochs 50\\n  python src/baselines.py --method diveye  --features_path data/features_all.jsonl\\n  python src/baselines.py --method all     --features_path data/features_all.jsonl --epochs 50\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nimport numpy as np\\nfrom collections import Counter\\n\\nimport torch\\nimport torch.nn as nn\\nimport torch.optim as optim\\nfrom torch.utils.data import DataLoader, TensorDataset\\n\\nfrom sklearn.linear_model import LinearRegression\\nfrom sklearn.preprocessing import StandardScaler\\nfrom sklearn.model_selection import train_test_split\\nfrom sklearn.metrics import (\\n    accuracy_score, confusion_matrix, classification_report, roc_auc_score,\\n)\\n\\n# ── Feature schema (must match extract_features.py / dcol_dataset.py) ──\\n\\nFEATURE_NAMES = [\\n    \\\"mean_ppl\\\", \\\"var_ppl\\\", \\\"skewness_ppl\\\", \\\"kurtosis_ppl\\\",\\n    \\\"p10_ppl\\\", \\\"p25_ppl\\\", \\\"p50_ppl\\\", \\\"p75_ppl\\\", \\\"p90_ppl\\\",\\n    \\\"mean_surprisal\\\", \\\"var_surprisal\\\", \\\"entropy_of_surprisal\\\",\\n    \\\"type_token_ratio\\\", \\\"hapax_ratio\\\", \\\"bigram_entropy\\\", \\\"trigram_entropy\\\",\\n    \\\"rep_2gram\\\", \\\"rep_3gram\\\", \\\"rep_4gram\\\",\\n]\\nNUM_FEATURES = len(FEATURE_NAMES)\\nNUM_DEPTHS = 4\\nDEPTH_LABELS = list(range(NUM_DEPTHS))\\n\\n# ── Data loading ──\\n\\ndef load_features(path):\\n    \\\"\\\"\\\"Load JSONL features file → (X [n, 19], y [n]).\\\"\\\"\\\"\\n    records = []\\n    with open(path) as f:\\n        for line in f:\\n            line = line.strip()\\n            if line:\\n                records.append(json.loads(line))\\n    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)\\n    y = np.array([r[\\\"depth\\\"] for r in records], dtype=np.int64)\\n    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)\\n    return X, y\\n\\n\\ndef prepare_splits(X, y, test_size=0.15, val_size=0.15, seed=42):\\n    idx = np.arange(len(y))\\n    train_val_idx, test_idx = train_test_split(\\n        idx, test_size=test_size, stratify=y, random_state=seed\\n    )\\n    rel_val = val_size / (1 - test_size)\\n    train_idx, val_idx = train_test_split(\\n        train_val_idx, test_size=rel_val,\\n        stratify=y[train_val_idx], random_state=seed\\n    )\\n    return (\\n        X[train_idx], y[train_idx],\\n        X[val_idx], y[val_idx],\\n        X[test_idx], y[test_idx],\\n    )\\n\\n# ── Evaluation metrics ──\\n\\ndef pairwise_auc(y_true, y_prob, d1, d2):\\n    mask = np.isin(y_true, [d1, d2])\\n    if mask.sum() < 2:\\n        return None\\n    yt = (y_true[mask] == d2).astype(int)\\n    if len(np.unique(yt)) < 2:\\n        return None\\n    yp = y_prob[mask, d2]\\n    return float(roc_auc_score(yt, yp))\\n\\n\\ndef compute_all_pairwise_auc(y_true, y_prob):\\n    result = {}\\n    for i, d1 in enumerate(DEPTH_LABELS):\\n        for d2 in DEPTH_LABELS[i + 1:]:\\n            auc = pairwise_auc(y_true, y_prob, d1, d2)\\n            result[f\\\"d{d1}_vs_d{d2}\\\"] = round(auc, 4) if auc is not None else None\\n    return result\\n\\n\\ndef bootstrap_ci(y_true, y_pred, metric_fn=accuracy_score, n_boot=1000, seed=42):\\n    rng = np.random.RandomState(seed)\\n    scores = []\\n    n = len(y_true)\\n    for _ in range(n_boot):\\n        idx = rng.choice(n, n, replace=True)\\n        scores.append(metric_fn(y_true[idx], y_pred[idx]))\\n    lo = float(np.percentile(scores, 2.5))\\n    hi = float(np.percentile(scores, 97.5))\\n    return lo, hi\\n\\n\\ndef evaluate(name, y_true, y_pred, y_prob=None):\\n    \\\"\\\"\\\"Print and return evaluation metrics.\\\"\\\"\\\"\\n    acc4 =\\n\\n... [截断: 输出过长，省略 20144 字符] ...\\n\\n),\\n    \\\"coral\\\":          (\\\"CORAL Ordinal Regression\\\", None),\\n    \\\"diveye\\\":         (\\\"DivEye (XGBoost)\\\", lambda: DivEyeBaseline()),\\n    \\\"rf\\\":             (\\\"Random Forest\\\", lambda: RandomForestBaseline()),\\n    \\\"lr\\\":             (\\\"Logistic Regression\\\", lambda: LogisticRegressionBaseline()),\\n}\\n\\n\\ndef run_baseline(method, X_train, y_train, X_val, y_val, X_test, y_test, args):\\n    if method == \\\"ppl_reg_single\\\":\\n        bl = PPLRegressionBaseline(mode=\\\"single\\\")\\n        bl.fit(X_train, y_train)\\n    elif method == \\\"ppl_reg\\\":\\n        bl = PPLRegressionBaseline(mode=\\\"multi\\\")\\n        bl.fit(X_train, y_train)\\n    elif method == \\\"ce_mlp\\\":\\n        bl = CEClassificationBaseline(\\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\\n            patience=args.patience, seed=args.seed,\\n        )\\n        bl.fit(X_train, y_train, X_val, y_val)\\n    elif method == \\\"coral\\\":\\n        bl = CORALBaseline(\\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\\n            patience=args.patience, seed=args.seed,\\n        )\\n        bl.fit(X_train, y_train, X_val, y_val)\\n    elif method == \\\"diveye\\\":\\n        bl = DivEyeBaseline(seed=args.seed)\\n        bl.fit(X_train, y_train)\\n    elif method == \\\"rf\\\":\\n        bl = RandomForestBaseline(n_estimators=100, seed=args.seed)\\n        bl.fit(X_train, y_train)\\n    elif method == \\\"lr\\\":\\n        bl = LogisticRegressionBaseline(max_iter=1000, seed=args.seed)\\n        bl.fit(X_train, y_train)\\n    else:\\n        print(f\\\"Unknown method: {method}\\\")\\n        return None\\n\\n    y_pred = bl.predict(X_test)\\n    y_prob = bl.predict_proba(X_test)\\n    name = BASELINE_REGISTRY.get(method, (method, None))[0]\\n    return evaluate(name, y_test, y_pred, y_prob)\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"Baseline battery for depth estimation.\\\")\\n    p.add_argument(\\\"--method\\\", default=\\\"all\\\",\\n                   choices=[\\\"ppl_reg_single\\\", \\\"ppl_reg\\\", \\\"ce_mlp\\\", \\\"coral\\\", \\\"diveye\\\", \\\"rf\\\", \\\"lr\\\", \\\"all\\\"])\\n    p.add_argument(\\\"--features_path\\\", default=\\\"data/features_all.jsonl\\\")\\n    p.add_argument(\\\"--output_dir\\\", default=\\\"results/baselines/\\\")\\n    p.add_argument(\\\"--seed\\\", type=int, default=42)\\n    p.add_argument(\\\"--test_size\\\", type=float, default=0.15)\\n    p.add_argument(\\\"--val_size\\\", type=float, default=0.15)\\n    p.add_argument(\\\"--epochs\\\", type=int, default=100)\\n    p.add_argument(\\\"--batch_size\\\", type=int, default=256)\\n    p.add_argument(\\\"--lr\\\", type=float, default=1e-3)\\n    p.add_argument(\\\"--patience\\\", type=int, default=10)\\n    return p.parse_args()\\n\\n\\ndef main():\\n    args = parse_args()\\n    print(f\\\"Loading features from {args.features_path} ...\\\")\\n    X, y = load_features(args.features_path)\\n    print(f\\\"  {X.shape[0]} samples, {X.shape[1]} features\\\")\\n    print(f\\\"  Depth distribution: {dict(Counter(y))}\\\")\\n\\n    X_train, y_train, X_val, y_val, X_test, y_test = prepare_splits(\\n        X, y, test_size=args.test_size, val_size=args.val_size, seed=args.seed\\n    )\\n    print(f\\\"  Train: {len(y_train)}, Val: {len(y_val)}, Test: {len(y_test)}\\\")\\n\\n    methods = list(BASELINE_REGISTRY.keys()) if args.method == \\\"all\\\" else [args.method]\\n    all_results = {}\\n\\n    for m in methods:\\n        result = run_baseline(m, X_train, y_train, X_val, y_val, X_test, y_test, args)\\n        if result is not None:\\n            all_results[m] = result\\n\\n    # Summary table\\n    if len(all_results) > 1:\\n        print(f\\\"\\\\n{'='*60}\\\")\\n        print(f\\\"  SUMMARY\\\")\\n        print(f\\\"{'='*60}\\\")\\n        print(f\\\"  {'Method':<35s} {'4-cls':>6s} {'3-cls':>6s} {'MAE':>6s}\\\")\\n        print(f\\\"  {'-'*35} {'-'*6} {'-'*6} {'-'*6}\\\")\\n        for m, r in all_results.items():\\n            print(f\\\"  {r['method']:<35s} {r['acc_4class']:6.4f} {r['acc_3class']:6.4f} {r['mae']:6.4f}\\\")\\n\\n\\n    os.makedirs(args.output_dir, exist_ok=True)\\n    out_path = os.path.join(args.output_dir, \\\"baseline_results.json\\\")\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(all_results, f, indent=2, default=str)\\n    print(f\\\"\\\\nResults saved to {out_path}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.05}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 137_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture. The server `src/baselines.py` has 772 lines with 7 baselines:
1. PPLRegressionBaseline (single/multi)
2. CEClassificationBaseline (MLP)
3. CORALBaseline
4. DivEyeBaseline (XGBoost)
5. RandomForestBaseline
6. LogisticRegressionBaseline

The task asks for:
1. Perplexity Regression ✅ exists


2. CORAL ✅ exists
3. CE ✅ exists
4. DivEye ✅ exists
5. Zero-shot LLM ❌ NOT in the unified file

The code also has RF and LR baselines. I notice the task expects a `--data_path` argument, but the current implementation uses `--features_path` instead. The main gap is that I need to add the Zero-shot LLM baseline, while the other four methods are already implemented and working.

The challenge is that Zero-shot LLM operates on raw text rather than feature vectors, which creates a mismatch with the unified baselines.py that processes JSONL features. I can work around this by adding Zero-shot LLM as a separate mode within the same script. My plan is to update the local baselines.py to match the server version with RF and LR included, add support for the `--data_path` CLI argument, and then integrate Zero-shot LLM as an alternative pathway that handles raw text input. I need to test each baseline to make sure they work correctly. The server already has baselines 1-6 implemented, but I'm missing the zero-shot LLM baseline that the task requires. Since it needs raw text data and API calls rather than pre-computed features, I'll need to integrate the existing implementation from `scripts/baseline_zeroshot_llm.py` into the main baselines file, and I should also add the `--data_path` CLI alias while I'm at it.

The challenge is that the unified baselines.py is already quite large at 772 lines, and adding zero-shot LLM will push it over 870 lines. I need to add the Zero-shot LLM class, support `--data_dirs` for text-based methods, create the `--data_path` alias, register it in the baseline registry, and handle its special loading requirements. Let me also verify whether the server has the raw text data in the depth_*.jsonl format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "e32e0677-40ba-411d-b596-407e10c5a931",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YZRFjcecAxxgVBmxystZ1Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3724,
      "cache_read_input_tokens": 63556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3724
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

_source line 138_

Good — the server `src/baselines.py` (772 lines) already has 7 baselines (PPL, CE, CORAL, DivEye, RF, LR). Missing: Zero-shot LLM, and `--data_path` alias. Let me check if raw text data exists on server, then update the unified file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "34517f40-7857-47d7-94c7-66b686663eb7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YZRFjcecAxxgVBmxystZ1Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3724,
      "cache_read_input_tokens": 63556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3724
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

_source line 139_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014YGqt4p85o8dAqXEokwnv5`</summary>

```json
{
  "server": "gpu-6000pro-2",
  "command": "find /root/autodl-tmp/recursive_gen_depth_est/data -name \"depth_*.jsonl\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "9ef5a392-1440-4d75-b403-b0b43f55b59b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YZRFjcecAxxgVBmxystZ1Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3724,
      "cache_read_input_tokens": 63556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3724
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

_source line 140_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XfyCQUhFsSjQE1KfURXusz`</summary>

```json
{
  "server": "gpu-6000pro-2",
  "command": "head -1 /root/autodl-tmp/recursive_gen_depth_est/data/features_all.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "60dd27d7-5467-4d1f-bde9-6ea12c243299",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YZRFjcecAxxgVBmxystZ1Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3724,
      "cache_read_input_tokens": 63556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3724
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

_source line 141 · 2026-05-14T23:04:03.950Z_

<details><summary>↩ Tool result · `toolu_014YGqt4p85o8dAqXEokwnv5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/recursive_gen_depth_est/data/depth_0.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/depth_1.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/depth_2.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/depth_0_features.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/depth_3.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl/depth_0.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl/depth_1.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl/depth_2.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl/depth_3.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/olmo/depth_0.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/olmo/depth_1.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/olmo/depth_2.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/olmo/depth_3.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/pythia_temp09/depth_1.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/pythia_temp09/depth_2.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/pythia_temp09/depth_3.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/pythia_topk50/depth_1.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/pythia_topk50/depth_2.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/pythia_topk50/depth_3.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/olmo_temp09/depth_1.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/olmo_temp09/depth_2.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl_temp09/depth_1.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl_temp09/depth_2.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl_temp09/depth_3.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl_topk50/depth_1.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "1125188c-99c0-4e35-a732-8a3dd6b243be",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/recursive_gen_depth_est/data/depth_0.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/depth_1.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/depth_2.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/depth_0_features.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/depth_3.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl/depth_0.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl/depth_1.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl/depth_2.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl/depth_3.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/olmo/depth_0.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/olmo/depth_1.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/olmo/depth_2.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/olmo/depth_3.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/pythia_temp09/depth_1.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/pythia_temp09/depth_2.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/pythia_temp09/depth_3.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/pythia_topk50/depth_1.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/pythia_topk50/depth_2.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/pythia_topk50/depth_3.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/olmo_temp09/depth_1.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/olmo_temp09/depth_2.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl_temp09/depth_1.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl_temp09/depth_2.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl_temp09/depth_3.jsonl\\\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl_topk50/depth_1.jsonl\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.76}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/recursive_gen_depth_est/data/depth_0.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/depth_1.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/depth_2.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/depth_0_features.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/depth_3.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl/depth_0.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl/depth_1.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl/depth_2.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl/depth_3.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/olmo/depth_0.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/olmo/depth_1.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/olmo/depth_2.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/olmo/depth_3.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/pythia_temp09/depth_1.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/pythia_temp09/depth_2.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/pythia_temp09/depth_3.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/pythia_topk50/depth_1.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/pythia_topk50/depth_2.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/pythia_topk50/depth_3.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/olmo_temp09/depth_1.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/olmo_temp09/depth_2.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl_temp09/depth_1.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl_temp09/depth_2.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl_temp09/depth_3.jsonl\\n/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl_topk50/depth_1.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 142 · 2026-05-14T23:04:04.863Z_

<details><summary>↩ Tool result · `toolu_01XfyCQUhFsSjQE1KfURXusz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"depth\\\": 0, \\\"sample_id\\\": 0, \\\"mean_ppl\\\": 1607.154718291221, \\\"var_ppl\\\": 158779688.72304317, \\\"skewness_ppl\\\": 10.406051089379453, \\\"kurtosis_ppl\\\": 114.01617768762445, \\\"p10_ppl\\\": 1.0253935757537525, \\\"p25_ppl\\\": 1.4685526791140988, \\\"p50_ppl\\\": 4.352294272371119, \\\"p75_ppl\\\": 39.40245503911115, \\\"p90_ppl\\\": 369.16657551683574, \\\"mean_surprisal\\\": 2.372938156607645, \\\"var_surprisal\\\": 6.239684146274182, \\\"entropy_of_surprisal\\\": 3.1822611603270903, \\\"type_token_ratio\\\": 0.570281124497992, \\\"hapax_ratio\\\": 0.7922535211267606, \\\"bigram_entropy\\\": 6.013228236535451, \\\"trigram_entropy\\\": 6.165336778855558, \\\"rep_2gram\\\": 0.11066398390342047, \\\"rep_3gram\\\": 0.028225806451612878, \\\"rep_4gram\\\": 0.014141414141414121}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "5486def8-6392-4b6e-8e63-2003ea41af7e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\\\\"depth\\\\\\\": 0, \\\\\\\"sample_id\\\\\\\": 0, \\\\\\\"mean_ppl\\\\\\\": 1607.154718291221, \\\\\\\"var_ppl\\\\\\\": 158779688.72304317, \\\\\\\"skewness_ppl\\\\\\\": 10.406051089379453, \\\\\\\"kurtosis_ppl\\\\\\\": 114.01617768762445, \\\\\\\"p10_ppl\\\\\\\": 1.0253935757537525, \\\\\\\"p25_ppl\\\\\\\": 1.4685526791140988, \\\\\\\"p50_ppl\\\\\\\": 4.352294272371119, \\\\\\\"p75_ppl\\\\\\\": 39.40245503911115, \\\\\\\"p90_ppl\\\\\\\": 369.16657551683574, \\\\\\\"mean_surprisal\\\\\\\": 2.372938156607645, \\\\\\\"var_surprisal\\\\\\\": 6.239684146274182, \\\\\\\"entropy_of_surprisal\\\\\\\": 3.1822611603270903, \\\\\\\"type_token_ratio\\\\\\\": 0.570281124497992, \\\\\\\"hapax_ratio\\\\\\\": 0.7922535211267606, \\\\\\\"bigram_entropy\\\\\\\": 6.013228236535451, \\\\\\\"trigram_entropy\\\\\\\": 6.165336778855558, \\\\\\\"rep_2gram\\\\\\\": 0.11066398390342047, \\\\\\\"rep_3gram\\\\\\\": 0.028225806451612878, \\\\\\\"rep_4gram\\\\\\\": 0.014141414141414121}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.9}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\\"depth\\\": 0, \\\"sample_id\\\": 0, \\\"mean_ppl\\\": 1607.154718291221, \\\"var_ppl\\\": 158779688.72304317, \\\"skewness_ppl\\\": 10.406051089379453, \\\"kurtosis_ppl\\\": 114.01617768762445, \\\"p10_ppl\\\": 1.0253935757537525, \\\"p25_ppl\\\": 1.4685526791140988, \\\"p50_ppl\\\": 4.352294272371119, \\\"p75_ppl\\\": 39.40245503911115, \\\"p90_ppl\\\": 369.16657551683574, \\\"mean_surprisal\\\": 2.372938156607645, \\\"var_surprisal\\\": 6.239684146274182, \\\"entropy_of_surprisal\\\": 3.1822611603270903, \\\"type_token_ratio\\\": 0.570281124497992, \\\"hapax_ratio\\\": 0.7922535211267606, \\\"bigram_entropy\\\": 6.013228236535451, \\\"trigram_entropy\\\": 6.165336778855558, \\\"rep_2gram\\\": 0.11066398390342047, \\\"rep_3gram\\\": 0.028225806451612878, \\\"rep_4gram\\\": 0.014141414141414121}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 143_

<details><summary>Logged reasoning block</summary>

```text
Raw text data exists in `depth_*.jsonl` files. The features file has the expected format. Now I have the full picture.

Let me now write the updated `src/baselines.py` that includes:
1. All existing baselines (PPL, CE, CORAL, DivEye, RF, LR)
2. Zero-shot LLM baseline
3. `--data_path` alias
4. Updated docstring listing all 7 methods

Then I'll deploy to server and dry-run.

Actually, let me think about what changes I need to make to the existing file. The server file is 772 lines. I need to:


1. Add Zero-shot LLM class (~80 lines)
2. Add `--data_dirs` and `--data_path` args
3. Add zero-shot to registry and run_baseline
4. Handle text-based loading for zero-shot

Let me write the complete updated file. Actually, since the server already has the file, let me just write the additions and push via ssh_execute. That's cleaner than writing 850 lines locally.

No wait — the task says to write `src/baselines.py`. And the project code is synced between local `artifacts/` and remote `src/`. Let me update the local file first, then sync to server.

Actually, looking at the project structure, I should update the local file in `artifacts/` and let the sync handle deployment. Let me start writing the updated baselines file with all the necessary changes integrated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "e823f8ae-2b04-4e53-8779-79ed8d008108",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGa3FruqqnbhquWaYrxzoe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2790,
      "cache_read_input_tokens": 67280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2790
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

_source line 144_

Now I have the complete picture. The server `src/baselines.py` has 7 baselines but is missing Zero-shot LLM. I'll add it and the `--data_path` alias, then deploy and dry-run.

Let me write the updated file locally and deploy to server.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "3413ece6-a073-4903-8188-3bf6557bda3d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGa3FruqqnbhquWaYrxzoe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2790,
      "cache_read_input_tokens": 67280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2790
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

_source line 145_

<details open><summary>🔧 Tool call — Read · `toolu_01Ki1o1i4rhMq6U3n2FynTci`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/baselines.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "932fc0de-89a8-4d41-b354-2b5f1260fbd9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGa3FruqqnbhquWaYrxzoe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2790,
      "cache_read_input_tokens": 67280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2790
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

_source line 146 · 2026-05-14T23:04:21.687Z_

<details><summary>↩ Tool result · `toolu_01Ki1o1i4rhMq6U3n2FynTci`</summary>

```text
1	"""
2	Baseline battery for recursive generation depth estimation.
3	
4	Baselines:
5	  1. PPLRegressionBaseline  — OLS regression on mean_ppl (single) or all 19 features (multi)
6	  2. CEClassificationBaseline — MLP with cross-entropy loss (DCOL ablation, no contrastive loss)
7	  3. CORALBaseline — Ordinal regression with K-1 binary classifiers (Cao et al., 2020)
8	  4. DivEyeBaseline — Surprisal diversity features + XGBoost (Basani & Chen, TMLR 2026)
9	
10	Usage:
11	  python src/baselines.py --method ppl_reg --features_path data/features_all.jsonl
12	  python src/baselines.py --method ce_mlp  --features_path data/features_all.jsonl --epochs 50
13	  python src/baselines.py --method coral   --features_path data/features_all.jsonl --epochs 50
14	  python src/baselines.py --method diveye  --features_path data/features_all.jsonl
15	  python src/baselines.py --method all     --features_path data/features_all.jsonl --epochs 50
16	"""
17	
18	import argparse
19	import json
20	import os
21	import sys
22	import numpy as np
23	from collections import Counter
24	
25	import torch
26	import torch.nn as nn
27	import torch.optim as optim
28	from torch.utils.data import DataLoader, TensorDataset
29	
30	from sklearn.linear_model import LinearRegression
31	from sklearn.preprocessing import StandardScaler
32	from sklearn.model_selection import train_test_split
33	from sklearn.metrics import (
34	    accuracy_score, confusion_matrix, classification_report, roc_auc_score,
35	)
36	
37	# ── Feature schema (must match extract_features.py / dcol_dataset.py) ──
38	
39	FEATURE_NAMES = [
40	    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
41	    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
42	    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
43	    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
44	    "rep_2gram", "rep_3gram", "rep_4gram",
45	]
46	NUM_FEATURES = len(FEATURE_NAMES)
47	NUM_DEPTHS = 4
48	DEPTH_LABELS = list(range(NUM_DEPTHS))
49	
50	# ── Data loading ──
51	
52	def load_features(path):
53	    """Load JSONL features file → (X [n, 19], y [n])."""
54	    records = []
55	    with open(path) as f:
56	        for line in f:
57	            line = line.strip()
58	            if line:
59	                records.append(json.loads(line))
60	    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)
61	    y = np.array([r["depth"] for r in records], dtype=np.int64)
62	    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
63	    return X, y
64	
65	
66	def prepare_splits(X, y, test_size=0.15, val_size=0.15, seed=42):
67	    idx = np.arange(len(y))
68	    train_val_idx, test_idx = train_test_split(
69	        idx, test_size=test_size, stratify=y, random_state=seed
70	    )
71	    rel_val = val_size / (1 - test_size)
72	    train_idx, val_idx = train_test_split(
73	        train_val_idx, test_size=rel_val,
74	        stratify=y[train_val_idx], random_state=seed
75	    )
76	    return (
77	        X[train_idx], y[train_idx],
78	        X[val_idx], y[val_idx],
79	        X[test_idx], y[test_idx],
80	    )
81	
82	# ── Evaluation metrics ──
83	
84	def pairwise_auc(y_true, y_prob, d1, d2):
85	    mask = np.isin(y_true, [d1, d2])
86	    if mask.sum() < 2:
87	        return None
88	    yt = (y_true[mask] == d2).astype(int)
89	    if len(np.unique(yt)) < 2:
90	        return None
91	    yp = y_prob[mask, d2]
92	    return float(roc_auc_score(yt, yp))
93	
94	
95	def compute_all_pairwise_auc(y_true, y_prob):
96	    result = {}
97	    for i, d1 in enumerate(DEPTH_LABELS):
98	        for d2 in DEPTH_LABELS[i + 1:]:
99	            auc = pairwise_auc(y_true, y_prob, d1, d2)
100	            result[f"d{d1}_vs_d{d2}"] = round(auc, 4) if auc is not None else None
101	    return result
102	
103	
104	def bootstrap_ci(y_true, y_pred, metric_fn=accuracy_score, n_boot=1000, seed=42):
105	    rng = np.random.RandomState(seed)
106	    scores = []
107	    n = len(y_true)
108	    for _ in range(n_boot):
109	        idx = rng.choice(n, n, replace=True)
110	        scores.append(metric_fn(y_true[idx], y_pred[idx]))
111	    lo = float(np.percentile(scores, 2.5))
112	    hi = float(np.percentile(scores, 97.5))
113	    return lo, hi
114	
115	
116	def evaluate(name, y_true, y_pred, y_prob=None):
117	    """Print and return evaluation metrics."""
118	    acc4 = accuracy_score(y_true, y_pred)
119	    ci_lo, ci_hi = bootstrap_ci(y_true, y_pred)
120	
121	    # 3-class accuracy (depth 1-3 only)
122	    mask_13 = y_true >= 1
123	    acc3 = accuracy_score(y_true[mask_13], y_pred[mask_13]) if mask_13.sum() > 0 else 0.0
124	
125	    mae = float(np.mean(np.abs(y_true - y_pred)))
126	
127	    cm = confusion_matrix(y_true, y_pred, labels=DEPTH_LABELS)
128	    per_class_recall = cm.diagonal() / cm.sum(axis=1).clip(min=1)
129	
130	    pair_aucs = {}
131	    if y_prob is not None:
132	        pair_aucs = compute_all_pairwise_auc(y_true, y_prob)
133	
134	    print(f"\n{'='*60}")
135	    print(f"  {name}")
136	    print(f"{'='*60}")
137	    print(f"  4-class accuracy : {acc4:.4f}  (95% CI: [{ci_lo:.4f}, {ci_hi:.4f}])")
138	    print(f"  3-class accuracy : {acc3:.4f}  (d1-d3 only)")
139	    print(f"  MAE              : {mae:.4f}")
140	    print(f"  Per-class recall : {dict(zip([f'd{d}' for d in DEPTH_LABELS], [round(r,4) for r in per_class_recall]))}")
141	    if pair_aucs:
142	        print(f"  Pairwise AUC     : {pair_aucs}")
143	    print(f"\n  Confusion matrix:")
144	    print(f"  {'':>8s}", " ".join(f"pred-{d}" for d in DEPTH_LABELS))
145	    for i, d in enumerate(DEPTH_LABELS):
146	        print(f"  true-{d}  ", " ".join(f"{cm[i,j]:6d}" for j in range(NUM_DEPTHS)))
147	
148	    cr = classification_report(
149	        y_true, y_pred,
150	        target_names=[f"depth-{d}" for d in DEPTH_LABELS],
151	        zero_division=0,
152	    )
153	    print(f"\n{cr}")
154	
155	    return {
156	        "method": name,
157	        "acc_4class": round(acc4, 4),
158	        "acc_4class_ci": [round(ci_lo, 4), round(ci_hi, 4)],
159	        "acc_3class": round(acc3, 4),
160	        "mae": round(mae, 4),
161	        "per_class_recall": {f"d{d}": round(r, 4) for d, r in zip(DEPTH_LABELS, per_class_recall)},
162	        "pairwise_auc": pair_aucs,
163	    }
164	
165	
166	# ═══════════════════════════════════════════════════════════════════════
167	#  Baseline 1: PPL Regression
168	# ═══════════════════════════════════════════════════════════════════════
169	
170	class PPLRegressionBaseline:
171	    """
172	    Linear regression → round to nearest depth.
173	
174	    Single-feature mode: depth = a * mean_ppl + b
175	    Multi-feature mode:  depth = X @ w + b  (19-dim OLS)
176	
177	    Simplest possible baseline. If mean_ppl alone suffices, complex models are
178	    unnecessary.
179	    """
180	
181	    def __init__(self, mode="multi"):
182	        self.mode = mode  # "single" or "multi"
183	        self.scaler = StandardScaler()
184	        self.model = LinearRegression()
185	
186	    def _select(self, X):
187	        if self.mode == "single":
188	            idx = FEATURE_NAMES.index("mean_ppl")
189	            return X[:, idx:idx+1]
190	        return X
191	
192	    def fit(self, X_train, y_train):
193	        Xs = self._select(X_train)
194	        Xs = self.scaler.fit_transform(Xs)
195	        self.model.fit(Xs, y_train.astype(np.float64))
196	
197	    def predict(self, X_test):
198	        Xs = self._select(X_test)
199	        Xs = self.scaler.transform(Xs)
200	        raw = self.model.predict(Xs)
201	        return np.clip(np.round(raw).astype(int), 0, NUM_DEPTHS - 1)
202	
203	    def predict_proba(self, X_test):
204	        preds = self.predict(X_test)
205	        prob = np.zeros((len(preds), NUM_DEPTHS))
206	        for i, p in enumerate(preds):
207	            prob[i, p] = 1.0
208	        return prob
209	
210	
211	# ═══════════════════════════════════════════════════════════════════════
212	#  Baseline 2: Cross-Entropy MLP (DCOL ablation)
213	# ═══════════════════════════════════════════════════════════════════════
214	
215	class _CEMLP(nn.Module):
216	    """19 → 128 → 64 → 4  with ReLU + dropout. Same architecture as DCOL's
217	    feature head, but trained with CE loss only (no contrastive loss)."""
218	
219	    def __init__(self, input_dim=NUM_FEATURES, hidden1=128, hidden2=64,
220	                 num_classes=NUM_DEPTHS, dropout=0.3):
221	        super().__init__()
222	        self.net = nn.Sequential(
223	            nn.Linear(input_dim, hidden1),
224	            nn.ReLU(),
225	            nn.Dropout(dropout),
226	            nn.Linear(hidden1, hidden2),
227	            nn.ReLU(),
228	            nn.Dropout(dropout),
229	            nn.Linear(hidden2, num_classes),
230	        )
231	
232	    def forward(self, x):
233	        return self.net(x)
234	
235	
236	class CEClassificationBaseline:
237	    """
238	    Standard multi-class MLP with cross-entropy loss.
239	
240	    Architecture identical to DCOL's feature classifier head (19→128→64→4)
241	    but uses only CE loss — no contrastive learning.
242	    This is the key ablation: if CE-MLP matches DCOL, the contrastive loss
243	    adds no value.
244	    """
245	
246	    def __init__(self, lr=1e-3, epochs=100, batch_size=256, patience=10,
247	                 device=None, seed=42):
248	        self.lr = lr
249	        self.epochs = epochs
250	        self.batch_size = batch_size
251	        self.patience = patience
252	        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
253	        self.seed = seed
254	        self.scaler = StandardScaler()
255	        self.model = None
256	
257	    def fit(self, X_train, y_train, X_val=None, y_val=None):
258	        torch.manual_seed(self.seed)
259	        np.random.seed(self.seed)
260	
261	        X_s = self.scaler.fit_transform(X_train).astype(np.float32)
262	        Xt = torch.tensor(X_s, device=self.device)
263	        yt = torch.tensor(y_train, dtype=torch.long, device=self.device)
264	        ds = TensorDataset(Xt, yt)
265	        loader = DataLoader(ds, batch_size=self.batch_size, shuffle=True)
266	
267	        self.model = _CEMLP().to(self.device)
268	        optimizer = optim.Adam(self.model.parameters(), lr=self.lr, weight_decay=1e-4)
269	        criterion = nn.CrossEntropyLoss()
270	
271	        best_loss = float("inf")
272	        wait = 0
273	        best_state = None
274	
275	        has_val = X_val is not None and y_val is not None
276	        if has_val:
277	            Xv = torch.tensor(self.scaler.transform(X_val).astype(np.float32),
278	                              device=self.device)
279	            yv = torch.tensor(y_val, dtype=torch.long, device=self.device)
280	
281	        for epoch in range(self.epochs):
282	            self.model.train()
283	            epoch_loss = 0.0
284	            for xb, yb in loader:
285	                optimizer.zero_grad()
286	                logits = self.model(xb)
287	                loss = criterion(logits, yb)
288	                loss.backward()
289	                optimizer.step()
290	                epoch_loss += loss.item() * len(xb)
291	            epoch_loss /= len(ds)
292	
293	            if has_val:
294	                self.model.eval()
295	                with torch.no_grad():
296	                    val_logits = self.model(Xv)
297	                    val_loss = criterion(val_logits, yv).item()
298	            else:
299	                val_loss = epoch_loss
300	
301	            if val_loss < best_loss - 1e-4:
302	                best_loss = val_loss
303	                best_state = {k: v.clone() for k, v in self.model.state_dict().items()}
304	                wait = 0
305	            else:
306	                wait += 1
307	                if wait >= self.patience:
308	                    break
309	
310	        if best_state is not None:
311	            self.model.load_state_dict(best_state)
312	
313	    def predict(self, X_test):
314	        self.model.eval()
315	        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),
316	                           device=self.device)
317	        with torch.no_grad():
318	            logits = self.model(X_s)
319	        return logits.argmax(dim=-1).cpu().numpy()
320	
321	    def predict_proba(self, X_test):
322	        self.model.eval()
323	        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),
324	                           device=self.device)
325	        with torch.no_grad():
326	            logits = self.model(X_s)
327	            probs = torch.softmax(logits, dim=-1)
328	        return probs.cpu().numpy()
329	
330	
331	# ═══════════════════════════════════════════════════════════════════════
332	#  Baseline 3: CORAL Ordinal Regression
333	# ═══════════════════════════════════════════════════════════════════════
334	
335	class _CORALNet(nn.Module):
336	    """
337	    CORAL ordinal regression (Cao et al., 2020, "Rank consistent ordinal
338	    regression for neural networks with consistent confidence sets").
339	
340	    Architecture: 19 → 128 → 64 → shared representation, then K-1 = 3
341	    independent sigmoid heads.
342	
343	    Each head k answers: P(depth > k).
344	    Prediction: depth = sum_k I[P(depth > k) > 0.5].
345	
346	    Loss (rank-consistent):
347	        L = sum_{k=0}^{K-2} BCE(sigmoid(w_k^T h + b_k), I[y > k])
348	
349	    Weight sharing across heads ensures rank consistency: predictions are
350	    monotonically decreasing in threshold order.
351	    """
352	
353	    def __init__(self, input_dim=NUM_FEATURES, hidden1=128, hidden2=64,
354	                 num_classes=NUM_DEPTHS, dropout=0.3):
355	        super().__init__()
356	        self.num_classes = num_classes
357	        self.backbone = nn.Sequential(
358	            nn.Linear(input_dim, hidden1),
359	            nn.ReLU(),
360	            nn.Dropout(dropout),
361	            nn.Linear(hidden1, hidden2),
362	            nn.ReLU(),
363	            nn.Dropout(dropout),
364	        )
365	        # K-1 independent binary heads (shared backbone, separate bias)
366	        self.fc = nn.Linear(hidden2, 1, bias=False)
367	        self.biases = nn.Parameter(torch.zeros(num_classes - 1))
368	
369	    def forward(self, x):
370	        h = self.backbone(x)             # [B, 64]
371	        logit_base = self.fc(h)          # [B, 1]
372	        # broadcast: [B, K-1]
373	        logits = logit_base + self.biases # each head shares weight, different bias
374	        return logits
375	
376	
377	class CORALBaseline:
378	    """
379	    CORAL ordinal regression for depth estimation.
380	
381	    Ref: Cao, Mirjalili & Raschka (2020). "Rank consistent ordinal regression
382	    for neural networks with consistent confidence sets." Pattern Recognition.
383	
384	    Exploits ordinal structure: depth 0 < 1 < 2 < 3.
385	    Alternative to DCOL's contrastive approach for leveraging label ordering.
386	    """
387	
388	    def __init__(self, lr=1e-3, epochs=100, batch_size=256, patience=10,
389	                 device=None, seed=42):
390	        self.lr = lr
391	        self.epochs = epochs
392	        self.batch_size = batch_size
393	        self.patience = patience
394	        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
395	        self.seed = seed
396	        self.scaler = StandardScaler()
397	        self.model = None
398	
399	    @staticmethod
400	    def _encode_ordinal(y, num_classes):
401	        """Convert class labels to K-1 binary ordinal targets.
402	        y=2, K=4 → [1, 1, 0]  (depth > 0? yes, depth > 1? yes, depth > 2? no)
403	        """
404	        n = len(y)
405	        targets = np.zeros((n, num_classes - 1), dtype=np.float32)
406	        for k in range(num_classes - 1):
407	            targets[:, k] = (y > k).astype(np.float32)
408	        return targets
409	
410	    def fit(self, X_train, y_train, X_val=None, y_val=None):
411	        torch.manual_seed(self.seed)
412	        np.random.seed(self.seed)
413	
414	        X_s = self.scaler.fit_transform(X_train).astype(np.float32)
415	        ord_targets = self._encode_ordinal(y_train, NUM_DEPTHS)
416	
417	        Xt = torch.tensor(X_s, device=self.device)
418	        ot = torch.tensor(ord_targets, device=self.device)
419	        ds = TensorDataset(Xt, ot)
420	        loader = DataLoader(ds, batch_size=self.batch_size, shuffle=True)
421	
422	        self.model = _CORALNet().to(self.device)
423	        optimizer = optim.Adam(self.model.parameters(), lr=self.lr, weight_decay=1e-4)
424	        criterion = nn.BCEWithLogitsLoss()
425	
426	        best_loss = float("inf")
427	        wait = 0
428	        best_state = None
429	
430	        has_val = X_val is not None and y_val is not None
431	        if has_val:
432	            Xv = torch.tensor(self.scaler.transform(X_val).astype(np.float32),
433	                              device=self.device)
434	            ov = torch.tensor(self._encode_ordinal(y_val, NUM_DEPTHS),
435	                              device=self.device)
436	
437	        for epoch in range(self.epochs):
438	            self.model.train()
439	            epoch_loss = 0.0
440	            for xb, ob in loader:
441	                optimizer.zero_grad()
442	                logits = self.model(xb)
443	                loss = criterion(logits, ob)
444	                loss.backward()
445	                optimizer.step()
446	                epoch_loss += loss.item() * len(xb)
447	            epoch_loss /= len(ds)
448	
449	            if has_val:
450	                self.model.eval()
451	                with torch.no_grad():
452	                    val_logits = self.model(Xv)
453	                    val_loss = criterion(val_logits, ov).item()
454	            else:
455	                val_loss = epoch_loss
456	
457	            if val_loss < best_loss - 1e-4:
458	                best_loss = val_loss
459	                best_state = {k: v.clone() for k, v in self.model.state_dict().items()}
460	                wait = 0
461	            else:
462	                wait += 1
463	                if wait >= self.patience:
464	                    break
465	
466	        if best_state is not None:
467	            self.model.load_state_dict(best_state)
468	
469	    def predict(self, X_test):
470	        self.model.eval()
471	        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),
472	                           device=self.device)
473	        with torch.no_grad():
474	            logits = self.model(X_s)
475	            probs = torch.sigmoid(logits)  # [B, K-1], P(depth > k)
476	        # depth = number of thresholds exceeded
477	        preds = (probs > 0.5).sum(dim=-1).cpu().numpy().astype(int)
478	        return preds
479	
480	    def predict_proba(self, X_test):
481	        """Convert cumulative probabilities to per-class probabilities.
482	        P(depth=k) = P(depth>k-1) - P(depth>k), with boundary conditions.
483	        """
484	        self.model.eval()
485	        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),
486	                           device=self.device)
487	        with torch.no_grad():
488	            logits = self.model(X_s)
489	            cum_probs = torch.sigmoid(logits).cpu().numpy()  # [B, K-1]
490	
491	        n = len(X_test)
492	        probs = np.zeros((n, NUM_DEPTHS))
493	        # P(depth=0) = 1 - P(depth>0)
494	        probs[:, 0] = 1.0 - cum_probs[:, 0]
495	        # P(depth=k) = P(depth>k-1) - P(depth>k) for k=1..K-2
496	        for k in range(1, NUM_DEPTHS - 1):
497	            probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]
498	        # P(depth=K-1) = P(depth>K-2)
499	        probs[:, NUM_DEPTHS - 1] = cum_probs[:, NUM_DEPTHS - 2]
500	        probs = np.clip(probs, 0, 1)
501	        row_sums = probs.sum(axis=1, keepdims=True)
502	        probs = probs / np.where(row_sums > 0, row_sums, 1.0)
503	        return probs
504	
505	
506	# ═══════════════════════════════════════════════════════════════════════
507	#  Baseline 4: DivEye (Surprisal Diversity + XGBoost)
508	# ═══════════════════════════════════════════════════════════════════════
509	
510	# DivEye feature groups mapped to our 19 features:
511	#   Distributional: mean_ppl, var_ppl, skewness_ppl, kurtosis_ppl → matches
512	#                   DivEye's mean/var/skewness/kurtosis of surprisal
513	#   Surprisal:      mean_surprisal, var_surprisal, entropy_of_surprisal
514	#   Lexical diversity: type_token_ratio, hapax_ratio, bigram_entropy, trigram_entropy
515	#   Repetition:     rep_2gram, rep_3gram, rep_4gram
516	#
517	# TODO: DivEye's temporal features (first-order ∆S and second-order ∆²S,
518	#       computed from per-token surprisal sequences) are not available in our
519	#       pre-computed features. Full DivEye reproduction requires raw token-level
520	#       surprisal; these summary statistics are a proxy.
521	
522	DIVEYE_FEATURE_INDICES = [
523	    FEATURE_NAMES.index(f) for f in [
524	        "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
525	        "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
526	        "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
527	        "rep_2gram", "rep_3gram", "rep_4gram",
528	    ]
529	]
530	
531	
532	class DivEyeBaseline:
533	    """
534	    DivEye-style detection adapted for depth estimation.
535	
536	    Ref: Basani, A. R. & Chen, P.-Y. (2026). Diversity Boosts AI-Generated Text Detection. Transactions on Machine Learning Research (TMLR).
537	    GitHub: https://github.com/IBM/diveye
538	
539	    DivEye's insight: human text has higher surprisal diversity (distributional,
540	    first-order temporal ∆S, second-order ∆²S). We adapt this to depth estimation:
541	    deeper recursive generations should have *lower* diversity.
542	
543	    Implementation: XGBoost on surprisal-related feature subset (14 of 19 features).
544	    Full DivEye also uses first/second-order temporal surprisal features from raw
545	    token sequences — those are not available in our pre-extracted features.
546	    """
547	
548	    def __init__(self, seed=42):
549	        self.seed = seed
550	        self.model = None
551	
552	    def fit(self, X_train, y_train, **kwargs):
553	        try:
554	            from xgboost import XGBClassifier
555	        except ImportError:
556	            print("[ERROR] xgboost not installed. Run: pip install xgboost")
557	            sys.exit(1)
558	
559	        Xd = X_train[:, DIVEYE_FEATURE_INDICES]
560	        self.model = XGBClassifier(
561	            n_estimators=200,
562	            max_depth=6,
563	            learning_rate=0.1,
564	            subsample=0.8,
565	            colsample_bytree=0.8,
566	            random_state=self.seed,
567	            use_label_encoder=False,
568	            eval_metric="mlogloss",
569	            verbosity=0,
570	        )
571	        self.model.fit(Xd, y_train)
572	
573	    def predict(self, X_test):
574	        Xd = X_test[:, DIVEYE_FEATURE_INDICES]
575	        return self.model.predict(Xd)
576	
577	    def predict_proba(self, X_test):
578	        Xd = X_test[:, DIVEYE_FEATURE_INDICES]
579	        probs = self.model.predict_proba(Xd)
580	        # Ensure output is [n, NUM_DEPTHS] even if some classes are missing
581	        if probs.shape[1] < NUM_DEPTHS:
582	            full = np.zeros((probs.shape[0], NUM_DEPTHS))
583	            for i, c in enumerate(self.model.classes_):
584	                full[:, c] = probs[:, i]
585	            return full
586	        return probs
587	
588	
589	# ═══════════════════════════════════════════════════════════════════════
590	#  Unified Runner
591	# ═══════════════════════════════════════════════════════════════════════
592	
593	BASELINE_REGISTRY = {
594	    "ppl_reg_single": ("PPL Regression (single: mean_ppl)", lambda: PPLRegressionBaseline(mode="single")),
595	    "ppl_reg":        ("PPL Regression (multi: 19-dim OLS)", lambda: PPLRegressionBaseline(mode="multi")),
596	    "ce_mlp":         ("CE-MLP (DCOL ablation)", None),  # needs args
597	    "coral":          ("CORAL Ordinal Regression", None),
598	    "diveye":         ("DivEye (XGBoost)", lambda: DivEyeBaseline()),
599	}
600	
601	
602	def run_baseline(method, X_train, y_train, X_val, y_val, X_test, y_test, args):
603	    if method == "ppl_reg_single":
604	        bl = PPLRegressionBaseline(mode="single")
605	        bl.fit(X_train, y_train)
606	    elif method == "ppl_reg":
607	        bl = PPLRegressionBaseline(mode="multi")
608	        bl.fit(X_train, y_train)
609	    elif method == "ce_mlp":
610	        bl = CEClassificationBaseline(
611	            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,
612	            patience=args.patience, seed=args.seed,
613	        )
614	        bl.fit(X_train, y_train, X_val, y_val)
615	    elif method == "coral":
616	        bl = CORALBaseline(
617	            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,
618	            patience=args.patience, seed=args.seed,
619	        )
620	        bl.fit(X_train, y_train, X_val, y_val)
621	    elif method == "diveye":
622	        bl = DivEyeBaseline(seed=args.seed)
623	        bl.fit(X_train, y_train)
624	    else:
625	        print(f"Unknown method: {method}")
626	        return None
627	
628	    y_pred = bl.predict(X_test)
629	    y_prob = bl.predict_proba(X_test)
630	    name = BASELINE_REGISTRY.get(method, (method, None))[0]
631	    return evaluate(name, y_test, y_pred, y_prob)
632	
633	
634	def parse_args():
635	    p = argparse.ArgumentParser(description="Baseline battery for depth estimation.")
636	    p.add_argument("--method", default="all",
637	                   choices=["ppl_reg_single", "ppl_reg", "ce_mlp", "coral", "diveye", "all"])
638	    p.add_argument("--features_path", default="data/features_all.jsonl")
639	    p.add_argument("--output_dir", default="results/baselines/")
640	    p.add_argument("--seed", type=int, default=42)
641	    p.add_argument("--test_size", type=float, default=0.15)
642	    p.add_argument("--val_size", type=float, default=0.15)
643	    p.add_argument("--epochs", type=int, default=100)
644	    p.add_argument("--batch_size", type=int, default=256)
645	    p.add_argument("--lr", type=float, default=1e-3)
646	    p.add_argument("--patience", type=int, default=10)
647	    return p.parse_args()
648	
649	
650	def main():
651	    args = parse_args()
652	    print(f"Loading features from {args.features_path} ...")
653	    X, y = load_features(args.features_path)
654	    print(f"  {X.shape[0]} samples, {X.shape[1]} features")
655	    print(f"  Depth distribution: {dict(Counter(y))}")
656	
657	    X_train, y_train, X_val, y_val, X_test, y_test = prepare_splits(
658	        X, y, test_size=args.test_size, val_size=args.val_size, seed=args.seed
659	    )
660	    print(f"  Train: {len(y_train)}, Val: {len(y_val)}, Test: {len(y_test)}")
661	
662	    methods = list(BASELINE_REGISTRY.keys()) if args.method == "all" else [args.method]
663	    all_results = {}
664	
665	    for m in methods:
666	        result = run_baseline(m, X_train, y_train, X_val, y_val, X_test, y_test, args)
667	        if result is not None:
668	            all_results[m] = result
669	
670	    # Summary table
671	    if len(all_results) > 1:
672	        print(f"\n{'='*60}")
673	        print(f"  SUMMARY")
674	        print(f"{'='*60}")
675	        print(f"  {'Method':<35s} {'4-cls':>6s} {'3-cls':>6s} {'MAE':>6s}")
676	        print(f"  {'-'*35} {'-'*6} {'-'*6} {'-'*6}")
677	        for m, r in all_results.items():
678	            print(f"  {r['method']:<35s} {r['acc_4class']:6.4f} {r['acc_3class']:6.4f} {r['mae']:6.4f}")
679	        # Reference: RF MVP
680	        print(f"  {'(ref) RF MVP':<35s} {'0.7815':>6s} {'—':>6s} {'—':>6s}")
681	
682	    os.makedirs(args.output_dir, exist_ok=True)
683	    out_path = os.path.join(args.output_dir, "baseline_results.json")
684	    with open(out_path, "w") as f:
685	        json.dump(all_results, f, indent=2, default=str)
686	    print(f"\nResults saved to {out_path}")
687	
688	
689	if __name__ == "__main__":
690	    main()
691	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "ca3b614d-d4ac-462f-a626-7b0e1a1039a8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/baselines.py",
      "content": "\"\"\"\nBaseline battery for recursive generation depth estimation.\n\nBaselines:\n  1. PPLRegressionBaseline  — OLS regression on mean_ppl (single) or all 19 features (multi)\n  2. CEClassificationBaseline — MLP with cross-entropy loss (DCOL ablation, no contrastive loss)\n  3. CORALBaseline — Ordinal regression with K-1 binary classifiers (Cao et al., 2020)\n  4. DivEyeBaseline — Surprisal diversity features + XGBoost (Basani & Chen, TMLR 2026)\n\nUsage:\n  python src/baselines.py --method ppl_reg --features_path data/features_all.jsonl\n  python src/baselines.py --method ce_mlp  --features_path data/features_all.jsonl --epochs 50\n  python src/baselines.py --method coral   --features_path data/features_all.jsonl --epochs 50\n  python src/baselines.py --method diveye  --features_path data/features_all.jsonl\n  python src/baselines.py --method all     --features_path data/features_all.jsonl --epochs 50\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport sys\nimport numpy as np\nfrom collections import Counter\n\nimport torch\nimport torch.nn as nn\nimport torch.optim as optim\nfrom torch.utils.data import DataLoader, TensorDataset\n\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.metrics import (\n    accuracy_score, confusion_matrix, classification_report, roc_auc_score,\n)\n\n# ── Feature schema (must match extract_features.py / dcol_dataset.py) ──\n\nFEATURE_NAMES = [\n    \"mean_ppl\", \"var_ppl\", \"skewness_ppl\", \"kurtosis_ppl\",\n    \"p10_ppl\", \"p25_ppl\", \"p50_ppl\", \"p75_ppl\", \"p90_ppl\",\n    \"mean_surprisal\", \"var_surprisal\", \"entropy_of_surprisal\",\n    \"type_token_ratio\", \"hapax_ratio\", \"bigram_entropy\", \"trigram_entropy\",\n    \"rep_2gram\", \"rep_3gram\", \"rep_4gram\",\n]\nNUM_FEATURES = len(FEATURE_NAMES)\nNUM_DEPTHS = 4\nDEPTH_LABELS = list(range(NUM_DEPTHS))\n\n# ── Data loading ──\n\ndef load_features(path):\n    \"\"\"Load JSONL features file → (X [n, 19], y [n]).\"\"\"\n    records = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                records.append(json.loads(line))\n    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)\n    y = np.array([r[\"depth\"] for r in records], dtype=np.int64)\n    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)\n    return X, y\n\n\ndef prepare_splits(X, y, test_size=0.15, val_size=0.15, seed=42):\n    idx = np.arange(len(y))\n    train_val_idx, test_idx = train_test_split(\n        idx, test_size=test_size, stratify=y, random_state=seed\n    )\n    rel_val = val_size / (1 - test_size)\n    train_idx, val_idx = train_test_split(\n        train_val_idx, test_size=rel_val,\n        stratify=y[train_val_idx], random_state=seed\n    )\n    return (\n        X[train_idx], y[train_idx],\n        X[val_idx], y[val_idx],\n        X[test_idx], y[test_idx],\n    )\n\n# ── Evaluation metrics ──\n\ndef pairwise_auc(y_true, y_prob, d1, d2):\n    mask = np.isin(y_true, [d1, d2])\n    if mask.sum() < 2:\n        return None\n    yt = (y_true[mask] == d2).astype(int)\n    if len(np.unique(yt)) < 2:\n        return None\n    yp = y_prob[mask, d2]\n    return float(roc_auc_score(yt, yp))\n\n\ndef compute_all_pairwise_auc(y_true, y_prob):\n    result = {}\n    for i, d1 in enumerate(DEPTH_LABELS):\n        for d2 in DEPTH_LABELS[i + 1:]:\n            auc = pairwise_auc(y_true, y_prob, d1, d2)\n            result[f\"d{d1}_vs_d{d2}\"] = round(auc, 4) if auc is not None else None\n    return result\n\n\ndef bootstrap_ci(y_true, y_pred, metric_fn=accuracy_score, n_boot=1000, seed=42):\n    rng = np.random.RandomState(seed)\n    scores = []\n    n = len(y_true)\n    for _ in range(n_boot):\n        idx = rng.choice(n, n, replace=True)\n        scores.append(metric_fn(y_true[idx], y_pred[idx]))\n    lo = float(np.percentile(scores, 2.5))\n    hi = float(np.percentile(scores, 97.5))\n    return lo, hi\n\n\ndef evaluate(name, y_true, y_pred, y_prob=None):\n    \"\"\"Print and return evaluation metrics.\"\"\"\n    acc4 = accuracy_score(y_true, y_pred)\n    ci_lo, ci_hi = bootstrap_ci(y_true, y_pred)\n\n    # 3-class accuracy (depth 1-3 only)\n    mask_13 = y_true >= 1\n    acc3 = accuracy_score(y_true[mask_13], y_pred[mask_13]) if mask_13.sum() > 0 else 0.0\n\n    mae = float(np.mean(np.abs(y_true - y_pred)))\n\n    cm = confusion_matrix(y_true, y_pred, labels=DEPTH_LABELS)\n    per_class_recall = cm.diagonal() / cm.sum(axis=1).clip(min=1)\n\n    pair_aucs = {}\n    if y_prob is not None:\n        pair_aucs = compute_all_pairwise_auc(y_true, y_prob)\n\n    print(f\"\\n{'='*60}\")\n    print(f\"  {name}\")\n    print(f\"{'='*60}\")\n    print(f\"  4-class accuracy : {acc4:.4f}  (95% CI: [{ci_lo:.4f}, {ci_hi:.4f}])\")\n    print(f\"  3-class accuracy : {acc3:.4f}  (d1-d3 only)\")\n    print(f\"  MAE              : {mae:.4f}\")\n    print(f\"  Per-class recall : {dict(zip([f'd{d}' for d in DEPTH_LABELS], [round(r,4) for r in per_class_recall]))}\")\n    if pair_aucs:\n        print(f\"  Pairwise AUC     : {pair_aucs}\")\n    print(f\"\\n  Confusion matrix:\")\n    print(f\"  {'':>8s}\", \" \".join(f\"pred-{d}\" for d in DEPTH_LABELS))\n    for i, d in enumerate(DEPTH_LABELS):\n        print(f\"  true-{d}  \", \" \".join(f\"{cm[i,j]:6d}\" for j in range(NUM_DEPTHS)))\n\n    cr = classification_report(\n        y_true, y_pred,\n        target_names=[f\"depth-{d}\" for d in DEPTH_LABELS],\n        zero_division=0,\n    )\n    print(f\"\\n{cr}\")\n\n    return {\n        \"method\": name,\n        \"acc_4class\": round(acc4, 4),\n        \"acc_4class_ci\": [round(ci_lo, 4), round(ci_hi, 4)],\n        \"acc_3class\": round(acc3, 4),\n        \"mae\": round(mae, 4),\n        \"per_class_recall\": {f\"d{d}\": round(r, 4) for d, r in zip(DEPTH_LABELS, per_class_recall)},\n        \"pairwise_auc\": pair_aucs,\n    }\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  Baseline 1: PPL Regression\n# ═══════════════════════════════════════════════════════════════════════\n\nclass PPLRegressionBaseline:\n    \"\"\"\n    Linear regression → round to nearest depth.\n\n    Single-feature mode: depth = a * mean_ppl + b\n    Multi-feature mode:  depth = X @ w + b  (19-dim OLS)\n\n    Simplest possible baseline. If mean_ppl alone suffices, complex models are\n    unnecessary.\n    \"\"\"\n\n    def __init__(self, mode=\"multi\"):\n        self.mode = mode  # \"single\" or \"multi\"\n        self.scaler = StandardScaler()\n        self.model = LinearRegression()\n\n    def _select(self, X):\n        if self.mode == \"single\":\n            idx = FEATURE_NAMES.index(\"mean_ppl\")\n            return X[:, idx:idx+1]\n        return X\n\n    def fit(self, X_train, y_train):\n        Xs = self._select(X_train)\n        Xs = self.scaler.fit_transform(Xs)\n        self.model.fit(Xs, y_train.astype(np.float64))\n\n    def predict(self, X_test):\n        Xs = self._select(X_test)\n        Xs = self.scaler.transform(Xs)\n        raw = self.model.predict(Xs)\n        return np.clip(np.round(raw).astype(int), 0, NUM_DEPTHS - 1)\n\n    def predict_proba(self, X_test):\n        preds = self.predict(X_test)\n        prob = np.zeros((len(preds), NUM_DEPTHS))\n        for i, p in enumerate(preds):\n            prob[i, p] = 1.0\n        return prob\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  Baseline 2: Cross-Entropy MLP (DCOL ablation)\n# ═══════════════════════════════════════════════════════════════════════\n\nclass _CEMLP(nn.Module):\n    \"\"\"19 → 128 → 64 → 4  with ReLU + dropout. Same architecture as DCOL's\n    feature head, but trained with CE loss only (no contrastive loss).\"\"\"\n\n    def __init__(self, input_dim=NUM_FEATURES, hidden1=128, hidden2=64,\n                 num_classes=NUM_DEPTHS, dropout=0.3):\n        super().__init__()\n        self.net = nn.Sequential(\n            nn.Linear(input_dim, hidden1),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n            nn.Linear(hidden1, hidden2),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n            nn.Linear(hidden2, num_classes),\n        )\n\n    def forward(self, x):\n        return self.net(x)\n\n\nclass CEClassificationBaseline:\n    \"\"\"\n    Standard multi-class MLP with cross-entropy loss.\n\n    Architecture identical to DCOL's feature classifier head (19→128→64→4)\n    but uses only CE loss — no contrastive learning.\n    This is the key ablation: if CE-MLP matches DCOL, the contrastive loss\n    adds no value.\n    \"\"\"\n\n    def __init__(self, lr=1e-3, epochs=100, batch_size=256, patience=10,\n                 device=None, seed=42):\n        self.lr = lr\n        self.epochs = epochs\n        self.batch_size = batch_size\n        self.patience = patience\n        self.device = device or (\"cuda\" if torch.cuda.is_available() else \"cpu\")\n        self.seed = seed\n        self.scaler = StandardScaler()\n        self.model = None\n\n    def fit(self, X_train, y_train, X_val=None, y_val=None):\n        torch.manual_seed(self.seed)\n        np.random.seed(self.seed)\n\n        X_s = self.scaler.fit_transform(X_train).astype(np.float32)\n        Xt = torch.tensor(X_s, device=self.device)\n        yt = torch.tensor(y_train, dtype=torch.long, device=self.device)\n        ds = TensorDataset(Xt, yt)\n        loader = DataLoader(ds, batch_size=self.batch_size, shuffle=True)\n\n        self.model = _CEMLP().to(self.device)\n        optimizer = optim.Adam(self.model.parameters(), lr=self.lr, weight_decay=1e-4)\n        criterion = nn.CrossEntropyLoss()\n\n        best_loss = float(\"inf\")\n        wait = 0\n        best_state = None\n\n        has_val = X_val is not None and y_val is not None\n        if has_val:\n            Xv = torch.tensor(self.scaler.transform(X_val).astype(np.float32),\n                              device=self.device)\n            yv = torch.tensor(y_val, dtype=torch.long, device=self.device)\n\n        for epoch in range(self.epochs):\n            self.model.train()\n            epoch_loss = 0.0\n            for xb, yb in loader:\n                optimizer.zero_grad()\n                logits = self.model(xb)\n                loss = criterion(logits, yb)\n                loss.backward()\n                optimizer.step()\n                epoch_loss += loss.item() * len(xb)\n            epoch_loss /= len(ds)\n\n            if has_val:\n                self.model.eval()\n                with torch.no_grad():\n                    val_logits = self.model(Xv)\n                    val_loss = criterion(val_logits, yv).item()\n            else:\n                val_loss = epoch_loss\n\n            if val_loss < best_loss - 1e-4:\n                best_loss = val_loss\n                best_state = {k: v.clone() for k, v in self.model.state_dict().items()}\n                wait = 0\n            else:\n                wait += 1\n                if wait >= self.patience:\n                    break\n\n        if best_state is not None:\n            self.model.load_state_dict(best_state)\n\n    def predict(self, X_test):\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n        return logits.argmax(dim=-1).cpu().numpy()\n\n    def predict_proba(self, X_test):\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n            probs = torch.softmax(logits, dim=-1)\n        return probs.cpu().numpy()\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  Baseline 3: CORAL Ordinal Regression\n# ═══════════════════════════════════════════════════════════════════════\n\nclass _CORALNet(nn.Module):\n    \"\"\"\n    CORAL ordinal regression (Cao et al., 2020, \"Rank consistent ordinal\n    regression for neural networks with consistent confidence sets\").\n\n    Architecture: 19 → 128 → 64 → shared representation, then K-1 = 3\n    independent sigmoid heads.\n\n    Each head k answers: P(depth > k).\n    Prediction: depth = sum_k I[P(depth > k) > 0.5].\n\n    Loss (rank-consistent):\n        L = sum_{k=0}^{K-2} BCE(sigmoid(w_k^T h + b_k), I[y > k])\n\n    Weight sharing across heads ensures rank consistency: predictions are\n    monotonically decreasing in threshold order.\n    \"\"\"\n\n    def __init__(self, input_dim=NUM_FEATURES, hidden1=128, hidden2=64,\n                 num_classes=NUM_DEPTHS, dropout=0.3):\n        super().__init__()\n        self.num_classes = num_classes\n        self.backbone = nn.Sequential(\n            nn.Linear(input_dim, hidden1),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n            nn.Linear(hidden1, hidden2),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n        )\n        # K-1 independent binary heads (shared backbone, separate bias)\n        self.fc = nn.Linear(hidden2, 1, bias=False)\n        self.biases = nn.Parameter(torch.zeros(num_classes - 1))\n\n    def forward(self, x):\n        h = self.backbone(x)             # [B, 64]\n        logit_base = self.fc(h)          # [B, 1]\n        # broadcast: [B, K-1]\n        logits = logit_base + self.biases # each head shares weight, different bias\n        return logits\n\n\nclass CORALBaseline:\n    \"\"\"\n    CORAL ordinal regression for depth estimation.\n\n    Ref: Cao, Mirjalili & Raschka (2020). \"Rank consistent ordinal regression\n    for neural networks with consistent confidence sets.\" Pattern Recognition.\n\n    Exploits ordinal structure: depth 0 < 1 < 2 < 3.\n    Alternative to DCOL's contrastive approach for leveraging label ordering.\n    \"\"\"\n\n    def __init__(self, lr=1e-3, epochs=100, batch_size=256, patience=10,\n                 device=None, seed=42):\n        self.lr = lr\n        self.epochs = epochs\n        self.batch_size = batch_size\n        self.patience = patience\n        self.device = device or (\"cuda\" if torch.cuda.is_available() else \"cpu\")\n        self.seed = seed\n        self.scaler = StandardScaler()\n        self.model = None\n\n    @staticmethod\n    def _encode_ordinal(y, num_classes):\n        \"\"\"Convert class labels to K-1 binary ordinal targets.\n        y=2, K=4 → [1, 1, 0]  (depth > 0? yes, depth > 1? yes, depth > 2? no)\n        \"\"\"\n        n = len(y)\n        targets = np.zeros((n, num_classes - 1), dtype=np.float32)\n        for k in range(num_classes - 1):\n            targets[:, k] = (y > k).astype(np.float32)\n        return targets\n\n    def fit(self, X_train, y_train, X_val=None, y_val=None):\n        torch.manual_seed(self.seed)\n        np.random.seed(self.seed)\n\n        X_s = self.scaler.fit_transform(X_train).astype(np.float32)\n        ord_targets = self._encode_ordinal(y_train, NUM_DEPTHS)\n\n        Xt = torch.tensor(X_s, device=self.device)\n        ot = torch.tensor(ord_targets, device=self.device)\n        ds = TensorDataset(Xt, ot)\n        loader = DataLoader(ds, batch_size=self.batch_size, shuffle=True)\n\n        self.model = _CORALNet().to(self.device)\n        optimizer = optim.Adam(self.model.parameters(), lr=self.lr, weight_decay=1e-4)\n        criterion = nn.BCEWithLogitsLoss()\n\n        best_loss = float(\"inf\")\n        wait = 0\n        best_state = None\n\n        has_val = X_val is not None and y_val is not None\n        if has_val:\n            Xv = torch.tensor(self.scaler.transform(X_val).astype(np.float32),\n                              device=self.device)\n            ov = torch.tensor(self._encode_ordinal(y_val, NUM_DEPTHS),\n                              device=self.device)\n\n        for epoch in range(self.epochs):\n            self.model.train()\n            epoch_loss = 0.0\n            for xb, ob in loader:\n                optimizer.zero_grad()\n                logits = self.model(xb)\n                loss = criterion(logits, ob)\n                loss.backward()\n                optimizer.step()\n                epoch_loss += loss.item() * len(xb)\n            epoch_loss /= len(ds)\n\n            if has_val:\n                self.model.eval()\n                with torch.no_grad():\n                    val_logits = self.model(Xv)\n                    val_loss = criterion(val_logits, ov).item()\n            else:\n                val_loss = epoch_loss\n\n            if val_loss < best_loss - 1e-4:\n                best_loss = val_loss\n                best_state = {k: v.clone() for k, v in self.model.state_dict().items()}\n                wait = 0\n            else:\n                wait += 1\n                if wait >= self.patience:\n                    break\n\n        if best_state is not None:\n            self.model.load_state_dict(best_state)\n\n    def predict(self, X_test):\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n            probs = torch.sigmoid(logits)  # [B, K-1], P(depth > k)\n        # depth = number of thresholds exceeded\n        preds = (probs > 0.5).sum(dim=-1).cpu().numpy().astype(int)\n        return preds\n\n    def predict_proba(self, X_test):\n        \"\"\"Convert cumulative probabilities to per-class probabilities.\n        P(depth=k) = P(depth>k-1) - P(depth>k), with boundary conditions.\n        \"\"\"\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n            cum_probs = torch.sigmoid(logits).cpu().numpy()  # [B, K-1]\n\n        n = len(X_test)\n        probs = np.zeros((n, NUM_DEPTHS))\n        # P(depth=0) = 1 - P(depth>0)\n        probs[:, 0] = 1.0 - cum_probs[:, 0]\n        # P(depth=k) = P(depth>k-1) - P(depth>k) for k=1..K-2\n        for k in range(1, NUM_DEPTHS - 1):\n            probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]\n        # P(depth=K-1) = P(depth>K-2)\n        probs[:, NUM_DEPTHS - 1] = cum_probs[:, NUM_DEPTHS - 2]\n        probs = np.clip(probs, 0, 1)\n        row_sums = probs.sum(axis=1, keepdims=True)\n        probs = probs / np.where(row_sums > 0, row_sums, 1.0)\n        return probs\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  Baseline 4: DivEye (Surprisal Diversity + XGBoost)\n# ═══════════════════════════════════════════════════════════════════════\n\n# DivEye feature groups mapped to our 19 features:\n#   Distributional: mean_ppl, var_ppl, skewness_ppl, kurtosis_ppl → matches\n#                   DivEye's mean/var/skewness/kurtosis of surprisal\n#   Surprisal:      mean_surprisal, var_surprisal, entropy_of_surprisal\n#   Lexical diversity: type_token_ratio, hapax_ratio, bigram_entropy, trigram_entropy\n#   Repetition:     rep_2gram, rep_3gram, rep_4gram\n#\n# TODO: DivEye's temporal features (first-order ∆S and second-order ∆²S,\n#       computed from per-token surprisal sequences) are not available in our\n#       pre-computed features. Full DivEye reproduction requires raw token-level\n#       surprisal; these summary statistics are a proxy.\n\nDIVEYE_FEATURE_INDICES = [\n    FEATURE_NAMES.index(f) for f in [\n        \"mean_ppl\", \"var_ppl\", \"skewness_ppl\", \"kurtosis_ppl\",\n        \"mean_surprisal\", \"var_surprisal\", \"entropy_of_surprisal\",\n        \"type_token_ratio\", \"hapax_ratio\", \"bigram_entropy\", \"trigram_entropy\",\n        \"rep_2gram\", \"rep_3gram\", \"rep_4gram\",\n    ]\n]\n\n\nclass DivEyeBaseline:\n    \"\"\"\n    DivEye-style detection adapted for depth estimation.\n\n    Ref: Basani, A. R. & Chen, P.-Y. (2026). Diversity Boosts AI-Generated Text Detection. Transactions on Machine Learning Research (TMLR).\n    GitHub: https://github.com/IBM/diveye\n\n    DivEye's insight: human text has higher surprisal diversity (distributional,\n    first-order temporal ∆S, second-order ∆²S). We adapt this to depth estimation:\n    deeper recursive generations should have *lower* diversity.\n\n    Implementation: XGBoost on surprisal-related feature subset (14 of 19 features).\n    Full DivEye also uses first/second-order temporal surprisal features from raw\n    token sequences — those are not available in our pre-extracted features.\n    \"\"\"\n\n    def __init__(self, seed=42):\n        self.seed = seed\n        self.model = None\n\n    def fit(self, X_train, y_train, **kwargs):\n        try:\n            from xgboost import XGBClassifier\n        except ImportError:\n            print(\"[ERROR] xgboost not installed. Run: pip install xgboost\")\n            sys.exit(1)\n\n        Xd = X_train[:, DIVEYE_FEATURE_INDICES]\n        self.model = XGBClassifier(\n            n_estimators=200,\n            max_depth=6,\n            learning_rate=0.1,\n            subsample=0.8,\n            colsample_bytree=0.8,\n            random_state=self.seed,\n            use_label_encoder=False,\n            eval_metric=\"mlogloss\",\n            verbosity=0,\n        )\n        self.model.fit(Xd, y_train)\n\n    def predict(self, X_test):\n        Xd = X_test[:, DIVEYE_FEATURE_INDICES]\n        return self.model.predict(Xd)\n\n    def predict_proba(self, X_test):\n        Xd = X_test[:, DIVEYE_FEATURE_INDICES]\n        probs = self.model.predict_proba(Xd)\n        # Ensure output is [n, NUM_DEPTHS] even if some classes are missing\n        if probs.shape[1] < NUM_DEPTHS:\n            full = np.zeros((probs.shape[0], NUM_DEPTHS))\n            for i, c in enumerate(self.model.classes_):\n                full[:, c] = probs[:, i]\n            return full\n        return probs\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  Unified Runner\n# ═══════════════════════════════════════════════════════════════════════\n\nBASELINE_REGISTRY = {\n    \"ppl_reg_single\": (\"PPL Regression (single: mean_ppl)\", lambda: PPLRegressionBaseline(mode=\"single\")),\n    \"ppl_reg\":        (\"PPL Regression (multi: 19-dim OLS)\", lambda: PPLRegressionBaseline(mode=\"multi\")),\n    \"ce_mlp\":         (\"CE-MLP (DCOL ablation)\", None),  # needs args\n    \"coral\":          (\"CORAL Ordinal Regression\", None),\n    \"diveye\":         (\"DivEye (XGBoost)\", lambda: DivEyeBaseline()),\n}\n\n\ndef run_baseline(method, X_train, y_train, X_val, y_val, X_test, y_test, args):\n    if method == \"ppl_reg_single\":\n        bl = PPLRegressionBaseline(mode=\"single\")\n        bl.fit(X_train, y_train)\n    elif method == \"ppl_reg\":\n        bl = PPLRegressionBaseline(mode=\"multi\")\n        bl.fit(X_train, y_train)\n    elif method == \"ce_mlp\":\n        bl = CEClassificationBaseline(\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\n            patience=args.patience, seed=args.seed,\n        )\n        bl.fit(X_train, y_train, X_val, y_val)\n    elif method == \"coral\":\n        bl = CORALBaseline(\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\n            patience=args.patience, seed=args.seed,\n        )\n        bl.fit(X_train, y_train, X_val, y_val)\n    elif method == \"diveye\":\n        bl = DivEyeBaseline(seed=args.seed)\n        bl.fit(X_train, y_train)\n    else:\n        print(f\"Unknown method: {method}\")\n        return None\n\n    y_pred = bl.predict(X_test)\n    y_prob = bl.predict_proba(X_test)\n    name = BASELINE_REGISTRY.get(method, (method, None))[0]\n    return evaluate(name, y_test, y_pred, y_prob)\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"Baseline battery for depth estimation.\")\n    p.add_argument(\"--method\", default=\"all\",\n                   choices=[\"ppl_reg_single\", \"ppl_reg\", \"ce_mlp\", \"coral\", \"diveye\", \"all\"])\n    p.add_argument(\"--features_path\", default=\"data/features_all.jsonl\")\n    p.add_argument(\"--output_dir\", default=\"results/baselines/\")\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--test_size\", type=float, default=0.15)\n    p.add_argument(\"--val_size\", type=float, default=0.15)\n    p.add_argument(\"--epochs\", type=int, default=100)\n    p.add_argument(\"--batch_size\", type=int, default=256)\n    p.add_argument(\"--lr\", type=float, default=1e-3)\n    p.add_argument(\"--patience\", type=int, default=10)\n    return p.parse_args()\n\n\ndef main():\n    args = parse_args()\n    print(f\"Loading features from {args.features_path} ...\")\n    X, y = load_features(args.features_path)\n    print(f\"  {X.shape[0]} samples, {X.shape[1]} features\")\n    print(f\"  Depth distribution: {dict(Counter(y))}\")\n\n    X_train, y_train, X_val, y_val, X_test, y_test = prepare_splits(\n        X, y, test_size=args.test_size, val_size=args.val_size, seed=args.seed\n    )\n    print(f\"  Train: {len(y_train)}, Val: {len(y_val)}, Test: {len(y_test)}\")\n\n    methods = list(BASELINE_REGISTRY.keys()) if args.method == \"all\" else [args.method]\n    all_results = {}\n\n    for m in methods:\n        result = run_baseline(m, X_train, y_train, X_val, y_val, X_test, y_test, args)\n        if result is not None:\n            all_results[m] = result\n\n    # Summary table\n    if len(all_results) > 1:\n        print(f\"\\n{'='*60}\")\n        print(f\"  SUMMARY\")\n        print(f\"{'='*60}\")\n        print(f\"  {'Method':<35s} {'4-cls':>6s} {'3-cls':>6s} {'MAE':>6s}\")\n        print(f\"  {'-'*35} {'-'*6} {'-'*6} {'-'*6}\")\n        for m, r in all_results.items():\n            print(f\"  {r['method']:<35s} {r['acc_4class']:6.4f} {r['acc_3class']:6.4f} {r['mae']:6.4f}\")\n        # Reference: RF MVP\n        print(f\"  {'(ref) RF MVP':<35s} {'0.7815':>6s} {'—':>6s} {'—':>6s}\")\n\n    os.makedirs(args.output_dir, exist_ok=True)\n    out_path = os.path.join(args.output_dir, \"baseline_results.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(all_results, f, indent=2, default=str)\n    print(f\"\\nResults saved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 691,
      "startLine": 1,
      "totalLines": 691
    }
  }
}
```

</details>

---


### Assistant

_source line 147_

<details><summary>Logged reasoning block</summary>

```text
Now I'll write the updated `artifacts/baselines.py` with all the additions:
1. RF and LR baselines (from server version)
2. Zero-shot LLM baseline (from `scripts/baseline_zeroshot_llm.py`)
3. `--data_path` alias for `--features_path`
4. `--data_dirs` for text-based methods
5. Updated docstring and registry

Let me write the complete file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "f03649c9-3319-4f15-8d64-2c3cdb81e0a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MX62vV4kKN3159kJBN2EuW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10905,
      "cache_read_input_tokens": 70070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10905
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

_source line 148_

Now I'll write the updated `baselines.py` with all 8 baselines including Zero-shot LLM, then deploy to server.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "5ac2c266-6031-4da1-955a-9208211de27d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MX62vV4kKN3159kJBN2EuW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10905,
      "cache_read_input_tokens": 70070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10905
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

_source line 149_

<details open><summary>🔧 Tool call — Write · `toolu_017dQtJUmffR7un8uA3ngsAq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/baselines.py",
  "content": "\"\"\"\nBaseline battery for recursive generation depth estimation.\n\nBaselines (feature-based, 19-dim input):\n  1. PPLRegressionBaseline  -- OLS regression on mean_ppl (single) or all 19 features (multi)\n  2. CEClassificationBaseline -- MLP with cross-entropy loss (DCOL ablation, no contrastive loss)\n  3. CORALBaseline -- Ordinal regression with K-1 binary classifiers (Cao et al., 2020)\n  4. DivEyeBaseline -- Surprisal diversity features + XGBoost (Basani & Chen, TMLR 2026)\n  5. RandomForestBaseline -- sklearn RF on 19-dim features\n  6. LogisticRegressionBaseline -- sklearn LR on 19-dim features\n\nBaselines (text-based, raw text input):\n  7. ZeroShotLLMBaseline -- Prompt an LLM (Claude/OpenAI) to classify depth directly\n\nUsage:\n  python src/baselines.py --method ppl_reg --features_path data/features_all.jsonl\n  python src/baselines.py --method ce_mlp  --features_path data/features_all.jsonl --epochs 50\n  python src/baselines.py --method coral   --features_path data/features_all.jsonl --epochs 50\n  python src/baselines.py --method diveye  --features_path data/features_all.jsonl\n  python src/baselines.py --method rf      --features_path data/features_all.jsonl\n  python src/baselines.py --method lr      --features_path data/features_all.jsonl\n  python src/baselines.py --method zeroshot --data_dirs data/ --provider claude --max_eval_samples 200\n  python src/baselines.py --method all     --features_path data/features_all.jsonl --epochs 50\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport re\nimport sys\nimport time\nimport numpy as np\nfrom collections import Counter\n\nimport torch\nimport torch.nn as nn\nimport torch.optim as optim\nfrom torch.utils.data import DataLoader, TensorDataset\n\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.metrics import (\n    accuracy_score, confusion_matrix, classification_report, roc_auc_score,\n)\n\n# -- Feature schema (must match extract_features.py / dcol_dataset.py) --\n\nFEATURE_NAMES = [\n    \"mean_ppl\", \"var_ppl\", \"skewness_ppl\", \"kurtosis_ppl\",\n    \"p10_ppl\", \"p25_ppl\", \"p50_ppl\", \"p75_ppl\", \"p90_ppl\",\n    \"mean_surprisal\", \"var_surprisal\", \"entropy_of_surprisal\",\n    \"type_token_ratio\", \"hapax_ratio\", \"bigram_entropy\", \"trigram_entropy\",\n    \"rep_2gram\", \"rep_3gram\", \"rep_4gram\",\n]\nNUM_FEATURES = len(FEATURE_NAMES)\nNUM_DEPTHS = 4\nDEPTH_LABELS = list(range(NUM_DEPTHS))\n\n# -- Data loading --\n\ndef load_features(path):\n    \"\"\"Load JSONL features file -> (X [n, 19], y [n]).\"\"\"\n    records = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                records.append(json.loads(line))\n    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)\n    y = np.array([r[\"depth\"] for r in records], dtype=np.int64)\n    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)\n    return X, y\n\n\ndef load_jsonl_texts(data_dirs, max_samples=0, seed=42):\n    \"\"\"Load raw text + depth labels from depth_*.jsonl files across directories.\"\"\"\n    import glob as glob_mod\n    texts, labels = [], []\n    for data_dir in data_dirs:\n        for d in range(NUM_DEPTHS):\n            fpath = os.path.join(data_dir, f\"depth_{d}.jsonl\")\n            if not os.path.exists(fpath):\n                matches = glob_mod.glob(os.path.join(data_dir, f\"*depth_{d}*.jsonl\"))\n                fpath = matches[0] if matches else None\n            if fpath is None or not os.path.exists(fpath):\n                continue\n            with open(fpath) as f:\n                for line in f:\n                    line = line.strip()\n                    if not line:\n                        continue\n                    rec = json.loads(line)\n                    texts.append(rec[\"text\"])\n                    labels.append(rec.get(\"depth\", d))\n    labels = np.array(labels, dtype=np.int64)\n    if max_samples > 0 and len(texts) > max_samples:\n        rng = np.random.RandomState(seed)\n        idx = sorted(rng.choice(len(texts), max_samples, replace=False))\n        texts = [texts[i] for i in idx]\n        labels = labels[idx]\n    print(f\"Loaded {len(texts)} text samples. Depth distribution: {dict(Counter(labels))}\")\n    return texts, labels\n\n\ndef prepare_splits(X, y, test_size=0.15, val_size=0.15, seed=42):\n    idx = np.arange(len(y))\n    train_val_idx, test_idx = train_test_split(\n        idx, test_size=test_size, stratify=y, random_state=seed\n    )\n    rel_val = val_size / (1 - test_size)\n    train_idx, val_idx = train_test_split(\n        train_val_idx, test_size=rel_val,\n        stratify=y[train_val_idx], random_state=seed\n    )\n    return (\n        X[train_idx], y[train_idx],\n        X[val_idx], y[val_idx],\n        X[test_idx], y[test_idx],\n    )\n\n# -- Evaluation metrics --\n\ndef pairwise_auc(y_true, y_prob, d1, d2):\n    mask = np.isin(y_true, [d1, d2])\n    if mask.sum() < 2:\n        return None\n    yt = (y_true[mask] == d2).astype(int)\n    if len(np.unique(yt)) < 2:\n        return None\n    yp = y_prob[mask, d2]\n    return float(roc_auc_score(yt, yp))\n\n\ndef compute_all_pairwise_auc(y_true, y_prob):\n    result = {}\n    for i, d1 in enumerate(DEPTH_LABELS):\n        for d2 in DEPTH_LABELS[i + 1:]:\n            auc = pairwise_auc(y_true, y_prob, d1, d2)\n            result[f\"d{d1}_vs_d{d2}\"] = round(auc, 4) if auc is not None else None\n    return result\n\n\ndef bootstrap_ci(y_true, y_pred, metric_fn=accuracy_score, n_boot=1000, seed=42):\n    rng = np.random.RandomState(seed)\n    scores = []\n    n = len(y_true)\n    for _ in range(n_boot):\n        idx = rng.choice(n, n, replace=True)\n        scores.append(metric_fn(y_true[idx], y_pred[idx]))\n    lo = float(np.percentile(scores, 2.5))\n    hi = float(np.percentile(scores, 97.5))\n    return lo, hi\n\n\ndef evaluate(name, y_true, y_pred, y_prob=None):\n    \"\"\"Print and return evaluation metrics.\"\"\"\n    acc4 = accuracy_score(y_true, y_pred)\n    ci_lo, ci_hi = bootstrap_ci(y_true, y_pred)\n\n    mask_13 = y_true >= 1\n    acc3 = accuracy_score(y_true[mask_13], y_pred[mask_13]) if mask_13.sum() > 0 else 0.0\n\n    mae = float(np.mean(np.abs(y_true - y_pred)))\n\n    cm = confusion_matrix(y_true, y_pred, labels=DEPTH_LABELS)\n    per_class_recall = cm.diagonal() / cm.sum(axis=1).clip(min=1)\n\n    pair_aucs = {}\n    if y_prob is not None:\n        pair_aucs = compute_all_pairwise_auc(y_true, y_prob)\n\n    print(f\"\\n{'='*60}\")\n    print(f\"  {name}\")\n    print(f\"{'='*60}\")\n    print(f\"  4-class accuracy : {acc4:.4f}  (95% CI: [{ci_lo:.4f}, {ci_hi:.4f}])\")\n    print(f\"  3-class accuracy : {acc3:.4f}  (d1-d3 only)\")\n    print(f\"  MAE              : {mae:.4f}\")\n    print(f\"  Per-class recall : {dict(zip([f'd{d}' for d in DEPTH_LABELS], [round(r,4) for r in per_class_recall]))}\")\n    if pair_aucs:\n        print(f\"  Pairwise AUC     : {pair_aucs}\")\n    print(f\"\\n  Confusion matrix:\")\n    print(f\"  {'':>8s}\", \" \".join(f\"pred-{d}\" for d in DEPTH_LABELS))\n    for i, d in enumerate(DEPTH_LABELS):\n        print(f\"  true-{d}  \", \" \".join(f\"{cm[i,j]:6d}\" for j in range(NUM_DEPTHS)))\n\n    cr = classification_report(\n        y_true, y_pred,\n        target_names=[f\"depth-{d}\" for d in DEPTH_LABELS],\n        zero_division=0,\n    )\n    print(f\"\\n{cr}\")\n\n    return {\n        \"method\": name,\n        \"acc_4class\": round(acc4, 4),\n        \"acc_4class_ci\": [round(ci_lo, 4), round(ci_hi, 4)],\n        \"acc_3class\": round(acc3, 4),\n        \"mae\": round(mae, 4),\n        \"per_class_recall\": {f\"d{d}\": round(r, 4) for d, r in zip(DEPTH_LABELS, per_class_recall)},\n        \"pairwise_auc\": pair_aucs,\n    }\n\n\n# ===================================================================\n#  Baseline 1: PPL Regression\n# ===================================================================\n\nclass PPLRegressionBaseline:\n    \"\"\"\n    Linear regression -> round to nearest depth.\n    Single-feature mode: depth = a * mean_ppl + b\n    Multi-feature mode:  depth = X @ w + b  (19-dim OLS)\n    \"\"\"\n\n    def __init__(self, mode=\"multi\"):\n        self.mode = mode\n        self.scaler = StandardScaler()\n        self.model = LinearRegression()\n\n    def _select(self, X):\n        if self.mode == \"single\":\n            idx = FEATURE_NAMES.index(\"mean_ppl\")\n            return X[:, idx:idx+1]\n        return X\n\n    def fit(self, X_train, y_train, **kwargs):\n        Xs = self._select(X_train)\n        Xs = self.scaler.fit_transform(Xs)\n        self.model.fit(Xs, y_train.astype(np.float64))\n\n    def predict(self, X_test):\n        Xs = self._select(X_test)\n        Xs = self.scaler.transform(Xs)\n        raw = self.model.predict(Xs)\n        return np.clip(np.round(raw).astype(int), 0, NUM_DEPTHS - 1)\n\n    def predict_proba(self, X_test):\n        preds = self.predict(X_test)\n        prob = np.zeros((len(preds), NUM_DEPTHS))\n        for i, p in enumerate(preds):\n            prob[i, p] = 1.0\n        return prob\n\n\n# ===================================================================\n#  Baseline 2: Cross-Entropy MLP (DCOL ablation)\n# ===================================================================\n\nclass _CEMLP(nn.Module):\n    \"\"\"19 -> 128 -> 64 -> 4  with ReLU + dropout.\"\"\"\n\n    def __init__(self, input_dim=NUM_FEATURES, hidden1=128, hidden2=64,\n                 num_classes=NUM_DEPTHS, dropout=0.3):\n        super().__init__()\n        self.net = nn.Sequential(\n            nn.Linear(input_dim, hidden1),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n            nn.Linear(hidden1, hidden2),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n            nn.Linear(hidden2, num_classes),\n        )\n\n    def forward(self, x):\n        return self.net(x)\n\n\nclass CEClassificationBaseline:\n    \"\"\"\n    Standard multi-class MLP with cross-entropy loss.\n    Architecture identical to DCOL's feature classifier head (19->128->64->4)\n    but uses only CE loss -- no contrastive learning.\n    Key ablation: if CE-MLP matches DCOL, the contrastive loss adds no value.\n    \"\"\"\n\n    def __init__(self, lr=1e-3, epochs=100, batch_size=256, patience=10,\n                 device=None, seed=42):\n        self.lr = lr\n        self.epochs = epochs\n        self.batch_size = batch_size\n        self.patience = patience\n        self.device = device or (\"cuda\" if torch.cuda.is_available() else \"cpu\")\n        self.seed = seed\n        self.scaler = StandardScaler()\n        self.model = None\n\n    def fit(self, X_train, y_train, X_val=None, y_val=None, **kwargs):\n        torch.manual_seed(self.seed)\n        np.random.seed(self.seed)\n\n        X_s = self.scaler.fit_transform(X_train).astype(np.float32)\n        Xt = torch.tensor(X_s, device=self.device)\n        yt = torch.tensor(y_train, dtype=torch.long, device=self.device)\n        ds = TensorDataset(Xt, yt)\n        loader = DataLoader(ds, batch_size=self.batch_size, shuffle=True)\n\n        self.model = _CEMLP().to(self.device)\n        optimizer = optim.Adam(self.model.parameters(), lr=self.lr, weight_decay=1e-4)\n        criterion = nn.CrossEntropyLoss()\n\n        best_loss = float(\"inf\")\n        wait = 0\n        best_state = None\n\n        has_val = X_val is not None and y_val is not None\n        if has_val:\n            Xv = torch.tensor(self.scaler.transform(X_val).astype(np.float32),\n                              device=self.device)\n            yv = torch.tensor(y_val, dtype=torch.long, device=self.device)\n\n        for epoch in range(self.epochs):\n            self.model.train()\n            epoch_loss = 0.0\n            for xb, yb in loader:\n                optimizer.zero_grad()\n                logits = self.model(xb)\n                loss = criterion(logits, yb)\n                loss.backward()\n                optimizer.step()\n                epoch_loss += loss.item() * len(xb)\n            epoch_loss /= len(ds)\n\n            if has_val:\n                self.model.eval()\n                with torch.no_grad():\n                    val_logits = self.model(Xv)\n                    val_loss = criterion(val_logits, yv).item()\n            else:\n                val_loss = epoch_loss\n\n            if val_loss < best_loss - 1e-4:\n                best_loss = val_loss\n                best_state = {k: v.clone() for k, v in self.model.state_dict().items()}\n                wait = 0\n            else:\n                wait += 1\n                if wait >= self.patience:\n                    break\n\n        if best_state is not None:\n            self.model.load_state_dict(best_state)\n\n    def predict(self, X_test):\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n        return logits.argmax(dim=-1).cpu().numpy()\n\n    def predict_proba(self, X_test):\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n            probs = torch.softmax(logits, dim=-1)\n        return probs.cpu().numpy()\n\n\n# ===================================================================\n#  Baseline 3: CORAL Ordinal Regression\n# ===================================================================\n\nclass _CORALNet(nn.Module):\n    \"\"\"\n    CORAL ordinal regression (Cao et al., 2020).\n    19 -> 128 -> 64 -> shared representation, then K-1=3 sigmoid heads.\n    Each head k: P(depth > k). Prediction: depth = sum_k I[P(depth > k) > 0.5].\n    Loss: sum_{k=0}^{K-2} BCE(sigmoid(w^T h + b_k), I[y > k])\n    \"\"\"\n\n    def __init__(self, input_dim=NUM_FEATURES, hidden1=128, hidden2=64,\n                 num_classes=NUM_DEPTHS, dropout=0.3):\n        super().__init__()\n        self.num_classes = num_classes\n        self.backbone = nn.Sequential(\n            nn.Linear(input_dim, hidden1),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n            nn.Linear(hidden1, hidden2),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n        )\n        self.fc = nn.Linear(hidden2, 1, bias=False)\n        self.biases = nn.Parameter(torch.zeros(num_classes - 1))\n\n    def forward(self, x):\n        h = self.backbone(x)\n        logit_base = self.fc(h)\n        logits = logit_base + self.biases\n        return logits\n\n\nclass CORALBaseline:\n    \"\"\"\n    CORAL ordinal regression for depth estimation.\n    Ref: Cao, Mirjalili & Raschka (2020). \"Rank consistent ordinal regression\n    for neural networks with consistent confidence sets.\" Pattern Recognition.\n    \"\"\"\n\n    def __init__(self, lr=1e-3, epochs=100, batch_size=256, patience=10,\n                 device=None, seed=42):\n        self.lr = lr\n        self.epochs = epochs\n        self.batch_size = batch_size\n        self.patience = patience\n        self.device = device or (\"cuda\" if torch.cuda.is_available() else \"cpu\")\n        self.seed = seed\n        self.scaler = StandardScaler()\n        self.model = None\n\n    @staticmethod\n    def _encode_ordinal(y, num_classes):\n        n = len(y)\n        targets = np.zeros((n, num_classes - 1), dtype=np.float32)\n        for k in range(num_classes - 1):\n            targets[:, k] = (y > k).astype(np.float32)\n        return targets\n\n    def fit(self, X_train, y_train, X_val=None, y_val=None, **kwargs):\n        torch.manual_seed(self.seed)\n        np.random.seed(self.seed)\n\n        X_s = self.scaler.fit_transform(X_train).astype(np.float32)\n        ord_targets = self._encode_ordinal(y_train, NUM_DEPTHS)\n\n        Xt = torch.tensor(X_s, device=self.device)\n        ot = torch.tensor(ord_targets, device=self.device)\n        ds = TensorDataset(Xt, ot)\n        loader = DataLoader(ds, batch_size=self.batch_size, shuffle=True)\n\n        self.model = _CORALNet().to(self.device)\n        optimizer = optim.Adam(self.model.parameters(), lr=self.lr, weight_decay=1e-4)\n        criterion = nn.BCEWithLogitsLoss()\n\n        best_loss = float(\"inf\")\n        wait = 0\n        best_state = None\n\n        has_val = X_val is not None and y_val is not None\n        if has_val:\n            Xv = torch.tensor(self.scaler.transform(X_val).astype(np.float32),\n                              device=self.device)\n            ov = torch.tensor(self._encode_ordinal(y_val, NUM_DEPTHS),\n                              device=self.device)\n\n        for epoch in range(self.epochs):\n            self.model.train()\n            epoch_loss = 0.0\n            for xb, ob in loader:\n                optimizer.zero_grad()\n                logits = self.model(xb)\n                loss = criterion(logits, ob)\n                loss.backward()\n                optimizer.step()\n                epoch_loss += loss.item() * len(xb)\n            epoch_loss /= len(ds)\n\n            if has_val:\n                self.model.eval()\n                with torch.no_grad():\n                    val_logits = self.model(Xv)\n                    val_loss = criterion(val_logits, ov).item()\n            else:\n                val_loss = epoch_loss\n\n            if val_loss < best_loss - 1e-4:\n                best_loss = val_loss\n                best_state = {k: v.clone() for k, v in self.model.state_dict().items()}\n                wait = 0\n            else:\n                wait += 1\n                if wait >= self.patience:\n                    break\n\n        if best_state is not None:\n            self.model.load_state_dict(best_state)\n\n    def predict(self, X_test):\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n            probs = torch.sigmoid(logits)\n        preds = (probs > 0.5).sum(dim=-1).cpu().numpy().astype(int)\n        return preds\n\n    def predict_proba(self, X_test):\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n            cum_probs = torch.sigmoid(logits).cpu().numpy()\n\n        n = len(X_test)\n        probs = np.zeros((n, NUM_DEPTHS))\n        probs[:, 0] = 1.0 - cum_probs[:, 0]\n        for k in range(1, NUM_DEPTHS - 1):\n            probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]\n        probs[:, NUM_DEPTHS - 1] = cum_probs[:, NUM_DEPTHS - 2]\n        probs = np.clip(probs, 0, 1)\n        row_sums = probs.sum(axis=1, keepdims=True)\n        probs = probs / np.where(row_sums > 0, row_sums, 1.0)\n        return probs\n\n\n# ===================================================================\n#  Baseline 4: DivEye (Surprisal Diversity + XGBoost)\n# ===================================================================\n#\n# DivEye feature groups mapped to our 19 features:\n#   Distributional: mean_ppl, var_ppl, skewness_ppl, kurtosis_ppl\n#   Surprisal:      mean_surprisal, var_surprisal, entropy_of_surprisal\n#   Lexical diversity: type_token_ratio, hapax_ratio, bigram_entropy, trigram_entropy\n#   Repetition:     rep_2gram, rep_3gram, rep_4gram\n#\n# Note: DivEye's temporal features (first-order dS and second-order d2S)\n# are not available in our pre-computed features.\n\nDIVEYE_FEATURE_INDICES = [\n    FEATURE_NAMES.index(f) for f in [\n        \"mean_ppl\", \"var_ppl\", \"skewness_ppl\", \"kurtosis_ppl\",\n        \"mean_surprisal\", \"var_surprisal\", \"entropy_of_surprisal\",\n        \"type_token_ratio\", \"hapax_ratio\", \"bigram_entropy\", \"trigram_entropy\",\n        \"rep_2gram\", \"rep_3gram\", \"rep_4gram\",\n    ]\n]\n\n\nclass DivEyeBaseline:\n    \"\"\"\n    DivEye-style detection adapted for depth estimation.\n    Ref: Basani & Chen (2026). \"Diversity Boosts AI-Generated Text Detection.\" TMLR.\n    XGBoost on surprisal-related feature subset (14 of 19 features).\n    \"\"\"\n\n    def __init__(self, seed=42):\n        self.seed = seed\n        self.model = None\n\n    def fit(self, X_train, y_train, **kwargs):\n        try:\n            from xgboost import XGBClassifier\n        except ImportError:\n            print(\"[ERROR] xgboost not installed. Run: pip install xgboost\")\n            sys.exit(1)\n\n        Xd = X_train[:, DIVEYE_FEATURE_INDICES]\n        self.model = XGBClassifier(\n            n_estimators=200,\n            max_depth=6,\n            learning_rate=0.1,\n            subsample=0.8,\n            colsample_bytree=0.8,\n            random_state=self.seed,\n            use_label_encoder=False,\n            eval_metric=\"mlogloss\",\n            verbosity=0,\n        )\n        self.model.fit(Xd, y_train)\n\n    def predict(self, X_test):\n        Xd = X_test[:, DIVEYE_FEATURE_INDICES]\n        return self.model.predict(Xd)\n\n    def predict_proba(self, X_test):\n        Xd = X_test[:, DIVEYE_FEATURE_INDICES]\n        probs = self.model.predict_proba(Xd)\n        if probs.shape[1] < NUM_DEPTHS:\n            full = np.zeros((probs.shape[0], NUM_DEPTHS))\n            for i, c in enumerate(self.model.classes_):\n                full[:, c] = probs[:, i]\n            return full\n        return probs\n\n\n# ===================================================================\n#  Baseline 5: Random Forest\n# ===================================================================\n\nclass RandomForestBaseline:\n\n    def __init__(self, n_estimators=100, seed=42):\n        self.seed = seed\n        self.n_estimators = n_estimators\n        self.scaler = StandardScaler()\n        self.model = None\n\n    def fit(self, X_train, y_train, **kwargs):\n        from sklearn.ensemble import RandomForestClassifier\n        X_s = self.scaler.fit_transform(X_train)\n        self.model = RandomForestClassifier(\n            n_estimators=self.n_estimators,\n            random_state=self.seed,\n            n_jobs=-1,\n        )\n        self.model.fit(X_s, y_train)\n\n    def predict(self, X_test):\n        X_s = self.scaler.transform(X_test)\n        return self.model.predict(X_s)\n\n    def predict_proba(self, X_test):\n        X_s = self.scaler.transform(X_test)\n        probs = self.model.predict_proba(X_s)\n        if probs.shape[1] < NUM_DEPTHS:\n            full = np.zeros((probs.shape[0], NUM_DEPTHS))\n            for i, c in enumerate(self.model.classes_):\n                full[:, c] = probs[:, i]\n            return full\n        return probs\n\n\n# ===================================================================\n#  Baseline 6: Logistic Regression\n# ===================================================================\n\nclass LogisticRegressionBaseline:\n\n    def __init__(self, max_iter=1000, seed=42):\n        self.seed = seed\n        self.max_iter = max_iter\n        self.scaler = StandardScaler()\n        self.model = None\n\n    def fit(self, X_train, y_train, **kwargs):\n        from sklearn.linear_model import LogisticRegression as _LR\n        X_s = self.scaler.fit_transform(X_train)\n        self.model = _LR(\n            max_iter=self.max_iter,\n            random_state=self.seed,\n            solver=\"lbfgs\",\n        )\n        self.model.fit(X_s, y_train)\n\n    def predict(self, X_test):\n        X_s = self.scaler.transform(X_test)\n        return self.model.predict(X_s)\n\n    def predict_proba(self, X_test):\n        X_s = self.scaler.transform(X_test)\n        probs = self.model.predict_proba(X_s)\n        if probs.shape[1] < NUM_DEPTHS:\n            full = np.zeros((probs.shape[0], NUM_DEPTHS))\n            for i, c in enumerate(self.model.classes_):\n                full[:, c] = probs[:, i]\n            return full\n        return probs\n\n\n# ===================================================================\n#  Baseline 7: Zero-shot LLM Prompting\n# ===================================================================\n\nZEROSHOT_SYSTEM_PROMPT = \"\"\"You are an expert at detecting AI-generated text and estimating its generation depth.\n\n\"Recursive generation depth\" refers to how many times a text has been through an LLM generation cycle:\n- Depth 0: Original human-written text (e.g., Wikipedia, StackExchange, academic papers)\n- Depth 1: Text generated by an LLM given human-written text as a prompt/seed\n- Depth 2: Text generated by an LLM given depth-1 text as input\n- Depth 3: Text generated by an LLM given depth-2 text as input\n\nKey patterns by depth:\n- Depth 0 (human): Rich vocabulary, domain-specific terminology, natural topic shifts, occasional typos/informal phrasing\n- Depth 1 (first-gen): Fluent but slightly generic, may have formulaic transitions, maintains topic coherence\n- Depth 2 (second-gen): More repetitive phrasing, narrower vocabulary, increasingly generic content, possible topic drift\n- Depth 3 (third-gen): Noticeable repetition, formulaic structure, may contain subtle incoherence or circular reasoning, very generic language\"\"\"\n\nZEROSHOT_USER_TEMPLATE = \"\"\"Analyze the following text and estimate its recursive generation depth (0, 1, 2, or 3).\n\nTEXT:\n{text}\n\nRespond with ONLY a JSON object in this exact format:\n{{\"depth\": &lt;integer 0-3>, \"confidence\": &lt;float 0-1>, \"reasoning\": \"&lt;brief one-sentence explanation>\"}}\"\"\"\n\n\ndef _parse_llm_response(response_text):\n    \"\"\"Extract depth prediction from LLM response.\"\"\"\n    json_match = re.search(r'\\{[^{}]*\"depth\"\\s*:\\s*(\\d)[^{}]*\\}', response_text)\n    if json_match:\n        try:\n            obj = json.loads(json_match.group(0))\n            depth = int(obj.get(\"depth\", -1))\n            confidence = float(obj.get(\"confidence\", 0.5))\n            if 0 <= depth <= 3:\n                return depth, confidence\n        except (json.JSONDecodeError, ValueError):\n            pass\n    digit_match = re.search(r'\\b([0-3])\\b', response_text)\n    if digit_match:\n        return int(digit_match.group(1)), 0.5\n    return 0, 0.0\n\n\ndef _call_claude(text, model, max_tokens=256):\n    import anthropic\n    client = anthropic.Anthropic()\n    message = client.messages.create(\n        model=model,\n        max_tokens=max_tokens,\n        system=ZEROSHOT_SYSTEM_PROMPT,\n        messages=[{\"role\": \"user\", \"content\": ZEROSHOT_USER_TEMPLATE.format(text=text)}],\n    )\n    return message.content[0].text\n\n\ndef _call_openai(text, model, max_tokens=256):\n    import openai\n    client = openai.OpenAI()\n    response = client.chat.completions.create(\n        model=model,\n        max_tokens=max_tokens,\n        messages=[\n            {\"role\": \"system\", \"content\": ZEROSHOT_SYSTEM_PROMPT},\n            {\"role\": \"user\", \"content\": ZEROSHOT_USER_TEMPLATE.format(text=text)},\n        ],\n    )\n    return response.choices[0].message.content\n\n\nclass ZeroShotLLMBaseline:\n    \"\"\"\n    Zero-shot LLM prompting for depth estimation.\n    No training -- uses in-context prompting to classify text depth.\n    Supports Claude (Anthropic) and OpenAI APIs.\n    \"\"\"\n\n    def __init__(self, provider=\"claude\", model=None, max_seq_len=512,\n                 rate_limit_delay=0.5):\n        self.provider = provider\n        self.model = model\n        if self.model is None:\n            self.model = \"claude-sonnet-4-20250514\" if provider == \"claude\" else \"gpt-4o\"\n        self.max_seq_len = max_seq_len\n        self.rate_limit_delay = rate_limit_delay\n        self._call_fn = _call_claude if provider == \"claude\" else _call_openai\n\n    def _truncate(self, text):\n        words = text.split()\n        approx_tokens = int(self.max_seq_len * 0.75)\n        if len(words) > approx_tokens:\n            words = words[:approx_tokens]\n        return \" \".join(words)\n\n    def fit(self, X_train, y_train, **kwargs):\n        pass\n\n    def predict_texts(self, texts):\n        \"\"\"Predict depth for raw text inputs.\"\"\"\n        y_preds, y_probs = [], []\n        errors = 0\n        for i, text in enumerate(texts):\n            truncated = self._truncate(text)\n            try:\n                response = self._call_fn(truncated, self.model)\n                depth, confidence = _parse_llm_response(response)\n                y_preds.append(depth)\n                prob = np.zeros(NUM_DEPTHS)\n                prob[depth] = confidence\n                remaining = (1.0 - confidence) / max(NUM_DEPTHS - 1, 1)\n                for d in range(NUM_DEPTHS):\n                    if d != depth:\n                        prob[d] = remaining\n                y_probs.append(prob)\n            except Exception as e:\n                print(f\"  [{i}] API error: {e}\")\n                y_preds.append(0)\n                y_probs.append(np.ones(NUM_DEPTHS) / NUM_DEPTHS)\n                errors += 1\n\n            if (i + 1) % 20 == 0:\n                print(f\"  Progress: {i+1}/{len(texts)}\")\n            if self.rate_limit_delay > 0:\n                time.sleep(self.rate_limit_delay)\n\n        if errors > 0:\n            print(f\"  {errors}/{len(texts)} API errors.\")\n        return np.array(y_preds), np.array(y_probs)\n\n    def predict(self, X_test):\n        raise NotImplementedError(\"ZeroShotLLMBaseline requires raw text. Use predict_texts().\")\n\n    def predict_proba(self, X_test):\n        raise NotImplementedError(\"ZeroShotLLMBaseline requires raw text. Use predict_texts().\")\n\n\n# ===================================================================\n#  Unified Runner\n# ===================================================================\n\nFEATURE_BASED_METHODS = [\"ppl_reg_single\", \"ppl_reg\", \"ce_mlp\", \"coral\", \"diveye\", \"rf\", \"lr\"]\nTEXT_BASED_METHODS = [\"zeroshot\"]\n\nBASELINE_REGISTRY = {\n    \"ppl_reg_single\": \"PPL Regression (single: mean_ppl)\",\n    \"ppl_reg\":        \"PPL Regression (multi: 19-dim OLS)\",\n    \"ce_mlp\":         \"CE-MLP (DCOL ablation)\",\n    \"coral\":          \"CORAL Ordinal Regression\",\n    \"diveye\":         \"DivEye (XGBoost)\",\n    \"rf\":             \"Random Forest\",\n    \"lr\":             \"Logistic Regression\",\n    \"zeroshot\":       \"Zero-shot LLM\",\n}\n\nALL_METHODS = FEATURE_BASED_METHODS + TEXT_BASED_METHODS\n\n\ndef _make_baseline(method, args):\n    if method == \"ppl_reg_single\":\n        return PPLRegressionBaseline(mode=\"single\")\n    elif method == \"ppl_reg\":\n        return PPLRegressionBaseline(mode=\"multi\")\n    elif method == \"ce_mlp\":\n        return CEClassificationBaseline(\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\n            patience=args.patience, seed=args.seed,\n        )\n    elif method == \"coral\":\n        return CORALBaseline(\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\n            patience=args.patience, seed=args.seed,\n        )\n    elif method == \"diveye\":\n        return DivEyeBaseline(seed=args.seed)\n    elif method == \"rf\":\n        return RandomForestBaseline(n_estimators=100, seed=args.seed)\n    elif method == \"lr\":\n        return LogisticRegressionBaseline(max_iter=1000, seed=args.seed)\n    elif method == \"zeroshot\":\n        return ZeroShotLLMBaseline(\n            provider=args.provider,\n            model=args.llm_model,\n            max_seq_len=args.max_seq_len,\n            rate_limit_delay=args.rate_limit_delay,\n        )\n    return None\n\n\ndef run_feature_baseline(method, X_train, y_train, X_val, y_val, X_test, y_test, args):\n    bl = _make_baseline(method, args)\n    if bl is None:\n        print(f\"Unknown method: {method}\")\n        return None\n    bl.fit(X_train, y_train, X_val=X_val, y_val=y_val)\n    y_pred = bl.predict(X_test)\n    y_prob = bl.predict_proba(X_test)\n    return evaluate(BASELINE_REGISTRY[method], y_test, y_pred, y_prob)\n\n\ndef run_zeroshot_baseline(texts, labels, args):\n    bl = _make_baseline(\"zeroshot\", args)\n    _, eval_idx = train_test_split(\n        np.arange(len(labels)), test_size=args.eval_split,\n        stratify=labels, random_state=args.seed,\n    )\n    eval_texts = [texts[i] for i in eval_idx]\n    eval_labels = labels[eval_idx]\n\n    if len(eval_texts) > args.max_eval_samples:\n        rng = np.random.RandomState(args.seed)\n        sample_idx = sorted(rng.choice(len(eval_texts), args.max_eval_samples, replace=False))\n        eval_texts = [eval_texts[i] for i in sample_idx]\n        eval_labels = eval_labels[sample_idx]\n\n    print(f\"Zero-shot: evaluating {len(eval_texts)} samples with {args.provider}/{bl.model}\")\n    print(f\"  Label distribution: {dict(Counter(eval_labels))}\")\n\n    y_pred, y_prob = bl.predict_texts(eval_texts)\n    return evaluate(BASELINE_REGISTRY[\"zeroshot\"], eval_labels, y_pred, y_prob)\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"Baseline battery for depth estimation.\")\n    p.add_argument(\"--method\", default=\"all\",\n                   choices=ALL_METHODS + [\"all\", \"all_features\"])\n    p.add_argument(\"--features_path\", \"--data_path\", default=\"data/features_all.jsonl\",\n                   dest=\"features_path\")\n    p.add_argument(\"--data_dirs\", nargs=\"+\", default=[\"data/\"],\n                   help=\"Directories containing depth_*.jsonl (for zero-shot)\")\n    p.add_argument(\"--output_dir\", default=\"results/baselines/\")\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--test_size\", type=float, default=0.15)\n    p.add_argument(\"--val_size\", type=float, default=0.15)\n    p.add_argument(\"--eval_split\", type=float, default=0.15)\n    p.add_argument(\"--epochs\", type=int, default=100)\n    p.add_argument(\"--batch_size\", type=int, default=256)\n    p.add_argument(\"--lr\", type=float, default=1e-3)\n    p.add_argument(\"--patience\", type=int, default=10)\n    p.add_argument(\"--max_seq_len\", type=int, default=512)\n    # Zero-shot LLM args\n    p.add_argument(\"--provider\", choices=[\"claude\", \"openai\"], default=\"claude\")\n    p.add_argument(\"--llm_model\", default=None,\n                   help=\"LLM model name (default: claude-sonnet-4-20250514 / gpt-4o)\")\n    p.add_argument(\"--max_eval_samples\", type=int, default=200,\n                   help=\"Max samples for zero-shot eval (API cost control)\")\n    p.add_argument(\"--rate_limit_delay\", type=float, default=0.5)\n    return p.parse_args()\n\n\ndef main():\n    args = parse_args()\n\n    if args.method == \"all\":\n        methods = FEATURE_BASED_METHODS\n        print(\"Running all feature-based baselines (use --method zeroshot for LLM baseline)\")\n    elif args.method == \"all_features\":\n        methods = FEATURE_BASED_METHODS\n    else:\n        methods = [args.method]\n\n    all_results = {}\n\n    feature_methods = [m for m in methods if m in FEATURE_BASED_METHODS]\n    text_methods = [m for m in methods if m in TEXT_BASED_METHODS]\n\n    if feature_methods:\n        print(f\"Loading features from {args.features_path} ...\")\n        X, y = load_features(args.features_path)\n        print(f\"  {X.shape[0]} samples, {X.shape[1]} features\")\n        print(f\"  Depth distribution: {dict(Counter(y))}\")\n\n        X_train, y_train, X_val, y_val, X_test, y_test = prepare_splits(\n            X, y, test_size=args.test_size, val_size=args.val_size, seed=args.seed\n        )\n        print(f\"  Train: {len(y_train)}, Val: {len(y_val)}, Test: {len(y_test)}\")\n\n        for m in feature_methods:\n            result = run_feature_baseline(\n                m, X_train, y_train, X_val, y_val, X_test, y_test, args\n            )\n            if result is not None:\n                all_results[m] = result\n\n    if text_methods:\n        if \"zeroshot\" in text_methods:\n            texts, labels = load_jsonl_texts(\n                args.data_dirs, max_samples=0, seed=args.seed\n            )\n            result = run_zeroshot_baseline(texts, labels, args)\n            if result is not None:\n                all_results[\"zeroshot\"] = result\n\n    if len(all_results) > 1:\n        print(f\"\\n{'='*60}\")\n        print(f\"  SUMMARY\")\n        print(f\"{'='*60}\")\n        print(f\"  {'Method':<35s} {'4-cls':>6s} {'3-cls':>6s} {'MAE':>6s}\")\n        print(f\"  {'-'*35} {'-'*6} {'-'*6} {'-'*6}\")\n        for m, r in all_results.items():\n            print(f\"  {r['method']:<35s} {r['acc_4class']:6.4f} {r['acc_3class']:6.4f} {r['mae']:6.4f}\")\n\n    os.makedirs(args.output_dir, exist_ok=True)\n    out_path = os.path.join(args.output_dir, \"baseline_results.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(all_results, f, indent=2, default=str)\n    print(f\"\\nResults saved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "b4e49cac-83b3-4bc5-bfb3-d0b9e55929ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MX62vV4kKN3159kJBN2EuW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10905,
      "cache_read_input_tokens": 70070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10905
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

_source line 150 · 2026-05-14T23:06:59.997Z_

<details><summary>↩ Tool result · `toolu_017dQtJUmffR7un8uA3ngsAq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/baselines.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "11bcffe4-1db6-45d4-9404-9b0713290ab3",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/baselines.py",
    "content": "\"\"\"\nBaseline battery for recursive generation depth estimation.\n\nBaselines (feature-based, 19-dim input):\n  1. PPLRegressionBaseline  -- OLS regression on mean_ppl (single) or all 19 features (multi)\n  2. CEClassificationBaseline -- MLP with cross-entropy loss (DCOL ablation, no contrastive loss)\n  3. CORALBaseline -- Ordinal regression with K-1 binary classifiers (Cao et al., 2020)\n  4. DivEyeBaseline -- Surprisal diversity features + XGBoost (Basani & Chen, TMLR 2026)\n  5. RandomForestBaseline -- sklearn RF on 19-dim features\n  6. LogisticRegressionBaseline -- sklearn LR on 19-dim features\n\nBaselines (text-based, raw text input):\n  7. ZeroShotLLMBaseline -- Prompt an LLM (Claude/OpenAI) to classify depth directly\n\nUsage:\n  python src/baselines.py --method ppl_reg --features_path data/features_all.jsonl\n  python src/baselines.py --method ce_mlp  --features_path data/features_all.jsonl --epochs 50\n  python src/baselines.py --method coral   --features_path data/features_all.jsonl --epochs 50\n  python src/baselines.py --method diveye  --features_path data/features_all.jsonl\n  python src/baselines.py --method rf      --features_path data/features_all.jsonl\n  python src/baselines.py --method lr      --features_path data/features_all.jsonl\n  python src/baselines.py --method zeroshot --data_dirs data/ --provider claude --max_eval_samples 200\n  python src/baselines.py --method all     --features_path data/features_all.jsonl --epochs 50\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport re\nimport sys\nimport time\nimport numpy as np\nfrom collections import Counter\n\nimport torch\nimport torch.nn as nn\nimport torch.optim as optim\nfrom torch.utils.data import DataLoader, TensorDataset\n\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.metrics import (\n    accuracy_score, confusion_matrix, classification_report, roc_auc_score,\n)\n\n# -- Feature schema (must match extract_features.py / dcol_dataset.py) --\n\nFEATURE_NAMES = [\n    \"mean_ppl\", \"var_ppl\", \"skewness_ppl\", \"kurtosis_ppl\",\n    \"p10_ppl\", \"p25_ppl\", \"p50_ppl\", \"p75_ppl\", \"p90_ppl\",\n    \"mean_surprisal\", \"var_surprisal\", \"entropy_of_surprisal\",\n    \"type_token_ratio\", \"hapax_ratio\", \"bigram_entropy\", \"trigram_entropy\",\n    \"rep_2gram\", \"rep_3gram\", \"rep_4gram\",\n]\nNUM_FEATURES = len(FEATURE_NAMES)\nNUM_DEPTHS = 4\nDEPTH_LABELS = list(range(NUM_DEPTHS))\n\n# -- Data loading --\n\ndef load_features(path):\n    \"\"\"Load JSONL features file -> (X [n, 19], y [n]).\"\"\"\n    records = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                records.append(json.loads(line))\n    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)\n    y = np.array([r[\"depth\"] for r in records], dtype=np.int64)\n    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)\n    return X, y\n\n\ndef load_jsonl_texts(data_dirs, max_samples=0, seed=42):\n    \"\"\"Load raw text + depth labels from depth_*.jsonl files across directories.\"\"\"\n    import glob as glob_mod\n    texts, labels = [], []\n    for data_dir in data_dirs:\n        for d in range(NUM_DEPTHS):\n            fpath = os.path.join(data_dir, f\"depth_{d}.jsonl\")\n            if not os.path.exists(fpath):\n                matches = glob_mod.glob(os.path.join(data_dir, f\"*depth_{d}*.jsonl\"))\n                fpath = matches[0] if matches else None\n            if fpath is None or not os.path.exists(fpath):\n                continue\n            with open(fpath) as f:\n                for line in f:\n                    line = line.strip()\n                    if not line:\n                        continue\n                    rec = json.loads(line)\n                    texts.append(rec[\"text\"])\n                    labels.append(rec.get(\"depth\", d))\n    labels = np.array(labels, dtype=np.int64)\n    if max_samples > 0 and len(texts) > max_samples:\n        rng = np.random.RandomState(seed)\n        idx = sorted(rng.choice(len(texts), max_samples, replace=False))\n        texts = [texts[i] for i in idx]\n        labels = labels[idx]\n    print(f\"Loaded {len(texts)} text samples. Depth distribution: {dict(Counter(labels))}\")\n    return texts, labels\n\n\ndef prepare_splits(X, y, test_size=0.15, val_size=0.15, seed=42):\n    idx = np.arange(len(y))\n    train_val_idx, test_idx = train_test_split(\n        idx, test_size=test_size, stratify=y, random_state=seed\n    )\n    rel_val = val_size / (1 - test_size)\n    train_idx, val_idx = train_test_split(\n        train_val_idx, test_size=rel_val,\n        stratify=y[train_val_idx], random_state=seed\n    )\n    return (\n        X[train_idx], y[train_idx],\n        X[val_idx], y[val_idx],\n        X[test_idx], y[test_idx],\n    )\n\n# -- Evaluation metrics --\n\ndef pairwise_auc(y_true, y_prob, d1, d2):\n    mask = np.isin(y_true, [d1, d2])\n    if mask.sum() < 2:\n        return None\n    yt = (y_true[mask] == d2).astype(int)\n    if len(np.unique(yt)) < 2:\n        return None\n    yp = y_prob[mask, d2]\n    return float(roc_auc_score(yt, yp))\n\n\ndef compute_all_pairwise_auc(y_true, y_prob):\n    result = {}\n    for i, d1 in enumerate(DEPTH_LABELS):\n        for d2 in DEPTH_LABELS[i + 1:]:\n            auc = pairwise_auc(y_true, y_prob, d1, d2)\n            result[f\"d{d1}_vs_d{d2}\"] = round(auc, 4) if auc is not None else None\n    return result\n\n\ndef bootstrap_ci(y_true, y_pred, metric_fn=accuracy_score, n_boot=1000, seed=42):\n    rng = np.random.RandomState(seed)\n    scores = []\n    n = len(y_true)\n    for _ in range(n_boot):\n        idx = rng.choice(n, n, replace=True)\n        scores.append(metric_fn(y_true[idx], y_pred[idx]))\n    lo = float(np.percentile(scores, 2.5))\n    hi = float(np.percentile(scores, 97.5))\n    return lo, hi\n\n\ndef evaluate(name, y_true, y_pred, y_prob=None):\n    \"\"\"Print and return evaluation metrics.\"\"\"\n    acc4 = accuracy_score(y_true, y_pred)\n    ci_lo, ci_hi = bootstrap_ci(y_true, y_pred)\n\n    mask_13 = y_true >= 1\n    acc3 = accuracy_score(y_true[mask_13], y_pred[mask_13]) if mask_13.sum() > 0 else 0.0\n\n    mae = float(np.mean(np.abs(y_true - y_pred)))\n\n    cm = confusion_matrix(y_true, y_pred, labels=DEPTH_LABELS)\n    per_class_recall = cm.diagonal() / cm.sum(axis=1).clip(min=1)\n\n    pair_aucs = {}\n    if y_prob is not None:\n        pair_aucs = compute_all_pairwise_auc(y_true, y_prob)\n\n    print(f\"\\n{'='*60}\")\n    print(f\"  {name}\")\n    print(f\"{'='*60}\")\n    print(f\"  4-class accuracy : {acc4:.4f}  (95% CI: [{ci_lo:.4f}, {ci_hi:.4f}])\")\n    print(f\"  3-class accuracy : {acc3:.4f}  (d1-d3 only)\")\n    print(f\"  MAE              : {mae:.4f}\")\n    print(f\"  Per-class recall : {dict(zip([f'd{d}' for d in DEPTH_LABELS], [round(r,4) for r in per_class_recall]))}\")\n    if pair_aucs:\n        print(f\"  Pairwise AUC     : {pair_aucs}\")\n    print(f\"\\n  Confusion matrix:\")\n    print(f\"  {'':>8s}\", \" \".join(f\"pred-{d}\" for d in DEPTH_LABELS))\n    for i, d in enumerate(DEPTH_LABELS):\n        print(f\"  true-{d}  \", \" \".join(f\"{cm[i,j]:6d}\" for j in range(NUM_DEPTHS)))\n\n    cr = classification_report(\n        y_true, y_pred,\n        target_names=[f\"depth-{d}\" for d in DEPTH_LABELS],\n        zero_division=0,\n    )\n    print(f\"\\n{cr}\")\n\n    return {\n        \"method\": name,\n        \"acc_4class\": round(acc4, 4),\n        \"acc_4class_ci\": [round(ci_lo, 4), round(ci_hi, 4)],\n        \"acc_3class\": round(acc3, 4),\n        \"mae\": round(mae, 4),\n        \"per_class_recall\": {f\"d{d}\": round(r, 4) for d, r in zip(DEPTH_LABELS, per_class_recall)},\n        \"pairwise_auc\": pair_aucs,\n    }\n\n\n# ===================================================================\n#  Baseline 1: PPL Regression\n# ===================================================================\n\nclass PPLRegressionBaseline:\n    \"\"\"\n    Linear regression -> round to nearest depth.\n    Single-feature mode: depth = a * mean_ppl + b\n    Multi-feature mode:  depth = X @ w + b  (19-dim OLS)\n    \"\"\"\n\n    def __init__(self, mode=\"multi\"):\n        self.mode = mode\n        self.scaler = StandardScaler()\n        self.model = LinearRegression()\n\n    def _select(self, X):\n        if self.mode == \"single\":\n            idx = FEATURE_NAMES.index(\"mean_ppl\")\n            return X[:, idx:idx+1]\n        return X\n\n    def fit(self, X_train, y_train, **kwargs):\n        Xs = self._select(X_train)\n        Xs = self.scaler.fit_transform(Xs)\n        self.model.fit(Xs, y_train.astype(np.float64))\n\n    def predict(self, X_test):\n        Xs = self._select(X_test)\n        Xs = self.scaler.transform(Xs)\n        raw = self.model.predict(Xs)\n        return np.clip(np.round(raw).astype(int), 0, NUM_DEPTHS - 1)\n\n    def predict_proba(self, X_test):\n        preds = self.predict(X_test)\n        prob = np.zeros((len(preds), NUM_DEPTHS))\n        for i, p in enumerate(preds):\n            prob[i, p] = 1.0\n        return prob\n\n\n# ===================================================================\n#  Baseline 2: Cross-Entropy MLP (DCOL ablation)\n# ===================================================================\n\nclass _CEMLP(nn.Module):\n    \"\"\"19 -> 128 -> 64 -> 4  with ReLU + dropout.\"\"\"\n\n    def __init__(self, input_dim=NUM_FEATURES, hidden1=128, hidden2=64,\n                 num_classes=NUM_DEPTHS, dropout=0.3):\n        super().__init__()\n        self.net = nn.Sequential(\n            nn.Linear(input_dim, hidden1),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n            nn.Linear(hidden1, hidden2),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n            nn.Linear(hidden2, num_classes),\n        )\n\n    def forward(self, x):\n        return self.net(x)\n\n\nclass CEClassificationBaseline:\n    \"\"\"\n    Standard multi-class MLP with cross-entropy loss.\n    Architecture identical to DCOL's feature classifier head (19->128->64->4)\n    but uses only CE loss -- no contrastive learning.\n    Key ablation: if CE-MLP matches DCOL, the contrastive loss adds no value.\n    \"\"\"\n\n    def __init__(self, lr=1e-3, epochs=100, batch_size=256, patience=10,\n                 device=None, seed=42):\n        self.lr = lr\n        self.epochs = epochs\n        self.batch_size = batch_size\n        self.patience = patience\n        self.device = device or (\"cuda\" if torch.cuda.is_available() else \"cpu\")\n        self.seed = seed\n        self.scaler = StandardScaler()\n        self.model = None\n\n    def fit(self, X_train, y_train, X_val=None, y_val=None, **kwargs):\n        torch.manual_seed(self.seed)\n        np.random.seed(self.seed)\n\n        X_s = self.scaler.fit_transform(X_train).astype(np.float32)\n        Xt = torch.tensor(X_s, device=self.device)\n        yt = torch.tensor(y_train, dtype=torch.long, device=self.device)\n        ds = TensorDataset(Xt, yt)\n        loader = DataLoader(ds, batch_size=self.batch_size, shuffle=True)\n\n        self.model = _CEMLP().to(self.device)\n        optimizer = optim.Adam(self.model.parameters(), lr=self.lr, weight_decay=1e-4)\n        criterion = nn.CrossEntropyLoss()\n\n        best_loss = float(\"inf\")\n        wait = 0\n        best_state = None\n\n        has_val = X_val is not None and y_val is not None\n        if has_val:\n            Xv = torch.tensor(self.scaler.transform(X_val).astype(np.float32),\n                              device=self.device)\n            yv = torch.tensor(y_val, dtype=torch.long, device=self.device)\n\n        for epoch in range(self.epochs):\n            self.model.train()\n            epoch_loss = 0.0\n            for xb, yb in loader:\n                optimizer.zero_grad()\n                logits = self.model(xb)\n                loss = criterion(logits, yb)\n                loss.backward()\n                optimizer.step()\n                epoch_loss += loss.item() * len(xb)\n            epoch_loss /= len(ds)\n\n            if has_val:\n                self.model.eval()\n                with torch.no_grad():\n                    val_logits = self.model(Xv)\n                    val_loss = criterion(val_logits, yv).item()\n            else:\n                val_loss = epoch_loss\n\n            if val_loss < best_loss - 1e-4:\n                best_loss = val_loss\n                best_state = {k: v.clone() for k, v in self.model.state_dict().items()}\n                wait = 0\n            else:\n                wait += 1\n                if wait >= self.patience:\n                    break\n\n        if best_state is not None:\n            self.model.load_state_dict(best_state)\n\n    def predict(self, X_test):\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n        return logits.argmax(dim=-1).cpu().numpy()\n\n    def predict_proba(self, X_test):\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n            probs = torch.softmax(logits, dim=-1)\n        return probs.cpu().numpy()\n\n\n# ===================================================================\n#  Baseline 3: CORAL Ordinal Regression\n# ===================================================================\n\nclass _CORALNet(nn.Module):\n    \"\"\"\n    CORAL ordinal regression (Cao et al., 2020).\n    19 -> 128 -> 64 -> shared representation, then K-1=3 sigmoid heads.\n    Each head k: P(depth > k). Prediction: depth = sum_k I[P(depth > k) > 0.5].\n    Loss: sum_{k=0}^{K-2} BCE(sigmoid(w^T h + b_k), I[y > k])\n    \"\"\"\n\n    def __init__(self, input_dim=NUM_FEATURES, hidden1=128, hidden2=64,\n                 num_classes=NUM_DEPTHS, dropout=0.3):\n        super().__init__()\n        self.num_classes = num_classes\n        self.backbone = nn.Sequential(\n            nn.Linear(input_dim, hidden1),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n            nn.Linear(hidden1, hidden2),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n        )\n        self.fc = nn.Linear(hidden2, 1, bias=False)\n        self.biases = nn.Parameter(torch.zeros(num_classes - 1))\n\n    def forward(self, x):\n        h = self.backbone(x)\n        logit_base = self.fc(h)\n        logits = logit_base + self.biases\n        return logits\n\n\nclass CORALBaseline:\n    \"\"\"\n    CORAL ordinal regression for depth estimation.\n    Ref: Cao, Mirjalili & Raschka (2020). \"Rank consistent ordinal regression\n    for neural networks with consistent confidence sets.\" Pattern Recognition.\n    \"\"\"\n\n    def __init__(self, lr=1e-3, epochs=100, batch_size=256, patience=10,\n                 device=None, seed=42):\n        self.lr = lr\n        self.epochs = epochs\n        self.batch_size = batch_size\n        self.patience = patience\n        self.device = device or (\"cuda\" if torch.cuda.is_available() else \"cpu\")\n        self.seed = seed\n        self.scaler = StandardScaler()\n        self.model = None\n\n    @staticmethod\n    def _encode_ordinal(y, num_classes):\n        n = len(y)\n        targets = np.zeros((n, num_classes - 1), dtype=np.float32)\n        for k in range(num_classes - 1):\n            targets[:, k] = (y > k).astype(np.float32)\n        return targets\n\n    def fit(self, X_train, y_train, X_val=None, y_val=None, **kwargs):\n        torch.manual_seed(self.seed)\n        np.random.seed(self.seed)\n\n        X_s = self.scaler.fit_transform(X_train).astype(np.float32)\n        ord_targets = self._encode_ordinal(y_train, NUM_DEPTHS)\n\n        Xt = torch.tensor(X_s, device=self.device)\n        ot = torch.tensor(ord_targets, device=self.device)\n        ds = TensorDataset(Xt, ot)\n        loader = DataLoader(ds, batch_size=self.batch_size, shuffle=True)\n\n        self.model = _CORALNet().to(self.device)\n        optimizer = optim.Adam(self.model.parameters(), lr=self.lr, weight_decay=1e-4)\n        criterion = nn.BCEWithLogitsLoss()\n\n        best_loss = float(\"inf\")\n        wait = 0\n        best_state = None\n\n        has_val = X_val is not None and y_val is not None\n        if has_val:\n            Xv = torch.tensor(self.scaler.transform(X_val).astype(np.float32),\n                              device=self.device)\n            ov = torch.tensor(self._encode_ordinal(y_val, NUM_DEPTHS),\n                              device=self.device)\n\n        for epoch in range(self.epochs):\n            self.model.train()\n            epoch_loss = 0.0\n            for xb, ob in loader:\n                optimizer.zero_grad()\n                logits = self.model(xb)\n                loss = criterion(logits, ob)\n                loss.backward()\n                optimizer.step()\n                epoch_loss += loss.item() * len(xb)\n            epoch_loss /= len(ds)\n\n            if has_val:\n                self.model.eval()\n                with torch.no_grad():\n                    val_logits = self.model(Xv)\n                    val_loss = criterion(val_logits, ov).item()\n            else:\n                val_loss = epoch_loss\n\n            if val_loss < best_loss - 1e-4:\n                best_loss = val_loss\n                best_state = {k: v.clone() for k, v in self.model.state_dict().items()}\n                wait = 0\n            else:\n                wait += 1\n                if wait >= self.patience:\n                    break\n\n        if best_state is not None:\n            self.model.load_state_dict(best_state)\n\n    def predict(self, X_test):\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n            probs = torch.sigmoid(logits)\n        preds = (probs > 0.5).sum(dim=-1).cpu().numpy().astype(int)\n        return preds\n\n    def predict_proba(self, X_test):\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n            cum_probs = torch.sigmoid(logits).cpu().numpy()\n\n        n = len(X_test)\n        probs = np.zeros((n, NUM_DEPTHS))\n        probs[:, 0] = 1.0 - cum_probs[:, 0]\n        for k in range(1, NUM_DEPTHS - 1):\n            probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]\n        probs[:, NUM_DEPTHS - 1] = cum_probs[:, NUM_DEPTHS - 2]\n        probs = np.clip(probs, 0, 1)\n        row_sums = probs.sum(axis=1, keepdims=True)\n        probs = probs / np.where(row_sums > 0, row_sums, 1.0)\n        return probs\n\n\n# ===================================================================\n#  Baseline 4: DivEye (Surprisal Diversity + XGBoost)\n# ===================================================================\n#\n# DivEye feature groups mapped to our 19 features:\n#   Distributional: mean_ppl, var_ppl, skewness_ppl, kurtosis_ppl\n#   Surprisal:      mean_surprisal, var_surprisal, entropy_of_surprisal\n#   Lexical diversity: type_token_ratio, hapax_ratio, bigram_entropy, trigram_entropy\n#   Repetition:     rep_2gram, rep_3gram, rep_4gram\n#\n# Note: DivEye's temporal features (first-order dS and second-order d2S)\n# are not available in our pre-computed features.\n\nDIVEYE_FEATURE_INDICES = [\n    FEATURE_NAMES.index(f) for f in [\n        \"mean_ppl\", \"var_ppl\", \"skewness_ppl\", \"kurtosis_ppl\",\n        \"mean_surprisal\", \"var_surprisal\", \"entropy_of_surprisal\",\n        \"type_token_ratio\", \"hapax_ratio\", \"bigram_entropy\", \"trigram_entropy\",\n        \"rep_2gram\", \"rep_3gram\", \"rep_4gram\",\n    ]\n]\n\n\nclass DivEyeBaseline:\n    \"\"\"\n    DivEye-style detection adapted for depth estimation.\n    Ref: Basani & Chen (2026). \"Diversity Boosts AI-Generated Text Detection.\" TMLR.\n    XGBoost on surprisal-related feature subset (14 of 19 features).\n    \"\"\"\n\n    def __init__(self, seed=42):\n        self.seed = seed\n        self.model = None\n\n    def fit(self, X_train, y_train, **kwargs):\n        try:\n            from xgboost import XGBClassifier\n        except ImportError:\n            print(\"[ERROR] xgboost not installed. Run: pip install xgboost\")\n            sys.exit(1)\n\n        Xd = X_train[:, DIVEYE_FEATURE_INDICES]\n        self.model = XGBClassifier(\n            n_estimators=200,\n            max_depth=6,\n            learning_rate=0.1,\n            subsample=0.8,\n            colsample_bytree=0.8,\n            random_state=self.seed,\n            use_label_encoder=False,\n            eval_metric=\"mlogloss\",\n            verbosity=0,\n        )\n        self.model.fit(Xd, y_train)\n\n    def predict(self, X_test):\n        Xd = X_test[:, DIVEYE_FEATURE_INDICES]\n        return self.model.predict(Xd)\n\n    def predict_proba(self, X_test):\n        Xd = X_test[:, DIVEYE_FEATURE_INDICES]\n        probs = self.model.predict_proba(Xd)\n        if probs.shape[1] < NUM_DEPTHS:\n            full = np.zeros((probs.shape[0], NUM_DEPTHS))\n            for i, c in enumerate(self.model.classes_):\n                full[:, c] = probs[:, i]\n            return full\n        return probs\n\n\n# ===================================================================\n#  Baseline 5: Random Forest\n# ===================================================================\n\nclass RandomForestBaseline:\n\n    def __init__(self, n_estimators=100, seed=42):\n        self.seed = seed\n        self.n_estimators = n_estimators\n        self.scaler = StandardScaler()\n        self.model = None\n\n    def fit(self, X_train, y_train, **kwargs):\n        from sklearn.ensemble import RandomForestClassifier\n        X_s = self.scaler.fit_transform(X_train)\n        self.model = RandomForestClassifier(\n            n_estimators=self.n_estimators,\n            random_state=self.seed,\n            n_jobs=-1,\n        )\n        self.model.fit(X_s, y_train)\n\n    def predict(self, X_test):\n        X_s = self.scaler.transform(X_test)\n        return self.model.predict(X_s)\n\n    def predict_proba(self, X_test):\n        X_s = self.scaler.transform(X_test)\n        probs = self.model.predict_proba(X_s)\n        if probs.shape[1] < NUM_DEPTHS:\n            full = np.zeros((probs.shape[0], NUM_DEPTHS))\n            for i, c in enumerate(self.model.classes_):\n                full[:, c] = probs[:, i]\n            return full\n        return probs\n\n\n# ===================================================================\n#  Baseline 6: Logistic Regression\n# ===================================================================\n\nclass LogisticRegressionBaseline:\n\n    def __init__(self, max_iter=1000, seed=42):\n        self.seed = seed\n        self.max_iter = max_iter\n        self.scaler = StandardScaler()\n        self.model = None\n\n    def fit(self, X_train, y_train, **kwargs):\n        from sklearn.linear_model import LogisticRegression as _LR\n        X_s = self.scaler.fit_transform(X_train)\n        self.model = _LR(\n            max_iter=self.max_iter,\n            random_state=self.seed,\n            solver=\"lbfgs\",\n        )\n        self.model.fit(X_s, y_train)\n\n    def predict(self, X_test):\n        X_s = self.scaler.transform(X_test)\n        return self.model.predict(X_s)\n\n    def predict_proba(self, X_test):\n        X_s = self.scaler.transform(X_test)\n        probs = self.model.predict_proba(X_s)\n        if probs.shape[1] < NUM_DEPTHS:\n            full = np.zeros((probs.shape[0], NUM_DEPTHS))\n            for i, c in enumerate(self.model.classes_):\n                full[:, c] = probs[:, i]\n            return full\n        return probs\n\n\n# ===================================================================\n#  Baseline 7: Zero-shot LLM Prompting\n# ===================================================================\n\nZEROSHOT_SYSTEM_PROMPT = \"\"\"You are an expert at detecting AI-generated text and estimating its generation depth.\n\n\"Recursive generation depth\" refers to how many times a text has been through an LLM generation cycle:\n- Depth 0: Original human-written text (e.g., Wikipedia, StackExchange, academic papers)\n- Depth 1: Text generated by an LLM given human-written text as a prompt/seed\n- Depth 2: Text generated by an LLM given depth-1 text as input\n- Depth 3: Text generated by an LLM given depth-2 text as input\n\nKey patterns by depth:\n- Depth 0 (human): Rich vocabulary, domain-specific terminology, natural topic shifts, occasional typos/informal phrasing\n- Depth 1 (first-gen): Fluent but slightly generic, may have formulaic transitions, maintains topic coherence\n- Depth 2 (second-gen): More repetitive phrasing, narrower vocabulary, increasingly generic content, possible topic drift\n- Depth 3 (third-gen): Noticeable repetition, formulaic structure, may contain subtle incoherence or circular reasoning, very generic language\"\"\"\n\nZEROSHOT_USER_TEMPLATE = \"\"\"Analyze the following text and estimate its recursive generation depth (0, 1, 2, or 3).\n\nTEXT:\n{text}\n\nRespond with ONLY a JSON object in this exact format:\n{{\"depth\": &lt;integer 0-3>, \"confidence\": &lt;float 0-1>, \"reasoning\": \"&lt;brief one-sentence explanation>\"}}\"\"\"\n\n\ndef _parse_llm_response(response_text):\n    \"\"\"Extract depth prediction from LLM response.\"\"\"\n    json_match = re.search(r'\\{[^{}]*\"depth\"\\s*:\\s*(\\d)[^{}]*\\}', response_text)\n    if json_match:\n        try:\n            obj = json.loads(json_match.group(0))\n            depth = int(obj.get(\"depth\", -1))\n            confidence = float(obj.get(\"confidence\", 0.5))\n            if 0 <= depth <= 3:\n                return depth, confidence\n        except (json.JSONDecodeError, ValueError):\n            pass\n    digit_match = re.search(r'\\b([0-3])\\b', response_text)\n    if digit_match:\n        return int(digit_match.group(1)), 0.5\n    return 0, 0.0\n\n\ndef _call_claude(text, model, max_tokens=256):\n    import anthropic\n    client = anthropic.Anthropic()\n    message = client.messages.create(\n        model=model,\n        max_tokens=max_tokens,\n        system=ZEROSHOT_SYSTEM_PROMPT,\n        messages=[{\"role\": \"user\", \"content\": ZEROSHOT_USER_TEMPLATE.format(text=text)}],\n    )\n    return message.content[0].text\n\n\ndef _call_openai(text, model, max_tokens=256):\n    import openai\n    client = openai.OpenAI()\n    response = client.chat.completions.create(\n        model=model,\n        max_tokens=max_tokens,\n        messages=[\n            {\"role\": \"system\", \"content\": ZEROSHOT_SYSTEM_PROMPT},\n            {\"role\": \"user\", \"content\": ZEROSHOT_USER_TEMPLATE.format(text=text)},\n        ],\n    )\n    return response.choices[0].message.content\n\n\nclass ZeroShotLLMBaseline:\n    \"\"\"\n    Zero-shot LLM prompting for depth estimation.\n    No training -- uses in-context prompting to classify text depth.\n    Supports Claude (Anthropic) and OpenAI APIs.\n    \"\"\"\n\n    def __init__(self, provider=\"claude\", model=None, max_seq_len=512,\n                 rate_limit_delay=0.5):\n        self.provider = provider\n        self.model = model\n        if self.model is None:\n            self.model = \"claude-sonnet-4-20250514\" if provider == \"claude\" else \"gpt-4o\"\n        self.max_seq_len = max_seq_len\n        self.rate_limit_delay = rate_limit_delay\n        self._call_fn = _call_claude if provider == \"claude\" else _call_openai\n\n    def _truncate(self, text):\n        words = text.split()\n        approx_tokens = int(self.max_seq_len * 0.75)\n        if len(words) > approx_tokens:\n            words = words[:approx_tokens]\n        return \" \".join(words)\n\n    def fit(self, X_train, y_train, **kwargs):\n        pass\n\n    def predict_texts(self, texts):\n        \"\"\"Predict depth for raw text inputs.\"\"\"\n        y_preds, y_probs = [], []\n        errors = 0\n        for i, text in enumerate(texts):\n            truncated = self._truncate(text)\n            try:\n                response = self._call_fn(truncated, self.model)\n                depth, confidence = _parse_llm_response(response)\n                y_preds.append(depth)\n                prob = np.zeros(NUM_DEPTHS)\n                prob[depth] = confidence\n                remaining = (1.0 - confidence) / max(NUM_DEPTHS - 1, 1)\n                for d in range(NUM_DEPTHS):\n                    if d != depth:\n                        prob[d] = remaining\n                y_probs.append(prob)\n            except Exception as e:\n                print(f\"  [{i}] API error: {e}\")\n                y_preds.append(0)\n                y_probs.append(np.ones(NUM_DEPTHS) / NUM_DEPTHS)\n                errors += 1\n\n            if (i + 1) % 20 == 0:\n                print(f\"  Progress: {i+1}/{len(texts)}\")\n            if self.rate_limit_delay > 0:\n                time.sleep(self.rate_limit_delay)\n\n        if errors > 0:\n            print(f\"  {errors}/{len(texts)} API errors.\")\n        return np.array(y_preds), np.array(y_probs)\n\n    def predict(self, X_test):\n        raise NotImplementedError(\"ZeroShotLLMBaseline requires raw text. Use predict_texts().\")\n\n    def predict_proba(self, X_test):\n        raise NotImplementedError(\"ZeroShotLLMBaseline requires raw text. Use predict_texts().\")\n\n\n# ===================================================================\n#  Unified Runner\n# ===================================================================\n\nFEATURE_BASED_METHODS = [\"ppl_reg_single\", \"ppl_reg\", \"ce_mlp\", \"coral\", \"diveye\", \"rf\", \"lr\"]\nTEXT_BASED_METHODS = [\"zeroshot\"]\n\nBASELINE_REGISTRY = {\n    \"ppl_reg_single\": \"PPL Regression (single: mean_ppl)\",\n    \"ppl_reg\":        \"PPL Regression (multi: 19-dim OLS)\",\n    \"ce_mlp\":         \"CE-MLP (DCOL ablation)\",\n    \"coral\":          \"CORAL Ordinal Regression\",\n    \"diveye\":         \"DivEye (XGBoost)\",\n    \"rf\":             \"Random Forest\",\n    \"lr\":             \"Logistic Regression\",\n    \"zeroshot\":       \"Zero-shot LLM\",\n}\n\nALL_METHODS = FEATURE_BASED_METHODS + TEXT_BASED_METHODS\n\n\ndef _make_baseline(method, args):\n    if method == \"ppl_reg_single\":\n        return PPLRegressionBaseline(mode=\"single\")\n    elif method == \"ppl_reg\":\n        return PPLRegressionBaseline(mode=\"multi\")\n    elif method == \"ce_mlp\":\n        return CEClassificationBaseline(\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\n            patience=args.patience, seed=args.seed,\n        )\n    elif method == \"coral\":\n        return CORALBaseline(\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\n            patience=args.patience, seed=args.seed,\n        )\n    elif method == \"diveye\":\n        return DivEyeBaseline(seed=args.seed)\n    elif method == \"rf\":\n        return RandomForestBaseline(n_estimators=100, seed=args.seed)\n    elif method == \"lr\":\n        return LogisticRegressionBaseline(max_iter=1000, seed=args.seed)\n    elif method == \"zeroshot\":\n        return ZeroShotLLMBaseline(\n            provider=args.provider,\n            model=args.llm_model,\n            max_seq_len=args.max_seq_len,\n            rate_limit_delay=args.rate_limit_delay,\n        )\n    return None\n\n\ndef run_feature_baseline(method, X_train, y_train, X_val, y_val, X_test, y_test, args):\n    bl = _make_baseline(method, args)\n    if bl is None:\n        print(f\"Unknown method: {method}\")\n        return None\n    bl.fit(X_train, y_train, X_val=X_val, y_val=y_val)\n    y_pred = bl.predict(X_test)\n    y_prob = bl.predict_proba(X_test)\n    return evaluate(BASELINE_REGISTRY[method], y_test, y_pred, y_prob)\n\n\ndef run_zeroshot_baseline(texts, labels, args):\n    bl = _make_baseline(\"zeroshot\", args)\n    _, eval_idx = train_test_split(\n        np.arange(len(labels)), test_size=args.eval_split,\n        stratify=labels, random_state=args.seed,\n    )\n    eval_texts = [texts[i] for i in eval_idx]\n    eval_labels = labels[eval_idx]\n\n    if len(eval_texts) > args.max_eval_samples:\n        rng = np.random.RandomState(args.seed)\n        sample_idx = sorted(rng.choice(len(eval_texts), args.max_eval_samples, replace=False))\n        eval_texts = [eval_texts[i] for i in sample_idx]\n        eval_labels = eval_labels[sample_idx]\n\n    print(f\"Zero-shot: evaluating {len(eval_texts)} samples with {args.provider}/{bl.model}\")\n    print(f\"  Label distribution: {dict(Counter(eval_labels))}\")\n\n    y_pred, y_prob = bl.predict_texts(eval_texts)\n    return evaluate(BASELINE_REGISTRY[\"zeroshot\"], eval_labels, y_pred, y_prob)\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"Baseline battery for depth estimation.\")\n    p.add_argument(\"--method\", default=\"all\",\n                   choices=ALL_METHODS + [\"all\", \"all_features\"])\n    p.add_argument(\"--features_path\", \"--data_path\", default=\"data/features_all.jsonl\",\n                   dest=\"features_path\")\n    p.add_argument(\"--data_dirs\", nargs=\"+\", default=[\"data/\"],\n                   help=\"Directories containing depth_*.jsonl (for zero-shot)\")\n    p.add_argument(\"--output_dir\", default=\"results/baselines/\")\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--test_size\", type=float, default=0.15)\n    p.add_argument(\"--val_size\", type=float, default=0.15)\n    p.add_argument(\"--eval_split\", type=float, default=0.15)\n    p.add_argument(\"--epochs\", type=int, default=100)\n    p.add_argument(\"--batch_size\", type=int, default=256)\n    p.add_argument(\"--lr\", type=float, default=1e-3)\n    p.add_argument(\"--patience\", type=int, default=10)\n    p.add_argument(\"--max_seq_len\", type=int, default=512)\n    # Zero-shot LLM args\n    p.add_argument(\"--provider\", choices=[\"claude\", \"openai\"], default=\"claude\")\n    p.add_argument(\"--llm_model\", default=None,\n                   help=\"LLM model name (default: claude-sonnet-4-20250514 / gpt-4o)\")\n    p.add_argument(\"--max_eval_samples\", type=int, default=200,\n                   help=\"Max samples for zero-shot eval (API cost control)\")\n    p.add_argument(\"--rate_limit_delay\", type=float, default=0.5)\n    return p.parse_args()\n\n\ndef main():\n    args = parse_args()\n\n    if args.method == \"all\":\n        methods = FEATURE_BASED_METHODS\n        print(\"Running all feature-based baselines (use --method zeroshot for LLM baseline)\")\n    elif args.method == \"all_features\":\n        methods = FEATURE_BASED_METHODS\n    else:\n        methods = [args.method]\n\n    all_results = {}\n\n    feature_methods = [m for m in methods if m in FEATURE_BASED_METHODS]\n    text_methods = [m for m in methods if m in TEXT_BASED_METHODS]\n\n    if feature_methods:\n        print(f\"Loading features from {args.features_path} ...\")\n        X, y = load_features(args.features_path)\n        print(f\"  {X.shape[0]} samples, {X.shape[1]} features\")\n        print(f\"  Depth distribution: {dict(Counter(y))}\")\n\n        X_train, y_train, X_val, y_val, X_test, y_test = prepare_splits(\n            X, y, test_size=args.test_size, val_size=args.val_size, seed=args.seed\n        )\n        print(f\"  Train: {len(y_train)}, Val: {len(y_val)}, Test: {len(y_test)}\")\n\n        for m in feature_methods:\n            result = run_feature_baseline(\n                m, X_train, y_train, X_val, y_val, X_test, y_test, args\n            )\n            if result is not None:\n                all_results[m] = result\n\n    if text_methods:\n        if \"zeroshot\" in text_methods:\n            texts, labels = load_jsonl_texts(\n                args.data_dirs, max_samples=0, seed=args.seed\n            )\n            result = run_zeroshot_baseline(texts, labels, args)\n            if result is not None:\n                all_results[\"zeroshot\"] = result\n\n    if len(all_results) > 1:\n        print(f\"\\n{'='*60}\")\n        print(f\"  SUMMARY\")\n        print(f\"{'='*60}\")\n        print(f\"  {'Method':<35s} {'4-cls':>6s} {'3-cls':>6s} {'MAE':>6s}\")\n        print(f\"  {'-'*35} {'-'*6} {'-'*6} {'-'*6}\")\n        for m, r in all_results.items():\n            print(f\"  {r['method']:<35s} {r['acc_4class']:6.4f} {r['acc_3class']:6.4f} {r['mae']:6.4f}\")\n\n    os.makedirs(args.output_dir, exist_ok=True)\n    out_path = os.path.join(args.output_dir, \"baseline_results.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(all_results, f, indent=2, default=str)\n    print(f\"\\nResults saved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 24,
        "newStart": 1,
        "newLines": 34,
        "lines": [
          " \"\"\"",
          " Baseline battery for recursive generation depth estimation.",
          " ",
          "-Baselines:",
          "-  1. PPLRegressionBaseline  — OLS regression on mean_ppl (single) or all 19 features (multi)",
          "-  2. CEClassificationBaseline — MLP with cross-entropy loss (DCOL ablation, no contrastive loss)",
          "-  3. CORALBaseline — Ordinal regression with K-1 binary classifiers (Cao et al., 2020)",
          "-  4. DivEyeBaseline — Surprisal diversity features + XGBoost (Basani & Chen, TMLR 2026)",
          "+Baselines (feature-based, 19-dim input):",
          "+  1. PPLRegressionBaseline  -- OLS regression on mean_ppl (single) or all 19 features (multi)",
          "+  2. CEClassificationBaseline -- MLP with cross-entropy loss (DCOL ablation, no contrastive loss)",
          "+  3. CORALBaseline -- Ordinal regression with K-1 binary classifiers (Cao et al., 2020)",
          "+  4. DivEyeBaseline -- Surprisal diversity features + XGBoost (Basani & Chen, TMLR 2026)",
          "+  5. RandomForestBaseline -- sklearn RF on 19-dim features",
          "+  6. LogisticRegressionBaseline -- sklearn LR on 19-dim features",
          " ",
          "+Baselines (text-based, raw text input):",
          "+  7. ZeroShotLLMBaseline -- Prompt an LLM (Claude/OpenAI) to classify depth directly",
          "+",
          " Usage:",
          "   python src/baselines.py --method ppl_reg --features_path data/features_all.jsonl",
          "   python src/baselines.py --method ce_mlp  --features_path data/features_all.jsonl --epochs 50",
          "   python src/baselines.py --method coral   --features_path data/features_all.jsonl --epochs 50",
          "   python src/baselines.py --method diveye  --features_path data/features_all.jsonl",
          "+  python src/baselines.py --method rf      --features_path data/features_all.jsonl",
          "+  python src/baselines.py --method lr      --features_path data/features_all.jsonl",
          "+  python src/baselines.py --method zeroshot --data_dirs data/ --provider claude --max_eval_samples 200",
          "   python src/baselines.py --method all     --features_path data/features_all.jsonl --epochs 50",
          " \"\"\"",
          " ",
          " import argparse",
          " import json",
          " import os",
          "+import re",
          " import sys",
          "+import time",
          " import numpy as np",
          " from collections import Counter",
          " "
        ]
      },
      {
        "oldStart": 34,
        "oldLines": 7,
        "newStart": 44,
        "newLines": 7,
        "lines": [
          "     accuracy_score, confusion_matrix, classification_report, roc_auc_score,",
          " )",
          " ",
          "-# ── Feature schema (must match extract_features.py / dcol_dataset.py) ──",
          "+# -- Feature schema (must match extract_features.py / dcol_dataset.py) --",
          " ",
          " FEATURE_NAMES = [",
          "     \"mean_ppl\", \"var_ppl\", \"skewness_ppl\", \"kurtosis_ppl\","
        ]
      },
      {
        "oldStart": 47,
        "oldLines": 10,
        "newStart": 57,
        "newLines": 10,
        "lines": [
          " NUM_DEPTHS = 4",
          " DEPTH_LABELS = list(range(NUM_DEPTHS))",
          " ",
          "-# ── Data loading ──",
          "+# -- Data loading --",
          " ",
          " def load_features(path):",
          "-    \"\"\"Load JSONL features file → (X [n, 19], y [n]).\"\"\"",
          "+    \"\"\"Load JSONL features file -> (X [n, 19], y [n]).\"\"\"",
          "     records = []",
          "     with open(path) as f:",
          "         for line in f:"
        ]
      },
      {
        "oldStart": 63,
        "oldLines": 6,
        "newStart": 73,
        "newLines": 36,
        "lines": [
          "     return X, y",
          " ",
          " ",
          "+def load_jsonl_texts(data_dirs, max_samples=0, seed=42):",
          "+    \"\"\"Load raw text + depth labels from depth_*.jsonl files across directories.\"\"\"",
          "+    import glob as glob_mod",
          "+    texts, labels = [], []",
          "+    for data_dir in data_dirs:",
          "+        for d in range(NUM_DEPTHS):",
          "+            fpath = os.path.join(data_dir, f\"depth_{d}.jsonl\")",
          "+            if not os.path.exists(fpath):",
          "+                matches = glob_mod.glob(os.path.join(data_dir, f\"*depth_{d}*.jsonl\"))",
          "+                fpath = matches[0] if matches else None",
          "+            if fpath is None or not os.path.exists(fpath):",
          "+                continue",
          "+            with open(fpath) as f:",
          "+                for line in f:",
          "+                    line = line.strip()",
          "+                    if not line:",
          "+                        continue",
          "+                    rec = json.loads(line)",
          "+                    texts.append(rec[\"text\"])",
          "+                    labels.append(rec.get(\"depth\", d))",
          "+    labels = np.array(labels, dtype=np.int64)",
          "+    if max_samples > 0 and len(texts) > max_samples:",
          "+        rng = np.random.RandomState(seed)",
          "+        idx = sorted(rng.choice(len(texts), max_samples, replace=False))",
          "+        texts = [texts[i] for i in idx]",
          "+        labels = labels[idx]",
          "+    print(f\"Loaded {len(texts)} text samples. Depth distribution: {dict(Counter(labels))}\")",
          "+    return texts, labels",
          "+",
          "+",
          " def prepare_splits(X, y, test_size=0.15, val_size=0.15, seed=42):",
          "     idx = np.arange(len(y))",
          "     train_val_idx, test_idx = train_test_split("
        ]
      },
      {
        "oldStart": 79,
        "oldLines": 7,
        "newStart": 119,
        "newLines": 7,
        "lines": [
          "         X[test_idx], y[test_idx],",
          "     )",
          " ",
          "-# ── Evaluation metrics ──",
          "+# -- Evaluation metrics --",
          " ",
          " def pairwise_auc(y_true, y_prob, d1, d2):",
          "     mask = np.isin(y_true, [d1, d2])"
        ]
      },
      {
        "oldStart": 118,
        "oldLines": 7,
        "newStart": 158,
        "newLines": 6,
        "lines": [
          "     acc4 = accuracy_score(y_true, y_pred)",
          "     ci_lo, ci_hi = bootstrap_ci(y_true, y_pred)",
          " ",
          "-    # 3-class accuracy (depth 1-3 only)",
          "     mask_13 = y_true >= 1",
          "     acc3 = accuracy_score(y_true[mask_13], y_pred[mask_13]) if mask_13.sum() > 0 else 0.0",
          " "
        ]
      },
      {
        "oldStart": 163,
        "oldLines": 23,
        "newStart": 202,
        "newLines": 19,
        "lines": [
          "     }",
          " ",
          " ",
          "-# ═══════════════════════════════════════════════════════════════════════",
          "+# ===================================================================",
          " #  Baseline 1: PPL Regression",
          "-# ═══════════════════════════════════════════════════════════════════════",
          "+# ===================================================================",
          " ",
          " class PPLRegressionBaseline:",
          "     \"\"\"",
          "-    Linear regression → round to nearest depth.",
          "-",
          "+    Linear regression -> round to nearest depth.",
          "     Single-feature mode: depth = a * mean_ppl + b",
          "     Multi-feature mode:  depth = X @ w + b  (19-dim OLS)",
          "-",
          "-    Simplest possible baseline. If mean_ppl alone suffices, complex models are",
          "-    unnecessary.",
          "     \"\"\"",
          " ",
          "     def __init__(self, mode=\"multi\"):",
          "-        self.mode = mode  # \"single\" or \"multi\"",
          "+        self.mode = mode",
          "         self.scaler = StandardScaler()",
          "         self.model = LinearRegression()",
          " "
        ]
      },
      {
        "oldStart": 189,
        "oldLines": 7,
        "newStart": 224,
        "newLines": 7,
        "lines": [
          "             return X[:, idx:idx+1]",
          "         return X",
          " ",
          "-    def fit(self, X_train, y_train):",
          "+    def fit(self, X_train, y_train, **kwargs):",
          "         Xs = self._select(X_train)",
          "         Xs = self.scaler.fit_transform(Xs)",
          "         self.model.fit(Xs, y_train.astype(np.float64))"
        ]
      },
      {
        "oldStart": 208,
        "oldLines": 13,
        "newStart": 243,
        "newLines": 12,
        "lines": [
          "         return prob",
          " ",
          " ",
          "-# ═══════════════════════════════════════════════════════════════════════",
          "+# ===================================================================",
          " #  Baseline 2: Cross-Entropy MLP (DCOL ablation)",
          "-# ═══════════════════════════════════════════════════════════════════════",
          "+# ===================================================================",
          " ",
          " class _CEMLP(nn.Module):",
          "-    \"\"\"19 → 128 → 64 → 4  with ReLU + dropout. Same architecture as DCOL's",
          "-    feature head, but trained with CE loss only (no contrastive loss).\"\"\"",
          "+    \"\"\"19 -> 128 -> 64 -> 4  with ReLU + dropout.\"\"\"",
          " ",
          "     def __init__(self, input_dim=NUM_FEATURES, hidden1=128, hidden2=64,",
          "                  num_classes=NUM_DEPTHS, dropout=0.3):"
        ]
      },
      {
        "oldStart": 236,
        "oldLines": 11,
        "newStart": 270,
        "newLines": 9,
        "lines": [
          " class CEClassificationBaseline:",
          "     \"\"\"",
          "     Standard multi-class MLP with cross-entropy loss.",
          "-",
          "-    Architecture identical to DCOL's feature classifier head (19→128→64→4)",
          "-    but uses only CE loss — no contrastive learning.",
          "-    This is the key ablation: if CE-MLP matches DCOL, the contrastive loss",
          "-    adds no value.",
          "+    Architecture identical to DCOL's feature classifier head (19->128->64->4)",
          "+    but uses only CE loss -- no contrastive learning.",
          "+    Key ablation: if CE-MLP matches DCOL, the contrastive loss adds no value.",
          "     \"\"\"",
          " ",
          "     def __init__(self, lr=1e-3, epochs=100, batch_size=256, patience=10,"
        ]
      },
      {
        "oldStart": 254,
        "oldLines": 7,
        "newStart": 286,
        "newLines": 7,
        "lines": [
          "         self.scaler = StandardScaler()",
          "         self.model = None",
          " ",
          "-    def fit(self, X_train, y_train, X_val=None, y_val=None):",
          "+    def fit(self, X_train, y_train, X_val=None, y_val=None, **kwargs):",
          "         torch.manual_seed(self.seed)",
          "         np.random.seed(self.seed)",
          " "
        ]
      },
      {
        "oldStart": 328,
        "oldLines": 26,
        "newStart": 360,
        "newLines": 16,
        "lines": [
          "         return probs.cpu().numpy()",
          " ",
          " ",
          "-# ═══════════════════════════════════════════════════════════════════════",
          "+# ===================================================================",
          " #  Baseline 3: CORAL Ordinal Regression",
          "-# ═══════════════════════════════════════════════════════════════════════",
          "+# ===================================================================",
          " ",
          " class _CORALNet(nn.Module):",
          "     \"\"\"",
          "-    CORAL ordinal regression (Cao et al., 2020, \"Rank consistent ordinal",
          "-    regression for neural networks with consistent confidence sets\").",
          "-",
          "-    Architecture: 19 → 128 → 64 → shared representation, then K-1 = 3",
          "-    independent sigmoid heads.",
          "-",
          "-    Each head k answers: P(depth > k).",
          "-    Prediction: depth = sum_k I[P(depth > k) > 0.5].",
          "-",
          "-    Loss (rank-consistent):",
          "-        L = sum_{k=0}^{K-2} BCE(sigmoid(w_k^T h + b_k), I[y > k])",
          "-",
          "-    Weight sharing across heads ensures rank consistency: predictions are",
          "-    monotonically decreasing in threshold order.",
          "+    CORAL ordinal regression (Cao et al., 2020).",
          "+    19 -> 128 -> 64 -> shared representation, then K-1=3 sigmoid heads.",
          "+    Each head k: P(depth > k). Prediction: depth = sum_k I[P(depth > k) > 0.5].",
          "+    Loss: sum_{k=0}^{K-2} BCE(sigmoid(w^T h + b_k), I[y > k])",
          "     \"\"\"",
          " ",
          "     def __init__(self, input_dim=NUM_FEATURES, hidden1=128, hidden2=64,"
        ]
      },
      {
        "oldStart": 362,
        "oldLines": 27,
        "newStart": 384,
        "newLines": 21,
        "lines": [
          "             nn.ReLU(),",
          "             nn.Dropout(dropout),",
          "         )",
          "-        # K-1 independent binary heads (shared backbone, separate bias)",
          "         self.fc = nn.Linear(hidden2, 1, bias=False)",
          "         self.biases = nn.Parameter(torch.zeros(num_classes - 1))",
          " ",
          "     def forward(self, x):",
          "-        h = self.backbone(x)             # [B, 64]",
          "-        logit_base = self.fc(h)          # [B, 1]",
          "-        # broadcast: [B, K-1]",
          "-        logits = logit_base + self.biases # each head shares weight, different bias",
          "+        h = self.backbone(x)",
          "+        logit_base = self.fc(h)",
          "+        logits = logit_base + self.biases",
          "         return logits",
          " ",
          " ",
          " class CORALBaseline:",
          "     \"\"\"",
          "     CORAL ordinal regression for depth estimation.",
          "-",
          "     Ref: Cao, Mirjalili & Raschka (2020). \"Rank consistent ordinal regression",
          "     for neural networks with consistent confidence sets.\" Pattern Recognition.",
          "-",
          "-    Exploits ordinal structure: depth 0 < 1 < 2 < 3.",
          "-    Alternative to DCOL's contrastive approach for leveraging label ordering.",
          "     \"\"\"",
          " ",
          "     def __init__(self, lr=1e-3, epochs=100, batch_size=256, patience=10,"
        ]
      },
      {
        "oldStart": 398,
        "oldLines": 16,
        "newStart": 414,
        "newLines": 13,
        "lines": [
          " ",
          "     @staticmethod",
          "     def _encode_ordinal(y, num_classes):",
          "-        \"\"\"Convert class labels to K-1 binary ordinal targets.",
          "-        y=2, K=4 → [1, 1, 0]  (depth > 0? yes, depth > 1? yes, depth > 2? no)",
          "-        \"\"\"",
          "         n = len(y)",
          "         targets = np.zeros((n, num_classes - 1), dtype=np.float32)",
          "         for k in range(num_classes - 1):",
          "             targets[:, k] = (y > k).astype(np.float32)",
          "         return targets",
          " ",
          "-    def fit(self, X_train, y_train, X_val=None, y_val=None):",
          "+    def fit(self, X_train, y_train, X_val=None, y_val=None, **kwargs):",
          "         torch.manual_seed(self.seed)",
          "         np.random.seed(self.seed)",
          " "
        ]
      },
      {
        "oldStart": 472,
        "oldLines": 30,
        "newStart": 485,
        "newLines": 23,
        "lines": [
          "                            device=self.device)",
          "         with torch.no_grad():",
          "             logits = self.model(X_s)",
          "-            probs = torch.sigmoid(logits)  # [B, K-1], P(depth > k)",
          "-        # depth = number of thresholds exceeded",
          "+            probs = torch.sigmoid(logits)",
          "         preds = (probs > 0.5).sum(dim=-1).cpu().numpy().astype(int)",
          "         return preds",
          " ",
          "     def predict_proba(self, X_test):",
          "-        \"\"\"Convert cumulative probabilities to per-class probabilities.",
          "-        P(depth=k) = P(depth>k-1) - P(depth>k), with boundary conditions.",
          "-        \"\"\"",
          "         self.model.eval()",
          "         X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),",
          "                            device=self.device)",
          "         with torch.no_grad():",
          "             logits = self.model(X_s)",
          "-            cum_probs = torch.sigmoid(logits).cpu().numpy()  # [B, K-1]",
          "+            cum_probs = torch.sigmoid(logits).cpu().numpy()",
          " ",
          "         n = len(X_test)",
          "         probs = np.zeros((n, NUM_DEPTHS))",
          "-        # P(depth=0) = 1 - P(depth>0)",
          "         probs[:, 0] = 1.0 - cum_probs[:, 0]",
          "-        # P(depth=k) = P(depth>k-1) - P(depth>k) for k=1..K-2",
          "         for k in range(1, NUM_DEPTHS - 1):",
          "             probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]",
          "-        # P(depth=K-1) = P(depth>K-2)",
          "         probs[:, NUM_DEPTHS - 1] = cum_probs[:, NUM_DEPTHS - 2]",
          "         probs = np.clip(probs, 0, 1)",
          "         row_sums = probs.sum(axis=1, keepdims=True)"
        ]
      },
      {
        "oldStart": 503,
        "oldLines": 21,
        "newStart": 509,
        "newLines": 18,
        "lines": [
          "         return probs",
          " ",
          " ",
          "-# ═══════════════════════════════════════════════════════════════════════",
          "+# ===================================================================",
          " #  Baseline 4: DivEye (Surprisal Diversity + XGBoost)",
          "-# ═══════════════════════════════════════════════════════════════════════",
          "-",
          "+# ===================================================================",
          "+#",
          " # DivEye feature groups mapped to our 19 features:",
          "-#   Distributional: mean_ppl, var_ppl, skewness_ppl, kurtosis_ppl → matches",
          "-#                   DivEye's mean/var/skewness/kurtosis of surprisal",
          "+#   Distributional: mean_ppl, var_ppl, skewness_ppl, kurtosis_ppl",
          " #   Surprisal:      mean_surprisal, var_surprisal, entropy_of_surprisal",
          " #   Lexical diversity: type_token_ratio, hapax_ratio, bigram_entropy, trigram_entropy",
          " #   Repetition:     rep_2gram, rep_3gram, rep_4gram",
          " #",
          "-# TODO: DivEye's temporal features (first-order ∆S and second-order ∆²S,",
          "-#       computed from per-token surprisal sequences) are not available in our",
          "-#       pre-computed features. Full DivEye reproduction requires raw token-level",
          "-#       surprisal; these summary statistics are a proxy.",
          "+# Note: DivEye's temporal features (first-order dS and second-order d2S)",
          "+# are not available in our pre-computed features.",
          " ",
          " DIVEYE_FEATURE_INDICES = [",
          "     FEATURE_NAMES.index(f) for f in ["
        ]
      },
      {
        "oldStart": 532,
        "oldLines": 17,
        "newStart": 535,
        "newLines": 8,
        "lines": [
          " class DivEyeBaseline:",
          "     \"\"\"",
          "     DivEye-style detection adapted for depth estimation.",
          "-",
          "-    Ref: Basani, A. R. & Chen, P.-Y. (2026). Diversity Boosts AI-Generated Text Detection. Transactions on Machine Learning Research (TMLR).",
          "-    GitHub: https://github.com/IBM/diveye",
          "-",
          "-    DivEye's insight: human text has higher surprisal diversity (distributional,",
          "-    first-order temporal ∆S, second-order ∆²S). We adapt this to depth estimation:",
          "-    deeper recursive generations should have *lower* diversity.",
          "-",
          "-    Implementation: XGBoost on surprisal-related feature subset (14 of 19 features).",
          "-    Full DivEye also uses first/second-order temporal surprisal features from raw",
          "-    token sequences — those are not available in our pre-extracted features.",
          "+    Ref: Basani & Chen (2026). \"Diversity Boosts AI-Generated Text Detection.\" TMLR.",
          "+    XGBoost on surprisal-related feature subset (14 of 19 features).",
          "     \"\"\"",
          " ",
          "     def __init__(self, seed=42):"
        ]
      },
      {
        "oldStart": 577,
        "oldLines": 7,
        "newStart": 571,
        "newLines": 6,
        "lines": [
          "     def predict_proba(self, X_test):",
          "         Xd = X_test[:, DIVEYE_FEATURE_INDICES]",
          "         probs = self.model.predict_proba(Xd)",
          "-        # Ensure output is [n, NUM_DEPTHS] even if some classes are missing",
          "         if probs.shape[1] < NUM_DEPTHS:",
          "             full = np.zeros((probs.shape[0], NUM_DEPTHS))",
          "             for i, c in enumerate(self.model.classes_):"
        ]
      },
      {
        "oldStart": 586,
        "oldLines": 88,
        "newStart": 579,
        "newLines": 373,
        "lines": [
          "         return probs",
          " ",
          " ",
          "-# ═══════════════════════════════════════════════════════════════════════",
          "+# ===================================================================",
          "+#  Baseline 5: Random Forest",
          "+# ===================================================================",
          "+",
          "+class RandomForestBaseline:",
          "+",
          "+    def __init__(self, n_estimators=100, seed=42):",
          "+        self.seed = seed",
          "+        self.n_estimators = n_estimators",
          "+        self.scaler = StandardScaler()",
          "+        self.model = None",
          "+",
          "+    def fit(self, X_train, y_train, **kwargs):",
          "+        from sklearn.ensemble import RandomForestClassifier",
          "+        X_s = self.scaler.fit_transform(X_train)",
          "+        self.model = RandomForestClassifier(",
          "+            n_estimators=self.n_estimators,",
          "+            random_state=self.seed,",
          "+            n_jobs=-1,",
          "+        )",
          "+        self.model.fit(X_s, y_train)",
          "+",
          "+    def predict(self, X_test):",
          "+        X_s = self.scaler.transform(X_test)",
          "+        return self.model.predict(X_s)",
          "+",
          "+    def predict_proba(self, X_test):",
          "+        X_s = self.scaler.transform(X_test)",
          "+        probs = self.model.predict_proba(X_s)",
          "+        if probs.shape[1] < NUM_DEPTHS:",
          "+            full = np.zeros((probs.shape[0], NUM_DEPTHS))",
          "+            for i, c in enumerate(self.model.classes_):",
          "+                full[:, c] = probs[:, i]",
          "+            return full",
          "+        return probs",
          "+",
          "+",
          "+# ===================================================================",
          "+#  Baseline 6: Logistic Regression",
          "+# ===================================================================",
          "+",
          "+class LogisticRegressionBaseline:",
          "+",
          "+    def __init__(self, max_iter=1000, seed=42):",
          "+        self.seed = seed",
          "+        self.max_iter = max_iter",
          "+        self.scaler = StandardScaler()",
          "+        self.model = None",
          "+",
          "+    def fit(self, X_train, y_train, **kwargs):",
          "+        from sklearn.linear_model import LogisticRegression as _LR",
          "+        X_s = self.scaler.fit_transform(X_train)",
          "+        self.model = _LR(",
          "+            max_iter=self.max_iter,",
          "+            random_state=self.seed,",
          "+            solver=\"lbfgs\",",
          "+        )",
          "+        self.model.fit(X_s, y_train)",
          "+",
          "+    def predict(self, X_test):",
          "+        X_s = self.scaler.transform(X_test)",
          "+        return self.model.predict(X_s)",
          "+",
          "+    def predict_proba(self, X_test):",
          "+        X_s = self.scaler.transform(X_test)",
          "+        probs = self.model.predict_proba(X_s)",
          "+        if probs.shape[1] < NUM_DEPTHS:",
          "+            full = np.zeros((probs.shape[0], NUM_DEPTHS))",
          "+            for i, c in enumerate(self.model.classes_):",
          "+                full[:, c] = probs[:, i]",
          "+            return full",
          "+        return probs",
          "+",
          "+",
          "+# ===================================================================",
          "+#  Baseline 7: Zero-shot LLM Prompting",
          "+# ===================================================================",
          "+",
          "+ZEROSHOT_SYSTEM_PROMPT = \"\"\"You are an expert at detecting AI-generated text and estimating its generation depth.",
          "+",
          "+\"Recursive generation depth\" refers to how many times a text has been through an LLM generation cycle:",
          "+- Depth 0: Original human-written text (e.g., Wikipedia, StackExchange, academic papers)",
          "+- Depth 1: Text generated by an LLM given human-written text as a prompt/seed",
          "+- Depth 2: Text generated by an LLM given depth-1 text as input",
          "+- Depth 3: Text generated by an LLM given depth-2 text as input",
          "+",
          "+Key patterns by depth:",
          "+- Depth 0 (human): Rich vocabulary, domain-specific terminology, natural topic shifts, occasional typos/informal phrasing",
          "+- Depth 1 (first-gen): Fluent but slightly generic, may have formulaic transitions, maintains topic coherence",
          "+- Depth 2 (second-gen): More repetitive phrasing, narrower vocabulary, increasingly generic content, possible topic drift",
          "+- Depth 3 (third-gen): Noticeable repetition, formulaic structure, may contain subtle incoherence or circular reasoning, very generic language\"\"\"",
          "+",
          "+ZEROSHOT_USER_TEMPLATE = \"\"\"Analyze the following text and estimate its recursive generation depth (0, 1, 2, or 3).",
          "+",
          "+TEXT:",
          "+{text}",
          "+",
          "+Respond with ONLY a JSON object in this exact format:",
          "+{{\"depth\": &lt;integer 0-3>, \"confidence\": &lt;float 0-1>, \"reasoning\": \"&lt;brief one-sentence explanation>\"}}\"\"\"",
          "+",
          "+",
          "+def _parse_llm_response(response_text):",
          "+    \"\"\"Extract depth prediction from LLM response.\"\"\"",
          "+    json_match = re.search(r'\\{[^{}]*\"depth\"\\s*:\\s*(\\d)[^{}]*\\}', response_text)",
          "+    if json_match:",
          "+        try:",
          "+            obj = json.loads(json_match.group(0))",
          "+            depth = int(obj.get(\"depth\", -1))",
          "+            confidence = float(obj.get(\"confidence\", 0.5))",
          "+            if 0 <= depth <= 3:",
          "+                return depth, confidence",
          "+        except (json.JSONDecodeError, ValueError):",
          "+            pass",
          "+    digit_match = re.search(r'\\b([0-3])\\b', response_text)",
          "+    if digit_match:",
          "+        return int(digit_match.group(1)), 0.5",
          "+    return 0, 0.0",
          "+",
          "+",
          "+def _call_claude(text, model, max_tokens=256):",
          "+    import anthropic",
          "+    client = anthropic.Anthropic()",
          "+    message = client.messages.create(",
          "+        model=model,",
          "+        max_tokens=max_tokens,",
          "+        system=ZEROSHOT_SYSTEM_PROMPT,",
          "+        messages=[{\"role\": \"user\", \"content\": ZEROSHOT_USER_TEMPLATE.format(text=text)}],",
          "+    )",
          "+    return message.content[0].text",
          "+",
          "+",
          "+def _call_openai(text, model, max_tokens=256):",
          "+    import openai",
          "+    client = openai.OpenAI()",
          "+    response = client.chat.completions.create(",
          "+        model=model,",
          "+        max_tokens=max_tokens,",
          "+        messages=[",
          "+            {\"role\": \"system\", \"content\": ZEROSHOT_SYSTEM_PROMPT},",
          "+            {\"role\": \"user\", \"content\": ZEROSHOT_USER_TEMPLATE.format(text=text)},",
          "+        ],",
          "+    )",
          "+    return response.choices[0].message.content",
          "+",
          "+",
          "+class ZeroShotLLMBaseline:",
          "+    \"\"\"",
          "+    Zero-shot LLM prompting for depth estimation.",
          "+    No training -- uses in-context prompting to classify text depth.",
          "+    Supports Claude (Anthropic) and OpenAI APIs.",
          "+    \"\"\"",
          "+",
          "+    def __init__(self, provider=\"claude\", model=None, max_seq_len=512,",
          "+                 rate_limit_delay=0.5):",
          "+        self.provider = provider",
          "+        self.model = model",
          "+        if self.model is None:",
          "+            self.model = \"claude-sonnet-4-20250514\" if provider == \"claude\" else \"gpt-4o\"",
          "+        self.max_seq_len = max_seq_len",
          "+        self.rate_limit_delay = rate_limit_delay",
          "+        self._call_fn = _call_claude if provider == \"claude\" else _call_openai",
          "+",
          "+    def _truncate(self, text):",
          "+        words = text.split()",
          "+        approx_tokens = int(self.max_seq_len * 0.75)",
          "+        if len(words) > approx_tokens:",
          "+            words = words[:approx_tokens]",
          "+        return \" \".join(words)",
          "+",
          "+    def fit(self, X_train, y_train, **kwargs):",
          "+        pass",
          "+",
          "+    def predict_texts(self, texts):",
          "+        \"\"\"Predict depth for raw text inputs.\"\"\"",
          "+        y_preds, y_probs = [], []",
          "+        errors = 0",
          "+        for i, text in enumerate(texts):",
          "+            truncated = self._truncate(text)",
          "+            try:",
          "+                response = self._call_fn(truncated, self.model)",
          "+                depth, confidence = _parse_llm_response(response)",
          "+                y_preds.append(depth)",
          "+                prob = np.zeros(NUM_DEPTHS)",
          "+                prob[depth] = confidence",
          "+                remaining = (1.0 - confidence) / max(NUM_DEPTHS - 1, 1)",
          "+                for d in range(NUM_DEPTHS):",
          "+                    if d != depth:",
          "+                        prob[d] = remaining",
          "+                y_probs.append(prob)",
          "+            except Exception as e:",
          "+                print(f\"  [{i}] API error: {e}\")",
          "+                y_preds.append(0)",
          "+                y_probs.append(np.ones(NUM_DEPTHS) / NUM_DEPTHS)",
          "+                errors += 1",
          "+",
          "+            if (i + 1) % 20 == 0:",
          "+                print(f\"  Progress: {i+1}/{len(texts)}\")",
          "+            if self.rate_limit_delay > 0:",
          "+                time.sleep(self.rate_limit_delay)",
          "+",
          "+        if errors > 0:",
          "+            print(f\"  {errors}/{len(texts)} API errors.\")",
          "+        return np.array(y_preds), np.array(y_probs)",
          "+",
          "+    def predict(self, X_test):",
          "+        raise NotImplementedError(\"ZeroShotLLMBaseline requires raw text. Use predict_texts().\")",
          "+",
          "+    def predict_proba(self, X_test):",
          "+        raise NotImplementedError(\"ZeroShotLLMBaseline requires raw text. Use predict_texts().\")",
          "+",
          "+",
          "+# ===================================================================",
          " #  Unified Runner",
          "-# ═══════════════════════════════════════════════════════════════════════",
          "+# ===================================================================",
          " ",
          "+FEATURE_BASED_METHODS = [\"ppl_reg_single\", \"ppl_reg\", \"ce_mlp\", \"coral\", \"diveye\", \"rf\", \"lr\"]",
          "+TEXT_BASED_METHODS = [\"zeroshot\"]",
          "+",
          " BASELINE_REGISTRY = {",
          "-    \"ppl_reg_single\": (\"PPL Regression (single: mean_ppl)\", lambda: PPLRegressionBaseline(mode=\"single\")),",
          "-    \"ppl_reg\":        (\"PPL Regression (multi: 19-dim OLS)\", lambda: PPLRegressionBaseline(mode=\"multi\")),",
          "-    \"ce_mlp\":         (\"CE-MLP (DCOL ablation)\", None),  # needs args",
          "-    \"coral\":          (\"CORAL Ordinal Regression\", None),",
          "-    \"diveye\":         (\"DivEye (XGBoost)\", lambda: DivEyeBaseline()),",
          "+    \"ppl_reg_single\": \"PPL Regression (single: mean_ppl)\",",
          "+    \"ppl_reg\":        \"PPL Regression (multi: 19-dim OLS)\",",
          "+    \"ce_mlp\":         \"CE-MLP (DCOL ablation)\",",
          "+    \"coral\":          \"CORAL Ordinal Regression\",",
          "+    \"diveye\":         \"DivEye (XGBoost)\",",
          "+    \"rf\":             \"Random Forest\",",
          "+    \"lr\":             \"Logistic Regression\",",
          "+    \"zeroshot\":       \"Zero-shot LLM\",",
          " }",
          " ",
          "+ALL_METHODS = FEATURE_BASED_METHODS + TEXT_BASED_METHODS",
          " ",
          "-def run_baseline(method, X_train, y_train, X_val, y_val, X_test, y_test, args):",
          "+",
          "+def _make_baseline(method, args):",
          "     if method == \"ppl_reg_single\":",
          "-        bl = PPLRegressionBaseline(mode=\"single\")",
          "-        bl.fit(X_train, y_train)",
          "+        return PPLRegressionBaseline(mode=\"single\")",
          "     elif method == \"ppl_reg\":",
          "-        bl = PPLRegressionBaseline(mode=\"multi\")",
          "-        bl.fit(X_train, y_train)",
          "+        return PPLRegressionBaseline(mode=\"multi\")",
          "     elif method == \"ce_mlp\":",
          "-        bl = CEClassificationBaseline(",
          "+        return CEClassificationBaseline(",
          "             lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,",
          "             patience=args.patience, seed=args.seed,",
          "         )",
          "-        bl.fit(X_train, y_train, X_val, y_val)",
          "     elif method == \"coral\":",
          "-        bl = CORALBaseline(",
          "+        return CORALBaseline(",
          "             lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,",
          "             patience=args.patience, seed=args.seed,",
          "         )",
          "-        bl.fit(X_train, y_train, X_val, y_val)",
          "     elif method == \"diveye\":",
          "-        bl = DivEyeBaseline(seed=args.seed)",
          "-        bl.fit(X_train, y_train)",
          "-    else:",
          "+        return DivEyeBaseline(seed=args.seed)",
          "+    elif method == \"rf\":",
          "+        return RandomForestBaseline(n_estimators=100, seed=args.seed)",
          "+    elif method == \"lr\":",
          "+        return LogisticRegressionBaseline(max_iter=1000, seed=args.seed)",
          "+    elif method == \"zeroshot\":",
          "+        return ZeroShotLLMBaseline(",
          "+            provider=args.provider,",
          "+            model=args.llm_model,",
          "+            max_seq_len=args.max_seq_len,",
          "+            rate_limit_delay=args.rate_limit_delay,",
          "+        )",
          "+    return None",
          "+",
          "+",
          "+def run_feature_baseline(method, X_train, y_train, X_val, y_val, X_test, y_test, args):",
          "+    bl = _make_baseline(method, args)",
          "+    if bl is None:",
          "         print(f\"Unknown method: {method}\")",
          "         return None",
          "-",
          "+    bl.fit(X_train, y_train, X_val=X_val, y_val=y_val)",
          "     y_pred = bl.predict(X_test)",
          "     y_prob = bl.predict_proba(X_test)",
          "-    name = BASELINE_REGISTRY.get(method, (method, None))[0]",
          "-    return evaluate(name, y_test, y_pred, y_prob)",
          "+    return evaluate(BASELINE_REGISTRY[method], y_test, y_pred, y_prob)",
          " ",
          " ",
          "+def run_zeroshot_baseline(texts, labels, args):",
          "+    bl = _make_baseline(\"zeroshot\", args)",
          "+    _, eval_idx = train_test_split(",
          "+        np.arange(len(labels)), test_size=args.eval_split,",
          "+        stratify=labels, random_state=args.seed,",
          "+    )",
          "+    eval_texts = [texts[i] for i in eval_idx]",
          "+    eval_labels = labels[eval_idx]",
          "+",
          "+    if len(eval_texts) > args.max_eval_samples:",
          "+        rng = np.random.RandomState(args.seed)",
          "+        sample_idx = sorted(rng.choice(len(eval_texts), args.max_eval_samples, replace=False))",
          "+        eval_texts = [eval_texts[i] for i in sample_idx]",
          "+        eval_labels = eval_labels[sample_idx]",
          "+",
          "+    print(f\"Zero-shot: evaluating {len(eval_texts)} samples with {args.provider}/{bl.model}\")",
          "+    print(f\"  Label distribution: {dict(Counter(eval_labels))}\")",
          "+",
          "+    y_pred, y_prob = bl.predict_texts(eval_texts)",
          "+    return evaluate(BASELINE_REGISTRY[\"zeroshot\"], eval_labels, y_pred, y_prob)",
          "+",
          "+",
          " def parse_args():",
          "     p = argparse.ArgumentParser(description=\"Baseline battery for depth estimation.\")",
          "     p.add_argument(\"--method\", default=\"all\",",
          "-                   choices=[\"ppl_reg_single\", \"ppl_reg\", \"ce_mlp\", \"coral\", \"diveye\", \"all\"])",
          "-    p.add_argument(\"--features_path\", default=\"data/features_all.jsonl\")",
          "+                   choices=ALL_METHODS + [\"all\", \"all_features\"])",
          "+    p.add_argument(\"--features_path\", \"--data_path\", default=\"data/features_all.jsonl\",",
          "+                   dest=\"features_path\")",
          "+    p.add_argument(\"--data_dirs\", nargs=\"+\", default=[\"data/\"],",
          "+                   help=\"Directories containing depth_*.jsonl (for zero-shot)\")",
          "     p.add_argument(\"--output_dir\", default=\"results/baselines/\")",
          "     p.add_argument(\"--seed\", type=int, default=42)",
          "     p.add_argument(\"--test_size\", type=float, default=0.15)",
          "     p.add_argument(\"--val_size\", type=float, default=0.15)",
          "+    p.add_argument(\"--eval_split\", type=float, default=0.15)",
          "     p.add_argument(\"--epochs\", type=int, default=100)",
          "     p.add_argument(\"--batch_size\", type=int, default=256)",
          "     p.add_argument(\"--lr\", type=float, default=1e-3)",
          "     p.add_argument(\"--patience\", type=int, default=10)",
          "+    p.add_argument(\"--max_seq_len\", type=int, default=512)",
          "+    # Zero-shot LLM args",
          "+    p.add_argument(\"--provider\", choices=[\"claude\", \"openai\"], default=\"claude\")",
          "+    p.add_argument(\"--llm_model\", default=None,",
          "+                   help=\"LLM model name (default: claude-sonnet-4-20250514 / gpt-4o)\")",
          "+    p.add_argument(\"--max_eval_samples\", type=int, default=200,",
          "+                   help=\"Max samples for zero-shot eval (API cost control)\")",
          "+    p.add_argument(\"--rate_limit_delay\", type=float, default=0.5)",
          "     return p.parse_args()",
          " ",
          " ",
          " def main():",
          "     args = parse_args()",
          "-    print(f\"Loading features from {args.features_path} ...\")",
          "-    X, y = load_features(args.features_path)",
          "-    print(f\"  {X.shape[0]} samples, {X.shape[1]} features\")",
          "-    print(f\"  Depth distribution: {dict(Counter(y))}\")",
          " ",
          "-    X_train, y_train, X_val, y_val, X_test, y_test = prepare_splits(",
          "-        X, y, test_size=args.test_size, val_size=args.val_size, seed=args.seed",
          "-    )",
          "-    print(f\"  Train: {len(y_train)}, Val: {len(y_val)}, Test: {len(y_test)}\")",
          "+    if args.method == \"all\":",
          "+        methods = FEATURE_BASED_METHODS",
          "+        print(\"Running all feature-based baselines (use --method zeroshot for LLM baseline)\")",
          "+    elif args.method == \"all_features\":",
          "+        methods = FEATURE_BASED_METHODS",
          "+    else:",
          "+        methods = [args.method]",
          " ",
          "-    methods = list(BASELINE_REGISTRY.keys()) if args.method == \"all\" else [args.method]",
          "     all_results = {}",
          " ",
          "-    for m in methods:",
          "-        result = run_baseline(m, X_train, y_train, X_val, y_val, X_test, y_test, args)",
          "-        if result is not None:",
          "-            all_results[m] = result",
          "+    feature_methods = [m for m in methods if m in FEATURE_BASED_METHODS]",
          "+    text_methods = [m for m in methods if m in TEXT_BASED_METHODS]",
          " ",
          "-    # Summary table",
          "+    if feature_methods:",
          "+        print(f\"Loading features from {args.features_path} ...\")",
          "+        X, y = load_features(args.features_path)",
          "+        print(f\"  {X.shape[0]} samples, {X.shape[1]} features\")",
          "+        print(f\"  Depth distribution: {dict(Counter(y))}\")",
          "+",
          "+        X_train, y_train, X_val, y_val, X_test, y_test = prepare_splits(",
          "+            X, y, test_size=args.test_size, val_size=args.val_size, seed=args.seed",
          "+        )",
          "+        print(f\"  Train: {len(y_train)}, Val: {len(y_val)}, Test: {len(y_test)}\")",
          "+",
          "+        for m in feature_methods:",
          "+            result = run_feature_baseline(",
          "+                m, X_train, y_train, X_val, y_val, X_test, y_test, args",
          "+            )",
          "+            if result is not None:",
          "+                all_results[m] = result",
          "+",
          "+    if text_methods:",
          "+        if \"zeroshot\" in text_methods:",
          "+            texts, labels = load_jsonl_texts(",
          "+                args.data_dirs, max_samples=0, seed=args.seed",
          "+            )",
          "+            result = run_zeroshot_baseline(texts, labels, args)",
          "+            if result is not None:",
          "+                all_results[\"zeroshot\"] = result",
          "+",
          "     if len(all_results) > 1:",
          "         print(f\"\\n{'='*60}\")",
          "         print(f\"  SUMMARY\")"
        ]
      },
      {
        "oldStart": 676,
        "oldLines": 8,
        "newStart": 954,
        "newLines": 6,
        "lines": [
          "         print(f\"  {'-'*35} {'-'*6} {'-'*6} {'-'*6}\")",
          "         for m, r in all_results.items():",
          "             print(f\"  {r['method']:<35s} {r['acc_4class']:6.4f} {r['acc_3class']:6.4f} {r['mae']:6.4f}\")",
          "-        # Reference: RF MVP",
          "-        print(f\"  {'(ref) RF MVP':<35s} {'0.7815':>6s} {'—':>6s} {'—':>6s}\")",
          " ",
          "     os.makedirs(args.output_dir, exist_ok=True)",
          "     out_path = os.path.join(args.output_dir, \"baseline_results.json\")"
        ]
      }
    ],
    "originalFile": "\"\"\"\nBaseline battery for recursive generation depth estimation.\n\nBaselines:\n  1. PPLRegressionBaseline  — OLS regression on mean_ppl (single) or all 19 features (multi)\n  2. CEClassificationBaseline — MLP with cross-entropy loss (DCOL ablation, no contrastive loss)\n  3. CORALBaseline — Ordinal regression with K-1 binary classifiers (Cao et al., 2020)\n  4. DivEyeBaseline — Surprisal diversity features + XGBoost (Basani & Chen, TMLR 2026)\n\nUsage:\n  python src/baselines.py --method ppl_reg --features_path data/features_all.jsonl\n  python src/baselines.py --method ce_mlp  --features_path data/features_all.jsonl --epochs 50\n  python src/baselines.py --method coral   --features_path data/features_all.jsonl --epochs 50\n  python src/baselines.py --method diveye  --features_path data/features_all.jsonl\n  python src/baselines.py --method all     --features_path data/features_all.jsonl --epochs 50\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport sys\nimport numpy as np\nfrom collections import Counter\n\nimport torch\nimport torch.nn as nn\nimport torch.optim as optim\nfrom torch.utils.data import DataLoader, TensorDataset\n\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.metrics import (\n    accuracy_score, confusion_matrix, classification_report, roc_auc_score,\n)\n\n# ── Feature schema (must match extract_features.py / dcol_dataset.py) ──\n\nFEATURE_NAMES = [\n    \"mean_ppl\", \"var_ppl\", \"skewness_ppl\", \"kurtosis_ppl\",\n    \"p10_ppl\", \"p25_ppl\", \"p50_ppl\", \"p75_ppl\", \"p90_ppl\",\n    \"mean_surprisal\", \"var_surprisal\", \"entropy_of_surprisal\",\n    \"type_token_ratio\", \"hapax_ratio\", \"bigram_entropy\", \"trigram_entropy\",\n    \"rep_2gram\", \"rep_3gram\", \"rep_4gram\",\n]\nNUM_FEATURES = len(FEATURE_NAMES)\nNUM_DEPTHS = 4\nDEPTH_LABELS = list(range(NUM_DEPTHS))\n\n# ── Data loading ──\n\ndef load_features(path):\n    \"\"\"Load JSONL features file → (X [n, 19], y [n]).\"\"\"\n    records = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                records.append(json.loads(line))\n    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)\n    y = np.array([r[\"depth\"] for r in records], dtype=np.int64)\n    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)\n    return X, y\n\n\ndef prepare_splits(X, y, test_size=0.15, val_size=0.15, seed=42):\n    idx = np.arange(len(y))\n    train_val_idx, test_idx = train_test_split(\n        idx, test_size=test_size, stratify=y, random_state=seed\n    )\n    rel_val = val_size / (1 - test_size)\n    train_idx, val_idx = train_test_split(\n        train_val_idx, test_size=rel_val,\n        stratify=y[train_val_idx], random_state=seed\n    )\n    return (\n        X[train_idx], y[train_idx],\n        X[val_idx], y[val_idx],\n        X[test_idx], y[test_idx],\n    )\n\n# ── Evaluation metrics ──\n\ndef pairwise_auc(y_true, y_prob, d1, d2):\n    mask = np.isin(y_true, [d1, d2])\n    if mask.sum() < 2:\n        return None\n    yt = (y_true[mask] == d2).astype(int)\n    if len(np.unique(yt)) < 2:\n        return None\n    yp = y_prob[mask, d2]\n    return float(roc_auc_score(yt, yp))\n\n\ndef compute_all_pairwise_auc(y_true, y_prob):\n    result = {}\n    for i, d1 in enumerate(DEPTH_LABELS):\n        for d2 in DEPTH_LABELS[i + 1:]:\n            auc = pairwise_auc(y_true, y_prob, d1, d2)\n            result[f\"d{d1}_vs_d{d2}\"] = round(auc, 4) if auc is not None else None\n    return result\n\n\ndef bootstrap_ci(y_true, y_pred, metric_fn=accuracy_score, n_boot=1000, seed=42):\n    rng = np.random.RandomState(seed)\n    scores = []\n    n = len(y_true)\n    for _ in range(n_boot):\n        idx = rng.choice(n, n, replace=True)\n        scores.append(metric_fn(y_true[idx], y_pred[idx]))\n    lo = float(np.percentile(scores, 2.5))\n    hi = float(np.percentile(scores, 97.5))\n    return lo, hi\n\n\ndef evaluate(name, y_true, y_pred, y_prob=None):\n    \"\"\"Print and return evaluation metrics.\"\"\"\n    acc4 = accuracy_score(y_true, y_pred)\n    ci_lo, ci_hi = bootstrap_ci(y_true, y_pred)\n\n    # 3-class accuracy (depth 1-3 only)\n    mask_13 = y_true >= 1\n    acc3 = accuracy_score(y_true[mask_13], y_pred[mask_13]) if mask_13.sum() > 0 else 0.0\n\n    mae = float(np.mean(np.abs(y_true - y_pred)))\n\n    cm = confusion_matrix(y_true, y_pred, labels=DEPTH_LABELS)\n    per_class_recall = cm.diagonal() / cm.sum(axis=1).clip(min=1)\n\n    pair_aucs = {}\n    if y_prob is not None:\n        pair_aucs = compute_all_pairwise_auc(y_true, y_prob)\n\n    print(f\"\\n{'='*60}\")\n    print(f\"  {name}\")\n    print(f\"{'='*60}\")\n    print(f\"  4-class accuracy : {acc4:.4f}  (95% CI: [{ci_lo:.4f}, {ci_hi:.4f}])\")\n    print(f\"  3-class accuracy : {acc3:.4f}  (d1-d3 only)\")\n    print(f\"  MAE              : {mae:.4f}\")\n    print(f\"  Per-class recall : {dict(zip([f'd{d}' for d in DEPTH_LABELS], [round(r,4) for r in per_class_recall]))}\")\n    if pair_aucs:\n        print(f\"  Pairwise AUC     : {pair_aucs}\")\n    print(f\"\\n  Confusion matrix:\")\n    print(f\"  {'':>8s}\", \" \".join(f\"pred-{d}\" for d in DEPTH_LABELS))\n    for i, d in enumerate(DEPTH_LABELS):\n        print(f\"  true-{d}  \", \" \".join(f\"{cm[i,j]:6d}\" for j in range(NUM_DEPTHS)))\n\n    cr = classification_report(\n        y_true, y_pred,\n        target_names=[f\"depth-{d}\" for d in DEPTH_LABELS],\n        zero_division=0,\n    )\n    print(f\"\\n{cr}\")\n\n    return {\n        \"method\": name,\n        \"acc_4class\": round(acc4, 4),\n        \"acc_4class_ci\": [round(ci_lo, 4), round(ci_hi, 4)],\n        \"acc_3class\": round(acc3, 4),\n        \"mae\": round(mae, 4),\n        \"per_class_recall\": {f\"d{d}\": round(r, 4) for d, r in zip(DEPTH_LABELS, per_class_recall)},\n        \"pairwise_auc\": pair_aucs,\n    }\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  Baseline 1: PPL Regression\n# ═══════════════════════════════════════════════════════════════════════\n\nclass PPLRegressionBaseline:\n    \"\"\"\n    Linear regression → round to nearest depth.\n\n    Single-feature mode: depth = a * mean_ppl + b\n    Multi-feature mode:  depth = X @ w + b  (19-dim OLS)\n\n    Simplest possible baseline. If mean_ppl alone suffices, complex models are\n    unnecessary.\n    \"\"\"\n\n    def __init__(self, mode=\"multi\"):\n        self.mode = mode  # \"single\" or \"multi\"\n        self.scaler = StandardScaler()\n        self.model = LinearRegression()\n\n    def _select(self, X):\n        if self.mode == \"single\":\n            idx = FEATURE_NAMES.index(\"mean_ppl\")\n            return X[:, idx:idx+1]\n        return X\n\n    def fit(self, X_train, y_train):\n        Xs = self._select(X_train)\n        Xs = self.scaler.fit_transform(Xs)\n        self.model.fit(Xs, y_train.astype(np.float64))\n\n    def predict(self, X_test):\n        Xs = self._select(X_test)\n        Xs = self.scaler.transform(Xs)\n        raw = self.model.predict(Xs)\n        return np.clip(np.round(raw).astype(int), 0, NUM_DEPTHS - 1)\n\n    def predict_proba(self, X_test):\n        preds = self.predict(X_test)\n        prob = np.zeros((len(preds), NUM_DEPTHS))\n        for i, p in enumerate(preds):\n            prob[i, p] = 1.0\n        return prob\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  Baseline 2: Cross-Entropy MLP (DCOL ablation)\n# ═══════════════════════════════════════════════════════════════════════\n\nclass _CEMLP(nn.Module):\n    \"\"\"19 → 128 → 64 → 4  with ReLU + dropout. Same architecture as DCOL's\n    feature head, but trained with CE loss only (no contrastive loss).\"\"\"\n\n    def __init__(self, input_dim=NUM_FEATURES, hidden1=128, hidden2=64,\n                 num_classes=NUM_DEPTHS, dropout=0.3):\n        super().__init__()\n        self.net = nn.Sequential(\n            nn.Linear(input_dim, hidden1),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n            nn.Linear(hidden1, hidden2),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n            nn.Linear(hidden2, num_classes),\n        )\n\n    def forward(self, x):\n        return self.net(x)\n\n\nclass CEClassificationBaseline:\n    \"\"\"\n    Standard multi-class MLP with cross-entropy loss.\n\n    Architecture identical to DCOL's feature classifier head (19→128→64→4)\n    but uses only CE loss — no contrastive learning.\n    This is the key ablation: if CE-MLP matches DCOL, the contrastive loss\n    adds no value.\n    \"\"\"\n\n    def __init__(self, lr=1e-3, epochs=100, batch_size=256, patience=10,\n                 device=None, seed=42):\n        self.lr = lr\n        self.epochs = epochs\n        self.batch_size = batch_size\n        self.patience = patience\n        self.device = device or (\"cuda\" if torch.cuda.is_available() else \"cpu\")\n        self.seed = seed\n        self.scaler = StandardScaler()\n        self.model = None\n\n    def fit(self, X_train, y_train, X_val=None, y_val=None):\n        torch.manual_seed(self.seed)\n        np.random.seed(self.seed)\n\n        X_s = self.scaler.fit_transform(X_train).astype(np.float32)\n        Xt = torch.tensor(X_s, device=self.device)\n        yt = torch.tensor(y_train, dtype=torch.long, device=self.device)\n        ds = TensorDataset(Xt, yt)\n        loader = DataLoader(ds, batch_size=self.batch_size, shuffle=True)\n\n        self.model = _CEMLP().to(self.device)\n        optimizer = optim.Adam(self.model.parameters(), lr=self.lr, weight_decay=1e-4)\n        criterion = nn.CrossEntropyLoss()\n\n        best_loss = float(\"inf\")\n        wait = 0\n        best_state = None\n\n        has_val = X_val is not None and y_val is not None\n        if has_val:\n            Xv = torch.tensor(self.scaler.transform(X_val).astype(np.float32),\n                              device=self.device)\n            yv = torch.tensor(y_val, dtype=torch.long, device=self.device)\n\n        for epoch in range(self.epochs):\n            self.model.train()\n            epoch_loss = 0.0\n            for xb, yb in loader:\n                optimizer.zero_grad()\n                logits = self.model(xb)\n                loss = criterion(logits, yb)\n                loss.backward()\n                optimizer.step()\n                epoch_loss += loss.item() * len(xb)\n            epoch_loss /= len(ds)\n\n            if has_val:\n                self.model.eval()\n                with torch.no_grad():\n                    val_logits = self.model(Xv)\n                    val_loss = criterion(val_logits, yv).item()\n            else:\n                val_loss = epoch_loss\n\n            if val_loss < best_loss - 1e-4:\n                best_loss = val_loss\n                best_state = {k: v.clone() for k, v in self.model.state_dict().items()}\n                wait = 0\n            else:\n                wait += 1\n                if wait >= self.patience:\n                    break\n\n        if best_state is not None:\n            self.model.load_state_dict(best_state)\n\n    def predict(self, X_test):\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n        return logits.argmax(dim=-1).cpu().numpy()\n\n    def predict_proba(self, X_test):\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n            probs = torch.softmax(logits, dim=-1)\n        return probs.cpu().numpy()\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  Baseline 3: CORAL Ordinal Regression\n# ═══════════════════════════════════════════════════════════════════════\n\nclass _CORALNet(nn.Module):\n    \"\"\"\n    CORAL ordinal regression (Cao et al., 2020, \"Rank consistent ordinal\n    regression for neural networks with consistent confidence sets\").\n\n    Architecture: 19 → 128 → 64 → shared representation, then K-1 = 3\n    independent sigmoid heads.\n\n    Each head k answers: P(depth > k).\n    Prediction: depth = sum_k I[P(depth > k) > 0.5].\n\n    Loss (rank-consistent):\n        L = sum_{k=0}^{K-2} BCE(sigmoid(w_k^T h + b_k), I[y > k])\n\n    Weight sharing across heads ensures rank consistency: predictions are\n    monotonically decreasing in threshold order.\n    \"\"\"\n\n    def __init__(self, input_dim=NUM_FEATURES, hidden1=128, hidden2=64,\n                 num_classes=NUM_DEPTHS, dropout=0.3):\n        super().__init__()\n        self.num_classes = num_classes\n        self.backbone = nn.Sequential(\n            nn.Linear(input_dim, hidden1),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n            nn.Linear(hidden1, hidden2),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n        )\n        # K-1 independent binary heads (shared backbone, separate bias)\n        self.fc = nn.Linear(hidden2, 1, bias=False)\n        self.biases = nn.Parameter(torch.zeros(num_classes - 1))\n\n    def forward(self, x):\n        h = self.backbone(x)             # [B, 64]\n        logit_base = self.fc(h)          # [B, 1]\n        # broadcast: [B, K-1]\n        logits = logit_base + self.biases # each head shares weight, different bias\n        return logits\n\n\nclass CORALBaseline:\n    \"\"\"\n    CORAL ordinal regression for depth estimation.\n\n    Ref: Cao, Mirjalili & Raschka (2020). \"Rank consistent ordinal regression\n    for neural networks with consistent confidence sets.\" Pattern Recognition.\n\n    Exploits ordinal structure: depth 0 < 1 < 2 < 3.\n    Alternative to DCOL's contrastive approach for leveraging label ordering.\n    \"\"\"\n\n    def __init__(self, lr=1e-3, epochs=100, batch_size=256, patience=10,\n                 device=None, seed=42):\n        self.lr = lr\n        self.epochs = epochs\n        self.batch_size = batch_size\n        self.patience = patience\n        self.device = device or (\"cuda\" if torch.cuda.is_available() else \"cpu\")\n        self.seed = seed\n        self.scaler = StandardScaler()\n        self.model = None\n\n    @staticmethod\n    def _encode_ordinal(y, num_classes):\n        \"\"\"Convert class labels to K-1 binary ordinal targets.\n        y=2, K=4 → [1, 1, 0]  (depth > 0? yes, depth > 1? yes, depth > 2? no)\n        \"\"\"\n        n = len(y)\n        targets = np.zeros((n, num_classes - 1), dtype=np.float32)\n        for k in range(num_classes - 1):\n            targets[:, k] = (y > k).astype(np.float32)\n        return targets\n\n    def fit(self, X_train, y_train, X_val=None, y_val=None):\n        torch.manual_seed(self.seed)\n        np.random.seed(self.seed)\n\n        X_s = self.scaler.fit_transform(X_train).astype(np.float32)\n        ord_targets = self._encode_ordinal(y_train, NUM_DEPTHS)\n\n        Xt = torch.tensor(X_s, device=self.device)\n        ot = torch.tensor(ord_targets, device=self.device)\n        ds = TensorDataset(Xt, ot)\n        loader = DataLoader(ds, batch_size=self.batch_size, shuffle=True)\n\n        self.model = _CORALNet().to(self.device)\n        optimizer = optim.Adam(self.model.parameters(), lr=self.lr, weight_decay=1e-4)\n        criterion = nn.BCEWithLogitsLoss()\n\n        best_loss = float(\"inf\")\n        wait = 0\n        best_state = None\n\n        has_val = X_val is not None and y_val is not None\n        if has_val:\n            Xv = torch.tensor(self.scaler.transform(X_val).astype(np.float32),\n                              device=self.device)\n            ov = torch.tensor(self._encode_ordinal(y_val, NUM_DEPTHS),\n                              device=self.device)\n\n        for epoch in range(self.epochs):\n            self.model.train()\n            epoch_loss = 0.0\n            for xb, ob in loader:\n                optimizer.zero_grad()\n                logits = self.model(xb)\n                loss = criterion(logits, ob)\n                loss.backward()\n                optimizer.step()\n                epoch_loss += loss.item() * len(xb)\n            epoch_loss /= len(ds)\n\n            if has_val:\n                self.model.eval()\n                with torch.no_grad():\n                    val_logits = self.model(Xv)\n                    val_loss = criterion(val_logits, ov).item()\n            else:\n                val_loss = epoch_loss\n\n            if val_loss < best_loss - 1e-4:\n                best_loss = val_loss\n                best_state = {k: v.clone() for k, v in self.model.state_dict().items()}\n                wait = 0\n            else:\n                wait += 1\n                if wait >= self.patience:\n                    break\n\n        if best_state is not None:\n            self.model.load_state_dict(best_state)\n\n    def predict(self, X_test):\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n            probs = torch.sigmoid(logits)  # [B, K-1], P(depth > k)\n        # depth = number of thresholds exceeded\n        preds = (probs > 0.5).sum(dim=-1).cpu().numpy().astype(int)\n        return preds\n\n    def predict_proba(self, X_test):\n        \"\"\"Convert cumulative probabilities to per-class probabilities.\n        P(depth=k) = P(depth>k-1) - P(depth>k), with boundary conditions.\n        \"\"\"\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n            cum_probs = torch.sigmoid(logits).cpu().numpy()  # [B, K-1]\n\n        n = len(X_test)\n        probs = np.zeros((n, NUM_DEPTHS))\n        # P(depth=0) = 1 - P(depth>0)\n        probs[:, 0] = 1.0 - cum_probs[:, 0]\n        # P(depth=k) = P(depth>k-1) - P(depth>k) for k=1..K-2\n        for k in range(1, NUM_DEPTHS - 1):\n            probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]\n        # P(depth=K-1) = P(depth>K-2)\n        probs[:, NUM_DEPTHS - 1] = cum_probs[:, NUM_DEPTHS - 2]\n        probs = np.clip(probs, 0, 1)\n        row_sums = probs.sum(axis=1, keepdims=True)\n        probs = probs / np.where(row_sums > 0, row_sums, 1.0)\n        return probs\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  Baseline 4: DivEye (Surprisal Diversity + XGBoost)\n# ═══════════════════════════════════════════════════════════════════════\n\n# DivEye feature groups mapped to our 19 features:\n#   Distributional: mean_ppl, var_ppl, skewness_ppl, kurtosis_ppl → matches\n#                   DivEye's mean/var/skewness/kurtosis of surprisal\n#   Surprisal:      mean_surprisal, var_surprisal, entropy_of_surprisal\n#   Lexical diversity: type_token_ratio, hapax_ratio, bigram_entropy, trigram_entropy\n#   Repetition:     rep_2gram, rep_3gram, rep_4gram\n#\n# TODO: DivEye's temporal features (first-order ∆S and second-order ∆²S,\n#       computed from per-token surprisal sequences) are not available in our\n#       pre-computed features. Full DivEye reproduction requires raw token-level\n#       surprisal; these summary statistics are a proxy.\n\nDIVEYE_FEATURE_INDICES = [\n    FEATURE_NAMES.index(f) for f in [\n        \"mean_ppl\", \"var_ppl\", \"skewness_ppl\", \"kurtosis_ppl\",\n        \"mean_surprisal\", \"var_surprisal\", \"entropy_of_surprisal\",\n        \"type_token_ratio\", \"hapax_ratio\", \"bigram_entropy\", \"trigram_entropy\",\n        \"rep_2gram\", \"rep_3gram\", \"rep_4gram\",\n    ]\n]\n\n\nclass DivEyeBaseline:\n    \"\"\"\n    DivEye-style detection adapted for depth estimation.\n\n    Ref: Basani, A. R. & Chen, P.-Y. (2026). Diversity Boosts AI-Generated Text Detection. Transactions on Machine Learning Research (TMLR).\n    GitHub: https://github.com/IBM/diveye\n\n    DivEye's insight: human text has higher surprisal diversity (distributional,\n    first-order temporal ∆S, second-order ∆²S). We adapt this to depth estimation:\n    deeper recursive generations should have *lower* diversity.\n\n    Implementation: XGBoost on surprisal-related feature subset (14 of 19 features).\n    Full DivEye also uses first/second-order temporal surprisal features from raw\n    token sequences — those are not available in our pre-extracted features.\n    \"\"\"\n\n    def __init__(self, seed=42):\n        self.seed = seed\n        self.model = None\n\n    def fit(self, X_train, y_train, **kwargs):\n        try:\n            from xgboost import XGBClassifier\n        except ImportError:\n            print(\"[ERROR] xgboost not installed. Run: pip install xgboost\")\n            sys.exit(1)\n\n        Xd = X_train[:, DIVEYE_FEATURE_INDICES]\n        self.model = XGBClassifier(\n            n_estimators=200,\n            max_depth=6,\n            learning_rate=0.1,\n            subsample=0.8,\n            colsample_bytree=0.8,\n            random_state=self.seed,\n            use_label_encoder=False,\n            eval_metric=\"mlogloss\",\n            verbosity=0,\n        )\n        self.model.fit(Xd, y_train)\n\n    def predict(self, X_test):\n        Xd = X_test[:, DIVEYE_FEATURE_INDICES]\n        return self.model.predict(Xd)\n\n    def predict_proba(self, X_test):\n        Xd = X_test[:, DIVEYE_FEATURE_INDICES]\n        probs = self.model.predict_proba(Xd)\n        # Ensure output is [n, NUM_DEPTHS] even if some classes are missing\n        if probs.shape[1] < NUM_DEPTHS:\n            full = np.zeros((probs.shape[0], NUM_DEPTHS))\n            for i, c in enumerate(self.model.classes_):\n                full[:, c] = probs[:, i]\n            return full\n        return probs\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  Unified Runner\n# ═══════════════════════════════════════════════════════════════════════\n\nBASELINE_REGISTRY = {\n    \"ppl_reg_single\": (\"PPL Regression (single: mean_ppl)\", lambda: PPLRegressionBaseline(mode=\"single\")),\n    \"ppl_reg\":        (\"PPL Regression (multi: 19-dim OLS)\", lambda: PPLRegressionBaseline(mode=\"multi\")),\n    \"ce_mlp\":         (\"CE-MLP (DCOL ablation)\", None),  # needs args\n    \"coral\":          (\"CORAL Ordinal Regression\", None),\n    \"diveye\":         (\"DivEye (XGBoost)\", lambda: DivEyeBaseline()),\n}\n\n\ndef run_baseline(method, X_train, y_train, X_val, y_val, X_test, y_test, args):\n    if method == \"ppl_reg_single\":\n        bl = PPLRegressionBaseline(mode=\"single\")\n        bl.fit(X_train, y_train)\n    elif method == \"ppl_reg\":\n        bl = PPLRegressionBaseline(mode=\"multi\")\n        bl.fit(X_train, y_train)\n    elif method == \"ce_mlp\":\n        bl = CEClassificationBaseline(\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\n            patience=args.patience, seed=args.seed,\n        )\n        bl.fit(X_train, y_train, X_val, y_val)\n    elif method == \"coral\":\n        bl = CORALBaseline(\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\n            patience=args.patience, seed=args.seed,\n        )\n        bl.fit(X_train, y_train, X_val, y_val)\n    elif method == \"diveye\":\n        bl = DivEyeBaseline(seed=args.seed)\n        bl.fit(X_train, y_train)\n    else:\n        print(f\"Unknown method: {method}\")\n        return None\n\n    y_pred = bl.predict(X_test)\n    y_prob = bl.predict_proba(X_test)\n    name = BASELINE_REGISTRY.get(method, (method, None))[0]\n    return evaluate(name, y_test, y_pred, y_prob)\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"Baseline battery for depth estimation.\")\n    p.add_argument(\"--method\", default=\"all\",\n                   choices=[\"ppl_reg_single\", \"ppl_reg\", \"ce_mlp\", \"coral\", \"diveye\", \"all\"])\n    p.add_argument(\"--features_path\", default=\"data/features_all.jsonl\")\n    p.add_argument(\"--output_dir\", default=\"results/baselines/\")\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--test_size\", type=float, default=0.15)\n    p.add_argument(\"--val_size\", type=float, default=0.15)\n    p.add_argument(\"--epochs\", type=int, default=100)\n    p.add_argument(\"--batch_size\", type=int, default=256)\n    p.add_argument(\"--lr\", type=float, default=1e-3)\n    p.add_argument(\"--patience\", type=int, default=10)\n    return p.parse_args()\n\n\ndef main():\n    args = parse_args()\n    print(f\"Loading features from {args.features_path} ...\")\n    X, y = load_features(args.features_path)\n    print(f\"  {X.shape[0]} samples, {X.shape[1]} features\")\n    print(f\"  Depth distribution: {dict(Counter(y))}\")\n\n    X_train, y_train, X_val, y_val, X_test, y_test = prepare_splits(\n        X, y, test_size=args.test_size, val_size=args.val_size, seed=args.seed\n    )\n    print(f\"  Train: {len(y_train)}, Val: {len(y_val)}, Test: {len(y_test)}\")\n\n    methods = list(BASELINE_REGISTRY.keys()) if args.method == \"all\" else [args.method]\n    all_results = {}\n\n    for m in methods:\n        result = run_baseline(m, X_train, y_train, X_val, y_val, X_test, y_test, args)\n        if result is not None:\n            all_results[m] = result\n\n    # Summary table\n    if len(all_results) > 1:\n        print(f\"\\n{'='*60}\")\n        print(f\"  SUMMARY\")\n        print(f\"{'='*60}\")\n        print(f\"  {'Method':<35s} {'4-cls':>6s} {'3-cls':>6s} {'MAE':>6s}\")\n        print(f\"  {'-'*35} {'-'*6} {'-'*6} {'-'*6}\")\n        for m, r in all_results.items():\n            print(f\"  {r['method']:<35s} {r['acc_4class']:6.4f} {r['acc_3class']:6.4f} {r['mae']:6.4f}\")\n        # Reference: RF MVP\n        print(f\"  {'(ref) RF MVP':<35s} {'0.7815':>6s} {'—':>6s} {'—':>6s}\")\n\n    os.makedirs(args.output_dir, exist_ok=True)\n    out_path = os.path.join(args.output_dir, \"baseline_results.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(all_results, f, indent=2, default=str)\n    print(f\"\\nResults saved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "userModified": false
  }
}
```

</details>

---


### Assistant

_source line 151_

Now deploying to server and running dry-run validation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "23cea151-6c80-4de0-bf62-df89a60f6a78",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KvrPDdLjfak5pJ5Nkxhuen",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12144,
      "cache_read_input_tokens": 80975,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12144
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

_source line 152_

<details open><summary>🔧 Tool call — Read · `toolu_01L8fscmKpkiGjXLcLWGeMgZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/baselines.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "937ace78-ec56-4fdb-93fe-da50135e1753",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KvrPDdLjfak5pJ5Nkxhuen",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12144,
      "cache_read_input_tokens": 80975,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12144
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

_source line 153 · 2026-05-14T23:07:08.817Z_

<details><summary>↩ Tool result · `toolu_01L8fscmKpkiGjXLcLWGeMgZ`</summary>

```text
1	"""
2	Baseline battery for recursive generation depth estimation.
3	
4	Baselines (feature-based, 19-dim input):
5	  1. PPLRegressionBaseline  -- OLS regression on mean_ppl (single) or all 19 features (multi)
6	  2. CEClassificationBaseline -- MLP with cross-entropy loss (DCOL ablation, no contrastive loss)
7	  3. CORALBaseline -- Ordinal regression with K-1 binary classifiers (Cao et al., 2020)
8	  4. DivEyeBaseline -- Surprisal diversity features + XGBoost (Basani & Chen, TMLR 2026)
9	  5. RandomForestBaseline -- sklearn RF on 19-dim features
10	  6. LogisticRegressionBaseline -- sklearn LR on 19-dim features
11	
12	Baselines (text-based, raw text input):
13	  7. ZeroShotLLMBaseline -- Prompt an LLM (Claude/OpenAI) to classify depth directly
14	
15	Usage:
16	  python src/baselines.py --method ppl_reg --features_path data/features_all.jsonl
17	  python src/baselines.py --method ce_mlp  --features_path data/features_all.jsonl --epochs 50
18	  python src/baselines.py --method coral   --features_path data/features_all.jsonl --epochs 50
19	  python src/baselines.py --method diveye  --features_path data/features_all.jsonl
20	  python src/baselines.py --method rf      --features_path data/features_all.jsonl
21	  python src/baselines.py --method lr      --features_path data/features_all.jsonl
22	  python src/baselines.py --method zeroshot --data_dirs data/ --provider claude --max_eval_samples 200
23	  python src/baselines.py --method all     --features_path data/features_all.jsonl --epochs 50
24	"""
25	
26	import argparse
27	import json
28	import os
29	import re
30	import sys
31	import time
32	import numpy as np
33	from collections import Counter
34	
35	import torch
36	import torch.nn as nn
37	import torch.optim as optim
38	from torch.utils.data import DataLoader, TensorDataset
39	
40	from sklearn.linear_model import LinearRegression
41	from sklearn.preprocessing import StandardScaler
42	from sklearn.model_selection import train_test_split
43	from sklearn.metrics import (
44	    accuracy_score, confusion_matrix, classification_report, roc_auc_score,
45	)
46	
47	# -- Feature schema (must match extract_features.py / dcol_dataset.py) --
48	
49	FEATURE_NAMES = [
50	    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
51	    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
52	    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
53	    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
54	    "rep_2gram", "rep_3gram", "rep_4gram",
55	]
56	NUM_FEATURES = len(FEATURE_NAMES)
57	NUM_DEPTHS = 4
58	DEPTH_LABELS = list(range(NUM_DEPTHS))
59	
60	# -- Data loading --
61	
62	def load_features(path):
63	    """Load JSONL features file -> (X [n, 19], y [n])."""
64	    records = []
65	    with open(path) as f:
66	        for line in f:
67	            line = line.strip()
68	            if line:
69	                records.append(json.loads(line))
70	    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)
71	    y = np.array([r["depth"] for r in records], dtype=np.int64)
72	    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
73	    return X, y
74	
75	
76	def load_jsonl_texts(data_dirs, max_samples=0, seed=42):
77	    """Load raw text + depth labels from depth_*.jsonl files across directories."""
78	    import glob as glob_mod
79	    texts, labels = [], []
80	    for data_dir in data_dirs:
81	        for d in range(NUM_DEPTHS):
82	            fpath = os.path.join(data_dir, f"depth_{d}.jsonl")
83	            if not os.path.exists(fpath):
84	                matches = glob_mod.glob(os.path.join(data_dir, f"*depth_{d}*.jsonl"))
85	                fpath = matches[0] if matches else None
86	            if fpath is None or not os.path.exists(fpath):
87	                continue
88	            with open(fpath) as f:
89	                for line in f:
90	                    line = line.strip()
91	                    if not line:
92	                        continue
93	                    rec = json.loads(line)
94	                    texts.append(rec["text"])
95	                    labels.append(rec.get("depth", d))
96	    labels = np.array(labels, dtype=np.int64)
97	    if max_samples > 0 and len(texts) > max_samples:
98	        rng = np.random.RandomState(seed)
99	        idx = sorted(rng.choice(len(texts), max_samples, replace=False))
100	        texts = [texts[i] for i in idx]
101	        labels = labels[idx]
102	    print(f"Loaded {len(texts)} text samples. Depth distribution: {dict(Counter(labels))}")
103	    return texts, labels
104	
105	
106	def prepare_splits(X, y, test_size=0.15, val_size=0.15, seed=42):
107	    idx = np.arange(len(y))
108	    train_val_idx, test_idx = train_test_split(
109	        idx, test_size=test_size, stratify=y, random_state=seed
110	    )
111	    rel_val = val_size / (1 - test_size)
112	    train_idx, val_idx = train_test_split(
113	        train_val_idx, test_size=rel_val,
114	        stratify=y[train_val_idx], random_state=seed
115	    )
116	    return (
117	        X[train_idx], y[train_idx],
118	        X[val_idx], y[val_idx],
119	        X[test_idx], y[test_idx],
120	    )
121	
122	# -- Evaluation metrics --
123	
124	def pairwise_auc(y_true, y_prob, d1, d2):
125	    mask = np.isin(y_true, [d1, d2])
126	    if mask.sum() < 2:
127	        return None
128	    yt = (y_true[mask] == d2).astype(int)
129	    if len(np.unique(yt)) < 2:
130	        return None
131	    yp = y_prob[mask, d2]
132	    return float(roc_auc_score(yt, yp))
133	
134	
135	def compute_all_pairwise_auc(y_true, y_prob):
136	    result = {}
137	    for i, d1 in enumerate(DEPTH_LABELS):
138	        for d2 in DEPTH_LABELS[i + 1:]:
139	            auc = pairwise_auc(y_true, y_prob, d1, d2)
140	            result[f"d{d1}_vs_d{d2}"] = round(auc, 4) if auc is not None else None
141	    return result
142	
143	
144	def bootstrap_ci(y_true, y_pred, metric_fn=accuracy_score, n_boot=1000, seed=42):
145	    rng = np.random.RandomState(seed)
146	    scores = []
147	    n = len(y_true)
148	    for _ in range(n_boot):
149	        idx = rng.choice(n, n, replace=True)
150	        scores.append(metric_fn(y_true[idx], y_pred[idx]))
151	    lo = float(np.percentile(scores, 2.5))
152	    hi = float(np.percentile(scores, 97.5))
153	    return lo, hi
154	
155	
156	def evaluate(name, y_true, y_pred, y_prob=None):
157	    """Print and return evaluation metrics."""
158	    acc4 = accuracy_score(y_true, y_pred)
159	    ci_lo, ci_hi = bootstrap_ci(y_true, y_pred)
160	
161	    mask_13 = y_true >= 1
162	    acc3 = accuracy_score(y_true[mask_13], y_pred[mask_13]) if mask_13.sum() > 0 else 0.0
163	
164	    mae = float(np.mean(np.abs(y_true - y_pred)))
165	
166	    cm = confusion_matrix(y_true, y_pred, labels=DEPTH_LABELS)
167	    per_class_recall = cm.diagonal() / cm.sum(axis=1).clip(min=1)
168	
169	    pair_aucs = {}
170	    if y_prob is not None:
171	        pair_aucs = compute_all_pairwise_auc(y_true, y_prob)
172	
173	    print(f"\n{'='*60}")
174	    print(f"  {name}")
175	    print(f"{'='*60}")
176	    print(f"  4-class accuracy : {acc4:.4f}  (95% CI: [{ci_lo:.4f}, {ci_hi:.4f}])")
177	    print(f"  3-class accuracy : {acc3:.4f}  (d1-d3 only)")
178	    print(f"  MAE              : {mae:.4f}")
179	    print(f"  Per-class recall : {dict(zip([f'd{d}' for d in DEPTH_LABELS], [round(r,4) for r in per_class_recall]))}")
180	    if pair_aucs:
181	        print(f"  Pairwise AUC     : {pair_aucs}")
182	    print(f"\n  Confusion matrix:")
183	    print(f"  {'':>8s}", " ".join(f"pred-{d}" for d in DEPTH_LABELS))
184	    for i, d in enumerate(DEPTH_LABELS):
185	        print(f"  true-{d}  ", " ".join(f"{cm[i,j]:6d}" for j in range(NUM_DEPTHS)))
186	
187	    cr = classification_report(
188	        y_true, y_pred,
189	        target_names=[f"depth-{d}" for d in DEPTH_LABELS],
190	        zero_division=0,
191	    )
192	    print(f"\n{cr}")
193	
194	    return {
195	        "method": name,
196	        "acc_4class": round(acc4, 4),
197	        "acc_4class_ci": [round(ci_lo, 4), round(ci_hi, 4)],
198	        "acc_3class": round(acc3, 4),
199	        "mae": round(mae, 4),
200	        "per_class_recall": {f"d{d}": round(r, 4) for d, r in zip(DEPTH_LABELS, per_class_recall)},
201	        "pairwise_auc": pair_aucs,
202	    }
203	
204	
205	# ===================================================================
206	#  Baseline 1: PPL Regression
207	# ===================================================================
208	
209	class PPLRegressionBaseline:
210	    """
211	    Linear regression -> round to nearest depth.
212	    Single-feature mode: depth = a * mean_ppl + b
213	    Multi-feature mode:  depth = X @ w + b  (19-dim OLS)
214	    """
215	
216	    def __init__(self, mode="multi"):
217	        self.mode = mode
218	        self.scaler = StandardScaler()
219	        self.model = LinearRegression()
220	
221	    def _select(self, X):
222	        if self.mode == "single":
223	            idx = FEATURE_NAMES.index("mean_ppl")
224	            return X[:, idx:idx+1]
225	        return X
226	
227	    def fit(self, X_train, y_train, **kwargs):
228	        Xs = self._select(X_train)
229	        Xs = self.scaler.fit_transform(Xs)
230	        self.model.fit(Xs, y_train.astype(np.float64))
231	
232	    def predict(self, X_test):
233	        Xs = self._select(X_test)
234	        Xs = self.scaler.transform(Xs)
235	        raw = self.model.predict(Xs)
236	        return np.clip(np.round(raw).astype(int), 0, NUM_DEPTHS - 1)
237	
238	    def predict_proba(self, X_test):
239	        preds = self.predict(X_test)
240	        prob = np.zeros((len(preds), NUM_DEPTHS))
241	        for i, p in enumerate(preds):
242	            prob[i, p] = 1.0
243	        return prob
244	
245	
246	# ===================================================================
247	#  Baseline 2: Cross-Entropy MLP (DCOL ablation)
248	# ===================================================================
249	
250	class _CEMLP(nn.Module):
251	    """19 -> 128 -> 64 -> 4  with ReLU + dropout."""
252	
253	    def __init__(self, input_dim=NUM_FEATURES, hidden1=128, hidden2=64,
254	                 num_classes=NUM_DEPTHS, dropout=0.3):
255	        super().__init__()
256	        self.net = nn.Sequential(
257	            nn.Linear(input_dim, hidden1),
258	            nn.ReLU(),
259	            nn.Dropout(dropout),
260	            nn.Linear(hidden1, hidden2),
261	            nn.ReLU(),
262	            nn.Dropout(dropout),
263	            nn.Linear(hidden2, num_classes),
264	        )
265	
266	    def forward(self, x):
267	        return self.net(x)
268	
269	
270	class CEClassificationBaseline:
271	    """
272	    Standard multi-class MLP with cross-entropy loss.
273	    Architecture identical to DCOL's feature classifier head (19->128->64->4)
274	    but uses only CE loss -- no contrastive learning.
275	    Key ablation: if CE-MLP matches DCOL, the contrastive loss adds no value.
276	    """
277	
278	    def __init__(self, lr=1e-3, epochs=100, batch_size=256, patience=10,
279	                 device=None, seed=42):
280	        self.lr = lr
281	        self.epochs = epochs
282	        self.batch_size = batch_size
283	        self.patience = patience
284	        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
285	        self.seed = seed
286	        self.scaler = StandardScaler()
287	        self.model = None
288	
289	    def fit(self, X_train, y_train, X_val=None, y_val=None, **kwargs):
290	        torch.manual_seed(self.seed)
291	        np.random.seed(self.seed)
292	
293	        X_s = self.scaler.fit_transform(X_train).astype(np.float32)
294	        Xt = torch.tensor(X_s, device=self.device)
295	        yt = torch.tensor(y_train, dtype=torch.long, device=self.device)
296	        ds = TensorDataset(Xt, yt)
297	        loader = DataLoader(ds, batch_size=self.batch_size, shuffle=True)
298	
299	        self.model = _CEMLP().to(self.device)
300	        optimizer = optim.Adam(self.model.parameters(), lr=self.lr, weight_decay=1e-4)
301	        criterion = nn.CrossEntropyLoss()
302	
303	        best_loss = float("inf")
304	        wait = 0
305	        best_state = None
306	
307	        has_val = X_val is not None and y_val is not None
308	        if has_val:
309	            Xv = torch.tensor(self.scaler.transform(X_val).astype(np.float32),
310	                              device=self.device)
311	            yv = torch.tensor(y_val, dtype=torch.long, device=self.device)
312	
313	        for epoch in range(self.epochs):
314	            self.model.train()
315	            epoch_loss = 0.0
316	            for xb, yb in loader:
317	                optimizer.zero_grad()
318	                logits = self.model(xb)
319	                loss = criterion(logits, yb)
320	                loss.backward()
321	                optimizer.step()
322	                epoch_loss += loss.item() * len(xb)
323	            epoch_loss /= len(ds)
324	
325	            if has_val:
326	                self.model.eval()
327	                with torch.no_grad():
328	                    val_logits = self.model(Xv)
329	                    val_loss = criterion(val_logits, yv).item()
330	            else:
331	                val_loss = epoch_loss
332	
333	            if val_loss < best_loss - 1e-4:
334	                best_loss = val_loss
335	                best_state = {k: v.clone() for k, v in self.model.state_dict().items()}
336	                wait = 0
337	            else:
338	                wait += 1
339	                if wait >= self.patience:
340	                    break
341	
342	        if best_state is not None:
343	            self.model.load_state_dict(best_state)
344	
345	    def predict(self, X_test):
346	        self.model.eval()
347	        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),
348	                           device=self.device)
349	        with torch.no_grad():
350	            logits = self.model(X_s)
351	        return logits.argmax(dim=-1).cpu().numpy()
352	
353	    def predict_proba(self, X_test):
354	        self.model.eval()
355	        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),
356	                           device=self.device)
357	        with torch.no_grad():
358	            logits = self.model(X_s)
359	            probs = torch.softmax(logits, dim=-1)
360	        return probs.cpu().numpy()
361	
362	
363	# ===================================================================
364	#  Baseline 3: CORAL Ordinal Regression
365	# ===================================================================
366	
367	class _CORALNet(nn.Module):
368	    """
369	    CORAL ordinal regression (Cao et al., 2020).
370	    19 -> 128 -> 64 -> shared representation, then K-1=3 sigmoid heads.
371	    Each head k: P(depth > k). Prediction: depth = sum_k I[P(depth > k) > 0.5].
372	    Loss: sum_{k=0}^{K-2} BCE(sigmoid(w^T h + b_k), I[y > k])
373	    """
374	
375	    def __init__(self, input_dim=NUM_FEATURES, hidden1=128, hidden2=64,
376	                 num_classes=NUM_DEPTHS, dropout=0.3):
377	        super().__init__()
378	        self.num_classes = num_classes
379	        self.backbone = nn.Sequential(
380	            nn.Linear(input_dim, hidden1),
381	            nn.ReLU(),
382	            nn.Dropout(dropout),
383	            nn.Linear(hidden1, hidden2),
384	            nn.ReLU(),
385	            nn.Dropout(dropout),
386	        )
387	        self.fc = nn.Linear(hidden2, 1, bias=False)
388	        self.biases = nn.Parameter(torch.zeros(num_classes - 1))
389	
390	    def forward(self, x):
391	        h = self.backbone(x)
392	        logit_base = self.fc(h)
393	        logits = logit_base + self.biases
394	        return logits
395	
396	
397	class CORALBaseline:
398	    """
399	    CORAL ordinal regression for depth estimation.
400	    Ref: Cao, Mirjalili & Raschka (2020). "Rank consistent ordinal regression
401	    for neural networks with consistent confidence sets." Pattern Recognition.
402	    """
403	
404	    def __init__(self, lr=1e-3, epochs=100, batch_size=256, patience=10,
405	                 device=None, seed=42):
406	        self.lr = lr
407	        self.epochs = epochs
408	        self.batch_size = batch_size
409	        self.patience = patience
410	        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
411	        self.seed = seed
412	        self.scaler = StandardScaler()
413	        self.model = None
414	
415	    @staticmethod
416	    def _encode_ordinal(y, num_classes):
417	        n = len(y)
418	        targets = np.zeros((n, num_classes - 1), dtype=np.float32)
419	        for k in range(num_classes - 1):
420	            targets[:, k] = (y > k).astype(np.float32)
421	        return targets
422	
423	    def fit(self, X_train, y_train, X_val=None, y_val=None, **kwargs):
424	        torch.manual_seed(self.seed)
425	        np.random.seed(self.seed)
426	
427	        X_s = self.scaler.fit_transform(X_train).astype(np.float32)
428	        ord_targets = self._encode_ordinal(y_train, NUM_DEPTHS)
429	
430	        Xt = torch.tensor(X_s, device=self.device)
431	        ot = torch.tensor(ord_targets, device=self.device)
432	        ds = TensorDataset(Xt, ot)
433	        loader = DataLoader(ds, batch_size=self.batch_size, shuffle=True)
434	
435	        self.model = _CORALNet().to(self.device)
436	        optimizer = optim.Adam(self.model.parameters(), lr=self.lr, weight_decay=1e-4)
437	        criterion = nn.BCEWithLogitsLoss()
438	
439	        best_loss = float("inf")
440	        wait = 0
441	        best_state = None
442	
443	        has_val = X_val is not None and y_val is not None
444	        if has_val:
445	            Xv = torch.tensor(self.scaler.transform(X_val).astype(np.float32),
446	                              device=self.device)
447	            ov = torch.tensor(self._encode_ordinal(y_val, NUM_DEPTHS),
448	                              device=self.device)
449	
450	        for epoch in range(self.epochs):
451	            self.model.train()
452	            epoch_loss = 0.0
453	            for xb, ob in loader:
454	                optimizer.zero_grad()
455	                logits = self.model(xb)
456	                loss = criterion(logits, ob)
457	                loss.backward()
458	                optimizer.step()
459	                epoch_loss += loss.item() * len(xb)
460	            epoch_loss /= len(ds)
461	
462	            if has_val:
463	                self.model.eval()
464	                with torch.no_grad():
465	                    val_logits = self.model(Xv)
466	                    val_loss = criterion(val_logits, ov).item()
467	            else:
468	                val_loss = epoch_loss
469	
470	            if val_loss < best_loss - 1e-4:
471	                best_loss = val_loss
472	                best_state = {k: v.clone() for k, v in self.model.state_dict().items()}
473	                wait = 0
474	            else:
475	                wait += 1
476	                if wait >= self.patience:
477	                    break
478	
479	        if best_state is not None:
480	            self.model.load_state_dict(best_state)
481	
482	    def predict(self, X_test):
483	        self.model.eval()
484	        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),
485	                           device=self.device)
486	        with torch.no_grad():
487	            logits = self.model(X_s)
488	            probs = torch.sigmoid(logits)
489	        preds = (probs > 0.5).sum(dim=-1).cpu().numpy().astype(int)
490	        return preds
491	
492	    def predict_proba(self, X_test):
493	        self.model.eval()
494	        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),
495	                           device=self.device)
496	        with torch.no_grad():
497	            logits = self.model(X_s)
498	            cum_probs = torch.sigmoid(logits).cpu().numpy()
499	
500	        n = len(X_test)
501	        probs = np.zeros((n, NUM_DEPTHS))
502	        probs[:, 0] = 1.0 - cum_probs[:, 0]
503	        for k in range(1, NUM_DEPTHS - 1):
504	            probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]
505	        probs[:, NUM_DEPTHS - 1] = cum_probs[:, NUM_DEPTHS - 2]
506	        probs = np.clip(probs, 0, 1)
507	        row_sums = probs.sum(axis=1, keepdims=True)
508	        probs = probs / np.where(row_sums > 0, row_sums, 1.0)
509	        return probs
510	
511	
512	# ===================================================================
513	#  Baseline 4: DivEye (Surprisal Diversity + XGBoost)
514	# ===================================================================
515	#
516	# DivEye feature groups mapped to our 19 features:
517	#   Distributional: mean_ppl, var_ppl, skewness_ppl, kurtosis_ppl
518	#   Surprisal:      mean_surprisal, var_surprisal, entropy_of_surprisal
519	#   Lexical diversity: type_token_ratio, hapax_ratio, bigram_entropy, trigram_entropy
520	#   Repetition:     rep_2gram, rep_3gram, rep_4gram
521	#
522	# Note: DivEye's temporal features (first-order dS and second-order d2S)
523	# are not available in our pre-computed features.
524	
525	DIVEYE_FEATURE_INDICES = [
526	    FEATURE_NAMES.index(f) for f in [
527	        "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
528	        "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
529	        "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
530	        "rep_2gram", "rep_3gram", "rep_4gram",
531	    ]
532	]
533	
534	
535	class DivEyeBaseline:
536	    """
537	    DivEye-style detection adapted for depth estimation.
538	    Ref: Basani & Chen (2026). "Diversity Boosts AI-Generated Text Detection." TMLR.
539	    XGBoost on surprisal-related feature subset (14 of 19 features).
540	    """
541	
542	    def __init__(self, seed=42):
543	        self.seed = seed
544	        self.model = None
545	
546	    def fit(self, X_train, y_train, **kwargs):
547	        try:
548	            from xgboost import XGBClassifier
549	        except ImportError:
550	            print("[ERROR] xgboost not installed. Run: pip install xgboost")
551	            sys.exit(1)
552	
553	        Xd = X_train[:, DIVEYE_FEATURE_INDICES]
554	        self.model = XGBClassifier(
555	            n_estimators=200,
556	            max_depth=6,
557	            learning_rate=0.1,
558	            subsample=0.8,
559	            colsample_bytree=0.8,
560	            random_state=self.seed,
561	            use_label_encoder=False,
562	            eval_metric="mlogloss",
563	            verbosity=0,
564	        )
565	        self.model.fit(Xd, y_train)
566	
567	    def predict(self, X_test):
568	        Xd = X_test[:, DIVEYE_FEATURE_INDICES]
569	        return self.model.predict(Xd)
570	
571	    def predict_proba(self, X_test):
572	        Xd = X_test[:, DIVEYE_FEATURE_INDICES]
573	        probs = self.model.predict_proba(Xd)
574	        if probs.shape[1] < NUM_DEPTHS:
575	            full = np.zeros((probs.shape[0], NUM_DEPTHS))
576	            for i, c in enumerate(self.model.classes_):
577	                full[:, c] = probs[:, i]
578	            return full
579	        return probs
580	
581	
582	# ===================================================================
583	#  Baseline 5: Random Forest
584	# ===================================================================
585	
586	class RandomForestBaseline:
587	
588	    def __init__(self, n_estimators=100, seed=42):
589	        self.seed = seed
590	        self.n_estimators = n_estimators
591	        self.scaler = StandardScaler()
592	        self.model = None
593	
594	    def fit(self, X_train, y_train, **kwargs):
595	        from sklearn.ensemble import RandomForestClassifier
596	        X_s = self.scaler.fit_transform(X_train)
597	        self.model = RandomForestClassifier(
598	            n_estimators=self.n_estimators,
599	            random_state=self.seed,
600	            n_jobs=-1,
601	        )
602	        self.model.fit(X_s, y_train)
603	
604	    def predict(self, X_test):
605	        X_s = self.scaler.transform(X_test)
606	        return self.model.predict(X_s)
607	
608	    def predict_proba(self, X_test):
609	        X_s = self.scaler.transform(X_test)
610	        probs = self.model.predict_proba(X_s)
611	        if probs.shape[1] < NUM_DEPTHS:
612	            full = np.zeros((probs.shape[0], NUM_DEPTHS))
613	            for i, c in enumerate(self.model.classes_):
614	                full[:, c] = probs[:, i]
615	            return full
616	        return probs
617	
618	
619	# ===================================================================
620	#  Baseline 6: Logistic Regression
621	# ===================================================================
622	
623	class LogisticRegressionBaseline:
624	
625	    def __init__(self, max_iter=1000, seed=42):
626	        self.seed = seed
627	        self.max_iter = max_iter
628	        self.scaler = StandardScaler()
629	        self.model = None
630	
631	    def fit(self, X_train, y_train, **kwargs):
632	        from sklearn.linear_model import LogisticRegression as _LR
633	        X_s = self.scaler.fit_transform(X_train)
634	        self.model = _LR(
635	            max_iter=self.max_iter,
636	            random_state=self.seed,
637	            solver="lbfgs",
638	        )
639	        self.model.fit(X_s, y_train)
640	
641	    def predict(self, X_test):
642	        X_s = self.scaler.transform(X_test)
643	        return self.model.predict(X_s)
644	
645	    def predict_proba(self, X_test):
646	        X_s = self.scaler.transform(X_test)
647	        probs = self.model.predict_proba(X_s)
648	        if probs.shape[1] < NUM_DEPTHS:
649	            full = np.zeros((probs.shape[0], NUM_DEPTHS))
650	            for i, c in enumerate(self.model.classes_):
651	                full[:, c] = probs[:, i]
652	            return full
653	        return probs
654	
655	
656	# ===================================================================
657	#  Baseline 7: Zero-shot LLM Prompting
658	# ===================================================================
659	
660	ZEROSHOT_SYSTEM_PROMPT = """You are an expert at detecting AI-generated text and estimating its generation depth.
661	
662	"Recursive generation depth" refers to how many times a text has been through an LLM generation cycle:
663	- Depth 0: Original human-written text (e.g., Wikipedia, StackExchange, academic papers)
664	- Depth 1: Text generated by an LLM given human-written text as a prompt/seed
665	- Depth 2: Text generated by an LLM given depth-1 text as input
666	- Depth 3: Text generated by an LLM given depth-2 text as input
667	
668	Key patterns by depth:
669	- Depth 0 (human): Rich vocabulary, domain-specific terminology, natural topic shifts, occasional typos/informal phrasing
670	- Depth 1 (first-gen): Fluent but slightly generic, may have formulaic transitions, maintains topic coherence
671	- Depth 2 (second-gen): More repetitive phrasing, narrower vocabulary, increasingly generic content, possible topic drift
672	- Depth 3 (third-gen): Noticeable repetition, formulaic structure, may contain subtle incoherence or circular reasoning, very generic language"""
673	
674	ZEROSHOT_USER_TEMPLATE = """Analyze the following text and estimate its recursive generation depth (0, 1, 2, or 3).
675	
676	TEXT:
677	{text}
678	
679	Respond with ONLY a JSON object in this exact format:
680	{{"depth": &lt;integer 0-3>, "confidence": &lt;float 0-1>, "reasoning": "&lt;brief one-sentence explanation>"}}"""
681	
682	
683	def _parse_llm_response(response_text):
684	    """Extract depth prediction from LLM response."""
685	    json_match = re.search(r'\{[^{}]*"depth"\s*:\s*(\d)[^{}]*\}', response_text)
686	    if json_match:
687	        try:
688	            obj = json.loads(json_match.group(0))
689	            depth = int(obj.get("depth", -1))
690	            confidence = float(obj.get("confidence", 0.5))
691	            if 0 <= depth <= 3:
692	                return depth, confidence
693	        except (json.JSONDecodeError, ValueError):
694	            pass
695	    digit_match = re.search(r'\b([0-3])\b', response_text)
696	    if digit_match:
697	        return int(digit_match.group(1)), 0.5
698	    return 0, 0.0
699	
700	
701	def _call_claude(text, model, max_tokens=256):
702	    import anthropic
703	    client = anthropic.Anthropic()
704	    message = client.messages.create(
705	        model=model,
706	        max_tokens=max_tokens,
707	        system=ZEROSHOT_SYSTEM_PROMPT,
708	        messages=[{"role": "user", "content": ZEROSHOT_USER_TEMPLATE.format(text=text)}],
709	    )
710	    return message.content[0].text
711	
712	
713	def _call_openai(text, model, max_tokens=256):
714	    import openai
715	    client = openai.OpenAI()
716	    response = client.chat.completions.create(
717	        model=model,
718	        max_tokens=max_tokens,
719	        messages=[
720	            {"role": "system", "content": ZEROSHOT_SYSTEM_PROMPT},
721	            {"role": "user", "content": ZEROSHOT_USER_TEMPLATE.format(text=text)},
722	        ],
723	    )
724	    return response.choices[0].message.content
725	
726	
727	class ZeroShotLLMBaseline:
728	    """
729	    Zero-shot LLM prompting for depth estimation.
730	    No training -- uses in-context prompting to classify text depth.
731	    Supports Claude (Anthropic) and OpenAI APIs.
732	    """
733	
734	    def __init__(self, provider="claude", model=None, max_seq_len=512,
735	                 rate_limit_delay=0.5):
736	        self.provider = provider
737	        self.model = model
738	        if self.model is None:
739	            self.model = "claude-sonnet-4-20250514" if provider == "claude" else "gpt-4o"
740	        self.max_seq_len = max_seq_len
741	        self.rate_limit_delay = rate_limit_delay
742	        self._call_fn = _call_claude if provider == "claude" else _call_openai
743	
744	    def _truncate(self, text):
745	        words = text.split()
746	        approx_tokens = int(self.max_seq_len * 0.75)
747	        if len(words) > approx_tokens:
748	            words = words[:approx_tokens]
749	        return " ".join(words)
750	
751	    def fit(self, X_train, y_train, **kwargs):
752	        pass
753	
754	    def predict_texts(self, texts):
755	        """Predict depth for raw text inputs."""
756	        y_preds, y_probs = [], []
757	        errors = 0
758	        for i, text in enumerate(texts):
759	            truncated = self._truncate(text)
760	            try:
761	                response = self._call_fn(truncated, self.model)
762	                depth, confidence = _parse_llm_response(response)
763	                y_preds.append(depth)
764	                prob = np.zeros(NUM_DEPTHS)
765	                prob[depth] = confidence
766	                remaining = (1.0 - confidence) / max(NUM_DEPTHS - 1, 1)
767	                for d in range(NUM_DEPTHS):
768	                    if d != depth:
769	                        prob[d] = remaining
770	                y_probs.append(prob)
771	            except Exception as e:
772	                print(f"  [{i}] API error: {e}")
773	                y_preds.append(0)
774	                y_probs.append(np.ones(NUM_DEPTHS) / NUM_DEPTHS)
775	                errors += 1
776	
777	            if (i + 1) % 20 == 0:
778	                print(f"  Progress: {i+1}/{len(texts)}")
779	            if self.rate_limit_delay > 0:
780	                time.sleep(self.rate_limit_delay)
781	
782	        if errors > 0:
783	            print(f"  {errors}/{len(texts)} API errors.")
784	        return np.array(y_preds), np.array(y_probs)
785	
786	    def predict(self, X_test):
787	        raise NotImplementedError("ZeroShotLLMBaseline requires raw text. Use predict_texts().")
788	
789	    def predict_proba(self, X_test):
790	        raise NotImplementedError("ZeroShotLLMBaseline requires raw text. Use predict_texts().")
791	
792	
793	# ===================================================================
794	#  Unified Runner
795	# ===================================================================
796	
797	FEATURE_BASED_METHODS = ["ppl_reg_single", "ppl_reg", "ce_mlp", "coral", "diveye", "rf", "lr"]
798	TEXT_BASED_METHODS = ["zeroshot"]
799	
800	BASELINE_REGISTRY = {
801	    "ppl_reg_single": "PPL Regression (single: mean_ppl)",
802	    "ppl_reg":        "PPL Regression (multi: 19-dim OLS)",
803	    "ce_mlp":         "CE-MLP (DCOL ablation)",
804	    "coral":          "CORAL Ordinal Regression",
805	    "diveye":         "DivEye (XGBoost)",
806	    "rf":             "Random Forest",
807	    "lr":             "Logistic Regression",
808	    "zeroshot":       "Zero-shot LLM",
809	}
810	
811	ALL_METHODS = FEATURE_BASED_METHODS + TEXT_BASED_METHODS
812	
813	
814	def _make_baseline(method, args):
815	    if method == "ppl_reg_single":
816	        return PPLRegressionBaseline(mode="single")
817	    elif method == "ppl_reg":
818	        return PPLRegressionBaseline(mode="multi")
819	    elif method == "ce_mlp":
820	        return CEClassificationBaseline(
821	            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,
822	            patience=args.patience, seed=args.seed,
823	        )
824	    elif method == "coral":
825	        return CORALBaseline(
826	            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,
827	            patience=args.patience, seed=args.seed,
828	        )
829	    elif method == "diveye":
830	        return DivEyeBaseline(seed=args.seed)
831	    elif method == "rf":
832	        return RandomForestBaseline(n_estimators=100, seed=args.seed)
833	    elif method == "lr":
834	        return LogisticRegressionBaseline(max_iter=1000, seed=args.seed)
835	    elif method == "zeroshot":
836	        return ZeroShotLLMBaseline(
837	            provider=args.provider,
838	            model=args.llm_model,
839	            max_seq_len=args.max_seq_len,
840	            rate_limit_delay=args.rate_limit_delay,
841	        )
842	    return None
843	
844	
845	def run_feature_baseline(method, X_train, y_train, X_val, y_val, X_test, y_test, args):
846	    bl = _make_baseline(method, args)
847	    if bl is None:
848	        print(f"Unknown method: {method}")
849	        return None
850	    bl.fit(X_train, y_train, X_val=X_val, y_val=y_val)
851	    y_pred = bl.predict(X_test)
852	    y_prob = bl.predict_proba(X_test)
853	    return evaluate(BASELINE_REGISTRY[method], y_test, y_pred, y_prob)
854	
855	
856	def run_zeroshot_baseline(texts, labels, args):
857	    bl = _make_baseline("zeroshot", args)
858	    _, eval_idx = train_test_split(
859	        np.arange(len(labels)), test_size=args.eval_split,
860	        stratify=labels, random_state=args.seed,
861	    )
862	    eval_texts = [texts[i] for i in eval_idx]
863	    eval_labels = labels[eval_idx]
864	
865	    if len(eval_texts) > args.max_eval_samples:
866	        rng = np.random.RandomState(args.seed)
867	        sample_idx = sorted(rng.choice(len(eval_texts), args.max_eval_samples, replace=False))
868	        eval_texts = [eval_texts[i] for i in sample_idx]
869	        eval_labels = eval_labels[sample_idx]
870	
871	    print(f"Zero-shot: evaluating {len(eval_texts)} samples with {args.provider}/{bl.model}")
872	    print(f"  Label distribution: {dict(Counter(eval_labels))}")
873	
874	    y_pred, y_prob = bl.predict_texts(eval_texts)
875	    return evaluate(BASELINE_REGISTRY["zeroshot"], eval_labels, y_pred, y_prob)
876	
877	
878	def parse_args():
879	    p = argparse.ArgumentParser(description="Baseline battery for depth estimation.")
880	    p.add_argument("--method", default="all",
881	                   choices=ALL_METHODS + ["all", "all_features"])
882	    p.add_argument("--features_path", "--data_path", default="data/features_all.jsonl",
883	                   dest="features_path")
884	    p.add_argument("--data_dirs", nargs="+", default=["data/"],
885	                   help="Directories containing depth_*.jsonl (for zero-shot)")
886	    p.add_argument("--output_dir", default="results/baselines/")
887	    p.add_argument("--seed", type=int, default=42)
888	    p.add_argument("--test_size", type=float, default=0.15)
889	    p.add_argument("--val_size", type=float, default=0.15)
890	    p.add_argument("--eval_split", type=float, default=0.15)
891	    p.add_argument("--epochs", type=int, default=100)
892	    p.add_argument("--batch_size", type=int, default=256)
893	    p.add_argument("--lr", type=float, default=1e-3)
894	    p.add_argument("--patience", type=int, default=10)
895	    p.add_argument("--max_seq_len", type=int, default=512)
896	    # Zero-shot LLM args
897	    p.add_argument("--provider", choices=["claude", "openai"], default="claude")
898	    p.add_argument("--llm_model", default=None,
899	                   help="LLM model name (default: claude-sonnet-4-20250514 / gpt-4o)")
900	    p.add_argument("--max_eval_samples", type=int, default=200,
901	                   help="Max samples for zero-shot eval (API cost control)")
902	    p.add_argument("--rate_limit_delay", type=float, default=0.5)
903	    return p.parse_args()
904	
905	
906	def main():
907	    args = parse_args()
908	
909	    if args.method == "all":
910	        methods = FEATURE_BASED_METHODS
911	        print("Running all feature-based baselines (use --method zeroshot for LLM baseline)")
912	    elif args.method == "all_features":
913	        methods = FEATURE_BASED_METHODS
914	    else:
915	        methods = [args.method]
916	
917	    all_results = {}
918	
919	    feature_methods = [m for m in methods if m in FEATURE_BASED_METHODS]
920	    text_methods = [m for m in methods if m in TEXT_BASED_METHODS]
921	
922	    if feature_methods:
923	        print(f"Loading features from {args.features_path} ...")
924	        X, y = load_features(args.features_path)
925	        print(f"  {X.shape[0]} samples, {X.shape[1]} features")
926	        print(f"  Depth distribution: {dict(Counter(y))}")
927	
928	        X_train, y_train, X_val, y_val, X_test, y_test = prepare_splits(
929	            X, y, test_size=args.test_size, val_size=args.val_size, seed=args.seed
930	        )
931	        print(f"  Train: {len(y_train)}, Val: {len(y_val)}, Test: {len(y_test)}")
932	
933	        for m in feature_methods:
934	            result = run_feature_baseline(
935	                m, X_train, y_train, X_val, y_val, X_test, y_test, args
936	            )
937	            if result is not None:
938	                all_results[m] = result
939	
940	    if text_methods:
941	        if "zeroshot" in text_methods:
942	            texts, labels = load_jsonl_texts(
943	                args.data_dirs, max_samples=0, seed=args.seed
944	            )
945	            result = run_zeroshot_baseline(texts, labels, args)
946	            if result is not None:
947	                all_results["zeroshot"] = result
948	
949	    if len(all_results) > 1:
950	        print(f"\n{'='*60}")
951	        print(f"  SUMMARY")
952	        print(f"{'='*60}")
953	        print(f"  {'Method':<35s} {'4-cls':>6s} {'3-cls':>6s} {'MAE':>6s}")
954	        print(f"  {'-'*35} {'-'*6} {'-'*6} {'-'*6}")
955	        for m, r in all_results.items():
956	            print(f"  {r['method']:<35s} {r['acc_4class']:6.4f} {r['acc_3class']:6.4f} {r['mae']:6.4f}")
957	
958	    os.makedirs(args.output_dir, exist_ok=True)
959	    out_path = os.path.join(args.output_dir, "baseline_results.json")
960	    with open(out_path, "w") as f:
961	        json.dump(all_results, f, indent=2, default=str)
962	    print(f"\nResults saved to {out_path}")
963	
964	
965	if __name__ == "__main__":
966	    main()
967	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "98708770-0857-4929-ac4e-5ac1d239b592",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/baselines.py",
      "content": "\"\"\"\nBaseline battery for recursive generation depth estimation.\n\nBaselines (feature-based, 19-dim input):\n  1. PPLRegressionBaseline  -- OLS regression on mean_ppl (single) or all 19 features (multi)\n  2. CEClassificationBaseline -- MLP with cross-entropy loss (DCOL ablation, no contrastive loss)\n  3. CORALBaseline -- Ordinal regression with K-1 binary classifiers (Cao et al., 2020)\n  4. DivEyeBaseline -- Surprisal diversity features + XGBoost (Basani & Chen, TMLR 2026)\n  5. RandomForestBaseline -- sklearn RF on 19-dim features\n  6. LogisticRegressionBaseline -- sklearn LR on 19-dim features\n\nBaselines (text-based, raw text input):\n  7. ZeroShotLLMBaseline -- Prompt an LLM (Claude/OpenAI) to classify depth directly\n\nUsage:\n  python src/baselines.py --method ppl_reg --features_path data/features_all.jsonl\n  python src/baselines.py --method ce_mlp  --features_path data/features_all.jsonl --epochs 50\n  python src/baselines.py --method coral   --features_path data/features_all.jsonl --epochs 50\n  python src/baselines.py --method diveye  --features_path data/features_all.jsonl\n  python src/baselines.py --method rf      --features_path data/features_all.jsonl\n  python src/baselines.py --method lr      --features_path data/features_all.jsonl\n  python src/baselines.py --method zeroshot --data_dirs data/ --provider claude --max_eval_samples 200\n  python src/baselines.py --method all     --features_path data/features_all.jsonl --epochs 50\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport re\nimport sys\nimport time\nimport numpy as np\nfrom collections import Counter\n\nimport torch\nimport torch.nn as nn\nimport torch.optim as optim\nfrom torch.utils.data import DataLoader, TensorDataset\n\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.metrics import (\n    accuracy_score, confusion_matrix, classification_report, roc_auc_score,\n)\n\n# -- Feature schema (must match extract_features.py / dcol_dataset.py) --\n\nFEATURE_NAMES = [\n    \"mean_ppl\", \"var_ppl\", \"skewness_ppl\", \"kurtosis_ppl\",\n    \"p10_ppl\", \"p25_ppl\", \"p50_ppl\", \"p75_ppl\", \"p90_ppl\",\n    \"mean_surprisal\", \"var_surprisal\", \"entropy_of_surprisal\",\n    \"type_token_ratio\", \"hapax_ratio\", \"bigram_entropy\", \"trigram_entropy\",\n    \"rep_2gram\", \"rep_3gram\", \"rep_4gram\",\n]\nNUM_FEATURES = len(FEATURE_NAMES)\nNUM_DEPTHS = 4\nDEPTH_LABELS = list(range(NUM_DEPTHS))\n\n# -- Data loading --\n\ndef load_features(path):\n    \"\"\"Load JSONL features file -> (X [n, 19], y [n]).\"\"\"\n    records = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                records.append(json.loads(line))\n    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)\n    y = np.array([r[\"depth\"] for r in records], dtype=np.int64)\n    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)\n    return X, y\n\n\ndef load_jsonl_texts(data_dirs, max_samples=0, seed=42):\n    \"\"\"Load raw text + depth labels from depth_*.jsonl files across directories.\"\"\"\n    import glob as glob_mod\n    texts, labels = [], []\n    for data_dir in data_dirs:\n        for d in range(NUM_DEPTHS):\n            fpath = os.path.join(data_dir, f\"depth_{d}.jsonl\")\n            if not os.path.exists(fpath):\n                matches = glob_mod.glob(os.path.join(data_dir, f\"*depth_{d}*.jsonl\"))\n                fpath = matches[0] if matches else None\n            if fpath is None or not os.path.exists(fpath):\n                continue\n            with open(fpath) as f:\n                for line in f:\n                    line = line.strip()\n                    if not line:\n                        continue\n                    rec = json.loads(line)\n                    texts.append(rec[\"text\"])\n                    labels.append(rec.get(\"depth\", d))\n    labels = np.array(labels, dtype=np.int64)\n    if max_samples > 0 and len(texts) > max_samples:\n        rng = np.random.RandomState(seed)\n        idx = sorted(rng.choice(len(texts), max_samples, replace=False))\n        texts = [texts[i] for i in idx]\n        labels = labels[idx]\n    print(f\"Loaded {len(texts)} text samples. Depth distribution: {dict(Counter(labels))}\")\n    return texts, labels\n\n\ndef prepare_splits(X, y, test_size=0.15, val_size=0.15, seed=42):\n    idx = np.arange(len(y))\n    train_val_idx, test_idx = train_test_split(\n        idx, test_size=test_size, stratify=y, random_state=seed\n    )\n    rel_val = val_size / (1 - test_size)\n    train_idx, val_idx = train_test_split(\n        train_val_idx, test_size=rel_val,\n        stratify=y[train_val_idx], random_state=seed\n    )\n    return (\n        X[train_idx], y[train_idx],\n        X[val_idx], y[val_idx],\n        X[test_idx], y[test_idx],\n    )\n\n# -- Evaluation metrics --\n\ndef pairwise_auc(y_true, y_prob, d1, d2):\n    mask = np.isin(y_true, [d1, d2])\n    if mask.sum() < 2:\n        return None\n    yt = (y_true[mask] == d2).astype(int)\n    if len(np.unique(yt)) < 2:\n        return None\n    yp = y_prob[mask, d2]\n    return float(roc_auc_score(yt, yp))\n\n\ndef compute_all_pairwise_auc(y_true, y_prob):\n    result = {}\n    for i, d1 in enumerate(DEPTH_LABELS):\n        for d2 in DEPTH_LABELS[i + 1:]:\n            auc = pairwise_auc(y_true, y_prob, d1, d2)\n            result[f\"d{d1}_vs_d{d2}\"] = round(auc, 4) if auc is not None else None\n    return result\n\n\ndef bootstrap_ci(y_true, y_pred, metric_fn=accuracy_score, n_boot=1000, seed=42):\n    rng = np.random.RandomState(seed)\n    scores = []\n    n = len(y_true)\n    for _ in range(n_boot):\n        idx = rng.choice(n, n, replace=True)\n        scores.append(metric_fn(y_true[idx], y_pred[idx]))\n    lo = float(np.percentile(scores, 2.5))\n    hi = float(np.percentile(scores, 97.5))\n    return lo, hi\n\n\ndef evaluate(name, y_true, y_pred, y_prob=None):\n    \"\"\"Print and return evaluation metrics.\"\"\"\n    acc4 = accuracy_score(y_true, y_pred)\n    ci_lo, ci_hi = bootstrap_ci(y_true, y_pred)\n\n    mask_13 = y_true >= 1\n    acc3 = accuracy_score(y_true[mask_13], y_pred[mask_13]) if mask_13.sum() > 0 else 0.0\n\n    mae = float(np.mean(np.abs(y_true - y_pred)))\n\n    cm = confusion_matrix(y_true, y_pred, labels=DEPTH_LABELS)\n    per_class_recall = cm.diagonal() / cm.sum(axis=1).clip(min=1)\n\n    pair_aucs = {}\n    if y_prob is not None:\n        pair_aucs = compute_all_pairwise_auc(y_true, y_prob)\n\n    print(f\"\\n{'='*60}\")\n    print(f\"  {name}\")\n    print(f\"{'='*60}\")\n    print(f\"  4-class accuracy : {acc4:.4f}  (95% CI: [{ci_lo:.4f}, {ci_hi:.4f}])\")\n    print(f\"  3-class accuracy : {acc3:.4f}  (d1-d3 only)\")\n    print(f\"  MAE              : {mae:.4f}\")\n    print(f\"  Per-class recall : {dict(zip([f'd{d}' for d in DEPTH_LABELS], [round(r,4) for r in per_class_recall]))}\")\n    if pair_aucs:\n        print(f\"  Pairwise AUC     : {pair_aucs}\")\n    print(f\"\\n  Confusion matrix:\")\n    print(f\"  {'':>8s}\", \" \".join(f\"pred-{d}\" for d in DEPTH_LABELS))\n    for i, d in enumerate(DEPTH_LABELS):\n        print(f\"  true-{d}  \", \" \".join(f\"{cm[i,j]:6d}\" for j in range(NUM_DEPTHS)))\n\n    cr = classification_report(\n        y_true, y_pred,\n        target_names=[f\"depth-{d}\" for d in DEPTH_LABELS],\n        zero_division=0,\n    )\n    print(f\"\\n{cr}\")\n\n    return {\n        \"method\": name,\n        \"acc_4class\": round(acc4, 4),\n        \"acc_4class_ci\": [round(ci_lo, 4), round(ci_hi, 4)],\n        \"acc_3class\": round(acc3, 4),\n        \"mae\": round(mae, 4),\n        \"per_class_recall\": {f\"d{d}\": round(r, 4) for d, r in zip(DEPTH_LABELS, per_class_recall)},\n        \"pairwise_auc\": pair_aucs,\n    }\n\n\n# ===================================================================\n#  Baseline 1: PPL Regression\n# ===================================================================\n\nclass PPLRegressionBaseline:\n    \"\"\"\n    Linear regression -> round to nearest depth.\n    Single-feature mode: depth = a * mean_ppl + b\n    Multi-feature mode:  depth = X @ w + b  (19-dim OLS)\n    \"\"\"\n\n    def __init__(self, mode=\"multi\"):\n        self.mode = mode\n        self.scaler = StandardScaler()\n        self.model = LinearRegression()\n\n    def _select(self, X):\n        if self.mode == \"single\":\n            idx = FEATURE_NAMES.index(\"mean_ppl\")\n            return X[:, idx:idx+1]\n        return X\n\n    def fit(self, X_train, y_train, **kwargs):\n        Xs = self._select(X_train)\n        Xs = self.scaler.fit_transform(Xs)\n        self.model.fit(Xs, y_train.astype(np.float64))\n\n    def predict(self, X_test):\n        Xs = self._select(X_test)\n        Xs = self.scaler.transform(Xs)\n        raw = self.model.predict(Xs)\n        return np.clip(np.round(raw).astype(int), 0, NUM_DEPTHS - 1)\n\n    def predict_proba(self, X_test):\n        preds = self.predict(X_test)\n        prob = np.zeros((len(preds), NUM_DEPTHS))\n        for i, p in enumerate(preds):\n            prob[i, p] = 1.0\n        return prob\n\n\n# ===================================================================\n#  Baseline 2: Cross-Entropy MLP (DCOL ablation)\n# ===================================================================\n\nclass _CEMLP(nn.Module):\n    \"\"\"19 -> 128 -> 64 -> 4  with ReLU + dropout.\"\"\"\n\n    def __init__(self, input_dim=NUM_FEATURES, hidden1=128, hidden2=64,\n                 num_classes=NUM_DEPTHS, dropout=0.3):\n        super().__init__()\n        self.net = nn.Sequential(\n            nn.Linear(input_dim, hidden1),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n            nn.Linear(hidden1, hidden2),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n            nn.Linear(hidden2, num_classes),\n        )\n\n    def forward(self, x):\n        return self.net(x)\n\n\nclass CEClassificationBaseline:\n    \"\"\"\n    Standard multi-class MLP with cross-entropy loss.\n    Architecture identical to DCOL's feature classifier head (19->128->64->4)\n    but uses only CE loss -- no contrastive learning.\n    Key ablation: if CE-MLP matches DCOL, the contrastive loss adds no value.\n    \"\"\"\n\n    def __init__(self, lr=1e-3, epochs=100, batch_size=256, patience=10,\n                 device=None, seed=42):\n        self.lr = lr\n        self.epochs = epochs\n        self.batch_size = batch_size\n        self.patience = patience\n        self.device = device or (\"cuda\" if torch.cuda.is_available() else \"cpu\")\n        self.seed = seed\n        self.scaler = StandardScaler()\n        self.model = None\n\n    def fit(self, X_train, y_train, X_val=None, y_val=None, **kwargs):\n        torch.manual_seed(self.seed)\n        np.random.seed(self.seed)\n\n        X_s = self.scaler.fit_transform(X_train).astype(np.float32)\n        Xt = torch.tensor(X_s, device=self.device)\n        yt = torch.tensor(y_train, dtype=torch.long, device=self.device)\n        ds = TensorDataset(Xt, yt)\n        loader = DataLoader(ds, batch_size=self.batch_size, shuffle=True)\n\n        self.model = _CEMLP().to(self.device)\n        optimizer = optim.Adam(self.model.parameters(), lr=self.lr, weight_decay=1e-4)\n        criterion = nn.CrossEntropyLoss()\n\n        best_loss = float(\"inf\")\n        wait = 0\n        best_state = None\n\n        has_val = X_val is not None and y_val is not None\n        if has_val:\n            Xv = torch.tensor(self.scaler.transform(X_val).astype(np.float32),\n                              device=self.device)\n            yv = torch.tensor(y_val, dtype=torch.long, device=self.device)\n\n        for epoch in range(self.epochs):\n            self.model.train()\n            epoch_loss = 0.0\n            for xb, yb in loader:\n                optimizer.zero_grad()\n                logits = self.model(xb)\n                loss = criterion(logits, yb)\n                loss.backward()\n                optimizer.step()\n                epoch_loss += loss.item() * len(xb)\n            epoch_loss /= len(ds)\n\n            if has_val:\n                self.model.eval()\n                with torch.no_grad():\n                    val_logits = self.model(Xv)\n                    val_loss = criterion(val_logits, yv).item()\n            else:\n                val_loss = epoch_loss\n\n            if val_loss < best_loss - 1e-4:\n                best_loss = val_loss\n                best_state = {k: v.clone() for k, v in self.model.state_dict().items()}\n                wait = 0\n            else:\n                wait += 1\n                if wait >= self.patience:\n                    break\n\n        if best_state is not None:\n            self.model.load_state_dict(best_state)\n\n    def predict(self, X_test):\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n        return logits.argmax(dim=-1).cpu().numpy()\n\n    def predict_proba(self, X_test):\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n            probs = torch.softmax(logits, dim=-1)\n        return probs.cpu().numpy()\n\n\n# ===================================================================\n#  Baseline 3: CORAL Ordinal Regression\n# ===================================================================\n\nclass _CORALNet(nn.Module):\n    \"\"\"\n    CORAL ordinal regression (Cao et al., 2020).\n    19 -> 128 -> 64 -> shared representation, then K-1=3 sigmoid heads.\n    Each head k: P(depth > k). Prediction: depth = sum_k I[P(depth > k) > 0.5].\n    Loss: sum_{k=0}^{K-2} BCE(sigmoid(w^T h + b_k), I[y > k])\n    \"\"\"\n\n    def __init__(self, input_dim=NUM_FEATURES, hidden1=128, hidden2=64,\n                 num_classes=NUM_DEPTHS, dropout=0.3):\n        super().__init__()\n        self.num_classes = num_classes\n        self.backbone = nn.Sequential(\n            nn.Linear(input_dim, hidden1),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n            nn.Linear(hidden1, hidden2),\n            nn.ReLU(),\n            nn.Dropout(dropout),\n        )\n        self.fc = nn.Linear(hidden2, 1, bias=False)\n        self.biases = nn.Parameter(torch.zeros(num_classes - 1))\n\n    def forward(self, x):\n        h = self.backbone(x)\n        logit_base = self.fc(h)\n        logits = logit_base + self.biases\n        return logits\n\n\nclass CORALBaseline:\n    \"\"\"\n    CORAL ordinal regression for depth estimation.\n    Ref: Cao, Mirjalili & Raschka (2020). \"Rank consistent ordinal regression\n    for neural networks with consistent confidence sets.\" Pattern Recognition.\n    \"\"\"\n\n    def __init__(self, lr=1e-3, epochs=100, batch_size=256, patience=10,\n                 device=None, seed=42):\n        self.lr = lr\n        self.epochs = epochs\n        self.batch_size = batch_size\n        self.patience = patience\n        self.device = device or (\"cuda\" if torch.cuda.is_available() else \"cpu\")\n        self.seed = seed\n        self.scaler = StandardScaler()\n        self.model = None\n\n    @staticmethod\n    def _encode_ordinal(y, num_classes):\n        n = len(y)\n        targets = np.zeros((n, num_classes - 1), dtype=np.float32)\n        for k in range(num_classes - 1):\n            targets[:, k] = (y > k).astype(np.float32)\n        return targets\n\n    def fit(self, X_train, y_train, X_val=None, y_val=None, **kwargs):\n        torch.manual_seed(self.seed)\n        np.random.seed(self.seed)\n\n        X_s = self.scaler.fit_transform(X_train).astype(np.float32)\n        ord_targets = self._encode_ordinal(y_train, NUM_DEPTHS)\n\n        Xt = torch.tensor(X_s, device=self.device)\n        ot = torch.tensor(ord_targets, device=self.device)\n        ds = TensorDataset(Xt, ot)\n        loader = DataLoader(ds, batch_size=self.batch_size, shuffle=True)\n\n        self.model = _CORALNet().to(self.device)\n        optimizer = optim.Adam(self.model.parameters(), lr=self.lr, weight_decay=1e-4)\n        criterion = nn.BCEWithLogitsLoss()\n\n        best_loss = float(\"inf\")\n        wait = 0\n        best_state = None\n\n        has_val = X_val is not None and y_val is not None\n        if has_val:\n            Xv = torch.tensor(self.scaler.transform(X_val).astype(np.float32),\n                              device=self.device)\n            ov = torch.tensor(self._encode_ordinal(y_val, NUM_DEPTHS),\n                              device=self.device)\n\n        for epoch in range(self.epochs):\n            self.model.train()\n            epoch_loss = 0.0\n            for xb, ob in loader:\n                optimizer.zero_grad()\n                logits = self.model(xb)\n                loss = criterion(logits, ob)\n                loss.backward()\n                optimizer.step()\n                epoch_loss += loss.item() * len(xb)\n            epoch_loss /= len(ds)\n\n            if has_val:\n                self.model.eval()\n                with torch.no_grad():\n                    val_logits = self.model(Xv)\n                    val_loss = criterion(val_logits, ov).item()\n            else:\n                val_loss = epoch_loss\n\n            if val_loss < best_loss - 1e-4:\n                best_loss = val_loss\n                best_state = {k: v.clone() for k, v in self.model.state_dict().items()}\n                wait = 0\n            else:\n                wait += 1\n                if wait >= self.patience:\n                    break\n\n        if best_state is not None:\n            self.model.load_state_dict(best_state)\n\n    def predict(self, X_test):\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n            probs = torch.sigmoid(logits)\n        preds = (probs > 0.5).sum(dim=-1).cpu().numpy().astype(int)\n        return preds\n\n    def predict_proba(self, X_test):\n        self.model.eval()\n        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),\n                           device=self.device)\n        with torch.no_grad():\n            logits = self.model(X_s)\n            cum_probs = torch.sigmoid(logits).cpu().numpy()\n\n        n = len(X_test)\n        probs = np.zeros((n, NUM_DEPTHS))\n        probs[:, 0] = 1.0 - cum_probs[:, 0]\n        for k in range(1, NUM_DEPTHS - 1):\n            probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]\n        probs[:, NUM_DEPTHS - 1] = cum_probs[:, NUM_DEPTHS - 2]\n        probs = np.clip(probs, 0, 1)\n        row_sums = probs.sum(axis=1, keepdims=True)\n        probs = probs / np.where(row_sums > 0, row_sums, 1.0)\n        return probs\n\n\n# ===================================================================\n#  Baseline 4: DivEye (Surprisal Diversity + XGBoost)\n# ===================================================================\n#\n# DivEye feature groups mapped to our 19 features:\n#   Distributional: mean_ppl, var_ppl, skewness_ppl, kurtosis_ppl\n#   Surprisal:      mean_surprisal, var_surprisal, entropy_of_surprisal\n#   Lexical diversity: type_token_ratio, hapax_ratio, bigram_entropy, trigram_entropy\n#   Repetition:     rep_2gram, rep_3gram, rep_4gram\n#\n# Note: DivEye's temporal features (first-order dS and second-order d2S)\n# are not available in our pre-computed features.\n\nDIVEYE_FEATURE_INDICES = [\n    FEATURE_NAMES.index(f) for f in [\n        \"mean_ppl\", \"var_ppl\", \"skewness_ppl\", \"kurtosis_ppl\",\n        \"mean_surprisal\", \"var_surprisal\", \"entropy_of_surprisal\",\n        \"type_token_ratio\", \"hapax_ratio\", \"bigram_entropy\", \"trigram_entropy\",\n        \"rep_2gram\", \"rep_3gram\", \"rep_4gram\",\n    ]\n]\n\n\nclass DivEyeBaseline:\n    \"\"\"\n    DivEye-style detection adapted for depth estimation.\n    Ref: Basani & Chen (2026). \"Diversity Boosts AI-Generated Text Detection.\" TMLR.\n    XGBoost on surprisal-related feature subset (14 of 19 features).\n    \"\"\"\n\n    def __init__(self, seed=42):\n        self.seed = seed\n        self.model = None\n\n    def fit(self, X_train, y_train, **kwargs):\n        try:\n            from xgboost import XGBClassifier\n        except ImportError:\n            print(\"[ERROR] xgboost not installed. Run: pip install xgboost\")\n            sys.exit(1)\n\n        Xd = X_train[:, DIVEYE_FEATURE_INDICES]\n        self.model = XGBClassifier(\n            n_estimators=200,\n            max_depth=6,\n            learning_rate=0.1,\n            subsample=0.8,\n            colsample_bytree=0.8,\n            random_state=self.seed,\n            use_label_encoder=False,\n            eval_metric=\"mlogloss\",\n            verbosity=0,\n        )\n        self.model.fit(Xd, y_train)\n\n    def predict(self, X_test):\n        Xd = X_test[:, DIVEYE_FEATURE_INDICES]\n        return self.model.predict(Xd)\n\n    def predict_proba(self, X_test):\n        Xd = X_test[:, DIVEYE_FEATURE_INDICES]\n        probs = self.model.predict_proba(Xd)\n        if probs.shape[1] < NUM_DEPTHS:\n            full = np.zeros((probs.shape[0], NUM_DEPTHS))\n            for i, c in enumerate(self.model.classes_):\n                full[:, c] = probs[:, i]\n            return full\n        return probs\n\n\n# ===================================================================\n#  Baseline 5: Random Forest\n# ===================================================================\n\nclass RandomForestBaseline:\n\n    def __init__(self, n_estimators=100, seed=42):\n        self.seed = seed\n        self.n_estimators = n_estimators\n        self.scaler = StandardScaler()\n        self.model = None\n\n    def fit(self, X_train, y_train, **kwargs):\n        from sklearn.ensemble import RandomForestClassifier\n        X_s = self.scaler.fit_transform(X_train)\n        self.model = RandomForestClassifier(\n            n_estimators=self.n_estimators,\n            random_state=self.seed,\n            n_jobs=-1,\n        )\n        self.model.fit(X_s, y_train)\n\n    def predict(self, X_test):\n        X_s = self.scaler.transform(X_test)\n        return self.model.predict(X_s)\n\n    def predict_proba(self, X_test):\n        X_s = self.scaler.transform(X_test)\n        probs = self.model.predict_proba(X_s)\n        if probs.shape[1] < NUM_DEPTHS:\n            full = np.zeros((probs.shape[0], NUM_DEPTHS))\n            for i, c in enumerate(self.model.classes_):\n                full[:, c] = probs[:, i]\n            return full\n        return probs\n\n\n# ===================================================================\n#  Baseline 6: Logistic Regression\n# ===================================================================\n\nclass LogisticRegressionBaseline:\n\n    def __init__(self, max_iter=1000, seed=42):\n        self.seed = seed\n        self.max_iter = max_iter\n        self.scaler = StandardScaler()\n        self.model = None\n\n    def fit(self, X_train, y_train, **kwargs):\n        from sklearn.linear_model import LogisticRegression as _LR\n        X_s = self.scaler.fit_transform(X_train)\n        self.model = _LR(\n            max_iter=self.max_iter,\n            random_state=self.seed,\n            solver=\"lbfgs\",\n        )\n        self.model.fit(X_s, y_train)\n\n    def predict(self, X_test):\n        X_s = self.scaler.transform(X_test)\n        return self.model.predict(X_s)\n\n    def predict_proba(self, X_test):\n        X_s = self.scaler.transform(X_test)\n        probs = self.model.predict_proba(X_s)\n        if probs.shape[1] < NUM_DEPTHS:\n            full = np.zeros((probs.shape[0], NUM_DEPTHS))\n            for i, c in enumerate(self.model.classes_):\n                full[:, c] = probs[:, i]\n            return full\n        return probs\n\n\n# ===================================================================\n#  Baseline 7: Zero-shot LLM Prompting\n# ===================================================================\n\nZEROSHOT_SYSTEM_PROMPT = \"\"\"You are an expert at detecting AI-generated text and estimating its generation depth.\n\n\"Recursive generation depth\" refers to how many times a text has been through an LLM generation cycle:\n- Depth 0: Original human-written text (e.g., Wikipedia, StackExchange, academic papers)\n- Depth 1: Text generated by an LLM given human-written text as a prompt/seed\n- Depth 2: Text generated by an LLM given depth-1 text as input\n- Depth 3: Text generated by an LLM given depth-2 text as input\n\nKey patterns by depth:\n- Depth 0 (human): Rich vocabulary, domain-specific terminology, natural topic shifts, occasional typos/informal phrasing\n- Depth 1 (first-gen): Fluent but slightly generic, may have formulaic transitions, maintains topic coherence\n- Depth 2 (second-gen): More repetitive phrasing, narrower vocabulary, increasingly generic content, possible topic drift\n- Depth 3 (third-gen): Noticeable repetition, formulaic structure, may contain subtle incoherence or circular reasoning, very generic language\"\"\"\n\nZEROSHOT_USER_TEMPLATE = \"\"\"Analyze the following text and estimate its recursive generation depth (0, 1, 2, or 3).\n\nTEXT:\n{text}\n\nRespond with ONLY a JSON object in this exact format:\n{{\"depth\": &lt;integer 0-3>, \"confidence\": &lt;float 0-1>, \"reasoning\": \"&lt;brief one-sentence explanation>\"}}\"\"\"\n\n\ndef _parse_llm_response(response_text):\n    \"\"\"Extract depth prediction from LLM response.\"\"\"\n    json_match = re.search(r'\\{[^{}]*\"depth\"\\s*:\\s*(\\d)[^{}]*\\}', response_text)\n    if json_match:\n        try:\n            obj = json.loads(json_match.group(0))\n            depth = int(obj.get(\"depth\", -1))\n            confidence = float(obj.get(\"confidence\", 0.5))\n            if 0 <= depth <= 3:\n                return depth, confidence\n        except (json.JSONDecodeError, ValueError):\n            pass\n    digit_match = re.search(r'\\b([0-3])\\b', response_text)\n    if digit_match:\n        return int(digit_match.group(1)), 0.5\n    return 0, 0.0\n\n\ndef _call_claude(text, model, max_tokens=256):\n    import anthropic\n    client = anthropic.Anthropic()\n    message = client.messages.create(\n        model=model,\n        max_tokens=max_tokens,\n        system=ZEROSHOT_SYSTEM_PROMPT,\n        messages=[{\"role\": \"user\", \"content\": ZEROSHOT_USER_TEMPLATE.format(text=text)}],\n    )\n    return message.content[0].text\n\n\ndef _call_openai(text, model, max_tokens=256):\n    import openai\n    client = openai.OpenAI()\n    response = client.chat.completions.create(\n        model=model,\n        max_tokens=max_tokens,\n        messages=[\n            {\"role\": \"system\", \"content\": ZEROSHOT_SYSTEM_PROMPT},\n            {\"role\": \"user\", \"content\": ZEROSHOT_USER_TEMPLATE.format(text=text)},\n        ],\n    )\n    return response.choices[0].message.content\n\n\nclass ZeroShotLLMBaseline:\n    \"\"\"\n    Zero-shot LLM prompting for depth estimation.\n    No training -- uses in-context prompting to classify text depth.\n    Supports Claude (Anthropic) and OpenAI APIs.\n    \"\"\"\n\n    def __init__(self, provider=\"claude\", model=None, max_seq_len=512,\n                 rate_limit_delay=0.5):\n        self.provider = provider\n        self.model = model\n        if self.model is None:\n            self.model = \"claude-sonnet-4-20250514\" if provider == \"claude\" else \"gpt-4o\"\n        self.max_seq_len = max_seq_len\n        self.rate_limit_delay = rate_limit_delay\n        self._call_fn = _call_claude if provider == \"claude\" else _call_openai\n\n    def _truncate(self, text):\n        words = text.split()\n        approx_tokens = int(self.max_seq_len * 0.75)\n        if len(words) > approx_tokens:\n            words = words[:approx_tokens]\n        return \" \".join(words)\n\n    def fit(self, X_train, y_train, **kwargs):\n        pass\n\n    def predict_texts(self, texts):\n        \"\"\"Predict depth for raw text inputs.\"\"\"\n        y_preds, y_probs = [], []\n        errors = 0\n        for i, text in enumerate(texts):\n            truncated = self._truncate(text)\n            try:\n                response = self._call_fn(truncated, self.model)\n                depth, confidence = _parse_llm_response(response)\n                y_preds.append(depth)\n                prob = np.zeros(NUM_DEPTHS)\n                prob[depth] = confidence\n                remaining = (1.0 - confidence) / max(NUM_DEPTHS - 1, 1)\n                for d in range(NUM_DEPTHS):\n                    if d != depth:\n                        prob[d] = remaining\n                y_probs.append(prob)\n            except Exception as e:\n                print(f\"  [{i}] API error: {e}\")\n                y_preds.append(0)\n                y_probs.append(np.ones(NUM_DEPTHS) / NUM_DEPTHS)\n                errors += 1\n\n            if (i + 1) % 20 == 0:\n                print(f\"  Progress: {i+1}/{len(texts)}\")\n            if self.rate_limit_delay > 0:\n                time.sleep(self.rate_limit_delay)\n\n        if errors > 0:\n            print(f\"  {errors}/{len(texts)} API errors.\")\n        return np.array(y_preds), np.array(y_probs)\n\n    def predict(self, X_test):\n        raise NotImplementedError(\"ZeroShotLLMBaseline requires raw text. Use predict_texts().\")\n\n    def predict_proba(self, X_test):\n        raise NotImplementedError(\"ZeroShotLLMBaseline requires raw text. Use predict_texts().\")\n\n\n# ===================================================================\n#  Unified Runner\n# ===================================================================\n\nFEATURE_BASED_METHODS = [\"ppl_reg_single\", \"ppl_reg\", \"ce_mlp\", \"coral\", \"diveye\", \"rf\", \"lr\"]\nTEXT_BASED_METHODS = [\"zeroshot\"]\n\nBASELINE_REGISTRY = {\n    \"ppl_reg_single\": \"PPL Regression (single: mean_ppl)\",\n    \"ppl_reg\":        \"PPL Regression (multi: 19-dim OLS)\",\n    \"ce_mlp\":         \"CE-MLP (DCOL ablation)\",\n    \"coral\":          \"CORAL Ordinal Regression\",\n    \"diveye\":         \"DivEye (XGBoost)\",\n    \"rf\":             \"Random Forest\",\n    \"lr\":             \"Logistic Regression\",\n    \"zeroshot\":       \"Zero-shot LLM\",\n}\n\nALL_METHODS = FEATURE_BASED_METHODS + TEXT_BASED_METHODS\n\n\ndef _make_baseline(method, args):\n    if method == \"ppl_reg_single\":\n        return PPLRegressionBaseline(mode=\"single\")\n    elif method == \"ppl_reg\":\n        return PPLRegressionBaseline(mode=\"multi\")\n    elif method == \"ce_mlp\":\n        return CEClassificationBaseline(\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\n            patience=args.patience, seed=args.seed,\n        )\n    elif method == \"coral\":\n        return CORALBaseline(\n            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,\n            patience=args.patience, seed=args.seed,\n        )\n    elif method == \"diveye\":\n        return DivEyeBaseline(seed=args.seed)\n    elif method == \"rf\":\n        return RandomForestBaseline(n_estimators=100, seed=args.seed)\n    elif method == \"lr\":\n        return LogisticRegressionBaseline(max_iter=1000, seed=args.seed)\n    elif method == \"zeroshot\":\n        return ZeroShotLLMBaseline(\n            provider=args.provider,\n            model=args.llm_model,\n            max_seq_len=args.max_seq_len,\n            rate_limit_delay=args.rate_limit_delay,\n        )\n    return None\n\n\ndef run_feature_baseline(method, X_train, y_train, X_val, y_val, X_test, y_test, args):\n    bl = _make_baseline(method, args)\n    if bl is None:\n        print(f\"Unknown method: {method}\")\n        return None\n    bl.fit(X_train, y_train, X_val=X_val, y_val=y_val)\n    y_pred = bl.predict(X_test)\n    y_prob = bl.predict_proba(X_test)\n    return evaluate(BASELINE_REGISTRY[method], y_test, y_pred, y_prob)\n\n\ndef run_zeroshot_baseline(texts, labels, args):\n    bl = _make_baseline(\"zeroshot\", args)\n    _, eval_idx = train_test_split(\n        np.arange(len(labels)), test_size=args.eval_split,\n        stratify=labels, random_state=args.seed,\n    )\n    eval_texts = [texts[i] for i in eval_idx]\n    eval_labels = labels[eval_idx]\n\n    if len(eval_texts) > args.max_eval_samples:\n        rng = np.random.RandomState(args.seed)\n        sample_idx = sorted(rng.choice(len(eval_texts), args.max_eval_samples, replace=False))\n        eval_texts = [eval_texts[i] for i in sample_idx]\n        eval_labels = eval_labels[sample_idx]\n\n    print(f\"Zero-shot: evaluating {len(eval_texts)} samples with {args.provider}/{bl.model}\")\n    print(f\"  Label distribution: {dict(Counter(eval_labels))}\")\n\n    y_pred, y_prob = bl.predict_texts(eval_texts)\n    return evaluate(BASELINE_REGISTRY[\"zeroshot\"], eval_labels, y_pred, y_prob)\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"Baseline battery for depth estimation.\")\n    p.add_argument(\"--method\", default=\"all\",\n                   choices=ALL_METHODS + [\"all\", \"all_features\"])\n    p.add_argument(\"--features_path\", \"--data_path\", default=\"data/features_all.jsonl\",\n                   dest=\"features_path\")\n    p.add_argument(\"--data_dirs\", nargs=\"+\", default=[\"data/\"],\n                   help=\"Directories containing depth_*.jsonl (for zero-shot)\")\n    p.add_argument(\"--output_dir\", default=\"results/baselines/\")\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--test_size\", type=float, default=0.15)\n    p.add_argument(\"--val_size\", type=float, default=0.15)\n    p.add_argument(\"--eval_split\", type=float, default=0.15)\n    p.add_argument(\"--epochs\", type=int, default=100)\n    p.add_argument(\"--batch_size\", type=int, default=256)\n    p.add_argument(\"--lr\", type=float, default=1e-3)\n    p.add_argument(\"--patience\", type=int, default=10)\n    p.add_argument(\"--max_seq_len\", type=int, default=512)\n    # Zero-shot LLM args\n    p.add_argument(\"--provider\", choices=[\"claude\", \"openai\"], default=\"claude\")\n    p.add_argument(\"--llm_model\", default=None,\n                   help=\"LLM model name (default: claude-sonnet-4-20250514 / gpt-4o)\")\n    p.add_argument(\"--max_eval_samples\", type=int, default=200,\n                   help=\"Max samples for zero-shot eval (API cost control)\")\n    p.add_argument(\"--rate_limit_delay\", type=float, default=0.5)\n    return p.parse_args()\n\n\ndef main():\n    args = parse_args()\n\n    if args.method == \"all\":\n        methods = FEATURE_BASED_METHODS\n        print(\"Running all feature-based baselines (use --method zeroshot for LLM baseline)\")\n    elif args.method == \"all_features\":\n        methods = FEATURE_BASED_METHODS\n    else:\n        methods = [args.method]\n\n    all_results = {}\n\n    feature_methods = [m for m in methods if m in FEATURE_BASED_METHODS]\n    text_methods = [m for m in methods if m in TEXT_BASED_METHODS]\n\n    if feature_methods:\n        print(f\"Loading features from {args.features_path} ...\")\n        X, y = load_features(args.features_path)\n        print(f\"  {X.shape[0]} samples, {X.shape[1]} features\")\n        print(f\"  Depth distribution: {dict(Counter(y))}\")\n\n        X_train, y_train, X_val, y_val, X_test, y_test = prepare_splits(\n            X, y, test_size=args.test_size, val_size=args.val_size, seed=args.seed\n        )\n        print(f\"  Train: {len(y_train)}, Val: {len(y_val)}, Test: {len(y_test)}\")\n\n        for m in feature_methods:\n            result = run_feature_baseline(\n                m, X_train, y_train, X_val, y_val, X_test, y_test, args\n            )\n            if result is not None:\n                all_results[m] = result\n\n    if text_methods:\n        if \"zeroshot\" in text_methods:\n            texts, labels = load_jsonl_texts(\n                args.data_dirs, max_samples=0, seed=args.seed\n            )\n            result = run_zeroshot_baseline(texts, labels, args)\n            if result is not None:\n                all_results[\"zeroshot\"] = result\n\n    if len(all_results) > 1:\n        print(f\"\\n{'='*60}\")\n        print(f\"  SUMMARY\")\n        print(f\"{'='*60}\")\n        print(f\"  {'Method':<35s} {'4-cls':>6s} {'3-cls':>6s} {'MAE':>6s}\")\n        print(f\"  {'-'*35} {'-'*6} {'-'*6} {'-'*6}\")\n        for m, r in all_results.items():\n            print(f\"  {r['method']:<35s} {r['acc_4class']:6.4f} {r['acc_3class']:6.4f} {r['mae']:6.4f}\")\n\n    os.makedirs(args.output_dir, exist_ok=True)\n    out_path = os.path.join(args.output_dir, \"baseline_results.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(all_results, f, indent=2, default=str)\n    print(f\"\\nResults saved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 967,
      "startLine": 1,
      "totalLines": 967
    }
  }
}
```

</details>

---


### Assistant

_source line 154_

Good, the file looks correct. Now deploying to server and running dry-run on feature-based baselines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7a5b072-af3a-4c7a-827e-4f61fc12b1ec",
  "uuid": "b487f6c7-1f48-44ed-a1c5-e33983d03d5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VpqXVHCuVyETApQCG1HbSq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13929,
      "cache_read_input_tokens": 93119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13929
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
