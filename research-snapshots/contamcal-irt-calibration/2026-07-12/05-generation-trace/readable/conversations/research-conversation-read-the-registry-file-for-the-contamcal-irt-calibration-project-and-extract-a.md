# Research conversation: Read the registry file for the contamcal-irt-calibration project and extract ALL experiments with status=PREPARING. For 

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a0f8d178133f84394.jsonl`
- **Structured JSON:** [`33744a33d474b9c72f50.json`](../../sessions/33/33744a33d474b9c72f50.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

15 recorded events

### User

_source line 1 · 2026-05-17T13:12:24.481Z_

Read the registry file for the contamcal-irt-calibration project and extract ALL experiments with status=PREPARING. For each one, output: exp_id, hypothesis (first 80 chars), created_at date.

The registry is a large JSON file that was saved earlier. Try reading it from:
/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-17809d4e/ef7b3b85-62a5-48d7-b7b6-9b5a9eaae037/tool-results/mcp-agent-ml-research-read_registry-1779014796334.txt

If that file doesn't exist, use the Bash tool to run:
```
python3 -c "
import json, yaml
with open('/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/registry.yaml') as f:
    reg = yaml.safe_load(f)
exps = reg.get('experiments', {})
for k, v in exps.items():
    if v.get('status') == 'PREPARING':
        hyp = (v.get('hypothesis') or '')[:80]
        created = v.get('created_at', '?')
        print(f'{k} | {created} | {hyp}')
