# Research conversation: [CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。 详情: Process exited cleanly, W&B data available - exp_id: qwen14b_dens

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-3/f10c8440-160d-45f2-b3c9-6c60a26f3fd0.jsonl`
- **Structured JSON:** [`238e31ad830445ed9575.json`](../../sessions/23/238e31ad830445ed9575.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T18:18:13.759Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T18:18:13.759Z",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "content": "[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。\n详情: Process exited cleanly, W&B data available\n\n- exp_id: qwen14b_dense_4task_v2\n- project: distill_sparse_swiglu\n- server: westd-41718\n- log_path: ~/runs/distill_sparse_swiglu/qwen14b_dense_4task_v2.log"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T18:18:13.763Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T18:18:13.763Z",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0"
}
```

---

## Round 1

50 recorded events

### User

_source line 3 · 2026-05-19T18:18:13.798Z_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: qwen14b_dense_4task_v2
- project: distill_sparse_swiglu
- server: westd-41718
- log_path: ~/runs/distill_sparse_swiglu/qwen14b_dense_4task_v2.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "4685578a-62f4-4e3c-9ae6-7efcd8955d99",
  "type": "user",
  "uuid": "2d1ccfa6-5229-43f6-ab3b-aa7e2220308b",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T18:18:13.797Z_

```json
{
  "parentUuid": "2d1ccfa6-5229-43f6-ab3b-aa7e2220308b",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
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
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
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
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
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
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
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
  "uuid": "7459d11c-4773-47ae-869f-6a833cd33ae9",
  "timestamp": "2026-05-19T18:18:13.797Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T18:18:13.797Z_

```json
{
  "parentUuid": "7459d11c-4773-47ae-869f-6a833cd33ae9",
  "isSidechain": false,
  "attachment": {
    "type": "mcp_instructions_delta",
    "addedNames": [
      "agent-ml-research"
    ],
    "addedBlocks": [
      "## agent-ml-research\nML research experiment management tools"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "24a60b00-9d65-4b5d-9fa0-ea4dbc3164b9",
  "timestamp": "2026-05-19T18:18:13.797Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-19T18:18:13.797Z_

```json
{
  "parentUuid": "24a60b00-9d65-4b5d-9fa0-ea4dbc3164b9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5e72bf51-8dff-4e3d-97ef-fe1551112aff",
  "timestamp": "2026-05-19T18:18:13.797Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze experiment results and transition to done",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0"
}
```

---

### Assistant

_source line 8 · 2026-05-19T18:18:18.669Z_

<details><summary>Logged reasoning block</summary>

```text
A CRON callback has arrived indicating that experiment `qwen14b_dense_4task_v2` has completed and is now in ANALYZING state. I need to:

1. First do session-start: read registry, reconcile crons, read report.md, read ROADMAP.md
2. Then analyze the experiment results
3. Update registry and report
4. Report to Director

Let me start by reading the registry and other project state.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e72bf51-8dff-4e3d-97ef-fe1551112aff",
  "isSidechain": false,
  "requestId": "req_011CbCPRqGQ2VSMDpA2ZkPhC",
  "type": "assistant",
  "uuid": "0dc4c4ff-7028-48db-b248-0d0a37b85839",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018SWSvT1tBpiaEhHPZcRMn6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25974,
      "cache_read_input_tokens": 11841,
      "output_tokens": 270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 270,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25974
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

### Assistant

_source line 9 · 2026-05-19T18:18:19.793Z_

Session 启动，先同步项目状态，然后处理实验完成回调。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dc4c4ff-7028-48db-b248-0d0a37b85839",
  "isSidechain": false,
  "requestId": "req_011CbCPRqGQ2VSMDpA2ZkPhC",
  "type": "assistant",
  "uuid": "a857c9af-e4d9-42a2-91ee-42fb06e2913b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018SWSvT1tBpiaEhHPZcRMn6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25974,
      "cache_read_input_tokens": 11841,
      "output_tokens": 270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 270,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25974
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

### Tool call

_source line 10 · 2026-05-19T18:18:20.570Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EPP8YMGMofEFk6SfufRSsL`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
  "max_results": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a857c9af-e4d9-42a2-91ee-42fb06e2913b",
  "isSidechain": false,
  "requestId": "req_011CbCPRqGQ2VSMDpA2ZkPhC",
  "type": "assistant",
  "uuid": "7524a631-0324-41c0-aaf4-cfd2f57814e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018SWSvT1tBpiaEhHPZcRMn6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25974,
      "cache_read_input_tokens": 11841,
      "output_tokens": 270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 270,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25974
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

_source line 11 · 2026-05-19T18:18:20.593Z_

<details><summary>↩ Tool result · `toolu_01EPP8YMGMofEFk6SfufRSsL`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__reconcile_crons"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_roadmap"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7524a631-0324-41c0-aaf4-cfd2f57814e2",
  "isSidechain": false,
  "promptId": "4685578a-62f4-4e3c-9ae6-7efcd8955d99",
  "type": "user",
  "uuid": "9fad0b94-16ab-47f5-a625-17d44b7a5ed4",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_roadmap"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
    "total_deferred_tools": 82
  },
  "sourceToolAssistantUUID": "7524a631-0324-41c0-aaf4-cfd2f57814e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T18:18:23.424Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01JBMZzropSorK2hZn6BaZrM`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fad0b94-16ab-47f5-a625-17d44b7a5ed4",
  "isSidechain": false,
  "requestId": "req_011CbCPSLYY3bdpERfoQ1PKa",
  "type": "assistant",
  "uuid": "fa64b9d5-6437-4814-b7a4-65bdc44ca0a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTZsRP8WAe8EeGpNNLVMDU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1148,
      "cache_read_input_tokens": 37815,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1148,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 245,
          "cache_read_input_tokens": 37815,
          "cache_creation_input_tokens": 1148,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1148
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

### Tool call

_source line 13 · 2026-05-19T18:18:23.895Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reconcile_crons · `toolu_019JusiCwtpfQcmien9muFJ2`</summary>

```json
{}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa64b9d5-6437-4814-b7a4-65bdc44ca0a8",
  "isSidechain": false,
  "requestId": "req_011CbCPSLYY3bdpERfoQ1PKa",
  "type": "assistant",
  "uuid": "4e1b5ace-b3ed-4b6b-9ccb-e3c1e3b6516b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTZsRP8WAe8EeGpNNLVMDU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1148,
      "cache_read_input_tokens": 37815,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1148,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 245,
          "cache_read_input_tokens": 37815,
          "cache_creation_input_tokens": 1148,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1148
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

### Tool call

_source line 14 · 2026-05-19T18:18:24.292Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017k5HxDg4GvVbz2RQzmsFEu`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e1b5ace-b3ed-4b6b-9ccb-e3c1e3b6516b",
  "isSidechain": false,
  "requestId": "req_011CbCPSLYY3bdpERfoQ1PKa",
  "type": "assistant",
  "uuid": "25610811-bc2f-4535-ad32-ccf47a08bb04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTZsRP8WAe8EeGpNNLVMDU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1148,
      "cache_read_input_tokens": 37815,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1148,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 245,
          "cache_read_input_tokens": 37815,
          "cache_creation_input_tokens": 1148,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1148
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

### Tool call

_source line 15 · 2026-05-19T18:18:24.299Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap · `toolu_01MuvrJdx7WMBGWmUoc3SNRS`</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25610811-bc2f-4535-ad32-ccf47a08bb04",
  "isSidechain": false,
  "requestId": "req_011CbCPSLYY3bdpERfoQ1PKa",
  "type": "assistant",
  "uuid": "1db9227d-c4cb-4ae9-a392-887b20f58ca0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTZsRP8WAe8EeGpNNLVMDU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1148,
      "cache_read_input_tokens": 37815,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1148,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 245,
          "cache_read_input_tokens": 37815,
          "cache_creation_input_tokens": 1148,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1148
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

_source line 16 · 2026-05-19T18:18:25.233Z_

<details><summary>↩ Tool result · `toolu_01JBMZzropSorK2hZn6BaZrM`</summary>

```text
Error: result (417,152 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-agent-97ac3267/f10c8440-160d-45f2-b3c9-6c60a26f3fd0/tool-results/mcp-agent-ml-research-read_registry-1779214705209.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-agent-97ac3267/f10c8440-160d-45f2-b3c9-6c60a26f3fd0/tool-results/mcp-agent-ml-research-read_registry-1779214705209.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-agent-97ac3267/f10c8440-160d-45f2-b3c9-6c60a26f3fd0/tool-results/mcp-agent-ml-research-read_registry-1779214705209.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa64b9d5-6437-4814-b7a4-65bdc44ca0a8",
  "isSidechain": false,
  "promptId": "4685578a-62f4-4e3c-9ae6-7efcd8955d99",
  "type": "user",
  "uuid": "cbece236-41e3-4cff-b685-8b813c5796ea",
  "toolUseResult": "Error: result (417,152 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-agent-97ac3267/f10c8440-160d-45f2-b3c9-6c60a26f3fd0/tool-results/mcp-agent-ml-research-read_registry-1779214705209.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-agent-97ac3267/f10c8440-160d-45f2-b3c9-6c60a26f3fd0/tool-results/mcp-agent-ml-research-read_registry-1779214705209.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-agent-97ac3267/f10c8440-160d-45f2-b3c9-6c60a26f3fd0/tool-results/mcp-agent-ml-research-read_registry-1779214705209.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"qwen14b_kl30_s42_gsm8k_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:52:58.669Z\", \"updated_at\": \"2026-05-19T18:18:22.084Z\", \"hypothesis\": \"KL s42 GSM8K supplement for Qwen-14B (retry). Enables KL vs TEAL comparison on reasoning task. v1 killed due to GPU contention on 41718:1.\", \"parent\": \"qwen14b_kl30_s42_eval_uniform_v3\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s42_gsm8k_v2 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks gsm8k --seq_len 2048 --gpu 0\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"166099\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_gsm8k_v2.log\", \"submitted_at\": \"2026-05-19T18:18:18.206Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-41718\", \"gpu\": \"cuda:0\", \"pid\": \"166099\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_gsm8k_v2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s42_gsm8k_v2 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks gsm8k --seq_len 2048 --gpu 0\\\"\"}}, \"qwen14b_dense_4task_v2\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:48:38.383Z\", \"updated_at\": \"2026-05-19T18:18:05.933Z\", \"hypothesis\": \"Qwen-14B dense baseline remaining 4 tasks (wikitext2, arc_challenge, winogrande, mmlu). Retry of qwen14b_dense_4task which OOMed due to GSM8K orphan process. Orphan now killed.\", \"parent\": \"qwen14b_dense_baseline\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u src/benchmark_eval.py --exp_id qwen14b_dense_4task_v2 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --dense --tasks wikitext2,arc_challenge,winogrande,mmlu --seq_len 2048 --gpu 0\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"164330\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_dense_4task_v2.log\", \"submitted_at\": \"2026-05-19T17:49:35.043Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-41718\", \"gpu\": \"cuda:1\", \"pid\": \"164330\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_dense_4task_v2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u src/benchmark_eval.py --exp_id qwen14b_dense_4task_v2 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --dense --tasks wikitext2,arc_challenge,winogrande,mmlu --seq_len 2048 --gpu 0\\\"\", \"finished_at\": \"2026-05-19T18:18:04.940Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:18:10.535756+00:00\"}]}}, \"qwen14b_dense_hspiqa\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:15:01.916Z\", \"updated_at\": \"2026-05-19T18:14:50.005Z\", \"hypothesis\": \"Qwen-14B dense baseline hellaswag+piqa supplement. Completing 6-task suite for 14B comparison table.\", \"parent\": \"qwen14b_dense_baseline\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u src/benchmark_eval.py --exp_id qwen14b_dense_hspiqa --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --dense --tasks hellaswag,piqa --seq_len 2048 --gpu 0\", \"server\": \"westd-41718\", \"gpu\": 0, \"pid\": 162200, \"model_name\": \"qwen2.5-14b\", \"data_path\": \"hellaswag,piqa (lm_eval builtin)\", \"data_count\": null, \"seed\": null, \"eval_data\": \"hellaswag,piqa\", \"checkpoint_source\": \"dense (no checkpoint)\"}, \"log_path\": \"/root/distill_sparse_swiglu/logs/qwen14b_dense_hspiqa.log\", \"checkpoint_path\": \"N/A\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T18:14:44.020Z\", \"metrics\": {\"hellaswag_acc\": 0.6444, \"hellaswag_acc_norm\": 0.8421, \"piqa_acc\": 0.809, \"piqa_acc_norm\": 0.8194}}, \"qwen14b_kl30_s42_gsm8k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:34:34.287Z\", \"updated_at\": \"2026-05-19T17:50:51.366Z\", \"hypothesis\": \"KL s42 GSM8K supplement for Qwen-14B. Enables KL vs TEAL comparison on reasoning task (Round 12 Q6).\", \"parent\": \"qwen14b_kl30_s42_eval_uniform_v3\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && CUDA_VISIBLE_DEVICES=1 python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s42_gsm8k --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks gsm8k --seq_len 2048 --gpu 0\", \"server\": \"westd-41718\", \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 1319, \"model_name\": \"Qwen2.5-14B\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt\", \"eval_data\": \"gsm8k\"}, \"failure_reason\": \"GPU contention, killed to free cuda:1 for dense_4task. Worker launched without submit_training_job (no cron monitoring).\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T17:39:17.253Z\"}, \"qwen14b_dense_4task\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:42:50.508Z\", \"updated_at\": \"2026-05-19T17:50:33.183Z\", \"hypothesis\": \"Qwen-14B dense baseline remaining 4 tasks (wikitext2, arc_challenge, winogrande, mmlu). Parallel with qwen14b_dense_hspiqa (HS+PIQA) on cuda:0 to complete full 6-task dense baseline for 14B comparison table.\", \"parent\": \"qwen14b_dense_baseline\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u src/benchmark_eval.py --exp_id qwen14b_dense_4task --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --dense --tasks wikitext2,arc_challenge,winogrande,mmlu --seq_len 2048 --gpu 0\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"163891\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_dense_4task.log\", \"submitted_at\": \"2026-05-19T17:44:42.250Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 162.1, \"gpu_hours\": 0.05}, \"server\": \"westd-41718\", \"gpu\": \"cuda:1\", \"pid\": \"163891\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_dense_4task.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u src/benchmark_eval.py --exp_id qwen14b_dense_4task --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --dense --tasks wikitext2,arc_challenge,winogrande,mmlu --seq_len 2048 --gpu 0\\\"\", \"finished_at\": \"2026-05-19T17:47:20.778Z\"}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 2.90 GiB. GPU 0 has a total capacity of 94.97 GiB of which 1.77 GiB is free. Process 163225 has 61.77 GiB memory in use. Including non-PyTorch memory, this process has 31.41 GiB memory in use. Of the allocated me\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T17:47:24.338Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T17:47:32.378208+00:00\"}]}, \"notes\": \"失败原因: CUDA OOM at MMLU loglikelihood stage. Process 163225 (orphaned child of killed gsm8k experiment PID 163224) held 61.77 GiB on cuda:1, leaving only 1.77 GiB free. lm_head forward pass needed 2.90 GiB allocation. | 已有成果: arc_challenge eval completed (~33%), wikitext2 completed. | 后续: v2 已自动重新提交 (PID 164330, westd-41718:cuda:1), orphan 已清理。\"}, \"qwen14b_teal275_hspiqa\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:48:36.615Z\", \"updated_at\": \"2026-05-19T17:49:31.357Z\", \"hypothesis\": \"TEAL@27.5% uniform HellaSwag+PIQA supplement for Qwen-14B. Completes 6-task TEAL baseline alongside qwen14b_teal275_uniform_eval_v3 (wikitext2/arc/wg/mmlu/gsm8k).\", \"parent\": \"qwen14b_teal275_uniform_eval_v3\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u src/benchmark_eval.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --baseline_mode teal_vanilla --allocation uniform --sparsity_target 0.275 --tasks hellaswag,piqa --exp_id qwen14b_teal275_hspiqa --seq_len 2048 --gpu 0\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"126076\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_teal275_hspiqa.log\", \"submitted_at\": \"2026-05-19T17:49:28.650Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"pid\": \"126076\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_teal275_hspiqa.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u src/benchmark_eval.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --baseline_mode teal_vanilla --allocation uniform --sparsity_target 0.275 --tasks hellaswag,piqa --exp_id qwen14b_teal275_hspiqa --seq_len 2048 --gpu 0\\\"\"}}, \"qwen14b_kl30_s456_eval_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T15:37:22.929Z\", \"updated_at\": \"2026-05-19T17:11:30.700Z\", \"hypothesis\": \"Qwen-14B KL s456 eval with D075 sigmoid fix + uniform allocation on westd-41718. Standard 6-task list. Re-run of v2 to verify on different server. Completing 3-seed comparison table.\", \"parent\": \"qwen14b_kl30_s456\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s456_eval_v3 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0\", \"server\": \"westd-41718\", \"gpu\": \"cuda:0\", \"pid\": 156636, \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s456_eval_v3.log\", \"account\": \"root\", \"checkpoint_source\": \"checkpoints/qwen14b_kl30_s456/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu\", \"data_path\": \"wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu\", \"data_count\": 6, \"model_name\": \"qwen2.5-14b\", \"seed\": 456, \"tasks\": [\"wikitext2\", \"arc_challenge\", \"winogrande\", \"hellaswag\", \"piqa\", \"mmlu\"], \"sparsity_target\": 0.3, \"allocation\": \"uniform\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"checkpoints/qwen14b_kl30_s456/predictor_kl_normalized.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s456_eval_v3.log\", \"completed_at\": \"2026-05-19T17:11:24.041Z\", \"metrics\": {\"wikitext2_ppl\": 7.8992, \"arc_challenge_acc_norm\": 0.5145, \"winogrande_acc\": 0.7316, \"hellaswag_acc_norm\": 0.7249, \"piqa_acc_norm\": 0.7677, \"mmlu_acc\": 0.6351}}, \"flashinfer_benchmark_llama8b_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:08:38.448Z\", \"updated_at\": \"2026-05-19T17:08:40.329Z\", \"hypothesis\": \"Wall-clock inference speedup: gather-matmul sparse FFN (30%/50% sparsity) vs dense on LLaMA-3.1-8B. Full-sparse path: all 3 projections (gate/up/down) use gathered weights. Addresses reviewer W3.\"}, \"flashinfer_benchmark_llama8b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:05:25.529Z\", \"updated_at\": \"2026-05-19T17:08:31.111Z\", \"hypothesis\": \"Wall-clock inference speedup: gather-matmul sparse FFN (30%/50% sparsity) vs dense on LLaMA-3.1-8B. Full-sparse path: all 3 projections (gate/up/down) use gathered weights. Addresses reviewer W3.\", \"spec\": {\"command\": \"python src/benchmark_flashinfer.py --output results/benchmark_flashinfer.json\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"pid\": 123470, \"model_name\": \"LLaMA-3.1-8B\", \"data_path\": \"N/A\", \"data_count\": 0, \"seed\": 42, \"log_path\": \"logs/flashinfer_benchmark.log\", \"checkpoint_source\": \"checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T17:08:31.111Z\"}, \"qwen14b_teal275_uniform_hspiqa\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T15:58:55.851Z\", \"updated_at\": \"2026-05-19T17:03:12.867Z\", \"spec\": {\"hypothesis\": \"TEAL@27.5% uniform hellaswag+piqa supplement for Qwen-14B. Completing 6-task alignment for 14B comparison table.\", \"parent\": \"qwen14b_teal275_uniform_eval_v3\", \"command\": \"HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache CUDA_VISIBLE_DEVICES=0 python -u src/benchmark_eval.py --exp_id qwen14b_teal275_uniform_hspiqa --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --baseline_mode teal_vanilla --sparsity_target 0.275 --allocation uniform --tasks hellaswag,piqa --seq_len 2048 --gpu 0\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"pid\": 119473, \"data_path\": \"/root/autodl-tmp/.hf_cache/datasets/\", \"data_count\": 0, \"model_name\": \"Qwen2.5-14B\", \"seed\": 42, \"checkpoint_source\": \"N/A (TEAL vanilla)\", \"eval_data\": \"hellaswag,piqa\", \"log_path\": \"/root/distill_sparse_swiglu/logs/qwen14b_teal275_uniform_hspiqa.log\"}, \"conclusion\": \"success\", \"metrics\": {\"hellaswag_acc\": 0.5092, \"hellaswag_acc_norm\": 0.6993, \"piqa_acc\": 0.753, \"piqa_acc_norm\": 0.7476}, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/distill_sparse_swiglu/logs/qwen14b_teal275_uniform_hspiqa.log\", \"hypothesis\": \"TEAL@27.5% uniform sparsity on Qwen2.5-14B preserves hellaswag and piqa accuracy within acceptable degradation bounds, completing the 6-task evaluation suite for the 14B model comparison table.\", \"completed_at\": \"2026-05-19T17:03:12.867Z\"}, \"qwen14b_kl30_s123_eval_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T15:12:25.174Z\", \"updated_at\": \"2026-05-19T16:40:36.656Z\", \"hypothesis\": \"Qwen-14B KL 30% s123 eval rerun with D075 sigmoid fix (teal_global_masks: sigmoid(logits) replaces degenerate mag*hard_mask) + uniform allocation on westd-41718 cuda:1. Completing multi-seed comparison table. v4 was pre-D075 on westd-34887.\", \"parent\": \"qwen14b_kl30_s123_eval_v4\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s123_eval_v5 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0\", \"server\": \"westd-41718\", \"gpu_ids\": [1], \"pid\": \"154366\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s123_eval_v5.log\", \"model_name\": \"qwen2.5-14b\", \"data_path\": \"wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu\", \"data_count\": 6, \"seed\": 123, \"checkpoint_source\": \"qwen14b_kl30_s123\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu\"}, \"conclusion\": \"success\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s123_eval_v5.log\", \"checkpoint_path\": \"checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt\", \"metrics\": {\"wikitext2_ppl\": 7.9367, \"arc_challenge_acc_norm\": 0.541, \"winogrande_acc\": 0.7403, \"hellaswag_acc_norm\": 0.7287, \"piqa_acc_norm\": 0.765, \"mmlu_acc\": 0.6234}, \"completed_at\": \"2026-05-19T16:40:36.656Z\"}, \"qwen14b_kl30_s42_eval_uniform_v3\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-19T14:22:33.970Z\", \"updated_at\": \"2026-05-19T15:56:42.110Z\", \"hypothesis\": \"Re-run of s42 eval after D075 evaluate.py teal_global_masks() fix. sigmoid(logits) replaces degenerate mag*hard_mask scoring for correct per-layer top-k neuron selection.\", \"parent\": \"qwen14b_kl30_s42_eval_uniform_v2\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s42_eval_uniform_v3 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"pid\": 114094, \"data_path\": \"wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu\", \"data_count\": 145, \"model_name\": \"qwen2.5-14b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_eval_uniform_v3.log\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt\", \"completed_at\": \"2026-05-19T15:56:35.106Z\", \"metrics\": {\"wikitext2_ppl\": 7.8715, \"arc_challenge_acc\": 0.5051, \"arc_challenge_acc_norm\": 0.5495, \"winogrande_acc\": 0.7127, \"mmlu_acc\": 0.648, \"hellaswag_acc_norm\": 0.7268, \"piqa_acc_norm\": 0.7476}}, \"qwen14b_kl30_s456_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:20:38.257Z\", \"updated_at\": \"2026-05-19T15:36:39.762Z\", \"hypothesis\": \"Qwen-14B KL s456 eval with D075 sigmoid fix + uniform allocation. Standard 6-task list. Completing 3-seed comparison table.\", \"parent\": \"qwen14b_kl30_s456\", \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-19T11:21:13.805Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s456_eval_v2 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0 2>&1\\\"\", \"finished_at\": \"2026-05-19T12:50:15.974Z\", \"training_hours\": 1.48}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s456_eval_v2 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"100060\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s456_eval_v2.log\", \"submitted_at\": \"2026-05-19T11:21:16.055Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"results/benchmark/qwen14b_kl30_s456_eval_v2/results.json\", \"wall_clock_seconds\": 5418.2, \"gpu_hours\": 1.51}, \"pid\": \"100060\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s456_eval_v2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T12:50:21.997661+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 7.6933, \"arc_challenge_acc\": 0.5051, \"arc_challenge_acc_norm\": 0.5324, \"winogrande_acc\": 0.723, \"mmlu_acc\": 0.6411, \"hellaswag_acc\": 0.5197, \"hellaswag_acc_norm\": 0.7113, \"piqa_acc\": 0.7421, \"piqa_acc_norm\": 0.7552, \"model_sparsity\": 0.275}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T12:51:34.208Z\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/qwen14b_kl30_s456/predictor_kl_normalized.pt\"}, \"qwen14b_teal30_uniform_hspiqa_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:25:23.976Z\", \"updated_at\": \"2026-05-19T15:31:08.241Z\", \"hypothesis\": \"TEAL 30% uniform on Qwen-14B HellaSwag+PIQA. Re-submit after erroneous kill (TEAL vanilla not affected by D075 bug).\", \"parent\": \"qwen14b_teal30_uniform_eval_4task\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --baseline_mode teal_vanilla --allocation uniform --sparsity_target 0.3 --tasks hellaswag,piqa --exp_id qwen14b_teal30_uniform_hspiqa_v2 --gpu 0\", \"server\": \"westd-41718\", \"gpu_ids\": [0], \"pid\": 152255, \"model_name\": \"qwen2.5-14b\", \"data_path\": \"hellaswag,piqa\", \"data_count\": 0, \"seed\": 42, \"log_path\": \"/root/distill_sparse_swiglu/logs/qwen14b_teal30_uniform_hspiqa.log\", \"checkpoint_source\": \"/root/autodl-tmp/models/qwen2.5-14b/\", \"eval_data\": \"hellaswag,piqa\", \"checkpoint_path\": \"N/A\", \"result_path\": \"/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_hspiqa_v2/results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"hellaswag_acc\": 0.4936, \"hellaswag_acc_norm\": 0.6756, \"piqa_acc\": 0.7443, \"piqa_acc_norm\": 0.7427}, \"completed_at\": \"2026-05-19T15:31:08.241Z\"}, \"qwen14b_teal275_uniform_eval_v3\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:39:28.152Z\", \"updated_at\": \"2026-05-19T15:25:28.446Z\", \"hypothesis\": \"TEAL@27.5% uniform baseline for sparsity-matched KL comparison on Qwen-14B. Fix: relaxed _uniform_topk_masks assert from 0.02 to 0.05 tolerance. Current tasks: wikitext2,arc,wg,mmlu,gsm8k. Missing hellaswag+piqa will supplement.\", \"parent\": \"qwen14b_teal275_uniform_eval_v2\", \"spec\": {\"pid\": 115174, \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"command\": \"python -u src/benchmark_eval.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --baseline_mode teal_vanilla --allocation uniform --sparsity_target 0.275 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --exp_id qwen14b_teal275_uniform_eval_v3 --seq_len 2048 --gpu 0\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"qwen2.5-14b\", \"seed\": 42, \"checkpoint_source\": \"N/A (TEAL vanilla)\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\"}}, \"qwen14b_teal275_uniform_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:25:22.236Z\", \"updated_at\": \"2026-05-19T14:33:35.288Z\", \"hypothesis\": \"TEAL@27.5% uniform baseline for sparsity-matched KL comparison. Re-submit after erroneous kill (TEAL vanilla not affected by D075 bug). Expect same results as original submission would have produced.\", \"parent\": \"qwen14b_teal30_uniform_eval_4task\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --baseline_mode teal_vanilla --allocation uniform --sparsity_target 0.275 --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --exp_id qwen14b_teal275_uniform_eval_v2 --seq_len 2048 --gpu 0\", \"server\": \"westd-34887\", \"gpu_ids\": [1], \"pid\": 113842, \"model_name\": \"qwen2.5-14b\", \"data_path\": \"wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu\", \"data_count\": 0, \"seed\": 42, \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_teal275_uniform_eval_v2.log\", \"checkpoint_source\": \"/root/autodl-tmp/models/qwen2.5-14b/\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T14:33:35.288Z\"}, \"qwen14b_teal30_uniform_hspiqa\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:19:22.790Z\", \"updated_at\": \"2026-05-19T14:16:26.699Z\", \"hypothesis\": \"TEAL 30% uniform sparsity on Qwen-14B should show consistent accuracy drop on HellaSwag and PIQA compared to dense baseline, completing the 5-task evaluation suite for the 14B comparison table.\", \"parent\": \"qwen14b_teal30_uniform_eval_4task\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --baseline_mode teal_vanilla --allocation uniform --sparsity_target 0.3 --tasks hellaswag,piqa --exp_id qwen14b_teal30_uniform_hspiqa --gpu 0\", \"server\": \"westd-41718\", \"model_name\": \"qwen2.5-14b\", \"eval_data\": \"hellaswag,piqa\", \"checkpoint_source\": \"N/A\", \"data_path\": \"N/A\", \"data_count\": 0, \"seed\": 42}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T14:16:26.699Z\"}, \"qwen14b_teal275_uniform_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:47:12.391Z\", \"updated_at\": \"2026-05-19T14:16:24.757Z\", \"hypothesis\": \"TEAL@27.5% uniform baseline provides a fair sparsity-matched comparison for KL predictor (actual 27.5% due to Layer 1-4 zero sparsity). Expect similar or slightly different PPL/downstream vs TEAL@30% since 2.5pp less pruning.\", \"parent\": \"qwen14b_teal30_uniform_eval_4task\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --baseline_mode teal_vanilla --allocation uniform --sparsity_target 0.275 --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --exp_id qwen14b_teal275_uniform_eval --seq_len 2048 --gpu 0\", \"server\": \"westd-34887\", \"data_path\": \"wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu\", \"data_count\": 0, \"model_name\": \"qwen2.5-14b\", \"seed\": \"N/A\", \"checkpoint_source\": \"N/A (TEAL vanilla baseline)\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T14:16:24.757Z\"}, \"qwen14b_kl30_s42_eval_uniform_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:23:44.297Z\", \"updated_at\": \"2026-05-19T14:16:22.737Z\", \"hypothesis\": \"Qwen-14B KL 30% s42 eval under TEAL uniform allocation will produce comparable downstream metrics to s123/s456 (also uniform), enabling valid 3-seed comparison. Retry of v1 which failed due to missing HF offline env vars (network unreachable). v2 adds HF_DATASETS_OFFLINE=1, TRANSFORMERS_OFFLINE=1, HF_HUB_OFFLINE=1.\", \"parent\": \"qwen14b_kl30_s42_eval_uniform\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s42_eval_uniform_v2 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"108969\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_eval_uniform_v2.log\", \"submitted_at\": \"2026-05-19T13:28:52.653Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2850.1, \"gpu_hours\": 0.79}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T14:16:22.737Z\"}, \"qwen14b_kl30_s42_eval_uniform\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:13:51.678Z\", \"updated_at\": \"2026-05-19T13:44:20.478Z\", \"hypothesis\": \"Qwen-14B KL 30% s42 eval under TEAL uniform allocation will produce comparable downstream metrics to s123/s456 (also uniform), enabling valid 3-seed comparison. Prior s42 eval used global_topk (the default), making it inconsistent with s123/s456 which used uniform.\", \"parent\": \"qwen14b_kl30_s42\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s42_eval_uniform --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0\", \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"checkpoint_source\": \"qwen14b_kl30_s42\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu\", \"model_name\": \"qwen2.5-14b\", \"seed\": 42, \"data_path\": \"wikitext-103\", \"data_count\": \"N/A\"}, \"conclusion\": \"failed\", \"log_path\": \"/root/distill_sparse_swiglu/logs/qwen14b_kl30_s42_eval_uniform.log\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"reproduce\": {\"finished_at\": \"2026-05-19T13:25:20.601Z\"}, \"completed_at\": \"2026-05-19T13:25:23.923Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T13:25:29.006163+00:00\"}]}, \"notes\": \"失败原因: lm-eval 加载数据集时尝试访问 HF Hub，但服务器网络不通。Traceback: RuntimeError: Cannot send a request, as the client has been closed. 根因: 提交命令缺少 HF_DATASETS_OFFLINE=1 / TRANSFORMERS_OFFLINE=1 / HF_HUB_OFFLINE=1 环境变量。已知模式（memory.md）。v2 已准备，加了离线环境变量。\"}, \"qwen14b_kl30_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T08:21:05.971Z\", \"updated_at\": \"2026-05-19T13:43:53.414Z\", \"hypothesis\": \"KL-normalized Lagrangian distillation at 30% sparsity target on Qwen2.5-14B (seed 123) will produce a predictor that achieves comparable downstream quality to dense baseline while pruning ~30% of SwiGLU intermediate activations.\", \"parent\": \"qwen14b_kl30_s42\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-19T08:21:37.397Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type kl_normalized --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target 0.3 --lambda_max 5000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_kl30_s123 --gpu 0 2>&1\\\"\", \"finished_at\": \"2026-05-19T08:38:55.316Z\", \"training_hours\": 0.29}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type kl_normalized --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target 0.3 --lambda_max 5000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_kl30_s123 --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"91294\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s123.log\", \"submitted_at\": \"2026-05-19T08:21:40.612Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 19332.8, \"gpu_hours\": 5.37}, \"pid\": \"91294\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s123.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T08:39:01.848528+00:00\"}]}, \"metrics\": {\"final_loss_kl_norm\": 0.326, \"final_kl_raw\": 0.326, \"final_sparsity\": 0.277, \"final_constraint\": 0.037, \"final_lambda\": 5000, \"final_tau\": 0.1, \"steps\": 1000, \"trainable_params\": \"117M (0.793%)\"}, \"checkpoint_path\": \"checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T13:43:53.414Z\"}, \"qwen14b_kl30_s123_eval_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:25:23.513Z\", \"updated_at\": \"2026-05-19T13:05:52.694Z\", \"hypothesis\": \"Qwen-14B KL 30% s123 benchmark eval (WikiText-2 PPL + 5 downstream: ARC/WG/HS/PIQA/MMLU) with TEAL uniform allocation. Retry after v2/v3 OOM (caused by orphan PID 93142, now killed). Multi-seed replication to confirm MMLU reversal is systematic.\", \"parent\": \"qwen14b_kl30_s123\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-19T11:25:41.684Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s123_eval_v4 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0 2>&1\\\"\", \"finished_at\": \"2026-05-19T12:55:31.217Z\", \"training_hours\": 1.5}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s123_eval_v4 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"100832\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s123_eval_v4.log\", \"submitted_at\": \"2026-05-19T11:25:43.987Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"results/benchmark/qwen14b_kl30_s123_eval_v4/results.json\", \"wall_clock_seconds\": 6008.7, \"gpu_hours\": 1.67}, \"pid\": \"100832\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s123_eval_v4.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T12:55:36.631835+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 7.6607, \"arc_challenge_acc\": 0.5222, \"arc_challenge_acc_norm\": 0.5606, \"winogrande_acc\": 0.7293, \"hellaswag_acc\": 0.5179, \"hellaswag_acc_norm\": 0.7132, \"piqa_acc\": 0.7388, \"piqa_acc_norm\": 0.7535, \"mmlu_acc\": 0.6449}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T13:05:52.694Z\"}, \"qwen14b_kl30_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T08:21:07.866Z\", \"updated_at\": \"2026-05-19T12:52:55.464Z\", \"hypothesis\": \"Qwen-14B KL 30% with seed 456 should replicate s42's MMLU reversal pattern (KL < TEAL on MMLU), confirming it is a systematic property of the loss function on this model family rather than seed-specific noise. Multi-seed replication strengthens W2 response about MMLU reversal being architecture-dependent.\", \"parent\": \"qwen14b_kl30_s42\", \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-19T08:21:45.434Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type kl_normalized --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 456 --sparsity_target 0.3 --lambda_max 5000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_kl30_s456 --gpu 0 2>&1\\\"\", \"finished_at\": \"2026-05-19T08:39:08.437Z\", \"training_hours\": 0.29}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type kl_normalized --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 456 --sparsity_target 0.3 --lambda_max 5000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_kl30_s456 --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"91451\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s456.log\", \"submitted_at\": \"2026-05-19T08:21:47.704Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 16267.8, \"gpu_hours\": 4.52}, \"pid\": \"91451\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s456.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T08:39:17.923262+00:00\"}]}, \"metrics\": {\"final_loss\": 0.3086, \"final_kl_norm\": 0.2715, \"final_sparsity\": 0.277, \"final_constraint\": 0.0366, \"final_lambda\": 5000, \"final_tau\": 0.1, \"training_steps\": 1000}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/qwen14b_kl30_s456/predictor_kl_normalized.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T12:52:55.464Z\"}, \"qwen14b_kl30_s456_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T08:41:23.198Z\", \"updated_at\": \"2026-05-19T11:28:16.323Z\", \"hypothesis\": \"Qwen-14B KL 30% s456 benchmark eval (WikiText-2 PPL + 6 downstream tasks) with TEAL uniform allocation at 30% sparsity. Multi-seed replication of qwen14b_kl30_s42 eval to confirm KL vs TEAL performance gap is systematic on Qwen-14B, not seed-specific noise.\", \"parent\": \"qwen14b_kl30_s456\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s456_eval --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu,gsm8k --seq_len 2048 --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"93278\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s456_eval.log\", \"account\": \"root\", \"data_path\": \"wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu,gsm8k\", \"data_count\": 7, \"model_name\": \"qwen2.5-14b\", \"seed\": 456, \"checkpoint_source\": \"qwen14b_kl30_s456\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu,gsm8k\", \"checkpoint_path\": \"checkpoints/qwen14b_kl30_s456/predictor_kl_normalized.pt\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T11:28:16.323Z\"}, \"qwen14b_kl30_s123_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T08:41:03.644Z\", \"updated_at\": \"2026-05-19T11:28:15.243Z\", \"hypothesis\": \"The qwen14b_kl30_s123 predictor at 30% TEAL uniform sparsity will maintain downstream benchmark performance (ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K) within acceptable degradation from the dense baseline.\", \"parent\": \"qwen14b_kl30_s123\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu,gsm8k --sparsity_mode teal_global --allocation uniform --seq_len 2048 --gpu 0 --exp_id qwen14b_kl30_s123_eval\", \"server\": \"westd-34887\", \"data_path\": \"wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu,gsm8k\", \"data_count\": 7, \"model_name\": \"qwen2.5-14b\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu,gsm8k\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s123_eval.log\", \"pid\": \"93137\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T11:27:09.250Z\"}, \"qwen14b_kl30_s123_eval_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:24:01.513Z\", \"updated_at\": \"2026-05-19T11:25:18.056Z\", \"hypothesis\": \"Qwen-14B KL 30% s123 benchmark eval (WikiText-2 PPL + 5 downstream: ARC/WG/HS/PIQA/MMLU) with TEAL uniform allocation. Retry after v2 OOM. Multi-seed replication to confirm MMLU reversal is systematic.\", \"parent\": \"qwen14b_kl30_s123\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-19T11:24:23.255Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s123_eval_v3 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0 2>&1\\\"\", \"finished_at\": \"2026-05-19T11:24:50.473Z\", \"training_hours\": 0.01}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s123_eval_v3 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"100585\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s123_eval_v3.log\", \"submitted_at\": \"2026-05-19T11:24:26.070Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 28.0, \"gpu_hours\": 0.01}, \"pid\": \"100585\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s123_eval_v3.log\", \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 27.51 GiB. GPU 0 has a total capacity of 94.97 GiB of which 2.55 GiB is free. Process 93142 has 91.87 GiB memory in use. Including non-PyTorch memory, this process has 550.00 MiB memory in use. Of the allocated m\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T11:24:54.090Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T11:24:58.595500+00:00\"}]}}, \"qwen14b_kl30_s123_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:20:36.444Z\", \"updated_at\": \"2026-05-19T11:23:55.893Z\", \"hypothesis\": \"Qwen-14B KL 30% s123 benchmark eval (WikiText-2 PPL + 5 downstream: ARC/WG/HS/PIQA/MMLU) with TEAL uniform allocation. Multi-seed replication to confirm MMLU reversal is systematic. GSM8K excluded due to generate_until cost on 14B.\", \"parent\": \"qwen14b_kl30_s123\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-19T11:21:05.995Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s123_eval_v2 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0 2>&1\\\"\", \"finished_at\": \"2026-05-19T11:21:31.704Z\", \"training_hours\": 0.01}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s123_eval_v2 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"99904\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s123_eval_v2.log\", \"submitted_at\": \"2026-05-19T11:21:08.256Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 27.6, \"gpu_hours\": 0.01}, \"pid\": \"99904\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s123_eval_v2.log\", \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 27.51 GiB. GPU 0 has a total capacity of 94.97 GiB of which 2.55 GiB is free. Process 93142 has 91.87 GiB memory in use. Including non-PyTorch memory, this process has 550.00 MiB memory in use. Of the allocated m\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T11:21:35.897Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T11:21:40.453494+00:00\"}]}}, \"teal_28.5pct_sanity\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:52:16.546Z\", \"updated_at\": \"2026-05-19T07:47:00.307Z\", \"hypothesis\": \"TEAL vanilla at 28.5% sparsity (matching KL predictor's actual achieved sparsity) produces similar PPL to TEAL at 30%, confirming the 1.5pp sparsity gap does not meaningfully affect the KL vs TEAL comparison. If PPL difference is < 0.1, the comparison is fair.\", \"spec\": {\"checkpoint_path\": \"N/A (training-free)\", \"log_path\": \"/root/distill_sparse_swiglu/logs/teal_28.5pct_sanity.log\"}, \"metrics\": {\"wikitext2_ppl\": 10.3}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T07:47:00.307Z\"}, \"mistral_dense_hellaswag_piqa\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:19:17.368Z\", \"updated_at\": \"2026-05-19T07:43:18.197Z\", \"hypothesis\": \"Mistral-7B-v0.3 Dense baseline on HellaSwag (10-shot) and PIQA (0-shot). Required to complete Dense row in tab:mistral_downstream. Parent: lm_eval_mistral_dense.\", \"parent\": \"lm_eval_mistral_dense\", \"spec\": {\"checkpoint_path\": \"N/A (dense)\", \"log_path\": \"/root/distill_sparse_swiglu/logs/mistral_dense_hellaswag_piqa.log\"}, \"metrics\": {\"hellaswag_acc_norm\": 0.832, \"piqa_acc_norm\": 0.8188}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T07:43:18.198Z\"}, \"bce_gumbel_no_penalty_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:54:15.611Z\", \"updated_at\": \"2026-05-19T07:19:51.533Z\", \"hypothesis\": \"BCE+Gumbel without adaptive penalty controller isolates the effect of Gumbel relaxation from Lagrangian sparsity control. If PPL degrades significantly vs bce_gumbel_lagrangian_isolation (38.02), penalty controller is necessary; if similar, Gumbel alone suffices.\", \"parent\": \"bce_gumbel_lagrangian_isolation\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/train_bce_gumbel_no_penalty.py --lr 3e-3 --num_steps 1000 --sparsity_target 0.5 --seed 42 --output_dir checkpoints/bce_gumbel_no_penalty_s42 --gpu 0\", \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"wikitext-103\", \"data_count\": 1, \"seed\": 42, \"checkpoint_path\": \"checkpoints/bce_gumbel_no_penalty_s42/predictor_bce_gumbel_no_penalty.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_gumbel_no_penalty_s42.log\", \"checkpoint_source\": \"train from scratch (no penalty variant)\", \"eval_data\": \"wikitext-103\"}, \"pid\": 87162, \"metrics\": {\"training_bce_loss\": 0.6307, \"training_sparsity\": 0.383, \"wikitext2_ppl\": 32.22, \"training_time_seconds\": 977.6}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T07:19:51.533Z\"}, \"qwen14b_mask_divergence_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:55:58.629Z\", \"updated_at\": \"2026-05-19T07:02:59.470Z\", \"hypothesis\": \"Per-layer Jaccard divergence between KL-predicted and magnitude-based masks on Qwen-14B reveals whether cross-scale models exhibit similar layer-wise importance disagreement patterns as LLaMA-8B. Higher divergence at specific layers indicates the predictor discovers non-trivial importance patterns beyond magnitude.\", \"spec\": {\"command\": \"bash run_mask_divergence.sh\", \"server\": \"westd-34887\", \"data_path\": \"/root/autodl-tmp/data/wikitext2/test\", \"data_count\": 32, \"model_name\": \"qwen2.5-14b + llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/qwen14b_kl30_s42 + checkpoints/kl_sparsity30_s42_v3\", \"log_path\": \"logs/mask_divergence_analysis.log\", \"checkpoint_path\": \"results/qwen14b_mask_divergence_30pct.json\"}, \"metrics\": {\"qwen14b_mean_jaccard\": 0.4016, \"qwen14b_std_jaccard\": 0.0756, \"qwen14b_max_jaccard\": 0.446, \"qwen14b_max_layer\": 11, \"qwen14b_min_jaccard\": 0.0627, \"qwen14b_min_layer\": 4, \"llama8b_mean_jaccard\": 0.3939, \"llama8b_std_jaccard\": 0.0314, \"llama8b_max_jaccard\": 0.4818, \"llama8b_max_layer\": 0, \"llama8b_min_jaccard\": 0.3528, \"llama8b_min_layer\": 14}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T07:02:59.471Z\"}, \"mistral_kl30_hellaswag_piqa\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:11:30.999Z\", \"updated_at\": \"2026-05-19T05:51:17.403Z\", \"hypothesis\": \"KL 30% predictor on Mistral-7B evaluated on HellaSwag (10-shot) and PIQA (0-shot) with TEAL uniform allocation. Completes the 7-task Mistral comparison table (KL vs TEAL). TEAL 30% baseline: HS=60.1%, PIQA=72.1%. Required for W2 cross-architecture claim.\", \"parent\": \"mistral_kl30_downstream\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-19T05:11:57.577Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id mistral_kl30_hellaswag_piqa --model_name_or_path /root/autodl-tmp/models/mistral-7b --checkpoint checkpoints/mistral_kl30_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.30 --allocation uniform --tasks hellaswag,piqa --gpu 0 2>&1\\\"\", \"finished_at\": \"2026-05-19T05:49:16.733Z\", \"training_hours\": 0.62}, \"spec\": {\"checkpoint_path\": \"checkpoints/mistral_kl30_s42/predictor_kl_normalized.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/mistral_kl30_hellaswag_piqa.log\"}, \"pid\": \"81206\", \"log_path\": \"~/runs/distill_sparse_swiglu/mistral_kl30_hellaswag_piqa.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T05:49:22.985203+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"hellaswag_acc_norm\": 0.6892, \"piqa_acc_norm\": 0.7519}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/results/benchmark/mistral_kl30_hellaswag_piqa/results.json\", \"completed_at\": \"2026-05-19T05:51:14.916Z\"}, \"eval_c1_retrain_30pct_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:38:44.698Z\", \"updated_at\": \"2026-05-19T05:20:06.906Z\", \"spec\": {\"command\": \"benchmark_eval.py C1 retrain eval\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"122794\", \"log_path\": \"~/runs/distill_sparse_swiglu/eval_c1_retrain_30pct_s456.log\", \"submitted_at\": \"2026-05-19T03:38:44.173Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"downstream tasks\", \"data_count\": 5, \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"checkpoint_path\": \"checkpoints/c1_retrain_30pct_s456/predictor_bce_kl_targets.pt\", \"wall_clock_seconds\": 5283.3, \"gpu_hours\": 1.47}, \"metrics\": {\"wikitext2_ppl\": 8.82, \"arc_challenge_acc_norm\": 0.4471, \"winogrande_acc\": 0.6993, \"mmlu_acc\": 0.4104, \"gsm8k_exact_match\": 0.066}, \"hypothesis\": \"C1 retrain eval s456: BCE predictor trained on kl_30pct_s456 oracle (matching main table) evaluated at 30% TEAL uniform. Eliminates oracle inconsistency between C1 ablation table and main results table.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T05:06:47.495Z\"}, \"eval_c1_retrain_30pct_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:38:41.759Z\", \"updated_at\": \"2026-05-19T05:20:05.795Z\", \"spec\": {\"command\": \"benchmark_eval.py C1 retrain eval\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"122653\", \"log_path\": \"~/runs/distill_sparse_swiglu/eval_c1_retrain_30pct_s123.log\", \"submitted_at\": \"2026-05-19T03:38:41.245Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"downstream tasks\", \"data_count\": 5, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"checkpoint_path\": \"checkpoints/c1_retrain_30pct_s123/predictor_bce_kl_targets.pt\", \"wall_clock_seconds\": 5284.2, \"gpu_hours\": 1.47}, \"metrics\": {\"wikitext2_ppl\": 8.84, \"arc_challenge_acc_norm\": 0.4471, \"winogrande_acc\": 0.6977, \"mmlu_acc\": 0.3992, \"gsm8k_exact_match\": 0.0682}, \"hypothesis\": \"C1 retrain eval s123: BCE predictor trained on kl_30pct_s123 oracle (matching main table) evaluated at 30% TEAL uniform. Eliminates oracle inconsistency between C1 ablation table and main results table.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T05:06:45.455Z\"}, \"c1_retrain_30pct_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:22:36.158Z\", \"updated_at\": \"2026-05-19T05:06:43.280Z\", \"spec\": {\"command\": \"train_bce_kl_targets.py C1 retrain\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"121232\", \"log_path\": \"~/runs/distill_sparse_swiglu/c1_retrain_30pct_s456.log\", \"submitted_at\": \"2026-05-19T03:23:23.125Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 1, \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"checkpoint_path\": \"checkpoints/c1_retrain_30pct_s456/predictor_bce_kl_targets.pt\", \"wall_clock_seconds\": 6200.2, \"gpu_hours\": 1.72}, \"metrics\": {\"training_agreement\": 0.977, \"training_sparsity\": 0.312, \"wikitext2_ppl\": 7.38, \"actual_sparsity\": 0.346}, \"hypothesis\": \"C1 retrain training s456: Train BCE predictor using kl_30pct_s456 oracle masks (consistent with main table), replacing kl_sparsity30_s456. Eliminates reviewer attack surface on oracle inconsistency.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T05:06:43.280Z\"}, \"c1_retrain_30pct_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:22:33.404Z\", \"updated_at\": \"2026-05-19T05:06:41.273Z\", \"spec\": {\"command\": \"train_bce_kl_targets.py C1 retrain\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"120745\", \"log_path\": \"~/runs/distill_sparse_swiglu/c1_retrain_30pct_s123.log\", \"submitted_at\": \"2026-05-19T03:22:32.813Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 1, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"checkpoint_path\": \"checkpoints/c1_retrain_30pct_s123/predictor_bce_kl_targets.pt\", \"wall_clock_seconds\": 6248.5, \"gpu_hours\": 1.74}, \"metrics\": {\"training_agreement\": 0.977, \"training_sparsity\": 0.31, \"wikitext2_ppl\": 7.54, \"actual_sparsity\": 0.332}, \"hypothesis\": \"C1 retrain training s123: Train BCE predictor using kl_30pct_s123 oracle masks (consistent with main table), replacing kl_sparsity30_s123. Eliminates reviewer attack surface on oracle inconsistency.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T05:06:41.273Z\"}, \"mistral_teal50_downstream\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:15:46.635Z\", \"updated_at\": \"2026-05-19T05:06:39.140Z\", \"hypothesis\": \"Training-free TEAL 50% uniform allocation baseline on Mistral-7B for downstream tasks (PPL + ARC + WG + MMLU + GSM8K + HellaSwag + PIQA). Completes cross-architecture sparsity regime comparison alongside KL 50% results. Required for W2 cross-architecture claim.\", \"spec\": {\"command\": \"benchmark_eval.py Mistral TEAL\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"74915\", \"log_path\": \"~/runs/distill_sparse_swiglu/mistral_teal50_downstream.log\", \"submitted_at\": \"2026-05-19T03:16:11.426Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"downstream tasks\", \"data_count\": 7, \"model_name\": \"Mistral-7B-v0.1\", \"seed\": 42, \"checkpoint_path\": \"N/A (training-free)\", \"wall_clock_seconds\": 6627.7, \"gpu_hours\": 1.84}, \"metrics\": {\"wikitext2_ppl\": 18.3061, \"arc_challenge_acc_norm\": 0.2457, \"winogrande_acc\": 0.5091, \"mmlu_acc\": 0.2635, \"gsm8k_exact_match\": 0.0341, \"hellaswag_acc_norm\": 0.3603, \"piqa_acc_norm\": 0.6045}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T05:06:39.140Z\"}, \"mistral_teal30_downstream\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:15:45.662Z\", \"updated_at\": \"2026-05-19T05:06:37.120Z\", \"hypothesis\": \"Training-free TEAL 30% uniform allocation baseline on Mistral-7B for downstream tasks (PPL + ARC + WG + MMLU + GSM8K + HellaSwag + PIQA). Without this TEAL baseline, Mistral cross-architecture comparison cannot isolate KL predictor improvement from TEAL inherent capability. Required for W2 cross-architecture claim.\", \"spec\": {\"command\": \"benchmark_eval.py Mistral TEAL\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"74835\", \"log_path\": \"~/runs/distill_sparse_swiglu/mistral_teal30_downstream.log\", \"submitted_at\": \"2026-05-19T03:16:09.014Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"downstream tasks\", \"data_count\": 7, \"model_name\": \"Mistral-7B-v0.1\", \"seed\": 42, \"checkpoint_path\": \"N/A (training-free)\", \"wall_clock_seconds\": 6628.1, \"gpu_hours\": 1.84}, \"metrics\": {\"wikitext2_ppl\": 8.3807, \"arc_challenge_acc_norm\": 0.4113, \"winogrande_acc\": 0.6354, \"mmlu_acc\": 0.4348, \"gsm8k_exact_match\": 0.1592, \"hellaswag_acc_norm\": 0.6011, \"piqa_acc_norm\": 0.7214}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T05:06:37.120Z\"}, \"c1_ablation_30pct_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:07:23.205Z\", \"updated_at\": \"2026-05-19T03:15:21.487Z\", \"hypothesis\": \"C1 causal ablation at 30% sparsity seed 456: BCE predictor trained on KL-derived oracle masks should reproduce KL quality (max Δ ≤ 2pp downstream), confirming target quality drives KL advantage across seeds. Multi-seed validation strengthens C1 claim.\", \"spec\": {\"command\": \"benchmark_eval.py C1@30% s456\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"115020\", \"log_path\": \"~/runs/distill_sparse_swiglu/c1_ablation_30pct_s456.log\", \"submitted_at\": \"2026-05-19T02:08:45.984Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"checkpoint_source\": \"c1_ablation_30pct_s456 (train)\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"checkpoints/c1_ablation_30pct_s456/predictor_bce_kl_targets.pt\", \"wall_clock_seconds\": 3995.5, \"gpu_hours\": 1.11}, \"metrics\": {\"wikitext2_ppl\": 8.84, \"mmlu_acc\": 0.367, \"winogrande_acc\": 0.6938}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T03:15:21.487Z\"}, \"c1_ablation_30pct_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:07:21.635Z\", \"updated_at\": \"2026-05-19T03:15:19.324Z\", \"hypothesis\": \"C1 causal ablation at 30% sparsity seed 123: BCE predictor trained on KL-derived oracle masks should reproduce KL quality (max Δ ≤ 2pp downstream), confirming target quality drives KL advantage across seeds. Multi-seed validation strengthens C1 claim.\", \"spec\": {\"command\": \"benchmark_eval.py C1@30% s123\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"117411\", \"log_path\": \"~/runs/distill_sparse_swiglu/c1_ablation_30pct_s123.log\", \"submitted_at\": \"2026-05-19T02:26:49.892Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"checkpoint_source\": \"c1_ablation_30pct_s123 (train)\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"checkpoints/c1_ablation_30pct_s123/predictor_bce_kl_targets.pt\", \"wall_clock_seconds\": 2909.4, \"gpu_hours\": 0.81}, \"metrics\": {\"wikitext2_ppl\": 8.83, \"mmlu_acc\": 0.3833, \"winogrande_acc\": 0.7119}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T03:15:19.324Z\"}, \"mistral_kl30_downstream\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:07:32.697Z\", \"updated_at\": \"2026-05-19T03:14:27.156Z\", \"hypothesis\": \"KL 30% predictor on Mistral-7B evaluated on downstream tasks (ARC, WG, MMLU, GSM8K) with TEAL uniform allocation. Dense Mistral baseline: ARC=60.2%, WG=78.7%, MMLU=62.4%, GSM8K=36.5%. Supports W2 cross-architecture downstream claim.\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --model_name_or_path /root/autodl-tmp/models/mistral-7b --checkpoint checkpoints/mistral_kl30_s42/predictor_kl_normalized.pt --sparsity_target 0.30 --allocation uniform --tasks arc_challenge,winogrande,mmlu,gsm8k\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"71614\", \"log_path\": \"~/runs/distill_sparse_swiglu/mistral_kl30_downstream.log\", \"submitted_at\": \"2026-05-19T02:11:32.172Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 4, \"model_name\": \"Mistral-7B-v0.1\", \"seed\": 42, \"checkpoint_source\": \"mistral_kl30_s42\", \"eval_data\": \"arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"checkpoints/mistral_kl30_s42/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 3775.0, \"gpu_hours\": 1.05}, \"metrics\": {\"arc_challenge_acc_norm\": 0.5017, \"winogrande_acc\": 0.6914, \"mmlu_acc\": 0.4404, \"gsm8k_exact_match\": 0.1114}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T03:14:27.156Z\"}, \"bce_50pct_teal_global_unified\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:07:25.925Z\", \"updated_at\": \"2026-05-19T03:14:25.300Z\", \"hypothesis\": \"BCE iso-compute predictor evaluated at 50% TEAL global_topk on unified protocol (PPL + 4 downstream tasks). Provides fair BCE comparison at 50% using same eval protocol as KL experiments. Supports N3 fair BCE comparison claim.\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --checkpoint checkpoints/bce_isocompute_v3_s42/predictor_bce.pt --sparsity_target 0.50 --allocation global_topk --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"71114\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_50pct_teal_global_unified.log\", \"submitted_at\": \"2026-05-19T02:09:18.141Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"bce_isocompute_v3_s42\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"checkpoints/bce_isocompute_v3_s42/predictor_bce.pt\", \"wall_clock_seconds\": 3907.2, \"gpu_hours\": 1.09}, \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-19T02:14:08.675Z\"}, \"metrics\": {\"wikitext2_ppl\": 27.97, \"arc_challenge_acc_norm\": 0.2765, \"winogrande_acc\": 0.5162, \"mmlu_acc\": 0.2614, \"gsm8k_exact_match\": 0.019}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T03:14:25.300Z\"}, \"bce_isocompute_hellaswag_piqa_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:08:16.119Z\", \"updated_at\": \"2026-05-19T02:32:57.874Z\", \"hypothesis\": \"BCE iso-compute predictor evaluated on HellaSwag (10-shot) and PIQA (0-shot) with TEAL uniform 30% completes the BCE row in the 6-task downstream table. Expected to show larger degradation than KL 30% (hellaswag=70.85%, piqa=74.81%). V2: submit on 34887 where checkpoint exists (M026 lesson).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id bce_isocompute_hellaswag_piqa_v2 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/bce_isocompute_v3_s42/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.30 --allocation uniform --tasks hellaswag,piqa --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"69598\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_isocompute_hellaswag_piqa_v2.log\", \"submitted_at\": \"2026-05-19T01:38:00.231Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"checkpoints/bce_isocompute_v3_s42/predictor_bce.pt\", \"wall_clock_seconds\": 3297.6, \"gpu_hours\": 0.92}, \"metrics\": {\"hellaswag_acc_norm\": 0.6281, \"piqa_acc_norm\": 0.7421}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T02:32:57.874Z\"}, \"c1_eval_30pct_s456\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:24:04.213Z\", \"updated_at\": \"2026-05-19T02:24:04.213Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && export CUDA_VISIBLE_DEVICES=1 && python -u src/benchmark_eval.py --exp_id c1_ablation_30pct_s456 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/c1_ablation_30pct_s456/predictor_bce_kl_targets.pt --sparsity_mode teal_global --sparsity_target 0.30 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"116878\", \"log_path\": \"~/runs/distill_sparse_swiglu/c1_eval_30pct_s456.log\", \"submitted_at\": \"2026-05-19T02:24:03.564Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"c1_ablation_30pct_eval_34887\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:27:54.967Z\", \"updated_at\": \"2026-05-19T01:38:57.451Z\", \"hypothesis\": \"C1@30% eval on 34887 where checkpoint exists. TEAL uniform 30%, PPL+ARC+WinoGrande+MMLU+GSM8K. Compare vs KL 30% uniform (PPL=8.82, ARC=50.3%, Wino=72.1%, MMLU=44.8%, GSM8K=14.3%).\", \"parent\": \"c1_ablation_30pct_s42_v2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id c1_ablation_30pct_eval_34887 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/c1_ablation_30pct_s42/predictor_bce_kl_targets.pt --sparsity_mode teal_global --sparsity_target 0.30 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"68680\", \"log_path\": \"~/runs/distill_sparse_swiglu/c1_ablation_30pct_eval_34887.log\", \"submitted_at\": \"2026-05-19T01:28:27.235Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"checkpoints/c1_ablation_30pct_s42/predictor_bce_kl_targets.pt\", \"notes\": \"Duplicate of c1_ablation_30pct_s42_eval_v2 (same checkpoint, same params). Registry未及时更新导致Worker误判为未提交。\", \"wall_clock_seconds\": 630.2, \"gpu_hours\": 0.18}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T01:38:57.451Z\"}, \"kl30_uniform_hellaswag_piqa\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:12:05.345Z\", \"updated_at\": \"2026-05-19T01:37:12.599Z\", \"hypothesis\": \"KL 30% uniform predictor should maintain near-dense performance on HellaSwag (10-shot) and PIQA (0-shot) at the recommended 30% operating point, consistent with graceful degradation observed on ARC/Winogrande/MMLU/GSM8K. Broadens downstream coverage from 4 to 6 tasks.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl30_uniform_hellaswag_piqa --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks hellaswag,piqa --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"60749\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_uniform_hellaswag_piqa.log\", \"submitted_at\": \"2026-05-18T23:12:36.402Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 8392.0, \"gpu_hours\": 2.33}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T01:32:28.414Z\", \"metrics\": {\"hellaswag_acc_norm\": 0.7085, \"piqa_acc_norm\": 0.7481, \"note\": \"from v2 retry\"}}, \"kl50_global_hellaswag_piqa\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:12:07.411Z\", \"updated_at\": \"2026-05-19T01:37:11.562Z\", \"hypothesis\": \"KL 50% global predictor HellaSwag/PIQA establishes upper-bound degradation at high sparsity. Expected to show larger drops than 30% but still meaningful retention, completing the 6-task regime curve at 50% sparsity.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl50_global_hellaswag_piqa --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation global_topk --tasks hellaswag,piqa --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"60890\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl50_global_hellaswag_piqa.log\", \"submitted_at\": \"2026-05-18T23:12:39.174Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 8387.4, \"gpu_hours\": 2.33}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T01:32:26.603Z\", \"metrics\": {\"hellaswag_acc_norm\": 0.5895, \"piqa_acc_norm\": 0.6948, \"note\": \"from v2 retry\"}}, \"kl50_uniform_hellaswag_piqa\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T00:30:56.542Z\", \"updated_at\": \"2026-05-19T01:36:35.995Z\", \"hypothesis\": \"KL 50% uniform predictor HellaSwag/PIQA completes the P1 table: uniform allocation at high sparsity. Expected to show moderate degradation from dense, less severe than global_topk (which had hellaswag=58.95%, piqa=69.48%).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_ENDPOINT=https://hf-mirror.com && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl50_uniform_hellaswag_piqa --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks hellaswag,piqa --gpu 0 2>&1\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"110903\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl50_uniform_hellaswag_piqa.log\", \"submitted_at\": \"2026-05-19T00:31:36.025Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 3647.1, \"gpu_hours\": 1.01}, \"metrics\": {\"hellaswag_acc_norm\": 0.5666, \"piqa_acc_norm\": 0.691}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T01:32:23.113Z\"}, \"c1_ablation_30pct_s42_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T00:32:20.594Z\", \"updated_at\": \"2026-05-19T01:34:04.236Z\", \"hypothesis\": \"C1@30% eval on 34887 (checkpoint confirmed there). PPL already measured: 9.4463. Running full downstream (ARC, WinoGrande, MMLU, GSM8K) with TEAL uniform 30%.\", \"parent\": \"c1_ablation_30pct_s42_v2\", \"spec\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"command\": \"nohup python -u src/benchmark_eval.py --checkpoint checkpoints/c1_ablation_30pct_s42/predictor_bce_kl_targets.pt --sparsity_target 0.30 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_source\": \"checkpoints/c1_ablation_30pct_s42/predictor_bce_kl_targets.pt\", \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"log_path\": \"/root/distill_sparse_swiglu/results/benchmark/c1_ablation_30pct_s42_eval/results.json\", \"checkpoint_path\": \"checkpoints/c1_ablation_30pct_s42/predictor_bce_kl_targets.pt\"}, \"metrics\": {\"wikitext2_ppl\": 9.4463, \"arc_challenge_acc_norm\": 0.4027, \"winogrande_acc\": 0.674, \"mmlu_acc\": 0.4229, \"gsm8k_exact_match\": 0.0758}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T01:34:04.236Z\"}, \"c1_ablation_30pct_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T00:23:44.772Z\", \"updated_at\": \"2026-05-19T01:32:24.856Z\", \"hypothesis\": \"C1 causal ablation at 30% sparsity: BCE predictor trained on KL-derived oracle masks should achieve similar PPL and downstream metrics as KL predictor, demonstrating target quality (not gradient coupling) drives KL advantage. V2: fixed script path (train_bce_kl_targets.py exists on 41718 not 34887).\", \"parent\": \"c1_ablation_30pct_s42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/train_bce_kl_targets.py --kl_checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --output_dir checkpoints/c1_ablation_30pct_s42 --gpu 0 --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.30 2>&1\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"110240\", \"log_path\": \"~/runs/distill_sparse_swiglu/c1_ablation_30pct_s42_v2.log\", \"submitted_at\": \"2026-05-19T00:24:26.474Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"checkpoints/c1_ablation_30pct_s42/predictor_bce_kl_targets.pt\", \"wall_clock_seconds\": 4078.4, \"gpu_hours\": 1.13}, \"metrics\": {\"agreement\": 0.975}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T01:32:24.856Z\"}, \"dense_baseline_hellaswag_piqa\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T00:04:50.389Z\", \"updated_at\": \"2026-05-19T01:32:20.749Z\", \"hypothesis\": \"Dense LLaMA-3.1-8B baseline on HellaSwag and PIQA establishes reference performance for the 6-task downstream evaluation suite. Required to compute degradation percentages for sparse predictors on these two new tasks.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id dense_baseline_hellaswag_piqa --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --dense --tasks hellaswag,piqa --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"65370\", \"log_path\": \"~/runs/distill_sparse_swiglu/dense_baseline_hellaswag_piqa.log\", \"submitted_at\": \"2026-05-19T00:24:29.304Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (dense baseline)\", \"wall_clock_seconds\": 4071.4, \"gpu_hours\": 1.13}, \"metrics\": {\"hellaswag_acc_norm\": 0.8235, \"piqa_acc_norm\": 0.809}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T01:32:20.749Z\"}, \"bce_isocompute_hellaswag_piqa\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T00:34:52.111Z\", \"updated_at\": \"2026-05-19T01:08:09.261Z\", \"hypothesis\": \"BCE iso-compute predictor evaluated on HellaSwag+PIQA with TEAL uniform 30% completes the BCE row in the 6-task downstream table. Expected to show larger degradation than KL 30% (which had hellaswag=70.85%, piqa=74.81%).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_ENDPOINT=https://hf-mirror.com && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id bce_isocompute_hellaswag_piqa --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/bce_isocompute_v3_s42/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks hellaswag,piqa --gpu 0 2>&1\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"111367\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_isocompute_hellaswag_piqa.log\", \"submitted_at\": \"2026-05-19T00:35:32.526Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"failure_reason\": \"checkpoint bce_isocompute_v3_s42/predictor_bce.pt not on 41718\", \"wall_clock_seconds\": 1956.7, \"gpu_hours\": 0.54}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T01:08:09.261Z\"}, \"c1_ablation_30pct_s42_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T00:27:36.305Z\", \"updated_at\": \"2026-05-19T00:32:18.584Z\", \"hypothesis\": \"C1@30% eval: BCE predictor trained on KL oracle masks at 30% sparsity should achieve PPL and downstream metrics close to KL 30% uniform (PPL=8.82, ARC=50.3%, Wino=72.1%, MMLU=44.8%, GSM8K=14.3%), confirming target quality drives KL advantage at the recommended operating point.\", \"parent\": \"c1_ablation_30pct_s42_v2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id c1_ablation_30pct_s42_eval --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/c1_ablation_30pct_s42/predictor_bce_kl_targets.pt --sparsity_mode teal_global --sparsity_target 0.30 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"110557\", \"log_path\": \"~/runs/distill_sparse_swiglu/c1_ablation_30pct_s42_eval.log\", \"submitted_at\": \"2026-05-19T00:28:25.644Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"failure_reason\": \"checkpoint not on 41718, only on 34887\", \"wall_clock_seconds\": 232.9, \"gpu_hours\": 0.06}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T00:32:18.584Z\"}, \"kl50_global_hellaswag_piqa_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:27:29.696Z\", \"updated_at\": \"2026-05-19T00:29:56.105Z\", \"hypothesis\": \"KL 50% global predictor HellaSwag/PIQA establishes upper-bound degradation at high sparsity. Expected to show larger drops than 30% but still meaningful retention, completing the 6-task regime curve at 50% sparsity. V2: retry after fixing HF dataset cache.\", \"parent\": \"kl50_global_hellaswag_piqa\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_ENDPOINT=https://hf-mirror.com && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl50_global_hellaswag_piqa_v2 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation global_topk --tasks hellaswag,piqa --gpu 0 2>&1\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"107873\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl50_global_hellaswag_piqa_v2.log\", \"submitted_at\": \"2026-05-18T23:30:36.539Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 3559.6, \"gpu_hours\": 0.99}, \"metrics\": {\"hellaswag_acc_norm\": 0.5895, \"piqa_acc_norm\": 0.6948}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T00:29:56.105Z\"}, \"kl30_uniform_hellaswag_piqa_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:27:28.149Z\", \"updated_at\": \"2026-05-19T00:29:54.134Z\", \"hypothesis\": \"KL 30% uniform predictor should maintain near-dense performance on HellaSwag (10-shot) and PIQA (0-shot) at the recommended 30% operating point, consistent with graceful degradation observed on ARC/Winogrande/MMLU/GSM8K. Broadens downstream coverage from 4 to 6 tasks. V2: retry after fixing HF dataset cache (hellaswag+piqa now pre-downloaded).\", \"parent\": \"kl30_uniform_hellaswag_piqa\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl30_uniform_hellaswag_piqa_v2 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks hellaswag,piqa --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"62608\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_uniform_hellaswag_piqa_v2.log\", \"submitted_at\": \"2026-05-18T23:29:59.115Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 3595.0, \"gpu_hours\": 1.0}, \"metrics\": {\"hellaswag_acc_norm\": 0.7085, \"piqa_acc_norm\": 0.7481}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T00:29:54.134Z\"}, \"kl30_s42_global_mmlu_recheck\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:25:44.731Z\", \"updated_at\": \"2026-05-19T00:03:53.079Z\", \"hypothesis\": \"s42 global 30% MMLU=25.3% is an anomalous outlier (vs s123=38.1%, s456=43.8%) likely due to eval instability rather than predictor quality, since PPL is consistent across seeds (8.93-8.98). Rerunning with identical protocol should either reproduce the low score (confirming seed-specific MMLU sensitivity) or show a normal score (confirming eval noise).\", \"parent\": \"kl30_s42_global_v3\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl30_s42_global_mmlu_recheck --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.30 --allocation global_topk --tasks mmlu --gpu 0 2>&1\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"107214\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_s42_global_mmlu_recheck.log\", \"submitted_at\": \"2026-05-18T23:26:42.040Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"results_path\": \"/root/distill_sparse_swiglu/results/benchmark/kl30_s42_global_mmlu_recheck/results.json\", \"wall_clock_seconds\": 2231.0, \"gpu_hours\": 0.62}, \"metrics\": {\"mmlu_acc\": 0.2527, \"mmlu_stderr\": 0.00364}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T00:03:53.079Z\"}, \"c1_ablation_30pct_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:25:43.181Z\", \"updated_at\": \"2026-05-19T00:03:46.334Z\", \"hypothesis\": \"C1 causal ablation at 30% sparsity (recommended operating point): BCE predictor trained on KL-derived oracle masks should achieve similar PPL and downstream metrics as the KL predictor at 30%, demonstrating that KL's advantage comes from mask quality (target effect) rather than gradient coupling. At 30% where downstream metrics are well-preserved, C1 should show smaller gaps than at 50% where degradation was severe.\", \"parent\": \"c1_ablation_s42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/train_bce_kl_targets.py --kl_checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --output_dir checkpoints/c1_ablation_30pct_s42 --gpu 0 --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.30 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/distill_sparse_swiglu/c1_ablation_30pct_s42.log\", \"submitted_at\": \"2026-05-18T23:26:38.159Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"failure_reason\": \"train_bce_kl_targets.py not found on 34887\", \"wall_clock_seconds\": 2228.2, \"gpu_hours\": 0.62}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T00:03:46.334Z\"}, \"kl30_s456_global_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:12:57.454Z\", \"updated_at\": \"2026-05-18T23:11:50.581Z\", \"hypothesis\": \"KL 30% predictor (seed 456) global_topk eval on westd-34887 with unified protocol. Resolves MMLU contradiction (27.1% on 41718 vs 43.8% on 34887 in prior runs). Expect PPL ~8.93 consistent with s42 (8.98) and s123.\", \"parent\": \"bench_kl30_global\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl30_s456_global_v3 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation global_topk --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"57573\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_s456_global_v3.log\", \"submitted_at\": \"2026-05-18T22:13:39.098Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 3479.8, \"gpu_hours\": 0.97}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T23:11:38.872Z\", \"metrics\": {\"wikitext2_ppl\": 8.9332, \"arc_challenge_acc_norm\": 0.4633, \"winogrande_acc\": 0.7111, \"mmlu_acc\": 0.4382, \"gsm8k_exact_match\": 0.0758, \"actual_sparsity\": 0.3, \"allocation\": \"global_topk\"}}, \"kl30_s123_global_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:12:55.969Z\", \"updated_at\": \"2026-05-18T23:11:49.677Z\", \"hypothesis\": \"KL 30% predictor (seed 123) global_topk eval on westd-34887 with unified protocol. Resolves cross-server MMLU inconsistency (41718 vs 34887 checkpoint/eval differences). Expect PPL ~8.93 consistent with s42 (8.98) and s456.\", \"parent\": \"bench_kl30_global\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl30_s123_global_v3 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation global_topk --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"57495\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_s123_global_v3.log\", \"submitted_at\": \"2026-05-18T22:13:36.958Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 3480.3, \"gpu_hours\": 0.97}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T23:11:37.295Z\", \"metrics\": {\"wikitext2_ppl\": 8.9748, \"arc_challenge_acc_norm\": 0.4531, \"winogrande_acc\": 0.693, \"mmlu_acc\": 0.3807, \"gsm8k_exact_match\": 0.0758, \"actual_sparsity\": 0.3, \"allocation\": \"global_topk\"}}, \"kl30_s456_uniform_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:53:04.002Z\", \"updated_at\": \"2026-05-18T21:36:19.800Z\", \"hypothesis\": \"KL 30% predictor (seed 456) with uniform allocation produces consistent PPL and downstream metrics with s42 baseline (PPL=8.82), enabling mean±std reporting at the recommended 30% operating point. V3 runs on westd-34887 for server-consistent comparison.\", \"conclusion\": \"success\", \"notes\": \"Resubmitted per Director instruction (v2 had no metrics in registry). Running on westd-34887:1 for server-consistent comparison with bench_kl30_uniform (s42).\", \"parent\": \"bench_kl30_uniform\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl30_s456_uniform_v3 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"52781\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_s456_uniform_v3.log\", \"submitted_at\": \"2026-05-18T20:29:52.286Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 3971.6, \"gpu_hours\": 1.1}, \"completed_at\": \"2026-05-18T21:36:03.852Z\", \"metrics\": {\"wikitext2_ppl\": 8.7947, \"arc_challenge_acc_norm\": 0.4505, \"winogrande_acc\": 0.6875, \"mmlu_acc\": 0.4198, \"gsm8k_exact_match\": 0.0758, \"actual_sparsity\": 0.3, \"allocation\": \"uniform\", \"eval_wall_time_sec\": 2325.3}}, \"kl30_s123_uniform_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:53:02.649Z\", \"updated_at\": \"2026-05-18T21:36:18.318Z\", \"hypothesis\": \"KL 30% predictor (seed 123) with uniform allocation produces consistent PPL and downstream metrics with s42 baseline (PPL=8.82), enabling mean±std reporting at the recommended 30% operating point. V3 runs on westd-34887 for server-consistent comparison.\", \"conclusion\": \"success\", \"notes\": \"Resubmitted per Director instruction (v2 had no metrics in registry). Running on westd-34887:0 for server-consistent comparison with bench_kl30_uniform (s42).\", \"parent\": \"bench_kl30_uniform\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl30_s123_uniform_v3 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"52701\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_s123_uniform_v3.log\", \"submitted_at\": \"2026-05-18T20:29:50.182Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 3972.1, \"gpu_hours\": 1.1}, \"completed_at\": \"2026-05-18T21:36:02.270Z\", \"metrics\": {\"wikitext2_ppl\": 8.8308, \"arc_challenge_acc_norm\": 0.4531, \"winogrande_acc\": 0.6938, \"mmlu_acc\": 0.3944, \"gsm8k_exact_match\": 0.0751, \"actual_sparsity\": 0.3, \"allocation\": \"uniform\", \"eval_wall_time_sec\": 2157.6}}, \"wallclock_speedup_30_50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:28:09.668Z\", \"updated_at\": \"2026-05-18T19:57:43.693Z\", \"hypothesis\": \"Predictor overhead characterization: KL predictor adds minimal inference overhead (target < 5% of total inference time) at 30% and 50% sparsity levels, measured as ms/token and % of dense baseline. No sparse kernel exists (mask-and-multiply only), so no wall-clock speedup expected. Positive if overhead is small enough to be practical when sparse kernels become available.\", \"conclusion\": \"success\", \"metrics\": {\"dense_tok_s_bs1\": 17308.5, \"dense_tok_s_bs8\": 15636.6, \"kl30_tok_s_bs1\": 16089.2, \"kl30_tok_s_bs8\": 14697.4, \"kl50_tok_s_bs1\": 16056.8, \"kl50_tok_s_bs8\": 14756.8, \"overhead_bs1_30pct\": \"7%\", \"overhead_bs1_50pct\": \"7%\", \"overhead_bs8_30pct\": \"6%\", \"overhead_bs8_50pct\": \"6%\", \"predictor_latency_bs1_ms\": 3.2, \"predictor_latency_bs8_ms\": 14.4, \"note\": \"mask-and-multiply only, no sparse kernel. Memory identical across conditions.\"}, \"spec\": {\"command\": \"bash -c \\\"source /root/.bashrc && cd /root/distill_sparse_swiglu && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_latency.py --device cuda:0\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"49534\", \"log_path\": \"~/runs/distill_sparse_swiglu/wallclock_speedup_30_50.log\", \"submitted_at\": \"2026-05-18T19:22:13.822Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (benchmark)\", \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"data_path\": \"wikitext2 (inference benchmark)\", \"data_count\": 100, \"eval_data\": \"N/A (latency benchmark)\", \"wall_clock_seconds\": 2129.9, \"gpu_hours\": 0.59}, \"completed_at\": \"2026-05-18T19:57:43.694Z\"}, \"kl_sparsity35_s42_eval_teal_uniform\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:13:24.518Z\", \"updated_at\": \"2026-05-18T19:57:42.134Z\", \"hypothesis\": \"KL 35% uniform allocation eval completes the dual-column (global + uniform) data for the regime curve.\", \"parent\": \"kl_sparsity35_s42\", \"spec\": {\"command\": \"bash -c \\\"source /root/.bashrc && cd /root/distill_sparse_swiglu && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl_sparsity35_s42_eval_teal_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity35_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.35 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"47628\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity35_s42_eval_teal_uniform.log\", \"submitted_at\": \"2026-05-18T18:49:18.007Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"checkpoints/kl_sparsity35_s42/predictor_kl_normalized.pt\", \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 4104.1, \"gpu_hours\": 1.14}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 9.4416, \"arc_challenge_acc_norm\": 0.3874, \"winogrande_acc\": 0.6654, \"mmlu_acc\": 0.3783, \"gsm8k_exact_match\": 0.0432, \"actual_sparsity\": 0.35, \"allocation\": \"uniform\"}, \"completed_at\": \"2026-05-18T19:57:42.134Z\"}, \"kl_sparsity25_s42_eval_teal_uniform\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:13:23.135Z\", \"updated_at\": \"2026-05-18T19:57:39.981Z\", \"hypothesis\": \"KL 25% uniform allocation eval completes the dual-column (global + uniform) data for the regime curve.\", \"parent\": \"kl_sparsity25_s42\", \"spec\": {\"command\": \"bash -c \\\"source /root/.bashrc && cd /root/distill_sparse_swiglu && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl_sparsity25_s42_eval_teal_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity25_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.25 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"96039\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity25_s42_eval_teal_uniform.log\", \"submitted_at\": \"2026-05-18T19:00:31.451Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"checkpoints/kl_sparsity25_s42/predictor_kl_normalized.pt\", \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 3428.5, \"gpu_hours\": 0.95}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.2344, \"arc_challenge_acc_norm\": 0.465, \"winogrande_acc\": 0.7182, \"mmlu_acc\": 0.4395, \"gsm8k_exact_match\": 0.1099, \"actual_sparsity\": 0.25, \"allocation\": \"uniform\"}, \"completed_at\": \"2026-05-18T19:57:39.981Z\"}, \"kl_sparsity25_s42_eval_teal\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:42:53.858Z\", \"updated_at\": \"2026-05-18T19:57:37.597Z\", \"hypothesis\": \"KL 25% predictor TEAL eval at actual achieved sparsity 0.230, extending regime curve with PPL+downstream at the mildest sparsity level.\", \"spec\": {\"command\": \"bash -c \\\"source /root/.bashrc && cd /root/distill_sparse_swiglu && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl_sparsity25_s42_eval_teal --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity25_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.230 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"95246\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity25_s42_eval_teal.log\", \"submitted_at\": \"2026-05-18T18:54:06.133Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"checkpoints/kl_sparsity25_s42/predictor_kl_normalized.pt\", \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 3811.5, \"gpu_hours\": 1.06}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.169, \"arc_challenge_acc_norm\": 0.4539, \"winogrande_acc\": 0.7056, \"mmlu_acc\": 0.466, \"gsm8k_exact_match\": 0.1145, \"actual_sparsity\": 0.23, \"allocation\": \"global_topk\"}, \"completed_at\": \"2026-05-18T19:57:37.597Z\"}, \"kl_sparsity40_s42_eval_teal_uniform\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:13:21.692Z\", \"updated_at\": \"2026-05-18T19:23:42.618Z\", \"hypothesis\": \"KL predictor at 40% sparsity with TEAL uniform allocation fills the gap in the 6-point regime curve, providing protocol-consistent data alongside existing global_topk eval.\", \"conclusion\": \"killed\", \"notes\": \"Director决定跳过: checkpoint已删, 5/6点足够, global 40%数据已有(PPL=10.12), 重训+eval性价比不高\"}, \"c1_ablation_bce_kl_targets_s123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:05:11.065Z\", \"updated_at\": \"2026-05-18T19:21:37.465Z\", \"spec\": {\"command\": \"python -u src/train_bce_kl_targets.py --kl_checkpoint checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt --output_dir checkpoints/c1_ablation_bce_kl_targets_s123_v2 --gpu 0 --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target 0.50\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"93700\", \"log_path\": \"~/runs/distill_sparse_swiglu/c1_ablation_bce_kl_targets_s123_v2.log\", \"submitted_at\": \"2026-05-18T18:24:05Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/wikitext103/\", \"data_count\": 1000, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"checkpoints/c1_ablation_bce_kl_targets_s123_v2/predictor_bce_kl_targets.pt\", \"wall_clock_seconds\": 2106.7, \"gpu_hours\": 0.59}, \"hypothesis\": \"C1 causal ablation with seed 123 using CORRECT 50% KL oracle (mvp_kl_norm_v2_s123): BCE predictor trained on KL-derived targets should match KL predictor PPL at matched sparsity, confirming target quality as primary driver of KL advantage with multi-seed robustness.\", \"parent\": \"c1_ablation_bce_kl_targets_s42\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.0537, \"ppl\": 9.32, \"sparsity\": 0.615, \"agreement\": 0.979, \"note\": \"Consistent with s42 (PPL=9.29, sparsity=0.609, agreement=0.978). Both seeds converge to ~61% eval sparsity. C1 confirmed multi-seed robust.\"}, \"completed_at\": \"2026-05-18T18:59:11.736Z\"}, \"kl_sparsity45_s42_eval_teal_uniform\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:13:25.328Z\", \"updated_at\": \"2026-05-18T18:59:13.229Z\", \"hypothesis\": \"KL 45% uniform allocation eval completes the dual-column (global + uniform) data for the regime curve.\", \"parent\": \"kl_sparsity45_s42\", \"spec\": {\"command\": \"benchmark_eval.py --checkpoint checkpoints/kl_sparsity45_s42/predictor_kl_normalized.pt --sparsity_target 0.45 --allocation uniform\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"42823\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity45_s42_eval_teal_uniform.log\", \"submitted_at\": \"2026-05-18T18:02:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"checkpoints/kl_sparsity45_s42/predictor_kl_normalized.pt\", \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 3433.2, \"gpu_hours\": 0.95}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 10.9488, \"arc_challenge_acc_norm\": 0.3763, \"winogrande_acc\": 0.6361, \"mmlu_acc\": 0.3063, \"gsm8k_exact_match\": 0.0273, \"actual_sparsity\": 0.45, \"allocation\": \"uniform\"}, \"completed_at\": \"2026-05-18T18:59:13.230Z\"}, \"kl_sparsity45_s42_eval_teal\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:42:56.721Z\", \"updated_at\": \"2026-05-18T18:27:37.704Z\", \"hypothesis\": \"KL predictor at 45% actual sparsity evaluated with TEAL global top-k produces PPL in the 10.5-11.5 range, extending the sparsity-quality curve from 3 to 6 data points for smoother regime characterization.\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id kl_sparsity45_s42_eval_teal --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity45_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.449 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"39543\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity45_s42_eval_teal.log\", \"submitted_at\": \"2026-05-18T17:12:50.194Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/kl_sparsity45_s42/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 2697.4, \"gpu_hours\": 0.75}, \"reproduce\": {\"finished_at\": \"2026-05-18T17:53:16.532Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T17:53:21.006870+00:00\"}]}, \"metrics\": {\"ppl_wikitext2\": 10.803, \"arc_challenge_acc\": 0.3498, \"arc_challenge_acc_norm\": 0.3916, \"winogrande_acc\": 0.6464, \"mmlu_acc\": 0.3037, \"gsm8k_exact_match\": 0.0296, \"actual_sparsity\": 0.449}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/results/benchmark/kl_sparsity45_s42_eval_teal/results.json\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity45_s42_eval_teal.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T17:57:47.584Z\", \"notes\": \"PPL=10.80 符合预期。Downstream 与 bench_kl50_global 对比实际更优（ARC 39.16% vs 32.85%，MMLU 30.37% vs 27.89%）。前次标记 negative 基于错误参考数据。\"}, \"kl_sparsity35_s42_eval_teal\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:42:55.307Z\", \"updated_at\": \"2026-05-18T18:27:35.827Z\", \"hypothesis\": \"KL predictor at 35% actual sparsity evaluated with TEAL global top-k produces PPL in the 9.5-10.5 range, filling a data point between 30% (PPL 8.82) and 50% (PPL 11.79) for the sparsity-quality tradeoff curve.\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id kl_sparsity35_s42_eval_teal --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity35_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.336 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"39463\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity35_s42_eval_teal.log\", \"submitted_at\": \"2026-05-18T17:12:47.611Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/kl_sparsity35_s42/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 2739.8, \"gpu_hours\": 0.76}, \"reproduce\": {\"finished_at\": \"2026-05-18T17:55:53.602Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T17:55:58.536696+00:00\"}]}, \"metrics\": {\"ppl_wikitext2\": 9.3133, \"arc_challenge_acc\": 0.3643, \"arc_challenge_acc_norm\": 0.3891, \"winogrande_acc\": 0.6764, \"mmlu_acc\": 0.4041, \"gsm8k_exact_match\": 0.0773, \"actual_sparsity\": 0.336}, \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity35_s42_eval_teal.log\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/results/benchmark/kl_sparsity35_s42_eval_teal/results.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T17:58:27.455Z\", \"notes\": \"PPL=9.31 符合预期。Downstream 与 bench_kl30_global 对比无异常（前次标记 negative 基于错误参考数据）。MMLU=40.41% 高于 30% global 的 25.27%，待确认是否 allocation 配置差异。\"}, \"bce_30pct_s42_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:22:54.751Z\", \"updated_at\": \"2026-05-18T18:07:17.865Z\", \"hypothesis\": \"BCE predictor trained at 30% target (actual sparsity collapsed to 4.2%) evaluated with forced TEAL top-k at 30%. If downstream metrics approach KL 30% level, BCE's prediction quality is adequate when allocation is externally enforced; if not, KL's mask patterns are genuinely superior even with matched allocation.\", \"spec\": {\"command\": \"bash run_benchmark.sh --exp_id bce_30pct_s42_eval\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"89396\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_30pct_s42_eval.log\", \"submitted_at\": \"2026-05-18T17:12:44.182Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext2+arc_challenge+winogrande+mmlu+gsm8k\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"bce_30pct_s42\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 3269.1, \"gpu_hours\": 0.91}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/bce_30pct_s42/predictor_bce.pt\", \"log_path\": \"/root/runs/distill_sparse_swiglu/bce_30pct_s42_eval.log\", \"parent\": \"bce_30pct_s42\", \"metrics\": {\"wikitext2_ppl\": 11.2445, \"arc_challenge_acc\": 0.3848, \"arc_challenge_acc_norm\": 0.4121, \"winogrande_acc\": 0.6598, \"mmlu_acc\": 0.3633, \"gsm8k_exact_match\": 0.0599, \"gsm8k_exact_match_strict\": 0.0538, \"sparsity_target\": 0.3, \"allocation\": \"global_topk\", \"training_sparsity_native\": 0.042, \"eval_wall_time_sec\": 2275.8}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T18:07:13.327Z\", \"notes\": \"BCE 30% downstream is not catastrophically collapsed (unlike KL 50% GSM8K→1%), but consistently worse than both KL 30% and TEAL 30% baseline. PPL 11.24 vs KL 8.8-9.0 vs TEAL 10.97. Key: BCE predictor's native sparsity was only 4.2% (Lagrangian failed), so TEAL forced 30% externally. The resulting masks are inferior to KL-trained masks at same allocation. Confirms BCE gradient insufficiency extends to downstream quality, not just PPL.\"}, \"c1_ablation_bce_kl_targets_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:05:45.421Z\", \"updated_at\": \"2026-05-18T17:58:52.373Z\", \"hypothesis\": \"C1 causal ablation with seed 123 replicates the s42 finding (BCE+KL-targets PPL = KL PPL at matched sparsity), confirming that target quality is the primary driver of KL advantage with multi-seed robustness.\", \"parent\": \"c1_ablation_bce_kl_targets_s42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/distill_sparse_swiglu && PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True WANDB_MODE=offline python -u src/train_bce_kl_targets.py --kl_checkpoint checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt --seed 123 --num_steps 1000 --sparsity_target 0.50 --output_dir checkpoints/c1_ablation_bce_kl_targets_s123 --gpu 0\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"88845\", \"log_path\": \"~/runs/distill_sparse_swiglu/c1_ablation_bce_kl_targets_s123.log\", \"submitted_at\": \"2026-05-18T17:09:08.310Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 858.3, \"gpu_hours\": 0.24}, \"conclusion\": \"negative\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"completed_at\": \"2026-05-18T17:23:26.601Z\", \"metrics\": {\"ppl\": 11.71, \"sparsity\": 0.5, \"agreement\": 0.834, \"bce_loss\": 0.448, \"note\": \"BCE+KL-targets PPL=11.71 ≈ KL PPL=11.79 at matched 50% sparsity, confirming target quality as primary driver\"}, \"notes\": \"实验使用了错误的 30% KL oracle (kl_sparsity30_s123) 而非 50% oracle (mvp_kl_norm_v2_s123)，与 s42 实验条件不匹配，结果不可用于 multi-seed claim。需用正确 oracle 重跑。agreement=0.834 远低于 s42 的 0.978 即为佐证。\"}, \"kl_sparsity25_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:31:55.829Z\", \"updated_at\": \"2026-05-18T17:22:05.378Z\", \"hypothesis\": \"KL predictor at 25% sparsity seed 123 for multi-seed robustness, expected to match s42 (sparsity 0.230, loss 0.158) confirming consistent convergence at the mild-sparsity regime.\", \"spec\": {\"checkpoint_path\": \"checkpoints/kl_sparsity25_s123/predictor_kl_normalized.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity25_s123.log\", \"command\": \"python -u src/train.py --loss_type kl_normalized --num_steps 1000 --seed 123 --sparsity_target 0.25\", \"server\": \"westd-41718\", \"data_path\": \"wikitext-103\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 123}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.153, \"final_sparsity\": 0.23, \"steps\": 1000}, \"completed_at\": \"2026-05-18T17:22:05.378Z\"}, \"kl_sparsity35_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:54:27.364Z\", \"updated_at\": \"2026-05-18T17:16:46.186Z\", \"hypothesis\": \"KL predictor at 35% sparsity fills the gap between 30% (PPL 8.82) and 50% (PPL 11.79), expected PPL ~9.5-10.5 based on smooth degradation curve, extending regime analysis from 3 to 6 sparsity levels.\", \"spec\": {\"checkpoint_path\": \"checkpoints/kl_sparsity35_s42/predictor_kl_normalized.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity35_s42.log\"}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.203, \"final_sparsity\": 0.336, \"steps\": 1000}, \"completed_at\": \"2026-05-18T17:03:36.871Z\"}, \"kl_sparsity45_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:13:56.643Z\", \"updated_at\": \"2026-05-18T17:03:38.385Z\", \"hypothesis\": \"KL predictor at 45% sparsity fills the gap between 30% (PPL 8.82) and 50% (PPL 11.79), expected PPL ~10.5-11.0, extending regime analysis curve to 6 sparsity levels for smoother quality-efficiency tradeoff characterization.\", \"spec\": {\"checkpoint_path\": \"checkpoints/kl_sparsity45_s42/predictor_kl_normalized.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity45_s42.log\"}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.33, \"final_sparsity\": 0.449, \"steps\": 1000}, \"completed_at\": \"2026-05-18T17:03:38.385Z\"}, \"c1_ablation_eval_uniform\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:54:28.779Z\", \"updated_at\": \"2026-05-18T17:03:13.481Z\", \"hypothesis\": \"Controlled eval of C1 ablation checkpoint at exactly 50% sparsity with uniform allocation using benchmark_eval.py, resolving the sparsity mismatch confound (training eval was 60.9% not 50%). If PPL remains close to or below KL (11.96), target quality conclusion holds under controlled conditions.\", \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"N/A (stdout)\"}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.9638, \"arc_challenge_acc_norm\": 0.3217, \"winogrande_acc\": 0.6314, \"mmlu_acc\": 0.2779, \"gsm8k_exact_match\": 0.0205, \"sparsity_target\": 0.5, \"allocation\": \"uniform\"}, \"completed_at\": \"2026-05-18T17:03:13.481Z\"}, \"c1_ablation_bce_kl_targets_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T14:49:10.286Z\", \"updated_at\": \"2026-05-18T16:36:46.281Z\", \"hypothesis\": \"Causal ablation isolating gradient coupling vs target quality: BCE predictor trained on KL-derived oracle masks achieves PPL 9.29 at 60.9% sparsity, matching KL predictor's 9.21 at 60.6% (delta=0.08). This proves target quality (mask patterns) is the primary driver of KL's advantage, not gradient coupling through the LLM.\", \"spec\": {\"command\": \"python -u src/train_bce_kl_targets.py --kl_checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --output_dir checkpoints/c1_ablation_bce_kl_targets_s42 --gpu 0 --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42\", \"server\": \"westd-41718\", \"data_path\": \"/root/autodl-tmp/data/wikitext103/\", \"data_count\": 1000, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"checkpoint_path\": \"checkpoints/c1_ablation_bce_kl_targets_s42/predictor_bce_kl_targets.pt\", \"log_path\": \"/root/distill_sparse_swiglu/logs/c1_ablation_bce_kl_targets_s42.log\"}, \"metrics\": {\"wt2_ppl\": 9.29, \"eval_sparsity\": 0.609, \"oracle_agreement\": 0.978, \"final_bce_loss\": 0.0545, \"train_steps\": 1000, \"train_time_sec\": 877.1, \"reference_kl_ppl\": 11.79, \"reference_bce_ppl\": 22.51}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T15:51:21.827Z\", \"notes\": \"KL hard mask eval: PPL=9.21 @ 60.6% sparsity. C1 (BCE+KL targets): PPL=9.29 @ 60.9% sparsity. At matched sparsity, BCE+KL targets ≈ KL, confirming target quality is the key factor. The 11.79 PPL comparison was invalid (TEAL forced @50%, not hard mask @natural sparsity). KL-vs-magnitude mask agreement: 53%. C1 benchmark_eval.py (forced TEAL @50%) submitted as c1_ablation_eval_uniform.\"}, \"kl_sparsity25_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:52:52.145Z\", \"updated_at\": \"2026-05-18T16:35:14.718Z\", \"hypothesis\": \"KL predictor at 25% sparsity extends the regime analysis curve, expected to show smaller PPL degradation than 30% (8.82) since less pruning preserves more capacity, establishing the mild-sparsity end of the quality-efficiency tradeoff.\", \"spec\": {\"command\": \"python -u src/train.py --loss_type kl_normalized --num_steps 1000 --sparsity_target 0.25 --seed 42\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"83319\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity25_s42.log\", \"submitted_at\": \"2026-05-18T15:53:07.224Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/kl_sparsity25_s42/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 2282.1, \"gpu_hours\": 0.63}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T16:31:09.309Z\", \"metrics\": {\"train_loss_final\": 0.1582, \"kl_normalized_final\": 0.1582, \"sparsity_actual\": 0.23, \"sparsity_target\": 0.25, \"lambda_final\": 5000, \"tau_final\": 0.1, \"steps\": 1000}}, \"bce_30pct_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T14:49:11.624Z\", \"updated_at\": \"2026-05-18T16:20:28.191Z\", \"hypothesis\": \"BCE predictor at 30% sparsity baseline for Table 2 recommended configuration, establishing BCE quality floor at the mild sparsity regime to quantify KL advantage across sparsity levels.\", \"spec\": {\"command\": \"WANDB_MODE=offline PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True python -u src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.3 --gpu 0 --output_dir checkpoints/bce_30pct_s42 --wandb_run_name bce_30pct_s42 --dataset wikitext-103 --gradient_checkpointing\", \"server\": \"westd-41718\", \"data_path\": \"wikitext-103\", \"data_count\": 1000, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/bce_30pct_s42/predictor_bce.pt\", \"log_path\": \"logs/bce_30pct_s42.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T16:20:28.191Z\"}, \"kl30_s456_uniform_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:56:03.041Z\", \"updated_at\": \"2026-05-18T13:49:03.020Z\", \"spec\": {\"command\": \"benchmark_eval.py --checkpoint checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt --sparsity_target 0.3 --allocation uniform\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"72798\", \"log_path\": \"/root/runs/distill_sparse_swiglu/kl30_s456_uniform_v2.log\", \"submitted_at\": \"2026-05-18T12:56:02.610Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt\", \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 3173.0, \"gpu_hours\": 0.88}, \"conclusion\": \"success\", \"hypothesis\": \"KL-divergence-trained predictor at 30% sparsity with uniform allocation preserves downstream task accuracy comparable to dense model, because uniform budget avoids per-layer optimization variance across seeds.\", \"completed_at\": \"2026-05-18T13:48:55.643Z\", \"metrics\": {\"wikitext2_ppl\": 8.8284, \"arc_challenge_acc_norm\": 0.4505, \"winogrande_acc\": 0.6953, \"mmlu_acc\": 0.3727, \"gsm8k_exact_match\": 0.0705}}, \"kl30_s123_uniform_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:56:00.298Z\", \"updated_at\": \"2026-05-18T13:49:01.613Z\", \"spec\": {\"command\": \"benchmark_eval.py --checkpoint checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt --sparsity_target 0.3 --allocation uniform\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"72660\", \"log_path\": \"/root/runs/distill_sparse_swiglu/kl30_s123_uniform_v2.log\", \"submitted_at\": \"2026-05-18T12:55:59.810Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt\", \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 3174.5, \"gpu_hours\": 0.88}, \"conclusion\": \"success\", \"hypothesis\": \"KL-divergence-trained predictor at 30% sparsity with uniform allocation preserves downstream task accuracy comparable to dense model, because uniform budget avoids per-layer optimization variance across seeds.\", \"completed_at\": \"2026-05-18T13:48:54.263Z\", \"metrics\": {\"wikitext2_ppl\": 8.8186, \"arc_challenge_acc_norm\": 0.471, \"winogrande_acc\": 0.6961, \"mmlu_acc\": 0.3763, \"gsm8k_exact_match\": 0.0705}}, \"kl50_s42_global_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:06:08.725Z\", \"updated_at\": \"2026-05-18T12:56:46.654Z\", \"spec\": {\"command\": \"benchmark_eval.py kl50_s42_global_eval\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"25221\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl50_s42_global_eval.log\", \"submitted_at\": \"2026-05-18T12:06:08.197Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/distill_sparse_swiglu\", \"data_count\": 5, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 3038.5, \"gpu_hours\": 0.84}, \"metrics\": {\"wikitext2_ppl\": 11.8038, \"arc_challenge_acc_norm\": 0.3336, \"winogrande_acc\": 0.6338, \"mmlu_acc\": 0.2819, \"gsm8k_exact_match\": 0.0167}, \"conclusion\": \"success\", \"checkpoint_path\": \"results/benchmark/kl50_s42_global_eval/results.json\", \"hypothesis\": \"KL-trained predictor at 50% sparsity with global_topk allocation preserves downstream task quality better than uniform allocation because it concentrates capacity in high-importance layers identified by learned importance scores.\", \"completed_at\": \"2026-05-18T12:56:46.654Z\"}, \"kl_comp_50pct_s42_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T11:01:53.600Z\", \"updated_at\": \"2026-05-18T11:51:13.313Z\", \"hypothesis\": \"KL+compensation at 50% sparsity (s42) downstream eval shows compensation benefit over KL-only at 50% sparsity level.\", \"parent\": \"kl_comp_50pct_s42\", \"spec\": {\"command\": \"benchmark_eval.py --checkpoint checkpoints/kl_comp_50pct_s42/predictor_with_comp.pt --sparsity_mode teal_global --sparsity_target 0.5\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"67521\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_comp_50pct_s42_eval.log\", \"submitted_at\": \"2026-05-18T11:02:09.751Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext2+lm_eval\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/kl_comp_50pct_s42/predictor_with_comp.pt\", \"eval_data\": \"arc_challenge,winogrande,mmlu,gsm8k,wikitext2\", \"checkpoint_path\": \"checkpoints/kl_comp_50pct_s42/predictor_with_comp.pt\", \"wall_clock_seconds\": 2943.6, \"gpu_hours\": 0.82}, \"metrics\": {\"wikitext2_ppl\": 11.7933, \"arc_challenge_acc_norm\": 0.3285, \"winogrande_acc\": 0.6346, \"mmlu_acc\": 0.2789, \"gsm8k_exact_match\": 0.0129}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T11:51:13.313Z\"}, \"kl_comp_30pct_s456_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T11:01:52.407Z\", \"updated_at\": \"2026-05-18T11:51:11.832Z\", \"hypothesis\": \"KL+compensation at 30% sparsity (s456) downstream eval matches s42/s123 comp eval quality, confirming multi-seed consistency of compensation approach.\", \"parent\": \"kl_comp_30pct_s456\", \"spec\": {\"command\": \"benchmark_eval.py --checkpoint checkpoints/kl_comp_30pct_s456/predictor_with_comp.pt --sparsity_mode teal_global --sparsity_target 0.3\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"67364\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_comp_30pct_s456_eval.log\", \"submitted_at\": \"2026-05-18T11:02:04.387Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext2+lm_eval\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"checkpoint_source\": \"checkpoints/kl_comp_30pct_s456/predictor_with_comp.pt\", \"eval_data\": \"arc_challenge,winogrande,mmlu,gsm8k,wikitext2\", \"checkpoint_path\": \"checkpoints/kl_comp_30pct_s456/predictor_with_comp.pt\", \"wall_clock_seconds\": 2947.4, \"gpu_hours\": 0.82}, \"metrics\": {\"wikitext2_ppl\": 8.9614, \"arc_challenge_acc_norm\": 0.4462, \"winogrande_acc\": 0.7143, \"mmlu_acc\": 0.2714, \"gsm8k_exact_match\": 0.0887}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T11:51:11.832Z\"}, \"kl50_s456_uniform_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:01:36.336Z\", \"updated_at\": \"2026-05-18T11:51:10.391Z\", \"hypothesis\": \"KL 50% uniform allocation (s456) shows downstream degradation vs global_topk, providing third seed for allocation strategy comparison.\", \"parent\": \"kl50_s456_train\", \"spec\": {\"command\": \"bash -c \\\"source /root/.bashrc && cd /root/distill_sparse_swiglu && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl50_s456_uniform_eval --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_50pct_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"21832\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl50_s456_uniform_eval.log\", \"submitted_at\": \"2026-05-18T11:00:47.975Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"checkpoints/kl_50pct_s456/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 3022.4, \"gpu_hours\": 0.84}, \"metrics\": {\"wikitext2_ppl\": 11.9538, \"arc_challenge_acc_norm\": 0.3831, \"winogrande_acc\": 0.6196, \"mmlu_acc\": 0.275, \"gsm8k_exact_match\": 0.0288}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T11:51:10.391Z\"}, \"kl_comp_30pct_s123_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:01:33.560Z\", \"updated_at\": \"2026-05-18T11:51:08.740Z\", \"hypothesis\": \"KL+compensation at 30% sparsity (s123) downstream benchmarks match s42, confirming compensation eval stability across seeds.\", \"parent\": \"kl_comp_30pct_s123\", \"spec\": {\"command\": \"bash -c \\\"source /root/.bashrc && cd /root/distill_sparse_swiglu && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl_comp_30pct_s123_eval --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_comp_30pct_s123/predictor_with_comp.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"21693\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_comp_30pct_s123_eval.log\", \"submitted_at\": \"2026-05-18T11:00:44.711Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"checkpoints/kl_comp_30pct_s123/predictor_with_comp.pt\", \"wall_clock_seconds\": 3024.0, \"gpu_hours\": 0.84}, \"metrics\": {\"wikitext2_ppl\": 8.9788, \"arc_challenge_acc_norm\": 0.3993, \"winogrande_acc\": 0.6898, \"mmlu_acc\": 0.2531, \"gsm8k_exact_match\": 0.0842}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T11:51:08.740Z\"}, \"kl_comp_50pct_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:03:41.768Z\", \"updated_at\": \"2026-05-18T11:01:39.812Z\", \"hypothesis\": \"KL+compensation at 50% sparsity (s42) recovers quality similar to 30% compensation, validating that compensation heads generalize across sparsity levels.\", \"parent\": \"kl_comp_30pct_s42\", \"spec\": {\"command\": \"nohup bash -c 'source /root/.bashrc && cd /root/distill_sparse_swiglu && WANDB_MODE=offline CUDA_VISIBLE_DEVICES=1 python -u src/train_compensation.py --predictor_checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --sparsity_target 0.5 --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-4 --seed 42 --dataset wikitext-103 --log_every 100 --output_dir checkpoints/kl_comp_50pct_s42 --gpu 0' > ~/runs/distill_sparse_swiglu/kl_comp_50pct_s42.log 2>&1 &\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/runs/distill_sparse_swiglu/kl_comp_50pct_s42.log\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"eval_data\": \"N/A\", \"checkpoint_path\": \"checkpoints/kl_comp_50pct_s42/compensation.pt\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T11:01:39.812Z\"}, \"kl_comp_30pct_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:01:38.795Z\", \"updated_at\": \"2026-05-18T11:01:38.495Z\", \"hypothesis\": \"KL+compensation at 30% sparsity (s456) produces similar quality recovery as s42 and s123, providing third seed for multi-seed compensation results.\", \"parent\": \"kl30_8b_s456_train\", \"spec\": {\"command\": \"nohup bash -c 'source /root/.bashrc && cd /root/distill_sparse_swiglu && WANDB_MODE=offline CUDA_VISIBLE_DEVICES=0 python -u src/train_compensation.py --predictor_checkpoint checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt --sparsity_target 0.3 --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-4 --seed 456 --dataset wikitext-103 --log_every 100 --output_dir checkpoints/kl_comp_30pct_s456 --gpu 0' > ~/runs/distill_sparse_swiglu/kl_comp_30pct_s456.log 2>&1 &\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/runs/distill_sparse_swiglu/kl_comp_30pct_s456.log\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"checkpoint_source\": \"checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt\", \"eval_data\": \"N/A\", \"checkpoint_path\": \"checkpoints/kl_comp_30pct_s456/compensation.pt\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T11:01:38.495Z\"}, \"kl50_s42_uniform_eval\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-18T08:10:46.903Z\", \"updated_at\": \"2026-05-18T10:01:31.667Z\", \"hypothesis\": \"KL 50% uniform allocation (s42) shows downstream degradation vs global_topk, consistent with s123 results, providing multi-seed evidence for allocation strategy comparison in Table 3.\", \"parent\": \"bench_kl50_uniform\", \"completed_at\": \"2026-05-18T09:07:05.451Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}, \"spec\": {\"command\": \"nohup bash -c '... CUDA_VISIBLE_DEVICES=1 python -u src/benchmark_eval.py --exp_id kl50_s42_uniform_eval ...' > ~/runs/distill_sparse_swiglu/kl50_s42_uniform_eval.log 2>&1 &\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"15367\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl50_s42_uniform_eval.log\", \"submitted_at\": \"2026-05-18T17:06:00Z\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\"}, \"metrics\": {\"wikitext2_ppl\": 11.9638, \"arc_challenge_acc_norm\": 0.3259, \"winogrande_acc\": 0.6235, \"mmlu_acc\": 0.2792, \"gsm8k_exact_match\": 0.0197}, \"conclusion\": \"success\"}, \"kl_comp_30pct_s42_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T09:00:31.189Z\", \"updated_at\": \"2026-05-18T10:01:30.174Z\", \"hypothesis\": \"KL+compensation at 30% sparsity (s42) improves downstream benchmark quality over KL-only predictor, validating that compensation heads recover quality lost to sparse activation.\", \"parent\": \"kl_comp_30pct_s42\", \"spec\": {\"command\": \"nohup bash -c '... CUDA_VISIBLE_DEVICES=0 python -u src/benchmark_eval.py --exp_id kl_comp_30pct_s42_eval ...' > ~/runs/distill_sparse_swiglu/kl_comp_30pct_s42_eval.log 2>&1 &\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"15055\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_comp_30pct_s42_eval.log\", \"submitted_at\": \"2026-05-18T17:06:00Z\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/kl_comp_30pct_s42/predictor_with_comp.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_comp_30pct_s42/predictor_with_comp.pt\"}, \"metrics\": {\"wikitext2_ppl\": 8.9788, \"arc_challenge_acc_norm\": 0.3993, \"winogrande_acc\": 0.6898, \"mmlu_acc\": 0.2531, \"gsm8k_exact_match\": 0.0842}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T10:01:30.174Z\"}, \"kl_comp_30pct_s123_ppl\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T09:28:39.271Z\", \"updated_at\": \"2026-05-18T09:31:56.282Z\", \"hypothesis\": \"KL+compensation at 30% sparsity (s123) PPL matches s42 results (~8.98 WikiText2, ~16.04 C4), confirming compensation training stability across seeds.\", \"parent\": \"kl_comp_30pct_s123\", \"spec\": {\"checkpoint_path\": \"checkpoints/kl_comp_30pct_s123/predictor_with_comp.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_comp_30pct_s123_ppl.log\"}, \"metrics\": {\"wikitext2_ppl\": 8.9768, \"c4_ppl\": 16.0401, \"sparsity\": 0.3, \"allocation\": \"global_topk\", \"model\": \"llama-3.1-8b\", \"seed\": 123}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T09:31:56.282Z\"}, \"kl_comp_30pct_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T08:38:37.230Z\", \"updated_at\": \"2026-05-18T09:28:16.543Z\", \"hypothesis\": \"KL+compensation at 30% sparsity with seed 123 converges to similar quality as seed 42, confirming compensation training stability across seeds.\", \"parent\": \"kl_comp_30pct_s42\", \"spec\": {\"checkpoint_path\": \"checkpoints/kl_comp_30pct_s123/predictor_with_comp.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_comp_30pct_s123.log\"}, \"metrics\": {\"final_loss\": 0.7617, \"steps\": 1000, \"compensation_params\": 67248128, \"compensation_pct\": 0.837, \"mean_head_norm_final\": 9.2012, \"loss_trajectory\": [2.0469, 1.3828, 1.0703, 0.9609, 0.8711, 0.7305, 0.6875, 0.7773, 0.7969, 0.7617]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T09:28:16.543Z\"}, \"kl_comp_30pct_s42_ppl\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T09:00:32.715Z\", \"updated_at\": \"2026-05-18T09:25:31.004Z\", \"hypothesis\": \"KL+compensation at 30% sparsity (s42) reduces perplexity degradation on WikiText-2 and C4 compared to KL-only predictor, confirming compensation heads improve language modeling quality.\", \"parent\": \"kl_comp_30pct_s42\", \"spec\": {\"command\": \"nohup bash -c 'CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 python -u src/benchmark_eval.py --exp_id kl_comp_30pct_s42_ppl --checkpoint checkpoints/kl_comp_30pct_s42/predictor_with_comp.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks wikitext2,c4 --gpu 0'\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"61490\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_comp_30pct_s42_ppl.log\", \"submitted_at\": \"2026-05-18T09:00:00Z\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"wikitext2,c4\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/kl_comp_30pct_s42/predictor_with_comp.pt\", \"eval_data\": \"wikitext2,c4\", \"checkpoint_path\": \"checkpoints/kl_comp_30pct_s42/predictor_with_comp.pt\", \"wall_clock_seconds\": 1531.0, \"gpu_hours\": 0.43}, \"metrics\": {\"wikitext2_ppl\": 8.9768, \"c4_ppl\": 16.0401, \"sparsity\": 0.3, \"allocation\": \"global_topk\", \"model\": \"llama-3.1-8b\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T09:25:31.004Z\"}, \"kl_comp_30pct_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T08:18:40.552Z\", \"updated_at\": \"2026-05-18T09:00:05.308Z\", \"hypothesis\": \"Per-layer compensation heads (0.837% extra params) trained on KL-distilled 30% sparsity predictor recover quality lost to sparse activation, reducing compensation loss from 2.36 to 0.70 over 1000 steps.\", \"spec\": {\"command\": \"WANDB_MODE=offline python src/train_compensation.py --predictor_checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_target 0.3 --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-4 --seed 42 --dataset wikitext-103 --log_every 100 --output_dir checkpoints/kl_comp_30pct_s42 --gpu 0\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/distill_sparse_swiglu/kl_comp_30pct_s42.log\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 1000, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/kl_comp_30pct_s42/predictor_with_comp.pt\"}, \"metrics\": {\"final_loss\": 0.6992, \"steps\": 1000, \"compensation_params\": 67248128, \"compensation_pct\": 0.837, \"mean_head_norm_final\": 9.2012, \"loss_trajectory\": [2.3594, 1.3516, 1.0859, 0.9219, 0.8789, 0.8281, 0.7461, 0.7344, 0.6953, 0.6992]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T09:00:05.309Z\"}, \"c4_ood_kl50_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T07:51:02.498Z\", \"updated_at\": \"2026-05-18T08:51:08.334Z\", \"hypothesis\": \"KL-distilled predictor at 50% sparsity (seed 456) generalizes to out-of-distribution C4 data with perplexity degradation under 0.5 points vs dense, matching the OOD robustness pattern seen in seed 42/123 checkpoints.\", \"parent\": \"kl50_s456_train\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/bin/activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 python -u src/benchmark_eval.py --exp_id c4_ood_kl50_s456 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_50pct_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks c4 --gpu 1'\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"12424\", \"log_path\": \"~/runs/distill_sparse_swiglu/c4_ood_kl50_s456.log\", \"submitted_at\": \"2026-05-18T16:45:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/c4_val\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"checkpoint_source\": \"checkpoints/kl_50pct_s456/predictor_kl_normalized.pt\", \"eval_data\": \"c4\", \"checkpoint_path\": \"checkpoints/kl_50pct_s456/predictor_kl_normalized.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"c4_ppl\": 23.9867, \"sparsity\": 0.5, \"allocation\": \"global_topk\", \"seed\": 456}, \"completed_at\": \"2026-05-18T08:51:08.334Z\"}, \"c4_ood_kl50_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T08:14:11.123Z\", \"updated_at\": \"2026-05-18T08:51:06.795Z\", \"hypothesis\": \"KL 50% s42 predictor C4 OOD PPL matches s123 result (~23.6), confirming cross-seed OOD consistency at 50% sparsity and completing the 30%/50% sparsity x seed OOD matrix.\", \"parent\": \"c4_ood_kl50_s123\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/bin/activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 python -u src/benchmark_eval.py --exp_id c4_ood_kl50_s42 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks c4 --gpu 0'\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"12354\", \"log_path\": \"~/runs/distill_sparse_swiglu/c4_ood_kl50_s42.log\", \"submitted_at\": \"2026-05-18T16:45:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/c4_val\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"eval_data\": \"c4\", \"checkpoint_path\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\"}, \"metrics\": {\"c4_ppl\": 23.5297, \"sparsity\": 0.5, \"allocation\": \"global_topk\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T08:51:06.795Z\"}, \"kl50_s456_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:49:04.123Z\", \"updated_at\": \"2026-05-18T08:44:45.720Z\", \"hypothesis\": \"KL-trained predictor at 50% sparsity (seed 456) with global_topk allocation preserves benchmark quality comparable to seed 123, confirming multi-seed consistency at 50% sparsity level.\", \"parent\": \"kl50_s456_train\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/autodl-tmp/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 python -u src/benchmark_eval.py --exp_id kl50_s456_eval --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_50pct_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl50_s456_eval.log\", \"submitted_at\": \"2026-05-18T08:10:52.211Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"checkpoint_source\": \"checkpoints/kl_50pct_s456/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"checkpoints/kl_50pct_s456/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 1948.5, \"gpu_hours\": 0.54}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.8614, \"arc_challenge_acc_norm\": 0.3754, \"winogrande_acc\": 0.6417, \"mmlu_acc\": 0.2784, \"gsm8k_exact_match\": 0.0212}, \"completed_at\": \"2026-05-18T08:43:20.688Z\"}, \"c4_ood_kl30_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T08:18:42.154Z\", \"updated_at\": \"2026-05-18T08:20:21.159Z\", \"hypothesis\": \"KL 30% s456 C4 OOD PPL matches s42/s123 results, confirming cross-seed OOD consistency at 30% sparsity.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_c4_predictor.py --ckpt checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt --name kl_30pct_s456 --max_samples 200\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"58551\", \"log_path\": \"~/runs/distill_sparse_swiglu/c4_ood_kl30_s456.log\", \"submitted_at\": \"2026-05-18T08:18:51.218Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"c4_val\", \"data_count\": 132, \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"checkpoint_source\": \"checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt\", \"eval_data\": \"c4_val\", \"checkpoint_path\": \"checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 89.9, \"gpu_hours\": 0.02}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T08:20:21.159Z\"}, \"c4_ood_kl30_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T08:10:45.949Z\", \"updated_at\": \"2026-05-18T08:13:39.395Z\", \"hypothesis\": \"KL 30% s42 predictor C4 OOD PPL matches s123 result (~16.03), confirming cross-seed OOD generalization consistency.\", \"parent\": \"c4_ood_kl30_s123_v2\", \"spec\": {\"command\": \"bash -c \\\"source /root/.bashrc && cd /root/distill_sparse_swiglu && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id c4_ood_kl30_s42_v2 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks c4 --gpu 0\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"57018\", \"log_path\": \"~/runs/distill_sparse_swiglu/c4_ood_kl30_s42_v2.log\", \"submitted_at\": \"2026-05-18T08:11:02.499Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/c4_val\", \"data_count\": 364608, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\", \"eval_data\": \"c4_validation\", \"checkpoint_path\": \"checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 156.9, \"gpu_hours\": 0.04}, \"metrics\": {\"c4_ppl\": 16.0401, \"allocation\": \"global_topk\", \"sparsity\": 0.3, \"model\": \"llama-3.1-8b\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T08:13:39.395Z\"}, \"c4_ood_kl50_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:49:44.632Z\", \"updated_at\": \"2026-05-18T07:10:34.269Z\", \"hypothesis\": \"KL-trained predictor at 50% sparsity shows higher C4 OOD PPL degradation than 30% sparsity, establishing the sparsity-OOD relationship curve. Complements the 30% C4 OOD data from c4_ood_kl30_s42 (PPL=16.05) and pending c4_ood_kl30_s123.\", \"parent\": \"kl50_s123_eval\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 python -u src/benchmark_eval.py --exp_id c4_ood_kl50_s123 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_50pct_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks c4 --gpu 0\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"6082\", \"log_path\": \"~/runs/distill_sparse_swiglu/c4_ood_kl50_s123.log\", \"submitted_at\": \"2026-05-18T06:50:53.125Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/c4_val\", \"data_count\": 364608, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/kl_50pct_s123/predictor_kl_normalized.pt\", \"eval_data\": \"c4_validation\", \"checkpoint_path\": \"checkpoints/kl_50pct_s123/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 1181.1, \"gpu_hours\": 0.33}, \"metrics\": {\"c4_ppl\": 23.6064, \"allocation\": \"global_topk\", \"sparsity\": 0.5, \"model\": \"llama-3.1-8b\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T07:10:34.269Z\"}, \"downstream_ext_kl50_uniform_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:53:37.495Z\", \"updated_at\": \"2026-05-18T07:09:29.677Z\", \"hypothesis\": \"KL 50% uniform predictor preserves extended downstream task quality (HellaSwag, PIQA, BoolQ) comparable to the 30% sparsity condition, verifying graceful degradation at higher sparsity on tasks beyond the core benchmark suite.\", \"parent\": \"bench_kl50_uniform\", \"spec\": {\"command\": \"python src/benchmark_eval.py --exp_id downstream_ext_kl50_uniform_s42 --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --allocation uniform --sparsity_target 0.5 --tasks hellaswag,piqa,boolq --gpu 0\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"53382\", \"log_path\": \"~/runs/distill_sparse_swiglu/downstream_ext_kl50_uniform_s42.log\", \"submitted_at\": \"2026-05-18T06:53:51.338Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"lm-eval cached\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"eval_data\": \"hellaswag,piqa,boolq\", \"wall_clock_seconds\": 938.3, \"gpu_hours\": 0.26}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T07:09:29.677Z\"}, \"downstream_ext_kl30_uniform_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:53:39.069Z\", \"updated_at\": \"2026-05-18T07:09:28.203Z\", \"hypothesis\": \"KL 30% uniform predictor seed 123 matches seed 42 extended downstream results (HellaSwag, PIQA, BoolQ) within expected variance, providing multi-seed confidence for extended task evaluation.\", \"parent\": \"downstream_ext_kl30_s42\", \"spec\": {\"command\": \"python src/benchmark_eval.py --exp_id downstream_ext_kl30_uniform_s123 --checkpoint checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --allocation uniform --sparsity_target 0.3 --tasks hellaswag,piqa,boolq --gpu 0\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"53848\", \"log_path\": \"~/runs/distill_sparse_swiglu/downstream_ext_kl30_uniform_s123.log\", \"submitted_at\": \"2026-05-18T06:54:24.696Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"lm-eval cached\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt\", \"eval_data\": \"hellaswag,piqa,boolq\", \"wall_clock_seconds\": 903.5, \"gpu_hours\": 0.25}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T07:09:28.203Z\"}, \"c4_ood_dense_baseline_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:14:33.520Z\", \"updated_at\": \"2026-05-18T06:48:53.906Z\", \"hypothesis\": \"Dense baseline C4 PPL establishes the upper bound for OOD generalization comparison. This is the reference against which KL predictor sparsity degradation on C4 is measured.\", \"parent\": \"c4_ood_dense_baseline\", \"spec\": {\"command\": \"bash -c \\\"cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id c4_ood_dense_baseline_v2 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --dense --tasks c4 --gpu 0\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"51568\", \"log_path\": \"/root/runs/distill_sparse_swiglu/c4_ood_dense_baseline_v2.log\", \"submitted_at\": \"2026-05-18T06:18:22.513Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/c4_val\", \"data_count\": 364608, \"model_name\": \"llama-3.1-8b\", \"seed\": 0, \"checkpoint_source\": \"none\", \"eval_data\": \"c4_validation\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 1825.0, \"gpu_hours\": 0.51}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T06:48:47.489Z\", \"metrics\": {\"c4_ppl\": 9.2075, \"model\": \"llama-3.1-8b\", \"eval_sequences\": 132, \"seq_len\": 2048}}, \"c4_ood_kl30_s123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:14:31.361Z\", \"updated_at\": \"2026-05-18T06:48:49.465Z\", \"hypothesis\": \"KL-trained predictor (30% sparsity, seed 123) generalizes to out-of-distribution C4 validation data, maintaining low PPL degradation vs dense baseline, because the predictor learns activation importance patterns that transfer across text domains.\", \"parent\": \"c4_ood_kl30_s123\", \"spec\": {\"command\": \"bash -c \\\"cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id c4_ood_kl30_s123_v2 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks c4 --gpu 0\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"51495\", \"log_path\": \"/root/runs/distill_sparse_swiglu/c4_ood_kl30_s123_v2.log\", \"submitted_at\": \"2026-05-18T06:18:20.711Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/c4_val\", \"data_count\": 364608, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt\", \"eval_data\": \"c4_validation\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 1825.4, \"gpu_hours\": 0.51}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T06:48:46.138Z\", \"metrics\": {\"c4_ppl\": 16.0259, \"allocation\": \"global_topk\", \"sparsity\": 0.3, \"model\": \"llama-3.1-8b\", \"eval_sequences\": 132, \"seq_len\": 2048}}, \"kl50_s456_train\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:44:19.280Z\", \"updated_at\": \"2026-05-18T06:48:03.605Z\", \"spec\": {\"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_50pct_s456/predictor_kl_normalized.pt\", \"log_path\": \"/root/runs/distill_sparse_swiglu/kl50_s456_train.log\"}, \"hypothesis\": \"KL-normalized distillation at 50% sparsity with seed 456 converges to similar loss as seed 123, confirming training stability across seeds\", \"metrics\": {\"final_loss\": 0.397, \"final_kl_normalized\": 0.397, \"final_sparsity\": 0.492, \"final_lambda\": 5000, \"final_tau\": 0.1, \"steps_completed\": 1000}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T06:48:03.605Z\"}, \"kl50_s123_uniform_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T05:50:55.894Z\", \"updated_at\": \"2026-05-18T06:48:01.479Z\", \"hypothesis\": \"Uniform per-layer allocation with KL-trained predictor (seed 123, 50% sparsity) will show worse benchmark performance than global_topk allocation, demonstrating the value of learned budget allocation for phase transition analysis in Table 3.\", \"parent\": \"kl50_s123_eval\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id kl50_s123_uniform_eval --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_50pct_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 17800, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/kl_50pct_s123/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"checkpoints/kl_50pct_s123/predictor_kl_normalized.pt\", \"log_path\": \"/root/runs/distill_sparse_swiglu/kl50_s123_uniform_eval.log\"}, \"metrics\": {\"wikitext2_ppl\": 11.89, \"arc_challenge_acc_norm\": 37.88, \"winogrande_acc\": 62.19, \"mmlu_acc\": 27.75, \"gsm8k_exact_match\": 2.35, \"comparison_vs_global_topk\": {\"ppl_delta\": -0.94, \"arc_c_delta\": -5.55, \"wg_delta\": -6.71, \"mmlu_delta\": -8.2, \"gsm8k_delta\": -5}, \"note\": \"Uniform allocation: better PPL but catastrophic downstream degradation vs global_topk. Confirms global_topk allocation is critical for downstream quality.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T06:48:01.479Z\"}, \"c4_ood_kl30_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T05:04:06.474Z\", \"updated_at\": \"2026-05-18T06:12:40.787Z\", \"hypothesis\": \"KL-trained predictor (30% sparsity, seed 123) generalizes to out-of-distribution C4 validation data, maintaining low PPL degradation vs dense baseline, because the predictor learns activation importance patterns that transfer across text domains.\", \"parent\": \"kl_sparsity30_s123\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id c4_ood_kl30_s123 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks c4 --gpu 0\", \"server\": \"westd-41718\", \"data_path\": \"/root/autodl-tmp/.hf_cache/hub/datasets--allenai--c4/\", \"data_count\": 256, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt\", \"eval_data\": \"c4_validation\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T06:12:40.787Z\"}, \"c4_ood_dense_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T05:04:08.095Z\", \"updated_at\": \"2026-05-18T06:12:39.491Z\", \"hypothesis\": \"Dense baseline C4 PPL establishes the upper bound for OOD generalization comparison. This is the reference against which KL predictor sparsity degradation on C4 is measured.\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id c4_ood_dense_baseline --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --dense --tasks c4 --gpu 1\", \"server\": \"westd-41718\", \"data_path\": \"/root/autodl-tmp/.hf_cache/hub/datasets--allenai--c4/\", \"data_count\": 256, \"model_name\": \"llama-3.1-8b\", \"seed\": 0, \"checkpoint_source\": \"none\", \"eval_data\": \"c4_validation\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T06:12:39.491Z\"}, \"kl50_s123_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:02:35.894Z\", \"updated_at\": \"2026-05-18T05:51:23.448Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id kl50_s123_eval --checkpoint checkpoints/kl_50pct_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"99952\", \"log_path\": \"/root/runs/distill_sparse_swiglu/kl50_s123_eval.log\", \"submitted_at\": \"2026-05-17T11:02:35.356Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"checkpoints/kl_50pct_s123/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"data_path\": \"N/A\", \"data_count\": 0, \"checkpoint_path\": \"checkpoints/kl_50pct_s123/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 67728.1, \"gpu_hours\": 18.81}, \"hypothesis\": \"KL-trained predictor at 50% sparsity (seed 123) with global_topk allocation preserves benchmark quality on wikitext2, arc_challenge, winogrande, mmlu, gsm8k tasks.\", \"parent\": \"kl_50pct_s123\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.745, \"arc_challenge\": 0.3814, \"winogrande\": 0.6125, \"mmlu\": 0.2752, \"gsm8k\": 0.0281}, \"completed_at\": \"2026-05-18T05:51:23.448Z\"}, \"snr_extended_r6w3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T01:55:41.436Z\", \"updated_at\": \"2026-05-18T03:42:12.200Z\", \"hypothesis\": \"Extended SNR analysis (steps 0-300, 7 checkpoints) with 95% CI shows KL gradient signal-to-noise ratio consistently exceeds BCE across training, explaining why KL converges to better sparsity patterns. Addresses reviewer R6-W3.\", \"conclusion\": \"success\", \"metrics\": {\"kl_snr_step300\": 0.0058773, \"bce_snr_step300\": 0.00114449, \"snr_ratio_step300\": 5.14, \"kl_train_time_s\": 641, \"bce_train_time_s\": 320, \"num_checkpoints\": 7, \"steps_range\": \"0-300\"}, \"spec\": {\"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"westd-34887:/root/distill_sparse_swiglu/artifacts/snr_extended/\"}, \"completed_at\": \"2026-05-18T03:42:12.200Z\"}, \"kl30_8b_s456_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T01:54:50.231Z\", \"updated_at\": \"2026-05-18T03:42:10.843Z\", \"hypothesis\": \"KL 30% s456 downstream eval (PPL+ARC+WG+MMLU+GSM8K) validates cross-seed consistency of KL advantage for Table 2 multi-seed reporting.\", \"parent\": \"kl30_8b_s456_train\", \"spec\": {\"command\": \"benchmark_eval.py 5-task on kl_sparsity30_s456 checkpoint\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"37480\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"checkpoint_source\": \"kl30_8b_s456_train\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"westd-41718:/root/distill_sparse_swiglu/artifacts/kl30_8b_s456_eval/\"}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.9614, \"arc_challenge_acc\": 0.436, \"arc_challenge_acc_norm\": 0.4462, \"winogrande_acc\": 0.7143, \"mmlu_acc\": 0.2714, \"gsm8k_exact_match\": 0.0887}, \"completed_at\": \"2026-05-18T03:42:10.843Z\"}, \"kl30_8b_s123_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T01:54:48.304Z\", \"updated_at\": \"2026-05-18T03:42:09.516Z\", \"hypothesis\": \"KL 30% s123 downstream eval (PPL+ARC+WG+MMLU+GSM8K) validates cross-seed consistency of KL advantage for Table 2 multi-seed reporting.\", \"parent\": \"kl30_8b_s123_train\", \"spec\": {\"command\": \"benchmark_eval.py 5-task on kl_sparsity30_s123 checkpoint\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"37184\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"checkpoint_source\": \"kl30_8b_s123_train\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"westd-41718:/root/distill_sparse_swiglu/artifacts/kl30_8b_s123_eval/\"}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.9267, \"arc_challenge_acc\": 0.4462, \"arc_challenge_acc_norm\": 0.4744, \"winogrande_acc\": 0.7024, \"mmlu_acc\": 0.3836, \"gsm8k_exact_match\": 0.0917}, \"completed_at\": \"2026-05-18T03:42:09.516Z\"}, \"bce_isocompute_v3_s42_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T01:03:16.947Z\", \"updated_at\": \"2026-05-18T03:42:08.122Z\", \"hypothesis\": \"BCE iso-compute v3 s42 checkpoint downstream eval (PPL, ARC, WG, MMLU, GSM8K) completes 3-seed mean±std for Table 2 BCE row. Expected PPL ~28 consistent with s456 (28.35) and s123 (28.06).\", \"parent\": \"bce_isocompute_v3_s42\", \"spec\": {\"command\": \"bash -c \\\"cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/benchmark_eval.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b/ --checkpoint checkpoints/bce_isocompute_v3_s42/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --exp_id bce_isocompute_v3_s42_eval --gpu 0\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"91355\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"bce_isocompute_v3_s42\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"westd-34887:/root/distill_sparse_swiglu/artifacts/bce_isocompute_v3_s42_eval/\"}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 27.9696, \"arc_challenge_acc\": 0.2346, \"arc_challenge_acc_norm\": 0.2765, \"winogrande_acc\": 0.5162, \"mmlu_acc\": 0.2614, \"gsm8k_exact_match\": 0.019}, \"completed_at\": \"2026-05-18T03:42:08.122Z\"}, \"qwen14b_kl30_uniform_eval_4task\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T00:31:52.875Z\", \"updated_at\": \"2026-05-18T02:11:50.367Z\", \"hypothesis\": \"KL predictor 14B uniform allocation 4-task eval (no GSM8K). Tests if uniform allocation recovers KL's MMLU from 63.72 (global_topk) to >70% (matching TEAL 71.83).\", \"spec\": {\"command\": \"bash -c \\\"cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache /root/miniconda3/bin/python -u src/benchmark_eval.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --allocation uniform --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu --exp_id qwen14b_kl30_uniform_4task --gpu 0\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"87144\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_uniform_eval_4task.log\", \"submitted_at\": \"2026-05-18T00:52:59.360Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"qwen2.5-14b\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu\", \"data_count\": 0, \"seed\": 42, \"checkpoint_source\": \"qwen14b_kl30_s42\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu\", \"wall_clock_seconds\": 3914.6, \"gpu_hours\": 1.09}, \"reproduce\": {\"finished_at\": \"2026-05-18T01:21:39.937Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T01:21:44.831285+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 7.63, \"mmlu_acc\": 0.6449, \"arc_challenge_acc_norm\": 0.5444, \"winogrande_acc\": 0.7245}, \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A (eval-only experiment)\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_uniform_eval_4task.log\", \"completed_at\": \"2026-05-18T01:58:13.990Z\"}, \"qwen14b_teal30_uniform_eval_4task\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T00:31:54.286Z\", \"updated_at\": \"2026-05-18T02:11:41.846Z\", \"hypothesis\": \"TEAL vanilla 14B uniform allocation 4-task control. Baseline for comparing allocation effect on TEAL vs KL downstream metrics.\", \"spec\": {\"command\": \"bash -c \\\"cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache /root/miniconda3/bin/python -u src/benchmark_eval.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --baseline_mode teal_vanilla --allocation uniform --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu --exp_id qwen14b_teal30_uniform_4task --gpu 0\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"87283\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_teal30_uniform_eval_4task.log\", \"submitted_at\": \"2026-05-18T00:53:02.718Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"qwen2.5-14b\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu\", \"data_count\": 0, \"seed\": 42, \"checkpoint_source\": \"N/A (TEAL vanilla)\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu\", \"wall_clock_seconds\": 3912.8, \"gpu_hours\": 1.09}, \"reproduce\": {\"finished_at\": \"2026-05-18T01:21:48.903Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T01:21:54.917321+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 8.01, \"mmlu_acc\": 0.6634, \"arc_challenge_acc_norm\": 0.5529, \"winogrande_acc\": 0.6985}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only experiment)\", \"completed_at\": \"2026-05-18T01:58:15.536Z\"}, \"kl30_8b_s456_train\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T00:21:15.119Z\", \"updated_at\": \"2026-05-18T01:54:21.784Z\", \"hypothesis\": \"KL 30% predictor multi-seed replication (seed=456) for Table 2 statistical robustness. Third seed for mean±std reporting. Expect consistent convergence to ~0.285 sparsity and comparable downstream metrics.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/distill_sparse_swiglu && python -u src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 456 --sparsity_target 0.3 --gpu 0 --output_dir checkpoints/kl_sparsity30_s456 --dataset wikitext-103 --gradient_checkpointing --lambda_max 5000\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"35045\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_8b_s456_train.log\", \"submitted_at\": \"2026-05-18T00:21:33.744Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 1000, \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"wall_clock_seconds\": 2825.2, \"gpu_hours\": 0.78}, \"reproduce\": {\"finished_at\": \"2026-05-18T01:08:35.312Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T01:08:38.931Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T01:08:45.544169+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 8.9614, \"sparsity\": 0.3, \"training_loss\": 0.148}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt\"}, \"kl30_8b_s123_train\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T00:21:13.138Z\", \"updated_at\": \"2026-05-18T01:54:20.897Z\", \"hypothesis\": \"KL 30% predictor multi-seed replication (seed=123) for Table 2 statistical robustness. Training should converge to similar sparsity (~0.285) and loss as s42 (loss=0.165). Full downstream eval validates cross-seed consistency of KL advantage over BCE/TEAL.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/distill_sparse_swiglu && python -u src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target 0.3 --gpu 0 --output_dir checkpoints/kl_sparsity30_s123 --dataset wikitext-103 --gradient_checkpointing --lambda_max 5000\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"34700\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_8b_s123_train.log\", \"submitted_at\": \"2026-05-18T00:21:30.726Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 1000, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"wall_clock_seconds\": 2785.8, \"gpu_hours\": 0.77}, \"reproduce\": {\"finished_at\": \"2026-05-18T01:07:53.757Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T01:07:56.530Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T01:08:01.178437+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 8.9267, \"sparsity\": 0.3, \"training_loss\": 0.147}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt\"}, \"qwen14b_teal30_uniform_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T22:49:43.286Z\", \"updated_at\": \"2026-05-18T00:33:40.746Z\", \"hypothesis\": \"TEAL vanilla with uniform allocation (control) establishes the allocation effect on downstream tasks independent of predictor quality; comparing global_topk vs uniform for TEAL isolates allocation from prediction\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_teal30_uniform --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --baseline_mode teal_vanilla --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"81296\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_teal30_uniform_eval.log\", \"submitted_at\": \"2026-05-17T23:10:16.678Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/models/qwen2.5-14b/\", \"data_count\": 0, \"model_name\": \"qwen2.5-14b\", \"seed\": 42, \"checkpoint_source\": \"N/A (TEAL vanilla)\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 5001.2, \"gpu_hours\": 1.39}, \"reproduce\": {\"finished_at\": \"2026-05-18T00:33:32.754Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T00:33:37.886Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T00:33:44.824305+00:00\"}]}}, \"qwen14b_kl30_uniform_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T22:49:41.807Z\", \"updated_at\": \"2026-05-18T00:33:19.659Z\", \"hypothesis\": \"KL predictor's poor 14B MMLU (63.72 vs TEAL 71.83) is caused by global_topk allocation starving knowledge-critical middle layers; switching to uniform per-layer allocation will recover MMLU while trading some PPL\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_kl30_uniform --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"81217\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_uniform_eval.log\", \"submitted_at\": \"2026-05-17T23:10:14.740Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/models/qwen2.5-14b/\", \"data_count\": 0, \"model_name\": \"qwen2.5-14b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 4984.9, \"gpu_hours\": 1.38}, \"reproduce\": {\"finished_at\": \"2026-05-18T00:33:17.060Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T00:33:19.659Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T00:33:23.548544+00:00\"}]}}, \"c4_ood_kl30_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:35:10.382Z\", \"updated_at\": \"2026-05-17T23:50:12.416Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/distill_sparse_swiglu && python -u src/benchmark_eval.py --exp_id c4_ood_kl30_s42 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b/ --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks c4 --gpu 0\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"78732\", \"log_path\": \"~/runs/distill_sparse_swiglu/c4_ood_kl30_s42.log\", \"submitted_at\": \"2026-05-17T22:38:54.320Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/c4_val/\", \"data_count\": 132, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"kl_sparsity30_s42_v3\", \"eval_data\": \"c4_val\", \"wall_clock_seconds\": 3088.6, \"gpu_hours\": 0.86}, \"hypothesis\": \"KL predictor trained on WikiText-2 generalizes to out-of-distribution C4 data; C4 PPL degradation ratio should be comparable to WikiText-2 ratio vs dense\", \"conclusion\": \"success\", \"metrics\": {\"c4_ppl\": 16.0458, \"allocation\": \"global_topk\", \"sparsity\": 0.3, \"model\": \"llama-3.1-8b\", \"eval_sequences\": 132, \"seq_len\": 2048}, \"checkpoint_path\": \"N/A (eval-only experiment)\", \"log_path\": \"~/runs/distill_sparse_swiglu/c4_ood_kl30_s42.log\", \"completed_at\": \"2026-05-17T23:30:22.886Z\"}, \"qwen14b_teal30_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:44:02.456Z\", \"updated_at\": \"2026-05-17T22:50:42.054Z\", \"hypothesis\": \"TEAL magnitude pruning at 30% sparsity on Qwen-2.5-14B produces higher PPL than KL-distilled predictor (7.62 TEAL global), establishing the improvement of learned prediction over static magnitude thresholding at 14B scale\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_teal30 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --baseline_mode teal_vanilla --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"model_name\": \"qwen2.5-14b\", \"data_path\": \"lm-eval-harness datasets\", \"data_count\": 0, \"seed\": 42, \"pid\": \"6896\"}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.7332, \"arc_challenge_acc_norm\": 0.5683, \"winogrande_acc\": 0.7269, \"mmlu_acc\": 0.7183, \"gsm8k_exact_match\": 0.4951}, \"checkpoint_path\": \"N/A (TEAL vanilla)\", \"log_path\": \"logs/qwen14b_teal30_eval.log\", \"completed_at\": \"2026-05-17T22:50:42.054Z\"}, \"qwen14b_bce30_s42_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T16:47:04.947Z\", \"updated_at\": \"2026-05-17T22:50:22.578Z\", \"hypothesis\": \"Qwen-14B BCE predictor at 30% sparsity shows worse downstream performance (MMLU, ARC, WinoGrande, GSM8K) than KL predictor, confirming objective mismatch penalty persists in downstream tasks beyond PPL (KL TEAL PPL=7.62 vs BCE TEAL PPL=8.76)\", \"parent\": \"qwen14b_bce30_s42\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_bce30_s42_eval --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_bce30_s42/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"59122\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_bce30_s42_eval.log\", \"submitted_at\": \"2026-05-17T16:47:51.067Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 21751.5, \"gpu_hours\": 6.04}, \"pid\": \"59122\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_bce30_s42_eval.log\", \"reproduce\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_bce30_s42_eval --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_bce30_s42/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"finished_at\": \"2026-05-17T22:40:16.602Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T22:40:24.251568+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 8.7634, \"arc_challenge_acc_norm\": 0.5759, \"winogrande_acc\": 0.7261, \"mmlu_acc\": 0.7167, \"gsm8k_exact_match\": 0.5307}, \"checkpoint_path\": \"checkpoints/qwen14b_bce30_s42/predictor_bce.pt\", \"completed_at\": \"2026-05-17T22:40:16Z\", \"conclusion\": \"negative\"}, \"qwen14b_dense_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:47:04.949Z\", \"updated_at\": \"2026-05-17T22:26:12.490Z\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_dense_baseline --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"18845\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_dense_baseline.log\", \"submitted_at\": \"2026-05-17T18:47:34.739Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"qwen2.5-14b\", \"data_path\": \"lm-eval-harness datasets\", \"data_count\": 0, \"seed\": 42, \"wall_clock_seconds\": 13034.6, \"gpu_hours\": 3.62}, \"hypothesis\": \"Qwen-2.5-14B dense baseline downstream metrics (PPL, ARC-c, WinoGrande, MMLU, GSM8K) provide reference for computing degradation ratio of KL/BCE/TEAL sparse predictors at 14B scale, enabling cross-scale comparison with LLaMA-8B results\", \"reproduce\": {\"finished_at\": \"2026-05-17T22:24:15.654Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T22:24:20.978994+00:00\"}]}, \"log_path\": \"logs/downstream_dense_baseline.log\", \"checkpoint_path\": \"N/A (dense baseline)\", \"conclusion\": \"success\", \"metrics\": {\"ppl\": 5.1854, \"arc_challenge\": 0.6758, \"winogrande\": 0.8106, \"mmlu\": 0.7977, \"gsm8k\": 0.8757}, \"completed_at\": \"2026-05-17T22:24:49.323Z\"}, \"bce_isocompute_v3_s123_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T21:38:39.052Z\", \"updated_at\": \"2026-05-17T22:21:34.177Z\", \"hypothesis\": \"BCE predictor seed 123 at 50% sparsity eval metrics (PPL, MMLU, ARC, WG, GSM8K) align with seeds 42/456, completing 3-seed mean±std for Table 2 BCE row\", \"parent\": \"bce_isocompute_v3_s123\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id bce_isocompute_v3_s123 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/bce_isocompute_v3_s123/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"checkpoint_source\": \"bce_isocompute_v3_s123\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"checkpoints/bce_isocompute_v3_s123/predictor_bce.pt\", \"log_path\": \"logs/bce_isocompute_v3_s123_eval.log\", \"completed_at\": \"2026-05-17T22:21:28.081Z\", \"metrics\": {\"wikitext2_ppl\": 28.0627, \"arc_challenge_acc_norm\": 0.2696, \"winogrande_acc\": 0.513, \"mmlu_acc\": 0.2655, \"gsm8k_exact_match\": 0.022}}, \"bce_isocompute_v3_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T17:41:58.488Z\", \"updated_at\": \"2026-05-17T21:36:11.832Z\", \"hypothesis\": \"BCE predictor with seed 123 at 50% sparsity produces similar training loss and downstream metrics as seeds 42/456, completing the 3-seed validation for Table 2 BCE row stability\", \"parent\": \"bce_isocompute_v3_s42\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 2700 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target 0.5 --gpu 0 --output_dir checkpoints/bce_isocompute_v3_s123 --wandb_run_name bce_isocompute_v3_s123 --dataset wikitext-103 --gradient_checkpointing --log_every 100\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"72392\", \"log_path\": \"/root/runs/distill_sparse_swiglu/bce_isocompute_v3_s123.log\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"wikitext-103\", \"data_count\": 0, \"seed\": 123, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"checkpoints/bce_isocompute_v3_s123/predictor_bce.pt\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T21:36:11.832Z\"}, \"bce_isocompute_v3_s456_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T20:02:53.092Z\", \"updated_at\": \"2026-05-17T20:48:24.378Z\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id bce_isocompute_v3_s456 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/bce_isocompute_v3_s456/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"69504\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_isocompute_v3_s456_eval.log\", \"submitted_at\": \"2026-05-17T20:02:52.758Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b + bce_isocompute_v3 predictor\", \"data_path\": \"wikitext2 + arc_challenge + winogrande + mmlu + gsm8k\", \"data_count\": 200, \"seed\": 456, \"checkpoint_source\": \"bce_isocompute_v3_s456\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"checkpoints/bce_isocompute_v3_s456/predictor_bce.pt\", \"wall_clock_seconds\": 2729.1, \"gpu_hours\": 0.76}, \"hypothesis\": \"BCE iso-compute v3 s456 checkpoint 在 PPL 和 downstream (MMLU/ARC/WinoGrande/GSM8K) 上与 s42 结果一致，为 Table 2 BCE 行提供 3-seed mean±std\", \"parent\": \"bce_isocompute_v3_s456\", \"reproduce\": {\"finished_at\": \"2026-05-17T20:45:48.427Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T20:45:52.286106+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"teal_sparse_ppl\": 28.3503, \"model_level_sparsity\": 0.5, \"arc_challenge_acc\": 0.2312, \"arc_challenge_acc_stderr\": 0.01232, \"arc_challenge_acc_norm\": 0.2807, \"arc_challenge_acc_norm_stderr\": 0.01313, \"winogrande_acc\": 0.5241, \"winogrande_acc_stderr\": 0.01404, \"mmlu_acc\": 0.2567, \"mmlu_acc_stderr\": 0.00367, \"gsm8k_exact_match\": 0.022, \"gsm8k_exact_match_stderr\": 0.00404, \"gsm8k_exact_match_strict\": 0.00834, \"gsm8k_exact_match_strict_stderr\": 0.0025}, \"completed_at\": \"2026-05-17T20:48:21.901Z\"}, \"bce_isocompute_v3_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T17:41:59.821Z\", \"updated_at\": \"2026-05-17T20:03:51.348Z\", \"hypothesis\": \"BCE iso-compute 2700 steps with seed 456 at 50% sparsity produces comparable results to s42 (PPL and downstream), providing multi-seed validation for Table 2 BCE row\", \"parent\": \"bce_isocompute_v3_s42\", \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 2700 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 456 --sparsity_target 0.5 --gpu 0 --output_dir checkpoints/bce_isocompute_v3_s456 --wandb_run_name bce_isocompute_v3_s456 --dataset wikitext-103 --gradient_checkpointing --log_every 100\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"67029\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_isocompute_v3_s456.log\", \"submitted_at\": \"2026-05-17T19:13:30.954Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"wikitext-103\", \"data_count\": 0, \"seed\": 456, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"wikitext-103 (training data)\", \"checkpoint_path\": \"checkpoints/bce_isocompute_v3_s456/predictor_bce.pt\", \"wall_clock_seconds\": 2957.0, \"gpu_hours\": 0.82}, \"reproduce\": {\"finished_at\": \"2026-05-17T20:01:09.845Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T20:01:13.768692+00:00\"}]}, \"metrics\": {\"final_loss\": 0.6368, \"final_sparsity\": 0.51, \"training_steps\": 2700}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T20:02:47.951Z\", \"checkpoint_path\": \"checkpoints/bce_isocompute_v3_s456/predictor_bce.pt\"}, \"qwen14b_kl30_s42_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:50:41.706Z\", \"updated_at\": \"2026-05-17T19:14:25.031Z\", \"hypothesis\": \"Qwen-2.5-14B with distilled 30% sparsity predictor maintains strong downstream performance (MMLU, ARC, WinoGrande) at 30% activation sparsity, with PPL degradation ratio consistent with training-time measurement (1.47x TEAL global)\", \"parent\": \"qwen14b_kl30_s42\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s42 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"52224\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_eval.log\", \"submitted_at\": \"2026-05-17T14:52:07.328Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 15737.7, \"gpu_hours\": 4.37}, \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"52224\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_eval.log\", \"reproduce\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s42 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"finished_at\": \"2026-05-17T18:51:45.662Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T18:51:50.659306+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 7.6232, \"arc_challenge_acc_norm\": 0.5717, \"winogrande_acc\": 0.7206, \"mmlu_acc\": 0.6372, \"gsm8k_exact_match\": 0.4882}, \"conclusion\": \"success\", \"checkpoint_path\": \"checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt\", \"completed_at\": \"2026-05-17T19:14:25.031Z\"}, \"c4_download\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:44:27.112Z\", \"updated_at\": \"2026-05-17T18:45:37.399Z\", \"spec\": {\"command\": \"bash -c \\\"export HF_ENDPOINT=https://hf-mirror.com && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u /tmp/download_c4.py\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"18522\", \"log_path\": \"~/runs/distill_sparse_swiglu/c4_download.log\", \"submitted_at\": \"2026-05-17T18:45:36.676Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"kl50_global_s123_reeval\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T17:41:56.673Z\", \"updated_at\": \"2026-05-17T18:34:20.571Z\", \"hypothesis\": \"Re-eval 50% KL global s123 with correct checkpoint (mvp_kl_norm_v2_s123) to fix data consistency issue in Table 2 Row 6, where previous eval used kl_50pct_s123 checkpoint instead\", \"parent\": \"kl_50pct_s123_global\", \"server\": \"westd-41718\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl50_global_s123_reeval --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"finished_at\": \"2026-05-17T18:28:54.207Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-17T17:48:21.031Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T17:48:24.990388+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T18:28:59.489303+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"pid\": \"14578\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"account\": \"root\", \"log_path\": \"logs/kl50_global_s123_reeval.log\", \"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl50_global_s123 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b/ --predictor_path checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt --sparsity_target 0.5 --allocation global --tasks wikitext2,arc_challenge,winogrande,mmlu --gpu 0\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"N/A\", \"data_count\": 0, \"seed\": 123, \"checkpoint_source\": \"checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu\"}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.7184, \"arc_challenge_acc_norm\": 0.3635, \"winogrande_acc\": 0.6109, \"mmlu_acc\": 0.2834, \"gsm8k_exact_match\": 0.0258}, \"checkpoint_path\": \"checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt\"}, \"downstream_teal30_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T17:08:25.083Z\", \"updated_at\": \"2026-05-17T17:45:46.103Z\", \"hypothesis\": \"TEAL magnitude pruning at 30% sparsity on LLaMA-8B produces worse downstream performance (HellaSwag/PIQA/BoolQ) than KL-distilled predictor (KL: 0.727/0.760/0.769), establishing KL advantage extends beyond PPL to diverse downstream tasks\", \"server\": \"westd-41718\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id downstream_teal30_baseline --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --baseline_mode teal_vanilla --sparsity_target 0.3 --tasks hellaswag,piqa,boolq --gpu 0\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"12150\", \"log_path\": \"~/runs/distill_sparse_swiglu/downstream_teal30_baseline.log\", \"submitted_at\": \"2026-05-17T17:09:09.433Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2196.7, \"gpu_hours\": 0.61}, \"pid\": \"12150\", \"log_path\": \"~/runs/distill_sparse_swiglu/downstream_teal30_baseline.log\", \"reproduce\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id downstream_teal30_baseline --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --baseline_mode teal_vanilla --sparsity_target 0.3 --tasks hellaswag,piqa,boolq --gpu 0\", \"finished_at\": \"2026-05-17T17:44:05.384Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T17:44:09.138919+00:00\"}]}, \"metrics\": {\"hellaswag_acc\": 0.4878, \"hellaswag_acc_norm\": 0.667, \"piqa_acc\": 0.7258, \"piqa_acc_norm\": 0.7361, \"boolq_acc\": 0.685}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only)\", \"completed_at\": \"2026-05-17T17:45:46.103Z\"}, \"kl30_s456_uniform_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:56:50.797Z\", \"updated_at\": \"2026-05-17T17:39:20.918Z\", \"hypothesis\": \"30% sparsity with uniform allocation on seed 456 will show MMLU comparable to s42/s123 uniform results (~0.39-0.41), confirming uniform allocation provides more consistent cross-seed MMLU than global allocation which showed high variance (0.25-0.44)\", \"parent\": \"kl30_s456_train\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl30_s456_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_30pct_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"49864\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_s456_uniform_eval.log\", \"submitted_at\": \"2026-05-17T14:24:33.044Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 7397.6, \"gpu_hours\": 2.05}, \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"49864\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_s456_uniform_eval.log\", \"reproduce\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl30_s456_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_30pct_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"finished_at\": \"2026-05-17T15:03:53.827Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T15:03:57.023840+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.4198, \"ppl_uniform\": 8.7947, \"arc_challenge\": 0.4505, \"winogrande\": 0.6875, \"gsm8k\": 0.0758}, \"checkpoint_path\": \"checkpoints/kl_30pct_s456/predictor_kl_normalized.pt\", \"completed_at\": \"2026-05-17T16:27:50.690Z\"}, \"downstream_dense_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T16:29:57.759Z\", \"updated_at\": \"2026-05-17T17:05:51.063Z\", \"hypothesis\": \"Dense LLaMA-3.1-8B baseline on HellaSwag/PIQA/BoolQ provides reference scores for computing KL-30% sparsity degradation on extended downstream tasks, expected to show minimal degradation (less than 5pp drop from dense)\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id downstream_dense_baseline --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --tasks hellaswag,piqa,boolq --gpu 0\", \"server\": \"westd-41718\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"data_path\": \"hellaswag,piqa,boolq\", \"data_count\": 0}, \"metrics\": {\"hellaswag_acc_norm\": 0.8233, \"hellaswag_acc_norm_stderr\": 0.0038, \"piqa_acc_norm\": 0.8074, \"piqa_acc_norm_stderr\": 0.0092, \"boolq_acc\": 0.8294, \"boolq_acc_stderr\": 0.0066}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (dense baseline)\", \"log_path\": \"/root/distill_sparse_swiglu/logs/downstream_dense_baseline.log\", \"completed_at\": \"2026-05-17T17:05:51.063Z\"}, \"qwen14b_bce30_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T16:03:24.580Z\", \"updated_at\": \"2026-05-17T16:51:07.306Z\", \"hypothesis\": \"BCE with 10x stronger Lagrangian (lambda_max=50000) on Qwen-14B achieves target 30% sparsity. If still fails (sparsity <25%), this confirms BCE gradient signal is fundamentally insufficient at 14B scale to drive sparsity through Lagrangian constraint, which is itself a publishable finding about objective mismatch scaling.\", \"parent\": \"qwen14b_bce30_s42\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type bce --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.3 --lambda_max 50000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_bce30_s42_v2 --wandb_run_name qwen14b_bce30_s42_v2 --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"57864\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_bce30_s42_v2.log\", \"submitted_at\": \"2026-05-17T16:26:53.579Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1453.7, \"gpu_hours\": 0.4}, \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-17T16:04:35.846Z\", \"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type bce --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.3 --lambda_max 50000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_bce30_s42_v2 --wandb_run_name qwen14b_bce30_s42_v2 --gpu 0\", \"finished_at\": \"2026-05-17T16:36:02.114Z\", \"training_hours\": 0.52}, \"pid\": \"57864\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_bce30_s42_v2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T16:36:05.665812+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"predictor_native_sparsity\": 0.064, \"lambda_max\": 50000, \"final_bce_loss\": 0.5324, \"steps\": 1000, \"constraint_satisfied\": false, \"sparsity_trajectory\": \"49%→5% collapse in 50 steps, no recovery over 950 steps\", \"note\": \"10x stronger Lagrangian produces identical sparsity as v1 (lambda=5000). Confirms BCE gradient insufficiency is fundamental, not constraint strength.\"}, \"checkpoint_path\": \"checkpoints/qwen14b_bce30_s42_v2/predictor_bce.pt\", \"completed_at\": \"2026-05-17T16:51:07.306Z\"}, \"qwen14b_bce30_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:44:00.465Z\", \"updated_at\": \"2026-05-17T16:48:35.405Z\", \"hypothesis\": \"BCE objective on Qwen-2.5-14B at 30% sparsity produces significantly worse PPL than KL (mirroring LLaMA-8B where KL PPL=11.79 vs BCE PPL=22.51), confirming objective mismatch between per-neuron BCE training and global top-k inference generalizes across model scales\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type bce --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.3 --lambda_max 5000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_bce30_s42 --wandb_run_name qwen14b_bce30_s42 --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"55026\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_bce30_s42.log\", \"submitted_at\": \"2026-05-17T15:45:38.131Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2533.6, \"gpu_hours\": 0.7}, \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-17T15:45:17.302Z\", \"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type bce --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.3 --lambda_max 5000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_bce30_s42 --wandb_run_name qwen14b_bce30_s42 --gpu 0\", \"finished_at\": \"2026-05-17T15:54:32.863Z\", \"training_hours\": 0.15}, \"pid\": \"55026\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_bce30_s42.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T15:54:42.131414+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"dense_ppl\": 5.18, \"predictor_hard_mask_ppl\": 5.57, \"teal_global_ppl\": 8.76, \"ppl_ratio_hard_mask\": 1.075, \"ppl_ratio_hard_mask_note\": \"at predictor native 6.4% sparsity, not comparable to KL's 28.1%\", \"ppl_ratio_teal\": 1.69, \"actual_sparsity_teal\": 0.3, \"predictor_native_sparsity\": 0.064, \"training_log_sparsity_note\": \"Training Lagrangian failed (predictor sparsity=6.4%). Inference via TEAL forces 30% externally. TEAL PPL 8.76 is valid for method comparison.\", \"final_loss\": 0.5561, \"final_bce_loss\": 0.5324, \"steps\": 1000, \"constraint_satisfied\": false}, \"checkpoint_path\": \"checkpoints/qwen14b_bce30_s42/predictor_bce.pt\", \"completed_at\": \"2026-05-17T16:27:51.729Z\"}, \"downstream_extended_kl30_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:28:07.772Z\", \"updated_at\": \"2026-05-17T16:29:24.438Z\", \"hypothesis\": \"KL-distilled 30% sparsity predictor (s42, global) maintains strong performance on extended downstream benchmarks (HellaSwag, PIQA, TriviaQA, HumanEval) beyond the core evaluation suite, demonstrating broad capability retention at 30% activation sparsity\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id downstream_extended_kl30_s42 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks hellaswag,piqa,boolq --gpu 0\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"lm-eval-harness datasets\", \"data_count\": 0, \"seed\": 42, \"checkpoint_source\": \"kl_sparsity30_s42_v3\"}, \"metrics\": {\"hellaswag_acc_norm\": 0.727, \"hellaswag_acc\": 0.527, \"piqa_acc_norm\": 0.7595, \"piqa_acc\": 0.747, \"boolq_acc\": 0.7685}, \"conclusion\": \"success\", \"checkpoint_path\": \"checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/results/benchmark/downstream_extended_kl30_s42/\", \"completed_at\": \"2026-05-17T16:29:24.438Z\"}, \"kl30_s123_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:07:31.323Z\", \"updated_at\": \"2026-05-17T15:56:43.852Z\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl30_s123_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_30pct_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"42014\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_s123_eval.log\", \"submitted_at\": \"2026-05-17T12:53:02.294Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-2 + lm-eval cached\", \"data_count\": \"full\", \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/kl_30pct_s123/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"checkpoints/kl_30pct_s123/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 11021.6, \"gpu_hours\": 3.06}, \"hypothesis\": \"30% uniform allocation consistently improves MMLU across seeds — s123 uniform should show similar +15pp gain over global as s42 (0.2527→0.4061), confirming allocation-driven variance stabilization\", \"reproduce\": {\"finished_at\": \"2026-05-17T13:29:37.212Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T13:29:43.245057+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.8308, \"arc_challenge_acc_norm\": 0.4531, \"winogrande_acc\": 0.6938, \"mmlu_acc\": 0.3944, \"gsm8k_exact_match\": 0.0751, \"actual_sparsity\": 0.3, \"allocation\": \"uniform\"}, \"completed_at\": \"2026-05-17T15:56:43.852Z\"}, \"kl30_s456_train\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:49:00.577Z\", \"updated_at\": \"2026-05-17T15:56:42.699Z\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && /root/miniconda3/bin/python -u src/train.py --loss_type kl_normalized --sparsity_target 0.3 --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 456 --lambda_max 5000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/kl_30pct_s456 --wandb_run_name kl_30pct_s456\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"42087\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_s456_train.log\", \"submitted_at\": \"2026-05-17T12:53:04.086Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103 local\", \"data_count\": \"full\", \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 456, \"checkpoint_path\": \"checkpoints/kl_30pct_s456/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 11018.6, \"gpu_hours\": 3.06}, \"hypothesis\": \"KL-normalized 30% predictor training with seed 456 produces comparable PPL to s42 (8.98) and s123 (8.97), enabling 3-seed multi-seed validation of uniform allocation claim\", \"reproduce\": {\"finished_at\": \"2026-05-17T13:29:14.238Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T13:29:17.491679+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.2021, \"actual_sparsity\": 0.289, \"constraint_satisfied\": true, \"training_steps\": 1000}, \"completed_at\": \"2026-05-17T15:56:42.699Z\"}, \"qwen14b_kl30_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:27:08.956Z\", \"updated_at\": \"2026-05-17T14:50:16.405Z\", \"hypothesis\": \"KL-normalized sparsity predictor distillation generalizes from LLaMA-8B to Qwen-2.5-14B: at 30% sparsity the predictor should achieve comparable relative PPL degradation (dense→sparse ratio) as LLaMA-8B (6.12→8.98, 1.47x), validating cross-scale and cross-architecture transferability of the distillation method\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type kl_normalized --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.3 --lambda_max 5000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_kl30_s42 --wandb_run_name qwen14b_kl30_s42 --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"50349\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s42.log\", \"submitted_at\": \"2026-05-17T14:28:58.095Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1278.3, \"gpu_hours\": 0.36}, \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"50349\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s42.log\", \"reproduce\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type kl_normalized --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.3 --lambda_max 5000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_kl30_s42 --wandb_run_name qwen14b_kl30_s42 --gpu 0\", \"finished_at\": \"2026-05-17T14:44:07.166Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T14:44:10.372979+00:00\"}]}, \"metrics\": {\"dense_ppl\": 5.18, \"predictor_hard_mask_ppl\": 6.8, \"teal_global_ppl\": 7.62, \"ppl_ratio_hard_mask\": 1.31, \"ppl_ratio_teal\": 1.47, \"final_loss\": 0.3398, \"training_sparsity\": 0.281, \"teal_sparsity\": 0.3, \"lambda\": 5000, \"steps\": 1000}, \"checkpoint_path\": \"checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T14:50:16.405Z\"}, \"kl50_s456_global_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:56:48.642Z\", \"updated_at\": \"2026-05-17T14:38:11.650Z\", \"hypothesis\": \"50% global allocation with seed 456 produces MMLU consistent with s42 (0.2789) and s123 (0.2752), completing the 3-seed global baseline at 50% sparsity\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl50_s456_global --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/mvp_kl_norm_v2_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"44798\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl50_s456_global_eval.log\", \"submitted_at\": \"2026-05-17T13:33:43.512Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-2 + lm-eval cached\", \"data_count\": \"full\", \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 456, \"checkpoint_source\": \"checkpoints/mvp_kl_norm_v2_s456/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 3039.3, \"gpu_hours\": 0.84}, \"reproduce\": {\"finished_at\": \"2026-05-17T14:17:22.092Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T14:17:27.779906+00:00\"}]}, \"metrics\": {\"ppl_wikitext2\": 11.8057, \"arc_challenge\": 0.3319, \"winogrande\": 0.6488, \"mmlu\": 0.2794, \"gsm8k\": 0.0212}, \"conclusion\": \"success\", \"checkpoint_path\": \"checkpoints/mvp_kl_norm_v2_s456/predictor_kl_normalized.pt\", \"log_path\": \"results/benchmark/kl50_s456_global/results.json\", \"completed_at\": \"2026-05-17T14:24:22.828Z\"}, \"kl30_s456_global_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:56:49.733Z\", \"updated_at\": \"2026-05-17T14:38:10.811Z\", \"hypothesis\": \"30% global allocation with seed 456 produces MMLU comparable to s42 (0.2527) and s123 (0.3807), quantifying seed variance under global allocation at 30%\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl30_s456_global --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_30pct_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"44873\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_s456_global_eval.log\", \"submitted_at\": \"2026-05-17T13:33:45.790Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-2 + lm-eval cached\", \"data_count\": \"full\", \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 456, \"checkpoint_source\": \"checkpoints/kl_30pct_s456/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 3038.2, \"gpu_hours\": 0.84}, \"reproduce\": {\"finished_at\": \"2026-05-17T14:17:00.942Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T14:17:04.207728+00:00\"}]}, \"metrics\": {\"ppl_wikitext2\": 8.9332, \"arc_challenge\": 0.4633, \"winogrande\": 0.7111, \"mmlu\": 0.4382, \"gsm8k\": 0.0758}, \"conclusion\": \"success\", \"checkpoint_path\": \"checkpoints/kl_30pct_s456/predictor_kl_normalized.pt\", \"log_path\": \"results/benchmark/kl30_s456_global/results.json\", \"completed_at\": \"2026-05-17T14:24:24.018Z\"}, \"kl_30pct_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:49:49.718Z\", \"updated_at\": \"2026-05-17T11:50:21.212Z\", \"hypothesis\": \"Multi-seed validation: KL 30% with seed=123 should produce PPL consistent with s42=8.98, confirming result stability\", \"spec\": {\"command\": \"python src/benchmark_eval.py --exp_id kl_30pct_s123 --checkpoint checkpoints/kl_30pct_s123/predictor_kl_normalized.pt --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"server\": \"westd-34887\", \"data_path\": \"wikitext-2 local + lm-eval cached\", \"data_count\": \"full\", \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 123, \"checkpoint_path\": \"checkpoints/kl_30pct_s123/predictor_kl_normalized.pt\", \"log_path\": \"results/benchmark/kl_30pct_s123_global/results.json\"}, \"metrics\": {\"ppl_wikitext2\": 8.9748, \"arc_challenge_acc_norm\": 0.4531, \"winogrande_acc\": 0.693, \"mmlu_acc\": 0.3807, \"gsm8k_exact_match\": 0.0758, \"sparsity\": 0.3, \"allocation\": \"global\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T11:50:21.212Z\"}, \"mistral_teal70_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:46:08.339Z\", \"updated_at\": \"2026-05-17T11:49:01.151Z\", \"hypothesis\": \"TEAL vanilla magnitude-based pruning at 70% sparsity on Mistral provides the baseline PPL reference for evaluating KL-distilled predictor improvements\", \"metrics\": {\"wikitext2_ppl\": 61.716, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"teal_vanilla_70pct\", \"sparsity\": 0.7, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 56.1922}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python src/benchmark_eval.py --baseline_mode teal_vanilla --sparsity 0.7 --allocation uniform\", \"server\": \"westd-34887\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_path\": \"N/A (baseline eval)\", \"log_path\": \"/root/distill_sparse_swiglu/results/benchmark/mistral_teal70_baseline/results.json\"}, \"completed_at\": \"2026-05-17T11:49:01.151Z\"}, \"mistral_teal30_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:46:06.522Z\", \"updated_at\": \"2026-05-17T11:48:59.184Z\", \"hypothesis\": \"TEAL vanilla magnitude-based pruning at 30% sparsity on Mistral provides the baseline PPL reference for evaluating KL-distilled predictor improvements\", \"metrics\": {\"wikitext2_ppl\": 8.3807, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"teal_vanilla_30pct\", \"sparsity\": 0.3, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 2.8569}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python src/benchmark_eval.py --baseline_mode teal_vanilla --sparsity 0.3 --allocation uniform\", \"server\": \"westd-34887\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_path\": \"N/A (baseline eval)\", \"log_path\": \"/root/distill_sparse_swiglu/results/benchmark/mistral_teal30_baseline/results.json\"}, \"completed_at\": \"2026-05-17T11:48:59.184Z\"}, \"mistral_kl70_teal_global\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:46:05.252Z\", \"updated_at\": \"2026-05-17T11:48:56.568Z\", \"hypothesis\": \"KL-distilled predictor with TEAL global-threshold allocation at 70% sparsity on Mistral achieves lower PPL than TEAL vanilla by leveraging learned importance scores for threshold selection\", \"metrics\": {\"wikitext2_ppl\": 13.3254, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_teal_global_70pct\", \"sparsity\": 0.7, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 7.8016}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python src/benchmark_eval.py --checkpoint checkpoints/mistral_kl70_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity 0.7\", \"server\": \"westd-34887\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/mistral_kl70_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/results/benchmark/mistral_kl70_teal_global/results.json\"}, \"completed_at\": \"2026-05-17T11:48:56.568Z\"}, \"mistral_kl50_teal_global\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:46:03.724Z\", \"updated_at\": \"2026-05-17T11:48:54.379Z\", \"hypothesis\": \"KL-distilled predictor with TEAL global-threshold allocation at 50% sparsity on Mistral achieves lower PPL than TEAL vanilla by leveraging learned importance scores for threshold selection\", \"metrics\": {\"wikitext2_ppl\": 8.6489, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_teal_global_50pct\", \"sparsity\": 0.5, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 3.1251}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python src/benchmark_eval.py --checkpoint checkpoints/mistral_kl_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity 0.5\", \"server\": \"westd-34887\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/mistral_kl_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/results/benchmark/mistral_kl50_teal_global/results.json\"}, \"completed_at\": \"2026-05-17T11:48:54.380Z\"}, \"mistral_kl30_teal_global\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:46:02.883Z\", \"updated_at\": \"2026-05-17T11:48:51.844Z\", \"hypothesis\": \"KL-distilled predictor with TEAL global-threshold allocation at 30% sparsity on Mistral achieves lower PPL than TEAL vanilla by leveraging learned importance scores for threshold selection\", \"metrics\": {\"wikitext2_ppl\": 6.7733, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_teal_global_30pct\", \"sparsity\": 0.3, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 1.2495}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python src/benchmark_eval.py --checkpoint checkpoints/mistral_kl30_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity 0.3\", \"server\": \"westd-34887\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/mistral_kl30_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/results/benchmark/mistral_kl30_teal_global/results.json\"}, \"completed_at\": \"2026-05-17T11:48:51.844Z\"}, \"mistral_kl70_pertoken\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:46:00.698Z\", \"updated_at\": \"2026-05-17T11:48:49.483Z\", \"hypothesis\": \"KL-distilled predictor with per-token pruning at 70% sparsity on Mistral achieves lower PPL than TEAL vanilla baseline by learning importance-aware neuron selection\", \"metrics\": {\"wikitext2_ppl\": 9.1086, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_pertoken_70pct\", \"sparsity\": 0.7, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 3.5848}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python src/benchmark_eval.py --checkpoint checkpoints/mistral_kl70_s42/predictor_kl_normalized.pt --sparsity_mode per_token --sparsity 0.7\", \"server\": \"westd-34887\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/mistral_kl70_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/results/benchmark/mistral_kl70_pertoken/results.json\"}, \"completed_at\": \"2026-05-17T11:48:49.483Z\"}, \"mistral_kl50_pertoken\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:45:59.708Z\", \"updated_at\": \"2026-05-17T11:48:47.665Z\", \"hypothesis\": \"KL-distilled predictor with per-token pruning at 50% sparsity on Mistral achieves lower PPL than TEAL vanilla baseline by learning importance-aware neuron selection\", \"metrics\": {\"wikitext2_ppl\": 7.2931, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_pertoken_50pct\", \"sparsity\": 0.5, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 1.7693}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python src/benchmark_eval.py --checkpoint checkpoints/mistral_kl_s42/predictor_kl_normalized.pt --sparsity_mode per_token --sparsity 0.5\", \"server\": \"westd-34887\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/mistral_kl_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/results/benchmark/mistral_kl50_pertoken/results.json\"}, \"completed_at\": \"2026-05-17T11:48:47.665Z\"}, \"mistral_kl30_pertoken\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:45:58.299Z\", \"updated_at\": \"2026-05-17T11:48:45.384Z\", \"hypothesis\": \"KL-distilled predictor with per-token pruning at 30% sparsity on Mistral achieves lower PPL than TEAL vanilla baseline by learning importance-aware neuron selection\", \"metrics\": {\"wikitext2_ppl\": 6.048, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_pertoken_30pct\", \"sparsity\": 0.3, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 0.5242}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python src/benchmark_eval.py --checkpoint checkpoints/mistral_kl30_s42/predictor_kl_normalized.pt --sparsity_mode per_token --sparsity 0.3\", \"server\": \"westd-34887\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/mistral_kl30_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/results/benchmark/mistral_kl30_pertoken/results.json\"}, \"completed_at\": \"2026-05-17T11:48:45.384Z\"}, \"mistral_dense_ppl\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:45:57.639Z\", \"updated_at\": \"2026-05-17T11:48:43.546Z\", \"hypothesis\": \"Mistral-7B-v0.3 dense WikiText-2 PPL establishes the upper-bound reference for all Mistral sparsity experiments\", \"metrics\": {\"wikitext2_ppl\": 5.5238, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"dense\", \"sparsity\": 0}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python src/benchmark_eval.py --model /root/autodl-tmp/models/mistral-7b/ --dense --tasks wikitext2\", \"server\": \"westd-34887\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_path\": \"N/A (dense eval)\", \"log_path\": \"/root/distill_sparse_swiglu/results/benchmark/mistral_dense_ppl/results.json\"}, \"completed_at\": \"2026-05-17T11:48:43.546Z\"}, \"kl_50pct_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:45:30.258Z\", \"updated_at\": \"2026-05-17T11:46:12.691Z\", \"hypothesis\": \"Multi-seed validation: KL 50% with seed=123 should produce PPL consistent with s42=11.79, confirming result stability\", \"spec\": {\"command\": \"python src/train_kl.py --seed 123 --sparsity_target 0.5 + benchmark_eval.py\", \"server\": \"westd-34887\", \"data_path\": \"wikitext-103 local\", \"data_count\": \"full\", \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 123, \"checkpoint_path\": \"checkpoints/kl_50pct_s123/predictor_kl_normalized.pt\", \"log_path\": \"results/benchmark/kl_50pct_s123_global/results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"ppl_wikitext2\": 11.745, \"arc_challenge_acc_norm\": 0.3814, \"winogrande_acc\": 0.6125, \"mmlu_acc\": 0.2752, \"gsm8k_exact_match\": 0.0281, \"sparsity\": 0.5, \"allocation\": \"global\"}, \"completed_at\": \"2026-05-17T11:46:12.691Z\"}, \"lm_eval_mistral_dense\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:04:50.269Z\", \"updated_at\": \"2026-05-17T11:46:11.110Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export TRANSFORMERS_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && python -u src/eval_benchmark.py --condition mistral_dense --tasks lm_eval --skip_ppl --gpu 0 --batch_size 4 --output_dir results/plan_009_mistral 2>&1 | tee logs/eval_mistral_dense_downstream.log\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"181111\", \"log_path\": \"~/runs/distill_sparse_swiglu/lm_eval_mistral_dense.log\", \"submitted_at\": \"2026-05-16T00:04:50.125Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 8243.6, \"gpu_hours\": 2.29}, \"conclusion\": \"success\", \"metrics\": {\"arc_challenge_acc_norm\": 0.6024, \"winogrande_acc\": 0.7869, \"mmlu_acc\": 0.6244, \"gsm8k_exact_match\": 0.3654, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"dense\", \"server\": \"westd-34887\"}, \"completed_at\": \"2026-05-16T02:22:13.690Z\", \"hypothesis\": \"Mistral-7B-v0.3 dense downstream benchmarks (ARC, WinoGrande, MMLU, GSM8K) establish the upper-bound reference for sparse model evaluation\"}, \"lm_eval_mistral_kl_50pct\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:56:57.775Z\", \"updated_at\": \"2026-05-17T11:46:10.270Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/lm_eval_sparse.py --model_name_or_path /root/autodl-tmp/models/mistral-7b/ --predictor_path checkpoints/mistral_kl_s42/predictor_kl_normalized.pt --sparsity_target 0.5 --tasks arc_challenge,winogrande,mmlu,gsm8k --output_path results/lm_eval_mistral_kl_50pct\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"195242\", \"log_path\": \"logs/lm_eval_mistral_kl_50pct.log\", \"submitted_at\": \"2026-05-16T10:56:32Z\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/mistral_kl_s42/predictor_kl_normalized.pt\"}, \"hypothesis\": \"KL-distilled predictor at 50% sparsity on Mistral preserves downstream task performance (ARC, WinoGrande, MMLU, GSM8K) relative to dense baseline\", \"reproduce\": {\"finished_at\": \"2026-05-16T04:14:21.036Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-16T04:14:21.866Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T04:14:24.376301+00:00\"}]}, \"metrics\": {\"arc_challenge_acc\": 0.2927, \"arc_challenge_acc_norm\": 0.3183, \"arc_challenge_acc_norm_stderr\": 0.0136, \"winogrande_acc\": 0.629, \"winogrande_acc_stderr\": 0.0136, \"mmlu_acc\": 0.2295, \"mmlu_acc_stderr\": 0.0035, \"mmlu_stem_acc\": 0.2125, \"mmlu_humanities_acc\": 0.2421, \"mmlu_social_sciences_acc\": 0.2171, \"mmlu_other_acc\": 0.2398, \"gsm8k_exact_match_strict\": 0.0045, \"gsm8k_exact_match_flexible\": 0.0212, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_distill_50pct_sparsity_s42\", \"arc_challenge_retention_vs_dense\": 0.528, \"winogrande_retention_vs_dense\": 0.799, \"mmlu_retention_vs_dense\": 0.368, \"gsm8k_retention_vs_dense\": 0.012}, \"notes\": \"Cron 误判为 failed（无 W&B 数据、无 sentinel 文件），Reviewer 确认日志完整、results/lm_eval_mistral_kl_50pct/summary.json 已生成。实际 conclusion=negative: MMLU 0.2295 (随机水平), GSM8K strict 0.0045。与 Llama 50% 一致的 cross-architecture downstream collapse，支撑 D028 Narrative A。\", \"parent\": \"mistral_kl_s42\"}, \"mistral_teal50_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T01:18:14.890Z\", \"updated_at\": \"2026-05-17T11:46:07.390Z\", \"hypothesis\": \"TEAL vanilla magnitude-based pruning at 50% sparsity on Mistral provides the baseline PPL reference for evaluating KL-distilled predictor improvements\", \"metrics\": {\"teal_baseline_ppl\": 18.3061, \"dense_ppl\": 5.5238, \"teal_vs_dense_ratio\": 3.31}, \"conclusion\": \"success\", \"spec\": {\"command\": \"benchmark_eval.py --model_path /root/autodl-tmp/models/mistral-7b/ --sparsity_mode teal_global --sparsity 0.5\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"model_name\": \"mistral-7b-v0.3\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"seed\": 42, \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/distill_sparse_swiglu/logs/mistral_teal50_baseline.log\"}, \"completed_at\": \"2026-05-17T01:18:40.098Z\", \"parent\": \"mistral_kl_s42\"}, \"kl50_s456_train_eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:22:27.459Z\", \"updated_at\": \"2026-05-17T11:22:27.459Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && bash /root/distill_sparse_swiglu/scripts/run_kl50_s456.sh\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"31394\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl50_s456_train_eval.log\", \"submitted_at\": \"2026-05-17T11:22:27.196Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"kl_bce_f1_oracle\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:44:06.291Z\", \"updated_at\": \"2026-05-17T07:45:02.127Z\", \"hypothesis\": \"BCE achieves higher per-neuron F1 against oracle magnitude mask than KL, but KL achieves far better PPL, proving that per-neuron mask accuracy is the wrong optimization proxy and output distribution fidelity (KL) is structurally superior\", \"spec\": {\"command\": \"python /root/distill_sparse_swiglu/scripts/kl_bce_f1_oracle.py\", \"server\": \"westd-34887\", \"data_path\": \"C4 calibration\", \"data_count\": 50, \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 42, \"checkpoint_source\": \"mvp_kl_norm_v2_s42 + bce_isocompute_v3_s42\", \"eval_data\": \"F1/precision/recall vs oracle magnitude top-50% mask\"}, \"conclusion\": \"success\", \"metrics\": {\"bce_f1\": 0.6128, \"bce_precision\": 0.6132, \"bce_recall\": 0.6124, \"kl_f1\": 0.5397, \"kl_precision\": 0.5112, \"kl_recall\": 0.5715, \"random_f1\": 0.5, \"kl_ppl\": 11.79, \"bce_ppl\": 22.51}}, \"global_30pct_retention\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:35:45.803Z\", \"updated_at\": \"2026-05-17T07:36:43.424Z\", \"hypothesis\": \"30% global top-k allocation starves middle knowledge layers (L12-20), explaining MMLU degradation; global allocation distributes budget away from layers with uniformly moderate activation scores\", \"spec\": {\"command\": \"python global_30pct_retention_analysis_script.py\", \"server\": \"westd-34887\", \"data_path\": \"C4 calibration\", \"data_count\": 50, \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 42, \"checkpoint_source\": \"kl_sparsity30_s42_v3\", \"eval_data\": \"C4 50 samples seq_len=2048 global top-k retention per layer\", \"checkpoint_path\": \"N/A (analysis)\", \"log_path\": \"/root/distill_sparse_swiglu/artifacts/global_30pct_retention_analysis.json\"}, \"conclusion\": \"negative\", \"metrics\": {\"early_retention\": 0.771, \"middle_retention\": 0.764, \"knowledge_L12_20_retention\": 0.797, \"late_L24_31_retention\": 0.501, \"L31_retention\": 0.284, \"L30_retention\": 0.366, \"starved_layers\": \"L27-L31\"}, \"completed_at\": \"2026-05-17T07:36:43.424Z\"}, \"reverse_kl_50pct_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:00:23.139Z\", \"updated_at\": \"2026-05-17T07:35:31.384Z\", \"hypothesis\": \"Reverse KL (mode-seeking, KL(p_sparse||p_dense)) produces different sparsity patterns than forward KL (mode-covering); mode-seeking may concentrate probability mass on fewer but more important neurons, potentially improving downstream at cost of PPL\", \"spec\": {\"command\": \"PYTHONUNBUFFERED=1 WANDB_MODE=disabled CUDA_VISIBLE_DEVICES=0 python src/train.py --loss_type reverse_kl --sparsity_target 0.5 --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --kl_temperature 1.0 --tau_start 1.0 --tau_end 0.1 --warmup_steps 100 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/reverse_kl_50pct_s42 --wandb_run_name reverse_kl_50pct_s42\", \"server\": \"westd-34887\", \"data_path\": \"wikitext-103\", \"data_count\": \"~4M tokens\", \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"random_init\", \"log_path\": \"/root/distill_sparse_swiglu/logs/reverse_kl_50pct_s42.log\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/reverse_kl_50pct_s42/\"}, \"conclusion\": \"negative\", \"metrics\": {\"ppl_wikitext2\": 12.8, \"vs_forward_kl\": \"+1.01 (+8.6%)\", \"sparsity\": 0.5}, \"completed_at\": \"2026-05-17T07:15:43.012Z\"}, \"jsd_50pct_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:00:24.134Z\", \"updated_at\": \"2026-05-17T07:15:44.018Z\", \"hypothesis\": \"JSD (symmetric divergence) balances mode-covering and mode-seeking properties, potentially combining forward KL's PPL advantage with reverse KL's downstream preservation\", \"spec\": {\"command\": \"PYTHONUNBUFFERED=1 WANDB_MODE=disabled CUDA_VISIBLE_DEVICES=1 python src/train.py --loss_type jsd --sparsity_target 0.5 --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --kl_temperature 1.0 --tau_start 1.0 --tau_end 0.1 --warmup_steps 100 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/jsd_50pct_s42 --wandb_run_name jsd_50pct_s42\", \"server\": \"westd-34887\", \"data_path\": \"wikitext-103\", \"data_count\": \"~4M tokens\", \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"random_init\", \"log_path\": \"/root/distill_sparse_swiglu/logs/jsd_50pct_s42.log\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/jsd_50pct_s42/\"}, \"conclusion\": \"negative\", \"metrics\": {\"ppl_wikitext2\": 12.54, \"vs_forward_kl\": \"+0.75 (+6.4%)\", \"sparsity\": 0.5}, \"completed_at\": \"2026-05-17T07:15:44.018Z\"}, \"mag_preservation_reg\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T05:12:31.666Z\", \"updated_at\": \"2026-05-17T05:12:31.666Z\", \"conclusion\": \"failed\"}, \"teal_kl_overlap_corrected\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T05:10:52.550Z\", \"updated_at\": \"2026-05-17T05:11:35.489Z\", \"hypothesis\": \"The 1.48x magnitude ratio of KL-only-pruned neurons is not a selection bias artifact; permutation testing and percentile rank analysis will confirm KL systematically prunes high-magnitude neurons that TEAL preserves\", \"parent\": \"teal_kl_overlap_analysis\", \"spec\": {\"command\": \"python /root/distill_sparse_swiglu/scripts/teal_kl_overlap_corrected.py\", \"server\": \"westd-34887\", \"data_path\": \"cached activations from teal_kl_overlap.py\", \"data_count\": 27, \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 42, \"checkpoint_source\": \"teal_kl_overlap_analysis\", \"eval_data\": \"permutation test 1000 iterations on cached activations\", \"checkpoint_path\": \"N/A (analysis)\", \"log_path\": \"/root/distill_sparse_swiglu/artifacts/teal_kl_overlap_corrected.json\"}, \"conclusion\": \"success\", \"metrics\": {\"z_score\": 7260.3, \"p_value\": 0, \"median_percentile_rank\": 78.6, \"iqr_q1\": 64.4, \"iqr_q3\": 89.1, \"layers_significant\": \"31/32\", \"exception_layer\": 31}, \"completed_at\": \"2026-05-17T05:11:35.489Z\"}, \"sparsity_floor_extended\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T05:06:15.328Z\", \"updated_at\": \"2026-05-17T05:06:53.424Z\", \"hypothesis\": \"KL predictor's static sparsity floor scales with target sparsity but remains negligible (<1%) even at 70%, confirming the predictor learns contextual decisions not static patterns across all sparsity regimes\", \"parent\": \"natural_sparsity_floor_30pct\", \"spec\": {\"command\": \"python /root/distill_sparse_swiglu/scripts/sparsity_floor_extended.py\", \"server\": \"westd-34887\", \"data_path\": \"C4 calibration seq_len=2048\", \"data_count\": 50, \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 42, \"checkpoint_source\": \"kl_30pct_s42_v3, mvp_kl_norm_v2_s42, kl_sparsity70_s42\", \"eval_data\": \"C4 calibration 50 samples seq_len=2048\", \"checkpoint_path\": \"N/A (analysis)\", \"log_path\": \"/root/distill_sparse_swiglu/artifacts/sparsity_floor_extended.json\"}, \"conclusion\": \"success\", \"metrics\": {\"floor_30pct\": 0.0499, \"floor_50pct\": 0.0726, \"floor_70pct\": 0.1936, \"late_layer_max_30\": 0.4604, \"late_layer_max_50\": 1.2347, \"late_layer_max_70\": 4.3666, \"threshold\": 0.1, \"seq_len\": 2048, \"num_samples\": 50}, \"completed_at\": \"2026-05-17T05:06:53.424Z\"}, \"gradient_snr_constrained_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T04:42:09.639Z\", \"updated_at\": \"2026-05-17T04:42:47.488Z\", \"hypothesis\": \"Under fair Lagrangian-constrained training (both KL and BCE targeting 50% sparsity), KL still provides dramatically higher gradient SNR than BCE, confirming the advantage is from end-to-end coupling not from unconstrained regime\", \"parent\": \"gradient_snr_kl_vs_bce\", \"spec\": {\"command\": \"python /root/distill_sparse_swiglu/scripts/gradient_snr_constrained.py\", \"server\": \"westd-34887\", \"data_path\": \"C4 calibration\", \"data_count\": 200, \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 42, \"checkpoint_source\": \"gradient_snr_kl_vs_bce\", \"eval_data\": \"C4 calibration 200 steps gradient recording\", \"checkpoint_path\": \"N/A (analysis)\", \"log_path\": \"/root/distill_sparse_swiglu/artifacts/gradient_snr_constrained_results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"kl_avg_snr\": 0.000545, \"bce_avg_snr\": 5.28e-06, \"snr_ratio\": 103.2, \"kl_final_sparsity\": 0.508, \"bce_final_sparsity\": 0.591, \"steps\": 200}, \"completed_at\": \"2026-05-17T04:42:47.488Z\"}, \"teal_kl_overlap_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T04:40:07.085Z\", \"updated_at\": \"2026-05-17T04:40:49.604Z\", \"hypothesis\": \"KL predictor and TEAL prune different neuron sets; KL sacrifices high-magnitude knowledge neurons (concentrated in middle layers) to optimize output distribution matching, explaining why TEAL retains MMLU advantage despite worse PPL\", \"spec\": {\"command\": \"python /root/distill_sparse_swiglu/scripts/teal_kl_overlap.py\", \"server\": \"westd-34887\", \"data_path\": \"C4 calibration\", \"data_count\": 27, \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 42, \"checkpoint_path\": \"N/A (analysis)\", \"log_path\": \"/root/distill_sparse_swiglu/artifacts/teal_kl_overlap_analysis.json\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_jaccard\": 0.396, \"divergence_ratio\": 0.433, \"kl_only_pruned_magnitude_ratio\": 1.48, \"teal_only_pruned_mean_gate_prob\": 0.614, \"min_jaccard_layer\": \"L17-L18 (0.19)\", \"max_jaccard_layer\": \"L26-L28 (0.55)\"}, \"completed_at\": \"2026-05-17T04:40:49.604Z\"}, \"natural_sparsity_floor_30pct\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T04:39:07.157Z\", \"updated_at\": \"2026-05-17T04:39:42.442Z\", \"hypothesis\": \"KL predictor at 30% sparsity has a significant static sparsity floor (always-pruned neurons), explaining why actual sparsity (28.5%) undershoots target; if floor is high, predictor relies heavily on static patterns rather than contextual decisions\", \"spec\": {\"command\": \"python /root/distill_sparse_swiglu/scripts/natural_sparsity_floor.py\", \"server\": \"westd-34887\", \"data_path\": \"C4 calibration\", \"data_count\": 100, \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 42, \"checkpoint_path\": \"N/A (analysis)\", \"log_path\": \"/root/distill_sparse_swiglu/artifacts/natural_sparsity_floor_analysis.json\"}, \"conclusion\": \"success\", \"metrics\": {\"always_pruned_ratio\": 0.0006, \"always_pruned_count\": 278, \"total_neurons\": 458752, \"late_layer_max_ratio\": 0.0051, \"threshold\": 0.1}, \"completed_at\": \"2026-05-17T04:39:42.442Z\"}, \"gradient_snr_kl_vs_bce\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T04:14:30.896Z\", \"updated_at\": \"2026-05-17T04:15:00.192Z\", \"hypothesis\": \"KL loss provides higher gradient signal-to-noise ratio than BCE because end-to-end coupling propagates output-distribution information to early layers, while BCE's local proxy targets saturate early-layer gradients\", \"spec\": {\"command\": \"python /root/distill_sparse_swiglu/scripts/gradient_snr_analysis.py\", \"server\": \"westd-34887\", \"data_path\": \"C4 calibration\", \"data_count\": 80, \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 42, \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/root/distill_sparse_swiglu/artifacts/gradient_snr_results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"kl_avg_snr\": 5.77e-05, \"bce_avg_snr\": 1e-05, \"snr_ratio\": 5.76, \"early_layer_ratio_range\": \"34-156x\", \"late_layer_ratio_range\": \"2-4x\"}, \"completed_at\": \"2026-05-17T04:15:00.192Z\"}, \"training_free_wina_greedy\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:07:09.080Z\", \"updated_at\": \"2026-05-17T03:01:14.968Z\", \"spec\": {\"command\": \"python src/evaluate.py --baseline_mode wina_greedy --sparsity_target 0.5 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --gpu 0\", \"server\": \"westd-34887\", \"data_path\": \"wikitext-2 (HF)\", \"data_count\": 141, \"model_name\": \"LLaMA-3.1-8B\", \"seed\": \"default\", \"checkpoint_source\": \"N/A (training-free baseline)\", \"eval_data\": \"WikiText-2\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/wina_greedy_eval.log\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T19:07:30.505Z\", \"metrics\": {\"wina_greedy_ppl\": 2126.03, \"dense_ppl\": 6.12, \"model_level_sparsity\": 0.5, \"eval_dataset\": \"WikiText-2\", \"eval_seq_len\": 2048, \"greedy_allocation_summary\": \"layers 0-11: 0.90, layer 12: 0.85, layer 13: 0.80, layer 14: 0.70, layers 15-16: 0.50-0.55, layers 17-20: 0.30-0.35, layers 21-24: 0.05-0.15, layers 25-31: 0.00\"}, \"hypothesis\": \"WINA greedy per-layer budget allocation 是否优于 TEAL 的 uniform/global top-k——如果 PPL 极差则说明 greedy allocation 在 SwiGLU FFN 结构上不适用\", \"notes\": \"WINA greedy PPL=2126.03 (vs dense 6.12, vs TEAL uniform 23.31)。Greedy allocation 彻底失败。证伪分析：greedy 按逐层 sensitivity 贪心分配 budget，但 SwiGLU 的 gate*up 结构使层间 importance 相互依赖——greedy 将后层 budget 压到 0%（layers 25-31），摧毁 LM head 直连层。这证实 per-layer budget 需要保证每层最低 keep ratio，uniform 是更安全的起点。\"}, \"bench_teal70\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T01:19:59.714Z\", \"updated_at\": \"2026-05-17T03:01:08.870Z\", \"hypothesis\": \"TEAL magnitude-based 70% sparsity 的 PPL 退化程度——量化 training-free pruning 在极端稀疏度下的失败模式（预期 PPL>50，远差于 KL predictor，确认 beyond-critical regime 中静态方法彻底失效）\", \"metrics\": {\"wikitext2_ppl\": 100.11, \"dense_ppl\": 6.12, \"actual_sparsity\": 0.7, \"source\": \"training_free_baselines experiment (vanilla teal global)\"}, \"conclusion\": \"success\", \"spec\": {\"command\": \"benchmark_eval.py (data sourced from training_free_baselines)\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"model_name\": \"llama-3.1-8b\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"seed\": 42, \"checkpoint_path\": \"N/A (no predictor, vanilla TEAL)\", \"log_path\": \"N/A (existing data)\"}, \"completed_at\": \"2026-05-17T01:28:38.684Z\"}, \"bench_kl70_global\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T01:19:58.812Z\", \"updated_at\": \"2026-05-17T03:01:06.065Z\", \"hypothesis\": \"KL predictor 在 70% 极端稀疏度 (beyond-critical regime) + global top-k 下的 PPL——与 TEAL 70% (100.11) 对比量化 KL 优势在高稀疏度下是否放大（预期 advantage ratio >5×）\", \"metrics\": {\"wikitext2_ppl\": 17.91, \"dense_ppl\": 6.12, \"actual_sparsity\": 0.7, \"source\": \"kl_sparsity70_s42_v2 (teal_global_masks protocol)\", \"vanilla_teal_ppl\": 100.11}, \"conclusion\": \"success\", \"spec\": {\"command\": \"benchmark_eval.py (data sourced from kl_sparsity70_s42_v2)\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"model_name\": \"llama-3.1-8b\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"seed\": 42, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_sparsity70_s42/predictor_kl_normalized.pt\", \"log_path\": \"N/A (existing data)\"}, \"completed_at\": \"2026-05-17T01:28:37.679Z\"}, \"bench_kl50_global\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:04:18.606Z\", \"updated_at\": \"2026-05-17T03:01:03.243Z\", \"hypothesis\": \"KL 50% + global top-k 在统一 few-shot 协议下的 downstream 崩溃程度——量化 global allocation 导致的知识层 over-pruning 严重性（MMLU 预期<30%，接近随机，确认 global top-k 在 50% 下不可用于知识任务）\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && export WANDB_MODE=offline && python -u src/benchmark_eval.py --exp_id bench_kl50_global --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"222648\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_kl50_global.log\", \"submitted_at\": \"2026-05-16T09:37:16.642Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"checkpoint_source\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_path\": \"wikitext2+lm_eval\", \"data_count\": 0, \"seed\": 42, \"wall_clock_seconds\": 7362.3, \"gpu_hours\": 2.05}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/results/benchmark/bench_kl50_global/results.json\", \"completed_at\": \"2026-05-16T11:39:58.990Z\", \"metrics\": {\"wikitext2_ppl\": 11.7933, \"arc_challenge_acc_norm\": 0.3285, \"winogrande_acc\": 0.6346, \"mmlu_acc\": 0.2789, \"gsm8k_exact_match\": 0.0129, \"actual_sparsity\": 0.5}}, \"bench_kl30_uniform\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:04:04.454Z\", \"updated_at\": \"2026-05-17T03:00:59.902Z\", \"hypothesis\": \"KL 30% + uniform per-layer allocation 在统一 few-shot 协议下同时保持低 PPL 和较好 downstream——验证此为论文推荐的实用配置（PPL/downstream/latency 最佳平衡点，MMLU 预期>35%）\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id bench_kl30_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"219007\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_kl30_uniform.log\", \"submitted_at\": \"2026-05-16T08:01:09.960Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 4530.9, \"gpu_hours\": 1.26}, \"metrics\": {\"wikitext2_ppl\": 8.8157, \"arc_challenge_acc_norm\": 0.4078, \"winogrande_acc\": 0.6859, \"mmlu_acc\": 0.4061, \"gsm8k_exact_match\": 0.0735, \"actual_sparsity\": 0.3}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T09:16:40.819Z\"}, \"eval_kl30_teal_30pct\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:15:54.042Z\", \"updated_at\": \"2026-05-17T03:00:57.138Z\", \"hypothesis\": \"KL 30% predictor 在 sparsity_target=0.3 条件下的真实 TEAL PPL——验证之前 13.63 是否由 evaluate.py 默认 target=0.5 导致虚高（正确值预期接近 9.0 而非 13.6）\", \"spec\": {\"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"command\": \"CUDA_VISIBLE_DEVICES=0 nohup python -u src/evaluate.py --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_target 0.3 --gpu 0\", \"pid\": 213573, \"log_path\": \"~/runs/distill_sparse_swiglu/eval_kl30_teal_30pct.log\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"wikitext-2 + c4\", \"data_count\": 200, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext-2, c4\", \"parent\": \"kl_sparsity30_s42_v3\", \"checkpoint_path\": \"N/A (eval only)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T06:21:51.097Z\", \"metrics\": {\"dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 7.3, \"teal_sparse_ppl\": 8.98, \"sparsity_target\": 0.3, \"actual_sparsity\": 0.3}}, \"bench_dense\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:10:27.292Z\", \"updated_at\": \"2026-05-17T03:00:54.085Z\", \"hypothesis\": \"Dense LLaMA-3.1-8B 在 benchmark_eval.py 统一 few-shot 协议 (ARC-c 25-shot, WG 5-shot, MMLU 5-shot, GSM8K 8-shot) 的基准分——所有 sparse 方法对比的上界，任何 sparse 配置超过此值即为评估 bug\", \"spec\": {\"command\": \"benchmark_eval.py --dense --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"209887\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_dense.log\", \"submitted_at\": \"2026-05-16T05:24:03.581Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext2 + arc_challenge + winogrande + mmlu + gsm8k\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b (dense baseline)\", \"seed\": 42, \"wall_clock_seconds\": 3056.0, \"gpu_hours\": 0.85, \"checkpoint_path\": \"N/A (eval only)\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:12:49.576Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:12:51.738928+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 6.1173, \"arc_challenge_acc\": 0.5478, \"arc_challenge_acc_norm\": 0.5828, \"winogrande_acc\": 0.7806, \"mmlu_acc\": 0.6527, \"gsm8k_exact_match\": 0.4875}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/results/benchmark/bench_dense/results.json\", \"completed_at\": \"2026-05-16T06:14:59.574Z\"}, \"kl_sparsity30_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:30:30.528Z\", \"updated_at\": \"2026-05-17T03:00:50.360Z\", \"spec\": {\"command\": \"bash -c 'source setup_env.sh && python src/train.py --loss_type kl_normalized --sparsity_target 0.3 --num_steps 1000 --gradient_checkpointing'\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"132397\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity30_s42_v2.log\", \"submitted_at\": \"2026-05-15T20:30:30.429Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 1000, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"wall_clock_seconds\": 2662.6, \"gpu_hours\": 0.74}, \"hypothesis\": \"KL distillation 在 30% 温和稀疏度下能用 lambda_max=1000 稳定收敛到目标——如果 sparsity 不达标则说明 Lagrangian cap 需要按目标稀疏度级别调整（低 sparsity 需要更高 cap 来平衡小 constraint 信号）\", \"reproduce\": {\"finished_at\": \"2026-05-15T21:06:59.646Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:07:00.882117+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s42/predictor_kl_normalized.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity30_s42_v2.log\", \"completed_at\": \"2026-05-15T21:14:53.017Z\", \"metrics\": {\"final_loss\": 0.1465, \"kl_normalized\": 0.1465, \"kl_raw\": 0.1465, \"model_level_sparsity\": 0.281, \"sparsity_target\": 0.3, \"lambda_sparse_final\": 1000, \"lambda_max_cap\": 1000, \"tau_final\": 0.1, \"constraint_loss_final\": 0, \"training_steps\": 1000, \"wall_clock_seconds\": 2662.6, \"gpu_hours\": 0.74, \"note\": \"No PPL evaluation in training script. Sparsity stuck at 0.281 (same as v1). Lambda hit cap=1000 by step 220 and could not push sparsity further. W&B run was offline (not synced).\"}}, \"bce_gumbel_lagrangian_isolation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T20:58:31.768Z\", \"updated_at\": \"2026-05-17T03:00:37.906Z\", \"spec\": {\"command\": \"train_bce_gumbel.py --lr {1e-4,1e-3,3e-3} --num_steps 1000 --sparsity_target 0.5\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"model_name\": \"llama-3.1-8b\", \"data_path\": \"WikiText-103 train\", \"data_count\": null, \"seed\": 42, \"hypothesis\": \"BCE loss with identical framework (Gumbel+Lagrangian) still fails vs KL, proving loss function is the key factor\", \"checkpoint_path\": \"checkpoints/bce_framework_lr{1e4,1e3,3e3}/predictor_bce_gumbel.pt\", \"log_path\": \"/root/runs/bce_iso_framework.log\"}, \"metrics\": {\"lr_1e4_ppl\": 42.99, \"lr_1e3_ppl\": 48.4, \"lr_3e3_ppl\": 38.02, \"lr_1e4_bce_loss\": 0.7158, \"lr_1e3_bce_loss\": 0.6781, \"lr_3e3_bce_loss\": 0.6632, \"lr_1e4_sparsity\": 0.514, \"lr_1e3_sparsity\": 0.506, \"lr_3e3_sparsity\": 0.504, \"best_ppl\": 38.02, \"best_lr\": \"3e-3\", \"kl_baseline_ppl\": 11.79, \"gap_vs_kl\": 26.23}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T20:59:02.649Z\", \"hypothesis\": \"消融分离 Gumbel-sigmoid 和 Lagrangian 对 KL 训练成功的各自贡献——确认两者都是必要组件（去掉任一导致 sparsity collapse 或 PPL 显著退化）还是其中之一可省\"}, \"eval_c4_ood_kl50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:12:11.039Z\", \"updated_at\": \"2026-05-17T03:00:36.669Z\", \"spec\": {\"command\": \"python src/eval_c4_ood.py\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"model_name\": \"llama-3.1-8b\", \"data_path\": \"allenai/c4 validation (200 samples)\", \"data_count\": 200, \"seed\": 42, \"checkpoint_source\": \"mvp_kl_norm_v2_s42\", \"hypothesis\": \"KL predictor trained on WikiText-103 generalizes to OOD C4 data, maintaining advantage over TEAL\", \"checkpoint_path\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/results/c4_ood_ppl.json\"}, \"metrics\": {\"dense_ppl\": 9.2075, \"kl_50_global_ppl\": 18.401, \"teal_50_ppl\": 38.7503, \"kl_vs_dense_ratio\": 2, \"teal_vs_dense_ratio\": 4.21}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T19:58:43.318Z\", \"hypothesis\": \"KL predictor (WikiText-103 训练) 在 C4 OOD 数据上仍保持有效性（PPL 退化<15% vs in-distribution）——验证 predictor 学到的 neuron 重要性 pattern 是通用的而非 overfit 训练分布\"}, \"longbench_kl30_uniform_v6\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T16:56:19.111Z\", \"updated_at\": \"2026-05-17T03:00:35.333Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id longbench_kl30_uniform_v6 --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --multi_gpu --batch_size 1 --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"251051\", \"log_path\": \"~/runs/distill_sparse_swiglu/longbench_kl30_uniform_v6.log\", \"submitted_at\": \"2026-05-16T16:58:48.412Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"Xnhyacinth/LongBench\", \"data_count\": 800, \"seed\": 42, \"checkpoint_source\": \"kl_sparsity30_s42_v3\", \"checkpoint_path\": \"checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 6412.6, \"gpu_hours\": 3.56}, \"reproduce\": {\"finished_at\": \"2026-05-16T18:42:47.635Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T18:42:49.768403+00:00\"}]}, \"metrics\": {\"longbench_narrativeqa\": 4.12, \"longbench_qasper\": 6.23, \"longbench_gov_report\": 16.97, \"longbench_multi_news\": 18.01, \"runtime_seconds\": 6156.6}, \"conclusion\": \"negative\", \"notes\": \"LongBench KL 30% uniform: 3/4 任务显著低于 dense baseline（narrativeqa -44%, qasper -54%, gov_report -44%）。multi_news 异常高于 dense 但 dense baseline 本身极低(2.5)，可能是评估噪声。结论：uniform allocation 在长上下文任务上不如 dense，不纳入论文主体。\", \"completed_at\": \"2026-05-16T18:45:40.999Z\", \"parent\": \"longbench_dense_v6\", \"hypothesis\": \"KL 30% uniform 在 LongBench 长上下文任务能保持接近 dense 水平（差异<20%）——如果显著退化则说明 uniform per-layer budget 对长上下文中注意力依赖层的 neuron 保留不足\"}, \"longbench_dense_v6\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T15:37:54.958Z\", \"updated_at\": \"2026-05-17T03:00:33.325Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id longbench_dense_v6 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --dense --multi_gpu --batch_size 1 --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"247777\", \"log_path\": \"~/runs/distill_sparse_swiglu/longbench_dense_v6.log\", \"submitted_at\": \"2026-05-16T15:37:54.676Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"Xnhyacinth/LongBench\", \"data_count\": 800, \"seed\": 42, \"checkpoint_path\": \"N/A (dense baseline)\", \"wall_clock_seconds\": 4643.5, \"gpu_hours\": 2.58}, \"reproduce\": {\"finished_at\": \"2026-05-16T16:53:17.934Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T16:53:20.054818+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"longbench_narrativeqa\": 7.3, \"longbench_qasper\": 13.4, \"longbench_gov_report\": 30.5, \"longbench_multi_news\": 2.5}, \"log_path\": \"~/runs/distill_sparse_swiglu/longbench_dense_v6.log\", \"completed_at\": \"2026-05-16T16:55:18.181Z\", \"hypothesis\": \"Dense LLaMA 在 LongBench 长上下文任务 (NarrativeQA, Qasper, GovReport, MultiNews) 的基准分——作为 KL sparse 条件在长上下文场景的参照上界\"}, \"bench_kl50_uniform_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:27:20.124Z\", \"updated_at\": \"2026-05-17T03:00:32.121Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id bench_kl50_uniform_s456 --checkpoint checkpoints/mvp_kl_norm_v2_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 1\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"245022\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_kl50_uniform_s456.log\", \"submitted_at\": \"2026-05-16T14:50:27.834Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"wikitext-2 + downstream\", \"data_count\": 159, \"seed\": 456, \"checkpoint_source\": \"mvp_kl_norm_v2_s456\", \"checkpoint_path\": \"checkpoints/mvp_kl_norm_v2_s456/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 2707.2, \"gpu_hours\": 0.75}, \"reproduce\": {\"finished_at\": \"2026-05-16T15:32:45.150Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T15:32:47.250911+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 11.9604, \"arc_challenge_acc_norm\": 0.3345, \"winogrande_acc\": 0.6275, \"mmlu_acc\": 0.2874, \"gsm8k_exact_match\": 0.0212, \"actual_sparsity\": 0.5}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T15:35:35.058Z\", \"hypothesis\": \"KL 50% uniform multi-seed (s456) 统一协议评测——验证 PPL 结果跨种子稳定性（与 s42 差异<0.5 PPL 即确认 CV<1%）\"}, \"bench_kl50_uniform_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:27:17.469Z\", \"updated_at\": \"2026-05-17T03:00:31.166Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id bench_kl50_uniform_s123 --checkpoint checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"244544\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_kl50_uniform_s123.log\", \"submitted_at\": \"2026-05-16T14:49:46.268Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"wikitext-2 + downstream\", \"data_count\": 159, \"seed\": 123, \"checkpoint_source\": \"mvp_kl_norm_v2_s123\", \"checkpoint_path\": \"checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 2566.4, \"gpu_hours\": 0.71}, \"reproduce\": {\"finished_at\": \"2026-05-16T15:30:06.732Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T15:30:07.883751+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 11.83, \"arc_challenge_acc_norm\": 0.3515, \"winogrande_acc\": 0.6298, \"mmlu_acc\": 0.2751, \"gsm8k_exact_match\": 0.0235, \"actual_sparsity\": 0.5}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T15:32:32.686Z\", \"hypothesis\": \"KL 50% uniform multi-seed (s123) 统一协议评测——验证 PPL 结果跨种子稳定性（与 s42 差异<0.5 PPL 即确认 CV<1%）\"}, \"latency_benchmark\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:06:00.262Z\", \"updated_at\": \"2026-05-17T03:00:24.496Z\", \"spec\": {\"command\": \"python src/latency_benchmark.py\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"model_name\": \"llama-3.1-8b\", \"data_path\": \"N/A (synthetic input)\", \"data_count\": 100, \"seed\": 42, \"checkpoint_path\": \"N/A (benchmark)\", \"log_path\": \"/root/distill_sparse_swiglu/src/latency_benchmark.py\"}, \"conclusion\": \"success\", \"metrics\": {\"gpu_model\": \"NVIDIA RTX PRO 6000 Blackwell Server Edition\", \"dtype\": \"float16\", \"attn\": \"flash_attention_2\", \"batch\": 1, \"seq_len\": 2048, \"warmup\": 10, \"iters\": 100, \"dense_ms\": 119.11, \"dense_std\": 0.57, \"dense_tokens_per_s\": 17194.5, \"kl_30pct_ms\": 126.64, \"kl_30pct_std\": 0.7, \"kl_30pct_tokens_per_s\": 16171.8, \"kl_30pct_speedup\": 0.941, \"kl_50pct_ms\": 126.78, \"kl_50pct_std\": 0.31, \"kl_50pct_tokens_per_s\": 16154.2, \"kl_50pct_speedup\": 0.939, \"comp_30pct_ms\": 129.94, \"comp_30pct_std\": 0.75, \"comp_30pct_tokens_per_s\": 15761.4, \"comp_30pct_speedup\": 0.917, \"comp_50pct_ms\": 129.71, \"comp_50pct_std\": 0.53, \"comp_50pct_tokens_per_s\": 15788.8, \"comp_50pct_speedup\": 0.918, \"predictor_overhead_ms\": 3.17, \"predictor_overhead_pct\": 2.7, \"per_layer_predictor_ms\": 0.099, \"dense_ffn_per_layer_ms\": 2.427, \"sparse_ffn_pred_per_layer_ms\": 2.686, \"compensation_overhead_ms\": 3.3}, \"completed_at\": \"2026-05-16T14:24:47.243Z\", \"hypothesis\": \"KL predictor 的推理 latency overhead <10%（相对 dense baseline）——验证 predictor forward pass 不构成实用性瓶颈，支撑 practical deployment claim\"}, \"bench_kl40_global\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:20:14.275Z\", \"updated_at\": \"2026-05-17T03:00:21.964Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id bench_kl40_global --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity40_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.4 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"230101\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_kl40_global.log\", \"submitted_at\": \"2026-05-16T12:20:36.763Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"wikitext2+lm_eval\", \"data_count\": 0, \"seed\": 42, \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 2204.5, \"gpu_hours\": 0.61}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 10.117, \"arc_challenge_acc_norm\": 0.4096, \"winogrande_acc\": 0.6535, \"mmlu_acc\": 0.3806, \"gsm8k_exact_match\": 0.05, \"actual_sparsity\": 0.4}, \"checkpoint_path\": \"results/benchmark/bench_kl40_global/results.json\", \"completed_at\": \"2026-05-16T12:57:21.229Z\", \"hypothesis\": \"KL 40% + global top-k 统一协议评测——定位 budget-neutral 到 budget-deficit 转折点的精确退化程度，与 30%/50% 构成连续 sparsity 曲线\"}, \"bench_kl50_uniform\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:40:34.336Z\", \"updated_at\": \"2026-05-17T03:00:20.321Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id bench_kl50_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"229957\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_kl50_uniform.log\", \"submitted_at\": \"2026-05-16T12:20:33.499Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"wikitext2+lm_eval\", \"data_count\": 0, \"seed\": 42, \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 2207.1, \"gpu_hours\": 0.61}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.963, \"arc_challenge_acc_norm\": 0.3276, \"winogrande_acc\": 0.629, \"mmlu_acc\": 0.2777, \"gsm8k_exact_match\": 0.0212, \"actual_sparsity\": 0.5}, \"checkpoint_path\": \"results/benchmark/bench_kl50_uniform/results.json\", \"completed_at\": \"2026-05-16T12:57:20.631Z\", \"hypothesis\": \"KL 50% + uniform per-layer allocation 在统一协议下的 PPL 和 downstream——验证 uniform allocation 在 50% 下是否比 global top-k 保留更好的知识能力（MMLU 差异是否显著）\"}, \"bench_teal50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:40:31.432Z\", \"updated_at\": \"2026-05-17T03:00:16.203Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id bench_teal50 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --baseline_mode teal_vanilla --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"227770\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_teal50.log\", \"submitted_at\": \"2026-05-16T11:40:14.784Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"wikitext2+lm_eval\", \"data_count\": 0, \"seed\": 42, \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 2388.9, \"gpu_hours\": 0.66}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 23.31, \"arc_challenge_acc_norm\": 0.2841, \"winogrande_acc\": 0.5304, \"mmlu_acc\": 0.2832, \"gsm8k_exact_match\": 0.0197, \"actual_sparsity\": 0.5}, \"completed_at\": \"2026-05-16T12:20:03.725Z\", \"hypothesis\": \"TEAL 50% training-free baseline 统一协议评测——量化 KL predictor 在中等 sparsity 下相对 TEAL 的 PPL 优势幅度（预期 KL/TEAL ratio >1.5×）\"}, \"bench_teal30\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:40:29.575Z\", \"updated_at\": \"2026-05-17T03:00:14.912Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id bench_teal30 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --baseline_mode teal_vanilla --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"227692\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_teal30.log\", \"submitted_at\": \"2026-05-16T11:40:12.233Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"wikitext2+lm_eval\", \"data_count\": 0, \"seed\": 42, \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 2376.5, \"gpu_hours\": 0.66}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 10.97, \"arc_challenge_acc_norm\": 0.4232, \"winogrande_acc\": 0.6606, \"mmlu_acc\": 0.3861, \"gsm8k_exact_match\": 0.0788, \"actual_sparsity\": 0.3}, \"completed_at\": \"2026-05-16T12:19:48.700Z\", \"hypothesis\": \"TEAL 30% training-free baseline 统一协议评测——量化 KL predictor 在低 sparsity 下相对 TEAL 的 PPL 优势幅度（预期 KL/TEAL ratio >1.2×）\"}, \"bench_kl30_global\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:36:59.346Z\", \"updated_at\": \"2026-05-17T03:00:13.448Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && export WANDB_MODE=offline && python -u src/benchmark_eval.py --exp_id bench_kl30_global --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"222726\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_kl30_global.log\", \"submitted_at\": \"2026-05-16T09:37:18.471Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"checkpoint_source\": \"checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_path\": \"wikitext2+lm_eval\", \"data_count\": 0, \"seed\": 42, \"wall_clock_seconds\": 7359.9, \"gpu_hours\": 2.04}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/results/benchmark/bench_kl30_global/results.json\", \"completed_at\": \"2026-05-16T11:39:58.351Z\", \"metrics\": {\"wikitext2_ppl\": 8.9768, \"arc_challenge_acc_norm\": 0.3968, \"winogrande_acc\": 0.7017, \"mmlu_acc\": 0.2527, \"gsm8k_exact_match\": 0.0879, \"actual_sparsity\": 0.3}, \"hypothesis\": \"KL 30% predictor + global top-k allocation 的统一协议评测——与 uniform allocation 对比确认 global top-k 在低 sparsity 下是否仍导致知识层 over-pruning（MMLU 差异>5pp 即确认）\"}, \"lm_eval_dense\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:39:59.634Z\", \"updated_at\": \"2026-05-17T02:59:46.203Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 lm_eval --model hf --model_args pretrained=meta-llama/Llama-3.1-8B,dtype=float16 --tasks arc_challenge,winogrande,mmlu,gsm8k --batch_size auto --output_path /root/distill_sparse_swiglu/results/lm_eval_dense/\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"177099\", \"log_path\": \"~/runs/distill_sparse_swiglu/lm_eval_dense.log\", \"submitted_at\": \"2026-05-15T23:46:22.064Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"arc_challenge_acc_norm\": 0.5819, \"winogrande_acc\": 0.7814, \"mmlu_acc\": 0.6532, \"gsm8k_exact_match\": 0.5004, \"eval_tasks\": [\"arc_challenge\", \"winogrande\", \"mmlu\", \"gsm8k\"], \"model\": \"llama-3.1-8b\", \"condition\": \"dense\", \"server\": \"westd-34887\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (dense baseline, no predictor checkpoint)\", \"log_path\": \"/root/distill_sparse_swiglu/logs/lm_eval_dense/\", \"completed_at\": \"2026-05-15T23:43:36.784Z\", \"hypothesis\": \"Dense LLaMA-3.1-8B 在 lm-eval-harness 标准 downstream benchmark (ARC-c, WG, MMLU, GSM8K) 的基准分——所有 sparse 条件对比的参照上界\"}, \"lm_eval_kl_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:34:42.788Z\", \"updated_at\": \"2026-05-17T02:59:43.893Z\", \"spec\": {\"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/plan_007/\"}, \"notes\": \"## lm-eval Results (2026-05-16)\\n\\n| Task | Dense | KL Sparse 50% | Drop |\\n|------|-------|---------------|------|\\n| arc_challenge | 0.5819 | 0.3771 | -35.2% |\\n| winogrande | 0.7814 | 0.6156 | -21.2% |\\n| mmlu | 0.6532 | 0.2591 | -60.3% |\\n| gsm8k | 0.5004 | 0.0121 | -97.6% |\\n\\nEXIT_CODE=129 (SIGHUP). 结果保存在 plan_007/ 目录。\\n\\n### acc_norm 确认 (worker 验证)\\n所有指标已正确使用 acc_norm（可用时），无需修正。MMLU 无 acc_norm。\\n\\n### Mask 逻辑审查 (worker 验证) — 无 bug\\n- Mask shape/type/位置/predictor checkpoint 全部正确\\n- HFLM 透传验证：logit diff = 0.000000（patch 完整保留到 lm-eval）\\n- Per-token sparsity 动态工作：content words 保留更多 neurons\\n- 平均 sparsity 0.5031 ≈ 目标 0.50\\n\\n### 根因确认：PPL-Downstream Disconnect 是真实现象\\n\\\"Paris\\\" 从 dense top-2 (16.0) 降到 sparse top-5 (14.81)。logit 微小偏移足以翻转 4-choice 答案。\\n- PPL 是平均指标 → 多数 token 合理即可\\n- MMLU/GSM8K 要求精确知识检索 → 单个 token logit 偏移即致命\\n- Predictor 在 C4/WikiText 上训练，优化 PPL 而非 downstream accuracy\\n\\n### \\\"A\\\" Token Bias (debug worker 诊断)\\nSparse model MMLU letter-choice 下系统性偏好 \\\"A\\\"。是深层表征损伤的症状。\\n\\n### 服务器进程状态 (00:35 UTC)\\n- cuda:0: PID 181121 (Mistral dense gsm8k) — debug 进程已被 kill\\n- cuda:1: PID 174850 (Mistral KL gsm8k), PID 179918 (KL sparse rerun)\", \"metrics\": {\"arc_challenge_acc_norm\": 0.3771, \"winogrande_acc\": 0.6156, \"mmlu_acc\": 0.2591, \"gsm8k_exact_match\": 0.0121, \"eval_tasks\": [\"arc_challenge\", \"winogrande\", \"mmlu\", \"gsm8k\"], \"model\": \"llama-3.1-8b\", \"condition\": \"kl_sparse_50pct\", \"server\": \"westd-34887\", \"exit_code\": 129, \"wall_time_sec\": 3010, \"flag\": \"SUSPECT — gsm8k 0.50→0.01 catastrophic drop; PID 179918 rerunning with lm_eval_sparse.py\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A (eval experiment, source: /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt)\", \"log_path\": \"~/runs/distill_sparse_swiglu/lm_eval_kl_s42.log\", \"completed_at\": \"2026-05-16T01:57:27.364Z\", \"hypothesis\": \"KL predictor 的 PPL 优势 (9.21 vs dense 6.12) 能转化为 downstream task (ARC-c, WG, MMLU, GSM8K) 的保持——如果 downstream 崩溃而 PPL 良好则揭示 PPL-downstream disconnect 现象\"}, \"kl_sparsity70_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:34:18.823Z\", \"updated_at\": \"2026-05-17T02:59:42.831Z\", \"spec\": {\"command\": \"bash -c 'source setup_env.sh && python src/train.py --loss_type kl_normalized --sparsity_target 0.7 --num_steps 1000 --gradient_checkpointing'\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"132988\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity70_s42_v2.log\", \"submitted_at\": \"2026-05-15T20:34:18.724Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 1000, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"wall_clock_seconds\": 2456.7, \"gpu_hours\": 0.68}, \"reproduce\": {\"finished_at\": \"2026-05-15T21:11:35.632Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:11:36.854658+00:00\"}]}, \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 13.84, \"predictor_teal_sparse_ppl\": 17.91, \"vanilla_teal_sparse_ppl\": 100.11, \"teal_sparse_ppl\": 17.91, \"teal_sparse_ppl_static_baseline\": 17.91, \"model_level_sparsity\": 0.7, \"teal_sparse_note\": \"17.91 = predictor-based TEAL (teal_global_masks: predictor-gated magnitude scoring + global topk @70%). vanilla TEAL @70% = 100.11. 代码来源: quick_sp70.py L10 imports teal_global_masks, L60 调用. plan_007_all_ppl_fixed.json 的 mode=static_mask_70pct metadata 有误导性.\", \"eval_dataset\": \"wikitext-2\", \"eval_seq_len\": 2048, \"calibration_samples\": 32, \"per_layer_sparsity_range\": [0.508, 0.876]}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_sparsity70_s42/predictor_kl_normalized.pt\", \"conclusion\": \"success\", \"notes\": \"## Training Analysis (2026-05-16)\\n\\n### Training Summary\\n- 1000/1000 steps completed, EXIT_CODE=0\\n- Sparsity converged to ~0.688 (target 0.70, within 0.65-0.75 success range)\\n- Lambda hit cap 1000 by step 10, tau annealed 0.999 → 0.100\\n- KL loss: 1.18 → 0.61\\n\\n### PPL Evaluation Results\\n- true_dense_ppl: 6.12\\n- predictor_hard_mask_ppl: **13.84** (per-token adaptive mask)\\n- teal_sparse_ppl: **17.91** (static global topk, FIXED via D017)\\n- model_level_sparsity: 0.699\\n\\n### D017 Bug Fix (2026-05-15)\\nOriginal teal_sparse_ppl=136,069 was caused by using raw sigmoid scores for global topk mask selection. Sigmoid probabilities lack magnitude information and are poor proxies for static neuron importance. Fix: score neurons by mean(|intermediate| * predictor_hard_mask) — activation magnitude weighted by predictor decisions. Also added per-layer mean normalization (from _global_topk_masks). Result: 136K → 17.91.\", \"completed_at\": \"2026-05-15T21:15:15.421Z\", \"teal_sparse_ppl\": 17.91, \"hypothesis\": \"KL distillation 在 70% 极端稀疏度 (beyond-critical regime) 下仍能收敛且保持相对于 TEAL 的 PPL 优势——验证方法在高稀疏度下 advantage ratio 是否放大\"}, \"training_free_baselines\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:31:40.470Z\", \"updated_at\": \"2026-05-17T02:59:35.177Z\", \"spec\": {\"hypothesis\": \"Training-free baselines (TEAL Greedy, Vanilla TEAL, R-Sparse, WINA) at 50% sparsity establish lower bound\", \"model_name\": \"llama-3.1-8b\", \"server\": \"westd-34887\", \"data_path\": \"wikitext-2\", \"seed\": 42, \"command\": \"evaluate.py with various baseline methods\"}, \"conclusion\": \"success\", \"metrics\": {\"dense_ppl\": 6.12, \"vanilla_teal_global_ppl_30pct\": 10.97, \"vanilla_teal_global_ppl_50pct\": 23.31, \"vanilla_teal_global_ppl_70pct\": 100.11, \"wina_global_ppl_30pct\": 11.45, \"wina_global_ppl_50pct\": 27.93, \"wina_global_ppl_70pct\": 137.24, \"uniform_50pct_ppl\": 23.9, \"teal_greedy_ppl\": 33.47, \"vanilla_teal_global_ppl\": 23.31, \"wina_global_ppl\": 27.93, \"rsparse_global_ppl\": 151.2}, \"checkpoint_path\": \"N/A (training-free evaluation, no checkpoint)\", \"log_path\": \"N/A (training-free evaluation)\", \"completed_at\": \"2026-05-15T18:31:50Z\", \"notes\": \"2026-05-16 全部用 D017 bugfix (per-layer mean normalization) 后代码统一重跑确认。三个 sparsity level 全部物理一致：30% < 50% < 70%。TEAL: 10.97 < 23.31 < 100.11, WINA: 11.45 < 27.93 < 137.24。旧 70% TEAL=17.91 是 predictor-based TEAL (非 vanilla TEAL)，不可直接比较。代码确认 _global_topk_masks 包含 per-layer mean normalization (s_f / mu)。环境: HF_DATASETS_OFFLINE=1, CUDA_VISIBLE_DEVICES=1, setup_env.sh sourced。\", \"hypothesis\": \"TEAL magnitude-based training-free pruning 在多个 sparsity level (30/50/70%) 的 PPL 表现——建立 KL predictor 的标准参照基线，量化\\\"需要训练\\\"带来的增量\"}, \"bce_comp_staged_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:27:26.983Z\", \"updated_at\": \"2026-05-17T02:59:32.249Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train_bce_comp.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --num_steps 1000 --batch_size 4 --seq_len 2048 --predictor_lr 1e-3 --comp_lr 1e-3 --seed 42 --sparsity_target 0.5 --comp_warmup_steps 200 --comp_bottleneck 256 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/bce_comp_staged_s42 --wandb_run_name bce_comp_staged_s42 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"100045\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_comp_staged_s42.log\", \"submitted_at\": \"2026-05-15T18:02:08.405Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1585.7, \"gpu_hours\": 0.44}, \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T17:59:11.805Z\", \"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train_bce_comp.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --num_steps 1000 --batch_size 4 --seq_len 2048 --predictor_lr 1e-3 --comp_lr 1e-3 --seed 42 --sparsity_target 0.5 --comp_warmup_steps 200 --comp_bottleneck 256 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/bce_comp_staged_s42 --wandb_run_name bce_comp_staged_s42 --dataset wikitext-103\\\"\", \"finished_at\": \"2026-05-15T18:21:40.121Z\", \"training_hours\": 0.37}, \"pid\": \"100045\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_comp_staged_s42.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:21:41.095868+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/bce_comp_staged_s42/predictor_bce_comp.pt\", \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 25.44, \"predictor_hard_mask_ppl_no_comp\": 27.96, \"teal_sparse_ppl\": 44.54, \"model_level_sparsity\": 0.558, \"ppl_increase_vs_true_dense_pct\": 315.7, \"comp_loss_final\": 0.0033, \"bce_loss_final\": 0.6379, \"eval_seq_len\": 2048, \"calibration_samples\": 32}, \"notes\": \"BCE+Compensation staged training (200步BCE warmup + 800步joint). 训练正常完成1000步。Compensation带来约9%的per-token PPL改善(27.96→25.44)，但仍远差于KL-only(9.21)，差距2.8倍。TEAL路径不经过comp network，PPL=44.54与BCE-only一致。训练曲线：comp_loss从Phase2开始的0.0053稳定下降至0.0033，说明comp网络在学习但改善空间有限。⚠️ Sparsity mismatch: BCE+comp model_level_sparsity=0.558 vs KL model_level_sparsity=0.498。论文对比时必须标注此差异——BCE+comp 稀疏度更高意味着其 PPL 劣势可能被低估。结论：compensation不能弥补BCE损失函数的根本缺陷——不区分neuron重要性。强化Claim 1：KL distillation通过端到端输出对齐隐式学到neuron重要性排序，是更优方案。\", \"completed_at\": \"2026-05-15T18:28:34.060Z\", \"hypothesis\": \"BCE predictor + 后置 error compensation 能缩小与 KL-only 的 PPL 差距——如果差距仍>2× 则说明 BCE 损失函数本身（非 compensation 不足）是根本限制\"}, \"spon_training\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:27:18.117Z\", \"updated_at\": \"2026-05-17T02:59:29.428Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train_spon.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --predictor_checkpoint /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --num_steps 1000 --batch_size 8 --seq_len 128 --lr 1e-5 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/spon_kl_s42 --warmup_steps 100 --log_every 100 --dataset wikitext-103 --gradient_checkpointing\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"100400\", \"log_path\": \"~/runs/distill_sparse_swiglu/spon_training.log\", \"submitted_at\": \"2026-05-15T18:02:21.626Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1567.7, \"gpu_hours\": 0.44}, \"notes\": \"## 训练概要\\n1000 steps 正常完成，loss 波动在 0.38-0.47 区间，未有效收敛。Bias norm 从 0→0.041 后在 step 700 饱和。LR cosine+warmup 正常 (1e-5→0)。仅 458K/8B 可训练参数 (0.0057%)。\\n\\n## WikiText-2 评估 (seq_len=2048, 141 sequences)\\n- True Dense PPL: 6.12\\n- Per-token sparse PPL (predictor hard mask, no SPON): 9.22 (+50.6%)\\n- Per-token sparse + SPON PPL: 9.10 (+48.7%)\\n- SPON recovery: 仅 3.8% of sparse-vs-dense gap (0.12 PPL improvement)\\n- TEAL global mask sparse PPL (from KL-only eval): 12.08\\n\\n## 结论: **Negative**\\nSPON bias 补偿效果极其微弱，仅恢复 3.8% 的稀疏化误差。可能原因：\\n1. Bias norm 极小 (mean=0.041) 且提前饱和，说明学习容量不足或信号太弱\\n2. 训练 seq_len=128 vs eval seq_len=2048 的 mismatch 可能削弱效果\\n3. Per-token predictor hard mask 本身已经较好 (sparse PPL 9.22 vs TEAL global 12.08)，残余误差可能不是简单的 additive bias 能补偿的\\n\\n## Claim 2 影响\\nSPON + KL predictor 的加性组合改善微不足道。如果要验证 Claim 2，可能需要：(a) 更高表达力的补偿机制替代 static bias，或 (b) 更长 seq_len 训练，或 (c) 在 TEAL global mask 场景下测试 SPON（误差更大，补偿空间更大）。\", \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T17:59:12.581Z\", \"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train_spon.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --predictor_checkpoint /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --num_steps 1000 --batch_size 8 --seq_len 128 --lr 1e-5 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/spon_kl_s42 --warmup_steps 100 --log_every 100 --dataset wikitext-103 --gradient_checkpointing\\\"\", \"finished_at\": \"2026-05-15T18:11:02.835Z\", \"training_hours\": 0.2}, \"pid\": \"100400\", \"log_path\": \"~/runs/distill_sparse_swiglu/spon_training.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:11:03.876129+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"true_dense_ppl\": 6.1193, \"predictor_hard_mask_ppl\": 9.2165, \"spon_sparse_ppl\": 9.0977, \"spon_recovery_pct\": 3.8, \"ppl_improvement_from_spon\": 0.1188, \"ppl_increase_vs_true_dense_pct\": 48.7, \"ppl_increase_no_spon_vs_true_dense_pct\": 50.6, \"mean_bias_norm\": 0.040596, \"max_bias_norm\": 0.054199, \"teal_sparse_ppl\": 12.08, \"teal_with_spon_ppl\": 11.93, \"spon_dense_ppl_degradation\": 6.19, \"model_level_sparsity\": 0.5, \"eval_seq_len\": 2048, \"eval_samples\": 141, \"trainable_params\": 458752, \"trainable_pct\": 0.0057}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/spon_kl_s42/spon_biases.pt\", \"completed_at\": \"2026-05-15T18:28:29.369Z\", \"hypothesis\": \"SPON static bias correction 能显著恢复（>10%）稀疏化引入的 output 误差——如果恢复率<10% 则说明 static additive bias 无法补偿 contextual sparsity 的 token 级动态误差\"}, \"kl_only_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:19:37.074Z\", \"updated_at\": \"2026-05-17T02:59:26.550Z\", \"spec\": {\"hypothesis\": \"KL normalized v3 seed robustness: seed=1 应与 s42/s123/s456 一致，扩展到 5-seed headline\", \"loss_type\": \"kl_normalized_v3\", \"kl_normalization\": \"÷seq_len only (v3 fix)\", \"lagrangian\": \"lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]\", \"model_name\": \"llama-3.1-8b\", \"seed\": 1, \"data_path\": \"wikitext-103 (HF cached)\", \"parent\": \"mvp_kl_norm_v2_s42\", \"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 1 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/kl_only_s1 --wandb_run_name kl_only_s1 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"88843\", \"data_count\": null}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:57:17.967Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:57:20.105509+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_only_s1/predictor_kl_normalized.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_only_s1.log\", \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 9.15, \"teal_sparse_ppl\": 11.99, \"model_level_sparsity\": 0.498, \"ppl_increase_vs_true_dense_pct\": 96}, \"notes\": \"训练 1000 步正常完成，最终 loss=0.332, sparsity=0.484, lambda=1000。WikiText-2 评估：true_dense=6.12, hard_mask=9.15, teal_sparse=11.99, sparsity=0.498, PPL increase=31.0%。\\\\n\\\\n## 5-seed 汇总表 (KL normalized v3)\\\\n| Metric | s0 | s1 | s42 | s123 | s456 | Mean ± Std |\\\\n|--------|----|----|-----|------|------|------------|\\\\n| Dense PPL | 9.19 | 9.15 | 9.21 | 9.25 | 9.14 | 9.19 ± 0.04 |\\\\n| Sparse PPL | 12.03 | 11.99 | 12.08 | 11.91 | 13.58 | 12.32 ± 0.71 |\\\\n| PPL increase | 30.9% | 31.0% | 31.2% | 28.8% | 48.6% | 34.1% ± 8.2% |\\\\n\\\\n5-seed headline: sparse PPL 12.32 ± 0.71 (排除 s456 异常值后 4-seed mean=12.00 ± 0.07)。s1 是 5-seed 中最优（sparse PPL 11.99, dense PPL 9.15），确认 KL normalized v3 seed 鲁棒性良好。\", \"completed_at\": \"2026-05-15T18:09:33.637Z\", \"hypothesis\": \"Pure KL distillation 训练动态 multi-seed (seed=1) 验证：无约束 KL 的自然 sparsity emergence pattern 是否跨种子稳定\"}, \"kl_only_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:19:35.138Z\", \"updated_at\": \"2026-05-17T02:59:24.175Z\", \"spec\": {\"hypothesis\": \"KL normalized v3 seed robustness: seed=0 应与 s42/s123/s456 一致，扩展到 5-seed headline\", \"loss_type\": \"kl_normalized_v3\", \"kl_normalization\": \"÷seq_len only (v3 fix)\", \"lagrangian\": \"lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]\", \"model_name\": \"llama-3.1-8b\", \"seed\": 0, \"data_path\": \"wikitext-103 (HF cached)\", \"parent\": \"mvp_kl_norm_v2_s42\", \"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 0 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/kl_only_s0 --wandb_run_name kl_only_s0 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"88764\", \"data_count\": null}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:57:15.663Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:57:16.587876+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 9.19, \"teal_sparse_ppl\": 12.03, \"model_level_sparsity\": 0.499, \"ppl_increase_vs_true_dense_pct\": 96.57, \"eval_seq_len\": 2048, \"calibration_samples\": 32}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_only_s0/predictor_kl_normalized.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_only_s0.log\", \"notes\": \"训练 1000 步正常完成，最终 loss=0.305, sparsity=0.488, lambda=1000。\\\\n\\\\n## WikiText-2 评估 (seq_len=2048 重跑)\\\\n**2026-05-15 重跑原因**: 原 eval 使用 --seq_len 1024，与其他 seed (s1/s42/s123/s456) 的 2048 不一致，结果不可比。已用 seq_len=2048 重跑，结果与原始一致。\\\\n- true_dense_ppl: 6.12\\\\n- predictor_hard_mask_ppl (Dense PPL): 9.19\\\\n- teal_sparse_ppl (Sparse PPL): 12.03\\\\n- model_level_sparsity: 0.499\\\\n- ppl_increase_vs_true_dense_pct: 96.57%\\\\n\\\\n## 5-seed 汇总表 (KL normalized v3)\\\\n| Metric | s0 | s1 | s42 | s123 | s456 | Mean ± Std |\\\\n|--------|----|----|-----|------|------|------------|\\\\n| Dense PPL | 9.19 | 9.15 | 9.21 | 9.25 | 9.14 | 9.19 ± 0.04 |\\\\n| Sparse PPL | 12.03 | 11.99 | 12.08 | 11.91 | 13.58 | 12.32 ± 0.71 |\\\\n| PPL increase | 30.9% | 31.0% | 31.2% | 28.8% | 48.6% | 34.1% ± 8.2% |\\\\n\\\\n5-seed headline: sparse PPL 12.32 ± 0.71 (排除 s456 异常值后 4-seed mean=12.00 ± 0.07)。s0 结果与 s42/s123 高度一致，确认 KL normalized v3 seed 鲁棒性良好。s456 仍为唯一异常值。\", \"completed_at\": \"2026-05-15T18:09:33.157Z\", \"hypothesis\": \"Pure KL distillation（无 sparsity constraint）的训练动态：验证 KL loss 是否自然产生 sparse gate pattern，还是需要显式 sparsity 约束引导\"}, \"mvp_kl_norm_v2_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:19:33.798Z\", \"updated_at\": \"2026-05-17T02:59:22.263Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 456 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s456 --wandb_run_name mvp_kl_norm_v2_s456 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"74987\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_kl_norm_v2_s456.log\", \"submitted_at\": \"2026-05-15T15:57:22.577Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103 (HF cached)\", \"data_count\": null, \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"loss_type\": \"kl_normalized_v3\", \"kl_normalization\": \"÷seq_len only (v3 fix)\", \"lagrangian\": \"lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]\", \"hypothesis\": \"Fixed KL normalization (÷seq_len only, no ÷vocab_size) + Lagrangian produces better sparsity predictor than BCE at 50% sparsity\", \"wall_clock_seconds\": 2653.4, \"gpu_hours\": 0.74}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:33:37.465Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:33:38.622345+00:00\"}]}, \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 9.14, \"teal_sparse_ppl\": 13.58, \"model_level_sparsity\": 0.498, \"ppl_increase_vs_true_dense_pct\": 121.9, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s456/predictor_kl_normalized.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_kl_norm_v2_s456.log\", \"notes\": \"## 训练指标 (1000 steps)\\n- 最终 kl_raw: ~0.29-0.32, sparsity: 0.480-0.488, lambda: 1000 (饱和), tau: 0.1\\n- 训练正常完成，无报错\\n\\n## WikiText-2 评估\\n- True Dense PPL: 6.12\\n- Dense/Hard-mask PPL: 9.14\\n- TEAL Sparse PPL: 13.58\\n- PPL increase: 48.6%\\n- Model sparsity: 0.498\\n\\n## s456 Outlier 根因分析 (2026-05-15)\\n训练端完全正常（loss/sparsity/lambda 与其他 seed 一致）。问题在 TEAL 推理时的全局 topk 分配：\\n- s456 predictor 对 Layer 31 的 sigmoid 均分 = 0.5161（其他 4 seed 均值 = 0.5287，差 -0.0126）\\n- TEAL 将 Layer 31 keep ratio 压到 49.9%（其他 seed 52.1%），Layer 31 直连 LM head，微小剪枝差异被放大\\n- Layer 12 也偏低（-431 neurons），预算被挤向 Layer 7（+771 neurons）\\n- Hard-mask PPL 不受影响因为 per-token mask 不经过全局 topk\\n结论：不需要重跑。是 TEAL 全局分配的放大效应，非 predictor 质量问题。\\n论文报告建议：报 4-seed mean=12.00±0.07 + 注明 s456 为 TEAL 分配 outlier。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:41:35.971Z\", \"parent\": \"mvp_kl_norm_v2_s42\", \"hypothesis\": \"KL normalized predictor multi-seed 验证 (seed=456)：方法有效性不依赖种子选择，sparse PPL 应与 s42 (12.08) 一致（CV<5%）\"}, \"mvp_kl_norm_v2_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:19:03.245Z\", \"updated_at\": \"2026-05-17T02:59:20.835Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s123 --wandb_run_name mvp_kl_norm_v2_s123 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"72811\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_kl_norm_v2_s123.log\", \"submitted_at\": \"2026-05-15T15:19:03.209Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"Fixed KL normalization (÷seq_len only, no ÷vocab_size) + Lagrangian produces better sparsity predictor than BCE at 50% sparsity\", \"data_path\": \"wikitext-103 (HF cached)\", \"data_count\": null, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"loss_type\": \"kl_normalized_v3\", \"kl_normalization\": \"÷seq_len only (v3 fix)\", \"lagrangian\": \"lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]\", \"wall_clock_seconds\": 3568.6, \"gpu_hours\": 0.99}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:55:26.143Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:55:27.903101+00:00\"}]}, \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 9.2474, \"teal_sparse_ppl\": 11.9128, \"model_level_sparsity\": 0.4979, \"ppl_increase_vs_true_dense_pct\": 94.7, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:18:31.818Z\", \"notes\": \"KL normalized v3 (÷seq_len only), seed=123, 1000步训练。\\n\\n## WikiText-2 评估\\n| 指标 | KL s123 | BCE s123 |\\n|------|---------|----------|\\n| Dense PPL | 9.25 | 28.38 |\\n| Sparse PPL | 11.91 | 44.59 |\\n| PPL increase | 28.8% | 57.1% |\\n| Sparsity | 0.498 | 0.496 |\\n\\n## 结论: SUCCESS\\nKL normalized loss 在所有指标上显著优于 BCE。与 KL s42 高度一致（sparse PPL 11.91 vs 12.08），seed 稳定性良好。\", \"parent\": \"mvp_kl_norm_v2_s42\", \"hypothesis\": \"KL normalized predictor multi-seed 验证 (seed=123)：方法有效性不依赖种子选择，sparse PPL 应与 s42 (12.08) 一致（CV<5%）\"}, \"mvp_kl_norm_v2_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:19:01.567Z\", \"updated_at\": \"2026-05-17T02:59:19.006Z\", \"spec\": {\"command\": \"python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42 --dataset wikitext-103\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"72734\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_kl_norm_v2_s42.log\", \"submitted_at\": \"2026-05-15T15:19:01.533Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"Fixed KL normalization (÷seq_len only, no ÷vocab_size) + Lagrangian produces better sparsity predictor than BCE at 50% sparsity\", \"data_path\": \"wikitext-103\", \"data_count\": 1000, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"loss_type\": \"kl_normalized_v3\", \"kl_normalization\": \"÷seq_len only (v3 fix)\", \"lagrangian\": \"lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]\", \"wall_clock_seconds\": 3093.4, \"gpu_hours\": 0.86}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:55:23.754Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:55:24.584694+00:00\"}]}, \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 9.2142, \"teal_sparse_ppl\": 12.0776, \"model_level_sparsity\": 0.4979, \"ppl_increase_vs_true_dense_pct\": 97.4, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_kl_norm_v2_s42.log\", \"notes\": \"KL normalized v2 (÷seq_len only, 修复 ÷vocab_size bug) + Lagrangian, 1000步训练。\\n\\n## 训练指标\\n- KL loss: 1.18→0.49(step100)→0.26(step500)→0.30(step1000)\\n- Sparsity: 0.406→0.492→0.484→0.488, 稳定接近 target=0.5\\n- Lambda 收敛到 cap=1000, constraint=0 (满足约束)\\n\\n## WikiText-2 评估 (同一 evaluate.py 做公平对比)\\n|  | KL norm v2 (s42) | BCE (s42 rerun) |\\n|--|------------------|-----------------|\\n| Dense(hard mask) PPL | 9.21 | 27.96 |\\n| Sparse(TEAL) PPL | 12.08 | 44.54 |\\n| PPL increase | 31.2% | 59.3% |\\n| Model sparsity | 0.498 | 0.496 |\\n\\n## 重要发现\\nevaluate.py 的 \\\"Dense baseline\\\" 实际是通过 predictor hard mask 的评估（PredictorWrapper._patch_mlps() monkey-patch 所有 MLP，forward_dense() 执行后 sparse_mode 重置为 True）。因此 \\\"dense\\\" PPL 反映的是 predictor per-token hard mask 质量，而非真 dense 模型性能。\\n\\nKL predictor hard mask PPL (9.21) 接近真 dense (~8-9), 说明其学会了精准识别不重要 neuron。BCE hard mask PPL (27.96) 远差于真 dense，说明 BCE predictor 误杀重要 neuron。\\n\\n## Per-layer sparsity 分布差异\\n- KL: 非均匀 (0.215-0.806), 中间层低稀疏(保护), 后层高稀疏\\n- BCE: 较均匀 (0.430-0.664), 后层略高\\n\\n## 结论: SUCCESS\\nKL normalized loss 在所有指标上显著优于 BCE: TEAL sparse PPL 12.08 vs 44.54, PPL increase 31.2% vs 59.3%。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:10:34.895Z\", \"parent\": \"kl_lagrangian_quicktest\", \"hypothesis\": \"Per-token KL normalized loss (÷seq_len, 修复 ÷vocab_size bug) + 高 lambda_max Lagrangian 能同时解决量级不匹配和稀疏性坍塌，稳定收敛到 50% sparsity 且 PPL 显著优于 BCE\"}, \"kl_lagrangian_quicktest\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:17:49.894Z\", \"updated_at\": \"2026-05-17T02:59:15.944Z\", \"spec\": {\"hypothesis\": \"Lagrangian multiplier 自适应约束替代固定 reg_weight，防止 KL 训练稀疏性坍塌\", \"loss_type\": \"kl_lagrangian\", \"seed\": 42, \"model\": \"Llama-3.1-8B\", \"sparsity\": 0.5, \"steps\": 200, \"batch_size\": 4, \"seq_len\": 2048, \"gpu\": \"cuda:0\", \"server\": \"westd-34887\", \"parent\": \"mvp_kl_s42\"}, \"conclusion\": \"negative\", \"metrics\": {\"final_kl_loss\": 418, \"final_constraint_loss\": 1.211, \"final_sparsity\": 0.141, \"final_lambda\": 5.06, \"steps\": 200, \"sparsity_trajectory\": [0.406, 0.387, 0.289, 0.168, 0.141]}, \"notes\": \"NEGATIVE: Lagrangian 仍无法阻止稀疏性坍塌。Sparsity 0.406→0.141。根因: KL loss (~418) vs constraint (~1.2)，3 个数量级差距。lambda ×1.5 增长太慢 + cap=100 不够。即使 lambda=100, constraint=36 仍远小于 KL=418。梯度信号不足: clamp 约束项的梯度被 vocab 维度 KL 梯度淹没。\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_lagrangian_quicktest/predictor_kl.pt\", \"log_path\": \"Worker log: worker_code_lagrangian-kl_20260515T131820\", \"completed_at\": \"2026-05-15T13:32:07.173Z\", \"parent\": \"mvp_kl_s42\", \"hypothesis\": \"Lagrangian multiplier 自适应约束（lambda ×1.5 增长, cap=100）能解决 mvp_kl_s42 中固定 reg_weight 导致的稀疏性坍塌——如果仍坍塌则说明 KL/constraint 量级差需要更激进的 lambda 策略\"}, \"mvp_bce_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:51:08.412Z\", \"updated_at\": \"2026-05-17T02:59:12.511Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 456 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_bce_s456 --wandb_run_name mvp_bce_s456 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"61162\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_bce_s456.log\", \"submitted_at\": \"2026-05-15T13:34:54.067Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 988.6, \"gpu_hours\": 0.27}, \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"61162\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_bce_s456.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 456 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_bce_s456 --wandb_run_name mvp_bce_s456 --dataset wikitext-103\\\"\", \"finished_at\": \"2026-05-15T13:51:22.018Z\"}, \"notes\": \"训练完成 1000/1000 步，checkpoint 已保存。EXIT_CODE=129 (SIGHUP) 发生在 checkpoint save 之后、evaluation 之前。训练指标与 s42/s123 高度一致 (bce_loss=0.6388, sparsity=0.551)。待评估 WikiText-2 PPL。\", \"conclusion\": \"success\", \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"completed_at\": \"2026-05-15T13:51:22.638Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:51:23.359184+00:00\"}]}, \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 28.1437, \"teal_sparse_ppl\": 43.033, \"model_level_sparsity\": 0.4957, \"ppl_increase_vs_true_dense_pct\": 603.3, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_bce_s456/predictor_bce.pt\", \"hypothesis\": \"BCE predictor multi-seed 验证 (seed=456)：BCE 方法有效性不依赖种子选择，PPL 应与 s42 一致（CV<5%）\"}, \"mvp_bce_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:51:07.010Z\", \"updated_at\": \"2026-05-17T02:59:11.198Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_bce_s123 --wandb_run_name mvp_bce_s123 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"56744\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_bce_s123.log\", \"submitted_at\": \"2026-05-15T13:08:25.578Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1352.4, \"gpu_hours\": 0.38}, \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"56744\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_bce_s123.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_bce_s123 --wandb_run_name mvp_bce_s123 --dataset wikitext-103\\\"\", \"finished_at\": \"2026-05-15T13:24:41.027Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:24:41.707456+00:00\"}]}, \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 28.3817, \"teal_sparse_ppl\": 44.5864, \"model_level_sparsity\": 0.4957, \"ppl_increase_vs_true_dense_pct\": 629, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_bce_s123/predictor_bce.pt\", \"notes\": \"BCE loss, seed=123, 1000 steps. 训练正常完成，无报错。\\n\\n与 mvp_bce_s42 对比:\\n| 指标 | s42 | s123 | 差异 |\\n|------|-----|------|------|\\n| final_total_loss | 0.643 | 0.6433 | +0.0003 |\\n| final_bce_loss | 0.6379 | 0.6382 | +0.0003 |\\n| final_reg_loss | 0.0051 | 0.0051 | 相同 |\\n| final_sparsity | 0.551 | 0.551 | 相同 |\\n| model_level_sparsity | 0.498 | 0.498 | 相同 |\\n| wikitext2_ppl_dense | 27.96 | 28.38 | +0.42 |\\n| wikitext2_ppl_sparse | 44.21 | 44.83 | +0.62 |\\n| ppl_increase_pct | 58.1% | 57.9% | -0.2pp |\\n| training_time_min | 25.5 | 15.4 | -10.1min (可能因GPU型号差异) |\\n\\n结论: 两个 seed 的结果高度一致。loss、sparsity、PPL 增幅几乎相同，seed 稳定性良好。dense PPL 略有差异（28.38 vs 27.96）属正常 WikiText-2 评估波动。逐层稀疏性分布呈前低后高模式（浅层 ~0.44-0.47，深层 ~0.59-0.65），与 TEAL 论文观察一致。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T13:30:58.026Z\", \"hypothesis\": \"BCE predictor multi-seed 验证 (seed=123)：BCE 方法有效性不依赖种子选择，PPL 应与 s42 一致（CV<5%）\"}, \"mvp_bce_s42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T11:51:05.131Z\", \"updated_at\": \"2026-05-17T02:59:08.627Z\", \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_bce_s42 --wandb_run_name mvp_bce_s42 --dataset wikitext-103\\\"\", \"finished_at\": \"2026-05-15T12:25:03.637Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-15T11:58:31.436Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T11:58:32.308080+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T12:25:04.331964+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: DatasetNotFoundError — cerebras/SlimPajama-627B 在 HF Hub 上不存在或无法访问 (data_utils.py:36) | error_type: data | 已有成果: 模型加载成功 | 建议: 确认数据集路径或改用本地/streaming 方式\"}}, \"notes\": \"训练+评估完成。训练: 1000 steps, 25.5 min, BCE loss 0.6711→0.6430。评估: WikiText-2 PPL dense=27.96 → sparse=44.21 (+58.1%)。C4 评估跳过（离线模式无法 streaming 加载）。TEAL 逐层分布: 浅层~44-50%, 深层51-66%。注意: dense baseline 27.96 高于文献~6 因使用 packed chunks 非 sliding window，但 dense/sparse 对比公平。evaluate.py 有 off-by-one bug 已修复（原始 shift 重复导致错位）。58% PPL 增幅对 MVP 1000 steps 可接受，文献中充分训练可降至 1-5%。\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_bce_s42 --wandb_run_name mvp_bce_s42 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"50143\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_bce_s42.log\", \"submitted_at\": \"2026-05-15T12:08:23.512Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1677.7, \"gpu_hours\": 0.47}, \"pid\": \"50143\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_bce_s42.log\", \"conclusion\": \"success\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 27.9603, \"teal_sparse_ppl\": 44.537, \"model_level_sparsity\": 0.4957, \"ppl_increase_vs_true_dense_pct\": 628, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_bce_s42/predictor_bce.pt\", \"hypothesis\": \"BCE loss 训练 sparse gate predictor (seed=42) 在 50% sparsity 下能产生有效预测——作为 KL distillation 的对照基线，BCE 直接拟合 binary mask 而非蒸馏 dense output distribution\"}, \"mvp_kl_s42\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-15T11:50:59.003Z\", \"updated_at\": \"2026-05-17T02:59:05.828Z\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_kl_s42 --wandb_run_name mvp_kl_s42 --dataset wikitext-103\\\"\", \"finished_at\": \"2026-05-15T13:14:04.493Z\"}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 1.96 GiB. GPU 0 has a total capacity of 94.97 GiB of which 1.88 GiB is free. Including non-PyTorch memory, this process has 93.08 GiB memory in use. Of the allocated memory 88.41 GiB is allocated by PyTorch, and \", \"completed_at\": \"2026-05-15T11:58:28.834Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T11:58:29.490811+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T12:10:37.036636+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:14:05.191408+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"诊断中 | fix_worker_id: worker_diagnose_mvp_kl_s42_20260515T115944 | 两个 seed-42 实验同时 ~15s 崩溃，疑似同一根因\"}}, \"notes\": \"NEGATIVE: 稀疏性坍塌。Sparsity 0.328→0.000 (step 500+ 全 0)。根因: KL loss (收敛 3.3) 远大于 reg (0.05)，66 倍差距，fixed reg_weight=0.1 完全压不住。KL 最优解是 sparse=dense (0% sparsity)。修复: Lagrangian multiplier 自适应约束（Director 批准）。\", \"conclusion\": \"negative\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_kl_s42 --wandb_run_name mvp_kl_s42 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"53754\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_kl_s42.log\", \"submitted_at\": \"2026-05-15T12:37:15.045Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2424.9, \"gpu_hours\": 0.67}, \"pid\": \"53754\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_kl_s42.log\", \"metrics\": {\"final_total_loss\": 3.3438, \"final_kl_loss\": 3.2969, \"final_reg_loss\": 0.05, \"final_sparsity\": 0, \"steps\": 1000, \"tau_final\": 0.1, \"wikitext2_ppl_dense\": 6.12, \"wikitext2_ppl_sparse\": 455.93, \"wikitext2_ppl_increase_pct\": 7349, \"model_level_sparsity\": 0.372, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_kl_s42/predictor_kl.pt\"}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_kl_s42/predictor_kl.pt\", \"hypothesis\": \"Raw KL divergence loss 直接蒸馏 dense→sparse gate，结合固定 sparsity regularization (reg_weight=0.1)，能稳定收敛到目标 50% 稀疏度——如果 sparsity collapse 则说明 KL loss 量级远大于 reg 需要自适应平衡\"}, \"mistral_kl70_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T00:16:13.454Z\", \"updated_at\": \"2026-05-17T02:58:56.173Z\", \"hypothesis\": \"KL distillation predictor generalizes across architectures: Mistral-7B at 70% sparsity should show similar KL advantage over TEAL as LLaMA, validating cross-architecture claim\", \"spec\": {\"command\": \"train.py --loss_type kl_normalized --model_path /root/autodl-tmp/models/mistral-7b/ --target_sparsity 0.7 --num_steps 1000 --seed 42 --gpu 1\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"model_name\": \"mistral-7b-v0.3\", \"data_path\": \"WikiText-103 train\", \"data_count\": 0, \"seed\": 42, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mistral_kl70_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/logs/mistral_kl70_s42.log\"}, \"metrics\": {\"kl_per_token_ppl\": 9.1086, \"kl_teal_global_ppl\": 13.3254, \"teal_baseline_ppl\": 61.716, \"dense_ppl\": 5.5238, \"kl_advantage_ratio\": 6.77, \"final_loss\": 0.3945, \"actual_sparsity\": 0.682}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T01:16:50.764Z\", \"parent\": \"mistral_kl_s42\"}, \"mistral_kl30_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T00:16:12.670Z\", \"updated_at\": \"2026-05-17T02:58:55.221Z\", \"hypothesis\": \"KL distillation predictor generalizes across architectures: Mistral-7B at 30% sparsity should show similar KL advantage over TEAL as LLaMA, validating cross-architecture claim\", \"spec\": {\"command\": \"train.py --loss_type kl_normalized --model_path /root/autodl-tmp/models/mistral-7b/ --target_sparsity 0.3 --num_steps 1000 --seed 42 --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"model_name\": \"mistral-7b-v0.3\", \"data_path\": \"WikiText-103 train\", \"data_count\": 0, \"seed\": 42, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mistral_kl30_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/logs/mistral_kl30_s42.log\"}, \"metrics\": {\"kl_per_token_ppl\": 6.048, \"kl_teal_global_ppl\": 6.7733, \"teal_baseline_ppl\": 8.3807, \"dense_ppl\": 5.5238, \"kl_advantage_ratio\": 1.386, \"ppl_vs_dense_pct\": 9.5}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T01:16:49.881Z\", \"parent\": \"mistral_kl_s42\"}, \"plan_005_subsumption_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:20:21.300Z\", \"updated_at\": \"2026-05-17T02:58:53.349Z\", \"spec\": {\"command\": \"python src/subsumption_test.py --num_samples 50 --seq_len 2048\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"129873\", \"log_path\": \"~/runs/distill_sparse_swiglu/plan_005_subsumption_s42.log\", \"submitted_at\": \"2026-05-15T20:20:21.197Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 50, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_path\": \"results/subsumption_test/subsumption_results.json\", \"wall_clock_seconds\": 566.8, \"gpu_hours\": 0.16}, \"hypothesis\": \"验证 SPON bias correction 与 KL predictor mask 效应的关系：正交性、量级比、跨层非线性交互。结果支持 D010 \\\"marginal complement\\\" framing — SPON corrections are orthogonal and negligibly small (magnitude ratio 16%, cos_sim 0.20).\", \"metrics\": {\"linearity_ratio\": 0.2644, \"linearity_ratio_std\": 0.0073, \"magnitude_ratio\": 0.1578, \"magnitude_ratio_std\": 0.0088, \"cosine_similarity\": 0.1962, \"cosine_similarity_std\": 0.0268, \"predictor_effect_norm\": 482.65, \"spon_correction_norm\": 76.2, \"interaction_norm\": 147.74, \"num_samples\": 50, \"seq_len\": 2048, \"conclusion_type\": \"weak_subsumption\"}, \"conclusion\": \"success\", \"notes\": \"## Subsumption Test Results (50 samples, seq_len=2048)\\n\\n### 核心指标\\n- Linearity ratio: 0.264 ± 0.007 (cross-layer cascade non-linearity)\\n- Magnitude ratio: 0.158 ± 0.009 (SPON correction / predictor effect)\\n- Cosine similarity: 0.196 ± 0.027 (near-orthogonal)\\n\\n### Effect magnitudes\\n- ‖D(predictor)‖ = 482.65 (KL predictor logit shift)\\n- ‖D(SPON)‖ = 76.20 (SPON bias correction logit shift)\\n- ‖interaction‖ = 147.74 (cross-layer cascade non-linearity)\\n\\n### 结论：Informative — SPON corrections are orthogonal and negligibly small\\n\\n1. **SPON 与 mask 效应正交**：cos_sim ≈ 0.20，两种修正作用在不同维度\\n2. **SPON 量级微小**：仅为 predictor 效应的 16%（76 vs 483）\\n3. **逐层精确可加**：交互项（148）来源于跨层级联非线性（down_proj 是线性的，层内 mask+bias 严格可加），非层内交互\\n4. **支持 D010 \\\"marginal complement\\\" framing**：SPON 提供的是正交但微弱的补充，不构成有意义的 compositional gain\\n\\n⚠️ 不使用 \\\"subsumption\\\" 措辞——数据显示正交性而非包含关系。正确表述：SPON corrections are orthogonal to and much smaller than predictor mask effects; the non-zero interaction term arises from cross-layer cascading, not intra-layer coupling.\\n\\n### 产出文件\\nresults/subsumption_test/subsumption_results.json (15KB)\", \"completed_at\": \"2026-05-15T20:29:47.949Z\", \"parent\": \"spon_training\"}, \"eval_bce_v3_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:53:24.152Z\", \"updated_at\": \"2026-05-17T02:58:52.396Z\", \"hypothesis\": \"D031 eval: BCE iso-compute v3 评测——对比 KL predictor 在相同 sparsity (50%) 下的 PPL/TEAL，证明 KL 优势来自 loss 函数本身而非计算量差异 (Reviewer Concern #2 defense)\", \"spec\": {\"command\": \"evaluate.py PPL + benchmark_eval.py downstream\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"211431\", \"log_path\": \"~/runs/distill_sparse_swiglu/eval_bce_v3_s42.log\", \"submitted_at\": \"2026-05-16T05:55:21.920Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext2 + arc_challenge + winogrande + mmlu + gsm8k\", \"data_count\": 200, \"model_name\": \"llama-3.1-8b + bce_isocompute_v3 predictor\", \"seed\": 42, \"checkpoint_source\": \"bce_isocompute_v3_s42\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/results/benchmark/bce_isocompute_v3_s42/results.json\", \"wall_clock_seconds\": 7528.4, \"gpu_hours\": 2.09}, \"reproduce\": {\"finished_at\": \"2026-05-16T07:57:06.016Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T07:57:08.267902+00:00\"}]}, \"metrics\": {\"dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 22.51, \"teal_sparse_ppl\": 27.97, \"model_level_sparsity\": 0.5, \"arc_challenge_acc\": 0.2048, \"arc_challenge_acc_norm\": 0.2398, \"arc_challenge_acc_norm_stderr\": 0.0125, \"winogrande_acc\": 0.5059, \"winogrande_acc_stderr\": 0.0141, \"mmlu_acc\": 0.3002, \"mmlu_acc_stderr\": 0.0038, \"gsm8k_exact_match\": 0.0485, \"gsm8k_exact_match_strict\": 0.0425, \"gsm8k_exact_match_stderr\": 0.0059}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T08:00:50.289Z\", \"parent\": \"bce_isocompute_v3_s42\"}, \"lm_eval_teal_30pct\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:19:18.755Z\", \"updated_at\": \"2026-05-17T02:58:50.565Z\", \"hypothesis\": \"TEAL 30% training-free downstream eval — 与 KL 30% 对比，看 training-free baseline 在低 sparsity 下的 downstream 表现。配合 50% 数据点构建完整 sparsity-task tradeoff 曲线。\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 CUDA_VISIBLE_DEVICES=0 python -u src/lm_eval_teal.py --sparsity_target 0.3 --tasks arc_challenge,winogrande,mmlu,gsm8k --gpu 0 --output_path results/lm_eval_teal_30pct\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"194814\", \"log_path\": \"~/runs/distill_sparse_swiglu/lm_eval_teal_30pct.log\", \"submitted_at\": \"2026-05-16T10:55:00.000Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"meta-llama/Llama-3.1-8B\", \"seed\": 42, \"checkpoint_path\": \"N/A (training-free)\"}, \"metrics\": {\"arc_challenge\": {\"acc\": 0.3933, \"acc_norm\": 0.4155, \"acc_stderr\": 0.0143, \"acc_norm_stderr\": 0.0144}, \"winogrande\": {\"acc\": 0.6559, \"acc_stderr\": 0.0134}, \"mmlu\": {\"acc\": 0.3598, \"acc_stderr\": 0.004}, \"mmlu_stem\": {\"acc\": 0.313}, \"mmlu_humanities\": {\"acc\": 0.3305}, \"mmlu_social_sciences\": {\"acc\": 0.4108}, \"mmlu_other\": {\"acc\": 0.401}, \"gsm8k\": {\"exact_match_strict\": 0.0849, \"exact_match_flexible\": 0.0925, \"strict_stderr\": 0.0077, \"flexible_stderr\": 0.008}, \"actual_sparsity\": 0.3}, \"conclusion\": \"negative\", \"notes\": \"TEAL 30% vs KL 30% vs Dense (0-shot): ARC-c acc_norm: TEAL=0.4155 > KL=0.3737 (+4.2pp), Dense=0.5819. WinoGrande: TEAL=0.6559 < KL=0.6756 (-2.0pp), Dense=0.7814. MMLU: TEAL=0.3598 > KL=0.2874 (+7.2pp), Dense=0.6532. GSM8K strict: TEAL=0.0849 ≈ KL=0.0743 (+1.1pp), Dense=0.5004. TEAL 在知识密集型任务(ARC-c, MMLU)上显著优于 KL distill，但在推理任务(GSM8K)上两者都崩溃严重。整体仍远低于 Dense baseline，30% sparsity 对 downstream 损害巨大。\", \"completed_at\": \"2026-05-16T03:32:50.782Z\", \"parent\": \"lm_eval_teal_50pct\"}, \"lm_eval_kl_30pct_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:35:56.358Z\", \"updated_at\": \"2026-05-17T02:58:49.558Z\", \"hypothesis\": \"30% sparsity downstream eval (ARC-c, WinoGrande, MMLU, GSM8K) - 与 50% 对比看退化是否有梯度。决定论文是否能 claim \\\"30% 为推荐配置\\\"。\", \"spec\": {\"command\": \"python -u src/lm_eval_sparse.py --tasks arc_challenge,winogrande,mmlu,gsm8k --sparsity_target 0.3\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"191335\", \"log_path\": \"~/runs/distill_sparse_swiglu/lm_eval_kl_30pct_s42.log\", \"submitted_at\": \"2026-05-16T01:58:48.081Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"meta-llama/Llama-3.1-8B\", \"seed\": 42, \"wall_clock_seconds\": 3037.2, \"gpu_hours\": 0.84}, \"notes\": \"第一次提交 (PID 186674) 因 HF httpx \\\"Cannot send a request, client closed\\\" 失败，无输出。需设 HF_HUB_OFFLINE=1 重跑。\", \"reproduce\": {\"finished_at\": \"2026-05-16T02:46:54.414Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T02:46:56.057400+00:00\"}]}, \"metrics\": {\"arc_challenge_acc\": 0.3575, \"arc_challenge_acc_norm\": 0.3737, \"winogrande_acc\": 0.6756, \"mmlu_acc\": 0.2874, \"gsm8k_exact_match_strict\": 0.0743, \"gsm8k_exact_match_flexible\": 0.0781, \"actual_sparsity\": 0.3, \"model\": \"llama-3.1-8b\", \"condition\": \"kl_distill_30pct_sparsity_s42\", \"mmlu_stem_acc\": 0.2499, \"mmlu_social_sciences_acc\": 0.2896, \"mmlu_humanities_acc\": 0.2786, \"mmlu_other_acc\": 0.3363}, \"conclusion\": \"negative\", \"checkpoint_path\": \"results/lm_eval_kl_30pct/results.json\", \"completed_at\": \"2026-05-16T02:49:25.308Z\", \"parent\": \"lm_eval_kl_s42\"}, \"gsm8k_gen_compare\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:35:56.904Z\", \"updated_at\": \"2026-05-17T02:58:48.632Z\", \"hypothesis\": \"GSM8K 生成质量对比：dense vs KL sparse 50% greedy 生成 5-10 样本。判断退化是\\\"推理丧失（重复/无意义文本）\\\"还是\\\"仅数字算错\\\"。\", \"spec\": {\"command\": \"python src/gsm8k_gen_compare.py\", \"server\": \"westd-34887\", \"model_name\": \"Llama-3.1-8B\", \"data_path\": \"openai/gsm8k test split\", \"data_count\": 10, \"seed\": 42, \"description\": \"GSM8K generation quality comparison: dense vs KL sparse 50%\"}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/artifacts/gsm8k_gen_compare.txt\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-16T00:43:29.657Z\", \"notes\": \"## GSM8K 生成质量对比：Dense vs KL Sparse 50% (10 samples)\\n\\n### 结论：推理能力根本性丧失（模式 A），非仅数字算错\\n\\n| 维度 | Dense | Sparse 50% |\\n|------|-------|------------|\\n| 推理连贯性 | 多步推理，逻辑清晰 | 1-3 句后进入无限重复循环 |\\n| 正确答案 | 多数正确 | 0/10 |\\n| 重复退化 | 无 | 10/10 全部出现 |\\n| 拼写质量 | 正常 | 退化（crabs→crbs, skein→skeen）|\\n\\n### 退化模式\\nSparse 模型能生成与问题相关的开头（如 \\\"First, we need to know...\\\"），但随即进入同一句话的无限重复（15+ 次）。Sample 7 中正确算出 9×2=18，但无法继续推理。\\n\\n### 对论文的意义\\n50% sparsity 摧毁了深层推理能力。PPL-downstream disconnect 的机制：PPL 衡量 next-token 平均质量，repetition loop 的每个重复 token 仍有较高概率（模型\\\"自信地\\\"重复），但推理链断裂。\", \"parent\": \"lm_eval_kl_s42\"}, \"d030_kl40_uniform\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:18:45.733Z\", \"updated_at\": \"2026-05-17T02:58:48.163Z\", \"hypothesis\": \"D033: KL 40% sparsity with UNIFORM per-layer allocation — 定位 allocation 修复的精确 threshold。30% uniform MMLU=40.61%（修复有效），50% uniform MMLU=27.77%（修复失效）。40% 是 threshold 精确定位的关键数据点。\", \"notes\": \"Director 确认方案 B：训练专用 40% predictor（非复用 30%/50% predictor eval）。流程：train.py --sparsity_target 0.4 (1000步, ~45min) → evaluate.py --sparsity_target 0.4 + lm_eval downstream with uniform allocation。排在 BCE v3 完成后用同一张卡（cuda:1）。与 30%/50% 保持一致，每个 sparsity level 用专用 predictor。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && export WANDB_MODE=offline && echo '=== Phase 1: Train 40% KL predictor (1000 steps) ===' && python -u src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.4 --gpu 0 --output_dir checkpoints/kl_sparsity40_s42 --wandb_run_name d030_kl40_uniform --dataset wikitext-103 --gradient_checkpointing --lambda_max 5000 --log_every 100 2>&1 && echo '=== Phase 2: Evaluate with uniform allocation ===' && python -u src/benchmark_eval.py --exp_id d030_kl40_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity40_s42/predictor_kl_normalized.pt --sparsity_mode per_token --sparsity_target 0.4 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"215866\", \"log_path\": \"~/runs/distill_sparse_swiglu/d030_kl40_uniform.log\", \"submitted_at\": \"2026-05-16T07:01:57.183Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"checkpoints/kl_sparsity40_s42/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 8082.5, \"gpu_hours\": 2.25}, \"metrics\": {\"wikitext2_ppl\": 8.3627, \"arc_challenge_acc_norm\": 0.4181, \"winogrande_acc\": 0.6717, \"mmlu_acc\": 0.3068, \"gsm8k_exact_match\": 0.0394, \"actual_sparsity\": 0.398}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T09:16:39.695Z\", \"parent\": \"d030_kl30_uniform\"}, \"d030_kl50_uniform\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:30:55.969Z\", \"updated_at\": \"2026-05-17T02:58:47.243Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id d030_kl50_uniform --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"203702\", \"log_path\": \"~/runs/distill_sparse_swiglu/d030_kl50_uniform.log\", \"submitted_at\": \"2026-05-16T04:30:55.806Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 2309.5, \"gpu_hours\": 0.64}, \"hypothesis\": \"D030: KL 50% sparsity with UNIFORM per-layer allocation — 30% uniform 显示 MMLU +12pp 但 GSM8K 无恢复。50% 测试更高 sparsity 下 uniform 是否仍能部分修复知识类任务。\", \"reproduce\": {\"finished_at\": \"2026-05-16T05:02:36.667Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T05:02:41.980046+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.96, \"arc_challenge_acc_norm\": 0.3276, \"winogrande_acc\": 0.629, \"mmlu_acc\": 0.2777, \"gsm8k_exact_match\": 0.0212, \"actual_sparsity\": 0.5, \"allocation\": \"uniform\", \"per_layer_sparsity\": \"uniform 0.500 across all 32 layers\", \"mmlu_change_vs_global\": \"+1.86pp (0.2591 → 0.2777, not significant)\", \"gsm8k_change_vs_global\": \"+0.91pp (0.0121 → 0.0212, not significant)\", \"conclusion_note\": \"50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在 50% sparsity 下消失。\"}, \"checkpoint_path\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/results/d030_kl50_uniform/\", \"completed_at\": \"2026-05-16T05:09:25.315Z\", \"notes\": \"## D030 50% Uniform 结果\\n\\n50% uniform per-layer allocation 未能修复 downstream collapse。MMLU 0.2777（接近随机 0.25），GSM8K 0.0212，与 global top-k 的 0.2591/0.0121 几乎无差异。\\n\\n### 与 30% Uniform 对比\\n30% uniform 将 MMLU 从 0.2874 拉到 0.4061（+12pp），但 50% uniform 对 MMLU 仅 +1.86pp。说明 uniform allocation 的修复效应在 50% 下完全消失。\\n\\n### 结论\\n50% 是 downstream capability 的断崖点。无论 per-layer allocation 策略如何，50% sparsity 对 SwiGLU FFN 的知识检索和推理能力有根本性破坏。支撑 Narrative A（50% collapse is universal）。\\n\\n### 对论文的意义\\n- Claim 3 需要调整：30% 可以作为\\\"推荐配置\\\"叙述（PPL 8.82, MMLU 0.4061），但 50% 只能用于 PPL 场景\\n- 论文应报告 30% uniform 为 downstream-safe operating point\", \"parent\": \"d030_kl30_uniform\"}, \"bce_isocompute_v3_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T03:56:03.520Z\", \"updated_at\": \"2026-05-17T02:58:46.255Z\", \"hypothesis\": \"D031: BCE iso-compute 重跑（v1/v2 两次被 tmux 杀死）。2700 步匹配 KL 1000 步总 FLOPs (ratio≈2.71x)，50% sparsity。Reviewer Concern #2 defense: 验证 KL 优势来自 loss 函数本身而非计算量差异。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 nohup python -u src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 2700 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir checkpoints/bce_isocompute_v3_s42 --wandb_run_name bce_isocompute_v3_s42 --dataset wikitext-103 --gradient_checkpointing --log_every 100\", \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"pid\": 205598, \"log_path\": \"/root/distill_sparse_swiglu/logs/bce_isocompute_v3_s42.log\", \"data_path\": \"wikitext-103\", \"data_count\": null, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"backend\": \"nohup\", \"wrapper_pid\": 205597}, \"reproduce\": {\"finished_at\": \"2026-05-16T05:31:19.117Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T05:31:20.410Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T05:31:25.365333+00:00\"}]}, \"metrics\": {\"steps\": 2700, \"loss\": 0.6382, \"bce_loss\": 0.6371, \"reg_loss\": 0.001, \"sparsity\": 0.51, \"training_time_seconds\": 2828, \"note\": \"BCE saturation confirmed: step 500→2700 only 0.006 improvement\"}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/bce_isocompute_v3_s42/predictor_bce.pt\", \"parent\": \"bce_isocompute_v2_s42\"}, \"spon_2048_s42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T18:40:29.059Z\", \"updated_at\": \"2026-05-17T02:58:45.331Z\", \"completed_at\": \"2026-05-15T18:54:46.600Z\", \"failure_reason\": \"启动后崩溃，日志仅9行，停在 Setting up data loader... 待诊断\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:17:06.065446+00:00\"}]}, \"reproduce\": {\"finished_at\": \"2026-05-15T19:17:02.371Z\"}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/spon_2048_s42/spon_biases.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/spon_2048_s42.log\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train_spon.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --predictor_checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-5 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir checkpoints/spon_2048_s42 --warmup_steps 100 --log_every 100 --dataset wikitext-103 --gradient_checkpointing\\\"\", \"server\": \"westd-34887\", \"data_path\": \"wikitext-103 (HF cached)\", \"data_count\": null, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"mvp_kl_norm_v2_s42 predictor\", \"eval_data\": \"wikitext-2\"}, \"conclusion\": \"negative\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 9.2165, \"spon_sparse_ppl\": 8.991, \"spon_recovery_pct\": 7.3, \"ppl_improvement_from_spon\": 0.2255, \"mean_bias_norm\": 0.05312, \"max_bias_norm\": 0.065918, \"model_level_sparsity\": 0.498, \"eval_seq_len\": 2048, \"training_seq_len\": 2048, \"eval_samples\": 141, \"trainable_params\": 458752, \"trainable_pct\": 0.0057, \"training_steps\": 1000, \"final_loss\": 0.377, \"dense_with_spon_ppl\": 6.1823, \"dense_ppl_degradation\": 0.0651, \"teal_sparse_no_spon_ppl\": 12.0776, \"teal_sparse_with_spon_ppl\": 11.7907, \"spon_recovery_teal_pct\": 4.8, \"teal_sparsity\": 0.4979}, \"notes\": \"## SPON seq_len=2048 重训，消除 train/eval length mismatch confound\\n\\n### 训练概要\\n1000 steps 正常完成。Loss 从 0.41 下降到 0.38 区间后波动。Bias norm 从 0→0.053 在 step 700 饱和（vs seq_len=128 版的 0.041）。Seq_len=2048 训练使得 bias 学到更多信息（norm 更高 30%），但改善仍有限。\\n\\n### WikiText-2 评估 (seq_len=2048, 141 sequences)\\n- True Dense PPL: 6.12\\n- Predictor Hard Mask PPL (no SPON): 9.22 (+50.6%)\\n- SPON Sparse PPL: 8.99 (+46.9%)\\n- **SPON recovery: 7.3%** (0.23 PPL improvement)\\n\\n### 与 spon_training (seq_len=128) 对比\\n| 指标 | seq_len=128 | seq_len=2048 | 变化 |\\n|------|-------------|--------------|------|\\n| SPON recovery | 3.8% | 7.3% | +3.5pp |\\n| PPL improvement | 0.12 | 0.23 | +0.11 |\\n| mean_bias_norm | 0.041 | 0.053 | +30% |\\n| spon_sparse_ppl | 9.10 | 8.99 | -0.11 |\\n\\n### 结论: **Negative** (recovery 7.3% < 10% 阈值)\\n消除 seq_len mismatch 后 SPON recovery 从 3.8% 提升到 7.3%，说明 mismatch 确实是部分原因，但即使在匹配条件下 static bias 仍只能恢复不到 10% 的稀疏化误差。确认 D009 \\\"KL subsumes SPON\\\" reframe：KL predictor 的 per-token mask 已经很好地适应了重要 neuron，残余误差不是简单的 additive bias 能补偿的。\", \"parent\": \"spon_training\"}, \"kl_sparsity30_s42_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:09:36.571Z\", \"updated_at\": \"2026-05-17T02:58:44.374Z\", \"hypothesis\": \"KL distillation @ 30% sparsity, lambda_max=5000 (v2 lambda_max=1000 导致 sparsity 仅收敛到 0.281). Plan_008 sparsity sweep 30% 数据点重跑。\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 WANDB_MODE=offline python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.3 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s42_v3 --wandb_run_name kl_sparsity30_s42_v3 --dataset wikitext-103 --gradient_checkpointing --lambda_max 5000 --log_every 100\\\"\", \"server\": \"westd-34887\", \"data_path\": \"wikitext-103\", \"data_count\": 1000, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"plan_id\": \"plan_008\", \"lambda_max\": 5000, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\", \"log_path\": \"/root/runs/distill_sparse_swiglu/kl_sparsity30_s42_v3.log\"}, \"metrics\": {\"loss\": 0.165, \"kl_normalized\": 0.165, \"kl_raw\": 0.165, \"sparsity\": 0.285, \"lambda_sparse\": 5000, \"tau\": 0.1, \"constraint_loss\": 0, \"steps\": 1000, \"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 7.3, \"teal_sparse_ppl\": 8.98, \"teal_sparse_ppl_note\": \"已通过 eval_kl30_teal_30pct 独立验证 (sparsity_target=0.3, D034)\", \"model_level_sparsity\": 0.3, \"eval_dataset\": \"wikitext-2\", \"eval_seq_len\": 2048}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T22:13:55.789Z\", \"notes\": \"D016 决策：sparsity=0.285（target=0.30），lambda_max=5000 仍无法推到 target。Director 接受为实际数据点——predictor 在 ~28.5% 有自然下限，不再重跑。论文报 achieved sparsity 28.5%（不写 target 30%）。\\n\\n## PPL 评估（已修正，D034）\\n- predictor_hard_mask_ppl=7.30: per-token adaptive mask 评估值\\n- teal_sparse_ppl=8.98: 已通过 eval_kl30_teal_30pct 独立验证（sparsity_target=0.3）\\n- D032 曾误判原值 8.98 为\\\"Mistral 数据误拷\\\"，实际原值正确。13.63 是 evaluate.py 默认 sparsity_target=0.5 的结果（非 30% PPL）\\n\\nPer-layer sparsity: 早期层 0.13-0.23, 中间层 0.30-0.34, 后层 0.50-0.70。\", \"teal_sparse_ppl\": 13.63, \"parent\": \"kl_sparsity30_s42_v2\"}, \"steps_curve_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T23:53:44.668Z\", \"updated_at\": \"2026-05-16T23:57:45.934Z\", \"spec\": {\"command\": \"train.py --loss_type kl_normalized --num_steps 1000 --save_every 200\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"model_name\": \"llama-3.1-8b\", \"data_path\": \"WikiText-103 train\", \"data_count\": 0, \"seed\": 42, \"hypothesis\": \"KL predictor training converges within 600-800 steps, 1000 steps is sufficient and near-saturated\", \"checkpoint_path\": \"checkpoints/steps_curve_s42/\", \"log_path\": \"/root/runs/steps_curve_s42_v3.log\"}, \"metrics\": {\"step200_ppl\": 15.158, \"step400_ppl\": 12.538, \"step600_ppl\": 12.046, \"step800_ppl\": 11.907, \"step1000_ppl\": 11.906, \"convergence_step\": 800, \"ppl_800_vs_1000_delta\": 0.001}, \"conclusion\": \"success\", \"hypothesis\": \"KL predictor training converges within 600-800 steps; 1000 steps is sufficient and near-saturated performance\", \"completed_at\": \"2026-05-16T23:57:45.934Z\"}, \"tau_schedule_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T23:53:42.391Z\", \"updated_at\": \"2026-05-16T23:57:45.222Z\", \"spec\": {\"command\": \"train.py --loss_type kl_normalized --tau_start {0.5/0.1} --tau_end {0.5/0.1} --num_steps 1000\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"model_name\": \"llama-3.1-8b\", \"data_path\": \"WikiText-103 train\", \"data_count\": 0, \"seed\": 42, \"hypothesis\": \"Temperature schedule has minor impact on final PPL - method is robust to tau choice within reasonable range\", \"checkpoint_path\": \"checkpoints/tau_ablation_fixed{05,01}/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/logs/tau_ablation.log\"}, \"metrics\": {\"tau_linear_baseline_ppl\": 11.963, \"tau_fixed05_ppl\": 11.861, \"tau_fixed01_ppl\": 12.072, \"tau_fixed05_loss\": 0.248, \"tau_fixed01_loss\": 0.43, \"best_tau\": \"fixed_0.5\", \"ppl_range\": 0.211}, \"conclusion\": \"success\", \"hypothesis\": \"Temperature schedule has minor impact on final PPL - method is robust to tau choice within reasonable range (fixed 0.5 vs fixed 0.1 vs linear annealing)\", \"completed_at\": \"2026-05-16T23:57:45.222Z\"}, \"steps_curve_s42_v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"retry_count\": 0, \"created_at\": \"2026-05-16T22:15:19.436Z\", \"updated_at\": \"2026-05-16T22:15:19.436Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/distill_sparse_swiglu && export HF_DATASETS_OFFLINE=1 && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export WANDB_MODE=disabled && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/train.py --loss_type kl_normalized --num_steps 1000 --sparsity_target 0.5 --lr 1e-3 --seed 42 --gradient_checkpointing --gpu 0 --output_dir checkpoints/steps_curve_s42 --save_every 200\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"276223\", \"log_path\": \"~/runs/distill_sparse_swiglu/steps_curve_s42_v3.log\", \"submitted_at\": \"2026-05-16T22:15:18.899Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"steps_curve_s42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"retry_count\": 0, \"created_at\": \"2026-05-16T22:14:37.684Z\", \"updated_at\": \"2026-05-16T22:14:37.684Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/distill_sparse_swiglu && export HF_DATASETS_OFFLINE=1 && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/train.py --loss_type kl_normalized --num_steps 1000 --sparsity_target 0.5 --lr 1e-3 --seed 42 --gradient_checkpointing --gpu 0 --output_dir checkpoints/steps_curve_s42 --save_every 200\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"276024\", \"log_path\": \"~/runs/distill_sparse_swiglu/steps_curve_s42_v2.log\", \"submitted_at\": \"2026-05-16T22:14:37.474Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"steps_curve_s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"retry_count\": 0, \"created_at\": \"2026-05-16T22:13:36.875Z\", \"updated_at\": \"2026-05-16T22:13:36.875Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/distill_sparse_swiglu && export HF_DATASETS_OFFLINE=1 && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && CUDA_VISIBLE_DEVICES=1 python -u src/train.py --loss_type kl_normalized --num_steps 1000 --sparsity_target 0.5 --lr 1e-3 --seed 42 --gradient_checkpointing --gpu 0 --output_dir checkpoints/steps_curve_s42 --save_every 200\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/distill_sparse_swiglu/steps_curve_s42.log\", \"submitted_at\": \"2026-05-16T22:13:36.670Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"db_sensitivity_sweep\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T20:02:33.553Z\", \"updated_at\": \"2026-05-16T22:04:02.778Z\", \"spec\": {\"command\": \"bash /root/distill_sparse_swiglu/src/run_db_sweep.sh 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"model_name\": \"llama-3.1-8b\", \"data_path\": \"WikiText-103 train\", \"data_count\": 0, \"seed\": 42, \"hypothesis\": \"Predictor bottleneck dimension d_b has low sensitivity to final PPL, justifying default d_b=128 choice\", \"checkpoint_path\": \"checkpoints/db_sweep_{64,256,512}/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/logs/db_sweep.log\"}, \"metrics\": {\"db64_per_token_ppl\": 10.158, \"db64_teal_global_ppl\": 12.076, \"db64_sparsity\": 0.5, \"db64_loss\": 0.361, \"db128_teal_global_ppl\": 11.963, \"db128_per_token_ppl\": 9.218, \"db256_per_token_ppl\": 8.586, \"db256_teal_global_ppl\": 12.105, \"db256_sparsity\": 0.5, \"db256_loss\": 0.27, \"db512_per_token_ppl\": 7.933, \"db512_teal_global_ppl\": 12.315, \"db512_sparsity\": 0.5, \"db512_loss\": 0.224, \"best_teal_global_db\": 128, \"best_teal_global_ppl\": 11.963}, \"conclusion\": \"success\", \"hypothesis\": \"Predictor bottleneck dimension d_b has low sensitivity to teal_global PPL across 4x range (64-512), justifying d_b=128 as default without hyperparameter tuning\", \"completed_at\": \"2026-05-16T22:04:02.778Z\"}, \"longbench_kl30_uniform_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:22:55.841Z\", \"updated_at\": \"2026-05-16T17:00:25.982Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export PYTHONUNBUFFERED=1 && export WANDB_MODE=offline && python -u src/benchmark_eval.py --exp_id longbench_kl30_uniform_v2 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"234888\", \"log_path\": \"~/runs/distill_sparse_swiglu/longbench_kl30_uniform_v2.log\", \"submitted_at\": \"2026-05-16T13:23:06.466Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 13039.5, \"gpu_hours\": 3.62}, \"conclusion\": \"failed\", \"notes\": \"OOM: 两个进程争抢同一 GPU + 无 flash-attn 导致内存溢出\", \"completed_at\": \"2026-05-16T17:00:25.982Z\"}, \"longbench_dense_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:22:57.327Z\", \"updated_at\": \"2026-05-16T17:00:25.298Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export PYTHONUNBUFFERED=1 && export WANDB_MODE=offline && python -u src/benchmark_eval.py --exp_id longbench_dense_v2 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --dense --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"235029\", \"log_path\": \"~/runs/distill_sparse_swiglu/longbench_dense_v2.log\", \"submitted_at\": \"2026-05-16T13:23:09.454Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 13035.8, \"gpu_hours\": 3.62}, \"conclusion\": \"failed\", \"notes\": \"OOM: 两个进程争抢同一 GPU + 无 flash-attn 导致内存溢出\", \"completed_at\": \"2026-05-16T17:00:25.298Z\"}, \"longbench_kl30_uniform_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:32:56.949Z\", \"updated_at\": \"2026-05-16T17:00:24.335Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export PYTHONUNBUFFERED=1 && export WANDB_MODE=offline && python -u src/benchmark_eval.py --exp_id longbench_kl30_uniform_v3 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"236025\", \"log_path\": \"~/runs/distill_sparse_swiglu/longbench_kl30_uniform_v3.log\", \"submitted_at\": \"2026-05-16T13:33:10.304Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12434.0, \"gpu_hours\": 3.45}, \"conclusion\": \"failed\", \"notes\": \"OOM: 单卡无法处理 32k token LongBench 文档，需要 2 卡 tensor parallel\", \"completed_at\": \"2026-05-16T17:00:24.335Z\"}, \"longbench_dense_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:32:58.232Z\", \"updated_at\": \"2026-05-16T17:00:23.387Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export PYTHONUNBUFFERED=1 && export WANDB_MODE=offline && python -u src/benchmark_eval.py --exp_id longbench_dense_v3 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --dense --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"236168\", \"log_path\": \"~/runs/distill_sparse_swiglu/longbench_dense_v3.log\", \"submitted_at\": \"2026-05-16T13:33:13.165Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12430.2, \"gpu_hours\": 3.45}, \"conclusion\": \"failed\", \"notes\": \"OOM: 单卡无法处理 32k token LongBench 文档，需要 2 卡 tensor parallel\", \"completed_at\": \"2026-05-16T17:00:23.387Z\"}, \"longbench_dense_v5\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:45:44.157Z\", \"updated_at\": \"2026-05-16T14:45:11.139Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export PYTHONUNBUFFERED=1 && export WANDB_MODE=offline && export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True && python -u src/benchmark_eval.py --exp_id longbench_dense_v5 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --dense --multi_gpu --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"237289\", \"log_path\": \"~/runs/distill_sparse_swiglu/longbench_dense_v5.log\", \"submitted_at\": \"2026-05-16T13:45:43.972Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\", \"notes\": \"LongBench 正式放弃（Director 决策）。5 次 OOM 失败，物理内存不可解。论文不纳入 LongBench。\"}, \"longbench_dense_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:40:39.061Z\", \"updated_at\": \"2026-05-16T13:44:29.665Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export PYTHONUNBUFFERED=1 && export WANDB_MODE=offline && python -u src/benchmark_eval.py --exp_id longbench_dense_v4 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --dense --multi_gpu --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"236858\", \"log_path\": \"~/runs/distill_sparse_swiglu/longbench_dense_v4.log\", \"submitted_at\": \"2026-05-16T13:40:47.623Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 222.0, \"gpu_hours\": 0.12}, \"conclusion\": \"failed\", \"notes\": \"OOM: CUDA 内存碎片化（reserved 17.98GB > requested 13.98GB），非绝对容量不足。需加 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True\", \"completed_at\": \"2026-05-16T13:44:29.665Z\"}, \"longbench_dense\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:57:41.121Z\", \"updated_at\": \"2026-05-16T13:21:12.937Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id longbench_dense --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --dense --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"233330\", \"log_path\": \"~/runs/distill_sparse_swiglu/longbench_dense.log\", \"submitted_at\": \"2026-05-16T13:01:46.958Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"longbench\", \"data_count\": 0, \"seed\": 42, \"eval_data\": \"longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news\", \"wall_clock_seconds\": 1160.1, \"gpu_hours\": 0.32}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T13:21:07.075Z\", \"notes\": \"HF_HUB_OFFLINE=1 + 数据未缓存导致下载失败\"}, \"longbench_kl30_uniform\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:57:39.563Z\", \"updated_at\": \"2026-05-16T13:21:12.363Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id longbench_kl30_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"233187\", \"log_path\": \"~/runs/distill_sparse_swiglu/longbench_kl30_uniform.log\", \"submitted_at\": \"2026-05-16T13:01:44.138Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"longbench\", \"data_count\": 0, \"seed\": 42, \"checkpoint_source\": \"checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\", \"eval_data\": \"longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news\", \"wall_clock_seconds\": 1162.3, \"gpu_hours\": 0.32}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T13:21:06.425Z\", \"notes\": \"HF_HUB_OFFLINE=1 + 数据未缓存导致下载失败\"}, \"bench_mistral_kl50_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:22:12.157Z\", \"updated_at\": \"2026-05-16T05:23:45.617Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id bench_mistral_kl50_s42 --model_name_or_path /root/autodl-tmp/models/mistral-7b --checkpoint checkpoints/mistral_kl_s42/predictor_kl_normalized.pt --sparsity_mode per_token --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"207957\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_mistral_kl50_s42.log\", \"submitted_at\": \"2026-05-16T05:11:11.758Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 192.5, \"gpu_hours\": 0.05}, \"hypothesis\": \"D029: Mistral KL 50% sparsity — benchmark_eval.py 统一 few-shot 评测 (ARC-c=25, WG=5, MMLU=5, GSM8K=8)。与 lm_eval_mistral_kl_50pct (0-shot) 对比，确保评测一致性。\", \"conclusion\": \"killed\", \"notes\": \"D034 修正：PID 207962 实际仍在 cuda:0 运行。之前 registry 误标为 killed（Director 优先级调整时标记，但进程未被实际终止）。等完成后更新实际结果。\", \"gpu\": \"cuda:0\", \"server\": \"westd-34887\", \"account\": \"root\", \"pid\": \"207957\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_mistral_kl50_s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id bench_mistral_kl50_s42 --model_name_or_path /root/autodl-tmp/models/mistral-7b --checkpoint checkpoints/mistral_kl_s42/predictor_kl_normalized.pt --sparsity_mode per_token --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\\\"\"}, \"completed_at\": \"2026-05-16T05:14:24.251Z\"}, \"lm_eval_teal_50pct\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:35:57.527Z\", \"updated_at\": \"2026-05-16T04:52:09.866Z\", \"hypothesis\": \"TEAL 50% training-free sparse downstream eval - 判断 downstream 崩溃是否为所有 50% sparsity 方法的固有限制，而非 KL predictor 特有问题。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 python -u src/lm_eval_teal.py --sparsity_target 0.5 --tasks arc_challenge,winogrande,mmlu,gsm8k --output_path results/lm_eval_teal_50pct\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"190830\", \"log_path\": \"~/runs/distill_sparse_swiglu/lm_eval_teal_50pct.log\", \"submitted_at\": \"2026-05-16T01:58:07.000Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2215.3, \"gpu_hours\": 0.62}, \"notes\": \"TEAL 50% downstream 结果确认 collapse 是 universal：\\n\\n| Task | TEAL 50% | KL 50% | Dense | TEAL drop | KL drop |\\n|------|----------|--------|-------|-----------|---------|\\n| arc_challenge (acc_norm) | 0.2910 | 0.3771 | 0.5819 | -50.0% | -35.2% |\\n| winogrande (acc) | 0.5556 | 0.6156 | 0.7814 | -28.9% | -21.2% |\\n| mmlu (acc) | 0.2856 | 0.2591 | 0.6532 | -56.3% | -60.3% |\\n| gsm8k (flexible-extract) | 0.0190 | 0.0121 | 0.5004 | -96.2% | -97.6% |\\n\\n关键发现：\\n1. TEAL 和 KL 在 MMLU/GSM8K 上均出现灾难性崩溃（接近随机水平），证明 50% sparsity downstream collapse 不是 KL predictor 特有问题\\n2. TEAL 在 ARC/WinoGrande 上甚至比 KL 更差（TEAL drop -50%/-29% vs KL drop -35%/-21%），说明 training-free 方法在简单 task 上也不如 learned predictor\\n3. MMLU/GSM8K 两者均近随机（MMLU ~0.25-0.29 = 4-choice random level），collapse 程度相当\\n4. 结论：50% unstructured sparsity 对 SwiGLU FFN 的 downstream capability 有根本性破坏，与 sparsity 选择方法无关\", \"reproduce\": {\"finished_at\": \"2026-05-16T02:32:09.806Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T02:32:11.809131+00:00\"}]}, \"metrics\": {\"method\": \"vanilla_teal\", \"sparsity\": 0.5, \"actual_sparsity\": 0.5, \"arc_challenge_acc_norm\": 0.291, \"winogrande_acc\": 0.5556, \"mmlu_acc\": 0.2856, \"gsm8k_exact_match_flexible\": 0.019, \"gsm8k_exact_match_strict\": 0.0114, \"arc_challenge_drop_vs_dense\": -0.5, \"winogrande_drop_vs_dense\": -0.289, \"mmlu_drop_vs_dense\": -0.563, \"gsm8k_drop_vs_dense\": -0.962, \"model\": \"Llama-3.1-8B\", \"condition\": \"TEAL 50% training-free sparsity\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval experiment, TEAL training-free)\", \"log_path\": \"~/runs/distill_sparse_swiglu/lm_eval_teal_50pct.log\", \"completed_at\": \"2026-05-16T02:35:02.296Z\", \"model\": \"Llama-3.1-8B\"}, \"d030_kl30_uniform\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T03:53:01.230Z\", \"updated_at\": \"2026-05-16T04:34:08.796Z\", \"hypothesis\": \"D030: KL 30% sparsity with UNIFORM per-layer allocation — 验证 global top-k 的 per-layer 不均匀是否是 downstream 崩溃的根因。对比 global top-k 的 MMLU 28.74%/GSM8K 7.43%。\", \"spec\": {\"checkpoint_path\": \"checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/d030_kl30_uniform.log\"}, \"plan_id\": \"plan_008\", \"reproduce\": {\"finished_at\": \"2026-05-16T04:27:03.930Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T04:27:05.705355+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 8.8157, \"arc_challenge_acc_norm\": 0.4078, \"winogrande_acc\": 0.6859, \"mmlu_acc\": 0.4061, \"gsm8k_exact_match\": 0.0735, \"actual_sparsity\": 0.3, \"allocation\": \"uniform\", \"per_layer_sparsity\": \"uniform 0.301 across all 32 layers\", \"mmlu_improvement_vs_global\": \"+11.87pp (0.2874 → 0.4061)\", \"gsm8k_change_vs_global\": \"no change (0.0743 → 0.0735, within noise)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T04:30:47.204Z\"}, \"mistral_kl_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:12:33.050Z\", \"updated_at\": \"2026-05-16T04:27:36.290Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 WANDB_MODE=offline python src/train.py --model_name_or_path /root/autodl-tmp/models/mistral-7b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mistral_kl_s42 --wandb_run_name mistral_kl_s42 --dataset wikitext-103 --gradient_checkpointing --log_every 100 2>&1 | tee ~/runs/distill_sparse_swiglu/mistral_kl_s42.log\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"147627\", \"log_path\": \"~/runs/distill_sparse_swiglu/mistral_kl_s42.log\", \"submitted_at\": \"2026-05-15T22:12:32.930Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": null, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mistral_kl_s42/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 2579.6, \"gpu_hours\": 0.72}, \"hypothesis\": \"Mistral-7B-v0.3 跨架构验证：KL normalized loss @ 50% sparsity。验证 KL distillation 方法在非 Llama 架构上也有效。Plan_009 第一个实验。\", \"reproduce\": {\"finished_at\": \"2026-05-15T22:49:21.591Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:49:26.713271+00:00\"}]}, \"metrics\": {\"train_final_loss\": 0.2188, \"train_final_kl_raw\": 0.2188, \"train_final_kl_norm\": 0.2188, \"train_final_constraint\": 0, \"train_final_sparsity\": 0.48, \"train_final_lambda\": 1000, \"train_final_tau\": 0.1, \"train_steps_completed\": 1000, \"true_dense_ppl\": 5.52, \"predictor_hard_mask_ppl\": 7.3, \"teal_sparse_ppl\": 8.98, \"model_level_sparsity\": 0.5, \"eval_dataset\": \"wikitext-2\", \"eval_seq_len\": 2048, \"calibration_samples\": 32, \"eval_samples\": 159}, \"notes\": \"teal_sparse_ppl=8.98 已通过原始日志验证 (eval_mistral_kl_s42.log)，模型=mistral-7b, predictor=predictor_kl_normalized.pt, sparsity=0.5，三项指标均与日志一致 [2026-05-16 D032交叉验证]\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T22:55:32.556Z\"}, \"kl_lagrangian_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:34:10.257Z\", \"updated_at\": \"2026-05-16T03:08:33.111Z\", \"spec\": {\"hypothesis\": \"Lagrangian v2: lambda_init=50 + 2x update rate, 解决 KL/constraint 3 个数量级尺度差\", \"loss_type\": \"kl_lagrangian_v2\", \"seed\": 42, \"model\": \"Llama-3.1-8B\", \"sparsity\": 0.5, \"steps\": 200, \"batch_size\": 4, \"seq_len\": 2048, \"gpu\": \"cuda:0\", \"server\": \"westd-34887\", \"parent\": \"kl_lagrangian_quicktest\"}, \"notes\": \"取消: Director 改为方案 C（KL 归一化 + Lagrangian），v2 仅调参数不够。新实验 kl_normalized_quicktest 替代。\", \"conclusion\": \"killed\"}, \"kl_norm_v3_quicktest\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:16:56.462Z\", \"updated_at\": \"2026-05-16T03:08:32.570Z\", \"spec\": {\"hypothesis\": \"修复 ÷vocab_size bug 后, KL 归一化仅 ÷seq_len, kl_raw 应下降且 sparsity 收敛\", \"loss_type\": \"kl_normalized_v3\", \"seed\": 42, \"model\": \"Llama-3.1-8B\", \"model_name\": \"llama-3.1-8b\", \"sparsity\": 0.5, \"steps\": 200, \"batch_size\": 4, \"seq_len\": 2048, \"gpu\": \"cuda:0\", \"server\": \"westd-34887\", \"parent\": \"kl_normalized_quicktest\", \"data_path\": \"wikitext-103 (HF cached)\", \"command\": \"PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --loss_type kl_normalized --num_steps 200 --batch_size 4 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir checkpoints/kl_norm_v3_quicktest\", \"kl_normalization\": \"÷seq_len only (fixed: removed ÷vocab_size from train.py)\", \"lagrangian\": \"lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]\"}, \"conclusion\": \"killed\", \"metrics\": {\"step1_kl_raw\": 1.1797, \"step1_kl_norm\": 1.1797, \"step1_sparsity\": 0.406, \"step1_lambda\": 2, \"step50_kl_raw\": 0.7344, \"step50_kl_norm\": 0.7344, \"step50_sparsity\": 0.514, \"step50_lambda\": 1.95, \"step100_kl_raw\": 0.625, \"step100_kl_norm\": 0.625, \"step100_sparsity\": 0.496, \"step100_lambda\": 1000, \"step150_kl_raw\": 0.5703, \"step150_kl_norm\": 0.5703, \"step150_sparsity\": 0.48, \"step150_lambda\": 1000, \"step200_kl_raw\": 0.6836, \"step200_kl_norm\": 0.6836, \"step200_sparsity\": 0.477, \"step200_lambda\": 1000, \"step200_constraint\": 0.01178, \"kl_trend\": \"decreasing (1.18→0.57 min, uptick to 0.68 at end)\", \"sparsity_range\": \"0.477-0.514 after step 50\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_norm_v3_quicktest/predictor_kl_normalized.pt\"}, \"notes\": \"PASS: Bug 修复后 kl_norm = kl_raw (仅保留 losses.py 的 ÷seq_len)。KL 从 1.18 下降到 0.57(step150)，sparsity 收敛到 0.477-0.514。Lambda 到 1000 cap 是因为 sparsity 在 margin 边界(0.477-0.484 < target-0.02=0.48)。注意: step 200 KL 略回升到 0.68(lr 接近 0 + tau=0.1 硬化)。\"}, \"mvp_kl_norm_s456\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:30:12.769Z\", \"updated_at\": \"2026-05-16T03:08:31.529Z\", \"spec\": {\"hypothesis\": \"Normalized KL (÷seq_len) + Lagrangian 约束在 1000 步完整训练下产生优于 BCE 的稀疏预测器\", \"loss_type\": \"kl_normalized\", \"seed\": 456, \"model\": \"Llama-3.1-8B\", \"model_name\": \"llama-3.1-8b\", \"sparsity\": 0.5, \"steps\": 1000, \"batch_size\": 4, \"seq_len\": 2048, \"server\": \"westd-34887\", \"parent\": \"kl_normalized_quicktest\", \"data_path\": \"wikitext-103 (HF cached)\", \"kl_normalization\": \"÷seq_len only\", \"lagrangian\": \"lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]\"}, \"conclusion\": \"killed\"}, \"spon_kl_s42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:27:18.621Z\", \"updated_at\": \"2026-05-16T03:08:30.602Z\", \"spec\": {\"hypothesis\": \"SPON learnable bias vectors + KL loss 在 50% sparsity 下补偿稀疏化误差，复现论文效果并为 plan_005 组合实验铺路\", \"loss_type\": \"kl_spon\", \"seed\": 42, \"model_name\": \"llama-3.1-8b\", \"sparsity\": 0.5, \"server\": \"westd-34887\", \"parent\": \"mvp_kl_norm_v2_s42\", \"data_path\": \"wikitext-103 (HF cached)\"}, \"conclusion\": \"killed\"}, \"diag_30pct_downstream\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:34:04.456Z\", \"updated_at\": \"2026-05-16T03:08:29.808Z\", \"spec\": {\"hypothesis\": \"50% sparsity 导致 downstream 崩溃是梯度断崖还是渐进退化？30% sparse model 如果保持合理 downstream → 确认 50% 是断崖点；如果也崩 → 问题更根本\", \"model_name\": \"meta-llama/Llama-3.1-8B + KL predictor 30% sparse\", \"checkpoint_source\": \"/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\", \"eval_data\": \"arc_challenge, winogrande, mmlu, gsm8k\", \"server\": \"westd-34887\", \"seed\": 42, \"parent\": \"kl_sparsity30_s42_v3\"}, \"conclusion\": \"killed\"}, \"diag_gsm8k_gencomp\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:34:07.736Z\", \"updated_at\": \"2026-05-16T03:08:29.420Z\", \"spec\": {\"hypothesis\": \"稀疏模型 GSM8K 退化是推理能力丧失（输出无意义/重复）还是仅格式错误（推理正确但答案格式不匹配）？\", \"model_name\": \"meta-llama/Llama-3.1-8B dense vs KL sparse 50%\", \"eval_data\": \"GSM8K 5-10 samples, greedy generation\", \"server\": \"westd-34887\", \"seed\": 42, \"parent\": \"lm_eval_kl_s42\"}, \"notes\": \"10 GSM8K samples compared (dense vs KL sparse 50% TEAL). Sparse model suffers FUNDAMENTAL reasoning collapse: (1) 10/10 samples degenerate into repetitive loops within 1-3 sentences; (2) no sample produces correct final answer or completes multi-step reasoning; (3) sparse model can generate topically relevant opening text but immediately enters infinite repetition (e.g. \\\"We can then use the formula...\\\" repeated 15+ times); (4) occasional partial correctness in first sentence (Sample 7: correctly computes 9*2=18 but never adds +3); (5) spelling degradation observed (crabs→crbs, skein→skeen). Dense model generates coherent step-by-step reasoning and often reaches correct answers. Conclusion: GSM8K score of 0.0121 is NOT caused by answer extraction/format mismatch — it reflects genuine loss of reasoning and generation ability under 50% TEAL sparsity with KL-trained predictor.\", \"conclusion\": \"killed\"}, \"diag_teal_downstream\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:34:11.737Z\", \"updated_at\": \"2026-05-16T03:08:28.224Z\", \"spec\": {\"hypothesis\": \"TEAL 50% sparse 是否也出现同样的 downstream 崩溃？如果是 → 50% sparsity 固有限制，KL 的 PPL 优势仍有论文价值；如果否 → KL predictor 引入了额外退化\", \"model_name\": \"meta-llama/Llama-3.1-8B + TEAL 50% sparse (training-free)\", \"eval_data\": \"arc_challenge, winogrande, mmlu, gsm8k\", \"server\": \"westd-34887\", \"seed\": 42, \"parent\": \"training_free_baselines\"}, \"conclusion\": \"killed\"}, \"bce_isocompute_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:47:02.076Z\", \"updated_at\": \"2026-05-16T02:24:56.731Z\", \"spec\": {\"command\": \"python src/train.py --loss_type bce --num_steps 2700 --sparsity_target 0.5\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"123984\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_isocompute_s42_v2.log\", \"submitted_at\": \"2026-05-15T19:47:01.988Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 0, \"model_name\": \"meta-llama/Llama-3.1-8B\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 23874.7, \"gpu_hours\": 6.63}, \"hypothesis\": \"BCE 在等量 FLOPs (2700 步 vs KL 1000 步, ratio=2.71x) 下是否能缩小与 KL 的 PPL 差距？如果不能，说明 KL 的优势来自 loss 函数本身而非计算量（Reviewer Concern #2 defense）。[Retry of bce_isocompute_s42 which crashed at step 500]\", \"notes\": \"PID 123984 已死亡（v2 重试也失败）。tmux session 再次被外部终止，与 v1 相同模式。BCE iso-compute 实验需要在清空 GPU 后单独重跑。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T02:24:56.731Z\"}, \"eval_spon_supp_retry\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:44:22.659Z\", \"updated_at\": \"2026-05-16T02:24:55.659Z\", \"spec\": {\"command\": \"python src/eval_spon_supplementary.py --gpu 0 --seq_len 2048\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"123231\", \"log_path\": \"~/runs/distill_sparse_swiglu/eval_spon_supp_retry.log\", \"submitted_at\": \"2026-05-15T19:44:22.577Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"spon eval\", \"data_count\": 0, \"model_name\": \"meta-llama/Llama-3.1-8B\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 24033.1, \"gpu_hours\": 6.68}, \"conclusion\": \"failed\", \"notes\": \"PID 123231 已死亡。SPON 补充 eval，tmux session 消失，被后续实验覆盖。\", \"completed_at\": \"2026-05-16T02:24:55.659Z\"}, \"lm_eval_dense_test\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:30:54.405Z\", \"updated_at\": \"2026-05-16T02:24:54.247Z\", \"spec\": {\"command\": \"python src/benchmark_eval.py --dense --tasks arc_challenge\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"153249\", \"log_path\": \"~/runs/distill_sparse_swiglu/lm_eval_dense_test.log\", \"submitted_at\": \"2026-05-15T22:30:54.294Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"arc_challenge\", \"data_count\": 0, \"model_name\": \"meta-llama/Llama-3.1-8B\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 14040.0, \"gpu_hours\": 3.9}, \"conclusion\": \"failed\", \"notes\": \"PID 153249 已死亡。早期探索性 eval，tmux session 消失，被后续实验覆盖。\", \"completed_at\": \"2026-05-16T02:24:54.247Z\"}, \"lm_eval_mistral_downstream\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:34:22.527Z\", \"updated_at\": \"2026-05-16T02:24:53.274Z\", \"spec\": {\"command\": \"python -u src/eval_benchmark.py --condition mistral_kl_s42 --tasks lm_eval\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"174840\", \"log_path\": \"~/runs/distill_sparse_swiglu/lm_eval_mistral_downstream.log\", \"submitted_at\": \"2026-05-15T23:34:22.413Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"lm_eval benchmarks\", \"data_count\": 0, \"model_name\": \"mistralai/Mistral-7B\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 10230.9, \"gpu_hours\": 2.84}, \"conclusion\": \"failed\", \"notes\": \"PID 174840 已死亡（进程不存在）。被后续实验 lm_eval_teal_50pct 占用 cuda:1 时挤掉，tmux session 消失。\", \"completed_at\": \"2026-05-16T02:24:53.274Z\"}, \"mvp_kl_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:51:00.876Z\", \"updated_at\": \"2026-05-16T02:23:07.388Z\", \"spec\": {\"hypothesis\": \"KL-trained predictor captures joint neuron interactions via end-to-end gradient flow, outperforming BCE at 50% sparsity\", \"loss_type\": \"kl\", \"seed\": 123, \"model\": \"Llama-3.1-8B\", \"sparsity\": 0.5, \"steps\": 1000, \"batch_size\": 4, \"seq_len\": 2048, \"gpu\": \"cuda:0\", \"server\": \"westd-34887\", \"eval\": \"WikiText-2 + C4 perplexity\", \"checkpoint_path\": \"N/A (killed)\", \"log_path\": \"N/A\"}, \"notes\": \"Killed: 使用旧 KL 配置（无归一化），已被 mvp_kl_norm_s123 替代。参见 kl_normalized_quicktest 验证 seq_len-only 归一化有效。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T02:23:07.388Z\"}, \"mvp_kl_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:51:02.768Z\", \"updated_at\": \"2026-05-16T02:23:06.464Z\", \"spec\": {\"hypothesis\": \"KL-trained predictor captures joint neuron interactions via end-to-end gradient flow, outperforming BCE at 50% sparsity\", \"loss_type\": \"kl\", \"seed\": 456, \"model\": \"Llama-3.1-8B\", \"sparsity\": 0.5, \"steps\": 1000, \"batch_size\": 4, \"seq_len\": 2048, \"gpu\": \"cuda:0\", \"server\": \"westd-34887\", \"eval\": \"WikiText-2 + C4 perplexity\", \"checkpoint_path\": \"N/A (killed)\", \"log_path\": \"N/A\"}, \"conclusion\": \"killed\", \"notes\": \"Killed: 使用旧 KL 配置（无归一化），已被 mvp_kl_norm_s456 替代。参见 kl_normalized_quicktest 验证 seq_len-only 归一化有效。\", \"completed_at\": \"2026-05-16T02:23:06.464Z\"}, \"bce_isocompute_v2_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:01:43.104Z\", \"updated_at\": \"2026-05-15T21:11:42.245Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 1000 --warmup_steps 100 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --sparsity_reg_weight 2.0 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/bce_isocompute_v2_s42 --gradient_checkpointing --log_every 100 --save_every 250 --wandb_run_name bce_isocompute_v2_s42\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"129182\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_isocompute_v2_s42.log\", \"submitted_at\": \"2026-05-15T20:16:10.918Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1727.3, \"gpu_hours\": 0.48}, \"hypothesis\": \"BCE 在 iso-compute (1000 steps) + iso-sparsity (STE reg_weight=2.0 使 sparsity 收敛到 ~0.50) 下是否能缩小与 KL 的 PPL 差距？消除 compute 和 sparsity 两个 confound。\", \"notes\": \"## Eval Results (2026-05-16)\\n- true_dense_ppl: 6.12\\n- predictor_hard_mask_ppl: 26.76\\n- teal_sparse_ppl: 54.84\\n- sparsity_target: 0.50 (converged correctly, STE fix worked)\\n\\n## Training Summary\\n- 1000 steps, 1048s (1.05s/step), EXIT_CODE=0\\n- BCE loss: 0.6714 → 0.6586 (only 5% better than random 0.693)\\n- Reg loss: 0.0171 → 0.0051 (sparsity converged to 0.50)\\n- reg_weight=2.0, Gumbel-sigmoid STE\\n\\n## Comparison with KL Baseline\\n- KL normalized (50% sparsity, 4-seed mean): teal_sparse_ppl = 12.00 ± 0.07\\n- BCE v2: teal_sparse_ppl = 54.84 — 4.6x worse than KL\\n\\n## Conclusion\\nBCE + STE dramatically underperforms KL at 50% sparsity under iso-compute (1000 steps). BCE treats each neuron as an independent binary classification, losing inter-neuron coordination and output distribution signal. The predictor barely learned meaningful patterns (BCE only 5% better than random). KL's direct output-distribution matching provides much stronger learning signal. BCE is not a viable alternative loss for sparsity predictor training.\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/bce_isocompute_v2_s42/\", \"metrics\": {\"final_loss\": 0.6637, \"final_bce_loss\": 0.6586, \"final_reg_loss\": 0.0051, \"final_sparsity\": 0.502, \"training_steps\": 1000, \"training_time_sec\": 1047.8, \"reg_weight\": 2, \"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 26.76, \"teal_sparse_ppl\": 54.84, \"eval_seq_len\": 2048, \"eval_dataset\": \"wikitext-2\"}, \"completed_at\": \"2026-05-15T20:44:58.239Z\"}, \"kl_sparsity70_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:24:08.219Z\", \"updated_at\": \"2026-05-15T20:35:03.728Z\", \"spec\": {\"hypothesis\": \"KL distillation @ 70% sparsity (aggressive pruning). Part of plan_008 3-level sparsity sweep (30/50/70%). Expect larger PPL increase than 50% but KL should maintain advantage over BCE. Paired with kl_sparsity30_s42.\", \"command\": \"CUDA_VISIBLE_DEVICES=1 bash -c 'source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=offline python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.7 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/kl_sparsity70_s42 --wandb_run_name kl_sparsity70_s42 --dataset wikitext-103'\", \"server\": \"westd-34887\", \"data_path\": \"wikitext-103\", \"data_count\": -1, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"plan_id\": \"plan_008\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T20:34:52.005Z\", \"notes\": \"cuda:1 系统性问题：进程启动后快速死亡，零日志/零checkpoint/零stderr。连续三个进程在 cuda:1 上死亡(plan_005完成后)。需硬件诊断后才能重跑。conclusion=killed(系统kill，非OOM)。\"}, \"kl_sparsity30_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:24:03.207Z\", \"updated_at\": \"2026-05-15T20:35:02.572Z\", \"spec\": {\"hypothesis\": \"KL distillation @ 30% sparsity (mild pruning). Part of plan_008 3-level sparsity sweep (30/50/70%). Expect small PPL increase vs dense. Paired with kl_sparsity70_s42 and existing 50% data.\", \"plan_id\": \"plan_008\", \"command\": \"python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.3 --gpu 1 --output_dir /root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s42 --wandb_run_name kl_sparsity30_s42 --dataset wikitext-103 --gradient_checkpointing\", \"server\": \"westd-34887\", \"data_path\": \"wikitext-103\", \"data_count\": 1000, \"model_name\": \"llama-3.1-8b\", \"seed\": 42}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T20:34:51.064Z\", \"notes\": \"cuda:1 系统性问题：进程启动后快速死亡，零日志/零checkpoint/零stderr。与 kl_sparsity70_s42 同一模式——cuda:1 连续三个进程(plan_005后)均快速死亡。需硬件诊断后才能重跑。conclusion=killed(系统kill，非OOM)。v2版本(PID 132397)也同样死亡。\"}, \"ste_baseline_s42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T18:35:42.177Z\", \"updated_at\": \"2026-05-15T20:03:55.571Z\", \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T18:39:42.234Z\", \"finished_at\": \"2026-05-15T19:53:10.785Z\", \"training_hours\": 1.22}, \"completed_at\": \"2026-05-15T18:50:00.760Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"negative\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:53:11.891844+00:00\"}]}, \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=offline python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --relaxation ste --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/ste_baseline_s42 --wandb_run_name ste_baseline_s42 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"116142\", \"log_path\": \"~/runs/distill_sparse_swiglu/ste_baseline_s42.log\", \"submitted_at\": \"2026-05-15T19:17:21.463Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": null, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"wall_clock_seconds\": 2794.1, \"gpu_hours\": 0.78}, \"notes\": \"STE baseline 代码实现完成 (Worker worker_code_ste_baseline_20260515T183635)。修改：src/predictor.py 新增 STEMask 类（hard threshold + STE gradient），src/train.py 新增 --relaxation ste/gumbel 参数。\\n\\n## WikiText-2 评估 (seq_len=2048, 141 sequences, calibration=32)\\n- True Dense PPL: 6.12\\n- Predictor Hard Mask PPL: 8.18 (per-token sparsity=0.470, 低于 target 0.5)\\n- TEAL Sparse PPL: **15.77** (global 50% sparsity)\\n\\n## vs Gumbel-sigmoid 对比 (TEAL Sparse PPL, 公平 50% 全局稀疏度)\\n| 指标 | STE | Gumbel 4-seed mean | 差异 |\\n|------|-----|---------------------|------|\\n| TEAL Sparse PPL | 15.77 | 12.00 ± 0.07 | +31.4% |\\n| Hard Mask PPL | 8.18 | 9.19 ± 0.04 | -11.0%* |\\n| Per-token sparsity | 0.470 | 0.498 | -2.8pp |\\n\\n*Hard mask PPL 不可直接比较：STE per-token sparsity 仅 0.470（低于 Gumbel 0.498），较低稀疏度自然带来较低 PPL。\\n\\n## Lambda 震荡统计\\nSTE hard threshold 导致 Lagrangian multiplier 剧烈震荡：\\n- Steps 70-130 (关键不稳定区间): mean=66.40, std=94.87, range=[0.01, 1000]\\n- 前 500 步 (51 pts): mean=688.07, std=440.57, min=0.01, max=1000\\n- 后 500 步 (51 pts): mean=965.69, std=141.59, min=250, max=1000\\n- 全程: mean=826.88, std=354.23\\n\\nLambda 在前 100 步内从 0.01 飙升到 1000 再回落到 3.91，反复震荡。对比 Gumbel 训练中 lambda 平稳收敛到 cap，STE 的 constraint 满足极不稳定。\\n\\n## 根因分析\\nSTE hard threshold (>0.5=keep, ≤0.5=prune) 导致：\\n1. 离散 sparsity 值（sigmoid 微小变化可翻转大量 neuron）→ constraint 满足不稳定\\n2. Lambda 被迫在 0.01-1000 间震荡以追踪快速变化的 constraint violation\\n3. 最终收敛到 lambda=1000 (cap) 但 per-token sparsity 仅 0.470（未达 target 0.5）\\n4. 逐层稀疏度极端两极化（Layer 0-17: 5-56%, Layer 18-31: 56-90%），导致 TEAL 全局分配效果差\\n\\n## Conclusion: SUCCESS (验证 Gumbel 必要性)\\nTEAL sparse PPL 15.77 显著差于 Gumbel 12.00 (+31.4%)，确认 Gumbel soft mask 的平滑梯度对 KL distillation 训练至关重要。可直接用于 Reviewer Concern #3 defense。\", \"hypothesis\": \"STE relaxation (hard threshold + straight-through gradient) 是否能匹配 Gumbel-sigmoid 的 KL distillation 效果？如果差距大，说明 Gumbel soft mask 对 KL 训练至关重要（Reviewer Concern #3 defense）。\", \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 8.18, \"teal_sparse_ppl\": 15.77, \"model_level_sparsity\": 0.47, \"ppl_increase_vs_true_dense_pct\": 157.7, \"eval_seq_len\": 2048, \"calibration_samples\": 32, \"eval_dataset\": \"wikitext-2\", \"per_token_sparsity\": 0.47, \"lambda_stats\": {\"steps_70_130_mean\": 66.4, \"steps_70_130_std\": 94.87, \"first_500_mean\": 688.07, \"first_500_std\": 440.57, \"last_500_mean\": 965.69, \"last_500_std\": 141.59, \"overall_mean\": 826.88, \"overall_std\": 354.23}}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/ste_baseline_s42/predictor_kl_normalized.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/ste_baseline_s42.log\", \"conclusion\": \"success\"}, \"spon_supp_eval_retry\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:58:35.272Z\", \"updated_at\": \"2026-05-15T20:01:49.058Z\", \"spec\": {\"command\": \"TRANSFORMERS_OFFLINE=1 HF_DATASETS_OFFLINE=1 python src/eval_spon_supplementary.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --spon_checkpoint checkpoints/spon_2048_s42/spon_biases.pt --gpu 0 --seq_len 2048\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"123231\", \"log_path\": \"~/runs/distill_sparse_swiglu/eval_spon_supp_retry.log\", \"model_name\": \"llama-3.1-8b\", \"checkpoint_source\": \"spon_2048_s42\", \"eval_data\": \"wikitext-2\", \"data_path\": \"wikitext-2\", \"data_count\": 141, \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-15T20:01:48.568Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T20:01:49.058Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T20:01:50.055038+00:00\"}]}}, \"bce_isocompute_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:29:17.153Z\", \"updated_at\": \"2026-05-15T19:40:29.742Z\", \"hypothesis\": \"BCE 在等量 FLOPs (2700 步 vs KL 1000 步, ratio=2.71x) 下是否能缩小与 KL 的 PPL 差距？如果不能，说明 KL 的优势来自 loss 函数本身而非计算量（Reviewer Concern #2 defense）。\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=offline python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 2700 --warmup_steps 100 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --dataset wikitext-103 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/bce_isocompute_s42 --wandb_run_name bce_isocompute_2700steps_s42 --gradient_checkpointing\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"120879\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_isocompute_s42.log\", \"submitted_at\": \"2026-05-15T19:29:28.887Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": null, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"wall_clock_seconds\": 656.1, \"gpu_hours\": 0.18}, \"notes\": \"Iso-compute BCE: 2700 步匹配 KL 1000 步的总 FLOPs (ratio=2.71x, 实测 profile_flops.py: KL 0.549s/step vs BCE 0.202s/step @BS=1,SL=512)。\\\\nReviewer Concern #2 defense: 验证 KL 优势来自 loss 函数本身而非计算量差异。\\\\n\\\\n## FLOPs 计算依据\\\\n- KL 每步: dense fwd (no grad) + sparse fwd (grad) + backward w/ gradient checkpointing = 0.549s\\\\n- BCE 每步: dense fwd (no grad) + predictor fwd/bwd (~0.9% model FLOPs) = 0.202s\\\\n- Ratio: 2.71x → 1000 KL steps ≈ 2700 BCE steps\\\\n\\\\n## 失败记录 [2026-05-15]\\\\n进程在 Step 500/2700 后静默退出（PID 120879）。日志仅 17 行，最后记录 Step 500: loss=0.6461, bce=0.6406, reg=0.0055, sparsity=0.555。无 error traceback，无 checkpoint 产出。wandb offline 数据截至 03:38（启动后仅 9 分钟）。疑似 OOM 或被外部 kill。\", \"plan_id\": \"plan_003\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T19:40:24.980Z\"}, \"ste_kl_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:48:15.860Z\", \"updated_at\": \"2026-05-15T18:56:12.716Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && WANDB_MODE=offline PYTHONUNBUFFERED=1 python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_ste --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/ste_kl_s42 --wandb_run_name ste_kl_s42 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"112197\", \"log_path\": \"~/runs/distill_sparse_swiglu/ste_kl_s42.log\", \"submitted_at\": \"2026-05-15T18:50:37.022Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103 (HF cached)\", \"data_count\": null, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from scratch with STE mask)\", \"eval_data\": \"wikitext-2 (post-training eval)\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 335.7, \"gpu_hours\": 0.09}, \"conclusion\": \"killed\", \"notes\": \"Director 确认 cuda:1 空转超过 30 分钟，ste_kl_s42 进程 PID 112197 已死。释放 cuda:1 给 ste_baseline_s42 重跑。\", \"completed_at\": \"2026-05-15T18:56:12.716Z\"}, \"spon_training_seq2048\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:35:39.812Z\", \"updated_at\": \"2026-05-15T18:54:31.996Z\", \"spec\": {\"hypothesis\": \"SPON seq_len=2048 重训消除 train/eval seq_len mismatch confound (原 128 vs eval 2048)，决定 Claim 2 是否有救\", \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"server\": \"westd-34887\", \"parent\": \"spon_training\", \"data_path\": \"wikitext-103 (HF cached)\", \"loss_type\": \"kl_spon\", \"sparsity\": 0.5, \"steps\": 1000, \"seq_len\": 2048, \"batch_size\": 4, \"gpu\": \"cuda:0\"}, \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T18:39:41.493Z\"}, \"conclusion\": \"killed\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\", \"completed_at\": \"2026-05-15T18:41:36.489Z\"}, \"mvp_kl_norm_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:30:10.779Z\", \"updated_at\": \"2026-05-15T14:56:37.217Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_s123 --wandb_run_name mvp_kl_norm_s123 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"69608\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_kl_norm_s123.log\", \"submitted_at\": \"2026-05-15T14:30:49.142Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103 (HF cached)\", \"data_count\": null, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"wall_clock_seconds\": 1548.1, \"gpu_hours\": 0.43}, \"conclusion\": \"failed\", \"failure_reason\": \"KL normalization bug: train.py:228 ÷vocab_size + losses.py ÷seq_len = double normalization, kl_norm≈0.00007, gradient signal ~10^-5\", \"completed_at\": \"2026-05-15T14:56:37.217Z\"}, \"mvp_kl_norm_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:23:52.490Z\", \"updated_at\": \"2026-05-15T14:56:36.798Z\", \"spec\": {\"hypothesis\": \"Normalized KL (÷seq_len) + Lagrangian 约束在 1000 步完整训练下产生优于 BCE 的稀疏预测器 (PPL increase < 58%)\", \"loss_type\": \"kl_normalized\", \"seed\": 42, \"model\": \"Llama-3.1-8B\", \"model_name\": \"llama-3.1-8b\", \"sparsity\": 0.5, \"steps\": 1000, \"batch_size\": 4, \"seq_len\": 2048, \"gpu\": \"cuda:0\", \"server\": \"westd-34887\", \"parent\": \"kl_normalized_quicktest\", \"data_path\": \"wikitext-103 (HF cached)\", \"data_count\": null, \"kl_normalization\": \"÷seq_len only\", \"lagrangian\": \"lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]\", \"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_s42 --wandb_run_name mvp_kl_norm_s42 --dataset wikitext-103\\\"\"}, \"pid\": 67789, \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_kl_norm_s42.log\", \"notes\": \"Director 指令的 mvp_kl_s42（新配方）。Normalized KL (÷seq_len) + Lagrangian, 1000 steps, seed=42。已于 session 恢复时提交 (PID=67789)。训练完后需跑 WikiText-2 + C4 eval。\", \"conclusion\": \"failed\", \"failure_reason\": \"KL normalization bug: train.py:228 ÷vocab_size + losses.py ÷seq_len = double normalization, kl_norm≈0.00007, gradient signal ~10^-5\", \"completed_at\": \"2026-05-15T14:56:36.798Z\"}, \"kl_normalized_quicktest\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:36:21.345Z\", \"updated_at\": \"2026-05-15T14:36:32.465Z\", \"spec\": {\"hypothesis\": \"KL loss per-token-per-dim 归一化后 (~0.003 量级) + Lagrangian 约束可维持 50% sparsity\", \"loss_type\": \"kl_normalized\", \"seed\": 42, \"model\": \"Llama-3.1-8B\", \"sparsity\": 0.5, \"steps\": 200, \"batch_size\": 4, \"seq_len\": 2048, \"gpu\": \"cuda:0\", \"server\": \"westd-34887\", \"parent\": \"kl_lagrangian_quicktest\", \"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 200 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/kl_normalized_quicktest --wandb_run_name kl_normalized_quicktest --dataset wikitext-103\\\"\", \"data_path\": \"wikitext-103 (HF cached)\", \"data_count\": null, \"model_name\": \"llama-3.1-8b\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_normalized_quicktest/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/logs/kl_normalized_quicktest.log\"}, \"conclusion\": \"failed\", \"metrics\": {\"step1_kl\": 1.18, \"step200_kl\": 0.641, \"step200_sparsity\": 0.504, \"final_lambda\": 8, \"sparsity_converged_step\": 80, \"sparsity_trajectory\": [0.406, 0.398, 0.398, 0.457, 0.52, 0.506, 0.504, 0.504], \"lambda_trajectory\": [1, 2, 4, 8, 8, 8, 8, 8]}, \"notes\": \"FAILED: 代码 bug — train.py:228 有 kl_norm = kl_raw / vocab_size (÷128256), 同时 KLDistillLoss 已做 kl / seq_len。总归一化 = ÷(seq_len × vocab_size), kl_norm≈0.00007。梯度信号~10^-5, predictor 只学了维持 50% 总量。kl_raw 实际从 1.18 上升到 9.94（非下降）。之前的 SUCCESS 结论是错误的。\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_normalized_quicktest/predictor_kl.pt\", \"log_path\": \"Worker log: worker_code_fix-kl-norm_20260515T135636\", \"completed_at\": \"2026-05-15T14:18:05.703Z\", \"failure_reason\": \"KL normalization bug: train.py:228 ÷vocab_size + losses.py ÷seq_len = double normalization, kl_norm≈0.00007. 结论 \\\"seq_len-only 归一化有效\\\" 是错误的——实际代码从未改为 seq_len-only。kl_raw 从 1.18 上升到 9.94 (非下降), predictor 只学了维持 50% 总量没学到哪些神经元重要。\"}}, \"count\": 257, \"total\": 257, \"baseline\": \"bench_dense\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0668}}"
    }
  },
  "sourceToolAssistantUUID": "fa64b9d5-6437-4814-b7a4-65bdc44ca0a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。 详情: Process exited cleanly, W&B data available  - exp_id: qwen14b_dense_4task_v2 - project: distill_sparse_swiglu - server: westd-41718 - log_path: ~…",
  "leafUuid": "cbece236-41e3-4cff-b685-8b813c5796ea",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze experiment results and transition to done",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0"
}
```

---

### Tool result

_source line 19 · 2026-05-19T18:18:31.310Z_

<details><summary>↩ Tool result · `toolu_019JusiCwtpfQcmien9muFJ2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reconciled\": 3, \"results\": [{\"exp_id\": \"qwen14b_teal275_uniform_eval_v3\", \"success\": true, \"actions\": [\"Job still running (pid=115174)\"]}, {\"exp_id\": \"qwen14b_teal275_hspiqa\", \"success\": true, \"actions\": [\"Job still running (pid=126076)\"]}, {\"exp_id\": \"qwen14b_kl30_s42_gsm8k_v2\", \"success\": true, \"actions\": [\"Skipped (created 1s ago < interval 120s)\"]}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e1b5ace-b3ed-4b6b-9ccb-e3c1e3b6516b",
  "isSidechain": false,
  "promptId": "4685578a-62f4-4e3c-9ae6-7efcd8955d99",
  "type": "user",
  "uuid": "bf1d9311-85e0-4c5c-8d13-4da5fc282361",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reconciled\\\": 3, \\\"results\\\": [{\\\"exp_id\\\": \\\"qwen14b_teal275_uniform_eval_v3\\\", \\\"success\\\": true, \\\"actions\\\": [\\\"Job still running (pid=115174)\\\"]}, {\\\"exp_id\\\": \\\"qwen14b_teal275_hspiqa\\\", \\\"success\\\": true, \\\"actions\\\": [\\\"Job still running (pid=126076)\\\"]}, {\\\"exp_id\\\": \\\"qwen14b_kl30_s42_gsm8k_v2\\\", \\\"success\\\": true, \\\"actions\\\": [\\\"Skipped (created 1s ago < interval 120s)\\\"]}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reconciled\": 3, \"results\": [{\"exp_id\": \"qwen14b_teal275_uniform_eval_v3\", \"success\": true, \"actions\": [\"Job still running (pid=115174)\"]}, {\"exp_id\": \"qwen14b_teal275_hspiqa\", \"success\": true, \"actions\": [\"Job still running (pid=126076)\"]}, {\"exp_id\": \"qwen14b_kl30_s42_gsm8k_v2\", \"success\": true, \"actions\": [\"Skipped (created 1s ago < interval 120s)\"]}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "4e1b5ace-b3ed-4b6b-9ccb-e3c1e3b6516b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T18:18:31.326Z_

<details><summary>↩ Tool result · `toolu_017k5HxDg4GvVbz2RQzmsFEu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/report.md\", \"content\": \"# Handover — 2026-05-19\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| qwen14b_kl30_s42_gsm8k_v2 | KL s42 GSM8K supplement for Qwen-14B (retry). Enables KL vs TEAL comparison on reasoning task. v1 killed due to GPU contention on 41718:1. | — | — | — |\\n| qwen14b_teal275_hspiqa | TEAL@27.5% uniform HellaSwag+PIQA supplement for Qwen-14B. Completes 6-task TEAL baseline alongside qwen14b_teal275_uniform_eval_v3 (wikitext2/arc/wg/mmlu/gsm8k). | — | — | — |\\n| qwen14b_teal275_uniform_eval_v3 | TEAL@27.5% uniform baseline for sparsity-matched KL comparison on Qwen-14B. Fix: relaxed _uniform_topk_masks assert from 0.02 to 0.05 tolerance. Current tasks: wikitext2,arc,wg,mmlu,gsm8k. Missing hellaswag+piqa will supplement. | — | — | — |\\n\\n## 待处理\\n- flashinfer_benchmark_llama8b_v2: Wall-clock inference speedup: gather-matmul sparse FFN (30%/50% sparsity) vs dense on LLaMA-3.1-8B. Full-sparse path: all 3 projections (gate/up/down) use gathered weights. Addresses reviewer W3.（准备中）\\n- c1_eval_30pct_s456（准备中）\\n- kl_sparsity40_s42_eval_teal_uniform: KL predictor at 40% sparsity with TEAL uniform allocation fills the gap in the 6-point regime curve, providing protocol-consistent data alongside existing global_topk eval.（准备中）\\n- c4_download（准备中）\\n- kl50_s456_train_eval（准备中）\\n- mag_preservation_reg（准备中）\\n- longbench_dense_v5（准备中）\\n- kl_lagrangian_v2（准备中）\\n- kl_norm_v3_quicktest（准备中）\\n- mvp_kl_norm_s456（准备中）\\n- …另有 4 项\\n\\n## 近期结论\\n- **qwen14b_dense_hspiqa** (success): Qwen-14B dense baseline hellaswag+piqa supplement. Completing 6-task suite for 14B comparison table. ← 基于 qwen14b_dense_baseline\\n- **qwen14b_kl30_s42_gsm8k** (killed): KL s42 GSM8K supplement for Qwen-14B. Enables KL vs TEAL comparison on reasoning task (Round 12 Q6). ← 基于 qwen14b_kl30_s42_eval_uniform_v3\\n- **qwen14b_dense_4task** (failed): Qwen-14B dense baseline remaining 4 tasks (wikitext2, arc_challenge, winogrande, mmlu). Parallel with qwen14b_dense_hspiqa (HS+PIQA) on cuda:0 to complete full 6-task dense baseline for 14B comparison table. ← 基于 qwen14b_dense_baseline\\n\\n## 趋势\\n成功 171 / 负向 21 / 失败 30 / 共 239\\nhellaswag_acc_norm: 0.8421 ↑（近 3 次 success）\\npiqa_acc_norm: 0.8194 ↑（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-34887: 无 GPU 信息\\nwestd-41718: 无 GPU 信息\\n\\n## 告警\\n- mvp_kl_s123: 已被终止 — unknown\\n- mvp_kl_s456: 已被终止 — unknown\\n- kl_normalized_quicktest: 训练失败 — unknown\\n- mvp_kl_norm_s42: 训练失败 — unknown\\n- mvp_kl_norm_s123: 训练失败 — unknown\\n- spon_training_seq2048: 已被终止 — unknown\\n- ste_kl_s42: 已被终止 — unknown\\n- bce_isocompute_s42: 训练失败 — unknown\\n- eval_spon_supp_retry: 训练失败 — unknown\\n- bce_isocompute_s42_v2: 已被终止 — unknown\\n- spon_supp_eval_retry: 训练失败 — unknown\\n- kl_sparsity30_s42: 已被终止 — unknown\\n- kl_sparsity70_s42: 已被终止 — unknown\\n- lm_eval_dense_test: 训练失败 — unknown\\n- lm_eval_mistral_downstream: 训练失败 — unknown\\n- bench_mistral_kl50_s42: 已被终止 — unknown\\n- longbench_kl30_uniform: 训练失败 — unknown\\n- longbench_dense: 训练失败 — unknown\\n- longbench_kl30_uniform_v2: 训练失败 — unknown\\n- longbench_dense_v2: 训练失败 — unknown\\n- longbench_kl30_uniform_v3: 训练失败 — unknown\\n- longbench_dense_v3: 训练失败 — unknown\\n- longbench_dense_v4: 训练失败 — unknown\\n- steps_curve_s42: 已被终止 — unknown\\n- steps_curve_s42_v2: 已被终止 — unknown\\n- qwen14b_kl30_uniform_eval: 训练失败 — unknown\\n- qwen14b_teal30_uniform_eval: 训练失败 — unknown\\n- c4_ood_kl30_s123: 训练失败 — unknown\\n- c4_ood_dense_baseline: 训练失败 — unknown\\n- downstream_ext_kl50_uniform_s42: 训练失败 — unknown\\n- downstream_ext_kl30_uniform_s123: 训练失败 — unknown\\n- c1_ablation_30pct_s42: 训练失败 — unknown\\n- c1_ablation_30pct_s42_eval: 训练失败 — unknown\\n- bce_isocompute_hellaswag_piqa: 训练失败 — unknown\\n- c1_ablation_30pct_eval_34887: 已被终止 — unknown\\n- qwen14b_kl30_s123_eval: 已被终止 — unknown\\n- qwen14b_kl30_s456_eval: 已被终止 — unknown\\n- qwen14b_kl30_s123_eval_v2: 训练失败 — unknown\\n- qwen14b_kl30_s123_eval_v3: 训练失败 — unknown\\n- qwen14b_kl30_s42_eval_uniform: 训练失败 — unknown\\n- qwen14b_teal30_uniform_hspiqa: 已被终止 — unknown\\n- qwen14b_kl30_s42_eval_uniform_v2: 已被终止 — unknown\\n- qwen14b_teal275_uniform_eval: 已被终止 — unknown\\n- qwen14b_teal275_uniform_eval_v2: 训练失败 — unknown\\n- flashinfer_benchmark_llama8b: 训练失败 — unknown\\n- qwen14b_kl30_s42_gsm8k: 已被终止 — unknown\\n- qwen14b_dense_4task: 训练失败 — unknown\\n\", \"total_chars\": 4246, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25610811-bc2f-4535-ad32-ccf47a08bb04",
  "isSidechain": false,
  "promptId": "4685578a-62f4-4e3c-9ae6-7efcd8955d99",
  "type": "user",
  "uuid": "4590d4fb-f640-4b07-9330-2708c8b810eb",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/report.md\\\", \\\"content\\\": \\\"# Handover — 2026-05-19\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\\\n|--------|------|------|---------|-----|\\\\n| qwen14b_kl30_s42_gsm8k_v2 | KL s42 GSM8K supplement for Qwen-14B (retry). Enables KL vs TEAL comparison on reasoning task. v1 killed due to GPU contention on 41718:1. | — | — | — |\\\\n| qwen14b_teal275_hspiqa | TEAL@27.5% uniform HellaSwag+PIQA supplement for Qwen-14B. Completes 6-task TEAL baseline alongside qwen14b_teal275_uniform_eval_v3 (wikitext2/arc/wg/mmlu/gsm8k). | — | — | — |\\\\n| qwen14b_teal275_uniform_eval_v3 | TEAL@27.5% uniform baseline for sparsity-matched KL comparison on Qwen-14B. Fix: relaxed _uniform_topk_masks assert from 0.02 to 0.05 tolerance. Current tasks: wikitext2,arc,wg,mmlu,gsm8k. Missing hellaswag+piqa will supplement. | — | — | — |\\\\n\\\\n## 待处理\\\\n- flashinfer_benchmark_llama8b_v2: Wall-clock inference speedup: gather-matmul sparse FFN (30%/50% sparsity) vs dense on LLaMA-3.1-8B. Full-sparse path: all 3 projections (gate/up/down) use gathered weights. Addresses reviewer W3.（准备中）\\\\n- c1_eval_30pct_s456（准备中）\\\\n- kl_sparsity40_s42_eval_teal_uniform: KL predictor at 40% sparsity with TEAL uniform allocation fills the gap in the 6-point regime curve, providing protocol-consistent data alongside existing global_topk eval.（准备中）\\\\n- c4_download（准备中）\\\\n- kl50_s456_train_eval（准备中）\\\\n- mag_preservation_reg（准备中）\\\\n- longbench_dense_v5（准备中）\\\\n- kl_lagrangian_v2（准备中）\\\\n- kl_norm_v3_quicktest（准备中）\\\\n- mvp_kl_norm_s456（准备中）\\\\n- …另有 4 项\\\\n\\\\n## 近期结论\\\\n- **qwen14b_dense_hspiqa** (success): Qwen-14B dense baseline hellaswag+piqa supplement. Completing 6-task suite for 14B comparison table. ← 基于 qwen14b_dense_baseline\\\\n- **qwen14b_kl30_s42_gsm8k** (killed): KL s42 GSM8K supplement for Qwen-14B. Enables KL vs TEAL comparison on reasoning task (Round 12 Q6). ← 基于 qwen14b_kl30_s42_eval_uniform_v3\\\\n- **qwen14b_dense_4task** (failed): Qwen-14B dense baseline remaining 4 tasks (wikitext2, arc_challenge, winogrande, mmlu). Parallel with qwen14b_dense_hspiqa (HS+PIQA) on cuda:0 to complete full 6-task dense baseline for 14B comparison table. ← 基于 qwen14b_dense_baseline\\\\n\\\\n## 趋势\\\\n成功 171 / 负向 21 / 失败 30 / 共 239\\\\nhellaswag_acc_norm: 0.8421 ↑（近 3 次 success）\\\\npiqa_acc_norm: 0.8194 ↑（近 3 次 success）\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\nwestd-34887: 无 GPU 信息\\\\nwestd-41718: 无 GPU 信息\\\\n\\\\n## 告警\\\\n- mvp_kl_s123: 已被终止 — unknown\\\\n- mvp_kl_s456: 已被终止 — unknown\\\\n- kl_normalized_quicktest: 训练失败 — unknown\\\\n- mvp_kl_norm_s42: 训练失败 — unknown\\\\n- mvp_kl_norm_s123: 训练失败 — unknown\\\\n- spon_training_seq2048: 已被终止 — unknown\\\\n- ste_kl_s42: 已被终止 — unknown\\\\n- bce_isocompute_s42: 训练失败 — unknown\\\\n- eval_spon_supp_retry: 训练失败 — unknown\\\\n- bce_isocompute_s42_v2: 已被终止 — unknown\\\\n- spon_supp_eval_retry: 训练失败 — unknown\\\\n- kl_sparsity30_s42: 已被终止 — unknown\\\\n- kl_sparsity70_s42: 已被终止 — unknown\\\\n- lm_eval_dense_test: 训练失败 — unknown\\\\n- lm_eval_mistral_downstream: 训练失败 — unknown\\\\n- bench_mistral_kl50_s42: 已被终止 — unknown\\\\n- longbench_kl30_uniform: 训练失败 — unknown\\\\n- longbench_dense: 训练失败 — unknown\\\\n- longbench_kl30_uniform_v2: 训练失败 — unknown\\\\n- longbench_dense_v2: 训练失败 — unknown\\\\n- longbench_kl30_uniform_v3: 训练失败 — unknown\\\\n- longbench_dense_v3: 训练失败 — unknown\\\\n- longbench_dense_v4: 训练失败 — unknown\\\\n- steps_curve_s42: 已被终止 — unknown\\\\n- steps_curve_s42_v2: 已被终止 — unknown\\\\n- qwen14b_kl30_uniform_eval: 训练失败 — unknown\\\\n- qwen14b_teal30_uniform_eval: 训练失败 — unknown\\\\n- c4_ood_kl30_s123: 训练失败 — unknown\\\\n- c4_ood_dense_baseline: 训练失败 — unknown\\\\n- downstream_ext_kl50_uniform_s42: 训练失败 — unknown\\\\n- downstream_ext_kl30_uniform_s123: 训练失败 — unknown\\\\n- c1_ablation_30pct_s42: 训练失败 — unknown\\\\n- c1_ablation_30pct_s42_eval: 训练失败 — unknown\\\\n- bce_isocompute_hellaswag_piqa: 训练失败 — unknown\\\\n- c1_ablation_30pct_eval_34887: 已被终止 — unknown\\\\n- qwen14b_kl30_s123_eval: 已被终止 — unknown\\\\n- qwen14b_kl30_s456_eval: 已被终止 — unknown\\\\n- qwen14b_kl30_s123_eval_v2: 训练失败 — unknown\\\\n- qwen14b_kl30_s123_eval_v3: 训练失败 — unknown\\\\n- qwen14b_kl30_s42_eval_uniform: 训练失败 — unknown\\\\n- qwen14b_teal30_uniform_hspiqa: 已被终止 — unknown\\\\n- qwen14b_kl30_s42_eval_uniform_v2: 已被终止 — unknown\\\\n- qwen14b_teal275_uniform_eval: 已被终止 — unknown\\\\n- qwen14b_teal275_uniform_eval_v2: 训练失败 — unknown\\\\n- flashinfer_benchmark_llama8b: 训练失败 — unknown\\\\n- qwen14b_kl30_s42_gsm8k: 已被终止 — unknown\\\\n- qwen14b_dense_4task: 训练失败 — unknown\\\\n\\\", \\\"total_chars\\\": 4246, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/report.md\", \"content\": \"# Handover — 2026-05-19\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| qwen14b_kl30_s42_gsm8k_v2 | KL s42 GSM8K supplement for Qwen-14B (retry). Enables KL vs TEAL comparison on reasoning task. v1 killed due to GPU contention on 41718:1. | — | — | — |\\n| qwen14b_teal275_hspiqa | TEAL@27.5% uniform HellaSwag+PIQA supplement for Qwen-14B. Completes 6-task TEAL baseline alongside qwen14b_teal275_uniform_eval_v3 (wikitext2/arc/wg/mmlu/gsm8k). | — | — | — |\\n| qwen14b_teal275_uniform_eval_v3 | TEAL@27.5% uniform baseline for sparsity-matched KL comparison on Qwen-14B. Fix: relaxed _uniform_topk_masks assert from 0.02 to 0.05 tolerance. Current tasks: wikitext2,arc,wg,mmlu,gsm8k. Missing hellaswag+piqa will supplement. | — | — | — |\\n\\n## 待处理\\n- flashinfer_benchmark_llama8b_v2: Wall-clock inference speedup: gather-matmul sparse FFN (30%/50% sparsity) vs dense on LLaMA-3.1-8B. Full-sparse path: all 3 projections (gate/up/down) use gathered weights. Addresses reviewer W3.（准备中）\\n- c1_eval_30pct_s456（准备中）\\n- kl_sparsity40_s42_eval_teal_uniform: KL predictor at 40% sparsity with TEAL uniform allocation fills the gap in the 6-point regime curve, providing protocol-consistent data alongside existing global_topk eval.（准备中）\\n- c4_download（准备中）\\n- kl50_s456_train_eval（准备中）\\n- mag_preservation_reg（准备中）\\n- longbench_dense_v5（准备中）\\n- kl_lagrangian_v2（准备中）\\n- kl_norm_v3_quicktest（准备中）\\n- mvp_kl_norm_s456（准备中）\\n- …另有 4 项\\n\\n## 近期结论\\n- **qwen14b_dense_hspiqa** (success): Qwen-14B dense baseline hellaswag+piqa supplement. Completing 6-task suite for 14B comparison table. ← 基于 qwen14b_dense_baseline\\n- **qwen14b_kl30_s42_gsm8k** (killed): KL s42 GSM8K supplement for Qwen-14B. Enables KL vs TEAL comparison on reasoning task (Round 12 Q6). ← 基于 qwen14b_kl30_s42_eval_uniform_v3\\n- **qwen14b_dense_4task** (failed): Qwen-14B dense baseline remaining 4 tasks (wikitext2, arc_challenge, winogrande, mmlu). Parallel with qwen14b_dense_hspiqa (HS+PIQA) on cuda:0 to complete full 6-task dense baseline for 14B comparison table. ← 基于 qwen14b_dense_baseline\\n\\n## 趋势\\n成功 171 / 负向 21 / 失败 30 / 共 239\\nhellaswag_acc_norm: 0.8421 ↑（近 3 次 success）\\npiqa_acc_norm: 0.8194 ↑（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-34887: 无 GPU 信息\\nwestd-41718: 无 GPU 信息\\n\\n## 告警\\n- mvp_kl_s123: 已被终止 — unknown\\n- mvp_kl_s456: 已被终止 — unknown\\n- kl_normalized_quicktest: 训练失败 — unknown\\n- mvp_kl_norm_s42: 训练失败 — unknown\\n- mvp_kl_norm_s123: 训练失败 — unknown\\n- spon_training_seq2048: 已被终止 — unknown\\n- ste_kl_s42: 已被终止 — unknown\\n- bce_isocompute_s42: 训练失败 — unknown\\n- eval_spon_supp_retry: 训练失败 — unknown\\n- bce_isocompute_s42_v2: 已被终止 — unknown\\n- spon_supp_eval_retry: 训练失败 — unknown\\n- kl_sparsity30_s42: 已被终止 — unknown\\n- kl_sparsity70_s42: 已被终止 — unknown\\n- lm_eval_dense_test: 训练失败 — unknown\\n- lm_eval_mistral_downstream: 训练失败 — unknown\\n- bench_mistral_kl50_s42: 已被终止 — unknown\\n- longbench_kl30_uniform: 训练失败 — unknown\\n- longbench_dense: 训练失败 — unknown\\n- longbench_kl30_uniform_v2: 训练失败 — unknown\\n- longbench_dense_v2: 训练失败 — unknown\\n- longbench_kl30_uniform_v3: 训练失败 — unknown\\n- longbench_dense_v3: 训练失败 — unknown\\n- longbench_dense_v4: 训练失败 — unknown\\n- steps_curve_s42: 已被终止 — unknown\\n- steps_curve_s42_v2: 已被终止 — unknown\\n- qwen14b_kl30_uniform_eval: 训练失败 — unknown\\n- qwen14b_teal30_uniform_eval: 训练失败 — unknown\\n- c4_ood_kl30_s123: 训练失败 — unknown\\n- c4_ood_dense_baseline: 训练失败 — unknown\\n- downstream_ext_kl50_uniform_s42: 训练失败 — unknown\\n- downstream_ext_kl30_uniform_s123: 训练失败 — unknown\\n- c1_ablation_30pct_s42: 训练失败 — unknown\\n- c1_ablation_30pct_s42_eval: 训练失败 — unknown\\n- bce_isocompute_hellaswag_piqa: 训练失败 — unknown\\n- c1_ablation_30pct_eval_34887: 已被终止 — unknown\\n- qwen14b_kl30_s123_eval: 已被终止 — unknown\\n- qwen14b_kl30_s456_eval: 已被终止 — unknown\\n- qwen14b_kl30_s123_eval_v2: 训练失败 — unknown\\n- qwen14b_kl30_s123_eval_v3: 训练失败 — unknown\\n- qwen14b_kl30_s42_eval_uniform: 训练失败 — unknown\\n- qwen14b_teal30_uniform_hspiqa: 已被终止 — unknown\\n- qwen14b_kl30_s42_eval_uniform_v2: 已被终止 — unknown\\n- qwen14b_teal275_uniform_eval: 已被终止 — unknown\\n- qwen14b_teal275_uniform_eval_v2: 训练失败 — unknown\\n- flashinfer_benchmark_llama8b: 训练失败 — unknown\\n- qwen14b_kl30_s42_gsm8k: 已被终止 — unknown\\n- qwen14b_dense_4task: 训练失败 — unknown\\n\", \"total_chars\": 4246, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "25610811-bc2f-4535-ad32-ccf47a08bb04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T18:18:31.340Z_

<details><summary>↩ Tool result · `toolu_01MuvrJdx7WMBGWmUoc3SNRS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ROADMAP.md\", \"content\": \"# distill_sparse_swiglu — Research Dashboard\\n\\n> 最后更新: 2026-05-19 05:07 UTC | 更新原因: D071 Mistral cross-arch downstream 确认 KL 优势，进入最终整合阶段\\n\\n> 最后更新: 2026-05-19 05:10 UTC | 更新原因: D071 Mistral cross-arch 确认\\n\\n## 核心方向\\nKL distillation discovers fundamentally different neuron importance patterns for SwiGLU sparsity prediction (LLaMA-3.1-8B). C1 causal ablation provides evidence target quality drives KL advantage. Cross-arch (Mistral) downstream confirms KL > TEAL. 详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: 最终数据整合 → Round 11 review → ARR 提交\\n- **架构**: LLaMA-3.1-8B (主) + Mistral-7B (cross-arch, downstream confirmed) + Qwen-14B (cross-scale)\\n- **D071**: Mistral TEAL baseline 确认 KL downstream 优势 (ARC +9pp, WG +5.6pp)\\n- **C1 retrain**: max Δ=1.70pp with consistent checkpoints ✅\\n- **Paper P1-P9 text patches**: ✅\\n- **Paper consistency**: 0 critical / 0 warning ✅\\n\\n## 实验状态\\n\\n### 全部完成\\n- ✅ Mistral TEAL 30%: ARC=41.1%, WG=63.5%, MMLU=43.5% → KL wins (ARC +9, WG +5.6)\\n- ✅ Mistral TEAL 50%: MMLU=26.4%≈random → capacity cliff cross-arch\\n- ✅ C1 retrain s123/s456: max Δ=1.70pp, consistent with main table\\n- ✅ BCE 50% unified: PPL=27.97, MMLU=26.1%≈random\\n- ✅ C1@30% 3-seed: all Δ ≤ 1.70pp\\n\\n### 进行中\\n- 🔄 Mistral KL 30% HellaSwag/PIQA (~30min) — 补全 Mistral 对比表\\n\\n## 后续\\n- [ ] Paper Agent 整合 Mistral cross-arch + C1 retrain 数据\\n- [ ] Mistral KL HellaSwag/PIQA 到齐后补表\\n- [ ] Round 11 review (continue mode)\\n- [ ] 最终 ARR 提交\\n\\n## GPU 预算\\n本项目分配: westd-34887 (cuda:0,1) + westd-41718 (cuda:0,1) = 4 GPU\\n状态: 34887:0 Mistral KL HS/PIQA, 其余空闲\\n\\n## DDL\\nEMNLP 2026 ARR May cycle: **2026-05-25** (6 天)\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D079 | 2026-05-19 | 放弃 wall-clock speedup claim，论文定位为 prediction quali | flashinfer_benchmark_34887 |\\n| D078 | 2026-05-19 | 投入 flashinfer sparse kernel 开发（3h 硬上限），现有 mask-and | benchmark_latency |\\n| D077 | 2026-05-19 | TEAL assertion tolerance 0.02→0.05 + 重提 v3/teal275 | qwen14b_kl30_s42_eval_uniform_v3, qwen14b_teal275_uniform_eval_v2 |\\n| D076 | 2026-05-19 | D074 superseded: Layer 1-4 零稀疏性是 eval pipeline bug | qwen14b_kl30_s42_eval_uniform_v2 |\\n| D075 | 2026-05-19 | 确认 eval pipeline bug（mag*hard_mask 退化），修复代码并重跑全部 Q | qwen14b_kl30_s42_eval_uniform_v2, qwen14b_kl30_s123_eval_v4, qwen14b_kl30_s456_eval_v2, qwen14b_teal275_uniform_eval |\\n| D074 | 2026-05-19 | Qwen-14B Layer 1-4 零稀疏性确认为 predictor 行为，补跑 TEAL@27 | qwen14b_kl30_s42_eval_uniform_v2, qwen14b_kl30_s123_eval_v4, qwen14b_kl30_s456_eval_v2, qwen14b_teal_27.5pct_uniform |\\n| D073 | 2026-05-19 | Round 12 Action Matrix: Fix N1/N2 data errors, del | bce_gumbel_no_penalty_s42, bce_comp_staged_s42, qwen14b_kl30_s123, qwen14b_kl30_s456 |\\n| D072 | 2026-05-19 | Round 11 Action Matrix: C1 reframe (mask transfera | qwen14b_mask_divergence_analysis, teal_28.5pct_sanity, bce_gumbel_no_penalty_s42 |\\n| D071 | 2026-05-19 | Mistral TEAL baseline 确认 KL cross-arch downstream  | mistral_teal30_downstream, mistral_teal50_downstream, eval_c1_retrain_30pct_s123, eval_c1_retrain_30pct_s456 |\\n| D070 | 2026-05-19 | Accept 冲刺计划修正：砍 LLaMA-3-8B（同一家族）和 sparse kernel（高风 | mistral_kl30_downstream |\\n\\n\", \"lines\": 58}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1db9227d-c4cb-4ae9-a392-887b20f58ca0",
  "isSidechain": false,
  "promptId": "4685578a-62f4-4e3c-9ae6-7efcd8955d99",
  "type": "user",
  "uuid": "34612c5e-a88e-434c-8fc2-57fa7fb235a6",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ROADMAP.md\\\", \\\"content\\\": \\\"# distill_sparse_swiglu — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-19 05:07 UTC | 更新原因: D071 Mistral cross-arch downstream 确认 KL 优势，进入最终整合阶段\\\\n\\\\n> 最后更新: 2026-05-19 05:10 UTC | 更新原因: D071 Mistral cross-arch 确认\\\\n\\\\n## 核心方向\\\\nKL distillation discovers fundamentally different neuron importance patterns for SwiGLU sparsity prediction (LLaMA-3.1-8B). C1 causal ablation provides evidence target quality drives KL advantage. Cross-arch (Mistral) downstream confirms KL > TEAL. 详见 paper_framing.md。\\\\n\\\\n## 当前进展\\\\n- **阶段**: 最终数据整合 → Round 11 review → ARR 提交\\\\n- **架构**: LLaMA-3.1-8B (主) + Mistral-7B (cross-arch, downstream confirmed) + Qwen-14B (cross-scale)\\\\n- **D071**: Mistral TEAL baseline 确认 KL downstream 优势 (ARC +9pp, WG +5.6pp)\\\\n- **C1 retrain**: max Δ=1.70pp with consistent checkpoints ✅\\\\n- **Paper P1-P9 text patches**: ✅\\\\n- **Paper consistency**: 0 critical / 0 warning ✅\\\\n\\\\n## 实验状态\\\\n\\\\n### 全部完成\\\\n- ✅ Mistral TEAL 30%: ARC=41.1%, WG=63.5%, MMLU=43.5% → KL wins (ARC +9, WG +5.6)\\\\n- ✅ Mistral TEAL 50%: MMLU=26.4%≈random → capacity cliff cross-arch\\\\n- ✅ C1 retrain s123/s456: max Δ=1.70pp, consistent with main table\\\\n- ✅ BCE 50% unified: PPL=27.97, MMLU=26.1%≈random\\\\n- ✅ C1@30% 3-seed: all Δ ≤ 1.70pp\\\\n\\\\n### 进行中\\\\n- 🔄 Mistral KL 30% HellaSwag/PIQA (~30min) — 补全 Mistral 对比表\\\\n\\\\n## 后续\\\\n- [ ] Paper Agent 整合 Mistral cross-arch + C1 retrain 数据\\\\n- [ ] Mistral KL HellaSwag/PIQA 到齐后补表\\\\n- [ ] Round 11 review (continue mode)\\\\n- [ ] 最终 ARR 提交\\\\n\\\\n## GPU 预算\\\\n本项目分配: westd-34887 (cuda:0,1) + westd-41718 (cuda:0,1) = 4 GPU\\\\n状态: 34887:0 Mistral KL HS/PIQA, 其余空闲\\\\n\\\\n## DDL\\\\nEMNLP 2026 ARR May cycle: **2026-05-25** (6 天)\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D079 | 2026-05-19 | 放弃 wall-clock speedup claim，论文定位为 prediction quali | flashinfer_benchmark_34887 |\\\\n| D078 | 2026-05-19 | 投入 flashinfer sparse kernel 开发（3h 硬上限），现有 mask-and | benchmark_latency |\\\\n| D077 | 2026-05-19 | TEAL assertion tolerance 0.02→0.05 + 重提 v3/teal275 | qwen14b_kl30_s42_eval_uniform_v3, qwen14b_teal275_uniform_eval_v2 |\\\\n| D076 | 2026-05-19 | D074 superseded: Layer 1-4 零稀疏性是 eval pipeline bug | qwen14b_kl30_s42_eval_uniform_v2 |\\\\n| D075 | 2026-05-19 | 确认 eval pipeline bug（mag*hard_mask 退化），修复代码并重跑全部 Q | qwen14b_kl30_s42_eval_uniform_v2, qwen14b_kl30_s123_eval_v4, qwen14b_kl30_s456_eval_v2, qwen14b_teal275_uniform_eval |\\\\n| D074 | 2026-05-19 | Qwen-14B Layer 1-4 零稀疏性确认为 predictor 行为，补跑 TEAL@27 | qwen14b_kl30_s42_eval_uniform_v2, qwen14b_kl30_s123_eval_v4, qwen14b_kl30_s456_eval_v2, qwen14b_teal_27.5pct_uniform |\\\\n| D073 | 2026-05-19 | Round 12 Action Matrix: Fix N1/N2 data errors, del | bce_gumbel_no_penalty_s42, bce_comp_staged_s42, qwen14b_kl30_s123, qwen14b_kl30_s456 |\\\\n| D072 | 2026-05-19 | Round 11 Action Matrix: C1 reframe (mask transfera | qwen14b_mask_divergence_analysis, teal_28.5pct_sanity, bce_gumbel_no_penalty_s42 |\\\\n| D071 | 2026-05-19 | Mistral TEAL baseline 确认 KL cross-arch downstream  | mistral_teal30_downstream, mistral_teal50_downstream, eval_c1_retrain_30pct_s123, eval_c1_retrain_30pct_s456 |\\\\n| D070 | 2026-05-19 | Accept 冲刺计划修正：砍 LLaMA-3-8B（同一家族）和 sparse kernel（高风 | mistral_kl30_downstream |\\\\n\\\\n\\\", \\\"lines\\\": 58}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ROADMAP.md\", \"content\": \"# distill_sparse_swiglu — Research Dashboard\\n\\n> 最后更新: 2026-05-19 05:07 UTC | 更新原因: D071 Mistral cross-arch downstream 确认 KL 优势，进入最终整合阶段\\n\\n> 最后更新: 2026-05-19 05:10 UTC | 更新原因: D071 Mistral cross-arch 确认\\n\\n## 核心方向\\nKL distillation discovers fundamentally different neuron importance patterns for SwiGLU sparsity prediction (LLaMA-3.1-8B). C1 causal ablation provides evidence target quality drives KL advantage. Cross-arch (Mistral) downstream confirms KL > TEAL. 详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: 最终数据整合 → Round 11 review → ARR 提交\\n- **架构**: LLaMA-3.1-8B (主) + Mistral-7B (cross-arch, downstream confirmed) + Qwen-14B (cross-scale)\\n- **D071**: Mistral TEAL baseline 确认 KL downstream 优势 (ARC +9pp, WG +5.6pp)\\n- **C1 retrain**: max Δ=1.70pp with consistent checkpoints ✅\\n- **Paper P1-P9 text patches**: ✅\\n- **Paper consistency**: 0 critical / 0 warning ✅\\n\\n## 实验状态\\n\\n### 全部完成\\n- ✅ Mistral TEAL 30%: ARC=41.1%, WG=63.5%, MMLU=43.5% → KL wins (ARC +9, WG +5.6)\\n- ✅ Mistral TEAL 50%: MMLU=26.4%≈random → capacity cliff cross-arch\\n- ✅ C1 retrain s123/s456: max Δ=1.70pp, consistent with main table\\n- ✅ BCE 50% unified: PPL=27.97, MMLU=26.1%≈random\\n- ✅ C1@30% 3-seed: all Δ ≤ 1.70pp\\n\\n### 进行中\\n- 🔄 Mistral KL 30% HellaSwag/PIQA (~30min) — 补全 Mistral 对比表\\n\\n## 后续\\n- [ ] Paper Agent 整合 Mistral cross-arch + C1 retrain 数据\\n- [ ] Mistral KL HellaSwag/PIQA 到齐后补表\\n- [ ] Round 11 review (continue mode)\\n- [ ] 最终 ARR 提交\\n\\n## GPU 预算\\n本项目分配: westd-34887 (cuda:0,1) + westd-41718 (cuda:0,1) = 4 GPU\\n状态: 34887:0 Mistral KL HS/PIQA, 其余空闲\\n\\n## DDL\\nEMNLP 2026 ARR May cycle: **2026-05-25** (6 天)\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D079 | 2026-05-19 | 放弃 wall-clock speedup claim，论文定位为 prediction quali | flashinfer_benchmark_34887 |\\n| D078 | 2026-05-19 | 投入 flashinfer sparse kernel 开发（3h 硬上限），现有 mask-and | benchmark_latency |\\n| D077 | 2026-05-19 | TEAL assertion tolerance 0.02→0.05 + 重提 v3/teal275 | qwen14b_kl30_s42_eval_uniform_v3, qwen14b_teal275_uniform_eval_v2 |\\n| D076 | 2026-05-19 | D074 superseded: Layer 1-4 零稀疏性是 eval pipeline bug | qwen14b_kl30_s42_eval_uniform_v2 |\\n| D075 | 2026-05-19 | 确认 eval pipeline bug（mag*hard_mask 退化），修复代码并重跑全部 Q | qwen14b_kl30_s42_eval_uniform_v2, qwen14b_kl30_s123_eval_v4, qwen14b_kl30_s456_eval_v2, qwen14b_teal275_uniform_eval |\\n| D074 | 2026-05-19 | Qwen-14B Layer 1-4 零稀疏性确认为 predictor 行为，补跑 TEAL@27 | qwen14b_kl30_s42_eval_uniform_v2, qwen14b_kl30_s123_eval_v4, qwen14b_kl30_s456_eval_v2, qwen14b_teal_27.5pct_uniform |\\n| D073 | 2026-05-19 | Round 12 Action Matrix: Fix N1/N2 data errors, del | bce_gumbel_no_penalty_s42, bce_comp_staged_s42, qwen14b_kl30_s123, qwen14b_kl30_s456 |\\n| D072 | 2026-05-19 | Round 11 Action Matrix: C1 reframe (mask transfera | qwen14b_mask_divergence_analysis, teal_28.5pct_sanity, bce_gumbel_no_penalty_s42 |\\n| D071 | 2026-05-19 | Mistral TEAL baseline 确认 KL cross-arch downstream  | mistral_teal30_downstream, mistral_teal50_downstream, eval_c1_retrain_30pct_s123, eval_c1_retrain_30pct_s456 |\\n| D070 | 2026-05-19 | Accept 冲刺计划修正：砍 LLaMA-3-8B（同一家族）和 sparse kernel（高风 | mistral_kl30_downstream |\\n\\n\", \"lines\": 58}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "1db9227d-c4cb-4ae9-a392-887b20f58ca0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-19T18:18:41.221Z_

<details><summary>Logged reasoning block</summary>

```text
Let me understand the situation:

1. **Experiment `qwen14b_dense_4task_v2`** has completed (ANALYZING state) - this is a retry of `qwen14b_dense_4task` which failed earlier.
2. **Running experiments**: qwen14b_teal275_uniform_eval_v3, qwen14b_teal275_hspiqa, qwen14b_kl30_s42_gsm8k_v2
3. **ROADMAP**: We're in the final data consolidation phase, 6 days to EMNLP 2026 ARR deadline (May 25)


4. **Context**: This is about completing the Qwen-14B dense baseline for 4 tasks (wikitext2, arc_challenge, winogrande, mmlu)

Now I need to pull the specific experiment details from the registry, spawn a worker to analyze the results by reading logs and fetching metrics from W&B, then update the registry with the findings and report.md before briefing the Director.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34612c5e-a88e-434c-8fc2-57fa7fb235a6",
  "isSidechain": false,
  "requestId": "req_011CbCPT8PKQQYQi32oPbQci",
  "type": "assistant",
  "uuid": "58bdd4dc-20aa-40e8-8ee6-ded129b85ecd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APenxzHe2vYeCwKWhjrFwx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5193,
      "cache_read_input_tokens": 38963,
      "output_tokens": 1044,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5193,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1044,
          "cache_read_input_tokens": 38963,
          "cache_creation_input_tokens": 5193,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5193
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

### Assistant

_source line 23 · 2026-05-19T18:18:41.329Z_

Cron 同步完成：3 个实验仍在运行（teal275_uniform_eval_v3, teal275_hspiqa, kl30_s42_gsm8k_v2）。现在处理 `qwen14b_dense_4task_v2` 完成回调。

先提取该实验的 registry 详情。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58bdd4dc-20aa-40e8-8ee6-ded129b85ecd",
  "isSidechain": false,
  "requestId": "req_011CbCPT8PKQQYQi32oPbQci",
  "type": "assistant",
  "uuid": "beaa58ee-0f57-494d-9d33-8e804796ed05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APenxzHe2vYeCwKWhjrFwx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5193,
      "cache_read_input_tokens": 38963,
      "output_tokens": 1044,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5193,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1044,
          "cache_read_input_tokens": 38963,
          "cache_creation_input_tokens": 5193,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5193
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

### Tool call

_source line 24 · 2026-05-19T18:18:46.058Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FvGXGKFU8grc2cv1DfjRjL`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-agent-97ac3267/f10c8440-160d-45f2-b3c9-6c60a26f3fd0/tool-results/mcp-agent-ml-research-read_registry-1779214705209.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nregistry = json.loads(data['result'])\nexps = registry['data']['experiments']\n# Find qwen14b_dense_4task_v2\nfor e in exps:\n    if e.get('exp_id') == 'qwen14b_dense_4task_v2':\n        print(json.dumps(e, indent=2))\n        break\n\"",
  "description": "Extract qwen14b_dense_4task_v2 experiment details from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "beaa58ee-0f57-494d-9d33-8e804796ed05",
  "isSidechain": false,
  "requestId": "req_011CbCPT8PKQQYQi32oPbQci",
  "type": "assistant",
  "uuid": "a74aeb4f-c77e-4d25-8136-4511c0f4e40e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APenxzHe2vYeCwKWhjrFwx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5193,
      "cache_read_input_tokens": 38963,
      "output_tokens": 1044,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5193,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1044,
          "cache_read_input_tokens": 38963,
          "cache_creation_input_tokens": 5193,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5193
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

_source line 25 · 2026-05-19T18:18:46.391Z_

<details><summary>↩ Tool result · reported error · `toolu_01FvGXGKFU8grc2cv1DfjRjL`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 8, in &lt;module>
    if e.get('exp_id') == 'qwen14b_dense_4task_v2':
       ^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a74aeb4f-c77e-4d25-8136-4511c0f4e40e",
  "isSidechain": false,
  "promptId": "4685578a-62f4-4e3c-9ae6-7efcd8955d99",
  "type": "user",
  "uuid": "1585111f-9ff5-4af4-998c-fc2f6cee4276",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 8, in &lt;module>\n    if e.get('exp_id') == 'qwen14b_dense_4task_v2':\n       ^^^^^\nAttributeError: 'str' object has no attribute 'get'",
  "sourceToolAssistantUUID": "a74aeb4f-c77e-4d25-8136-4511c0f4e40e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T18:18:49.050Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014MigPGgUu1GjDc6P6z6hUK`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-agent-97ac3267/f10c8440-160d-45f2-b3c9-6c60a26f3fd0/tool-results/mcp-agent-ml-research-read_registry-1779214705209.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nregistry = json.loads(data['result'])\nexps = registry['data']['experiments']\n# Also get qwen14b_dense_baseline and qwen14b_dense_hspiqa for comparison\nfor e in exps:\n    if e.get('exp_id') in ['qwen14b_dense_baseline', 'qwen14b_dense_hspiqa', 'qwen14b_dense_4task']:\n        print(f'=== {e[\\\"exp_id\\\"]} ===')\n        print(json.dumps({k: e[k] for k in ['exp_id','status','conclusion','hypothesis','metrics','parent'] if k in e}, indent=2))\n        print()\n\"",
  "description": "Get related dense baseline experiments for comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1585111f-9ff5-4af4-998c-fc2f6cee4276",
  "isSidechain": false,
  "requestId": "req_011CbCPT8PKQQYQi32oPbQci",
  "type": "assistant",
  "uuid": "232cf7e4-241b-41b1-b9fe-4ec008f7c012",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APenxzHe2vYeCwKWhjrFwx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5193,
      "cache_read_input_tokens": 38963,
      "output_tokens": 1044,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5193,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1044,
          "cache_read_input_tokens": 38963,
          "cache_creation_input_tokens": 5193,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5193
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

_source line 27 · 2026-05-19T18:18:49.052Z_

<details><summary>↩ Tool result · reported error · `toolu_014MigPGgUu1GjDc6P6z6hUK`</summary>

```text
&lt;tool_use_error>Cancelled: parallel tool call Bash(cat /home/ubuntu/.claude-account-3/proje…) errored&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "232cf7e4-241b-41b1-b9fe-4ec008f7c012",
  "isSidechain": false,
  "promptId": "4685578a-62f4-4e3c-9ae6-7efcd8955d99",
  "type": "user",
  "uuid": "8593d6d0-0201-49cc-8162-5d9ed94bed63",
  "toolUseResult": "Cancelled: parallel tool call Bash(cat /home/ubuntu/.claude-account-3/proje…) errored",
  "sourceToolAssistantUUID": "232cf7e4-241b-41b1-b9fe-4ec008f7c012",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。 详情: Process exited cleanly, W&B data available  - exp_id: qwen14b_dense_4task_v2 - project: distill_sparse_swiglu - server: westd-41718 - log_path: ~…",
  "leafUuid": "8593d6d0-0201-49cc-8162-5d9ed94bed63",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze experiment results and transition to done",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0"
}
```

---

### Tool call

_source line 30 · 2026-05-19T18:18:57.941Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Gfizunxz3eqLLugSdTCjuT`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-agent-97ac3267/f10c8440-160d-45f2-b3c9-6c60a26f3fd0/tool-results/mcp-agent-ml-research-read_registry-1779214705209.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult_str = data['result']\nregistry = json.loads(result_str)\nprint(type(registry))\nif isinstance(registry, dict):\n    print(list(registry.keys())[:5])\n    d = registry.get('data', registry)\n    if isinstance(d, dict):\n        print(list(d.keys())[:5])\n        exps = d.get('experiments', [])\n        print(f'experiments type: {type(exps)}, len: {len(exps) if isinstance(exps, list) else \\\"N/A\\\"}')\n        if isinstance(exps, list) and len(exps) > 0:\n            print(f'first item type: {type(exps[0])}')\n            if isinstance(exps[0], dict):\n                print(exps[0].get('exp_id'))\n            else:\n                print(repr(exps[0])[:200])\n\" 2>&1 | head -20",
  "description": "Debug registry JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8593d6d0-0201-49cc-8162-5d9ed94bed63",
  "isSidechain": false,
  "requestId": "req_011CbCPUS8h2111v2iCtYBej",
  "type": "assistant",
  "uuid": "d73c0b66-e3f2-491a-bda8-307ea4e10b17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWGx5XQ5JVa32XcSWCrKsP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1221,
      "cache_read_input_tokens": 44156,
      "output_tokens": 432,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1221,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 432,
          "cache_read_input_tokens": 44156,
          "cache_creation_input_tokens": 1221,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1221
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

_source line 31 · 2026-05-19T18:18:58.067Z_

<details><summary>↩ Tool result · `toolu_01Gfizunxz3eqLLugSdTCjuT`</summary>

```text
&lt;class 'dict'>
['success', 'data', 'error', 'metadata']
['experiments', 'count', 'total', 'baseline']
experiments type: &lt;class 'dict'>, len: N/A
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d73c0b66-e3f2-491a-bda8-307ea4e10b17",
  "isSidechain": false,
  "promptId": "4685578a-62f4-4e3c-9ae6-7efcd8955d99",
  "type": "user",
  "uuid": "e8a7d519-5ccc-4b0a-ba0e-c546cf911177",
  "toolUseResult": {
    "stdout": "&lt;class 'dict'>\n['success', 'data', 'error', 'metadata']\n['experiments', 'count', 'total', 'baseline']\nexperiments type: &lt;class 'dict'>, len: N/A",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d73c0b66-e3f2-491a-bda8-307ea4e10b17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-19T18:18:58.073Z_

```json
{
  "parentUuid": "e8a7d519-5ccc-4b0a-ba0e-c546cf911177",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "fa2f9134-a92c-4f85-b72d-b0ee2fc3b4d3",
  "timestamp": "2026-05-19T18:18:58.073Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 33 · 2026-05-19T18:19:03.481Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EwpUvxNrkTzSVHwf5EQeoF`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-agent-97ac3267/f10c8440-160d-45f2-b3c9-6c60a26f3fd0/tool-results/mcp-agent-ml-research-read_registry-1779214705209.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nregistry = json.loads(data['result'])\nexps = registry['data']['experiments']\n# It's a dict keyed by exp_id\ntarget_ids = ['qwen14b_dense_4task_v2', 'qwen14b_dense_baseline', 'qwen14b_dense_hspiqa', 'qwen14b_dense_4task']\nfor eid in target_ids:\n    if eid in exps:\n        print(f'=== {eid} ===')\n        print(json.dumps(exps[eid], indent=2))\n        print()\n    else:\n        print(f'{eid}: NOT FOUND')\n        print()\n\" 2>&1",
  "description": "Extract target experiments from registry dict"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa2f9134-a92c-4f85-b72d-b0ee2fc3b4d3",
  "isSidechain": false,
  "requestId": "req_011CbCPV6YVo7bAMQ5Q8V7L9",
  "type": "assistant",
  "uuid": "e3eb2b6a-1b71-4b0d-a1ba-14067f6249ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H1ks6GxkaAaSiND3oN2bJk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 600,
      "cache_read_input_tokens": 45377,
      "output_tokens": 373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 600,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 373,
          "cache_read_input_tokens": 45377,
          "cache_creation_input_tokens": 600,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 600
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

_source line 34 · 2026-05-19T18:19:03.570Z_

<details><summary>↩ Tool result · `toolu_01EwpUvxNrkTzSVHwf5EQeoF`</summary>

```text
=== qwen14b_dense_4task_v2 ===
{
  "status": "ANALYZING",
  "retry_count": 0,
  "created_at": "2026-05-19T17:48:38.383Z",
  "updated_at": "2026-05-19T18:18:05.933Z",
  "hypothesis": "Qwen-14B dense baseline remaining 4 tasks (wikitext2, arc_challenge, winogrande, mmlu). Retry of qwen14b_dense_4task which OOMed due to GSM8K orphan process. Orphan now killed.",
  "parent": "qwen14b_dense_baseline",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u src/benchmark_eval.py --exp_id qwen14b_dense_4task_v2 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --dense --tasks wikitext2,arc_challenge,winogrande,mmlu --seq_len 2048 --gpu 0\"",
    "server": "westd-41718",
    "gpu": [
      "cuda:1"
    ],
    "pid": "164330",
    "log_path": "~/runs/distill_sparse_swiglu/qwen14b_dense_4task_v2.log",
    "submitted_at": "2026-05-19T17:49:35.043Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root"
  },
  "server": "westd-41718",
  "gpu": "cuda:1",
  "pid": "164330",
  "log_path": "~/runs/distill_sparse_swiglu/qwen14b_dense_4task_v2.log",
  "reproduce": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u src/benchmark_eval.py --exp_id qwen14b_dense_4task_v2 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --dense --tasks wikitext2,arc_challenge,winogrande,mmlu --seq_len 2048 --gpu 0\"",
    "finished_at": "2026-05-19T18:18:04.940Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-19T18:18:10.535756+00:00"
      }
    ]
  }
}

=== qwen14b_dense_baseline ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-17T18:47:04.949Z",
  "updated_at": "2026-05-17T22:26:12.490Z",
  "spec": {
    "command": "cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_dense_baseline --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0",
    "server": "westd-41718",
    "gpu": [
      "cuda:0"
    ],
    "pid": "18845",
    "log_path": "~/runs/distill_sparse_swiglu/qwen14b_dense_baseline.log",
    "submitted_at": "2026-05-17T18:47:34.739Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "model_name": "qwen2.5-14b",
    "data_path": "lm-eval-harness datasets",
    "data_count": 0,
    "seed": 42,
    "wall_clock_seconds": 13034.6,
    "gpu_hours": 3.62
  },
  "hypothesis": "Qwen-2.5-14B dense baseline downstream metrics (PPL, ARC-c, WinoGrande, MMLU, GSM8K) provide reference for computing degradation ratio of KL/BCE/TEAL sparse predictors at 14B scale, enabling cross-scale comparison with LLaMA-8B results",
  "reproduce": {
    "finished_at": "2026-05-17T22:24:15.654Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-17T22:24:20.978994+00:00"
      }
    ]
  },
  "log_path": "logs/downstream_dense_baseline.log",
  "checkpoint_path": "N/A (dense baseline)",
  "conclusion": "success",
  "metrics": {
    "ppl": 5.1854,
    "arc_challenge": 0.6758,
    "winogrande": 0.8106,
    "mmlu": 0.7977,
    "gsm8k": 0.8757
  },
  "completed_at": "2026-05-17T22:24:49.323Z"
}

=== qwen14b_dense_hspiqa ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-19T17:15:01.916Z",
  "updated_at": "2026-05-19T18:14:50.005Z",
  "hypothesis": "Qwen-14B dense baseline hellaswag+piqa supplement. Completing 6-task suite for 14B comparison table.",
  "parent": "qwen14b_dense_baseline",
  "spec": {
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u src/benchmark_eval.py --exp_id qwen14b_dense_hspiqa --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --dense --tasks hellaswag,piqa --seq_len 2048 --gpu 0",
    "server": "westd-41718",
    "gpu": 0,
    "pid": 162200,
    "model_name": "qwen2.5-14b",
    "data_path": "hellaswag,piqa (lm_eval builtin)",
    "data_count": null,
    "seed": null,
    "eval_data": "hellaswag,piqa",
    "checkpoint_source": "dense (no checkpoint)"
  },
  "log_path": "/root/distill_sparse_swiglu/logs/qwen14b_dense_hspiqa.log",
  "checkpoint_path": "N/A",
  "conclusion": "success",
  "completed_at": "2026-05-19T18:14:44.020Z",
  "metrics": {
    "hellaswag_acc": 0.6444,
    "hellaswag_acc_norm": 0.8421,
    "piqa_acc": 0.809,
    "piqa_acc_norm": 0.8194
  }
}

=== qwen14b_dense_4task ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-19T17:42:50.508Z",
  "updated_at": "2026-05-19T17:50:33.183Z",
  "hypothesis": "Qwen-14B dense baseline remaining 4 tasks (wikitext2, arc_challenge, winogrande, mmlu). Parallel with qwen14b_dense_hspiqa (HS+PIQA) on cuda:0 to complete full 6-task dense baseline for 14B comparison table.",
  "parent": "qwen14b_dense_baseline",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u src/benchmark_eval.py --exp_id qwen14b_dense_4task --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --dense --tasks wikitext2,arc_challenge,winogrande,mmlu --seq_len 2048 --gpu 0\"",
    "server": "westd-41718",
    "gpu": [
      "cuda:1"
    ],
    "pid": "163891",
    "log_path": "~/runs/distill_sparse_swiglu/qwen14b_dense_4task.log",
    "submitted_at": "2026-05-19T17:44:42.250Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 162.1,
    "gpu_hours": 0.05
  },
  "server": "westd-41718",
  "gpu": "cuda:1",
  "pid": "163891",
  "log_path": "~/runs/distill_sparse_swiglu/qwen14b_dense_4task.log",
  "reproduce": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u src/benchmark_eval.py --exp_id qwen14b_dense_4task --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --dense --tasks wikitext2,arc_challenge,winogrande,mmlu --seq_len 2048 --gpu 0\"",
    "finished_at": "2026-05-19T17:47:20.778Z"
  },
  "failure_reason": "CUDA OOM: CUDA out of memory. Tried to allocate 2.90 GiB. GPU 0 has a total capacity of 94.97 GiB of which 1.77 GiB is free. Process 163225 has 61.77 GiB memory in use. Including non-PyTorch memory, this process has 31.41 GiB memory in use. Of the allocated me",
  "conclusion": "failed",
  "completed_at": "2026-05-19T17:47:24.338Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-19T17:47:32.378208+00:00"
      }
    ]
  },
  "notes": "\u5931\u8d25\u539f\u56e0: CUDA OOM at MMLU loglikelihood stage. Process 163225 (orphaned child of killed gsm8k experiment PID 163224) held 61.77 GiB on cuda:1, leaving only 1.77 GiB free. lm_head forward pass needed 2.90 GiB allocation. | \u5df2\u6709\u6210\u679c: arc_challenge eval completed (~33%), wikitext2 completed. | \u540e\u7eed: v2 \u5df2\u81ea\u52a8\u91cd\u65b0\u63d0\u4ea4 (PID 164330, westd-41718:cuda:1), orphan \u5df2\u6e05\u7406\u3002"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3eb2b6a-1b71-4b0d-a1ba-14067f6249ee",
  "isSidechain": false,
  "promptId": "4685578a-62f4-4e3c-9ae6-7efcd8955d99",
  "type": "user",
  "uuid": "9c4cbdd6-5b3a-42d3-976c-7e81832c50c6",
  "toolUseResult": {
    "stdout": "=== qwen14b_dense_4task_v2 ===\n{\n  \"status\": \"ANALYZING\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-19T17:48:38.383Z\",\n  \"updated_at\": \"2026-05-19T18:18:05.933Z\",\n  \"hypothesis\": \"Qwen-14B dense baseline remaining 4 tasks (wikitext2, arc_challenge, winogrande, mmlu). Retry of qwen14b_dense_4task which OOMed due to GSM8K orphan process. Orphan now killed.\",\n  \"parent\": \"qwen14b_dense_baseline\",\n  \"spec\": {\n    \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u src/benchmark_eval.py --exp_id qwen14b_dense_4task_v2 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --dense --tasks wikitext2,arc_challenge,winogrande,mmlu --seq_len 2048 --gpu 0\\\"\",\n    \"server\": \"westd-41718\",\n    \"gpu\": [\n      \"cuda:1\"\n    ],\n    \"pid\": \"164330\",\n    \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_dense_4task_v2.log\",\n    \"submitted_at\": \"2026-05-19T17:49:35.043Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\"\n  },\n  \"server\": \"westd-41718\",\n  \"gpu\": \"cuda:1\",\n  \"pid\": \"164330\",\n  \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_dense_4task_v2.log\",\n  \"reproduce\": {\n    \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u src/benchmark_eval.py --exp_id qwen14b_dense_4task_v2 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --dense --tasks wikitext2,arc_challenge,winogrande,mmlu --seq_len 2048 --gpu 0\\\"\",\n    \"finished_at\": \"2026-05-19T18:18:04.940Z\"\n  },\n  \"extra\": {\n    \"hook_events\": [\n      {\n        \"event\": \"on_complete\",\n        \"action\": \"agent\",\n        \"ts\": \"2026-05-19T18:18:10.535756+00:00\"\n      }\n    ]\n  }\n}\n\n=== qwen14b_dense_baseline ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-17T18:47:04.949Z\",\n  \"updated_at\": \"2026-05-17T22:26:12.490Z\",\n  \"spec\": {\n    \"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_dense_baseline --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\",\n    \"server\": \"westd-41718\",\n    \"gpu\": [\n      \"cuda:0\"\n    ],\n    \"pid\": \"18845\",\n    \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_dense_baseline.log\",\n    \"submitted_at\": \"2026-05-17T18:47:34.739Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"model_name\": \"qwen2.5-14b\",\n    \"data_path\": \"lm-eval-harness datasets\",\n    \"data_count\": 0,\n    \"seed\": 42,\n    \"wall_clock_seconds\": 13034.6,\n    \"gpu_hours\": 3.62\n  },\n  \"hypothesis\": \"Qwen-2.5-14B dense baseline downstream metrics (PPL, ARC-c, WinoGrande, MMLU, GSM8K) provide reference for computing degradation ratio of KL/BCE/TEAL sparse predictors at 14B scale, enabling cross-scale comparison with LLaMA-8B results\",\n  \"reproduce\": {\n    \"finished_at\": \"2026-05-17T22:24:15.654Z\"\n  },\n  \"extra\": {\n    \"hook_events\": [\n      {\n        \"event\": \"on_complete\",\n        \"action\": \"agent\",\n        \"ts\": \"2026-05-17T22:24:20.978994+00:00\"\n      }\n    ]\n  },\n  \"log_path\": \"logs/downstream_dense_baseline.log\",\n  \"checkpoint_path\": \"N/A (dense baseline)\",\n  \"conclusion\": \"success\",\n  \"metrics\": {\n    \"ppl\": 5.1854,\n    \"arc_challenge\": 0.6758,\n    \"winogrande\": 0.8106,\n    \"mmlu\": 0.7977,\n    \"gsm8k\": 0.8757\n  },\n  \"completed_at\": \"2026-05-17T22:24:49.323Z\"\n}\n\n=== qwen14b_dense_hspiqa ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-19T17:15:01.916Z\",\n  \"updated_at\": \"2026-05-19T18:14:50.005Z\",\n  \"hypothesis\": \"Qwen-14B dense baseline hellaswag+piqa supplement. Completing 6-task suite for 14B comparison table.\",\n  \"parent\": \"qwen14b_dense_baseline\",\n  \"spec\": {\n    \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u src/benchmark_eval.py --exp_id qwen14b_dense_hspiqa --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --dense --tasks hellaswag,piqa --seq_len 2048 --gpu 0\",\n    \"server\": \"westd-41718\",\n    \"gpu\": 0,\n    \"pid\": 162200,\n    \"model_name\": \"qwen2.5-14b\",\n    \"data_path\": \"hellaswag,piqa (lm_eval builtin)\",\n    \"data_count\": null,\n    \"seed\": null,\n    \"eval_data\": \"hellaswag,piqa\",\n    \"checkpoint_source\": \"dense (no checkpoint)\"\n  },\n  \"log_path\": \"/root/distill_sparse_swiglu/logs/qwen14b_dense_hspiqa.log\",\n  \"checkpoint_path\": \"N/A\",\n  \"conclusion\": \"success\",\n  \"completed_at\": \"2026-05-19T18:14:44.020Z\",\n  \"metrics\": {\n    \"hellaswag_acc\": 0.6444,\n    \"hellaswag_acc_norm\": 0.8421,\n    \"piqa_acc\": 0.809,\n    \"piqa_acc_norm\": 0.8194\n  }\n}\n\n=== qwen14b_dense_4task ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-19T17:42:50.508Z\",\n  \"updated_at\": \"2026-05-19T17:50:33.183Z\",\n  \"hypothesis\": \"Qwen-14B dense baseline remaining 4 tasks (wikitext2, arc_challenge, winogrande, mmlu). Parallel with qwen14b_dense_hspiqa (HS+PIQA) on cuda:0 to complete full 6-task dense baseline for 14B comparison table.\",\n  \"parent\": \"qwen14b_dense_baseline\",\n  \"spec\": {\n    \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u src/benchmark_eval.py --exp_id qwen14b_dense_4task --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --dense --tasks wikitext2,arc_challenge,winogrande,mmlu --seq_len 2048 --gpu 0\\\"\",\n    \"server\": \"westd-41718\",\n    \"gpu\": [\n      \"cuda:1\"\n    ],\n    \"pid\": \"163891\",\n    \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_dense_4task.log\",\n    \"submitted_at\": \"2026-05-19T17:44:42.250Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"wall_clock_seconds\": 162.1,\n    \"gpu_hours\": 0.05\n  },\n  \"server\": \"westd-41718\",\n  \"gpu\": \"cuda:1\",\n  \"pid\": \"163891\",\n  \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_dense_4task.log\",\n  \"reproduce\": {\n    \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u src/benchmark_eval.py --exp_id qwen14b_dense_4task --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --dense --tasks wikitext2,arc_challenge,winogrande,mmlu --seq_len 2048 --gpu 0\\\"\",\n    \"finished_at\": \"2026-05-19T17:47:20.778Z\"\n  },\n  \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 2.90 GiB. GPU 0 has a total capacity of 94.97 GiB of which 1.77 GiB is free. Process 163225 has 61.77 GiB memory in use. Including non-PyTorch memory, this process has 31.41 GiB memory in use. Of the allocated me\",\n  \"conclusion\": \"failed\",\n  \"completed_at\": \"2026-05-19T17:47:24.338Z\",\n  \"extra\": {\n    \"hook_events\": [\n      {\n        \"event\": \"on_failed\",\n        \"action\": \"agent\",\n        \"ts\": \"2026-05-19T17:47:32.378208+00:00\"\n      }\n    ]\n  },\n  \"notes\": \"\\u5931\\u8d25\\u539f\\u56e0: CUDA OOM at MMLU loglikelihood stage. Process 163225 (orphaned child of killed gsm8k experiment PID 163224) held 61.77 GiB on cuda:1, leaving only 1.77 GiB free. lm_head forward pass needed 2.90 GiB allocation. | \\u5df2\\u6709\\u6210\\u679c: arc_challenge eval completed (~33%), wikitext2 completed. | \\u540e\\u7eed: v2 \\u5df2\\u81ea\\u52a8\\u91cd\\u65b0\\u63d0\\u4ea4 (PID 164330, westd-41718:cuda:1), orphan \\u5df2\\u6e05\\u7406\\u3002\"\n}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "e3eb2b6a-1b71-4b0d-a1ba-14067f6249ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-19T18:19:17.501Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture:

1. **qwen14b_dense_4task_v2** is in ANALYZING state - it's a retry of qwen14b_dense_4task which OOMed due to an orphan process
2. It evaluates Qwen-14B dense baseline on 4 tasks: wikitext2, arc_challenge, winogrande, mmlu
3. **qwen14b_dense_baseline** already has these metrics: ppl=5.1854, arc_challenge=0.6758, winogrande=0.8106, mmlu=0.7977, gsm8k=0.8757


4. **qwen14b_dense_hspiqa** has hellaswag and piqa scores at 0.8421 and 0.8194 respectively

Wait, this is odd - the baseline already has wikitext2, arc, winogrande, and mmlu results, so why is dense_4task_v2 re-running them? Looking back at the hypothesis, it says this is a retry of the original dense_4task that crashed on the GSM8K orphan process, but the description says it's only running those four tasks, not GSM8K.

Actually, I think I see what's happening - the baseline was run with different environment settings and without the explicit seq_len 2048 parameter that v2 uses. Since TEAL and KL evaluations use seq_len 2048, they probably need to re-run the baseline with matching settings for a fair comparison. I should check the logs to confirm what's actually different between these runs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c4cbdd6-5b3a-42d3-976c-7e81832c50c6",
  "isSidechain": false,
  "requestId": "req_011CbCPVWAokJ4kTPFVC7j3Q",
  "type": "assistant",
  "uuid": "ab04b1c5-2c4f-46f9-b083-ef2a618423f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AbUESJfFiWRiuH1Wr1ACJx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3818,
      "cache_read_input_tokens": 45977,
      "output_tokens": 764,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3818,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 764,
          "cache_read_input_tokens": 45977,
          "cache_creation_input_tokens": 3818,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3818
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

### Assistant

_source line 36 · 2026-05-19T18:19:17.833Z_

实验上下文清楚了：`qwen14b_dense_4task_v2` 是 v1（OOM）的重试，评估 Qwen-14B dense baseline 在 wikitext2/arc/wg/mmlu 上的结果。需要派 Worker 读日志提取指标。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab04b1c5-2c4f-46f9-b083-ef2a618423f0",
  "isSidechain": false,
  "requestId": "req_011CbCPVWAokJ4kTPFVC7j3Q",
  "type": "assistant",
  "uuid": "42795cf5-e059-40d5-9694-43410fb9b854",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AbUESJfFiWRiuH1Wr1ACJx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3818,
      "cache_read_input_tokens": 45977,
      "output_tokens": 764,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3818,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 764,
          "cache_read_input_tokens": 45977,
          "cache_creation_input_tokens": 3818,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3818
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

### Tool call

_source line 37 · 2026-05-19T18:19:19.374Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017VrGDv4udcTzh7shand7pB`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__save_project_file",
  "max_results": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42795cf5-e059-40d5-9694-43410fb9b854",
  "isSidechain": false,
  "requestId": "req_011CbCPVWAokJ4kTPFVC7j3Q",
  "type": "assistant",
  "uuid": "4358de59-8fb8-4df3-85b9-1c0008593afc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AbUESJfFiWRiuH1Wr1ACJx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3818,
      "cache_read_input_tokens": 45977,
      "output_tokens": 764,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3818,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 764,
          "cache_read_input_tokens": 45977,
          "cache_creation_input_tokens": 3818,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3818
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

_source line 38 · 2026-05-19T18:19:19.380Z_

<details><summary>↩ Tool result · `toolu_017VrGDv4udcTzh7shand7pB`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__spawn_worker"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__update_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__main_agent_post_to_director"
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
  "parentUuid": "4358de59-8fb8-4df3-85b9-1c0008593afc",
  "isSidechain": false,
  "promptId": "4685578a-62f4-4e3c-9ae6-7efcd8955d99",
  "type": "user",
  "uuid": "6a085f86-df75-4524-a28b-ef8e156a1474",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 82
  },
  "sourceToolAssistantUUID": "4358de59-8fb8-4df3-85b9-1c0008593afc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。 详情: Process exited cleanly, W&B data available  - exp_id: qwen14b_dense_4task_v2 - project: distill_sparse_swiglu - server: westd-41718 - log_path: ~…",
  "leafUuid": "6a085f86-df75-4524-a28b-ef8e156a1474",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze experiment results and transition to done",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0"
}
```

---

### Assistant

_source line 41 · 2026-05-19T18:19:22.775Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to spawn a Worker to read the log file on westd-41718 and extract metrics from the experiment. Let me also read the resource-saturation skill as required before reporting to Director.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a085f86-df75-4524-a28b-ef8e156a1474",
  "isSidechain": false,
  "requestId": "req_011CbCPWfvibgqHwEo4abpt4",
  "type": "assistant",
  "uuid": "f1a8719c-59e2-4a21-bdac-576edbc55102",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Bw6XvLSnWpk9R8eKk8yZg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2949,
      "cache_read_input_tokens": 49795,
      "output_tokens": 906,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2949,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 906,
          "cache_read_input_tokens": 49795,
          "cache_creation_input_tokens": 2949,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2949
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

### Assistant

_source line 42 · 2026-05-19T18:19:23.504Z_

派 Worker 读取日志并提取指标。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1a8719c-59e2-4a21-bdac-576edbc55102",
  "isSidechain": false,
  "requestId": "req_011CbCPWfvibgqHwEo4abpt4",
  "type": "assistant",
  "uuid": "ea1eec96-2184-4b36-93cb-c7d09884c9cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Bw6XvLSnWpk9R8eKk8yZg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2949,
      "cache_read_input_tokens": 49795,
      "output_tokens": 906,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2949,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 906,
          "cache_read_input_tokens": 49795,
          "cache_creation_input_tokens": 2949,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2949
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

### Tool call

_source line 43 · 2026-05-19T18:19:34.479Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker · `toolu_01Kzz7fLopMGnCV47D1RYYBp`</summary>

```json
{
  "task_type": "analysis:qwen14b_dense_4task_v2",
  "project": "distill_sparse_swiglu",
  "task_prompt": "## 任务\n分析已完成的实验 `qwen14b_dense_4task_v2` 的结果。\n\n## 背景\n这是 Qwen-14B dense baseline 在 4 个 downstream 任务上的评估（wikitext2, arc_challenge, winogrande, mmlu），是 v1（因 OOM 失败）的重试。实验在 westd-41718 上运行，已正常退出。\n\n已有的 dense baseline 参考值（来自 qwen14b_dense_baseline，不同 run）：\n- ppl: 5.1854\n- arc_challenge: 0.6758\n- winogrande: 0.8106\n- mmlu: 0.7977\n\n另有 qwen14b_dense_hspiqa 的结果：\n- hellaswag_acc_norm: 0.8421\n- piqa_acc_norm: 0.8194\n\n## 需要做的事\n\n1. SSH 到 westd-41718，读取日志文件：\n   - `~/runs/distill_sparse_swiglu/qwen14b_dense_4task_v2.log`\n   - 也检查 `/root/distill_sparse_swiglu/logs/` 下是否有对应的 JSON 结果文件\n\n2. 提取所有 4 个任务的指标：\n   - wikitext2 PPL\n   - arc_challenge accuracy (acc 和 acc_norm)\n   - winogrande accuracy (acc)\n   - mmlu accuracy (acc)\n   \n3. 检查是否有任何错误或异常（partial results, warnings 等）\n\n4. 与已有的 qwen14b_dense_baseline 对比（上面的参考值），确认数值是否一致（同一模型 dense eval 应该非常接近）\n\n## 产出\n在回复中列出：\n- 所有提取到的指标（精确数值）\n- 与 baseline 的对比\n- 是否有任何异常\n- 建议 conclusion（success/negative/failed）\n\n## 服务器信息\n- 服务器: westd-41718\n- 环境: conda base（source /root/miniconda3/etc/profile.d/conda.sh && conda activate base）\n- 项目路径: /root/distill_sparse_swiglu\n",
  "tool_groups": [
    "ssh"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea1eec96-2184-4b36-93cb-c7d09884c9cf",
  "isSidechain": false,
  "requestId": "req_011CbCPWfvibgqHwEo4abpt4",
  "type": "assistant",
  "uuid": "7dadc5c9-b66c-4e7a-9156-6158762477ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Bw6XvLSnWpk9R8eKk8yZg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2949,
      "cache_read_input_tokens": 49795,
      "output_tokens": 906,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2949,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 906,
          "cache_read_input_tokens": 49795,
          "cache_creation_input_tokens": 2949,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2949
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

### Tool call

_source line 44 · 2026-05-19T18:19:35.203Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MeG4i6fu46Cb1ZLfuDX3R6`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7dadc5c9-b66c-4e7a-9156-6158762477ac",
  "isSidechain": false,
  "requestId": "req_011CbCPWfvibgqHwEo4abpt4",
  "type": "assistant",
  "uuid": "abb97b36-65f3-42e7-9df7-739a0154782e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Bw6XvLSnWpk9R8eKk8yZg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2949,
      "cache_read_input_tokens": 49795,
      "output_tokens": 906,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2949,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 906,
          "cache_read_input_tokens": 49795,
          "cache_creation_input_tokens": 2949,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2949
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

_source line 45 · 2026-05-19T18:19:37.402Z_

<details><summary>↩ Tool result · `toolu_01Kzz7fLopMGnCV47D1RYYBp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analysis_qwen14b_dense_4task_v2_20260519T181935\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/workers/worker_analysis_qwen14b_dense_4task_v2_20260519T181935.log\", \"setup_data\": {}, \"message\": \"Worker worker_analysis_qwen14b_dense_4task_v2_20260519T181935 started. Use get_worker_status('worker_analysis_qwen14b_dense_4task_v2_20260519T181935') to check progress.\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7dadc5c9-b66c-4e7a-9156-6158762477ac",
  "isSidechain": false,
  "promptId": "4685578a-62f4-4e3c-9ae6-7efcd8955d99",
  "type": "user",
  "uuid": "4e0293db-8fcd-4ac9-98b1-9d66013f45a0",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_analysis_qwen14b_dense_4task_v2_20260519T181935\\\", \\\"status\\\": \\\"running\\\", \\\"log_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/workers/worker_analysis_qwen14b_dense_4task_v2_20260519T181935.log\\\", \\\"setup_data\\\": {}, \\\"message\\\": \\\"Worker worker_analysis_qwen14b_dense_4task_v2_20260519T181935 started. Use get_worker_status('worker_analysis_qwen14b_dense_4task_v2_20260519T181935') to check progress.\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_analysis_qwen14b_dense_4task_v2_20260519T181935\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/workers/worker_analysis_qwen14b_dense_4task_v2_20260519T181935.log\", \"setup_data\": {}, \"message\": \"Worker worker_analysis_qwen14b_dense_4task_v2_20260519T181935 started. Use get_worker_status('worker_analysis_qwen14b_dense_4task_v2_20260519T181935') to check progress.\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "7dadc5c9-b66c-4e7a-9156-6158762477ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T18:19:37.411Z_

<details><summary>↩ Tool result · `toolu_01MeG4i6fu46Cb1ZLfuDX3R6`</summary>

```text
1	---
2	name: resource-saturation
3	description: "当你准备向 Director 汇报前、收到 cron/worker 回调、审批通过准备开跑、怀疑 Worker 池不够饱和时,立即使用本 skill。四部分:A) GPU 分配率(分配了没跑=失职) B) GPU 效率 C) 非 GPU 任务并行(Worker 池<2=失职) D) 汇报必须带 [资源] 行。"
4	always: false
5	roles:
6	  - director
7	  - agent
8	---
9	
10	# 资源饱和度自检（硬约束）
11	
12	## A. GPU 分配率检查
13	
14	调 `get_project_resource_usage(project)` 看:
15	- 已分配给本项目的 GPU 总数和具体卡号
16	- 实际在跑任务的 GPU 数和具体卡号（交叉 registry RUNNING + nvidia-smi 进程）
17	- 分配了但没跑的 GPU 清单 ⚠️
18	
19	任何"分配了但没跑"的 GPU = 失职。必须立即:
20	- 派 Worker 铺 dry-run / 下一批实验代码准备
21	- 铺 ablation（从 experiment-matrix 空白格子里挑）
22	- 确实无实验可铺 → 向 Director 汇报"暂无可铺实验"+ 建议下一步方向(扩 ablation 维度 / 加 baseline / 加 benchmark)。**不要建议归还 GPU**——项目级 GPU 归还只在归档时由 `archive_project` 自动触发, 不是 Director 中途的动作
23	
24	**单实验不占多卡**: 分配 4 卡但实验只用 1 卡 → 另 3 卡必须并行跑其他实验,不能空占。
25	
26	## B. GPU 效率检查
27	
28	调 `get_gpu_health(server)`:
29	- 空闲 GPU（util < 10% 持续 > 5 min）→ 立即铺任务
30	- 低利用率（util < 50% 持续 > 15 min）→ spawn_worker 诊断（batch / IO / 同步）
31	- OOM 风险（显存 > 90% 持续 10 min）→ 主动降 batch / 调优
32	
33	## C. 非 GPU 任务并行
34	
35	GPU 在跑 ≠ 你空闲。以下 CPU / 网络任务**必须**派独立 Worker 并行:
36	- 下一批实验的数据集下载 / 预处理 / fingerprint
37	- 下一批实验的代码准备 / dry-run / 环境配置
38	- 论文文献调研 / related work 检索
39	- 已完成实验的 log 深度分析 / metric 聚合
40	- 论文章节起草
41	- 代码 review / refactor
42	
43	**硬约束**: 任一时刻 Worker 池 < 2 个 = 失职（除非真的全部下游阻塞在等 GPU,这时应当向 Director 申请扩 GPU）。
44	
45	## D. 汇报格式
46	
47	向 Director 汇报时开头必须带资源声明行:
48	
49	    [资源] GPU 分配 N / 实际在跑 M | Worker 池 K (其中 GPU 任务 A / CPU 任务 B)
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "abb97b36-65f3-42e7-9df7-739a0154782e",
  "isSidechain": false,
  "promptId": "4685578a-62f4-4e3c-9ae6-7efcd8955d99",
  "type": "user",
  "uuid": "d70a2a0e-6cef-457c-9260-dddd7b5585df",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md",
      "content": "---\nname: resource-saturation\ndescription: \"当你准备向 Director 汇报前、收到 cron/worker 回调、审批通过准备开跑、怀疑 Worker 池不够饱和时,立即使用本 skill。四部分:A) GPU 分配率(分配了没跑=失职) B) GPU 效率 C) 非 GPU 任务并行(Worker 池<2=失职) D) 汇报必须带 [资源] 行。\"\nalways: false\nroles:\n  - director\n  - agent\n---\n\n# 资源饱和度自检（硬约束）\n\n## A. GPU 分配率检查\n\n调 `get_project_resource_usage(project)` 看:\n- 已分配给本项目的 GPU 总数和具体卡号\n- 实际在跑任务的 GPU 数和具体卡号（交叉 registry RUNNING + nvidia-smi 进程）\n- 分配了但没跑的 GPU 清单 ⚠️\n\n任何\"分配了但没跑\"的 GPU = 失职。必须立即:\n- 派 Worker 铺 dry-run / 下一批实验代码准备\n- 铺 ablation（从 experiment-matrix 空白格子里挑）\n- 确实无实验可铺 → 向 Director 汇报\"暂无可铺实验\"+ 建议下一步方向(扩 ablation 维度 / 加 baseline / 加 benchmark)。**不要建议归还 GPU**——项目级 GPU 归还只在归档时由 `archive_project` 自动触发, 不是 Director 中途的动作\n\n**单实验不占多卡**: 分配 4 卡但实验只用 1 卡 → 另 3 卡必须并行跑其他实验,不能空占。\n\n## B. GPU 效率检查\n\n调 `get_gpu_health(server)`:\n- 空闲 GPU（util < 10% 持续 > 5 min）→ 立即铺任务\n- 低利用率（util < 50% 持续 > 15 min）→ spawn_worker 诊断（batch / IO / 同步）\n- OOM 风险（显存 > 90% 持续 10 min）→ 主动降 batch / 调优\n\n## C. 非 GPU 任务并行\n\nGPU 在跑 ≠ 你空闲。以下 CPU / 网络任务**必须**派独立 Worker 并行:\n- 下一批实验的数据集下载 / 预处理 / fingerprint\n- 下一批实验的代码准备 / dry-run / 环境配置\n- 论文文献调研 / related work 检索\n- 已完成实验的 log 深度分析 / metric 聚合\n- 论文章节起草\n- 代码 review / refactor\n\n**硬约束**: 任一时刻 Worker 池 < 2 个 = 失职（除非真的全部下游阻塞在等 GPU,这时应当向 Director 申请扩 GPU）。\n\n## D. 汇报格式\n\n向 Director 汇报时开头必须带资源声明行:\n\n    [资源] GPU 分配 N / 实际在跑 M | Worker 池 K (其中 GPU 任务 A / CPU 任务 B)\n",
      "numLines": 50,
      "startLine": 1,
      "totalLines": 50
    }
  },
  "sourceToolAssistantUUID": "abb97b36-65f3-42e7-9df7-739a0154782e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-19T18:19:48.008Z_

<details><summary>Logged reasoning block</summary>

```text
Worker 已派出分析实验结果。需要等 Worker 回调。同时我需要检查资源饱和度。

Let me also check GPU resource usage and current worker status to prepare the Director report. Let me check what GPUs are allocated and what's running.

From reconcile_crons I know:
- qwen14b_teal275_uniform_eval_v3: still running (pid=115174)
- qwen14b_teal275_hspiqa: still running (pid=126076)
- qwen14b_kl30_s42_gsm8k_v2: just created


- 
Looking at the GPU allocation from the roadmap, I have 4 GPUs total across two machines (westd-34887 and westd-41718, each with cuda:0,1), and currently only cuda:0 on 34887 is running the Mistral KL HS/PIQA job while the rest are idle. Let me pull the current resource metrics to see what's actually being consumed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d70a2a0e-6cef-457c-9260-dddd7b5585df",
  "isSidechain": false,
  "requestId": "req_011CbCPXzkaGcWryzZroi4xt",
  "type": "assistant",
  "uuid": "dc88ba1c-d5f2-43fc-92ab-cd7675980660",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2ghFcT1oz5DcKVYAYQXf1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2250,
      "cache_read_input_tokens": 52744,
      "output_tokens": 364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2250,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 364,
          "cache_read_input_tokens": 52744,
          "cache_creation_input_tokens": 2250,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2250
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

### Assistant

_source line 48 · 2026-05-19T18:19:48.010Z_

Worker 已派出。同时检查资源状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc88ba1c-d5f2-43fc-92ab-cd7675980660",
  "isSidechain": false,
  "requestId": "req_011CbCPXzkaGcWryzZroi4xt",
  "type": "assistant",
  "uuid": "f9672556-2f79-460f-a544-c0c296db7bc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2ghFcT1oz5DcKVYAYQXf1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2250,
      "cache_read_input_tokens": 52744,
      "output_tokens": 364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2250,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 364,
          "cache_read_input_tokens": 52744,
          "cache_creation_input_tokens": 2250,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2250
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

### Tool call

_source line 49 · 2026-05-19T18:19:48.017Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014g3riBNkWjWu1FdB7p22Ni`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_project_resource_usage,mcp__agent-ml-research__list_workers",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9672556-2f79-460f-a544-c0c296db7bc3",
  "isSidechain": false,
  "requestId": "req_011CbCPXzkaGcWryzZroi4xt",
  "type": "assistant",
  "uuid": "8973be8f-428b-42a5-b0ec-54ef7223087b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2ghFcT1oz5DcKVYAYQXf1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2250,
      "cache_read_input_tokens": 52744,
      "output_tokens": 364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2250,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 364,
          "cache_read_input_tokens": 52744,
          "cache_creation_input_tokens": 2250,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2250
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

_source line 50 · 2026-05-19T18:19:48.024Z_

<details><summary>↩ Tool result · `toolu_014g3riBNkWjWu1FdB7p22Ni`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__get_project_resource_usage"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__list_workers"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8973be8f-428b-42a5-b0ec-54ef7223087b",
  "isSidechain": false,
  "promptId": "4685578a-62f4-4e3c-9ae6-7efcd8955d99",
  "type": "user",
  "uuid": "19c69e4f-dd97-4950-b403-dc323b39cbec",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__list_workers"
    ],
    "query": "select:mcp__agent-ml-research__get_project_resource_usage,mcp__agent-ml-research__list_workers",
    "total_deferred_tools": 82
  },
  "sourceToolAssistantUUID": "8973be8f-428b-42a5-b0ec-54ef7223087b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-19T18:19:52.142Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_project_resource_usage · `toolu_016R2Yp2oAq3dN3dEPZ5g4Eq`</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19c69e4f-dd97-4950-b403-dc323b39cbec",
  "isSidechain": false,
  "requestId": "req_011CbCPYnVAUSn83vWeSZUr6",
  "type": "assistant",
  "uuid": "24f83cc2-24be-4f78-980d-bc4bb59059db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJU9uVCxdGoFxXxZHGZU6A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 54994,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 143,
          "cache_read_input_tokens": 54994,
          "cache_creation_input_tokens": 747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 747
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

### Tool call

_source line 52 · 2026-05-19T18:19:52.291Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers · `toolu_01FQ53YZ2ZZmyBmnit9BPkei`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "status": "running"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24f83cc2-24be-4f78-980d-bc4bb59059db",
  "isSidechain": false,
  "requestId": "req_011CbCPYnVAUSn83vWeSZUr6",
  "type": "assistant",
  "uuid": "486f5c45-82c9-45ac-8aba-a3cf9ecc07a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_97ac3267",
  "sessionId": "f10c8440-160d-45f2-b3c9-6c60a26f3fd0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJU9uVCxdGoFxXxZHGZU6A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 54994,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 143,
          "cache_read_input_tokens": 54994,
          "cache_creation_input_tokens": 747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 747
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
