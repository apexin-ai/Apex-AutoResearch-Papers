# code gold set eval pipeline — Part 1 of 2

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Worker execution logs

[Transcript overview](../code-gold-set-eval-pipeline.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/26/266d5fbc7dd9ab6ff921.json)

## Before a recorded user message

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
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
    "mcp__agent-ml-research__read_registry",
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
  "uuid": "18bbebe7-ebce-4b3c-9ee3-e92452cbf6d2",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-agent-progress-probe/memory/"
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
    "resetsAt": 1778814000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "2251b5e9-4e8e-4738-874c-d60354f555cb",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by exploring the project structure to understand the existing codebase, then write the evaluation pipeline.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "e657738e-c6d4-499d-a50b-6cc7aec2d8d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EUZ5AwC77vxemnSHQwWkHW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11725,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11725
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

I'll explore the project structure first to understand existing code, then write the evaluation pipeline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "c547cb7a-457f-462d-b155-fb0c9b8f47a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EUZ5AwC77vxemnSHQwWkHW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11725,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11725
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Agent · `toolu_01VfW5EfnnaX5b9Xeuvm1upB`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Explore project structure",
  "prompt": "Explore the project at /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/ thoroughly. I need to understand:\n\n1. Full directory tree structure (especially src/, data/, artifacts/, models/)\n2. Feature extraction code in src/features/ - how structural features are extracted, what functions are available\n3. Model definitions in src/models/ - especially ProgressProbe (GRU+attention), how it's loaded and used for inference\n4. Data files in data/ - what's in windows_labeled.jsonl, embeddings.pt, any other data files\n5. Any existing evaluation code\n6. How sklearn classifiers (RF/GB/LR) are trained and saved - look for pickle files or training scripts\n7. LLM-as-judge code - how predictions are cached\n8. Any config files or constants\n\nBe very thorough - search across src/, data/, artifacts/, scripts/, and any other directories. Read key files fully to understand APIs and data formats."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "7a00f401-a3a9-4d3b-a59a-8c5a371a5240",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EUZ5AwC77vxemnSHQwWkHW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11725,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11725
      },
      "output_tokens": 28,
      "service_tier": "standard",
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Explore project structure",
  "task_type": "local_agent",
  "prompt": "Explore the project at /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/ thoroughly. I need to understand:\n\n1. Full directory tree structure (especially src/, data/, artifacts/, models/)\n2. Feature extraction code in src/features/ - how structural features are extracted, what functions are available\n3. Model definitions in src/models/ - especially ProgressProbe (GRU+attention), how it's loaded and used for inference\n4. Data files in data/ - what's in windows_labeled.jsonl, embeddings.pt, any other data files\n5. Any existing evaluation code\n6. How sklearn classifiers (RF/GB/LR) are trained and saved - look for pickle files or training scripts\n7. LLM-as-judge code - how predictions are cached\n8. Any config files or constants\n\nBe very thorough - search across src/, data/, artifacts/, scripts/, and any other directories. Read key files fully to understand APIs and data formats.",
  "uuid": "58e06c6f-abdf-4553-ba8c-a2f3c1185b65",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


## Round 1

## Round 1

178 recorded events


### User

_source line 8 · 2026-05-14T22:40:12.180Z_

Explore the project at /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/ thoroughly. I need to understand:

1. Full directory tree structure (especially src/, data/, artifacts/, models/)
2. Feature extraction code in src/features/ - how structural features are extracted, what functions are available
3. Model definitions in src/models/ - especially ProgressProbe (GRU+attention), how it's loaded and used for inference
4. Data files in data/ - what's in windows_labeled.jsonl, embeddings.pt, any other data files
5. Any existing evaluation code
6. How sklearn classifiers (RF/GB/LR) are trained and saved - look for pickle files or training scripts
7. LLM-as-judge code - how predictions are cached
8. Any config files or constants

Be very thorough - search across src/, data/, artifacts/, scripts/, and any other directories. Read key files fully to understand APIs and data formats.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "54c2d60f-2db8-4c44-8c90-f8d4dd5cefb9"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 18330,
    "tool_uses": 1,
    "duration_ms": 1882
  },
  "last_tool_name": "Bash",
  "uuid": "f9e43c48-56a1-44c9-a790-bc855428c1e4",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Bash · `toolu_01JwrYq1w8TgyJW61u49v71p`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe -type f -name \"*.py\" -o -name \"*.json\" -o -name \"*.pt\" -o -name \"*.pkl\" -o -name \"*.yaml\" -o -name \"*.txt\" | head -100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "33a72b9b-e2bd-4fa7-a85d-65d20944895e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RDcymiPXjVUK7318EWQy3q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18321,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18321,
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

_source line 11 · 2026-05-14T22:40:14.242Z_

<details><summary>↩ Tool result · `toolu_01JwrYq1w8TgyJW61u49v71p`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/figures/paper/gen_fig_lf_temporal.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/figures/paper/gen_fig_pipeline.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/figures/paper/gen_fig_data_scaling.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/_acl_template/anthology.bib.txt
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_code_oh-full-finetune_20260514T150345_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_analysis_lf_temporal_dynamics_20260514T095842_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_paper_writing_related_work_20260514T220345_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_infra_sync_v2_code_data_20260514T063519_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_paper_writing_introduction_20260514T221107_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_code_lf1_fix_rerun_v2_20260514T054930_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_code_outcome-bp-3seed_20260514T124930_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_check_ablation-lf-holdout-v2_20260514T145806_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_train_train-without-ob_20260514T135043_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_data_annotation_materials_20260514T102725_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_paper_writing_analysis_20260514T215253_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_fix_data-scaling-v2_20260514T143449_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_fix_gold-pipeline-probe-split_20260514T194423_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_infra_openhands-eval-followup-v2_20260514T115335_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_check_data-scaling-v2_20260514T145800_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_paper_figure_20260514T190818_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_paper_writing_experiments_20260514T211641_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_ssh_encoder-ablation-gpu-check_20260514T122512_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_research_openhands_data_explore_20260514T081819_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_code_flyingsquid-baseline_20260514T110819_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_infra_openhands_cross_agent_20260514T095826_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_diag_server-status-collect-results_20260514T143048_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_fix_openhands-fewshot-device_20260514T140527_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_infra_llm_judge_monitor_20260514T112716_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_analysis_error-analysis-v3_20260514T125143_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_analysis_cross-domain-bootstrap_20260514T220201_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_infra_llm-judge-monitor_20260514T115002_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_submit_baseline-meanpool-lr_20260514T095131_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_eval_lf_oracle_run_20260514T090024_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_code_phase1_code_review_20260514T062729_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_diagnose_emb_001_verify_20260514T074440_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_analysis_stag-rate-audit_20260514T222656_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_eval_error_analysis_20260514T084032_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_code_openhands-fewshot-probe_20260514T122155_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_analysis_encoder-ablation-results_20260514T135021_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_eval_cosinesim-check_20260514T154822_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_diag_oh-cmdrep-data-discrepancy_20260514T154005_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_code_structural-on-twv_20260514T173953_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_code_data-scaling-fix_20260514T183227_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_paper_research_20260514T194953_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_train_oh-full-finetune_20260514T150243_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_infra_gpu_env_setup_20260514T060135_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_fix_data-scaling_20260514T143443_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_infra_gpu-identity-check_20260514T124017_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_code_probe001_dryrun_20260514T071715_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_paper_writing_method_20260514T212853_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_multiseed_e5large-probe_20260514T215551_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_infra_openhands_eval_followup_20260514T102609_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_paper_writing_analysis_20260514T215456_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_ops_gpu-status-check_20260514T111601_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_diag_baseline-f1-discrepancy_20260514T152624_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_diag_ssh-gpu-check_20260514T134001_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_diag_post-oom-status_20260514T141017_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_code_phase0_lfs_windows_20260514T053644_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_train_ablation-supcon_20260514T161233_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_diag_baseline-llm-judge-final_20260514T140715_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_eval_cosine_baseline_debug_20260514T083817_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_analysis_baseline-llm-judge-collect_20260514T134301_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_analysis_paired-bootstrap_20260514T212555_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_analysis_gpu-dual-inference_20260514T221738_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_multiseed_bgem3-probe_20260514T215558_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_research_literature-compilation_20260514T183143_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_eval_lf_oracle_conf0_20260514T092025_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_code_meanpool_lr_impl_and_run_20260514T094501_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_infra_openhands_relabel_and_eval_20260514T111119_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_infra_data_code_sync_20260514T060732_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_code_openhands_lf_fix_20260514T104722_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_infra_env-setup-data-explore_20260514T044911_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_code_llm_judge_baseline_20260514T102134_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_analysis_f1-stag-breakdown_20260514T151440_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_data_openhands-annotation-materials_20260514T124009_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_exp_conf2-subset_20260514T184004_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_code_temporal-label-model_20260514T170841_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_analysis_twv-sigma-sweep_20260514T174032_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_analysis_structural-data-scaling_20260514T194312_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_diag_check-running-experiments_20260514T145754_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_monitor_baseline-llm-judge_20260514T134529_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_analysis_oh-lf-temporal_20260514T174011_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_infra_ssh_check_autodl_20260514T055601_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_analysis_gte-large-check_20260514T134036_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_train_oh-cmdrep-ablation_20260514T150300_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_analysis_f1-stag-trajlen_20260514T220654_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_train_encoder-ablation-dual_20260514T134503_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_code_baselines_verify_20260514T071724_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_infra_sync_eval_train_20260514T073708_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_paper_writing_appendix_20260514T221502_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_data_annotation-fix_20260514T115316_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_infra_emb001_check_result_20260514T075727_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_code_encoder-ablation-probe-train_20260514T134014_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_diagnose_probe_001_20260514T080733_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_eval_bgem3-multiseed-test_20260514T221221_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_research_annotation-prep_20260514T111216_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_code_cross-agent-structural-baseline_20260514T170555_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_infra_tmux_and_submit_emb001_20260514T063932_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_analysis_lf-temporal-dynamics_20260514T150420_result.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "2a468881-ffa4-4f09-8593-6cdb6a0bba5d"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 24504,
    "tool_uses": 2,
    "duration_ms": 3441
  },
  "last_tool_name": "Bash",
  "uuid": "cad28529-756d-4123-aea3-8c3840e99781",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Bash · `toolu_01LjDef9984UQHDLH2uWw3wc`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "03e7ebc3-8c11-4f2c-8a8e-bb03e6a034ab",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Eb2A9ipfdsNk1Zp2ox1fAX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6170,
      "cache_read_input_tokens": 18321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6170,
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

_source line 14 · 2026-05-14T22:40:15.674Z_

<details><summary>↩ Tool result · `toolu_01LjDef9984UQHDLH2uWw3wc`</summary>

```text
total 372
drwxr-xr-x 10 ubuntu ubuntu  4096 May 14 22:39 .
drwxrwxr-x  4 ubuntu ubuntu  4096 May 14 04:18 ..
drwxr-xr-x  3 ubuntu ubuntu  4096 May 14 04:18 .claude
drwxr-xr-x  6 ubuntu ubuntu  4096 May 14 05:50 .venv
-rw-r--r--  1 ubuntu ubuntu 12784 May 14 22:40 AGENTS.md
-rw-r--r--  1 ubuntu ubuntu     0 May 14 04:20 ROADMAP.lock
-rw-------  1 ubuntu ubuntu  5256 May 14 22:26 ROADMAP.md
drwxr-xr-x 32 ubuntu ubuntu  4096 May 14 22:16 artifacts
drwxr-xr-x  2 ubuntu ubuntu 24576 May 14 22:31 checkpoints
-rw-r--r--  1 ubuntu ubuntu  7147 May 14 13:24 data_volume_control.py
-rw-r--r--  1 ubuntu ubuntu     0 May 14 04:20 decisions.lock
-rw-------  1 ubuntu ubuntu 49129 May 14 22:26 decisions.yaml
drwxr-xr-x  4 ubuntu ubuntu  4096 May 14 05:47 docs
-rwxr-xr-x  1 ubuntu ubuntu     0 May 14 05:47 dream_registry.lock
-rw-------  1 ubuntu ubuntu  4055 May 14 22:36 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu  4060 May 14 22:36 dream_registry.yaml.bak
-rw-r--r--  1 ubuntu ubuntu 27961 May 14 19:18 evaluate_gold_set.py
-rw-r--r--  1 ubuntu ubuntu     0 May 14 16:23 experiment_plan.lock
-rw-------  1 ubuntu ubuntu  5367 May 14 22:39 experiment_plan.yaml
drwxr-xr-x  3 ubuntu ubuntu  4096 May 14 18:48 figures
-rw-r--r--  1 ubuntu ubuntu 27371 May 14 20:48 literature_map.yaml
drwxr-xr-x  4 ubuntu ubuntu  4096 May 14 04:22 logs
-rw-r--r--  1 ubuntu ubuntu  4178 May 14 22:13 memory.md
-rw-r--r--  1 ubuntu ubuntu 12729 May 14 22:12 paper_framing.md
-rw-r--r--  1 ubuntu ubuntu     0 May 14 21:22 paper_provenance.lock
-rw-------  1 ubuntu ubuntu 16922 May 14 22:29 paper_provenance.yaml
-rw-r--r--  1 ubuntu ubuntu     0 May 14 06:11 registry.lock
-rw-------  1 ubuntu ubuntu 83186 May 14 22:31 registry.yaml
-rw-r--r--  1 ubuntu ubuntu  1379 May 14 22:31 report.md
-rwxr-xr-x  1 ubuntu ubuntu     0 May 14 04:18 study_status.lock
drwxr-xr-x  3 ubuntu ubuntu  4096 May 14 22:30 task_context
-rw-r--r--  1 ubuntu ubuntu 20638 May 14 22:12 writing_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "b3564140-5376-48df-a03e-130bb0bdcd64"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 25547,
    "tool_uses": 3,
    "duration_ms": 4929
  },
  "last_tool_name": "Bash",
  "uuid": "b95dfe4f-bc8c-4597-a368-536fa5a00d0d",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_01292X3ruie4ZTi8gDRdzkYy`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe -maxdepth 3 -type d | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "cd28a761-860a-44f3-b41f-11f234755805",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0194THTF1SsRbmaf1HJM2N9k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 24491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1041,
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

_source line 17 · 2026-05-14T22:40:17.176Z_

<details><summary>↩ Tool result · `toolu_01292X3ruie4ZTi8gDRdzkYy`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/.claude
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/.claude/sessions
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/.claude/sessions/agent_11ed1ef2
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/.claude/sessions/agent_d092e844
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/.claude/sessions/agent_db1f8d54
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/.claude/sessions/agent_efeee377
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/.claude/sessions/briefer_3751096d
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/.claude/sessions/director_e5138af7
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/.claude/sessions/paper_agent_73e7a7ea
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/.claude/sessions/reviewer_5c65abec
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/.venv
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/.venv/bin
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/.venv/include
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/.venv/lib
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/.venv/lib/python3.14
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/.venv/share
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/.venv/share/man
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/__pycache__
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/chart
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/data
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/intermediate
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/paper
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/report
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/ablation-architecture
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/ablation-architecture/data
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/ablation-supcon
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/ablation-supcon/data
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/ablation-window-size
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/ablation-window-size/data
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/baseline_flyingsquid
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/baseline_flyingsquid/report
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/confidence-gradient
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/confidence-gradient/data
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/cross-agent-eval
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/cross-agent-eval/report
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/cross-agent-no-cmdrep
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/cross-agent-no-cmdrep/data
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/data
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/data-volume-control
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/data-volume-control/report
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/dream_reports
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/dream_reports/dream_20260514T081656
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/dream_reports/dream_20260514T095527
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/dream_reports/dream_20260514T184058
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/dream_reports/dream_20260514T214352
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/encoder-ablation-probe-bgem3
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/encoder-ablation-probe-bgem3/data
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/human-annotation
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/human-annotation/data
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/human-annotation/report
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/lf-temporal-dynamics
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/lf-temporal-dynamics/chart
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/lf-temporal-dynamics/data
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/multiseed-structural
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/multiseed-structural/data
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/non-nlp-baseline
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/non-nlp-baseline/report
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/oh-cmdrep-ablation
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/oh-cmdrep-ablation/data
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/oh-full-finetune
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/oh-full-finetune/data
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/oh-lf-temporal-dynamics
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/oh-lf-temporal-dynamics/data
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/openhands-fewshot-probe
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/openhands-fewshot-probe/intermediate
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/outcome-bp-sensitivity
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/outcome-bp-sensitivity/report
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/probe-002
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/probe-002/report
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/probe_001
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/probe_001/data
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/structural-data-scaling
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/structural-data-scaling/data
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/structural-on-twv
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/structural-on-twv/data
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/temporal-label-model
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/temporal-label-model/report
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/tlm-probe-comparison
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/tlm-probe-comparison/report
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/train-without-ob
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/train-without-ob/data
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/twv-ablation
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/twv-ablation/data
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/checkpoints
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/_acl_template
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/results
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/results/figures
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/figures
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/figures/paper
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/chats
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/chats/archive
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/task_context
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/task_context/history
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/task_context/history/agent
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/task_context/history/director
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/task_context/history/reviewer
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "10afb3e1-d532-4333-a866-e5c89e30cbd2"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 29238,
    "tool_uses": 4,
    "duration_ms": 6703
  },
  "last_tool_name": "Bash",
  "uuid": "af3ad9fd-bd61-4024-9bc6-ec716db0e343",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Bash · `toolu_01Pc84zMgrtUdttEpZAmHobX`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe -maxdepth 2 -name \"*.py\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "89c4ce93-7ed9-4aba-ac7a-d69bccaeef05",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YDH2QpJvU1cRBPQf1uKsYH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3689,
      "cache_read_input_tokens": 25532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3689,
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

_source line 20 · 2026-05-14T22:40:18.948Z_

<details><summary>↩ Tool result · `toolu_01Pc84zMgrtUdttEpZAmHobX`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/data_volume_control.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/window_extractor.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/evaluate.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/oh_cmdrep_ablation.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/probe_model.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/labeling_functions.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/train_architecture_ablation.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/lf_oracle_baseline.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/label_quality_check_v2.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/train_supcon.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/lf_conflict_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/label_quality_check.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/oh_full_finetune.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/generate_embeddings.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/fewshot_probe.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/non_nlp_baseline.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/baselines.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/baseline_meanpool_lr.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/data_scaling.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/baseline_llm_judge.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "816f5e8f-f577-4b25-9088-eaae431d4cbb"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 30154,
    "tool_uses": 5,
    "duration_ms": 8364
  },
  "last_tool_name": "Bash",
  "uuid": "34e0e79a-e106-48f4-b569-8b7e9a143ab9",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_013PZeuSh4yjUHh5hZByEwsJ`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe -maxdepth 2 -name \"*.jsonl\" -o -name \"*.pt\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "f86a7181-2888-4b4b-8ae0-1b38795a7636",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011H6yPZSX8tMUP7aMysG9s2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 848,
      "cache_read_input_tokens": 29221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 848,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-14T22:40:20.604Z_

<details><summary>↩ Tool result · `toolu_013PZeuSh4yjUHh5hZByEwsJ`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/ralph_loop_timeline.jsonl
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "684c21da-cce9-4de0-8e1e-837df9dee30b"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 30370,
    "tool_uses": 6,
    "duration_ms": 9558
  },
  "last_tool_name": "Bash",
  "uuid": "0b058157-9e7b-43ca-a00f-6feace32f02c",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Bash · `toolu_01Q9U1oaqb5aaDyqW84H3eiv`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts -name \"*.jsonl\" -o -name \"*.pt\" -o -name \"*.pkl\" 2>/dev/null | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "0b751081-ae40-4993-b109-983ccff4c331",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AfEw1Tf1KfyrEr8bnrGZGK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 151,
      "cache_read_input_tokens": 30069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 151,
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

_source line 26 · 2026-05-14T22:40:21.830Z_

<details><summary>↩ Tool result · `toolu_01Q9U1oaqb5aaDyqW84H3eiv`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/data/windows_labeled_60a35a.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/data/swe_agent_trajectories_5000.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/data/swe_agent_trajectories_1000.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/data/windows_labeled.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/data/label_quality_details_v2.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/data/swe_agent_trajectories_5000.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/data/swe_agent_trajectories_1000.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/data/windows_labeled.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/data/label_quality_details.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/data/label_quality_details_v2.jsonl
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "14dafea7-77f0-442c-be66-1fa2b37b3e69"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 31022,
    "tool_uses": 7,
    "duration_ms": 11019
  },
  "last_tool_name": "Bash",
  "uuid": "c9dd25c9-855a-472c-9744-319afce5759b",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_01DQjs92MynMDQ5jL4uHLFg4`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts -maxdepth 2 -type f -name \"*.py\" | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "f27daeb6-1825-4e76-b1c7-88f38bafea39",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WD8RhkamvPk2ffn45ndNdg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 651,
      "cache_read_input_tokens": 30220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 651,
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

_source line 29 · 2026-05-14T22:40:23.268Z_

<details><summary>↩ Tool result · `toolu_01DQjs92MynMDQ5jL4uHLFg4`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/baseline_llm_judge.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/baseline_meanpool_lr.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/baselines.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/data_loader.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/data_scaling.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/download_5k.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/evaluate.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/fewshot_probe.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/generate_embeddings.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/label_quality_check.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/label_quality_check_v2.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/labeling_functions.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/lf_conflict_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/lf_oracle_baseline.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/non_nlp_baseline.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/oh_cmdrep_ablation.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/oh_full_finetune.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/probe_model.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/train_architecture_ablation.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/train_probe.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/train_supcon.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/window_extractor.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "95cd5a75-f048-409c-8d4a-adf439928db6"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Reading artifacts/probe_model.py",
  "usage": {
    "total_tokens": 31934,
    "tool_uses": 8,
    "duration_ms": 12569
  },
  "last_tool_name": "Read",
  "uuid": "756a2bfd-ad43-46d7-90f1-ed0d55a53812",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01TKE36mi8H2EJwv91kxQzec`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/probe_model.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "aee87a47-cc57-4a72-bf25-65c78b9dfad1",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TVta2McsihiPm3qeSSWb7F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 910,
      "cache_read_input_tokens": 30871,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 910,
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

_source line 32 · 2026-05-14T22:40:24.760Z_

<details><summary>↩ Tool result · `toolu_01TKE36mi8H2EJwv91kxQzec`</summary>

```text
1	#!/usr/bin/env python3
2	"""GRU-based progress probe model, dataset, and data splitting utilities."""
3	
4	import random
5	from pathlib import Path
6	
7	import torch
8	import torch.nn as nn
9	from torch.utils.data import Dataset
10	
11	
12	class ProgressProbe(nn.Module):
13	    """2-layer GRU probe for progress/stagnation binary classification.
14	
15	    Input:  (batch, seq_len, embed_dim)
16	    Output: (batch,) logits (apply sigmoid for probabilities)
17	    """
18	
19	    def __init__(self, embed_dim: int, hidden_size: int = 256, num_layers: int = 2, dropout: float = 0.1):
20	        super().__init__()
21	        self.gru = nn.GRU(
22	            embed_dim,
23	            hidden_size,
24	            num_layers=num_layers,
25	            batch_first=True,
26	            dropout=dropout if num_layers > 1 else 0.0,
27	        )
28	        self.classifier = nn.Linear(hidden_size, 1)
29	
30	    def forward(self, x: torch.Tensor, lengths: torch.Tensor = None) -> torch.Tensor:
31	        if lengths is not None:
32	            x = nn.utils.rnn.pack_padded_sequence(x, lengths.cpu(), batch_first=True, enforce_sorted=False)
33	        _, hidden = self.gru(x)
34	        out = hidden[-1]  # last layer hidden: (batch, hidden_size)
35	        return self.classifier(out).squeeze(-1)
36	
37	
38	class WindowDataset(Dataset):
39	    """Dataset of pre-computed window embeddings + binary labels."""
40	
41	    def __init__(self, embeddings: list[torch.Tensor], labels: list[int]):
42	        assert len(embeddings) == len(labels)
43	        self.embeddings = embeddings
44	        self.labels = labels
45	
46	    def __len__(self):
47	        return len(self.labels)
48	
49	    def __getitem__(self, idx):
50	        return self.embeddings[idx], self.labels[idx]
51	
52	
53	def collate_fn(batch):
54	    """Pad variable-length window embeddings to the max length in the batch."""
55	    embeddings_list, labels_list = zip(*batch)
56	    lengths = torch.tensor([e.shape[0] for e in embeddings_list], dtype=torch.long)
57	    max_len = lengths.max().item()
58	    embed_dim = embeddings_list[0].shape[1]
59	
60	    padded = torch.zeros(len(batch), max_len, embed_dim)
61	    for i, e in enumerate(embeddings_list):
62	        padded[i, : e.shape[0]] = e
63	
64	    labels = torch.tensor(labels_list, dtype=torch.float32)
65	    return padded, labels, lengths
66	
67	
68	def split_by_instance(
69	    instance_ids: list[str],
70	    train_ratio: float = 0.7,
71	    val_ratio: float = 0.15,
72	    seed: int = 42,
73	) -> tuple[list[int], list[int], list[int]]:
74	    """Split indices so all windows from the same instance stay in one split."""
75	    unique = sorted(set(instance_ids))
76	    rng = random.Random(seed)
77	    rng.shuffle(unique)
78	
79	    n = len(unique)
80	    n_train = int(n * train_ratio)
81	    n_val = int(n * val_ratio)
82	
83	    train_set = set(unique[:n_train])
84	    val_set = set(unique[n_train : n_train + n_val])
85	
86	    train_idx, val_idx, test_idx = [], [], []
87	    for i, iid in enumerate(instance_ids):
88	        if iid in train_set:
89	            train_idx.append(i)
90	        elif iid in val_set:
91	            val_idx.append(i)
92	        else:
93	            test_idx.append(i)
94	
95	    return train_idx, val_idx, test_idx
96	
97	
98	def load_split_datasets(
99	    data_path: str | Path, seed: int = 42
100	) -> tuple[WindowDataset, WindowDataset, WindowDataset, dict]:
101	    """Load embeddings.pt and return train/val/test WindowDatasets + split info."""
102	    data = torch.load(data_path, weights_only=False)
103	    embeddings = data["embeddings"]
104	    labels = data["labels"]
105	    instance_ids = data["instance_ids"]
106	
107	    train_idx, val_idx, test_idx = split_by_instance(instance_ids, seed=seed)
108	
109	    def subset(indices):
110	        return WindowDataset([embeddings[i] for i in indices], [labels[i] for i in indices])
111	
112	    split_info = {
113	        "train_indices": train_idx,
114	        "val_indices": val_idx,
115	        "test_indices": test_idx,
116	        "seed": seed,
117	        "embed_dim": data["embed_dim"],
118	    }
119	    return subset(train_idx), subset(val_idx), subset(test_idx), split_info
120	
121	
122	if __name__ == "__main__":
123	    print("=== ProgressProbe forward pass test ===")
124	    embed_dim = 1024
125	    batch_size = 4
126	
127	    model = ProgressProbe(embed_dim=embed_dim)
128	    print(f"Model: {model}")
129	    total_params = sum(p.numel() for p in model.parameters())
130	    print(f"Total parameters: {total_params:,}")
131	
132	    # Random data with variable sequence lengths
133	    lengths = torch.tensor([3, 7, 5, 2])
134	    max_len = lengths.max().item()
135	    x = torch.randn(batch_size, max_len, embed_dim)
136	    logits = model(x, lengths)
137	    probs = torch.sigmoid(logits)
138	
139	    print(f"Input shape:  {x.shape}")
140	    print(f"Lengths:      {lengths.tolist()}")
141	    print(f"Logits shape: {logits.shape}")
142	    print(f"Logits:       {logits.tolist()}")
143	    print(f"Probs:        {[f'{p:.4f}' for p in probs.tolist()]}")
144	
145	    # Test dataset + collate
146	    dummy_embeds = [torch.randn(l, embed_dim) for l in [3, 5, 2, 8]]
147	    dummy_labels = [1, 0, 1, 0]
148	    ds = WindowDataset(dummy_embeds, dummy_labels)
149	    batch = [ds[i] for i in range(len(ds))]
150	    padded, labels, lens = collate_fn(batch)
151	    print(f"\nCollate test: padded={padded.shape}, labels={labels.shape}, lengths={lens.tolist()}")
152	
153	    # Test split
154	    instance_ids = ["a", "a", "b", "b", "c", "c", "d", "d", "e", "e"]
155	    tr, va, te = split_by_instance(instance_ids, seed=42)
156	    print(f"\nSplit test (10 samples, 5 instances): train={len(tr)}, val={len(va)}, test={len(te)}")
157	    print("All tests passed.")
158	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "71cffe2b-e2a2-48b2-a9fb-9750a9733482"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Reading artifacts/window_extractor.py",
  "usage": {
    "total_tokens": 34179,
    "tool_uses": 9,
    "duration_ms": 14563
  },
  "last_tool_name": "Read",
  "uuid": "7b5bf7ce-1fd3-4d9c-a0da-cbc938b4b53e",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_017UQq7XwHWEJfk2cysihCd7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/window_extractor.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "a01bdbe6-5c87-4992-aeaa-3e06edd5d4e2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014dzWfCiVkp6MU3vpE8GAw9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 2241,
      "cache_read_input_tokens": 31781,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2241,
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

_source line 35 · 2026-05-14T22:40:26.755Z_

<details><summary>↩ Tool result · `toolu_017UQq7XwHWEJfk2cysihCd7`</summary>

```text
1	"""Sliding window extraction and labeling pipeline for agent_progress_probe."""
2	
3	from __future__ import annotations
4	
5	import json
6	import sys
7	from collections import Counter
8	from pathlib import Path
9	
10	sys.path.insert(0, str(Path(__file__).parent))
11	
12	from data_loader import Step, Trajectory, load_trajectories_streaming
13	from labeling_functions import ALL_LFS, ABSTAIN
14	
15	WINDOW_SIZE_PAIRS = 5  # 5 action-observation pairs = 10 steps
16	STRIDE_PAIRS = 2       # slide by 2 pairs = 4 steps
17	WINDOW_SIZE_STEPS = WINDOW_SIZE_PAIRS * 2  # 10
18	STRIDE_STEPS = STRIDE_PAIRS * 2            # 4
19	MIN_STEPS_FOR_WINDOW = 12  # system + issue + at least 10 interaction steps
20	
21	
22	def extract_windows(trajectory: Trajectory) -> list[dict]:
23	    """Extract sliding windows from a trajectory.
24	
25	    Skips step 0 (system) and step 1 (issue description).
26	    Returns list of window dicts with steps and metadata.
27	    """
28	    # Start from step 2 (first ai action after issue)
29	    interaction_steps = [s for s in trajectory.steps if s.index >= 2]
30	
31	    if not interaction_steps:
32	        return []
33	
34	    trajectory_id = f"{trajectory.instance_id}__{trajectory.model_name}__r{trajectory.row_index}"
35	    common = {
36	        "trajectory_id": trajectory_id,
37	        "instance_id": trajectory.instance_id,
38	        "row_index": trajectory.row_index,
39	    }
40	    windows = []
41	
42	    if len(interaction_steps) < WINDOW_SIZE_STEPS:
43	        # Short trajectory: single window with all available steps
44	        windows.append({
45	            **common,
46	            "window_idx": 0,
47	            "steps": interaction_steps,
48	            "step_indices": [s.index for s in interaction_steps],
49	            "short_trajectory": True,
50	        })
51	    else:
52	        idx = 0
53	        while idx + WINDOW_SIZE_STEPS <= len(interaction_steps):
54	            w_steps = interaction_steps[idx:idx + WINDOW_SIZE_STEPS]
55	            windows.append({
56	                **common,
57	                "window_idx": len(windows),
58	                "steps": w_steps,
59	                "step_indices": [s.index for s in w_steps],
60	                "short_trajectory": False,
61	            })
62	            idx += STRIDE_STEPS
63	
64	        # If there are remaining steps that form a partial window at the end,
65	        # include them only if we haven't already covered them
66	        if idx < len(interaction_steps) and idx != 0:
67	            remaining = interaction_steps[idx:]
68	            if len(remaining) >= 4:  # at least 2 pairs
69	                windows.append({
70	                    **common,
71	                    "window_idx": len(windows),
72	                    "steps": remaining,
73	                    "step_indices": [s.index for s in remaining],
74	                    "short_trajectory": False,
75	                })
76	
77	    return windows
78	
79	
80	def label_windows(windows: list[dict], trajectory: Trajectory) -> list[dict]:
81	    """Apply all labeling functions to extracted windows."""
82	    total_windows = len(windows)
83	
84	    for i, w in enumerate(windows):
85	        position = {
86	            "window_idx": i,
87	            "total_windows": total_windows,
88	            "is_last": i == total_windows - 1,
89	        }
90	        labels = {}
91	        for lf_name, lf_fn in ALL_LFS:
92	            labels[lf_name] = lf_fn(w["steps"], trajectory, position)
93	
94	        w["labels"] = labels
95	
96	        # Majority vote (excluding abstains)
97	        non_abstain = [v for v in labels.values() if v != ABSTAIN]
98	        if non_abstain:
99	            counts = Counter(non_abstain)
100	            w["majority_label"] = counts.most_common(1)[0][0]
101	            w["confidence"] = counts.most_common(1)[0][1]
102	        else:
103	            w["majority_label"] = ABSTAIN
104	            w["confidence"] = 0
105	
106	    return windows
107	
108	
109	def process_trajectory(trajectory: Trajectory) -> list[dict]:
110	    """Full pipeline: extract windows and apply labels."""
111	    windows = extract_windows(trajectory)
112	    if not windows:
113	        return []
114	    return label_windows(windows, trajectory)
115	
116	
117	def window_to_serializable(w: dict) -> dict:
118	    """Convert a window dict to JSON-serializable format (no Step objects)."""
119	    return {
120	        "trajectory_id": w["trajectory_id"],
121	        "instance_id": w["instance_id"],
122	        "row_index": w["row_index"],
123	        "window_idx": w["window_idx"],
124	        "step_indices": w["step_indices"],
125	        "short_trajectory": w.get("short_trajectory", False),
126	        "labels": w["labels"],
127	        "majority_label": w["majority_label"],
128	        "confidence": w["confidence"],
129	    }
130	
131	
132	def run_pipeline(data_path: str | Path, output_path: str | Path, limit: int | None = None):
133	    """Run the full pipeline on all trajectories and save results."""
134	    data_path = Path(data_path)
135	    output_path = Path(output_path)
136	    output_path.parent.mkdir(parents=True, exist_ok=True)
137	
138	    # Statistics counters
139	    total_windows = 0
140	    total_trajectories = 0
141	    short_trajectories = 0
142	    resolved_windows = 0
143	    unresolved_windows = 0
144	
145	    lf_counts = {name: Counter() for name, _ in ALL_LFS}
146	    majority_counts = Counter()
147	    high_conf_counts = Counter()  # confidence >= 2
148	    agreement_total = 0
149	    agreement_agree = 0
150	
151	    resolved_label_counts = Counter()
152	    unresolved_label_counts = Counter()
153	
154	    with open(output_path, "w") as fout:
155	        for traj in load_trajectories_streaming(data_path, limit=limit):
156	            total_trajectories += 1
157	            windows = process_trajectory(traj)
158	
159	            if not windows:
160	                continue
161	
162	            if windows[0].get("short_trajectory"):
163	                short_trajectories += 1
164	
165	            for w in windows:
166	                total_windows += 1
167	
168	                if traj.target:
169	                    resolved_windows += 1
170	                else:
171	                    unresolved_windows += 1
172	
173	                # Per-LF stats
174	                for lf_name, _ in ALL_LFS:
175	                    label = w["labels"][lf_name]
176	                    lf_counts[lf_name][label] += 1
177	
178	                # Majority vote stats
179	                majority_counts[w["majority_label"]] += 1
180	                if w["confidence"] >= 2:
181	                    high_conf_counts[w["majority_label"]] += 1
182	
183	                # Agreement: when >=2 LFs are non-abstain
184	                non_abstain_labels = [v for v in w["labels"].values() if v != ABSTAIN]
185	                if len(non_abstain_labels) >= 2:
186	                    agreement_total += 1
187	                    if len(set(non_abstain_labels)) == 1:
188	                        agreement_agree += 1
189	
190	                # By resolved/unresolved
191	                if traj.target:
192	                    resolved_label_counts[w["majority_label"]] += 1
193	                else:
194	                    unresolved_label_counts[w["majority_label"]] += 1
195	
196	                # Write serialized window
197	                fout.write(json.dumps(window_to_serializable(w)) + "\n")
198	
199	            if total_trajectories % 100 == 0:
200	                print(f"  Processed {total_trajectories} trajectories, {total_windows} windows...")
201	
202	    # Generate report
203	    stats = {
204	        "total_windows": total_windows,
205	        "total_trajectories": total_trajectories,
206	        "short_trajectories": short_trajectories,
207	        "resolved_windows": resolved_windows,
208	        "unresolved_windows": unresolved_windows,
209	        "lf_counts": {k: dict(v) for k, v in lf_counts.items()},
210	        "majority_counts": dict(majority_counts),
211	        "high_conf_counts": dict(high_conf_counts),
212	        "agreement_total": agreement_total,
213	        "agreement_agree": agreement_agree,
214	        "resolved_label_counts": dict(resolved_label_counts),
215	        "unresolved_label_counts": dict(unresolved_label_counts),
216	    }
217	
218	    return stats
219	
220	
221	def generate_report(stats: dict, report_path: str | Path):
222	    """Generate markdown statistics report."""
223	    report_path = Path(report_path)
224	
225	    total = stats["total_windows"]
226	    lines = []
227	    lines.append("# Label Statistics Report")
228	    lines.append("")
229	    lines.append("## 1. 窗口总数")
230	    lines.append("")
231	    lines.append(f"| 指标 | 值 |")
232	    lines.append(f"|------|-----|")
233	    lines.append(f"| 总窗口数 | {total:,} |")
234	    lines.append(f"| 总轨迹数 | {stats['total_trajectories']:,} |")
235	    lines.append(f"| 短轨迹数 (<12 steps) | {stats['short_trajectories']:,} |")
236	    lines.append(f"| Resolved 轨迹窗口 | {stats['resolved_windows']:,} |")
237	    lines.append(f"| Unresolved 轨迹窗口 | {stats['unresolved_windows']:,} |")
238	    lines.append("")
239	
240	    lines.append("## 2. 每个 LF 的覆盖率")
241	    lines.append("")
242	    lines.append("| LF | 非 Abstain 数 | 覆盖率 |")
243	    lines.append("|-----|--------------|--------|")
244	    for lf_name, _ in ALL_LFS:
245	        counts = stats["lf_counts"][lf_name]
246	        non_abstain = sum(v for k, v in counts.items() if k != ABSTAIN)
247	        coverage = non_abstain / total * 100 if total > 0 else 0
248	        lines.append(f"| {lf_name} | {non_abstain:,} | {coverage:.1f}% |")
249	    lines.append("")
250	
251	    lines.append("## 3. 每个 LF 的标签分布")
252	    lines.append("")
253	    label_names = {1: "progress", 0: "stagnation", -1: "abstain"}
254	    for lf_name, _ in ALL_LFS:
255	        counts = stats["lf_counts"][lf_name]
256	        lines.append(f"### {lf_name}")
257	        lines.append("")
258	        lines.append("| 标签 | 数量 | 占比 |")
259	        lines.append("|------|------|------|")
260	        for label_val in [1, 0, -1]:
261	            c = counts.get(label_val, 0)
262	            pct = c / total * 100 if total > 0 else 0
263	            lines.append(f"| {label_names[label_val]} | {c:,} | {pct:.1f}% |")
264	        lines.append("")
265	
266	    lines.append("## 4. LF 一致性")
267	    lines.append("")
268	    agree_total = stats["agreement_total"]
269	    agree_agree = stats["agreement_agree"]
270	    agree_rate = agree_agree / agree_total * 100 if agree_total > 0 else 0
271	    lines.append(f"- ≥2 个 LF 都非 abstain 的窗口数：{agree_total:,}")
272	    lines.append(f"- 其中标签一致的窗口数：{agree_agree:,}")
273	    lines.append(f"- **一致率：{agree_rate:.1f}%**")
274	    lines.append("")
275	
276	    lines.append("## 5. 多数投票标签分布（高置信度，confidence ≥ 2）")
277	    lines.append("")
278	    high_conf = stats["high_conf_counts"]
279	    high_total = sum(high_conf.values())
280	    lines.append(f"高置信度窗口总数：{high_total:,}")
281	    lines.append("")
282	    lines.append("| 标签 | 数量 | 占比 |")
283	    lines.append("|------|------|------|")
284	    for label_val in [1, 0]:
285	        c = high_conf.get(label_val, 0)
286	        pct = c / high_total * 100 if high_total > 0 else 0
287	        lines.append(f"| {label_names[label_val]} | {c:,} | {pct:.1f}% |")
288	    lines.append("")
289	
290	    lines.append("## 6. 按 Resolved/Unresolved 分组的标签分布")
291	    lines.append("")
292	    lines.append("### Resolved 轨迹")
293	    lines.append("")
294	    lines.append("| Majority Label | 数量 | 占比 |")
295	    lines.append("|----------------|------|------|")
296	    res_total = sum(stats["resolved_label_counts"].values())
297	    for label_val in [1, 0, -1]:
298	        c = stats["resolved_label_counts"].get(label_val, 0)
299	        pct = c / res_total * 100 if res_total > 0 else 0
300	        lines.append(f"| {label_names[label_val]} | {c:,} | {pct:.1f}% |")
301	    lines.append("")
302	
303	    lines.append("### Unresolved 轨迹")
304	    lines.append("")
305	    lines.append("| Majority Label | 数量 | 占比 |")
306	    lines.append("|----------------|------|------|")
307	    unres_total = sum(stats["unresolved_label_counts"].values())
308	    for label_val in [1, 0, -1]:
309	        c = stats["unresolved_label_counts"].get(label_val, 0)
310	        pct = c / unres_total * 100 if unres_total > 0 else 0
311	        lines.append(f"| {label_names[label_val]} | {c:,} | {pct:.1f}% |")
312	    lines.append("")
313	
314	    lines.append("## 7. 类别平衡评估")
315	    lines.append("")
316	    prog_high = high_conf.get(1, 0)
317	    stag_high = high_conf.get(0, 0)
318	    if high_total > 0:
319	        ratio = max(prog_high, stag_high) / max(min(prog_high, stag_high), 1)
320	        lines.append(f"- Progress (高置信): {prog_high:,}")
321	        lines.append(f"- Stagnation (高置信): {stag_high:,}")
322	        lines.append(f"- 比例 (多/少): {ratio:.1f}:1")
323	        lines.append("")
324	        if ratio > 3:
325	            lines.append("**严重不平衡。** 建议：")
326	            lines.append("1. 对少数类进行过采样 (SMOTE 或重复采样)")
327	            lines.append("2. 使用 class weights 在训练时补偿")
328	            lines.append("3. 考虑调整 LF 阈值以增加少数类覆盖")
329	            lines.append("4. 使用 focal loss 代替 cross-entropy")
330	        elif ratio > 1.5:
331	            lines.append("**中度不平衡。** 建议使用 class weights 或在评估时关注 F1 而非 accuracy。")
332	        else:
333	            lines.append("**类别相对平衡。** 标准训练流程即可。")
334	    else:
335	        lines.append("无高置信度窗口，无法评估类别平衡。")
336	    lines.append("")
337	
338	    report_path.write_text("\n".join(lines))
339	    print(f"Report saved to {report_path}")
340	
341	
342	if __name__ == "__main__":
343	    DATA_PATH = (
344	        "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/"
345	        "agent_progress_probe/artifacts/data/swe_agent_trajectories_1000.jsonl"
346	    )
347	    OUTPUT_PATH = (
348	        "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/"
349	        "agent_progress_probe/artifacts/data/windows_labeled.jsonl"
350	    )
351	    REPORT_PATH = (
352	        "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/"
353	        "agent_progress_probe/artifacts/label_statistics_report.md"
354	    )
355	
356	    # First test with 10 trajectories
357	    print("=" * 60)
358	    print("VALIDATION: Testing with 10 trajectories")
359	    print("=" * 60)
360	
361	    test_stats = run_pipeline(DATA_PATH, OUTPUT_PATH + ".test", limit=10)
362	    print(f"\nTest results: {test_stats['total_windows']} windows from {test_stats['total_trajectories']} trajectories")
363	    print(f"LF coverage:")
364	    for lf_name, _ in ALL_LFS:
365	        counts = test_stats["lf_counts"][lf_name]
366	        non_abstain = sum(v for k, v in counts.items() if k != -1)
367	        print(f"  {lf_name}: {non_abstain}/{test_stats['total_windows']} non-abstain")
368	    print(f"Majority vote: {test_stats['majority_counts']}")
369	
370	    # Spot check: print a few windows with labels
371	    print("\n" + "=" * 60)
372	    print("SPOT CHECK: First 3 windows from first trajectory")
373	    print("=" * 60)
374	
375	    from data_loader import load_trajectories_streaming
376	    traj = next(load_trajectories_streaming(DATA_PATH, limit=1))
377	    windows = process_trajectory(traj)
378	    for w in windows[:3]:
379	        print(f"\nWindow {w['window_idx']}: steps {w['step_indices'][0]}-{w['step_indices'][-1]}")
380	        print(f"  Labels: {w['labels']}")
381	        print(f"  Majority: {w['majority_label']} (confidence={w['confidence']})")
382	        # Show commands in window
383	        for s in w["steps"]:
384	            if s.is_action and s.command:
385	                cmd_preview = s.command[:80].replace('\n', ' ')
386	                print(f"    Step {s.index} cmd: {cmd_preview}")
387	
388	    # Full run
389	    print("\n" + "=" * 60)
390	    print("FULL RUN: Processing all 1000 trajectories")
391	    print("=" * 60)
392	
393	    stats = run_pipeline(DATA_PATH, OUTPUT_PATH)
394	    generate_report(stats, REPORT_PATH)
395	
396	    print(f"\nDone. {stats['total_windows']:,} windows labeled.")
397	    print(f"Output: {OUTPUT_PATH}")
398	    print(f"Report: {REPORT_PATH}")
399	
400	    # Clean up test file
401	    Path(OUTPUT_PATH + ".test").unlink(missing_ok=True)
402	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "4a4ba299-a9ae-4f86-b5cc-ca16b8715b1a"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Reading artifacts/labeling_functions.py",
  "usage": {
    "total_tokens": 40094,
    "tool_uses": 10,
    "duration_ms": 16444
  },
  "last_tool_name": "Read",
  "uuid": "ccfe01e8-f40c-449b-8ed3-e9ed16e51e91",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01VBwfejcChSrK8NPaWG12mC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/labeling_functions.py",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "47da06a9-2fd1-4807-b895-a3439e3cf269",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QpZVKv4ythRsw2xUsm12QT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 5905,
      "cache_read_input_tokens": 34022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5905,
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

_source line 38 · 2026-05-14T22:40:28.631Z_

<details><summary>↩ Tool result · `toolu_01VBwfejcChSrK8NPaWG12mC`</summary>

```text
1	"""Labeling functions for agent progress probe.
2	
3	Each LF takes a sliding window of steps and returns:
4	  1 = progress, 0 = stagnation, -1 = abstain
5	"""
6	
7	from __future__ import annotations
8	
9	import re
10	from difflib import SequenceMatcher
11	from typing import TYPE_CHECKING
12	
13	if TYPE_CHECKING:
14	    from data_loader import Step, Trajectory
15	
16	PROGRESS = 1
17	STAGNATION = 0
18	ABSTAIN = -1
19	
20	EDIT_PATTERN = re.compile(r"^edit\s+\d+", re.MULTILINE)
21	SEARCH_CMDS = {"search_dir", "search_file", "find_file", "find", "grep"}
22	
23	
24	def _extract_edited_files(steps: list[Step]) -> tuple[int, set[str]]:
25	    """Count edit commands and unique files edited in a window."""
26	    edit_count = 0
27	    files = set()
28	    for step in steps:
29	        if not step.is_action:
30	            continue
31	        cmd = step.command
32	        if not cmd:
33	            continue
34	        if cmd.strip().startswith("edit"):
35	            edit_count += 1
36	            # Try to get the filename from the next observation
37	            idx = step.index
38	            for s in steps:
39	                if s.index == idx + 1 and s.is_observation:
40	                    match = re.search(r"\[File:\s*([^\]]+?)(?:\s*\(\d+\s*lines)", s.text)
41	                    if match:
42	                        files.add(match.group(1).strip())
43	                    break
44	    return edit_count, files
45	
46	
47	def _count_search_only(steps: list[Step]) -> int:
48	    """Count consecutive search/find commands without any edit."""
49	    count = 0
50	    for step in steps:
51	        if not step.is_action:
52	            continue
53	        cmd = step.command
54	        if not cmd:
55	            continue
56	        first_word = cmd.strip().split()[0] if cmd.strip() else ""
57	        if first_word in SEARCH_CMDS:
58	            count += 1
59	    return count
60	
61	
62	def lf_file_diff_delta(window: list[Step], trajectory: Trajectory, window_position: dict) -> int:
63	    """LF1: Whether the agent is meaningfully modifying code in this window."""
64	    edit_count, files = _extract_edited_files(window)
65	
66	    if edit_count >= 2 and len(files) >= 1:
67	        return PROGRESS
68	    if edit_count == 0:
69	        search_count = _count_search_only(window)
70	        if search_count >= 3:
71	            return STAGNATION
72	        return ABSTAIN
73	    return ABSTAIN
74	
75	
76	def _cmd_similarity(a: str, b: str) -> float:
77	    """Character-level similarity between two commands using SequenceMatcher."""
78	    if a == b:
79	        return 1.0
80	    if not a or not b:
81	        return 0.0
82	    return SequenceMatcher(None, a, b).ratio()
83	
84	
85	def _has_consecutive_similar(commands: list[str], min_run: int = 3, threshold: float = 0.9) -> bool:
86	    """Check if there are ≥min_run consecutive commands with similarity > threshold."""
87	    if len(commands) < min_run:
88	        return False
89	    run = 1
90	    for i in range(1, len(commands)):
91	        if _cmd_similarity(commands[i - 1], commands[i]) >= threshold:
92	            run += 1
93	            if run >= min_run:
94	                return True
95	        else:
96	            run = 1
97	    return False
98	
99	
100	def lf_command_repetition(window: list[Step], trajectory: Trajectory, window_position: dict) -> int:
101	    """LF2: Detect command repetition patterns as stagnation signal."""
102	    commands = [s.command for s in window if s.is_action and s.command is not None]
103	
104	    if len(commands) < 2:
105	        return ABSTAIN
106	
107	    if _has_consecutive_similar(commands, min_run=3, threshold=1.0):
108	        return STAGNATION
109	
110	    if _has_consecutive_similar(commands, min_run=3, threshold=0.9):
111	        return STAGNATION
112	
113	    if len(set(commands)) == len(commands):
114	        return PROGRESS
115	
116	    return ABSTAIN
117	
118	
119	# --- Deprecated ---
120	def _parse_test_pass_rate(text: str) -> float | None:
121	    passed = 0
122	    failed = 0
123	    passed_lines = re.findall(r"PASSED\s+\S+", text)
124	    failed_lines = re.findall(r"FAILED\s+\S+", text)
125	    passed += len(passed_lines)
126	    failed += len(failed_lines)
127	    summary_passed = re.search(r"(\d+)\s+passed", text)
128	    summary_failed = re.search(r"(\d+)\s+failed", text)
129	    if summary_passed and passed == 0:
130	        passed = int(summary_passed.group(1))
131	    if summary_failed and failed == 0:
132	        failed = int(summary_failed.group(1))
133	    total = passed + failed
134	    if total == 0:
135	        return None
136	    return passed / total
137	
138	
139	def lf_test_pass_rate_transition_deprecated(window: list[Step], trajectory: Trajectory, window_position: dict) -> int:
140	    """LF2 (deprecated): Whether test pass rate is improving within the window."""
141	    test_runs = []
142	    for step in window:
143	        if not step.is_observation:
144	            continue
145	        if not step.has_test_output:
146	            continue
147	        rate = _parse_test_pass_rate(step.text)
148	        if rate is not None:
149	            test_runs.append(rate)
150	    if len(test_runs) < 2:
151	        return ABSTAIN
152	    last = test_runs[-1]
153	    second_last = test_runs[-2]
154	    if last > second_last:
155	        return PROGRESS
156	    return STAGNATION
157	
158	
159	def lf_outcome_backpropagation(window: list[Step], trajectory: Trajectory, window_position: dict) -> int:
160	    """LF3: Label last windows based on final trajectory outcome."""
161	    total_windows = window_position["total_windows"]
162	    window_idx = window_position["window_idx"]
163	
164	    is_last_two = window_idx >= total_windows - 2
165	
166	    if trajectory.exit_status in ("exit_context",):
167	        return STAGNATION
168	
169	    if not is_last_two:
170	        return ABSTAIN
171	
172	    if trajectory.target:
173	        return PROGRESS
174	    else:
175	        return STAGNATION
176	
177	
178	ALL_LFS = [
179	    ("file_diff_delta", lf_file_diff_delta),
180	    ("command_repetition", lf_command_repetition),
181	    ("outcome_backpropagation", lf_outcome_backpropagation),
182	]
183	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "35424270-a82d-44ed-803a-455b18f19d40"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Reading artifacts/data_loader.py",
  "usage": {
    "total_tokens": 42340,
    "tool_uses": 11,
    "duration_ms": 18130
  },
  "last_tool_name": "Read",
  "uuid": "f7fc53d5-2f31-4f2b-b1fa-b2dee1631fb6",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01WcxSWY3VUPhWqLQjr542Bz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/data_loader.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "fde39e2d-c153-4138-a1f5-e5de8b1fa32e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VB2XH1d2mgBzgkxWd75KvC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 2238,
      "cache_read_input_tokens": 39927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2238,
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

_source line 41 · 2026-05-14T22:40:30.320Z_

<details><summary>↩ Tool result · `toolu_01WcxSWY3VUPhWqLQjr542Bz`</summary>

````text
1	# SWE-agent trajectories data loader for agent_progress_probe project.
2	# Loads and parses nebius/SWE-agent-trajectories JSONL data into structured objects.
3	
4	from __future__ import annotations
5	
6	import json
7	import re
8	from dataclasses import dataclass, field
9	from pathlib import Path
10	from typing import Optional
11	
12	
13	@dataclass
14	class Step:
15	    """A single step in an agent trajectory."""
16	    index: int
17	    role: str  # "system", "user", or "ai"
18	    text: str
19	    mask: bool
20	    cutoff_date: Optional[str] = None
21	    system_prompt: Optional[str] = None
22	
23	    @property
24	    def is_action(self) -> bool:
25	        return self.role == "ai"
26	
27	    @property
28	    def is_observation(self) -> bool:
29	        return self.role == "user" and self.index > 0
30	
31	    @property
32	    def is_system(self) -> bool:
33	        return self.role == "system"
34	
35	    @property
36	    def command(self) -> Optional[str]:
37	        """Extract the command from an AI step's code block. Returns None for non-AI steps."""
38	        if self.role != "ai":
39	            return None
40	        match = re.search(r"```\n?(.*?)```", self.text, re.DOTALL)
41	        if match:
42	            return match.group(1).strip()
43	        return None
44	
45	    @property
46	    def has_file_display(self) -> bool:
47	        return "[File:" in self.text
48	
49	    @property
50	    def has_error(self) -> bool:
51	        return "Traceback" in self.text or "Error" in self.text
52	
53	    @property
54	    def has_test_output(self) -> bool:
55	        text = self.text
56	        return ("PASSED" in text or "FAILED" in text) and "test" in text.lower()
57	
58	
59	@dataclass
60	class TestResult:
61	    """Parsed test results from eval_logs."""
62	    passed: list[str] = field(default_factory=list)
63	    failed: list[str] = field(default_factory=list)
64	    errored: list[str] = field(default_factory=list)
65	
66	    @property
67	    def total(self) -> int:
68	        return len(self.passed) + len(self.failed) + len(self.errored)
69	
70	    @property
71	    def pass_rate(self) -> float:
72	        if self.total == 0:
73	            return 0.0
74	        return len(self.passed) / self.total
75	
76	
77	@dataclass
78	class Trajectory:
79	    """A complete agent trajectory for one SWE-bench instance attempt."""
80	    instance_id: str
81	    model_name: str
82	    target: bool  # True = resolved, False = unresolved
83	    steps: list[Step]
84	    exit_status: str
85	    generated_patch: Optional[str]
86	    eval_logs: Optional[str]
87	    row_index: int = 0  # source file line number, ensures unique trajectory_id
88	
89	    @property
90	    def num_steps(self) -> int:
91	        return len(self.steps)
92	
93	    @property
94	    def actions(self) -> list[Step]:
95	        return [s for s in self.steps if s.is_action]
96	
97	    @property
98	    def observations(self) -> list[Step]:
99	        return [s for s in self.steps if s.is_observation]
100	
101	    @property
102	    def issue_text(self) -> Optional[str]:
103	        """The issue description from step 1 (first user message)."""
104	        if len(self.steps) > 1 and self.steps[1].role == "user":
105	            return self.steps[1].text
106	        return None
107	
108	    @property
109	    def has_patch(self) -> bool:
110	        return bool(self.generated_patch and self.generated_patch.strip())
111	
112	    def parse_eval_test_results(self) -> Optional[TestResult]:
113	        """Parse test results from eval_logs.
114	
115	        Returns:
116	            TestResult with lists of passed/failed/errored test names,
117	            or None if eval_logs is empty or has no test section.
118	        """
119	        if not self.eval_logs:
120	            return None
121	        start_marker = "___TESTS_SECTION___"
122	        end_marker = "___TESTS_SECTION_END"
123	        if start_marker not in self.eval_logs:
124	            return None
125	        start = self.eval_logs.index(start_marker)
126	        end = self.eval_logs.index(end_marker) if end_marker in self.eval_logs else len(self.eval_logs)
127	        section = self.eval_logs[start:end]
128	
129	        result = TestResult()
130	        for line in section.splitlines():
131	            line = line.strip()
132	            if line.startswith("PASSED "):
133	                result.passed.append(line[7:])
134	            elif line.startswith("FAILED "):
135	                name = line[7:].split(" - ")[0]
136	                result.failed.append(name)
137	            elif line.startswith("ERROR "):
138	                result.errored.append(line[6:])
139	        return result
140	
141	    def extract_mid_trajectory_test_results(self) -> list[tuple[int, TestResult]]:
142	        """Find pytest runs within the trajectory observations.
143	
144	        Returns:
145	            List of (step_index, TestResult) for steps containing pytest output.
146	        """
147	        results = []
148	        for step in self.observations:
149	            if not step.has_test_output:
150	                continue
151	            tr = TestResult()
152	            for line in step.text.splitlines():
153	                line = line.strip()
154	                if line.startswith("PASSED "):
155	                    tr.passed.append(line[7:])
156	                elif line.startswith("FAILED "):
157	                    name = line[7:].split(" - ")[0]
158	                    tr.failed.append(name)
159	                elif line.startswith("ERROR "):
160	                    tr.errored.append(line[6:])
161	            summary = re.search(r"(\d+) passed", step.text)
162	            if summary and not tr.passed:
163	                tr.passed = [f"unnamed_{i}" for i in range(int(summary.group(1)))]
164	            summary = re.search(r"(\d+) failed", step.text)
165	            if summary and not tr.failed:
166	                tr.failed = [f"unnamed_{i}" for i in range(int(summary.group(1)))]
167	            if tr.total > 0:
168	                results.append((step.index, tr))
169	        return results
170	
171	    def get_edit_commands(self) -> list[tuple[int, str]]:
172	        """Extract all edit commands from the trajectory.
173	
174	        Returns:
175	            List of (step_index, command_text) for steps containing edit commands.
176	        """
177	        edits = []
178	        for step in self.actions:
179	            cmd = step.command
180	            if cmd and cmd.strip().startswith("edit"):
181	                edits.append((step.index, cmd))
182	        return edits
183	
184	
185	def parse_trajectory(raw: dict, row_index: int = 0) -> Trajectory:
186	    """Parse a single raw record dict into a Trajectory object.
187	
188	    Args:
189	        raw: A dict with keys: instance_id, model_name, target, trajectory,
190	             exit_status, generated_patch, eval_logs.
191	        row_index: Source file line number for unique identification.
192	
193	    Returns:
194	        A Trajectory object with parsed Steps.
195	    """
196	    steps = []
197	    for i, step_raw in enumerate(raw.get("trajectory") or []):
198	        steps.append(Step(
199	            index=i,
200	            role=step_raw.get("role", "unknown"),
201	            text=step_raw.get("text") or "",
202	            mask=step_raw.get("mask", False),
203	            cutoff_date=step_raw.get("cutoff_date"),
204	            system_prompt=step_raw.get("system_prompt"),
205	        ))
206	
207	    return Trajectory(
208	        instance_id=raw.get("instance_id", ""),
209	        model_name=raw.get("model_name", ""),
210	        target=raw.get("target", False),
211	        steps=steps,
212	        exit_status=raw.get("exit_status", ""),
213	        generated_patch=raw.get("generated_patch"),
214	        eval_logs=raw.get("eval_logs"),
215	        row_index=row_index,
216	    )
217	
218	
219	def extract_steps(trajectory: Trajectory) -> list[Step]:
220	    """Extract the step sequence from a trajectory, excluding the system step.
221	
222	    Args:
223	        trajectory: A parsed Trajectory object.
224	
225	    Returns:
226	        List of Steps starting from step 1 (the issue description),
227	        excluding the system prompt step.
228	    """
229	    return [s for s in trajectory.steps if not s.is_system]
230	
231	
232	def load_trajectories(path: str | Path) -> list[Trajectory]:
233	    """Load trajectories from a JSONL file.
234	
235	    Args:
236	        path: Path to a .jsonl file where each line is a JSON record.
237	
238	    Returns:
239	        List of Trajectory objects.
240	    """
241	    path = Path(path)
242	    trajectories = []
243	    with open(path) as f:
244	        for i, line in enumerate(f):
245	            line = line.strip()
246	            if not line:
247	                continue
248	            raw = json.loads(line)
249	            trajectories.append(parse_trajectory(raw, row_index=i))
250	    return trajectories
251	
252	
253	def load_trajectories_streaming(path: str | Path, limit: int | None = None):
254	    """Lazily yield trajectories from a JSONL file.
255	
256	    Args:
257	        path: Path to a .jsonl file.
258	        limit: Maximum number of trajectories to yield. None for all.
259	
260	    Yields:
261	        Trajectory objects one at a time.
262	    """
263	    path = Path(path)
264	    count = 0
265	    with open(path) as f:
266	        for i, line in enumerate(f):
267	            line = line.strip()
268	            if not line:
269	                continue
270	            raw = json.loads(line)
271	            yield parse_trajectory(raw, row_index=i)
272	            count += 1
273	            if limit and count >= limit:
274	                break
275	
276	
277	if __name__ == "__main__":
278	    import sys
279	    data_path = sys.argv[1] if len(sys.argv) > 1 else (
280	        "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/"
281	        "agent_progress_probe/artifacts/data/swe_agent_trajectories_1000.jsonl"
282	    )
283	
284	    print(f"Loading from {data_path}...")
285	    trajs = load_trajectories(data_path)
286	    print(f"Loaded {len(trajs)} trajectories")
287	
288	    resolved = [t for t in trajs if t.target]
289	    unresolved = [t for t in trajs if not t.target]
290	    print(f"Resolved: {len(resolved)}, Unresolved: {len(unresolved)}")
291	
292	    t = trajs[0]
293	    print(f"\nSample trajectory: {t.instance_id}")
294	    print(f"  Steps: {t.num_steps}, Actions: {len(t.actions)}, Observations: {len(t.observations)}")
295	    print(f"  Has patch: {t.has_patch}, Target: {t.target}")
296	
297	    test_result = t.parse_eval_test_results()
298	    if test_result:
299	        print(f"  Eval tests: {len(test_result.passed)} passed, {len(test_result.failed)} failed, pass_rate={test_result.pass_rate:.2f}")
300	
301	    edits = t.get_edit_commands()
302	    print(f"  Edit commands: {len(edits)}")
303	
304	    mid_tests = t.extract_mid_trajectory_test_results()
305	    print(f"  Mid-trajectory test runs: {len(mid_tests)}")
306	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "5b1f694c-5188-4d89-b8f5-dd5248fb8eb7"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Reading artifacts/baselines.py",
  "usage": {
    "total_tokens": 46122,
    "tool_uses": 12,
    "duration_ms": 19812
  },
  "last_tool_name": "Read",
  "uuid": "a6f6f0f3-0efc-4fb9-bcf2-479e739d3038",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01MPMnFGRUzNJjz4GnxQJ7KA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/baselines.py",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "878175c6-299a-4df6-9a3a-257e34fbb84d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LxepRhZxTNRpwSropbstd9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3781,
      "cache_read_input_tokens": 42165,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3781,
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

_source line 44 · 2026-05-14T22:40:32.000Z_

<details><summary>↩ Tool result · `toolu_01MPMnFGRUzNJjz4GnxQJ7KA`</summary>

````text
1	#!/usr/bin/env python3
2	"""Baseline methods for progress/stagnation classification.
3	
4	Each baseline implements a unified interface:
5	    fit(train_data, val_data=None)
6	    predict(data) -> list[int]
7	    evaluate(data) -> dict
8	
9	Data format: list of dicts, each containing:
10	    - "label": int (0=stagnation, 1=progress)
11	    - "embeddings": torch.Tensor (seq_len, embed_dim) — for cosine baseline
12	    - "steps": list[{"role": str, "text": str}] — for repeat-3 baseline
13	"""
14	
15	import re
16	import random
17	
18	import numpy as np
19	import torch
20	from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
21	
22	
23	def extract_command(text: str) -> str | None:
24	    match = re.search(r"```\n?(.*?)```", text, re.DOTALL)
25	    return match.group(1).strip() if match else None
26	
27	
28	def compute_metrics(labels: list[int], preds: list[int]) -> dict:
29	    return {
30	        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
31	        "accuracy": accuracy_score(labels, preds),
32	        "precision_macro": precision_score(labels, preds, average="macro", zero_division=0),
33	        "recall_macro": recall_score(labels, preds, average="macro", zero_division=0),
34	        "f1_stagnation": f1_score(labels, preds, pos_label=0, zero_division=0),
35	        "f1_progress": f1_score(labels, preds, pos_label=1, zero_division=0),
36	    }
37	
38	
39	class BaselineModel:
40	    name: str = "baseline"
41	
42	    def fit(self, train_data: list[dict], val_data: list[dict] | None = None):
43	        pass
44	
45	    def predict(self, data: list[dict]) -> list[int]:
46	        raise NotImplementedError
47	
48	    def evaluate(self, data: list[dict]) -> dict:
49	        labels = [d["label"] for d in data]
50	        preds = self.predict(data)
51	        return compute_metrics(labels, preds)
52	
53	
54	class RandomBaseline(BaselineModel):
55	    name = "Random"
56	
57	    def __init__(self, seed: int = 42):
58	        self.seed = seed
59	        self.pos_ratio = 0.5
60	
61	    def fit(self, train_data, val_data=None):
62	        labels = [d["label"] for d in train_data]
63	        self.pos_ratio = sum(labels) / len(labels) if labels else 0.5
64	
65	    def predict(self, data):
66	        rng = random.Random(self.seed)
67	        return [1 if rng.random() < self.pos_ratio else 0 for _ in data]
68	
69	
70	class MajorityBaseline(BaselineModel):
71	    name = "Majority"
72	
73	    def __init__(self):
74	        self.majority_class = 0
75	
76	    def fit(self, train_data, val_data=None):
77	        labels = [d["label"] for d in train_data]
78	        self.majority_class = 1 if sum(labels) > len(labels) / 2 else 0
79	
80	    def predict(self, data):
81	        return [self.majority_class] * len(data)
82	
83	
84	class CosineSimilarityBaseline(BaselineModel):
85	    name = "CosineSim"
86	
87	    def __init__(self):
88	        self.threshold = 0.5
89	        self.invert = False
90	
91	    @staticmethod
92	    def _avg_adjacent_cosine(embeddings: torch.Tensor) -> float:
93	        if embeddings.shape[0] < 2:
94	            return 0.0
95	        e = torch.nn.functional.normalize(embeddings, p=2, dim=1)
96	        sims = (e[:-1] * e[1:]).sum(dim=1)
97	        return sims.mean().item()
98	
99	    def fit(self, train_data, val_data=None):
100	        tune_data = val_data if val_data else train_data
101	        labels = [d["label"] for d in tune_data]
102	        scores = [self._avg_adjacent_cosine(d["embeddings"]) for d in tune_data]
103	
104	        best_f1, best_t, best_inv = -1.0, 0.5, False
105	        for t in np.arange(-1.0, 1.01, 0.01):
106	            for inv in (False, True):
107	                preds = [int((s >= t) != inv) for s in scores]
108	                f = f1_score(labels, preds, average="macro", zero_division=0)
109	                if f > best_f1:
110	                    best_f1, best_t, best_inv = f, t, inv
111	        self.threshold = best_t
112	        self.invert = best_inv
113	
114	    def predict(self, data):
115	        return [int((self._avg_adjacent_cosine(d["embeddings"]) >= self.threshold) != self.invert) for d in data]
116	
117	
118	class Repeat3Baseline(BaselineModel):
119	    name = "Repeat-3"
120	
121	    @staticmethod
122	    def _predict_one(steps: list[dict]) -> int:
123	        ai_commands = []
124	        for s in steps:
125	            if s.get("role") == "ai":
126	                cmd = extract_command(s.get("text", ""))
127	                if cmd is not None:
128	                    ai_commands.append(cmd)
129	        if len(ai_commands) >= 3 and ai_commands[-1] == ai_commands[-2] == ai_commands[-3]:
130	            return 0  # stagnation
131	        return 1  # progress
132	
133	    def predict(self, data):
134	        return [self._predict_one(d.get("steps", [])) for d in data]
135	
136	
137	ALL_BASELINES = [RandomBaseline, MajorityBaseline, CosineSimilarityBaseline, Repeat3Baseline]
138	
139	
140	if __name__ == "__main__":
141	    print("=== Baseline self-test with random data ===")
142	    embed_dim = 1024
143	    n_samples = 100
144	
145	    data = []
146	    for i in range(n_samples):
147	        seq_len = random.randint(3, 10)
148	        label = random.choice([0, 1])
149	        steps = []
150	        for j in range(seq_len):
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "32d2b797-6b05-4b28-af41-c2b9912a2516"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Reading artifacts/train_probe.py",
  "usage": {
    "total_tokens": 48181,
    "tool_uses": 13,
    "duration_ms": 21794
  },
  "last_tool_name": "Read",
  "uuid": "7acf0d08-c218-4b94-ba95-04a272db9c6e",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_016bB8hLpyj9QD35hJE9H3jM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/train_probe.py",
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "c23a6024-63cd-4fac-95ba-1011e3ee4a2c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VTvg54BntbpbYz9hucSmD3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2053,
      "cache_read_input_tokens": 45946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2053,
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

_source line 47 · 2026-05-14T22:40:33.986Z_

<details><summary>↩ Tool result · `toolu_016bB8hLpyj9QD35hJE9H3jM`</summary>

```text
1	#!/usr/bin/env python3
2	"""Train the GRU progress probe on pre-computed window embeddings."""
3	
4	import argparse
5	import json
6	import random
7	import sys
8	from pathlib import Path
9	
10	import numpy as np
11	import torch
12	import torch.nn as nn
13	from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
14	from torch.utils.data import DataLoader
15	
16	sys.path.insert(0, str(Path(__file__).parent))
17	from probe_model import ProgressProbe, WindowDataset, collate_fn, split_by_instance
18	
19	
20	def set_seed(seed: int):
21	    random.seed(seed)
22	    np.random.seed(seed)
23	    torch.manual_seed(seed)
24	    if torch.cuda.is_available():
25	        torch.cuda.manual_seed_all(seed)
26	
27	
28	def compute_metrics(labels: list[int], preds: list[int]) -> dict:
29	    return {
30	        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
31	        "accuracy": accuracy_score(labels, preds),
32	        "precision_macro": precision_score(labels, preds, average="macro", zero_division=0),
33	        "recall_macro": recall_score(labels, preds, average="macro", zero_division=0),
34	        "f1_stagnation": f1_score(labels, preds, pos_label=0, zero_division=0),
35	        "f1_progress": f1_score(labels, preds, pos_label=1, zero_division=0),
36	    }
37	
38	
39	class EarlyStopping:
40	    def __init__(self, patience: int = 5):
41	        self.patience = patience
42	        self.counter = 0
43	        self.best_score = None
44	        self.should_stop = False
45	
46	    def step(self, score: float) -> bool:
47	        if self.best_score is None or score > self.best_score:
48	            self.best_score = score
49	            self.counter = 0
50	            return True
51	        self.counter += 1
52	        if self.counter >= self.patience:
53	            self.should_stop = True
54	        return False
55	
56	
57	@torch.no_grad()
58	def evaluate_epoch(model: nn.Module, loader: DataLoader, device: str) -> dict:
59	    model.eval()
60	    all_labels, all_preds = [], []
61	    for padded, labels, lengths in loader:
62	        logits = model(padded.to(device), lengths)
63	        preds = (torch.sigmoid(logits) >= 0.5).long().cpu()
64	        all_labels.extend(labels.long().tolist())
65	        all_preds.extend(preds.tolist())
66	    return compute_metrics(all_labels, all_preds)
67	
68	
69	def main():
70	    parser = argparse.ArgumentParser(description="Train GRU progress probe")
71	    parser.add_argument("--data_dir", required=True, help="Directory containing embeddings.pt")
72	    parser.add_argument("--output_dir", required=True, help="Output directory for checkpoints")
73	    parser.add_argument("--lr", type=float, default=1e-3)
74	    parser.add_argument("--batch_size", type=int, default=32)
75	    parser.add_argument("--epochs", type=int, default=20)
76	    parser.add_argument("--hidden_size", type=int, default=256)
77	    parser.add_argument("--num_layers", type=int, default=2)
78	    parser.add_argument("--dropout", type=float, default=0.1)
79	    parser.add_argument("--weight_decay", type=float, default=0.01)
80	    parser.add_argument("--patience", type=int, default=5)
81	    parser.add_argument("--seed", type=int, default=42)
82	    parser.add_argument("--min_confidence", type=int, default=0, help="Min confidence for training (0=all, 2=high-conf)")
83	    parser.add_argument("--wandb", action="store_true", help="Enable W&B logging")
84	    args = parser.parse_args()
85	
86	    set_seed(args.seed)
87	    output_dir = Path(args.output_dir)
88	    output_dir.mkdir(parents=True, exist_ok=True)
89	    device = "cuda" if torch.cuda.is_available() else "cpu"
90	
91	    # Load data
92	    data_path = Path(args.data_dir) / "embeddings.pt"
93	    data = torch.load(data_path, weights_only=False)
94	    embeddings = data["embeddings"]
95	    labels = data["labels"]
96	    instance_ids = data["instance_ids"]
97	    confidences = data.get("confidences", [1] * len(labels))
98	    embed_dim = data["embed_dim"]
99	
100	    # Filter by confidence
101	    if args.min_confidence > 0:
102	        keep = [i for i, c in enumerate(confidences) if c >= args.min_confidence]
103	        print(f"Confidence filter: {len(keep)}/{len(labels)} windows with conf>={args.min_confidence}")
104	        embeddings = [embeddings[i] for i in keep]
105	        labels = [labels[i] for i in keep]
106	        instance_ids = [instance_ids[i] for i in keep]
107	        confidences = [confidences[i] for i in keep]
108	
109	    # Split
110	    train_idx, val_idx, test_idx = split_by_instance(instance_ids, seed=args.seed)
111	    split_info = {
112	        "train_indices": train_idx,
113	        "val_indices": val_idx,
114	        "test_indices": test_idx,
115	        "seed": args.seed,
116	        "embed_dim": embed_dim,
117	        "min_confidence": args.min_confidence,
118	        "keep_indices": keep if args.min_confidence > 0 else None,
119	    }
120	    with open(output_dir / "split_info.json", "w") as f:
121	        json.dump(split_info, f)
122	
123	    def make_dataset(indices):
124	        return WindowDataset([embeddings[i] for i in indices], [labels[i] for i in indices])
125	
126	    train_ds = make_dataset(train_idx)
127	    val_ds = make_dataset(val_idx)
128	
129	    train_labels = [labels[i] for i in train_idx]
130	    num_pos = sum(train_labels)
131	    num_neg = len(train_labels) - num_pos
132	    pos_weight = torch.tensor([num_neg / max(num_pos, 1)]).to(device)
133	
134	    print(f"Train: {len(train_ds)} (pos={num_pos}, neg={num_neg})")
135	    print(f"Val:   {len(val_ds)}")
136	    print(f"Test:  {len(test_idx)}")
137	    print(f"pos_weight: {pos_weight.item():.3f}")
138	
139	    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True, collate_fn=collate_fn)
140	    val_loader = DataLoader(val_ds, batch_size=args.batch_size, collate_fn=collate_fn)
141	
142	    # Model
143	    model = ProgressProbe(
144	        embed_dim=embed_dim,
145	        hidden_size=args.hidden_size,
146	        num_layers=args.num_layers,
147	        dropout=args.dropout,
148	    ).to(device)
149	
150	    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
151	    criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
152	    early_stopping = EarlyStopping(patience=args.patience)
153	
154	    # W&B
155	    if args.wandb:
156	        import wandb
157	
158	        wandb.init(project="agent-progress-probe", config=vars(args))
159	
160	    # Training loop
161	    history = []
162	    for epoch in range(1, args.epochs + 1):
163	        model.train()
164	        total_loss = 0.0
165	        n_samples = 0
166	        for padded, batch_labels, lengths in train_loader:
167	            padded = padded.to(device)
168	            batch_labels = batch_labels.to(device)
169	
170	            logits = model(padded, lengths)
171	            loss = criterion(logits, batch_labels)
172	
173	            optimizer.zero_grad()
174	            loss.backward()
175	            optimizer.step()
176	
177	            total_loss += loss.item() * len(batch_labels)
178	            n_samples += len(batch_labels)
179	
180	        avg_loss = total_loss / n_samples
181	        val_metrics = evaluate_epoch(model, val_loader, device)
182	
183	        record = {"epoch": epoch, "train_loss": avg_loss, **{f"val_{k}": v for k, v in val_metrics.items()}}
184	        history.append(record)
185	
186	        is_best = early_stopping.step(val_metrics["macro_f1"])
187	        marker = " *" if is_best else ""
188	        print(
189	            f"Epoch {epoch:2d} | loss={avg_loss:.4f} | "
190	            f"val_F1={val_metrics['macro_f1']:.4f} "
191	            f"acc={val_metrics['accuracy']:.4f}{marker}"
192	        )
193	
194	        if is_best:
195	            torch.save(
196	                {
197	                    "model_state_dict": model.state_dict(),
198	                    "embed_dim": embed_dim,
199	                    "hidden_size": args.hidden_size,
200	                    "num_layers": args.num_layers,
201	                    "dropout": args.dropout,
202	                    "epoch": epoch,
203	                    "val_macro_f1": val_metrics["macro_f1"],
204	                    "args": vars(args),
205	                },
206	                output_dir / "best_model.pt",
207	            )
208	
209	        if args.wandb:
210	            import wandb
211	
212	            wandb.log(record)
213	
214	        if early_stopping.should_stop:
215	            print(f"Early stopping at epoch {epoch}")
216	            break
217	
218	    # Save history
219	    with open(output_dir / "train_history.json", "w") as f:
220	        json.dump(history, f, indent=2)
221	
222	    print(f"\nBest val macro-F1: {early_stopping.best_score:.4f}")
223	    print(f"Outputs saved to {output_dir}")
224	
225	
226	if __name__ == "__main__":
227	    main()
228	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "a7ba3dca-b42c-4c49-9acf-183a484a266a"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Reading artifacts/evaluate.py",
  "usage": {
    "total_tokens": 51391,
    "tool_uses": 14,
    "duration_ms": 23568
  },
  "last_tool_name": "Read",
  "uuid": "d5a09f7d-a310-413b-848d-d7465be6cf15",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_01Ra5FoUW6toRM3agsBkiuGy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/evaluate.py",
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "c3d19ec8-4d1c-4326-9a4b-7c9ae19440d3",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01G2WQGd9ZuASabNF1c1FHzT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3208,
      "cache_read_input_tokens": 47999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3208,
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

_source line 50 · 2026-05-14T22:40:35.757Z_

<details><summary>↩ Tool result · `toolu_01Ra5FoUW6toRM3agsBkiuGy`</summary>

```text
1	#!/usr/bin/env python3
2	"""Evaluate the GRU probe and all baselines on the test set, output comparison table."""
3	
4	import argparse
5	import json
6	import sys
7	from pathlib import Path
8	
9	import torch
10	from torch.utils.data import DataLoader
11	
12	sys.path.insert(0, str(Path(__file__).parent))
13	from baselines import (
14	    ALL_BASELINES,
15	    CosineSimilarityBaseline,
16	    RandomBaseline,
17	    Repeat3Baseline,
18	    compute_metrics,
19	)
20	from probe_model import ProgressProbe, WindowDataset, collate_fn
21	
22	
23	def parse_row_index(trajectory_id: str) -> int:
24	    """Extract row_index from trajectory_id 'instance_id__model_name__r{idx}'."""
25	    return int(trajectory_id.rsplit("__r", 1)[1])
26	
27	
28	def build_trajectory_index(traj_path: str) -> dict:
29	    """Map row_index (int) -> list of step dicts."""
30	    index = {}
31	    with open(traj_path) as f:
32	        for row_idx, line in enumerate(f):
33	            line = line.strip()
34	            if not line:
35	                continue
36	            raw = json.loads(line)
37	            steps = []
38	            for s in raw.get("trajectory") or []:
39	                steps.append({
40	                    "role": s.get("role", "unknown"),
41	                    "text": s.get("text") or s.get("system_prompt") or "",
42	                })
43	            index[row_idx] = steps
44	    return index
45	
46	
47	def load_windows(path: str) -> dict:
48	    """Load windows and index by trajectory_id__w{window_idx}."""
49	    index = {}
50	    with open(path) as f:
51	        for line in f:
52	            line = line.strip()
53	            if line:
54	                w = json.loads(line)
55	                wid = f"{w['trajectory_id']}__w{w['window_idx']}"
56	                index[wid] = w
57	    return index
58	
59	
60	def build_baseline_data(
61	    data: dict, indices: list[int], traj_index: dict
62	) -> list[dict]:
63	    """Construct baseline-compatible data dicts for given indices."""
64	    result = []
65	    for i in indices:
66	        tid = data["trajectory_ids"][i]
67	        row_idx = parse_row_index(tid)
68	        traj_steps = traj_index.get(row_idx, [])
69	
70	        steps = []
71	        for si in data["step_indices_list"][i]:
72	            if si < len(traj_steps):
73	                steps.append(traj_steps[si])
74	            else:
75	                steps.append({"role": "unknown", "text": ""})
76	
77	        result.append({
78	            "label": data["labels"][i],
79	            "embeddings": data["embeddings"][i],
80	            "steps": steps,
81	        })
82	    return result
83	
84	
85	@torch.no_grad()
86	def evaluate_probe(model: ProgressProbe, loader: DataLoader, device: str) -> tuple[dict, list[int]]:
87	    model.eval()
88	    all_labels, all_preds = [], []
89	    for padded, labels, lengths in loader:
90	        logits = model(padded.to(device), lengths)
91	        preds = (torch.sigmoid(logits) >= 0.5).long().cpu()
92	        all_labels.extend(labels.long().tolist())
93	        all_preds.extend(preds.tolist())
94	    return compute_metrics(all_labels, all_preds), all_preds
95	
96	
97	def print_table(results: list[tuple[str, dict]]):
98	    header = "| Method | Macro-F1 | Accuracy | Precision | Recall | F1(stag) | F1(prog) |"
99	    sep = "|" + "|".join(["---"] * 7) + "|"
100	    print(header)
101	    print(sep)
102	    for name, m in results:
103	        print(
104	            f"| {name:20s} | {m['macro_f1']:.4f}   | {m['accuracy']:.4f}   | "
105	            f"{m['precision_macro']:.4f}    | {m['recall_macro']:.4f} | "
106	            f"{m['f1_stagnation']:.4f}   | {m['f1_progress']:.4f}   |"
107	        )
108	
109	
110	def main():
111	    parser = argparse.ArgumentParser(description="Evaluate probe + baselines on test set")
112	    parser.add_argument("--data_dir", required=True, help="Directory containing embeddings.pt")
113	    parser.add_argument("--checkpoint", required=True, help="Path to best_model.pt")
114	    parser.add_argument("--split_info", required=True, help="Path to split_info.json")
115	    parser.add_argument("--trajectories", required=True, help="Path to original trajectories JSONL")
116	    parser.add_argument("--batch_size", type=int, default=64)
117	    parser.add_argument("--device", default=None)
118	    args = parser.parse_args()
119	
120	    device = args.device or ("cuda" if torch.cuda.is_available() else "cpu")
121	
122	    # Load embeddings data
123	    data = torch.load(Path(args.data_dir) / "embeddings.pt", weights_only=False)
124	
125	    # Apply same confidence filter used during training
126	    with open(args.split_info) as f:
127	        split_info = json.load(f)
128	
129	    keep_indices = split_info.get("keep_indices")
130	    if keep_indices is not None:
131	        min_conf = split_info.get("min_confidence", 0)
132	        print(f"Applying confidence filter (min_confidence={min_conf}): {len(keep_indices)}/{len(data['labels'])} windows")
133	        data = {
134	            "embeddings": [data["embeddings"][i] for i in keep_indices],
135	            "labels": [data["labels"][i] for i in keep_indices],
136	            "trajectory_ids": [data["trajectory_ids"][i] for i in keep_indices],
137	            "instance_ids": [data["instance_ids"][i] for i in keep_indices],
138	            "step_indices_list": [data["step_indices_list"][i] for i in keep_indices],
139	            "confidences": [data["confidences"][i] for i in keep_indices],
140	        }
141	
142	    train_idx = split_info["train_indices"]
143	    val_idx = split_info["val_indices"]
144	    test_idx = split_info["test_indices"]
145	
146	    print(f"Test set: {len(test_idx)} windows")
147	
148	    # ── Probe evaluation ──
149	    ckpt = torch.load(args.checkpoint, weights_only=False)
150	    model = ProgressProbe(
151	        embed_dim=ckpt["embed_dim"],
152	        hidden_size=ckpt["hidden_size"],
153	        num_layers=ckpt["num_layers"],
154	    ).to(device)
155	    model.load_state_dict(ckpt["model_state_dict"])
156	
157	    test_ds = WindowDataset(
158	        [data["embeddings"][i] for i in test_idx],
159	        [data["labels"][i] for i in test_idx],
160	    )
161	    test_loader = DataLoader(test_ds, batch_size=args.batch_size, collate_fn=collate_fn)
162	    probe_metrics, _ = evaluate_probe(model, test_loader, device)
163	
164	    # ── Baseline evaluation ──
165	    print("Loading trajectory data for baselines ...")
166	    traj_index = build_trajectory_index(args.trajectories)
167	
168	    train_bl = build_baseline_data(data, train_idx, traj_index)
169	    val_bl = build_baseline_data(data, val_idx, traj_index)
170	    test_bl = build_baseline_data(data, test_idx, traj_index)
171	
172	    results = [("GRU Probe", probe_metrics)]
173	
174	    for cls in ALL_BASELINES:
175	        bl = cls()
176	        bl.fit(train_bl, val_bl)
177	        metrics = bl.evaluate(test_bl)
178	        results.append((bl.name, metrics))
179	
180	    # ── Output ──
181	    print()
182	    print_table(results)
183	
184	    # Best baseline comparison
185	    baseline_results = results[1:]
186	    best_bl_name, best_bl_m = max(baseline_results, key=lambda x: x[1]["macro_f1"])
187	    delta = probe_metrics["macro_f1"] - best_bl_m["macro_f1"]
188	    pct = (delta / best_bl_m["macro_f1"] * 100) if best_bl_m["macro_f1"] > 0 else float("inf")
189	
190	    print(f"\nBest baseline: {best_bl_name} (Macro-F1: {best_bl_m['macro_f1']:.4f})")
191	    print(f"GRU Probe improvement: {delta:+.4f} ({pct:+.1f}%)")
192	
193	
194	if __name__ == "__main__":
195	    main()
196	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "dbcf6881-bead-4863-8ecb-395d89641413"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Reading artifacts/baseline_llm_judge.py",
  "usage": {
    "total_tokens": 54191,
    "tool_uses": 15,
    "duration_ms": 25817
  },
  "last_tool_name": "Read",
  "uuid": "f1a75106-668a-482d-aed7-179b096fcae7",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_01DpKdkbUd3qAdUVSRc5wSYN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/baseline_llm_judge.py",
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "f973d5d2-1a40-429d-8a77-35869c992e4c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NMztGoRb1xLMiMZ86zoaKX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2798,
      "cache_read_input_tokens": 51207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2798,
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

_source line 53 · 2026-05-14T22:40:38.004Z_

<details><summary>↩ Tool result · `toolu_01DpKdkbUd3qAdUVSRc5wSYN`</summary>

````text
1	#!/usr/bin/env python3
2	"""LLM-as-Judge baseline for progress/stagnation classification.
3	
4	Uses an LLM to zero-shot or few-shot classify agent trajectory windows,
5	as an upper-bound baseline for comparison with trained probes.
6	
7	Requires: pip install openai
8	API key via --api_key or OPENROUTER_API_KEY env var.
9	"""
10	
11	import argparse
12	import json
13	import os
14	import re
15	import sys
16	import time
17	from pathlib import Path
18	from collections import Counter
19	
20	import openai
21	from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
22	
23	
24	LABEL_MAP = {"stagnation": 0, "stagnating": 0, "stagnant": 0,
25	             "progress": 1, "progressing": 1, "advancing": 1}
26	
27	ZERO_SHOT_SYSTEM = """You are an expert at analyzing software engineering agent trajectories. Your task is to determine whether an agent is making meaningful progress toward solving a coding task, or whether it is stagnating (repeating actions, going in circles, or failing to advance).
28	
29	You will be shown a window of consecutive steps from the agent's interaction. Each step has a role (ai = agent action, user = environment observation) and text content.
30	
31	Respond ONLY with a JSON object in this exact format:
32	{"judgment": "progress" or "stagnation", "confidence": 1-5, "reasoning": "brief explanation"}"""
33	
34	ZERO_SHOT_USER = """Below is a window of {n_steps} consecutive steps from a software engineering agent's trajectory.
35	
36	{steps_text}
37	
38	Based on these steps, is the agent making meaningful progress toward solving the task, or is it stagnating?"""
39	
40	FEW_SHOT_SYSTEM = """You are an expert at analyzing software engineering agent trajectories. Your task is to determine whether an agent is making meaningful progress toward solving a coding task, or whether it is stagnating (repeating actions, going in circles, or failing to advance).
41	
42	You will be shown a window of consecutive steps from the agent's interaction. Each step has a role (ai = agent action, user = environment observation) and text content.
43	
44	Here are some examples:
45	
46	{examples}
47	
48	Respond ONLY with a JSON object in this exact format:
49	{{"judgment": "progress" or "stagnation", "confidence": 1-5, "reasoning": "brief explanation"}}"""
50	
51	
52	def compute_metrics(labels, preds):
53	    return {
54	        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
55	        "accuracy": accuracy_score(labels, preds),
56	        "precision_macro": precision_score(labels, preds, average="macro", zero_division=0),
57	        "recall_macro": recall_score(labels, preds, average="macro", zero_division=0),
58	        "f1_stagnation": f1_score(labels, preds, pos_label=0, zero_division=0),
59	        "f1_progress": f1_score(labels, preds, pos_label=1, zero_division=0),
60	    }
61	
62	
63	def truncate_text(text, max_chars=500):
64	    if not text:
65	        return ""
66	    if len(text) <= max_chars:
67	        return text
68	    return text[:max_chars] + "... [truncated]"
69	
70	
71	def format_steps(steps, max_total_chars=6000):
72	    parts = []
73	    budget = max_total_chars
74	    per_step = max(200, budget // max(len(steps), 1))
75	
76	    for i, step in enumerate(steps):
77	        role = step.get("role", "unknown")
78	        text = step.get("text", "") or ""
79	        truncated = truncate_text(text, per_step)
80	        part = f"[Step {i+1} | {role}]\n{truncated}"
81	        parts.append(part)
82	
83	    return "\n\n".join(parts)
84	
85	
86	def load_trajectories_index(traj_path):
87	    """Build index: row_index -> trajectory dict."""
88	    index = {}
89	    with open(traj_path) as f:
90	        for row_idx, line in enumerate(f):
91	            line = line.strip()
92	            if line:
93	                index[row_idx] = json.loads(line)
94	    return index
95	
96	
97	def extract_window_steps(window, traj_index):
98	    """Get actual step texts for a window from trajectory data."""
99	    row_idx = window["row_index"]
100	    step_indices = window["step_indices"]
101	    traj = traj_index.get(row_idx)
102	    if traj is None:
103	        return []
104	    trajectory = traj.get("trajectory", [])
105	    steps = []
106	    for si in step_indices:
107	        if si < len(trajectory):
108	            s = trajectory[si]
109	            steps.append({"role": s.get("role", "unknown"),
110	                          "text": s.get("text", "") or ""})
111	    return steps
112	
113	
114	def select_few_shot_examples(train_windows, traj_index, n_progress=1, n_stagnation=1, n_boundary=1):
115	    """Select high-confidence examples from training set for few-shot prompting."""
116	    progress_examples = []
117	    stagnation_examples = []
118	
119	    for w in train_windows:
120	        if w["confidence"] >= 3:
121	            if w["majority_label"] == 1:
122	                progress_examples.append(w)
123	            elif w["majority_label"] == 0:
124	                stagnation_examples.append(w)
125	
126	    # Boundary: conf=2 examples
127	    boundary_examples = [w for w in train_windows if w["confidence"] == 2]
128	
129	    import random
130	    rng = random.Random(42)
131	    selected = []
132	
133	    if progress_examples:
134	        selected.extend(rng.sample(progress_examples, min(n_progress, len(progress_examples))))
135	    if stagnation_examples:
136	        selected.extend(rng.sample(stagnation_examples, min(n_stagnation, len(stagnation_examples))))
137	    if boundary_examples:
138	        selected.extend(rng.sample(boundary_examples, min(n_boundary, len(boundary_examples))))
139	
140	    examples_text = []
141	    for i, w in enumerate(selected):
142	        steps = extract_window_steps(w, traj_index)
143	        label_str = "progress" if w["majority_label"] == 1 else "stagnation"
144	        steps_formatted = format_steps(steps, max_total_chars=2000)
145	        examples_text.append(
146	            f"--- Example {i+1} (Answer: {label_str}) ---\n{steps_formatted}\n"
147	            f'{{"judgment": "{label_str}", "confidence": {w["confidence"]}, "reasoning": "This is a {label_str} example."}}'
148	        )
149	
150	    return "\n\n".join(examples_text)
151	
152	
153	def parse_llm_response(text):
154	    """Extract judgment from LLM response with robust fallback."""
155	    # Try direct JSON parse
156	    try:
157	        obj = json.loads(text.strip())
158	        j = obj.get("judgment", "").lower().strip()
159	        if j in LABEL_MAP:
160	            return LABEL_MAP[j], obj.get("confidence", 0), obj.get("reasoning", "")
161	    except json.JSONDecodeError:
162	        pass
163	
164	    # Try extracting JSON from markdown code block
165	    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
166	    if m:
167	        try:
168	            obj = json.loads(m.group(1))
169	            j = obj.get("judgment", "").lower().strip()
170	            if j in LABEL_MAP:
171	                return LABEL_MAP[j], obj.get("confidence", 0), obj.get("reasoning", "")
172	        except json.JSONDecodeError:
173	            pass
174	
175	    # Try finding JSON object in text
176	    m = re.search(r"\{[^{}]*\"judgment\"[^{}]*\}", text, re.DOTALL)
177	    if m:
178	        try:
179	            obj = json.loads(m.group(0))
180	            j = obj.get("judgment", "").lower().strip()
181	            if j in LABEL_MAP:
182	                return LABEL_MAP[j], obj.get("confidence", 0), obj.get("reasoning", "")
183	        except json.JSONDecodeError:
184	            pass
185	
186	    # Keyword fallback
187	    lower = text.lower()
188	    if "stagnat" in lower and "progress" not in lower:
189	        return 0, 0, "keyword_fallback"
190	    if "progress" in lower and "stagnat" not in lower:
191	        return 1, 0, "keyword_fallback"
192	
193	    return -1, 0, "parse_failed"
194	
195	
196	def call_llm(client, model, system_msg, user_msg, max_retries=3):
197	    """Call LLM with retry logic. Returns (response_text, input_tokens, output_tokens)."""
198	    for attempt in range(max_retries):
199	        try:
200	            resp = client.chat.completions.create(
201	                model=model,
202	                messages=[
203	                    {"role": "system", "content": system_msg},
204	                    {"role": "user", "content": user_msg},
205	                ],
206	                temperature=0.0,
207	                max_tokens=256,
208	            )
209	            choice = resp.choices[0]
210	            usage = resp.usage
211	            return (
212	                choice.message.content or "",
213	                usage.prompt_tokens if usage else 0,
214	                usage.completion_tokens if usage else 0,
215	            )
216	        except (openai.RateLimitError, openai.APITimeoutError, openai.APIConnectionError) as e:
217	            wait = 2 ** (attempt + 1)
218	            print(f"  Retry {attempt+1}/{max_retries} after {type(e).__name__}, waiting {wait}s", flush=True)
219	            time.sleep(wait)
220	        except openai.APIError as e:
221	            if attempt < max_retries - 1:
222	                wait = 2 ** (attempt + 1)
223	                print(f"  Retry {attempt+1}/{max_retries} after APIError: {e}, waiting {wait}s", flush=True)
224	                time.sleep(wait)
225	            else:
226	                print(f"  FAILED after {max_retries} retries: {e}", flush=True)
227	                return "", 0, 0
228	    return "", 0, 0
229	
230	
231	def main():
232	    parser = argparse.ArgumentParser(description="LLM-as-Judge baseline for progress/stagnation")
233	    parser.add_argument("--data_dir", required=True, help="Dir containing data/windows_labeled.jsonl")
234	    parser.add_argument("--split_info", required=True, help="Path to split_info.json")
235	    parser.add_argument("--trajectories", required=True, help="Path to swe_agent_trajectories_5000.jsonl")
236	    parser.add_argument("--api_key", default=None, help="API key (or set OPENROUTER_API_KEY)")
237	    parser.add_argument("--base_url", default="http://47.94.22.126/v1", help="API base URL")
238	    parser.add_argument("--model", default="anthropic/claude-sonnet-4-6", help="Model ID")
239	    parser.add_argument("--mode", choices=["zero-shot", "few-shot"], default="zero-shot")
240	    parser.add_argument("--max_windows", type=int, default=0, help="0 = all test windows")
241	    parser.add_argument("--output", default="results/llm_judge_results.json", help="Output path")
242	    parser.add_argument("--resume", action="store_true", help="Resume from existing partial results")
243	    parser.add_argument("--rps", type=float, default=5.0, help="Max requests per second")
244	    parser.add_argument("--budget", type=float, default=100.0, help="Max spend in USD before pausing")
245	    parser.add_argument("--list_models", action="store_true", help="List available models and exit")
246	    args = parser.parse_args()
247	
248	    api_key = [REDACTED] or os.environ.get("OPENROUTER_API_KEY", "")
249	    if not api_key:
[REDACTED]	        print("ERROR: Provide --api_key or set OPENROUTER_API_KEY", file=sys.stderr)
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "d728712c-2be2-4e80-b5c2-9ff581897cf8"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Reading artifacts/generate_embeddings.py",
  "usage": {
    "total_tokens": 57931,
    "tool_uses": 16,
    "duration_ms": 27899
  },
  "last_tool_name": "Read",
  "uuid": "d78df718-7331-487c-b1b3-a03b45713608",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_01EP6NruL39kA6tigKVdccaf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/generate_embeddings.py",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "a2cb42c1-da03-4e24-8471-236f5d64e62a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CkRfuJPXNavqEmW1MSsaoW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 3735,
      "cache_read_input_tokens": 54005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3735,
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

_source line 56 · 2026-05-14T22:40:40.086Z_

<details><summary>↩ Tool result · `toolu_01EP6NruL39kA6tigKVdccaf`</summary>

```text
1	#!/usr/bin/env python3
2	"""Generate step embeddings for labeled windows using Qwen3-Embedding-0.6B.
3	
4	Expected windows_labeled.jsonl format (one JSON per line):
5	    {"trajectory_id": str, "window_idx": int, "step_indices": [int, ...],
6	     "majority_label": int (0=stagnation, 1=progress, -1=abstain),
7	     "confidence": int, "labels": {...}, "short_trajectory": bool}
8	
9	trajectory_id format: "instance_id__model_name__r{row_index}"
10	
11	Requires the original trajectories JSONL to retrieve step texts.
12	
13	Output: embeddings.pt containing per-window embedding tensors + metadata.
14	"""
15	
16	import argparse
17	import json
18	from collections import defaultdict
19	from pathlib import Path
20	
21	import torch
22	import torch.nn.functional as F
23	from tqdm import tqdm
24	from transformers import AutoModel, AutoTokenizer
25	
26	
27	def last_token_pool(last_hidden_states: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
28	    left_padding = attention_mask[:, -1].sum() == attention_mask.shape[0]
29	    if left_padding:
30	        return last_hidden_states[:, -1]
31	    seq_lengths = attention_mask.sum(dim=1) - 1
32	    batch_idx = torch.arange(last_hidden_states.shape[0], device=last_hidden_states.device)
33	    return last_hidden_states[batch_idx, seq_lengths]
34	
35	
36	def parse_row_index(trajectory_id: str) -> int:
37	    """Extract row_index from trajectory_id 'instance_id__model_name__r{idx}'."""
38	    return int(trajectory_id.rsplit("__r", 1)[1])
39	
40	
41	def build_trajectory_index(traj_path: str) -> tuple[dict, dict]:
42	    """Build trajectory index from raw JSONL.
43	
44	    Returns:
45	        steps_index: row_index (int) -> list of step dicts
46	        meta_index: row_index (int) -> {"instance_id": str, "model_name": str}
47	    """
48	    steps_index = {}
49	    meta_index = {}
50	    with open(traj_path) as f:
51	        for row_idx, line in enumerate(f):
52	            line = line.strip()
53	            if not line:
54	                continue
55	            raw = json.loads(line)
56	            steps = []
57	            for s in raw.get("trajectory") or []:
58	                steps.append({
59	                    "role": s.get("role", "unknown"),
60	                    "text": s.get("text") or s.get("system_prompt") or "",
61	                })
62	            steps_index[row_idx] = steps
63	            meta_index[row_idx] = {
64	                "instance_id": raw.get("instance_id", ""),
65	                "model_name": raw.get("model_name", ""),
66	            }
67	    return steps_index, meta_index
68	
69	
70	def load_windows(path: str) -> list[dict]:
71	    windows = []
72	    with open(path) as f:
73	        for line in f:
74	            line = line.strip()
75	            if line:
76	                windows.append(json.loads(line))
77	    return windows
78	
79	
80	@torch.no_grad()
81	def encode_texts(
82	    texts: list[str], model, tokenizer, batch_size: int, max_length: int, device: str
83	) -> torch.Tensor:
84	    all_embeds = []
85	    for i in range(0, len(texts), batch_size):
86	        batch = texts[i : i + batch_size]
87	        encoded = tokenizer(
88	            batch, max_length=max_length, padding=True, truncation=True, return_tensors="pt"
89	        ).to(device)
90	        outputs = model(**encoded)
91	        embeds = last_token_pool(outputs.last_hidden_state, encoded["attention_mask"])
92	        embeds = F.normalize(embeds, p=2, dim=1)
93	        all_embeds.append(embeds.cpu())
94	    return torch.cat(all_embeds, dim=0)
95	
96	
97	def main():
98	    parser = argparse.ArgumentParser(description="Generate step embeddings using Qwen3-Embedding-0.6B")
99	    parser.add_argument("--windows", required=True, help="Path to windows_labeled.jsonl")
100	    parser.add_argument("--trajectories", required=True, help="Path to original trajectories JSONL")
101	    parser.add_argument("--output", required=True, help="Output .pt file path")
102	    parser.add_argument("--model_name", default="Qwen/Qwen3-Embedding-0.6B")
103	    parser.add_argument("--batch_size", type=int, default=64, help="Texts per encoding batch")
104	    parser.add_argument("--max_length", type=int, default=512, help="Max tokens per step text")
105	    parser.add_argument("--device", default=None, help="Device (auto-detect if unset)")
106	    parser.add_argument("--chunk_size", type=int, default=500, help="Windows per checkpoint chunk")
107	    args = parser.parse_args()
108	
109	    output_path = Path(args.output)
110	    output_path.parent.mkdir(parents=True, exist_ok=True)
111	    checkpoint_path = output_path.with_suffix(".ckpt.pt")
112	    device = args.device or ("cuda" if torch.cuda.is_available() else "cpu")
113	
114	    # Resume
115	    start_idx = 0
116	    results = {"embeddings": [], "labels": [], "trajectory_ids": [], "instance_ids": [], "step_indices_list": [], "confidences": []}
117	    if checkpoint_path.exists():
118	        ckpt = torch.load(checkpoint_path, weights_only=False)
119	        results = ckpt["results"]
120	        start_idx = ckpt["next_idx"]
121	        print(f"Resumed from checkpoint: {start_idx} windows done")
122	
123	    # Load model
124	    print(f"Loading {args.model_name} ...")
125	    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)
126	    tokenizer.padding_side = "right"
127	    model = (
128	        AutoModel.from_pretrained(args.model_name, trust_remote_code=True, torch_dtype=torch.float16)
129	        .to(device)
130	        .eval()
131	    )
132	    embed_dim = model.config.hidden_size
133	    print(f"embed_dim={embed_dim}, device={device}")
134	
135	    # Load data
136	    print("Building trajectory index ...")
137	    traj_index, meta_index = build_trajectory_index(args.trajectories)
138	    print(f"Indexed {len(traj_index)} trajectories")
139	
140	    all_windows = load_windows(args.windows)
141	    windows = [w for w in all_windows if w.get("majority_label", -1) != -1]
142	    print(f"Total windows: {len(all_windows)}, usable (non-ABSTAIN): {len(windows)}, pending: {len(windows) - start_idx}")
143	
144	    if start_idx >= len(windows):
145	        print("All windows already processed.")
146	        return
147	
148	    pbar = tqdm(total=len(windows), initial=start_idx, desc="Embedding")
149	
150	    for chunk_start in range(start_idx, len(windows), args.chunk_size):
151	        chunk_end = min(chunk_start + args.chunk_size, len(windows))
152	        chunk = windows[chunk_start:chunk_end]
153	
154	        # Collect all step texts in this chunk
155	        all_texts = []
156	        text_map = []  # (window_idx_in_chunk, step_position)
157	        for ci, w in enumerate(chunk):
158	            row_index = w.get("row_index") or parse_row_index(w["trajectory_id"])
159	            steps = traj_index.get(row_index, [])
160	            for si, step_idx in enumerate(w["step_indices"]):
161	                text = steps[step_idx]["text"] if step_idx < len(steps) else ""
162	                all_texts.append(text if text else "[empty]")
163	                text_map.append((ci, si))
164	
165	        # Batch encode
166	        if all_texts:
167	            all_embeds = encode_texts(all_texts, model, tokenizer, args.batch_size, args.max_length, device)
168	        else:
169	            all_embeds = torch.zeros(0, embed_dim)
170	
171	        # Reassemble per window
172	        window_positions = defaultdict(list)
173	        for pos, (ci, si) in enumerate(text_map):
174	            window_positions[ci].append((si, pos))
175	
176	        for ci, w in enumerate(chunk):
177	            positions = sorted(window_positions.get(ci, []), key=lambda x: x[0])
178	            if positions:
179	                window_tensor = torch.stack([all_embeds[pos] for _, pos in positions])
180	            else:
181	                window_tensor = torch.zeros(1, embed_dim)
182	
183	            ri = w.get("row_index") or parse_row_index(w["trajectory_id"])
184	            instance_id = w.get("instance_id", meta_index[ri]["instance_id"])
185	            results["embeddings"].append(window_tensor)
186	            results["labels"].append(w["majority_label"])
187	            results["trajectory_ids"].append(w["trajectory_id"])
188	            results["instance_ids"].append(instance_id)
189	            results["step_indices_list"].append(w["step_indices"])
190	            results["confidences"].append(w["confidence"])
191	
192	        pbar.update(len(chunk))
193	
194	        # Checkpoint
195	        torch.save({"results": results, "next_idx": chunk_end}, checkpoint_path)
196	
197	    pbar.close()
198	
199	    # Save final output
200	    torch.save(
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "a3268b18-6865-4a08-a1d3-4f725dbae6bb"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Running ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 61018,
    "tool_uses": 17,
    "duration_ms": 29904
  },
  "last_tool_name": "Bash",
  "uuid": "c6ad0dd6-6414-4b6e-af08-1cf71593444e",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Bash · `toolu_01TnDSaHPyHD3F3ykXgrr9bW`</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/data/ 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "2b663cbb-bf19-4205-a49b-a2f8f2fa6095",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01F6vHQo1SvU5SLgMeoQcA4U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3082,
      "cache_read_input_tokens": 57740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3082,
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

_source line 59 · 2026-05-14T22:40:42.155Z_

<details><summary>↩ Tool result · `toolu_01TnDSaHPyHD3F3ykXgrr9bW`</summary>

```text
total 457M
-rw-r--r-- 1 ubuntu ubuntu  85K May 14 05:43 label_quality_details.jsonl
-rw-r--r-- 1 ubuntu ubuntu 140K May 14 06:02 label_quality_details_v2.jsonl
-rw-r--r-- 1 ubuntu ubuntu  69M May 14 05:00 swe_agent_trajectories_1000.jsonl
-rw-r--r-- 1 ubuntu ubuntu 367M May 14 05:54 swe_agent_trajectories_5000.jsonl
-rw-r--r-- 1 ubuntu ubuntu  21M May 14 06:32 windows_labeled.jsonl
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "80f952c2-bd53-4041-a564-148226433050"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 61320,
    "tool_uses": 18,
    "duration_ms": 31462
  },
  "last_tool_name": "Bash",
  "uuid": "07201e06-53de-4051-8788-a10499edb497",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Bash · `toolu_01353sZJdeGYkmo6F5zs9kyE`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe -name \"*.pkl\" -o -name \"*.joblib\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "25deee44-19d5-4ec2-8afd-9efb270a7b90",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LPsJBpWKdvLbLv8DmgwpN8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 300,
      "cache_read_input_tokens": 60822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 300,
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

_source line 62 · 2026-05-14T22:40:43.876Z_

<details><summary>↩ Tool result · `toolu_01353sZJdeGYkmo6F5zs9kyE`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/.venv/lib/python3.14/site-packages/numpy/_core/tests/data/astype_copy.pkl
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "f3839ccf-80c2-4c0c-9cd4-8a74724df9a5"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 61502,
    "tool_uses": 19,
    "duration_ms": 33004
  },
  "last_tool_name": "Bash",
  "uuid": "aa810ca8-ff19-4416-8f21-ee1e76eb2fa5",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Bash · `toolu_01HyR9xwH5vG1w8EBFFzExQb`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/checkpoints -type f 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "d5ab8505-0de0-4376-95af-083fff717247",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BXreUD8RB5BaPpyaiMnV1Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 180,
      "cache_read_input_tokens": 61122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 180,
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

_source line 65 · 2026-05-14T22:40:45.256Z_

<details><summary>↩ Tool result · `toolu_01HyR9xwH5vG1w8EBFFzExQb`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/checkpoints/openhands-fewshot-probe_DONE_20260514T142936.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/checkpoints/ablation-window-size_DONE_20260514T145741.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/checkpoints/cross-encoder-consistency_RUNNING_20260514T223115.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/checkpoints/baseline-llm-judge_ALLOCATED_20260514T114820.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/checkpoints/probe_001_QUEUED_20260514T080312.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/checkpoints/emb_001_RUNNING_20260514T064146.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/checkpoints/baseline-llm-judge_QUEUED_20260514T114815.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/checkpoints/outcome-bp-sensitivity_ALLOCATED_20260514T121220.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/checkpoints/baseline-llm-judge_RUNNING_20260514T114826.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/checkpoints/error-analysis_DONE_20260514T160612.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/checkpoints/twv-ablation_QUEUED_20260514T182134.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/checkpoints/data-scaling-v2_ANALYZING_20260514T145849.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/checkpoints/conf2-subset-v2_PREPARING_20260514T215017.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/checkpoints/f1-stag-analysis_RUNNING_20260514T221955.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/checkpoints/ablation-lf-holdout-v2_ANALYZING_20260514T145848.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/checkpoints/ablation-supcon_QUEUED_20260514T161749.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/checkpoints/calibration-analysis_RUNNING_20260514T223132.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/checkpoints/multiseed-structural_RUNNING_20260514T185609.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/checkpoints/ablation-lf-holdout-v2_ALLOCATED_20260514T145438.json
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/checkpoints/ablation-supcon_DONE_20260514T162118.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "2405f80a-d935-46b5-8113-e7b467c4be63"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 62581,
    "tool_uses": 20,
    "duration_ms": 34526
  },
  "last_tool_name": "Bash",
  "uuid": "54095aca-3a5c-4ba1-a040-d7c6a9676d41",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Bash · `toolu_01GwUkPmgarypM1U9GJAV1mf`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts -name \"best_model.pt\" -o -name \"embeddings.pt\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "e263d009-660b-4306-8555-565b4be41120",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Jhvr8DwxCqCFnvF9RwtmSu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1077,
      "cache_read_input_tokens": 61302,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1077,
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

_source line 68 · 2026-05-14T22:40:46.773Z_

<details><summary>↩ Tool result · `toolu_01GwUkPmgarypM1U9GJAV1mf`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "3e67ada0-1d42-4dae-a6e3-a9694275411f"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Reading evaluate_gold_set.py",
  "usage": {
    "total_tokens": 62718,
    "tool_uses": 21,
    "duration_ms": 36116
  },
  "last_tool_name": "Read",
  "uuid": "2822e449-c466-43b4-a5e8-79b52a5ce91f",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 70_

<details open><summary>🔧 Tool call — Read · `toolu_01RsRcDDy22CujsZC9EuUDQz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/evaluate_gold_set.py",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "d9990e07-fce3-4d4a-815b-f7d52e034e5b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DhTCJYNHJu2DiAQzzA9r2V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 136,
      "cache_read_input_tokens": 62379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 136,
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

_source line 71 · 2026-05-14T22:40:48.306Z_

<details><summary>↩ Tool result · `toolu_01RsRcDDy22CujsZC9EuUDQz`</summary>

````text
1	#!/usr/bin/env python3
2	"""Gold Set Evaluation Pipeline.
3	
4	Evaluates multiple models/label sources against human-annotated gold labels.
5	
6	Input:
7	  --gold_csv PATH   : CSV with columns (window_id, gold_label)
8	                      window_id format: {trajectory_id}__w{window_idx}
9	  --output_dir PATH : Output directory for results JSON + markdown report
10	
11	Evaluated models:
12	  1. MV labels        — majority vote from labeling functions
13	  2. probe_001        — GRU probe (checkpoints/best_model.pt)
14	  3. Structural RF    — RandomForest on hand-crafted features (trained on-the-fly)
15	  4. Structural GB    — GradientBoosting on hand-crafted features (trained on-the-fly)
16	  5. TWV labels       — Temporally-Weighted Vote σ=2 labels (data/windows_tlm_labels.jsonl)
17	
18	Output:
19	  - results.json     : Per-model metrics + gold distribution + deltas
20	  - report.md        : Human-readable markdown comparison report
21	
22	Dependencies: torch, scikit-learn, numpy
23	
24	Dry-run mode (--dry_run):
25	  Generates pseudo gold labels from conf>=2 MV labels, runs full pipeline.
26	"""
27	
28	import argparse
29	import csv
30	import json
31	import os
32	import re
33	import sys
34	import time
35	import warnings
36	from collections import Counter
37	from difflib import SequenceMatcher
38	from pathlib import Path
39	
40	import numpy as np
41	import torch
42	import torch.nn as nn
43	from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
44	from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
45	from sklearn.preprocessing import StandardScaler
46	from torch.utils.data import DataLoader
47	
48	warnings.filterwarnings("ignore", category=UserWarning)
49	
50	# ---------------------------------------------------------------------------
51	# Import probe model from project
52	# ---------------------------------------------------------------------------
53	sys.path.insert(0, str(Path(__file__).parent))
54	from probe_model import ProgressProbe, WindowDataset, collate_fn
55	
56	
57	# ===========================================================================
58	# Metrics
59	# ===========================================================================
60	
61	def compute_metrics(y_true, y_pred):
62	    return {
63	        "macro_f1": f1_score(y_true, y_pred, average="macro", zero_division=0),
64	        "f1_stag": f1_score(y_true, y_pred, pos_label=0, zero_division=0),
65	        "f1_prog": f1_score(y_true, y_pred, pos_label=1, zero_division=0),
66	        "precision_stag": precision_score(y_true, y_pred, pos_label=0, zero_division=0),
67	        "recall_stag": recall_score(y_true, y_pred, pos_label=0, zero_division=0),
68	        "accuracy": accuracy_score(y_true, y_pred),
69	    }
70	
71	
72	# ===========================================================================
73	# Structural feature extraction (from non_nlp_baseline.py)
74	# ===========================================================================
75	
76	EDIT_CMDS = {"edit", "str_replace", "create", "insert"}
77	SEARCH_CMDS = {"search_dir", "search_file", "find_file", "find", "grep", "view"}
78	NAV_CMDS = {"open", "goto", "scroll_down", "scroll_up", "cd", "ls", "cat"}
79	
80	
81	def _extract_command(text):
82	    match = re.search(r"```\n?(.*?)```", text, re.DOTALL)
83	    return match.group(1).strip() if match else None
84	
85	
86	def _cmd_similarity(a, b):
87	    if a == b:
88	        return 1.0
89	    if not a or not b:
90	        return 0.0
91	    return SequenceMatcher(None, a, b).ratio()
92	
93	
94	def extract_structural_features(steps, is_short):
95	    n = len(steps)
96	    if n == 0:
97	        return np.zeros(30, dtype=np.float32)
98	
99	    texts = [s["text"] for s in steps]
100	    text_lens = [len(t) for t in texts]
101	    actions = [(s, t) for s, t in zip(steps, texts) if s["role"] == "ai"]
102	    observations = [(s, t) for s, t in zip(steps, texts) if s["role"] == "user"]
103	    n_actions = len(actions)
104	    n_obs = len(observations)
105	
106	    mean_tlen = np.mean(text_lens)
107	    std_tlen = np.std(text_lens) if n > 1 else 0.0
108	    max_tlen = max(text_lens)
109	    min_tlen = min(text_lens)
110	    action_lens = [len(t) for _, t in actions] if actions else [0]
111	    obs_lens = [len(t) for _, t in observations] if observations else [0]
112	    mean_action_len = np.mean(action_lens)
113	    mean_obs_len = np.mean(obs_lens)
114	
115	    if n > 1:
116	        x = np.arange(n, dtype=float)
117	        y = np.array(text_lens, dtype=float)
118	        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (n * np.dot(x, x) - x.sum() ** 2 + 1e-9)
119	    else:
120	        slope = 0.0
121	
122	    commands = []
123	    for s, t in actions:
124	        cmd = _extract_command(t)
125	        if cmd:
126	            commands.append(cmd)
127	    n_cmds = len(commands)
128	    cmd_lens = [len(c) for c in commands] if commands else [0]
129	    mean_cmd_len = np.mean(cmd_lens)
130	    max_cmd_len = max(cmd_lens) if cmd_lens else 0
131	
132	    if n_cmds > 0:
133	        unique_cmds = len(set(commands))
134	        unique_cmd_ratio = unique_cmds / n_cmds
135	        cmd_counter = Counter(commands)
136	        max_repeat = cmd_counter.most_common(1)[0][1]
137	        repeat_ratio = max_repeat / n_cmds
138	    else:
139	        unique_cmd_ratio = 1.0
140	        repeat_ratio = 0.0
141	
142	    n_edit = n_search = n_nav = n_submit = 0
143	    for cmd in commands:
144	        first_word = cmd.strip().split()[0] if cmd.strip() else ""
145	        if first_word in EDIT_CMDS:
146	            n_edit += 1
147	        elif first_word in SEARCH_CMDS:
148	            n_search += 1
149	        elif first_word in NAV_CMDS:
150	            n_nav += 1
151	        elif first_word == "submit":
152	            n_submit += 1
153	    edit_ratio = n_edit / max(n_cmds, 1)
154	    search_ratio = n_search / max(n_cmds, 1)
155	
156	    if n_cmds >= 2:
157	        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]
158	        avg_adj_sim = np.mean(sims)
159	        max_adj_sim = max(sims)
160	        max_run, cur_run = 1, 1
161	        for s in sims:
162	            if s >= 0.9:
163	                cur_run += 1
164	                max_run = max(max_run, cur_run)
165	            else:
166	                cur_run = 1
167	    else:
168	        avg_adj_sim = max_adj_sim = 0.0
169	        max_run = 0
170	
171	    n_errors = sum(1 for t in texts if "Traceback" in t or "Error" in t)
172	    n_test_output = sum(1 for t in texts if ("PASSED" in t or "FAILED" in t) and "test" in t.lower())
173	    n_file_display = sum(1 for t in texts if "[File:" in t)
174	    n_nonzero_exit = sum(
175	        1 for _, t in observations if re.search(r"exit code [1-9]|returned non-zero|command not found", t)
176	    )
177	
178	    return np.array([
179	        n, n_actions, n_obs, n_actions / max(n, 1),
180	        mean_tlen, std_tlen, max_tlen, min_tlen,
181	        mean_action_len, mean_obs_len, slope,
182	        n_cmds, mean_cmd_len, max_cmd_len,
183	        unique_cmd_ratio, repeat_ratio,
184	        n_edit, n_search, n_nav, n_submit,
185	        edit_ratio, search_ratio,
186	        avg_adj_sim, max_adj_sim, max_run,
187	        n_errors, n_test_output, n_file_display, n_nonzero_exit,
188	        float(is_short),
189	    ], dtype=np.float32)
190	
191	
192	# ===========================================================================
193	# Data loading helpers
194	# ===========================================================================
195	
196	def load_windows_jsonl(path):
197	    windows = []
198	    with open(path) as f:
199	        for line in f:
200	            line = line.strip()
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "dbd83b6a-1a27-4664-8eb3-cb4a9b264244"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Reading artifacts/non_nlp_baseline.py",
  "usage": {
    "total_tokens": 65681,
    "tool_uses": 22,
    "duration_ms": 38207
  },
  "last_tool_name": "Read",
  "uuid": "11af7f27-2f95-4249-a7a9-53d3acb5b99e",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 73_

<details open><summary>🔧 Tool call — Read · `toolu_011WdoRqdGmnukj6NBexzBF8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/non_nlp_baseline.py",
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "d4dbe014-d382-4ead-ab9d-81092c7d3e1e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DidRdX1LkyPfjAiBxv3HHA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 2957,
      "cache_read_input_tokens": 62515,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2957,
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

_source line 74 · 2026-05-14T22:40:50.396Z_

<details><summary>↩ Tool result · `toolu_011WdoRqdGmnukj6NBexzBF8`</summary>

````text
1	#!/usr/bin/env python3
2	"""Non-NLP baseline: structural/numerical features only.
3	
4	Extracts hand-crafted features from raw trajectory steps (no embeddings),
5	trains LogisticRegression, RandomForest, GradientBoosting.
6	Uses the same train/val/test split as probe_001.
7	"""
8	
9	import json
10	import re
11	import sys
12	import argparse
13	from collections import Counter
14	from difflib import SequenceMatcher
15	from pathlib import Path
16	
17	import numpy as np
18	from sklearn.linear_model import LogisticRegression
19	from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
20	from sklearn.preprocessing import StandardScaler
21	from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
22	
23	
24	def compute_metrics(labels, preds):
25	    return {
26	        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
27	        "accuracy": accuracy_score(labels, preds),
28	        "precision_macro": precision_score(labels, preds, average="macro", zero_division=0),
29	        "recall_macro": recall_score(labels, preds, average="macro", zero_division=0),
30	        "f1_stagnation": f1_score(labels, preds, pos_label=0, zero_division=0),
31	        "f1_progress": f1_score(labels, preds, pos_label=1, zero_division=0),
32	    }
33	
34	
35	def extract_command(text):
36	    match = re.search(r"```\n?(.*?)```", text, re.DOTALL)
37	    return match.group(1).strip() if match else None
38	
39	
40	EDIT_CMDS = {"edit", "str_replace", "create", "insert"}
41	SEARCH_CMDS = {"search_dir", "search_file", "find_file", "find", "grep", "view"}
42	NAV_CMDS = {"open", "goto", "scroll_down", "scroll_up", "cd", "ls", "cat"}
43	
44	
45	def cmd_similarity(a, b):
46	    if a == b:
47	        return 1.0
48	    if not a or not b:
49	        return 0.0
50	    return SequenceMatcher(None, a, b).ratio()
51	
52	
53	def extract_features(steps, is_short):
54	    """Extract structural features from a list of step dicts.
55	
56	    Each step dict has: role, text
57	    """
58	    n = len(steps)
59	    if n == 0:
60	        return np.zeros(30)
61	
62	    roles = [s["role"] for s in steps]
63	    texts = [s["text"] for s in steps]
64	    text_lens = [len(t) for t in texts]
65	
66	    actions = [(s, t) for s, t in zip(steps, texts) if s["role"] == "ai"]
67	    observations = [(s, t) for s, t in zip(steps, texts) if s["role"] == "user"]
68	
69	    n_actions = len(actions)
70	    n_obs = len(observations)
71	
72	    # --- text length features ---
73	    mean_tlen = np.mean(text_lens)
74	    std_tlen = np.std(text_lens) if n > 1 else 0.0
75	    max_tlen = max(text_lens)
76	    min_tlen = min(text_lens)
77	
78	    action_lens = [len(t) for _, t in actions] if actions else [0]
79	    obs_lens = [len(t) for _, t in observations] if observations else [0]
80	    mean_action_len = np.mean(action_lens)
81	    mean_obs_len = np.mean(obs_lens)
82	
83	    # text length trend (slope via simple linear regression)
84	    if n > 1:
85	        x = np.arange(n, dtype=float)
86	        y = np.array(text_lens, dtype=float)
87	        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (n * np.dot(x, x) - x.sum()**2 + 1e-9)
88	    else:
89	        slope = 0.0
90	
91	    # --- command features ---
92	    commands = []
93	    for s, t in actions:
94	        cmd = extract_command(t)
95	        if cmd:
96	            commands.append(cmd)
97	
98	    n_cmds = len(commands)
99	    cmd_lens = [len(c) for c in commands] if commands else [0]
100	    mean_cmd_len = np.mean(cmd_lens)
101	    max_cmd_len = max(cmd_lens) if cmd_lens else 0
102	
103	    if n_cmds > 0:
104	        unique_cmds = len(set(commands))
105	        unique_cmd_ratio = unique_cmds / n_cmds
106	        cmd_counter = Counter(commands)
107	        max_repeat = cmd_counter.most_common(1)[0][1]
108	        repeat_ratio = max_repeat / n_cmds
109	    else:
110	        unique_cmd_ratio = 1.0
111	        repeat_ratio = 0.0
112	
113	    # command type counts
114	    n_edit = 0
115	    n_search = 0
116	    n_nav = 0
117	    n_submit = 0
118	    for cmd in commands:
119	        first_word = cmd.strip().split()[0] if cmd.strip() else ""
120	        if first_word in EDIT_CMDS:
121	            n_edit += 1
122	        elif first_word in SEARCH_CMDS:
123	            n_search += 1
124	        elif first_word in NAV_CMDS:
125	            n_nav += 1
126	        elif first_word == "submit":
127	            n_submit += 1
128	
129	    edit_ratio = n_edit / max(n_cmds, 1)
130	    search_ratio = n_search / max(n_cmds, 1)
131	
132	    # adjacent command similarity
133	    if n_cmds >= 2:
134	        sims = [cmd_similarity(commands[i], commands[i+1]) for i in range(n_cmds - 1)]
135	        avg_adj_sim = np.mean(sims)
136	        max_adj_sim = max(sims)
137	        # max consecutive run with sim >= 0.9
138	        max_run = 1
139	        cur_run = 1
140	        for s in sims:
141	            if s >= 0.9:
142	                cur_run += 1
143	                max_run = max(max_run, cur_run)
144	            else:
145	                cur_run = 1
146	    else:
147	        avg_adj_sim = 0.0
148	        max_adj_sim = 0.0
149	        max_run = 0
150	
151	    # --- content pattern features ---
152	    n_errors = sum(1 for t in texts if "Traceback" in t or "Error" in t)
153	    n_test_output = sum(1 for t in texts if ("PASSED" in t or "FAILED" in t) and "test" in t.lower())
154	    n_file_display = sum(1 for t in texts if "[File:" in t)
155	
156	    # exit code patterns in observations (look for "exit code" or "$?" patterns)
157	    n_nonzero_exit = sum(1 for _, t in observations if re.search(r"exit code [1-9]|returned non-zero|command not found", t))
158	
159	    feature_vec = np.array([
160	        n,                    # 0: num_steps
161	        n_actions,            # 1: num_actions
162	        n_obs,                # 2: num_observations
163	        n_actions / max(n, 1),# 3: action_ratio
164	        mean_tlen,            # 4: mean_text_len
165	        std_tlen,             # 5: std_text_len
166	        max_tlen,             # 6: max_text_len
167	        min_tlen,             # 7: min_text_len
168	        mean_action_len,      # 8: mean_action_len
169	        mean_obs_len,         # 9: mean_obs_len
170	        slope,                # 10: text_len_trend
171	        n_cmds,               # 11: num_commands
172	        mean_cmd_len,         # 12: mean_cmd_len
173	        max_cmd_len,          # 13: max_cmd_len
174	        unique_cmd_ratio,     # 14: unique_cmd_ratio
175	        repeat_ratio,         # 15: max_repeat_ratio
176	        n_edit,               # 16: num_edit_cmds
177	        n_search,             # 17: num_search_cmds
178	        n_nav,                # 18: num_nav_cmds
179	        n_submit,             # 19: num_submit_cmds
180	        edit_ratio,           # 20: edit_ratio
181	        search_ratio,         # 21: search_ratio
182	        avg_adj_sim,          # 22: avg_adjacent_cmd_similarity
183	        max_adj_sim,          # 23: max_adjacent_cmd_similarity
184	        max_run,              # 24: max_consecutive_similar_cmds
185	        n_errors,             # 25: num_errors
186	        n_test_output,        # 26: num_test_outputs
187	        n_file_display,       # 27: num_file_displays
188	        n_nonzero_exit,       # 28: num_nonzero_exits
189	        float(is_short),      # 29: is_short_trajectory
190	    ], dtype=np.float32)
191	
192	    return feature_vec
193	
194	
195	FEATURE_NAMES = [
196	    "num_steps", "num_actions", "num_observations", "action_ratio",
197	    "mean_text_len", "std_text_len", "max_text_len", "min_text_len",
198	    "mean_action_len", "mean_obs_len", "text_len_trend",
199	    "num_commands", "mean_cmd_len", "max_cmd_len",
200	    "unique_cmd_ratio", "max_repeat_ratio",
201	    "num_edit_cmds", "num_search_cmds", "num_nav_cmds", "num_submit_cmds",
202	    "edit_ratio", "search_ratio",
203	    "avg_adjacent_cmd_sim", "max_adjacent_cmd_sim", "max_consecutive_similar",
204	    "num_errors", "num_test_outputs", "num_file_displays", "num_nonzero_exits",
205	    "is_short_trajectory",
206	]
207	
208	
209	def build_trajectory_index(traj_path):
210	    """row_index -> list of step dicts [{role, text}, ...]"""
211	    index = {}
212	    with open(traj_path) as f:
213	        for row_idx, line in enumerate(f):
214	            line = line.strip()
215	            if not line:
216	                continue
217	            raw = json.loads(line)
218	            steps = []
219	            for s in raw.get("trajectory") or []:
220	                steps.append({
221	                    "role": s.get("role", "unknown"),
222	                    "text": s.get("text") or s.get("system_prompt") or "",
223	                })
224	            index[row_idx] = steps
225	    return index
226	
227	
228	def load_windows(path):
229	    windows = []
230	    with open(path) as f:
231	        for line in f:
232	            line = line.strip()
233	            if line:
234	                windows.append(json.loads(line))
235	    return windows
236	
237	
238	def print_table(results):
239	    header = "| Method                      | Macro-F1 | Accuracy | F1(stag) | F1(prog) |"
240	    sep = "|" + "|".join(["-" * 30] + ["-" * 10] * 4) + "|"
241	    print(header)
242	    print(sep)
243	    for name, m in results:
244	        row = f"| {name:28s} |"
245	        for key in ["macro_f1", "accuracy", "f1_stagnation", "f1_progress"]:
246	            v = m.get(key)
247	            if v is None:
248	                row += "    —     |"
249	            else:
250	                row += f" {v:.4f}   |"
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "ca2a9cb1-37ce-4d90-ba55-8f06d52764d1"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Reading artifacts/data_scaling.py",
  "usage": {
    "total_tokens": 69321,
    "tool_uses": 23,
    "duration_ms": 40277
  },
  "last_tool_name": "Read",
  "uuid": "d55bf4ca-aaf4-415f-8cce-c6cdfb620772",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 76_

<details open><summary>🔧 Tool call — Read · `toolu_012DAVT2AuvWth4J5JLQG6jp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/data_scaling.py",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "8f887fac-e642-40b9-81d8-2509318a2696",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CqHj8BTpTH7YRsHFYWMfmS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 3632,
      "cache_read_input_tokens": 65472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3632,
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

_source line 77 · 2026-05-14T22:40:52.464Z_

<details><summary>↩ Tool result · `toolu_012DAVT2AuvWth4J5JLQG6jp`</summary>

```text
1	#!/usr/bin/env python3
2	"""Data scaling experiment: evaluate probe sensitivity to training data volume.
3	
4	Trains GRU probe with 10%/25%/50%/100% of training instances (instance-level
5	subsampling). Test and val sets are fixed across all ratios.
6	Baseline (100% data, probe_001): test macro_f1=0.905 (conf>=2, 15401 windows)
7	"""
8	
9	import json
10	import random
11	import sys
12	from pathlib import Path
13	
14	import numpy as np
15	import torch
16	import torch.nn as nn
17	from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
18	from torch.utils.data import DataLoader
19	
20	sys.path.insert(0, str(Path(__file__).parent))
21	from probe_model import ProgressProbe, WindowDataset, collate_fn, split_by_instance
22	
23	RATIOS = [0.10, 0.25, 0.50, 1.00]
24	SEED = 42
25	MIN_CONFIDENCE = 2
26	HIDDEN_SIZE = 256
27	NUM_LAYERS = 2
28	LR = 1e-3
29	BATCH_SIZE = 32
30	EPOCHS = 20
31	PATIENCE = 5
32	DROPOUT = 0.1
33	WEIGHT_DECAY = 0.01
34	
35	
36	def set_seed(seed: int):
37	    random.seed(seed)
38	    np.random.seed(seed)
39	    torch.manual_seed(seed)
40	    if torch.cuda.is_available():
41	        torch.cuda.manual_seed_all(seed)
42	
43	
44	def compute_metrics(labels, preds):
45	    return {
46	        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
47	        "accuracy": accuracy_score(labels, preds),
48	        "precision_macro": precision_score(labels, preds, average="macro", zero_division=0),
49	        "recall_macro": recall_score(labels, preds, average="macro", zero_division=0),
50	        "f1_stagnation": f1_score(labels, preds, pos_label=0, zero_division=0),
51	        "f1_progress": f1_score(labels, preds, pos_label=1, zero_division=0),
52	    }
53	
54	
55	class EarlyStopping:
56	    def __init__(self, patience=5):
57	        self.patience = patience
58	        self.counter = 0
59	        self.best_score = None
60	        self.should_stop = False
61	
62	    def step(self, score):
63	        if self.best_score is None or score > self.best_score:
64	            self.best_score = score
65	            self.counter = 0
66	            return True
67	        self.counter += 1
68	        if self.counter >= self.patience:
69	            self.should_stop = True
70	        return False
71	
72	
73	@torch.no_grad()
74	def evaluate(model, loader, device):
75	    model.eval()
76	    all_labels, all_preds = [], []
77	    for padded, labels, lengths in loader:
78	        logits = model(padded.to(device), lengths)
79	        preds = (torch.sigmoid(logits) >= 0.5).long().cpu()
80	        all_labels.extend(labels.long().tolist())
81	        all_preds.extend(preds.tolist())
82	    return compute_metrics(all_labels, all_preds)
83	
84	
85	def subsample_train_instances(instance_ids, train_idx, ratio, seed):
86	    """Subsample training instances at given ratio, return new train window indices."""
87	    train_instances = sorted(set(instance_ids[i] for i in train_idx))
88	    rng = random.Random(seed)
89	    k = max(1, int(len(train_instances) * ratio))
90	    selected = set(rng.sample(train_instances, k))
91	    return [i for i in train_idx if instance_ids[i] in selected], len(train_instances), k
92	
93	
94	def train_one_ratio(ratio, embeddings, labels, instance_ids, embed_dim,
95	                    train_idx, val_idx, test_idx, device):
96	    set_seed(SEED)
97	
98	    sub_train_idx, total_inst, kept_inst = subsample_train_instances(
99	        instance_ids, train_idx, ratio, SEED
100	    )
101	
102	    def make_ds(indices):
103	        return WindowDataset([embeddings[i] for i in indices], [labels[i] for i in indices])
104	
105	    train_ds = make_ds(sub_train_idx)
106	    val_ds = make_ds(val_idx)
107	    test_ds = make_ds(test_idx)
108	
109	    train_labels = [labels[i] for i in sub_train_idx]
110	    num_pos = sum(train_labels)
111	    num_neg = len(train_labels) - num_pos
112	    pos_weight = torch.tensor([num_neg / max(num_pos, 1)]).to(device)
113	
114	    print(f"\n{'='*60}")
115	    print(f"Ratio: {ratio*100:.0f}% | instances: {kept_inst}/{total_inst} | "
116	          f"windows: {len(train_ds)} (pos={num_pos}, neg={num_neg})")
117	    print(f"Val: {len(val_ds)} | Test: {len(test_ds)} | pos_weight: {pos_weight.item():.3f}")
118	
119	    train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True, collate_fn=collate_fn)
120	    val_loader = DataLoader(val_ds, batch_size=BATCH_SIZE, collate_fn=collate_fn)
121	    test_loader = DataLoader(test_ds, batch_size=BATCH_SIZE, collate_fn=collate_fn)
122	
123	    model = ProgressProbe(
124	        embed_dim=embed_dim,
125	        hidden_size=HIDDEN_SIZE,
126	        num_layers=NUM_LAYERS,
127	        dropout=DROPOUT,
128	    ).to(device)
129	
130	    optimizer = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=WEIGHT_DECAY)
131	    criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
132	    early_stopping = EarlyStopping(patience=PATIENCE)
133	
134	    best_state = None
135	    for epoch in range(1, EPOCHS + 1):
136	        model.train()
137	        total_loss, n = 0.0, 0
138	        for padded, batch_labels, lengths in train_loader:
139	            padded = padded.to(device)
140	            batch_labels = batch_labels.to(device)
141	            logits = model(padded, lengths)
142	            loss = criterion(logits, batch_labels)
143	            optimizer.zero_grad()
144	            loss.backward()
145	            optimizer.step()
146	            total_loss += loss.item() * len(batch_labels)
147	            n += len(batch_labels)
148	
149	        avg_loss = total_loss / n
150	        val_metrics = evaluate(model, val_loader, device)
151	        is_best = early_stopping.step(val_metrics["macro_f1"])
152	        marker = " *" if is_best else ""
153	        print(f"  Epoch {epoch:2d} | loss={avg_loss:.4f} | "
154	              f"val_F1={val_metrics['macro_f1']:.4f} acc={val_metrics['accuracy']:.4f}{marker}")
155	
156	        if is_best:
157	            best_state = {k: v.clone() for k, v in model.state_dict().items()}
158	
159	        if early_stopping.should_stop:
160	            print(f"  Early stopping at epoch {epoch}")
161	            break
162	
163	    model.load_state_dict(best_state)
164	    test_metrics = evaluate(model, test_loader, device)
165	    print(f"  Test: macro_f1={test_metrics['macro_f1']:.4f} acc={test_metrics['accuracy']:.4f}")
166	
167	    return {
168	        "ratio": ratio,
169	        "train_instances": kept_inst,
170	        "total_instances": total_inst,
171	        "train_windows": len(train_ds),
172	        "val_windows": len(val_ds),
173	        "test_windows": len(test_ds),
174	        "best_val_macro_f1": early_stopping.best_score,
175	        "test_metrics": test_metrics,
176	    }
177	
178	
179	def main():
180	    device = "cuda" if torch.cuda.is_available() else "cpu"
181	    print(f"Device: {device}")
182	
183	    data_dir = Path(__file__).parent
184	    data_path = data_dir / "embeddings.pt"
185	    data = torch.load(data_path, weights_only=False)
186	
187	    embeddings = data["embeddings"]
188	    labels = data["labels"]
189	    instance_ids = data["instance_ids"]
190	    confidences = data.get("confidences", [1] * len(labels))
191	    embed_dim = data["embed_dim"]
192	
193	    keep = [i for i, c in enumerate(confidences) if c >= MIN_CONFIDENCE]
194	    print(f"Confidence filter: {len(keep)}/{len(labels)} windows with conf>={MIN_CONFIDENCE}")
195	    embeddings = [embeddings[i] for i in keep]
196	    labels = [labels[i] for i in keep]
197	    instance_ids = [instance_ids[i] for i in keep]
198	
199	    train_idx, val_idx, test_idx = split_by_instance(instance_ids, seed=SEED)
200	    print(f"Split: train={len(train_idx)}, val={len(val_idx)}, test={len(test_idx)}")
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "9e4e9dfa-fe47-426a-9e48-809ab42ee5a8"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 72255,
    "tool_uses": 24,
    "duration_ms": 42267
  },
  "last_tool_name": "Bash",
  "uuid": "19ec721f-5a34-4d2b-a001-a07a635737d2",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 79_

<details open><summary>🔧 Tool call — Bash · `toolu_01Y5EDeWUfDdqzM4uB1nHFoD`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe -maxdepth 2 -name \"*.yaml\" -o -name \"*.json\" | grep -E \"(config|const|setup)\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "f1480693-592a-495f-a472-471ef36da5ac",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018bqC7ge4BMTfaStYRMG6CE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 2924,
      "cache_read_input_tokens": 69104,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2924,
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

_source line 80 · 2026-05-14T22:40:54.507Z_

<details><summary>↩ Tool result · `toolu_01Y5EDeWUfDdqzM4uB1nHFoD`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "e41bbc9a-a057-461c-b492-0da54deec3a5"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Reading memory.md",
  "usage": {
    "total_tokens": 72399,
    "tool_uses": 25,
    "duration_ms": 43611
  },
  "last_tool_name": "Read",
  "uuid": "89fa8897-19b8-467c-b012-8dea9845f796",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 82_

<details open><summary>🔧 Tool call — Read · `toolu_01Ggx8e2H8RfNqHdqcbazDNC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "94bc7f00-cdd4-4c4a-8b77-92de5735c783",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0121GmTSPUwSCvFeRDNjiyxN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 142,
      "cache_read_input_tokens": 72028,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 142,
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

_source line 83 · 2026-05-14T22:40:55.797Z_

<details><summary>↩ Tool result · `toolu_01Ggx8e2H8RfNqHdqcbazDNC`</summary>

```text
1	# Agent Progress Probe - Memory
2	
3	## F1_stag Per-Class Breakdown 分析 (2026-05-14)
4	
5	### 基本信息
6	- 模型: probe_001 (checkpoints_full/best_model.pt)
7	- 测试集: 8101 windows (full split), 2206 with conf≥2
8	- 整体 (conf≥2): f1_stag=0.8522, macro_f1=0.8946, precision_stag=0.9509, recall_stag=0.772
9	
10	### Dim1: 按 Confidence 分层
11	| Conf | N | n_stag | f1_stag | prec_stag | rec_stag | f1_prog |
12	|------|---|--------|---------|-----------|----------|---------|
13	| 1 | 5895 | 1502 | 0.7452 | 0.7235 | 0.7683 | 0.9092 |
14	| 2 | 2149 | 711 | 0.8498 | 0.9512 | 0.7679 | 0.9359 |
15	| 3 | 57 | 17 | 0.9412 | 0.9412 | 0.9412 | 0.975 |
16	
17	**发现**: f1_stag 随 confidence 单调递增 (0.74→0.85→0.94)。conf=2 的瓶颈是 recall_stag=0.77 (precision 很高 0.95)。
18	
19	### Dim2: 按 Trajectory 长度分层
20	| 长度 | N | n_stag | f1_stag | prec_stag | rec_stag |
21	|------|---|--------|---------|-----------|----------|
22	| short (<10) | 17 | 2 | 0.0 | 0.0 | 0.0 |
23	| medium (10-30) | 1018 | 123 | 0.6637 | 0.74 | 0.6016 |
24	| long (>30) | 7066 | 2105 | 0.7836 | 0.7872 | 0.78 |
25	
26	**发现**: 中等长度 trajectory 的 f1_stag 最低 (0.66)，recall_stag 仅 0.60。长 trajectory (>30 步) 表现最好。conf≥2 下长 trajectory f1_stag=0.86。
27	
28	### Dim3: 按 LF 一致性分层
29	| Pattern | N | n_stag | f1_stag | f1_prog |
30	|---------|---|--------|---------|---------|
31	| 2lf_agree | 1535 | 316 | **0.9462** | 0.9861 |
32	| 3lf_unanimous | 57 | 17 | **0.9412** | 0.975 |
33	| 2lf_disagree | 1714 | 427 | 0.7829 | 0.9071 |
34	| 3lf_2v1_split | 614 | 395 | 0.7565 | 0.7235 |
35	| 1lf_only | 4181 | 1075 | 0.7266 | 0.91 |
36	
37	**发现**: LF 一致性是 f1_stag 的关键预测因子。2-LF 一致或 3-LF 全票一致时 f1_stag > 0.94；3-LF 2v1 分裂时降至 0.76，且 f1_prog 也大跌 (0.72)。
38	
39	### Dim4: 按 Outcome 分层
40	| Outcome | N (全) | f1_stag (全) | N (conf≥2) | f1_stag (conf≥2) |
41	|---------|--------|------------|------------|-------------------|
42	| resolved | 739 | 0.8116 | 303 | **0.3333** |
43	| unresolved | 7362 | 0.7755 | 1903 | 0.8545 |
44	
45	**发现**: conf≥2 下 resolved 的 f1_stag 骤降至 0.33，因为 resolved trajectory 中 conf≥2 的 stag 样本极少。全测试集上 resolved 的 f1_stag (0.81) 反而略高于 unresolved (0.78)。
46	
47	### Dim5: 错误子类型分析 (conf≥2)
48	**Missed Stagnation (FP in standard CM, N=166)**:
49	- **100% 来自 unresolved** trajectory
50	- 89% 是 3lf_2v1_split pattern (OB 投 progress 但整体标为 stag)
51	- 99% 的 OB vote = 0 (progress)
52	- 位置分布: last_third 58%, mid_third 31%, first_third 11%
53	- 平均 prob=0.776 (高置信度错误)，45% prob>0.8
54	
55	**False Stag Alarm (FN in standard CM, N=29)**:
56	- 86% unresolved，14% resolved
57	- 59% 是 2lf_agree pattern
58	- 平均 prob=0.215 (低置信度)
59	- 100% prob<0.6
60	
61	### 核心结论
62	1. **f1_stag 瓶颈 = recall_stag**：precision 很高 (0.95) 但 recall 偏低 (0.77)
63	2. **主要错误模式**: OB-与其他 LF 分歧时 (3lf_2v1_split)，probe 跟随 OB 的 progress 判断，漏掉了真实的 stagnation → 166/195 (85%) 的错误是这类
64	3. **高置信度盲点**: 这些 missed stagnation 的平均 sigmoid prob=0.78，probe 很"确信"地犯错
65	4. **trajectory 尾部最难**: 58% 的 missed stagnation 在 trajectory 最后 1/3
66	5. **LF 一致性是质量信号**: 一致时 f1_stag > 0.94，分裂时降至 0.76
67	
68	## 跨域评估数据泄漏警告 (2026-05-14)
69	
70	cross-agent-structural 报告的 Struct GB 0.9674 macro_f1 (全量 OH 150k windows) 在 instance-level test split 上跌至 **0.6936**（-27.4pp）。Probe 在同一 test split 上 0.7512，反超 GB（Δ=5.76pp, p<0.001）。
71	
72	**原因假设**: cross-agent-structural 的 0.967 评估可能未按 instance 隔离训练/测试——structural features 在 SWE 上训练后直接在全量 OH 上评估（zero-shot），但 OH 的 LF 标签可能存在 instance 内窗口相关性，导致 zero-shot 数字虚高。
73	
74	**影响**: 论文 Claim 1 跨域数字（"structural features 0.967 cross-agent"）需要修正。3 个 Worker 正在调查。
75	
76	**决策**: 等 Worker 完成后确认真实跨域数字。如果 0.694 成立，跨域叙事需调整——structural 优势可能限于 in-domain。
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "f1c86cc7-2f75-461e-8c4d-60ecbda19ce9"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Reading paper_framing.md",
  "usage": {
    "total_tokens": 74660,
    "tool_uses": 26,
    "duration_ms": 45500
  },
  "last_tool_name": "Read",
  "uuid": "48492d0b-de2b-4e9e-97a5-152cdec2df47",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 85_

<details open><summary>🔧 Tool call — Read · `toolu_01JyEhnf7nK2pcD9YEAW88gi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/paper_framing.md",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "7e48bd70-76a4-4ffb-9918-3c959e994c74",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015iy6Z67FVDUSgBtXXquqzN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 2259,
      "cache_read_input_tokens": 72170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2259,
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

_source line 86 · 2026-05-14T22:40:57.687Z_

<details><summary>↩ Tool result · `toolu_01JyEhnf7nK2pcD9YEAW88gi`</summary>

```text
1	# Paper Framing — agent_progress_probe
2	
3	## Target Venue
4	- Primary: EMNLP 2026 ARR (submission deadline: May 25, 2026; commitment: August 2, 2026)
5	- Format: Long paper (8 pages + appendix)
6	- Track: LLM Agents
7	- Paper type: **Empirical analysis paper**（D039 pivot: 从 method paper 转 empirical study）
8	- Fallback: ACL 2026 ARR August cycle (~August 15 deadline)
9	
10	## Core Claims (3 条) — D039 Pivot
11	
12	1. **Stagnation Signals Are Structural, Not Semantic (primary contribution)**: 系统性对比发现 agent stagnation 信号本质是结构性的——30 个结构特征（命令重复率、唯一命令比、文件 diff 频率等）在 in-domain (RF 0.9951) 和 cross-agent (GB 0.967) 都近完美预测停滞，全面优于 NL embedding probe (in-domain 0.906, cross-domain 0.751) 和 LLM-as-judge (+24.3pp)。Encoder-agnostic（3 个 encoder 均 >0.90）；最优窗口 k=5 (0.9309)；data scaling 10%→100% 单调递增。这揭示：(a) stagnation detection 不需要语义理解——简单结构特征已足够；(b) 结构特征天然跨 agent 迁移（不依赖 embedding domain adaptation）；(c) NL embedding 对 stagnation detection 无增量价值。**改变社区对 agent monitoring 方法选型的认知：从昂贵的表示学习转向轻量结构监控。** Gold set 验证 structural features 是否检测到真实 stagnation（非仅 circular eval artifact）是论文成立的关键。
13	
14	2. **LF Temporal Dynamics Are Systematic but Agent-Specific (analytical contribution)**: LFs 在 trajectory 上展现**系统性但 agent-specific 的**时序角色。SWE-Agent 上：cmd_rep leading (-1.87步)、file_diff concurrent (-1.2步)、OB lagging (+6.7步)。**OH 上 cmd_rep 角色反转**（从 leading 变 lagging +3.32步），而 file_diff（leading, -4.9步）和 OB（lagging, +18.1步）跨域一致。**消融验证：去掉 cmd_rep 后 OH F1 从 0.7512 飙升到 0.9272（+17.6pp）**，证明 cmd_rep 在 OH 上是噪声源而非信号。根因：cmd_rep 在 OH 上 92.3% firing rate + 71% FP，失去区分性。这揭示 LF 行为与 agent 架构之间的交互效应——为 weak supervision pipeline 在 sequential agent data 上的设计提供实证指导。同时量化 circular evaluation 问题：structural features 以 0.9951 F1 逆向工程 LF 标签，证明 LF-derived labels 上的高分不等于真实检测能力。
15	
16	3. **Temporal Label Model: A Well-Motivated Negative Finding (D039 negative result)**: 标准 data programming（majority vote）在 agent trajectory 上违反 i.i.d. 假设——LFs 产生系统性时序动态，这 motivate 了 temporal label model（TLM）的开发。然而，三种 TLM 实现**均未能超越简单 MV**：(a) **TWV（时序加权投票）**：绝大多数 σ 下有害（twv-ablation）；唯一微弱正向的 σ=2 训练的下游分类器全面劣化（in-domain -4.9pp, cross-agent -21.7pp, conf≥2 -1.8pp）(structural-on-twv)；(b) **HMM-TLM**：stagnation class overpredict；(c) **Lag-aware HMM**：仅追平 MV（0.8936）。**结论**：在当前 3-LF、低冲突（conf≥2 一致率 95.1%）的 regime 下，temporal alignment 的收益被噪声引入抵消。TWV 改变的主要是低置信标签，但改变方向是错的。这是对 "i.i.d. violation → temporal model must help" 这一直觉的重要否定，为未来 temporal label model 研究提供了关键约束条件。
17	
18	## Story Spine
19	
20	- **Problem**: LLM agents 在长期任务中频繁"语义停滞"——执行看似合理但集体无效的动作序列。每个动作可能非重复、局部合理，但整个窗口缺乏 goal-directed progress。现有方法要么检测结构性循环（漏掉语义多样的停滞），要么做 step-level scoring（丢失窗口内的时序动态），要么依赖 LLM 自我评估（高开销 + 受困模型的判断力受限）。
21	
22	- **Existing approaches & gaps**: (a) Cycle detectors（CDCS+CDSA, SpecRA, TrajAD）捕获重复/异常但漏掉语义多样的停滞；(b) Process Reward Models — **AgentPRM (Xi et al., ACM Web 2026, arxiv 2511.08325)** 是最直接的竞争者：用 TD/GAE 训练 step-level PRM 评估 "promise and progress"，但需要 outcome labels + RL pipeline，是 training signal 而非 monitoring tool。另有 PRM framework (arxiv 2502.10325)、ToolPRMBench (arxiv 2601.12294)、trajectory-level reward modeling (arxiv 2604.08178)。PRM 方向在 2025-2026 非常拥挤，我们的差异：**不需要 outcome labels**、**window-level 捕获 temporal dynamics**、**monitoring 而非 training**；(c) Self-reflection（Reflexion, LATS, Tree of Thoughts）依赖被困模型的自我评估，且是 intervention 而非 monitoring；(d) RL value functions (CodeRL) 需要 reward shaping；(e) **Agent monitoring 新方向**："Monitoring LLM Agents for Sequentially Contextual Harm" (ICLR 2025 Workshop) 论证了 sequence-level monitoring 的必要性（单步分析不够）；"Reliable Weak-to-Strong Monitoring" (arxiv 2508.19461) 研究了弱模型监控强 agent，但关注 safety 而非 progress；(f) **Agent degradation benchmark**：SlopCodeBench (arxiv 2603.24755, 2026) 量化了 coding agent 在长期任务中的退化——verbosity 90% 轨迹上升、erosion 80%——为我们的 problem motivation 提供了最新实证。
23	
24	- **Our framing (D039 Pivot)**: Progress stagnation detection 的系统性实证研究。**三层贡献**：(1) **Structural Signal Discovery (primary)** — 系统性对比揭示 stagnation 信号本质是结构性的（结构特征 in-domain 0.9951, cross-domain 0.967），NL embedding 和 LLM-as-judge 均无增量——改变社区对 agent monitoring 方法选型的认知，从表示学习转向轻量结构监控；(2) **LF Temporal Dynamics Analysis** — 量化 LFs 在 agent trajectory 上的时序角色 + 跨 agent 迁移分析 + circular evaluation 问题的方法论贡献——为 sequential data 上的 weak supervision 提供实证指导；(3) **TLM Negative Finding** — 系统性测试三种 temporal label model 实现，均未超越 MV，提供重要的负面结果和 failure analysis——约束未来研究方向。
25	
26	- **Headline result template**: "We present a systematic empirical study of progress stagnation detection in LLM agents through weak supervision. Our central finding is that stagnation signals are fundamentally structural: simple features (command repetition ratio, file diff frequency) achieve 0.995 in-domain and 0.967 cross-agent F1, decisively surpassing both neural embedding approaches (0.906/0.751) and LLM-as-judge baselines. We further discover that labeling functions exhibit systematic temporal dynamics — command_repetition leads stagnation onset by ~1.87 steps while outcome_backpropagation lags by +6.7 steps — but these temporal roles are agent-specific (cmd_rep reverses from leading to lagging on OpenHands; removing it improves OH F1 by +17.6pp). Despite these well-characterized temporal patterns motivating a temporal label model, three implementations (TWV, HMM, lag-aware HMM) all fail to improve over simple majority vote — with TWV labels actually degrading downstream classifiers by up to 21.7pp. This negative finding reveals that in the low-conflict regime of current LF frameworks, temporal alignment introduces more noise than signal. Our results redirect agent monitoring from expensive representation learning and complex label models toward lightweight structural approaches."
27	
28	## Venue Fit Risks
29	
30	- **EMNLP vs ICSE**: 核心 LFs 和数据 100% 来自 SE 领域。贴合 NLP venue 的策略：(a) weak supervision on sequential data 是通用方法论，适用于任何有时序结构的标注场景——data programming / Snorkel 出自 NLP 社区；(b) structural vs semantic signal 的发现对任何 agent monitoring 系统有指导意义；(c) circular evaluation 问题是 weak supervision 评估的通用挑战；(d) TLM negative finding 对 sequential label model 研究有方法论价值。
31	- **Reviewer lottery**: 遇到 SE-skeptical 的 NLP reviewer 可能被判 "more suitable for ICSE/FSE"——通过强化方法论洞见的跨域普适性和 LLM agent 社区的 NLP 属性来降低风险。
32	- **"Negative finding paper 不够 novel"**: 论文不是纯 negative finding——structural signal discovery (Claim 1) 是强正面结果；TLM negative finding (Claim 3) 附带详细 failure analysis 和对未来研究的约束条件。EMNLP 接受 analysis paper 和 well-motivated negative results。
33	- **vs PRMs（2025-2026 最拥挤的方向）**: Related Work 加专门小节。核心定位差异：PRM 需要 outcome labels + RL pipeline（昂贵），我们是 monitoring tool + weak supervision pipeline（轻量）；PRM 是 step-level training signal，我们是 window-level detection。
34	- **"Why not LLM-as-judge?"**: 已有 baseline 对比——structural approach <5ms inference vs LLM 高开销，且 structural +24.3pp。
35	
36	## Anticipated Reviewer Concerns & Countermeasures
37	
38	| Concern | 应对 |
39	|---------|------|
40	| Circular evaluation（训练和评估都在自动标签上） | 多层防御：(1) 明确声明 F1 = LF consensus fidelity；(2) structural baseline 0.9951 量化 circularity 上界（逆向工程 LF 规则）；(3) Cross-domain OH 是 non-circular 评估；(4) **Gold set 人工标注**（650 窗口，关键路径） |
41	| Structural features outperform everything — so what's the point of the probe? | 诚实报告 + 解读：structural features 在 LF-derived labels 上的 0.9951 是 circularity 上界（features ≈ LF inputs, labels = LF outputs）。Probe 的独立价值在 non-circular 维度：real-time inference、end-to-end deployment、gold set 上的对比。Gold set 是最终裁判 |
42	| TLM negative finding 不够有 contribution | Failure analysis 详细到足以约束未来研究：(1) 3-LF 低冲突 regime（conf≥2 一致率 95.1%）限制了 temporal alignment 的改进空间；(2) TWV 在低置信区改变标签方向错误；(3) 三种不同实现排除了实现偏差。论文同时有强正面结果（Claim 1, 2） |
43	| 跨 agent 迁移只测了两个 SE agent | Two-agent scope 在 Limitations 讨论 + structural features 跨域 0.967 的强迁移证据。Future work 包含 non-SE agents |
44	| 为什么不直接用 LLM | LLM-as-judge baseline 已对比：structural RF +33.3pp、probe +24.3pp vs LLM、<5ms vs LLM 高开销 |
45	| outcome_backpropagation 信息泄露 | 3-seed holdout：移除 OB 后 f1_stag=0.641±0.034（-22pp），7.1pp 为纯信号贡献。OB 作为 "Privileged Distant Supervision"，在 3-LF 框架中不可替代 |
46	| Probe 只学了 LF 启发式 | LF oracle baseline（All-Agreement 0.854, probe +5.1pp）+ 错误分析（FP 65% = LF 未覆盖的语义多样停滞）+ gold set 最终验证 |
47	| Architecture novelty 不足 | 论文定位为 empirical analysis paper，novelty 在发现和方法论洞见，不在架构 |
48	| "Semantic stagnation" rebrands existing concepts | 明确映射到现有 agent failure mode taxonomy + window-level formulation 的特殊性论证 |
49	| Related work incomplete | 扩展到 30+ references：PRMs / agent self-reflection / weak supervision / agent degradation benchmarks |
50	| Embedding model unspecified | 具名 Qwen3-Embedding-0.6B + encoder ablation（BGE/E5/GTE，三者均 >0.90） |
51	| LF hold-one-out ablation 解读 | **禁止 "去掉 X 后 F1 更高" 的 claim**（test set 偏移假象）。正确框架：覆盖率贡献 + 跨集泛化 + 标签一致性 |
52	| Structural data scaling 不能表述为 "robustness to data scarcity" | Circular eval 框架下正确解读：结构特征 ≈ LF 输入，10% 数据即可学会 LF→label 映射（RF 0.991）。这是 LF 重建的简单性证据，不是检测鲁棒性。论文呈现时标注 $^\dagger$ circular caveat，与 probe 的 data scaling（0.805→0.906，真正的学习曲线）对比呈现 |
53	| OB 移除后 f1_stag 数字来源 | ✅ **已闭环**：outcome-bp-3seed 3-seed mean f1_stag=0.641±0.034（seeds 42/123/456: 0.600/0.640/0.683）。"0.000" 来源已溯清：woob 模型在 OB-only 窗口子集（687w）上全预测 progress 导致子集 f1_stag=0.000，非完整测试集结果。D025/D026 已正确撤回。 |
54	
55	## D039 Pivot 变更记录
56	- D034 → D039: Claim 1 TLM（原"论文最强 claim"）降级为 Claim 3 negative finding
57	- D034 → D039: Claim 2 structural signal 升级为 Claim 1 primary contribution
58	- D034 → D039: Claim 3 LF temporal → Claim 2，加入 circular eval methodology
59	- D039 新增: TLM 三种实现全败的 failure analysis 作为独立贡献
60	- D039 触发实验: structural-on-twv (TWV labels degrade downstream -4.9pp ~ -21.7pp) + twv-ablation (TWV harmful for most σ) + temporal-label-model (HMM/lag-aware HMM failed)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "059c779a-907d-4b71-9391-7cbebd1ea50b"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Running ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 79505,
    "tool_uses": 27,
    "duration_ms": 48528
  },
  "last_tool_name": "Bash",
  "uuid": "6e7b9912-5ce3-431b-ac0d-9beb7c407755",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 88_

<details open><summary>🔧 Tool call — Bash · `toolu_01KrsoKzTWdZ3G8rzsHXKqou`</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/*.py | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "a70b45a5-e493-49a5-b446-278b136fe9d2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FwHrzAieFdSm6hFpmeZzKq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 4843,
      "cache_read_input_tokens": 74429,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4843,
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

_source line 89 · 2026-05-14T22:41:00.783Z_

<details><summary>↩ Tool result · `toolu_01KrsoKzTWdZ3G8rzsHXKqou`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu  18K May 14 10:30 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/baseline_llm_judge.py
-rw-r--r-- 1 ubuntu ubuntu 5.8K May 14 09:46 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/baseline_meanpool_lr.py
-rw-r--r-- 1 ubuntu ubuntu 5.6K May 14 08:41 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/baselines.py
-rw-r--r-- 1 ubuntu ubuntu 9.7K May 14 06:23 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/data_loader.py
-rw-r--r-- 1 ubuntu ubuntu 7.8K May 14 14:16 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/data_scaling.py
-rw-r--r-- 1 ubuntu ubuntu 1.4K May 14 05:45 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/download_5k.py
-rw-r--r-- 1 ubuntu ubuntu 6.8K May 14 07:20 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/evaluate.py
-rw-r--r-- 1 ubuntu ubuntu  14K May 14 14:01 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/fewshot_probe.py
-rw-r--r-- 1 ubuntu ubuntu 8.4K May 14 06:33 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/generate_embeddings.py
-rw-r--r-- 1 ubuntu ubuntu  17K May 14 05:43 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/label_quality_check.py
-rw-r--r-- 1 ubuntu ubuntu  16K May 14 06:01 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/label_quality_check_v2.py
-rw-r--r-- 1 ubuntu ubuntu 5.5K May 14 05:45 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/labeling_functions.py
-rw-r--r-- 1 ubuntu ubuntu  20K May 14 06:08 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/lf_conflict_analysis.py
-rw-r--r-- 1 ubuntu ubuntu 7.0K May 14 08:23 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/lf_oracle_baseline.py
-rw-r--r-- 1 ubuntu ubuntu  17K May 14 16:02 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/non_nlp_baseline.py
-rw-r--r-- 1 ubuntu ubuntu  16K May 14 15:09 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/oh_cmdrep_ablation.py
-rw-r--r-- 1 ubuntu ubuntu  13K May 14 15:06 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/oh_full_finetune.py
-rw-r--r-- 1 ubuntu ubuntu 5.2K May 14 05:45 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/probe_model.py
-rw-r--r-- 1 ubuntu ubuntu  16K May 14 16:22 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/train_architecture_ablation.py
-rw-r--r-- 1 ubuntu ubuntu 8.0K May 14 07:19 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/train_probe.py
-rw-r--r-- 1 ubuntu ubuntu  18K May 14 16:16 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/train_supcon.py
-rw-r--r-- 1 ubuntu ubuntu  15K May 14 06:30 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/window_extractor.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "bb113f32-cba6-4276-9eb7-489ad2ffcd51"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Reading artifacts/train_supcon.py",
  "usage": {
    "total_tokens": 80971,
    "tool_uses": 28,
    "duration_ms": 49994
  },
  "last_tool_name": "Read",
  "uuid": "5c93a16e-8776-44ae-b6ed-ed1058823b1f",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 91_

<details open><summary>🔧 Tool call — Read · `toolu_01WfxCo1z1VqDjnKt6zSEpLT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/train_supcon.py",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "7da009c4-9236-47b0-b547-dfbde8362b5d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0165VX36cPtJ5v4dG18q6yEu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 79272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1460,
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

_source line 92 · 2026-05-14T22:41:02.191Z_

<details><summary>↩ Tool result · `toolu_01WfxCo1z1VqDjnKt6zSEpLT`</summary>

```text
1	#!/usr/bin/env python3
2	"""Train GRU probe with Supervised Contrastive Loss auxiliary objective.
3	
4	Total loss = BCE_loss + lambda * SupCon_loss
5	SupCon applied on GRU last-layer hidden state (before classifier).
6	"""
7	
8	import argparse
9	import json
10	import random
11	import sys
12	from pathlib import Path
13	
14	import numpy as np
15	import torch
16	import torch.nn as nn
17	import torch.nn.functional as F
18	from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
19	from torch.utils.data import DataLoader
20	
21	sys.path.insert(0, str(Path(__file__).parent))
22	from probe_model import ProgressProbe, WindowDataset, collate_fn, split_by_instance
23	
24	
25	class SupConLoss(nn.Module):
26	    """Supervised Contrastive Loss (Khosla et al., 2020).
27	
28	    Pulls same-class representations together, pushes different-class apart.
29	    """
30	
31	    def __init__(self, temperature: float = 0.07):
32	        super().__init__()
33	        self.temperature = temperature
34	
35	    def forward(self, features: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
36	        """
37	        Args:
38	            features: (batch, hidden_dim) - will be L2-normalized internally
39	            labels: (batch,) - binary labels {0, 1}
40	        Returns:
41	            scalar loss
42	        """
43	        device = features.device
44	        batch_size = features.shape[0]
45	        if batch_size <= 1:
46	            return torch.tensor(0.0, device=device, requires_grad=True)
47	
48	        features = F.normalize(features, dim=1)
49	        similarity = torch.mm(features, features.t()) / self.temperature
50	
51	        # Mask: 1 where labels match (positive pairs), 0 on diagonal
52	        labels = labels.view(-1, 1)
53	        mask = torch.eq(labels, labels.t()).float().to(device)
54	        mask.fill_diagonal_(0)
55	
56	        # Check we have at least one positive pair
57	        if mask.sum() == 0:
58	            return torch.tensor(0.0, device=device, requires_grad=True)
59	
60	        # For numerical stability, subtract max from logits
61	        logits_max, _ = similarity.max(dim=1, keepdim=True)
62	        logits = similarity - logits_max.detach()
63	
64	        # Exclude self-contrast
65	        logits_mask = torch.ones_like(mask)
66	        logits_mask.fill_diagonal_(0)
67	
68	        # exp(sim) for all pairs except self
69	        exp_logits = torch.exp(logits) * logits_mask
70	        log_prob = logits - torch.log(exp_logits.sum(dim=1, keepdim=True) + 1e-12)
71	
72	        # Mean log-probability over positive pairs
73	        mean_log_prob = (mask * log_prob).sum(dim=1) / (mask.sum(dim=1) + 1e-12)
74	        loss = -mean_log_prob.mean()
75	        return loss
76	
77	
78	def forward_with_hidden(model: ProgressProbe, x: torch.Tensor, lengths: torch.Tensor = None):
79	    """Get both logits and hidden state from ProgressProbe."""
80	    if lengths is not None:
81	        x = nn.utils.rnn.pack_padded_sequence(x, lengths.cpu(), batch_first=True, enforce_sorted=False)
82	    _, hidden = model.gru(x)
83	    h = hidden[-1]  # (batch, hidden_size)
84	    logits = model.classifier(h).squeeze(-1)
85	    return logits, h
86	
87	
88	def set_seed(seed: int):
89	    random.seed(seed)
90	    np.random.seed(seed)
91	    torch.manual_seed(seed)
92	    if torch.cuda.is_available():
93	        torch.cuda.manual_seed_all(seed)
94	
95	
96	def compute_metrics(labels: list[int], preds: list[int]) -> dict:
97	    return {
98	        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
99	        "accuracy": accuracy_score(labels, preds),
100	        "precision_macro": precision_score(labels, preds, average="macro", zero_division=0),
101	        "recall_macro": recall_score(labels, preds, average="macro", zero_division=0),
102	        "f1_stagnation": f1_score(labels, preds, pos_label=0, zero_division=0),
103	        "f1_progress": f1_score(labels, preds, pos_label=1, zero_division=0),
104	    }
105	
106	
107	class EarlyStopping:
108	    def __init__(self, patience: int = 5):
109	        self.patience = patience
110	        self.counter = 0
111	        self.best_score = None
112	        self.should_stop = False
113	
114	    def step(self, score: float) -> bool:
115	        if self.best_score is None or score > self.best_score:
116	            self.best_score = score
117	            self.counter = 0
118	            return True
119	        self.counter += 1
120	        if self.counter >= self.patience:
121	            self.should_stop = True
122	        return False
123	
124	
125	@torch.no_grad()
126	def evaluate_epoch(model: nn.Module, loader: DataLoader, device: str) -> dict:
127	    model.eval()
128	    all_labels, all_preds = [], []
129	    for padded, labels, lengths in loader:
130	        logits, _ = forward_with_hidden(model, padded.to(device), lengths)
131	        preds = (torch.sigmoid(logits) >= 0.5).long().cpu()
132	        all_labels.extend(labels.long().tolist())
133	        all_preds.extend(preds.tolist())
134	    return compute_metrics(all_labels, all_preds)
135	
136	
137	@torch.no_grad()
138	def compute_separability(model: nn.Module, loader: DataLoader, device: str) -> dict:
139	    """Compute inter-class / intra-class cosine distance ratio on hidden states."""
140	    model.eval()
141	    all_h, all_labels = [], []
142	    for padded, labels, lengths in loader:
143	        _, h = forward_with_hidden(model, padded.to(device), lengths)
144	        all_h.append(h.cpu())
145	        all_labels.append(labels)
146	
147	    all_h = F.normalize(torch.cat(all_h, dim=0), dim=1)
148	    all_labels = torch.cat(all_labels, dim=0)
149	
150	    mask_0 = all_labels == 0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "cf8275fd-9a0d-4d5c-9c3e-e52289a2c7a9"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 83073,
    "tool_uses": 29,
    "duration_ms": 52350
  },
  "last_tool_name": "Bash",
  "uuid": "e2e25153-319b-4d6c-a87c-aa47b59c3ff0",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 94_

<details open><summary>🔧 Tool call — Bash · `toolu_018RgHRuSJJMcj2h77aiXr8s`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe -maxdepth 1 -name \"README*\" -o -name \"SETUP*\" -o -name \"*.md\" | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "931d7269-bd52-48c5-8041-6ce6159d7b77",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R7aNVuSrawxmN6XPQmneqm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 2090,
      "cache_read_input_tokens": 80732,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2090,
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

_source line 95 · 2026-05-14T22:41:04.591Z_

<details><summary>↩ Tool result · `toolu_018RgHRuSJJMcj2h77aiXr8s`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/memory.md
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/report.md
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/ROADMAP.md
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "4f40f417-f336-42df-b9cd-e3fbfe920535"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Reading artifacts/lf_oracle_baseline.py",
  "usage": {
    "total_tokens": 83376,
    "tool_uses": 30,
    "duration_ms": 54002
  },
  "last_tool_name": "Read",
  "uuid": "1801baee-24ae-40f1-a2b7-eb9b8deeb9f8",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 97_

<details open><summary>🔧 Tool call — Read · `toolu_01TQeVYPTnbqoMZuFrxGuc9i`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/lf_oracle_baseline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "54622fa4-7318-4b15-b172-add565039227",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EE7jQZR8NQxkbSQSLtPDJZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 293,
      "cache_read_input_tokens": 82822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 293,
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

_source line 98 · 2026-05-14T22:41:06.194Z_

<details><summary>↩ Tool result · `toolu_01TQeVYPTnbqoMZuFrxGuc9i`</summary>

```text
1	#!/usr/bin/env python3
2	"""LF Oracle Baseline — evaluate labeling function voting strategies without training.
3	
4	Applies various LF ensemble strategies on the same test split used by the GRU probe,
5	using raw LF outputs from windows_labeled.jsonl (no embeddings, no training).
6	
7	Input:
8	    --data_dir: directory containing data/windows_labeled.jsonl
9	    --split_info: path to checkpoints/split_info.json (from train_probe.py)
10	
11	Output:
12	    Markdown comparison table of LF baselines vs GRU probe (test_macro_f1=0.9055).
13	"""
14	
15	import argparse
16	import json
17	import sys
18	from collections import Counter
19	from pathlib import Path
20	
21	LF_NAMES = ["file_diff_delta", "command_repetition", "outcome_backpropagation"]
22	PROBE_REF_MACRO_F1 = 0.9055
23	
24	
25	def load_windows(path: str) -> list[dict]:
26	    """Load all windows from JSONL, preserving file order."""
27	    windows = []
28	    with open(path) as f:
29	        for line in f:
30	            line = line.strip()
31	            if line:
32	                windows.append(json.loads(line))
33	    return windows
34	
35	
36	def compute_prior(windows: list[dict]) -> float:
37	    """P(progress) from training set majority labels."""
38	    labels = [w["majority_label"] for w in windows]
39	    return sum(labels) / len(labels) if labels else 0.5
40	
41	
42	def predict_majority_vote(windows: list[dict], prior: float) -> list[int]:
43	    """Use majority_label directly. All test windows should be non-abstain after filtering."""
44	    fallback = 1 if prior >= 0.5 else 0
45	    return [w["majority_label"] if w["majority_label"] != -1 else fallback for w in windows]
46	
47	
48	def predict_any_stagnation(windows: list[dict], prior: float) -> list[int]:
49	    """Any LF votes stagnation(0) → predict stagnation."""
50	    fallback = 1 if prior >= 0.5 else 0
51	    preds = []
52	    for w in windows:
53	        vals = [w["labels"][lf] for lf in LF_NAMES]
54	        if 0 in vals:
55	            preds.append(0)
56	        elif any(v != -1 for v in vals):
57	            preds.append(1)
58	        else:
59	            preds.append(fallback)
60	    return preds
61	
62	
63	def predict_all_agreement(windows: list[dict], prior: float) -> list[int]:
64	    """Predict only when all non-abstain LFs agree; otherwise use prior."""
65	    fallback = 1 if prior >= 0.5 else 0
66	    preds = []
67	    for w in windows:
68	        active = [w["labels"][lf] for lf in LF_NAMES if w["labels"][lf] != -1]
69	        if active and len(set(active)) == 1:
70	            preds.append(active[0])
71	        else:
72	            preds.append(fallback)
73	    return preds
74	
75	
76	def predict_single_lf(windows: list[dict], lf_name: str, prior: float) -> list[int]:
77	    """Single LF as classifier; abstain → prior."""
78	    fallback = 1 if prior >= 0.5 else 0
79	    return [w["labels"][lf_name] if w["labels"][lf_name] != -1 else fallback for w in windows]
80	
81	
82	def print_table(results: list[tuple[str, dict]]):
83	    header = "| Method                      | Macro-F1 | Accuracy | Prec(M) | Rec(M) | F1(stag) | F1(prog) |"
84	    sep = "|" + "|".join(["-" * 30] + ["-" * 10] * 6) + "|"
85	    print(header)
86	    print(sep)
87	    for name, m in results:
88	        row = f"| {name:28s} |"
89	        for key in ["macro_f1", "accuracy", "precision_macro", "recall_macro", "f1_stagnation", "f1_progress"]:
90	            v = m.get(key)
91	            if v is None:
92	                row += "    —     |"
93	            else:
94	                row += f" {v:.4f}   |"
95	        print(row)
96	
97	
98	def main():
99	    parser = argparse.ArgumentParser(
100	        description="LF Oracle Baseline — evaluate LF voting strategies on test split"
101	    )
102	    parser.add_argument("--data_dir", required=True, help="Dir containing data/windows_labeled.jsonl")
103	    parser.add_argument("--split_info", required=True, help="Path to split_info.json")
104	    args = parser.parse_args()
105	
106	    sys.path.insert(0, str(Path(__file__).parent))
107	    from baselines import compute_metrics
108	
109	    # Load windows (same filtering as generate_embeddings.py)
110	    data_path = Path(args.data_dir) / "data" / "windows_labeled.jsonl"
111	    all_windows = load_windows(str(data_path))
112	    usable = [w for w in all_windows if w.get("majority_label", -1) != -1]
113	    print(f"Loaded {len(all_windows)} windows, {len(usable)} usable (non-abstain)")
114	
115	    with open(args.split_info) as f:
116	        split_info = json.load(f)
117	
118	    # Apply confidence filter (mirrors train_probe.py)
119	    keep_indices = split_info.get("keep_indices")
120	    if keep_indices is not None:
121	        min_conf = split_info.get("min_confidence", 0)
122	        print(f"Confidence filter (min_confidence={min_conf}): {len(keep_indices)}/{len(usable)} windows")
123	        windows = [usable[i] for i in keep_indices]
124	    else:
125	        windows = usable
126	
127	    train_idx = split_info["train_indices"]
128	    val_idx = split_info["val_indices"]
129	    test_idx = split_info["test_indices"]
130	
131	    train_windows = [windows[i] for i in train_idx]
132	    test_windows = [windows[i] for i in test_idx]
133	
134	    gt = [w["majority_label"] for w in test_windows]
135	    prior = compute_prior(train_windows)
136	
137	    print(f"Split — train: {len(train_idx)}, val: {len(val_idx)}, test: {len(test_idx)}")
138	    print(f"Prior P(progress) = {prior:.4f}")
139	    print(f"Test label distribution: {dict(Counter(gt))}")
140	    print()
141	
142	    results = []
143	
144	    # Reference row
145	    results.append(("GRU Probe (probe_001 ref)", {"macro_f1": PROBE_REF_MACRO_F1}))
146	
147	    # LF ensemble variants
148	    strategies = [
149	        ("LF Majority Vote", predict_majority_vote(test_windows, prior)),
150	        ("LF Any-Stagnation", predict_any_stagnation(test_windows, prior)),
151	        ("LF All-Agreement", predict_all_agreement(test_windows, prior)),
152	    ]
153	    for lf in LF_NAMES:
154	        strategies.append((f"Single LF: {lf}", predict_single_lf(test_windows, lf, prior)))
155	
156	    for name, preds in strategies:
157	        results.append((name, compute_metrics(gt, preds)))
158	
159	    # LF coverage stats
160	    print("=== LF Coverage on Test Set ===")
161	    for lf in LF_NAMES:
162	        n_active = sum(1 for w in test_windows if w["labels"][lf] != -1)
163	        n_total = len(test_windows)
164	        print(f"  {lf}: {n_active}/{n_total} ({n_active / n_total * 100:.1f}%)")
165	    n_all_agree = sum(
166	        1 for w in test_windows
167	        if len(set(v for v in [w["labels"][lf] for lf in LF_NAMES] if v != -1)) == 1
168	        and any(w["labels"][lf] != -1 for lf in LF_NAMES)
169	    )
170	    print(f"  All non-abstain agree: {n_all_agree}/{len(test_windows)} ({n_all_agree / len(test_windows) * 100:.1f}%)")
171	    print()
172	
173	    # Results table
174	    print("=== Results ===")
175	    print_table(results)
176	
177	    # Summary
178	    lf_results = results[1:]
179	    best_name, best_m = max(lf_results, key=lambda x: x[1]["macro_f1"])
180	    print(f"\nBest LF baseline: {best_name} (Macro-F1={best_m['macro_f1']:.4f})")
181	    delta = PROBE_REF_MACRO_F1 - best_m["macro_f1"]
182	    print(f"GRU Probe vs best LF: {delta:+.4f}")
183	
184	    # Save JSON results
185	    output_path = Path(args.data_dir) / "lf_oracle_results.json"
186	    json_results = {}
187	    for name, m in results:
188	        json_results[name] = {k: round(v, 4) if v is not None else None for k, v in m.items()}
189	    with open(output_path, "w") as f:
190	        json.dump(json_results, f, indent=2)
191	    print(f"\nResults saved to {output_path}")
192	
193	
194	if __name__ == "__main__":
195	    main()
196	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "3669f089-952d-4dde-8a5a-fedfc66e9439"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Running head -50 /home/ubuntu/.agent-ml-research-idea_gen…",
  "usage": {
    "total_tokens": 86352,
    "tool_uses": 31,
    "duration_ms": 56777
  },
  "last_tool_name": "Bash",
  "uuid": "bfb6199f-888d-43af-aa57-561cad1df999",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 100_

<details open><summary>🔧 Tool call — Bash · `toolu_01AkyBnj9JK5abt3oQnvXToZ`</summary>

```json
{
  "command": "head -50 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/data/windows_labeled.jsonl | python3 -m json.tool | head -60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "06675b0a-2fd7-4fff-a958-1b55b989e2ab",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MicJMk5CKuiXMqXkyttfT3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 2974,
      "cache_read_input_tokens": 83115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2974,
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

_source line 101 · 2026-05-14T22:41:09.083Z_

<details><summary>↩ Tool result · `toolu_01AkyBnj9JK5abt3oQnvXToZ`</summary>

```text
Extra data: line 2 column 1 (char 385)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "fb325865-6564-411b-a021-3e89f7e58f99"
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
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "description": "Running head -2 /home/ubuntu/.agent-ml-research-idea_gen_…",
  "usage": {
    "total_tokens": 86675,
    "tool_uses": 32,
    "duration_ms": 58431
  },
  "last_tool_name": "Bash",
  "uuid": "3c492e50-bdb4-4a8a-9d7c-f591f1341544",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool call

_source line 103_

<details open><summary>🔧 Tool call — Bash · `toolu_01K3KeWL6r8jUmQ7QM55jT2U`</summary>

```json
{
  "command": "head -2 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/data/windows_labeled.jsonl | tail -1 | python3 -m json.tool"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "d115735d-892e-4a9c-8bf3-9e6a43831f2b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YNhKquDWpLo4di6yvVhzXR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 258,
      "cache_read_input_tokens": 86089,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 258,
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

_source line 104 · 2026-05-14T22:41:10.728Z_

<details><summary>↩ Tool result · `toolu_01K3KeWL6r8jUmQ7QM55jT2U`</summary>

```text
{
    "trajectory_id": "Azure__azure-functions-python-worker-890__swe-agent-llama-70b__r0",
    "instance_id": "Azure__azure-functions-python-worker-890",
    "row_index": 0,
    "window_idx": 1,
    "step_indices": [
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15
    ],
    "short_trajectory": false,
    "labels": {
        "file_diff_delta": -1,
        "command_repetition": 1,
        "outcome_backpropagation": -1
    },
    "majority_label": 1,
    "confidence": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "1ac1ff58-3d6d-4a22-a0a0-ec37be0c4fd4"
}
```

</details>

---


### System

_source line 105_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "af612741562296de2",
  "tool_use_id": "toolu_01VfW5EfnnaX5b9Xeuvm1upB",
  "status": "completed",
  "output_file": "",
  "summary": "Explore project structure",
  "usage": {
    "total_tokens": 86989,
    "tool_uses": 32,
    "duration_ms": 102599
  },
  "uuid": "1738da7d-8d40-4e6c-bc71-67d553f7febf",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool result

_source line 106 · 2026-05-14T22:41:54.785Z_

<details><summary>↩ Tool result · `toolu_01VfW5EfnnaX5b9Xeuvm1upB`</summary>

````text
Perfect! Now I have all the information I need. Let me create a comprehensive summary.

## Comprehensive Exploration Summary: Agent Progress Probe Project

I've thoroughly explored the agent_progress_probe project. Here's a complete overview of the codebase architecture, data formats, and key components:

---

## 1. PROJECT STRUCTURE

**Root directory**: `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/`

**Key subdirectories**:
- **artifacts/**: All source code, data, and experiment scripts
  - `*.py`: 22 Python modules for models, training, evaluation, baselines
  - `data/`: JSONL data files and binary embeddings
  - Subdirectories for different experiments (probe_001, ablation-*, encoder-ablation-*, etc.)
- **checkpoints/**: JSON task status files for experiment tracking (500+ entries)
- **docs/, figures/**: Paper documentation and figure generation scripts
- **logs/**: Worker execution logs (100+ worker results)
- **task_context/**: Multi-agent system history and context

---

## 2. DATA FORMAT & FILES

**Main data files** (`artifacts/data/`):
- `swe_agent_trajectories_1000.jsonl` (69M): 1000 agent trajectories from SWE-bench
- `swe_agent_trajectories_5000.jsonl` (367M): 5000 trajectories
- `windows_labeled.jsonl` (21M): Labeled sliding windows (~350k+ windows)
  - Format per line: `{trajectory_id, instance_id, row_index, window_idx, step_indices, short_trajectory, labels{}, majority_label, confidence}`
  - Labels from 3 labeling functions + majority vote
  - Confidence: 1, 2, or 3 (agreement among LFs)
- `label_quality_details*.jsonl`: Quality analysis JSONLs

**Data structure details**:

**Step object** (in trajectories):
```python
{
  "role": "system|user|ai",  # system=prompt, user=environment observation, ai=agent action
  "text": str,               # actual step content
  "mask": bool,
  "cutoff_date": str (optional),
  "system_prompt": str (optional)
}
```

**Trajectory object**:
```python
{
  "instance_id": str,        # SWE-bench instance ID
  "model_name": str,         # agent model (e.g., "swe-agent-llama-70b")
  "target": bool,            # True=resolved, False=unresolved
  "trajectory": [steps],     # sequence of steps
  "exit_status": str,
  "generated_patch": str (optional),
  "eval_logs": str (optional),
  "row_index": int           # for unique trajectory identification
}
```

**Window object** (labeled):
```python
{
  "trajectory_id": f"{instance_id}__{model_name}__r{row_index}",
  "instance_id": str,
  "row_index": int,
  "window_idx": int,         # window position in trajectory
  "step_indices": [int, ...],# which steps this window spans
  "short_trajectory": bool,  # whether full trajectory < 12 steps
  "labels": {
    "file_diff_delta": int,              # -1/0/1 (abstain/stagnation/progress)
    "command_repetition": int,
    "outcome_backpropagation": int
  },
  "majority_label": int,     # -1/0/1 majority vote across LFs
  "confidence": int          # 1-3 (# of LFs agreeing with majority)
}
```

---

## 3. FEATURE EXTRACTION CODE

**File**: `artifacts/window_extractor.py`

**Key functions**:

1. **`extract_windows(trajectory)`**:
   - Sliding window extraction from trajectories
   - Window config: WINDOW_SIZE_PAIRS=5 (10 steps), STRIDE_PAIRS=2 (4 steps)
   - Skips system/issue steps, operates on interaction steps only
   - Short trajectories (<12 steps): single window with all steps
   - Long trajectories: slide by stride, capture partial tail windows (≥4 steps)
   - Returns list of dicts with window metadata and steps

2. **`label_windows(windows, trajectory)`**:
   - Applies all 3 labeling functions to each window
   - Computes majority vote + confidence (# of LFs agreeing)
   - Confidence values: 1 (minority), 2 (majority+1 agrees), 3 (unanimous)

3. **`process_trajectory(trajectory)`**:
   - Full pipeline: extract → label

4. **`run_pipeline(data_path, output_path, limit)`**:
   - Streaming pipeline over all trajectories
   - Statistics collection: LF coverage, agreement rates, label distribution by outcome

---

## 4. LABELING FUNCTIONS

**File**: `artifacts/labeling_functions.py`

**Three labeling functions**:

1. **`lf_file_diff_delta(window, trajectory, window_position)`**:
   - Signals **progress** if ≥2 edits with ≥1 unique file
   - Signals **stagnation** if ≥3 consecutive search/find commands with no edits
   - Otherwise **abstains**

2. **`lf_command_repetition(window, trajectory, window_position)`**:
   - Signals **stagnation** if 3+ consecutive commands identical OR >90% similar
   - Signals **progress** if all commands unique
   - Otherwise **abstains**

3. **`lf_outcome_backpropagation(window, trajectory, window_position)`**:
   - Only fires on last 2 windows
   - Signals **progress** if trajectory.target==True (resolved)
   - Signals **stagnation** if trajectory.target==False (unresolved)
   - Special: trajectory.exit_status=="exit_context" → always stagnation
   - Otherwise **abstains**

---

## 5. MODEL DEFINITIONS

**File**: `artifacts/probe_model.py`

**Architecture: ProgressProbe (2-layer GRU + attention)**

```python
class ProgressProbe(nn.Module):
    def __init__(
        self,
        embed_dim: int,            # embedding dimension (typically 1024)
        hidden_size: int = 256,    # GRU hidden state size
        num_layers: int = 2,       # 2-layer GRU
        dropout: float = 0.1       # dropout between layers
    )
    
    def forward(
        self,
        x: torch.Tensor,           # (batch, seq_len, embed_dim)
        lengths: torch.Tensor = None  # (batch,) actual sequence lengths
    ) -> torch.Tensor:
        # GRU with pack_padded_sequence for variable lengths
        # Output: (batch,) logits → apply sigmoid for [0,1] probability
```

**Training harness**: `artifacts/train_probe.py`
- Loss: BCEWithLogitsLoss with pos_weight (handles class imbalance)
- Optimizer: AdamW with weight_decay
- Early stopping on val macro-F1
- Data split: instance-level (all windows from same instance in same split)
- Confidence filtering: optional min_confidence filter (0 or 2)

**Inference**: Sigmoid threshold at 0.5 for binary classification

---

## 6. EMBEDDING GENERATION

**File**: `artifacts/generate_embeddings.py`

**Model**: Qwen3-Embedding-0.6B (768 embedding dim)
- Last-token pooling with attention mask awareness
- L2 normalization
- Batch processing with checkpoint recovery

**Output format** (saved as `embeddings.pt`):
```python
{
    "embeddings": list[torch.Tensor],  # per-window sequence of embeddings
    "labels": list[int],               # 0/1 labels (from windows_labeled.jsonl)
    "trajectory_ids": list[str],       # unique trajectory identifiers
    "instance_ids": list[str],         # SWE-bench instance IDs
    "step_indices_list": list[list[int]],  # step indices for each window
    "confidences": list[int],          # LF confidence (1-3)
    "embed_dim": int                   # 768 for Qwen3-Embedding-0.6B
}
```

---

## 7. SKLEARN CLASSIFIERS (STRUCTURAL FEATURES)

**File**: `artifacts/non_nlp_baseline.py`

**30 structural features** extracted from raw steps (no embeddings):

**Text length features** (5):
- mean_text_len, std_text_len, max_text_len, min_text_len, text_len_trend (linear regression slope)

**Action/observation statistics** (3):
- num_actions, num_observations, action_ratio

**Command features** (8):
- num_commands, mean_cmd_len, max_cmd_len, unique_cmd_ratio, max_repeat_ratio
- num_edit_cmds, num_search_cmds, num_nav_cmds, num_submit_cmds
- edit_ratio, search_ratio

**Command similarity** (3):
- avg_adjacent_cmd_similarity, max_adjacent_cmd_similarity, max_consecutive_similar (>=0.9 threshold)

**Content patterns** (4):
- num_errors (Traceback|Error regex), num_test_outputs (PASSED|FAILED), num_file_displays ([File: pattern), num_nonzero_exits

**Metadata** (1):
- is_short_trajectory (bool)

**Sklearn models**:
- LogisticRegression, RandomForestClassifier, GradientBoostingClassifier
- Trained on full train split, evaluated on test split
- StandardScaler normalization

---

## 8. BASELINES

**File**: `artifacts/baselines.py`

1. **RandomBaseline**: Samples from P(progress) = train label ratio
2. **MajorityBaseline**: Always predicts majority class
3. **CosineSimilarityBaseline**: Tuned on val set; predicts based on avg adjacent embedding cosine similarity
4. **Repeat3Baseline**: Heuristic — stagnation if last 3 commands identical

---

## 9. LLM-AS-JUDGE BASELINE

**File**: `artifacts/baseline_llm_judge.py`

**System prompt**: Expert at analyzing agent trajectories; classify progress vs stagnation

**Modes**:
- **zero-shot**: Direct classification with task description
- **few-shot**: 3 examples (1 progress high-conf, 1 stagnation high-conf, 1 boundary conf=2)

**API integration**:
- OpenRouter API (configurable model, default: claude-sonnet-4-6)
- Exponential backoff + retry logic
- Response parsing: JSON extraction with fallback keyword matching

**Output format**: `{"judgment": "progress"|"stagnation", "confidence": 1-5, "reasoning": str}`

**Caching**: Predictions cached to JSONL with hashing to avoid re-inference

---

## 10. EVALUATION CODE

**File**: `artifacts/evaluate.py`

**Pipeline**:
1. Load embeddings.pt (with optional confidence filtering)
2. Load best_model.pt checkpoint
3. Build test WindowDataset
4. Forward pass: compute logits, threshold at 0.5
5. Compute metrics: macro-F1, accuracy, precision/recall per class, F1(stagnation), F1(progress)
6. Run all baselines (train on train_bl, eval on test_bl)
7. Print comparison table

**Baseline data construction**: Rebuilds steps from trajectory index + step_indices to support Repeat3Baseline

---

## 11. GOLD SET EVALUATION

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/evaluate_gold_set.py`

**Purpose**: Evaluate models against human-annotated gold labels (non-circular evaluation)

**Models evaluated**:
1. GRU Probe (checkpoint: best_model.pt)
2. Structural RF (trained on-the-fly)
3. Structural GB (trained on-the-fly)
4. LF Majority Vote baseline
5. TWV (Temporally-Weighted Vote) labels

**Dry-run mode**: Generates pseudo-gold labels from conf≥2 MV labels

**Structural feature extraction**: 30 features (detailed in section 7)

---

## 12. DATA SPLITS

**Split strategy**: Instance-level (all windows from same instance in same split)

**Function**: `split_by_instance(instance_ids, train_ratio=0.7, val_ratio=0.15, seed=42)`

**Returns**: train_idx, val_idx, test_idx

**Saved metadata**: `split_info.json`
```python
{
    "train_indices": list[int],
    "val_indices": list[int],
    "test_indices": list[int],
    "seed": int,
    "embed_dim": int,
    "min_confidence": int (optional),
    "keep_indices": list[int] (optional, after filtering)
}
```

---

## 13. CONFIGURATION & CONSTANTS

**Window extraction** (`window_extractor.py`):
- WINDOW_SIZE_PAIRS = 5 (→ 10 steps)
- STRIDE_PAIRS = 2 (→ 4 steps)
- MIN_STEPS_FOR_WINDOW = 12

**Training defaults** (`train_probe.py` argparse):
- lr = 1e-3
- batch_size = 32
- epochs = 20
- hidden_size = 256
- num_layers = 2
- dropout = 0.1
- weight_decay = 0.01
- patience = 5 (early stopping)

**Data scaling experiment** (`data_scaling.py`):
- RATIOS = [0.10, 0.25, 0.50, 1.00]
- MIN_CONFIDENCE = 2 (for high-confidence subset)

---

## 14. KEY DATA FILES SUMMARY

| File | Size | Records | Format | Purpose |
|------|------|---------|--------|---------|
| swe_agent_trajectories_1000.jsonl | 69M | 1000 | JSONL | Base trajectories (1000 instances) |
| swe_agent_trajectories_5000.jsonl | 367M | 5000 | JSONL | Extended trajectories (5000 instances) |
| windows_labeled.jsonl | 21M | ~350k | JSONL (one per line) | Windows with LF labels |
| embeddings.pt | Variable | ~200k+ | PyTorch .pt | Window embeddings from Qwen3-0.6B |
| label_quality_details.jsonl | 85K | ~1500 | JSONL | Quality analysis metadata |
| label_quality_details_v2.jsonl | 140K | ~2000 | JSONL | Updated quality analysis |

---

## 15. KEY APIS & FUNCTION SIGNATURES

**Data loading**:
- `load_trajectories(path: str | Path) → list[Trajectory]`
- `load_trajectories_streaming(path: str | Path, limit: int) → Generator[Trajectory]`
- `load_windows(path: str) → dict` (window_id → window_dict)
- `build_trajectory_index(traj_path: str) → dict[int, list[dict]]`

**Embedding encoding**:
- `encode_texts(texts: list[str], model, tokenizer, batch_size, max_length, device) → torch.Tensor`

**Feature extraction**:
- `extract_structural_features(steps: list[dict], is_short: bool) → np.ndarray[30]`

**Metrics**:
- `compute_metrics(labels: list[int], preds: list[int]) → dict`
  - Returns: {macro_f1, accuracy, precision_macro, recall_macro, f1_stagnation, f1_progress}

---

## 16. EXPERIMENT TRACKING

Experiments tracked via JSON checkpoints in `checkpoints/`:
- Status tags: QUEUED, ALLOCATED, RUNNING, ANALYZING, DONE, ERROR
- Experiment naming: probe_001, ablation-supcon, baseline-llm-judge, cross-agent-structural, etc.

Worker logs in `logs/workers/` with pattern: `worker_{task}_{name}_{timestamp}_result.json`

---

## 17. RESEARCH CONTEXT (from memory.md & paper_framing.md)

**Paper claims**:
1. **Structural signals are fundamental**: 30 structural features achieve 0.9951 in-domain, 0.967 cross-domain F1 (vs probe 0.906 in-domain, 0.751 cross-domain)
2. **LF temporal dynamics are systematic but agent-specific**: Command repetition leads stagnation by ~1.87 steps on SWE-Agent but lags on OpenHands (+3.32 steps)
3. **Temporal Label Models fail**: Three TLM implementations (TWV, HMM, lag-aware HMM) don't improve over majority vote; TWV degrades cross-agent F1 by -21.7pp

**Key findings**:
- f1_stag bottleneck = recall_stag (precision 0.95, recall 0.77)
- LF agreement is quality signal (2-LF agreement f1_stag=0.9462 vs 3-LF 2v1 split f1_stag=0.7565)
- 85% of missed stagnation errors come from OB-vs-other LF splits
- "Circular evaluation": structural RF 0.9951 F1 proves LF labels ≈ LF feature inputs

---

## 18. DEPENDENCIES & TOOLS

**Python packages**:
- torch, transformers (for GRU probe & embedding generation)
- scikit-learn (for RF/GB/LR classifiers)
- numpy, scipy (numerical computation)
- openai/openrouter SDK (for LLM-as-judge)
- tqdm (progress bars)

**Models**:
- Qwen/Qwen3-Embedding-0.6B (embedding model, 768-dim)
- Claude Sonnet 4.6 (LLM-as-judge baseline)

---

This comprehensive exploration covers all core components, data formats, models, and evaluation infrastructure in the agent_progress_probe project. The system is a well-structured empirical study combining weak supervision (labeling functions), neural architectures (GRU probe), and classical ML (RF/GB on structural features) for detecting agent progress stagnation.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "3814cbce-e5c8-4a49-9c23-7c7f6ef6702f",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Explore the project at /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/ thoroughly. I need to understand:\n\n1. Full directory tree structure (especially src/, data/, artifacts/, models/)\n2. Feature extraction code in src/features/ - how structural features are extracted, what functions are available\n3. Model definitions in src/models/ - especially ProgressProbe (GRU+attention), how it's loaded and used for inference\n4. Data files in data/ - what's in windows_labeled.jsonl, embeddings.pt, any other data files\n5. Any existing evaluation code\n6. How sklearn classifiers (RF/GB/LR) are trained and saved - look for pickle files or training scripts\n7. LLM-as-judge code - how predictions are cached\n8. Any config files or constants\n\nBe very thorough - search across src/, data/, artifacts/, scripts/, and any other directories. Read key files fully to understand APIs and data formats.",
    "agentId": "af612741562296de2",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have all the information I need. Let me create a comprehensive summary.\n\n## Comprehensive Exploration Summary: Agent Progress Probe Project\n\nI've thoroughly explored the agent_progress_probe project. Here's a complete overview of the codebase architecture, data formats, and key components:\n\n---\n\n## 1. PROJECT STRUCTURE\n\n**Root directory**: `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/`\n\n**Key subdirectories**:\n- **artifacts/**: All source code, data, and experiment scripts\n  - `*.py`: 22 Python modules for models, training, evaluation, baselines\n  - `data/`: JSONL data files and binary embeddings\n  - Subdirectories for different experiments (probe_001, ablation-*, encoder-ablation-*, etc.)\n- **checkpoints/**: JSON task status files for experiment tracking (500+ entries)\n- **docs/, figures/**: Paper documentation and figure generation scripts\n- **logs/**: Worker execution logs (100+ worker results)\n- **task_context/**: Multi-agent system history and context\n\n---\n\n## 2. DATA FORMAT & FILES\n\n**Main data files** (`artifacts/data/`):\n- `swe_agent_trajectories_1000.jsonl` (69M): 1000 agent trajectories from SWE-bench\n- `swe_agent_trajectories_5000.jsonl` (367M): 5000 trajectories\n- `windows_labeled.jsonl` (21M): Labeled sliding windows (~350k+ windows)\n  - Format per line: `{trajectory_id, instance_id, row_index, window_idx, step_indices, short_trajectory, labels{}, majority_label, confidence}`\n  - Labels from 3 labeling functions + majority vote\n  - Confidence: 1, 2, or 3 (agreement among LFs)\n- `label_quality_details*.jsonl`: Quality analysis JSONLs\n\n**Data structure details**:\n\n**Step object** (in trajectories):\n```python\n{\n  \"role\": \"system|user|ai\",  # system=prompt, user=environment observation, ai=agent action\n  \"text\": str,               # actual step content\n  \"mask\": bool,\n  \"cutoff_date\": str (optional),\n  \"system_prompt\": str (optional)\n}\n```\n\n**Trajectory object**:\n```python\n{\n  \"instance_id\": str,        # SWE-bench instance ID\n  \"model_name\": str,         # agent model (e.g., \"swe-agent-llama-70b\")\n  \"target\": bool,            # True=resolved, False=unresolved\n  \"trajectory\": [steps],     # sequence of steps\n  \"exit_status\": str,\n  \"generated_patch\": str (optional),\n  \"eval_logs\": str (optional),\n  \"row_index\": int           # for unique trajectory identification\n}\n```\n\n**Window object** (labeled):\n```python\n{\n  \"trajectory_id\": f\"{instance_id}__{model_name}__r{row_index}\",\n  \"instance_id\": str,\n  \"row_index\": int,\n  \"window_idx\": int,         # window position in trajectory\n  \"step_indices\": [int, ...],# which steps this window spans\n  \"short_trajectory\": bool,  # whether full trajectory < 12 steps\n  \"labels\": {\n    \"file_diff_delta\": int,              # -1/0/1 (abstain/stagnation/progress)\n    \"command_repetition\": int,\n    \"outcome_backpropagation\": int\n  },\n  \"majority_label\": int,     # -1/0/1 majority vote across LFs\n  \"confidence\": int          # 1-3 (# of LFs agreeing with majority)\n}\n```\n\n---\n\n## 3. FEATURE EXTRACTION CODE\n\n**File**: `artifacts/window_extractor.py`\n\n**Key functions**:\n\n1. **`extract_windows(trajectory)`**:\n   - Sliding window extraction from trajectories\n   - Window config: WINDOW_SIZE_PAIRS=5 (10 steps), STRIDE_PAIRS=2 (4 steps)\n   - Skips system/issue steps, operates on interaction steps only\n   - Short trajectories (<12 steps): single window with all steps\n   - Long trajectories: slide by stride, capture partial tail windows (≥4 steps)\n   - Returns list of dicts with window metadata and steps\n\n2. **`label_windows(windows, trajectory)`**:\n   - Applies all 3 labeling functions to each window\n   - Computes majority vote + confidence (# of LFs agreeing)\n   - Confidence values: 1 (minority), 2 (majority+1 agrees), 3 (unanimous)\n\n3. **`process_trajectory(trajectory)`**:\n   - Full pipeline: extract → label\n\n4. **`run_pipeline(data_path, output_path, limit)`**:\n   - Streaming pipeline over all trajectories\n   - Statistics collection: LF coverage, agreement rates, label distribution by outcome\n\n---\n\n## 4. LABELING FUNCTIONS\n\n**File**: `artifacts/labeling_functions.py`\n\n**Three labeling functions**:\n\n1. **`lf_file_diff_delta(window, trajectory, window_position)`**:\n   - Signals **progress** if ≥2 edits with ≥1 unique file\n   - Signals **stagnation** if ≥3 consecutive search/find commands with no edits\n   - Otherwise **abstains**\n\n2. **`lf_command_repetition(window, trajectory, window_position)`**:\n   - Signals **stagnation** if 3+ consecutive commands identical OR >90% similar\n   - Signals **progress** if all commands unique\n   - Otherwise **abstains**\n\n3. **`lf_outcome_backpropagation(window, trajectory, window_position)`**:\n   - Only fires on last 2 windows\n   - Signals **progress** if trajectory.target==True (resolved)\n   - Signals **stagnation** if trajectory.target==False (unresolved)\n   - Special: trajectory.exit_status==\"exit_context\" → always stagnation\n   - Otherwise **abstains**\n\n---\n\n## 5. MODEL DEFINITIONS\n\n**File**: `artifacts/probe_model.py`\n\n**Architecture: ProgressProbe (2-layer GRU + attention)**\n\n```python\nclass ProgressProbe(nn.Module):\n    def __init__(\n        self,\n        embed_dim: int,            # embedding dimension (typically 1024)\n        hidden_size: int = 256,    # GRU hidden state size\n        num_layers: int = 2,       # 2-layer GRU\n        dropout: float = 0.1       # dropout between layers\n    )\n    \n    def forward(\n        self,\n        x: torch.Tensor,           # (batch, seq_len, embed_dim)\n        lengths: torch.Tensor = None  # (batch,) actual sequence lengths\n    ) -> torch.Tensor:\n        # GRU with pack_padded_sequence for variable lengths\n        # Output: (batch,) logits → apply sigmoid for [0,1] probability\n```\n\n**Training harness**: `artifacts/train_probe.py`\n- Loss: BCEWithLogitsLoss with pos_weight (handles class imbalance)\n- Optimizer: AdamW with weight_decay\n- Early stopping on val macro-F1\n- Data split: instance-level (all windows from same instance in same split)\n- Confidence filtering: optional min_confidence filter (0 or 2)\n\n**Inference**: Sigmoid threshold at 0.5 for binary classification\n\n---\n\n## 6. EMBEDDING GENERATION\n\n**File**: `artifacts/generate_embeddings.py`\n\n**Model**: Qwen3-Embedding-0.6B (768 embedding dim)\n- Last-token pooling with attention mask awareness\n- L2 normalization\n- Batch processing with checkpoint recovery\n\n**Output format** (saved as `embeddings.pt`):\n```python\n{\n    \"embeddings\": list[torch.Tensor],  # per-window sequence of embeddings\n    \"labels\": list[int],               # 0/1 labels (from windows_labeled.jsonl)\n    \"trajectory_ids\": list[str],       # unique trajectory identifiers\n    \"instance_ids\": list[str],         # SWE-bench instance IDs\n    \"step_indices_list\": list[list[int]],  # step indices for each window\n    \"confidences\": list[int],          # LF confidence (1-3)\n    \"embed_dim\": int                   # 768 for Qwen3-Embedding-0.6B\n}\n```\n\n---\n\n## 7. SKLEARN CLASSIFIERS (STRUCTURAL FEATURES)\n\n**File**: `artifacts/non_nlp_baseline.py`\n\n**30 structural features** extracted from raw steps (no embeddings):\n\n**Text length features** (5):\n- mean_text_len, std_text_len, max_text_len, min_text_len, text_len_trend (linear regression slope)\n\n**Action/observation statistics** (3):\n- num_actions, num_observations, action_ratio\n\n**Command features** (8):\n- num_commands, mean_cmd_len, max_cmd_len, unique_cmd_ratio, max_repeat_ratio\n- num_edit_cmds, num_search_cmds, num_nav_cmds, num_submit_cmds\n- edit_ratio, search_ratio\n\n**Command similarity** (3):\n- avg_adjacent_cmd_similarity, max_adjacent_cmd_similarity, max_consecutive_similar (>=0.9 threshold)\n\n**Content patterns** (4):\n- num_errors (Traceback|Error regex), num_test_outputs (PASSED|FAILED), num_file_displays ([File: pattern), num_nonzero_exits\n\n**Metadata** (1):\n- is_short_trajectory (bool)\n\n**Sklearn models**:\n- LogisticRegression, RandomForestClassifier, GradientBoostingClassifier\n- Trained on full train split, evaluated on test split\n- StandardScaler normalization\n\n---\n\n## 8. BASELINES\n\n**File**: `artifacts/baselines.py`\n\n1. **RandomBaseline**: Samples from P(progress) = train label ratio\n2. **MajorityBaseline**: Always predicts majority class\n3. **CosineSimilarityBaseline**: Tuned on val set; predicts based on avg adjacent embedding cosine similarity\n4. **Repeat3Baseline**: Heuristic — stagnation if last 3 commands identical\n\n---\n\n## 9. LLM-AS-JUDGE BASELINE\n\n**File**: `artifacts/baseline_llm_judge.py`\n\n**System prompt**: Expert at analyzing agent trajectories; classify progress vs stagnation\n\n**Modes**:\n- **zero-shot**: Direct classification with task description\n- **few-shot**: 3 examples (1 progress high-conf, 1 stagnation high-conf, 1 boundary conf=2)\n\n**API integration**:\n- OpenRouter API (configurable model, default: claude-sonnet-4-6)\n- Exponential backoff + retry logic\n- Response parsing: JSON extraction with fallback keyword matching\n\n**Output format**: `{\"judgment\": \"progress\"|\"stagnation\", \"confidence\": 1-5, \"reasoning\": str}`\n\n**Caching**: Predictions cached to JSONL with hashing to avoid re-inference\n\n---\n\n## 10. EVALUATION CODE\n\n**File**: `artifacts/evaluate.py`\n\n**Pipeline**:\n1. Load embeddings.pt (with optional confidence filtering)\n2. Load best_model.pt checkpoint\n3. Build test WindowDataset\n4. Forward pass: compute logits, threshold at 0.5\n5. Compute metrics: macro-F1, accuracy, precision/recall per class, F1(stagnation), F1(progress)\n6. Run all baselines (train on train_bl, eval on test_bl)\n7. Print comparison table\n\n**Baseline data construction**: Rebuilds steps from trajectory index + step_indices to support Repeat3Baseline\n\n---\n\n## 11. GOLD SET EVALUATION\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/evaluate_gold_set.py`\n\n**Purpose**: Evaluate models against human-annotated gold labels (non-circular evaluation)\n\n**Models evaluated**:\n1. GRU Probe (checkpoint: best_model.pt)\n2. Structural RF (trained on-the-fly)\n3. Structural GB (trained on-the-fly)\n4. LF Majority Vote baseline\n5. TWV (Temporally-Weighted Vote) labels\n\n**Dry-run mode**: Generates pseudo-gold labels from conf≥2 MV labels\n\n**Structural feature extraction**: 30 features (detailed in section 7)\n\n---\n\n## 12. DATA SPLITS\n\n**Split strategy**: Instance-level (all windows from same instance in same split)\n\n**Function**: `split_by_instance(instance_ids, train_ratio=0.7, val_ratio=0.15, seed=42)`\n\n**Returns**: train_idx, val_idx, test_idx\n\n**Saved metadata**: `split_info.json`\n```python\n{\n    \"train_indices\": list[int],\n    \"val_indices\": list[int],\n    \"test_indices\": list[int],\n    \"seed\": int,\n    \"embed_dim\": int,\n    \"min_confidence\": int (optional),\n    \"keep_indices\": list[int] (optional, after filtering)\n}\n```\n\n---\n\n## 13. CONFIGURATION & CONSTANTS\n\n**Window extraction** (`window_extractor.py`):\n- WINDOW_SIZE_PAIRS = 5 (→ 10 steps)\n- STRIDE_PAIRS = 2 (→ 4 steps)\n- MIN_STEPS_FOR_WINDOW = 12\n\n**Training defaults** (`train_probe.py` argparse):\n- lr = 1e-3\n- batch_size = 32\n- epochs = 20\n- hidden_size = 256\n- num_layers = 2\n- dropout = 0.1\n- weight_decay = 0.01\n- patience = 5 (early stopping)\n\n**Data scaling experiment** (`data_scaling.py`):\n- RATIOS = [0.10, 0.25, 0.50, 1.00]\n- MIN_CONFIDENCE = 2 (for high-confidence subset)\n\n---\n\n## 14. KEY DATA FILES SUMMARY\n\n| File | Size | Records | Format | Purpose |\n|------|------|---------|--------|---------|\n| swe_agent_trajectories_1000.jsonl | 69M | 1000 | JSONL | Base trajectories (1000 instances) |\n| swe_agent_trajectories_5000.jsonl | 367M | 5000 | JSONL | Extended trajectories (5000 instances) |\n| windows_labeled.jsonl | 21M | ~350k | JSONL (one per line) | Windows with LF labels |\n| embeddings.pt | Variable | ~200k+ | PyTorch .pt | Window embeddings from Qwen3-0.6B |\n| label_quality_details.jsonl | 85K | ~1500 | JSONL | Quality analysis metadata |\n| label_quality_details_v2.jsonl | 140K | ~2000 | JSONL | Updated quality analysis |\n\n---\n\n## 15. KEY APIS & FUNCTION SIGNATURES\n\n**Data loading**:\n- `load_trajectories(path: str | Path) → list[Trajectory]`\n- `load_trajectories_streaming(path: str | Path, limit: int) → Generator[Trajectory]`\n- `load_windows(path: str) → dict` (window_id → window_dict)\n- `build_trajectory_index(traj_path: str) → dict[int, list[dict]]`\n\n**Embedding encoding**:\n- `encode_texts(texts: list[str], model, tokenizer, batch_size, max_length, device) → torch.Tensor`\n\n**Feature extraction**:\n- `extract_structural_features(steps: list[dict], is_short: bool) → np.ndarray[30]`\n\n**Metrics**:\n- `compute_metrics(labels: list[int], preds: list[int]) → dict`\n  - Returns: {macro_f1, accuracy, precision_macro, recall_macro, f1_stagnation, f1_progress}\n\n---\n\n## 16. EXPERIMENT TRACKING\n\nExperiments tracked via JSON checkpoints in `checkpoints/`:\n- Status tags: QUEUED, ALLOCATED, RUNNING, ANALYZING, DONE, ERROR\n- Experiment naming: probe_001, ablation-supcon, baseline-llm-judge, cross-agent-structural, etc.\n\nWorker logs in `logs/workers/` with pattern: `worker_{task}_{name}_{timestamp}_result.json`\n\n---\n\n## 17. RESEARCH CONTEXT (from memory.md & paper_framing.md)\n\n**Paper claims**:\n1. **Structural signals are fundamental**: 30 structural features achieve 0.9951 in-domain, 0.967 cross-domain F1 (vs probe 0.906 in-domain, 0.751 cross-domain)\n2. **LF temporal dynamics are systematic but agent-specific**: Command repetition leads stagnation by ~1.87 steps on SWE-Agent but lags on OpenHands (+3.32 steps)\n3. **Temporal Label Models fail**: Three TLM implementations (TWV, HMM, lag-aware HMM) don't improve over majority vote; TWV degrades cross-agent F1 by -21.7pp\n\n**Key findings**:\n- f1_stag bottleneck = recall_stag (precision 0.95, recall 0.77)\n- LF agreement is quality signal (2-LF agreement f1_stag=0.9462 vs 3-LF 2v1 split f1_stag=0.7565)\n- 85% of missed stagnation errors come from OB-vs-other LF splits\n- \"Circular evaluation\": structural RF 0.9951 F1 proves LF labels ≈ LF feature inputs\n\n---\n\n## 18. DEPENDENCIES & TOOLS\n\n**Python packages**:\n- torch, transformers (for GRU probe & embedding generation)\n- scikit-learn (for RF/GB/LR classifiers)\n- numpy, scipy (numerical computation)\n- openai/openrouter SDK (for LLM-as-judge)\n- tqdm (progress bars)\n\n**Models**:\n- Qwen/Qwen3-Embedding-0.6B (embedding model, 768-dim)\n- Claude Sonnet 4.6 (LLM-as-judge baseline)\n\n---\n\nThis comprehensive exploration covers all core components, data formats, models, and evaluation infrastructure in the agent_progress_probe project. The system is a well-structured empirical study combining weak supervision (labeling functions), neural architectures (GRU probe), and classical ML (RF/GB on structural features) for detecting agent progress stagnation."
      }
    ],
    "totalDurationMs": 102603,
    "totalTokens": 91315,
    "totalToolUseCount": 32,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 86347,
      "output_tokens": 4655,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 313
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 4655,
          "cache_read_input_tokens": 86347,
          "cache_creation_input_tokens": 313,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 313,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 16,
      "searchCount": 0,
      "bashCount": 16,
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

_source line 107_

Now let me read the key source files I'll need to reuse.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "9ed1ed33-3037-4706-bf15-a4a1dff76df2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQEuLeTb7oxY5Br5A2utFx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5038,
      "cache_read_input_tokens": 23566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5038
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

_source line 108_

<details open><summary>🔧 Tool call — Read · `toolu_01P2taXTNwEYQSS7mT8uyBKG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/non_nlp_baseline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "42c380b2-0e1c-4497-8507-f5c79d6257d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQEuLeTb7oxY5Br5A2utFx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5038,
      "cache_read_input_tokens": 23566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5038
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

_source line 109 · 2026-05-14T22:41:58.228Z_

<details><summary>↩ Tool result · `toolu_01P2taXTNwEYQSS7mT8uyBKG`</summary>

````text
1	#!/usr/bin/env python3
2	"""Non-NLP baseline: structural/numerical features only.
3	
4	Extracts hand-crafted features from raw trajectory steps (no embeddings),
5	trains LogisticRegression, RandomForest, GradientBoosting.
6	Uses the same train/val/test split as probe_001.
7	"""
8	
9	import json
10	import re
11	import sys
12	import argparse
13	from collections import Counter
14	from difflib import SequenceMatcher
15	from pathlib import Path
16	
17	import numpy as np
18	from sklearn.linear_model import LogisticRegression
19	from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
20	from sklearn.preprocessing import StandardScaler
21	from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
22	
23	
24	def compute_metrics(labels, preds):
25	    return {
26	        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
27	        "accuracy": accuracy_score(labels, preds),
28	        "precision_macro": precision_score(labels, preds, average="macro", zero_division=0),
29	        "recall_macro": recall_score(labels, preds, average="macro", zero_division=0),
30	        "f1_stagnation": f1_score(labels, preds, pos_label=0, zero_division=0),
31	        "f1_progress": f1_score(labels, preds, pos_label=1, zero_division=0),
32	    }
33	
34	
35	def extract_command(text):
36	    match = re.search(r"```\n?(.*?)```", text, re.DOTALL)
37	    return match.group(1).strip() if match else None
38	
39	
40	EDIT_CMDS = {"edit", "str_replace", "create", "insert"}
41	SEARCH_CMDS = {"search_dir", "search_file", "find_file", "find", "grep", "view"}
42	NAV_CMDS = {"open", "goto", "scroll_down", "scroll_up", "cd", "ls", "cat"}
43	
44	
45	def cmd_similarity(a, b):
46	    if a == b:
47	        return 1.0
48	    if not a or not b:
49	        return 0.0
50	    return SequenceMatcher(None, a, b).ratio()
51	
52	
53	def extract_features(steps, is_short):
54	    """Extract structural features from a list of step dicts.
55	
56	    Each step dict has: role, text
57	    """
58	    n = len(steps)
59	    if n == 0:
60	        return np.zeros(30)
61	
62	    roles = [s["role"] for s in steps]
63	    texts = [s["text"] for s in steps]
64	    text_lens = [len(t) for t in texts]
65	
66	    actions = [(s, t) for s, t in zip(steps, texts) if s["role"] == "ai"]
67	    observations = [(s, t) for s, t in zip(steps, texts) if s["role"] == "user"]
68	
69	    n_actions = len(actions)
70	    n_obs = len(observations)
71	
72	    # --- text length features ---
73	    mean_tlen = np.mean(text_lens)
74	    std_tlen = np.std(text_lens) if n > 1 else 0.0
75	    max_tlen = max(text_lens)
76	    min_tlen = min(text_lens)
77	
78	    action_lens = [len(t) for _, t in actions] if actions else [0]
79	    obs_lens = [len(t) for _, t in observations] if observations else [0]
80	    mean_action_len = np.mean(action_lens)
81	    mean_obs_len = np.mean(obs_lens)
82	
83	    # text length trend (slope via simple linear regression)
84	    if n > 1:
85	        x = np.arange(n, dtype=float)
86	        y = np.array(text_lens, dtype=float)
87	        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (n * np.dot(x, x) - x.sum()**2 + 1e-9)
88	    else:
89	        slope = 0.0
90	
91	    # --- command features ---
92	    commands = []
93	    for s, t in actions:
94	        cmd = extract_command(t)
95	        if cmd:
96	            commands.append(cmd)
97	
98	    n_cmds = len(commands)
99	    cmd_lens = [len(c) for c in commands] if commands else [0]
100	    mean_cmd_len = np.mean(cmd_lens)
101	    max_cmd_len = max(cmd_lens) if cmd_lens else 0
102	
103	    if n_cmds > 0:
104	        unique_cmds = len(set(commands))
105	        unique_cmd_ratio = unique_cmds / n_cmds
106	        cmd_counter = Counter(commands)
107	        max_repeat = cmd_counter.most_common(1)[0][1]
108	        repeat_ratio = max_repeat / n_cmds
109	    else:
110	        unique_cmd_ratio = 1.0
111	        repeat_ratio = 0.0
112	
113	    # command type counts
114	    n_edit = 0
115	    n_search = 0
116	    n_nav = 0
117	    n_submit = 0
118	    for cmd in commands:
119	        first_word = cmd.strip().split()[0] if cmd.strip() else ""
120	        if first_word in EDIT_CMDS:
121	            n_edit += 1
122	        elif first_word in SEARCH_CMDS:
123	            n_search += 1
124	        elif first_word in NAV_CMDS:
125	            n_nav += 1
126	        elif first_word == "submit":
127	            n_submit += 1
128	
129	    edit_ratio = n_edit / max(n_cmds, 1)
130	    search_ratio = n_search / max(n_cmds, 1)
131	
132	    # adjacent command similarity
133	    if n_cmds >= 2:
134	        sims = [cmd_similarity(commands[i], commands[i+1]) for i in range(n_cmds - 1)]
135	        avg_adj_sim = np.mean(sims)
136	        max_adj_sim = max(sims)
137	        # max consecutive run with sim >= 0.9
138	        max_run = 1
139	        cur_run = 1
140	        for s in sims:
141	            if s >= 0.9:
142	                cur_run += 1
143	                max_run = max(max_run, cur_run)
144	            else:
145	                cur_run = 1
146	    else:
147	        avg_adj_sim = 0.0
148	        max_adj_sim = 0.0
149	        max_run = 0
150	
151	    # --- content pattern features ---
152	    n_errors = sum(1 for t in texts if "Traceback" in t or "Error" in t)
153	    n_test_output = sum(1 for t in texts if ("PASSED" in t or "FAILED" in t) and "test" in t.lower())
154	    n_file_display = sum(1 for t in texts if "[File:" in t)
155	
156	    # exit code patterns in observations (look for "exit code" or "$?" patterns)
157	    n_nonzero_exit = sum(1 for _, t in observations if re.search(r"exit code [1-9]|returned non-zero|command not found", t))
158	
159	    feature_vec = np.array([
160	        n,                    # 0: num_steps
161	        n_actions,            # 1: num_actions
162	        n_obs,                # 2: num_observations
163	        n_actions / max(n, 1),# 3: action_ratio
164	        mean_tlen,            # 4: mean_text_len
165	        std_tlen,             # 5: std_text_len
166	        max_tlen,             # 6: max_text_len
167	        min_tlen,             # 7: min_text_len
168	        mean_action_len,      # 8: mean_action_len
169	        mean_obs_len,         # 9: mean_obs_len
170	        slope,                # 10: text_len_trend
171	        n_cmds,               # 11: num_commands
172	        mean_cmd_len,         # 12: mean_cmd_len
173	        max_cmd_len,          # 13: max_cmd_len
174	        unique_cmd_ratio,     # 14: unique_cmd_ratio
175	        repeat_ratio,         # 15: max_repeat_ratio
176	        n_edit,               # 16: num_edit_cmds
177	        n_search,             # 17: num_search_cmds
178	        n_nav,                # 18: num_nav_cmds
179	        n_submit,             # 19: num_submit_cmds
180	        edit_ratio,           # 20: edit_ratio
181	        search_ratio,         # 21: search_ratio
182	        avg_adj_sim,          # 22: avg_adjacent_cmd_similarity
183	        max_adj_sim,          # 23: max_adjacent_cmd_similarity
184	        max_run,              # 24: max_consecutive_similar_cmds
185	        n_errors,             # 25: num_errors
186	        n_test_output,        # 26: num_test_outputs
187	        n_file_display,       # 27: num_file_displays
188	        n_nonzero_exit,       # 28: num_nonzero_exits
189	        float(is_short),      # 29: is_short_trajectory
190	    ], dtype=np.float32)
191	
192	    return feature_vec
193	
194	
195	FEATURE_NAMES = [
196	    "num_steps", "num_actions", "num_observations", "action_ratio",
197	    "mean_text_len", "std_text_len", "max_text_len", "min_text_len",
198	    "mean_action_len", "mean_obs_len", "text_len_trend",
199	    "num_commands", "mean_cmd_len", "max_cmd_len",
200	    "unique_cmd_ratio", "max_repeat_ratio",
201	    "num_edit_cmds", "num_search_cmds", "num_nav_cmds", "num_submit_cmds",
202	    "edit_ratio", "search_ratio",
203	    "avg_adjacent_cmd_sim", "max_adjacent_cmd_sim", "max_consecutive_similar",
204	    "num_errors", "num_test_outputs", "num_file_displays", "num_nonzero_exits",
205	    "is_short_trajectory",
206	]
207	
208	
209	def build_trajectory_index(traj_path):
210	    """row_index -> list of step dicts [{role, text}, ...]"""
211	    index = {}
212	    with open(traj_path) as f:
213	        for row_idx, line in enumerate(f):
214	            line = line.strip()
215	            if not line:
216	                continue
217	            raw = json.loads(line)
218	            steps = []
219	            for s in raw.get("trajectory") or []:
220	                steps.append({
221	                    "role": s.get("role", "unknown"),
222	                    "text": s.get("text") or s.get("system_prompt") or "",
223	                })
224	            index[row_idx] = steps
225	    return index
226	
227	
228	def load_windows(path):
229	    windows = []
230	    with open(path) as f:
231	        for line in f:
232	            line = line.strip()
233	            if line:
234	                windows.append(json.loads(line))
235	    return windows
236	
237	
238	def print_table(results):
239	    header = "| Method                      | Macro-F1 | Accuracy | F1(stag) | F1(prog) |"
240	    sep = "|" + "|".join(["-" * 30] + ["-" * 10] * 4) + "|"
241	    print(header)
242	    print(sep)
243	    for name, m in results:
244	        row = f"| {name:28s} |"
245	        for key in ["macro_f1", "accuracy", "f1_stagnation", "f1_progress"]:
246	            v = m.get(key)
247	            if v is None:
248	                row += "    —     |"
249	            else:
250	                row += f" {v:.4f}   |"
251	        print(row)
252	
253	
254	def main():
255	    parser = argparse.ArgumentParser(description="Non-NLP structural baseline")
256	    parser.add_argument("--data_dir", required=True)
257	    parser.add_argument("--split_info", required=True)
258	    parser.add_argument("--trajectories", required=True)
259	    args = parser.parse_args()
260	
261	    data_dir = Path(args.data_dir)
262	
263	    # Load split info
264	    with open(args.split_info) as f:
265	        split_info = json.load(f)
266	
267	    # Build trajectory index
268	    print("Building trajectory index ...")
269	    traj_index = build_trajectory_index(args.trajectories)
270	    print(f"Indexed {len(traj_index)} trajectories")
271	
272	    # Load windows
273	    print("Loading windows ...")
274	    all_windows = load_windows(data_dir / "windows_labeled.jsonl")
275	    print(f"Total windows: {len(all_windows)}")
276	
277	    # Step 1: filter out ABSTAIN (mirrors generate_embeddings.py)
278	    non_abstain = [w for w in all_windows if w.get("majority_label", -1) != -1]
279	    print(f"Non-abstain: {len(non_abstain)}")
280	
281	    # Step 2: apply keep_indices (confidence filter, indexes into non_abstain array)
282	    keep_indices = split_info.get("keep_indices")
283	    if keep_indices is not None:
284	        min_conf = split_info.get("min_confidence", 0)
285	        print(f"Confidence filter (min_confidence={min_conf}): {len(keep_indices)}/{len(non_abstain)}")
286	        windows = [non_abstain[i] for i in keep_indices]
287	    else:
288	        windows = non_abstain
289	
290	    print(f"Usable windows: {len(windows)}")
291	
292	    # Extract features for all usable windows
293	    print("Extracting features ...")
294	    features = []
295	    labels = []
296	    n_missing = 0
297	    for w in windows:
298	        row_idx = w.get("row_index", 0)
299	        step_indices = w["step_indices"]
300	        traj_steps = traj_index.get(row_idx, [])
301	
302	        window_steps = []
303	        for si in step_indices:
304	            if si < len(traj_steps):
305	                window_steps.append(traj_steps[si])
306	            else:
307	                window_steps.append({"role": "unknown", "text": ""})
308	                n_missing += 1
309	
310	        feat = extract_features(window_steps, w.get("short_trajectory", False))
311	        features.append(feat)
312	        labels.append(w["majority_label"])
313	
314	    X = np.stack(features)
315	    y = np.array(labels)
316	    print(f"Feature matrix: {X.shape}, missing steps: {n_missing}")
317	
318	    # Split
319	    train_idx = split_info["train_indices"]
320	    val_idx = split_info["val_indices"]
321	    test_idx = split_info["test_indices"]
322	    print(f"Split — train: {len(train_idx)}, val: {len(val_idx)}, test: {len(test_idx)}")
323	
324	    X_train, y_train = X[train_idx], y[train_idx]
325	    X_val, y_val = X[val_idx], y[val_idx]
326	    X_test, y_test = X[test_idx], y[test_idx]
327	
328	    print(f"Train label dist: stag={sum(y_train==0)}, prog={sum(y_train==1)}")
329	    print(f"Test label dist:  stag={sum(y_test==0)}, prog={sum(y_test==1)}")
330	    print()
331	
332	    # Standardize
333	    scaler = StandardScaler()
334	    X_train_s = scaler.fit_transform(X_train)
335	    X_val_s = scaler.transform(X_val)
336	    X_test_s = scaler.transform(X_test)
337	
338	    results = []
339	    results.append(("GRU Probe (ref)", {"macro_f1": 0.9055}))
340	    results.append(("MeanPool+LR (ref)", {"macro_f1": 0.8435}))
341	
342	    # --- LogisticRegression ---
343	    print("=== Logistic Regression (C tuning) ===")
344	    best_c, best_val_f1 = None, -1
345	    for c in [0.001, 0.01, 0.1, 1.0, 10.0, 100.0]:
346	        lr = LogisticRegression(max_iter=2000, C=c, solver="lbfgs")
347	        lr.fit(X_train_s, y_train)
348	        val_preds = lr.predict(X_val_s)
349	        m = compute_metrics(y_val.tolist(), val_preds.tolist())
350	        print(f"  C={c:7.3f} → val Macro-F1={m['macro_f1']:.4f}")
351	        if m["macro_f1"] > best_val_f1:
352	            best_val_f1 = m["macro_f1"]
353	            best_c = c
354	
355	    print(f"  Best C={best_c}")
356	    lr_final = LogisticRegression(max_iter=2000, C=best_c, solver="lbfgs")
357	    lr_final.fit(X_train_s, y_train)
358	    test_preds_lr = lr_final.predict(X_test_s)
359	    m_lr = compute_metrics(y_test.tolist(), test_preds_lr.tolist())
360	    results.append(("Struct + LR", m_lr))
361	    print(f"  Test: {m_lr}")
362	
363	    # Feature importance (LR coefficients)
364	    print("\n  Top features (LR coef magnitude):")
365	    coefs = np.abs(lr_final.coef_[0])
366	    top_idx = np.argsort(coefs)[::-1][:10]
367	    for i in top_idx:
368	        print(f"    {FEATURE_NAMES[i]:30s} = {lr_final.coef_[0][i]:+.4f}")
369	    print()
370	
371	    # --- RandomForest ---
372	    print("=== Random Forest (n_estimators tuning) ===")
373	    best_n, best_val_f1_rf = None, -1
374	    for n in [50, 100, 200, 500]:
375	        rf = RandomForestClassifier(n_estimators=n, max_depth=10, random_state=42, n_jobs=-1)
376	        rf.fit(X_train, y_train)
377	        val_preds = rf.predict(X_val)
378	        m = compute_metrics(y_val.tolist(), val_preds.tolist())
379	        print(f"  n={n:4d} → val Macro-F1={m['macro_f1']:.4f}")
380	        if m["macro_f1"] > best_val_f1_rf:
381	            best_val_f1_rf = m["macro_f1"]
382	            best_n = n
383	
384	    print(f"  Best n_estimators={best_n}")
385	    rf_final = RandomForestClassifier(n_estimators=best_n, max_depth=10, random_state=42, n_jobs=-1)
386	    rf_final.fit(X_train, y_train)
387	    test_preds_rf = rf_final.predict(X_test)
388	    m_rf = compute_metrics(y_test.tolist(), test_preds_rf.tolist())
389	    results.append(("Struct + RF", m_rf))
390	    print(f"  Test: {m_rf}")
391	
392	    print("\n  Top features (RF importance):")
393	    imp = rf_final.feature_importances_
394	    top_idx = np.argsort(imp)[::-1][:10]
395	    for i in top_idx:
396	        print(f"    {FEATURE_NAMES[i]:30s} = {imp[i]:.4f}")
397	    print()
398	
399	    # --- GradientBoosting ---
400	    print("=== Gradient Boosting ===")
401	    best_lr_gb, best_val_f1_gb = None, -1
402	    for lr_val in [0.01, 0.05, 0.1, 0.2]:
403	        gb = GradientBoostingClassifier(
404	            n_estimators=200, learning_rate=lr_val, max_depth=5, random_state=42
405	        )
406	        gb.fit(X_train, y_train)
407	        val_preds = gb.predict(X_val)
408	        m = compute_metrics(y_val.tolist(), val_preds.tolist())
409	        print(f"  lr={lr_val:.2f} → val Macro-F1={m['macro_f1']:.4f}")
410	        if m["macro_f1"] > best_val_f1_gb:
411	            best_val_f1_gb = m["macro_f1"]
412	            best_lr_gb = lr_val
413	
414	    print(f"  Best lr={best_lr_gb}")
415	    gb_final = GradientBoostingClassifier(
416	        n_estimators=200, learning_rate=best_lr_gb, max_depth=5, random_state=42
417	    )
418	    gb_final.fit(X_train, y_train)
419	    test_preds_gb = gb_final.predict(X_test)
420	    m_gb = compute_metrics(y_test.tolist(), test_preds_gb.tolist())
421	    results.append(("Struct + GB", m_gb))
422	    print(f"  Test: {m_gb}")
423	    print()
424	
425	    # --- Summary ---
426	    print("=" * 80)
427	    print("RESULTS SUMMARY")
428	    print("=" * 80)
429	    print_table(results)
430	
431	    # Best non-NLP
432	    best_name = max(results[2:], key=lambda x: x[1].get("macro_f1", 0))
433	    print(f"\nBest structural baseline: {best_name[0]} (Macro-F1={best_name[1]['macro_f1']:.4f})")
434	    print(f"vs GRU Probe:      {0.9055 - best_name[1]['macro_f1']:+.4f}")
435	    print(f"vs MeanPool+LR:    {0.8435 - best_name[1]['macro_f1']:+.4f}")
436	
437	    # Save results
438	    output = {
439	        "Struct + LR": {f"test_{k}": round(v, 4) for k, v in m_lr.items()},
440	        "Struct + RF": {f"test_{k}": round(v, 4) for k, v in m_rf.items()},
441	        "Struct + GB": {f"test_{k}": round(v, 4) for k, v in m_gb.items()},
442	        "best_model": best_name[0],
443	        "best_macro_f1": round(best_name[1]["macro_f1"], 4),
444	        "probe_ref_macro_f1": 0.9055,
445	        "meanpool_lr_ref_macro_f1": 0.8435,
446	        "num_features": len(FEATURE_NAMES),
447	        "feature_names": FEATURE_NAMES,
448	        "hyperparams": {
449	            "LR_best_C": best_c,
450	            "RF_best_n_estimators": best_n,
451	            "GB_best_lr": best_lr_gb,
452	        },
453	    }
454	    out_path = data_dir / "non_nlp_baseline_results.json"
455	    with open(out_path, "w") as f:
456	        json.dump(output, f, indent=2)
457	    print(f"\nResults saved to {out_path}")
458	
459	
460	if __name__ == "__main__":
461	    main()
462	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "829749a5-3778-4dd8-b0c5-0c69121a4c21",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/non_nlp_baseline.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Non-NLP baseline: structural/numerical features only.\n\nExtracts hand-crafted features from raw trajectory steps (no embeddings),\ntrains LogisticRegression, RandomForest, GradientBoosting.\nUses the same train/val/test split as probe_001.\n\"\"\"\n\nimport json\nimport re\nimport sys\nimport argparse\nfrom collections import Counter\nfrom difflib import SequenceMatcher\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score\n\n\ndef compute_metrics(labels, preds):\n    return {\n        \"macro_f1\": f1_score(labels, preds, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(labels, preds),\n        \"precision_macro\": precision_score(labels, preds, average=\"macro\", zero_division=0),\n        \"recall_macro\": recall_score(labels, preds, average=\"macro\", zero_division=0),\n        \"f1_stagnation\": f1_score(labels, preds, pos_label=0, zero_division=0),\n        \"f1_progress\": f1_score(labels, preds, pos_label=1, zero_division=0),\n    }\n\n\ndef extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\n\ndef cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_features(steps, is_short):\n    \"\"\"Extract structural features from a list of step dicts.\n\n    Each step dict has: role, text\n    \"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30)\n\n    roles = [s[\"role\"] for s in steps]\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    # --- text length features ---\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    # text length trend (slope via simple linear regression)\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (n * np.dot(x, x) - x.sum()**2 + 1e-9)\n    else:\n        slope = 0.0\n\n    # --- command features ---\n    commands = []\n    for s, t in actions:\n        cmd = extract_command(t)\n        if cmd:\n            commands.append(cmd)\n\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    # command type counts\n    n_edit = 0\n    n_search = 0\n    n_nav = 0\n    n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    # adjacent command similarity\n    if n_cmds >= 2:\n        sims = [cmd_similarity(commands[i], commands[i+1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        # max consecutive run with sim >= 0.9\n        max_run = 1\n        cur_run = 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = 0.0\n        max_adj_sim = 0.0\n        max_run = 0\n\n    # --- content pattern features ---\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower())\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n\n    # exit code patterns in observations (look for \"exit code\" or \"$?\" patterns)\n    n_nonzero_exit = sum(1 for _, t in observations if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t))\n\n    feature_vec = np.array([\n        n,                    # 0: num_steps\n        n_actions,            # 1: num_actions\n        n_obs,                # 2: num_observations\n        n_actions / max(n, 1),# 3: action_ratio\n        mean_tlen,            # 4: mean_text_len\n        std_tlen,             # 5: std_text_len\n        max_tlen,             # 6: max_text_len\n        min_tlen,             # 7: min_text_len\n        mean_action_len,      # 8: mean_action_len\n        mean_obs_len,         # 9: mean_obs_len\n        slope,                # 10: text_len_trend\n        n_cmds,               # 11: num_commands\n        mean_cmd_len,         # 12: mean_cmd_len\n        max_cmd_len,          # 13: max_cmd_len\n        unique_cmd_ratio,     # 14: unique_cmd_ratio\n        repeat_ratio,         # 15: max_repeat_ratio\n        n_edit,               # 16: num_edit_cmds\n        n_search,             # 17: num_search_cmds\n        n_nav,                # 18: num_nav_cmds\n        n_submit,             # 19: num_submit_cmds\n        edit_ratio,           # 20: edit_ratio\n        search_ratio,         # 21: search_ratio\n        avg_adj_sim,          # 22: avg_adjacent_cmd_similarity\n        max_adj_sim,          # 23: max_adjacent_cmd_similarity\n        max_run,              # 24: max_consecutive_similar_cmds\n        n_errors,             # 25: num_errors\n        n_test_output,        # 26: num_test_outputs\n        n_file_display,       # 27: num_file_displays\n        n_nonzero_exit,       # 28: num_nonzero_exits\n        float(is_short),      # 29: is_short_trajectory\n    ], dtype=np.float32)\n\n    return feature_vec\n\n\nFEATURE_NAMES = [\n    \"num_steps\", \"num_actions\", \"num_observations\", \"action_ratio\",\n    \"mean_text_len\", \"std_text_len\", \"max_text_len\", \"min_text_len\",\n    \"mean_action_len\", \"mean_obs_len\", \"text_len_trend\",\n    \"num_commands\", \"mean_cmd_len\", \"max_cmd_len\",\n    \"unique_cmd_ratio\", \"max_repeat_ratio\",\n    \"num_edit_cmds\", \"num_search_cmds\", \"num_nav_cmds\", \"num_submit_cmds\",\n    \"edit_ratio\", \"search_ratio\",\n    \"avg_adjacent_cmd_sim\", \"max_adjacent_cmd_sim\", \"max_consecutive_similar\",\n    \"num_errors\", \"num_test_outputs\", \"num_file_displays\", \"num_nonzero_exits\",\n    \"is_short_trajectory\",\n]\n\n\ndef build_trajectory_index(traj_path):\n    \"\"\"row_index -> list of step dicts [{role, text}, ...]\"\"\"\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append({\n                    \"role\": s.get(\"role\", \"unknown\"),\n                    \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                })\n            index[row_idx] = steps\n    return index\n\n\ndef load_windows(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef print_table(results):\n    header = \"| Method                      | Macro-F1 | Accuracy | F1(stag) | F1(prog) |\"\n    sep = \"|\" + \"|\".join([\"-\" * 30] + [\"-\" * 10] * 4) + \"|\"\n    print(header)\n    print(sep)\n    for name, m in results:\n        row = f\"| {name:28s} |\"\n        for key in [\"macro_f1\", \"accuracy\", \"f1_stagnation\", \"f1_progress\"]:\n            v = m.get(key)\n            if v is None:\n                row += \"    —     |\"\n            else:\n                row += f\" {v:.4f}   |\"\n        print(row)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Non-NLP structural baseline\")\n    parser.add_argument(\"--data_dir\", required=True)\n    parser.add_argument(\"--split_info\", required=True)\n    parser.add_argument(\"--trajectories\", required=True)\n    args = parser.parse_args()\n\n    data_dir = Path(args.data_dir)\n\n    # Load split info\n    with open(args.split_info) as f:\n        split_info = json.load(f)\n\n    # Build trajectory index\n    print(\"Building trajectory index ...\")\n    traj_index = build_trajectory_index(args.trajectories)\n    print(f\"Indexed {len(traj_index)} trajectories\")\n\n    # Load windows\n    print(\"Loading windows ...\")\n    all_windows = load_windows(data_dir / \"windows_labeled.jsonl\")\n    print(f\"Total windows: {len(all_windows)}\")\n\n    # Step 1: filter out ABSTAIN (mirrors generate_embeddings.py)\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"Non-abstain: {len(non_abstain)}\")\n\n    # Step 2: apply keep_indices (confidence filter, indexes into non_abstain array)\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        min_conf = split_info.get(\"min_confidence\", 0)\n        print(f\"Confidence filter (min_confidence={min_conf}): {len(keep_indices)}/{len(non_abstain)}\")\n        windows = [non_abstain[i] for i in keep_indices]\n    else:\n        windows = non_abstain\n\n    print(f\"Usable windows: {len(windows)}\")\n\n    # Extract features for all usable windows\n    print(\"Extracting features ...\")\n    features = []\n    labels = []\n    n_missing = 0\n    for w in windows:\n        row_idx = w.get(\"row_index\", 0)\n        step_indices = w[\"step_indices\"]\n        traj_steps = traj_index.get(row_idx, [])\n\n        window_steps = []\n        for si in step_indices:\n            if si < len(traj_steps):\n                window_steps.append(traj_steps[si])\n            else:\n                window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                n_missing += 1\n\n        feat = extract_features(window_steps, w.get(\"short_trajectory\", False))\n        features.append(feat)\n        labels.append(w[\"majority_label\"])\n\n    X = np.stack(features)\n    y = np.array(labels)\n    print(f\"Feature matrix: {X.shape}, missing steps: {n_missing}\")\n\n    # Split\n    train_idx = split_info[\"train_indices\"]\n    val_idx = split_info[\"val_indices\"]\n    test_idx = split_info[\"test_indices\"]\n    print(f\"Split — train: {len(train_idx)}, val: {len(val_idx)}, test: {len(test_idx)}\")\n\n    X_train, y_train = X[train_idx], y[train_idx]\n    X_val, y_val = X[val_idx], y[val_idx]\n    X_test, y_test = X[test_idx], y[test_idx]\n\n    print(f\"Train label dist: stag={sum(y_train==0)}, prog={sum(y_train==1)}\")\n    print(f\"Test label dist:  stag={sum(y_test==0)}, prog={sum(y_test==1)}\")\n    print()\n\n    # Standardize\n    scaler = StandardScaler()\n    X_train_s = scaler.fit_transform(X_train)\n    X_val_s = scaler.transform(X_val)\n    X_test_s = scaler.transform(X_test)\n\n    results = []\n    results.append((\"GRU Probe (ref)\", {\"macro_f1\": 0.9055}))\n    results.append((\"MeanPool+LR (ref)\", {\"macro_f1\": 0.8435}))\n\n    # --- LogisticRegression ---\n    print(\"=== Logistic Regression (C tuning) ===\")\n    best_c, best_val_f1 = None, -1\n    for c in [0.001, 0.01, 0.1, 1.0, 10.0, 100.0]:\n        lr = LogisticRegression(max_iter=2000, C=c, solver=\"lbfgs\")\n        lr.fit(X_train_s, y_train)\n        val_preds = lr.predict(X_val_s)\n        m = compute_metrics(y_val.tolist(), val_preds.tolist())\n        print(f\"  C={c:7.3f} → val Macro-F1={m['macro_f1']:.4f}\")\n        if m[\"macro_f1\"] > best_val_f1:\n            best_val_f1 = m[\"macro_f1\"]\n            best_c = c\n\n    print(f\"  Best C={best_c}\")\n    lr_final = LogisticRegression(max_iter=2000, C=best_c, solver=\"lbfgs\")\n    lr_final.fit(X_train_s, y_train)\n    test_preds_lr = lr_final.predict(X_test_s)\n    m_lr = compute_metrics(y_test.tolist(), test_preds_lr.tolist())\n    results.append((\"Struct + LR\", m_lr))\n    print(f\"  Test: {m_lr}\")\n\n    # Feature importance (LR coefficients)\n    print(\"\\n  Top features (LR coef magnitude):\")\n    coefs = np.abs(lr_final.coef_[0])\n    top_idx = np.argsort(coefs)[::-1][:10]\n    for i in top_idx:\n        print(f\"    {FEATURE_NAMES[i]:30s} = {lr_final.coef_[0][i]:+.4f}\")\n    print()\n\n    # --- RandomForest ---\n    print(\"=== Random Forest (n_estimators tuning) ===\")\n    best_n, best_val_f1_rf = None, -1\n    for n in [50, 100, 200, 500]:\n        rf = RandomForestClassifier(n_estimators=n, max_depth=10, random_state=42, n_jobs=-1)\n        rf.fit(X_train, y_train)\n        val_preds = rf.predict(X_val)\n        m = compute_metrics(y_val.tolist(), val_preds.tolist())\n        print(f\"  n={n:4d} → val Macro-F1={m['macro_f1']:.4f}\")\n        if m[\"macro_f1\"] > best_val_f1_rf:\n            best_val_f1_rf = m[\"macro_f1\"]\n            best_n = n\n\n    print(f\"  Best n_estimators={best_n}\")\n    rf_final = RandomForestClassifier(n_estimators=best_n, max_depth=10, random_state=42, n_jobs=-1)\n    rf_final.fit(X_train, y_train)\n    test_preds_rf = rf_final.predict(X_test)\n    m_rf = compute_metrics(y_test.tolist(), test_preds_rf.tolist())\n    results.append((\"Struct + RF\", m_rf))\n    print(f\"  Test: {m_rf}\")\n\n    print(\"\\n  Top features (RF importance):\")\n    imp = rf_final.feature_importances_\n    top_idx = np.argsort(imp)[::-1][:10]\n    for i in top_idx:\n        print(f\"    {FEATURE_NAMES[i]:30s} = {imp[i]:.4f}\")\n    print()\n\n    # --- GradientBoosting ---\n    print(\"=== Gradient Boosting ===\")\n    best_lr_gb, best_val_f1_gb = None, -1\n    for lr_val in [0.01, 0.05, 0.1, 0.2]:\n        gb = GradientBoostingClassifier(\n            n_estimators=200, learning_rate=lr_val, max_depth=5, random_state=42\n        )\n        gb.fit(X_train, y_train)\n        val_preds = gb.predict(X_val)\n        m = compute_metrics(y_val.tolist(), val_preds.tolist())\n        print(f\"  lr={lr_val:.2f} → val Macro-F1={m['macro_f1']:.4f}\")\n        if m[\"macro_f1\"] > best_val_f1_gb:\n            best_val_f1_gb = m[\"macro_f1\"]\n            best_lr_gb = lr_val\n\n    print(f\"  Best lr={best_lr_gb}\")\n    gb_final = GradientBoostingClassifier(\n        n_estimators=200, learning_rate=best_lr_gb, max_depth=5, random_state=42\n    )\n    gb_final.fit(X_train, y_train)\n    test_preds_gb = gb_final.predict(X_test)\n    m_gb = compute_metrics(y_test.tolist(), test_preds_gb.tolist())\n    results.append((\"Struct + GB\", m_gb))\n    print(f\"  Test: {m_gb}\")\n    print()\n\n    # --- Summary ---\n    print(\"=\" * 80)\n    print(\"RESULTS SUMMARY\")\n    print(\"=\" * 80)\n    print_table(results)\n\n    # Best non-NLP\n    best_name = max(results[2:], key=lambda x: x[1].get(\"macro_f1\", 0))\n    print(f\"\\nBest structural baseline: {best_name[0]} (Macro-F1={best_name[1]['macro_f1']:.4f})\")\n    print(f\"vs GRU Probe:      {0.9055 - best_name[1]['macro_f1']:+.4f}\")\n    print(f\"vs MeanPool+LR:    {0.8435 - best_name[1]['macro_f1']:+.4f}\")\n\n    # Save results\n    output = {\n        \"Struct + LR\": {f\"test_{k}\": round(v, 4) for k, v in m_lr.items()},\n        \"Struct + RF\": {f\"test_{k}\": round(v, 4) for k, v in m_rf.items()},\n        \"Struct + GB\": {f\"test_{k}\": round(v, 4) for k, v in m_gb.items()},\n        \"best_model\": best_name[0],\n        \"best_macro_f1\": round(best_name[1][\"macro_f1\"], 4),\n        \"probe_ref_macro_f1\": 0.9055,\n        \"meanpool_lr_ref_macro_f1\": 0.8435,\n        \"num_features\": len(FEATURE_NAMES),\n        \"feature_names\": FEATURE_NAMES,\n        \"hyperparams\": {\n            \"LR_best_C\": best_c,\n            \"RF_best_n_estimators\": best_n,\n            \"GB_best_lr\": best_lr_gb,\n        },\n    }\n    out_path = data_dir / \"non_nlp_baseline_results.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nResults saved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 462,
      "startLine": 1,
      "totalLines": 462
    }
  }
}
````

</details>

---


### Tool call

_source line 110_

<details open><summary>🔧 Tool call — Read · `toolu_012RQTLYztNw9Y7nSEgaNLNG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/evaluate.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "acb82afa-ba65-432a-8cb3-1cb75bd6b438",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQEuLeTb7oxY5Br5A2utFx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5038,
      "cache_read_input_tokens": 23566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5038
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

_source line 111 · 2026-05-14T22:41:58.502Z_

<details><summary>↩ Tool result · `toolu_012RQTLYztNw9Y7nSEgaNLNG`</summary>

```text
1	#!/usr/bin/env python3
2	"""Evaluate the GRU probe and all baselines on the test set, output comparison table."""
3	
4	import argparse
5	import json
6	import sys
7	from pathlib import Path
8	
9	import torch
10	from torch.utils.data import DataLoader
11	
12	sys.path.insert(0, str(Path(__file__).parent))
13	from baselines import (
14	    ALL_BASELINES,
15	    CosineSimilarityBaseline,
16	    RandomBaseline,
17	    Repeat3Baseline,
18	    compute_metrics,
19	)
20	from probe_model import ProgressProbe, WindowDataset, collate_fn
21	
22	
23	def parse_row_index(trajectory_id: str) -> int:
24	    """Extract row_index from trajectory_id 'instance_id__model_name__r{idx}'."""
25	    return int(trajectory_id.rsplit("__r", 1)[1])
26	
27	
28	def build_trajectory_index(traj_path: str) -> dict:
29	    """Map row_index (int) -> list of step dicts."""
30	    index = {}
31	    with open(traj_path) as f:
32	        for row_idx, line in enumerate(f):
33	            line = line.strip()
34	            if not line:
35	                continue
36	            raw = json.loads(line)
37	            steps = []
38	            for s in raw.get("trajectory") or []:
39	                steps.append({
40	                    "role": s.get("role", "unknown"),
41	                    "text": s.get("text") or s.get("system_prompt") or "",
42	                })
43	            index[row_idx] = steps
44	    return index
45	
46	
47	def load_windows(path: str) -> dict:
48	    """Load windows and index by trajectory_id__w{window_idx}."""
49	    index = {}
50	    with open(path) as f:
51	        for line in f:
52	            line = line.strip()
53	            if line:
54	                w = json.loads(line)
55	                wid = f"{w['trajectory_id']}__w{w['window_idx']}"
56	                index[wid] = w
57	    return index
58	
59	
60	def build_baseline_data(
61	    data: dict, indices: list[int], traj_index: dict
62	) -> list[dict]:
63	    """Construct baseline-compatible data dicts for given indices."""
64	    result = []
65	    for i in indices:
66	        tid = data["trajectory_ids"][i]
67	        row_idx = parse_row_index(tid)
68	        traj_steps = traj_index.get(row_idx, [])
69	
70	        steps = []
71	        for si in data["step_indices_list"][i]:
72	            if si < len(traj_steps):
73	                steps.append(traj_steps[si])
74	            else:
75	                steps.append({"role": "unknown", "text": ""})
76	
77	        result.append({
78	            "label": data["labels"][i],
79	            "embeddings": data["embeddings"][i],
80	            "steps": steps,
81	        })
82	    return result
83	
84	
85	@torch.no_grad()
86	def evaluate_probe(model: ProgressProbe, loader: DataLoader, device: str) -> tuple[dict, list[int]]:
87	    model.eval()
88	    all_labels, all_preds = [], []
89	    for padded, labels, lengths in loader:
90	        logits = model(padded.to(device), lengths)
91	        preds = (torch.sigmoid(logits) >= 0.5).long().cpu()
92	        all_labels.extend(labels.long().tolist())
93	        all_preds.extend(preds.tolist())
94	    return compute_metrics(all_labels, all_preds), all_preds
95	
96	
97	def print_table(results: list[tuple[str, dict]]):
98	    header = "| Method | Macro-F1 | Accuracy | Precision | Recall | F1(stag) | F1(prog) |"
99	    sep = "|" + "|".join(["---"] * 7) + "|"
100	    print(header)
101	    print(sep)
102	    for name, m in results:
103	        print(
104	            f"| {name:20s} | {m['macro_f1']:.4f}   | {m['accuracy']:.4f}   | "
105	            f"{m['precision_macro']:.4f}    | {m['recall_macro']:.4f} | "
106	            f"{m['f1_stagnation']:.4f}   | {m['f1_progress']:.4f}   |"
107	        )
108	
109	
110	def main():
111	    parser = argparse.ArgumentParser(description="Evaluate probe + baselines on test set")
112	    parser.add_argument("--data_dir", required=True, help="Directory containing embeddings.pt")
113	    parser.add_argument("--checkpoint", required=True, help="Path to best_model.pt")
114	    parser.add_argument("--split_info", required=True, help="Path to split_info.json")
115	    parser.add_argument("--trajectories", required=True, help="Path to original trajectories JSONL")
116	    parser.add_argument("--batch_size", type=int, default=64)
117	    parser.add_argument("--device", default=None)
118	    args = parser.parse_args()
119	
120	    device = args.device or ("cuda" if torch.cuda.is_available() else "cpu")
121	
122	    # Load embeddings data
123	    data = torch.load(Path(args.data_dir) / "embeddings.pt", weights_only=False)
124	
125	    # Apply same confidence filter used during training
126	    with open(args.split_info) as f:
127	        split_info = json.load(f)
128	
129	    keep_indices = split_info.get("keep_indices")
130	    if keep_indices is not None:
131	        min_conf = split_info.get("min_confidence", 0)
132	        print(f"Applying confidence filter (min_confidence={min_conf}): {len(keep_indices)}/{len(data['labels'])} windows")
133	        data = {
134	            "embeddings": [data["embeddings"][i] for i in keep_indices],
135	            "labels": [data["labels"][i] for i in keep_indices],
136	            "trajectory_ids": [data["trajectory_ids"][i] for i in keep_indices],
137	            "instance_ids": [data["instance_ids"][i] for i in keep_indices],
138	            "step_indices_list": [data["step_indices_list"][i] for i in keep_indices],
139	            "confidences": [data["confidences"][i] for i in keep_indices],
140	        }
141	
142	    train_idx = split_info["train_indices"]
143	    val_idx = split_info["val_indices"]
144	    test_idx = split_info["test_indices"]
145	
146	    print(f"Test set: {len(test_idx)} windows")
147	
148	    # ── Probe evaluation ──
149	    ckpt = torch.load(args.checkpoint, weights_only=False)
150	    model = ProgressProbe(
151	        embed_dim=ckpt["embed_dim"],
152	        hidden_size=ckpt["hidden_size"],
153	        num_layers=ckpt["num_layers"],
154	    ).to(device)
155	    model.load_state_dict(ckpt["model_state_dict"])
156	
157	    test_ds = WindowDataset(
158	        [data["embeddings"][i] for i in test_idx],
159	        [data["labels"][i] for i in test_idx],
160	    )
161	    test_loader = DataLoader(test_ds, batch_size=args.batch_size, collate_fn=collate_fn)
162	    probe_metrics, _ = evaluate_probe(model, test_loader, device)
163	
164	    # ── Baseline evaluation ──
165	    print("Loading trajectory data for baselines ...")
166	    traj_index = build_trajectory_index(args.trajectories)
167	
168	    train_bl = build_baseline_data(data, train_idx, traj_index)
169	    val_bl = build_baseline_data(data, val_idx, traj_index)
170	    test_bl = build_baseline_data(data, test_idx, traj_index)
171	
172	    results = [("GRU Probe", probe_metrics)]
173	
174	    for cls in ALL_BASELINES:
175	        bl = cls()
176	        bl.fit(train_bl, val_bl)
177	        metrics = bl.evaluate(test_bl)
178	        results.append((bl.name, metrics))
179	
180	    # ── Output ──
181	    print()
182	    print_table(results)
183	
184	    # Best baseline comparison
185	    baseline_results = results[1:]
186	    best_bl_name, best_bl_m = max(baseline_results, key=lambda x: x[1]["macro_f1"])
187	    delta = probe_metrics["macro_f1"] - best_bl_m["macro_f1"]
188	    pct = (delta / best_bl_m["macro_f1"] * 100) if best_bl_m["macro_f1"] > 0 else float("inf")
189	
190	    print(f"\nBest baseline: {best_bl_name} (Macro-F1: {best_bl_m['macro_f1']:.4f})")
191	    print(f"GRU Probe improvement: {delta:+.4f} ({pct:+.1f}%)")
192	
193	
194	if __name__ == "__main__":
195	    main()
196	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "ffe2391c-3922-4cec-bdcc-cb299029758d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/evaluate.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Evaluate the GRU probe and all baselines on the test set, output comparison table.\"\"\"\n\nimport argparse\nimport json\nimport sys\nfrom pathlib import Path\n\nimport torch\nfrom torch.utils.data import DataLoader\n\nsys.path.insert(0, str(Path(__file__).parent))\nfrom baselines import (\n    ALL_BASELINES,\n    CosineSimilarityBaseline,\n    RandomBaseline,\n    Repeat3Baseline,\n    compute_metrics,\n)\nfrom probe_model import ProgressProbe, WindowDataset, collate_fn\n\n\ndef parse_row_index(trajectory_id: str) -> int:\n    \"\"\"Extract row_index from trajectory_id 'instance_id__model_name__r{idx}'.\"\"\"\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\ndef build_trajectory_index(traj_path: str) -> dict:\n    \"\"\"Map row_index (int) -> list of step dicts.\"\"\"\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append({\n                    \"role\": s.get(\"role\", \"unknown\"),\n                    \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                })\n            index[row_idx] = steps\n    return index\n\n\ndef load_windows(path: str) -> dict:\n    \"\"\"Load windows and index by trajectory_id__w{window_idx}.\"\"\"\n    index = {}\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                w = json.loads(line)\n                wid = f\"{w['trajectory_id']}__w{w['window_idx']}\"\n                index[wid] = w\n    return index\n\n\ndef build_baseline_data(\n    data: dict, indices: list[int], traj_index: dict\n) -> list[dict]:\n    \"\"\"Construct baseline-compatible data dicts for given indices.\"\"\"\n    result = []\n    for i in indices:\n        tid = data[\"trajectory_ids\"][i]\n        row_idx = parse_row_index(tid)\n        traj_steps = traj_index.get(row_idx, [])\n\n        steps = []\n        for si in data[\"step_indices_list\"][i]:\n            if si < len(traj_steps):\n                steps.append(traj_steps[si])\n            else:\n                steps.append({\"role\": \"unknown\", \"text\": \"\"})\n\n        result.append({\n            \"label\": data[\"labels\"][i],\n            \"embeddings\": data[\"embeddings\"][i],\n            \"steps\": steps,\n        })\n    return result\n\n\n@torch.no_grad()\ndef evaluate_probe(model: ProgressProbe, loader: DataLoader, device: str) -> tuple[dict, list[int]]:\n    model.eval()\n    all_labels, all_preds = [], []\n    for padded, labels, lengths in loader:\n        logits = model(padded.to(device), lengths)\n        preds = (torch.sigmoid(logits) >= 0.5).long().cpu()\n        all_labels.extend(labels.long().tolist())\n        all_preds.extend(preds.tolist())\n    return compute_metrics(all_labels, all_preds), all_preds\n\n\ndef print_table(results: list[tuple[str, dict]]):\n    header = \"| Method | Macro-F1 | Accuracy | Precision | Recall | F1(stag) | F1(prog) |\"\n    sep = \"|\" + \"|\".join([\"---\"] * 7) + \"|\"\n    print(header)\n    print(sep)\n    for name, m in results:\n        print(\n            f\"| {name:20s} | {m['macro_f1']:.4f}   | {m['accuracy']:.4f}   | \"\n            f\"{m['precision_macro']:.4f}    | {m['recall_macro']:.4f} | \"\n            f\"{m['f1_stagnation']:.4f}   | {m['f1_progress']:.4f}   |\"\n        )\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Evaluate probe + baselines on test set\")\n    parser.add_argument(\"--data_dir\", required=True, help=\"Directory containing embeddings.pt\")\n    parser.add_argument(\"--checkpoint\", required=True, help=\"Path to best_model.pt\")\n    parser.add_argument(\"--split_info\", required=True, help=\"Path to split_info.json\")\n    parser.add_argument(\"--trajectories\", required=True, help=\"Path to original trajectories JSONL\")\n    parser.add_argument(\"--batch_size\", type=int, default=64)\n    parser.add_argument(\"--device\", default=None)\n    args = parser.parse_args()\n\n    device = args.device or (\"cuda\" if torch.cuda.is_available() else \"cpu\")\n\n    # Load embeddings data\n    data = torch.load(Path(args.data_dir) / \"embeddings.pt\", weights_only=False)\n\n    # Apply same confidence filter used during training\n    with open(args.split_info) as f:\n        split_info = json.load(f)\n\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        min_conf = split_info.get(\"min_confidence\", 0)\n        print(f\"Applying confidence filter (min_confidence={min_conf}): {len(keep_indices)}/{len(data['labels'])} windows\")\n        data = {\n            \"embeddings\": [data[\"embeddings\"][i] for i in keep_indices],\n            \"labels\": [data[\"labels\"][i] for i in keep_indices],\n            \"trajectory_ids\": [data[\"trajectory_ids\"][i] for i in keep_indices],\n            \"instance_ids\": [data[\"instance_ids\"][i] for i in keep_indices],\n            \"step_indices_list\": [data[\"step_indices_list\"][i] for i in keep_indices],\n            \"confidences\": [data[\"confidences\"][i] for i in keep_indices],\n        }\n\n    train_idx = split_info[\"train_indices\"]\n    val_idx = split_info[\"val_indices\"]\n    test_idx = split_info[\"test_indices\"]\n\n    print(f\"Test set: {len(test_idx)} windows\")\n\n    # ── Probe evaluation ──\n    ckpt = torch.load(args.checkpoint, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n\n    test_ds = WindowDataset(\n        [data[\"embeddings\"][i] for i in test_idx],\n        [data[\"labels\"][i] for i in test_idx],\n    )\n    test_loader = DataLoader(test_ds, batch_size=args.batch_size, collate_fn=collate_fn)\n    probe_metrics, _ = evaluate_probe(model, test_loader, device)\n\n    # ── Baseline evaluation ──\n    print(\"Loading trajectory data for baselines ...\")\n    traj_index = build_trajectory_index(args.trajectories)\n\n    train_bl = build_baseline_data(data, train_idx, traj_index)\n    val_bl = build_baseline_data(data, val_idx, traj_index)\n    test_bl = build_baseline_data(data, test_idx, traj_index)\n\n    results = [(\"GRU Probe\", probe_metrics)]\n\n    for cls in ALL_BASELINES:\n        bl = cls()\n        bl.fit(train_bl, val_bl)\n        metrics = bl.evaluate(test_bl)\n        results.append((bl.name, metrics))\n\n    # ── Output ──\n    print()\n    print_table(results)\n\n    # Best baseline comparison\n    baseline_results = results[1:]\n    best_bl_name, best_bl_m = max(baseline_results, key=lambda x: x[1][\"macro_f1\"])\n    delta = probe_metrics[\"macro_f1\"] - best_bl_m[\"macro_f1\"]\n    pct = (delta / best_bl_m[\"macro_f1\"] * 100) if best_bl_m[\"macro_f1\"] > 0 else float(\"inf\")\n\n    print(f\"\\nBest baseline: {best_bl_name} (Macro-F1: {best_bl_m['macro_f1']:.4f})\")\n    print(f\"GRU Probe improvement: {delta:+.4f} ({pct:+.1f}%)\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 196,
      "startLine": 1,
      "totalLines": 196
    }
  }
}
```

</details>

---


### Tool call

_source line 112_

<details open><summary>🔧 Tool call — Read · `toolu_01QBaLTC3mbhbWaqAsPvvaMD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/probe_model.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "eb84333e-4c40-4e53-b89f-600a57b6b485",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQEuLeTb7oxY5Br5A2utFx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5038,
      "cache_read_input_tokens": 23566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5038
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

_source line 113 · 2026-05-14T22:41:58.852Z_

<details><summary>↩ Tool result · `toolu_01QBaLTC3mbhbWaqAsPvvaMD`</summary>

```text
1	#!/usr/bin/env python3
2	"""GRU-based progress probe model, dataset, and data splitting utilities."""
3	
4	import random
5	from pathlib import Path
6	
7	import torch
8	import torch.nn as nn
9	from torch.utils.data import Dataset
10	
11	
12	class ProgressProbe(nn.Module):
13	    """2-layer GRU probe for progress/stagnation binary classification.
14	
15	    Input:  (batch, seq_len, embed_dim)
16	    Output: (batch,) logits (apply sigmoid for probabilities)
17	    """
18	
19	    def __init__(self, embed_dim: int, hidden_size: int = 256, num_layers: int = 2, dropout: float = 0.1):
20	        super().__init__()
21	        self.gru = nn.GRU(
22	            embed_dim,
23	            hidden_size,
24	            num_layers=num_layers,
25	            batch_first=True,
26	            dropout=dropout if num_layers > 1 else 0.0,
27	        )
28	        self.classifier = nn.Linear(hidden_size, 1)
29	
30	    def forward(self, x: torch.Tensor, lengths: torch.Tensor = None) -> torch.Tensor:
31	        if lengths is not None:
32	            x = nn.utils.rnn.pack_padded_sequence(x, lengths.cpu(), batch_first=True, enforce_sorted=False)
33	        _, hidden = self.gru(x)
34	        out = hidden[-1]  # last layer hidden: (batch, hidden_size)
35	        return self.classifier(out).squeeze(-1)
36	
37	
38	class WindowDataset(Dataset):
39	    """Dataset of pre-computed window embeddings + binary labels."""
40	
41	    def __init__(self, embeddings: list[torch.Tensor], labels: list[int]):
42	        assert len(embeddings) == len(labels)
43	        self.embeddings = embeddings
44	        self.labels = labels
45	
46	    def __len__(self):
47	        return len(self.labels)
48	
49	    def __getitem__(self, idx):
50	        return self.embeddings[idx], self.labels[idx]
51	
52	
53	def collate_fn(batch):
54	    """Pad variable-length window embeddings to the max length in the batch."""
55	    embeddings_list, labels_list = zip(*batch)
56	    lengths = torch.tensor([e.shape[0] for e in embeddings_list], dtype=torch.long)
57	    max_len = lengths.max().item()
58	    embed_dim = embeddings_list[0].shape[1]
59	
60	    padded = torch.zeros(len(batch), max_len, embed_dim)
61	    for i, e in enumerate(embeddings_list):
62	        padded[i, : e.shape[0]] = e
63	
64	    labels = torch.tensor(labels_list, dtype=torch.float32)
65	    return padded, labels, lengths
66	
67	
68	def split_by_instance(
69	    instance_ids: list[str],
70	    train_ratio: float = 0.7,
71	    val_ratio: float = 0.15,
72	    seed: int = 42,
73	) -> tuple[list[int], list[int], list[int]]:
74	    """Split indices so all windows from the same instance stay in one split."""
75	    unique = sorted(set(instance_ids))
76	    rng = random.Random(seed)
77	    rng.shuffle(unique)
78	
79	    n = len(unique)
80	    n_train = int(n * train_ratio)
81	    n_val = int(n * val_ratio)
82	
83	    train_set = set(unique[:n_train])
84	    val_set = set(unique[n_train : n_train + n_val])
85	
86	    train_idx, val_idx, test_idx = [], [], []
87	    for i, iid in enumerate(instance_ids):
88	        if iid in train_set:
89	            train_idx.append(i)
90	        elif iid in val_set:
91	            val_idx.append(i)
92	        else:
93	            test_idx.append(i)
94	
95	    return train_idx, val_idx, test_idx
96	
97	
98	def load_split_datasets(
99	    data_path: str | Path, seed: int = 42
100	) -> tuple[WindowDataset, WindowDataset, WindowDataset, dict]:
101	    """Load embeddings.pt and return train/val/test WindowDatasets + split info."""
102	    data = torch.load(data_path, weights_only=False)
103	    embeddings = data["embeddings"]
104	    labels = data["labels"]
105	    instance_ids = data["instance_ids"]
106	
107	    train_idx, val_idx, test_idx = split_by_instance(instance_ids, seed=seed)
108	
109	    def subset(indices):
110	        return WindowDataset([embeddings[i] for i in indices], [labels[i] for i in indices])
111	
112	    split_info = {
113	        "train_indices": train_idx,
114	        "val_indices": val_idx,
115	        "test_indices": test_idx,
116	        "seed": seed,
117	        "embed_dim": data["embed_dim"],
118	    }
119	    return subset(train_idx), subset(val_idx), subset(test_idx), split_info
120	
121	
122	if __name__ == "__main__":
123	    print("=== ProgressProbe forward pass test ===")
124	    embed_dim = 1024
125	    batch_size = 4
126	
127	    model = ProgressProbe(embed_dim=embed_dim)
128	    print(f"Model: {model}")
129	    total_params = sum(p.numel() for p in model.parameters())
130	    print(f"Total parameters: {total_params:,}")
131	
132	    # Random data with variable sequence lengths
133	    lengths = torch.tensor([3, 7, 5, 2])
134	    max_len = lengths.max().item()
135	    x = torch.randn(batch_size, max_len, embed_dim)
136	    logits = model(x, lengths)
137	    probs = torch.sigmoid(logits)
138	
139	    print(f"Input shape:  {x.shape}")
140	    print(f"Lengths:      {lengths.tolist()}")
141	    print(f"Logits shape: {logits.shape}")
142	    print(f"Logits:       {logits.tolist()}")
143	    print(f"Probs:        {[f'{p:.4f}' for p in probs.tolist()]}")
144	
145	    # Test dataset + collate
146	    dummy_embeds = [torch.randn(l, embed_dim) for l in [3, 5, 2, 8]]
147	    dummy_labels = [1, 0, 1, 0]
148	    ds = WindowDataset(dummy_embeds, dummy_labels)
149	    batch = [ds[i] for i in range(len(ds))]
150	    padded, labels, lens = collate_fn(batch)
151	    print(f"\nCollate test: padded={padded.shape}, labels={labels.shape}, lengths={lens.tolist()}")
152	
153	    # Test split
154	    instance_ids = ["a", "a", "b", "b", "c", "c", "d", "d", "e", "e"]
155	    tr, va, te = split_by_instance(instance_ids, seed=42)
156	    print(f"\nSplit test (10 samples, 5 instances): train={len(tr)}, val={len(va)}, test={len(te)}")
157	    print("All tests passed.")
158	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "441c2592-08ec-46bd-b342-2123ca09716b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/probe_model.py",
      "content": "#!/usr/bin/env python3\n\"\"\"GRU-based progress probe model, dataset, and data splitting utilities.\"\"\"\n\nimport random\nfrom pathlib import Path\n\nimport torch\nimport torch.nn as nn\nfrom torch.utils.data import Dataset\n\n\nclass ProgressProbe(nn.Module):\n    \"\"\"2-layer GRU probe for progress/stagnation binary classification.\n\n    Input:  (batch, seq_len, embed_dim)\n    Output: (batch,) logits (apply sigmoid for probabilities)\n    \"\"\"\n\n    def __init__(self, embed_dim: int, hidden_size: int = 256, num_layers: int = 2, dropout: float = 0.1):\n        super().__init__()\n        self.gru = nn.GRU(\n            embed_dim,\n            hidden_size,\n            num_layers=num_layers,\n            batch_first=True,\n            dropout=dropout if num_layers > 1 else 0.0,\n        )\n        self.classifier = nn.Linear(hidden_size, 1)\n\n    def forward(self, x: torch.Tensor, lengths: torch.Tensor = None) -> torch.Tensor:\n        if lengths is not None:\n            x = nn.utils.rnn.pack_padded_sequence(x, lengths.cpu(), batch_first=True, enforce_sorted=False)\n        _, hidden = self.gru(x)\n        out = hidden[-1]  # last layer hidden: (batch, hidden_size)\n        return self.classifier(out).squeeze(-1)\n\n\nclass WindowDataset(Dataset):\n    \"\"\"Dataset of pre-computed window embeddings + binary labels.\"\"\"\n\n    def __init__(self, embeddings: list[torch.Tensor], labels: list[int]):\n        assert len(embeddings) == len(labels)\n        self.embeddings = embeddings\n        self.labels = labels\n\n    def __len__(self):\n        return len(self.labels)\n\n    def __getitem__(self, idx):\n        return self.embeddings[idx], self.labels[idx]\n\n\ndef collate_fn(batch):\n    \"\"\"Pad variable-length window embeddings to the max length in the batch.\"\"\"\n    embeddings_list, labels_list = zip(*batch)\n    lengths = torch.tensor([e.shape[0] for e in embeddings_list], dtype=torch.long)\n    max_len = lengths.max().item()\n    embed_dim = embeddings_list[0].shape[1]\n\n    padded = torch.zeros(len(batch), max_len, embed_dim)\n    for i, e in enumerate(embeddings_list):\n        padded[i, : e.shape[0]] = e\n\n    labels = torch.tensor(labels_list, dtype=torch.float32)\n    return padded, labels, lengths\n\n\ndef split_by_instance(\n    instance_ids: list[str],\n    train_ratio: float = 0.7,\n    val_ratio: float = 0.15,\n    seed: int = 42,\n) -> tuple[list[int], list[int], list[int]]:\n    \"\"\"Split indices so all windows from the same instance stay in one split.\"\"\"\n    unique = sorted(set(instance_ids))\n    rng = random.Random(seed)\n    rng.shuffle(unique)\n\n    n = len(unique)\n    n_train = int(n * train_ratio)\n    n_val = int(n * val_ratio)\n\n    train_set = set(unique[:n_train])\n    val_set = set(unique[n_train : n_train + n_val])\n\n    train_idx, val_idx, test_idx = [], [], []\n    for i, iid in enumerate(instance_ids):\n        if iid in train_set:\n            train_idx.append(i)\n        elif iid in val_set:\n            val_idx.append(i)\n        else:\n            test_idx.append(i)\n\n    return train_idx, val_idx, test_idx\n\n\ndef load_split_datasets(\n    data_path: str | Path, seed: int = 42\n) -> tuple[WindowDataset, WindowDataset, WindowDataset, dict]:\n    \"\"\"Load embeddings.pt and return train/val/test WindowDatasets + split info.\"\"\"\n    data = torch.load(data_path, weights_only=False)\n    embeddings = data[\"embeddings\"]\n    labels = data[\"labels\"]\n    instance_ids = data[\"instance_ids\"]\n\n    train_idx, val_idx, test_idx = split_by_instance(instance_ids, seed=seed)\n\n    def subset(indices):\n        return WindowDataset([embeddings[i] for i in indices], [labels[i] for i in indices])\n\n    split_info = {\n        \"train_indices\": train_idx,\n        \"val_indices\": val_idx,\n        \"test_indices\": test_idx,\n        \"seed\": seed,\n        \"embed_dim\": data[\"embed_dim\"],\n    }\n    return subset(train_idx), subset(val_idx), subset(test_idx), split_info\n\n\nif __name__ == \"__main__\":\n    print(\"=== ProgressProbe forward pass test ===\")\n    embed_dim = 1024\n    batch_size = 4\n\n    model = ProgressProbe(embed_dim=embed_dim)\n    print(f\"Model: {model}\")\n    total_params = sum(p.numel() for p in model.parameters())\n    print(f\"Total parameters: {total_params:,}\")\n\n    # Random data with variable sequence lengths\n    lengths = torch.tensor([3, 7, 5, 2])\n    max_len = lengths.max().item()\n    x = torch.randn(batch_size, max_len, embed_dim)\n    logits = model(x, lengths)\n    probs = torch.sigmoid(logits)\n\n    print(f\"Input shape:  {x.shape}\")\n    print(f\"Lengths:      {lengths.tolist()}\")\n    print(f\"Logits shape: {logits.shape}\")\n    print(f\"Logits:       {logits.tolist()}\")\n    print(f\"Probs:        {[f'{p:.4f}' for p in probs.tolist()]}\")\n\n    # Test dataset + collate\n    dummy_embeds = [torch.randn(l, embed_dim) for l in [3, 5, 2, 8]]\n    dummy_labels = [1, 0, 1, 0]\n    ds = WindowDataset(dummy_embeds, dummy_labels)\n    batch = [ds[i] for i in range(len(ds))]\n    padded, labels, lens = collate_fn(batch)\n    print(f\"\\nCollate test: padded={padded.shape}, labels={labels.shape}, lengths={lens.tolist()}\")\n\n    # Test split\n    instance_ids = [\"a\", \"a\", \"b\", \"b\", \"c\", \"c\", \"d\", \"d\", \"e\", \"e\"]\n    tr, va, te = split_by_instance(instance_ids, seed=42)\n    print(f\"\\nSplit test (10 samples, 5 instances): train={len(tr)}, val={len(va)}, test={len(te)}\")\n    print(\"All tests passed.\")\n",
      "numLines": 158,
      "startLine": 1,
      "totalLines": 158
    }
  }
}
```

</details>

---


### Assistant

_source line 114_

Now let me read the existing gold set eval file and the LLM judge baseline to understand caching format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "bf7793d0-191b-4e48-8eff-8bcf310c721f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTY1FZU4e3Hb2yRA1CTNNZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12084,
      "cache_read_input_tokens": 28604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12084
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

_source line 115_

<details open><summary>🔧 Tool call — Read · `toolu_01BzxLRjmVeyxspo6576henC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/evaluate_gold_set.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "0ceea73d-9da2-461c-a928-01273ff2c451",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTY1FZU4e3Hb2yRA1CTNNZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12084,
      "cache_read_input_tokens": 28604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12084
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

_source line 116 · 2026-05-14T22:42:03.317Z_

<details><summary>↩ Tool result · `toolu_01BzxLRjmVeyxspo6576henC`</summary>

````text
1	#!/usr/bin/env python3
2	"""Gold Set Evaluation Pipeline.
3	
4	Evaluates multiple models/label sources against human-annotated gold labels.
5	
6	Input:
7	  --gold_csv PATH   : CSV with columns (window_id, gold_label)
8	                      window_id format: {trajectory_id}__w{window_idx}
9	  --output_dir PATH : Output directory for results JSON + markdown report
10	
11	Evaluated models:
12	  1. MV labels        — majority vote from labeling functions
13	  2. probe_001        — GRU probe (checkpoints/best_model.pt)
14	  3. Structural RF    — RandomForest on hand-crafted features (trained on-the-fly)
15	  4. Structural GB    — GradientBoosting on hand-crafted features (trained on-the-fly)
16	  5. TWV labels       — Temporally-Weighted Vote σ=2 labels (data/windows_tlm_labels.jsonl)
17	
18	Output:
19	  - results.json     : Per-model metrics + gold distribution + deltas
20	  - report.md        : Human-readable markdown comparison report
21	
22	Dependencies: torch, scikit-learn, numpy
23	
24	Dry-run mode (--dry_run):
25	  Generates pseudo gold labels from conf>=2 MV labels, runs full pipeline.
26	"""
27	
28	import argparse
29	import csv
30	import json
31	import os
32	import re
33	import sys
34	import time
35	import warnings
36	from collections import Counter
37	from difflib import SequenceMatcher
38	from pathlib import Path
39	
40	import numpy as np
41	import torch
42	import torch.nn as nn
43	from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
44	from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
45	from sklearn.preprocessing import StandardScaler
46	from torch.utils.data import DataLoader
47	
48	warnings.filterwarnings("ignore", category=UserWarning)
49	
50	# ---------------------------------------------------------------------------
51	# Import probe model from project
52	# ---------------------------------------------------------------------------
53	sys.path.insert(0, str(Path(__file__).parent))
54	from probe_model import ProgressProbe, WindowDataset, collate_fn
55	
56	
57	# ===========================================================================
58	# Metrics
59	# ===========================================================================
60	
61	def compute_metrics(y_true, y_pred):
62	    return {
63	        "macro_f1": f1_score(y_true, y_pred, average="macro", zero_division=0),
64	        "f1_stag": f1_score(y_true, y_pred, pos_label=0, zero_division=0),
65	        "f1_prog": f1_score(y_true, y_pred, pos_label=1, zero_division=0),
66	        "precision_stag": precision_score(y_true, y_pred, pos_label=0, zero_division=0),
67	        "recall_stag": recall_score(y_true, y_pred, pos_label=0, zero_division=0),
68	        "accuracy": accuracy_score(y_true, y_pred),
69	    }
70	
71	
72	# ===========================================================================
73	# Structural feature extraction (from non_nlp_baseline.py)
74	# ===========================================================================
75	
76	EDIT_CMDS = {"edit", "str_replace", "create", "insert"}
77	SEARCH_CMDS = {"search_dir", "search_file", "find_file", "find", "grep", "view"}
78	NAV_CMDS = {"open", "goto", "scroll_down", "scroll_up", "cd", "ls", "cat"}
79	
80	
81	def _extract_command(text):
82	    match = re.search(r"```\n?(.*?)```", text, re.DOTALL)
83	    return match.group(1).strip() if match else None
84	
85	
86	def _cmd_similarity(a, b):
87	    if a == b:
88	        return 1.0
89	    if not a or not b:
90	        return 0.0
91	    return SequenceMatcher(None, a, b).ratio()
92	
93	
94	def extract_structural_features(steps, is_short):
95	    n = len(steps)
96	    if n == 0:
97	        return np.zeros(30, dtype=np.float32)
98	
99	    texts = [s["text"] for s in steps]
100	    text_lens = [len(t) for t in texts]
101	    actions = [(s, t) for s, t in zip(steps, texts) if s["role"] == "ai"]
102	    observations = [(s, t) for s, t in zip(steps, texts) if s["role"] == "user"]
103	    n_actions = len(actions)
104	    n_obs = len(observations)
105	
106	    mean_tlen = np.mean(text_lens)
107	    std_tlen = np.std(text_lens) if n > 1 else 0.0
108	    max_tlen = max(text_lens)
109	    min_tlen = min(text_lens)
110	    action_lens = [len(t) for _, t in actions] if actions else [0]
111	    obs_lens = [len(t) for _, t in observations] if observations else [0]
112	    mean_action_len = np.mean(action_lens)
113	    mean_obs_len = np.mean(obs_lens)
114	
115	    if n > 1:
116	        x = np.arange(n, dtype=float)
117	        y = np.array(text_lens, dtype=float)
118	        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (n * np.dot(x, x) - x.sum() ** 2 + 1e-9)
119	    else:
120	        slope = 0.0
121	
122	    commands = []
123	    for s, t in actions:
124	        cmd = _extract_command(t)
125	        if cmd:
126	            commands.append(cmd)
127	    n_cmds = len(commands)
128	    cmd_lens = [len(c) for c in commands] if commands else [0]
129	    mean_cmd_len = np.mean(cmd_lens)
130	    max_cmd_len = max(cmd_lens) if cmd_lens else 0
131	
132	    if n_cmds > 0:
133	        unique_cmds = len(set(commands))
134	        unique_cmd_ratio = unique_cmds / n_cmds
135	        cmd_counter = Counter(commands)
136	        max_repeat = cmd_counter.most_common(1)[0][1]
137	        repeat_ratio = max_repeat / n_cmds
138	    else:
139	        unique_cmd_ratio = 1.0
140	        repeat_ratio = 0.0
141	
142	    n_edit = n_search = n_nav = n_submit = 0
143	    for cmd in commands:
144	        first_word = cmd.strip().split()[0] if cmd.strip() else ""
145	        if first_word in EDIT_CMDS:
146	            n_edit += 1
147	        elif first_word in SEARCH_CMDS:
148	            n_search += 1
149	        elif first_word in NAV_CMDS:
150	            n_nav += 1
151	        elif first_word == "submit":
152	            n_submit += 1
153	    edit_ratio = n_edit / max(n_cmds, 1)
154	    search_ratio = n_search / max(n_cmds, 1)
155	
156	    if n_cmds >= 2:
157	        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]
158	        avg_adj_sim = np.mean(sims)
159	        max_adj_sim = max(sims)
160	        max_run, cur_run = 1, 1
161	        for s in sims:
162	            if s >= 0.9:
163	                cur_run += 1
164	                max_run = max(max_run, cur_run)
165	            else:
166	                cur_run = 1
167	    else:
168	        avg_adj_sim = max_adj_sim = 0.0
169	        max_run = 0
170	
171	    n_errors = sum(1 for t in texts if "Traceback" in t or "Error" in t)
172	    n_test_output = sum(1 for t in texts if ("PASSED" in t or "FAILED" in t) and "test" in t.lower())
173	    n_file_display = sum(1 for t in texts if "[File:" in t)
174	    n_nonzero_exit = sum(
175	        1 for _, t in observations if re.search(r"exit code [1-9]|returned non-zero|command not found", t)
176	    )
177	
178	    return np.array([
179	        n, n_actions, n_obs, n_actions / max(n, 1),
180	        mean_tlen, std_tlen, max_tlen, min_tlen,
181	        mean_action_len, mean_obs_len, slope,
182	        n_cmds, mean_cmd_len, max_cmd_len,
183	        unique_cmd_ratio, repeat_ratio,
184	        n_edit, n_search, n_nav, n_submit,
185	        edit_ratio, search_ratio,
186	        avg_adj_sim, max_adj_sim, max_run,
187	        n_errors, n_test_output, n_file_display, n_nonzero_exit,
188	        float(is_short),
189	    ], dtype=np.float32)
190	
191	
192	# ===========================================================================
193	# Data loading helpers
194	# ===========================================================================
195	
196	def load_windows_jsonl(path):
197	    windows = []
198	    with open(path) as f:
199	        for line in f:
200	            line = line.strip()
201	            if line:
202	                windows.append(json.loads(line))
203	    return windows
204	
205	
206	def build_trajectory_index(traj_path):
207	    index = {}
208	    with open(traj_path) as f:
209	        for row_idx, line in enumerate(f):
210	            line = line.strip()
211	            if not line:
212	                continue
213	            raw = json.loads(line)
214	            steps = []
215	            for s in raw.get("trajectory") or []:
216	                steps.append({
217	                    "role": s.get("role", "unknown"),
218	                    "text": s.get("text") or s.get("system_prompt") or "",
219	                })
220	            index[row_idx] = steps
221	    return index
222	
223	
224	def window_id(w):
225	    return f"{w['trajectory_id']}__w{w['window_idx']}"
226	
227	
228	def parse_row_index(trajectory_id):
229	    return int(trajectory_id.rsplit("__r", 1)[1])
230	
231	
232	# ===========================================================================
233	# Evaluators
234	# ===========================================================================
235	
236	def evaluate_mv(gold_wids, gold_labels, wid_to_window):
237	    preds = []
238	    valid_gold = []
239	    for wid, gl in zip(gold_wids, gold_labels):
240	        w = wid_to_window.get(wid)
241	        if w is None:
242	            continue
243	        preds.append(w["majority_label"])
244	        valid_gold.append(gl)
245	    if not preds:
246	        return None, 0
247	    return compute_metrics(valid_gold, preds), len(preds)
248	
249	
250	def evaluate_twv(gold_wids, gold_labels, wid_to_twv):
251	    preds = []
252	    valid_gold = []
253	    for wid, gl in zip(gold_wids, gold_labels):
254	        twv = wid_to_twv.get(wid)
255	        if twv is None:
256	            continue
257	        preds.append(twv["twv_label"])
258	        valid_gold.append(gl)
259	    if not preds:
260	        return None, 0
261	    return compute_metrics(valid_gold, preds), len(preds)
262	
263	
264	@torch.no_grad()
265	def evaluate_probe_model(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):
266	    if not os.path.exists(ckpt_path):
267	        return None, 0
268	
269	    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)
270	    model = ProgressProbe(
271	        embed_dim=ckpt["embed_dim"],
272	        hidden_size=ckpt["hidden_size"],
273	        num_layers=ckpt["num_layers"],
274	    ).to(device)
275	    model.load_state_dict(ckpt["model_state_dict"])
276	    model.eval()
277	
278	    gold_embs = []
279	    valid_gold = []
280	    for wid, gl in zip(gold_wids, gold_labels):
281	        idx = wid_to_emb_idx.get(wid)
282	        if idx is None:
283	            continue
284	        gold_embs.append(embeddings[idx])
285	        valid_gold.append(gl)
286	
287	    if not gold_embs:
288	        return None, 0
289	
290	    ds = WindowDataset(gold_embs, valid_gold)
291	    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)
292	
293	    all_preds = []
294	    all_labels = []
295	    for padded, labels, lengths in loader:
296	        logits = model(padded.to(device), lengths)
297	        preds = (torch.sigmoid(logits) >= 0.5).long().cpu()
298	        all_preds.extend(preds.tolist())
299	        all_labels.extend(labels.long().tolist())
300	
301	    return compute_metrics(all_labels, all_preds), len(all_preds)
302	
303	
304	def evaluate_structural(
305	    gold_wids, gold_labels, wid_to_noabs_idx,
306	    all_features, all_mv_labels, split_info, model_cls, model_kwargs, use_scaler=False,
307	):
308	    keep_indices = split_info.get("keep_indices")
309	    if keep_indices is not None:
310	        feat_subset = all_features[keep_indices]
311	        label_subset = np.array(all_mv_labels)[keep_indices]
312	    else:
313	        feat_subset = all_features
314	        label_subset = np.array(all_mv_labels)
315	
316	    train_idx = split_info["train_indices"]
317	    X_train = feat_subset[train_idx]
318	    y_train = label_subset[train_idx]
319	
320	    scaler = None
321	    if use_scaler:
322	        scaler = StandardScaler()
323	        X_train = scaler.fit_transform(X_train)
324	
325	    clf = model_cls(**model_kwargs)
326	    clf.fit(X_train, y_train)
327	
328	    gold_feats = []
329	    valid_gold = []
330	    for wid, gl in zip(gold_wids, gold_labels):
331	        idx = wid_to_noabs_idx.get(wid)
332	        if idx is None:
333	            continue
334	        gold_feats.append(all_features[idx])
335	        valid_gold.append(gl)
336	
337	    if not gold_feats:
338	        return None, 0
339	
340	    X_gold = np.stack(gold_feats)
341	    if scaler is not None:
342	        X_gold = scaler.transform(X_gold)
343	    preds = clf.predict(X_gold).tolist()
344	
345	    return compute_metrics(valid_gold, preds), len(preds)
346	
347	
348	# ===========================================================================
349	# Dry-run: generate pseudo gold CSV
350	# ===========================================================================
351	
352	def generate_pseudo_gold(windows, min_confidence=2):
353	    rows = []
354	    for w in windows:
355	        if w.get("majority_label", -1) == -1:
356	            continue
357	        if w.get("confidence", 0) >= min_confidence:
358	            rows.append((window_id(w), w["majority_label"]))
359	    return rows
360	
361	
362	# ===========================================================================
363	# Report generation
364	# ===========================================================================
365	
366	def generate_report(results, gold_dist, mv_gold_agreement, output_dir):
367	    lines = ["# Gold Set Evaluation Report\n"]
368	    lines.append(f"**Date**: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
369	
370	    lines.append("## Gold Label Distribution\n")
371	    total = gold_dist.get("total", 0)
372	    n_stag = gold_dist.get("stagnation", 0)
373	    n_prog = gold_dist.get("progress", 0)
374	    lines.append(f"- Total gold windows: **{total}**")
375	    lines.append(f"- Stagnation (0): **{n_stag}** ({100*n_stag/max(total,1):.1f}%)")
376	    lines.append(f"- Progress (1): **{n_prog}** ({100*n_prog/max(total,1):.1f}%)\n")
377	
378	    lines.append("## Per-Model Results vs Gold\n")
379	    header = "| Model | N | Macro-F1 | F1(stag) | F1(prog) | Prec(stag) | Rec(stag) | Accuracy |"
380	    sep = "|---|---|---|---|---|---|---|---|"
381	    lines.append(header)
382	    lines.append(sep)
383	    for name, metrics, n in results:
384	        if metrics is None:
385	            lines.append(f"| {name} | — | SKIPPED | | | | | |")
386	            continue
387	        lines.append(
388	            f"| {name} | {n} "
389	            f"| {metrics['macro_f1']:.4f} "
390	            f"| {metrics['f1_stag']:.4f} "
391	            f"| {metrics['f1_prog']:.4f} "
392	            f"| {metrics['precision_stag']:.4f} "
393	            f"| {metrics['recall_stag']:.4f} "
394	            f"| {metrics['accuracy']:.4f} |"
395	        )
396	    lines.append("")
397	
398	    if mv_gold_agreement is not None:
399	        lines.append("## MV vs Gold Agreement (Circular Eval Indicator)\n")
400	        lines.append(f"- MV-Gold agreement rate: **{mv_gold_agreement['agreement_rate']:.4f}**")
401	        lines.append(f"- MV-Gold disagreement count: **{mv_gold_agreement['n_disagree']}** / {mv_gold_agreement['n_total']}")
402	        lines.append(f"- Implication: models trained on MV labels have a ceiling of ~{mv_gold_agreement['agreement_rate']:.1%} accuracy when evaluated against gold.\n")
403	
404	    mv_metrics = None
405	    for name, m, _ in results:
406	        if name == "MV Labels" and m is not None:
407	            mv_metrics = m
408	            break
409	
410	    if mv_metrics is not None:
411	        lines.append("## MV-derived vs Gold-derived Metric Deltas\n")
412	        lines.append("Shows how much each model's gold-eval metrics differ from its MV-eval metrics.")
413	        lines.append("Positive delta = gold metric higher than MV metric.\n")
414	        lines.append("| Model | Δ Macro-F1 | Δ F1(stag) | Δ Accuracy |")
415	        lines.append("|---|---|---|---|")
416	        for name, metrics, _ in results:
417	            if metrics is None or name == "MV Labels":
418	                continue
419	            lines.append(
420	                f"| {name} "
421	                f"| — | — | — |"
422	            )
423	        lines.append("")
424	        lines.append("*(Full MV-derived metrics will be computed when original test-set results are available.)*\n")
425	
426	    report_text = "\n".join(lines)
427	    report_path = Path(output_dir) / "report.md"
428	    report_path.write_text(report_text)
429	    return report_path
430	
431	
432	# ===========================================================================
433	# Main
434	# ===========================================================================
435	
436	def main():
437	    parser = argparse.ArgumentParser(description="Evaluate models against gold labels")
438	    parser.add_argument("--gold_csv", type=str, default=None, help="Gold labels CSV (window_id, gold_label)")
439	    parser.add_argument("--output_dir", type=str, required=True, help="Output directory")
440	    parser.add_argument("--data_dir", type=str, default="data", help="Data directory")
441	    parser.add_argument("--checkpoint", type=str, default="checkpoints/best_model.pt", help="GRU probe checkpoint")
442	    parser.add_argument("--twv_checkpoint", type=str, default="checkpoints_tlm_twv/best_model.pt", help="TWV probe checkpoint")
443	    parser.add_argument("--split_info", type=str, default="checkpoints/split_info.json", help="Split info JSON")
444	    parser.add_argument("--trajectories", type=str, default="data/swe_agent_trajectories_5000.jsonl", help="Raw trajectories")
445	    parser.add_argument("--device", type=str, default=None, help="Device (e.g. cuda:1)")
446	    parser.add_argument("--dry_run", action="store_true", help="Generate pseudo gold from conf>=2 MV labels")
447	    parser.add_argument("--dry_run_min_conf", type=int, default=2, help="Min confidence for dry-run pseudo gold")
448	    args = parser.parse_args()
449	
450	    t_start = time.time()
451	    base_dir = Path(__file__).parent
452	    data_dir = base_dir / args.data_dir
453	    output_dir = Path(args.output_dir)
454	    output_dir.mkdir(parents=True, exist_ok=True)
455	
456	    device = args.device or ("cuda" if torch.cuda.is_available() else "cpu")
457	    print(f"Device: {device}")
458	
459	    # ------------------------------------------------------------------
460	    # 1. Load windows
461	    # ------------------------------------------------------------------
462	    print("Loading windows_labeled.jsonl ...")
463	    all_windows = load_windows_jsonl(data_dir / "windows_labeled.jsonl")
464	    non_abstain = [w for w in all_windows if w.get("majority_label", -1) != -1]
465	    print(f"  Total windows: {len(all_windows)}, non-abstain: {len(non_abstain)}")
466	
467	    wid_to_window = {window_id(w): w for w in non_abstain}
468	    wid_to_noabs_idx = {window_id(w): i for i, w in enumerate(non_abstain)}
469	
470	    # ------------------------------------------------------------------
471	    # 2. Load or generate gold labels
472	    # ------------------------------------------------------------------
473	    if args.dry_run:
474	        print(f"DRY RUN: generating pseudo gold from conf>={args.dry_run_min_conf} MV labels ...")
475	        pseudo_gold = generate_pseudo_gold(all_windows, min_confidence=args.dry_run_min_conf)
476	        gold_wids = [wid for wid, _ in pseudo_gold]
477	        gold_labels = [label for _, label in pseudo_gold]
478	        print(f"  Pseudo gold windows: {len(gold_wids)}")
479	
480	        csv_path = output_dir / "pseudo_gold.csv"
481	        with open(csv_path, "w", newline="") as f:
482	            writer = csv.writer(f)
483	            writer.writerow(["window_id", "gold_label"])
484	            for wid, label in pseudo_gold:
485	                writer.writerow([wid, label])
486	        print(f"  Saved pseudo gold CSV: {csv_path}")
487	    else:
488	        if args.gold_csv is None:
489	            print("ERROR: --gold_csv required when not in --dry_run mode")
490	            sys.exit(1)
491	        print(f"Loading gold CSV: {args.gold_csv}")
492	        gold_wids = []
493	        gold_labels = []
494	        with open(args.gold_csv) as f:
495	            reader = csv.DictReader(f)
496	            for row in reader:
497	                gold_wids.append(row["window_id"])
498	                gold_labels.append(int(row["gold_label"]))
499	        print(f"  Gold windows: {len(gold_wids)}")
500	
501	    gold_dist = {
502	        "total": len(gold_labels),
503	        "stagnation": sum(1 for l in gold_labels if l == 0),
504	        "progress": sum(1 for l in gold_labels if l == 1),
505	    }
506	    print(f"  Distribution: stag={gold_dist['stagnation']}, prog={gold_dist['progress']}")
507	
508	    # ------------------------------------------------------------------
509	    # 3. Load embeddings
510	    # ------------------------------------------------------------------
511	    print("Loading embeddings.pt ...")
512	    emb_data = torch.load(data_dir / "embeddings.pt", map_location="cpu", weights_only=False)
513	    embeddings = emb_data["embeddings"]
514	    emb_trajectory_ids = emb_data.get("trajectory_ids", [])
515	    print(f"  Embeddings loaded: {len(embeddings)}")
516	
517	    wid_to_emb_idx = {}
518	    if len(emb_trajectory_ids) == len(non_abstain):
519	        for i, w in enumerate(non_abstain):
520	            wid_to_emb_idx[window_id(w)] = i
521	    else:
522	        print(f"  WARNING: embedding count ({len(embeddings)}) != non_abstain ({len(non_abstain)}), building fallback index")
523	        for i in range(len(embeddings)):
524	            if i < len(non_abstain):
525	                wid_to_emb_idx[window_id(non_abstain[i])] = i
526	
527	    # ------------------------------------------------------------------
528	    # 4. Load split info
529	    # ------------------------------------------------------------------
530	    split_info_path = base_dir / args.split_info
531	    print(f"Loading split info: {split_info_path}")
532	    with open(split_info_path) as f:
533	        split_info = json.load(f)
534	
535	    # ------------------------------------------------------------------
536	    # 5. Evaluate each model
537	    # ------------------------------------------------------------------
538	    results = []
539	
540	    # --- 5a. MV Labels ---
541	    print("\n[1/5] Evaluating MV Labels vs Gold ...")
542	    mv_metrics, mv_n = evaluate_mv(gold_wids, gold_labels, wid_to_window)
543	    if mv_metrics:
544	        print(f"  macro_f1={mv_metrics['macro_f1']:.4f}, accuracy={mv_metrics['accuracy']:.4f}, n={mv_n}")
545	    else:
546	        print("  SKIPPED: no matching windows")
547	    results.append(("MV Labels", mv_metrics, mv_n))
548	
549	    # --- 5b. GRU Probe ---
550	    probe_ckpt = base_dir / args.checkpoint
551	    print(f"\n[2/5] Evaluating GRU Probe vs Gold ...")
552	    if probe_ckpt.exists():
553	        probe_metrics, probe_n = evaluate_probe_model(
554	            gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(probe_ckpt), device
555	        )
556	        if probe_metrics:
557	            print(f"  macro_f1={probe_metrics['macro_f1']:.4f}, accuracy={probe_metrics['accuracy']:.4f}, n={probe_n}")
558	        else:
559	            print("  SKIPPED: no matching gold windows in embeddings")
560	    else:
561	        print(f"  SKIPPED: checkpoint not found at {probe_ckpt}")
562	        probe_metrics, probe_n = None, 0
563	    results.append(("GRU Probe", probe_metrics, probe_n))
564	
565	    # --- 5c/5d. Structural RF & GB ---
566	    traj_path = base_dir / args.trajectories
567	    struct_available = traj_path.exists()
568	    if struct_available:
569	        print(f"\n[3-4/5] Building structural features ...")
570	        traj_index = build_trajectory_index(str(traj_path))
571	        print(f"  Indexed {len(traj_index)} trajectories")
572	
573	        all_features = []
574	        all_mv_labels = []
575	        for w in non_abstain:
576	            row_idx = w.get("row_index", 0)
577	            step_indices = w["step_indices"]
578	            traj_steps = traj_index.get(row_idx, [])
579	            window_steps = []
580	            for si in step_indices:
581	                if si < len(traj_steps):
582	                    window_steps.append(traj_steps[si])
583	                else:
584	                    window_steps.append({"role": "unknown", "text": ""})
585	            feat = extract_structural_features(window_steps, w.get("short_trajectory", False))
586	            all_features.append(feat)
587	            all_mv_labels.append(w["majority_label"])
588	
589	        all_features = np.stack(all_features)
590	        print(f"  Feature matrix: {all_features.shape}")
591	
592	        # RF
593	        print("  Evaluating Structural RF ...")
594	        rf_metrics, rf_n = evaluate_structural(
595	            gold_wids, gold_labels, wid_to_noabs_idx,
596	            all_features, all_mv_labels, split_info,
597	            RandomForestClassifier,
598	            {"n_estimators": 200, "max_depth": 10, "random_state": 42, "n_jobs": -1},
599	        )
600	        if rf_metrics:
601	            print(f"  RF: macro_f1={rf_metrics['macro_f1']:.4f}, accuracy={rf_metrics['accuracy']:.4f}, n={rf_n}")
602	        else:
603	            print("  RF: SKIPPED")
604	        results.append(("Structural RF", rf_metrics, rf_n))
605	
606	        # GB
607	        print("  Evaluating Structural GB ...")
608	        gb_metrics, gb_n = evaluate_structural(
609	            gold_wids, gold_labels, wid_to_noabs_idx,
610	            all_features, all_mv_labels, split_info,
611	            GradientBoostingClassifier,
612	            {"n_estimators": 200, "learning_rate": 0.1, "max_depth": 5, "random_state": 42},
613	        )
614	        if gb_metrics:
615	            print(f"  GB: macro_f1={gb_metrics['macro_f1']:.4f}, accuracy={gb_metrics['accuracy']:.4f}, n={gb_n}")
616	        else:
617	            print("  GB: SKIPPED")
618	        results.append(("Structural GB", gb_metrics, gb_n))
619	    else:
620	        print(f"\n[3-4/5] SKIPPED structural baselines: {traj_path} not found")
621	        results.append(("Structural RF", None, 0))
622	        results.append(("Structural GB", None, 0))
623	
624	    # --- 5e. TWV Labels ---
625	    twv_labels_path = data_dir / "windows_tlm_labels.jsonl"
626	    print(f"\n[5/5] Evaluating TWV Labels vs Gold ...")
627	    if twv_labels_path.exists():
628	        twv_windows = load_windows_jsonl(str(twv_labels_path))
629	        wid_to_twv = {}
630	        for w in twv_windows:
631	            wid = f"{w['trajectory_id']}__w{w['window_idx']}"
632	            wid_to_twv[wid] = w
633	        twv_metrics, twv_n = evaluate_twv(gold_wids, gold_labels, wid_to_twv)
634	        if twv_metrics:
635	            print(f"  macro_f1={twv_metrics['macro_f1']:.4f}, accuracy={twv_metrics['accuracy']:.4f}, n={twv_n}")
636	        else:
637	            print("  SKIPPED: no matching windows")
638	    else:
639	        print(f"  SKIPPED: {twv_labels_path} not found")
640	        twv_metrics, twv_n = None, 0
641	    results.append(("TWV Labels", twv_metrics, twv_n))
642	
643	    # --- 5f. TWV Probe (bonus) ---
644	    twv_ckpt = base_dir / args.twv_checkpoint
645	    if twv_ckpt.exists():
646	        twv_emb_path = base_dir / "data_tlm_twv" / "embeddings.pt"
647	        if twv_emb_path.exists():
648	            print("\n[bonus] Evaluating TWV Probe vs Gold ...")
649	            twv_emb_data = torch.load(twv_emb_path, map_location="cpu", weights_only=False)
650	            twv_embeddings = twv_emb_data["embeddings"]
651	
652	            twv_wid_to_emb_idx = {}
653	            twv_all_windows = load_windows_jsonl(str(twv_labels_path)) if twv_labels_path.exists() else []
654	            twv_non_abstain = [w for w in twv_all_windows if w.get("mv_label", -1) != -1]
655	            if len(twv_embeddings) == len(twv_non_abstain):
656	                for i, w in enumerate(twv_non_abstain):
657	                    wid = f"{w['trajectory_id']}__w{w['window_idx']}"
658	                    twv_wid_to_emb_idx[wid] = i
659	            else:
660	                for i, w in enumerate(non_abstain):
661	                    if i < len(twv_embeddings):
662	                        twv_wid_to_emb_idx[window_id(w)] = i
663	
664	            twv_probe_metrics, twv_probe_n = evaluate_probe_model(
665	                gold_wids, gold_labels, twv_wid_to_emb_idx, twv_embeddings, str(twv_ckpt), device
666	            )
667	            if twv_probe_metrics:
668	                print(f"  macro_f1={twv_probe_metrics['macro_f1']:.4f}, accuracy={twv_probe_metrics['accuracy']:.4f}, n={twv_probe_n}")
669	                results.append(("TWV Probe", twv_probe_metrics, twv_probe_n))
670	            else:
671	                print("  SKIPPED: no matching windows")
672	
673	    # ------------------------------------------------------------------
674	    # 6. MV-Gold agreement
675	    # ------------------------------------------------------------------
676	    n_agree = 0
677	    n_total = 0
678	    for wid, gl in zip(gold_wids, gold_labels):
679	        w = wid_to_window.get(wid)
680	        if w is None:
681	            continue
682	        n_total += 1
683	        if w["majority_label"] == gl:
684	            n_agree += 1
685	    mv_gold_agreement = {
686	        "agreement_rate": n_agree / max(n_total, 1),
687	        "n_agree": n_agree,
688	        "n_disagree": n_total - n_agree,
689	        "n_total": n_total,
690	    }
691	    print(f"\nMV-Gold agreement: {n_agree}/{n_total} = {mv_gold_agreement['agreement_rate']:.4f}")
692	
693	    # ------------------------------------------------------------------
694	    # 7. Output
695	    # ------------------------------------------------------------------
696	    elapsed = time.time() - t_start
697	
698	    output = {
699	        "gold_distribution": gold_dist,
700	        "mv_gold_agreement": mv_gold_agreement,
701	        "models": {},
702	        "elapsed_seconds": round(elapsed, 2),
703	        "dry_run": args.dry_run,
704	    }
705	    for name, metrics, n in results:
706	        output["models"][name] = {
707	            "n_evaluated": n,
708	            "metrics": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,
709	        }
710	
711	    json_path = output_dir / "results.json"
712	    with open(json_path, "w") as f:
713	        json.dump(output, f, indent=2)
714	    print(f"\nResults JSON: {json_path}")
715	
716	    report_path = generate_report(results, gold_dist, mv_gold_agreement, output_dir)
717	    print(f"Report: {report_path}")
718	    print(f"\nTotal elapsed: {elapsed:.1f}s")
719	
720	
721	if __name__ == "__main__":
722	    main()
723	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "7ef7902a-70ab-42e5-a993-adb73bb58427",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/evaluate_gold_set.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Gold Set Evaluation Pipeline.\n\nEvaluates multiple models/label sources against human-annotated gold labels.\n\nInput:\n  --gold_csv PATH   : CSV with columns (window_id, gold_label)\n                      window_id format: {trajectory_id}__w{window_idx}\n  --output_dir PATH : Output directory for results JSON + markdown report\n\nEvaluated models:\n  1. MV labels        — majority vote from labeling functions\n  2. probe_001        — GRU probe (checkpoints/best_model.pt)\n  3. Structural RF    — RandomForest on hand-crafted features (trained on-the-fly)\n  4. Structural GB    — GradientBoosting on hand-crafted features (trained on-the-fly)\n  5. TWV labels       — Temporally-Weighted Vote σ=2 labels (data/windows_tlm_labels.jsonl)\n\nOutput:\n  - results.json     : Per-model metrics + gold distribution + deltas\n  - report.md        : Human-readable markdown comparison report\n\nDependencies: torch, scikit-learn, numpy\n\nDry-run mode (--dry_run):\n  Generates pseudo gold labels from conf>=2 MV labels, runs full pipeline.\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport os\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter\nfrom difflib import SequenceMatcher\nfrom pathlib import Path\n\nimport numpy as np\nimport torch\nimport torch.nn as nn\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score\nfrom sklearn.preprocessing import StandardScaler\nfrom torch.utils.data import DataLoader\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Import probe model from project\n# ---------------------------------------------------------------------------\nsys.path.insert(0, str(Path(__file__).parent))\nfrom probe_model import ProgressProbe, WindowDataset, collate_fn\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (from non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (n * np.dot(x, x) - x.sum() ** 2 + 1e-9)\n    else:\n        slope = 0.0\n\n    commands = []\n    for s, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower())\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1 for _, t in observations if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    return np.array([\n        n, n_actions, n_obs, n_actions / max(n, 1),\n        mean_tlen, std_tlen, max_tlen, min_tlen,\n        mean_action_len, mean_obs_len, slope,\n        n_cmds, mean_cmd_len, max_cmd_len,\n        unique_cmd_ratio, repeat_ratio,\n        n_edit, n_search, n_nav, n_submit,\n        edit_ratio, search_ratio,\n        avg_adj_sim, max_adj_sim, max_run,\n        n_errors, n_test_output, n_file_display, n_nonzero_exit,\n        float(is_short),\n    ], dtype=np.float32)\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append({\n                    \"role\": s.get(\"role\", \"unknown\"),\n                    \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                })\n            index[row_idx] = steps\n    return index\n\n\ndef window_id(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Evaluators\n# ===========================================================================\n\ndef evaluate_mv(gold_wids, gold_labels, wid_to_window):\n    preds = []\n    valid_gold = []\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        preds.append(w[\"majority_label\"])\n        valid_gold.append(gl)\n    if not preds:\n        return None, 0\n    return compute_metrics(valid_gold, preds), len(preds)\n\n\ndef evaluate_twv(gold_wids, gold_labels, wid_to_twv):\n    preds = []\n    valid_gold = []\n    for wid, gl in zip(gold_wids, gold_labels):\n        twv = wid_to_twv.get(wid)\n        if twv is None:\n            continue\n        preds.append(twv[\"twv_label\"])\n        valid_gold.append(gl)\n    if not preds:\n        return None, 0\n    return compute_metrics(valid_gold, preds), len(preds)\n\n\n@torch.no_grad()\ndef evaluate_probe_model(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    if not os.path.exists(ckpt_path):\n        return None, 0\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    gold_embs = []\n    valid_gold = []\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            continue\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_labels = []\n    for padded, labels, lengths in loader:\n        logits = model(padded.to(device), lengths)\n        preds = (torch.sigmoid(logits) >= 0.5).long().cpu()\n        all_preds.extend(preds.tolist())\n        all_labels.extend(labels.long().tolist())\n\n    return compute_metrics(all_labels, all_preds), len(all_preds)\n\n\ndef evaluate_structural(\n    gold_wids, gold_labels, wid_to_noabs_idx,\n    all_features, all_mv_labels, split_info, model_cls, model_kwargs, use_scaler=False,\n):\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    gold_feats = []\n    valid_gold = []\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        gold_feats.append(all_features[idx])\n        valid_gold.append(gl)\n\n    if not gold_feats:\n        return None, 0\n\n    X_gold = np.stack(gold_feats)\n    if scaler is not None:\n        X_gold = scaler.transform(X_gold)\n    preds = clf.predict(X_gold).tolist()\n\n    return compute_metrics(valid_gold, preds), len(preds)\n\n\n# ===========================================================================\n# Dry-run: generate pseudo gold CSV\n# ===========================================================================\n\ndef generate_pseudo_gold(windows, min_confidence=2):\n    rows = []\n    for w in windows:\n        if w.get(\"majority_label\", -1) == -1:\n            continue\n        if w.get(\"confidence\", 0) >= min_confidence:\n            rows.append((window_id(w), w[\"majority_label\"]))\n    return rows\n\n\n# ===========================================================================\n# Report generation\n# ===========================================================================\n\ndef generate_report(results, gold_dist, mv_gold_agreement, output_dir):\n    lines = [\"# Gold Set Evaluation Report\\n\"]\n    lines.append(f\"**Date**: {time.strftime('%Y-%m-%d %H:%M:%S')}\\n\")\n\n    lines.append(\"## Gold Label Distribution\\n\")\n    total = gold_dist.get(\"total\", 0)\n    n_stag = gold_dist.get(\"stagnation\", 0)\n    n_prog = gold_dist.get(\"progress\", 0)\n    lines.append(f\"- Total gold windows: **{total}**\")\n    lines.append(f\"- Stagnation (0): **{n_stag}** ({100*n_stag/max(total,1):.1f}%)\")\n    lines.append(f\"- Progress (1): **{n_prog}** ({100*n_prog/max(total,1):.1f}%)\\n\")\n\n    lines.append(\"## Per-Model Results vs Gold\\n\")\n    header = \"| Model | N | Macro-F1 | F1(stag) | F1(prog) | Prec(stag) | Rec(stag) | Accuracy |\"\n    sep = \"|---|---|---|---|---|---|---|---|\"\n    lines.append(header)\n    lines.append(sep)\n    for name, metrics, n in results:\n        if metrics is None:\n            lines.append(f\"| {name} | — | SKIPPED | | | | | |\")\n            continue\n        lines.append(\n            f\"| {name} | {n} \"\n            f\"| {metrics['macro_f1']:.4f} \"\n            f\"| {metrics['f1_stag']:.4f} \"\n            f\"| {metrics['f1_prog']:.4f} \"\n            f\"| {metrics['precision_stag']:.4f} \"\n            f\"| {metrics['recall_stag']:.4f} \"\n            f\"| {metrics['accuracy']:.4f} |\"\n        )\n    lines.append(\"\")\n\n    if mv_gold_agreement is not None:\n        lines.append(\"## MV vs Gold Agreement (Circular Eval Indicator)\\n\")\n        lines.append(f\"- MV-Gold agreement rate: **{mv_gold_agreement['agreement_rate']:.4f}**\")\n        lines.append(f\"- MV-Gold disagreement count: **{mv_gold_agreement['n_disagree']}** / {mv_gold_agreement['n_total']}\")\n        lines.append(f\"- Implication: models trained on MV labels have a ceiling of ~{mv_gold_agreement['agreement_rate']:.1%} accuracy when evaluated against gold.\\n\")\n\n    mv_metrics = None\n    for name, m, _ in results:\n        if name == \"MV Labels\" and m is not None:\n            mv_metrics = m\n            break\n\n    if mv_metrics is not None:\n        lines.append(\"## MV-derived vs Gold-derived Metric Deltas\\n\")\n        lines.append(\"Shows how much each model's gold-eval metrics differ from its MV-eval metrics.\")\n        lines.append(\"Positive delta = gold metric higher than MV metric.\\n\")\n        lines.append(\"| Model | Δ Macro-F1 | Δ F1(stag) | Δ Accuracy |\")\n        lines.append(\"|---|---|---|---|\")\n        for name, metrics, _ in results:\n            if metrics is None or name == \"MV Labels\":\n                continue\n            lines.append(\n                f\"| {name} \"\n                f\"| — | — | — |\"\n            )\n        lines.append(\"\")\n        lines.append(\"*(Full MV-derived metrics will be computed when original test-set results are available.)*\\n\")\n\n    report_text = \"\\n\".join(lines)\n    report_path = Path(output_dir) / \"report.md\"\n    report_path.write_text(report_text)\n    return report_path\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Evaluate models against gold labels\")\n    parser.add_argument(\"--gold_csv\", type=str, default=None, help=\"Gold labels CSV (window_id, gold_label)\")\n    parser.add_argument(\"--output_dir\", type=str, required=True, help=\"Output directory\")\n    parser.add_argument(\"--data_dir\", type=str, default=\"data\", help=\"Data directory\")\n    parser.add_argument(\"--checkpoint\", type=str, default=\"checkpoints/best_model.pt\", help=\"GRU probe checkpoint\")\n    parser.add_argument(\"--twv_checkpoint\", type=str, default=\"checkpoints_tlm_twv/best_model.pt\", help=\"TWV probe checkpoint\")\n    parser.add_argument(\"--split_info\", type=str, default=\"checkpoints/split_info.json\", help=\"Split info JSON\")\n    parser.add_argument(\"--trajectories\", type=str, default=\"data/swe_agent_trajectories_5000.jsonl\", help=\"Raw trajectories\")\n    parser.add_argument(\"--device\", type=str, default=None, help=\"Device (e.g. cuda:1)\")\n    parser.add_argument(\"--dry_run\", action=\"store_true\", help=\"Generate pseudo gold from conf>=2 MV labels\")\n    parser.add_argument(\"--dry_run_min_conf\", type=int, default=2, help=\"Min confidence for dry-run pseudo gold\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    base_dir = Path(__file__).parent\n    data_dir = base_dir / args.data_dir\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device or (\"cuda\" if torch.cuda.is_available() else \"cpu\")\n    print(f\"Device: {device}\")\n\n    # ------------------------------------------------------------------\n    # 1. Load windows\n    # ------------------------------------------------------------------\n    print(\"Loading windows_labeled.jsonl ...\")\n    all_windows = load_windows_jsonl(data_dir / \"windows_labeled.jsonl\")\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total windows: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 2. Load or generate gold labels\n    # ------------------------------------------------------------------\n    if args.dry_run:\n        print(f\"DRY RUN: generating pseudo gold from conf>={args.dry_run_min_conf} MV labels ...\")\n        pseudo_gold = generate_pseudo_gold(all_windows, min_confidence=args.dry_run_min_conf)\n        gold_wids = [wid for wid, _ in pseudo_gold]\n        gold_labels = [label for _, label in pseudo_gold]\n        print(f\"  Pseudo gold windows: {len(gold_wids)}\")\n\n        csv_path = output_dir / \"pseudo_gold.csv\"\n        with open(csv_path, \"w\", newline=\"\") as f:\n            writer = csv.writer(f)\n            writer.writerow([\"window_id\", \"gold_label\"])\n            for wid, label in pseudo_gold:\n                writer.writerow([wid, label])\n        print(f\"  Saved pseudo gold CSV: {csv_path}\")\n    else:\n        if args.gold_csv is None:\n            print(\"ERROR: --gold_csv required when not in --dry_run mode\")\n            sys.exit(1)\n        print(f\"Loading gold CSV: {args.gold_csv}\")\n        gold_wids = []\n        gold_labels = []\n        with open(args.gold_csv) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                gold_wids.append(row[\"window_id\"])\n                gold_labels.append(int(row[\"gold_label\"]))\n        print(f\"  Gold windows: {len(gold_wids)}\")\n\n    gold_dist = {\n        \"total\": len(gold_labels),\n        \"stagnation\": sum(1 for l in gold_labels if l == 0),\n        \"progress\": sum(1 for l in gold_labels if l == 1),\n    }\n    print(f\"  Distribution: stag={gold_dist['stagnation']}, prog={gold_dist['progress']}\")\n\n    # ------------------------------------------------------------------\n    # 3. Load embeddings\n    # ------------------------------------------------------------------\n    print(\"Loading embeddings.pt ...\")\n    emb_data = torch.load(data_dir / \"embeddings.pt\", map_location=\"cpu\", weights_only=False)\n    embeddings = emb_data[\"embeddings\"]\n    emb_trajectory_ids = emb_data.get(\"trajectory_ids\", [])\n    print(f\"  Embeddings loaded: {len(embeddings)}\")\n\n    wid_to_emb_idx = {}\n    if len(emb_trajectory_ids) == len(non_abstain):\n        for i, w in enumerate(non_abstain):\n            wid_to_emb_idx[window_id(w)] = i\n    else:\n        print(f\"  WARNING: embedding count ({len(embeddings)}) != non_abstain ({len(non_abstain)}), building fallback index\")\n        for i in range(len(embeddings)):\n            if i < len(non_abstain):\n                wid_to_emb_idx[window_id(non_abstain[i])] = i\n\n    # ------------------------------------------------------------------\n    # 4. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = base_dir / args.split_info\n    print(f\"Loading split info: {split_info_path}\")\n    with open(split_info_path) as f:\n        split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 5. Evaluate each model\n    # ------------------------------------------------------------------\n    results = []\n\n    # --- 5a. MV Labels ---\n    print(\"\\n[1/5] Evaluating MV Labels vs Gold ...\")\n    mv_metrics, mv_n = evaluate_mv(gold_wids, gold_labels, wid_to_window)\n    if mv_metrics:\n        print(f\"  macro_f1={mv_metrics['macro_f1']:.4f}, accuracy={mv_metrics['accuracy']:.4f}, n={mv_n}\")\n    else:\n        print(\"  SKIPPED: no matching windows\")\n    results.append((\"MV Labels\", mv_metrics, mv_n))\n\n    # --- 5b. GRU Probe ---\n    probe_ckpt = base_dir / args.checkpoint\n    print(f\"\\n[2/5] Evaluating GRU Probe vs Gold ...\")\n    if probe_ckpt.exists():\n        probe_metrics, probe_n = evaluate_probe_model(\n            gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(probe_ckpt), device\n        )\n        if probe_metrics:\n            print(f\"  macro_f1={probe_metrics['macro_f1']:.4f}, accuracy={probe_metrics['accuracy']:.4f}, n={probe_n}\")\n        else:\n            print(\"  SKIPPED: no matching gold windows in embeddings\")\n    else:\n        print(f\"  SKIPPED: checkpoint not found at {probe_ckpt}\")\n        probe_metrics, probe_n = None, 0\n    results.append((\"GRU Probe\", probe_metrics, probe_n))\n\n    # --- 5c/5d. Structural RF & GB ---\n    traj_path = base_dir / args.trajectories\n    struct_available = traj_path.exists()\n    if struct_available:\n        print(f\"\\n[3-4/5] Building structural features ...\")\n        traj_index = build_trajectory_index(str(traj_path))\n        print(f\"  Indexed {len(traj_index)} trajectories\")\n\n        all_features = []\n        all_mv_labels = []\n        for w in non_abstain:\n            row_idx = w.get(\"row_index\", 0)\n            step_indices = w[\"step_indices\"]\n            traj_steps = traj_index.get(row_idx, [])\n            window_steps = []\n            for si in step_indices:\n                if si < len(traj_steps):\n                    window_steps.append(traj_steps[si])\n                else:\n                    window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n            feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n            all_features.append(feat)\n            all_mv_labels.append(w[\"majority_label\"])\n\n        all_features = np.stack(all_features)\n        print(f\"  Feature matrix: {all_features.shape}\")\n\n        # RF\n        print(\"  Evaluating Structural RF ...\")\n        rf_metrics, rf_n = evaluate_structural(\n            gold_wids, gold_labels, wid_to_noabs_idx,\n            all_features, all_mv_labels, split_info,\n            RandomForestClassifier,\n            {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n        )\n        if rf_metrics:\n            print(f\"  RF: macro_f1={rf_metrics['macro_f1']:.4f}, accuracy={rf_metrics['accuracy']:.4f}, n={rf_n}\")\n        else:\n            print(\"  RF: SKIPPED\")\n        results.append((\"Structural RF\", rf_metrics, rf_n))\n\n        # GB\n        print(\"  Evaluating Structural GB ...\")\n        gb_metrics, gb_n = evaluate_structural(\n            gold_wids, gold_labels, wid_to_noabs_idx,\n            all_features, all_mv_labels, split_info,\n            GradientBoostingClassifier,\n            {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n        )\n        if gb_metrics:\n            print(f\"  GB: macro_f1={gb_metrics['macro_f1']:.4f}, accuracy={gb_metrics['accuracy']:.4f}, n={gb_n}\")\n        else:\n            print(\"  GB: SKIPPED\")\n        results.append((\"Structural GB\", gb_metrics, gb_n))\n    else:\n        print(f\"\\n[3-4/5] SKIPPED structural baselines: {traj_path} not found\")\n        results.append((\"Structural RF\", None, 0))\n        results.append((\"Structural GB\", None, 0))\n\n    # --- 5e. TWV Labels ---\n    twv_labels_path = data_dir / \"windows_tlm_labels.jsonl\"\n    print(f\"\\n[5/5] Evaluating TWV Labels vs Gold ...\")\n    if twv_labels_path.exists():\n        twv_windows = load_windows_jsonl(str(twv_labels_path))\n        wid_to_twv = {}\n        for w in twv_windows:\n            wid = f\"{w['trajectory_id']}__w{w['window_idx']}\"\n            wid_to_twv[wid] = w\n        twv_metrics, twv_n = evaluate_twv(gold_wids, gold_labels, wid_to_twv)\n        if twv_metrics:\n            print(f\"  macro_f1={twv_metrics['macro_f1']:.4f}, accuracy={twv_metrics['accuracy']:.4f}, n={twv_n}\")\n        else:\n            print(\"  SKIPPED: no matching windows\")\n    else:\n        print(f\"  SKIPPED: {twv_labels_path} not found\")\n        twv_metrics, twv_n = None, 0\n    results.append((\"TWV Labels\", twv_metrics, twv_n))\n\n    # --- 5f. TWV Probe (bonus) ---\n    twv_ckpt = base_dir / args.twv_checkpoint\n    if twv_ckpt.exists():\n        twv_emb_path = base_dir / \"data_tlm_twv\" / \"embeddings.pt\"\n        if twv_emb_path.exists():\n            print(\"\\n[bonus] Evaluating TWV Probe vs Gold ...\")\n            twv_emb_data = torch.load(twv_emb_path, map_location=\"cpu\", weights_only=False)\n            twv_embeddings = twv_emb_data[\"embeddings\"]\n\n            twv_wid_to_emb_idx = {}\n            twv_all_windows = load_windows_jsonl(str(twv_labels_path)) if twv_labels_path.exists() else []\n            twv_non_abstain = [w for w in twv_all_windows if w.get(\"mv_label\", -1) != -1]\n            if len(twv_embeddings) == len(twv_non_abstain):\n                for i, w in enumerate(twv_non_abstain):\n                    wid = f\"{w['trajectory_id']}__w{w['window_idx']}\"\n                    twv_wid_to_emb_idx[wid] = i\n            else:\n                for i, w in enumerate(non_abstain):\n                    if i < len(twv_embeddings):\n                        twv_wid_to_emb_idx[window_id(w)] = i\n\n            twv_probe_metrics, twv_probe_n = evaluate_probe_model(\n                gold_wids, gold_labels, twv_wid_to_emb_idx, twv_embeddings, str(twv_ckpt), device\n            )\n            if twv_probe_metrics:\n                print(f\"  macro_f1={twv_probe_metrics['macro_f1']:.4f}, accuracy={twv_probe_metrics['accuracy']:.4f}, n={twv_probe_n}\")\n                results.append((\"TWV Probe\", twv_probe_metrics, twv_probe_n))\n            else:\n                print(\"  SKIPPED: no matching windows\")\n\n    # ------------------------------------------------------------------\n    # 6. MV-Gold agreement\n    # ------------------------------------------------------------------\n    n_agree = 0\n    n_total = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        n_total += 1\n        if w[\"majority_label\"] == gl:\n            n_agree += 1\n    mv_gold_agreement = {\n        \"agreement_rate\": n_agree / max(n_total, 1),\n        \"n_agree\": n_agree,\n        \"n_disagree\": n_total - n_agree,\n        \"n_total\": n_total,\n    }\n    print(f\"\\nMV-Gold agreement: {n_agree}/{n_total} = {mv_gold_agreement['agreement_rate']:.4f}\")\n\n    # ------------------------------------------------------------------\n    # 7. Output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n\n    output = {\n        \"gold_distribution\": gold_dist,\n        \"mv_gold_agreement\": mv_gold_agreement,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n        \"dry_run\": args.dry_run,\n    }\n    for name, metrics, n in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nResults JSON: {json_path}\")\n\n    report_path = generate_report(results, gold_dist, mv_gold_agreement, output_dir)\n    print(f\"Report: {report_path}\")\n    print(f\"\\nTotal elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 723,
      "startLine": 1,
      "totalLines": 723
    }
  }
}
````

</details>

---


### Tool call

_source line 117_

<details open><summary>🔧 Tool call — Read · `toolu_019JBgTj3L8djFzBv9bBxnb6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/baseline_llm_judge.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "4687a836-d755-483f-bea9-d6b53263abfb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTY1FZU4e3Hb2yRA1CTNNZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12084,
      "cache_read_input_tokens": 28604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12084
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

_source line 118 · 2026-05-14T22:42:03.597Z_

<details><summary>↩ Tool result · `toolu_019JBgTj3L8djFzBv9bBxnb6`</summary>

````text
1	#!/usr/bin/env python3
2	"""LLM-as-Judge baseline for progress/stagnation classification.
3	
4	Uses an LLM to zero-shot or few-shot classify agent trajectory windows,
5	as an upper-bound baseline for comparison with trained probes.
6	
7	Requires: pip install openai
8	API key via --api_key or OPENROUTER_API_KEY env var.
9	"""
10	
11	import argparse
12	import json
13	import os
14	import re
15	import sys
16	import time
17	from pathlib import Path
18	from collections import Counter
19	
20	import openai
21	from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
22	
23	
24	LABEL_MAP = {"stagnation": 0, "stagnating": 0, "stagnant": 0,
25	             "progress": 1, "progressing": 1, "advancing": 1}
26	
27	ZERO_SHOT_SYSTEM = """You are an expert at analyzing software engineering agent trajectories. Your task is to determine whether an agent is making meaningful progress toward solving a coding task, or whether it is stagnating (repeating actions, going in circles, or failing to advance).
28	
29	You will be shown a window of consecutive steps from the agent's interaction. Each step has a role (ai = agent action, user = environment observation) and text content.
30	
31	Respond ONLY with a JSON object in this exact format:
32	{"judgment": "progress" or "stagnation", "confidence": 1-5, "reasoning": "brief explanation"}"""
33	
34	ZERO_SHOT_USER = """Below is a window of {n_steps} consecutive steps from a software engineering agent's trajectory.
35	
36	{steps_text}
37	
38	Based on these steps, is the agent making meaningful progress toward solving the task, or is it stagnating?"""
39	
40	FEW_SHOT_SYSTEM = """You are an expert at analyzing software engineering agent trajectories. Your task is to determine whether an agent is making meaningful progress toward solving a coding task, or whether it is stagnating (repeating actions, going in circles, or failing to advance).
41	
42	You will be shown a window of consecutive steps from the agent's interaction. Each step has a role (ai = agent action, user = environment observation) and text content.
43	
44	Here are some examples:
45	
46	{examples}
47	
48	Respond ONLY with a JSON object in this exact format:
49	{{"judgment": "progress" or "stagnation", "confidence": 1-5, "reasoning": "brief explanation"}}"""
50	
51	
52	def compute_metrics(labels, preds):
53	    return {
54	        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
55	        "accuracy": accuracy_score(labels, preds),
56	        "precision_macro": precision_score(labels, preds, average="macro", zero_division=0),
57	        "recall_macro": recall_score(labels, preds, average="macro", zero_division=0),
58	        "f1_stagnation": f1_score(labels, preds, pos_label=0, zero_division=0),
59	        "f1_progress": f1_score(labels, preds, pos_label=1, zero_division=0),
60	    }
61	
62	
63	def truncate_text(text, max_chars=500):
64	    if not text:
65	        return ""
66	    if len(text) <= max_chars:
67	        return text
68	    return text[:max_chars] + "... [truncated]"
69	
70	
71	def format_steps(steps, max_total_chars=6000):
72	    parts = []
73	    budget = max_total_chars
74	    per_step = max(200, budget // max(len(steps), 1))
75	
76	    for i, step in enumerate(steps):
77	        role = step.get("role", "unknown")
78	        text = step.get("text", "") or ""
79	        truncated = truncate_text(text, per_step)
80	        part = f"[Step {i+1} | {role}]\n{truncated}"
81	        parts.append(part)
82	
83	    return "\n\n".join(parts)
84	
85	
86	def load_trajectories_index(traj_path):
87	    """Build index: row_index -> trajectory dict."""
88	    index = {}
89	    with open(traj_path) as f:
90	        for row_idx, line in enumerate(f):
91	            line = line.strip()
92	            if line:
93	                index[row_idx] = json.loads(line)
94	    return index
95	
96	
97	def extract_window_steps(window, traj_index):
98	    """Get actual step texts for a window from trajectory data."""
99	    row_idx = window["row_index"]
100	    step_indices = window["step_indices"]
101	    traj = traj_index.get(row_idx)
102	    if traj is None:
103	        return []
104	    trajectory = traj.get("trajectory", [])
105	    steps = []
106	    for si in step_indices:
107	        if si < len(trajectory):
108	            s = trajectory[si]
109	            steps.append({"role": s.get("role", "unknown"),
110	                          "text": s.get("text", "") or ""})
111	    return steps
112	
113	
114	def select_few_shot_examples(train_windows, traj_index, n_progress=1, n_stagnation=1, n_boundary=1):
115	    """Select high-confidence examples from training set for few-shot prompting."""
116	    progress_examples = []
117	    stagnation_examples = []
118	
119	    for w in train_windows:
120	        if w["confidence"] >= 3:
121	            if w["majority_label"] == 1:
122	                progress_examples.append(w)
123	            elif w["majority_label"] == 0:
124	                stagnation_examples.append(w)
125	
126	    # Boundary: conf=2 examples
127	    boundary_examples = [w for w in train_windows if w["confidence"] == 2]
128	
129	    import random
130	    rng = random.Random(42)
131	    selected = []
132	
133	    if progress_examples:
134	        selected.extend(rng.sample(progress_examples, min(n_progress, len(progress_examples))))
135	    if stagnation_examples:
136	        selected.extend(rng.sample(stagnation_examples, min(n_stagnation, len(stagnation_examples))))
137	    if boundary_examples:
138	        selected.extend(rng.sample(boundary_examples, min(n_boundary, len(boundary_examples))))
139	
140	    examples_text = []
141	    for i, w in enumerate(selected):
142	        steps = extract_window_steps(w, traj_index)
143	        label_str = "progress" if w["majority_label"] == 1 else "stagnation"
144	        steps_formatted = format_steps(steps, max_total_chars=2000)
145	        examples_text.append(
146	            f"--- Example {i+1} (Answer: {label_str}) ---\n{steps_formatted}\n"
147	            f'{{"judgment": "{label_str}", "confidence": {w["confidence"]}, "reasoning": "This is a {label_str} example."}}'
148	        )
149	
150	    return "\n\n".join(examples_text)
151	
152	
153	def parse_llm_response(text):
154	    """Extract judgment from LLM response with robust fallback."""
155	    # Try direct JSON parse
156	    try:
157	        obj = json.loads(text.strip())
158	        j = obj.get("judgment", "").lower().strip()
159	        if j in LABEL_MAP:
160	            return LABEL_MAP[j], obj.get("confidence", 0), obj.get("reasoning", "")
161	    except json.JSONDecodeError:
162	        pass
163	
164	    # Try extracting JSON from markdown code block
165	    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
166	    if m:
167	        try:
168	            obj = json.loads(m.group(1))
169	            j = obj.get("judgment", "").lower().strip()
170	            if j in LABEL_MAP:
171	                return LABEL_MAP[j], obj.get("confidence", 0), obj.get("reasoning", "")
172	        except json.JSONDecodeError:
173	            pass
174	
175	    # Try finding JSON object in text
176	    m = re.search(r"\{[^{}]*\"judgment\"[^{}]*\}", text, re.DOTALL)
177	    if m:
178	        try:
179	            obj = json.loads(m.group(0))
180	            j = obj.get("judgment", "").lower().strip()
181	            if j in LABEL_MAP:
182	                return LABEL_MAP[j], obj.get("confidence", 0), obj.get("reasoning", "")
183	        except json.JSONDecodeError:
184	            pass
185	
186	    # Keyword fallback
187	    lower = text.lower()
188	    if "stagnat" in lower and "progress" not in lower:
189	        return 0, 0, "keyword_fallback"
190	    if "progress" in lower and "stagnat" not in lower:
191	        return 1, 0, "keyword_fallback"
192	
193	    return -1, 0, "parse_failed"
194	
195	
196	def call_llm(client, model, system_msg, user_msg, max_retries=3):
197	    """Call LLM with retry logic. Returns (response_text, input_tokens, output_tokens)."""
198	    for attempt in range(max_retries):
199	        try:
200	            resp = client.chat.completions.create(
201	                model=model,
202	                messages=[
203	                    {"role": "system", "content": system_msg},
204	                    {"role": "user", "content": user_msg},
205	                ],
206	                temperature=0.0,
207	                max_tokens=256,
208	            )
209	            choice = resp.choices[0]
210	            usage = resp.usage
211	            return (
212	                choice.message.content or "",
213	                usage.prompt_tokens if usage else 0,
214	                usage.completion_tokens if usage else 0,
215	            )
216	        except (openai.RateLimitError, openai.APITimeoutError, openai.APIConnectionError) as e:
217	            wait = 2 ** (attempt + 1)
218	            print(f"  Retry {attempt+1}/{max_retries} after {type(e).__name__}, waiting {wait}s", flush=True)
219	            time.sleep(wait)
220	        except openai.APIError as e:
221	            if attempt < max_retries - 1:
222	                wait = 2 ** (attempt + 1)
223	                print(f"  Retry {attempt+1}/{max_retries} after APIError: {e}, waiting {wait}s", flush=True)
224	                time.sleep(wait)
225	            else:
226	                print(f"  FAILED after {max_retries} retries: {e}", flush=True)
227	                return "", 0, 0
228	    return "", 0, 0
229	
230	
231	def main():
232	    parser = argparse.ArgumentParser(description="LLM-as-Judge baseline for progress/stagnation")
233	    parser.add_argument("--data_dir", required=True, help="Dir containing data/windows_labeled.jsonl")
234	    parser.add_argument("--split_info", required=True, help="Path to split_info.json")
235	    parser.add_argument("--trajectories", required=True, help="Path to swe_agent_trajectories_5000.jsonl")
236	    parser.add_argument("--api_key", default=None, help="API key (or set OPENROUTER_API_KEY)")
237	    parser.add_argument("--base_url", default="http://47.94.22.126/v1", help="API base URL")
238	    parser.add_argument("--model", default="anthropic/claude-sonnet-4-6", help="Model ID")
239	    parser.add_argument("--mode", choices=["zero-shot", "few-shot"], default="zero-shot")
240	    parser.add_argument("--max_windows", type=int, default=0, help="0 = all test windows")
241	    parser.add_argument("--output", default="results/llm_judge_results.json", help="Output path")
242	    parser.add_argument("--resume", action="store_true", help="Resume from existing partial results")
243	    parser.add_argument("--rps", type=float, default=5.0, help="Max requests per second")
244	    parser.add_argument("--budget", type=float, default=100.0, help="Max spend in USD before pausing")
245	    parser.add_argument("--list_models", action="store_true", help="List available models and exit")
246	    args = parser.parse_args()
247	
248	    api_key = [REDACTED] or os.environ.get("OPENROUTER_API_KEY", "")
249	    if not api_key:
[REDACTED]	        print("ERROR: Provide --api_key or set OPENROUTER_API_KEY", file=sys.stderr)
251	        sys.exit(1)
252	
253	    client = openai.OpenAI(base_url=args.base_url, api_key=[REDACTED], timeout=60.0)
254	
255	    if args.list_models:
256	        models = client.models.list()
257	        for m in models.data:
258	            print(m.id)
259	        return
260	
261	    # Load data
262	    print("Loading windows...")
263	    windows_path = Path(args.data_dir) / "data" / "windows_labeled.jsonl"
264	    all_windows = []
265	    with open(windows_path) as f:
266	        for line in f:
267	            line = line.strip()
268	            if line:
269	                all_windows.append(json.loads(line))
270	    usable = [w for w in all_windows if w.get("majority_label", -1) != -1]
271	    print(f"  Total: {len(all_windows)}, usable: {len(usable)}")
272	
273	    print("Loading split info...")
274	    with open(args.split_info) as f:
275	        split_info = json.load(f)
276	
277	    keep_indices = split_info.get("keep_indices")
278	    if keep_indices is not None:
279	        windows = [usable[i] for i in keep_indices]
280	        print(f"  Confidence filter: {len(windows)}/{len(usable)}")
281	    else:
282	        windows = usable
283	
284	    train_idx = split_info["train_indices"]
285	    test_idx = split_info["test_indices"]
286	    train_windows = [windows[i] for i in train_idx]
287	    test_windows = [windows[i] for i in test_idx]
288	    print(f"  Train: {len(train_windows)}, Test: {len(test_windows)}")
289	
290	    if args.max_windows > 0:
291	        test_windows = test_windows[:args.max_windows]
292	        print(f"  Limiting to {len(test_windows)} test windows")
293	
294	    gt = [w["majority_label"] for w in test_windows]
295	    print(f"  Test label dist: {dict(Counter(gt))}")
296	
297	    print("Loading trajectories index...")
298	    traj_index = load_trajectories_index(args.trajectories)
299	    print(f"  Loaded {len(traj_index)} trajectories")
300	
301	    # Prepare few-shot examples if needed
302	    few_shot_examples_text = ""
303	    if args.mode == "few-shot":
304	        print("Selecting few-shot examples...")
305	        few_shot_examples_text = select_few_shot_examples(train_windows, traj_index)
306	
307	    # Resume support
308	    output_path = Path(args.output)
309	    output_path.parent.mkdir(parents=True, exist_ok=True)
310	    completed = {}
311	    if args.resume and output_path.exists():
312	        with open(output_path) as f:
313	            prev = json.load(f)
314	        for r in prev.get("results", []):
315	            key = f"{r['trajectory_id']}_{r['window_idx']}"
316	            completed[key] = r
317	        print(f"  Resuming: {len(completed)} windows already done")
318	
319	    # Run evaluation
320	    results = list(completed.values())
321	    total_input_tokens = sum(r.get("input_tokens", 0) for r in results)
322	    total_output_tokens = sum(r.get("output_tokens", 0) for r in results)
323	    parse_failures = sum(1 for r in results if r.get("predicted_label") == -1)
324	    min_interval = 1.0 / args.rps
325	
326	    print(f"\nStarting LLM evaluation: {len(test_windows)} windows, model={args.model}, mode={args.mode}")
327	    print(f"Rate limit: {args.rps} rps, budget: ${args.budget}")
328	    print("-" * 60)
329	
330	    last_call_time = 0.0
331	    for i, w in enumerate(test_windows):
332	        key = f"{w['trajectory_id']}_{w['window_idx']}"
333	        if key in completed:
334	            continue
335	
336	        # Budget check
337	        est_cost = (total_input_tokens * 3 + total_output_tokens * 15) / 1_000_000
338	        if est_cost > args.budget:
339	            print(f"\n*** BUDGET EXCEEDED: ~${est_cost:.2f} > ${args.budget}. Stopping. ***")
340	            break
341	
342	        # Rate limiting
343	        elapsed = time.time() - last_call_time
344	        if elapsed < min_interval:
345	            time.sleep(min_interval - elapsed)
346	
347	        # Build prompt
348	        steps = extract_window_steps(w, traj_index)
349	        steps_text = format_steps(steps)
350	
351	        if args.mode == "zero-shot":
352	            system_msg = ZERO_SHOT_SYSTEM
353	            user_msg = ZERO_SHOT_USER.format(n_steps=len(steps), steps_text=steps_text)
354	        else:
355	            system_msg = FEW_SHOT_SYSTEM.format(examples=few_shot_examples_text)
356	            user_msg = ZERO_SHOT_USER.format(n_steps=len(steps), steps_text=steps_text)
357	
358	        # Call LLM
359	        last_call_time = time.time()
360	        resp_text, in_tok, out_tok = call_llm(client, args.model, system_msg, user_msg)
361	        total_input_tokens += in_tok
362	        total_output_tokens += out_tok
363	
364	        pred_label, pred_conf, reasoning = parse_llm_response(resp_text)
365	        if pred_label == -1:
366	            parse_failures += 1
367	
368	        result = {
369	            "trajectory_id": w["trajectory_id"],
370	            "window_idx": w["window_idx"],
371	            "true_label": w["majority_label"],
372	            "predicted_label": pred_label,
373	            "llm_confidence": pred_conf,
374	            "reasoning": reasoning,
375	            "input_tokens": in_tok,
376	            "output_tokens": out_tok,
377	            "raw_response": resp_text,
378	        }
379	        results.append(result)
380	        completed[key] = result
381	
382	        # Progress logging
383	        if (i + 1) % 10 == 0 or i == len(test_windows) - 1:
384	            done = len(results)
385	            est_cost = (total_input_tokens * 3 + total_output_tokens * 15) / 1_000_000
386	            valid = [r for r in results if r["predicted_label"] != -1]
387	            if valid:
388	                cur_preds = [r["predicted_label"] for r in valid]
389	                cur_gt = [r["true_label"] for r in valid]
390	                cur_f1 = f1_score(cur_gt, cur_preds, average="macro", zero_division=0)
391	            else:
392	                cur_f1 = 0.0
393	            print(f"  [{done}/{len(test_windows)}] macro_f1={cur_f1:.4f} | "
394	                  f"tokens={total_input_tokens+total_output_tokens:,} | "
395	                  f"~${est_cost:.4f} | fails={parse_failures}")
396	
397	        # Checkpoint every 100
398	        if (i + 1) % 100 == 0:
399	            _save_results(output_path, results, args, total_input_tokens, total_output_tokens, parse_failures)
400	
401	    # Final save
402	    _save_results(output_path, results, args, total_input_tokens, total_output_tokens, parse_failures)
403	
404	    # Final metrics
405	    print("\n" + "=" * 60)
406	    valid_results = [r for r in results if r["predicted_label"] != -1]
407	    if valid_results:
408	        preds = [r["predicted_label"] for r in valid_results]
409	        labels = [r["true_label"] for r in valid_results]
410	        metrics = compute_metrics(labels, preds)
411	
412	        print(f"Model: {args.model} | Mode: {args.mode}")
413	        print(f"Windows evaluated: {len(results)} ({len(valid_results)} valid, {parse_failures} parse failures)")
414	        print(f"\n{'Metric':<20} {'Value':>10}")
415	        print("-" * 32)
416	        for k, v in metrics.items():
417	            print(f"{k:<20} {v:>10.4f}")
418	
419	        print(f"\nGRU Probe reference: macro_f1 = 0.9055")
420	        print(f"LLM Judge:          macro_f1 = {metrics['macro_f1']:.4f}")
421	        print(f"Delta:              {metrics['macro_f1'] - 0.9055:+.4f}")
422	    else:
423	        print("No valid results to compute metrics.")
424	
425	    # Cost summary
426	    est_cost = (total_input_tokens * 3 + total_output_tokens * 15) / 1_000_000
427	    print(f"\n--- Cost Summary ---")
428	    print(f"Input tokens:  {total_input_tokens:>12,}")
429	    print(f"Output tokens: {total_output_tokens:>12,}")
430	    print(f"Total tokens:  {total_input_tokens + total_output_tokens:>12,}")
431	    print(f"Est. cost:     ${est_cost:>11.4f} (assuming $3/M input, $15/M output)")
432	    if len(results) > 0:
433	        per_window = est_cost / len(results)
434	        remaining = len(test_windows) - len(results)
435	        print(f"Per window:    ${per_window:.6f}")
436	        if remaining > 0:
437	            print(f"Est. remaining ({remaining} windows): ${per_window * remaining:.4f}")
438	
439	    print(f"\nResults saved to {output_path}")
440	
441	
442	def _save_results(path, results, args, total_input_tokens, total_output_tokens, parse_failures):
443	    est_cost = (total_input_tokens * 3 + total_output_tokens * 15) / 1_000_000
444	    output = {
445	        "model": args.model,
446	        "mode": args.mode,
447	        "n_windows": len(results),
448	        "parse_failures": parse_failures,
449	        "total_input_tokens": total_input_tokens,
450	        "total_output_tokens": total_output_tokens,
451	        "est_cost_usd": round(est_cost, 4),
452	        "results": results,
453	    }
454	    with open(path, "w") as f:
455	        json.dump(output, f, indent=2, ensure_ascii=False)
456	
457	
458	if __name__ == "__main__":
459	    main()
460	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "3e5f3a2e-eea6-41f2-9237-f78e84a05955",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/baseline_llm_judge.py",
      "content": "#!/usr/bin/env python3\n\"\"\"LLM-as-Judge baseline for progress/stagnation classification.\n\nUses an LLM to zero-shot or few-shot classify agent trajectory windows,\nas an upper-bound baseline for comparison with trained probes.\n\nRequires: pip install openai\nAPI key via --api_key or OPENROUTER_API_KEY env var.\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport re\nimport sys\nimport time\nfrom pathlib import Path\nfrom collections import Counter\n\nimport openai\nfrom sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score\n\n\nLABEL_MAP = {\"stagnation\": 0, \"stagnating\": 0, \"stagnant\": 0,\n             \"progress\": 1, \"progressing\": 1, \"advancing\": 1}\n\nZERO_SHOT_SYSTEM = \"\"\"You are an expert at analyzing software engineering agent trajectories. Your task is to determine whether an agent is making meaningful progress toward solving a coding task, or whether it is stagnating (repeating actions, going in circles, or failing to advance).\n\nYou will be shown a window of consecutive steps from the agent's interaction. Each step has a role (ai = agent action, user = environment observation) and text content.\n\nRespond ONLY with a JSON object in this exact format:\n{\"judgment\": \"progress\" or \"stagnation\", \"confidence\": 1-5, \"reasoning\": \"brief explanation\"}\"\"\"\n\nZERO_SHOT_USER = \"\"\"Below is a window of {n_steps} consecutive steps from a software engineering agent's trajectory.\n\n{steps_text}\n\nBased on these steps, is the agent making meaningful progress toward solving the task, or is it stagnating?\"\"\"\n\nFEW_SHOT_SYSTEM = \"\"\"You are an expert at analyzing software engineering agent trajectories. Your task is to determine whether an agent is making meaningful progress toward solving a coding task, or whether it is stagnating (repeating actions, going in circles, or failing to advance).\n\nYou will be shown a window of consecutive steps from the agent's interaction. Each step has a role (ai = agent action, user = environment observation) and text content.\n\nHere are some examples:\n\n{examples}\n\nRespond ONLY with a JSON object in this exact format:\n{{\"judgment\": \"progress\" or \"stagnation\", \"confidence\": 1-5, \"reasoning\": \"brief explanation\"}}\"\"\"\n\n\ndef compute_metrics(labels, preds):\n    return {\n        \"macro_f1\": f1_score(labels, preds, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(labels, preds),\n        \"precision_macro\": precision_score(labels, preds, average=\"macro\", zero_division=0),\n        \"recall_macro\": recall_score(labels, preds, average=\"macro\", zero_division=0),\n        \"f1_stagnation\": f1_score(labels, preds, pos_label=0, zero_division=0),\n        \"f1_progress\": f1_score(labels, preds, pos_label=1, zero_division=0),\n    }\n\n\ndef truncate_text(text, max_chars=500):\n    if not text:\n        return \"\"\n    if len(text) <= max_chars:\n        return text\n    return text[:max_chars] + \"... [truncated]\"\n\n\ndef format_steps(steps, max_total_chars=6000):\n    parts = []\n    budget = max_total_chars\n    per_step = max(200, budget // max(len(steps), 1))\n\n    for i, step in enumerate(steps):\n        role = step.get(\"role\", \"unknown\")\n        text = step.get(\"text\", \"\") or \"\"\n        truncated = truncate_text(text, per_step)\n        part = f\"[Step {i+1} | {role}]\\n{truncated}\"\n        parts.append(part)\n\n    return \"\\n\\n\".join(parts)\n\n\ndef load_trajectories_index(traj_path):\n    \"\"\"Build index: row_index -> trajectory dict.\"\"\"\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if line:\n                index[row_idx] = json.loads(line)\n    return index\n\n\ndef extract_window_steps(window, traj_index):\n    \"\"\"Get actual step texts for a window from trajectory data.\"\"\"\n    row_idx = window[\"row_index\"]\n    step_indices = window[\"step_indices\"]\n    traj = traj_index.get(row_idx)\n    if traj is None:\n        return []\n    trajectory = traj.get(\"trajectory\", [])\n    steps = []\n    for si in step_indices:\n        if si < len(trajectory):\n            s = trajectory[si]\n            steps.append({\"role\": s.get(\"role\", \"unknown\"),\n                          \"text\": s.get(\"text\", \"\") or \"\"})\n    return steps\n\n\ndef select_few_shot_examples(train_windows, traj_index, n_progress=1, n_stagnation=1, n_boundary=1):\n    \"\"\"Select high-confidence examples from training set for few-shot prompting.\"\"\"\n    progress_examples = []\n    stagnation_examples = []\n\n    for w in train_windows:\n        if w[\"confidence\"] >= 3:\n            if w[\"majority_label\"] == 1:\n                progress_examples.append(w)\n            elif w[\"majority_label\"] == 0:\n                stagnation_examples.append(w)\n\n    # Boundary: conf=2 examples\n    boundary_examples = [w for w in train_windows if w[\"confidence\"] == 2]\n\n    import random\n    rng = random.Random(42)\n    selected = []\n\n    if progress_examples:\n        selected.extend(rng.sample(progress_examples, min(n_progress, len(progress_examples))))\n    if stagnation_examples:\n        selected.extend(rng.sample(stagnation_examples, min(n_stagnation, len(stagnation_examples))))\n    if boundary_examples:\n        selected.extend(rng.sample(boundary_examples, min(n_boundary, len(boundary_examples))))\n\n    examples_text = []\n    for i, w in enumerate(selected):\n        steps = extract_window_steps(w, traj_index)\n        label_str = \"progress\" if w[\"majority_label\"] == 1 else \"stagnation\"\n        steps_formatted = format_steps(steps, max_total_chars=2000)\n        examples_text.append(\n            f\"--- Example {i+1} (Answer: {label_str}) ---\\n{steps_formatted}\\n\"\n            f'{{\"judgment\": \"{label_str}\", \"confidence\": {w[\"confidence\"]}, \"reasoning\": \"This is a {label_str} example.\"}}'\n        )\n\n    return \"\\n\\n\".join(examples_text)\n\n\ndef parse_llm_response(text):\n    \"\"\"Extract judgment from LLM response with robust fallback.\"\"\"\n    # Try direct JSON parse\n    try:\n        obj = json.loads(text.strip())\n        j = obj.get(\"judgment\", \"\").lower().strip()\n        if j in LABEL_MAP:\n            return LABEL_MAP[j], obj.get(\"confidence\", 0), obj.get(\"reasoning\", \"\")\n    except json.JSONDecodeError:\n        pass\n\n    # Try extracting JSON from markdown code block\n    m = re.search(r\"```(?:json)?\\s*(\\{.*?\\})\\s*```\", text, re.DOTALL)\n    if m:\n        try:\n            obj = json.loads(m.group(1))\n            j = obj.get(\"judgment\", \"\").lower().strip()\n            if j in LABEL_MAP:\n                return LABEL_MAP[j], obj.get(\"confidence\", 0), obj.get(\"reasoning\", \"\")\n        except json.JSONDecodeError:\n            pass\n\n    # Try finding JSON object in text\n    m = re.search(r\"\\{[^{}]*\\\"judgment\\\"[^{}]*\\}\", text, re.DOTALL)\n    if m:\n        try:\n            obj = json.loads(m.group(0))\n            j = obj.get(\"judgment\", \"\").lower().strip()\n            if j in LABEL_MAP:\n                return LABEL_MAP[j], obj.get(\"confidence\", 0), obj.get(\"reasoning\", \"\")\n        except json.JSONDecodeError:\n            pass\n\n    # Keyword fallback\n    lower = text.lower()\n    if \"stagnat\" in lower and \"progress\" not in lower:\n        return 0, 0, \"keyword_fallback\"\n    if \"progress\" in lower and \"stagnat\" not in lower:\n        return 1, 0, \"keyword_fallback\"\n\n    return -1, 0, \"parse_failed\"\n\n\ndef call_llm(client, model, system_msg, user_msg, max_retries=3):\n    \"\"\"Call LLM with retry logic. Returns (response_text, input_tokens, output_tokens).\"\"\"\n    for attempt in range(max_retries):\n        try:\n            resp = client.chat.completions.create(\n                model=model,\n                messages=[\n                    {\"role\": \"system\", \"content\": system_msg},\n                    {\"role\": \"user\", \"content\": user_msg},\n                ],\n                temperature=0.0,\n                max_tokens=256,\n            )\n            choice = resp.choices[0]\n            usage = resp.usage\n            return (\n                choice.message.content or \"\",\n                usage.prompt_tokens if usage else 0,\n                usage.completion_tokens if usage else 0,\n            )\n        except (openai.RateLimitError, openai.APITimeoutError, openai.APIConnectionError) as e:\n            wait = 2 ** (attempt + 1)\n            print(f\"  Retry {attempt+1}/{max_retries} after {type(e).__name__}, waiting {wait}s\", flush=True)\n            time.sleep(wait)\n        except openai.APIError as e:\n            if attempt < max_retries - 1:\n                wait = 2 ** (attempt + 1)\n                print(f\"  Retry {attempt+1}/{max_retries} after APIError: {e}, waiting {wait}s\", flush=True)\n                time.sleep(wait)\n            else:\n                print(f\"  FAILED after {max_retries} retries: {e}\", flush=True)\n                return \"\", 0, 0\n    return \"\", 0, 0\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"LLM-as-Judge baseline for progress/stagnation\")\n    parser.add_argument(\"--data_dir\", required=True, help=\"Dir containing data/windows_labeled.jsonl\")\n    parser.add_argument(\"--split_info\", required=True, help=\"Path to split_info.json\")\n    parser.add_argument(\"--trajectories\", required=True, help=\"Path to swe_agent_trajectories_5000.jsonl\")\n    parser.add_argument(\"--api_key\", default=None, help=\"API key (or set OPENROUTER_API_KEY)\")\n    parser.add_argument(\"--base_url\", default=\"http://47.94.22.126/v1\", help=\"API base URL\")\n    parser.add_argument(\"--model\", default=\"anthropic/claude-sonnet-4-6\", help=\"Model ID\")\n    parser.add_argument(\"--mode\", choices=[\"zero-shot\", \"few-shot\"], default=\"zero-shot\")\n    parser.add_argument(\"--max_windows\", type=int, default=0, help=\"0 = all test windows\")\n    parser.add_argument(\"--output\", default=\"results/llm_judge_results.json\", help=\"Output path\")\n    parser.add_argument(\"--resume\", action=\"store_true\", help=\"Resume from existing partial results\")\n    parser.add_argument(\"--rps\", type=float, default=5.0, help=\"Max requests per second\")\n    parser.add_argument(\"--budget\", type=float, default=100.0, help=\"Max spend in USD before pausing\")\n    parser.add_argument(\"--list_models\", action=\"store_true\", help=\"List available models and exit\")\n    args = parser.parse_args()\n\n    api_key = [REDACTED] or os.environ.get(\"OPENROUTER_API_KEY\", \"\")\n    if not api_key:\n        [REDACTED]\"ERROR: Provide --api_key or set OPENROUTER_API_KEY\", file=sys.stderr)\n        sys.exit(1)\n\n    client = openai.OpenAI(base_url=args.base_url, api_key=[REDACTED], timeout=60.0)\n\n    if args.list_models:\n        models = client.models.list()\n        for m in models.data:\n            print(m.id)\n        return\n\n    # Load data\n    print(\"Loading windows...\")\n    windows_path = Path(args.data_dir) / \"data\" / \"windows_labeled.jsonl\"\n    all_windows = []\n    with open(windows_path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                all_windows.append(json.loads(line))\n    usable = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, usable: {len(usable)}\")\n\n    print(\"Loading split info...\")\n    with open(args.split_info) as f:\n        split_info = json.load(f)\n\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        windows = [usable[i] for i in keep_indices]\n        print(f\"  Confidence filter: {len(windows)}/{len(usable)}\")\n    else:\n        windows = usable\n\n    train_idx = split_info[\"train_indices\"]\n    test_idx = split_info[\"test_indices\"]\n    train_windows = [windows[i] for i in train_idx]\n    test_windows = [windows[i] for i in test_idx]\n    print(f\"  Train: {len(train_windows)}, Test: {len(test_windows)}\")\n\n    if args.max_windows > 0:\n        test_windows = test_windows[:args.max_windows]\n        print(f\"  Limiting to {len(test_windows)} test windows\")\n\n    gt = [w[\"majority_label\"] for w in test_windows]\n    print(f\"  Test label dist: {dict(Counter(gt))}\")\n\n    print(\"Loading trajectories index...\")\n    traj_index = load_trajectories_index(args.trajectories)\n    print(f\"  Loaded {len(traj_index)} trajectories\")\n\n    # Prepare few-shot examples if needed\n    few_shot_examples_text = \"\"\n    if args.mode == \"few-shot\":\n        print(\"Selecting few-shot examples...\")\n        few_shot_examples_text = select_few_shot_examples(train_windows, traj_index)\n\n    # Resume support\n    output_path = Path(args.output)\n    output_path.parent.mkdir(parents=True, exist_ok=True)\n    completed = {}\n    if args.resume and output_path.exists():\n        with open(output_path) as f:\n            prev = json.load(f)\n        for r in prev.get(\"results\", []):\n            key = f\"{r['trajectory_id']}_{r['window_idx']}\"\n            completed[key] = r\n        print(f\"  Resuming: {len(completed)} windows already done\")\n\n    # Run evaluation\n    results = list(completed.values())\n    total_input_tokens = sum(r.get(\"input_tokens\", 0) for r in results)\n    total_output_tokens = sum(r.get(\"output_tokens\", 0) for r in results)\n    parse_failures = sum(1 for r in results if r.get(\"predicted_label\") == -1)\n    min_interval = 1.0 / args.rps\n\n    print(f\"\\nStarting LLM evaluation: {len(test_windows)} windows, model={args.model}, mode={args.mode}\")\n    print(f\"Rate limit: {args.rps} rps, budget: ${args.budget}\")\n    print(\"-\" * 60)\n\n    last_call_time = 0.0\n    for i, w in enumerate(test_windows):\n        key = f\"{w['trajectory_id']}_{w['window_idx']}\"\n        if key in completed:\n            continue\n\n        # Budget check\n        est_cost = (total_input_tokens * 3 + total_output_tokens * 15) / 1_000_000\n        if est_cost > args.budget:\n            print(f\"\\n*** BUDGET EXCEEDED: ~${est_cost:.2f} > ${args.budget}. Stopping. ***\")\n            break\n\n        # Rate limiting\n        elapsed = time.time() - last_call_time\n        if elapsed < min_interval:\n            time.sleep(min_interval - elapsed)\n\n        # Build prompt\n        steps = extract_window_steps(w, traj_index)\n        steps_text = format_steps(steps)\n\n        if args.mode == \"zero-shot\":\n            system_msg = ZERO_SHOT_SYSTEM\n            user_msg = ZERO_SHOT_USER.format(n_steps=len(steps), steps_text=steps_text)\n        else:\n            system_msg = FEW_SHOT_SYSTEM.format(examples=few_shot_examples_text)\n            user_msg = ZERO_SHOT_USER.format(n_steps=len(steps), steps_text=steps_text)\n\n        # Call LLM\n        last_call_time = time.time()\n        resp_text, in_tok, out_tok = call_llm(client, args.model, system_msg, user_msg)\n        total_input_tokens += in_tok\n        total_output_tokens += out_tok\n\n        pred_label, pred_conf, reasoning = parse_llm_response(resp_text)\n        if pred_label == -1:\n            parse_failures += 1\n\n        result = {\n            \"trajectory_id\": w[\"trajectory_id\"],\n            \"window_idx\": w[\"window_idx\"],\n            \"true_label\": w[\"majority_label\"],\n            \"predicted_label\": pred_label,\n            \"llm_confidence\": pred_conf,\n            \"reasoning\": reasoning,\n            \"input_tokens\": in_tok,\n            \"output_tokens\": out_tok,\n            \"raw_response\": resp_text,\n        }\n        results.append(result)\n        completed[key] = result\n\n        # Progress logging\n        if (i + 1) % 10 == 0 or i == len(test_windows) - 1:\n            done = len(results)\n            est_cost = (total_input_tokens * 3 + total_output_tokens * 15) / 1_000_000\n            valid = [r for r in results if r[\"predicted_label\"] != -1]\n            if valid:\n                cur_preds = [r[\"predicted_label\"] for r in valid]\n                cur_gt = [r[\"true_label\"] for r in valid]\n                cur_f1 = f1_score(cur_gt, cur_preds, average=\"macro\", zero_division=0)\n            else:\n                cur_f1 = 0.0\n            print(f\"  [{done}/{len(test_windows)}] macro_f1={cur_f1:.4f} | \"\n                  f\"tokens={total_input_tokens+total_output_tokens:,} | \"\n                  f\"~${est_cost:.4f} | fails={parse_failures}\")\n\n        # Checkpoint every 100\n        if (i + 1) % 100 == 0:\n            _save_results(output_path, results, args, total_input_tokens, total_output_tokens, parse_failures)\n\n    # Final save\n    _save_results(output_path, results, args, total_input_tokens, total_output_tokens, parse_failures)\n\n    # Final metrics\n    print(\"\\n\" + \"=\" * 60)\n    valid_results = [r for r in results if r[\"predicted_label\"] != -1]\n    if valid_results:\n        preds = [r[\"predicted_label\"] for r in valid_results]\n        labels = [r[\"true_label\"] for r in valid_results]\n        metrics = compute_metrics(labels, preds)\n\n        print(f\"Model: {args.model} | Mode: {args.mode}\")\n        print(f\"Windows evaluated: {len(results)} ({len(valid_results)} valid, {parse_failures} parse failures)\")\n        print(f\"\\n{'Metric':<20} {'Value':>10}\")\n        print(\"-\" * 32)\n        for k, v in metrics.items():\n            print(f\"{k:<20} {v:>10.4f}\")\n\n        print(f\"\\nGRU Probe reference: macro_f1 = 0.9055\")\n        print(f\"LLM Judge:          macro_f1 = {metrics['macro_f1']:.4f}\")\n        print(f\"Delta:              {metrics['macro_f1'] - 0.9055:+.4f}\")\n    else:\n        print(\"No valid results to compute metrics.\")\n\n    # Cost summary\n    est_cost = (total_input_tokens * 3 + total_output_tokens * 15) / 1_000_000\n    print(f\"\\n--- Cost Summary ---\")\n    print(f\"Input tokens:  {total_input_tokens:>12,}\")\n    print(f\"Output tokens: {total_output_tokens:>12,}\")\n    print(f\"Total tokens:  {total_input_tokens + total_output_tokens:>12,}\")\n    print(f\"Est. cost:     ${est_cost:>11.4f} (assuming $3/M input, $15/M output)\")\n    if len(results) > 0:\n        per_window = est_cost / len(results)\n        remaining = len(test_windows) - len(results)\n        print(f\"Per window:    ${per_window:.6f}\")\n        if remaining > 0:\n            print(f\"Est. remaining ({remaining} windows): ${per_window * remaining:.4f}\")\n\n    print(f\"\\nResults saved to {output_path}\")\n\n\ndef _save_results(path, results, args, total_input_tokens, total_output_tokens, parse_failures):\n    est_cost = (total_input_tokens * 3 + total_output_tokens * 15) / 1_000_000\n    output = {\n        \"model\": args.model,\n        \"mode\": args.mode,\n        \"n_windows\": len(results),\n        \"parse_failures\": parse_failures,\n        \"total_input_tokens\": total_input_tokens,\n        \"total_output_tokens\": total_output_tokens,\n        \"est_cost_usd\": round(est_cost, 4),\n        \"results\": results,\n    }\n    with open(path, \"w\") as f:\n        json.dump(output, f, indent=2, ensure_ascii=False)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 460,
      "startLine": 1,
      "totalLines": 460
    }
  }
}
````

</details>

---


### Assistant

_source line 119_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the existing codebase. Let me also check if there's an existing `src/evaluation/` directory and what the actual source directory structure looks like.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "c4ba67c8-0c6e-4147-be7a-52b738bdfa71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HkWMigZ6n5nJaoQ6ksqU8x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17471,
      "cache_read_input_tokens": 40688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17471
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

Let me check the target directory structure and look for any existing LLM judge prediction files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "2b45cfcc-318c-4ef1-8f51-839f21ced159",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HkWMigZ6n5nJaoQ6ksqU8x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17471,
      "cache_read_input_tokens": 40688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17471
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

<details open><summary>🔧 Tool call — Bash · `toolu_01HuYDokgND5ZZMUmRtHLsbZ`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/ 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/ 2>/dev/null || echo \"no src dir\"",
  "description": "Check target directory structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "dada343e-f962-42a3-baf1-cc678c175a9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HkWMigZ6n5nJaoQ6ksqU8x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17471,
      "cache_read_input_tokens": 40688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17471
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

_source line 122 · 2026-05-14T22:42:10.741Z_

<details><summary>↩ Tool result · `toolu_01HuYDokgND5ZZMUmRtHLsbZ`</summary>

```text
---
no src dir
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "fc1b6a77-8762-4b93-abb9-d19aa330ddff",
  "tool_use_result": {
    "stdout": "---\nno src dir",
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

_source line 123_

<details open><summary>🔧 Tool call — Glob · `toolu_0171uPh7UGu7Gi8DzRnVSqmU`</summary>

```json
{
  "pattern": "**/llm_judge_results*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "d973f26f-4858-4b9d-b9ae-f1cef7fbdde3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HkWMigZ6n5nJaoQ6ksqU8x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17471,
      "cache_read_input_tokens": 40688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17471
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

_source line 124 · 2026-05-14T22:42:11.163Z_

<details><summary>↩ Tool result · `toolu_0171uPh7UGu7Gi8DzRnVSqmU`</summary>

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
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "423663c7-58d0-4757-9c8a-71ae4b846d13",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 73,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 125_

<details open><summary>🔧 Tool call — Bash · `toolu_01EYEdA9KusZ8Je1pJzNTDnX`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation",
  "description": "Create target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "db699b4b-6b6c-4351-930c-a497bf3e5a06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ui35UZsQQtkMdHpRn67AM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 489,
      "cache_read_input_tokens": 58159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 489
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

_source line 126 · 2026-05-14T22:42:14.238Z_

<details><summary>↩ Tool result · `toolu_01EYEdA9KusZ8Je1pJzNTDnX`</summary>

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
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "f3667b94-b573-47b8-b0f9-abf5ea1cf6de",
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


### Assistant

_source line 127_

Now I'll write the gold-set evaluation pipeline. It builds on the existing `evaluate_gold_set.py` patterns but adds: LLM-as-judge support, Cohen's kappa, confidence stratification, reliability diagrams, argparse CLI with `--models` selector, and JSON + PDF outputs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "6739ed24-19f6-4dc6-9559-036d332d3bea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UkTzf5vTheeKpDbJE7j3oy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 120,
      "cache_read_input_tokens": 58648,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 120
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

_source line 128_

<details open><summary>🔧 Tool call — Write · `toolu_011rFmZrDkMFvbSEtL3SsJUf`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter\nfrom difflib import SequenceMatcher\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    return np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = pdir / \"data\" / \"windows_labeled.jsonl\"\n    if not windows_path.exists():\n        windows_path = pdir / \"windows_labeled.jsonl\"\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = pdir / \"checkpoints\" / \"split_info.json\"\n    if not split_info_path.exists():\n        split_info_path = pdir / \"split_info.json\"\n    split_info = None\n    if split_info_path.exists():\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = pdir / \"data\" / \"embeddings.pt\"\n        if not emb_path.exists():\n            emb_path = pdir / \"embeddings.pt\"\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path.exists() and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if not emb_path.exists():\n                missing.append(f\"embeddings ({emb_path})\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "c2eedf1c-0806-44a5-bf8a-4d01aed1b573",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UkTzf5vTheeKpDbJE7j3oy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 120,
      "cache_read_input_tokens": 58648,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 120
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

_source line 129 · 2026-05-14T22:44:34.451Z_

<details><summary>↩ Tool result · `toolu_011rFmZrDkMFvbSEtL3SsJUf`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "449ce230-368a-4ebe-b482-52fb0165a8dc",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter\nfrom difflib import SequenceMatcher\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    return np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = pdir / \"data\" / \"windows_labeled.jsonl\"\n    if not windows_path.exists():\n        windows_path = pdir / \"windows_labeled.jsonl\"\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = pdir / \"checkpoints\" / \"split_info.json\"\n    if not split_info_path.exists():\n        split_info_path = pdir / \"split_info.json\"\n    split_info = None\n    if split_info_path.exists():\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = pdir / \"data\" / \"embeddings.pt\"\n        if not emb_path.exists():\n            emb_path = pdir / \"embeddings.pt\"\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path.exists() and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if not emb_path.exists():\n                missing.append(f\"embeddings ({emb_path})\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---


### Assistant

_source line 130_

Verifying the script parses arguments correctly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "272a93ba-3f9b-483c-a3d5-42b36b7ad549",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RgFxxormF1iRisq5NGiHNn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11111,
      "cache_read_input_tokens": 58768,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11111
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

_source line 131_

<details open><summary>🔧 Tool call — Bash · `toolu_019G23CWY2DqDbgK1TNqeb33`</summary>

```json
{
  "command": "python3 src/evaluation/gold_set_eval.py --help",
  "description": "Verify CLI argument parsing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "06722843-6795-4c75-86b3-2bc940e45488",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RgFxxormF1iRisq5NGiHNn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11111,
      "cache_read_input_tokens": 58768,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11111
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

_source line 132 · 2026-05-14T22:44:38.366Z_

<details><summary>↩ Tool result · reported error · `toolu_019G23CWY2DqDbgK1TNqeb33`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py", line 36, in &lt;module>
    from sklearn.calibration import calibration_curve
ModuleNotFoundError: No module named 'sklearn'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "5246058e-cf5b-4d88-b2ab-e89bba5795fa",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py\", line 36, in &lt;module>\n    from sklearn.calibration import calibration_curve\nModuleNotFoundError: No module named 'sklearn'"
}
```

</details>

---


### Tool call

_source line 133_

<details open><summary>🔧 Tool call — Bash · `toolu_01FNFBEMEoSJBoAqb2S6LTbm`</summary>

```json
{
  "command": "pip install scikit-learn matplotlib 2>&1 | tail -3",
  "description": "Install required dependencies"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "e81a6110-133a-4186-baf9-ff074416405b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dd2oMAemAxz6LYveMd4EpK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 208,
      "cache_read_input_tokens": 69879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 208
      },
      "output_tokens": 51,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 134 · 2026-05-14T22:44:42.010Z_

<details><summary>↩ Tool result · `toolu_01FNFBEMEoSJBoAqb2S6LTbm`</summary>

```text
note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "4698d560-49fc-42e1-b0bc-2f91a83ba05f",
  "tool_use_result": {
    "stdout": "note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.\nhint: See PEP 668 for the detailed specification.",
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

_source line 135_

<details open><summary>🔧 Tool call — Bash · `toolu_011FMdENS1bKEBkCZKA7zNqf`</summary>

```json
{
  "command": "python3 -m venv /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/.venv && source /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/.venv/bin/activate && pip install scikit-learn matplotlib numpy torch 2>&1 | tail -5",
  "description": "Create venv and install deps",
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
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "7433e03c-b129-4f71-abac-e4a473246e68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019KodqEu2KWGM6YbfJeRQX2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 157,
      "cache_read_input_tokens": 70087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 157
      },
      "output_tokens": 59,
      "service_tier": "standard",
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

_source line 136_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "br3m8rctg",
  "tool_use_id": "toolu_011FMdENS1bKEBkCZKA7zNqf",
  "description": "Create venv and install deps",
  "task_type": "local_bash",
  "uuid": "f656f2e6-6931-4032-88b7-c5104626ecc0",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### System

_source line 137_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "br3m8rctg",
  "tool_use_id": "toolu_011FMdENS1bKEBkCZKA7zNqf",
  "status": "completed",
  "output_file": "",
  "summary": "Create venv and install deps",
  "uuid": "fbb991f0-ab58-40d9-a0f5-fdfa677fbb7e",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool result

_source line 138 · 2026-05-14T22:45:07.521Z_

<details><summary>↩ Tool result · `toolu_011FMdENS1bKEBkCZKA7zNqf`</summary>

```text
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 35.2/35.2 MB 188.2 MB/s eta 0:00:00
Downloading threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
Installing collected packages: threadpoolctl, scipy, pyparsing, pillow, kiwisolver, joblib, fonttools, cycler, contourpy, scikit-learn, matplotlib

Successfully installed contourpy-1.3.3 cycler-0.12.1 fonttools-4.63.0 joblib-1.5.3 kiwisolver-1.5.0 matplotlib-3.10.9 pillow-12.2.0 pyparsing-3.3.2 scikit-learn-1.8.0 scipy-1.17.1 threadpoolctl-3.6.0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "93e7b44b-80b7-4928-ac87-e7bf0a0f51ff",
  "tool_use_result": {
    "stdout": "   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 35.2/35.2 MB 188.2 MB/s eta 0:00:00\nDownloading threadpoolctl-3.6.0-py3-none-any.whl (18 kB)\nInstalling collected packages: threadpoolctl, scipy, pyparsing, pillow, kiwisolver, joblib, fonttools, cycler, contourpy, scikit-learn, matplotlib\n\nSuccessfully installed contourpy-1.3.3 cycler-0.12.1 fonttools-4.63.0 joblib-1.5.3 kiwisolver-1.5.0 matplotlib-3.10.9 pillow-12.2.0 pyparsing-3.3.2 scikit-learn-1.8.0 scipy-1.17.1 threadpoolctl-3.6.0",
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

_source line 139_

<details open><summary>🔧 Tool call — Bash · `toolu_01KDRYPwKccji5ZCnej3LQVG`</summary>

```json
{
  "command": "source /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/.venv/bin/activate && python3 src/evaluation/gold_set_eval.py --help",
  "description": "Verify CLI with venv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "b558802e-ead1-4198-9bf5-af0dce64241d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013rAoBpLmUtQDmdpzkfpXvh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 438,
      "cache_read_input_tokens": 70244,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 438
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


### System

_source line 140_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "b7zcsfgme",
  "tool_use_id": "toolu_01KDRYPwKccji5ZCnej3LQVG",
  "description": "Verify CLI with venv",
  "task_type": "local_bash",
  "uuid": "fdb8ea73-abf6-4a2d-9621-3a9fa2512e1e",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### System

_source line 141_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "b7zcsfgme",
  "tool_use_id": "toolu_01KDRYPwKccji5ZCnej3LQVG",
  "status": "completed",
  "output_file": "",
  "summary": "Verify CLI with venv",
  "uuid": "1d4bfaf6-2b5b-4cdd-b4c9-42df872a44f1",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool result

_source line 142 · 2026-05-14T22:45:16.222Z_

<details><summary>↩ Tool result · `toolu_01KDRYPwKccji5ZCnej3LQVG`</summary>

```text
usage: gold_set_eval.py [-h] --gold-file GOLD_FILE
                        --predictions-dir PREDICTIONS_DIR
                        [--output-dir OUTPUT_DIR]
                        [--models {silver,rf,gb,lr,gru_probe,llm_judge} [{silver,rf,gb,lr,gru_probe,llm_judge} ...]]
                        [--device DEVICE] [--llm-predictions LLM_PREDICTIONS]
                        [--checkpoint CHECKPOINT]
                        [--trajectories TRAJECTORIES] [--n-bins N_BINS]

Gold-set evaluation pipeline for agent_progress_probe

options:
  -h, --help            show this help message and exit
  --gold-file GOLD_FILE
                        Path to gold label file (CSV or JSONL). Required
                        fields: window_id, gold_label (0=stagnation,
                        1=progress). Optional: annotator_id, confidence.
  --predictions-dir PREDICTIONS_DIR
                        Directory containing model artifacts:
                        data/windows_labeled.jsonl, data/embeddings.pt,
                        checkpoints/best_model.pt,
                        checkpoints/split_info.json,
                        data/swe_agent_trajectories_5000.jsonl,
                        results/llm_judge_results.json
  --output-dir OUTPUT_DIR
                        Output directory for results JSON and reliability PDF
                        (default: artifacts)
  --models {silver,rf,gb,lr,gru_probe,llm_judge} [{silver,rf,gb,lr,gru_probe,llm_judge} ...]
                        Which models to evaluate (default: all). Choices:
                        silver, rf, gb, lr, gru_probe, llm_judge
  --device DEVICE       Torch device (default: auto)
  --llm-predictions LLM_PREDICTIONS
                        Override path to LLM-as-judge cached predictions (JSON
                        or JSONL)
  --checkpoint CHECKPOINT
                        Override path to GRU probe checkpoint (default:
                        {predictions-dir}/checkpoints/best_model.pt)
  --trajectories TRAJECTORIES
                        Override path to raw trajectories JSONL
  --n-bins N_BINS       Calibration curve bins
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "c83c5665-1044-4f0a-93cf-8a4ec94c5af9",
  "tool_use_result": {
    "stdout": "usage: gold_set_eval.py [-h] --gold-file GOLD_FILE\n                        --predictions-dir PREDICTIONS_DIR\n                        [--output-dir OUTPUT_DIR]\n                        [--models {silver,rf,gb,lr,gru_probe,llm_judge} [{silver,rf,gb,lr,gru_probe,llm_judge} ...]]\n                        [--device DEVICE] [--llm-predictions LLM_PREDICTIONS]\n                        [--checkpoint CHECKPOINT]\n                        [--trajectories TRAJECTORIES] [--n-bins N_BINS]\n\nGold-set evaluation pipeline for agent_progress_probe\n\noptions:\n  -h, --help            show this help message and exit\n  --gold-file GOLD_FILE\n                        Path to gold label file (CSV or JSONL). Required\n                        fields: window_id, gold_label (0=stagnation,\n                        1=progress). Optional: annotator_id, confidence.\n  --predictions-dir PREDICTIONS_DIR\n                        Directory containing model artifacts:\n                        data/windows_labeled.jsonl, data/embeddings.pt,\n                        checkpoints/best_model.pt,\n                        checkpoints/split_info.json,\n                        data/swe_agent_trajectories_5000.jsonl,\n                        results/llm_judge_results.json\n  --output-dir OUTPUT_DIR\n                        Output directory for results JSON and reliability PDF\n                        (default: artifacts)\n  --models {silver,rf,gb,lr,gru_probe,llm_judge} [{silver,rf,gb,lr,gru_probe,llm_judge} ...]\n                        Which models to evaluate (default: all). Choices:\n                        silver, rf, gb, lr, gru_probe, llm_judge\n  --device DEVICE       Torch device (default: auto)\n  --llm-predictions LLM_PREDICTIONS\n                        Override path to LLM-as-judge cached predictions (JSON\n                        or JSONL)\n  --checkpoint CHECKPOINT\n                        Override path to GRU probe checkpoint (default:\n                        {predictions-dir}/checkpoints/best_model.pt)\n  --trajectories TRAJECTORIES\n                        Override path to raw trajectories JSONL\n  --n-bins N_BINS       Calibration curve bins",
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

_source line 143_

`--help` 正常。现在用 silver labels (conf>=2) 做一个 dry-run 来端到端验证 pipeline。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "d6de89ec-60dd-4d92-a038-c2e1bdc19c9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVM9HVxobfo3dCS1JfusNW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 692,
      "cache_read_input_tokens": 70682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 692
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

_source line 144_

<details open><summary>🔧 Tool call — Bash · `toolu_01TEftSbrRjHCdZjSTjfr9vX`</summary>

```json
{
  "command": "source /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/.venv/bin/activate && python3 -c \"\nimport json, csv, random\n\n# Load windows, pick 200 conf>=2 as pseudo gold\nwindows = []\nwith open('artifacts/data/windows_labeled.jsonl') as f:\n    for line in f:\n        line = line.strip()\n        if not line: continue\n        w = json.loads(line)\n        if w.get('majority_label', -1) != -1 and w.get('confidence', 0) >= 2:\n            wid = f\\\"{w['trajectory_id']}__w{w['window_idx']}\\\"\n            windows.append((wid, w['majority_label']))\n\nrandom.seed(42)\nsample = random.sample(windows, min(200, len(windows)))\nwith open('/tmp/pseudo_gold.csv', 'w', newline='') as f:\n    writer = csv.writer(f)\n    writer.writerow(['window_id', 'gold_label'])\n    for wid, label in sample:\n        writer.writerow([wid, label])\nprint(f'Wrote {len(sample)} pseudo gold labels to /tmp/pseudo_gold.csv')\n\"",
  "description": "Generate pseudo gold CSV for dry-run"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "56772d5b-3303-4b0c-8a36-7fc81167adee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVM9HVxobfo3dCS1JfusNW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 692,
      "cache_read_input_tokens": 70682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 692
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

_source line 145 · 2026-05-14T22:45:25.305Z_

<details><summary>↩ Tool result · `toolu_01TEftSbrRjHCdZjSTjfr9vX`</summary>

```text
Wrote 200 pseudo gold labels to /tmp/pseudo_gold.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "3d1cb141-69f1-4684-951e-d13c2b777db9",
  "tool_use_result": {
    "stdout": "Wrote 200 pseudo gold labels to /tmp/pseudo_gold.csv",
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

_source line 146_

<details open><summary>🔧 Tool call — Bash · `toolu_01GDDT1TTJngvrDNdK6f3kvM`</summary>

```json
{
  "command": "source .venv/bin/activate && python3 src/evaluation/gold_set_eval.py --gold-file /tmp/pseudo_gold.csv --predictions-dir . --output-dir /tmp/gold_eval_test --models silver 2>&1",
  "description": "Dry-run with silver labels only",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "fba855e6-32ac-4644-b915-416287953f5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JT7bZN4Hyz5kui4hPVWDMH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 558,
      "cache_read_input_tokens": 71374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 558
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


### System

_source line 147_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "b63n5cpa0",
  "tool_use_id": "toolu_01GDDT1TTJngvrDNdK6f3kvM",
  "description": "Dry-run with silver labels only",
  "task_type": "local_bash",
  "uuid": "628d65c5-9c10-4d3d-bad9-34e44c1bdc1f",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### System

_source line 148_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "b63n5cpa0",
  "tool_use_id": "toolu_01GDDT1TTJngvrDNdK6f3kvM",
  "status": "failed",
  "output_file": "",
  "summary": "Dry-run with silver labels only",
  "uuid": "ee3ff697-07b1-456c-ad79-ab47b482e491",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool result

_source line 149 · 2026-05-14T22:45:32.926Z_

<details><summary>↩ Tool result · reported error · `toolu_01GDDT1TTJngvrDNdK6f3kvM`</summary>

```text
Exit code 1
Loading gold labels: /tmp/pseudo_gold.csv
  Total: 200, stag=70, prog=130
Loading windows: windows_labeled.jsonl
Traceback (most recent call last):
  File "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py", line 954, in &lt;module>
    main()
    ~~~~^^
  File "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py", line 702, in main
    all_windows = load_windows_jsonl(str(windows_path))
  File "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py", line 269, in load_windows_jsonl
    with open(path) as f:
         ~~~~^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'windows_labeled.jsonl'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "80cdb0bf-d21a-4978-91ff-773454ce927f",
  "tool_use_result": "Error: Exit code 1\nLoading gold labels: /tmp/pseudo_gold.csv\n  Total: 200, stag=70, prog=130\nLoading windows: windows_labeled.jsonl\nTraceback (most recent call last):\n  File \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py\", line 954, in &lt;module>\n    main()\n    ~~~~^^\n  File \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py\", line 702, in main\n    all_windows = load_windows_jsonl(str(windows_path))\n  File \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py\", line 269, in load_windows_jsonl\n    with open(path) as f:\n         ~~~~^^^^^^\nFileNotFoundError: [Errno 2] No such file or directory: 'windows_labeled.jsonl'"
}
```

</details>

---


### Assistant

_source line 150_

The `predictions-dir` is `.` but windows are under `artifacts/data/`. Let me fix the path resolution to search more candidates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "5a798c33-e7ae-42f2-889f-35af8d1dc8ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q45GXEEq7EPQhpbJmqfWXN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 442,
      "cache_read_input_tokens": 71932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 442
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

_source line 151_

<details open><summary>🔧 Tool call — Read · `toolu_015vkZPBMPau25Y66voo7EKh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "offset": 693,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "1c572ce1-4751-4121-8865-d38ac20c44c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q45GXEEq7EPQhpbJmqfWXN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 442,
      "cache_read_input_tokens": 71932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 442
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

_source line 152 · 2026-05-14T22:45:37.028Z_

<details><summary>↩ Tool result · `toolu_015vkZPBMPau25Y66voo7EKh`</summary>

```text
693	    print(f"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}")
694	
695	    # ------------------------------------------------------------------
696	    # 2. Load windows_labeled.jsonl
697	    # ------------------------------------------------------------------
698	    windows_path = pdir / "data" / "windows_labeled.jsonl"
699	    if not windows_path.exists():
700	        windows_path = pdir / "windows_labeled.jsonl"
701	    print(f"Loading windows: {windows_path}")
702	    all_windows = load_windows_jsonl(str(windows_path))
703	    non_abstain = [w for w in all_windows if w.get("majority_label", -1) != -1]
704	    print(f"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}")
705	
706	    wid_to_window = {window_id_from_window(w): w for w in non_abstain}
707	    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "b1348d05-f1a7-42be-a2a5-67b15dd1b847",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
      "content": "    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = pdir / \"data\" / \"windows_labeled.jsonl\"\n    if not windows_path.exists():\n        windows_path = pdir / \"windows_labeled.jsonl\"\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}",
      "numLines": 15,
      "startLine": 693,
      "totalLines": 955
    }
  }
}
```

</details>

---


### Tool call

_source line 153_

<details open><summary>🔧 Tool call — Edit · `toolu_01NAUc7tGqgjHFVDGxHyyZX6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "old_string": "    windows_path = pdir / \"data\" / \"windows_labeled.jsonl\"\n    if not windows_path.exists():\n        windows_path = pdir / \"windows_labeled.jsonl\"",
  "new_string": "    windows_path = None\n    for candidate in [\n        pdir / \"data\" / \"windows_labeled.jsonl\",\n        pdir / \"windows_labeled.jsonl\",\n        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",\n    ]:\n        if candidate.exists():\n            windows_path = candidate\n            break\n    if windows_path is None:\n        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")\n        sys.exit(1)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "8b2b21fe-7e50-4c48-9b9a-20cfbd7c33b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qj894hmG1RLSWHFk4ScJx6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 474,
      "cache_read_input_tokens": 72374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 474
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

_source line 154 · 2026-05-14T22:45:41.679Z_

<details><summary>↩ Tool result · `toolu_01NAUc7tGqgjHFVDGxHyyZX6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "f0768f14-dc03-411a-a1ce-d99d5a47c70d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
    "oldString": "    windows_path = pdir / \"data\" / \"windows_labeled.jsonl\"\n    if not windows_path.exists():\n        windows_path = pdir / \"windows_labeled.jsonl\"",
    "newString": "    windows_path = None\n    for candidate in [\n        pdir / \"data\" / \"windows_labeled.jsonl\",\n        pdir / \"windows_labeled.jsonl\",\n        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",\n    ]:\n        if candidate.exists():\n            windows_path = candidate\n            break\n    if windows_path is None:\n        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")\n        sys.exit(1)",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter\nfrom difflib import SequenceMatcher\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    return np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = pdir / \"data\" / \"windows_labeled.jsonl\"\n    if not windows_path.exists():\n        windows_path = pdir / \"windows_labeled.jsonl\"\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = pdir / \"checkpoints\" / \"split_info.json\"\n    if not split_info_path.exists():\n        split_info_path = pdir / \"split_info.json\"\n    split_info = None\n    if split_info_path.exists():\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = pdir / \"data\" / \"embeddings.pt\"\n        if not emb_path.exists():\n            emb_path = pdir / \"embeddings.pt\"\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path.exists() and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if not emb_path.exists():\n                missing.append(f\"embeddings ({emb_path})\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 695,
        "oldLines": 9,
        "newStart": 695,
        "newLines": 18,
        "lines": [
          "     # ------------------------------------------------------------------",
          "     # 2. Load windows_labeled.jsonl",
          "     # ------------------------------------------------------------------",
          "-    windows_path = pdir / \"data\" / \"windows_labeled.jsonl\"",
          "-    if not windows_path.exists():",
          "-        windows_path = pdir / \"windows_labeled.jsonl\"",
          "+    windows_path = None",
          "+    for candidate in [",
          "+        pdir / \"data\" / \"windows_labeled.jsonl\",",
          "+        pdir / \"windows_labeled.jsonl\",",
          "+        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",",
          "+    ]:",
          "+        if candidate.exists():",
          "+            windows_path = candidate",
          "+            break",
          "+    if windows_path is None:",
          "+        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")",
          "+        sys.exit(1)",
          "     print(f\"Loading windows: {windows_path}\")",
          "     all_windows = load_windows_jsonl(str(windows_path))",
          "     non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]"
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


### Assistant

_source line 155_

Also fix split_info and embedding path resolution similarly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "b710e177-fb73-42e1-a6e9-283aa4be8044",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018fWvRgjgtWgVLfTJWcrzSg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 365,
      "cache_read_input_tokens": 72848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 365
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

_source line 156_

<details open><summary>🔧 Tool call — Edit · `toolu_01FxKjFWqRNgf2MttnmTqrtT`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "old_string": "    split_info_path = pdir / \"checkpoints\" / \"split_info.json\"\n    if not split_info_path.exists():\n        split_info_path = pdir / \"split_info.json\"\n    split_info = None\n    if split_info_path.exists():",
  "new_string": "    split_info_path = None\n    for candidate in [\n        pdir / \"checkpoints\" / \"split_info.json\",\n        pdir / \"split_info.json\",\n        pdir / \"artifacts\" / \"split_info.json\",\n    ]:\n        if candidate.exists():\n            split_info_path = candidate\n            break\n    split_info = None\n    if split_info_path is not None:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "500013dd-0986-47b1-b861-351524addfc2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018fWvRgjgtWgVLfTJWcrzSg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 365,
      "cache_read_input_tokens": 72848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 365
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

_source line 157 · 2026-05-14T22:45:46.779Z_

<details><summary>↩ Tool result · `toolu_01FxKjFWqRNgf2MttnmTqrtT`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "a6e286a9-6045-4286-b5fd-f6a4e5930b81",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
    "oldString": "    split_info_path = pdir / \"checkpoints\" / \"split_info.json\"\n    if not split_info_path.exists():\n        split_info_path = pdir / \"split_info.json\"\n    split_info = None\n    if split_info_path.exists():",
    "newString": "    split_info_path = None\n    for candidate in [\n        pdir / \"checkpoints\" / \"split_info.json\",\n        pdir / \"split_info.json\",\n        pdir / \"artifacts\" / \"split_info.json\",\n    ]:\n        if candidate.exists():\n            split_info_path = candidate\n            break\n    split_info = None\n    if split_info_path is not None:",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter\nfrom difflib import SequenceMatcher\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    return np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = None\n    for candidate in [\n        pdir / \"data\" / \"windows_labeled.jsonl\",\n        pdir / \"windows_labeled.jsonl\",\n        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",\n    ]:\n        if candidate.exists():\n            windows_path = candidate\n            break\n    if windows_path is None:\n        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")\n        sys.exit(1)\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = pdir / \"checkpoints\" / \"split_info.json\"\n    if not split_info_path.exists():\n        split_info_path = pdir / \"split_info.json\"\n    split_info = None\n    if split_info_path.exists():\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = pdir / \"data\" / \"embeddings.pt\"\n        if not emb_path.exists():\n            emb_path = pdir / \"embeddings.pt\"\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path.exists() and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if not emb_path.exists():\n                missing.append(f\"embeddings ({emb_path})\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 718,
        "oldLines": 11,
        "newStart": 718,
        "newLines": 17,
        "lines": [
          "     # ------------------------------------------------------------------",
          "     # 3. Load split info",
          "     # ------------------------------------------------------------------",
          "-    split_info_path = pdir / \"checkpoints\" / \"split_info.json\"",
          "-    if not split_info_path.exists():",
          "-        split_info_path = pdir / \"split_info.json\"",
          "+    split_info_path = None",
          "+    for candidate in [",
          "+        pdir / \"checkpoints\" / \"split_info.json\",",
          "+        pdir / \"split_info.json\",",
          "+        pdir / \"artifacts\" / \"split_info.json\",",
          "+    ]:",
          "+        if candidate.exists():",
          "+            split_info_path = candidate",
          "+            break",
          "     split_info = None",
          "-    if split_info_path.exists():",
          "+    if split_info_path is not None:",
          "         print(f\"Loading split info: {split_info_path}\")",
          "         with open(split_info_path) as f:",
          "             split_info = json.load(f)"
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


### Assistant

_source line 158_

Now fix the trajectory path, embedding path, and checkpoint path resolution to also search under `artifacts/`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "567641e5-24fa-46ce-afae-f4e4ee44501d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V69VB7R7oco1jcrZ3JjVeX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 381,
      "cache_read_input_tokens": 73213,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 381
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

_source line 159_

<details open><summary>🔧 Tool call — Edit · `toolu_017b7tQ6wEwJvhBZP5b1C2gg`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "old_string": "        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:",
  "new_string": "        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "8d48cf14-095a-4391-a1aa-e7c274601408",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V69VB7R7oco1jcrZ3JjVeX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 381,
      "cache_read_input_tokens": 73213,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 381
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

_source line 160 · 2026-05-14T22:45:52.458Z_

<details><summary>↩ Tool result · `toolu_017b7tQ6wEwJvhBZP5b1C2gg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "f2d59e39-5e7c-45d4-bb3b-ff28107da5d3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
    "oldString": "        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:",
    "newString": "        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter\nfrom difflib import SequenceMatcher\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    return np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = None\n    for candidate in [\n        pdir / \"data\" / \"windows_labeled.jsonl\",\n        pdir / \"windows_labeled.jsonl\",\n        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",\n    ]:\n        if candidate.exists():\n            windows_path = candidate\n            break\n    if windows_path is None:\n        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")\n        sys.exit(1)\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = None\n    for candidate in [\n        pdir / \"checkpoints\" / \"split_info.json\",\n        pdir / \"split_info.json\",\n        pdir / \"artifacts\" / \"split_info.json\",\n    ]:\n        if candidate.exists():\n            split_info_path = candidate\n            break\n    split_info = None\n    if split_info_path is not None:\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = pdir / \"data\" / \"embeddings.pt\"\n        if not emb_path.exists():\n            emb_path = pdir / \"embeddings.pt\"\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path.exists() and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if not emb_path.exists():\n                missing.append(f\"embeddings ({emb_path})\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 759,
        "oldLines": 7,
        "newStart": 759,
        "newLines": 9,
        "lines": [
          "             for candidate in [",
          "                 pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",",
          "                 pdir / \"swe_agent_trajectories_5000.jsonl\",",
          "+                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_5000.jsonl\",",
          "                 pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",",
          "+                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_1000.jsonl\",",
          "             ]:",
          "                 if candidate.exists():",
          "                     traj_path = candidate"
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

_source line 161_

<details open><summary>🔧 Tool call — Edit · `toolu_01HKUNchK6SJnoGUARXPM2dz`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "old_string": "        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n            ]:",
  "new_string": "        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n                pdir / \"artifacts\" / \"best_model.pt\",\n            ]:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "f2d8aa5e-a110-4b1b-b1a9-56e1e05680c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E48CSEdPczA5AyRD6XUf9x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 449,
      "cache_read_input_tokens": 73594,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 449
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

_source line 162 · 2026-05-14T22:45:56.204Z_

<details><summary>↩ Tool result · `toolu_01HKUNchK6SJnoGUARXPM2dz`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "dda716ac-4551-4a51-8372-87ed0d068303",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
    "oldString": "        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n            ]:",
    "newString": "        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n                pdir / \"artifacts\" / \"best_model.pt\",\n            ]:",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter\nfrom difflib import SequenceMatcher\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    return np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = None\n    for candidate in [\n        pdir / \"data\" / \"windows_labeled.jsonl\",\n        pdir / \"windows_labeled.jsonl\",\n        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",\n    ]:\n        if candidate.exists():\n            windows_path = candidate\n            break\n    if windows_path is None:\n        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")\n        sys.exit(1)\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = None\n    for candidate in [\n        pdir / \"checkpoints\" / \"split_info.json\",\n        pdir / \"split_info.json\",\n        pdir / \"artifacts\" / \"split_info.json\",\n    ]:\n        if candidate.exists():\n            split_info_path = candidate\n            break\n    split_info = None\n    if split_info_path is not None:\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = pdir / \"data\" / \"embeddings.pt\"\n        if not emb_path.exists():\n            emb_path = pdir / \"embeddings.pt\"\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path.exists() and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if not emb_path.exists():\n                missing.append(f\"embeddings ({emb_path})\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 841,
        "oldLines": 6,
        "newStart": 841,
        "newLines": 7,
        "lines": [
          "             for candidate in [",
          "                 pdir / \"checkpoints\" / \"best_model.pt\",",
          "                 pdir / \"best_model.pt\",",
          "+                pdir / \"artifacts\" / \"best_model.pt\",",
          "             ]:",
          "                 if candidate.exists():",
          "                     ckpt_path = candidate"
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

_source line 163_

<details open><summary>🔧 Tool call — Edit · `toolu_01CvXaBnWrrBPHdetxBypFAU`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "old_string": "        emb_path = pdir / \"data\" / \"embeddings.pt\"\n        if not emb_path.exists():\n            emb_path = pdir / \"embeddings.pt\"",
  "new_string": "        emb_path = None\n        for candidate in [\n            pdir / \"data\" / \"embeddings.pt\",\n            pdir / \"embeddings.pt\",\n            pdir / \"artifacts\" / \"data\" / \"embeddings.pt\",\n        ]:\n            if candidate.exists():\n                emb_path = candidate\n                break"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "f574f0dd-18ed-4d68-9b68-82c060c0c1c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uu3LFdb4To92Xf9eTyoiAQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 311,
      "cache_read_input_tokens": 74043,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 311
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

_source line 164 · 2026-05-14T22:46:00.376Z_

<details><summary>↩ Tool result · `toolu_01CvXaBnWrrBPHdetxBypFAU`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "02cb59e5-5290-44d0-b6a2-cc7421d03c54",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
    "oldString": "        emb_path = pdir / \"data\" / \"embeddings.pt\"\n        if not emb_path.exists():\n            emb_path = pdir / \"embeddings.pt\"",
    "newString": "        emb_path = None\n        for candidate in [\n            pdir / \"data\" / \"embeddings.pt\",\n            pdir / \"embeddings.pt\",\n            pdir / \"artifacts\" / \"data\" / \"embeddings.pt\",\n        ]:\n            if candidate.exists():\n                emb_path = candidate\n                break",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter\nfrom difflib import SequenceMatcher\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    return np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = None\n    for candidate in [\n        pdir / \"data\" / \"windows_labeled.jsonl\",\n        pdir / \"windows_labeled.jsonl\",\n        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",\n    ]:\n        if candidate.exists():\n            windows_path = candidate\n            break\n    if windows_path is None:\n        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")\n        sys.exit(1)\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = None\n    for candidate in [\n        pdir / \"checkpoints\" / \"split_info.json\",\n        pdir / \"split_info.json\",\n        pdir / \"artifacts\" / \"split_info.json\",\n    ]:\n        if candidate.exists():\n            split_info_path = candidate\n            break\n    split_info = None\n    if split_info_path is not None:\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n                pdir / \"artifacts\" / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = pdir / \"data\" / \"embeddings.pt\"\n        if not emb_path.exists():\n            emb_path = pdir / \"embeddings.pt\"\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path.exists() and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if not emb_path.exists():\n                missing.append(f\"embeddings ({emb_path})\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 847,
        "oldLines": 9,
        "newStart": 847,
        "newLines": 15,
        "lines": [
          "                     ckpt_path = candidate",
          "                     break",
          " ",
          "-        emb_path = pdir / \"data\" / \"embeddings.pt\"",
          "-        if not emb_path.exists():",
          "-            emb_path = pdir / \"embeddings.pt\"",
          "+        emb_path = None",
          "+        for candidate in [",
          "+            pdir / \"data\" / \"embeddings.pt\",",
          "+            pdir / \"embeddings.pt\",",
          "+            pdir / \"artifacts\" / \"data\" / \"embeddings.pt\",",
          "+        ]:",
          "+            if candidate.exists():",
          "+                emb_path = candidate",
          "+                break",
          " ",
          "         print(f\"\\nEvaluating: GRU Probe ...\")",
          "         if HAS_TORCH and HAS_PROBE and emb_path.exists() and ckpt_path is not None:"
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


### Assistant

_source line 165_

Now fix the None check for emb_path in the GRU probe section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "a7132674-cc83-4f00-9a62-8bfbb6773370",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HzqVn3s2Pnv8NizzgXpKRQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 429,
      "cache_read_input_tokens": 74354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 429
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

_source line 166_

<details open><summary>🔧 Tool call — Edit · `toolu_016RtuzBpQYYwBsixAZxJGYV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "old_string": "        if HAS_TORCH and HAS_PROBE and emb_path.exists() and ckpt_path is not None:",
  "new_string": "        if HAS_TORCH and HAS_PROBE and emb_path is not None and ckpt_path is not None:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "6d35d1cc-08c3-49a9-b3a2-121fcfab91b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HzqVn3s2Pnv8NizzgXpKRQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 429,
      "cache_read_input_tokens": 74354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 429
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