"
```

For each PREPARING experiment, categorize:
1. Is it a GPU task (training/eval) or CPU task (IRT/analysis)?
2. Is it likely stale/historical (created weeks ago, no recent updates)?
3. Does it have dependencies that aren't met?

Return a concise table with columns: exp_id | type (GPU/CPU) | stale? | recommendation (run/skip/clean)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "2503770b-472f-4357-9c10-a27570afcefc",
  "agentId": "a0f8d178133f84394",
  "type": "user",
  "uuid": "d7a9cfe7-e98f-4055-b3de-e65c9ce9cbc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "ef7b3b85-62a5-48d7-b7b6-9b5a9eaae037",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T13:12:24.485Z_

```json
{
  "parentUuid": "d7a9cfe7-e98f-4055-b3de-e65c9ce9cbc2",
  "isSidechain": true,
  "agentId": "a0f8d178133f84394",
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
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
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
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "97666745-16a0-4f58-8379-7cae8104397d",
  "timestamp": "2026-05-17T13:12:24.485Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "ef7b3b85-62a5-48d7-b7b6-9b5a9eaae037",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-17T13:12:27.316Z_



Let me first try reading the cached registry file, and if that fails, parse the YAML directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97666745-16a0-4f58-8379-7cae8104397d",
  "isSidechain": true,
  "agentId": "a0f8d178133f84394",
  "requestId": "req_011Cb8CVPr1Uv8xe5bqofZLM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec2c4852-7016-4190-800e-dae90aa78932",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "ef7b3b85-62a5-48d7-b7b6-9b5a9eaae037",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016k1xqtjzUz4XC8HKLEsdix",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30007,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30007,
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

_source line 4 · 2026-05-17T13:12:28.504Z_

<details open><summary>🔧 Tool call — Read · `toolu_012LU1ahFhpAcgVv6o8Nr2NZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-17809d4e/ef7b3b85-62a5-48d7-b7b6-9b5a9eaae037/tool-results/mcp-agent-ml-research-read_registry-1779014796334.txt",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec2c4852-7016-4190-800e-dae90aa78932",
  "isSidechain": true,
  "agentId": "a0f8d178133f84394",
  "requestId": "req_011Cb8CVPr1Uv8xe5bqofZLM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f654bf31-d457-43e7-a696-b447561eca9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "ef7b3b85-62a5-48d7-b7b6-9b5a9eaae037",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016k1xqtjzUz4XC8HKLEsdix",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30007,
      "cache_read_input_tokens": 0,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 30007
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 202,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 30007,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 30007,
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

_source line 5 · 2026-05-17T13:12:28.822Z_

<details><summary>↩ Tool result · reported error · `toolu_012LU1ahFhpAcgVv6o8Nr2NZ`</summary>

```text
File content (58715 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f654bf31-d457-43e7-a696-b447561eca9b",
  "isSidechain": true,
  "promptId": "2503770b-472f-4357-9c10-a27570afcefc",
  "agentId": "a0f8d178133f84394",
  "type": "user",
  "uuid": "4c769b7b-fc2d-430d-a980-426a691dd827",
  "toolUseResult": "Error: File content (58715 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "f654bf31-d457-43e7-a696-b447561eca9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "ef7b3b85-62a5-48d7-b7b6-9b5a9eaae037",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-17T13:12:34.642Z_

The file is large. Let me use the YAML approach directly, which will be faster and more targeted.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c769b7b-fc2d-430d-a980-426a691dd827",
  "isSidechain": true,
  "agentId": "a0f8d178133f84394",
  "requestId": "req_011Cb8CVp1ohu3B2DJJneUM2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e820229-9213-4b31-b11d-5ae307fae7a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "ef7b3b85-62a5-48d7-b7b6-9b5a9eaae037",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016NScCu8hpfUezxNoKQADp6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1104,
      "cache_read_input_tokens": 30007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1104,
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

_source line 7 · 2026-05-17T13:12:38.962Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DPkxcYHLit2KQw9mhU7GgA`</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/registry.yaml') as f:\n    reg = yaml.safe_load(f)\nexps = reg.get('experiments', {})\nfor k, v in sorted(exps.items()):\n    if v.get('status') == 'PREPARING':\n        hyp = (v.get('hypothesis') or '')[:80]\n        created = v.get('created_at', '?')\n        plan_id = v.get('plan_id', '')\n        parent = v.get('parent', '')\n        name = v.get('name', '')\n        print(f'ID: {k}')\n        print(f'  name: {name}')\n        print(f'  hypothesis: {hyp}')\n        print(f'  created_at: {created}')\n        print(f'  plan_id: {plan_id}')\n        print(f'  parent: {parent}')\n        print()\n\"\n",
  "description": "Extract all PREPARING experiments from registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e820229-9213-4b31-b11d-5ae307fae7a2",
  "isSidechain": true,
  "agentId": "a0f8d178133f84394",
  "requestId": "req_011Cb8CVp1ohu3B2DJJneUM2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fefe09e4-1098-4de8-8e54-3d84e9df58b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "ef7b3b85-62a5-48d7-b7b6-9b5a9eaae037",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016NScCu8hpfUezxNoKQADp6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1104,
      "cache_read_input_tokens": 30007,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1104
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 363,
          "cache_read_input_tokens": 30007,
          "cache_creation_input_tokens": 1104,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1104,
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

_source line 8 · 2026-05-17T13:12:39.943Z_

<details><summary>↩ Tool result · `toolu_01DPkxcYHLit2KQw9mhU7GgA`</summary>

```text
ID: exp006-gsm8k-d024-delta
  name: 
  hypothesis: 
  created_at: 2026-05-14T19:29:24.786Z
  plan_id: 
  parent: 

ID: exp006_pooled_rrf_irt_05b_15b_v2
  name: 
  hypothesis: 
  created_at: 2026-05-16T09:05:27.235Z
  plan_id: 
  parent: 

ID: exp_001_eval_05B_d000_s42_v2
  name: 
  hypothesis: 
  created_at: 2026-05-14T02:26:38.504Z
  plan_id: 
  parent: 

ID: exp_001_eval_05B_d000_s42_v3
  name: 
  hypothesis: 0% dosage 0.5B s42 baseline evaluation (v3, 修复版 evaluate.py) — 建立基线分数用于 calibrat
  created_at: 2026-05-14T02:30:50.700Z
  plan_id: 
  parent: 

ID: exp_001_eval_05B_d000_s42_v4
  name: 
  hypothesis: 0% dosage 0.5B s42 baseline eval (v4, 清理后干净重提交)
  created_at: 2026-05-14T02:35:30.672Z
  plan_id: 
  parent: 

ID: exp_001_eval_05B_d000_s42_v6
  name: 
  hypothesis: 0% dosage 0.5B s42 baseline eval (v6, GPU 2 干净状态直接提交)
  created_at: 2026-05-14T02:40:46.586Z
  plan_id: 
  parent: 

ID: exp_001_eval_05B_d100_aligned_v2
  name: 
  hypothesis: 
  created_at: 2026-05-14T15:19:36.281Z
  plan_id: 
  parent: 

ID: exp_001_eval_05B_d100_v3
  name: 
  hypothesis: 100% dosage 0.5B s42 contaminated model evaluation (v3, 修复版 evaluate.py) — 上界 co
  created_at: 2026-05-14T02:30:53.668Z
  plan_id: 
  parent: 

ID: exp_001_eval_05B_d100_v4
  name: 
  hypothesis: 100% dosage 0.5B s42 contaminated eval (v4, 清理后干净重提交)
  created_at: 2026-05-14T02:36:09.066Z
  plan_id: 
  parent: 

ID: exp_001_eval_05B_d100_v6
  name: 
  hypothesis: 100% dosage 0.5B s42 contaminated eval (v6, GPU 2 干净状态直接提交)
  created_at: 2026-05-14T02:40:56.017Z
  plan_id: 
  parent: 

ID: exp_001_eval_3B_d000_s42_a32_aligned
  name: 
  hypothesis: 3B d000 s42 alpha=32 aligned eval. Uses D076-retrained checkpoint (lr=5e-5). 0% 
  created_at: 2026-05-16T00:49:00.839Z
  plan_id: 
  parent: 

ID: exp_001_eval_3B_d000_s42_v2
  name: 
  hypothesis: 
  created_at: 2026-05-13T23:51:39.462Z
  plan_id: 
  parent: 

ID: exp_001_eval_3B_d005_s123
  name: 
  hypothesis: 
  created_at: 2026-05-15T14:15:40.861Z
  plan_id: 
  parent: 

ID: exp_001_eval_3B_d005_s42_aligned_v2
  name: 
  hypothesis: 
  created_at: 2026-05-15T11:12:39.327Z
  plan_id: 
  parent: 

ID: exp_001_eval_3B_d025_s123
  name: 
  hypothesis: 
  created_at: 2026-05-15T14:15:38.947Z
  plan_id: 
  parent: 

ID: exp_001_eval_llama32_3B_d000_s42_v2
  name: 
  hypothesis: 
  created_at: 2026-05-16T15:01:54.766Z
  plan_id: 
  parent: 

ID: exp_001_sft_15B_d025_s123
  name: 
  hypothesis: 
  created_at: 2026-05-15T07:45:07.671Z
  plan_id: 
  parent: 

ID: exp_001_sft_3B_d000_s42
  name: 
  hypothesis: 
  created_at: 2026-05-15T19:49:49.327Z
  plan_id: 
  parent: 

ID: exp_001_sft_3B_d000_v4
  name: 
  hypothesis: 
  created_at: 2026-05-15T20:12:58.215Z
  plan_id: 
  parent: 

ID: exp_001_sft_d005_05B_r3
  name: 
  hypothesis: 5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): retry #3 after v1/v2 OOM (
  created_at: 2026-05-13T23:58:49.282Z
  plan_id: 
  parent: exp_001_sft_d005_05B

ID: exp_002_signals_15B_instruct_gsm8k_v2
  name: 
  hypothesis: 1.5B-Instruct GSM8K signals (s1/s2/s4) to expand N for cross-family pooled IRT —
  created_at: 2026-05-16T21:29:30.056Z
  plan_id: 
  parent: 

ID: exp_006_irt_05B_v2
  name: 
  hypothesis: Tiered IRT calibration (D023): GSM8K/ARC direct NUTS + MMLU subsampled 1000 item
  created_at: 2026-05-14T18:04:35.326Z
  plan_id: 
  parent: exp_006_irt_05B_v1

ID: signals_05B_s123_batch
  name: 
  hypothesis: 
  created_at: 2026-05-16T11:01:02.098Z
  plan_id: 
  parent:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fefe09e4-1098-4de8-8e54-3d84e9df58b9",
  "isSidechain": true,
  "promptId": "2503770b-472f-4357-9c10-a27570afcefc",
  "agentId": "a0f8d178133f84394",
  "type": "user",
  "uuid": "c765ebe5-6d98-4351-9609-092884980282",
  "sourceToolAssistantUUID": "fefe09e4-1098-4de8-8e54-3d84e9df58b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "ef7b3b85-62a5-48d7-b7b6-9b5a9eaae037",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-17T13:12:43.522Z_

Now let me get more details on each to determine type, staleness, and dependencies.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c765ebe5-6d98-4351-9609-092884980282",
  "isSidechain": true,
  "agentId": "a0f8d178133f84394",
  "requestId": "req_011Cb8CWXxwEpz3WCx5UnQpw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5515c772-d245-4f1b-b29a-bf8ff0486d97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "ef7b3b85-62a5-48d7-b7b6-9b5a9eaae037",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmCcWka8ssyQ2cGRZgBGXb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2173,
      "cache_read_input_tokens": 31111,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2173,
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

_source line 10 · 2026-05-17T13:12:58.701Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NA9RaVqGxmeVWBHTMhzyhU`</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\nfrom datetime import datetime, timezone\n\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/registry.yaml') as f:\n    reg = yaml.safe_load(f)\nexps = reg.get('experiments', {})\n\nnow = datetime(2026, 5, 17, tzinfo=timezone.utc)\n\npreparing = {}\nfor k, v in exps.items():\n    if v.get('status') == 'PREPARING':\n        preparing[k] = v\n\n# Also check if parents exist and their status\nfor k, v in sorted(preparing.items()):\n    hyp = (v.get('hypothesis') or '(none)')[:80]\n    created_str = v.get('created_at', '?')\n    parent = v.get('parent', '')\n    name = v.get('name', k)\n    \n    # Parse created_at\n    if isinstance(created_str, str) and 'T' in created_str:\n        try:\n            ct = datetime.fromisoformat(created_str.replace('Z', '+00:00'))\n            age_days = (now - ct).days\n        except:\n            age_days = '?'\n    else:\n        age_days = '?'\n    \n    # Determine type from hypothesis/name\n    lower_name = (k + ' ' + (v.get('hypothesis') or '')).lower()\n    if any(w in lower_name for w in ['sft', 'train', 'finetun']):\n        task_type = 'GPU-train'\n    elif any(w in lower_name for w in ['eval', 'signal', 'benchmark']):\n        task_type = 'GPU-eval'\n    elif any(w in lower_name for w in ['irt', 'calibrat', 'pooled', 'rrf']):\n        task_type = 'CPU-IRT'\n    elif 'delta' in lower_name:\n        task_type = 'CPU-analysis'\n    else:\n        task_type = 'unknown'\n    \n    # Check parent status\n    parent_status = ''\n    if parent and parent in exps:\n        parent_status = exps[parent].get('status', '?')\n    \n    # Check if there's a later version (vN+1) that succeeded\n    superseded = False\n    # Simple heuristic: check if same base with higher version exists and is DONE\n    import re\n    base_match = re.match(r'(.+?)_v(\\d+)$', k)\n    if base_match:\n        base, ver = base_match.group(1), int(base_match.group(2))\n        for other_k, other_v in exps.items():\n            other_match = re.match(r'(.+?)_v(\\d+)$', other_k)\n            if other_match and other_match.group(1) == base:\n                other_ver = int(other_match.group(2))\n                if other_ver > ver and other_v.get('status') in ('DONE', 'RUNNING', 'ANALYZING'):\n                    superseded = True\n                    break\n    \n    stale = age_days != '?' and age_days >= 2\n    \n    print(f'{k}')\n    print(f'  type={task_type} | age={age_days}d | stale={stale} | superseded={superseded}')\n    if parent:\n        print(f'  parent={parent} (status={parent_status})')\n    print(f'  hyp: {hyp}')\n    print()\n\" 2>&1\n",
  "description": "Analyze PREPARING experiments for type, staleness, dependencies"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5515c772-d245-4f1b-b29a-bf8ff0486d97",
  "isSidechain": true,
  "agentId": "a0f8d178133f84394",
  "requestId": "req_011Cb8CWXxwEpz3WCx5UnQpw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73b7e96d-da67-4beb-81dd-db55fb4e81fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "ef7b3b85-62a5-48d7-b7b6-9b5a9eaae037",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmCcWka8ssyQ2cGRZgBGXb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2173,
      "cache_read_input_tokens": 31111,
      "output_tokens": 1002,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2173
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1002,
          "cache_read_input_tokens": 31111,
          "cache_creation_input_tokens": 2173,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2173,
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

_source line 11 · 2026-05-17T13:12:59.481Z_

<details><summary>↩ Tool result · `toolu_01NA9RaVqGxmeVWBHTMhzyhU`</summary>

```text
exp006-gsm8k-d024-delta
  type=CPU-analysis | age=2d | stale=True | superseded=False
  hyp: (none)

exp006_pooled_rrf_irt_05b_15b_v2
  type=CPU-IRT | age=0d | stale=False | superseded=False
  hyp: (none)

exp_001_eval_05B_d000_s42_v2
  type=GPU-eval | age=2d | stale=True | superseded=True
  hyp: (none)

exp_001_eval_05B_d000_s42_v3
  type=GPU-eval | age=2d | stale=True | superseded=True
  hyp: 0% dosage 0.5B s42 baseline evaluation (v3, 修复版 evaluate.py) — 建立基线分数用于 calibrat

exp_001_eval_05B_d000_s42_v4
  type=GPU-eval | age=2d | stale=True | superseded=True
  hyp: 0% dosage 0.5B s42 baseline eval (v4, 清理后干净重提交)

exp_001_eval_05B_d000_s42_v6
  type=GPU-eval | age=2d | stale=True | superseded=True
  hyp: 0% dosage 0.5B s42 baseline eval (v6, GPU 2 干净状态直接提交)

exp_001_eval_05B_d100_aligned_v2
  type=GPU-eval | age=2d | stale=True | superseded=True
  hyp: (none)

exp_001_eval_05B_d100_v3
  type=GPU-eval | age=2d | stale=True | superseded=True
  hyp: 100% dosage 0.5B s42 contaminated model evaluation (v3, 修复版 evaluate.py) — 上界 co

exp_001_eval_05B_d100_v4
  type=GPU-eval | age=2d | stale=True | superseded=True
  hyp: 100% dosage 0.5B s42 contaminated eval (v4, 清理后干净重提交)

exp_001_eval_05B_d100_v6
  type=GPU-eval | age=2d | stale=True | superseded=False
  hyp: 100% dosage 0.5B s42 contaminated eval (v6, GPU 2 干净状态直接提交)

exp_001_eval_3B_d000_s42_a32_aligned
  type=GPU-train | age=0d | stale=False | superseded=False
  hyp: 3B d000 s42 alpha=32 aligned eval. Uses D076-retrained checkpoint (lr=5e-5). 0% 

exp_001_eval_3B_d000_s42_v2
  type=GPU-eval | age=3d | stale=True | superseded=True
  hyp: (none)

exp_001_eval_3B_d005_s123
  type=GPU-eval | age=1d | stale=False | superseded=False
  hyp: (none)

exp_001_eval_3B_d005_s42_aligned_v2
  type=GPU-eval | age=1d | stale=False | superseded=False
  hyp: (none)

exp_001_eval_3B_d025_s123
  type=GPU-eval | age=1d | stale=False | superseded=False
  hyp: (none)

exp_001_eval_llama32_3B_d000_s42_v2
  type=GPU-eval | age=0d | stale=False | superseded=True
  hyp: (none)

exp_001_sft_15B_d025_s123
  type=GPU-train | age=1d | stale=False | superseded=False
  hyp: (none)

exp_001_sft_3B_d000_s42
  type=GPU-train | age=1d | stale=False | superseded=False
  hyp: (none)

exp_001_sft_3B_d000_v4
  type=GPU-train | age=1d | stale=False | superseded=False
  hyp: (none)

exp_001_sft_d005_05B_r3
  type=GPU-train | age=3d | stale=True | superseded=False
  parent=exp_001_sft_d005_05B (status=DONE)
  hyp: 5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): retry #3 after v1/v2 OOM (

exp_002_signals_15B_instruct_gsm8k_v2
  type=GPU-eval | age=0d | stale=False | superseded=False
  hyp: 1.5B-Instruct GSM8K signals (s1/s2/s4) to expand N for cross-family pooled IRT —

exp_006_irt_05B_v2
  type=GPU-eval | age=2d | stale=True | superseded=False
  parent=exp_006_irt_05B_v1 (status=DONE)
  hyp: Tiered IRT calibration (D023): GSM8K/ARC direct NUTS + MMLU subsampled 1000 item

signals_05B_s123_batch
  type=GPU-eval | age=0d | stale=False | superseded=False
  hyp: (none)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73b7e96d-da67-4beb-81dd-db55fb4e81fd",
  "isSidechain": true,
  "promptId": "2503770b-472f-4357-9c10-a27570afcefc",
  "agentId": "a0f8d178133f84394",
  "type": "user",
  "uuid": "ea8b741c-69aa-4b3d-9232-61966679baca",
  "sourceToolAssistantUUID": "73b7e96d-da67-4beb-81dd-db55fb4e81fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "ef7b3b85-62a5-48d7-b7b6-9b5a9eaae037",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-17T13:13:11.581Z_

Now let me check for the superseded v6 entry to be thorough.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea8b741c-69aa-4b3d-9232-61966679baca",
  "isSidechain": true,
  "agentId": "a0f8d178133f84394",
  "requestId": "req_011Cb8CXya6CNWt4pgrzpiui",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6165580e-333f-44ea-87c0-555f1c28cb67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "ef7b3b85-62a5-48d7-b7b6-9b5a9eaae037",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZ9LhPmR7RwWTCJGGyYzyb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2449,
      "cache_read_input_tokens": 33284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2449,
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

_source line 13 · 2026-05-17T13:13:18.402Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016kkRiJ3uuKu6Z9EXQ3sCzJ`</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/registry.yaml') as f:\n    reg = yaml.safe_load(f)\nexps = reg.get('experiments', {})\n\n# Check if exp_001_eval_05B_d100 has any later successful version\nfor k, v in sorted(exps.items()):\n    if k.startswith('exp_001_eval_05B_d100') and v.get('status') != 'PREPARING':\n        print(f'{k}: status={v.get(\\\"status\\\")} conclusion={v.get(\\\"conclusion\\\",\\\"\\\")}')\n\nprint('---')\n# Check exp_001_eval_llama32_3B supersession\nfor k, v in sorted(exps.items()):\n    if 'llama32_3B' in k:\n        print(f'{k}: status={v.get(\\\"status\\\")} conclusion={v.get(\\\"conclusion\\\",\\\"\\\")}')\n\nprint('---')\n# Check 3B d005 s42 aligned versions\nfor k, v in sorted(exps.items()):\n    if '3B_d005_s42' in k or '3B_d025_s123' in k or '3B_d005_s123' in k:\n        print(f'{k}: status={v.get(\\\"status\\\")} conclusion={v.get(\\\"conclusion\\\",\\\"\\\")}')\n\" 2>&1\n",
  "description": "Check supersession status for borderline cases"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6165580e-333f-44ea-87c0-555f1c28cb67",
  "isSidechain": true,
  "agentId": "a0f8d178133f84394",
  "requestId": "req_011Cb8CXya6CNWt4pgrzpiui",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3511870c-9bdc-47bd-8762-73df81729601",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "ef7b3b85-62a5-48d7-b7b6-9b5a9eaae037",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZ9LhPmR7RwWTCJGGyYzyb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2449,
      "cache_read_input_tokens": 33284,
      "output_tokens": 465,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2449
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 465,
          "cache_read_input_tokens": 33284,
          "cache_creation_input_tokens": 2449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2449,
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

_source line 14 · 2026-05-17T13:13:19.217Z_

<details><summary>↩ Tool result · `toolu_016kkRiJ3uuKu6Z9EXQ3sCzJ`</summary>

```text
exp_001_eval_05B_d100: status=DONE conclusion=failed
exp_001_eval_05B_d100_aligned: status=DONE conclusion=failed
exp_001_eval_05B_d100_aligned_v3: status=DONE conclusion=failed
exp_001_eval_05B_d100_aligned_v4: status=DONE conclusion=success
exp_001_eval_05B_d100_s123_aligned: status=DONE conclusion=success
exp_001_eval_05B_d100_v2: status=DONE conclusion=failed
exp_001_eval_05B_d100_v5: status=DONE conclusion=success
---
exp_001_eval_llama32_3B_d000_s42: status=DONE conclusion=killed
exp_001_eval_llama32_3B_d000_s42_v2: status=PREPARING conclusion=failed
exp_001_eval_llama32_3B_d000_s42_v3: status=DONE conclusion=success
exp_001_eval_llama32_3B_d005_s42: status=DONE conclusion=success
exp_001_eval_llama32_3B_d025_s42: status=DONE conclusion=success
exp_001_eval_llama32_3B_d100_s42: status=DONE conclusion=success
exp_001_sft_llama32_3B_d000_s42: status=DONE conclusion=success
exp_001_sft_llama32_3B_d005_s42: status=DONE conclusion=success
exp_001_sft_llama32_3B_d025_s42: status=DONE conclusion=success
exp_001_sft_llama32_3B_d100_s42: status=DONE conclusion=success
exp_002_signals_llama32_3B_d000_arc: status=DONE conclusion=success
exp_002_signals_llama32_3B_d000_arc_gsm8k: status=DONE conclusion=success
exp_002_signals_llama32_3B_d000_gsm8k: status=DONE conclusion=failed
exp_002_signals_llama32_3B_d000_gsm8k_v2: status=DONE conclusion=success
exp_002_signals_llama32_3B_d000_mmlu: status=DONE conclusion=success
exp_002_signals_llama32_3B_d005_arc_gsm8k: status=DONE conclusion=success
exp_002_signals_llama32_3B_d005_mmlu: status=DONE conclusion=success
exp_002_signals_llama32_3B_d025_completion: status=DONE conclusion=success
exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k: status=DONE conclusion=failed
exp_002_signals_llama32_3B_d100_arc: status=DONE conclusion=success
exp_002_signals_llama32_3B_d100_gsm8k: status=DONE conclusion=success
exp_002_signals_llama32_3B_d100_mmlu: status=DONE conclusion=killed
---
exp_001_eval_3B_d005_s123: status=PREPARING conclusion=
exp_001_eval_3B_d005_s123_aligned: status=DONE conclusion=success
exp_001_eval_3B_d005_s123_gsm8k: status=DONE conclusion=success
exp_001_eval_3B_d005_s123_para_aligned: status=DONE conclusion=success
exp_001_eval_3B_d005_s42_a32_batch: status=DONE conclusion=success
exp_001_eval_3B_d005_s42_aligned: status=DONE conclusion=success
exp_001_eval_3B_d005_s42_aligned_v2: status=PREPARING conclusion=killed
exp_001_eval_3B_d005_s42_para_aligned: status=DONE conclusion=success
exp_001_eval_3B_d025_s123: status=PREPARING conclusion=
exp_001_eval_3B_d025_s123_aligned: status=DONE conclusion=success
exp_001_eval_3B_d025_s123_para_aligned: status=DONE conclusion=success
exp_001_eval_llama32_3B_d005_s42: status=DONE conclusion=success
exp_001_sft_3B_d005_s123: status=DONE conclusion=success
exp_001_sft_3B_d005_s42_a32: status=DONE conclusion=success
exp_001_sft_3B_d025_s123: status=DONE conclusion=success
exp_001_sft_llama32_3B_d005_s42: status=DONE conclusion=success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3511870c-9bdc-47bd-8762-73df81729601",
  "isSidechain": true,
  "promptId": "2503770b-472f-4357-9c10-a27570afcefc",
  "agentId": "a0f8d178133f84394",
  "type": "user",
  "uuid": "62c72670-7abb-4ef2-b325-fc03d5317872",
  "sourceToolAssistantUUID": "3511870c-9bdc-47bd-8762-73df81729601",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "ef7b3b85-62a5-48d7-b7b6-9b5a9eaae037",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-17T13:13:51.098Z_

Here is the complete table of all 23 PREPARING experiments:

| exp_id | created | age | type | stale? | superseded? | recommendation |
|---|---|---|---|---|---|---|
| `exp_001_eval_05B_d000_s42_v2` | 05-14 | 3d | GPU-eval | YES | YES (v5+ DONE) | **clean** |
| `exp_001_eval_05B_d000_s42_v3` | 05-14 | 3d | GPU-eval | YES | YES (v5+ DONE) | **clean** |
| `exp_001_eval_05B_d000_s42_v4` | 05-14 | 3d | GPU-eval | YES | YES (v5+ DONE) | **clean** |
| `exp_001_eval_05B_d000_s42_v6` | 05-14 | 3d | GPU-eval | YES | YES (v5+ DONE) | **clean** |
| `exp_001_eval_05B_d100_aligned_v2` | 05-14 | 3d | GPU-eval | YES | YES (aligned_v4 DONE/success) | **clean** |
| `exp_001_eval_05B_d100_v3` | 05-14 | 3d | GPU-eval | YES | YES (v5 DONE/success) | **clean** |
| `exp_001_eval_05B_d100_v4` | 05-14 | 3d | GPU-eval | YES | YES (v5 DONE/success) | **clean** |
| `exp_001_eval_05B_d100_v6` | 05-14 | 3d | GPU-eval | YES | YES (aligned_v4 DONE/success) | **clean** |
| `exp_001_eval_3B_d000_s42_v2` | 05-13 | 4d | GPU-eval | YES | YES (later versions DONE) | **clean** |
| `exp_001_eval_llama32_3B_d000_s42_v2` | 05-16 | 1d | GPU-eval | no | YES (v3 DONE/success) | **clean** |
| `exp_001_eval_3B_d005_s42_aligned_v2` | 05-15 | 2d | GPU-eval | YES | YES (conclusion=killed, aligned DONE/success) | **clean** |
| `exp_001_eval_3B_d005_s123` | 05-15 | 2d | GPU-eval | YES | YES (aligned variant DONE/success) | **clean** |
| `exp_001_eval_3B_d025_s123` | 05-15 | 2d | GPU-eval | YES | YES (aligned variant DONE/success) | **clean** |
| `exp_001_sft_d005_05B_r3` | 05-13 | 4d | GPU-train | YES | no (parent DONE, but retry #3 after OOM) | **clean** (likely superseded by other 0.5B runs) |
| `exp_001_sft_3B_d000_s42` | 05-15 | 2d | GPU-train | YES | no | **review** (may have been superseded by v4) |
| `exp_001_sft_3B_d000_v4` | 05-15 | 2d | GPU-train | YES | no | **review** (check if 3B d000 SFT already done elsewhere) |
| `exp_001_sft_15B_d025_s123` | 05-15 | 2d | GPU-train | YES | no | **review** (may still be needed) |
| `exp006-gsm8k-d024-delta` | 05-14 | 3d | CPU-analysis | YES | no | **clean** (no hypothesis, stale) |
| `exp_006_irt_05B_v2` | 05-14 | 3d | CPU-IRT | YES | no (parent v1 DONE) | **review** (IRT calibration, may still be needed) |
| `exp006_pooled_rrf_irt_05b_15b_v2` | 05-16 | 1d | CPU-IRT | no | no | **run** (recent, pooled IRT analysis) |
| `exp_001_eval_3B_d000_s42_a32_aligned` | 05-16 | 1d | GPU-eval | no | no | **run** (recent, 3B alpha=32 aligned eval) |
| `exp_002_signals_15B_instruct_gsm8k_v2` | 05-16 | 0d | GPU-eval | no | no | **run** (recent, cross-family IRT signals) |
| `signals_05B_s123_batch` | 05-16 | 1d | GPU-eval | no | no | **run** (recent, signal batch) |

**Summary:**

- **13 to clean** - Superseded by later successful versions (v2/v3/v4/v5/v6 chains where a later version reached DONE/success). These are historical retry artifacts.
- **3 to review** - Stale but not clearly superseded: `exp_001_sft_3B_d000_s42`, `exp_001_sft_3B_d000_v4`, `exp_001_sft_15B_d025_s123`, `exp_006_irt_05B_v2`. Need to verify whether the underlying task was completed another way.
- **4 to run** - Recent (0-1 days old), not superseded: `exp006_pooled_rrf_irt_05b_15b_v2` (CPU-IRT), `exp_001_eval_3B_d000_s42_a32_aligned` (GPU-eval), `exp_002_signals_15B_instruct_gsm8k_v2` (GPU-eval), `signals_05B_s123_batch` (GPU-eval).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62c72670-7abb-4ef2-b325-fc03d5317872",
  "isSidechain": true,
  "agentId": "a0f8d178133f84394",
  "requestId": "req_011Cb8CZRsAX9RttLbTqKMJp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4570e80e-fd52-41d4-95d1-0ba616d39fac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "ef7b3b85-62a5-48d7-b7b6-9b5a9eaae037",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017hiPJQDjR69tBhuzTMgHBr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1682,
      "cache_read_input_tokens": 35733,
      "output_tokens": 1532,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1682
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1532,
          "cache_read_input_tokens": 35733,
          "cache_creation_input_tokens": 1682,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1682,
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
